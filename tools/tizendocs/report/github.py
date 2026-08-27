"""GitHub Actions workflow commands.

No dependencies and about twenty lines, kept as the cheapest possible path to
inline annotations if this is ever wired into CI.
"""
LEVELS = {"ERROR": "error", "WARN": "warning", "NOTE": "notice"}


def render(findings, summary=None):
    lines = []
    for finding in findings:
        parts = [f"file={finding.path}"]
        if finding.line:
            parts.append(f"line={finding.line}")
            parts.append(f"col={finding.col}")
        parts.append(f"title={finding.rule}")
        message = finding.message
        if finding.fix:
            message = f"{message} (fix: {finding.fix})"
        lines.append(f"::{LEVELS[finding.level]} {','.join(parts)}::{message}")
    return "".join(line + "\n" for line in lines)
