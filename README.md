# Tizen Docs

[![License](https://licensebuttons.net/l/by/3.0/88x31.png)](content-license.md)
[![License](https://img.shields.io/badge/licence-BSD-green.svg?style=flat)](LICENSE-CODE)
[![Build Status](https://jenkins-docs.stg.tizen.org/buildStatus/icon?job=STG_docs_PR_builder&subject=master%20build)](https://jenkins-docs.stg.tizen.org/job/STG_docs_PR_builder/)
[![Build Status](https://jenkins-docs.stg.tizen.org/buildStatus/icon?job=PRD_docs&subject=live%20build)](https://jenkins-docs.stg.tizen.org/job/PRD_docs/)
![Repository Size](https://img.shields.io/github/repo-size/Samsung/tizen-docs)

This repo contains Tizen documents for platform and application developers. 

All files under ./docs/ are hosted on the [Tizen Docs site](https://samsungtizenos.com/docs/bridge/). 

Only add information that is suitable for public release. Do not include credentials,
private contact information, unreleased product details, or other non-public material.

## Repository structure

```
tizen-docs/
├── docs/                       # Published site source (docs.tizen.org)
│   ├── application/            # App developer guides — native, web, dotnet, flutter
│   │   └── */api/               # Generated API reference (HTML). Do not hand-edit.
│   ├── sdk-tools/              # SDK and IDE tooling docs — tizen-studio, vscode-ext,
│   │                            #   vstools, vstools-mac, plus the sdktool-index
│   ├── platform/                # Platform/OS docs — HAL, compliance, porting,
│   │                            #   developing, reference, release-notes, what-is-tizen
│   ├── extensions/tizenx/       # TizenX extension SDK guides + generated API reference
│   └── trademarks.md            # Third-party trademark attribution page
├── styleguide/                  # Writing style and naming-rule references
├── reviewguide/                 # PR reviewer walkthroughs (per content type, stg build)
├── tools/                       # Documentation validator, run before every PR
├── .github/                     # CODEOWNERS, pull request template
└── .claude/skills/tizen-docs/   # Claude Code skill for authoring and review
```

`docs/` mixes hand-written Markdown with generated, versioned API-reference dumps
(HTML/JS/CSS under `*/api/**`). Of the roughly 80,000 tracked files under `docs/`, only
about 1,900 are hand-authored `.md` pages; the rest is generated API reference that must
be fixed upstream, never edited by hand — see
[AGENTS.md](AGENTS.md) for the full rule.

For a directory-by-directory breakdown with file counts, see the skill's
[directory map](.claude/skills/tizen-docs/references/directory-map.md).

## Working with an AI coding agent

Repository-specific instructions for AI coding agents are in
[AGENTS.md](AGENTS.md) and
[`.claude/skills/tizen-docs/SKILL.md`](.claude/skills/tizen-docs/SKILL.md).
They explain the public-content boundary, where documents belong, how to update the
published navigation, and which generated areas must be fixed upstream.

Validate changed documentation before opening a pull request:

```bash
python3 tools/check_docs.py --changed-only --base origin/master
git diff --check
```

`ERROR` findings block the pull request. `WARN` findings do not block, but each
one must be fixed or explained before approval. A successful run always prints
a summary line such as `check_docs: 0 ERROR, 0 WARN (12 files)`; if nothing is
printed at all the validator did not run, so check the `--base` revision.

If the change deletes, renames or moves a document, the same command also
reports what that breaks elsewhere in the repository. See
[`.claude/skills/tizen-docs/SKILL.md`](.claude/skills/tizen-docs/SKILL.md) for
the full workflow, and `python3 tools/check_docs.py --help` for the other
options.


## NOTE

To contribute, see the [Contributing Guide](CONTRIBUTING.md) and the [issues list](https://github.com/Samsung/tizen-docs/issues).

Please take a look at the following instructions before starting.

Write issues and pull requests in English.

### Workflow

We are going to review <span class="labels lh-default d-block d-md-inline">
<a class="d-inline-block IssueLabel" style="background-color: #6ee5bb; color: #000000" title="Push a new commit. It seems like a patch set." href="https://github.com/Samsung/tizen-docs/pulls?q=is%3Apr+is%3Aopen+label%3AReview%2FRequested">Review/Requested</a> PRs.
</span>
1. Contributors have to attach <span class="labels lh-default d-block d-md-inline">
    <a class="d-inline-block IssueLabel" style="background-color: #6ee5bb; color: #000000" title="Push a new commit. It seems like a patch set." href="https://github.com/Samsung/tizen-docs/pulls?q=is%3Apr+is%3Aopen+label%3AReview%2FRequested">Review/Requested</a>, as soon as creating a PR.
    </span>
2. Reviewers have to change the label to <span class="labels lh-default d-block d-md-inline">
            <a class="d-inline-block IssueLabel" style="background-color: #229fa5; color: #000000" title="Asking review for publishing" href="https://github.com/Samsung/tizen-docs/pulls?q=is%3Apr+is%3Aclosed+label%3AReview%2FReviewing">Review/Reviewing</a> when they starts to review a PR.
    </span>
3. When one of reviewers approve a PR, he/she has to update the label to <span class="labels lh-default d-block d-md-inline">
    <a class="d-inline-block IssueLabel" style="background-color: #0523aa; color: #ffffff" title="Ready for publishing" href="https://github.com/Samsung/tizen-docs/pulls?q=is%3Apr+is%3Aopen+label%3AReview%2FScheduled">Review/Scheduled</a>.
    </span>
4. Although the state is <span class="labels lh-default d-block d-md-inline">
    <a class="d-inline-block IssueLabel" style="background-color: #0523aa; color: #ffffff" title="Ready for publishing" href="https://github.com/Samsung/tizen-docs/pulls?q=is%3Apr+is%3Aopen+label%3AReview%2FScheduled">Review/Scheduled</a>
    </span> others can change it to <a class="d-inline-block IssueLabel" style="background-color: #229fa5; color: #000000" title="Asking review for publishing" href="https://github.com/Samsung/tizen-docs/pulls?q=is%3Apr+is%3Aclosed+label%3AReview%2FReviewing">Review/Reviewing</a> when more improvements are needed.

### Naming rules

[**Naming Rules for Tizen Terms**](./styleguide/naming-rules.md) was added. 


### Headings style

Please see the [**Headings style**](./styleguide/style.md#headings).

> ...
>
> Use sentence-style capitalization. Always capitalize:
>
> - The first word of a heading.  
> - The word following a colon in a title or heading (for example, "How to: Sort an array").  
> Headings should be done using atx-style, that is, use 1-6 hash characters (#) at the start of the line to indicate a heading, corresponding to HTML headings levels H1 through H6. Examples of first- and second-level headers are used above.  
>
> ...  


## License

The Tizen documents in this project are licensed under the [Creative Commons Attribution 3.0](https://creativecommons.org/licenses/by/3.0/) License and the Code Examples are under the [BSD-3-Clause License](https://www.tizen.org/bsd-3-clause-license). See [Content License](content-license.md) for more details.
