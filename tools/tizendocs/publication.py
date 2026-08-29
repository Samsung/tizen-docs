"""Helpers for publication graphs whose nodes are Markdown documents."""
import os

from . import markdown, paths


DOCUMENT_SYNTAXES = frozenset({"md-link", "html-a"})


def document_target(index, source_path, raw_url):
    """Resolve an internal document URL to an existing Markdown source.

    SDK prose contains a mixture of ``.md``, legacy ``.html`` and extensionless
    links.  The publisher converts all three to Markdown routes, so publication
    closure must use the same equivalence instead of treating them as different
    documents.
    """
    raw, _ = markdown.split_fragment(raw_url.partition("?")[0])
    if not raw or markdown.is_external(raw):
        return ""
    target = paths.resolve(source_path, raw)
    root, extension = os.path.splitext(target)
    candidates = [target]
    if extension.lower() in {".html", ".htm"}:
        candidates = [root + ".md"]
    elif not extension:
        candidates = [target + ".md", target + "/index.md"]
    for candidate in candidates:
        if candidate.endswith(".md") and index.exists(candidate):
            return candidate
    return ""


def linked_documents(index, source_path):
    """Yield existing internal document targets linked by one document."""
    source = index.source(source_path)
    for syntax, raw, offset in source.all_references():
        if syntax not in DOCUMENT_SYNTAXES:
            continue
        target = document_target(index, source_path, raw)
        if target:
            line, column = source.position(offset)
            yield target, line, column, raw
