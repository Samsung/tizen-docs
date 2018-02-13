# gbs devel

Use the `gbs devel` subcommand to facilitate package maintainers in maintaining the packaging branch in the orphan-packaging branch model. The command offers the following actions:

- `start` creates a new development branch with the upstream version embedded in its name.
- `export` exports patches from a development branch to its corresponding packaging branch.
- `drop` removes an unnecessary development branch.
- `switch` switches between the packaging branch and the corresponding development branch.
- `convert` converts a package to the orphan-packaging branch model.

For more information on the 2 maintenance models (orphan-packaging and joint-packaging) and their differences, see [Maintenance Models Supported by GBS](gbs-maintenance-models.md).

For command usage details, enter:

```bash
gbs devel help
```

The following code shows an example workflow:

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

## Action Commands

Synopsis:

```bash
gbs devel [-h] [--packaging-dir PACKAGING_DIR] [--spec SPEC]
               [--upstream-tag UPSTREAM_TAG] [--retain-history]
               [gitdir] <Second_Level_Subcommand>
```

The following example shows the second level subcommands for different actions:

```bash
gbs devel start
gbs devel export
gbs devel switch
gbs devel drop
gbs devel convert
```

The optional `--retain-history` parameter preserves the history of the local changes. In the convert action, for each commit in the old (joint-packaging) branch, this option creates a corresponding commit in the new orphan packaging branch.

To use each action:

- `gbs devel start`

  Creates a development branch by:

  - Using the upstream version as basis to create a local copy.
  - Applying all patches from the packaging branch on top of the local branch.
  - Importing the `.gbs.conf` file from the packaging branch.

  The upstream version is embedded in the development branch name. Thus, when doing a version bump, you must create a new development branch with this command.

  Before using the command, make sure that an orphan-packaging branch (containing all local changes as patches) and the other packaging files are available and ready for use.

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
  >
  > Each upstream version must have a dedicated development branch. In the above example, "development/tizen/1.0" corresponds to the upstream version 1.0.


- `gbs devel export`

  Exports patches to the packaging branch by:

  - Generating patches (one-per-commit) from the development branch.
  - Updating the spec file accordingly.

  > **Note**
  >
  > This command does not automatically commit the changes. The package maintainers must verify the changes and commit them manually.

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

- `gbs devel switch`

  Switches between the packaging branch and the corresponding development branch.

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

- `gbs devel drop`

  Removes the development branch to which the upstream version points.

  You must be on the packaging branch to delete the development branch. Note that the command only removes the development branch that the current (upstream) version points to. For example, assuming the current version is 2.0, if available branches include "development/tizen/1.0" and "development/tizen/2.0", only the latter is removed.

- `gbs convert`

  Converts a package from the joint-packaging maintenance model and Git-layout to the orphan-packaging model by:

  - Using the content of the packaging directory as a basis.
  - Automatically generating patches and putting these into a new orphan packaging branch.

  This command basically contains the output of the GBS export minus the source code tarball.

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

  The convert action only creates the orphan packaging branch. This means that you need to create the development branch separately with the `gbs devel start` command.  


## Using gbs devel with gbs build

The following example shows a recommended procedure that shows how the `gbs devel` and `gbs build` subcommands work together. The "acl" package is used as an example.

1. Show the branch in the joint-packaging model:
   ```bash
   ~/projects/acl[common*]$ git branch* common
   ```

1. Start to switch to the orphan-packaging model by creating the orphan-packaging branch:
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

   Show the branches to check the newly created "common-orphan" packaging branch in the orphan-packaging model:

   ```bash
   ~/projects/acl[common-orphan*]$ git branch
   common
   * common-orphan
   ```

1. Continue to create and check the development branch in the orphan-packaging model:
   ```bash
   ~/projects/acl[common-orphan*]$ gbs devel start
   info: Switching to branch 'development/common-orphan/2.2.51'
   ...
   ~/projects/acl[development/common-orphan/2.2.51*]$ git br
   common
   common-orphan
   * development/common-orphan/2.2.51
   ```

1. Perform local development and then export patches to the packaging branch:
   ```bash
   ~/projects/acl[development/common-orphan/2.2.51*]$ gbs devel export
   info: Exporting patches to packaging branch
   info: On branch 'development/common-orphan/2.2.51', switching to 'common-orphan'
   ...
   no changes added to commit (use "git add" and/or "git commit -a")
   ~/projects/acl[common-orphan*]$
   ```

1. Commit all changes on the packaging branch:
   ```bash
   ~/projects/acl[common-orphan*]$ git add -A && git commit -s
   ```

1. Perform building on the packaging branch:
   ```bash
   ~/projects/acl[common-orphan*]$ gbs build -A <Arch>
   ```

1. Switch to the development branch by using the `gbs devel switch` command:
   ```bash
   ~/projects/acl[common-orphan*]$ gbs devel switch
   ~/projects/acl[development/common-orphan/2.2.51]$
   ```

1. Perform building on the development branch:
   ```bash
   ~/projects/acl[development/common-orphan/2.2.51]$ gbs build -A <Arch>
   ```

   Make changes to the source code and build with uncommitted changes included:

   ```bash
   ~/projects/acl[development/common-orphan/2.2.51]$ gbs build -A <Arch> --include-all
   ```
