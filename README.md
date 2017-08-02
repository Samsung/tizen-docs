# tizen-docs

This project is for writing Tizen documents for platform and application developers. The documents will be published to new Tizen portal site.

## Branches
Contributions to this documents are welcome.
Please submit PRs to the **staging* branch, which is what's published to the staging docs.

The **master** branch is used for a ready-live.
The **live** branch will be used for publising to the Tizen portal site.

## Respository structure
TOC.md file defines the left-hand navigation panel that appears when you navigate to any page other than the Docs page.
Images are contained within media folders within each subfolder.


If you're adding a top-level node to the TOC.md, also make an entry for it in TOC.html.
You can export TOC.md without styple to make TOC.html

## Contribution workflow
1. Visit the page to edit on portal.tizen.org/docs (TBD), then click the Edit button on the top right. This brings you to the appropriate markdown page in the repo.
2. Edit the markdown:
    - If you're including images (use PNGs, generally), place them in the media folder that's in the topic's folder. Links are then media/<image_name>.png.
    - Relative links to other pages in this docset should be in the form ../<folder>/<topic-file>.md including the training .md. If you're linking to another topic in the same folder, then ../<folder>/ can be omitted. When using anchors, always remember to include the .md before the #.
    - When using external links, especially to portal.tizen.org/docs (TBD), omit any language tag like "ko" so that a reader in another language lands on a target page in that same language if it's available.
3. When you're done, enter a commit message below, and click Propose file change.
4. Send a pull request for your change. We review PRs on a regular basis.'
5. Thank you!

### Tip
Please copy & paste a line in TOC.html after exporting TOC.md.

```
<base href="docs/" target="content">
```

## Conventions


## Naming

Follow these naming conventions and capitalizations when referring to Tizen and related components.

Tizen: refers to the technology.

### Heading capitalizations

All headings need only capitalize the first word and proper names. Refer to most topics for examples.



### Screenshots and images

Make all images purposeful and easy to consume; avoid graphics for the sake of graphics. When using a screenshot, include a red rounded-rectangle outline of where the reader's eyes should go. That is, do the work to help the reader look at what you want them to look at, rather than burdening them with having to figure that our for themselves.

If an image has white bleed areas on the edges, draw a 1-pixel gray outline around the entire graphic.

Always include a meaningful description of the image in the markdown alt-text between the []'s. These descriptions are also a great place to put SEO terms that you don't otherwise want to appear in the text.

### Inline code

Delineate inline code with grave accents (backticks), as in `Tizen package`. This inline formatting is used for the following:

- Code
- Identifiers
- File names, folder names, and extensions
- Command line strings and arguments

Except for the following cases:

- When part of a surrounding code block.
- When appearing in the left-hand column of a table, because these are automatically bolded.
- When appearing in quoted strings
- When appearing in links (although when the term appears by itself, it's OK)

Markdown and HTML are ignored within inline code.


### Code blocks

Code blocks on portal.tizen.org (TBD) are delineated by with three grave accents (backticks), ```, at the beginning and the end. You do not need to indent code blocks unless they are contained within a list.

The opening ``` should be followed by a language code for proper syntax coloring, such as "xml", "json", "csharp", etc. Use "bash" for command-line examples and "output" for command-line results.

The only case when you should use ``` without a language tag is when creating a block of fixed-point text that isn't related to any kind of code. In these cases you can also just indent the code block, which can be preferable because it visually separates the code in an editor.

### Callouts

portal.tizen.org/docs (TBD) uses blockquotes for callouts, that is, lines starting with ">".

Callout sections with ">" only will appear with a solid gray line to the left.

You can also use one of the following callout tags on the first line that will create a shaded callout in the indicated color:

| Tag | Shading color | Topic with examples |
| --- | --- | --- |
| `> [!Note]` | Light blue, use for callouts without any special emphasis. | (TBD) |

### Links

In general, always use the title of the target page as the link text rather than words like "see here" or "this documentation".
Relative links to other pages in this docset should be in the form ../<folder>/<topic-file>.md including the trailing .md.
Links to other markdown files on portal.tizen.org (TBD) are case-insensitive (unlike links to files in GitHub, which are).
If you're linking to another topic in the same folder, then ../<folder>/ can be omitted.
When using anchors, always remember to include the .md before the #.
When using external links, especially to portal.tizen.org (TBD), omit any language tag like "en-us" so that a reader in another language lands on a target page in that same language if it's available.
Bare URLs are not automatically converted into links.

### Inline HTML

If you need to do something that markdown can't handle, use inline HTML. An example is creating a bullet list inside a table.

Use `&lt;` and `&gt;` for < and > characters outside a code block or inline code (delimited by backticks `).

Block-level HTML elements have a few restrictions:

They must be separated from surrounding text by blank lines.
The begin and end tags of the outermost block element must not be indented.
Markdown can't be used within HTML blocks.


**Reference**

We referred to https://github.com/NuGet/docs.microsoft.com-nuget.


