"""Table-of-contents parsing.

A TOC here is a Markdown file whose ATX heading depth *is* the navigation
depth, which no off-the-shelf documentation tool models. Metadata rides in the
link title:

    ## [Overview](/a/b.md "source:https://...,tags:['x'],authors:['y@z']")
"""
import os
import re
import urllib.parse
from dataclasses import dataclass, field

from . import markdown, paths

#: A TOC line: heading marker, then optionally a link with an optional title.
ENTRY = re.compile(
    r"^(?P<depth>#{1,6})\s*"
    r"(?:\[(?P<title>[^]]*)\]\((?P<href>[^)\s]*)"
    r"(?:\s+\"(?P<meta>[^\"]*)\")?\))?"
    r"(?P<trailing>.*)$")

#: Metadata is expected inside the link parentheses. Some generated TOCs put a
#: quoted string after the closing parenthesis instead, where it renders as
#: literal text.
TRAILING_META = re.compile(r"^\s*\"\s*(?P<meta>.*?)\"\s*$")

SOURCE = re.compile(r"source:\s*(\S+?),?(?:\s|$)")
KEY = re.compile(r"(?<![\w-])([a-z][a-z_-]*)\s*:")

#: The keys a TOC link title may carry.
KNOWN_KEYS = frozenset({"source", "tags", "authors"})

BLOB = "https://github.com/Samsung/tizen-docs/blob/master/"


@dataclass
class Node:
    toc: str
    line: int
    depth: int
    title: str
    href: str
    target: str = ""
    meta: str = ""
    meta_outside: bool = False


@dataclass
class Toc:
    path: str
    nodes: list = field(default_factory=list)
    depth_jumps: list = field(default_factory=list)

    @property
    def targets(self):
        return [node.target for node in self.nodes if node.target]


def _resolve(toc_path, href):
    raw = urllib.parse.unquote(href.strip("<> ")).partition("#")[0]
    if not raw or markdown.is_external(raw):
        return ""
    return paths.resolve(toc_path, raw)


def parse(text, path):
    """Parse one ``toc*.md`` into a :class:`Toc`."""
    result = Toc(path=path)
    previous = 0
    for number, line in enumerate(text.split("\n"), 1):
        match = ENTRY.match(line)
        if not match:
            continue
        depth = len(match.group("depth"))
        if previous and depth > previous + 1:
            result.depth_jumps.append((number, previous, depth))
        previous = depth
        if match.group("href") is None:
            continue  # A grouping node with no link is legitimate.
        meta = match.group("meta") or ""
        outside = False
        if not meta:
            trailing = TRAILING_META.match(match.group("trailing") or "")
            if trailing:
                meta, outside = trailing.group("meta"), True
        result.nodes.append(Node(
            toc=path, line=number, depth=depth,
            title=match.group("title") or "", href=match.group("href"),
            target=_resolve(path, match.group("href")),
            meta=meta, meta_outside=outside))
    return result


URL = re.compile(r"https?://\S+")


def metadata_keys(meta):
    """The keys a link title declares.

    URLs are stripped first: the scheme in a source: value would otherwise be
    read as a key named "https".
    """
    return set(KEY.findall(URL.sub("", meta)))


def declared_source(meta):
    """The repository path a ``source:`` URL claims, or ``""``."""
    found = SOURCE.search(meta)
    if not found:
        return ""
    url = found.group(1).rstrip(",")
    return url[len(BLOB):] if url.startswith(BLOB) else url
