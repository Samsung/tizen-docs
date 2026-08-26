"""The single-pass corpus index every check reads.

Deliberately never persisted to disk: building it costs about half a second,
so a cache would buy nothing and could only ever go stale.
"""
import functools
import os

from . import config as config_module
from . import markdown, paths
from .slug import slug


class DocsIndex:
    """An immutable-by-convention view of ``docs/`` at one point in time."""

    def __init__(self, root=None, config=None):
        self.root = root or paths.repo_root()
        self.config = config if config is not None else config_module.load(root=self.root)
        self.docs = os.path.join(self.root, paths.DOCS)
        self._files = None
        self._toc_files = None
        self._toc_targets = None
        self._edges = None
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
        """The anchor ids *path* defines: heading slugs and explicit anchors.

        Memoized separately from source(): a document linked from many places
        would otherwise re-slug every heading once per inbound link.
        """
        source = self.source(path)
        found = {slug(match.group(2)) for match in source.headings()}
        found.update(source.anchors())
        return frozenset(found)

    # ---- tables of contents ---------------------------------------------

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
