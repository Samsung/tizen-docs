---
name: tizen-docs
description: Add or review public Tizen documentation while preserving repository structure, TOC navigation, links, and publishing conventions.
---

# Working in Tizen Docs

This repository publishes documentation for the public Tizen Docs site. Work only with
content suitable for public release. Do not add credentials, private contact information,
unreleased product information, or other non-public material.

Use this skill when authoring, restructuring, or reviewing documentation here. It covers
the checks that can be automated and the judgement required around them.

## Sources of truth

When a decision is ambiguous, use evidence in this order:

1. [`CONTRIBUTING.md`](../../../CONTRIBUTING.md) and the
   [`styleguide/`](../../../styleguide/) documents
2. Sibling documents and the TOC that publishes them
3. This skill and its [TOC reference](references/toc-formats.md)

The existing repository contains legacy variations. Do not normalize unrelated files in a
focused change. Match the convention already used by the area you touch, and record a
separate cleanup issue when appropriate.

## Authoring workflow

1. **Choose the destination.** Browse the relevant section under `docs/` and locate its
   governing `toc*.md`. The main sections are `application/`, `platform/`, `iot/`,
   `partners/`, `extensions/`, and `blog/`.
2. **Check for imported content.** Do not hand-edit Markdown under `*/api/**`,
   `*/wiki/**`, or files ending in `.autogen.md`. Correct the upstream source and import
   the regenerated result instead.
3. **Name new files and directories** in lowercase kebab-case. Use `.md` for documents.
   Follow local exceptions only when matching an established imported or legacy area.
4. **Write the document.** Use one H1 as the first content heading, sentence-style
   headings, descriptive image alt text, and normal Markdown links. Follow the nearby
   document's frontmatter convention; do not invent metadata keys.
5. **Place media with its document.** Use the nearest `media/` directory and a path
   relative to the Markdown file.
6. **Register navigation.** Add the document to its governing TOC in the same hierarchy,
   ordering, and link format as its siblings. A document absent from its TOC is not
   discoverable on the published site.
7. **Validate the change.** Run the command below, then inspect the rendered Markdown and
   the diff.

```bash
python3 tools/check_docs.py --changed-only --base origin/master
git diff --check
```

## Link and TOC rules

- Document-body links and image paths must be relative and resolve to real files.
- Anchor links must point to headings that exist in the target document.
- Do not use a root-absolute link such as `/docs/...` in a document body.
- Existing TOC files intentionally use **site-root** paths such as
  `/application/native/guides/...`. Keep that convention in TOCs; do not convert an
  entire legacy TOC just to add one entry.
- When renaming a file or heading, update all incoming links and its TOC entry.

See [TOC formats](references/toc-formats.md) before creating a new TOC or editing an
unfamiliar one.

## Review workflow

Review both correctness and publication safety:

- Is all added content suitable for public release?
- Does the path match the surrounding information architecture?
- Is each new or moved document linked by its governing TOC?
- Do links, images, and anchors still resolve after the change?
- Does the change avoid hand-editing imported API or generated content?
- Does the prose follow the existing style guide and use clear, supported claims?

Run the validator for the pull request's changed files. Fix every `ERROR`; explain or fix
every `WARN` before approval.
