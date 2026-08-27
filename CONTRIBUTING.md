# Contributing

Thank you for your interest in contributing to the Tizen documentation!

This document covers the process for contributing to the articles and code samples
published at <https://samsungtizenos.com/docs>. Contributions may be as simple as a typo
correction or as complex as a new article.

Only contribute information suitable for public release. Do not add credentials, private
contact information, unreleased product details, or other non-public material.

Write all issues and pull requests — titles, descriptions, and comments — in English so
that the whole community can read and participate.

For the repository layout, the review labels, and the licence, see
[README.md](README.md). For the rules that apply while editing, see [AGENTS.md](AGENTS.md),
the [style guide](styleguide/), and the [reviewer guides](reviewguide/).

1. [Process for contributing](#process-for-contributing)
1. [File names](#file-names)
1. [How to open a pull request](#how-to-open-a-pull-request)
1. [DOs and DON'Ts](#dos-and-donts)
1. [Licence and the Contributor License Agreement](#licence-and-the-contributor-license-agreement)

## Process for contributing

You need a basic understanding of [Git and GitHub](https://guides.github.com/activities/hello-world/).

**Step 1: agree on the change.** For anything larger than a small fix, open an
[issue](https://github.com/Samsung/tizen-docs/issues) describing what you want to do and
where it belongs, and get feedback before investing time. You can also pick up one of the
[open issues](https://github.com/Samsung/tizen-docs/issues).

Decide which section the page belongs to and which table of contents publishes it. Each
top-level directory under `docs/` is a section: `application/` (app developer guides),
`sdk-tools/` (SDK and IDE tooling), `platform/` (Open Source Project), and `extensions/`.
A TOC is a Markdown file whose heading depth is the navigation depth.

Be aware that not every TOC is read by the publishing pipeline, and not every block of a
TOC that is read gets consumed. Under `sdk-tools/`, the six per-IDE TOCs
(`toc_vscode_*.md`, `toc_vs-ext_*.md`) are what actually publish, while
`sdk-tools/toc_all.md` documents the structure only. Confirm which TOC governs your page
rather than assuming `toc_all.md` is enough.

**Step 2: fork and branch.** Fork `Samsung/tizen-docs` and create a branch for your
changes. For a small edit you can use GitHub's web interface, which creates the branch for
you.

**Step 3: write.** Start from the [template](styleguide/template-guide.md) and follow the
[style guide](styleguide/style.md). Put the article in the folder for its section, and put
images in a `media` folder beside the article. A section's main article is `index.md`.

Register the page in its governing TOC. A page absent from every TOC is not reachable on
the published site.

**Step 4: validate.** Before opening the pull request:

```bash
python3 tools/check_docs.py --changed-only --base origin/master
git diff --check
```

`ERROR` findings block the pull request. `WARN` findings do not block, but each one should
be fixed or explained. The same command also reports what a deletion or rename breaks
elsewhere in the repository, including references written as HTML — which a search for the
filename in Markdown syntax will not find.

**Step 5: open the pull request** against `Samsung/tizen-docs/master`, and add the
`Review/Requested` label. Keep one pull request to one issue where you can; separate fixes
in unrelated files are easier to review separately. If the change closes an issue, put
`Fixes #Issue_Number` in the description.

A staging site is built for each pull request so you can see the rendered result before it
is published; see [reviewguide/stg_build.md](reviewguide/stg_build.md) for how to find and
refresh that URL.

**Step 6: respond to review.** A maintainer merges the pull request into `master` once the
feedback is applied. On a cadence, `master` is promoted to the `live` branch and your
contribution appears at <https://samsungtizenos.com/docs>.

## File names

- Only lowercase letters, numbers, and hyphens. No spaces or punctuation; use hyphens to
  separate words.
- Use specific action verbs, such as develop, buy, build, troubleshoot. No `-ing` words.
- No small words — leave out a, and, the, in, or.
- Markdown, with the `.md` extension.
- Keep names reasonably short: they become part of the article's URL.

## How to open a pull request

If you are new to GitHub, see [Fork a repo](https://help.github.com/articles/fork-a-repo/)
and [GitHub Flow](https://guides.github.com/introduction/flow/). In short, after forking
<https://github.com/Samsung/tizen-docs>:

```bash
git clone https://github.com/YOUR-USERNAME/tizen-docs.git
cd tizen-docs

# Add the original repository, so you can pull updates into your fork later.
git remote add upstream https://github.com/Samsung/tizen-docs.git

git switch -c my-change            # work on a branch, never on master
# ... edit, then validate as in step 4 above ...
git add <files> && git commit
git push origin my-change
```

Then open the pull request from your branch against `Samsung/tizen-docs/master`.

## DOs and DON'Ts

- **DON'T** surprise us with a large pull request. File an issue and start a discussion so
  we can agree on a direction before you invest a lot of time.
- **DO** write issues and pull requests in English.
- **DO** read the [style guide](styleguide/style.md).
- **DO** use the [template](styleguide/template-guide.md) as the starting point.
- **DO** create a separate branch on your fork before working on the articles.
- **DO** follow the [GitHub Flow workflow](https://guides.github.com/introduction/flow/).
- **DO** blog and tweet about your contributions, frequently!

> **Note**
>
> Some existing pages do not follow every guideline here or in the
> [style guide](styleguide/style.md) yet. We are working towards consistency across the
> site; see the [open issues](https://github.com/Samsung/tizen-docs/issues?q=is%3Aissue+is%3Aopen)
> tracking that.

## Licence and the Contributor License Agreement

Documentation is licensed under
[Creative Commons Attribution 3.0](https://creativecommons.org/licenses/by/3.0/) and code
examples under the [BSD-3-Clause License](https://www.tizen.org/bsd-3-clause-license). See
[content-license.md](content-license.md) for details.

By contributing you agree that your contribution is licensed under those terms. For
background on what that means, see
[Contributor License Agreement](https://en.wikipedia.org/wiki/Contributor_License_Agreement).
