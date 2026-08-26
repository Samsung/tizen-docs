"""M-* rules: image and media assets."""
import os

from .. import markdown
from ..findings import ERROR, WARN, Finding

ALT = "M-ALT"
JUNK = "M-JUNK"
ORPHAN = "M-ORPHAN"

#: Assets that are not web media and should not be published from a media/
#: directory. `.pdf` is deliberately absent: the compliance specifications
#: under docs/platform/compliance/media/ are tracked and are legitimate
#: downloads, even though .gitignore excludes *.pdf.
JUNK_SUFFIXES = ("~", ".docx", ".drawio", ".pptx", ".xlsx", ".bak", ".orig")

MEDIA_SUFFIXES = (".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp",
                  ".mp4", ".webm", ".pdf")


def check_alt_text(index, path, source):
    """Every image needs alt text.

    The one accessibility signal that is checkable from Markdown source; the
    rest needs a rendered page.
    """
    for match in markdown.IMAGE.finditer(source.text):
        label = match.group(0)[2:match.group(0).index("]")]
        if label.strip():
            continue
        line, col = source.position(match.start())
        yield Finding(ERROR, ALT, path, "image has no alt text",
                      line=line, col=col, syntax="md-image")


def _media_files(index):
    for path in sorted(index.files):
        directory, name = os.path.split(path)
        if os.path.basename(directory) != "media" and directory != "docs/images":
            continue
        if index.generated(path):
            continue
        yield path, name


def check_junk(index):
    for path, name in _media_files(index):
        if name.endswith(JUNK_SUFFIXES):
            yield Finding(WARN, JUNK, path,
                          "not web media; a media/ directory is published")


def check_orphans(index):
    """Assets nothing references.

    Reported, never gated. New content legitimately arrives as "image added in
    one change, referenced in the next", and the count is only meaningful once
    the link rules are clean: a broken reference makes its own target look
    unreferenced. The runner refuses to answer while any L-* error is open.
    """
    referenced = set()
    for target in index.in_edges:
        referenced.add(target)
        referenced.add(target.lower())
    for path, _ in _media_files(index):
        if path in referenced or path.lower() in referenced:
            continue
        size = os.path.getsize(index.absolute(path))
        yield Finding(WARN, ORPHAN, path,
                      f"not referenced by any document ({size / 1024:.0f} KB)")
