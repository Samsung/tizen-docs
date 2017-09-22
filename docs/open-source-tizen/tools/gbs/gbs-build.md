# gbs build

By using 'gbs build', the developer can build the source code and generate rpm packages locally. For instructions on using the build subcommand, use this command: gbs build --help

```bash
$ gbs build -h
```

### gbs build workflow

#### Input of gbs build

Below is the input for gbs build:

- git project(s) which contains rpm packaging files
- binary rpm repositories (remote or local)
- project build configurations (macros, flags, etc)

The binary rpm repositories contain all the binary rpm packages which are used to create the chroot environment and build packages, which can be remote, like tizen release or snapshot repositories, or local repository. Local repository supports two types:

- A standard repository with repodata exists
- A normal directory contains RPM packages. GBS will find all RPM packages under this directory.

Please refer to [Configuration File](https://source.tizen.org/documentation/reference/git-build-system/configuration-file) part to configure a repository.

#### Build workflow

The input and output of gbs build are all repositories.

**Note**: All the rpm packages under the output repository (by default, ~/GBS-ROOT/local/repos/<VERSION>/) will be used when building packages. That is, all the packages under the output repository will be applied to the build environment, so make sure the output repository is clean if you don't want this behavior.

Here's the basic gbs build workflow

```
 ____________________
|                    |      ___________
| Source Code (GIT)  |---->|           |      _________________________
|____________________|     |           |     |                         |
 ____________________      |           |     |  Local repository of    |
|                    |     |           |     |                         |
|    Build config    |---->| GBS build |---->|                         |
|____________________|     |           |     |                         |
 ____________________      |           |     |  build RPM packages     |
|                    |     |           |     |(~/GBS-ROOT/local/repos/)|
|Binary repositories |     |           |     |_________________________|
|in GBS conf         |---->|___________|                  |
|(Remote or Local)   |           ^                        |
|____________________|           |________________________|
```

From the above diagram, we can see the input and input are all repositories and the output repository located at '~/GBS-ROOT/locals/repos/' by default. You can change the repo path by using '--buildroot' to specify a different build root.

Local repos in gbs build root ('~/GBS-ROOT' by default) will affect build results, so you must make sure that repos don't contains old or unnecessary RPM packages. While running gbs build, you can specify '--clean-repos' to clean up local repos, which gbs created, before building. We recommend that gbs users set different gbs build root directories for different profiles. There are several ways:

- By default, the GBS build will put all output files under ~/GBS-ROOT/.
- If the environment variable TIZEN_BUILD_ROOT exists, ${TIZEN_BUILD_ROOT} will be used as output top dir
- If -B option is specified, then the specified directory is used, even if ${TIZEN_BUILD_ROOT} exists

#### Output of gbs build

Structure of a GBS build root directory

```bash
gbs output top dir
|-- local
| |-- cache # repodata and RPMs from remote repositories
| |-- repos # generated local repo top directory
| | |-- tizen # distro one: tizen
| | | |-- armv7l # store armv7l RPM packages
| | | |-- i586 # store x86 RPM packages
| | `-- tizen2.0 # build for distro two: tizen2.0
| | `-- i586 # the same as above
| |-- scratch.armv7l.0 # first build root for arm build
| |-- scratch.i586.0 # second build root for x86 build
| |-- scratch.i586.1 # third build root for x86 build
| |-- scratch.i586.2 # fourth build root for x86 build
| |-- scratch.i586.3 # fifth build root for x86 build
| | # The above build root dir can be used by gbs chroot <build root dir>
| `-- sources # sources generated for build, including tarball, spec, patches, etc.
| |-- tizen
| `-- tizen2.0
`-- meta # meta data used by gbs
```

### GBS Build Examples (Basic Usage)

1. Build a single package.
  ```bash
  $ cd package1$ gbs build -A i586
  ```

2. Build a package for different architectures.
   > **Note**
   > Supported architectures include: x86_64, i586, armv6l, armv7hl, armv7l, aarch64, mips, mipsel.

  ```bash
  $ gbs build -A armv7l #build package for armv7l$ gbs build -A i586 #build package for i586
  ```

3. Make a clean build by deleting the old build root. This option must be specified if the repo has been changed, for example, changed to another release.

  ```bash
  $ gbs build -A armv7l --clean
  ```

4. Build the package with a specific commit.
  ```bash
  $ gbs build -A armv7l --commit=<COMMIT_ID>
  ```

5. Use --overwrite to trigger a rebuild.
  If you have already built before, and want to rebuild, --overwrite should be specified, or the packages will be skipped.
  ```bash
  $ gbs build -A i586 --overwrite
  ```

  If you change the commit or specify --include-all option, it will always rebuild, so --overwrite is not needed.

6. Output the debug info.
  ```bash
  $ gbs build -A i586 --debug
  ```

7. Build against a local repository. You can config the local repo at .gbs.conf file or through the command line.
  ```bash
  $ gbs build -R /path/to/repo/dir/ -A i586
  ```

8. Use --noinit to build package in offline mode --noinit option can only be used if build root is ready. With --noinitoption, gbs will not connect the remote repo, and skip parsing & checking repo and initialize build environment. rpmbuildwill be used to build the package directly. Here's an example:

  ```bash
  $ gbs build -A i586 # build first and create build environment
  $ gbs build -A i586 --noinit # use --noinit to start building directly
  ```

9. Build with all uncommitted changes using --include-all.
  For example, the git tree contains one modified file and two extra files:
  ```bash
  $ git status -s
  M ail.pc.in
  ?? base.repo
  ?? main.repo
  ```
  - Build without the --include-all option

    Builds committed files only. All the modified files, which are not committed nor added, will NOT be built:

    ```bash
    $ gbs build -A i586
    warning: the following untracked files would NOT be included: base.repo main.repo
    warning: the following uncommitted changes would NOT be included: ail.pc.in
    warning: you can specify '--include-all' option to include these uncommitted and untracked files.
    ....
    info: Binaries RPM packages can be found here:
    /home/test/GBS-ROOT/local/scratch.i586.0/home/abuild/rpmbuild/RPMS/
    info: Done
    ```

  - Build with the --include-all option builds all the files:
    ```bash
    $ gbs build -A i586
    warning: the following untracked files would NOT be included: base.repo main.repo
    warning: the following uncommitted changes would NOT be included: ail.pc.in
    warning: you can specify '--include-all' option to include these uncommitted and untracked files.
    ....
    info: Binaries RPM packages can be found here:
    /home/test/GBS-ROOT/local/scratch.i586.0/home/abuild/rpmbuild/RPMS/
    info: Done
    ```
  - Use .gitignore to ignore specific files, when using the --include-all option. If you want to ignore some files types, you can update your .gitignore. For example:

    ```bash
    $ cat .gitignore
    .*
    */.*
    *.pyc
    *.patch*
    ```

### Incremental build

#### Incremental Concept

Starting from gbs 0.10, the gbs build subcommand supports building incrementally, which can be enabled by specifying the '--incremental' option.

This mode is designed for development and verification of single packages. It is not intended to replace the standard mode. Only one package can be built at a time using this mode.

This mode will set up the build environment in multiple steps, finishing by mounting the local Git tree of a package in the chroot build environment.

**Note**: Because gbs will mount your git tree to the build root, be very careful when you remove your build root. You need to make sure you've already umounted the source tree manually before you remove it.

This has the following benefits:

1. The build environment uses the latest source code and changes to source do not trigger a new build environment (in the chroot).
2. The Git source tree becomes the source of the builds. Any change made in the Git repository followed by invocation of the build script will build the changed sources
3. If the build fails for some reason, the build script will continue from the spot where it has failed, once the code has been changed to fix the problem causing the failure.

This mode is, in many ways, similar to traditional code development, where changes are made to sources, followed by running make to test and compile the changes. However, it enables development using the build environment of the target, instead of the host OS.

This method has some limitations, mostly related to packaging and how the sources are maintained. Among others, it depends on how the RPM spec file is composed:

1. It does not support patches in the spec file. All source has to be maintained as part of the Git tree

2. It requires a clean packaging workflow. Exotic workflows in the spec files might not work well, because this mode expects the following model:

   1. Code preparation (%prep)
   2. Code building (%build)
   3. Code installation (%install)

3. Because we run the %build section every time, if the %build script has configuration scripts (auto-tools), binaries might be regenerated, causing a complete build every time. To avoid this, you are encouraged to use the following macros, which can be overridden using the --no-configure option:
   %configure: runs the configure script with pre-defined paths and options.%reconfigure: regenerates the scripts and runs %configure%autogen: runs the autogen script

#### Example

In this example, we use dlog source code. First, we need to build with --incremental, then just modify one source file, and trigger the incremental build again. We will see that only modified source code has been compiled during the incremental build.

```bash
$ cd dlog
# first build:
$ gbs build -A i586 --incremental
$ vim log.c # change code
# second build:
$ gbs build -A i586 --incremental
info: generate repositories ...
info: build conf has been downloaded at:
/var/tmp/test-gbs/tizen.conf
info: Start building packages from: /home/test/packages/dlog (git)
info: Prepare sources...
info: Retrieving repo metadata...
info: Parsing package data...
info: *** overwriting dlog-0.4.1-5.1 i586 ***
info: Next pass:
dlog
info: *** building dlog-0.4.1-5.1 i586 tizen (worker: 0) ***
info: Doing incremental build
[ 0s] Memory limit set to 10854336KB
[ 0s] Using BUILD_ROOT=/home/test/GBS-ROOT/local/scratch.i586.0
[ 0s] Using BUILD_ARCH=i686:i586:i486:i386:noarch
[ 0s] test-desktop started "build dlog.spec" at Thu Sep 13 07:36:14 UTC 2012.
[ 0s] -----------------------------------------------------------------
[ 0s] ----- building dlog.spec (user abuild)
[ 0s] -----------------------------------------------------------------
[ 0s] -----------------------------------------------------------------
[ 0s] + rpmbuild --short-circuit -bc /home/abuild/rpmbuild/SOURCES/dlog.spec
[ 0s] Executing(%build): /bin/sh -e /var/tmp/rpm-tmp.XLz8je
[ 0s] + umask 022
[ 0s] + export LD_AS_NEEDED
[ 4s] + make -j4
[ 4s] make all-am
[ 4s] make[1]: Entering directory /home/abuild/rpmbuild/BUILD/dlog-0.4.1
[ 4s] /bin/sh ./libtool --tag=CC --mode=compile gcc -c -o log.lo log.c
[ 4s] mv -f .deps/log.Tpo .deps/log.Plo
[ 4s] /bin/sh ./libtool --tag=CC --mode=link gcc -o libdlog.la /usr/lib log.lo
[ 4s] libtool: link: gcc -shared .libs/log.o -o .libs/libdlog.so.0.0.0
[ 4s] libtool: link: ar cru .libs/libdlog.a log.o
[ 4s] libtool: link: ranlib .libs/libdlog.a
[ 4s] make[1]: Leaving directory /home/abuild/rpmbuild/BUILD/dlog-0.4.1
[ 4s] + exit 0
[ 4s] finished "build dlog.spec" at Thu Sep 13 07:36:18 UTC 2012.
[ 4s]
info: finished incremental building dlog
info: Local repo can be found here:
/home/test/GBS-ROOT/local/repos/tizen/
info: Done
```

From the buildlog, we can see that only log.c has been re-compiled. That's the incremental build behavior.

--noinit option can be used together with --incremental to make a build more quickly, like:

```bash
$ gbs build --incremental --noinit
```

#### Limitations of Incremental Build

Incremental build doesn't support all packages. Here are some limitations:

- Incremental build currently supports building only a single package. It doesn't support building multiple packages in parallel
- The tarball's name in the spec file should be %{name}-%{version}.{tar.gz|tar.bz2|zip|...}, otherwise GBS can't mount source code to build the root correctly
- %prep section should only contains %setup macro to unpack tarball, and should not contains other source code related operations, such as unpack another source, apply patches, etc.

### Multiple packages build (dependency build)

Multiple package build has been supported since gbs 0.10. If packages have dependencies on each other, gbs will build packages in the correct order calculated by dependency relationship. Previously built out RPMs will be used to build the following packages that depend on them, which is the dependency build.

**Examples**:

1. Build all packages under a specified package directory

  ```bash
  $ mkdir tizen-packages
  $ cp package1 package2 package3 ... tizen-packages/
  $ gbs build -A i586 tizen-packages # build all packages under tizen-packages
  ```

2. Build multiple packages in parallel with --threads

  ```bash
  # current directory have multiple packages, --threads can be used to set the max build worker at the same time
  $ gbs build -A armv7l --threads=4
  ```

3. Select a group of packages to be built

  The --binary-from-file option specifies a text file that contains a name list of RPM packages to be built. The format in the text file is one package per line.

  The --binary-list option specifies a list in which the package names are separated by comma.

  When the number of packages is small, thus the packages can be clearly presented in command line, it is recommended to use the --binary-list option for simplicity.

  ```bash
  $ gbs build -A i586 --binary-from-file=/path/to/packages.list
  $ gbs build -A i586 --binary-list=<pkg1>,<pkg2>
  ```

4. Exclude certain packages.

  The --exclude option specifies a list in which the names of packages to be ignored are separated by comma. The --exclude-from-file option specifies a text file that contains a name list of packages to be ignored.

  ```bash
  $ gbs build -A i586 tizen-packages --exclude=<pkg1>$ gbs build -A i586 tizen-packages --exclude=<pkg1>,<pkg2>$ gbs build -A i586 tizen-packages --exclude-from-file=/path/to/packages.list
  ```

5. Build packages based on dependencies. The --deps option enables GBS to build specific packages, together with all the related packages on which they depend.The --rdep option enables GBS to build specific packages, together with all the related packages that depend on them.

  The specific packages can be included by the --binary-from-file option or the --binary-list option, and be excluded by the --exclude option or the --exclude-from-file option.

  These two options are compatible. When added at the same time, besides the specific packages, GBS will build not only the related packages on which they depend, but also all the related packages that depend on them.

  ```bash
  $ gbs build -A i586 --binary-list=<pkg1>,<pkg2> --deps
  $ gbs build -A i586 --binary-list=<pkg1>,<pkg2> --rdeps
  $ gbs build -A i586 --binary-list=<pkg1>,<pkg2> --deps --rdeps
  ```

### Other useful options

#### Install extra packages to build root

--extra-packs=<pkgs list sep by comma> can be used to install extra packages:

```bash
$ gbs build -A i586 --binary-list=<pkg1>,<pkg2> --deps
$ gbs build -A i586 --binary-list=<pkg1>,<pkg2> --rdeps
$ gbs build -A i586 --binary-list=<pkg1>,<pkg2> --deps --rdeps
```

#### Keep all packages in build root

Generally, gbs build will remove unnecessary packages in build root. While transferring to build another package, you can use --keep-packs to keep all unnecessary packages, and just install missing build required packages. This option can be used to speed up build multiple packages.

```bash
$ gbs build --keep-packs
```

--keep-packs can be used to create one build root for building multiple packages. Once the build root is ready, you can use --noinit to build these packages quickly.

```bash
$ gbs build pkg1/ --keep-packs -A i586
$ gbs build pkg2/ --keep-packs -A i586
$ gbs build pkg3/ --keep-packs -A i586
```

Now, the build root (~/GBS-ROOT/local/scratch.i586.0) is ready for building pkg1, pkg2, and pkg3. You can use --noinit to build them offline, and don't need waste time to check repo updates and build root.

```bash
$ gbs build pkg1 --noinit
$ gbs build pkg2 --noinit
$ gbs build pkg3 --noinit
```

### Force GBS to work in native mode

Use --fallback-to-native option to force GBS to perform packaging for non-native packages in native packaging mode in the packaging phase of the building process, that is, ignore upstream branch and create tarball from HEAD (by default) or specified commit without generating any patch. Adding --fallback-to-native option when issuing gbs build or gbs exportis equvalent to adding "fallback_to_native = true" into [general] section in GBS configuration file.

> **Note:**
> This option serves as a work-around solution for solving export failures of some non-native packages caused by a tricky engineering problem. For Tizen native packages, GBS always performs packaging in native packaging mode.

An example is shown below:

```bash
$ gbs build -A i586 --fallback-to-native
```

#### Skip the building of src.rpm file

Normally, two types of package files are created during the package building process:

- The binary, or executable, package file
- The source package file

The source package file, that is, src.rpm file, contains everything needed to recreate a specific version of a package, therefore, src.rpm file is a great way to distribute source code, but is optional when developing source code, especially when the source git tree is huge.

Adding --skip-srcrpm option will enable GBS to skip the building of src.rpm file, thus speeding up the building process of huge source git trees during development phase. An example is shown below:

```bash
$ cd <Path_to_crosswalk>
$ gbs build -A i586 --skip-srcrpm
```

#### Use distributed compiler networks

Though GBS has already provided --threads option to speed up the build process by activating multiple build workers, yet for huge git tree like crosswalk, the efficiency of just using multiple build workers in one local machine is far from satisfactory. That's where --icecream option comes in.

--icecream option activates distributed compiler networks, that is, GBS will use build workers on both local machine and distributed networks, thus further speeding up the build process.

An example is shown below:

```bash
$ gbs build -A i586 --icecream=10
```

### Fetch the project build conf and customize build root (for Advanced Users)

Project build conf describes the project build configurations for the project, including pre-defined macros/packages/flags in the build environment. In Tizen releases, the build conf is released together with the released repo. You can find an example at: [http://download.tizen.org/releases/daily/trunk/ivi/latest/builddata/xxx-build.conf](http://download.tizen.org/releases/daily/trunk/ivi/latest/builddata/xxx-build.conf)

- gbs build will fetch the build conf automatically

  Starting from gbs 0.7.1, by default, gbs will fetch the build conf from a remote repo, if you specify the remote Tizen repo, and then store it in your temp environment. Here's the build log:

  ```bash
  $ gbs build -A i586
  info: generate repositories ...
  info: build conf has been downloaded at:
  /var/tmp/<user>-gbs/tizen2.0.conf
  info: generate tar ball: packaging/acpid-2.0.14.tar.bz2
  [sudo] password for <user>:
  ```

- build the package using your own project build conf, using the -D option

  You can save it and modify it, and then use it for your purposes:

  ```bash
  $ cp /var/tmp/<user>-gbs/tizen2.0.conf ~/tizen2.0.conf
  $ gbs build -A i586 -D ~/tizen2.0.conf
  ```

  If you need to customize the build config, refer to: [http://en.opensuse.org/openSUSE:Build_Service_prjconf](http://en.opensuse.org/openSUSE:Build_Service_prjconf)