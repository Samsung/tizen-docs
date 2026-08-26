"""N-* rules: file and directory naming."""
import os
import re

from ..findings import ERROR, Finding

KEBAB = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*\.md$")

RULE = "N-KEBAB"


def exempt(base):
    return base.startswith("toc") or base == "README.md"


def check_kebab(index, path, source):
    base = os.path.basename(path)
    if not exempt(base) and not KEBAB.match(base):
        yield Finding(ERROR, RULE, path, "new document names use lowercase kebab-case")
