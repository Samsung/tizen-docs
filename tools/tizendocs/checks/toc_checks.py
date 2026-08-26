"""T-* rules: table-of-contents and navigation.

TOC rules are corpus-scoped rather than per-document. There are fourteen TOC
files and reading all of them costs milliseconds, and the defect these catch -
an entry pointing at a file that no longer exists - is invisible to a
per-document run unless the change happens to touch that TOC. The three
dangling entries in the corpus had gone unnoticed for exactly that reason.
"""
import os

from .. import toc
from ..findings import ERROR, WARN, Finding

ORPHAN = "T-ORPHAN"
DANGLING = "T-DANGLING"
DEPTH = "T-DEPTH"
META = "T-META"
META_SRC = "T-META-SRC"

# A document absent from its TOC is not discoverable on the published site.
# Landing pages are exempt because the site routes a directory to them.
ORPHAN_EXEMPT = ("README.md", "index.md")


def check_orphan(index, path, source):
    """Documents no TOC links to.

    Two sub-cases with different remedies, so the message names which: a page
    nothing at all references is a deletion candidate, while one referenced
    from a document body is real content that simply needs registering.
    """
    base = os.path.basename(path)
    if base.startswith("toc") or base in ORPHAN_EXEMPT:
        return
    if path in index.toc_targets:
        return
    inbound = [ref for ref in index.references_to(path)
               if not os.path.basename(ref.source).startswith("toc")]
    if inbound:
        related = tuple(f"referenced by {ref.source}:{ref.line}" for ref in inbound[:5])
        message = (f"linked from no toc*.md, but referenced by {len(inbound)} "
                   "document(s) - register it in the governing TOC")
    else:
        related = ()
        message = ("linked from no toc*.md and referenced by no document - "
                   "unreachable on the published site; delete or register it")
    yield Finding(ERROR, ORPHAN, path, message, related=related)


def _tocs(index):
    for path in index.toc_files:
        yield toc.parse(index.source(path).text, path)


def check_dangling(index):
    """TOC entries whose target file does not exist - T-ORPHAN's missing mirror."""
    for parsed in _tocs(index):
        for node in parsed.nodes:
            if not node.target or index.exists(node.target):
                continue
            if index.exempt_existence(node.target):
                continue
            if not node.href.endswith(".md") and node.href.startswith("/"):
                continue  # A site-root route need not have a file here.
            yield Finding(ERROR, DANGLING, node.toc,
                          f"TOC entry target does not exist: {node.href}",
                          line=node.line, syntax="toc-md")


def check_depth(index):
    """Heading depth is navigation depth, so a skipped level loses a node."""
    for parsed in _tocs(index):
        for line, previous, depth in parsed.depth_jumps:
            yield Finding(ERROR, DEPTH, parsed.path,
                          f"navigation depth jumps from {previous} to {depth}",
                          line=line, syntax="toc-md")


def check_meta(index, path, source):
    """Metadata must sit inside the link parentheses and use known keys.

    Outside them it is not a link title at all; it renders as literal text.
    """
    if not os.path.basename(path).startswith("toc"):
        return
    parsed = toc.parse(source.text, path)
    outside = [node for node in parsed.nodes if node.meta_outside]
    if outside:
        yield Finding(
            WARN, META, path,
            f"{len(outside)} entries put link metadata after the closing "
            "parenthesis instead of inside it, where it renders as literal text",
            line=outside[0].line, syntax="toc-md")
    for node in parsed.nodes:
        if not node.meta:
            continue
        unknown = sorted(toc.metadata_keys(node.meta) - toc.KNOWN_KEYS)
        if unknown:
            yield Finding(WARN, META, path,
                          f"unknown link metadata key(s): {', '.join(unknown)}",
                          line=node.line, syntax="toc-md")


def check_meta_source(index):
    """A ``source:`` URL must name the entry's own link target."""
    for parsed in _tocs(index):
        if index.generated(parsed.path):
            continue
        for node in parsed.nodes:
            declared = toc.declared_source(node.meta)
            if not declared or not node.target or declared == node.target:
                continue
            yield Finding(ERROR, META_SRC, node.toc,
                          f"source: names {declared} but the entry links to "
                          f"{node.target}", line=node.line, syntax="toc-md")
