"""D-* rules: document body structure."""
import os

from ..findings import ERROR, Finding

RULE = "D-H1"


def exempt(base):
    return base.startswith("toc") or base == "README.md"


def check_h1(index, path, source):
    """Exactly one H1, and it must be the document's first heading."""
    base = os.path.basename(path)
    if exempt(base):
        return
    headings = source.headings()
    tops = [item for item in headings if len(item.group(1)) == 1]
    if len(tops) != 1:
        line = source.position(tops[1].start())[0] if len(tops) > 1 else 0
        yield Finding(ERROR, RULE, path, "document must contain exactly one H1", line=line)
    elif headings and len(headings[0].group(1)) != 1:
        line, col = source.position(headings[0].start())
        yield Finding(ERROR, RULE, path, "the first heading must be the H1",
                      line=line, col=col)
