"""Content advisories drawn from reviewguide/review_points_guide.md.

Both are WARN and both are deliberately narrow in scope, because their
corpus-wide violation counts can never reach zero and a rule that fires
hundreds of times is a rule people turn off.
"""
import os
import re

from ..findings import WARN, Finding

OVERVIEW = "D-OVERVIEW"
FEATPRIV = "L-FEATPRIV"

LANDING = ("overview.md", "index.md")

#: A Tizen feature or privilege key. reviewguide: "they look like a kind of URL,
#: but are not. As they are easy to be confused as a URL, always use code tag to
#: features and privileges to prevent the hyper link."
KEY = r"http://tizen\.org/(?:feature|privilege)/[^\s)>\"']+"
LINKED = re.compile(rf"\[[^]]*\]\(\s*({KEY})\s*\)")
AUTOLINK = re.compile(rf"<({KEY})>")

#: The reference pages define anchors with an empty link target, which is the
#: house idiom rather than a defect: [http://tizen.org/feature/x](){#feature/x}
EMPTY_TARGET = re.compile(r"\[http://tizen\.org/(?:feature|privilege)/[^]]*\]\(\s*\)")

#: Feature and privilege keys are declared in manifest snippets as XML bodies.
PRIVILEGE_ELEMENT = re.compile(r"<privilege>.*?</privilege>", re.S)


def check_overview(index, path, source):
    """A new page should be reachable from its section's landing page.

    reviewguide: "If a new file is added, add a simple description and a hyper
    link to overview.md of the section that the new page is included."

    Added files only, and WARN: two thirds of the existing corpus does not
    satisfy this, and a page reachable through the TOC alone is legitimate. The
    value is the reminder at the moment of writing.
    """
    base = os.path.basename(path)
    if base.startswith("toc") or base in LANDING or base == "README.md":
        return
    directory = os.path.dirname(path)
    while directory.startswith("docs"):
        landings = [f"{directory}/{name}" for name in LANDING]
        present = [page for page in landings if index.exists(page)]
        if present:
            if any(path in {ref for ref in _targets(index, page)} for page in present):
                return
            yield Finding(WARN, OVERVIEW, path,
                          "new page is not linked from "
                          f"{' or '.join(present)}; add it there or confirm the "
                          "TOC entry is the only route intended")
            return
        directory = os.path.dirname(directory)


def _targets(index, page):
    from .. import markdown, paths
    source = index.source(page)
    for _, url, _ in source.all_references():
        raw, _ = markdown.split_fragment(url)
        if raw and not markdown.is_external(raw):
            yield paths.resolve(page, raw)


def check_feature_privilege(index, path, source):
    """Feature and privilege keys must be code, not links."""
    text = PRIVILEGE_ELEMENT.sub("", source.text)
    for pattern in (LINKED, AUTOLINK):
        for match in pattern.finditer(text):
            if EMPTY_TARGET.search(text, max(0, match.start() - 200), match.end()):
                continue
            line, col = source.position(match.start())
            yield Finding(WARN, FEATPRIV, path,
                          "feature and privilege keys are not URLs; wrap "
                          f"`{match.group(1)}` in a code span so it does not "
                          "render as a link", line=line, col=col)
