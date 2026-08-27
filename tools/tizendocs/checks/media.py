"""M-* rules: image and media assets."""
import os
import re

from .. import markdown, paths
from ..findings import ERROR, WARN, Finding

ALT = "M-ALT"
ORPHAN = "M-ORPHAN"

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



#: File types that can reference an asset. Markdown alone is not enough: the
#: generated API reference is HTML with its own CSS and JS, toc.xml is XML, and
#: an asset referenced only from one of those is not an orphan.
REFERRER_SUFFIXES = (".md", ".html", ".htm", ".xml", ".yaml", ".yml",
                     ".js", ".css", ".json", ".txt", ".svg")

REFERENCE = re.compile(
    rb"""(?:src|href|url|poster|data|content)\s*=\s*['"]([^'"]+)['"]"""
    rb"""|\]\(([^)\s]+)""", re.I)


def _referenced_assets(index):
    """Every asset path referenced from any text file under docs/.

    Deliberately not the shared link graph, which is Markdown-only because
    every run builds it. This reads about 59,000 files and belongs in the
    opt-in media scan.
    """
    names = {os.path.basename(path).lower() for path, _ in _media_files(index)}
    found = set()
    for path in index.files:
        if not path.endswith(REFERRER_SUFFIXES):
            continue
        try:
            with open(index.absolute(path), "rb") as handle:
                data = handle.read()
        except OSError:
            continue
        directory = os.path.dirname(path)
        for match in REFERENCE.finditer(data):
            raw = (match.group(1) or match.group(2) or b"")
            raw = raw.split(b"#")[0].split(b"?")[0]
            if not raw:
                continue
            url = raw.decode("utf-8", "ignore")
            if url.startswith(("http", "mailto:", "data:", "//")):
                continue
            if os.path.basename(url).lower() not in names:
                continue
            target = paths.resolve(f"{directory}/x" if directory else "x", url)
            found.add(target)
            found.add(target.lower())
    return found


def check_orphans(index):
    """Assets nothing references.

    Reported, never gated. New content legitimately arrives as "image added in
    one change, referenced in the next", and the count is only meaningful once
    the link rules are clean: a broken reference makes its own target look
    unreferenced. The runner refuses to answer while any L-* error is open.
    """
    referenced = _referenced_assets(index)
    for path, _ in _media_files(index):
        if path in referenced or path.lower() in referenced:
            continue
        size = os.path.getsize(index.absolute(path))
        yield Finding(WARN, ORPHAN, path,
                      f"not referenced by any document ({size / 1024:.0f} KB)")
