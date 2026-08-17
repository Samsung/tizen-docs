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

## Editing rules

- Follow the existing heading depth and grouping nodes.
- Put an overview first when sibling entries use one.
- Preserve the nearby sibling ordering rather than applying a new global sort order.
- Link the document file, not merely its directory.
- Update a TOC entry whenever its document is moved or renamed.
