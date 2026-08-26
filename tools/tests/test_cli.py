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


def test_all_reports_the_same_from_any_directory():
    """The old code hardcoded a relative docs/ path, so running it from inside
    docs/ silently checked nothing and exited 0."""
    from_root = run("--all")
    from_docs = run("--all", cwd=REPO / "docs")
    assert from_root.stdout == from_docs.stdout
    assert from_docs.stdout != ""


def test_relative_path_from_a_subdirectory_resolves():
    result = run("overview/overview.md", cwd=REPO / "docs/application/flutter")
    assert "docs/application/flutter/overview/overview.md" in result.stdout


@pytest.mark.parametrize("flag", ["--format"])
def test_unknown_format_is_rejected(flag):
    assert run(flag, "yaml", "--all").returncode == 2
