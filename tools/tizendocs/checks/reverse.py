"""R-* rules: what a removal breaks elsewhere in the corpus.

--changed-only looks at the links going *out* of changed files. It cannot see
that deleting a page broke links in files the change never touched, and the
previous implementation made that worse by skipping deleted paths entirely
(`not os.path.isfile(path)` returned before any check ran).

This is the direction that matters most here: the recent history of this
repository is dominated by removals and information-architecture moves, and
reviewguide/review_points_guide.md documents the fix as a manual grep, with a
screenshot of someone doing it by hand.
"""
import os

from ..findings import ERROR, WARN, Finding

INBOUND = "R-INBOUND"
TOC = "R-TOC"
MEDIA = "R-MEDIA"
ANCHOR = "R-ANCHOR"


def _is_toc(path):
    return os.path.basename(path).startswith("toc")


def _describe(change, removed):
    replacement = change.replacement(removed)
    if replacement:
        return f"renamed to {replacement}", replacement
    return "deleted by this change; no replacement given", ""


def _findings(index, change, rule, want_toc):
    for removed in change.removed:
        if not removed.startswith("docs/"):
            continue
        note, replacement = _describe(change, removed)
        for reference in index.references_to(removed):
            if _is_toc(reference.source) is not want_toc:
                continue
            # A file that this change also removes cannot carry a stale link.
            if change.status.get(reference.source) in ("D", "R"):
                continue
            subject = "TOC entry references" if want_toc else "references"
            fix = ""
            if replacement:
                fix = _rewrite(reference.raw, removed, replacement)
            yield Finding(
                ERROR, rule, reference.source,
                f"{subject} {removed}, {note}",
                line=reference.line, col=reference.col,
                syntax=reference.syntax, fix=fix, cause=removed,
                related=(f"caused by {removed}",))


def _rewrite(raw, removed, replacement):
    """Suggest the new reference, preserving the author's link style."""
    fragment = raw.partition("#")[2]
    suffix = f"#{fragment}" if fragment else ""
    if raw.startswith("/"):
        return "/" + replacement[len("docs/"):] + suffix
    old_name, new_name = os.path.basename(removed), os.path.basename(replacement)
    if os.path.dirname(removed) == os.path.dirname(replacement):
        return raw.replace(old_name, new_name)
    return ""  # A moved file needs a recomputed relative path; leave it to a human.


def check_inbound(index, change):
    """Documents still pointing at a path this change removes."""
    yield from _findings(index, change, INBOUND, want_toc=False)


def check_toc(index, change):
    """TOC entries still pointing at a path this change removes.

    Separate from R-INBOUND because the remedy differs: a stale TOC entry
    silently drops a node out of site navigation, while a stale body link is a
    visible 404. Reported under one id, a reviewer fixes the body links and
    considers the finding closed.
    """
    yield from _findings(index, change, TOC, want_toc=True)


def check_media(index, change):
    """Assets that became unreferenced because their only documents are gone.

    reviewguide: "if a file is deleted, check the images used it the file. If
    there are images that are not used any more, remove the images also."

    The removed documents' references have to be read from the base revision:
    the reverse graph is built from the working tree, where they no longer
    exist.

    WARN because the intent is unobservable: the author may be moving content
    across two changes, or keeping an asset for a page not yet written.
    """
    from .. import markdown, paths

    candidates = set()
    for removed in change.removed:
        before = change.previous(removed)
        if before is None:
            continue
        for _, url, _ in markdown.Source(before).all_references():
            raw, _ = markdown.split_fragment(url)
            if not raw or markdown.is_external(raw):
                continue
            target = paths.resolve(removed, raw)
            if target.endswith(".md") or not target.startswith("docs/"):
                continue
            if os.path.basename(os.path.dirname(target)) != "media":
                continue
            if index.exists(target):
                candidates.add(target)

    orphaned = sorted(target for target in candidates
                      if not index.references_to(target))
    if not orphaned:
        return
    total = sum(os.path.getsize(index.absolute(path)) for path in orphaned)
    yield Finding(
        WARN, MEDIA, sorted(orphaned)[0],
        f"{len(orphaned)} media file(s) totalling {total / 1024:.0f} KB became "
        "unreferenced when this change removed the only documents using them; "
        "delete them or say why they are kept",
        related=tuple(sorted(orphaned)[:10]))


def check_anchor(index, change):
    """Headings a change removes that other documents still link to.

    SKILL.md already promises that renaming a heading means updating incoming
    links; this is the only mechanism that could keep that promise. WARN
    because the slug rule is an approximation of the renderer's.
    """
    from .. import slug as slug_module
    for path, state in sorted(change.status.items()):
        if state != "M" or not path.endswith(".md") or not index.exists(path):
            continue
        before = change.previous(path)
        if before is None:
            continue
        gone = _heading_slugs(before) - _heading_slugs(index.source(path).raw)
        for fragment in sorted(gone):
            for reference in index.references_to(path):
                if reference.raw.partition("#")[2].lower() != fragment:
                    continue
                yield Finding(
                    WARN, ANCHOR, reference.source,
                    f"links to #{fragment} in {path}, a heading this change "
                    "removes", line=reference.line, col=reference.col,
                    syntax=reference.syntax, cause=path)


def _heading_slugs(text):
    from .. import markdown, slug as slug_module
    source = markdown.Source(text)
    return {slug_module.slug(match.group(2)) for match in source.headings()}
