"""Human-readable report.

Keeps the historical ``LEVEL RULE path: message`` shape so existing greps and
habits survive, and adds ``:line`` plus an indented fix hint.
"""


def render(findings, summary=None):
    lines = []
    for finding in findings:
        lines.append(f"{finding.level} {finding.rule} {finding.location}: {finding.message}")
        if finding.fix:
            lines.append(f"  fix: {finding.fix}")
        for note in finding.related:
            lines.append(f"  └─ {note}")
    if summary:
        lines.append(summary)
    return "".join(line + "\n" for line in lines)
