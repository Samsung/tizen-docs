"""The optional style adapter.

Style is out of scope as a gate and will stay that way. The corpus carries
about 8,400 violations of six markdownlint rules - 5,079 hard tabs, 1,454
trailing-whitespace lines, 804 unlanguaged code fences - so a corpus-wide style
gate is arithmetically impossible to satisfy and would only ever be switched
off. Filtered to the lines a change actually touches, the same rules are
useful.

Everything here is NOTE level and cannot affect the exit code. markdownlint is
invoked through `npx --no-install`, so a machine without it gets one note
rather than a failure: the exit code stays a function of the standard-library
checks alone, and no npm problem can break the gate.
"""
import json
import os
import re
import subprocess

from .findings import NOTE, Finding

RULE_PREFIX = "S-"

#: The six rules worth reporting, and what each maps to.
RULES = {
    "MD003": "S-SETEXT", "MD004": "S-BULLET", "MD009": "S-TRAIL",
    "MD010": "S-TAB", "MD040": "S-FENCE", "MD047": "S-EOF",
}

RULE_IDS = tuple(sorted(set(RULES.values())))


def config_document():
    """The markdownlint-cli2 configuration, derived from RULES."""
    body = {"default": False, **{name: True for name in sorted(RULES)}}
    return json.dumps({"config": body, "globs": ["docs/**/*.md"]}, indent=2) + "\n"


def available():
    try:
        result = subprocess.run(
            ("npx", "--no-install", "markdownlint-cli2", "--version"),
            capture_output=True, text=True, timeout=60)
    except (OSError, subprocess.SubprocessError):
        return False
    return result.returncode == 0


def run(index, paths, changed_lines=None):
    """Yield NOTE findings for *paths*, optionally limited to changed lines."""
    if not paths:
        return
    if not available():
        yield Finding(NOTE, "S-UNAVAILABLE", "tools/docscheck.toml",
                      "markdownlint-cli2 is not installed, so style notes were "
                      "skipped; install it with `npm i -g markdownlint-cli2` or "
                      "ignore this line")
        return
    environment = {**os.environ, "MARKDOWNLINT_CONFIG": ""}
    result = subprocess.run(
        ("npx", "--no-install", "markdownlint-cli2", *paths),
        capture_output=True, text=True, cwd=index.root, env=environment)
    for line in (result.stderr or "").splitlines():
        finding = _parse(line, changed_lines)
        if finding is not None:
            yield finding


#: markdownlint-cli2 writes "path:line rule/name message" or
#: "path:line:col rule/name message" to stderr.
REPORT = re.compile(
    r"^(?P<path>[^:]+):(?P<line>\d+)(?::(?P<col>\d+))?\s+"
    r"(?P<code>MD\d+)(?:/\S+)?\s*(?P<message>.*)$")


def _parse(line, changed_lines):
    """Turn one markdownlint-cli2 stderr line into a finding."""
    match = REPORT.match(line.strip())
    if match is None:
        return None
    rule = RULES.get(match.group("code"))
    if rule is None:
        return None
    path, number = match.group("path"), int(match.group("line"))
    if changed_lines is not None and number not in changed_lines.get(path, set()):
        return None
    return Finding(NOTE, rule, path, match.group("message").strip(),
                   line=number, col=int(match.group("col") or 0))
