"""The reverse-direction rules: what a removal breaks elsewhere.

These are the rules the toolkit exists for. --changed-only inspects the links
going out of changed files, so it is structurally blind to the links coming in
to a deleted one - and the previous implementation compounded that by skipping
deleted paths before any check ran.
"""
import pytest

from conftest import REVERSE_SEED, run_change


def observed(git_tree, action):
    root, run = git_tree(REVERSE_SEED)
    action(root, run)
    return run_change(root, "HEAD~1")


def delete(root, run):
    run("rm", "-q", "docs/doomed.md")
    run("commit", "-q", "-m", "delete")


def rename(root, run):
    run("mv", "docs/doomed.md", "docs/renamed.md")
    run("commit", "-q", "-m", "rename")


def test_deletion_reports_every_surviving_reference(git_tree):
    findings = observed(git_tree, delete)
    assert {(f.rule, f.path, f.line) for f in findings
            if f.rule in {"R-INBOUND", "R-TOC"}} == {
        ("R-INBOUND", "docs/kept.md", 3),
        ("R-INBOUND", "docs/also.md", 3),
        ("R-TOC", "docs/toc_all.md", 3),
    }


def test_html_references_are_found_too(git_tree):
    """docs/also.md links via <a href>. Parsing only Markdown missed this
    class entirely, which is how a real deletion left five dangling HTML
    links in docs/application/dotnet/guides/index.md."""
    findings = observed(git_tree, delete)
    html = [f for f in findings if f.path == "docs/also.md"]
    assert [f.syntax for f in html] == ["html-a"]


def test_toc_entries_are_a_separate_rule(git_tree):
    """A stale TOC entry silently drops a node from site navigation; a stale
    body link is a visible 404. One id would let a reviewer fix the body links
    and consider it closed."""
    rules = {f.rule for f in observed(git_tree, delete)}
    assert rules == {"R-INBOUND", "R-TOC", "R-MEDIA"}


def test_media_used_only_by_the_deleted_page_is_reported(git_tree):
    """The removed page's own references have to be read from the base
    revision: the reverse graph is built from the working tree, where they no
    longer exist."""
    media = [f for f in observed(git_tree, delete) if f.rule == "R-MEDIA"]
    assert len(media) == 1
    assert media[0].related == ("docs/media/only-here.png",)


def test_every_link_finding_names_its_cause(git_tree):
    """So an agent can group all consequences of one removal into one comment."""
    findings = [f for f in observed(git_tree, delete)
                if f.rule in {"R-INBOUND", "R-TOC"}]
    assert {f.cause for f in findings} == {"docs/doomed.md"}


def test_deletion_offers_no_fix(git_tree):
    assert all(f.fix == "" for f in observed(git_tree, delete))


def test_removing_a_heading_reports_inbound_fragment_links(git_tree):
    """SKILL.md already promises that renaming a heading means updating
    incoming links; this is the only mechanism that could keep it."""
    root, run = git_tree(REVERSE_SEED)
    kept = root / "docs" / "kept.md"
    kept.write_text("# Kept\n\nA link to [doomed](doomed.md).\n", encoding="utf-8")
    run("add", "-A")
    run("commit", "-q", "-m", "remove a heading")
    findings = [f for f in run_change(root, "HEAD~1") if f.rule == "R-ANCHOR"]
    assert [(f.path, f.cause) for f in findings] == \
        [("docs/also.md", "docs/kept.md")]


def test_rename_suggests_the_new_path(git_tree):
    """git records renames in this repository as delete/add pairs, so -M is
    what makes a repair suggestable rather than just a complaint."""
    findings = observed(git_tree, rename)
    fixes = {(f.path, f.fix) for f in findings}
    assert fixes == {
        ("docs/kept.md", "renamed.md"),
        ("docs/also.md", "renamed.md"),
        ("docs/toc_all.md", "/renamed.md"),
    }
    assert all("renamed to docs/renamed.md" in f.message for f in findings)


def test_a_change_that_removes_nothing_reports_nothing(git_tree):
    """Why these can be ERROR from day one: they add no backlog."""
    root, run = git_tree(REVERSE_SEED)
    kept = root / "docs" / "kept.md"
    # Edit the prose but keep every heading, so nothing is removed at all.
    kept.write_text(kept.read_text(encoding="utf-8").replace("Body.", "Edited body."),
                    encoding="utf-8")
    run("add", "-A")
    run("commit", "-q", "-m", "edit")
    assert run_change(root, "HEAD~1") == []


def test_a_reference_from_a_file_also_deleted_is_not_reported(git_tree):
    """Removing a section wholesale must not report the section on itself."""
    root, run = git_tree(REVERSE_SEED)
    run("rm", "-q", "docs/doomed.md", "docs/kept.md", "docs/also.md")
    run("commit", "-q", "-m", "remove the section")
    findings = run_change(root, "HEAD~1")
    assert {f.path for f in findings if f.rule in {"R-INBOUND", "R-TOC"}} == \
        {"docs/toc_all.md"}


@pytest.mark.parametrize("case", ["PNG", "png"])
def test_case_only_differences_still_match(git_tree, case):
    """Authors on Windows write .PNG where the file is .png, and the published
    site is case-sensitive, so both spellings must resolve to one target."""
    seed = {
        "docs/toc_all.md": "# Guides\n## [Page](/page.md)\n",
        "docs/page.md": f'# Page\n\n<img src="media/shot.{case}" alt="A screenshot">\n',
        "docs/media/shot.png": "x",
    }
    root, run = git_tree(seed)
    run("rm", "-q", "docs/media/shot.png")
    run("commit", "-q", "-m", "delete the image")
    assert [f.rule for f in run_change(root, "HEAD~1")] == ["R-INBOUND"]
