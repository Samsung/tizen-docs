# Tizen Development Work Flow

## System Introduction

### SCM

The Source Code Management (SCM) system consists of these two parts:

- **Git.** A particularly powerful, flexible, and low-overhead version control system that makes collaborative development efficient and robust. For more information, refer to these resources:

  -[Git Community Book](http://git-scm.com/book)

  -[Git Wiki](https://git.wiki.kernel.org/index.php/Main_Page)

  -[Git Manual Page](https://www.kernel.org/pub/software/scm/git/docs/)

- **Gerrit.** A web-based code review system, facilitating online code reviews for projects using Git version control system. By showing changes in a side-by-side display and supporting inline comments, Gerrit optimizes the code review process, enhancing review quality. Furthermore, by permitting any authorized user to submit changes to the central Git repository, Gerrit simplifies the maintenance of the Git-based projects, enabling a more centralized use of Git.

### OBS

The Open Build Service (OBS) is an open and complete distribution development platform that provides the infrastructure for developers to easily create and release open source software for various Linux distributions on different hardware architectures. In addition, the OBS delivers a collaborative environment that enables developer groups to build and submit changes to other projects.

For more information, refer to the following resources:

- [Open Build Service](http://openbuildservice.org/)
- [Build Service (openSUSE)](http://en.opensuse.org/openSUSE:Build_Service)


## Git Branches

A given project in the Git repository has two possible branches: master branch and upstream branch.

**Note:** Master branch is mandatory, whereas upstream branch is optional. For detailed reasons, refer to the respective bullet list item below.

- **Master Branch (Mandatory)**

Git introduces the master branch (also known as development branch) during the initialization of a repository, thus the default branch in a repository is master branch and most developers keep the repository's most robust and dependable line of development on the master branch.

That is, the master branch hosts each project's full source tree (for example, C/C++, .h, makefile, etc.), including upstream source and Tizen local changes. Though master branch can be renamed or even deleted, it's best practice to regard it as mandatory and leave as is.

**Note:** Developers are responsible for maintaining the packaging changelog within the "/packaging" folder of each Git tree.

- **Upstream Branch (Optional)**

When talking about two repositories that have been cloned one from the other, the parent repository is commonly referred to as being "upstream".

This conventional concept applies to the "upstream branch", as well. More specifically, a parent branch is referred to as the "upstream branch" on which developers base their Git projects. Upstream branch becomes optional in the following scenarios:

- The project only involves purely native code from Tizen and has no upstream project to base on.
- The project does not need to track the latest update of the upstream project.


## Roles and Responsibilities

### Developers

Developers' responsibilities are:

- Write and submit code to the development branch of a Git project.
- Verify and review (vote "+1" or "-1") code changes for any project on any branch.

### Maintainers

Maintainers' responsibilities are:

- Create additional branches, such as upstream, development branch to profile projects.
- Rebase master branch to upstream branch.
- Review code, as well as approve (vote "+2") or reject (vote "-2") patches.

Guidelines for maintainers are:

- Despite the granted power, maintainers must not accept their own changes without passing peer review ("+1") or ("+2").
- The force push right is granted for maintainers to handle code rebase. Maintainers must not abuse the right to hide patch submissions that are supposed to be reviewed.

### Reviewers

Reviewers' responsibility is:

- Review code, as well as approve (vote "+2") or reject (vote "-2") patches.

### Release Engineers

Release Engineers' responsibilities are:

- Approve submission to OBS.
- Perform smoke-test of the resulting image and then transfer to the release area for QA engineers to perform further test.

### QA Engineers

QA Engineers' responsibility is:

- Perform thorough integration and verification of the image to eliminate regressions and bugs.



### Package Development Work Flow

The package development workflow is described in the following procedure and shown in the figure below:

![img](https://source.tizen.org/sites/default/files/users/user-1132/800px-tizen-work-flow.png)

1. Developers set up the development environment and install the development tools.

2. Developers clone the source code, do required development, and perform local verification through local build.

3. Developers submit patches to the Gerrit for all stakeholders to review.

4. Tizen back-end service and reviewers verify the patches through automated and manual testing, respectively, and then vote -1, 0, or +1 based on the quality of the patches.

   - Automated testing: Tizen back-end service automatically submits patches to the OBS to perform remote build and then posts the test results back to the Gerrit.
   - Manual testing: Testers verify the patches manually and then publish comments on the Gerrit.

5. Maintainers approve the patches (Code-Review +2) after they pass verifications (Verified +1) and then merge code changes to the Gerrit repository.

6. Maintainers/Developers submit packages to the OBS by using **gbs submit** command.

   **Note:** It's best practice to always have a maintainer role for every Tizen project, and maintainers should submit pakcages to the OBS as soon as all merged packages are ready for submission in order to prevent possible omission.

7. Tizen back-end service activates pre-release and normal release processes at the same time. During the pre-release process, Tizen images that incoporates specific packages are created and submitted to release engineers to review.

8. Release engineers accept or reject submissions based on the quality of the packages. For accepted submissions, the corresponding source code will be merged into the OBS repository, meanwhile, the normal release process takes over and publishes repos together with Tizen images.


### Package Generation

After submiting code from a source repository to the OBS, the backend generates the package file in the required format, as following step:

1. Create a tarball
   Create the tarball using 'git-archive'. The ‘/packaging’ directory must included in the tarball, as well.
   The tarball version is abstracted from the spec file by ‘rpmbuild’.
2. Take the contents of the packaging directory and put them alongside the tarball.

The package files in the required forma are shown in the figure below.

![img](https://source.tizen.org/sites/default/files/users/user-1132/700px-package-generation.png)

