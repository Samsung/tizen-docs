"""The text report keeps the historical line shape, so grep patterns survive."""
from tizendocs.findings import ERROR, Finding
from tizendocs.report import text


def test_line_shape():
    finding = Finding(ERROR, "L-BROKEN", "docs/a.md", "link target does not exist: b.md")
    assert text.render([finding]) == \
        "ERROR L-BROKEN docs/a.md: link target does not exist: b.md\n"


def test_no_findings_renders_nothing():
    assert text.render([]) == ""


def test_line_number_is_included_when_known():
    finding = Finding(ERROR, "L-DEPTH", "docs/a.md", "broken", line=41, col=7,
                      fix="media/x.mp4")
    assert text.render([finding]) == (
        "ERROR L-DEPTH docs/a.md:41: broken\n"
        "  fix: media/x.mp4\n")


def test_summary_is_appended_when_supplied():
    assert text.render([], "check_docs: 0 ERROR, 0 WARN (3 files, 0.10s)") == \
        "check_docs: 0 ERROR, 0 WARN (3 files, 0.10s)\n"
