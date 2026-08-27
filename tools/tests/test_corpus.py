"""Regression guard against the real corpus.

This is the precision guard: a change that starts emitting false positives
shows up here as a number moving, reviewed in the diff rather than discovered
by a contributor whose clean pull request suddenly fails.

Refresh with:  python3 tools/tests/refresh_corpus_expectation.py
"""
import collections
import json
import pathlib

import pytest

from conftest import TOOLS, run_tree

EXPECTATION = pathlib.Path(__file__).resolve().parent / "corpus-expected.json"


@pytest.mark.corpus
def test_corpus_findings_match_expectation():
    counts = collections.Counter(f.rule for f in run_tree(TOOLS.parent))
    expected = json.loads(EXPECTATION.read_text(encoding="utf-8"))
    assert dict(counts) == expected["counts"]
