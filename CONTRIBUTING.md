# Contributing

Thank you for your interest in contributing to the Tizen documentation!

The document covers the process for contributing to the articles and code samples that are hosted on the [Tizen documentation site](https://docs.tizen.org/). Contributions may be as simple as typo corrections or as complex as new articles.

1.  [Process for contributing](#process-for-contributing)
    1. [Repository structure](#repository-structure)
    1. [File Name](#file-name)
1.  [DOs and DON'Ts](#dos-and-donts)
1.  [Content license](#content-license)
1.  [Contributor License Agreement](#contributor-license-agreement)
1.  [Reference](#reference)


## Process for contributing

You need a basic understanding of [Git and GitHub.com](https://guides.github.com/activities/hello-world/).

**Step 1:** Skip this step for small changes. Open an [issue](https://github.com/Samsung/tizen-docs/issues) describing what you want to do, such as change an existing article or create a new one.
The content inside the **docs** folder is organized into sections that are reflected in the Table of Contents (docs/TOC.md). Define where the topic will be located in the docs/TOC.md. Get feedback on your proposal.

> **Note**
>
> docs/TOC.md has maximum 4th depth. You can use #, ##, ###, and ####. The title with # will be located on GNB(Global Navigation Bar).


You can also look at our [open issues](https://github.com/Samsung/tizen-docs/issues) list and volunteer to work on the ones you're interested in. 

**Step 2:** Fork the `/Samsung/tizen-docs` repo and create a branch for your changes.

For small changes, you can use GitHub's web interface. Simply click the **Edit the file in your fork of this project** on the file you'd like to change. 
GitHub creates the new branch for you when you submit the changes.

**Step 3:** Make the changes on this new branch.

If it's a new topic, you can use this [template file](./styleguide/template-guide.md) as your starting point. It contains the writing guidelines and also explains the metadata required for each article, such as author information.

Navigate to the folder that corresponds to the TOC location determined for your article in step 1.
That folder contains the Markdown files for all articles in that section.
If necessary, create a new folder to place the files for your content. The main article for that section is called *index.md*.
For images and other static resources, create a subfolder called **media** inside the folder that contains your article, if it doesn't already exist. Inside the **media** folder, create a subfolder with the article name (except for the index file).

Be sure to follow the proper Markdown syntax. For more information, see the [style guide](./styleguide/style.md).

### Repository structure

- All markdown files are in the docs folder and various subfolders.
- The docs/index.md file defines the landing (hub) page are it appears on docs.tizen.org (TBD).
- The docs/TOC.md file defines the left-hand navigation panel that appears when you navigate to any page other than the hub page.
- Images are contained within media folders within each subfolder.
- Example structure
  ```
  docs
    /open-source-tizen
      /porting
        porting-overview.md
        /media
          image.png
  ```

### File name

File names use the following rules:
- Contain only lowercase letters, numbers, and hyphens.
- No spaces or punctuation characters. Use the hyphens to separate words and numbers in the file name.
- Use action verbs that are specific, such as develop, buy, build, troubleshoot. No -ing words.
- No small words - don't include a, and, the, in, or, etc.
- Must be in Markdown and use the .md file extension.
- Keep file names reasonably short. They are part of the URL for your articles.

**Step 4:** Submit a Pull Request (PR) from your branch to `Samsung/tizen-docs/master`.

Each PR should usually address one issue at a time. The PR can modify one or multiple files. If you're addressing multiple fixes on different files, separate PRs are preferred.

If your PR is addressing an existing issue, add the `Fixes #Issue_Number` keyword to the commit message or PR description. That way, the issue is automatically closed when the PR is merged. For more information, see [Closing issues via commit messages](https://help.github.com/articles/closing-issues-via-commit-messages/).

The Tizen Document team will review your PR and let you know if there are any other updates/changes necessary in order to approve it.

> **Note**
>
> After you submit PRs to the master branch, you can see your changes on https://docs.stage.tizen.org/staging/{PR #}/ before they are published on the live Tizen Docs site.

**Step 5:** Make any necessary updates to your branch as discussed with the team.

The maintainers will merge your PR into the master branch once feedback has been applied and your change is approved.

On a certain cadence, we push all commits from master branch into the live branch and then you'll be able to see your contribution live at https://docs.tizen.org/.

### How to PR

1. Fork form the original repository, http://github.com/Samsung/tizen-docs.git.
   (Ref. https://help.github.com/articles/fork-a-repo/)

2. Type `git clone`, and then paste the URL you copied in 1. It will look like this, with your GitHub username instead of `YOUR-USERNAME`:
   ```bash
   $ git clone https://github.com/YOUR-USERNAME/tizen-docs.git
   ```
3. Set to synchronize the original repository and the forked repository.
   ```bash
   $ git remote -v
   $ git remote add upstream http://github.com/Samsung/tizen-docs.git
   $ git remote -v
   ```
4. Create a new branch on the forked repository or the local repository,
   and switch to the new branch.
   ```bash
   $ git checkout -b <new branch name>
   ```
5. Create a local commit.
   ```bash
   $ git status
   $ git add
   $ git commit -a
   ```
6. Push the branch
   ```bash
   $ git push origin <new branch name>
   ```
7. Open a pull requst on http://github.com/Samsung/tizen-docs.git.


## DOs and DON'Ts

The following list shows some guiding rules that you should keep in mind when you're contributing to the Tizen documentation:

- **DON'T** surprise us with large pull requests. Instead, file an issue and start a discussion so we can agree on a direction before you invest a large amount of time.
- **DO** read the [style guide](styleguide/style.md) guideline.
- **DO** use the [template](styleguide/template-guide.md) file as the starting point of your work.
- **DO** create a separate branch on your fork before working on the articles.
- **DO** follow the [GitHub Flow workflow](https://guides.github.com/introduction/flow/).
- **DO** blog and tweet (or whatever) about your contributions, frequently!

> **Note**
>
> you might notice that some of the topics are not currently following all the guidelines specified here and on the [style guide](./styleguide/style.md) as well. We're working towards achieving consistency throughout the site. Check the list of [open issues](https://github.com/Samsung/tizen-docs/issues?q=is%3Aissue+is%3Aopen) we're currently tracking for that specific goal.


## Content License

The contents in this project are under the [Creative Commons Attribution 3.0](http://creativecommons.org/licenses/by/3.0/) License or the [BSD-3-Clause License](https://www.tizen.org/bsd-3-clause-license).
For more information, see the [Content License](content-license.md).


## Contributor License Agreement

You can read more about [Contribution License Agreements (CLA)](https://en.wikipedia.org/wiki/Contributor_License_Agreement) on Wikipedia.


## Reference

- https://github.com/dotnet/docs
- https://github.com/NuGet/docs.microsoft.com-nuget
- https://github.com/google/styleguide/
