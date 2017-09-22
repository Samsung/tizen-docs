

# gbs devel

## Name

gbs devel - Facilitates package maintainers to better maintain packaging branch in the orphan-packaging branch model by offering the following actions:

- start - creates new development branch with upstream version embedded in its name.
- export - exports patches from a development branch to its corresponding packaging branch.
- drop - removes unnecessary development branch.
- switch - switches between packaging branch and the corresponding development branch.
- convert - converts a package to the orphan-packaging branch model.

For the difference between the two maintenance models, orphan-packaging and joint-packaging, refer to [Maintenance Models Supported by GBS](https://source.tizen.org/documentation/reference/git-build-system/maintenance-models-supported-gbs).

An indicative example of workflow is shown below:

```bash
# maintainer: create upstream branch and packaging branch (initial packaging)
...
# maintainer: push packaging and upstream branches (and tags) to Git/Gerrit
$ git push --tags origin upstream master
 
# maintainer: start development branch
$ gbs devel start
 
# maintainer: push development branch to Git/Gerrit
$ git push origin development/master/1.0
 
# developer: clone package
$ gbs clone git://review.tizen.org/example.git
 
# developer: modify code, test, commit on development branch
$ ...
$ gbs build
 
# developer: push changes for review
$ git push origin development/master/1.0:refs/for/development/master/1.0
 
# maintainer: after review, merge changes in Gerrit
# maintainer: generate patches, update packaging/release branch
$ gbs devel export
$ git add .
$ git commit -m"New change"
 
# maintainer: push packaging branch for review
$ git push master:refs/for/master
 
# maintainer: once merged, submit for integration
$ gbs submit
```

## Synopsis

- Subcommmand

  ```bash
  gbs devel <Second_Level_Subcommand> [Options]
  ```

- Second Level Subcommands

  ```bash
  gbs devel help
  gbs devel start
  gbs devel export
  gbs devel switch
  gbs devel drop
  gbs devel convert
  ```

## Description

This command facilitates package maintainers to better maintain packaging branch in the orphan-packaging branch model. With a variety of second level subcommands, **gbs devel** enables users to do the following:

- **gbs devel start**

  Creates a development branch by doing the following:

  - using the upstream version as basis to create a local copy
  - applying all patches from the packaging branch on top of the local branch
  - importing the .gbs.conf from the packaging branch

  The upstream version is embedded in the development branch name. Thus, when doing a version bump, one must create a new development branch by using **gbs devel start**.

  Before using **gbs devel start**, besides the other packaging files, an orphan-packaging branch that contains all local changes as patches must be available and ready for use.

  An example is shown below:

  ```bash
  $ git branch
  * tizen
  upstream
  $ gbs devel start
  info: Using 'packaging/dbus.spec' from 'working copy'
  info: Switching to branch 'development/tizen/1.0'
  info: Importing additional file(s) from branch 'tizen' into 'development/tizen/1.0'
  info: Trying to apply patches from branch 'tizen' onto '159fdbf680d2dcdd5f80568c3305e93114caddfa'
  info: Patches listed in 'dbus.spec' imported on 'development/tizen/1.0'
  info: Updating local .gbs.conf
  info: Committing local .gbs.conf to git
  $ git branch
  * development/tizen/1.0
  tizen
  upstream
  ```

  > **Note**
  > Each upsteam version must have a dedicated development branch, in this example, development/tizen/1.0 corresponds to upstream version 1.0.
  ```

  ```

- **gbs devel export**

  Exports patches to the packaging branch by doing the following:

  - generating patches (one-per-commit) from the development branch
  - updating the spec file accordingly

  > **Note**
  > This command doesn't automatically commit the changes, package maintainers need to verify the changes and commit them manually.

  An example is shown below:

  ```bash
  $ git branch
  * development/tizen/1.1
  upstream
  tizen
  $ gbs devel export
  info: Exporting patches to packaging branch
  info: On branch 'development/tizen/1.1', switching to 'tizen'
  info: Generating patches from git (6450890aa002b0868537ee50cc1aea177fdcc941..development/tizen/1.1)
  # On branch tizen
  # Changes not staged for commit:
  # (use "git add/rm <file>..." to update what will be committed)
  # (use "git checkout -- <file>..." to discard changes in working directory)
  #
  # modified: packaging/gbp-test.spec
  #
  # Untracked files:
  # (use "git add <file>..." to include in what will be committed)
  #
  # packaging/0004-New-commit.patch
  no changes added to commit (use "git add" and/or "git commit -a")
  ```

- **gbs devel switch**

  Switches between packaging branch and the corresponding development branch.

  An example is shown below:

  ```bash
  $ git branch
  development/tizen/1.1
  * tizen
  upstream
  $ gbs devel switch
  info: Switching to branch 'development/tizen/1.1'
  $ git branch
  * development/tizen/1.1
  tizen
  upstream
  $ gbs devel switch
  info: Switching to branch 'tizen'
  $ git branch
  development/tizen/1.1
  * tizen
  upstream
  ```

- **gbs devel drop**

  Removes the development branch that the upstream version points to.

  Users must be on the packaging branch to delete the development branch. Note that it only removes the development branch that the current (upstream) version points to, for example, assuming the current version is 2.0, if available branches include development/tizen/1.0 and development/tizen/2.0, only the latter will be removed.

- **gbs convert**

  Converting a package from the joint-packaging maintenance model and git-layout to the orphan-packaging model by doing the following:

  - using the content of the packaging directory as basis
  - automatically generating patches and puts these into a new orphan packaging branch

  Thus, it basically contains the output of gbs export minus the source code tarball.

  With the **--retain-history** option, GBS tries to preserve the history of the local changes. Basically, for each commit in the old (joint-packaging) branch a corresponding commit in the new orphan packaging branch is created.

  An example is shown below:

  ```bash
  $ git branch
  * tizen
  upstream
  $ gbs devel convert
  info: Converting package to orphan-packaging git layout
  info: Importing packaging files from branch 'tizen' to 'tizen-orphan'
  info: Generating patches from git (04e9d5867181807acae3b89f8ebc1f517c246933..d2ab912babf1ee161004b041ca2bd70f3ff7de0c)
  info: Package successfully converted to orphan-packaging.
  info: You're now on the new 'tizen-orphan' packaging branch (the old packaging branch 'tizen' was left intact).
  info: Please check all files and test building the package!
  info: You can now create the development branch with 'gbs devel start'
  $ git branch
  tizen
  * tizen-orphan
  upstream
  ```

  The convert action only create the orphan packaging branch. Thus, you need to create the development branch with gbs devel start.  

## Parameters

### Optional Parameters for Subcommands

```
--retain-history Preserve the history of the local changes.
```

## Using gbs-devel with gbs-build

A recommended procedure that vividly showcases the co-operation of gbs-devel and gbs-build GBS subcommands is shown below, acl package is taken as example here:

1. Show the branch in joint-packaging model.
   ```bash
   ~/projects/acl[common*]$ git branch* common
   ```

2. Start to switch to orphan-packaging model by creating orphan-packaging branch.
   ```bash
   ~/projects/acl[common*]$ gbs devel convert --retain-history
   info: Converting package to orphan-packaging git layout
   info: Importing packaging files from branch 'common' to 'common-orphan'
   ...
   info: You're now on the new 'common-orphan' packaging branch (the old packaging branch 'common' was left intact).
   info: Please check all files and test building the package!
   info: You can now create the development branch with 'gbs devel start'
   ~/projects/acl[common-orphan*]$
   ```

   Show the branches to check the newly created 'common-orphan' packaging branch in orphan-packaging model.

   ```bash
   ~/projects/acl[common-orphan*]$ git branch
   common
   * common-orphan
   ```

3. Continue to create and check the development branch in orphan-packaging model.
   ```bash
   ~/projects/acl[common-orphan*]$ gbs devel start
   info: Switching to branch 'development/common-orphan/2.2.51'
   ...
   ~/projects/acl[development/common-orphan/2.2.51*]$ git br
   common
   common-orphan
   * development/common-orphan/2.2.51
   ```

4. Perform local development and then export patches to packaging branch.
   ```bash
   ~/projects/acl[development/common-orphan/2.2.51*]$ gbs devel export
   info: Exporting patches to packaging branch
   info: On branch 'development/common-orphan/2.2.51', switching to 'common-orphan'
   ...
   no changes added to commit (use "git add" and/or "git commit -a")
   ~/projects/acl[common-orphan*]$
   ```

5. Commit all changes on packaging branch.
   ```bash
   ~/projects/acl[common-orphan*]$ git add -A && git commit -s
   ```

6. Perform building on packaging branch.
   ```bash
   ~/projects/acl[common-orphan*]$ gbs build -A <Arch>
   ```

7. Switch to development branch by using gbs devel switch.
   ```bash
   ~/projects/acl[common-orphan*]$ gbs devel switch
   ~/projects/acl[development/common-orphan/2.2.51]$
   ```

8. Perform building on development branch.
   ```bash
   ~/projects/acl[development/common-orphan/2.2.51]$ gbs build -A <Arch>
   ```

   Make changes to source code and build with uncommitted changes included:

   ```bash
   ~/projects/acl[development/common-orphan/2.2.51]$ gbs build -A <Arch> --include-all
   ```