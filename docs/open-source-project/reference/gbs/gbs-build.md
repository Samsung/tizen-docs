# gbs build

Use the `gbs build` subcommand to build the source code and generate RPM packages locally.

For command usage details, enter:

```bash
$ gbs build -help
```

## Command Workflow

The `gbs build` command requires the following input:

- Git projects that contain RPM packaging files
- Binary RPM repositories (remote or local)  
The binary RPM repositories contain all the binary RPM packages used to create the chroot environment and build packages, which can be remote, like tizen release or snapshot repositories, or local. The local repository supports 2 types:

  - Standard repository with existing repodata
  - Normal directory containing RPM packages. GBS finds all RPM packages within the directory.

  To configure a repository, see [GBS Configuration](gbs.conf.md).
- Project build configurations (such as macros and flags)


The following figure shows the basic GBS build workflow. The figure illustrates that input and output are both repositories, and the output repository is located at `~/GBS-ROOT/locals/repos/` by default. You can change the repository path by using the `--buildroot` option.

**Figure: GBS build workflow**

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

Local repos in the GBS build root (`~/GBS-ROOT` by default) affect build results, so make sure that repositories do not contain old or unnecessary RPM packages. While running the `gbs build` command, you can specify the `--clean-repos` option to clean up local GBS-created repositories before building. To avoid problems, also set a different GBS build root directory for each profile. The GBS build directory can be defined in many ways:

- By default, the GBS build puts all output files under `~/GBS-ROOT/`.
- If the `TIZEN_BUILD_ROOT` environment variable exists, `${TIZEN_BUILD_ROOT}` is used as the output top directory.
- If the `-B` option is specified, the specified directory is used, even if `${TIZEN_BUILD_ROOT}` exists.

> **Note**
>
> All RPM packages under the output repository (by default, `~/GBS-ROOT/local/repos/<VERSION>/`) are used when building packages. Since all the packages under the output repository are applied to the build environment, avoid unexpected results by making sure that the output repository is clean.

The following example shows the structure of the GBS build root directory in the workflow output:

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

## Examples

To perform a basic build:

- Build a single package:
  ```bash
  $ cd package1$ gbs build -A i586
  ```

- Build a package for different architectures:
   > **Note**
   >
   > Supported architectures include x86_64, i586, armv6l, armv7hl, armv7l, aarch64, mips, and mipsel.

  ```bash
  $ gbs build -A armv7l #build package for armv7l
  $ gbs build -A i586 #build package for i586
  ```

- Make a clean build by deleting the old build root.  
The `--clean` option must be specified if the repository has been changed, for example, to another release.

  ```bash
  $ gbs build -A armv7l --clean
  ```

- Build the package with a specific commit:
  ```bash
  $ gbs build -A armv7l --commit=<COMMIT_ID>
  ```

- Use the `--overwrite` option to trigger a rebuild.  
If you have already built before, and want to rebuild, specify the `--overwrite` option or the packages are skipped.
  ```bash
  $ gbs build -A i586 --overwrite
  ```

  If you change the commit or specify the `--include-all` option, it always rebuilds. In these cases, the `--overwrite` option is not needed.

- Output the debug info:
  ```bash
  $ gbs build -A i586 --debug
  ```

- Build against a local repository.  
You can configure the local repo in the `.gbs.conf` file or through the command line.
  ```bash
  $ gbs build -R /path/to/repo/dir/ -A i586
  ```

- Use the `--noinit` option to build a package in offline mode.  
This option can only be used if the build root is ready. When it is used, GBS does not connect the remote repository, and skips parsing and checking the repository and initializing the build environment. The package is built directly.

  ```bash
  $ gbs build -A i586 # build first and create build environment
  $ gbs build -A i586 --noinit # use --noinit to start building directly
  ```

- Build with all uncommitted changes using the `--include-all` option.  
  In the following examples, the Git tree contains 1 modified file and 2 extra files:
  ```bash
  $ git status -s
  M ail.pc.in
  ?? base.repo
  ?? main.repo
  ```
  - Build without the `--include-all` option

    Only committed files are built. None of the modified files, which are neither committed nor added, are built:

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

  - Build with the `--include-all` option

    All the files are built:
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
  - Use `.gitignore` to ignore specific files when using the `--include-all` option.

    If you want to ignore some file types, update your `.gitignore`:

    ```bash
    $ cat .gitignore
    .*
    */.*
    *.pyc
    *.patch*
    ```

## Incremental Build

Starting from GBS 0.10, the `gbs build` subcommand supports the `--incremental` option, which allows you to build incrementally.

The incremental mode is designed for development and verification of single packages. It is not intended to replace the standard mode. Only 1 package can be built at a time using the incremental mode.

The incremental mode sets up the build environment in multiple steps, finishing by mounting the local Git tree of a package in the chroot build environment.

> **Note**
>
> Because GBS mounts your Git tree to the build root, be very careful when you remove your build root. You need to make sure you have already unmounted the source tree manually before you remove it.

The incremental mode has the following benefits:

- The build environment uses the latest source code and changes to source do not trigger a new build environment (in the chroot).
- The Git source tree becomes the source of the builds. Any change made in the Git repository followed by invocation of the build script builds the changed sources.
- If the build fails for some reason, the build script continues from the spot where it has failed, once the code has been changed to fix the problem causing the failure.

Incremental building is, in many ways, similar to traditional code development, where changes are made to sources, followed by running make to test and compile the changes. However, it enables development using the build environment of the target, instead of the host OS.

The incremental mode has some limitations, mostly related to packaging and how the sources are maintained. Among others, it depends on how the RPM spec file is composed:

- The incremental mode does not support patches in the spec file. All source has to be maintained as part of the Git tree.

- The incremental mode requires a clean packaging workflow. Exotic workflows in the spec files do not always work well, because the incremental mode expects the following model:

  1. Code preparation (%prep)
  2. Code building (%build)
  3. Code installation (%install)

- The %prep section can only contain the %setup macro to unpack the tarball, and must not contain other source code-related operations, such as unpacking another source or applying patches.
  
- Because the %build section is run every time, if the %build script has configuration scripts (auto-tools), binaries can be regenerated, causing a complete build every time. To avoid this, use the following macros, which can be overridden using the `--no-configure` option:

    - %configure: runs the configure script with pre-defined paths and options.
	- %reconfigure: regenerates the scripts and runs %configure.
	- %autogen: runs the autogen script.

- You can build only a single package. You cannot build multiple packages in parallel.

- The tarball's name in the spec file must be `%{name}-%{version}.{tar.gz|tar.bz2|zip|...}`. Otherwise, GBS cannot mount the source code to build the root correctly.

The following example uses the dlog source code. First, it builds with the `--incremental` option, then modifies 1 source file and triggers the incremental build again. You can see that only modified source code gets compiled during the incremental build.

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

From the build log, you can see that only `log.c` has been re-compiled. That is the point of the incremental build behavior.

The `--noinit` option can be used together with `--incremental` to make a build more quickly:

```bash
$ gbs build --incremental --noinit
```

## Multiple Package Build (Dependency Build)

Multiple package build has been supported since GBS 0.10. If packages have dependencies on each other, GBS builds them in the correct order calculated by the dependency relationships. Previously built RPMs are used to build the packages that depend on them. This process is called a dependency build.

To perform a multiple package build:

- Build all packages under a specific package directory:

  ```bash
  $ mkdir tizen-packages
  $ cp package1 package2 package3 ... tizen-packages/
  $ gbs build -A i586 tizen-packages # build all packages under tizen-packages
  ```

- Build multiple packages in parallel with the `--threads` option:

  ```bash
  # current directory have multiple packages, --threads can be used to set the max build worker at the same time
  $ gbs build -A armv7l --threads=4
  ```

- Select a group of packages to be built:

  - The `--binary-from-file` option specifies a text file that contains a name list of RPM packages to be built. The format in the text file is 1 package per line.
  - The `--binary-list` option specifies a list in which the package names are separated by commas.

  When the number of packages is small and the packages can be clearly listed in the command line, use the `--binary-list` option for simplicity.

  ```bash
  $ gbs build -A i586 --binary-from-file=/path/to/packages.list
  $ gbs build -A i586 --binary-list=<pkg1>,<pkg2>
  ```

- Exclude certain packages:

  - The `--exclude` option specifies a list in which the names of packages to be ignored are separated by commas.
  - The `--exclude-from-file` option specifies a text file that contains a name list of packages to be ignored.

  ```bash
  $ gbs build -A i586 tizen-packages --exclude=<pkg1>
  $ gbs build -A i586 tizen-packages --exclude=<pkg1>,<pkg2>
  $ gbs build -A i586 tizen-packages --exclude-from-file=/path/to/packages.list
  ```

- Build packages based on dependencies:

  - The `--deps` option enables GBS to build specific packages, together with all related packages on which they depend.
  - The `--rdep` option enables GBS to build specific packages, together with all related packages that depend on them.

  The specific packages can be included by the `--binary-from-file` or `--binary-list` option, and excluded by the `--exclude` or `--exclude-from-file` option.

  The `--deps` and `--rdep` options are compatible. When added at the same time, besides the specific packages, GBS builds not only the related packages on which they depend, but also all the related packages that depend on them.

  ```bash
  $ gbs build -A i586 --binary-list=<pkg1>,<pkg2> --deps
  $ gbs build -A i586 --binary-list=<pkg1>,<pkg2> --rdeps
  $ gbs build -A i586 --binary-list=<pkg1>,<pkg2> --deps --rdeps
  ```

## Useful Building Options

The `gbs build` command offers some useful options:

- Install extra packages to build a root

  The `--extra-packs=<packages separated by commas>` option can be used to install extra packages:

  ```bash
  $ gbs build -A i586 --extra-packs=<pkg1>,<pkg2> --deps
  $ gbs build -A i586 --extra-packs=<pkg1>,<pkg2> --rdeps
  $ gbs build -A i586 --extra-packs=<pkg1>,<pkg2> --deps --rdeps
  ```

- Keep all packages in the build root

  Generally, the GBS build removes unnecessary packages in the build root. While transferring to build another package, you can use the `--keep-packs` option to keep all unnecessary packages, and just install missing required build packages. This option can be used to speed up building multiple packages.

  ```bash
  $ gbs build --keep-packs
  ```

  The `--keep-packs` option can be used to create 1 build root for building multiple packages. Once the build root is ready, you can use the `--noinit` option to build these packages quickly.

  ```bash
  $ gbs build pkg1/ --keep-packs -A i586
  $ gbs build pkg2/ --keep-packs -A i586
  $ gbs build pkg3/ --keep-packs -A i586
  ```

  Now, the build root (`~/GBS-ROOT/local/scratch.i586.0`) is ready for building `pkg1`, `pkg2`, and `pkg3`. You can use the `--noinit` option to build them offline, and need waste no time to check for repository updates and build root.

  ```bash
  $ gbs build pkg1 --noinit
  $ gbs build pkg2 --noinit
  $ gbs build pkg3 --noinit
  ```

### Forcing GBS to Work in the Native Mode

Use the `--fallback-to-native` option to force GBS to perform packaging for non-native packages in the native packaging mode in the packaging phase of the building process, that is, ignore the upstream branch and create a tarball from HEAD (by default) or specified commit without generating any patch. Adding the `--fallback-to-native` option when issuing the `gbs build` or `gbs export` command is equivalent to adding the `fallback_to_native = true` property into the `[general]` section of the GBS configuration file.

> **Note**
>
> This option serves as a work-around solution for solving export failures of some non-native packages caused by a tricky engineering problem. For Tizen native packages, GBS always performs packaging in the native packaging mode.

```bash
$ gbs build -A i586 --fallback-to-native
```

### Skipping the Building of the src.rpm File

Normally, 2 types of package files are created during the package building process:

- Binary, or executable, package file
- Source package file

The source package file (`src.rpm`) contains everything needed to recreate a specific version of a package. This makes the `src.rpm` file a great way to distribute source code. However, it is optional when developing source code, especially when the source Git tree is huge.

Adding the `--skip-srcrpm` option enables GBS to skip the building of the `src.rpm` file, speeding up the building process of huge source Git trees during development:

```bash
$ cd <Path_to_crosswalk>
$ gbs build -A i586 --skip-srcrpm
```

### Using Distributed Compiler Networks

Though GBS provides the `--threads` option to speed up the build process by activating multiple build workers, the efficiency of just using multiple build workers in 1 local machine is far from satisfactory, especially for a huge Git tree, such as crosswalk.

To improve the build process efficiency further, use the `--icecream` option, which activates distributed compiler networks. The option makes GBS use build workers on both the local machine and distributed networks.

```bash
$ gbs build -A i586 --icecream=10
```

## Fetching the Project Build Conf and Customizing the Build Root (for Advanced Users)

The project build conf describes the build configurations for the project, including all macros, packages, and flags predefined in the build environment. In Tizen releases, the build conf is released together with the released repository.

- Fetch the build conf automatically with the `gbs build` command

  Starting from GBS 0.7.1, by default, GBS fetches the build conf from a remote repository (if you specify the remote Tizen repository) and stores it in your temporary environment:

  ```bash
  $ gbs build -A i586
  info: generate repositories ...
  info: build conf has been downloaded at:
  /var/tmp/<user>-gbs/tizen2.0.conf
  info: generate tar ball: packaging/acpid-2.0.14.tar.bz2
  [sudo] password for <user>:
  ```

- Build the package using your own project build conf, by using the `-D` option

  You can save and modify the build conf, and use it for your own purposes:

  ```bash
  $ cp /var/tmp/<user>-gbs/tizen2.0.conf ~/tizen2.0.conf
  $ gbs build -A i586 -D ~/tizen2.0.conf
  ```

To customize the build config, see [http://en.opensuse.org/openSUSE:Build_Service_prjconf](http://en.opensuse.org/openSUSE:Build_Service_prjconf).
