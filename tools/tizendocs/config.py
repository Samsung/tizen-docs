"""Configuration: one place that decides what is exempt from what.

Scattering exclusions across several tools' own ignore files is how these
setups rot, so every checker reads this single source and third-party ignore
files are generated from it rather than hand-maintained.

TOML is used because tomllib is in the standard library (a YAML parser is not),
comments are first-class -- the *reason* for an exemption is the part that goes
stale -- and a typo raises instead of being coerced into a string.
"""
import fnmatch
import os
import re
import tomllib

from . import paths

DEFAULT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "docscheck.toml")

#: Values ``link_policy`` may take.
EXEMPT_EXISTENCE = "exempt-existence"


def compile_glob(pattern):
    """Translate a path glob to a regex.

    ``**`` crosses directory separators and may match zero segments, so
    ``docs/**/api/**`` matches both ``docs/api/x`` and ``docs/a/b/api/x``.
    ``*`` and ``?`` never cross a separator.
    """
    out = ["^"]
    index = 0
    while index < len(pattern):
        rest = pattern[index:]
        if rest.startswith("/**/"):
            out.append("/(?:.+/)?")
            index += 4
        elif rest.startswith("**/") and index == 0:
            out.append("(?:.+/)?")
            index += 3
        elif rest == "/**":
            out.append("/.+")
            index += 3
        elif rest.startswith("**"):
            out.append(".*")
            index += 2
        elif rest[0] == "*":
            out.append("[^/]*")
            index += 1
        elif rest[0] == "?":
            out.append("[^/]")
            index += 1
        elif rest[0] == "[":
            end = pattern.find("]", index)
            if end == -1:
                out.append(re.escape("["))
                index += 1
            else:
                out.append(pattern[index:end + 1])
                index = end + 1
        else:
            out.append(re.escape(rest[0]))
            index += 1
    out.append("$")
    return re.compile("".join(out))


class PathClass:
    """One entry of the ordered ``[[classes]]`` list."""

    def __init__(self, data):
        self.id = data["id"]
        raw = list(data.get("match", ()))
        #: A leading "?" marks a forward-looking guard: it may match nothing
        #: today without being stale. Imported content that is not currently
        #: present can reappear, and the exemption should already be in place.
        self.optional = {pattern.lstrip("?") for pattern in raw if pattern.startswith("?")}
        self.patterns = [pattern.lstrip("?") for pattern in raw]
        self.matchers = [compile_glob(pattern) for pattern in self.patterns]
        self.skip_rules = tuple(data.get("skip_rules", ()))
        self.only_rules = tuple(data.get("only_rules", ()))
        self.aggregate_rules = tuple(data.get("aggregate_rules", ()))
        self.link_policy = data.get("link_policy", "")
        self.reason = data.get("reason", "")

    def matches(self, path):
        return any(matcher.match(path) for matcher in self.matchers)


def rule_matches(rule, patterns):
    return any(fnmatch.fnmatchcase(rule, pattern) for pattern in patterns)


class Config:
    def __init__(self, data, source=""):
        self.source = source
        self.schema = data.get("schema", 1)
        self.classes = [PathClass(entry) for entry in data.get("classes", ())]
        self.rules = dict(data.get("rules", {}))

    # ---- path classification (first match wins) --------------------------

    def classify(self, path):
        """Return the first class matching *path*, or ``None``.

        Order is significant and declared in the file: a hand-written document
        that happens to live under an api/ directory must be listed before the
        generated class that would otherwise swallow it.
        """
        for entry in self.classes:
            if entry.matches(path):
                return entry
        return None

    def skips(self, path, rule):
        entry = self.classify(path)
        if entry is None:
            return False
        if entry.only_rules:
            return not rule_matches(rule, entry.only_rules)
        return rule_matches(rule, entry.skip_rules)

    def aggregates(self, path, rule):
        entry = self.classify(path)
        return bool(entry and rule_matches(rule, entry.aggregate_rules))

    def in_class(self, path, class_id):
        """Whether *path* belongs to the class named *class_id*.

        Unlike classify() this does not stop at the first match, because class
        membership and rule-skipping answer different questions: a versioned
        API route is both generated content *and* published elsewhere.
        """
        return any(entry.matches(path)
                   for entry in self.classes if entry.id == class_id)

    def exempt_existence(self, target):
        """Whether a link to *target* may point at a file that is not here."""
        return any(entry.matches(target)
                   for entry in self.classes if entry.link_policy == EXEMPT_EXISTENCE)

    # ---- severities ------------------------------------------------------

    def severity(self, rule, default):
        for pattern, level in self.rules.items():
            if fnmatch.fnmatchcase(rule, pattern):
                return level.upper()
        return default


def load(path=None, root=None):
    target = path or os.path.normpath(
        os.path.join(root or paths.repo_root(), "tools", "docscheck.toml"))
    if not os.path.isfile(target):
        return Config({}, source="")
    with open(target, "rb") as handle:
        return Config(tomllib.load(handle), source=paths.to_posix(target))
