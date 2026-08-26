"""The single-pass corpus index every check reads.

Deliberately never persisted to disk: building it costs about half a second,
so a cache would buy nothing and could only ever go stale.
"""
import functools
import os

import collections
from dataclasses import dataclass

from . import config as config_module
from . import markdown, paths
from . import slug as slug_module


@dataclass(frozen=True)
class Reference:
    """One edge of the link graph, with enough detail to report it."""

    source: str
    line: int
    col: int
    syntax: str
    raw: str


class DocsIndex:
    """An immutable-by-convention view of ``docs/`` at one point in time."""

    def __init__(self, root=None, config=None):
        self.root = root or paths.repo_root()
        self.config = config if config is not None else config_module.load(root=self.root)
        self.docs = os.path.join(self.root, paths.DOCS)
        self._files = None
        self._toc_files = None
        self._toc_targets = None
        self._in_edges = None

    # ---- filesystem -----------------------------------------------------

    def absolute(self, path):
        return os.path.join(self.root, path)

    @property
    def files(self):
        """Every path under ``docs/``, repository-relative and POSIX."""
        if self._files is None:
            found = set()
            for current, _, names in os.walk(self.docs):
                relative = paths.to_posix(os.path.relpath(current, self.root))
                for name in names:
                    found.add(f"{relative}/{name}")
            self._files = found
        return self._files

    def exists(self, path):
        return os.path.isfile(self.absolute(path))

    def real_name_of(self, path):
        """The on-disk path differing from *path* only in case, if any.

        There are no case-only collisions anywhere under docs/, so when this
        finds something the correction is unambiguous.
        """
        directory, name = os.path.split(path)
        try:
            entries = os.listdir(self.absolute(directory) if directory else self.root)
        except OSError:
            return ""
        lowered = name.lower()
        for entry in entries:
            if entry != name and entry.lower() == lowered:
                return f"{directory}/{entry}" if directory else entry
        return ""

    # ---- classification -------------------------------------------------

    def generated(self, path):
        """Whether *path* is imported output rather than hand-written."""
        return self.config.in_class(path, "generated")

    def exempt_existence(self, target):
        """Whether a link to *target* may point outside this checkout."""
        return self.config.exempt_existence(target)

    def skips(self, path, rule):
        return self.config.skips(path, rule)

    def handwritten(self, path):
        """Whether *path* is a document a person is expected to edit.

        Uses the first matching class rather than plain `generated` membership,
        so a hand-written page that happens to sit under an api/ directory is
        still selected by --all.
        """
        entry = self.config.classify(path)
        return entry is None or entry.id != "generated"

    # ---- documents ------------------------------------------------------

    @functools.lru_cache(maxsize=None)
    def source(self, path):
        """The masked document plus its offset-to-line mapping.

        Memoized because a document with many links to one target would
        otherwise re-read and re-parse that target once per link.
        """
        return markdown.Source(markdown.read(self.absolute(path)))

    @functools.lru_cache(maxsize=None)
    def anchors(self, path):
        """The anchor ids *path* defines, under every enabled slugger.

        Memoized separately from source(): a document linked from many places
        would otherwise re-slug every heading once per inbound link.
        """
        source = self.source(path)
        found = set(source.anchors())
        for match in source.headings():
            found.update(slug_module.variants(match.group(2)).values())
        return frozenset(found)

    @functools.lru_cache(maxsize=None)
    def primary_anchors(self, path):
        """Anchor ids under the primary slugger and explicit markup only."""
        source = self.source(path)
        found = set(source.anchors())
        for match in source.headings():
            found.add(slug_module.slug(match.group(2)))
        return frozenset(found)

    @functools.lru_cache(maxsize=None)
    def duplicate_headings(self, path):
        """Heading slugs that occur more than once.

        Renderers disambiguate repeats differently (-1, -2, or not at all), so
        a fragment aimed at a repeated heading is never reported as missing.
        """
        seen, repeated = set(), set()
        for match in self.source(path).headings():
            value = slug_module.slug(match.group(2))
            if value in seen:
                repeated.add(value)
            seen.add(value)
        return frozenset(repeated)

    # ---- tables of contents ---------------------------------------------

    # ---- reverse link graph ---------------------------------------------

    @property
    def in_edges(self):
        """Map every referenced path to the references pointing at it.

        Keys deliberately include paths that do not exist. That is the whole
        point: after a page is deleted the working tree has no file, but this
        map still lists every document and TOC that links to it, which is what
        --changed-only can never see by looking only at changed files.

        Built on demand, because only the reverse-direction rules need it.
        """
        if self._in_edges is None:
            graph = collections.defaultdict(list)
            for path in sorted(self.files):
                if not path.endswith(".md"):
                    continue
                source = self.source(path)
                for syntax, url, offset in source.all_references():
                    if not url or markdown.is_external(url):
                        continue
                    raw, _ = markdown.split_fragment(url)
                    if not raw:
                        continue
                    line, col = source.position(offset)
                    graph[paths.resolve(path, raw)].append(
                        Reference(path, line, col, syntax, url))
            self._in_edges = graph
        return self._in_edges

    def references_to(self, target):
        """References to *target*, matched case-insensitively.

        Authors on Windows write .PNG where the file is .png; the published
        site is case-sensitive, so both spellings must be found.
        """
        graph = self.in_edges
        found = list(graph.get(target, ()))
        lowered = target.lower()
        for key, edges in graph.items():
            if key != target and key.lower() == lowered:
                found.extend(edges)
        return sorted(found, key=lambda edge: (edge.source, edge.line, edge.col))

    @property
    def toc_files(self):
        if self._toc_files is None:
            self._toc_files = sorted(
                path for path in self.files
                if os.path.basename(path).startswith("toc") and path.endswith(".md"))
        return self._toc_files

    @property
    def toc_targets(self):
        """Every in-repository path any ``toc*.md`` links to."""
        if self._toc_targets is None:
            targets = set()
            for toc in self.toc_files:
                for match in markdown.LINK.finditer(self.source(toc).text):
                    raw, _ = markdown.split_fragment(match.group(1).strip("<> "))
                    if not raw or markdown.is_external(raw):
                        continue
                    targets.add(paths.resolve(toc, raw))
            self._toc_targets = targets
        return self._toc_targets
