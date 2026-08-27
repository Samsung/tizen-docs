"""Accepted findings, so a rule can gate everything else immediately.

The alternative to a baseline is leaving the rule off, which lets new instances
of the same defect land unnoticed. Recording the existing ones buys enforcement
for everything else while the backlog is worked through.
"""
from tizendocs import baseline
from tizendocs.findings import ERROR, WARN, Finding

BROKEN = Finding(ERROR, "L-BROKEN", "docs/a.md", "link target does not exist: x.md",
                 line=12)
OTHER = Finding(ERROR, "L-BROKEN", "docs/b.md", "link target does not exist: y.md",
                line=3)


def test_a_listed_finding_is_demoted_to_warn():
    kept, stale = baseline.apply([BROKEN], [baseline.key(BROKEN)])
    assert [f.level for f in kept] == [WARN]
    assert "[baselined]" in kept[0].message
    assert stale == []


def test_an_unlisted_finding_still_fails():
    kept, _ = baseline.apply([BROKEN, OTHER], [baseline.key(BROKEN)])
    assert [(f.rule, f.level) for f in kept] == [
        ("L-BROKEN", WARN), ("L-BROKEN", ERROR)]


def test_matching_ignores_line_numbers():
    """So editing a paragraph above a finding does not silently un-baseline it."""
    moved = Finding(BROKEN.level, BROKEN.rule, BROKEN.path, BROKEN.message, line=900)
    kept, stale = baseline.apply([moved], [baseline.key(BROKEN)])
    assert kept[0].level == WARN and stale == []


def test_an_entry_that_no_longer_reproduces_is_reported():
    """A stale baseline is how a regression hides."""
    _, stale = baseline.apply([], [baseline.key(BROKEN)])
    assert stale == [baseline.key(BROKEN)]


def test_comments_are_preserved_when_loading(tmp_path):
    path = tmp_path / "baseline.txt"
    path.write_text("# why\n\n" + baseline.key(BROKEN) + "\n", encoding="utf-8")
    entries, comments = baseline.load(str(path))
    assert entries == [baseline.key(BROKEN)]
    assert comments == ["# why"]


def test_a_missing_file_means_no_baseline(tmp_path):
    assert baseline.load(str(tmp_path / "absent.txt")) == ([], [])


def test_render_round_trips(tmp_path):
    path = tmp_path / "baseline.txt"
    path.write_text(baseline.render([BROKEN, OTHER], ["# header"]), encoding="utf-8")
    entries, comments = baseline.load(str(path))
    assert comments == ["# header"]
    assert set(entries) == {baseline.key(BROKEN), baseline.key(OTHER)}
