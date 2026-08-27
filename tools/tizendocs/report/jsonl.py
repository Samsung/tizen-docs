"""One JSON object per line: the format agents consume.

Line-delimited so it streams and truncates safely, and so `jq` works without
loading the whole report.
"""
import json


def render(findings, summary=None):
    return "".join(
        json.dumps(finding.as_dict(), sort_keys=True) + "\n" for finding in findings)
