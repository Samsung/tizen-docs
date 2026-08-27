"""Markdown text extraction: links, images, headings, anchors.

Code is *masked* rather than deleted. Deleting it was simpler, but it shifted
every subsequent offset, which made accurate line numbers impossible - and a
finding without a line number cannot become an inline review comment.
"""
import re
import urllib.parse

HEADING = re.compile(r"^(#{1,6})\s+(.+?)\s*$", re.M)
LINK = re.compile(r"(?<!!)\[[^]]*\]\(([^)\s]+)(?:\s+[^)]*)?\)")
IMAGE = re.compile(r"!\[[^]]*\]\(([^)\s]+)(?:\s+[^)]*)?\)")
NAMED_ANCHOR = re.compile(r'<a\s+(?:name|id)="([^"]+)"', re.I)
CURLY_ANCHOR = re.compile(r"\{#([^}]+)\}")

# Pattern kept byte-for-byte from the original implementation: loosening the
# closing fence to allow trailing text made an opening fence with a language
# tag pair as a closer, which silently masked live content.
# Raw HTML is used throughout the corpus wherever Markdown cannot express
# something: sized images, videos, and tables of links. Parsing only Markdown
# syntax left every one of those references unchecked.
HTML_TAG = re.compile(r"<(img|a|source|video|iframe)\b([^>]*)>", re.I)
HTML_ATTR = re.compile(r"\b(src|href|poster)\s*=\s*(['\"])(.*?)\2", re.I)

FENCE = re.compile(r"^\s*(```|~~~).*?^\s*\1\s*$", re.M | re.S)
INLINE_CODE = re.compile(r"`[^`]*`")

EXTERNAL = ("http://", "https://", "mailto:")


def read(path):
    with open(path, encoding="utf-8", errors="replace") as file:
        return file.read()


def _blank(match):
    """Replace a span with spaces, keeping its length and its newlines."""
    span = match.group(0)
    if "\n" not in span:  # the common case: inline code
        return " " * len(span)
    return "\n".join(" " * len(line) for line in span.split("\n"))


def without_code(text):
    """Mask fenced and inline code, preserving offsets and line breaks."""
    text = FENCE.sub(_blank, text)
    return INLINE_CODE.sub(_blank, text)


class Source:
    """A masked document plus the offset-to-line mapping findings need."""

    def __init__(self, raw):
        self.raw = raw
        self.text = without_code(raw)
        self._starts = None

    def position(self, offset):
        """Return the 1-based ``(line, column)`` for a character *offset*.

        The line table is built on first use. Most documents produce no
        findings at all, so computing it up front would be pure overhead.
        """
        if self._starts is None:
            starts, index = [0], self.text.find("\n")
            while index != -1:
                starts.append(index + 1)
                index = self.text.find("\n", index + 1)
            self._starts = starts
        low, high = 0, len(self._starts) - 1
        while low < high:
            middle = (low + high + 1) // 2
            if self._starts[middle] <= offset:
                low = middle
            else:
                high = middle - 1
        return low + 1, offset - self._starts[low] + 1

    def headings(self):
        return list(HEADING.finditer(self.text))

    def references(self):
        """Yield ``(syntax, url, offset)`` for every Markdown link and image.

        The offset is resolved to a line only when a finding is emitted; most
        references are fine and never need one.

        Links precede images, keeping the historical report order.
        """
        for pattern, syntax in ((LINK, "md-link"), (IMAGE, "md-image")):
            for match in pattern.finditer(self.text):
                yield syntax, match.group(1).strip("<> "), match.start()

    def html_references(self):
        """Yield ``(syntax, url, offset)`` for HTML link, image and media refs.

        Two stages rather than one regex, so a tag carrying more than one
        relevant attribute (a <video> with both src and poster) is fully
        covered.
        """
        for tag in HTML_TAG.finditer(self.text):
            name = tag.group(1).lower()
            for attr in HTML_ATTR.finditer(tag.group(2)):
                yield (f"html-{name}", attr.group(3).strip(),
                       tag.start(2) + attr.start(3))

    def all_references(self):
        """Every reference in the document, Markdown and HTML alike."""
        yield from self.references()
        yield from self.html_references()

    def anchors(self):
        found = {match.group(1).lower() for match in NAMED_ANCHOR.finditer(self.text)}
        found.update(m.group(1).lower() for m in CURLY_ANCHOR.finditer(self.text))
        return found


def split_fragment(url):
    """Return ``(path, fragment)`` with percent-escapes decoded."""
    raw, _, fragment = urllib.parse.unquote(url).partition("#")
    return raw, fragment


def is_external(url):
    return url.startswith(EXTERNAL)
