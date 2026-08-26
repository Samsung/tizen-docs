"""Command-line entry point.

The canonical invocation is referenced verbatim in README.md, AGENTS.md and
.claude/skills/tizen-docs/SKILL.md, so its flags must never change:

    python3 tools/check_docs.py --changed-only --base origin/master
"""
import argparse
import sys
import time

from . import checks, git, paths, report
from .findings import ERROR, LEVELS, WARN, rank
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
    parser.add_argument("--severity", default=WARN, choices=list(LEVELS),
                        help="lowest severity to report (default: WARN)")
    parser.add_argument("--warn-as-error", action="store_true",
                        help="exit non-zero on warnings as well as errors")
    parser.add_argument("--rules", default="",
                        help="comma-separated rule ids or prefixes to include")
    parser.add_argument("--exclude-rules", default="",
                        help="comma-separated rule ids or prefixes to exclude")
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


def _matches(rule, patterns):
    return any(rule == p or (p.endswith("*") and rule.startswith(p[:-1])) for p in patterns)


def filter_findings(findings, args):
    include = [p.strip() for p in args.rules.split(",") if p.strip()]
    exclude = [p.strip() for p in args.exclude_rules.split(",") if p.strip()]
    limit = rank(args.severity)
    kept = []
    for finding in findings:
        if rank(finding.level) > limit:
            continue
        if include and not _matches(finding.rule, include):
            continue
        if exclude and _matches(finding.rule, exclude):
            continue
        kept.append(finding)
    return kept


def summarize(findings, documents, elapsed):
    """A summary is printed even when nothing is wrong.

    Silence used to be ambiguous: a run with an unresolvable --base produced an
    empty path list and exited 0, so a reader could not tell "passed" from
    "did not run".
    """
    errors = sum(1 for f in findings if f.level == ERROR)
    warnings = sum(1 for f in findings if f.level == WARN)
    return (f"check_docs: {errors} ERROR, {warnings} WARN "
            f"({documents} files, {elapsed:.2f}s)")


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    started = time.monotonic()
    index = DocsIndex()
    selected = select_paths(args, index)
    if selected is None:
        parser.error("supply paths or use --changed-only")

    findings = filter_findings(
        [f for path in selected for f in checks.run(index, path)], args)
    elapsed = time.monotonic() - started
    summary = summarize(findings, len(selected), elapsed) if args.format == "text" else None
    sys.stdout.write(report.FORMATS[args.format](findings, summary))

    if args.warn_as_error:
        return 1 if findings else 0
    return 1 if any(f.is_error for f in findings) else 0
