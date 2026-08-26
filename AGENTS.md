# Working in Tizen Docs

This repository publishes documentation for the public Tizen Docs site. Add only
information that is suitable for public release. Never add credentials, private contact
details, unreleased product information, or material that is not approved for public
documentation.

Start with [README.md](README.md) and [CONTRIBUTING.md](CONTRIBUTING.md). For detailed
authoring and review instructions, read
[`.claude/skills/tizen-docs/SKILL.md`](.claude/skills/tizen-docs/SKILL.md).

## Essential rules

- Preserve the existing directory and TOC conventions. Follow sibling documents when a
  rule is unclear.
- Register every new document in its governing `toc*.md` file.
- Use either relative links or site-root paths such as `/application/...`. Both are
  supported by the publishing pipeline; match the convention used by sibling documents
  and the TOC you are editing.
- Versioned API links ending in `/api/<profile>/latest/...` are published separately
  from this checkout. Keep those links relative when that is the local convention; do
  not add generated API files solely to satisfy a documentation-link check.
- Use lowercase kebab-case names for new files and directories.
- Give each new hand-written document one H1 as its first content heading.
- Treat `*/api/**`, `*/wiki/**`, and `*.autogen.md` as imported content. Fix their source
  upstream instead of hand-editing generated output.
- Write issue and pull request titles, descriptions, and comments in English, even if the
  conversation that produced them was in another language.

## Validating a change

```bash
# Authoring, and before opening a pull request
python3 tools/check_docs.py --changed-only --base origin/master

# Reviewing someone else's pull request
python3 tools/check_docs.py --changed-only --base origin/master --format jsonl
```

The same command covers deletions, renames and moves: it reports every
surviving reference to a path the change removes, including references written
as HTML, which a search for the filename in Markdown syntax will miss.

`ERROR` blocks the pull request. Fix every one. `WARN` does not block, but each
one must be fixed, or explained in the pull request description or a review
comment, before approval.

A run always prints a summary line, for example
`check_docs: 0 ERROR, 0 WARN (12 files, 0.20s)`. **If nothing is printed at
all, the validator did not run** - check the `--base` revision.

The validator cannot judge whether an image leaks a user name, whether a code
block matches the prose describing it, or whether a heading follows the style
guide. Its silence is not approval; see the review checklist in
`.claude/skills/tizen-docs/SKILL.md`.
