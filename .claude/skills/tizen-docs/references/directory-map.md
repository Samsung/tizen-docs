# Tizen Docs directory map

A directory-by-directory breakdown of this repository, current as of the snapshot in
which this file was written. File and subdirectory counts are hand-written Markdown
under `docs/` unless noted otherwise; they will drift as the site grows, so treat them
as orientation, not a contract. When exact placement matters, browse the directory
itself.

Use this alongside [TOC formats](toc-formats.md): this file tells you *where* a
document belongs; that file tells you *how* to wire it into navigation once it is
there.

## Repository root

| Path | Purpose |
| --- | --- |
| `README.md`, `AGENTS.md`, `CONTRIBUTING.md` | Entry points for humans and AI agents |
| `LICENSE-CODE` | BSD-3-Clause license for code samples |
| `content-license.md` | CC BY 3.0 license for documentation content |
| `.github/CODEOWNERS` | Default reviewers for the whole repo |
| `.github/pull_request_template.md` | Required PR sections: Change Description, Bugs Fixed, API Changes |
| `styleguide/` | Writing rules — see below |
| `reviewguide/` | Reviewer walkthroughs — see below |
| `tools/` | Documentation validator; run before every PR. `check_docs.py` is the entry point, `docscheck.toml` holds every exemption and severity, `tizendocs/` the implementation, `tests/` its tests |
| `.claude/skills/tizen-docs/` | This skill |

## `docs/` — published site source

Everything under `docs/` is published to the Tizen Docs site. It contains roughly
990 hand-authored Markdown pages and, separately, tens of thousands of generated,
versioned API-reference files (mostly static HTML with supporting JS/CSS) under
`*/api/**` directories. The generated files are imported from another pipeline; never
hand-edit them (see AGENTS.md). The counts below are Markdown-file counts unless a row
says otherwise.

### `docs/application/` (~630 hand-written `.md`, plus ~53,000 generated API files)

Application-developer guides, organized by language profile. Tooling documentation
lives in [`docs/sdk-tools/`](#docssdk-tools-252-md) instead:

| Subdirectory | Content |
| --- | --- |
| `native/` (196 md) | C API guides, tutorials, overview. `native/api/` holds versioned, generated HTML API reference (e.g. `5.0/`, `6.5/`) — do not hand-edit. |
| `web/` (172 md) | Web/W3C API guides. `web/api/` holds the largest generated HTML block in the repo (device_api, ui_fw_api, w3c_api, versioned by release). See `reviewguide/review_points_web_api.md` before touching anything under here — Web is unusual in that the API reference itself lives in this repo as HTML, not Markdown, and must follow HTML markup conventions, not Markdown syntax. |
| `dotnet/` (197 md) | .NET guides for NUI. No `api/` directory: `/application/dotnet/api/**` is published from the TizenFX repository, not from here. |
| `flutter/` (14 md) | Flutter guides — the newest, smallest profile. |
| `features/` (5 md), `profiles/` (3 md) | Small cross-cutting overview pages. |

`application/toc_all.md` is the section's only TOC. Be aware that the publishing
pipeline reads just its `# .NET Application`, `# Web Application` and
`# Native Application` blocks; `# Get Started` and `# Reference` are not consumed
today, so adding a page there alone will not make it appear on the site.

### `docs/sdk-tools/` (252 md)

SDK and IDE tooling documentation, organized by tool:

| Subdirectory | Content |
| --- | --- |
| `tizen-studio/` (138 md) | Tizen Studio IDE guide: setup, common/native/web/platform tools, tizen-core, release notes. |
| `vscode-ext/` (63 md) | VS Code extension guide. |
| `vstools/` (49 md) | Visual Studio Tools for Tizen (Windows). |
| `vstools-mac/` (1 md) | Visual Studio Tools for Tizen (Mac). |
| `sdktool-index.md` | Flat A–Z index of every SDK tool, linking into the three trees above. |

Navigation here is unusual and worth understanding before you edit it. The six
per-IDE TOCs — `toc_vscode_{native,web,dotnet}.md` and
`toc_vs-ext_{native,web,dotnet}.md` — are what the pipeline actually publishes, one
per app-model × IDE permutation, and all six draw from the same three tool trees.
A page reachable in one permutation may be missing from another, so check every
TOC that should list a page, not just one.

`sdk-tools/toc_all.md` is *not* read by the pipeline. It documents the section's
information architecture and keeps `tools/check_docs.py` able to distinguish a
genuine orphan from a known one; adding a page there does not publish it.

### `docs/platform/` (120 md, plus a small generated HAL API tree)

Platform/OS documentation:

- `what-is-tizen/` — product overview, versions, device/profile summaries
- `HAL/` — hardware abstraction layer guides and API
- `compliance/` — compliance program, specification, test docs
- `developing/` — building, cloning, flashing, contributing to the Tizen platform itself
- `get-started/` — repo structure, conventions, workflow for platform contributors
- `porting/` — porting guides by subsystem (kernel, graphics, multimedia, connectivity, location)
- `reference/` — GBS, Gerrit, MIC, TIC FAQ, Docker setup, TP usage
- `release-notes/` — one file per Tizen platform version, back to Tizen 1.0

### `docs/extensions/tizenx/` (20 hand-written md, plus ~800 generated API files)

TizenX extension SDK documentation:

- `overview/` (1 md) — introduction
- `guides/` (18 md) — one guide per component (tizenx-zlog, tizenx-rpcport, tizenx-aurum, tizenx-genui, tizen-ui)
- `api/` (~800 md) — one directory per namespace (e.g. `Tizen.UI`, `Tizen.UI.Components`,
  `Tizen.UI.Widget`, `TizenX.GenUI`, `TizenX.RPCPort`, `TizenX.ZLog`, `TizenX.Aurum`).
  Generated from source; treat as imported content per AGENTS.md.

### Root docs

- `trademarks.md` — third-party trademark attribution page, with no owning section

## `styleguide/`

Writing rules referenced from `AGENTS.md` and this skill's "Sources of truth":
`style.md` (headings, tone), `naming-rules.md` (Tizen term naming), `template-guide.md`,
`custom-style.md`, `sample1.md` (worked example), plus a `media/` folder of screenshots.

## `reviewguide/`

Reviewer-facing walkthroughs, not yet referenced elsewhere in this skill — consult them
when reviewing a PR in the matching area:

- `review_points_guide.md` — general guide-page review points: branches, headings, adding
  a page (`toc_all.md`, `overview.md`), renaming/moving/deleting a page, tags
- `review_points_web_api.md` — Web API specifics: these files are HTML, not Markdown; use
  HTML tags (`<strong>`, `<li>`), not Markdown syntax, when editing them
- `review_points_release_note.md` — release-note conventions for both Tizen Studio and
  Tizen Platform notes: release date, tone, TOC registration
- `stg_build.md` — how to use the staging (stg) preview URL that Jenkins builds for each
  PR to check rendered output before merge
- `update_docs_tizen_org.md` — how a merged `master` change is promoted to the live
  `docs.tizen.org` site via a `master` → `live` pull request

## Cross-cutting: generated vs. hand-written content

Every `*/api/**` directory in this repository (`application/native/api`,
`application/web/api`, `platform/HAL/api`, `extensions/tizenx/api`) is generated and/or
versioned content imported from elsewhere. Together they account for the large majority
of files tracked here. `AGENTS.md` states the rule; this map exists so you know, before
you open an editor, which of the roughly 69,800 files under `docs/` are meant to be
hand-edited (about 990 Markdown pages) and which are not.

Two distinctions matter when a link points into one of those trees, and the validator
draws them:

- **Present and checked.** `application/web/api/`, `platform/HAL/api/` and
  `extensions/tizenx/api/` are in this repository, and the `latest` symlinks are
  committed, so links into them resolve and are verified.
- **Published elsewhere and exempt.** `application/dotnet/api/` does not exist here at
  all — the .NET API reference comes from the TizenFX repository — and versioned routes
  under `application/native/api/<profile>/latest/` are served by a separate pipeline.
  Links to these cannot be verified locally and are not reported.

A handful of hand-written pages live under an `api/` directory in spite of the rule, such
as `application/web/api/index.md`. They are listed in `tools/docscheck.toml` so the
validator keeps checking them.
