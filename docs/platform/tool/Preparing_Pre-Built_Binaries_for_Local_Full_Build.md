Introduction
------------

This document describes how to prepare pre-built binaries for local full
build,including the following:

-   Create a super set of pre-built binaries
-   Filter base packages
-   Perform full build by using the filtered binaries
-   Remove and add dependency packages
-   Update pre-built binaries with latest repo

Tizen [IVI](IVI "wikilink") is taken as example in this document.

Creating a Super Set of Pre-built Binaries
------------------------------------------

To create a super set of pre-built binaries, perform the following
precedure:

1\. Modify .gbs.conf under \~/tizen\_ivi\_src as follows:

`       [general]`\
`       tmpdir=/var/tmp/`\
`       profile = profile.tizen3.0_ivi`\
`       work_dir=.`\
`       [repo.tizen3.0_ivi]`\
`       url=HOSTNAME/pub/mirrors/tizen/releases/milestone/tizen/ivi/tizen_20140422.1`\
`       [profile.tizen3.0_ivi]`\
`       repos=repo.tizen3.0_ivi`\
`       buildconf=${work_dir}/scm/meta/build-config/build.conf`

2\. Clean cache and run build by executing the following commands:

`       sudo rm -rf ~/GBS-ROOT/local/cache`\
`       cd ~/tizen_ivi_src/platform/upstream`\
`       gbs build -A i586 --threads=4 --clean-once --clean-repos --exclude=libtool,gettext`

Upon successful \*\*gbs build\*\*, the original package binaries will be
stored into \~/GBS-ROOT/local/cache/<hash_ID>, waiting for further
filter to become useful set of pre-built binaries.

Filtering Base Packages
-----------------------

To filter base packages, perform the following procedure:

1\. Move binaries to another directory by executing the following
commands:

`       mkdir -p ~/tizen_ivi_src/pre-built-set/base/`\
`       mv ~/GBS-ROOT/local/cache/*rpm ~/tizen_ivi_src/pre-built-set/base/`

2\. Filter the base binaries by using the references below:

-   For failed packages (caused by downloading or other reasons), remove
    related binaries in the cache. In this case, we need to move the
    related binaries from base to another dir because the rpm is not
    neccessary. In the end, these failed packages should be fixed by
    developers and they don\'t belong to pre-built.

`       mkdir -p ~/tizen_ivi_src/pre-built-set/extra/`\
`       mv ~/tizen_ivi_src/pre-built-set/base/xxx.rpm ~/tizen_ivi_src/pre-built-set/extra/`

-   Based on experience, exclude the following packages from cache:

`     ail, alarm, app-core, app-checker, app-svc, aul, automotive-message-*, dbus-glib,`\
`     bundle, capi-*, docbook, ecore, evas, eeze, elf-*, gst-plugins, gstreamer, pkgmgr,`\
`     privacy-manager, python-*, perl-*, sensor, vconf, xdgmime, xmlcharent etc.`

-   Packages in a circle must be kept in cache or there will be
    expansion errors.

<!-- -->

-   There is another case as follows:

`     package A run time requires B, but the build order of package B is later than A, in this case, we should remove binary of package B directly.`\
`     Check the build log under ~/GBS-ROOT/local/repos/tizen3.0_ivi/i586/logs/success/`\
`     grep -r downloading *`\
`     A-1-0/log.txt:[    5s] [1/1] downloading `[`http://download.tizen.org/releases/milestone/tizen/ivi/tizen_20140422.1/repos/ivi/ia32/packages/i686/B-1-1.i686.rpm`](http://download.tizen.org/releases/milestone/tizen/ivi/tizen_20140422.1/repos/ivi/ia32/packages/i686/B-1-1.i686.rpm)` ...`\
`     the build order:`\
`     ...`\
`     info: *** [1/897] building A-1-0 i586 tizen3.0_ivi (worker: 0) ***`\
`     info: finished building A`\
`     ...`\
`     info: *** [10/897] building B-1-1 i586 tizen3.0_ivi (worker: 2) ***`\
`     info: finished building B`\
`     ...`\
`     In this case, remove B-1-1.i586.rpm in cache`

Performing Full Build by Using the Filtered Binaries
----------------------------------------------------

To perform full build by using the filtered binaries, perform the
following procedure:

1\. Clean cache and repos by executing the following commands:

`       sudo rm -rf ~/GBS-ROOT/local/cache`\
`       rm -rf ~/GBS-ROOT/local/repos`

2\. Remove remote repositories in .gbs.conf to leave just local pre-built
local repo, an example is shown below:

`       [general]`\
`       tmpdir=/var/tmp/`\
`       profile = profile.tizen3.0_ivi`\
`       work_dir=.`\
`       [repo.tizen3.0_x86]`\
`       url=${work_dir}/pre-built-set`\
`       [profile.tizen3.0_ivi]`\
`       repos=repo.tizen3.0_x86`\
`       buildconf=${work_dir}/scm/meta/build-config/build.conf`

3\. Build all packages by executing the following commands:

`       cd ~/tizen_ivi_src`\
`       gbs build -A i586 --threads=4 --clean-once --exclude=libtool,gettext`

Removing and Adding Dependency Packages
---------------------------------------

The logistics of this section is as follows:

`   check whether expansion error occurs`\
`   if yes`\
``        Add binaries to pre-built by following `Appendix_How to find dependency ``\
``        relationship for any package from repo` ``\
`   else`\
`       Go back to step-2 and step-3 recursively until you get a minimal pre-built`\
`       set.`

For example:

`   qt5:`\
`     nothing provides pkgconfig(aul)`

Then find the package that provides pkgconfig (aul)

`   grep -e "pkgconfig(aul)" .repo.cache| grep P:`\
`   P:aul-devel.i686-1397286673/1397286678/0: aul-devel = 0.0.286-2.291 aul-devel(x86-32) = 0.0.286-2.291 pkgconfig(aul) = 0.1.0`\
`   P:aul-devel.i686-1397286694/1397286699/0: aul-devel = 0.0.286-2.10 aul-devel(x86-32) = 0.0.286-2.10 pkgconfig(aul) = 0.1.0`

So put aul-devel binary into pre-built

Updating Pre-Built Binaries with Latest Repo
--------------------------------------------

We can use a script named update\_pre-built.py
(bj/gbs-testing/update\_prebuilt.py), which can automatically upgrade
the binaries in pre-built to the higher version with a latest repo, to
maitain pre-built binaries.

`   python update_pre-built.py -R HOSTNAME/pub/mirrors/tizen/releases/milestone/tizen/ivi/tizen_20140422.1/repos/ivi/ia32/packages/`\
`   -L ~/tizen_ivi_src/pre-built/toolchain-x86`

Upon successful execution of this script, the old binaries will be
replaced by the new binaries. If there is a repodata dir, make sure to
run \`createrepo \--update\` to update this pre-built directory.

`   createrepo --update ~/tizen_ivi_src/pre-built/toolchain-x86`

Appendix
--------

### How to find dependency relationship for any package from repo

Run gbs build with any package, press Ctr-c at the start of build. Repo
is which you want to build with.

`   gbs build -A i586 -R HOSTNAME/pub/mirrors/tizen/releases/milestone/tizen/ivi/tizen_20140422.1/ --skip-conf-repos --buildroot=~/MILSTONE`\
`   info: generate repositories ...`\
`   info: build conf has been downloaded at:`\
`         /var/tmp/tizen.conf`\
`   info: start building packages from: /home/testspace/f81517f68c214eabbd4f1445e9b01e77 (git)`\
`   2014-05-20 13:54 +0800`\
`   info: prepare sources...`\
`   info: start export source from: /home/testspace/f81517f68c214eabbd4f1445e9b01e77/fake ...`\
`   info: Creating (native) source archive fake-1.0.tbz2 from 'HEAD'`\
`   info: package files have been exported to:`\
`   /home/MILSTONE/local/sources/tizen/fake-1.0-1`\
`   info: retrieving repo metadata...`\
`   info: parsing package data...`\
`   info: building repo metadata ...`\
`   info: package dependency resolving ...`\
`   info: next pass:`\
`   fake`\
`   info: *** [1/1] building fake-1.0-1 i586 tizen (worker: 0) ***`\
`   VM_IMAGE: , VM_SWAP:`\
`   --repository /home/MILSTONE/local/repos/tizen/i586/RPMS --repository HOSTNAME/pub/mirrors/tizen/releases/milestone/tizen/ivi/tizen_20140422.1/repos/ivi/ia32/packages --repository HOSTNAME/pub/mirrors/tizen/releases/milestone/tizen/ivi/tizen_20140422.1/repos/emul/ia32/packages`\
`   logging output to /home/MILSTONE/local/BUILD-ROOTS/scratch.i586.0/.build.log...`\
`   [    0s] Memory limit set to 21777108KB`\
`   [    0s] Using BUILD_ROOT=/home/MILSTONE/local/BUILD-ROOTS/scratch.i586.0`\
`   [    0s] Using BUILD_ARCH=i686:i586:i486:i386:noarch`\
`   [    0s]`\
`   [    0s]`\
`   [    0s] started "build fake.spec" at Tue May 20 05:54:35 UTC 2014.`\
`   [    0s]`\
`   [    0s]`\
`   [    0s] processing specfile /home/MILSTONE/local/sources/tizen/fake-1.0-1/fake.spec ...`\
`   [    0s] init_buildsystem --configdir /usr/lib/build/configs --cachedir /home/MILSTONE/local/cache --repository /home/MILSTONE/local/repos/tizen/i586/RPMS --repository HOSTNAME/pub/mirrors/tizen/releases/milestone/tizen/ivi/tizen_20140422.1/repos/ivi/ia32/packages --repository HOSTNAME/pub/mirrors/tizen/releases/milestone/tizen/ivi/tizen_20140422.1/repos/emul/ia32/packages /home/MILSTONE/local/sources/tizen/fake-1.0-1/fake.spec ...`\
`   [    0s] initializing /home/MILSTONE/local/BUILD-ROOTS/scratch.i586.0/.srcfiles.cache ...`\
`   [    0s] /usr/lib/build/createrpmdeps /home/MILSTONE/local/repos/tizen/i586/RPMS`\
`   [    0s] /usr/lib/build/createrepomddeps --cachedir=/home/MILSTONE/local/cache HOSTNAME/pub/mirrors/tizen/releases/milestone/tizen/ivi/tizen_20140422.1/repos/ivi/ia32/packages`\
`   [    1s] /usr/lib/build/createrepomddeps --cachedir=/home/MILSTONE/local/cache HOSTNAME/pub/mirrors/tizen/releases/milestone/tizen/ivi/tizen_20140422.1/repos/emul/ia32/packages`\
`   ^C^C captured`\
`   warning: build failed, Leaving the logs in /home/MILSTONE/local/repos/tizen/i586/logs/fail/fake-1.0-1/log.txt`

Then open \~/MILSTONE/local/order/.repo.cache, it can provide all
information about every package from repo like:

`   P:mic-bootstrap-x86-arm.i586-1397164816/1397165006/0: mic-bootstrap-x86-arm = 1.0-13.20 mic-bootstrap-x86-arm(x86-32) = 1.0-13.20`\
`   R:mic-bootstrap-x86-arm.i586-1397164816/1397165006/0: /bin/sh`\
`   I:mic-bootstrap-x86-arm.i586-1397164816/1397165006/0: mic-bootstrap-x86-arm-1.0-13.20 1397164816`\
`   F:gdb-locale.noarch-1387595787/1387595811/0: HOSTNAME/pub/mirrors/tizen/releases/milestone/tizen/ivi/tizen_20140422.1/repos/ivi/ia32/packages/noarch/gdb-locale-7.5.1-10.1.noarch.rpm`\
`   P:gdb-locale.noarch-1387595787/1387595811/0: gdb-lang-all = 7.5.1 gdb-locale = 7.5.1-10.1`\
`   R:gdb-locale.noarch-1387595787/1387595811/0: gdb = 7.5.1`\
`   I:gdb-locale.noarch-1387595787/1387595811/0: gdb-locale-7.5.1-10.1 1387595787`\
`   F:zypper-locale.noarch-1387597203/1387597217/0: HOSTNAME/pub/mirrors/tizen/releases/milestone/tizen/ivi/tizen_20140422.1/repos/ivi/ia32/packages/noarch/zypper-locale-1.8.14-12.1.noarch.rpm`

The meaning of these prefix characters are:

-   P what this package provides
-   R what this package requires
-   F where to find this package
-   I Identifier of package

[Category:Tool](Category:Tool "wikilink")
