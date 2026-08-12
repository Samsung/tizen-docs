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
- Use relative links in document bodies. Existing TOC files use site-root paths such as
  `/application/...`; preserve that format when editing them.
- Use lowercase kebab-case names for new files and directories.
- Give each new hand-written document one H1 as its first content heading.
- Treat `*/api/**`, `*/wiki/**`, and `*.autogen.md` as imported content. Fix their source
  upstream instead of hand-editing generated output.

Before submitting a pull request, run:

```bash
python3 tools/check_docs.py --changed-only --base origin/master
```
