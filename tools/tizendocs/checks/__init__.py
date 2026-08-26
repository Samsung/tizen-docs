"""The rule registry.

Every rule is a generator ``(index, path, source) -> Iterable[Finding]`` with no
side effects: no printing, no exit codes. That purity is what lets the same
rules feed a text report, a machine-readable report, and later a CI gate.

REGISTRY order is the report order, and it is deliberately stable so that
output diffs stay reviewable.
"""
from dataclasses import replace

from . import (content, document, links, media, naming, reverse, toc_checks,
               xml_toc)

#: ``(rule id, function)`` in report order.
REGISTRY = (
    (naming.RULE, naming.check_kebab),
    (document.RULE, document.check_h1),
    (toc_checks.ORPHAN, toc_checks.check_orphan),
    (toc_checks.META, toc_checks.check_meta),
    (links.BROKEN, links.check_links),
    (media.ALT, media.check_alt_text),
    (document.FRONT_MATTER, document.check_front_matter),
    (naming.DIR_RULE, naming.check_directory),
    (content.OVERVIEW, content.check_overview),
    (content.FEATPRIV, content.check_feature_privilege),
)

#: Rules that read the whole corpus once rather than one document at a time.
#: ``(rule id, function)`` where the function takes ``(index)``.
CORPUS_REGISTRY = (
    (toc_checks.DANGLING, toc_checks.check_dangling),
    (toc_checks.DEPTH, toc_checks.check_depth),
    (toc_checks.META_SRC, toc_checks.check_meta_source),
    (toc_checks.DUP, toc_checks.check_duplicates),
    (xml_toc.XML, xml_toc.check_wellformed),
    (xml_toc.XMLVER, xml_toc.check_versions),
    (media.JUNK, media.check_junk),
)


#: Rules that scan every asset. Separate because the scan reads every text
#: file under docs/ and takes about a minute, which has no place in the run a
#: contributor makes before opening a pull request.
MEDIA_REGISTRY = (
    (media.ORPHAN, media.check_orphans),
)


#: Rules driven by the change set rather than by a document.
#: ``(rule id, function)`` where the function takes ``(index, change)``.
CHANGE_REGISTRY = (
    (reverse.INBOUND, reverse.check_inbound),
    (reverse.TOC, reverse.check_toc),
    (reverse.MEDIA, reverse.check_media),
    (reverse.ANCHOR, reverse.check_anchor),
)

RULE_IDS = tuple(dict.fromkeys(
    [rule for rule, _ in REGISTRY]
    + [rule for rule, _ in CORPUS_REGISTRY]
    + [rule for rule, _ in MEDIA_REGISTRY]
    + [links.ANCHOR, links.ANCHOR_AMBIG, links.HTML, links.DEPTH,
       links.CASE, links.DOCSPREFIX]
    + [rule for rule, _ in CHANGE_REGISTRY]))


def run_corpus(index):
    """Yield findings from rules that inspect the corpus as a whole."""
    for rule, function in CORPUS_REGISTRY:
        produced = {}
        for finding in function(index):
            level = index.config.severity(finding.rule, finding.level)
            if level != finding.level:
                finding = replace(finding, level=level)
            produced.setdefault(finding.path, []).append(finding)
        for path, findings in produced.items():
            yield from _aggregate(index, path, rule, findings)


def run_media(index):
    """Yield findings from the asset scan."""
    for rule, function in MEDIA_REGISTRY:
        for finding in function(index):
            level = index.config.severity(finding.rule, finding.level)
            yield finding if level == finding.level else replace(finding, level=level)


def run_change(index, change):
    """Yield findings attributable to a change rather than to one document."""
    for rule, function in CHANGE_REGISTRY:
        for finding in function(index, change):
            level = index.config.severity(finding.rule, finding.level)
            yield finding if level == finding.level else replace(finding, level=level)


ADDED_ONLY = "added-only"
CHANGED_ONLY = "changed-only"


def applies(index, path, rule, change):
    """Whether *rule* applies to *path* in this run."""
    if index.skips(path, rule):
        return False
    scope = index.config.scope(rule)
    if scope == ADDED_ONLY:
        # Without a change set there is no way to know what is new, so the
        # rule stays silent rather than reporting the whole legacy corpus.
        return bool(change) and change.status.get(path) == "A"
    if scope == CHANGED_ONLY:
        return bool(change) and path in change.status
    return True


def run(index, path, change=None):
    """Yield every finding for one document, in registry order."""
    if not path.startswith("docs/") or not path.endswith(".md") or not index.exists(path):
        return
    source = index.source(path)
    for rule, function in REGISTRY:
        if not applies(index, path, rule, change):
            continue
        produced = []
        for finding in function(index, path, source):
            # Severity lives in docscheck.toml, not in the rule, so promoting a
            # rule from WARN to ERROR after a cleanup is a config edit.
            level = index.config.severity(finding.rule, finding.level)
            produced.append(
                finding if level == finding.level else replace(finding, level=level))
        yield from _aggregate(index, path, rule, produced)


def _aggregate(index, path, rule, findings):
    """Collapse a rule's findings for one file into a single report.

    Configured per path class. A generated file with 799 malformed entries has
    one defect - in the generator - and 799 findings would only ever be a
    reason to stop reading the output.
    """
    if len(findings) < 2 or not index.config.aggregates(path, rule):
        yield from findings
        return
    first = findings[0]
    yield replace(
        first,
        message=(f"{len(findings)} findings in this generated file, first: "
                 f"{first.message} - correct the generator, not the output"),
        related=(f"and {len(findings) - 1} more in {path}",))
