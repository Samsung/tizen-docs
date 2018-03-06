# Maintenance Models Supported by GBS

From a package maintenance point of view, packages can be divided into 2 categories:

- **Native** packages, where you (Tizen) are the upstream and control the source code repository. An example in the context of Tizen could be power-manager. For native packages, you control the versioning and releasing, so package maintenance is simpler. You can release a new version basically whenever you want.
- **Non-native (or upstream)** packages, for which you (Tizen) are not the upstream. For example, the Linux kernel or zlib. For these packages, you need to follow the releasing process and schedule of the upstream project. For example, from a developer and legal point of view, it is very beneficial to clearly track the local modifications (that is, separate upstream and local changes) both in the source code repository and on the packaging level.

GBS divides packages into these 2 categories. GBS determines a package as non-native, if the Git repository has an upstream branch. The actual name of the upstream branch can be configured using the `upstream_branch`  option in the `.gbs.conf` file or with the `--upstream-branch` command line option.

GBS `build`, `remotebuild`, and `export` commands behave differently for native and non-native packages. Namely, the preparation of the packaging files for building differs.

GBS currently supports 2 different maintenance models for non-native packages: one with packaging and source code in the same branch and one with separate packaging and development branches.

## GBS and Native Packages

GBS simply creates a monolithic source tarball from the HEAD of the current branch. Packaging files, from the packaging directory, are copied as is. No patch generation is done.

The Git repository layout looks like this:

```bash
         v1.0    v2.0
            |       |
o---A---B---C---D---E   master
```

## GBS and Non-native Packages with Joint-packaging

In the joint-packaging model (where packaging and development are in the same branch), packaging data (spec file etc) is kept in the same branch with the source code:

```bash
              F---G---H   master (packaging + code changes)
             /
o---A---B---C---D---E     upstream
            |       |
          v1.0    v2.0
```

GBS tries to create a (real) upstream source tarball, auto-generate patches from the local changes, and auto-update the spec file accordingly. The logic is the following:

- Generate patches
  - Create patches between upstream-tag...HEAD, and remove possible old patches
  - Update the spec file: remove old `Patch:` tags and `%patch` macros and replace them with ones that correspond with the newly generated patches.
- Create an upstream tarball if patch-generation was successful
  - If the Git repository has a pristine-tar branch (and you have the pristine-tar tool installed), GBS tries to checkout the source tarball with pristine-tar.
  - If the previous step fails, GBS tries to create a source tarball from the correct upstream tag, matching the version taken from the `.spec` file.
- If the source tarball or patch generation fails, GBS reverts back to the old method (that is, treats the package as native), creating just 1 monolithic tarball without patch generation.

You cannot have any pre-existing patches in the packaging directory or spec file. Otherwise, GBS refuses to create patches. For information on manually maintained patches, see [Manually Maintained Patches](#manually-maintained-patches).

## GBS and Non-native Packages with Orphan-packaging

In the orphan-packaging model (with separate packaging and development branches), packaging data is kept in a separate (orphan) branch with no source code or common history with the code development branches:

```bash
o---I---J---K---L         master (packaging)

              F---G---H   development/master/1.0 (local source code changes)
             /
o---A---B---C---D---E     upstream
            |       |
          v1.0    v2.0
```

All packaging data, including patches, is stored in the packaging branch. The development branch only contains upstream sources with no packaging data. The `gbs devel` command assists in working with the separate branches.

Developers work on the development branch, making changes to the source code. When the package maintainer wants to release a new version of the package, they export changes (with `gbs devel`, 1 patch per commit) from the development branch to the packaging branch, commit the changes, update the change log, and submit a new version.

When building/exporting the package, GBS creates a real upstream source tarball (similar to the joint-packaging model). Patches are auto-generated (and the spec file auto-modified) when working on the development branch. When working on the packaging branch, the packaging files are exported with no modifications.

## Building in the Joint-packaging Model

For GBS to see the package as non-native (which enables upstream source tarball and patch generation), you need to:

1. Have an upstream branch in the Git repository, with untouched upstream sources.
1. Have the upstream tag format configured correctly in the package-specific `.gbs.conf` file. The default is `upstream/${upstreamversion}`.
1. Have your development branch be based on the upstream version (indicated in the `.spec` file).
1. Have all your local manually maintained patches (in the packaging directory) applied to your development branch and removed from the packaging directory.

Additionally, you can have a pristine-tar branch in the Git repository for generating the upstream tarball with the `pristine-tar` tool.

Edit, commit, and build code on your development branch. GBS handles the tarball and patch generation, as well as updating the `.spec` file. The following example demonstrates how GBS behaves in this situation (`gbs export` is being used as an example here for the truncated output):

```
$ gbs export -o export
info: Generating patches from git (v1.2.7..HEAD)
info: Didn't find any old '%patch' macros, adding new patches after the last '%setup' macro at line %s
info: Didn't find any old 'Patch' tags, adding new patches after the last 'Source' tag.
info: zlib-1.2.7.tar.bz2 does not exist, creating from 'v1.2.7'
info: package files have been exported to:
/home/test/src/zlib/export/zlib-1.2.7-0
```

When trying out the patch generation for the first time, first run the export command and examine the auto-updated spec file in the export directory to ensure that GBS updated it correctly. For information on manually maintained patches, see [Manually Maintained Patches](#manually-maintained-patches).

The upstream tarball and patch generation operation can fail for several reasons:

- Upstream tag was not found
  - Correct version is not present in the Git repository
  - Tag format is configured incorrectly
- Current branch is not a descendant of the upstream version that it claims to be derived from

## Building in the Orphan-packaging Model

In order to use the orphan-packaging model with non-native packages, you need to:

1. Have an upstream branch in the Git repository, with untouched upstream sources.
1. Have the upstream tag format configured correctly in the package-specific `.gbs.conf` file. The default is `upstream/${upstreamversion}`.
1. Have an orphan packaging branch that only contains packaging files, including patches.
1. Have a development branch in which all patches have been applied on top of the upstream version.

Again, additionally, you can have a pristine-tar branch in the Git repository for generating the upstream tarball with the `pristine-tar` tool.

Code development is done on the development branch: edit, commit, and build similarly to the joint-packaging model. However, all packaging changes are done in the packaging branch. And most importantly, submissions (releasing to integration) are done from the packaging branch. Before submitting, the package maintainer creates patches from the new changes in the development branch and commits these to the packaging branch. For more information on how to manage packaging and development branches, see [gbs devel](gbs-devel.md).

## Managing Upstream Sources

To maintain packages using the model described above, you need to keep unmodified upstream sources in a separate branch in your Git repository. GBS supports 2 models for this.

- Import upstream source archive to Git

  In this model, you import source tarballs (or ZIP files) from the upstream release to your Git repository using the `gbs import` command. GBS commits the sources in the upstream branch and creates a tag for the upstream release. An example of starting from scratch, that is importing to an empty repo:

  ```bash
  $ mkdir zlib && cd zlib && git init
  $ gbs import ../zlib-1.2.6.tar.gz
  ...
  $ git branch
  * master
  upstream
  $ git tag
  upstream/1.2.6
  ```

  Now you can start development just by adding packaging files to the master branch. When you need to update to a newer upstream version, use the `gbs import` command again:

  ```bash
  $ gbs import ../zlib-1.2.7.tar.gz
  $ git tag
  upstream/1.2.6
  upstream/1.2.7
  ```

  > **Note**
  >
  > Currently, GBS automatically merges the new upstream version to your master branch. You need to update the version number in your spec file accordingly.

- Track the remote Git

  In this model, you directly track a remote (Git) repository and the `gbs import` command is not used. GBS needs to know only the name of the upstream branch and the format of the upstream release tags. These are package-dependent information so you must configure them in a package-specific `.gbs.conf` in the master branch. For example, to start a package from scratch:

  ```bash
  $ git clone git://github.com/madler/zlib.git && cd zlib
  $ git branch -m master origin # to keep origin tracking the upstream
  $ git checkout -b master
  $ vim .gbs.conf
  $ git add .gbs.conf && git commit -m"Add gbs.conf"
  ```

  The example `.gbs.conf` configuration file is:

  ```
  [general]
  upstream_branch = origin
  upstream_tag = v${upstreamversion}
  ```

### Pristine-tar Support

You can use the `pristine-tar` for storing and checking out the upstream tarballs (see [http://joeyh.name/code/pristine-tar/](http://joeyh.name/code/pristine-tar/)). You can install `pristine-tar` from the Tizen tools repository. The tool guarantees that the tarball generated by GBS is bit-identical to the real upstream release source tarball. GBS uses `pristine-tar` automatically if you have it installed on your system. If you use `gbs import` to manage the upstream sources, it automatically commits new tarballs to the pristine-tar branch.

> **Note**
>
> The use of the `pristine-tar` tool is optional, but highly recommended.

However, if you track a remote upstream repository directly, you need to commit the upstream source tarballs to the pristine-tar branch manually. For example:

```bash
$ cd zlib
$ git branch
* master
origin
$ pristine-tar commit ../zlib-1.2.7.tar.gz v1.2.7
$ git branch
* master
origin
pristine-tar
```

## Converting an Existing Repository to a Non-native Package

To convert an existing repository to a non-native package:

1. An upstream branch is required:
   - If you are already tracking the upstream, just configure the upstream branch name and tag format in the package-specific `.gbp.conf` file.
   - If not, import the upstream source tarball with `gbs import` or add the upstream remote to your repository and start tracking that.
   > **Tip**:
   >
   > If you are tracking the upstream Git directly, consider running the `pristine-tar commit <tarball> <upstream-tag>` command.
1. Rebase your current development branch on the correct upstream version (that is, rebase on the upstream tag).
1. Remove all local patches: apply and commit them on top of your development branch and then remove the patches from the packaging directory and preferably from the spec file, too.
1. Optionally, if you want to maintain the package using the orphan-packaging model, you can create the packaging and development branches using the `gbs devel convert` command.

## Advanced Usage

<a name="manually-maintained-patches"></a>
### Manually Maintained Patches

GBS supports patches that are maintained manually, outside the automatic patch generation. This can be needed for architecture-dependent patches, for example, as GBS patch generation does not yet support conditional patches. Another example are patches that are applied on top of a secondary source tree, whose sources are not maintained in your Git tree, but only as a tarball in your packaging directory.

To use this feature, you must have your patches in the packaging directory and listed in the spec file. In addition, you must mark the patch to be ignored by the patch generation/importing by putting the `# Gbp-Ignore-Patches: <patch numbers>` line into the spec file. This makes GBS ignore the `Patch:` tags and `%patch` macros of the listed patches when importing or generating patches. An excerpt of an example spec file:

```
...
Source0: %{name}-%{version}.tar.bz2
# Gbp-Ignore-Patches: 0
Patch0: my.patch

%description
...
```

The `Gbp-Ignore-Patches` marker can be placed anywhere in the file, and is case-insensitive. The GBP prefix comes from git-buildpackage (gbp), which is used by GBS as the backend for patch generation.

> **Note**
>
> Pay attention to patch generation when building or exporting. The `gbs import` tool also ignores patches marked for manual maintenance when importing source RPMs.

### Patch Macro Location

GBS tries to automatically find the correct location to add the `%patch` macros in the spec file when updating it with the newly generated patches. This is usually successful, but GBS can also guess wrong. You can manually mark the location for auto-generated `%patch` macros by adding a `# Gbp-Patch-Macros` marker line into the spec file:

```
...
%prep
%setup
# do things here...

# Gbp-Patch-Macros

# do more things here...

%build
```

GBS places the new `%patch` macros after the marker line. This marker is case-insensitive, similar to `# Gbp-Ignore-Patches`.

### Squashing Commits

When generating patches, GBS supports squashing several commits into 1 monolithic diff. Currently, you can only squash from upstream-tag up to a given commit-ish. An example use case is squashing commits from an upstream release up to a stable update into a single diff (commits on top of the stable generate multiple patches normally). You can enable this with the `squash_patches_until` config file option or with the `--squash-patches-until` command line option: the format for the option is `<commit-ish>[:<filename-base>]`.

For example:

```bash
$ git branch
* master
stable
upstream
$ gbs export --squash-patches-until=stable:stable-update
info: Generating patches from git (upstream/0.1.2..HEAD)
info: Squashing commits a2a7d82..9c0f5ba into one monolithic 'stable-update.diff'
info: Didn't find any old 'Patch' tags, adding new patches after the last 'Source' tag.
info: Didn't find any old '%patch' macros, adding new patches after the last '%setup' macro
info: mypackage-0.1.2.tar.gz does not exist, creating from 'upstream/0.1.2'
info: package files have been exported to:
/home/user/src/mypackage/packaging/mypackage-0.1.2-1.21
```

> **Note**
>
> If you are planning to use this feature, configure it in the package-specific `.gbs.conf` file. This way, all users (including the automatic build machinery) build and export the package in a similar way.
