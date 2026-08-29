"""L-* rules: link, image and media target resolution.

A broken reference is reported under the most specific diagnosis that fits.
"Target does not exist" is true of all of them but actionable in none: the
useful report names the mistake, and for three of these classes it can also
name the correction.
"""
import os
import posixpath
import re

from .. import markdown, paths, slug as slug_module
from ..findings import ERROR, WARN, Finding
from .media import MEDIA_SUFFIXES

BROKEN = "L-BROKEN"
ANCHOR = "L-ANCHOR"
ANCHOR_AMBIG = "L-ANCHOR-AMBIG"
HTML = "L-HTML"
DEPTH = "L-DEPTH"
CASE = "L-CASE"
DOCSPREFIX = "L-DOCSPREFIX"

#: How a Markdown reference is described in a message.
KIND = {"md-link": "link", "md-image": "image"}

SITE_PREFIX = f"/{paths.DOCS}/"


def _describe(syntax):
    if syntax in KIND:
        return KIND[syntax]
    return f"<{syntax.removeprefix('html-')}> reference"


def _docs_prefixed(index, raw):
    """A site-root reference that redundantly repeats the docs/ directory.

    Site-root already means the docs/ directory, so "/docs/a/b.png" resolves to
    "docs/docs/a/b.png". Written by hand it looks right, which is why this
    needs its own diagnosis rather than a generic "does not exist".
    """
    if not raw.startswith(SITE_PREFIX):
        return ""
    candidate = paths.resolve("", raw[len(paths.DOCS) + 1:])
    return candidate if index.exists(candidate) else ""


def _is_media(raw):
    """An asset that has to be in this repository.

    The exemption below exists for site-root *routes*: /application/... is a
    published URL and the page behind it may come from another pipeline, so its
    absence here proves nothing. Media has no other pipeline — every image the
    site serves under docs/ is committed here — so a site-root media reference
    that resolves to nothing is simply broken and must be reported.

    Skipping it cost 33 images. A reference written "/docs/<path>" resolves to
    docs/docs/<path>, so the orphan scan never counted it and M-ORPHAN reported
    the files as unreferenced; #2388 then deleted them as dead weight while
    eight published pages still pointed at them. Reporting the reference is what
    closes that loop: check_orphans is only trusted once the L-* rules are
    clean, so the bad reference now has to be fixed before anything can be
    called an orphan.

    Compared case-insensitively: the corpus carries both .png and .PNG.
    """
    return raw.lower().endswith(MEDIA_SUFFIXES)


def _depth_shifted(index, source_path, raw):
    """A relative reference that resolves with one ../ added or removed.

    Almost always a file that moved without its links being recomputed, which
    reviewguide/review_points_guide.md illustrates with a screenshot.
    """
    if raw.startswith("/"):
        return ""
    directory = posixpath.dirname(source_path)
    for candidate_raw in (raw[3:] if raw.startswith("../") else None, f"../{raw}"):
        if not candidate_raw:
            continue
        candidate = paths.to_posix(
            posixpath.normpath(posixpath.join(directory, candidate_raw)))
        if index.exists(candidate):
            return candidate_raw
    return ""


def classify(index, source_path, raw, syntax):
    """Return ``(rule, fix)`` for a reference whose target does not exist."""
    prefixed = _docs_prefixed(index, raw)
    if prefixed:
        return DOCSPREFIX, raw[len(paths.DOCS) + 1:]

    target = paths.resolve(source_path, raw)
    real = index.real_name_of(target)
    if real:
        return CASE, os.path.basename(real) if "/" not in raw else \
            raw.rsplit("/", 1)[0] + "/" + os.path.basename(real)

    shifted = _depth_shifted(index, source_path, raw)
    if shifted:
        return DEPTH, shifted

    return (BROKEN if syntax in KIND else HTML), ""


def check_links(index, path, source):
    if os.path.basename(path).startswith("toc"):
        # A TOC is pure navigation, and T-DANGLING reports the same defect with
        # the framing a reviewer needs: a missing entry drops a node out of the
        # published menu, it is not just a 404 in prose.
        return
    for syntax, url, offset in source.all_references():
        if not url or markdown.is_external(url) or url.startswith("#"):
            continue
        raw, fragment = markdown.split_fragment(url)
        if not raw:
            continue
        target = paths.resolve(path, raw)
        if not index.exists(target):
            if raw.startswith("/") and not raw.endswith(".md") \
                    and not _is_media(raw):
                # A site-root route need not have a file here, but a redundant
                # docs/ prefix is a mistake whatever the extension.
                if not _docs_prefixed(index, raw):
                    continue
            if index.exempt_existence(target):
                continue  # Published by a separate pipeline; see docscheck.toml.
            rule, fix = classify(index, path, raw, syntax)
            line, col = source.position(offset)
            yield Finding(ERROR, rule, path,
                          f"{_describe(syntax)} target does not exist: {url}",
                          line=line, col=col, syntax=syntax, fix=fix)
        elif fragment and target.endswith(".md") and not index.generated(target):
            yield from _check_fragment(index, path, source, offset, url,
                                       target, fragment, syntax)


def _check_fragment(index, path, source, offset, url, target, fragment, syntax):
    """Report a fragment as missing only when no slugger can produce it."""
    wanted = fragment.lower()
    # Renderers disambiguate a repeated heading differently: some append -1,
    # some -2, some nothing at all. Accept the whole family rather than pick a
    # convention and report the others as missing.
    base = re.sub(r"-\d+$", "", wanted)
    if wanted in index.duplicate_headings(target) or \
            base in index.duplicate_headings(target):
        return
    if wanted in index.primary_anchors(target):
        return
    line, col = source.position(offset)
    if wanted in index.anchors(target):
        producers = sorted(
            name for name, function in slug_module.SLUGGERS
            if any(function(m.group(2)) == wanted
                   for m in index.source(target).headings()))
        yield Finding(
            WARN, ANCHOR_AMBIG, path,
            f"anchor is renderer-dependent - produced by {', '.join(producers)} "
            f"but not by {slug_module.PRIMARY}; prefer an explicit "
            f"<a name=\"{fragment}\"></a>: {url}",
            line=line, col=col, syntax=syntax)
        return
    yield Finding(ERROR, ANCHOR, path, f"anchor does not exist: {url}",
                  line=line, col=col, syntax=syntax)
