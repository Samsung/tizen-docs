"""T-* rules: table-of-contents and navigation.

TOC rules are corpus-scoped rather than per-document. There are fourteen TOC
files and reading all of them costs milliseconds, and the defect these catch -
an entry pointing at a file that no longer exists - is invisible to a
per-document run unless the change happens to touch that TOC. The three
dangling entries in the corpus had gone unnoticed for exactly that reason.
"""
import os

from .. import publication, toc
from ..findings import ERROR, WARN, Finding

ORPHAN = "T-ORPHAN"
DANGLING = "T-DANGLING"
DEPTH = "T-DEPTH"
META = "T-META"
META_SRC = "T-META-SRC"
CLOSURE = "T-CLOSURE"

# A document absent from its governing TOC is not discoverable in site
# navigation. README files are repository instructions, not documents. Any
# automatically navigated landing page must be declared in docscheck.toml;
# ``index.md`` is intentionally not a blanket exemption.
ORPHAN_EXEMPT = ("README.md",)


def check_orphan(index, path, source):
    """Documents no TOC links to.

    Two sub-cases with different remedies, so the message names which: a page
    nothing at all references is a deletion candidate, while one referenced
    from a document body is real content that simply needs registering.
    """
    base = os.path.basename(path)
    if (base.startswith("toc") or base in ORPHAN_EXEMPT
            or index.config.automatic_landing(path)
            or index.config.publication_exception(path)):
        return
    section = index.config.publication_section(path)
    all_tocs = index.toc_target_sources.get(path, ())
    # Repositories which have not declared an owner retain the historic "any
    # TOC" behaviour. The Tizen Docs configuration covers every public source
    # family explicitly, so new pages in those families cannot escape the gate.
    governing = section.governing_tocs if section else tuple(index.toc_files)
    registered = tuple(toc for toc in all_tocs if toc in governing)
    if registered:
        return
    inbound = [ref for ref in index.references_to(path)
               if not os.path.basename(ref.source).startswith("toc")]
    details = {
        "governing_tocs": list(governing),
        "registered_tocs": list(all_tocs),
        "inbound_links": len(inbound),
        "recommended_section": (section.recommended_section if section else ""),
    }
    if all_tocs:
        message = "registered only in a non-governing TOC; register it in the governing TOC"
    elif inbound:
        message = (f"referenced by {len(inbound)} document(s), but no governing "
                   "TOC publishes it - register it in the governing TOC")
    else:
        message = ("not registered in a governing TOC and referenced by no "
                   "document - register, retire, or add a reviewed exception")
    related = tuple(f"referenced by {ref.source}:{ref.line}" for ref in inbound[:5])
    yield Finding(ERROR, ORPHAN, path, message, related=related, data=details)


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


def check_link_closure(index):
    """Every published page's internal links must publish in that TOC too."""
    for section in index.config.publication_sections:
        if not section.require_link_closure:
            continue
        for toc_path in section.governing_tocs:
            if not index.exists(toc_path):
                continue
            parsed = toc.parse(index.source(toc_path).text, toc_path)
            published = {target for target in parsed.targets if index.exists(target)}
            for source_path in sorted(published):
                if not source_path.endswith(".md"):
                    continue
                for target, line, _, raw in publication.linked_documents(index, source_path):
                    if not section.matches(target) or target in published:
                        continue
                    yield Finding(
                        ERROR, CLOSURE, toc_path,
                        f"{source_path}:{line} links to {raw}, but this TOC does "
                        f"not publish {target}",
                        related=(f"add {target} to {toc_path}",),
                        syntax="toc-md")
