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
    docs/ silently checked nothing and exited 0.

    Compares the file count rather than findings, so this keeps working now
    that the corpus is clean.
    """
    from_root = run("--all")
    from_docs = run("--all", cwd=REPO / "docs")
    assert findings_only(from_root.stdout) == findings_only(from_docs.stdout)
    count = from_root.stdout.rsplit("(", 1)[1].split(" files")[0]
    assert int(count) > 900
    assert f"({count} files" in from_docs.stdout


def test_a_summary_is_always_printed():
    """Silence used to be ambiguous: an unresolvable --base produced no output
    and exit 0, so a reader could not tell "passed" from "did not run"."""
    result = run("--changed-only", "--base", "HEAD")
    assert result.stdout.splitlines()[-1].startswith("check_docs: ")


def test_every_format_is_accepted_and_well_formed():
    """Rendering of individual findings is asserted in test_formats.py; this
    checks the CLI wiring on the real corpus.

    The corpus is error-free, not finding-free: docscheck-baseline.txt accepts
    three P-ROUTE findings that belong to a generator upstream. Asserting empty
    output would make this test fail the moment a rule is switched on the way
    the baseline exists to allow, so it asserts the property that matters —
    nothing is reported as an error.
    """
    import json

    text = run("--all", "--format", "text")
    assert text.returncode == 0
    assert text.stdout.strip().splitlines()[-1].startswith("check_docs: 0 ERROR")

    lines = run("--all", "--format", "jsonl")
    assert lines.returncode == 0
    assert all(json.loads(line)["level"] != "ERROR"
               for line in lines.stdout.splitlines() if line.strip())

    assert "::error" not in run("--all", "--format", "github").stdout

    document = json.loads(run("--all", "--format", "sarif").stdout)
    assert document["version"] == "2.1.0"
    assert all(result.get("level") != "error"
               for result in document["runs"][0]["results"])


def test_a_clean_corpus_exits_zero():
    result = run("--all")
    assert result.returncode == 0
    assert result.stdout.strip().endswith(")")
    assert "0 ERROR" in result.stdout


def test_relative_path_from_a_subdirectory_resolves():
    """The summary names the file count, which proves the path was found."""
    result = run("overview/overview.md", cwd=REPO / "docs/application/flutter")
    assert "check_docs: " in result.stdout
    assert "(1 files" in result.stdout


@pytest.mark.parametrize("flag", ["--format"])
def test_unknown_format_is_rejected(flag):
    assert run(flag, "yaml", "--all").returncode == 2


def test_write_baseline_refuses_a_scoped_run():
    """A scoped run looked at a handful of files.

    Writing its findings would drop every entry it never examined, turning the
    baseline from a record of accepted findings into a way of losing them. The
    flag was declared and never implemented, so before this it silently did
    nothing at all — which is the same failure wearing a friendlier face.
    """
    result = run("--write-baseline", "docs/application/dotnet/overview.md")
    assert result.returncode == 2
    assert "--write-baseline needs --all" in result.stderr


def test_write_baseline_records_the_open_errors(tmp_path):
    """Round trip: what the flag writes is what makes the run clean."""
    target = tmp_path / "baseline.txt"
    written = run("--all", "--write-baseline", "--baseline", str(target))
    assert written.returncode == 0

    entries = [line for line in target.read_text(encoding="utf-8").splitlines()
               if line and not line.startswith("#")]
    assert entries, "the corpus has open P-ROUTE findings to record"
    assert all(len(line.split("\t")) == 3 for line in entries)

    after = run("--all", "--baseline", str(target), "--format", "text")
    assert after.returncode == 0
    assert after.stdout.strip().splitlines()[-1].startswith("check_docs: 0 ERROR")
