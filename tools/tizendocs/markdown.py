"""Markdown text extraction: links, images, headings, anchors."""
import re
import urllib.parse

HEADING = re.compile(r"^(#{1,6})\s+(.+?)\s*$", re.M)
LINK = re.compile(r"(?<!!)\[[^]]*\]\(([^)\s]+)(?:\s+[^)]*)?\)")
IMAGE = re.compile(r"!\[[^]]*\]\(([^)\s]+)(?:\s+[^)]*)?\)")
NAMED_ANCHOR = re.compile(r'<a\s+(?:name|id)="([^"]+)"', re.I)
CURLY_ANCHOR = re.compile(r"\{#([^}]+)\}")

EXTERNAL = ("http://", "https://", "mailto:")


def read(path):
    with open(path, encoding="utf-8", errors="replace") as file:
        return file.read()


def without_code(text):
    """Strip fenced and inline code so their contents are never linkified."""
    text = re.sub(r"^\s*(```|~~~).*?^\s*\1\s*$", "", text, flags=re.M | re.S)
    return re.sub(r"`[^`]*`", "", text)


def headings(text):
    return list(HEADING.finditer(text))


def references(text):
    """Yield ``(kind, url)`` for every Markdown link and image target.

    Links are yielded before images, matching the order findings were
    historically reported in.
    """
    for pattern, kind in ((LINK, "link"), (IMAGE, "image")):
        for match in pattern.finditer(text):
            yield kind, match.group(1).strip("<> ")


def split_fragment(url):
    """Return ``(path, fragment)`` with percent-escapes decoded."""
    raw, _, fragment = urllib.parse.unquote(url).partition("#")
    return raw, fragment


def is_external(url):
    return url.startswith(EXTERNAL)
