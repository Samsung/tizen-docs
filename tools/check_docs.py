#!/usr/bin/env python3
"""Validate public Tizen Docs Markdown files.

Run from anywhere in the repository:
  python3 tools/check_docs.py --changed-only --base origin/master
  python3 tools/check_docs.py path/to/document.md [path/to/toc_all.md]
  python3 tools/check_docs.py --all

This file is a permanent entry point: the command above is documented in
README.md, AGENTS.md and .claude/skills/tizen-docs/SKILL.md. The implementation
lives in tools/tizendocs/.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from tizendocs.cli import main  # noqa: E402  (import needs the path above)

if __name__ == "__main__":
    sys.exit(main())
