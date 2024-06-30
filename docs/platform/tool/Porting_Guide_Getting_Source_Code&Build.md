Follow this guide to download the full source code for your Tizen
platform and kernel.

-   **git clone**

1.  Download the `xml` file and extract each <git_path>.
2.  Clone each git project using the
    `git clone `[`ssh://`](ssh://)<Username>`@review.tizen.org:29418/`<git_path>
    command.

:   **Example**

<!-- -->

    $ wget https://download.tizen.org/releases/weekly/tizen/mobile/tizen-mobile_20160727.5/builddata/manifest/tizen-mobile_20160727.5_arm-wayland.xml
    $ for i in `cat tizen-mobile_20160727.5_arm-wayland.xml | grep "path" |  awk -F "\"" '{print $4}'`; do mkdir -p $i; cd $i/..; git clone ssh://<Username>@review.tizen.org:29418/$i; cd -; done

-   **repo init\' and \'repo sync**

1.  Initialize the repository using the
    `repo init -u `[`ssh://`](ssh://)<Username>`@review.tizen.org:29418/scm/manifest -b `<branch_name>` -m `<profile>`.xml`
    command.
2.  Replace the project\'s `.xml` file inside the `$workspace/.repo/`
    directory with the manifest file in the `$srcrpm_snapshot`.
3.  Use the `repo sync` to sync the repository.

:   **Example**

<!-- -->

    $ repo init -u ssh://<Username>@review.tizen.org:29418/scm/manifest -b tizen -m mobile.xml 
    $ wget --directory-prefix=$workspace/.repo/manifests/mobile/ https://download.tizen.org/releases/weekly/tizen/mobile/tizen-mobile_20160727.5/builddata/manifest/tizen-mobile_20160727.5_arm-wayland.xml
    $ mv $workspace/.repo/manifests/mobile/tizen-mobile_20160727.5_arm-wayland.xml projects.xml
    $ repo sync

When there is en error in the `repo sync` command, first of all check
whether the git project name inside the `projects.xml` file exists in
`review.tizen.org`.\
For more information, see [Cloning the Tizen
source](https://source.tizen.org/documentation/developer-guide/getting-started-guide/cloning-tizen-source).\
\
See the following links for more information:

-   Source code Management on Tizen releases:

:   GIT/Gerrit: <https://review.tizen.org/gerrit>

-   Tizen Build setup

:   [OBS](OBS "wikilink"): <https://build.tizen.org/>

-   Tizen Bug Tracking system

:   Jira: <https://bugs.tizen.org/jira>

-   Download URL: <http://download.tizen.org/>

Platform Build
--------------

-   To learn how to add something to Tizen, see [Developer
    Guide](https://source.tizen.org/documentation/developer-guide).

<!-- -->

-   To build the source code by using git build system, see [Git Build
    System](https://source.tizen.org/documentation/reference/git-build-system).

Kernel Build
------------

To build the Tizen kernel for the TM1 board:

1.  Install and setup cross compile tools on your system if the target
    and host are different (such as x86).\
    : You can use the Linaro toolchain binaries or the Ubuntu package of
    them and have your environment setup for the cross tools (such as
    export `CROSS_COMPILE=....`).
2.  Prepare the kernel source code for TM1 from
    `profile/mobile/platform/kernel/linux-3.10-sc7730`.

    :   `git: `[`https://review.tizen.org/git/?p=profile/mobile/platform/kernel/linux-3.10-sc7730.git`](https://review.tizen.org/git/?p=profile/mobile/platform/kernel/linux-3.10-sc7730.git)
    :   `branch: accepted/tizen_mobile`

3.  If your kernel source has been used to create binaries for other
    architecture, start by cleaning them up.

    :   `$ make distclean`

4.  Setup the `.config` file for TM1.

    :   `$ make ARCH=arm tizen_tm1_defconfig`

5.  After reconfiguring your needs (such as `make ARCH=arm menuconfig`)
    or using the stock configuration (no modifications), build it.

    :   `$ make ARCH=arm zImage`
    :   `$ make ARCH=arm dtbs`

6.  Create `devicetree` and `zImage` merged image with image tools.

    :   `$ scripts/sprd_dtbtool.sh -o arch/arm/boot/merged-dtb -p scripts/dtc/ -v arch/arm/boot/dts/`
    :   `$ scripts/sprd_mkdzimage.sh -o arch/arm/boot/dzImage -k arch/arm/boot/zImage -d arch/arm/boot/merged-dtb`

7.  Build and make kernel module image as well. Note that you may need
    to do sudo first to let `sudo -n` work in the script.

    :   `$ sudo ls`
    :   `$ scripts/mkmodimg.sh`

8.  Make a `.tar` archive from `dzImage` and `modules.img`.

    :   You can make your own `.tar` file from the 2 files.
    :   `$ tar cf FILENAME_YOU_WANT.tar -C arch/arm/boot dzImage -C ../../../usr/tmp-mod modules.img`

9.  Send the `.tar` image to the target using `lthor`.

    :   `$ lthor FILENAME_YOU_WANT.tar`

Image Build
-----------

-   To create the image by using MIC, see [MIC Image
    Creator](https://source.tizen.org/documentation/reference/mic-image-creator).

[Category:Tool](Category:Tool "wikilink")
