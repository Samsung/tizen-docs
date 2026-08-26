"""The single-pass corpus index every check reads.

Deliberately never persisted to disk: building it costs about half a second,
so a cache would buy nothing and could only ever go stale.
"""
import functools
import os

from . import markdown, paths
from .slug import slug

GENERATED = ("/api/", "/wiki/")


class DocsIndex:
    """An immutable-by-convention view of ``docs/`` at one point in time."""

    def __init__(self, root=None):
        self.root = root or paths.repo_root()
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

    @staticmethod
    def generated(path):
        return any(part in f"/{path}" for part in GENERATED) or path.endswith(".autogen.md")

    # ---- documents ------------------------------------------------------

    def text(self, path):
        return markdown.without_code(markdown.read(self.absolute(path)))

    @functools.lru_cache(maxsize=None)
    def anchors(self, path):
        """The anchor ids *path* defines: heading slugs and explicit anchors.

        Memoized because a document with many links to one target would
        otherwise re-parse that target once per link.
        """
        text = self.text(path)
        found = {slug(match.group(2)) for match in markdown.headings(text)}
        found.update(m.group(1).lower() for m in markdown.NAMED_ANCHOR.finditer(text))
        found.update(m.group(1).lower() for m in markdown.CURLY_ANCHOR.finditer(text))
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
                text = self.text(toc)
                for match in markdown.LINK.finditer(text):
                    raw, _ = markdown.split_fragment(match.group(1).strip("<> "))
                    if not raw or markdown.is_external(raw):
                        continue
                    targets.add(paths.resolve(toc, raw))
            self._toc_targets = targets
        return self._toc_targets
