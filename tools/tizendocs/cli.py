"""Command-line entry point.

The canonical invocation is referenced verbatim in README.md, AGENTS.md and
.claude/skills/tizen-docs/SKILL.md, so its flags must never change:

    python3 tools/check_docs.py --changed-only --base origin/master
"""
import argparse
import sys
import time

from . import checks, doctor, export, git, mediacmd, paths, report, style
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
    parser.add_argument("--removals", action="store_true",
                        help="also report what this change's deletions and "
                             "renames break elsewhere in the corpus")
    parser.add_argument("--no-removals", action="store_true",
                        help="skip the reverse-direction rules")
    parser.add_argument("--style", action="store_true",
                        help="also emit markdownlint notes for changed lines "
                             "(needs markdownlint-cli2; never affects the exit code)")
    return parser


def change_for(args, index):
    """The change set, when one is available and wanted.

    Reverse-direction rules run by default whenever a base revision is known:
    a removal that breaks other documents is exactly what a contributor most
    needs told, and it costs nothing on a change that removes nothing.
    """
    if args.no_removals or args.all or (args.paths and not args.changed_only):
        return None
    if not (args.changed_only or args.removals):
        return None
    return git.describe(args.base, index.root)


def select_paths(args, index):
    if args.all:
        # Every TOC is included even when generated: navigation is published
        # whoever wrote it, and docscheck.toml decides which rules apply.
        return sorted(path for path in index.files
                      if path.endswith(".md")
                      and (index.handwritten(path) or path in set(index.toc_files)))
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


SUBCOMMANDS = {"doctor": doctor.run, "media": mediacmd.run}


def run_export(argv):
    tool, check = "", False
    for index, value in enumerate(argv):
        if value == "--tool" and index + 1 < len(argv):
            tool = argv[index + 1]
        elif value == "--check":
            check = True
    return export.run(DocsIndex(), tool, check)


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    if argv and argv[0] == "export-ignores":
        return run_export(argv[1:])
    if argv and argv[0] in SUBCOMMANDS:
        return SUBCOMMANDS[argv[0]](DocsIndex())
    parser = build_parser()
    args = parser.parse_args(argv)
    started = time.monotonic()
    index = DocsIndex()
    selected = select_paths(args, index)
    if selected is None:
        parser.error("supply paths or use --changed-only")

    change = change_for(args, index)
    collected = [f for path in selected for f in checks.run(index, path, change)]

    # Corpus rules read all fourteen TOC files once. In a change-scoped run
    # their findings are attributed the same way everything else is, so a
    # contributor is not shown navigation problems they did not create.
    corpus = list(checks.run_corpus(index))
    if args.all or args.paths:
        collected.extend(corpus)
    else:
        touched = set(selected)
        collected.extend(f for f in corpus if f.path in touched)

    if change is not None and change.removed:
        collected.extend(checks.run_change(index, change))
    findings = filter_findings(collected, args)
    elapsed = time.monotonic() - started
    summary = summarize(findings, len(selected), elapsed) if args.format == "text" else None
    sys.stdout.write(report.FORMATS[args.format](findings, summary))

    if args.warn_as_error:
        return 1 if findings else 0
    return 1 if any(f.is_error for f in findings) else 0
