# gbs import

Use the `gbs import` subcommand to import source code or existing source RPM packages into the Git repository. Most of the time, this command is used for initializing a Git repository or for upgrading packages.

The import supports the following formats: source rpm, specfile, and tarball.

For command usage details, enter:

```bash
$ gbs import --help
```

The `gbs import` subcommand supports some common options:

- `--upstream-branch` defines the upstream branch name. If you use it, also define the name in the package-specific `.gbs.conf` file (in all relevant branches), so that the remote repository and all other users get the correct setting, too.
- `--no-pristine-tar` disables the use of the pristine-tar tool. It means that GBS does not import the upstream source tarball to the pristine-tar branch.
- `--filter` allows you to filter out files from the upstream source archive. For example, you can filter out the `.git` directory from the upstream tarball (with `--filter=.git`). This option can be given multiple times.

## Importing Source Packages

You can import from:

- Source rpm:

  ```bash
  $ gbs import sed-4.1.5-1/sed-4.1.5-1.src.rpm
  info: No git repository found, creating one.
  Initialized empty Git repository in /home/test/sed/.git/
  info: Tag upstream/4.1.5 not found, importing Upstream upstream sources
  info: Will create missing branch 'upstream'
  pristine-tar: committed sed-4.1.5.tar.gz.delta to branch pristine-tar
  info: Importing packaging files
  info: Will create missing branch 'master'
  info: Version '4.1.5-1' imported under 'sed'
  info: done.
  $ git tag
  upstream/4.1.5
  vendor/4.1.5-1
  $ cd sed && git branch
  * master
    pristine-tar
    upstream
  ```

- Spec file:

  ```bash
  $ gbs import sed-4.1.5-1/sed.spec
  info: No git repository found, creating one.
  Initialized empty Git repository in /home/test/sed/.git/
  info: Tag upstream/4.1.5 not found, importing Upstream upstream sources
  info: Will create missing branch 'upstream'
  pristine-tar: committed sed-4.1.5.tar.gz.delta to branch pristine-tar
  info: Importing packaging files
  info: Will create missing branch 'master'
  info: Version '4.1.5-1' imported under 'sed'
  info: done.
  $ cd sed && git branch
  * master
    pristine-tar
    upstream
  $ git tag
  upstream/4.1.5
  vendor/4.1.5-1
  ```

The source package import supports some special options:

- `--no-patch-import` disables the automatic patch import, so that GBS does not try to apply patches on top of the master branch. Apply patches manually or mark them as manually maintained (see [Manually Maintained Patches](gbs-maintenance-models.md#manually-maintained-patches)).
- `--native` specifies the package as a native package, with no separate upstream. No upstream Git branch is created and it is assumed that all content, including packaging files, are found in the source tarball inside the source package.
- `--allow-same-version` re-imports an already imported version of the package. It does not re-import the upstream sources, but only re-imports the packaging files to the master branch.
- `--packaging-dir` defines the directory for packaging files (default is `packaging/`). This can be needed if the upstream sources already have a directory named `packaging`. If you use this option, also define this setting in the package-specific `.gbs.conf` file (in all relevant branches) so that the remote repository and all other users get the correct setting, too.

If the source package contains patches, GBS tries to apply patches on top of the master branch:

```bash
Source0:    ftp://ftp.gnu.org/pub/gnu/sed/sed-%{version}.tar.gz
Source1001: packaging/sed.manifest
Patch0:     0001-hello.patch
%description
...
$ gbs import sed-patch/sed.spec
info: No git repository found, creating one.
Initialized empty Git repository in /home/test/sed/.git/
info: Tag upstream/4.1.5 not found, importing Upstream upstream sources
info: Will create missing branch 'upstream'
pristine-tar: committed sed-4.1.5.tar.gz.delta to branch pristine-tar
info: Importing packaging files
info: Will create missing branch 'master'
info: Importing patches to 'master' branch
info: Removing imported patch files from spec and packaging dir
info: Version '4.1.5-1' imported under 'sed'
info: done.
$ cd sed && git log --oneline
d94118f Autoremove imported patches from packaging
5d1333f hello
3a452d7 Imported vendor release 4.1.5-1
12104af Imported Upstream version 4.1.5
$ cat packaging/sed.spec
...
URL:        http://sed.sourceforge.net/
Source0:    ftp://ftp.gnu.org/pub/gnu/sed/sed-%{version}.tar.gz
Source1001: packaging/sed.manifest
%description
...
```

## Importing Upstream Sources

An import tar ball can be used to upgrade a package. GBS import only works if the upstream branch exists. Once the import succeeds, the new tar ball is unpacked and imported to the upstream branch. If a pristine-tar branch exists, the tar ball is also imported to that branch.

```bash
$ gbs import ../sed-4.2.0-1/sed-4.2.0.tar.gz
What is the upstream version? [4.2.0]
info: Importing '/home/test/sed-4.2.0-1/sed-4.2.0.tar.gz' to branch 'upstream'...
info: Source package is sed
info: Upstream version is 4.2.0
pristine-tar: committed sed-4.2.0.tar.gz.delta to branch pristine-tar
info: Successfully imported version 4.2.0 of /home/test/sed-4.2.0-1/sed-4.2.0.tar.gz
info: done.
test@test-desktop:~/sed$ git tag
upstream/4.1.5
upstream/4.2.0
$ git log --oneline
 d3d25a7 Imported vendor release 4.1.5-1
 1f6acaa Imported Upstream version 4.1.5
$ git checkout upstream && git log --oneline
 Switched to branch 'upstream'
 23220e6 Imported Upstream version 4.2.0
 1f6acaa Imported Upstream version 4.1.5
$ git checkout pristine-tar && git log --oneline
 Switched to branch 'pristine-tar'
 7d44dad pristine-tar data for sed-4.2.0.tar.gz
 71ee336 pristine-tar data for sed-4.1.5.tar.gz
```

The upstream source import supports some special options:

- `--upstream-vcs-tag` is used in case you track an upstream Git directly, but still want to import the official release tarballs. Using this option, you get the complete Git history of the upstream Git into your upstream branch. The difference between the real upstream Git tag and the release tarball (added autotools macros) is shown as 1 commit on top of the real upstream Git tag.
- `--merge` allows you to merge the imported upstream branch to the master automatically:

  ```bash
  $ gbs import --merge ../sed-4.2.0-1/sed-4.2.0.tar.gz
  What is the upstream version? [4.2.0]
  info: Importing '/home/test/sed-4.2.0-1/sed-4.2.0.tar.gz' to branch 'upstream'...
  info: Source package is sed
  info: Upstream version is 4.2.0
  pristine-tar: committed sed-4.2.0.tar.gz.delta to branch pristine-tar
  info: Merging to 'master'
  Merge made by recursive.
  info: Successfully imported version 4.2.0 of /home/test/sed-4.2.0-1/sed-4.2.0.tar.gz
  info: done.
  $ git log --oneline
   cc58b4c Merge commit 'upstream/4.2.0'
   1f157c3 Imported Upstream version 4.2.0
   482ef23 Imported vendor release 4.1.5-1
   fc76416 Imported Upstream version 4.1.5
  ```
