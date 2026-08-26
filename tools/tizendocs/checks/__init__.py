"""The rule registry.

Every rule is a generator ``(index, path, source) -> Iterable[Finding]`` with no
side effects: no printing, no exit codes. That purity is what lets the same
rules feed a text report, a machine-readable report, and later a CI gate.

REGISTRY order is the report order, and it is deliberately stable so that
output diffs stay reviewable.
"""
from dataclasses import replace

from . import document, links, naming, reverse, toc_checks

#: ``(rule id, function)`` in report order.
REGISTRY = (
    (naming.RULE, naming.check_kebab),
    (document.RULE, document.check_h1),
    (toc_checks.ORPHAN, toc_checks.check_orphan),
    (links.BROKEN, links.check_links),
)

#: Rules driven by the change set rather than by a document.
#: ``(rule id, function)`` where the function takes ``(index, change)``.
CHANGE_REGISTRY = (
    (reverse.INBOUND, reverse.check_inbound),
    (reverse.TOC, reverse.check_toc),
)

RULE_IDS = tuple(dict.fromkeys(
    [rule for rule, _ in REGISTRY]
    + [links.ANCHOR, links.HTML, links.DEPTH, links.CASE, links.DOCSPREFIX]
    + [rule for rule, _ in CHANGE_REGISTRY]))


def run_change(index, change):
    """Yield findings attributable to a change rather than to one document."""
    for rule, function in CHANGE_REGISTRY:
        for finding in function(index, change):
            level = index.config.severity(finding.rule, finding.level)
            yield finding if level == finding.level else replace(finding, level=level)


def run(index, path):
    """Yield every finding for one document, in registry order."""
    if not path.startswith("docs/") or not path.endswith(".md") or not index.exists(path):
        return
    source = index.source(path)
    for rule, function in REGISTRY:
        if index.skips(path, rule):
            continue
        for finding in function(index, path, source):
            # Severity lives in docscheck.toml, not in the rule, so promoting a
            # rule from WARN to ERROR after a cleanup is a config edit.
            level = index.config.severity(finding.rule, finding.level)
            yield finding if level == finding.level else replace(finding, level=level)
