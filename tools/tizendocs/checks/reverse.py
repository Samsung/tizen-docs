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

from ..findings import ERROR, Finding

INBOUND = "R-INBOUND"
TOC = "R-TOC"


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
