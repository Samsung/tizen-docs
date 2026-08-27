"""Heading-to-anchor slug generation.

The publishing pipeline's Markdown engine is the only authority on anchor ids,
and its configuration (_config.yml) is gitignored, so it cannot be read from
here. Worse, this corpus feeds two sites: docs.tizen.org and the tizen.dev
pipeline in tizen.org.v2.docs, whose scripts/lib/slugify.js differs from the
rule used here - it collapses runs of dashes and trims whitespace rather than
dashes. Its own comment states the risk plainly: reimplementing the renderer's
rule means that the moment the two diverge, healthy anchors are reported as
broken.

With enforcement resting on people and agents reading the output, the risk is
asymmetric: one false L-ANCHOR costs more than one missed. So several sluggers
are implemented and a fragment is accepted if *any* of them produces it. That
makes L-ANCHOR a proof of absence rather than a guess at the renderer, and
L-ANCHOR-AMBIG reports the renderer-dependent middle ground instead of
pretending it is fine.

When the engine is identified, delete the sluggers that do not apply.
"""
import re

STRIP_LINKS = re.compile(r"\[[^]]*\]\([^)]+\)")
INLINE_MARKS = re.compile(r"[`*_]")


def tizen_docs(text):
    """The rule this repository's validator has always used."""
    value = STRIP_LINKS.sub("", text)
    value = INLINE_MARKS.sub("", value).lower()
    value = re.sub(r"[^\w\s-]", "", value)
    return re.sub(r"\s+", "-", value).strip("-")


def v2_slugify(text):
    """tizen.org.v2.docs scripts/lib/slugify.js, which feeds tizen.dev."""
    value = text.lower()
    value = re.sub(r"[^\w\s-]", "", value)
    value = re.sub(r"\s+", "-", value)
    return re.sub(r"-+", "-", value).strip()


def github(text):
    """GitHub Flavored Markdown, which is what a reviewer sees in preview."""
    value = STRIP_LINKS.sub("", text).lower()
    value = re.sub(r"[^\w\s-]", "", value)
    return re.sub(r"\s+", "-", value)


#: Ordered; the first is treated as primary for L-ANCHOR-AMBIG.
SLUGGERS = (("tizen-docs", tizen_docs), ("v2-slugify", v2_slugify),
            ("github", github))

PRIMARY = SLUGGERS[0][0]


def slug(text):
    """The primary rule, kept as a name for callers that need just one."""
    return tizen_docs(text)


def variants(text):
    """Map slugger name to the anchor id it produces for *text*."""
    return {name: function(text) for name, function in SLUGGERS}
