"""Known findings that are accepted for now.

A rule can only be an ERROR gate if the corpus satisfies it, and some do not
yet. The choice is between leaving the rule off - in which case new instances
land unnoticed - and recording the existing ones so the rule can be switched
on immediately. This is the second option.

Entries are matched without line numbers, so editing a paragraph above a
finding does not silently un-baseline it. A baselined finding is reported as
WARN and does not fail the run; anything not listed still fails. An entry that
no longer reproduces is itself an error, because a stale baseline is how a
regression hides - but only in a whole-corpus run, since a scoped run simply
did not look at the file.
"""
import os

from .findings import WARN, Finding

DEFAULT = "tools/docscheck-baseline.txt"


def key(finding):
    return f"{finding.rule}\t{finding.path}\t{finding.message}"


def load(path):
    entries, comments = [], []
    if not os.path.isfile(path):
        return entries, comments
    with open(path, encoding="utf-8") as handle:
        for line in handle:
            line = line.rstrip("\n")
            if not line.strip():
                continue
            if line.startswith("#"):
                comments.append(line)
                continue
            entries.append(line)
    return entries, comments


def apply(findings, entries):
    """Return ``(findings, unmatched)`` with baselined findings demoted."""
    remaining = dict.fromkeys(entries, 0)
    out = []
    for finding in findings:
        identifier = key(finding)
        if identifier in remaining:
            remaining[identifier] += 1
            out.append(Finding(
                WARN, finding.rule, finding.path,
                f"{finding.message}  [baselined]", finding.line, finding.col,
                finding.fix, finding.syntax, finding.cause, finding.related,
                finding.data))
        else:
            out.append(finding)
    unmatched = [entry for entry, hits in remaining.items() if hits == 0]
    return out, unmatched


def render(findings, header):
    lines = list(header)
    lines.extend(sorted(key(finding) for finding in findings))
    return "\n".join(lines) + "\n"
