#!/usr/bin/env python3
"""Synchronize transitive SDK document-link targets into all variant TOCs."""
import argparse
import os
import re
import sys

TOOLS = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(TOOLS)
sys.path.insert(0, TOOLS)

from tizendocs import config, markdown, publication, toc  # noqa: E402
from tizendocs.index import DocsIndex  # noqa: E402

START = "<!-- docscheck:sdk-closure:start -->"
END = "<!-- docscheck:sdk-closure:end -->"
ANCHOR = "<!-- docscheck:referenced-sdk:end -->"
BLOCK = re.compile(rf"\n?{re.escape(START)}.*?{re.escape(END)}\n?", re.S)


def title(index, path):
    headings = index.source(path).headings()
    value = headings[0].group(2) if headings else os.path.splitext(os.path.basename(path))[0]
    value = re.sub(r"\[([^]]+)\]\([^)]+\)", r"\1", value)
    return value.replace("`", "").strip() or os.path.basename(path)


def closure(index, toc_path, text):
    seed_text = BLOCK.sub("\n", text)
    seeds = {target for target in toc.parse(seed_text, toc_path).targets
             if target.startswith("docs/sdk-tools/") and index.exists(target)}
    reached = set(seeds)
    pending = list(sorted(seeds))
    while pending:
        source = pending.pop()
        for target, _, _, _ in publication.linked_documents(index, source):
            if not target.startswith("docs/sdk-tools/") or target in reached:
                continue
            reached.add(target)
            pending.append(target)
    return sorted(reached - seeds)


def rendered_block(index, targets):
    lines = [START, "### Transitive link targets"]
    for target in targets:
        href = "/" + target.removeprefix("docs/")
        lines.append(f"#### [{title(index, target)}]({href})")
    lines.append(END)
    return "\n".join(lines) + "\n"


def synchronize(index, toc_path):
    absolute = index.absolute(toc_path)
    original = markdown.read(absolute)
    without = BLOCK.sub("\n", original)
    if ANCHOR not in without:
        raise ValueError(f"missing insertion marker in {toc_path}: {ANCHOR}")
    updated = without.replace(ANCHOR, rendered_block(index, closure(index, toc_path, without)) + ANCHOR, 1)
    return absolute, original, updated


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="fail if a TOC is not synchronized")
    args = parser.parse_args()
    index = DocsIndex(root=ROOT, config=config.load(root=ROOT))
    section = next(item for item in index.config.publication_sections if item.id == "sdk-tools")
    changed = []
    for toc_path in section.governing_tocs:
        absolute, original, updated = synchronize(index, toc_path)
        if updated == original:
            continue
        changed.append(toc_path)
        if not args.check:
            with open(absolute, "w", encoding="utf-8") as output:
                output.write(updated)
    if changed:
        print("SDK TOC closure is stale: " + ", ".join(changed))
        return 1 if args.check else 0
    print("SDK TOC closure is synchronized")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
