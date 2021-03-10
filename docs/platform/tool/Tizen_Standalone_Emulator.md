This document describes how to download and use a Tizen
[Emulator](Emulator "wikilink") image without installing the full Tizen
SDK. Running the emulator without the SDK is useful in environments
where web application development is not the primary focus such as
platform development and QA.

These steps have been tested on Ubuntu 12.04 (32/64-bit), Ubuntu 14.04
64-bit, Mac OS X 10.7 and Mac OS X 10.9. And these steps are also
described in the **README** file of the standalone emulator package.

Install the prerequisites for Tizen Emulator
============================================

1\. Oracle Java\* v6 or later needs to be installed (Do not use OpenJDK).

2\. For Ubuntu, the pre-requisite packages for Tizen Emulator are listed
as below.

`$ sudo apt-get install libdbus-1-3 libpng12-0 libpixman-1-0 libsdl1.2debian`

3\. For Mac OS X, the package e2fsprogs needs to be installed which
provides the tool e2fsck and resize2fs described in the following part
\"Modify Emulator image\".

`$ brew install e2fsprogs`

Download Tizen Emulator image
=============================

The compressed emulator files are about 300MB to 400M.

Tizen IVI Emulator snapshot image:

<http://download.tizen.org/snapshots/tizen/ivi/latest/images/emulator/ivi-mbr-i586-emul/><snapshot ID>\_ivi-mbr-i586-emul.tar.gz

Tizen Common Emulator snapshot image:

<http://download.tizen.org/snapshots/tizen/common/latest/images/emulator32-wayland/common-emulator-wayland-mbr-i586/><snapshot ID>\_common-emulator-wayland-mbr-i586.tar.gz

Download Tizen Standalone Emulator package
==========================================

The latest version is always updated on Intel internal wiki page [Tizen
Standalone
Emulator](http://otc-sdk.bj.intel.com/wiki/Tizen_Standalone_Emulator) in
advance. It will be updated to this public wiki page for each milestone.

Note that please keep using the latest version, since the old version
may not be able to boot up the latest emulator image.

  PLATFORM          STANDALONE EMULATOR                                                                                                                                      FILE SIZE   MD5 Checksum
  ----------------- -------------------------------------------------------------------------------------------------------------------------------------------------------- ----------- ----------------------------------
  Ubuntu® 32-bit    [standalone-emulator\_20141031\_ubuntu-32.zip](http://download.tizen.org/sdk/IVI/m14.4/standalone-emulator/standalone-emulator_20150129_ubuntu-32.zip)   24M         6af403be23388e619c625725be9c3541
  Ubuntu® 64-bit    [standalone-emulator\_20141031\_ubuntu-64.zip](http://download.tizen.org/sdk/IVI/m14.4/standalone-emulator/standalone-emulator_20150129_ubuntu-64.zip)   25M         2655734433113a07bdfe10a09b3c9ecd
  Mac OS X 64-bit   [standalone-emulator\_20141031\_macos-64.zip](http://download.tizen.org/sdk/IVI/m14.4/standalone-emulator/standalone-emulator_20150129_macos-64.zip)     15M         5f4bcd98410a156065e5aa2cfbf2a7fe

Modify Emulator image
=====================

1\. Move image \*.tar.gz to ./data/emulator-images/

`$ mv `<image>` ./data/emulator-images/`

2\. Run the script convert.sh.

`$ ./convert.sh`

The script convert.sh will do the following things.

1\) Unpack the image.

`$ tar xvzf `<image>

2\) Enlarge the image root partition size.

The resulting platform.img image file is about 1GB to 1.5GB. It is a
loop format image. The root partition is compressed by MIC tool when
creating the image. It was used by Samsung Mobile at the beginning.
However, qemu doesn\'t support loop format. To make it be used for
Emulator, we have to convert the format. Before image conversion, it
needs to enlarge root partition size by the following commands. This
will increase the image size to about 3.9G.

`$ e2fsck -f platform.img`\
`$ resize2fs platform.img 3900M`

3\) Change the image format to qcow2 format.

Qcow2 format is supported by qemu and meanwhile it is a growable format
which supports compression. The empty sectors are detected and
suppressed from the destination image in the process of converting the
format to qcow2. The conversion command is as below.

`$ ./bin/qemu-img convert -O qcow2 platform.img emulimg-3.0.x86`

The resulting emulimg-3.0.x86 is about 900MB.

[TC-1342](https://bugs.tizen.org/jira/browse/TC-1342) that is the
sub-task of [TC-199](https://bugs.tizen.org/jira/browse/TC-199) is being
tracked to solve the manual step 2 and step 3.

Use hardware virtualization
===========================

-   For Ubuntu, enable KVM module to use hardware virtualization.

`$ sudo modprobe -b kvm_intel`\
`or`\
`$ sudo modprobe -b kvm_amd`

You can use this command to confirm KVM has been loaded by kernel.

`$ lsmod | grep kvm`

-   For Mac OS X, install Intel HAXM to use hardware virtualization.

Open the DMG file ./intelhaxm/IntelHaxmTizen.dmg and run the installer
contained inside.

You can use this command to confirm HAXM has been loaded by kernel.

`$ kextstat | grep haxm`

Run
===

`$ ./run.sh`

This is the content of run.sh for Ubuntu. For Mac OS X, \'-enable-kvm\'
needs to be replaced by \'-enable-hax\'.

    LD_LIBRARY_PATH=./bin ./bin/emulator-x86 \
    --skin-args width=1080 height=1920 \
    skin.path=./skins/ivi \
    --qemu-args \
    -drive file=./data/emulator-images/emulimg-3.0.x86,if=virtio,index=1 \
    -boot c \
    -append "root=/dev/vda rw drm.debug=0 loglevel=255 console=ttyS0 video=LVDS-1:1080x1920-32@30 dpi=3140 ip=10.0.2.16::10.0.2.2:255.255.255.0::eth0:none vm_name=ivi" \
    -serial file:./logs/emulator.klog \
    -m 512 \
    -M maru-x86-machine \
    -net nic,model=virtio,macaddr=74:D0:2B:93:0E:12 \
    -soundhw all \
    -usb \
    -vga none \
    -L ./data/bios \
    -kernel ./data/kernel/bzImage.x86 \
    -net user,dhcpstart=10.0.2.16 \
    -rtc base=utc \
    -drive file=./data/swap/swap.img,if=virtio,index=2 \
    -enable-kvm \
    -enable-yagl \
    -enable-vigs \
    -yagl-backend vigs \
    -vigs-backend gl \
    -device virtio-esm-pci \
    -device virtio-hwkey-pci \
    -device codec-pci \
    -device maru-brightness \
    -device maru-camera \
    -device virtio-touchscreen-pci,max_point=10

Logs
====

You can find Emulator logs in ./logs directory.

Tools
=====

You can find sdb and qemu-img in ./bin directory. For Mac OS X, running
qemu-img depends on the libraries which are in the directory ./bin. So
qemu-img is put in the same directory ./bin with them.

Usefull tips
============

1\. Enable host keyboard.

Right click the Emulator skin -\> Advanced -\> Host Keyboard -\> On

2\. Custom Emulator scale.

Right click the Emulator skin -\> Scale -\> 1/4x or others. The
configuration will be saved in the file ./.skin.properties.

3\. Enable Emulator shell.

Right click the Emulator skin -\> Shell

It may pop an error dialog which says \"SDB file does not exist in the
following path\". The cause is that Tizen Emulator gets the sdb tool
from the \"../../\" directory which is relative to ./bin/emulator-x86.
If the SDK is installed, sdb is actually in that path.

Now you can copy the sdb tool to the parent directory of this package
\"standalone-emulator\" like this to work around this issue.

`$ cp ./bin/sdb ../`

4\. SDB online documentation.

You can also enter to the image by running sdb command \"./sdb shell\".
For more sdb commands, you can refer to [SDB online
documentation.](https://developer.tizen.org/dev-guide/2.2.0/org.tizen.gettingstarted/html/dev_env/smart_development_bridge.htm)

5\. Power key is used for turning on the screen.

Power key is used for turning on the screen when the screen is black.
But it cannot be used for power off.

FAQ
===

If you have any questions about Tizen standalone emulator, please
contact with [Liu, Alice](mailto:alice.liu@intel.com).

[Category:Tool](Category:Tool "wikilink")
[Category:Development](Category:Development "wikilink")
[Category:Common](Category:Common "wikilink")
