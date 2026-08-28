"""The machine-readable formats.

Fields are asserted individually because each exists for a consumer that
cannot derive it: line/col for inline comments, fix for one-click suggestions,
syntax to explain why a reviewer's grep missed it, cause to group every
consequence of one deletion.
"""
import json

from tizendocs.findings import ERROR, WARN, Finding
from tizendocs.report import github, jsonl, sarif

BROKEN = Finding(ERROR, "L-DEPTH", "docs/a.md", "target does not exist: ../m/x.mp4",
                 line=41, col=7, fix="m/x.mp4", syntax="html-source")
ORPHANED = Finding(WARN, "M-ORPHAN", "docs/m/y.png", "not referenced by any document")


def test_jsonl_is_one_object_per_line():
    lines = jsonl.render([BROKEN, ORPHANED]).splitlines()
    assert len(lines) == 2
    first = json.loads(lines[0])
    assert first["line"] == 41 and first["col"] == 7
    assert first["fix"] == "m/x.mp4"
    assert first["syntax"] == "html-source"


def test_jsonl_includes_structured_finding_data():
    finding = Finding(WARN, "T-ORPHAN", "docs/a.md", "unlisted",
                      data={"governing_tocs": ["docs/toc.md"],
                            "inbound_links": 2})
    record = json.loads(jsonl.render([finding]))
    assert record["governing_tocs"] == ["docs/toc.md"]
    assert record["inbound_links"] == 2


def test_jsonl_omits_empty_optional_fields():
    record = json.loads(jsonl.render([ORPHANED]).strip())
    assert "line" not in record and "fix" not in record and "cause" not in record


def test_github_annotations_carry_position_and_fix():
    line = github.render([BROKEN]).strip()
    assert line.startswith("::error file=docs/a.md,line=41,col=7,title=L-DEPTH::")
    assert "(fix: m/x.mp4)" in line


def test_github_maps_warn_to_warning():
    assert github.render([ORPHANED]).startswith("::warning ")


def test_sarif_is_valid_json_with_rules_and_results():
    document = json.loads(sarif.render([BROKEN, ORPHANED]))
    run = document["runs"][0]
    assert [rule["id"] for rule in run["tool"]["driver"]["rules"]] == ["L-DEPTH", "M-ORPHAN"]
    assert run["results"][0]["locations"][0]["physicalLocation"]["region"]["startLine"] == 41
    assert run["results"][1]["level"] == "warning"


def test_sarif_fingerprint_ignores_line_numbers():
    """So an unrelated edit above a finding does not invalidate a suppression."""
    moved = Finding(BROKEN.level, BROKEN.rule, BROKEN.path, BROKEN.message, line=999)
    assert sarif.fingerprint(moved) == sarif.fingerprint(BROKEN)


def test_sarif_relates_a_finding_to_its_cause():
    caused = Finding(ERROR, "R-INBOUND", "docs/b.md", "references a deleted path",
                     line=3, cause="docs/gone.md")
    result = json.loads(sarif.render([caused]))["runs"][0]["results"][0]
    assert result["relatedLocations"][0]["physicalLocation"]["artifactLocation"]["uri"] \
        == "docs/gone.md"
