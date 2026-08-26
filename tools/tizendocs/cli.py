"""Command-line entry point.

The canonical invocation is referenced verbatim in README.md, AGENTS.md and
.claude/skills/tizen-docs/SKILL.md, so its flags must never change:

    python3 tools/check_docs.py --changed-only --base origin/master
"""
import argparse
import sys

from . import checks, git, paths, report
from .index import DocsIndex


def build_parser():
    parser = argparse.ArgumentParser(
        prog="check_docs.py", description="Validate public Tizen Docs Markdown.")
    parser.add_argument("paths", nargs="*")
    parser.add_argument("--changed-only", action="store_true",
                        help="derive paths from git instead of the command line")
    parser.add_argument("--base", default="origin/master",
                        help="diff base for --changed-only (default: origin/master)")
    parser.add_argument("--all", action="store_true",
                        help="check every hand-written document in the corpus")
    parser.add_argument("--format", default="text", choices=sorted(report.FORMATS),
                        help="output format (default: text)")
    return parser


def select_paths(args, index):
    if args.all:
        return sorted(path for path in index.files
                      if path.endswith(".md") and not index.generated(path))
    if args.paths:
        return [paths.normalize(path, index.root) for path in args.paths]
    if args.changed_only:
        return git.changed_files(args.base, index.root)
    return None


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    index = DocsIndex()
    selected = select_paths(args, index)
    if selected is None:
        parser.error("supply paths or use --changed-only")

    findings = [finding for path in selected for finding in checks.run(index, path)]
    output = report.FORMATS[args.format](findings)
    if output:
        sys.stdout.write(output)
    return 1 if any(finding.is_error for finding in findings) else 0
