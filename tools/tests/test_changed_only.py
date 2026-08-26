"""--changed-only over a real git repository.

Covers all four diff states. The deletion case is the one the toolkit exists
to fix: a removed page breaks links in files the change never touched, and
--changed-only cannot see that until the reverse-direction rules land.
"""
import pytest

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


@pytest.mark.xfail(reason="closed by R-INBOUND/R-TOC; see the toolkit plan", strict=True)
def test_deleting_a_page_reports_the_links_it_breaks(git_tree):
    """docs/kept.md and docs/toc_all.md still point at the deleted page.

    Neither file is in the change set, so no current rule can see them.
    """
    from conftest import ids, run_tree
    root, run = git_tree(SEED)
    run("rm", "-q", "docs/doomed.md")
    run("commit", "-q", "-m", "delete")
    rules = {rule for rule, _ in ids(run_tree(root))}
    assert rules & {"R-INBOUND", "R-TOC"}
