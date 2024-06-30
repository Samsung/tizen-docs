Introduction
============

All parts until [\#Deploy to OBS](#Deploy_to_OBS "wikilink") are done
locally on developers PC. The only prerequisite for bootstrapping is
Linux distribution with development kit installed --- you will need
Autotools, GNU Make, CMake, GCC-base toolchain (compiler, binutils,
glibc-devel package and so on). Also Linux kernel
[https://www.kernel.org/doc/Documentation/admin-guide/binfmt-misc.rst
binfmt](https://www.kernel.org/doc/Documentation/admin-guide/binfmt-misc.rst_binfmt "wikilink")
feature should be enabled.

### Useful links

The main things used during bootstrapping are

1.  [Linux From Scratch](http://www.linuxfromscratch.org/lfs/) handbook
2.  [GCC
    Cross-toolchain](https://gcc.gnu.org/wiki/Building_Cross_Toolchains_with_gcc)
    build howto

Sources
=======

Sources for bootstrap have been taken from Linaro and patched with Tizen
project specific patches. As we don\'t have a separate file storage for
toolchain, sources can be downloaded right from OBS project. Here is
list of packages used during bootstrap:

1.  [binutils](https://build.tizen.org/package/show/Tizen:Base/binutils)
2.  [gcc](https://build.tizen.org/package/show/Tizen:Base/linaro-gcc)
3.  [rpm](https://build.tizen.org/package/show/Tizen:Base/rpm)
4.  [glibc](https://build.tizen.org/package/show/Tizen:Base/glibc)
5.  [qemu](https://build.tizen.org/package/show/Tools:qemu:2.7.x/qemu)

Bootstrap process
=================

The bootstrap produces working toolchain which may be used for initial
creation of Tizen environment. At the end of the process you will have a
toolchain and libc, which is enough to start building console tools and
libraries. The compiler bootstrap process is commonly known and is used
from time to time by different Linux distributions maintainers during
ports to new architecture, main difference is using Tizen-specific flags
during packages configuration, for example, aarch64-tizen-linux-gnu
target has been used. During this initial bootstrap sources have been
patched by hands one-by-one accordingly to spec-file patch sequence,
this work has to be done manually until you have working *rpmbuild* tool
which automates this job. It will happen after finishing [\#Build
RPM](#Build_RPM "wikilink") section of this manual.

Build Cross-compiler
--------------------

Common environment variables during build

`export ARCH=aarch64`\
`export LINUX_ARCH=arm64`\
`export CPU=armv8-a`\
`export TARGET=${ARCH}-tizen-linux-gnu`\
`export PREFIX=~/rootfs/`\
`export CROSS_COMPILE=${TARGET}-`\
`export PATH=$PATH:${PREFIX}/bin`\
`export TOOLCHAIN_ROOT=$(pwd)/toolchain`\
`mkdir -p ${PREFIX}/src`

### Binutils

`cd path/src/binutils`\
`mkdir build-dir`\
`cd build-dir`\
`../configure \`\
`  --prefix=${TOOLCHAIN_ROOT} \`\
`  --with-pkgversion='GNU Binutils; Tizen OS bootstrap / aarch' \`\
`  --disable-multilib \`\
`  --target=${TARGET}`\
`make`\
`make install`

### Linux Kernel Headers

Set up headers for *glibc*

#### Option 1

Download ready kernel headers from package \"linux-glibc-devel\". It can
be found e. g. at build.tizen.org for other architectures, since it\'s
architecture-independent. It contains headers that are installed to
/usr/include.

Move all headers to /usr/include

`unrpm linux-glibc-devel*.rpm`\
`cp -r ./usr/include/* ${TOOLCHAIN_ROOT}/${TARGET}/include`

#### Option 2

Or you can perform headers install from kernel

`make ARCH=${LINUX_ARCH} INSTALL_HDR_PATH=${TOOLCHAIN_ROOT}/${TARGET} headers_install`

### GCC step 1

`cd path/src/gcc`\
`mkdir build`\
`cd build`\
`../configure \`\
`  --prefix=${TOOLCHAIN_ROOT} \`\
`  --disable-multilib \`\
`  --build=${MACHTYPE} \`\
`  --with-arch=${CPU} \`\
`  --enable-languages=c,c++ \`\
`  --target=${TARGET}`

`make all-gcc`\
`make install-gcc`

### Glibc headers

`cd path/src/glibc`

`mkdir build`\
`cd build`

`CFLAGS="-O2 -g " \`\
`CC=${TOOLCHAIN_ROOT}/bin/${TARGET}-gcc \`\
`LD=${TOOLCHAIN_ROOT}/bin/${TARGET}-ld \`\
`../configure \`\
`  --build=${MACHTYPE} \`\
`  --host=${TARGET} \`\
`  --target=${TARGET} \`\
`  --prefix=${TOOLCHAIN_ROOT} \`\
`  --enable-add-ons \`\
`  --with-headers=${TOOLCHAIN_ROOT}/${TARGET}/include \`\
`  --disable-multilib \`\
`  libc_cv_forced_unwind=yes \`\
`  libc_cv_c_cleanup=yes`

`make install-bootstrap-headers=yes install-headers`\
`make csu/subdir_lib`\
`install csu/crt1.o csu/crti.o csu/crtn.o ${TOOLCHAIN_ROOT}/${TARGET}/lib`\
`${TOOLCHAIN_ROOT}/bin/${TARGET}-gcc -nostdlib -nostartfiles -shared -x c /dev/null -o ${TOOLCHAIN_ROOT}/lib/libc.so`\
`touch ${TOOLCHAIN_ROOT}/${TARGET}/include/gnu/stubs.h`

### libgcc

`cd path/src/gcc/build`\
`make all-target-libgcc`\
`make install-target-libgcc`

### Glibc

`cd path/src/glibc/build`\
`make`\
`make install`

### GCC step 2

`cd path/src/gcc`\
`make`\
`make install`

Initial Tizen environment build
-------------------------------

Initial environment is used during Base packages creation: it should
contain at least *rpmbuild* with dependencies and minimal build tools to
make rpmbuild able to create packages. This step results into RPM set,
ready for binary import into OBS project and start build there. After
the rpmbuild starts working there is no more need to patch sources by
hands and set up flags manually as it was in [\#Bootstrap
process](#Bootstrap_process "wikilink"). Subsection [\#Rebuild packages
with rpmbuild](#Rebuild_packages_with_rpmbuild "wikilink") repeats OBS
build environment work on local machine and produces the same output OBS
builserver does: resulting RPMs will be fully compatible with OBS build
environment and can be used by it.

Build qemu
----------

To make aarch64 build work the cpu emulator will be needed.
qemu-linux-user is used inside OBS environment, so it will be used.
Working AArch64 support appeared in qemu 2.0 release, but now it\'s
still being developed, so the best option for bootstrap is to get latest
git version. As OBS works with non-standard qemu binary
\"qemu-arm64-binfmt\" you will still need to apply at least patches
*0011-linux-user-add-binfmt-wrapper-for-argv-0-handling.patch* and
*0016-linux-user-binfmt-support-host-binaries.patch* from Tizen project
to work with OBS binformat configuration.

`./configure --prefix=/usr --sysconfdir=/etc --libexecdir=/usr/libexec --enable-linux-user --disable-system --enable-attr --static --disable-linux-aio --extra-cflags="-Wno-error=type-limits" --target-list=${ARCH}-linux-user --disable-libnfs`\
`make`

After that you will get qemu-arm64-binfmt binary, you need no install it
- it should be copied to chroot later. However it\'s good idea to use
this qemu during initial buildroot set up, so now it should be copied to
bin directory and binformat set to use it

`sudo cp aarch64-linux-user/qemu-arm64-binfmt /usr/bin`\
`echo ':aarch64:M::\x7fELF\x02\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\xb7:\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\xfe\xff\xff:/usr/bin/qemu-arm64-binfmt:P' > /proc/sys/fs/binfmt_misc/register`

Now you host machine is able to run aarch64 binaries.

`cp aarch64-linux-user/qemu-arm64-binfmt /path/to/buildroot/usr/bin`

And after installing qemu to buildroot you may try to chroot there.

Target glibc
------------

`mkdir -p ${PREFIX}/usr`\
`cp -r ${TOOLCHAIN_ROOT}/include ${PREFIX}/usr`

`mkdir target-build`\
`cd target-build`

`CFLAGS="-O2 -g " \`\
`CC=${TOOLCHAIN_ROOT}/bin/${TARGET}-gcc \`\
`LD=${TOOLCHAIN_ROOT}/bin/${TARGET}-ld \`\
`../configure \`\
`  --build=${MACHTYPE} \`\
`  --host=${TARGET} \`\
`  --target=${TARGET} \`\
`  --prefix=/usr \`\
`  --enable-add-ons \`\
`  --with-sysroot=${PREFIX} \`\
`  --disable-multilib \`\
`  libc_cv_forced_unwind=yes \`\
`  libc_cv_c_cleanup=yes`

`make`\
`make install DESTDIR=${PREFIX}`

Target binutils
---------------

`mkdir target-build`\
`cd target-build`\
`CC=${TOOLCHAIN_ROOT}/bin/${TARGET}-gcc \`\
`LD=${TOOLCHAIN_ROOT}/bin/${TARGET}-ld \`\
`../configure \`\
`  --host=${TARGET} \`\
`  --target=${TARGET} \`\
`  --prefix=/usr \`\
`  --with-sysroot=${PREFIX} \`\
`  --disable-multilib \`\
`  libc_cv_forced_unwind=yes \`\
`  libc_cv_c_cleanup=yes`\
`make install DESTDIR=${PREFIX}`

Target gcc
----------

`mkdir target-build`\
`cd target-build`\
`CC=${TOOLCHAIN_ROOT}/bin/${TARGET}-gcc \`\
`LD=${TOOLCHAIN_ROOT}/bin/${TARGET}-ld \`\
`../configure \`\
`  --host=${TARGET} \`\
`  --target=${TARGET} \`\
`  --prefix=/usr \`\
`  --with-sysroot=${PREFIX} \`\
`  --disable-multilib \`\
`  libc_cv_forced_unwind=yes \`\
`  libc_cv_c_cleanup=yes`\
`make install DESTDIR=${PREFIX}`

Prerequisites for chrooting
---------------------------

Next step is to receive working native toolchain which will be used by
rpmbuild during package build. During this step you need no fully Tizen
compatible packages with configuration equal to one produced by OBS. To
start RPM only package *placeholders* with minimal configurations will
be enough. So if package can be built without using a dependency ---
build it without a dependency. The most minimal configuration will be
fine, these packages will be replaced by normal ones after they are
built using rpmbuild.

The process is performed using cross-compiler, so the toolchain
environment variables should be set:

`export PATH=${TOOLCHAIN_ROOT}/bin`\
`export CC=${TARGET}-gcc`\
`export CXX=${TARGET}-g++`\
`export CPP=${TARGET}-cpp`\
`export LD=${TARGET}-ld`\
`export AR=${TARGET}-ar`\
`export NM=${TARGET}-nm`\
`export RANLIB=${TARGET}-ranlib`

Then you the process of manual package build is performed, for example
to start with *attr*:

`curl '`[`https://build.tizen.org/package/rawsourcefile?file=attr-2.4.47.src.tar.gz&package=attr&project=devel%3Aarm_toolchain%3AMobile%3ABase`](https://build.tizen.org/package/rawsourcefile?file=attr-2.4.47.src.tar.gz&package=attr&project=devel%3Aarm_toolchain%3AMobile%3ABase)`' -o attr-2.4.47.tar.gz`\
`tar xfz attr-2.4.47.tar.gz`\
`cd attr-2.4.47.tar.gz`\
`./configure --host=${TARGET} --target=${TARGET} --prefix=/usr`\
`make`\
`make install DESTDIR=${PREFIX}`

In order to speedup build process you may use *make -jN* command, where
*N* is number of threads make will use for build. Note: if you get
message like

`` Invalid configuration `aarch64-tizen-linux-gnu': machine `aarch64-tizen' not recognized ``

you may try to use *aarch64-unknown-linux-gnu* host and target type, if
this fails as well try running

`autoreconf -fi`

in source path to update GNU Autotools script to support aarch64
architecture.

The next step is create a minimal shell for buildroot:

`mkdir ~/rpmbuild/SOURCES/`\
`osc co -S Tizen:Base bash`\
`cd Tizen\:Base/bash`\
`` for f in `ls _service:*`; do mv $f $(echo $f | sed -e 's/_service:gbs://'); done ``\
`tar xf bash-3.2.57.tgz`\
`cd bash-3.2.57`\
`./configure --host=${TARGET} --target=${TARGET} --prefix=/usr --disable-job-control --enable-static-link --enable-minimal-config`\
`make`\
`make install DESTDIR=${PREFIX}`

This will provide a statically linked minimal shell which makes possible
to chroot inside the your buildroot and check things from inside. Such
test could be performed using

`mkdir -p ${PREFIX}/dev ${PREFIX}/sys ${PREFIX}/proc ${PREFIX}/tmp ${PREFIX}/root`\
`for dir in proc sys dev dev/pts dev/shm dev/mqueue proc/sys/fs/binfmt_misc proc/fs/nfsd; do`\
`   sudo mount -o bind /$dir ${PREFIX}/$dir`\
`done`\
`chroot ${PREFIX} /usr/bin/bash`

If previous steps have been completed successfully you should see a bash
prompt and working *attr* binary.

Create build environment inside chroot
--------------------------------------

Now you\'ll need to get minimal set of tools using

`cd pkg-name && mkdir build && cd build && ../configure --prefix=/usr --target=${TARGET} --host=${TARGET} && make && make install DESTDIR=${PREFIX}`

Great place to begin is building *grep*, *sed*, *gawk*, *m4*,
*diffutils*, *texinfo* since they are used for *configure* scripts. The
next steps are: perl, readline, ncurses, texinfo, nspr, nss, zlib, gzip,
xz, bzip2, tar, findutils, autoconf, automake, gettext, libtool, glib,
pkg-config. After you get minimal set using cross-compiler you can try
to boostrap compiler inside your new buildroot.

Build RPM
---------

Next step is building RPM package manager with *rpmbuild* tool to create
suitable packages to deploy binaries into OBS.

### Prerequisites for RPM

This is an iterative process starting with getting RPM sources from,
patching it accordingly to spec file from [project
page](https://build.tizen.org/package/show?package=rpm&project=Tizen:Base)
and compilation tries until succeeded. These actions can be performed
without *rpmbuild*, you can just use compilation from tarballs. So get
tarball with RPM, unpack and try to build it.

1.  Try to compile RPM with *./configure*
2.  Check if build fails because of missing dependency. E. g. first time
    it\'ll fail with with message that *nss* and *nspr* packages could
    not be found.
3.  Find, build and install missing package (with its own dependencies)
    1.  Download *nss* package, *configure && make && make install*
    2.  Download *nspr* package, *configure && make && make install*
4.  Return to 1. Repeat until you get working RPM.

During this step you need a minimal working RPM, so it\'s reasonable to
compile all libraries with *\--enable-minimal* flag if one has it.

Rebuild packages with rpmbuild
------------------------------

Now when you get a working *rpmbuild*, you may start building packages
ready for upload to OBS. You create a separate console, chroot inside
resulting system and start using rpmbuild.

From this step you should not track dependencies manually and configure
packages some specific way - rpmbuild does it by itself. If you don\'t
have a file which is needed to build a certain package, rpmbuild will
show a message.

`for dir in proc sys dev dev/pts dev/shm dev/mqueue proc/sys/fs/binfmt_misc proc/fs/nfsd; do`\
`   sudo mount -o bind /$dir ${PREFIX}/$dir`\
`done`\
`sudo chroot ${PREFIX} /bin/sh`

Before you start working with rpm packages in system you should
initialize rpm database

`rpm --initdb`

As rpmbuild provides a featured version of package, respectively to one
created during previous step, it\'s a good idea to install package after
it\'s built. This action works as a quick test also.

So approximate algorithm of package creation

`cp -r /path/to/obs/sources/acl/ /path/to/chroot/usr/src/packages/SOURCES`

And then, from chrooted terminal:

`rpmbuild -ba --define '_srcdefattr (-,root,root)' --nosignature --target=aarch64-tizen-linux /usr/src/packages/SOURCES/acl/acl.spec`\
`rpm -i --force /usr/src/packages/RPMS/aarch64/acl*.rpm`

Environment test
================

To test environment a simple deployment test could be performed.

`rpm --initdb --root=/tmp/testroot /mnt/bootstrapped_rpm_path/*`

Then try to chroot there:

`chroot /tmp/testroot /bin/bash`

and you should get a usable rpmbuild.

Build native compiler
---------------------

Native compiler can be built in a much simpler way than cross compiler,
since it can be built in only 1 stage directly. To do this, you should
perform configure process (like in the stage 2 of section [\#Build
Cross-compiler](#Build_Cross-compiler "wikilink")) except one small
change: to make compiler native, all values of options \"\--target\",
\"\--host\" and \"\--build\" should be the same and should be equal
\"aarch64-tizen-linux\"

### Binutils

`mkdir build-dir`\
`cd build-dir`\
`EXTRA_TARGETS=${TARGET}`\
`TARGET_OS=${TARGET}`\
`../configure 'CFLAGS=-O2 -g -fmessage-length=0 -D_FORTIFY_SOURCE=2 -fstack-protector -funwind-tables -fasynchronous-unwind-tables -Wno-error' \`\
`  --prefix=/usr \`\
`  '--with-pkgversion=GNU Binutils; Tizen bootstrap / aarch' \`\
`  --disable-nls \`\
`  --build=${TARGET} \`\
`  --target=${TARGET} \`\
`  --enable-targets=${TARGET}`\
`make`\
`make install DESTDIR=${PREFIX}`

Deploy to OBS
=============

Deployment process is described on [OSDev/Creating AArch64
Project](OSDev/Creating_AArch64_Project "wikilink") page. The deployment
process is just importing RPMs created locally onto buildserver using
*Binary import* manual for your version of OBS environment. These RPMs
may be used by any project after import, imported RPMs usage example
exists on
[OSDev/Using\_OBS\#Creating\_own\_development\_project](OSDev/Using_OBS#Creating_own_development_project "wikilink")
page.

[Category:Tool](Category:Tool "wikilink")
