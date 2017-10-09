# gbs import

The subcommand will help to import source code or existing source rpm packages into the git repository. Most of the time, it is used for initializing a git repository or for upgrading packages. It supports these formats: source rpm, specfile, and tarball. For instructions on using the import subcommand, use this command: gbs import --help

```bash
$ gbs import --help
```

### Importing source packages

#### Import from a source rpm

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

#### Import from spec file

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

#### Special options for importing source packages

If the source package contains patches, gbs will try to apply patches on top of master branch:

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

The --no-patch-import option disabled automatic patch import, i.e. gbs does not try to apply patches on top of the master branch. You should apply patches manually or mark them as manually maintained (see [manually maintained patches](https://source.tizen.org/documentation/reference/git-build-system/upstream-tarball-and-patch-generation-support)) With --native command line option you can specify the package as a native package, with no separate upstream. No upstream git branch is created and it is assumed that all content, including packaging files are found in the source tarball inside the source package. Using the --allow-same-version option you can re-import an already imported version of the package. This will not re-import the upstream sources, it'll only re-import the packaging files to the master branch. You can use the --packaging-dir option to define the directory for packaging files, i.e. some other than the default 'packaging/'. This may be needed e.g. if the upstream source sources already have a directory named 'packaging'. If you use this option you sould also define this setting in the package-specific .gbs.conf file (in all relevant branches) so that the remote repository and all other users get the correct setting, too.

### Importing upstream sources

Import tar ball can be used to upgrade a package. gbs import can only work if upstream branch exists. Once gbs importsucceeded, new tar ball will be unpacked and import to upstream branch. If pristine-tar branch exists, tar ball is also be imported to pristine-tar branch.

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

#### Special options for importing upstream sources

If you want to merge imported upstream branch to master automatically, --merge can be used:

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

You can use the --upstream-vcs-tag option in case you track upstream git directly, but still want to import the official release tarballs. Using this option, you get the complete git history of the upstream git in to your upstream branch. And, the diff between the real upstream git tag and the release tarball (e.g. added autotools macros) is shown as one commit on top of the real upstream git tag.

### Common options for importing source packages and upstream sources

This section describes the advanced command line options that are applicable for importing both source packages and upstream source archives. The --upstream-branch option may be used to define the upstream branch name. If you do this, you sould also define that in the package-specific .gbs.conf file (in all relevant branches), similarly to the '--packaging-dir' option. The --no-pristine-tar option disables the use of the pristine-tar tool. That is, gbs will not import the upstream source tarball to pristine-tar branch. With the --filter option one can filter out files from the upstream source archive. For example, you may need to filter out the .git directory from the upstream tarball (with --filter=.git). This option can be given multiple times.