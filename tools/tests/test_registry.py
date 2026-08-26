"""Meta-tests that make a rule impossible to land untested.

The failure mode these guard against is a check that can never fire - a
regex that silently stops matching, or a rule wired up but never reached.
Asserting exit codes alone cannot catch that, so instead we assert that every
registered rule has a fixture proving it fires, and a fixture proving it does
not fire on clean content.
"""
import pytest

from conftest import fixture_names, ids, reverse_scenarios, run_tree
from tizendocs import checks


def expected_ids(root):
    path = root / "expected.txt"
    if not path.exists():
        return []
    return sorted(
        tuple(line.split(" ", 1))
        for line in path.read_text(encoding="utf-8").split("\n") if line.strip())


def test_every_rule_has_a_fixture_that_fires(fixtures, git_tree):
    """A new rule with no failing fixture must fail this suite.

    Covers both registries: per-document rules come from the fixture trees,
    change-scoped rules from a real repository with a deletion in it.
    """
    fired = set()
    for name in fixture_names():
        fired.update(rule for rule, _ in ids(run_tree(fixtures / name)))

    fired.update(finding.rule for finding in reverse_scenarios(git_tree))

    missing = sorted(set(checks.RULE_IDS) - fired)
    assert not missing, f"rules with no fixture that triggers them: {missing}"


def test_no_fixture_fires_an_unregistered_rule(fixtures):
    registered = set(checks.RULE_IDS)
    for name in fixture_names():
        for rule, _ in ids(run_tree(fixtures / name)):
            assert rule in registered, f"{name} emitted unregistered rule {rule}"


def test_minimal_tree_is_clean(fixtures):
    """The inverse guard: a rule that always fires must fail here."""
    assert ids(run_tree(fixtures / "minimal")) == []


@pytest.mark.parametrize("name", [n for n in fixture_names() if n != "minimal"])
def test_fixture_matches_expected_findings(fixtures, name):
    root = fixtures / name
    assert sorted(ids(run_tree(root))) == expected_ids(root)
