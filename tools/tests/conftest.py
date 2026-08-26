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

from tizendocs import checks, config, git  # noqa: E402
from tizendocs.index import DocsIndex  # noqa: E402
from tizendocs.report import text  # noqa: E402


def real_config():
    """The repository's own docscheck.toml.

    Fixture trees carry no configuration of their own, so without this they
    would run with severities and scopes that do not exist in production - and
    a rule scoped to added files only would appear to fire on everything.
    """
    return config.load(root=str(TOOLS.parent))

#: A corpus where two documents and a TOC all point at doomed.md.
REVERSE_SEED = {
    "docs/toc_all.md": "# Guides\n## [Kept](/kept.md)\n## [Doomed](/doomed.md)\n",
    "docs/kept.md": '# Kept\n\nA link to [doomed](doomed.md).\n',
    "docs/also.md": '# Also\n\n<a href="doomed.md">doomed</a>\n',
    "docs/doomed.md": "# Doomed\n",
}


def run_change(root, base):
    """Findings the change-scoped rules produce for *root* against *base*."""
    index = DocsIndex(root=str(root), config=real_config())
    change = git.describe(base, str(root))
    return list(checks.run_change(index, change))


def checks_for(root, paths):
    """Per-document findings for an explicit path list, as --changed-only does."""
    index = DocsIndex(root=str(root), config=real_config())
    return [finding for path in paths for finding in checks.run(index, path)]


def declared_change(root):
    """A synthetic change set from a fixture's optional added.txt.

    Rules scoped to added files only need to know what is new, and a fixture
    should be able to say so without building a git repository for it.
    """
    listing = pathlib.Path(root) / "added.txt"
    if not listing.exists():
        return None
    added = [line.strip() for line in
             listing.read_text(encoding="utf-8").split("\n") if line.strip()]
    return git.Change(status={path: "A" for path in added})


def run_tree(root, change=None):
    """Run every applicable rule over *root* and return the findings.

    Covers the per-document, corpus and media registries, so a fixture proves a
    rule fires regardless of which registry it belongs to.
    """
    index = DocsIndex(root=str(root), config=real_config())
    change = change or declared_change(root)
    documents = sorted(path for path in index.files if path.endswith(".md"))
    findings = [f for path in documents for f in checks.run(index, path, change)]
    findings.extend(checks.run_corpus(index))
    findings.extend(checks.run_media(index))
    return findings


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
