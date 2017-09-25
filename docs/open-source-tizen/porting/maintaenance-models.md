# Maintenance Models Supported by GBS

## Native and non-native packages

From the package maintenance point of view, we can divide the packages into two categories:

- **Native**: packages where we/you/Tizen is the upstream and controls the source code repository. An example in the context of Tizen could be power-manager. For native packages, we control the versioning and releasing, so package maintenance is simpler. We can release a new version basically whenever we want.
- **Non-native (or upstream)**: packages for which we/you/Tizen is not the upstream. For example, the Linux kernel or zlib. For these packages, we need to follow the releasing process and schedule of the upstream project. For example, from a developer and legal point of view, it is very beneficial to clearly track the local modifications (that is, separate upstream and local changes) both in the source code repository and on the packaging level.

Also GBS divides packages into these two categories. GBS determines a package as non-native, if the git repository has an upstream branch. The actual name of the upstream branch can be configured using the 'upstream_branch' in option in the .gbs.conf file or with --upstream-branch command line option.

GBS build, remotebuild, and export commands behave differently for native and non-native packages. Namely, the preparation of the packaging files for building differs.

GBS currently supports two different maintenance models for non-native packages: one with packaging and source code in the same branch and one with separate packaging and development branches.

### GBS and native packages

GBS simply creates a monolithic source tarball from the HEAD of the current branch. Packaging files, from the packaging directory, are copied as is. No patch generation is done.

The Git repository layout looks like this:

```
         v1.0    v2.0
            |       |
o---A---B---C---D---E   master
```

### GBS and non-native packages: joint-packaging, i.e. packaging and development in the same branch

In the joint-packaging model packaging data (spec file etc) is kept in the same branch with the source code:

```
              F---G---H   master (packaging + code changes)
             /
o---A---B---C---D---E     upstream
            |       |
          v1.0    v2.0
```

GBS tries to create a (real) upstream source tarball, auto-generate patches from the local changes, and auto-update the spec file accordingly. The logic is the following:

- Generate patches
  - Create patches between upstream-tag..HEAD, remove possible old patches
  - Update the spec file: remove old 'Patch:' tags and '%patch' macros and replace them with ones that correspond with the newly generated patches.

- Create upstream tarball if patch-generation was successful
  - If the git repository has pristine-tar branch (and you have the pristine-tar tool installed), GBS tries to checkout the source tarball with pristine-tar
  - If the previous step fails, GBS tries to create a source tarball from the correct upstream tag, matching the version taken from the .spec file.

- If source tarball or patch generation fails GBS reverts back to the old method (that is, treats the package as native), creating just one monolithic tarball without patch generation.

You shouldn't have any pre-existing patches in the packaging directory or spec file. Otherwise, GBS refuses to create patches. Please see Advanced usage/Manually maintained patches section for manually maintained patches.

### GBS and non-native packages: orphan-packaging, i.e. separate packaging and development branches

In the orphan-packaging model packaging data is kept in a separate (orphan) branch with no source code or common history with the code development branch(es):

```
o---I---J---K---L         master (packaging)
 
              F---G---H   development/master/1.0 (local source code changes)
             /
o---A---B---C---D---E     upstream
            |       |
          v1.0    v2.0
```

All packaging data, including patches are stored in the packaging branch. Development branch only contains upstream sources - with no packaging data. The gbs devel command assists in working with the separate branches.

Developers work on the development branch, making changes to the source code. When the package maintainer wants to release a new version of the package, he/she exports changes (with gbs devel one patch per commit) from the development branch to the packaging branch, commits the changes, updates changelog and submits a new version.

When building/exporting the package GBS creates a real upstream source tarball (similar to the joint-packaging model). Patches are auto-generated (and spec file auto-modified) when working on the development branch. When working on the packaging branch the packaging files are exported as is with no modifications.

## Building non-native package in the joint-packaging model

This is pretty straightforward and easy to use. For GBS to see the package as non-native (i.e. enable upstream source tarball and patch generation) you should:

1. have upstream branch in the git repository, with untouched upstream sources
2. have upstream tag format configured correctly in the package specific .gbs.conf, default is upstream/${upstreamversion}
3. have your development branch be based on the upstream version (indicated in .spec)
4. all your local manually maintained patches (in packaging dir) applied in to your development branch and removed from the packaging directory

Additionally, you may have:

1. pristine-tar branch in the git repository for generating the upstream tarball with the pristine-tar tool

Doing development is easy: Just edit/commit/build on your development branch. GBS handles the tarball and patch generation, plus updating the spec file. Running gbs should look something like this (using gbs export as an example here for the shorted output):

```
$ gbs export -o export
info: Generating patches from git (v1.2.7..HEAD)
info: Didn't find any old '%patch' macros, adding new patches after the last '%setup' macro at line %s
info: Didn't find any old 'Patch' tags, adding new patches after the last 'Source' tag.
info: zlib-1.2.7.tar.bz2 does not exist, creating from 'v1.2.7'
info: package files have been exported to:
/home/test/src/zlib/export/zlib-1.2.7-0
```

When trying out the patch generation for the first time, you might want to export first and examine the auto-updated spec file (in the export directory) to see that GBS updated it correctly. Please see Advanced usage/Manually maintained patchessection for manually maintained patches.

Reasons for the upstream tarball and/or patch generation failure may be e.g.

- upstream tag was not found
  - version is not present in your git repository
  - tag format is configured incorrectly

- current branch is not a descendant of the upstream version that it claims to be derived from

## Building non-native package in the orphan-packaging model

In order to use the orphan-packaging model you should:

1. have upstream branch in the git repository, with untouched upstream sources
2. have upstream tag format configured correctly in the package specific .gbs.conf, default is upstream/${upstreamversion}
3. Have an orphan packaging branch that only contains packaging files, including patches
4. Have a development branch which is all patches applied on top of the upstream version

Again, additionally, you may have:

5. pristine-tar branch in the git repository for generating the upstream tarball with the pristine-tar tool

Code development is done on the development branch: just edit/commit/build similarly to the joint-packaging model. However, all packaging changes are done in the packaging branch. And most importantly, submissions (i.e. relesing to integration) are done from the packaging branch. Before submitting, the package maintainer creates patches from from the new changes in the development branch and commits these to the packaging branch. See the **GBS devel** section below for detailed instructions how to manage packaging and development branches with the *gbs devel* command.

## Managing upstream sources

This section is only of interest to the package maintainers.

To maintain packages using the model described above, you need to keep unmodified upstream sources in a separate branch in your git repository. GBS supports two models for this.

### Import upstream source archive to git

In this model, you import source tarballs (or zip files) from the upstream release to your git repository using the gbs import command. GBS commits the sources in the upstream branch and creates a tag for the upstream release. An example of starting from scratch, that is importing to an empty repo:

```
$ mkdir zlib && cd zlib && git init
$ gbs import ../zlib-1.2.6.tar.gz
...
$ git branch
* master
upstream
$ git tag
upstream/1.2.6
```

Now you could start development just by adding packaging files to the master branch. When you need to update to a newer upstream version, just use gbs import again:

```
$ gbs import ../zlib-1.2.7.tar.gz
$ git tag
upstream/1.2.6
upstream/1.2.7
```

**Note**
Currently, GBS automatically merges the new upstream version to your master branch. Thus, you need to update the version number in your spec file accordingly.

### Tracking remote git

In this model, you directly track a remote (git) repository. You shouldn't use GBS import at all. GBS needs to know only the name of the upstream branch and the format of the upstream release tags. These are package dependent information so you should configure them in a package-specific .gbs.conf in the master branch. An example for starting a package from scratch, again:

```
$ git clone git://github.com/madler/zlib.git && cd zlib
$ git branch -m master origin # to keep origin tracking the upstream
$ git checkout -b master
$ vim .gbs.conf
$ git add .gbs.conf && git commit -m"Add gbs.conf"
```

The example configuration file would be:

```
[general]
upstream_branch = origin
upstream_tag = v${upstreamversion}
```

### Pristine-tar support

Optionally (but highly recommended!), you can use pristine-tar for storing/checking out the upstream tarballs (see [http://joeyh.name/code/pristine-tar/](http://joeyh.name/code/pristine-tar/)). You can install it from the Tizen tools repository. Pristine-tar guarantees that the tarball generated by GBS is bit-identical to the real upstream release source tarball. GBS uses pristine-tar automatically if you have pristine-tar installed in your system. If you use GBS import to manage the upstream sources everything works out-of-the box: GBS import automatically commits new tarballs to the pristine-tar branch.

However, if you track a remote upstream repository directly, you need to commit the upstream source tarballs to pristine-tar branch manually. So, like in our zlib example:

```
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

## Converting existing repository to a non-native package

1. You need an upstream branch
 1. If you are already tracking the upstream, just configure the upstream branch name and tag format in the package-specific .gbp.conf.
 2. If not, import upstream source tarball with gbs import or add the upstream remote to your repo and start tracking that.
2. Recommended: If you're tracking the upstream git directly, you may want to do 'pristine-tar commit <tarball> <upstream-tag>'
3. Rebase your current development branch on the correct upstream version (that is, rebase on the upstream tag)
4. Remove all local patches: apply and commit them on top of your development branch and then remove the patches from the packaging directory and preferably from the spec file, too.
5. Optionally, if you want to maintain the package using the orphan-packaging model, you can create the packaging and development branches using the gbs devel convert command.

## Advanced usage

### Manually maintained patches

GBS supports manually maintaining patches, that is, outside the automatic patch generation. This may be needed for architecture-dependent patches, for example, as GBS patch generation does not yet support conditional patches. Another example could be patches that are applied on top of a secondary source tree, whose sources are not maintained in your git tree, but only as a tarball in your packaging directory.

To use this feature, you need to have your patch(es) in the packaging directory and listed in the spec. In addition, you need to mark the patch to be ignored by the patch generation/importing by putting # Gbp-Ignore-Patches: <patch numbers>into the spec file. This will make GBS ignore the 'Patch:' tags and '%patch' macros of the listed patches when importing or generating patches. An excerpt of an example spec file:

```
...
Source0: %{name}-%{version}.tar.bz2
# Gbp-Ignore-Patches: 0
Patch0: my.patch
 
%description
...
```

Actually, you can have this special marker anywhere in the spec file. And, it is case-insensitive, so you might use GBP-IGNORE-PATCHES:, for example, if you like it better. The reason for the GBP prefix is that GBS uses git-buildpackage (gbp) as the backend for patch generation.

**Note**
In addition, pay attention to patch generation when building or exporting. Also gbs import will ignore patches marked for manual maintenance when importing source rpms.

### Patch macro location

GBS tries to automatically find the correct location to add the '%patch' macros in the spec file when updating it with the newly generated patches. This usually works fine, but GBS can also guess wrong. You can manually mark the location for auto-generated '%patch' macros by adding a # Gbp-Patch-Macros marker line into the spec file. An excerpt of an example spec file:

```
...
%prep
%setup
# do things here...
 
# Gbp-Patch-Macros
 
# do more things here...
 
%build
```

GBS will put the new '%patch' macros after the marker line. This marker is case-insensitive, similar to # Gbp-Ignore-Patches.

### Squashing commits

When generating patches, GBS supports squashing a range of commits into one monolithic diff. Currently, one can only squash from upstream-tag up to a given commit-ish. An example use case could be squashing commits from an upstream release up to a stable update into a single diff (commits on top of the stable generate one patches normally). You can enable this with the 'squash_patches_until' config file option or with the '--squash-patches-until' command line option: the format for the option is <commit-ish>[:<filename-base>].

An example:

```
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

**Note**
If you're planning to use this, it is highly recommended that you configure it in the package-specific .gbs.conf file. This way, all users (including the automatic build machinery) build/export the package in a similar way.