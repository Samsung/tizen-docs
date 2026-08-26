# Tizen Docs TOC formats

TOC files are Markdown files named `toc.md`, `toc_all.md`, or a section-specific variant
such as `toc_vscode_web.md`. They drive the published navigation; their heading level is
the navigation depth.

## Existing site-root links

Top-level TOCs and many document bodies use paths rooted at the published site:

```markdown
# Guides
## [Overview](/application/native/guides/index.md)
### [Application lifecycle](/application/native/guides/applications/app-lifecycle.md)
```

Use this form when adding an entry to a document or TOC that already uses it. The leading
`/` means a path below `docs/`, not a filesystem path.

## Local TOCs

Some nested TOCs use links relative to their own directory:

```markdown
# API reference
## [Overview](index.md)
## [Core API](core-api.md)
```

Keep this format when that is what the target TOC uses.

## Entry metadata

Some TOCs carry per-entry metadata in the link **title**, inside the parentheses:

```markdown
# [Overview](guides/overview.md "source:https://github.com/Samsung/tizen-docs/blob/master/docs/platform/HAL/guides/overview.md, tags:['HAL'], authors:['name@samsung.com']")
```

Rules, all of which the validator checks:

- The metadata belongs **inside** the parentheses. A quoted string placed after the
  closing parenthesis is not a link title; it renders as literal text on the page.
- The keys are `source`, `tags`, and `authors` — `authors` plural, even for one person.
- `source` must be the GitHub blob URL of **the file this entry links to**. When the
  entry moves, the URL moves with it.

Only `docs/application/flutter/toc.md`, `docs/platform/HAL/toc.md`, and
`docs/extensions/tizenx/guides/toc.md` use metadata. The other TOCs carry none, and
adding it is not required. `docs/extensions/tizenx/api/toc.md` is generated and puts its
metadata outside the parentheses; fix the generator rather than the file.

## Editing rules

- Follow the existing heading depth and grouping nodes.
- Put an overview first when sibling entries use one.
- Preserve the nearby sibling ordering rather than applying a new global sort order.
- Link the document file, not merely its directory.
- Update a TOC entry whenever its document is moved or renamed.
- Never skip a heading level. Depth is navigation depth, so jumping from `##` to `####`
  drops a level out of the published menu.
- `docs/application/web/api/toc.xml` is a different mechanism entirely: Eclipse-help XML
  for the Web API reference, with hrefs relative to the build output rather than to this
  repository. When a new API version directory is imported, add it to the
  `<tizen-api version="...">` list there.
