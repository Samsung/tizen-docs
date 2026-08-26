"""The text report keeps the historical line shape, so grep patterns survive."""
from tizendocs.findings import ERROR, Finding
from tizendocs.report import text


def test_line_shape():
    finding = Finding(ERROR, "L-BROKEN", "docs/a.md", "link target does not exist: b.md")
    assert text.render([finding]) == \
        "ERROR L-BROKEN docs/a.md: link target does not exist: b.md\n"


def test_no_findings_renders_nothing():
    assert text.render([]) == ""
