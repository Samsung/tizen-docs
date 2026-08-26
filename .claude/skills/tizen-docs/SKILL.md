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
   governing `toc*.md`. The main sections are `application/`, `sdk-tools/`, `platform/`,
   and `extensions/`. Application guides and SDK/IDE tooling guides are separate
   sections: a page about a tool belongs under `sdk-tools/`, not under a language
   profile. See the [directory map](references/directory-map.md)
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
- Versioned API routes under `/application/native/api/<profile>/latest/` and
  `/application/dotnet/api/...` are published by a separate pipeline, so no file exists
  here and the validator does not check them. Preserve their established link form; do
  not add generated API files just to make a local path exist.
- Everything else under an `api/` directory *is* in this repository and *is* checked:
  `application/web/api/`, `platform/HAL/api/`, and `extensions/tizenx/api/`. The
  `latest` symlinks are committed, so most paths beneath them resolve.
- When renaming a file or heading, update all incoming links and its TOC entry. Run the
  validator with `--changed-only`; it lists them for you.

See [TOC formats](references/toc-formats.md) before creating a new TOC or editing an
unfamiliar one.

## Deleting, renaming, or moving a document

This is where breakage comes from, because the damage lands in files the change never
opened. Run the validator and work through what it reports:

```bash
python3 tools/check_docs.py --changed-only --base origin/master
```

1. **`R-INBOUND`** — every surviving reference to the old path. Remove or repoint each
   one. **This includes references written as HTML** (`<a href>`, `<img src>`,
   `<source src>`), which searching for the filename in Markdown syntax will not find.
   When the change is a rename, the finding carries the replacement path.
2. **`R-TOC`** — TOC entries for the old path. There are fourteen `toc*.md` files; a
   page can be listed in more than one.
3. **`R-MEDIA`** — images and videos that lost their last reference. Delete them, or say
   in the pull request why they are kept.
4. **`R-ANCHOR`** — inbound links to a heading the change removes.
5. **`overview.md`** — remove the entry from the section landing page as well.

There is no redirect mechanism in this repository. If a page likely has external inbound
links, prefer reducing it to a short stub pointing at its successor over deleting it.

Keep these changes small. A single 672-file cleanup (`26c727a41`) introduced a broken
link of its own.

If a change adds, renames or removes a **top-level** directory under `docs/`, the
downstream `tizen.org.v2.docs` pipeline hardcodes that list in
`scripts/pages/check-md-links.js`, and it has to be updated there too.

## Review workflow

Review both correctness and publication safety:

- Is all added content suitable for public release?
- Are the issue/PR title, description, and comments written in English?
- Does the path match the surrounding information architecture?
- Is each new or moved document linked by its governing TOC?
- Do links, images, and anchors still resolve after the change?
- Does the change avoid hand-editing imported API or generated content?
- Does the prose follow the existing style guide and use clear, supported claims?

Run the validator for the pull request's changed files. Fix every `ERROR`; fix or
explain every `WARN` before approval.

`WARN` rules you will actually see: `T-DUP` (a target listed twice in one TOC), `T-META`
(link metadata outside the parentheses, where it renders as literal text), `M-JUNK`
(a non-web asset in a `media/` directory), `M-ORPHAN`, `D-FM` (an unknown front-matter
key), `D-OVERVIEW` (a new page not linked from its section landing page), `L-FEATPRIV`
(a feature or privilege key rendered as a link instead of a code span),
`L-ANCHOR-AMBIG` (an anchor that resolves under one renderer's slug rule but not
another's), and the `R-MEDIA` / `R-ANCHOR` removal advisories.

### The validator cannot check these — its silence is not approval

1. **Personal information in an image.** A user name in a project path, a login screen,
   a local filesystem in a screenshot. Not detectable from text, and the highest
   consequence item in the whole review guide, because this repository is public. Look
   at every image a pull request adds.
2. **Whether a code block matches the prose describing it.** The review guide's own
   example is `Prefrence.Keys` in text against `Preference.Keys` in code.
3. **Code block indentation**, which is a rendering question — use the staging build.
4. **Heading sentence case and gerund use.** Not automated on purpose: the style guide
   and the template guide contradict each other, and distinguishing a proper noun from
   title case needs a curated term list this repository does not have.
5. **Release-note tone, dates, and the Release Details section**, which waits on
   platform approval.
6. **Which branch the pull request targets** (`master`, `live`, or
   `tizen_<VERSION>_prepare`).
7. **Whether the Dependencies section is right**, which needs platform knowledge.
8. **API links through the `latest` symlink**, which do not resolve in GitHub's preview.
   The staging build attached to the pull request is the only authority.

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
