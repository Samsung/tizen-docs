"""D-* rules: document body structure."""
import os

from ..findings import ERROR, WARN, Finding

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


FRONT_MATTER = "D-FM"

#: The only key the corpus uses. SKILL.md tells authors not to invent others.
KNOWN_KEYS = frozenset({"keyword"})


def check_front_matter(index, path, source):
    """Front matter, where present, must parse and use only known keys.

    A parse failure is reported distinctly from an unknown key: a tab-indented
    block yields an empty mapping in many parsers and would otherwise pass a
    permissive check silently.
    """
    raw = source.raw
    if not raw.startswith("---"):
        return
    end = raw.find("\n---", 3)
    if end == -1:
        yield Finding(ERROR, FRONT_MATTER, path,
                      "front matter is opened but never closed", line=1)
        return
    block = raw[3:end]
    keys = []
    for offset, line in enumerate(block.split("\n"), start=2):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line[:1] in " \t":
            continue  # A continuation of the previous key.
        name, separator, _ = line.partition(":")
        if not separator:
            yield Finding(ERROR, FRONT_MATTER, path,
                          f"front matter line is not a key: {line.strip()!r}",
                          line=offset)
            continue
        keys.append((name.strip(), offset))
    for name, offset in keys:
        if name not in KNOWN_KEYS:
            yield Finding(WARN, FRONT_MATTER, path,
                          f"unknown front matter key: {name}", line=offset)
