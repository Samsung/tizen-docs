"""The `media` subcommand.

Split out of the default run for two reasons. It reads every text file under
docs/ to build the reference set, which takes about a minute and has no place
in the check a contributor runs before opening a pull request. And its answer
is only meaningful once the link rules are clean: a reference that points at
the wrong path makes its own target look unreferenced, so running it over an
unfixed corpus overstates the result - by 296 MB, when this was first measured.
"""
from . import checks
from .findings import ERROR
from .report import text


def run(index, formatter=text.render):
    blockers = [finding
                for path in sorted(p for p in index.files
                                   if p.endswith(".md") and index.handwritten(p))
                for finding in checks.run(index, path)
                if finding.level == ERROR and finding.rule.startswith("L-")]
    if blockers:
        print(f"media: refusing to report - {len(blockers)} unresolved link "
              "error(s) would be miscounted as unreferenced assets.")
        print("       Fix them first: python3 tools/check_docs.py --all --rules 'L-*'")
        return 1

    findings = list(checks.run_media(index)) + list(checks.run_corpus(index))
    findings = [f for f in findings if f.rule.startswith("M-")]
    total = sum(_size(index, f) for f in findings)
    output = formatter(findings, f"media: {len(findings)} finding(s), "
                                f"{total / 1048576:.1f} MB")
    print(output, end="")
    return 0


def _size(index, finding):
    import os
    try:
        return os.path.getsize(index.absolute(finding.path))
    except OSError:
        return 0
