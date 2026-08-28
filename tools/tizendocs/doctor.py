"""Self-check for the configuration.

Exclusion lists rot in two directions. A missing entry produces noise, which
someone notices. A *stale* entry produces silence, which nobody notices: the
pattern stops matching anything and the exemption it documented is now just
misleading text. This command catches the second kind.

Written after a real instance: three paths listed under api-handwritten had
been deleted upstream, and nothing in the toolkit would have said so.
"""
import os
import re
from datetime import date

from . import checks

WILDCARD = re.compile(r"[*?\[]")


def literal_prefix(pattern):
    """The longest leading directory of *pattern* containing no wildcard."""
    head = WILDCARD.split(pattern, 1)[0]
    return head.rsplit("/", 1)[0] if "/" in head else head


def problems(index):
    """Yield human-readable problems with the loaded configuration."""
    config = index.config
    if not config.source:
        yield "no docscheck.toml found; built-in defaults are in use"
        return

    paths = index.files
    for entry in config.classes:
        for pattern, matcher in zip(entry.patterns, entry.matchers):
            if pattern in entry.optional:
                continue
            if any(matcher.match(path) for path in paths):
                continue
            # os.walk does not follow symlinked directories, and the versioned
            # API trees are reached through committed `latest` symlinks. For a
            # wildcard pattern, fall back to asking the filesystem about its
            # literal prefix. A pattern with no wildcard names one exact path,
            # so the prefix says nothing and the walked set is the answer.
            if WILDCARD.search(pattern):
                prefix = literal_prefix(pattern)
                if prefix and os.path.exists(index.absolute(prefix)):
                    continue
            yield (f"class {entry.id}: pattern matches nothing: {pattern}"
                   " - the path it exempted is gone, so delete it")

    # [naming] rots the same way a class pattern does: a directory gets
    # renamed or deleted and its entry becomes text that exempts nothing,
    # while still quietly widening what the rule accepts.
    if config.legacy_directories:
        present = {part
                   for path in paths
                   for part in os.path.dirname(path).split("/")[1:]}
        for name in config.legacy_directories:
            if name not in present:
                yield (f"[naming] legacy_directories: no directory named"
                       f" {name!r} exists - the name it exempted is gone,"
                       " so delete it")

    # Publication ownership is a contract with the conversion pipeline. A
    # typo silently makes every document in a section look unpublishable, so
    # validate the declared TOCs and keep exemptions from becoming permanent.
    for section in config.publication_sections:
        if not section.patterns:
            yield f"publication section {section.id}: match must not be empty"
        elif not any(section.matches(path) for path in paths):
            yield f"publication section {section.id}: match patterns match nothing"
        for toc in section.governing_tocs:
            if toc not in index.toc_files:
                yield (f"publication section {section.id}: governing TOC does not "
                       f"exist or is not a toc*.md: {toc}")

    for landing, matcher in zip(config.automatic_landings,
                                config._automatic_landing_matchers):
        if not any(matcher.match(path) for path in paths):
            yield f"publication automatic_landing matches nothing: {landing}"

    for exception in config.publication_exceptions:
        if not any(exception.matches(path) for path in paths):
            yield ("publication exception matches nothing: "
                   f"{', '.join(exception.patterns)}")
        if not exception.reason.strip() or not exception.owner.strip():
            yield "publication exception must declare a non-empty reason and owner"
        try:
            review = date.fromisoformat(str(exception.review_by))
        except ValueError:
            yield ("publication exception has an invalid review_by date: "
                   f"{exception.review_by!r}")
        else:
            if review < date.today():
                yield ("publication exception review_by has passed: "
                       f"{exception.review_by}")

    known = set(checks.RULE_IDS)
    for rule in config.rules:
        if "*" not in rule and rule not in known:
            yield f"severity set for unknown rule: {rule}"

    for rule in checks.RULE_IDS:
        if config.severity(rule, "") == "":
            yield f"rule has no severity in [rules]: {rule}"

    seen = []
    for entry in config.classes:
        for earlier in seen:
            shadowed = [p for p, m in zip(entry.patterns, entry.matchers)
                        if all(earlier.matches(path)
                               for path in paths if m.match(path))
                        and any(m.match(path) for path in paths)]
            if shadowed:
                yield (f"class {entry.id}: {shadowed} is fully shadowed by the"
                       f" earlier class {earlier.id}; first match wins")
        seen.append(entry)


def run(index):
    found = list(problems(index))
    for problem in found:
        print(f"docscheck.toml: {problem}")
    print(f"doctor: {len(found)} problem(s), "
          f"{len(index.config.classes)} classes, {len(checks.RULE_IDS)} rules")
    return 1 if found else 0
