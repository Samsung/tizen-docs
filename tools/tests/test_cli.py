"""CLI behaviour, including the failure modes the previous version had."""
import subprocess
import sys

import pytest

from conftest import TOOLS

SHIM = TOOLS / "check_docs.py"
REPO = TOOLS.parent


def run(*argv, cwd=REPO):
    return subprocess.run([sys.executable, str(SHIM), *argv],
                          capture_output=True, text=True, cwd=str(cwd))


def test_no_arguments_is_an_error():
    result = run()
    assert result.returncode == 2
    assert "supply paths or use --changed-only" in result.stderr


def findings_only(stdout):
    """Drop the summary line, whose elapsed time is not reproducible."""
    return [line for line in stdout.splitlines() if not line.startswith("check_docs:")]


def test_all_reports_the_same_from_any_directory():
    """The old code hardcoded a relative docs/ path, so running it from inside
    docs/ silently checked nothing and exited 0."""
    from_root = run("--all")
    from_docs = run("--all", cwd=REPO / "docs")
    assert findings_only(from_root.stdout) == findings_only(from_docs.stdout)
    assert findings_only(from_docs.stdout) != []


def test_a_summary_is_always_printed():
    """Silence used to be ambiguous: an unresolvable --base produced no output
    and exit 0, so a reader could not tell "passed" from "did not run"."""
    result = run("--changed-only", "--base", "HEAD")
    assert result.stdout.splitlines()[-1].startswith("check_docs: ")


def test_every_format_produces_output():
    for name in ("text", "jsonl", "sarif", "github"):
        result = run("--all", "--format", name)
        assert result.stdout.strip(), name
        assert result.returncode == 1, name


def test_relative_path_from_a_subdirectory_resolves():
    result = run("overview/overview.md", cwd=REPO / "docs/application/flutter")
    assert "docs/application/flutter/overview/overview.md" in result.stdout


@pytest.mark.parametrize("flag", ["--format"])
def test_unknown_format_is_rejected(flag):
    assert run(flag, "yaml", "--all").returncode == 2
