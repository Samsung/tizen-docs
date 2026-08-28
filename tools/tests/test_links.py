"""Link diagnosis. "Target does not exist" is true of every broken reference
and actionable for none, so each class gets its own rule and, where the
correction is unambiguous, a suggested fix."""
from conftest import FIXTURES, run_tree


def findings(name):
    """Link findings only.

    The media rules also fire on these fixtures, and correctly: a reference
    that points at the wrong path makes its own target look unreferenced. That
    interaction is asserted in the fixtures' expected findings and is why the
    media subcommand refuses to run while a link error is open.
    """
    return {(f.rule, f.fix) for f in run_tree(FIXTURES / name)
            if f.rule.startswith("L-")}


def test_html_references_are_checked():
    """Markdown-only parsing left every <a>, <img>, <source>, <video> and
    <iframe> reference in the corpus unverified."""
    assert findings("l-html") == {("L-HTML", "")}


def test_depth_shift_names_the_correction():
    """One ../ too many is the signature of a file that moved without its
    links being recomputed."""
    assert findings("l-depth") == {
        ("L-DEPTH", "media/clip.mp4"), ("L-DEPTH", "media/shot.png")}


def test_case_only_mismatch_names_the_real_filename():
    """Unambiguous: there are no case-only collisions under docs/."""
    assert findings("l-case") == {("L-CASE", "media/report.png")}


def test_redundant_docs_prefix_is_its_own_diagnosis():
    """Site-root already means the docs/ directory, so /docs/... resolves to
    docs/docs/... - which reads as correct when written by hand."""
    assert findings("l-docsprefix") == {("L-DOCSPREFIX", "/guides/media/shot.png")}


def test_a_site_root_route_without_an_extension_is_not_a_finding():
    """The published site serves routes that have no file in this checkout."""
    assert findings("minimal") == set()

def test_a_site_root_media_reference_must_resolve():
    """The route exemption above is for pages, not images.

    A page behind /application/... may come from another pipeline, so its
    absence here proves nothing. Media has no other pipeline — every image the
    site serves under docs/ is committed here — yet the exemption was keyed on
    "not .md" and swallowed images too.

    That silence cost 33 files. "/docs/<path>" resolves to docs/docs/<path>, so
    the orphan scan never counted those references either; M-ORPHAN called the
    images unreferenced and #2388 deleted them while eight published pages still
    pointed at them. Reporting the reference is what closes the loop: orphans
    are only trusted once the L-* rules are clean.
    """
    assert findings("l-media-site-root") == {("L-HTML", "")}
