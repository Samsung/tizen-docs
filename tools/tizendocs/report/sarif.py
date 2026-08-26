"""SARIF 2.1.0.

The recommended structured format if this is ever wired into CI. GitHub code
scanning ingests it directly, rules carry a helpUri so each finding can link to
the guide that motivates it, and relatedLocations can express "this finding is
here because *that* file changed" - which the reverse-direction rules need and
the other formats cannot represent.
"""
import json

HELP = "https://github.com/Samsung/tizen-docs/blob/master/reviewguide/review_points_guide.md"
LEVELS = {"ERROR": "error", "WARN": "warning", "NOTE": "note"}


def _location(path, line, col):
    region = {"startLine": line or 1}
    if col:
        region["startColumn"] = col
    return {"physicalLocation": {
        "artifactLocation": {"uri": path},
        "region": region}}


def render(findings, summary=None):
    rules = {}
    results = []
    for finding in findings:
        rules.setdefault(finding.rule, {
            "id": finding.rule,
            "shortDescription": {"text": finding.rule},
            "helpUri": HELP,
            "defaultConfiguration": {"level": LEVELS[finding.level]},
        })
        result = {
            "ruleId": finding.rule,
            "level": LEVELS[finding.level],
            "message": {"text": finding.message},
            "locations": [_location(finding.path, finding.line, finding.col)],
            "partialFingerprints": {"docscheck/v1": fingerprint(finding)},
        }
        if finding.cause:
            result["relatedLocations"] = [_location(finding.cause, 0, 0)]
        if finding.fix:
            result["fixes"] = [{"description": {"text": f"Use {finding.fix}"}}]
        results.append(result)
    document = {
        "version": "2.1.0",
        "$schema": "https://json.schemastore.org/sarif-2.1.0.json",
        "runs": [{
            "tool": {"driver": {
                "name": "check_docs",
                "informationUri": "https://github.com/Samsung/tizen-docs",
                "rules": [rules[key] for key in sorted(rules)]}},
            "results": results,
        }],
    }
    return json.dumps(document, indent=2) + "\n"


def fingerprint(finding):
    """Stable across unrelated edits: deliberately excludes the line number."""
    return f"{finding.rule}:{finding.path}:{finding.message}"
