Introduction
============

This document is to describe how to build Tizen 5.0 profile using GBS
fullbuild and create Tizen images using MIC for TM1 reference phone.\
\* TM1 specification: <https://wiki.tizen.org/wiki/TM1>

-   Full source: <http://review.tizen.org>
-   Branch: tizen
-   Target: TM1 (Z3)
-   Linux distribution: Ubuntu 16.04.3 X64 LTS
-   Repository:
    <http://download.tizen.org/snapshots/tizen/%7Bbase%7Cmobile>}

As a prerequisite, You must install GBS and MIC software by reading
\\How to install GBS and MIC is well described in official Tizen
documentation.

-   GBS:
    <https://source.tizen.org/documentation/reference/git-build-system>,
-   MIC image creator:
    <https://source.tizen.org/documentation/reference/mic-image-creator>\
    \

How to build Tizen:mobile with arm-wayland repository for TM1 device
will be described to give you an example.\
How to create Tizen images using mic with RPMs created by GBS Local Full
Build will be described in last chapter.

**Example**

    invain@u1604:/work/infra$ gbs --version
    gbs 0.24.1
    invain@u1604:/work/infra$ mic --version
    mic 0.27.1
    invain@u1604:/work/infra$ cat /etc/lsb-release 
    DISTRIB_ID=Ubuntu
    DISTRIB_RELEASE=16.04
    DISTRIB_CODENAME=trusty
    DISTRIB_DESCRIPTION="Ubuntu 16.04.4 LTS"

There are two ways to construct full source tree of Tizen 5.0 as
follows. In this page, We only depict how to build Tizen 5.0 full source
for TM1.

-   Use \'\*.src.rpm\'
-   Use \'repo init\' and \'repo sync\'

Download full source using repo
===============================

Setup parameters
----------------

Below describes the meaning of the each environment variable.

-   workspace : overall workspace\
-   buildroot: GBS build will be run and build result (RPMs and logs)
    will be located in this buildroot\
-   snapshot\_date: snapshot date that is available in the official
    repository.
-   snapshot\_base: snapshot url where pre-built rpms are published\
-   snapshot\_mobile: snapshot url where \*.src.rpm (which you want to
    build) are published\
-   repo\_base: path where pre-built rpms are downloaded\

**Example**

    $ workspace=/work/infra/gbs_fullbuild_mobile
    $ buildroot=$workspace/GBS-ROOT/
    $ snapshot_date=20180103.1
    $ snapshot_base=http://download.tizen.org/snapshots/tizen/base/tizen-base_${snapshot_date}/
    $ snapshot_mobile=http://download.tizen.org/snapshots/tizen/mobile/tizen-mobile_${snapshot_date}/
    $ repo_base=$workspace/pre-built/toolchain-arm/
     

    $ mkdir -p $workspace
    $ $ cd $workspace

\

Getting full source with repo command
-------------------------------------

-   To initialize repositories, Run repo init -u
    <ssh://><user_name>\@review.tizen.org:29418/scm/manifest -b <branch>
    -m <profile>.xml\
-   Replace projects.xml file inside \$workspace/.repo/ with manifest
    file in \$snapshot\_mobile\
-   To download latest repository, Run repo sync\

**Example**

    $ cd $workspace
    $ vi  ~/.ssh/config 
    Host review.tizen.org
    User <your_name>
    Identityfile ~/.ssh/tizen_rsa
    HostName review.tizen.org
    Port 29418
    $
    $ ssh -p 29418 <your_user_name>@review.tizen.org

      ****    Welcome to Gerrit Code Review    ****
      Hi Your Name, you have successfully connected over SSH.

      Unfortunately, interactive shells are disabled.
      To clone a hosted Git repository, use:
      git clone ssh://<your_user_name>@review.tizen.org:29418/REPOSITORY_NAME.git

    $ repo init -u ssh://<your_user_name>@review.tizen.org:29418/scm/manifest -b tizen -m mobile.xml 
    $ pushd ./.repo/manifests/mobile/
    $ wget $snapshot_mobile/builddata/manifest/tizen-mobile_${snapshot_date}_arm-wayland.xml
    $ mv projects.xml projects.xml.original
    $ mv tizen-mobile_${snapshot_date}_arm-wayland.xml  projects.xml
    $ popd
    $ time repo sync -j<CPU_NUMBER>

            . . . . . . OMISSSION . . . . . . 
     * [new tag]         v4.1.6     -> v4.1.6
     * [new tag]         v4.1.7     -> v4.1.7
     * [new tag]         v4.1.8     -> v4.1.8
     * [new tag]         v4.1.9     -> v4.1.9
    Fetching projects: 100% (624/624), done.  
    Checking out files: 100% (294637/294637), done. files:   4% (12474/294637)   
    Checking out files: 100% (43880/43880), done.
    Checking out files: 100% (50027/50027), done.ut files:  31% (15715/50027)   
    Checking out files: 100% (45937/45937), done.ut files:  36% (16588/45937)   
    Checking out files: 100% (46180/46180), done.ut files:  42% (19602/46180)   
    Syncing work tree: 100% (624/624), done.  

    real    49m51.088s
    user    16m59.840s
    sys 4m46.556s
    invain@db400:/work/infra/gbs_fullbuild_mobile$ 

-   If \"repo sync\" command completes successfully, you can have to see
    the below files and folders.

**Example**

    nvain@u1604:/work/infra/gbs_fullbuild_mobile$ ls -al
    total 44
    drwxrwxr-x 10 invain invain 4096  8\uc6d4  6 13:00 .
    drwxrwxr-x  3 invain invain 4096  8\uc6d4  6 12:24 ..
    -r--r--r--  1 invain invain  471  8\uc6d4  6 13:00 .gbs.conf
    drwxrwxr-x  7 invain invain 4096  8\uc6d4  6 09:43 .repo
    drwxrwxr-x  4 invain invain 4096  8\uc6d4  6 12:58 apps
    drwxrwxr-x  7 invain invain 4096  8\uc6d4  6 12:59 platform
    drwxrwxr-x  4 invain invain 4096  8\uc6d4  6 12:59 pre-built
    drwxrwxr-x  3 invain invain 4096  8\uc6d4  6 12:59 profile
    drwxrwxr-x  3 invain invain 4096  8\uc6d4  6 13:00 scm
    drwxrwxr-x  3 invain invain 4096  8\uc6d4  6 13:00 sdk
    drwxrwxr-x  6 invain invain 4096  8\uc6d4  6 13:00 tools
    invain@u1604:/work/infra/gbs_fullbuild_mobile$ 
    invain@u1604:/work/infra/gbs_fullbuild_mobile$ 
    invain@u1604:/work/infra/gbs_fullbuild_mobile$ du -sh ./.repo/
    14G           ./.repo/
    invain@u1604:/work/infra/gbs_fullbuild_mobile$ 
    invain@u1604:/work/infra/gbs_fullbuild_mobile$ 
    invain@u1604:/work/infra/gbs_fullbuild_mobile$ du -sh ./*
    45M         ./apps
    9.9G            ./platform
    196M    ./pre-built
    943M    ./profile
    208K    ./scm
    696K    ./sdk
    996K    ./tools

\
\* **TroubleShooting**: When there is en error in \'repo sync\', check
whether or not git project name of \'projects.xml\' exists in
<http://review.tizen.org>. If you face **\"error: Exited sync due to
fetch errors\"** message, try to run \"repo sync -f\" command. If you
face the error message repeatedly, you can find the reason of the issue
by running \"repo sync -f 2\>repo-sync-error.txt
1\>repo-sync-output.txt\" command in order to modify correctly the
folder name of the projects.

**Example**

    # Find incorrect project paths
    $ repo sync -f 2>repo-sync-error.txt 1>repo-sync-output.txt
    $ cat ./repo-sync-error.txt | grep error
    # Then, modify correctly a project path in the projects.xml file after checking  the latest project path on http://review.tizen.org.
    $ vim .repo/manifests/mobile/projects.xml
    platform/framework/base/tizen-locale                    --> platform/core/base/tizen-locale
     

If you want to modify the incorrect project paths automatically, we
recommend that you try to use check\_manifest.py script file that is
located in the ./\$workspace/.repo/manifests/Check\_manfiest/ folder.

**Example**

    cd /work/infra/gbs_fullbuild_mobile_20180117.1-1
    time repo init -u https://pbs:TylhenFPwSGpNtEg19ZA6u81ylrvqvEiAiemsF4MpQ@review.tizen.org/gerrit/p/scm/manifest -b tizen -m common.xml 
    cat ./repo/manifests/README
    vi  ./.repo/manifests/Check_manfiest/check_manifest.py
         171 gc = GerritClient('https://review.tizen.org/gerrit', '<usrname>', '<passwd>')
    ./.repo/manifests/Check_manfiest/check_manifest.py  --help
    ./.repo/manifests/Check_manfiest/check_manifest.py  --tizen-src .  -p common --url common-latest  --update
    cat  tizen_mobile_revision_diff.csv
     

\

Building full source using gbs
==============================

Get build.conf from official website
------------------------------------

-   Download xxxx-build.conf.gz from \$
    snapshot\_mobile/repos/arm-wayland/packages/repodata/ to
    \$workspace/scm/meta/build-config\
-   Run \"unzip xxxx-build.conf.gz\"\
-   Replace xxxx-build.conf.gz with
    \$workspace/scm/meta/build-config/build.conf\

**Example**

    $ cd $workspace
    $ curl $snapshot_mobile/repos/arm-wayland/packages/repodata/xxx-build.conf.gz|gunzip > ./scm/meta/build-config/build.conf

\

Configure .gbs.conf file
------------------------

-   Note that buildroot and buildconf variable must be existed in
    \$workspace/.gbs.conf for full build. If \$workspace/.gbs.conf is
    not existed, gbs try to find \~/.gbs.conf file.\

**Example**

    $ vi $workspace/.gbs.conf
     
    [general]
    tmpdir=/var/tmp/
    profile = profile.tizen5.0_mobile
    work_dir=.
    fallback_to_native=true
     
    [repo.tizen5.0_x86]
    url=${work_dir}/pre-built/toolchain-x86/
     
    [repo.tizen5.0_arm]
    url=${work_dir}/pre-built/toolchain-arm/
     
    [repo.tizen5.0_base]                                          <==== Here!!! Append this line.
    url=${work_dir}/pre-built/toolchain-arm/                      <==== Here!!! Append this line.
                                                                                                                                 
    [repo.tizen5.0_arm64]
    url=${work_dir}/pre-built/toolchain-arm64/
     
    [profile.tizen5.0_mobile]
    repos=repo.tizen5.0_x86,repo.tizen5.0_arm,repo.tizen5.0_base  <==== Here!!! Append this line.
    buildconf=${work_dir}/scm/meta/build-config/build.conf
    buildroot=./GBS-ROOT/                                         <==== Here!!! Append this line. (*Caution: Don't use ${work_dir} for buildroot)
    exclude_packages=libtool,gettext,texinfo

\

Build full source with gbs command
----------------------------------

-   Run \"gbs build\" command in \$workspace folder with appropriate
    build options.\
-   Refer to
    <https://source.tizen.org/ko/documentation/developer-guide/getting-started-guide/building-packages-locally-gbs>
    in order to set the list of packages to be excluded or to break
    dependency circle.
-   While \"gbs build\" command is running, The **depanneur** tool goes
    through local Git trees and evaluates packaging meta-data to
    determine packages needed and the build order. Please, refer to
    <https://wiki.tizen.org/wiki/Working_Mechanism_of_Depanneur> for
    more details on **depanneur**.

**Example**

    $ cd $workspace
    $ accel_pkgs="bash,bzip2-libs,c-ares,cmake,coreutils,diffutils,eglibc,elfutils-libelf,elfutils-libs,elfutils,fdupes,file,findutils,\
    gawk,gmp,gzip,libacl,libattr,libcap,libcurl,libfile,libgcc,liblua,libstdc++,make,mpc,mpfr,\
    ncurses-libs,nodejs,nspr,nss-softokn-freebl,nss,openssl,patch,popt,rpm-build,rpm-libs,rpm,sed,sqlite,tar,xz-libs,zlib,binutils,gcc"
    $ time sudo gbs build -A armv7l --threads=4 --clean-once --exclude=${accel_pkgs},filesystem,aul,libmm-sound,libtool  -B ./GBS-ROOT

-   For you convenience, you can specify the package list using
    \"exclude\_packages\" variable in order to be excluded for building
    as follows. Not that multiple packages can be separated by comma(,)

**Example**

    $ vi $workspace/.gbs.conf
    [profile.tizen5.0_mobile]
    exclude_packages=bash,bzip2-libs,c-ares,cmake,coreutils,diffutils,eglibc,elfutils-libelf,elfutils-libs,elfutils,fdupes,file,findutils,gawk,gmp,gzip,\
    libacl,libattr,libcap,libcurl,libfile,libgcc,liblua,libstdc++,make,mpc,mpfr,ncurses-libs,nodejs,nspr,nss- softokn-freebl,nss,openssl,patch,popt,\
    rpm-build,rpm-libs,rpm,sed,sqlite,tar,xz-libs,zlib,binutils,gcc,filesystem,aul,libmm-sound,libtool

-   Sometimes, you have to utilize the below flags of \"gbs build\"
    command to find a reason of a unexpected issue.

**Example**

    $ time sudo gbs build -A armv7l --threads=4 --clean-once  -B ./GBS-ROOT

    $ gbs build -A armv7l               # build all packages under current dir for armv7l
    $ gbs build -A armv7l --overwrite   # rebuild the packages
    $ gbs build -A armv7l --include-all # build packages including un-commit changes
    $ gbs build -A armv7l --incremental # incremental build
    $ gbs build -A armv7l --noinit      # build with offline mode
    $ gbs build -A armv7l --clean       # clean build by deleting the old build root
    $ gbs build -A armv7l --clean --clean-repos  #clean build by deleting the old build root and old repository
    $ gbs build -A armv7l <gitdir>      # build all packages under <gitdir>

-   **TroubleShooting**: **qemu: Unsupported syscall: 311**

While building all packages, the 311 numbered system call(e.g., **qemu:
Unsupported syscall: 311** ) warning message is displayed because
QEMU\'s linux-user emulation layer doesn\'t currently support any of the
compatible key control system calls. Fortunately, It is not harmful to
build Tizen packages.\

-   **TroubleShooting**: \"**Permission Denied at /usr/bin/depanneur
    line 2017**\" error message

If \"gbs build -A armv7l \...\" command generates the below error
message from second time with the same command (e.g., gbs build \....),
It results from the root privilege for QEMU\'s chroot.

**Example**

    Can't cd to (/work/infra/gbs_fullbuild_mobile/GBS-ROOT/local/BUILD-ROOTS/scratch.armv7l.2/etc/skel/) .applications: Permission Denied
     at /usr/bin/depanneur line 2017.
    Can't cd to (/work/infra/gbs_fullbuild_mobile/GBS-ROOT/local/BUILD-ROOTS/scratch.armv7l.2/etc/skel/) apps_rw: Permission Denied
     at /usr/bin/depanneur line 2017.
    Can't cd to (/work/infra/gbs_fullbuild_mobile/GBS-ROOT/local/BUILD-ROOTS/scratch.armv7l.2/etc/ssl/) private: Permission Denied
     at /usr/bin/depanneur line 2017.
    Can't cd to (/work/infra/gbs_fullbuild_mobile/GBS-ROOT/local/BUILD-ROOTS/scratch.armv7l.2/) root: Permission Denied
     at /usr/bin/depanneur line 2017.
    Can't cd to (/work/infra/gbs_fullbuild_mobile/GBS-ROOT/local/BUILD-ROOTS/scratch.armv7l.2/var/cache/) ldconfig: Permission Denied
     at /usr/bin/depanneur line 2017.

Please, remove ./GBS-ROOT/ folder. OR \"gbs build\" command with sudo.

**Example**

    sudo rm -rf ./GBS-ROOT/

-   **TroubleShooting**: \"**nothing provides pkgconfig(\...)**\" error
    message

It is not mandatory. However,If you face \"**nothing provides
pkgconfig(\...)**\" error message at build-time, you have to follow up
the below recipe that prepares Pre-built RPMs of Base to solve the issue
.

**Solution**: Using local folder as a base repository (Recommended):
Download all the RPMs in \$snapshot\_base/repos/arm/packages/ to
\$repo\_base. Check all the RPMs are well downloaded in \$repo\_base.\
**Example**

    $ wget --directory-prefix=$repo_base --mirror --reject index.html* -r -nH --no-parent --cut-dirs=8 $snapshot_base/repos/arm/packages/
    $ createrepo --update $repo_base
    $ createrepo --update pre-built/toolchain-arm
    $ createrepo --update pre-built/toolchain-x86

-   **TroubleShooting**: the build error of tizen-debug: **nothing
    provides glibc-debuginfo = 2.20**

The tizen-debug package requires glibc-debuginfo package to support
debugging operations(e.g. .debug\_frame section) via valgrind. The
glibc-debuginfo package is located in debug folder of download.tizen.org
website. So, you have to append the below repository additonally to
build tizen-debug package normally. **Example**

    http://download.tizen.org/snapshots/tizen/base/latest/repos/arm/debug/

\

-   **TroubleShooting**: error: Start commit \'upstream/x.x.x\' **not an
    ancestor of end commit \'HEAD**\'

Sometime, While running \"gbs build\" command, you can meet the below
error messages as a \"Export Error Packages\" issue. Please, refer to
the
<https://wiki.tizen.org/wiki/Analyzing_GBS_Local_Full_Build_Errors#Upstream_Tag_Issue>
for more details.

**Example**: error messages

      . . . Upper Omission  . . . 
    1941 info: start export source from: /work/infra/gbs_fullbuild_mobile3/platform/upstream/newfs-msdos ...
    1942 info: tracking branch: tizen-gerrit/upstream -> upstream
    1943 info: tracking branch: tizen-gerrit/pristine-tar -> pristine-tar
    1944 warning: Deprecated option '--git-export-only', please use '--no-build' instead!
    1945 info: Generating patches from git (upstream/1.0.0..HEAD)
    1946 error: Start commit 'upstream/1.0.0' not an ancestor of end commit 'HEAD'                                                          
    1947 error: Generating upstream tarball and/or generating patches failed. GBS tried this as you have upstream branch in you git tree. Fix the problem by either:
    1948   1. Update your upstream branch and/or fix the spec file. Also, check the upstream tag format.
    1949   2. Remove or rename the upstream branch (change the package to native)
    1950 See https://source.tizen.org/documentation/reference/git-build-system/upstream-package for more details.
    1951 error: <gbs>Failed to export packaging files from git tree
      . . . Below Omission  . . . 

You have to ask an appropriate package developers in order to fix the
incorrect tagging issue. Actually, this issue is generated by the
package developers that do not correctly observe [the \"Updating
Packages\"
manual](https://wiki.tizen.org/wiki/Updating_packages#3._Use_tarball)

**Example** : How to fix the issue

    $ git checkout tizen
    $ gbs submit -m "update to x.x.x"

Creating image using MIC
========================

Mobile Image Creator (MIC) is used to create images for Tizen software
platform.

Setup parameters
----------------

-   workspace : overall workspace for mic\
-   mic\_workspace: path for MIC workspace\
-   mic\_images: path where images are created\
-   mic\_ks\_files: path where \*.ks files are downloaded\
-   mic\_logs: path where mic log files are saved\
-   snapshot\_date: snapshot date that is available in the official
    repository.\
-   snapshot\_mobile which is used in GBS Local Fullbuild\
-   repo\_base: path which is used in GBS Local Fullbuild\

**Example**

    $ workspace=/work/infra/gbs_fullbuild_mobile
    $ mic_workspace=$workspace/mic_workspace
    $ mic_images=$mic_workspace/images
    $ mic_ks_files=$mic_workspace/builddata/image-configs
    $ mic_logs=$mic_workspace/builddata/logs
    $ snapshot_date=20180103.1
    $ snapshot_mobile=http://download.tizen.org/snapshots/tizen/mobile/tizen-mobile_$snapshot_date/
    $ repo_base=$workspace/pre-built/toolchain-arm/

    $ mkdir -p $mic_workspace $mic_images $mic_ks_files $mic_logs

\

Download \*.ks file
-------------------

-   Download \*.ks file (kickstart file) what you want from
    \$snapshot\_mobile/images\

`* `[`http://download.tizen.org/snapshots/tizen/mobile/latest/images/target-TM1/mobile-wayland-armv7l-tm1/tizen-mobile_${snaptshot_date}_mobile-wayland-armv7l-tm1.ks`](http://download.tizen.org/snapshots/tizen/mobile/latest/images/target-TM1/mobile-wayland-armv7l-tm1/tizen-mobile_$%7Bsnaptshot_date%7D_mobile-wayland-armv7l-tm1.ks)

**Example**

    $ wget --directory-prefix=$mic_ks_files $snapshot_mobile/images/target-TM1/mobile-wayland-armv7l-tm1/tizen-mobile_${snapshot_date}_mobile-boot-armv7l-tm1.ks

How to customize \*.ks file
---------------------------

-   We have to modify baseurl of \'repo\' in \*.ks file in order to use
    \*.RPMs which are built by GBS Local Full-build,\
-   Add \'\--priority=99\' to profile related repo to download
    mic-bootstrap.\
-   Add \'local\' repo in \*.ks file whose baseurl is path of GBS
    full-build results \*.RPMs\
-   Replace baseurl of \'base\' repo in \*.ks file from remote\_url to
    \$repo\_base\
-   Create repo and repodata from \$repo\_base to be used in \*.ks file\

**Example**

    $ vi ./tizen-mobile_20180105.4_mobile-wayland-armv7l-tm1.ks
       . . . Upper Omission . . . 
    #original ks file
    repo --name=mobile-wayland_armv7l --baseurl=http://download.tizen.org/snapshots/tizen/mobile/tizen-mobile_${snapshot_date}/repos/arm-wayland/packages/ --ssl_verify=no
    repo --name=base_arm --baseurl=http://download.tizen.org/snapshots/tizen/base/latest/repos/arm/packages/ --ssl_verify=no

    $ vi ./tizen-mobile_20180105.4_mobile-wayland-armv7l-tm1.ks
       . . . Upper Omission . . . 
    #modified ks file
    repo --name=mobile-wayland_armv7l --baseurl=http://download.tizen.org/snapshots/tizen/mobile/tizen-mobile_${snapshot_date}/repos/arm-wayland/packages/ --ssl_verify=no --priority=99
    repo --name=base_arm --baseurl=file:///work/infra/gbs_fullbuild_mobile/pre-built/toolchain-arm --priority=1
    repo --name=local_mobile --baseurl=file:///work/infra/gbs_fullbuild_mobile/GBS-ROOT/local/repos/tizen5.0_mobile/armv7l --priority=1

\

Generating image file using mic
-------------------------------

-   To create Tizen images, execute the following commands:\
-   Refer to the Tizen:IVI case
    (https://source.tizen.org/ko/documentation/developer-guide/all-one-instructions/creating-tizen-ivi-images-based-on-specific-snapshot-one-page?langredirect=1)\

<!-- -->

    $ mkdir $workspace
    $ sudo mic cr auto $mic_ks_files/tizen-mobile_${snapshot_date}_mobile-target-TM1-armv7l-tm1.ks --logfile=$mic_logs/_mobile-target-TM1-armv7l-tm1 -o $mic_images  
     ( $ sudo mic cr auto tizen_mobile-target-TM1-armv7l-tm1.ks  --tmpfs)

Tip & Techniques
================

Filtering Base Packages
-----------------------

To filter base packages, perform the following procedure:

1\. Move binaries to another directory by executing the following
commands:

`       mkdir -p ~/tizen_mobile_src/pre-built-set/base/`\
`       mv ~/GBS-ROOT/local/cache/*rpm ~/tizen_mobile_src/pre-built-set/base/`

2\. Filter the base binaries by using the references below:

-   For failed packages (caused by downloading or other reasons), remove
    related binaries in the cache. In this case, we need to move the
    related binaries from base to another dir because the rpm is not
    neccessary. In the end, these failed packages should be fixed by
    developers and they don\'t belong to pre-built.

`       mkdir -p ~/tizen_mobile_src/pre-built-set/extra/`\
`       mv ~/tizen_mobile_src/pre-built-set/base/xxx.rpm ~/tizen_mobile_src/pre-built-set/extra/`

-   Based on experience, exclude the following packages from cache:

`     ail, alarm, app-core, app-checker, app-svc, aul, automotive-message-*, dbus-glib,`\
`     bundle, capi-*, docbook, ecore, evas, eeze, elf-*, gst-plugins, gstreamer, pkgmgr,`\
`     privacy-manager, python-*, perl-*, sensor, vconf, xdgmime, xmlcharent etc.`

-   Packages in a circle must be kept in cache or there will be
    expansion errors.

<!-- -->

-   There is another case as follows:

`     package A run time requires B, but the build order of package B is later than A, in this case, we should remove binary of package B directly.`\
`     Check the build log under ~/GBS-ROOT/local/repos/tizen5.0_mobile/armv7l/logs/success/`\
`     grep -r downloading *`\
`     A-1-0/log.txt:[    5s] [1/1] downloading `[`http://download.tizen.org/releases/milestone/tizen/mobile/tizen_20140422.1/repos/mobile/arm/packages/i686/B-1-1.i686.rpm`](http://download.tizen.org/releases/milestone/tizen/mobile/tizen_20140422.1/repos/mobile/arm/packages/i686/B-1-1.i686.rpm)` ...`\
`     the build order:`\
`     ...`\
`     info: *** [1/897] building A-1-0 armv7l tizen5.0_mobile (worker: 0) ***`\
`     info: finished building A`\
`     ...`\
`     info: *** [10/897] building B-1-1 armv7l tizen5.0_mobile (worker: 2) ***`\
`     info: finished building B`\
`     ...`\
`     In this case, remove B-1-1.armv7l.rpm in cache`

Removing and Adding Dependency Packages
---------------------------------------

The logistics of this section is as follows:

`   check whether expansion error occurs`\
`   if yes`\
``        Add binaries to pre-built by following `Appendix_How to find dependency relationship for any package from repo` ``\
`   else`\
`       Go back to step-2 and step-3 recursively until you get a minimal pre-built`\
`       set.`

For example:

`   bluetooth-share:`\
`     nothing provides pkgconfig(aul)`

Then find the package that provides pkgconfig (aul)

`   pushd ./GBS-ROOT/local/order/`\
`   grep -e "pkgconfig(aul)" .repo.cache| grep P:`\
`   P:aul-devel.i686-1397286673/1397286678/0: aul-devel = 0.0.286-2.291 aul-devel(x86-32) = 0.0.286-2.291 pkgconfig(aul) = 0.1.0`\
`   P:aul-devel.i686-1397286694/1397286699/0: aul-devel = 0.0.286-2.10 aul-devel(x86-32) = 0.0.286-2.10 pkgconfig(aul) = 0.1.0`\
`   popd`

So put **aul-devel** binary into pre-built

Updating Pre-Built Binaries with Latest Repo
--------------------------------------------

To prepare pre-built binaries, execute the following commands:

`  $ cd ~/tizen_mobile_src/pre-built/toolchain-arm`\
`  $ ./tools/update_prebuilt.py -L . -R `[`http://download.tizen.org/snapshots/tizen/base/tizen-base_20180103.1/repos/arm/packages/`](http://download.tizen.org/snapshots/tizen/base/tizen-base_20180103.1/repos/arm/packages/)

Upon successful execution of this script, the old binaries will be
replaced by the new binaries. If there is a repodata dir, make sure to
run \`createrepo \--update\` to update this pre-built directory.

`   $createrepo --update ./repos_mobile`\
`   $ ls ./repos_mobile/repodata/`\
`   2fbd464035e46f900abeb4d84039d4afb1b3489420c9b633073faae470fa6b7d-primary.xml.gz`\
`   4931aad22ff6a92ae94024c6db65a52687a0ff20ed5560fc01558b4fe8b45f32-primary.sqlite.bz2`\
`   6bc611a44d146ae2171a53a3f2f5733e58998f4bd85b2e27a9d438fb44adf903-other.sqlite.bz2`\
`   6cc425f57f8a218ba78cbd190b1e3391068e62927876ed627f270ee60561b5f5-filelists.sqlite.bz2`\
`   713f5170c01e01b652f211baec23444e6aef7fdd699c867a32424d2f0ca962fc-filelists.xml.gz`\
`   d9224b4b38b9d6c2b18ef3dce0002ac0ff511dcc21177d9578eb83bceb423157-other.xml.gz`\
`   repomd.xml`

How to find dependency relationship for any package from repo
-------------------------------------------------------------

Run gbs build with any package, press Ctr-c at the start of build. Repo
is which you want to build with.

`   gbs build -A armv7 -R /pub/mirrors/tizen/releases/milestone/tizen/mobile/tizen_20140422.1/ --skip-conf-repos --buildroot=~/GBS-ROOT`\
`   info: generate repositories ...`\
`   info: build conf has been downloaded at:`\
`         /var/tmp/tizen.conf`\
`   info: start building packages from: /home/testspace/f81517f68c214eabbd4f1445e9b01e77 (git)`\
`   2014-05-20 13:54 +0800`\
`   info: prepare sources...`\
`   info: start export source from: /home/testspace/f81517f68c214eabbd4f1445e9b01e77/fake ...`\
`   info: Creating (native) source archive fake-1.0.tbz2 from 'HEAD'`\
`   info: package files have been exported to:`\
`   /home/GBS-ROOT/local/sources/tizen/fake-1.0-1`\
`   info: retrieving repo metadata...`\
`   info: parsing package data...`\
`   info: building repo metadata ...`\
`   info: package dependency resolving ...`\
`   info: next pass:`\
`   fake`\
`   info: *** [1/1] building fake-1.0-1 armv7l tizen (worker: 0) ***`\
`   VM_IMAGE: , VM_SWAP:`\
`   --repository /home/GBS-ROOT/local/repos/tizen/armv7l/RPMS --repository HOSTNAME/pub/mirrors/tizen/releases/milestone/tizen/mobile/tizen_20140422.1/repos/mobile/arm/packages --repository HOSTNAME/pub/mirrors/tizen/releases/milestone/tizen/mobile/tizen_20140422.1/repos/emul/arm/packages`\
`   logging output to /home/GBS-ROOT/local/BUILD-ROOTS/scratch.armv7l.0/.build.log...`\
`   [    0s] Memory limit set to 21777108KB`\
`   [    0s] Using BUILD_ROOT=/home/GBS-ROOT/local/BUILD-ROOTS/scratch.armv7l.0`\
`   [    0s] Using BUILD_ARCH=i686:armv7l:i486:i386:noarch`\
`   [    0s]`\
`   [    0s]`\
`   [    0s] started "build fake.spec" at Tue May 20 05:54:35 UTC 2014.`\
`   [    0s]`\
`   [    0s]`\
`   [    0s] processing specfile /home/GBS-ROOT/local/sources/tizen/fake-1.0-1/fake.spec ...`\
`   [    0s] init_buildsystem --configdir /usr/lib/build/configs --cachedir /home/GBS-ROOT/local/cache --repository /home/GBS-ROOT/local/repos/tizen/armv7l/RPMS --repository HOSTNAME/pub/mirrors/tizen/releases/milestone/tizen/mobile/tizen_20140422.1/repos/mobile/arm/packages --repository HOSTNAME/pub/mirrors/tizen/releases/milestone/tizen/mobile/tizen_20140422.1/repos/emul/arm/packages /home/GBS-ROOT/local/sources/tizen/fake-1.0-1/fake.spec ...`\
`   [    0s] initializing /home/GBS-ROOT/local/BUILD-ROOTS/scratch.armv7l.0/.srcfiles.cache ...`\
`   [    0s] /usr/lib/build/createrpmdeps /home/GBS-ROOT/local/repos/tizen/armv7l/RPMS`\
`   [    0s] /usr/lib/build/createrepomddeps --cachedir=/home/GBS-ROOT/local/cache HOSTNAME/pub/mirrors/tizen/releases/milestone/tizen/mobile/tizen_20140422.1/repos/mobile/arm/packages`\
`   [    1s] /usr/lib/build/createrepomddeps --cachedir=/home/GBS-ROOT/local/cache HOSTNAME/pub/mirrors/tizen/releases/milestone/tizen/mobile/tizen_20140422.1/repos/emul/arm/packages`\
`   ^C^C captured`\
`   warning: build failed, Leaving the logs in /home/GBS-ROOT/local/repos/tizen/armv7l/logs/fail/fake-1.0-1/log.txt`

Then open \~/GBS-ROOT/local/order/.repo.cache, it can provide all
information about every package from repo like:

`   P:mic-bootstrap-x86-arm.armv7l-1397164816/1397165006/0: mic-bootstrap-x86-arm = 1.0-13.20 mic-bootstrap-x86-arm(x86-32) = 1.0-13.20`\
`   R:mic-bootstrap-x86-arm.armv7l-1397164816/1397165006/0: /bin/sh`\
`   I:mic-bootstrap-x86-arm.armv7l-1397164816/1397165006/0: mic-bootstrap-x86-arm-1.0-13.20 1397164816`\
`   F:gdb-locale.noarch-1387595787/1387595811/0: HOSTNAME/pub/mirrors/tizen/releases/milestone/tizen/mobile/tizen_20140422.1/repos/mobile/arm/packages/noarch/gdb-locale-7.5.1-10.1.noarch.rpm`\
`   P:gdb-locale.noarch-1387595787/1387595811/0: gdb-lang-all = 7.5.1 gdb-locale = 7.5.1-10.1`\
`   R:gdb-locale.noarch-1387595787/1387595811/0: gdb = 7.5.1`\
`   I:gdb-locale.noarch-1387595787/1387595811/0: gdb-locale-7.5.1-10.1 1387595787`\
`   F:zypper-locale.noarch-1387597203/1387597217/0: HOSTNAME/pub/mirrors/tizen/releases/milestone/tizen/mobile/tizen_20140422.1/repos/mobile/arm/packages/noarch/zypper-locale-1.8.14-12.1.noarch.rpm`

The meaning of these prefix characters are:

-   P what this package provides
-   R what this package requires
-   F where to find this package
-   I Identifier of package

Full Build Script (FBS)
=======================

If you understand the above sections enough, you can easily repeat the
build procedure for your convenience. The Full Build Script (FBS) is a
simple script to understand how both full-build and partial-build are
executed by gbs. It helps that the developers can do both full-build and
partial-build easy-to-use without the need to read step-by-step
instruction.

Full build
----------

**Example: to build full-source locally**

1\. In case of the **repo sync \...** command, The script does not
perfectly handle the incorrect projects.xml.\
2. In case of the **gbs build \...** command, The normal operation of
the script is dependent on the correctness of the fetched snapshot
packages and that of the git repositories. 3. If you meet gbs issues,
please report your issue at Tizen mailling list.

-   Mailman - <https://lists.tizen.org/listinfo/dev>
-   Jira - <https://bugs.tizen.org/jira/projects/DEVT>

\$ vi ./fbs.sh



    #!/usr/bin/env bash
    # @Title: Full Build Script (FBS) 
    # @License: Apache
    # @Date: Jan-11-2017
    # @Contacts: leemgs@gmail.com
    # @Prequisites: cat, grep, wc, curl, time, repo, mkdir, wget, createrepo, rm, gunzip, gbs, tee, python-pip
    #    ($ sudo apt-get install coreutils gbs  createrepo python-pip wget curl  grep time gzip lynx-cur lynx )
    # @Host PC: 
    #   1. Ubuntu 16.04.5 LTS X64, Linux kernel 3.15.0-98-generic, GCC 4.8.4, Glibc 2.19
    #   2. Ubuntu 16.04.1 LTS X64, Linux kernel 4.5.0-42-generic,  GCC 5.5.0, Glibc 2.23
    # @Description: This script is to build full source with just one 'enter' key
    # It is Full Build Script (FBS) is a simple script to help personal developers that deploy Tizen platform
    # on their embedded devices as well as Tizen reference devices.
    # @Todo: a. Error handling function , b. Enabling check_manifest.py, c. Bottle-neck profiling
    #
    #-------------------------------- Configuration area: Please, modify with appropriate content --------------------
    # Define input arguments. There are five profiles currently in Tizen 5.0
    # __profie={common | mobile | ivi | tv | wearable | ...},
    # __target={arm-wayland | target-TM1 | ...},
    # __rpmrepo_date_base={20180119.1 | 20180119.2 | latest}    // We don't recommend that you use "latest" because it is not stable.
    # __rpmrepo_date_profile={20180123.1 | 20180123.1 | latest} // We don't recommend that you use "latest" because it is not stable.

    # 1) snapshot: lifespan of sanpshot is 3 months.
    function define_snapshot {
    __rpmrepo_date_base=20170210.1
    __rpmrepo_date_profile=20170210.1
    __rpmrepo_path=snapshots  
    __rpmrepo_addr=http://download.tizen.org/${__rpmrepo_path}/tizen
    __rpmrepo_base_url=${__rpmrepo_addr}/base/tizen-base_${__rpmrepo_date_base}
    __rpmrepo_profile_url=${__rpmrepo_addr}/${__profile}/tizen-${__profile}_${__rpmrepo_date_profile}
    }

    # 2) release(daily): lifespan of release(daily) is 3 months .
    function define_release_daily {
    __rpmrepo_date_base=20181016.1
    __rpmrepo_date_profile=20181020.2
    __rpmrepo_path=releases/daily
    __rpmrepo_addr=http://download.tizen.org/${__rpmrepo_path}/tizen
    __rpmrepo_base_url=${__rpmrepo_addr}/base/tizen-base_${__rpmrepo_date_base}
    __rpmrepo_profile_url=${__rpmrepo_addr}/${__profile}/tizen-${__profile}_${__rpmrepo_date_profile}
    }

    # 3) release(weekly): lifespan of release(weekly) is 2 years .
    function define_release_weekly {
    __rpmrepo_date_base=20181016.1
    __rpmrepo_date_profile=20181020.2
    __rpmrepo_path=releases/weekly  
    __rpmrepo_addr=http://download.tizen.org/${__rpmrepo_path}/tizen
    __rpmrepo_base_url=${__rpmrepo_addr}/base/tizen-base_${__rpmrepo_date_base}
    __rpmrepo_profile_url=${__rpmrepo_addr}/${__profile}/tizen-${__profile}_${__rpmrepo_date_profile}
    }

    # 4) release(official,m1/m2/m3): lifespan of release(official,m1/m2/m3) is 10 years.
    function define_release_official {
    __rpmrepo_date_base=20170104.1
    __rpmrepo_date_profile=20170111.1
    __rpmrepo_path=releases/milestone 
    __rpmrepo_addr=http://download.tizen.org/${__rpmrepo_path}/tizen
    __rpmrepo_base_url=${__rpmrepo_addr}/5.0.m2/5.0.m2-base/tizen-5.0.m2-base_${__rpmrepo_date_base}
    __rpmrepo_profile_url=${__rpmrepo_addr}/5.0.m2/5.0.m2-${__profile}/tizen-5.0.m2-${__profile}_${__rpmrepo_date_profile}
    }

    # Select one among the four RPM repositories.
    define_release_official
    __cpu_number=`cat /proc/cpuinfo  | grep "model name" | wc -l`

    #-------------------------------- Execution area: Please, don't modify the script from here ----------------------

    function error_display {
    if [ $? != 0 ]; then echo -e "$1"; exit 1 ;fi   
    }

    #### STEP 1/4: Sync the repository from https://git.tizen.org #######################################

    # TBI (To Be Implemented)
    function fix_incorrect_project_path_automatic {
    cat ./.repo/manifests/README
    ./.repo/manifests/Check_manfiest/check_manifest.py  --help
    error_display "\n\n* FBS:[1/4] Error Occurred while running check_manifest.py script"
    # How to add user id and password for https authentification of https://review.tizen.org
    # sudo apt-get install python-pip
    # sudo pip install pygerrit
    # vi  ./.repo/manifests/Check_manfiest/check_manifest.py
    #     171 gc = GerritClient('https://review.tizen.org/gerrit', '<usrname>', '<passwd>')
    ./.repo/manifests/Check_manfiest/check_manifest.py  --tizen-src .  -p ${__profile} --url ${__profile}-latest  --update
    # cat  tizen_mobile_revision_diff.csv
    }

    # Custom area: modify git repository address correctly in case of an wrong web addresses.
    function fix_incorrect_project_path_manual {
        sed -i -e 's/framework\/base\/tizen-locale/core\/base\/tizen-locale/g' ./.repo/manifests/${__profile}/projects.xml
        sed -i -e 's/core\/preloaded\/ug-wifi-direct/native\/ug-wifi-direct/g' ./.repo/manifests/${__profile}/projects.xml
        sed -i -e 's/core\/preloaded\/ug-nfc-efl/native\/ug-nfc-efl/g' ./.repo/manifests/${__profile}/projects.xml
        sed -i -e 's/core\/preloaded\/ug-wifi-efl/native\/ug-wifi-efl/g' ./.repo/manifests/${__profile}/projects.xml
        sed -i -e 's/core\/preloaded\/bluetooth-share-ui/native\/bluetooth-share-ui/g' ./.repo/manifests/${__profile}/projects.xml
        sed -i -e 's/core\/preloaded\/ug-mobile-ap/native\/ug-mobile-ap/g' ./.repo/manifests/${__profile}/projects.xml
        sed -i -e 's/core\/preloaded\/ug-bluetooth-efl/native\/ug-bluetooth-efl/g' ./.repo/manifests/${__profile}/projects.xml
    }

    function repo_init {
        cd $__workspace
        # time repo init -u ssh://${__tizen_id}@review.tizen.org:29418/scm/manifest -b tizen -m ${__profile}.xml 
        # time repo init -u https://${__tizen_id}:TylhenFPwSGpNtEg19ZA6u81ylrvqvEiAiemsF4MpQ@review.tizen.org/gerrit/p/scm/manifest -b tizen -m ${__profile}.xml 
        time repo init -u https://git.tizen.org/cgit/scm/manifest -b tizen -m ${__profile}.xml
        error_display "\n\n* FBS:[1/4] Error Occurred while running 'repo init' command"
        curl $__rpmrepo_profile_url/builddata/manifest/tizen-${__profile}_${__rpmrepo_date_profile}_arm-wayland.xml > ./.repo/manifests/${__profile}/projects.xml
        error_display "\n\n* FBS:[1/4] Error Occurred while downloading projects.xml with curl"
        # todo: fix_incorrect_project_path_automatic
        # todo: fix_incorrect_project_path_manual
    }

    function repo_sync {
        time repo sync -j${__cpu_number} 2>repo-sync-error.txt
        if [[ $? != 0 ]]; then
              echo -e "\n\n* FBS:[1/4] Error Occurred while downloading Source with repo sync"
              echo -e "     Please, modify correctly the below incorrect project paths after openning ./.repo/manifests/${__profile}/projects.xml.\n\n"
              cat repo-sync-error.txt | grep "error: Cannot fetch"
              exit 1
        fi
    }

    function download_git_repo {
        repo_init
        repo_sync
    }

    #### STEP 2/4: Download the pre-built RPM packages from http://download.tizen.org ###################
    function download_prebuilt_rpms {
        mkdir ./repos_base_packages
        mkdir ./repos_base_debug
        mkdir ./repos_${__profile}_packages
        mkdir ./repos_${__profile}_debug
        wget --directory-prefix=repos_base_packages --mirror --reject index.html* -r -nH --no-parent --cut-dirs=8  ${__rpmrepo_base_url}/repos/arm/packages/
        wget --directory-prefix=repos_base_debug --mirror --reject index.html* -r -nH --no-parent --cut-dirs=8  ${__rpmrepo_base_url}/repos/arm/debug/
        wget --directory-prefix=repos_${__profile}_packages --mirror --reject index.html* -r -nH --no-parent --cut-dirs=8 ${__rpmrepo_profile_url}/repos/${__target}/packages/
        wget --directory-prefix=repos_${__profile}_debug --mirror --reject index.html* -r -nH --no-parent --cut-dirs=8 ${__rpmrepo_profile_url}/repos/${__target}/debug/
        createrepo --update ./repos_base_packages
        createrepo --update ./repos_base_debug
        createrepo --update ./repos_${__profile}_packages
        createrepo --update ./repos_${__profile}_debug
        build_conf_file=`curl -l ${__rpmrepo_profile_url}/repos/${__target}/packages/repodata/ | grep -o "href=.*build\.conf\.gz\"" | sed -e 's/href="//g; s/"//g' `
        curl ${__rpmrepo_profile_url}/repos/${__target}/packages/repodata/${build_conf_file} | gunzip > ./scm/meta/build-config/build.conf
        error_display   "\n\n* FBS:[2/4] Error Occurred while downloading build.conf with curl"
    }

    #### STEP 3/4: Run full-build ########################################################################
    function run_full_build {
        rm -f ~/.gbs.conf
        rm -f ./.gbs.conf
        __local_repository_url="-R ./repos_base_packages/ -R ./repos_base_debug/  -R ./repos_${__profile}_packages/  -R ./repos_${__profile}_debug/"
        time gbs build --arch armv7l --threads ${__cpu_number} --clean-once --include-all  -B ./GBS-ROOT ${__local_repository_url}  -D ./scm/meta/build-config/build.conf | tee fbs-${__rpmrepo_date_profile}.txt
        error_display "\n\n* FBS:[3/4] Error Occurred while building packages with gbs build"
    }
    #### STEP 4/4: View the report #######################################################################
    function view_report {
        __report_file=${__workspace}/GBS-ROOT/local/repos/tizen/armv7l/index.html
        if [ ! -f ${__report_file} ];then
              echo -e "\n [Error] ${__report_file} is not generated."
        else
              lynx ${__report_file}
              error_display "\n\n* FBS:[4/4] Error Occurred while reading the report file"
        fi
    }

    #### Main function ###################################################################################
    # repo init -u https://git.tizen.org/cgit/scm/manifest -b tizen -m <PROFILE>.xml
    # repo sync 
    # gbs build --arch armv7l --threads <#CPU> --clean-once --include-all
    # firefox /GBS-ROOT/local/repos/tizen/<ARCH>/index.html
    #
    download_git_repo            # STEP 1/4
    download_prebuilt_rpms       # STEP 2/4
    run_full_build               # STEP 3/4
    view_report                  # STEP 4/4

**Screenshot**

The below screenshot shows the console-based report result after
completing \"Tizen5.0:Common local full-build\" with full build script
on Ubuntu 16.04.1 X64 PC. If you want to see the report with GUI
interface, you may run \"firefox
./GBS-ROOT/local/repos/tizen/armv7l/index.html\" command.

![FBS (Skeleton)
Screenshot](gbs-full-build-20181013-horizontal.png "FBS (Skeleton) Screenshot"){width="500"}

Partial build
-------------

**Example: to build one package (e.g. tizen-release package)**

-   The below example is to describe how to build a package in case that
    the developer try to enhance existing packages after doing
    full-build.

<!-- -->

    $ cd $__workspace
    $ cd ./platform/upstream/tizen-release
    $ vi ./partial-build.sh

    #!/bin/bash 
    __work_space=/work/infra/gbs_fullbuild_common_20181108.1
    __profile=common
    __cpu_number=1
    __local_repository_url="-R ${__work_space}/repos_base_packages/  -R ${__work_space}/repos_base_debug/  -R ${__work_space}/repos_${__profile}_packages/  -R ${__work_space}/repos_${__profile}_debug/"
    time gbs build --arch armv7l --threads  ${__cpu_number}  --clean-once --include-all  -B ${__work_space}/GBS-ROOT  ${__local_repository_url}  -D ${__work_space}/scm/meta/build-config/build.conf  

Contributing your experience
============================

If you find additional tips and techniques to compile Tizen 5.0 full
source locally, Please, update this wiki page as a volunteer.

[Category:Platform](Category:Platform "wikilink")
[Category:Tizen-3](Category:Tizen-3 "wikilink")
[Category:Tool](Category:Tool "wikilink")
