"""Link diagnosis. "Target does not exist" is true of every broken reference
and actionable for none, so each class gets its own rule and, where the
correction is unambiguous, a suggested fix."""
from conftest import FIXTURES, run_tree


def findings(name):
    return {(f.rule, f.fix) for f in run_tree(FIXTURES / name)}


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
