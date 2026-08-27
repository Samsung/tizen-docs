"""Generate third-party ignore files from docscheck.toml.

Hand-maintaining the same exclusions in .markdownlint-cli2.jsonc and in
docscheck.toml is how the two drift apart, and a drifted ignore file fails
silently. These are derived and `--check` reports drift, so the derived files
can be committed without becoming a second source of truth.
"""
import json

from . import style

HEADER = ("// GENERATED from tools/docscheck.toml by\n"
          "//     python3 tools/check_docs.py export-ignores --tool markdownlint\n"
          "// Do not edit. Change docscheck.toml and regenerate.\n")

TARGETS = {"markdownlint": ".markdownlint-cli2.jsonc"}


def markdownlint(index):
    """A config enabling only the six rules the style adapter reports."""
    ignores = []
    for entry in index.config.classes:
        if entry.id != "generated":
            continue
        ignores = [pattern for pattern in entry.patterns if pattern.endswith("**")]
    body = json.loads(style.config_document())
    body["ignores"] = sorted(ignores)
    return HEADER + json.dumps(body, indent=2) + "\n"


GENERATORS = {"markdownlint": markdownlint}


def run(index, tool, check=False):
    if tool not in GENERATORS:
        print(f"export-ignores: unknown tool {tool!r}; "
              f"choose from {', '.join(sorted(GENERATORS))}")
        return 2
    generated = GENERATORS[tool](index)
    if not check:
        print(generated, end="")
        return 0
    target = index.absolute(TARGETS[tool])
    try:
        with open(target, encoding="utf-8") as handle:
            current = handle.read()
    except OSError:
        print(f"export-ignores: {TARGETS[tool]} is missing; regenerate it")
        return 1
    if current != generated:
        print(f"export-ignores: {TARGETS[tool]} has drifted from docscheck.toml; "
              "regenerate it")
        return 1
    print(f"export-ignores: {TARGETS[tool]} matches docscheck.toml")
    return 0
