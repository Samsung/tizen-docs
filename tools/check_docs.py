#!/usr/bin/env python3
"""Validate changed public Tizen Docs Markdown files.

Run from the repository root:
  python3 tools/check_docs.py --changed-only --base origin/master
  python3 tools/check_docs.py path/to/document.md [path/to/toc_all.md]
"""
import argparse
import os
import re
import subprocess
import sys
import urllib.parse

DOCS = "docs"
GENERATED = ("/api/", "/wiki/")
LINK = re.compile(r"(?<!!)\[[^]]*\]\(([^)\s]+)(?:\s+[^)]*)?\)")
IMAGE = re.compile(r"!\[[^]]*\]\(([^)\s]+)(?:\s+[^)]*)?\)")
HEADING = re.compile(r"^(#{1,6})\s+(.+?)\s*$", re.M)
KEBAB = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*\.md$")


def generated(path):
    return any(part in f"/{path}" for part in GENERATED) or path.endswith(".autogen.md")


def read(path):
    with open(path, encoding="utf-8", errors="replace") as file:
        return file.read()


def without_code(text):
    text = re.sub(r"^\s*(```|~~~).*?^\s*\1\s*$", "", text, flags=re.M | re.S)
    return re.sub(r"`[^`]*`", "", text)


def slug(value):
    value = re.sub(r"\[[^]]*\]\([^)]+\)", "", value)
    value = re.sub(r"[`*_]", "", value).lower()
    value = re.sub(r"[^\w\s-]", "", value)
    return re.sub(r"\s+", "-", value).strip("-")


def anchors(path):
    return {slug(match.group(2)) for match in HEADING.finditer(without_code(read(path)))}


def report(level, rule, path, message):
    print(f"{level} {rule} {path}: {message}")
    return level == "ERROR"


def changed_files(base):
    paths = set()
    for command in (("git", "diff", "--name-only", f"{base}...HEAD"),
                    ("git", "diff", "--name-only", base)):
        result = subprocess.run(command, capture_output=True, text=True)
        paths.update(line for line in result.stdout.splitlines() if line)
    return sorted(paths)


def all_tocs():
    return [os.path.join(root, name) for root, _, files in os.walk(DOCS)
            for name in files if name.startswith("toc") and name.endswith(".md")]


def toc_targets():
    targets = set()
    for toc in all_tocs():
        for match in LINK.finditer(without_code(read(toc))):
            raw = urllib.parse.unquote(match.group(1).strip("<> ").split("#", 1)[0])
            if not raw or raw.startswith(("http://", "https://", "mailto:")):
                continue
            if raw.startswith("/"):
                raw = os.path.join(DOCS, raw.lstrip("/"))
            else:
                raw = os.path.join(os.path.dirname(toc), raw)
            targets.add(os.path.normpath(raw))
    return targets


def check(path, toc_entries):
    errors = False
    path = path.replace(os.sep, "/")
    if not path.startswith("docs/") or not path.endswith(".md") or not os.path.isfile(path):
        return errors
    text = without_code(read(path))
    base = os.path.basename(path)
    if not generated(path):
        if not base.startswith("toc") and base != "README.md" and not KEBAB.match(base):
            errors |= report("ERROR", "N-KEBAB", path, "new document names use lowercase kebab-case")
        headings = list(HEADING.finditer(text))
        if not base.startswith("toc") and base != "README.md":
            if len([item for item in headings if len(item.group(1)) == 1]) != 1:
                errors |= report("ERROR", "D-H1", path, "document must contain exactly one H1")
            elif headings and len(headings[0].group(1)) != 1:
                errors |= report("ERROR", "D-H1", path, "the first heading must be the H1")
        if not base.startswith("toc") and base not in ("README.md", "index.md") and path not in toc_entries:
            errors |= report("ERROR", "T-ORPHAN", path, "document is not linked from a TOC")
    for pattern, kind in ((LINK, "link"), (IMAGE, "image")):
        for match in pattern.finditer(text):
            url = match.group(1).strip("<> ")
            if not url or url.startswith(("http://", "https://", "mailto:")):
                continue
            raw, _, fragment = urllib.parse.unquote(url).partition("#")
            if raw.startswith("/"):
                if base.startswith("toc"):
                    target = os.path.normpath(os.path.join(DOCS, raw.lstrip("/")))
                else:
                    errors |= report("ERROR", "L-ROOT-ABS", path, f"{kind} uses a site-root path: {url}")
                    continue
            else:
                target = os.path.normpath(os.path.join(os.path.dirname(path), raw)) if raw else path
            if not os.path.isfile(target):
                errors |= report("ERROR", "L-BROKEN", path, f"{kind} target does not exist: {url}")
            elif fragment and target.endswith(".md") and not generated(target) and fragment.lower() not in anchors(target):
                errors |= report("ERROR", "L-ANCHOR", path, f"anchor does not exist: {url}")
    return errors


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="*")
    parser.add_argument("--changed-only", action="store_true")
    parser.add_argument("--base", default="origin/master")
    args = parser.parse_args()
    paths = args.paths or (changed_files(args.base) if args.changed_only else [])
    if not paths:
        parser.error("supply paths or use --changed-only")
    return 1 if any(check(path, toc_targets()) for path in paths) else 0


if __name__ == "__main__":
    sys.exit(main())
