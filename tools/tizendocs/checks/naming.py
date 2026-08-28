"""N-* rules: file and directory naming."""
import os
import re

from ..findings import ERROR, Finding

KEBAB = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*\.md$")
KEBAB_DIR = re.compile(r"^[a-z0-9]+(?:[-.][a-z0-9]+)*$")

RULE = "N-KEBAB"
DIR_RULE = "N-KEBAB-DIR"


def exempt(base):
    return base.startswith("toc") or base == "README.md"


def check_kebab(index, path, source):
    base = os.path.basename(path)
    if not exempt(base) and not KEBAB.match(base):
        yield Finding(ERROR, RULE, path, "new document names use lowercase kebab-case")


def check_directory(index, path, source):
    """New directory names must be lowercase kebab-case.

    Only new ones. Renaming an existing directory such as platform/HAL/ would
    break dozens of links for a cosmetic gain, so the legacy names stay and are
    listed under [naming] in docscheck.toml.

    That list is load-bearing rather than cosmetic. The rule is scoped to added
    files, but this check walks every component of the path, so without it
    adding *any* file inside a legacy directory reports the directory - a
    finding the change cannot act on and the rule never meant to raise.
    """
    for part in os.path.dirname(path).split("/")[1:]:
        if index.legacy_directory(part):
            continue
        if not KEBAB_DIR.match(part):
            yield Finding(ERROR, DIR_RULE, path,
                          f"directory name is not lowercase kebab-case: {part}")
            return
