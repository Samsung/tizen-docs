"""T-* rules: table-of-contents and navigation."""
import os

from ..findings import ERROR, Finding

ORPHAN = "T-ORPHAN"

# A document absent from its TOC is not discoverable on the published site.
# Landing pages are exempt because the site routes a directory to them.
ORPHAN_EXEMPT = ("README.md", "index.md")


def check_orphan(index, path, source):
    base = os.path.basename(path)
    if base.startswith("toc") or base in ORPHAN_EXEMPT:
        return
    if path not in index.toc_targets:
        yield Finding(ERROR, ORPHAN, path, "document is not linked from a TOC")
