#!/usr/bin/env python3
"""Rewrite tools/tests/corpus-expected.json from the current tree."""
import collections
import json
import os
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))

from conftest import TOOLS, run_tree  # noqa: E402

root = TOOLS.parent
counts = collections.Counter(f.rule for f in run_tree(root))
commit = subprocess.run(("git", "-C", str(root), "rev-parse", "--short", "HEAD"),
                        capture_output=True, text=True).stdout.strip()
payload = {"commit": commit, "counts": dict(sorted(counts.items()))}
(HERE / "corpus-expected.json").write_text(
    json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
