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
| `tools/check_docs.py` | Link/TOC validator; run before every PR |
| `.claude/skills/tizen-docs/` | This skill |

## `docs/` — published site source

Everything under `docs/` is published to the Tizen Docs site. It contains roughly
1,900 hand-authored Markdown pages and, separately, tens of thousands of generated,
versioned API-reference files (mostly static HTML with supporting JS/CSS) under
`*/api/**` directories. The generated files are imported from another pipeline; never
hand-edit them (see AGENTS.md). The counts below are Markdown-file counts unless a row
says otherwise.

### `docs/application/` (~880 hand-written `.md`, plus ~53,000 generated API files)

Application-developer guides, organized by SDK/language profile and by tool:

| Subdirectory | Content |
| --- | --- |
| `native/` (228 md) | C API guides, tutorials, overview. `native/api/` holds versioned, generated HTML API reference (e.g. `5.0/`, `6.5/`) — do not hand-edit. |
| `web/` (164 md) | Web/W3C API guides. `web/api/` holds the largest generated HTML block in the repo (device_api, ui_fw_api, w3c_api, versioned by release). See `reviewguide/review_points_web_api.md` before touching anything under here — Web is unusual in that the API reference itself lives in this repo as HTML, not Markdown, and must follow HTML markup conventions, not Markdown syntax. |
| `dotnet/` (201 md) | .NET/Xamarin guides; small generated `api/` stub. |
| `flutter/` (13 md) | Flutter guides — the newest, smallest profile. |
| `tizen-studio/` (138 md) | Tizen Studio IDE guide. |
| `vscode-ext/` (66 md) | VS Code extension guide. |
| `vstools/` (51 md) | Visual Studio Tools for Tizen (Windows). |
| `vstools-mac/` (1 md) | Visual Studio Tools for Tizen (Mac). |
| `features/` (5 md), `profiles/` (3 md) | Small cross-cutting overview pages. |

`application/` also carries several parallel top-level TOCs — `toc_all.md`,
`toc_all_new.md`, `toc_vscode_native.md`, `toc_vscode_web.md`, `toc_vscode_dotnet.md`,
`toc_vs-ext_native.md`, `toc_vs-ext_web.md`, `toc_vs-ext_dotnet.md` — one per IDE/profile
combination. Confirm which TOC(s) govern a page before editing navigation; a page can be
linked from more than one.

### `docs/platform/` (121 md, no generated bulk)

Platform/OS documentation:

- `what-is-tizen/` — product overview, versions, device/profile summaries
- `HAL/` — hardware abstraction layer guides and API
- `compliance/` — compliance program, specification, test docs
- `developing/` — building, cloning, flashing, contributing to the Tizen platform itself
- `get-started/` — repo structure, conventions, workflow for platform contributors
- `porting/` — porting guides by subsystem (kernel, graphics, multimedia, connectivity, location)
- `reference/` — GBS, Gerrit, MIC, TIC FAQ, Docker setup, TP usage
- `release-notes/` — one file per Tizen platform version, back to Tizen 1.0

### `docs/extensions/tizenx/` (819 md, ~800 of which are generated API reference)

TizenX extension SDK documentation:

- `overview/` (1 md) — introduction
- `guides/` (18 md) — one guide per component (tizenx-zlog, tizenx-rpcport, tizenx-aurum, tizenx-genui, tizen-ui)
- `api/` (~800 md) — one directory per namespace (e.g. `Tizen.UI`, `Tizen.UI.Components`,
  `Tizen.UI.Widget`, `TizenX.GenUI`, `TizenX.RPCPort`, `TizenX.ZLog`, `TizenX.Aurum`).
  Generated from source; treat as imported content per AGENTS.md.

### `docs/iot/` (16 hand-written md, plus ~8,100 generated API files)

IoT profile guides and overview (`get-started/`, `guides/`, `index.md`). `iot/api/`
holds generated, versioned HTML API reference at the same scale as
`application/web/api/` — do not hand-edit.

### `docs/partners/` (7 md)

Partner program docs: `iot-partners/`, `specialist/`.

### `docs/images/`, `docs/menu.yaml`, and root docs

- `images/` — image assets shared across sections (not tied to one document's `media/`)
- `menu.yaml` — top navigation config (top-level sections shown/hidden on the site)
- `get-started.md`, `glossary.md`, `trademarks.md` — standalone pages with no owning section

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
`application/web/api`, `application/dotnet/api`, `extensions/tizenx/api`, `iot/api`) is
generated and/or versioned content imported from elsewhere. Together they account for
the large majority of files tracked in this repository. `AGENTS.md` states the rule;
this map exists so you know, before you open an editor, which of the roughly 80,000
files under `docs/` are actually meant to be hand-edited (~1,900 Markdown pages) and
which are not.
