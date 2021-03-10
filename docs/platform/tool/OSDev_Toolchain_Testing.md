Glibc
=====

Build glibc on x86 host (cross-compilation)
-------------------------------------------

### Download glibc sources

Use osc utility to download sources from OBS, e.g.
[build.tizen.org](https://build.tizen.org). In case of using
build.tizen.org & Tizen:Base all dependent packages will be downloaded
and cached automatically. Otherwise you\'ll need to download them
manually (refer to [ this
section](#Download_additional_dependencies_manually "wikilink")).

`cd /path/to/obs/projects`\
`osc -A `[`https://build.tizen.org`](https://build.tizen.org)` co -S Tizen:Base glibc`\
`cd Tizen:Base/glibc`

### Build glibc

To build build glibc from downloaded sources, simply run:

`osc build standard armv7l --noservice --noverify --clean glibc.spec`

Change armv7l to your target architecture.

#### Omit building & running testsuite

If you want to run tests separately (on your target device), you may
comment out according lines in the .spec file before running \"osc
build\" command:

`sed -i -e '/^%check/,/^###/{/^###/b; s/^/#/}' glibc.spec`

or just run the command with \"\--nochecks\" option, as follows:

`osc build standard armv7l --noservice --noverify --nochecks --clean glibc.spec`

### Deploying buildroot on device

Refer to [ this section](#Prepare_SD_card_for_the_device "wikilink") if
your device has removable SD card.

Alternativbely, if your device is reachable via network, you may mount
your buildroot created by \"osc build\" as NFS shared folder, e.g.:

On your host run:

`mkdir -p /export`\
`ln -svf /path/to/your/buildroot /export/buildroot`\
`echo "/export/buildroot *(rw,async,no_subtree_check,no_root_squash)" >> /etc/exports`

**Note**: make sure you have nfs server package installed (e.g., on
Ubuntu/Debian it would be `nfs-kernel-server`). You may also want to
replace `*` in the last command with network address of your device (as
`*` provides access to an every node in your network).

You\'ll also need to fix some toolchain-related issues by removing
`qemu-accel` package from inside buildroot. Run (on host also):

`cd /path/to/your/buildroot`\
`chroot .`\
`mount -t proc none /proc`

Then remove the package:

`rpm -qa | grep qemu-accel | xargs rpm -e`

Fix `rpm db`-related errors and exit chroot:

`rm -rf /var/lib/rpm/__db.00*`\
`umount /proc`\
`exit`

Then on target device run:

`mount -t nfs host.ip.address:/export/buildroot /mnt`\
`cd /mnt`\
`mount -t proc proc proc/`\
`mount -t sysfs sys sys/`\
`mount -o bind /dev dev/`\
`mount -t devpts pts dev/pts/`\
`chroot .`

And there you\'re, ready to build & run the testsuite.

Build testsuite on device
-------------------------

From chroot environment run:

`cd /home/abuild/rpmbuild/BUILD/glibc-2.24/cc-base`\
`make -r PARALLELMFLAGS="-j4" check -k 2>&1 | tee make_check.log`

Here `-k` option prevents interruption on error,
`-r PARALLELMFLAGS="-j4"` allows to run several threads.

You can also check only one component (subdirectory):

`make -C /home/abuild/rpmbuild/BUILD/glibc-2.24/inet objdir=/home/abuild/rpmbuild/BUILD/glibc-2.24/cc-base check -k`

Options: `-C $absolute_source_dir objdir=$absolute_build_dir`.

The glibc testsuite contains a number of tests to check that the ABI of
glibc does not change. It compares symbol names and versions and static
variable sizes in generated binaries with those maintained in \*.abilist
in the source. The test runs as part of `make check`. You can also run
those separately via `make check-abi`.

**Results:** each subdirectory will contain a file *subdir-tests.sum*.
Also you will see the summary result after full testing, for example:

`Summary of test results:`\
`        4 FAIL`\
`        2418 PASS`\
`        32 UNRESOLVED`\
`        14 UNSUPPORTED`\
`        42 XFAIL`\
`        2 XPASS`

### Known issues

#### Clock desync

In case you see messages like:

`make: warning: Clock skew detected. Your build may be incomplete.`

while running \"make\" on target device, make sure your host and target
clocks are syncronized. If not, you may need to adjust your target
timezone to your local one, as follows:

`ln -svf /usr/share/zoneinfo/your/timezone /etc/localtime`

#### Warning \"Setting locale failed\"

If you observe messages like this while building process:

`perl: warning: Setting locale failed.`\
`perl: warning: Please check that your locale settings:`\
`        LANGUAGE = (unset),`\
`        LC_ALL = (unset),`\
`        LANG = "en_US.UTF-8"`\
`    are supported and installed on your system.`\
`perl: warning: Falling back to the standard locale ("C")`

there\'s no need to worry: it would generally make no harm. Howewer it
can be suppressed by setting a proper locale:

`sed -i -e '/en_US.UTF-8/{s/^.*en_US/en_US/}' /etc/locale.gen`\
`locale-gen`\
`export LANGUAGE=en_US.UTF-8`\
`export LANG=en_US.UTF-8`\
`export LC_ALL=en_US.UTF-8`

GCC
===

Current TODO-list
-----------------

-   Resolve dependencies for linaro-gcc (available now at private SPIN
    server)

<!-- -->

-   Add references for needed packages? (dejagnu etc.)

<!-- -->

-   Describe OBS build using osc in details?

<!-- -->

-   Describe OBS build using gbs?

<!-- -->

-   Describe testing ARM/AARCH64 builds for native platforms?

<!-- -->

-   Describe popular `RUNTESTFLAGS`?

<!-- -->

-   Apply patches for linaro-gcc (from build.tizen.org) to successfully
    run testsuite

<!-- -->

-   Verify testing on target device step-by-step

<!-- -->

-   Combine all patches for linaro-gcc.spec?

Building linaro-gcc testsuite with gbs
--------------------------------------

### Mininal .gbs.conf example

`   [general]`\
`   prifile   = profile.tizen.org.devel.base`\
`   buildconf = ~/wr/gbs/build_conf/devel.toolchains.ref/base/build.conf`\
`   buildroot = ~/GBS-ROOT/`\
`   `\
`   [profile.tizen.org.devel.base]`\
`   repos     = repo.tizen.org.devel.base, repo.tizen.org.devel.unified`\
`   `\
`   # devel:Toolchains:Base`\
`   [repo.tizen.org.devel.base]`\
`   url = `[`http://download.tizen.org/live/devel:/Toolchains:/Base/standard/`](http://download.tizen.org/live/devel:/Toolchains:/Base/standard/)\
`   `\
`   # devel:Toolchains:Unified`\
`   [repo.tizen.org.devel.unified]`\
`   url = `[`http://download.tizen.org/live/devel:/Toolchains:/Unified/standard/`](http://download.tizen.org/live/devel:/Toolchains:/Unified/standard/)

### Prepare dependences for linaro-gcc

Prepare all dependences and `linaro-gcc` sources:

`   mkdir linaro-gcc-test`\
`   cd linaro-gcc-test`\
`   `\
`   git clone `[`ssh://review.tizen.org:29418/platform/upstream/autogen.git`](ssh://review.tizen.org:29418/platform/upstream/autogen.git)` --branch tizen`\
`   git clone `[`ssh://review.tizen.org:29418/platform/upstream/dejagnu.git`](ssh://review.tizen.org:29418/platform/upstream/dejagnu.git)` --branch tizen`\
`   git clone `[`ssh://review.tizen.org:29418/platform/upstream/guile.git`](ssh://review.tizen.org:29418/platform/upstream/guile.git)` --branch tizen`\
`   git clone `[`ssh://review.tizen.org:29418/platform/upstream/libatomic_ops.git`](ssh://review.tizen.org:29418/platform/upstream/libatomic_ops.git)` --branch tizen`\
`   git clone `[`ssh://review.tizen.org:29418/platform/upstream/libgc.git`](ssh://review.tizen.org:29418/platform/upstream/libgc.git)` --branch tizen`\
`   `\
`   ln -sf /path/to/linaro-gcc/`

### Build with gbs

`   gbs build --clean -A x86_64 \`\
`       --profile=profile.tizen.org \`\
`       --define 'gcc_run_tests 1' \`\
`       --exclude gcc-armv7l,gcc-aarch64,gcc-armv7hl \`\
`       --binary-list=libatomic_ops,autogen,libgc,guile,dejagnu,linaro-gcc`

### Usage example with single script

`cat test_linaro_gcc`:

`   #!/usr/bin/env bash`\
`   `\
`   set -eux`\
`   `\
`   # Default is host $USERNAME`\
`   USER="${USER:-$USERNAME}"`\
`   LINARO_GCC="${LINARO_GCC:-~/wr/tizen/linaro-gcc/}"`\
`   DIR="${DIR:-linaro-gcc-test}"`\
`   `\
`   declare -a DEPS=(`\
`       "autogen"`\
`       "dejagnu"`\
`       "guile"`\
`       "libatomic_ops"`\
`       "libgc")`\
`   `\
`   # 1. Prepare`\
`   mkdir -p "$DIR"`\
`   cd "$DIR"`\
`   `\
`   # 2. Clone deps`\
`   for dep in "${DEPS[@]}"; do`\
`       if [ ! -d "$dep" ]; then`\
`       git clone `[`ssh://"${USERNAME}"@review.tizen.org:29418/platform/upstream/"${dep}`](ssh://%22$%7BUSERNAME%7D%22@review.tizen.org:29418/platform/upstream/%22$%7Bdep%7D)`".git --branch tizen`\
`       fi`\
`   done`\
`   `\
`   # 3. Link to linaro-gcc sources`\
`   [ ! -d linaro-gcc ] && ln -sf "$LINARO_GCC" linaro-gcc`\
`   `\
`   # 4. Build`\
`   gbs build --clean -A x86_64 \`\
`       --profile=profile.tizen.org \`\
`       --define 'gcc_run_tests 1' \`\
`       --exclude gcc-armv7l,gcc-aarch64,gcc-armv7hl \`\
`       --binary-list=libatomic_ops,autogen,libgc,guile,dejagnu,linaro-gcc`

Example usage:

`   USER=mkashkarov LINARO_GCC=~/wr/tizen/linaro-gcc ./test_linaro-gcc`

Get linaro-gcc and needed packages to run testsuite
---------------------------------------------------

### Using osc command line tool

`   # Path to buildroot used by osc`\
`   export GCC_BUILD_ROOT="/var/tmp/build-root/standard-x86_64/"`\
`   # Path to linaro-gcc directory used for build`\
`   export GCC_DIR="${GCC_BUILD_ROOT}/home/abuild/rpmbuild/BUILD/gcc-6.2.1/"`\
`   # Path to linaro-gcc build directory`\
`   export GCC_BUILD_DIR="$GCC_DIR/obj/"`\
`   # Path to ./contrib subfolder with scripts`\
`   export GCC_CONTRIB_DIR="$GCC_DIR/contrib/"`\
`   # Path to save manually downloaded binaries needed to run linaro-gcc testsuite`\
`   export DOWNLOAD_BINARIES="/path/to/store/binaries/"`

#### Download linaro-gcc package

Use [osc](https://wiki.tizen.org/OSDev/Using_OBS) to download linaro-gcc
package from [build.tizen.org](https://build.tizen.org) or other `OBS`
system.

For example:

`   cd /your/path/to/obs/projects/`\
`   osc -A `[`https://build.tizen.org`](https://build.tizen.org)` co -S devel:Toolchains:Base:ref linaro-gcc`\
`   cd devel:Toolchains:Base:ref/linaro-gcc`

#### Download additional dependencies manually

If you run the following build command

`   osc build standard armv7l --no-service --no-verify --clean linaro-gcc.spec --define='run_tests 1'`

And get this output:

`   buildinfo is broken... it says:`\
`   unresolvable: nothing provides dejagnu, nothing provides expect, nothing provides gdb`

Then you need to install additional packages for building testsuite.
(<span class="timestamp-wrapper"><span class="timestamp">\<2018-08-29
Wed\></span></span>: List of needed packages to install)

  ---------------- ------------------------------------------------------------------------------------- ----------
  Package          Link                                                                                  Private?
                                                                                                         
  autogen          <https://10.113.136.201/package/show/devel:Toolchains:standalone/autogen> \|+         
  dejagnu          <https://10.113.136.201/package/show/devel:Toolchains:standalone/dejagnu> \|+         
  gmp              <https://10.113.136.201/package/show/devel:Toolchains:standalone/gmp> \|+             
  guile            <https://10.113.136.201/package/show/devel:Toolchains:standalone/guile> \|+           
  libatomic\_ops   <https://10.113.136.201/package/show/devel:Toolchains:standalone/libatomic_ops> \|+   
  libgc            <https://10.113.136.201/package/show/devel:Toolchains:standalone/libgc> \|+           
  expat            <https://build.tizen.org/package/show/devel:Toolchains:Base:ref/expat>                
  libffi           <https://build.tizen.org/package/show/devel:Toolchains:Base:ref/libffi>               
  openssl          <https://build.tizen.org/package/show/devel:Toolchains:Base:ref/openssl>              
  python           <https://build.tizen.org/package/show/devel:Toolchains:Base:ref/python>               
  expect           <https://build.tizen.org/package/show/devel:Toolchains:Unified:ref/expect>            
  gdb              <https://build.tizen.org/package/show/devel:Toolchains:Unified:ref/gdb>               
  tcl              <https://build.tizen.org/package/show/devel:Toolchains:Unified:ref/tcl>               
  ---------------- ------------------------------------------------------------------------------------- ----------

##### Download needed binaries manually

Download all the binaries that are needed to perform `linaro-gcc`
testing (change `armv7l` to needed target):

`   osc -A `[`https://s014`](https://s014)` getbinaries devel:Toolchains:standalone autogen       standard armv7l -d ${DOWNLOAD_BINARIES}`\
`   osc -A `[`https://s014`](https://s014)` getbinaries devel:Toolchains:standalone dejagnu       standard armv7l -d ${DOWNLOAD_BINARIES}`\
`   osc -A `[`https://s014`](https://s014)` getbinaries devel:Toolchains:standalone gmp           standard armv7l -d ${DOWNLOAD_BINARIES}`\
`   osc -A `[`https://s014`](https://s014)` getbinaries devel:Toolchains:standalone guile         standard armv7l -d ${DOWNLOAD_BINARIES}`\
`   osc -A `[`https://s014`](https://s014)` getbinaries devel:Toolchains:standalone libatomic_ops standard armv7l -d ${DOWNLOAD_BINARIES}`\
`   osc -A `[`https://s014`](https://s014)` getbinaries devel:Toolchains:standalone libgc         standard armv7l -d ${DOWNLOAD_BINARIES}`\
`   osc -A `[`https://s014`](https://s014)` getbinaries devel:Toolchains:Base:ref expat           standard armv7l -d ${DOWNLOAD_BINARIES}`\
`   osc -A `[`https://s014`](https://s014)` getbinaries devel:Toolchains:Base:ref libffi          standard armv7l -d ${DOWNLOAD_BINARIES}`\
`   osc -A `[`https://s014`](https://s014)` getbinaries devel:Toolchains:Base:ref openssl         standard armv7l -d ${DOWNLOAD_BINARIES}`\
`   osc -A `[`https://s014`](https://s014)` getbinaries devel:Toolchains:Base:ref python          standard armv7l -d ${DOWNLOAD_BINARIES}`\
`   osc -A `[`https://s014`](https://s014)` getbinaries devel:Toolchains:Unified:ref expect       standard armv7l -d ${DOWNLOAD_BINARIES}`\
`   osc -A `[`https://s014`](https://s014)` getbinaries devel:Toolchains:Unified:ref gdb          standard armv7l -d ${DOWNLOAD_BINARIES}`\
`   osc -A `[`https://s014`](https://s014)` getbinaries devel:Toolchains:Unified:ref tcl          standard armv7l -d ${DOWNLOAD_BINARIES}`

Build linaro-gcc testsuite
--------------------------

This will test various components of `GCC`, such as compiler front ends
and runtime libraries. While running the testsuite, `DejaGnu` might emit
some harmless messages resembling
`WARNING: Couldn't find the global config file.` or
`WARNING: Couldn't find tool init file` that can be ignored.

### Build on host (x86\_64/i586) platform

#### Testing native compiler

Build `x86_64/i585` `linaro-gcc` with testsuite enabled:

`   osc build standard x86_64 --no-service --no-verify --clean \`\
`   --define 'run_tests 1' linaro-gcc.spec -p ${DOWNLOAD_BINARIES}`

#### Testing cross-compiler

You should specify target board for cross compiler. In case if you want
to test `armv7l`:

`   cd ${GCC_BUILD_DIR}/build`\
`   make check RUNTESTFLAGS=--target_board=arm-sim`

### Build on device (armv7l/aarch64) platform

You need to interrup `linaro-gcc` build right after `make ..` command
and before cleaning up object files at the end of the build to copy full
buildroot on the device and continue process there.

#### Build linaro-gcc

Run the build and wait till process exit after `make`:

`   osc build standard armv7l --no-service --clean --no-verify \`\
`   --root=${GCC_BUILD_ROOT} --define "run_tests 1" --define "exit_on_make_finish 1" \`\
`   -p ${DOWNLOAD_BINARIES}`

Like this:

`   [  746s] make[4]: Leaving directory '/home/abuild/rpmbuild/BUILD/gcc-6.2.1/obj/armv7l-tizen-linux-gnueabi/libsanitizer'`\
`   [  746s] make[3]: Leaving directory '/home/abuild/rpmbuild/BUILD/gcc-6.2.1/obj/armv7l-tizen-linux-gnueabi/libsanitizer'`\
`   [  746s] make[2]: Leaving directory '/home/abuild/rpmbuild/BUILD/gcc-6.2.1/obj/armv7l-tizen-linux-gnueabi/libsanitizer'`\
`   [  746s] make[1]: Leaving directory '/home/abuild/rpmbuild/BUILD/gcc-6.2.1/obj'`\
`   [  746s] + exit 1`\
`   [  746s] error: Bad exit status from /var/tmp/rpm-tmp.ULdtx9 (%build)`\
`   [  746s]`\
`   [  746s]`\
`   [  746s] RPM build errors:`\
`   [  746s]     Bad exit status from /var/tmp/rpm-tmp.ULdtx9 (%build)`

#### Prepare SD card for the device

You need about `4Gb` free space for the buildroot, about `4Gb` for the
swap and additional space duiring `gcc` build, so totally about `16Gb`
free space will be enough. You can save additional space by removing
`/home/abuild/rpmbuild/SOURCES/*` (inside chroot) and decreasing `make`
parallel jobs when build on device (do `make -j1 ..`, for example).

**NOTE**: `[target]sh-3.2# ..` means that you need to do commands on the
target device:

`   sdb root on`\
`   sdb shell`\
`   [target]sh-3.2# uname -a`\
`   Linux localhost 3.10.65 #1-Tizen SMP PREEMPT Mon Jul 16 02:47:16 UTC 2018 armv7l GNU/Linux`

Use SD card formatted to `ext4` (`fat32` does not support symbolic
links). To format SD card to `ext4`:

`   [target]sh-3.2# mkfs.ext4 /dev/mmcblk1p1`

Add the following line to `/etc/fstab` and reboot:

`   [target]sh-3.2# mount -o remount,rw /`\
`   [target]sh-3.2# echo "/dev/mmcblk1p1  /opt/media/SDCardA1     ext4    defaults,noatime        0       3" >> /etc/fstab`

Or you can mount manually every time device is loaded:

`   [target]sh-3.2# mount /dev/mmcblk1p1 /opt/media/SDCardA1`

Now you should have SD card mounted at `/opt/media/SDCardA1/`.

#### Copy buildroot to device

Archive build root used by `osc build...`:

`   cd ${GCC_BUILD_ROOT}`\
`   sudo tar cvfz gcc_buildroot.tar.gz .`

Adn then copy the archive to device:

`   sdb push gcc_buildroot.tar.gz /opt/media/SDCardA1`

#### Configure environment on the device

Connect to the device shell:

`   sdb root on`\
`   sdb shell`

Change fs to `read-write`:

`   [target]sh-3.2# mount -o remount,rw /`

Extract buildroot:

`   [target]sh-3.2# cd /opt/media/SDCardA1`\
`   # Avoid "make: warning:  Clock skew detected.  Your build may be incomplete."`\
`   # Insert date that is not in the past right now`\
`   [target]sh-3.2# date -s "2018-08-30 11:55"`\
`   [target]sh-3.2# mkdir -p gcc_buildroot`\
`   [target]sh-3.2# tar xvzf gcc_buildroot.tar.gz --owner root --group root --no-same-owner -C gcc_buildroot`

Mount the devices:

`   [target]sh-3.2# cd gcc_buildroot`\
`   [target]sh-3.2# mount -v --bind /dev ./dev`\
`   [target]sh-3.2# mount -vt devpts devpts ./dev/pts`\
`   [target]sh-3.2# mount -vt tmpfs shm ./dev/shm`\
`   [target]sh-3.2# mount -vt proc proc ./proc`\
`   [target]sh-3.2# mount -vt sysfs sysfs ./sys`

Get inside buildroot:

`   sh-3.2# pwd`\
`   /opt/media/SDCardA1/gcc_buildroot`\
`   [target]sh-3.2# chroot .`

Create swap file

`   # 4GB /swapfile`\
`   [target-chroot]sh-3.2# dd if=/dev/zero of=/swapfile bs=64M count=64`\
`   [target-chroot]sh-3.2# mkswap /swapfile`\
`   [target-chroot]sh-3.2# swapon /swapfile`\
`   # Verify`\
`   [target-chroot]sh-3.2# swapon --show`\
`   NAME      TYPE SIZE USED PRIO`\
`   /swapfile file   4G   0B   -1`

Fix link to `liblto_plugin.so`:

`   [target-chroot]sh-3.2# cd /usr/lib/gcc/armv7l-tizen-linux-gnueabi/6.2.1/`\
`   [target-chroot]sh-3.2# ln -sf liblto_plugin.so.0.0.0 liblto_plugin.so`

Prevent error messages related to `rpm db`:

`   [target-chroot]sh-3.2# rm -rf /var/lib/rpm/__db.00*`

Adjust `OOM` score settings:

`   [target-chroot]sh-3.2# echo -17 > /proc/$$/oom_adj`\
`   [target-chroot]sh-3.2# echo -1000 > /proc/$$/oom_score_adj`

#### Build testsuite on device

##### Build manually

`   [target-chroot]sh-3.2# cd /home/abuild/rpmbuild/BUILD/gcc-6.2.1/obj/`\
`   [target-chroot]sh-3.2# make check -k -j2 2>&1 | tee make_check.log`

##### Build using rpmbuild

Modify `rpm` macroses:

`   [target-chroot]sh-3.2# export HOME=/home/abuild`\
`   [target-chroot]sh-3.2# echo '%_topdir %{getenv:HOME}/rpmbuild' >> /usr/lib/rpm/macros`

Run `rpmbuild` started with `%build` section and turn off removing
`obj/` dir and `configure/make` steps:

`   cd %{HOME}/rpmbuild`\
`   rpmbuild --nodeps --noclean --short-circuit -bc --define '_srcdefattr (-,root,root)' \`\
`   --nosignature --target=armv7l-tizen-linux --define '_build_create_debug 1' \`\
`   --define 'run_tests_on_device 1' --define '_smp_mflags -j2' ${HOME}/rpmbuild/SOURCES/linaro-gcc.spec \`\
`   2>&1 | tee build_testsuite_log.txt`

APPENDIX A: Run the testsuite manually on selected tests
--------------------------------------------------------

In order to run sets of tests selectively, there are targets
`make check-gcc` and language specific `make check-c`, `make check-c++`,
`make check-fortran`, `make check-ada`, `make check-objc`,
`make check-obj-c++`, `make check-lto` in the gcc subdirectory of the
object directory. You can also just run `make check` in a subdirectory
of the object directory.

A more selective way to just run all gcc execute tests in the testsuite
is to use

`   make check-gcc RUNTESTFLAGS="execute.exp other-options"`

The file-matching expression following `filename.exp` is treated as a
series of whitespace-delimited glob expressions so that multiple
patterns may be passed, although any whitespace must either be escaped
or surrounded by single quotes if multiple expressions are desired. For
example,

`   make check-g++ RUNTESTFLAGS="old-deja.exp=9805*\ virtual2.c other-options" make`\
`   check-g++ RUNTESTFLAGS="'old-deja.exp=9805* virtual2.c' other-options"`

The `*.exp` files are located in the testsuite directories of the `GCC`
source, the most important ones being `compile.exp`, `execute.exp`,
`dg.exp` and `old-deja.exp`. To get a list of the possible `*.exp`
files, pipe the output of `make check` into a file and look at the
`Running … .exp` lines. Passing options and running multiple testsuites

You can pass multiple options to the testsuite using the
`--target_board` option of `DejaGNU`, either passed as part of
`RUNTESTFLAGS`, or directly to runtest if you prefer to work outside the
makefiles. For example,

`   make check-g++ RUNTESTFLAGS="--target_board=unix/-O3/-fmerge-constants"`

will run the standard `g++` testsuites (`unix` is the target name for a
standard native testsuite situation), passing `-O3 -fmerge-constants` to
the compiler on every test, i.e., slashes separate options.

You can run the testsuites multiple times using combinations of options
with a syntax similar to the brace expansion of popular shells:

`   …"--target_board=arm-sim\{-mhard-float,-msoft-float\}\{-O1,-O2,-O3,\}"`

(Note the empty option caused by the trailing comma in the final group.)
The following will run each testsuite eight times using the `arm-sim`
target, as if you had specified all possible combinations yourself:

`   --target_board='arm-sim/-mhard-float/-O1 \ arm-sim/-mhard-float/-O2 \`\
`           arm-sim/-mhard-float/-O3 \ arm-sim/-mhard-float \`\
`           arm-sim/-msoft-float/-O1 \ arm-sim/-msoft-float/-O2 \`\
`           arm-sim/-msoft-float/-O3 \ arm-sim/-msoft-float'`

They can be combined as many times as you wish, in arbitrary ways. This
list:

`   …"--target_board=unix/-Wextra\{-O3,-fno-strength\}\{-fomit-frame,\}"`

will generate four combinations, all involving `-Wextra`.

The disadvantage to this method is that the testsuites are run in
serial, which is a waste on multiprocessor systems. For users with
`GNU Make` and a shell which performs brace expansion, you can run the
testsuites in parallel by having the shell perform the combinations and
make do the parallel runs. Instead of using `--target_board`, use a
special makefile target:

`   make -jN check-testsuite//test-target/option1/option2/…`

For example,

`   make -j3 check-gcc//sh-hms-sim/{-m1,-m2,-m3,-m3e,-m4}/{,-nofpu}`

will run three concurrent `make-gcc` testsuites, eventually testing all
ten combinations as described above. Note that this is currently only
supported in the gcc subdirectory. (To see how this works, try typing
echo before the example given here.)

APPENDIX B: How to interpret test results?
------------------------------------------

The result of running the testsuite are various `*.sum` and `*.log`
files in the testsuite subdirectories. The `*.log` files contain a
detailed log of the compiler invocations and the corresponding results,
the `*.sum` files summarize the results. These summaries contain status
codes for all tests:

  -------------- --------------------------------------------
  Mark           Status
                 
  PASS:          the test passed as expected
  XPASS:         the test unexpectedly passed
  FAIL:          the test unexpectedly failed
  XFAIL:         the test failed as expected
  UNSUPPORTED:   the test is not supported on this platform
  ERROR:         the testsuite detected an error
  WARNING:       the testsuite detected a possible problem
  -------------- --------------------------------------------

APPENDIX C: Collect testsute results
------------------------------------

To collect testsuite results, you need to store all `*.log/*.sum` files
produced by testsute:

`   cd ${GCC_BUILD_DIR}`\
`   export TEST_RESULTS="${GCC_DIR}/testresults/"`\
`   # Create a folder to store .sum/.log result files`\
`   mkdir -p ${TEST_RESULTS}`\
`   cp $(find . -name "*.sum") ${TEST_RESULTS}`\
`   cp --parents $(find . -name "*.log"  \! -name "config.log" | grep -v 'acats.\?/tests' ) ${TEST_RESULTS}`\
`   chmod 644 $(find ${TEST_RESULTS} -type f)`

And now you should have something like this in the `${TEST_RESULTS}`
directory:

`   ├── obj`\
`   │   ├── gcc`\
`   │   │   └── testsuite`\
`   │   │       ├── g++`\
`   │   │       │   ├── g++.log`\
`   │   │       │   ├── g++.sum`\
`   │   │       ├── gfortran`\
`   │   │       │   ├── gfortran.log`\
`   │   │       │   ├── gfortran.sum`\
`   │   ├── gmp`\
`   │   │   └── tests`\
`   │   │       ├── cxx`\
`   │   │       │   └── test-suite.log`\
`   │   │       ├── misc`\
`   │   │       │   ├── test-suite.log`\
`   │   │       │   ├── t-locale.log`\
`   │   │       │   ├── t-printf.log`\
`   │   │       │   └── t-scanf.log`\
`   │   │       ├── mpf`\
`   │   │       │   ├── reuse.log`\
`   │   │       │   ├── t-add.log`\
`   │   │       │   ├── t-cmp_d.log`\
`   │   │       │   ├── t-cmp_si.log`\
`   │   │       │   ├── t-conv.log`\
`   ....`

APPENDIX D: Compare 2 testsuite results
---------------------------------------

To compare difference between 2 testsuite results you can use bash
script `compare_tests` from `${GCC_DIR}/contrib` folder:

Usage:

`   ${GCC_CONTRIB_DIR}/compare_tests /testresults/old_result /testresults/new_result`

Example output:

`   # Comparing directories`\
`   ## Dir1=testresults/old_result: 14 sum files`\
`   ## Dir2=testresults/new_result: 14 sum files`\
`   `\
`   # Extra sum files in Dir1=testresults/old_result`\
`   < testresults/old_result/obj/i586-tizen-linux-gnu/libatomic/testsuite/libatomic.sum`\
`   < testresults/old_result/obj/i586-tizen-linux-gnu/libgomp/testsuite/libgomp.sum`\
`   < testresults/old_result/obj/i586-tizen-linux-gnu/libitm/testsuite/libitm.sum`\
`   < testresults/old_result/obj/i586-tizen-linux-gnu/libstdc++-v3/testsuite/libstdc++.sum`\
`   `\
`   # Extra sum files in Dir2=testresults/new_result`\
`   > testresults/new_result/obj/x86_64-tizen-linux-gnu/libatomic/testsuite/libatomic.sum`\
`   > testresults/new_result/obj/x86_64-tizen-linux-gnu/libgomp/testsuite/libgomp.sum`\
`   > testresults/new_result/obj/x86_64-tizen-linux-gnu/libitm/testsuite/libitm.sum`\
`   > testresults/new_result/obj/x86_64-tizen-linux-gnu/libstdc++-v3/testsuite/libstdc++.sum`\
`   `\
`   # Comparing 10 common sum files`\
`   ## /bin/sh ./contrib/compare_tests  /tmp/gxx-sum1.24630 /tmp/gxx-sum2.24630`\
`   Tests that now fail, but worked before:`\
`   `\
`   21_strings/basic_string/allocator/char/move.cc execution test`\
`   21_strings/basic_string/allocator/char/move_assign.cc execution test`\
`   21_strings/basic_string/allocator/wchar_t/move.cc execution test`\
`   21_strings/basic_string/allocator/wchar_t/move_assign.cc execution test`\
`   21_strings/basic_string/requirements/exception/basic.cc execution test`\
`   23_containers/vector/bool/modifiers/insert/31370.cc execution test`\
`   27_io/basic_ostringstream/cons/move.cc execution test`\
`   27_io/basic_stringstream/cons/move.cc execution test`\
`   `\
`   Tests that now work, but didn't before:`\
`   `\
`   c-c++-common/asan/allocator_oom_test-1.c   -O0  (test for excess errors)`\
`   c-c++-common/asan/allocator_oom_test-1.c   -O0  (test for excess errors)`\
`   c-c++-common/asan/allocator_oom_test-1.c   -O1  (test for excess errors)`\
`   c-c++-common/asan/allocator_oom_test-1.c   -O1  (test for excess errors)`\
`   c-c++-common/asan/allocator_oom_test-1.c   -O2  (test for excess errors)`\
`   c-c++-common/asan/allocator_oom_test-1.c   -O2  (test for excess errors)`\
`   `\
`   New tests that FAIL:`\
`   `\
`   c-c++-common/isan/overflow-add.c   -O3 -g  output pattern test`\
`   c-c++-common/isan/overflow-add.c   -O3 -g  output pattern test`\
`   c-c++-common/isan/overflow-add.c   -Os  output pattern test`\
`   c-c++-common/isan/overflow-add.c   -Os  output pattern test`\
`   c-c++-common/isan/overflow-mul.c   -O0  output pattern test`\
`   c-c++-common/isan/overflow-mul.c   -O0  output pattern test`\
`   c-c++-common/isan/overflow-mul.c   -O1  output pattern test`\
`   c-c++-common/isan/overflow-mul.c   -O1  output pattern test`\
`   c-c++-common/isan/overflow-mul.c   -O2  output pattern test`\
`   c-c++-common/isan/overflow-mul.c   -O2  output pattern test`\
`   c-c++-common/isan/overflow-mul.c   -O2 -flto -fno-use-linker-plugin -flto-partition=none  output pattern test`\
`   `\
`   New tests that PASS:`\
`   `\
`   c-c++-common/asan/no-asan-stack.c   -O0   scan-assembler-not 0x41b58ab3|0x41B58AB3|1102416563`\
`   c-c++-common/asan/no-asan-stack.c   -O0   scan-assembler-not 0x41b58ab3|0x41B58AB3|1102416563`\
`   c-c++-common/asan/no-asan-stack.c   -O0   scan-assembler-not 0x41b58ab3|0x41B58AB3|1102416563`\
`   c-c++-common/asan/no-asan-stack.c   -O0   scan-assembler-not 0x41b58ab3|0x41B58AB3|1102416563`\
`   `\
`   Old tests that passed, that have disappeared: (Eeek!)`\
`   `\
`   23_containers/map/modifiers/erase/dr130-linkage-check.cc (test for excess errors)`\
`   23_containers/map/modifiers/erase/dr130-linkage-check.cc execution test`\
`   23_containers/multimap/modifiers/erase/dr130-linkage-check.cc (test for excess errors)`\
`   23_containers/multimap/modifiers/erase/dr130-linkage-check.cc execution test`\
`   23_containers/multiset/modifiers/erase/dr130-linkage-check.cc (test for excess errors)`\
`   23_containers/multiset/modifiers/erase/dr130-linkage-check.cc execution test`\
`   23_containers/set/modifiers/erase/dr130-linkage-check.cc (test for excess errors)`\
`   23_containers/set/modifiers/erase/dr130-linkage-check.cc execution test`\
`   `\
`   ## Differences found:`\
`   # 1 differences in 10 common sum files found`

APPENDIX E: <WIP> Configure target device with 1 script
-------------------------------------------------------

`   #!/usr/bin/env bash`\
`   `\
`   set -eux`\
`   `\
``    # Modify sdb path if `sdb` is not visible ``\
`   sdb_root_on() {`\
`       # TODO: additional checks?`\
`       ~/Downloads/sdb_2.2.31_ubuntu-64/data/tools/sdb root on`\
`   }`\
`   `\
`   sdb_shell() {`\
`       ~/Downloads/sdb_2.2.31_ubuntu-64/data/tools/sdb shell ${@}`\
`   }`\
`   `\
`   sdb_root_on`\
`   `\
`   # Sanity check`\
`   sdb_shell uname -a || exit 1`

[Category:Tool](Category:Tool "wikilink")
