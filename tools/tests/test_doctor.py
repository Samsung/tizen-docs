"""doctor catches the silent half of configuration rot.

A missing exemption produces noise and someone notices. A stale one produces
silence: the pattern matches nothing, and the exemption it documented is now
misleading text. This was not hypothetical - three paths listed while writing
this toolkit had already been deleted upstream.
"""
from tizendocs import checks, doctor
from tizendocs.config import Config
from tizendocs.index import DocsIndex


def index_for(tmp_path, **config):
    (tmp_path / "docs").mkdir(exist_ok=True)
    (tmp_path / "tools").mkdir(exist_ok=True)
    (tmp_path / "docs" / "live.md").write_text("# Live\n", encoding="utf-8")
    return DocsIndex(root=str(tmp_path), config=Config(config, source="test"))


#: Derived from the registry so adding a rule cannot silently stale this list.
ALL_SEVERITIES = {rule: "error" for rule in checks.RULE_IDS}


def test_reports_a_pattern_that_matches_nothing(tmp_path):
    index = index_for(tmp_path, rules=ALL_SEVERITIES,
                      classes=[{"id": "gone", "match": ["docs/deleted.md"]}])
    assert any("matches nothing" in problem and "docs/deleted.md" in problem
               for problem in doctor.problems(index))


def test_accepts_a_pattern_that_matches(tmp_path):
    index = index_for(tmp_path, rules=ALL_SEVERITIES,
                      classes=[{"id": "live", "match": ["docs/live.md"]}])
    assert list(doctor.problems(index)) == []


def test_optional_pattern_is_allowed_to_match_nothing(tmp_path):
    """Imported content that is absent today should already be exempt on the
    day it reappears, rather than after someone hand-edits it."""
    index = index_for(tmp_path, rules=ALL_SEVERITIES,
                      classes=[{"id": "guard", "match": ["?docs/**/wiki/**"]}])
    assert list(doctor.problems(index)) == []


def test_a_live_literal_prefix_satisfies_a_pattern(tmp_path):
    """os.walk does not follow symlinked directories, and the versioned API
    trees are reached through committed `latest` symlinks, so membership of the
    walked file set cannot be the only evidence a pattern is live."""
    index = index_for(tmp_path, rules=ALL_SEVERITIES,
                      classes=[{"id": "api", "match": ["docs/api/*/latest/**"]}])
    (tmp_path / "docs" / "api").mkdir()
    assert list(doctor.problems(index)) == []


def test_reports_a_severity_for_an_unknown_rule(tmp_path):
    index = index_for(tmp_path, rules={**ALL_SEVERITIES, "T-MENU": "error"},
                      classes=[{"id": "live", "match": ["docs/live.md"]}])
    assert any("unknown rule: T-MENU" in problem for problem in doctor.problems(index))


def test_reports_a_rule_with_no_severity(tmp_path):
    index = index_for(tmp_path, rules={}, classes=[])
    problems = list(doctor.problems(index))
    assert any("no severity" in problem for problem in problems)


def test_reports_a_class_fully_shadowed_by_an_earlier_one(tmp_path):
    """First match wins, so a later class covering only paths an earlier class
    already claims can never take effect."""
    index = index_for(tmp_path, rules=ALL_SEVERITIES, classes=[
        {"id": "broad", "match": ["docs/**"]},
        {"id": "narrow", "match": ["docs/live.md"]},
    ])
    assert any("shadowed" in problem for problem in doctor.problems(index))


def test_real_repository_configuration_is_healthy():
    assert list(doctor.problems(DocsIndex())) == []


def test_legacy_directory_that_still_exists_is_not_reported(tmp_path):
    """The list is only misleading once the directory it names is gone."""
    (tmp_path / "docs" / "HAL").mkdir(parents=True, exist_ok=True)
    (tmp_path / "docs" / "HAL" / "page.md").write_text("# P\n", encoding="utf-8")
    index = index_for(tmp_path, naming={"legacy_directories": ["HAL"]})
    assert not [p for p in doctor.problems(index) if "legacy_directories" in p]


def test_legacy_directory_that_is_gone_is_reported(tmp_path):
    """A renamed or deleted directory leaves an entry that exempts nothing.

    Left alone it keeps widening what N-KEBAB-DIR accepts while reading like
    documentation of a decision that no longer applies.
    """
    index = index_for(tmp_path, naming={"legacy_directories": ["GoneForGood"]})
    reported = [p for p in doctor.problems(index) if "legacy_directories" in p]
    assert len(reported) == 1
    assert "GoneForGood" in reported[0]
