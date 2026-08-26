"""Shared fixtures.

Production code is standard-library only; pytest is a development dependency.
"""
import os
import pathlib
import subprocess
import sys

import pytest

TOOLS = pathlib.Path(__file__).resolve().parent.parent
FIXTURES = pathlib.Path(__file__).resolve().parent / "fixtures"
sys.path.insert(0, str(TOOLS))

from tizendocs import checks  # noqa: E402
from tizendocs.index import DocsIndex  # noqa: E402
from tizendocs.report import text  # noqa: E402


def run_tree(root):
    """Run every rule over every Markdown file in *root* and return findings."""
    index = DocsIndex(root=str(root))
    documents = sorted(path for path in index.files if path.endswith(".md"))
    return [finding for path in documents for finding in checks.run(index, path)]


def ids(findings):
    """Findings as ``(rule, path)`` tuples, for precise assertions."""
    return [(f.rule, f.path) for f in findings]


def rendered(findings):
    return text.render(findings)


@pytest.fixture
def fixtures():
    return FIXTURES


def fixture_names():
    return sorted(p.name for p in FIXTURES.iterdir() if (p / "docs").is_dir())


@pytest.fixture
def git_tree(tmp_path):
    """A real git repository containing a docs/ tree, for --changed-only tests.

    Global and system git config are neutralised: a contributor's own
    commit.gpgsign or core.hooksPath would otherwise make this suite fail or
    hang on their machine only.
    """
    def build(files):
        root = tmp_path / "repo"
        (root / "docs").mkdir(parents=True)
        (root / "tools").mkdir()
        for name, body in files.items():
            target = root / name
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(body, encoding="utf-8")
        env = {
            **os.environ,
            "GIT_CONFIG_GLOBAL": os.devnull,
            "GIT_CONFIG_SYSTEM": os.devnull,
            "GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@example.invalid",
            "GIT_COMMITTER_NAME": "t", "GIT_COMMITTER_EMAIL": "t@example.invalid",
        }

        def run(*argv):
            return subprocess.run(
                ("git", "-C", str(root), "-c", "commit.gpgsign=false",
                 "-c", f"core.hooksPath={os.devnull}") + argv,
                capture_output=True, text=True, env=env, check=True)

        run("init", "-q", "-b", "main")
        run("add", "-A")
        run("commit", "-q", "-m", "seed")
        return root, run

    return build
