"""The optional style adapter and the generated ignore file.

Style is a NOTE-only advisory and must never affect the exit code: the corpus
carries about 8,400 violations of these six rules, so a gate is arithmetically
impossible to satisfy and would be switched off within a week.
"""
import json
import subprocess
import sys

from conftest import TOOLS, real_config
from tizendocs import export, style
from tizendocs.findings import NOTE
from tizendocs.index import DocsIndex

SHIM = TOOLS / "check_docs.py"
REPO = TOOLS.parent


def test_only_six_rules_are_reported():
    assert set(style.RULES) == {"MD003", "MD004", "MD009", "MD010", "MD040", "MD047"}
    body = json.loads(style.config_document())["config"]
    assert body["default"] is False
    assert all(body[name] for name in style.RULES)


def test_every_style_finding_is_a_note():
    finding = style._parse("docs/a.md:3 MD010/no-hard-tabs Hard tabs", None)
    assert finding.level == NOTE
    assert finding.rule == "S-TAB"
    assert finding.line == 3


def test_a_rule_outside_the_six_is_ignored():
    assert style._parse("docs/a.md:3 MD013/line-length Line too long", None) is None


def test_notes_are_filtered_to_changed_lines():
    """Reporting a pre-existing hard tab because someone edited the paragraph
    below it is how a rule earns a reputation for noise."""
    line = "docs/a.md:3 MD010/no-hard-tabs Hard tabs"
    assert style._parse(line, {"docs/a.md": {3}}) is not None
    assert style._parse(line, {"docs/a.md": {9}}) is None


def test_missing_markdownlint_yields_a_note_not_a_failure():
    index = DocsIndex(root=str(REPO), config=real_config())
    if style.available():
        return
    findings = list(style.run(index, ["docs/trademarks.md"]))
    assert [f.level for f in findings] == [NOTE]


def test_style_never_changes_the_exit_code():
    plain = subprocess.run([sys.executable, str(SHIM), "--all"],
                           capture_output=True, text=True, cwd=str(REPO))
    styled = subprocess.run([sys.executable, str(SHIM), "--all", "--style"],
                            capture_output=True, text=True, cwd=str(REPO))
    assert plain.returncode == styled.returncode


def test_generated_ignore_file_matches_the_configuration():
    """Committed and derived, so it cannot become a second source of truth."""
    index = DocsIndex(root=str(REPO), config=real_config())
    generated = export.markdownlint(index)
    on_disk = (REPO / ".markdownlint-cli2.jsonc").read_text(encoding="utf-8")
    assert on_disk == generated


def test_generated_file_says_it_is_generated():
    index = DocsIndex(root=str(REPO), config=real_config())
    assert export.markdownlint(index).startswith("// GENERATED from")
