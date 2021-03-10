Guide of MIC
------------

Overview
--------

The documentation is an essential guide of [MIC](MIC "wikilink"), which
is the image creation tool of Tizen OS, and it\'s supposed for people
that would like to study MIC more in principle and technical, if you
want to know the usage of MIC, you can learn it from manual pages and
help messages.

Description
-----------

MIC is supposed to create images for Linux distributions, currently
it\'s used for Tizen. The tool offers three major functions:

\- image creation

\- image conversion between two different formats

\- chrooting into an image

With the MIC tool, users can create different types of images for
different verticals, including live CD images, live USB images, raw
images, loop images, and fs images for chrooting. Also, if users would
like to modify the image directly, they can work in a chroot
environment, based on an existing live image using MIC\'s enhanced
chrooting. Besides, MIC enables transforming an image to another image
format, a very useful function for those sensitive to image format.

It can also provide plugin mechanism for developers to expand image type
or image options, and even to hook.

Background
----------

MIC is inherited from Meego mic, in Meego Times, they use OpenSUSE Build
System (now named as Open Build System) as infrastructure, the original
OBS integrated with kiwi as image creator, but kiwi is not good for
Meego customers. They borrowed Livecd from Fedora, turned out \'mic\',
say \'Meego Image Creator\'. The original Livecd is only focus on
creating Livecd format image, but \'mic\' extended more image formats,
like loop, raw, etc. Moreover this \'mic\' introduced \'chroot\' for
chrooting images directly, \'convert\' for converting between livecd and
liveusb, between raw and qcow2.

Coming to Tizen Times, people asked for a better user interface, and a
new designed \'mic\' was turned out with subcommands, plugin system and
improved messages, cleaning up most messes in original \'mic\'. In
Meego/Tizen infrastructure, image creator is integrated in BOSS, which
mainly dispatchs requests to generate repositories and create images.
This BOSS system has been replaced with Jenkins in current Tizen
infrastructure.

Image Formats
-------------

As \'mic\' has a long history, so it inherited many image format
support, and they are changing and updating in period. But the basic
usage should be in consistency.

\- fs: actually it\'s just a chroot directory, most of the time, it\'s
used for chroot

` and debugging, but it can be also used for 'nfs' booting`

\- loop: it targets to create an image being able to loop mount, and now
it can

` create one loop-mountable image for each partition, in Sumsung mobile development,`\
` these loop-mountable images are usually flashed by 'lthor'`

\- livecd: it\'s used to create iso format image, it supports hybrid iso
creation and

` squashfs compression, this format can be used in live booting`

\- liveusb: it\'s based on livecd format, adapts some specifics for usb
devices, so it

` targets to live booting by usb devices`

\- raw: actually it\'s a partitioned image, supports syslinux
bootloader, the original

` target is booted in a virtual machine, now it's used in Tizen IVI platform`

\- qcow2: it\'s introduced by QEMU team, and has the largest overhead
when growing the

` image, now it's used by Tizen Emulator image maintained by Tizen SDK team`

\- vmdk & vdi: deprecated

Workflow
--------

In simple, mic will require some loop devices for image files, and mount
them to mount point as kickstart file described, they are partitioned
and often with partition table, and each partition is formatted by
\'mkfs\' utilities. Then package manager (current is zypp) installs
packages described in kickstart file to build rootfs, the package
manager zypp is supposed to handle rpm files, retrieving rpm packages
from repositories described in kickstart file.

When rootfs finished, some configurations will be performed to set up
locale, language, timezone, etc. After that, mic will prepare the final
image, and release the compressed image file to output directory.
Finally, mic will unmount and clean up.

Say that there are two partitions present at kickstart file, which means
\'boot\' partition is 500MB, and root partition is 3500MB::

` lang en_US.UTF-8`\
` part /boot --size 500 --ondisk sda --fstype=ext2 --active`\
` part / --size 3500 --ondisk sda --fstype=ext4`

` %packages`\
` bash`\
` gcc`\
` %end`

` %post`\
` rpmdb --initdb`\
` %end`

So mic will possibly perform the following steps:

\- find one loopback device to setup image file of 4000MB::

` $ truncate --size=4000M mic.img`\
` $ losetup /dev/loop0 mic.img`

\- create two partitions and format the filesystems::

` $ parted -s /dev/loop0 unit s mkpart primary ext2 1 1023999  # first partition`\
` $ parted -s /dev/loop0 unit s mkpart primary ext4 1024000 7167999 # second partition`\
` $ parted -s /dev/loop0 set 1 boot on # active first partition`\
` $ kpartx -sa /dev/loop0`\
` $ mkfs.ext2 -F /dev/mapper/loop0p1 # format first partition`\
` $ mkfs.ext4 -F /dev/mapper/loop0p1 # format second partition`

\- mount two partitions to corresponding mountpoints::

` $ mount -t ext4 /dev/mapper/loop0p2 /var/tmp/mic/install_root`\
` $ mount -t ext2 /dev/mapper/loop0p1 /var/tmp/mic/install_root/boot`

\- install all needed packages to install\_root via backend package
manager::

` $ rpm --root=/var/tmp/mic/install_root -p -i bash.rpm gcc.rpm ...`

\- configure the image like \'lang en\_US.UTF-8\'::

` $ chroot /var/tmp/mic/install_root sed -i 's/^LANG=.*$/LANG=en_US.UTF-8/' /etc/sysconfig/i18n`

\- run post script in \'%post\' section::

` $ chroot /var/tmp/mic/install_root rpmdb --initdb`

\- unmount all mountpoints in reverse::

` $ umount -l /var/tmp/mic/install_root/boot`\
` $ umount -l /var/tmp/mic/install_root`

\- release up all devices in use::

` $ kpartx -d /dev/loop0`\
` $ losetup -d /dev/loop0`

\- package the image file and publish it to outdir::

` $ tar -czvf mic.tar.gz mic.img`\
` $ mv mic.img /var/tmp/mic/outdir`\
` $ mv /var/tmp/mic/outdir /home/who/mic-output/image`

Components & Modules
--------------------

The MIC tool is implemented by Python module, and it is designed to be
formed of the following components, like main program, config manager,
plugin manager, etc.

Main Program
------------

Source: tools/mic

The main program for mic is formed by three subcommands: create,
convert, chroot, they are supposed to be user interfaces. The three
subcommands are using \'cmdln\' module as command line parser.

Config Manager
--------------

Source: mic/conf.py

It is designed as singleton, the initial configures will be load from
mic config file, which is parsed by \'ConfigParser\' module. If config
file were not found, it will support default values. All values loaded
form config file could be overloaded by the value of the same option
from command line. It is designed to do:

\- fetch configure information from mic config file

\- get the value of the options from mic command line

\- keep the configuration information for other components to query

Plugin Manager
--------------

Source: mic/plugin.py

It is also designed as singleton, it will load all found plugins, which
will be running according to the value of specified options from config
manager. The default directory of plugins is \'/usr/lib/mic/plugins\'.

\- find all types of plugins from the plugin directory

\- store all found plugins in categories

\- provide interface to create, convert, and chroot

Kickstart Adapter
-----------------

Source: mic/kickstart/\*

As the whole image creation is driven by kickstart file, the kickstart
adapter provides \'read\_kickstart\' to parse kickstart syntax, and it
also allows some particular syntax by introducing custom commands and
sections, moreover it implements many KickstartConfigs according to
specified commands.

Custom sections in MIC:

\- \'%prepackages\': directive for packages needed to be pre-installed
under rootfs

\- \'%attachment\': directive for packages or files needed to be
attached as outputs

Custom commands in MIC:

\- \'repo\': based on \'repo\' of F14, introduced options: \'\--save\',
\'\--debuginfo\', \'\--source\', \'\--disable\', \'\--nocache\',
\'\--gpgkey\', \'\--priority\', \'\--ssl\_verify\'

\- \'part\': based on \'part\' of FC6, introduced options: \'\--align\',
\'\--extoptions\', \'\--uuid\', \'\--part-type\'

\- \'bootloader\': based on \'bootloader\' of F8, introduced options:
\'\--menus\', \'\--ptables\'

\- \'installerfw\_plugins\': new introduced command in MIC, see details
at following section

Partition & Filesystem
----------------------

Source: mic/utils/fs\_related.py, mic/utils/partitionedfs.py

The filesystem related module in MIC is used to provide functions like:
make filesystem, resize filesystem, mount filesystem, unmount
filesystem, loop setup, etc.

The partition module in MIC is used to provide functions like: create
partitions, format partition filesystem, mount partition image, unmount
partition image, etc. Supported features:

\- supported filesystems: vfat, ext2/3/4, btfs, squashfs

\- sparse loopback image

\- device mapper snapshot

Miscellaneous
-------------

Many utilities are introduced in MIC:

\- mic/msger.py: support formatted logging and colored messages

\- mic/utils/runner.py: support running external programs and pipeline

\- mic/archive.py: support archiving and compression

\- mic/utils/proxy.py: handle proxies including http\_proxy,
https\_proxy, no\_proxy

\- mic/utils/gpt\_parser.py: parse GPT partitions including GPT header
and GPT partition table

\- mic/utils/grabber.py: retrieve files and show text process of
retrieving

\- mic/utils/rpmmisc.py: provide rpm related functions

\- mic/utils/safeurl.py: handle url in safety way

Plugin Framework
----------------

The plugin framework is designed to make mic flexible to enhance,
developers can benefit it to implement their own image formats easily.

Plugin Class
------------

It consists of three types: imager, backend, hook. They are all
inherited from \_Plugin class, the \_Plugin class is designed as
metaclass and makes plugins easy to category.

\- imager: implement the special interface for create, convert, and
chroot

\- backend: provide interface to use package manager

\- hook: deal the hook function (Not Implemented)

\- considered as mid-ware between main program and imager class

Imager Plugins
--------------

It implements the necessary interfaces for create/chroot/convert the
image file with specified image format, basically each image format
supported in MIC will own one Imager plugin class separately, and will
utilize the related ImageCreator class.

\- fs\_plugin: implement fs image creation

\- loop\_plugin: implement loop image creation

\- raw\_plugin: implement raw image creation

\- livecd\_plugin: implement livecd image creation

\- liveusb\_plugin: implement liveusb image creation

\- qcow\_plugin: implement qcow2 image creation

Backend Plugins
---------------

It implements the necessary interfaces for installing packages, and it
will depend on some external package management tools, like libzypp and
yum. The interfaces is supposed to add repositories, select/deselect
packages, install/remove packages/groups, etc.

\- zypppkgmgr: depend on python binding of libzypp (python-zypp), and
used as default

\- yumpkgmgr: depend on pure yum module, and only available in native
mode

Installer Framework
-------------------

As raw image format is used in Tizen IVI, this format is changing over
time, like adding EFI support, record sparse info to bmap file, etc; and
mic has applied changes to support the features. Among them, A
remarkable feature is installer framework, original proposal from Sasha,
which can offload some work like \"set up bootloader\", \"configure
rootfs\" to product RPM package in Tizen IVI project.

In this framework, mic can drop several stages during image creation,
like set up bootloader, configure root filesystem. And they will be
migrated to rpm packages, for example, when rootfs is mounting in
/dev/loop0, and inside rootfs there is /tmp/dev/loop0 deep copied from
it. Originally bootloader should be set up in /dev/loop0 owned by host
OS, now it will be set up inside rootfs chroot in /tmp/dev/loop0 owned
by Tizen OS.

In technique, this deep copying is handled in mic, also mic will provide
some environment variables for the information, those setting up stuff
will be stored in setup-ivi-mbr or setup-ivi-efi, this package will be
installed into rootfs during installing stage, and its script will be
called during running post script from kickstart file to set up
bootloader.

References
----------

`*  MIC Reference: `[`https://source.tizen.org/documentation/reference/mic-image-creator`](https://source.tizen.org/documentation/reference/mic-image-creator)\
`*  Kickstart Reference: `[`http://fedoraproject.org/wiki/Anaconda/Kickstart`](http://fedoraproject.org/wiki/Anaconda/Kickstart)\
`*  Man page of losetup: `[`http://linux.die.net/man/8/losetup`](http://linux.die.net/man/8/losetup)\
`*  Man page of kpartx: `[`http://linux.die.net/man/8/kpartx`](http://linux.die.net/man/8/kpartx)\
`*  Man page of parted: `[`http://linux.die.net/man/8/parted`](http://linux.die.net/man/8/parted)\
`*  Man page of dmsetup: `[`http://linux.die.net/man/8/dmsetup`](http://linux.die.net/man/8/dmsetup)\
`*  RPM Documentation: `[`http://www.rpm.org/wiki/Docs#UserDocumentation`](http://www.rpm.org/wiki/Docs#UserDocumentation)\
`*  Sparse file: `[`http://en.wikipedia.org/wiki/Sparse_file`](http://en.wikipedia.org/wiki/Sparse_file)\
`*  Device mapper: `[`http://en.wikipedia.org/wiki/Device_mapper`](http://en.wikipedia.org/wiki/Device_mapper)\
`*  Libzypp Documentation: `[`http://doc.opensuse.org/projects/libzypp/HEAD/`](http://doc.opensuse.org/projects/libzypp/HEAD/)\
`*  Yum Wiki: `[`https://fedoraproject.org/wiki/Yum`](https://fedoraproject.org/wiki/Yum)

[Category:Tool](Category:Tool "wikilink")
