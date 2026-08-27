"""T-XML* rules: the Eclipse-help table of contents for the Web API reference.

docs/application/web/api/toc.xml is 36,000 lines and drives the whole Web API
navigation, so a malformed edit takes the section out silently.

Its hrefs are deliberately *not* checked. They all begin "html/", and
docs/application/web/api/html/ does not exist: the paths are relative to the
build's output layout, not to this repository. Verifying them would mean
guessing at the build, and mapping "html/" onto the versioned directories still
leaves the great majority unresolved because the file continues to enumerate
the Native API doxygen tree that is published elsewhere.
"""
import os
import re
import xml.etree.ElementTree as ElementTree

from ..findings import ERROR, Finding

XML = "T-XML"
XMLVER = "T-XMLVER"

TOC = "docs/application/web/api/toc.xml"
VERSION = re.compile(r'<tizen-api\s+version="([^"]+)"')
NUMERIC = re.compile(r"^\d+\.\d+(\.\d+)?$")


def _versions_on_disk(index):
    directory = index.absolute(os.path.dirname(TOC))
    try:
        entries = os.listdir(directory)
    except OSError:
        return set()
    return {name for name in entries
            if NUMERIC.match(name) and os.path.isdir(os.path.join(directory, name))}


def check_wellformed(index):
    if not index.exists(TOC):
        return
    try:
        ElementTree.parse(index.absolute(TOC))
    except ElementTree.ParseError as error:
        yield Finding(ERROR, XML, TOC, f"is not well-formed XML: {error}",
                      line=getattr(error, "position", (1, 0))[0])


def check_versions(index):
    """Declared API versions must match the directories that exist.

    The failure this catches happens at release time: a new Tizen version
    directory is imported and toc.xml is not updated, so the new reference is
    published but unreachable.
    """
    if not index.exists(TOC):
        return
    text = index.source(TOC).raw if TOC.endswith(".md") else \
        open(index.absolute(TOC), encoding="utf-8", errors="replace").read()
    declared = set(VERSION.findall(text))
    if not declared:
        return
    on_disk = _versions_on_disk(index)
    missing = sorted(on_disk - declared)
    extra = sorted(declared - on_disk)
    if missing:
        yield Finding(ERROR, XMLVER, TOC,
                      f"API version directories exist but are not declared: "
                      f"{', '.join(missing)}")
    if extra:
        yield Finding(ERROR, XMLVER, TOC,
                      f"declares API versions with no directory: {', '.join(extra)}")
