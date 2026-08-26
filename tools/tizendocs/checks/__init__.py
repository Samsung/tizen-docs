"""The rule registry.

Every rule is a generator ``(index, path, text) -> Iterable[Finding]`` with no
side effects: no printing, no exit codes. That purity is what lets the same
rules feed a text report, a machine-readable report, and later a CI gate.

REGISTRY order is the report order, and it is deliberately stable so that
output diffs stay reviewable.
"""
from . import document, links, naming, toc_checks

#: ``(rule id, function, skipped for generated content)``
REGISTRY = (
    (naming.RULE, naming.check_kebab, True),
    (document.RULE, document.check_h1, True),
    (toc_checks.ORPHAN, toc_checks.check_orphan, True),
    (links.BROKEN, links.check_links, False),
)

RULE_IDS = tuple(dict.fromkeys([rule for rule, _, _ in REGISTRY] + [links.ANCHOR]))


def run(index, path):
    """Yield every finding for one document, in registry order."""
    if not path.startswith("docs/") or not path.endswith(".md") or not index.exists(path):
        return
    text = index.text(path)
    generated = index.generated(path)
    for _, function, skip_when_generated in REGISTRY:
        if generated and skip_when_generated:
            continue
        yield from function(index, path, text)
