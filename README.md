# tizen-docs

This project is for writing Tizen documents for platform and application developers. The documents will be published to new Tizen Docs site.

## Branches

Contributions to this documents are welcome.  
Please submit PRs to the **live** branch, which is what's published to the live Tizen Docs site. You can see your changes on https://docs.stage.tizen.org/staging/{PR #}/ before they are published on the live Tizen Docs site.  
The **master** branch is used for a ready-live. It is used for the same purpose as tizen branch on Tizen public git.   
The **staging** branch is used for testing.

## Respository structure

- All markdown files are in the docs folder and various subfolders.
- The docs/index.md file defines the landing (hub) page are it appears on docs.tizen.org (TBD).
- The docs/TOC.md file defines the left-hand navigation panel that appears when you navigate to any page other than the hub page.
- Images are contained within media folders within each subfolder.

## Contribution workflow

1. Visit the page to edit on https://docs.tizen.org (TBD), then click the **Edit** button on the top right. This brings you to the appropriate markdown page in the repo.
1. Edit the markdown:
    1. If you're including images (use PNGs, generally), place them in the media folder that's in the topic's folder. Links are then `media/<image_name>.png`.
    1. Relative links to other pages in this docset should be in the form `../<folder>/<topic-file>.md` including the training `.md`. If you're linking to another topic in the same folder, then `../<folder>/` can be omitted. When using anchors, always remember to include the `.md` before the `#`.
1. When you're done, enter a commit message below, and click **Propose file change**.
1. Send a pull request for your change. We review PRs on a regular basis.'
1. Thank you!

If you're creating a new topic, keep the following in mind as well:

1. Always place the new topic in an appropriate subfolder, and follow the conventions for filenames as you see them used here.
1. In addition to adding your page, edit docs/TOC.md to add a link to that page.
1. If you're adding a top-level node to the TOC, also make an entry for it in docs/index.md.

> **Note**  
> TOC.md has maximum 4th depth. You can use #, ##, ###, and ####. The title with # will be located on GNB(Global Navigation Bar).

### How to PR
1. Fork form the original repository, http://github.com/Samsung/tizen-docs.

1. Clone the forked repository.
   ```
   $ git clone <forked repository URL>
   ```
1. Set to synchronize the original repository and the forked repository.
   ```
   $ git remote -v
   $ git remote add upstream http://github.com/Samsung/tizen-docs.git
   $ git remote -v
   ```
1. Create a new branch on the forked repository or the local repository,
   and switch to the new branch.
   ```
   $ git checkout -b <new branch name>
   ```
1. Create a local commit.
   ```
   $ git status
   $ git add
   $ git commit -a
   ```
1. Push the branch
   ```
   $ git push origin <new branch name>
   ```
1. Open a pull requst on http://github.com/Samsung/tizen-docs.git.


## Conventions
In general, if you don't see something described here, look in editing markdown files for examples.


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

Code blocks on docs.tizen.org (TBD) are delineated by with three grave accents (backticks), ```, at the beginning and the end. You do not need to indent code blocks unless they are contained within a list.

The opening ``` should be followed by a language code for proper syntax coloring, such as "xml", "json", "csharp", etc. Use "bash" for command-line examples and "output" for command-line results.

The only case when you should use ``` without a language tag is when creating a block of fixed-point text that isn't related to any kind of code. In these cases you can also just indent the code block, which can be preferable because it visually separates the code in an editor.

### Links

- In general, always use the title of the target page as the link text rather than words like "see here" or "this documentation".
- Relative links to other pages in this docset should be in the form `../<folder>/<topic-file>.md` including the trailing `.md`.
- Links to other markdown files on docs.microsoft.com are case-insensitive (unlike links to files in GitHub, which are).
- If you're linking to another topic in the same folder, then `../<folder>/` can be omitted.
- When using anchors, always remember to include the `.md` before the `#`.
- Bare URLs are not automatically converted into links.

## line break
- It's now possible to add a forced line break with two blank spaces at the end of the line:
```
line1  
line2
```

### Inline HTML

If you need to do something that markdown can't handle, use inline HTML. An example is creating a bullet list inside a table.

Use `&lt;` and `&gt;` for < and > characters outside a code block or inline code (delimited by backticks `).

Block-level HTML elements have a few restrictions:

* They must be separated from surrounding text by blank lines.
* The begin and end tags of the outermost block element must not be indented.
* Markdown can't be used within HTML blocks.

### Tip
Please copy & paste a line in TOC.html after exporting docs/TOC.md.

```
<base href="docs/" target="content">
```


**Reference**

We referred to https://github.com/NuGet/docs.microsoft.com-nuget.
