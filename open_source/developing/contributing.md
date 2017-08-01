# Contributing Code to Tizen

This topic provides information about how to contribute code to Tizen, including the following:

- Cloning source files over SSH
- Submitting a patch to Gerrit
- Reviewing a patch on Gerrit
- Submitting a package to the build system
- Reviewing and accepting a package on the build server (for release engineer only)

For more information about the whole work process, see [Tizen Development Working Mechanism](https://source.tizen.org/documentation/developer-guide/getting-started-guide/tizen-development-working-mechanism).

## Source Files Cloning over SSH

To clone source files for a specific project, see [Cloning Tizen Source Files](https://source.tizen.org/documentation/developer-guide/getting-started-guide/cloning-tizen-source).

## Patch Submission and Review on Gerrit

You can perform patch submission and review on Gerrit.

### Submitting a Patch to Gerrit

To submit a patch to Gerrit:

1. Switch to the project directory and perform local development.

2. Stage the revised content by executing the following command:

   ```
   $ git add <Revised_File>...
   ```

3. Commit the revised content by executing the following command:

   ```
   $ git commit
   ```

4. Push the patch to Gerrit by executing the following command:

   ```
   $ git push origin HEAD:refs/for/<remote_branch_name>
   ```

   **Note:** Valid values for <remote_branch_name> are:

   - **tizen**: corresponds to the branch of the latest Tizen version
   - **tizen_3.0**: corresponds to the Tizen 3.0 branch

For more information, see [Gerrit Documentation](https://review.tizen.org/gerrit/Documentation/index.html).

### Reviewing a Patch on Gerrit

To review a patch in the Gerrit Web GUI, publish the comments and vote for the patch.

The patch is merged or discarded depending on the voting results.The merge is performed if:

- The patch has at least one "+2" score and no "-2" score in the Code Review category.
- The patch has at least one "+1" score and no "-1" score in the Verified category.

**Note:** Voting "+2" requires a proper privilege level.

When a patch meets the above criteria, privileged users can submit to merge the patch to the Git repository.

## Package Submission and Review on the Build System

You can perform package submission, and, if you are a release engineer, review and accept the changes on the build system side.

### Submitting Packages to the Build System

You can submit a single package or a group of packages.

#### Submitting a Single Package

To submit a package to the build system, execute the following command:

```
$ gbs submit [-c <Commit_ID>] -m "<Comments>"
```

During the submission, the GBS automatically creates an annotated tag in the following format:

```
submit/$Tizen_Version/$(%Y%m%d.%H%M%S)
```

If the code change has already been merged in Gerrit, a merge request is created and release engineers are notified to review.

**Note:** If the patch has not been merged in Gerrit, the backend services abort the operation and send an email to the patch owner, to notify that the patch needs to be re-submitted after it is merged.

#### Submitting a Group of Packages

If multiple changed packages have mutual dependencies, they must be submitted as a group. This means that all of the packages must be submitted with one unified identification, through a process known as **group submission**.

This feature is supported by the collaboration of the Tizen client development tool (GBS) and Tizen backend services.

For the platform developers, GBS provides the `--tag <TAG>` option, to accept a developer specified "TAG" for the `gbs submit` command. All submissions for multiple packages with the same TAG are considered as a group, and packages in the same group are handled in the build system together.

For example, assume that "ail", a low level library, depends on "aul". "ail" developers have changed some APIs, and "aul" must be updated to adapt to the new API changes in "ail". Therefore, once all related patches have been merged to "ail" and "aul" separately, these two packages must be submitted as a group:

1. Submit one of the packages in the group to create a tag:

   ```
   $ cd platform/core/appfw/aul-1/$ gbs submit -m "<Comments>"
   ```

2. Obtain the tag name from the output of the above command, and use the same tag as a `--tag` parameter for other packages in the group:

   ```
   $ cd platform/core/appfw/ail/$ gbs submit --tag <same_tag> -m "<Comments>"
   ```

You can also specify the tag yourself, and use the same tag for all packages in the package group. In this case, the tag must follow the usual tag format with an optional suffix:

```
submit/$Tizen_Version/$(%Y%m%d.%H%M%S).N (N is a number you can choose freely)
```

Tizen backend services take care of all submissions with the same tag, and build them together.

### Reviewing a Package on the Build Server (for Release Engineers Only)

After a developer runs the `gbs submit` command, Tizen back-end service starts the pre-release and normal release processes at the same time. During the pre-release process, packages and Tizen images with a specific package inside are presented to release engineers and Quality Assurance (QA) engineers for review.

QA engineers are responsible for testing packages as isolated objects, as well as verifying Tizen images with a specific package inside to offer release engineers comprehensive information to make appropriate decision about whether to accept or reject a package, including the following:

- Whether the package impacts other dependent package builds.
- Whether the package brings in new bugs.
- Whether the package causes regression issues.
- Whether the package influences the performance of the Tizen image.

After the packages are accepted by release engineers, the corresponding images are automatically created by the normal release process and can be obtained on [http://download.tizen.org/releases/daily](http://download.tizen.org/releases/daily).