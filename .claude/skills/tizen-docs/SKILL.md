---
name: tizen-docs
description: Add or review public Tizen documentation while preserving repository structure, TOC navigation, links, and publishing conventions.
---

# Working in Tizen Docs

This repository publishes documentation for the public Tizen Docs site. Work only with
content suitable for public release. Do not add credentials, private contact information,
unreleased product information, or other non-public material.

Write issue and pull request titles, descriptions, and comments in English, regardless of
the language used in the conversation that produced them.

Use this skill when authoring, restructuring, or reviewing documentation here. It covers
the checks that can be automated and the judgement required around them.

## Sources of truth

When a decision is ambiguous, use evidence in this order:

1. [`CONTRIBUTING.md`](../../../CONTRIBUTING.md), the
   [`styleguide/`](../../../styleguide/) documents, and the
   [`reviewguide/`](../../../reviewguide/) documents
2. Sibling documents and the TOC that publishes them
3. This skill and its [directory map](references/directory-map.md) and
   [TOC reference](references/toc-formats.md)

The existing repository contains legacy variations. Do not normalize unrelated files in a
focused change. Match the convention already used by the area you touch, and record a
separate cleanup issue when appropriate.

## Authoring workflow

1. **Choose the destination.** Browse the relevant section under `docs/` and locate its
   governing `toc*.md`. The main sections are `application/`, `platform/`, `iot/`,
   `partners/`, `extensions/`, and `blog/`. See the [directory map](references/directory-map.md)
   for what each section and subdirectory contains, including which sibling files are
   generated content that should not be edited by hand.
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

- Document-body links and image paths can be relative or site-root paths such as
  `/application/...`; both must resolve to real published content. Match the convention
  used by sibling documents.
- Anchor links must point to headings that exist in the target document.
- Site-root paths are relative to the published `docs/` root. For example,
  `/application/native/guides/...` maps to `docs/application/native/guides/...`.
  Use the same style as nearby entries; do not convert an entire legacy document or TOC
  merely to change link style.
- The stable API routes under `/application/native/api/<profile>/latest/` and
  `/application/dotnet/api/<profile>/latest/` are published separately from this
  checkout. Preserve their established relative-link form; do not add generated API
  files just to make a local Markdown path exist.
- When renaming a file or heading, update all incoming links and its TOC entry.

See [TOC formats](references/toc-formats.md) before creating a new TOC or editing an
unfamiliar one.

## Review workflow

Review both correctness and publication safety:

- Is all added content suitable for public release?
- Are the issue/PR title, description, and comments written in English?
- Does the path match the surrounding information architecture?
- Is each new or moved document linked by its governing TOC?
- Do links, images, and anchors still resolve after the change?
- Does the change avoid hand-editing imported API or generated content?
- Does the prose follow the existing style guide and use clear, supported claims?

Run the validator for the pull request's changed files. Fix every `ERROR`; explain or fix
every `WARN` before approval.

For area-specific review points, consult the matching guide under
[`reviewguide/`](../../../reviewguide/) before approving:

- [`review_points_guide.md`](../../../reviewguide/review_points_guide.md) — general guide
  pages: branches, headings, adding/renaming/moving/deleting a page, tags
- [`review_points_web_api.md`](../../../reviewguide/review_points_web_api.md) — required
  for any change under `application/web/api/`: those files are HTML, not Markdown, and
  must use HTML markup (`<strong>`, `<li>`), not Markdown syntax
- [`review_points_release_note.md`](../../../reviewguide/review_points_release_note.md) —
  release-note conventions (release date, tone, TOC registration) for Tizen Studio and
  Tizen Platform notes
- [`stg_build.md`](../../../reviewguide/stg_build.md) — use the Jenkins-built staging URL
  attached to the PR to check rendered output before approving
- [`update_docs_tizen_org.md`](../../../reviewguide/update_docs_tizen_org.md) — how an
  approved `master` change is promoted to the live site via a separate `master` → `live`
  pull request; not needed for routine content review, but relevant when a reviewer is
  also asked to publish
