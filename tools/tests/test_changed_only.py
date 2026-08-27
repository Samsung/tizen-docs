"""--changed-only over a real git repository.

Covers all four diff states. The deletion case is the one the toolkit exists
to fix: a removed page breaks links in files the change never touched, and
--changed-only cannot see that until the reverse-direction rules land.
"""
from tizendocs import git

SEED = {
    "docs/toc_all.md": "# Guides\n## [Kept](/kept.md)\n## [Doomed](/doomed.md)\n",
    "docs/kept.md": "# Kept\n\nA link to [doomed](doomed.md).\n",
    "docs/doomed.md": "# Doomed\n",
}


def test_added_file_is_reported(git_tree):
    root, run = git_tree(SEED)
    (root / "docs" / "Added_File.md").write_text("# Added file\n", encoding="utf-8")
    run("add", "-A")
    run("commit", "-q", "-m", "add")
    assert "docs/Added_File.md" in git.changed_files("main~1", str(root))


def test_modified_file_is_reported(git_tree):
    root, run = git_tree(SEED)
    (root / "docs" / "kept.md").write_text("# Kept\n\nEdited.\n", encoding="utf-8")
    assert "docs/kept.md" in git.changed_files("HEAD", str(root))


def test_uncommitted_work_is_reported(git_tree):
    """The two-dot diff exists so a dirty tree is checked before committing."""
    root, _ = git_tree(SEED)
    (root / "docs" / "kept.md").write_text("# Kept\n\nUncommitted.\n", encoding="utf-8")
    assert "docs/kept.md" in git.changed_files("HEAD", str(root))


def test_deleted_path_appears_in_the_change_set(git_tree):
    root, run = git_tree(SEED)
    run("rm", "-q", "docs/doomed.md")
    run("commit", "-q", "-m", "delete")
    assert "docs/doomed.md" in git.changed_files("main~1", str(root))


def test_deleting_a_page_reports_the_links_it_breaks(git_tree):
    """docs/kept.md and docs/toc_all.md still point at the deleted page, and
    neither is in the change set.

    This is the case the per-document rules are structurally unable to see:
    they inspect the links going *out* of changed files. It is covered by the
    change-scoped rules instead, and it is why they exist.
    """
    from conftest import run_change
    root, run = git_tree(SEED)
    run("rm", "-q", "docs/doomed.md")
    run("commit", "-q", "-m", "delete")
    findings = run_change(root, "HEAD~1")
    assert {(f.rule, f.path) for f in findings} == {
        ("R-INBOUND", "docs/kept.md"),
        ("R-TOC", "docs/toc_all.md"),
    }


def test_change_scoped_per_document_rules_see_nothing_here(git_tree):
    """The contrast, kept so the gap cannot silently reopen.

    A whole-corpus run would report these as L-BROKEN. The gap is specific to
    change scoping, which is the mode contributors are told to use: the only
    changed path is the deleted file, and running the per-document rules over
    it yields nothing at all.
    """
    from conftest import checks_for
    root, run = git_tree(SEED)
    run("rm", "-q", "docs/doomed.md")
    run("commit", "-q", "-m", "delete")
    changed = git.changed_files("HEAD~1", str(root))
    assert changed == ["docs/doomed.md"]
    assert checks_for(root, changed) == []
