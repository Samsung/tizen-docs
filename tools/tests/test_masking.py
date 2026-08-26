"""Code masking must not shift offsets or hide live content.

Regression test for a real bug caught during development: relaxing the closing
fence pattern to allow trailing text made an *opening* fence with a language
tag pair as a *closing* fence. Everything after it was masked, which silently
hid an <a name="..."> anchor and produced a false L-ANCHOR on live content.
A finding count assertion alone would not have explained it.
"""
import pytest

from conftest import FIXTURES, TOOLS, ids, run_tree
from tizendocs.markdown import Source

FENCES = FIXTURES / "code-masking" / "docs" / "fences.md"


def test_masking_preserves_length_and_line_breaks():
    raw = FENCES.read_text(encoding="utf-8")
    source = Source(raw)
    assert len(source.text) == len(raw)
    assert source.text.count("\n") == raw.count("\n")


def test_language_tagged_opening_fence_is_not_a_closing_fence():
    """The anchor sits after two ```csharp blocks and must stay visible."""
    source = Source(FENCES.read_text(encoding="utf-8"))
    assert "encode" in source.anchors()


def test_content_inside_a_fence_is_not_linkified():
    source = Source(FENCES.read_text(encoding="utf-8"))
    urls = [url for _, url, _ in source.references()]
    assert "nowhere.md" not in urls
    assert "#encode" in urls


def test_headings_inside_a_fence_are_ignored():
    source = Source(FENCES.read_text(encoding="utf-8"))
    titles = [match.group(2) for match in source.headings()]
    assert titles == ["Fences", "Encode", "Later heading"]


def test_fixture_is_clean():
    assert ids(run_tree(FIXTURES / "code-masking")) == []


@pytest.mark.corpus
def test_corpus_offsets_never_drift():
    """Every reported line number in the real corpus is trustworthy only if
    masking is length-preserving everywhere."""
    drifted = []
    for path in (TOOLS.parent / "docs").rglob("*.md"):
        raw = path.read_text(encoding="utf-8", errors="replace")
        source = Source(raw)
        if len(source.text) != len(raw) or source.text.count("\n") != raw.count("\n"):
            drifted.append(str(path))
    assert drifted == []
