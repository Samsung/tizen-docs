mic-create Manual Page
----------------------

Author: Tizen.org

Name
----

mic create (cr) - Creates and manipulates images for Linux
distributions.

Synopsis
--------

### Subcommmand

` ::`

`     mic create(cr) `<Second_Level_Subcommand>` `<ksfile>\
`                                           [-h, --help] [--logfile=LOGFILE]`\
`                                           [-c CONFIG, --config=CONFIG]`\
`                                           [-k CACHEDIR, --cachedir=CACHEDIR]`\
`                                           [-o OUTDIR, --outdir=OUTDIR]`\
`                                           [-A ARCH, --arch=ARCH]`\
`                                           [--release=RID]`\
`                                           [--record-pkgs=RECORD_PKGS]`\
`                                           [--pkgmgr=PKGMGR]`\
`                                           [--local-pkgs-path=LOCAL_PKGS_PATH]`\
`                                           [--runtime=RUNTIME]`\
`                                           [--pack-to=PACK_TO] [--copy-kernel]`\
`                                           [--install-pkgs=INSTALL_PKGS]`\
`                                           [--check-pkgs=CHECK_PKGS] [--tmpfs]`

### Second Level Subcommands

` ::`

`     mic create(cr) help `<Second_Level_Subcommand>\
`     mic create(cr) auto `<ksfile>` [-h, --help]`\
`     mic create(cr) fs `<ksfile>` [-h, --help] [--include-src]`\
`     mic create(cr) livecd `<ksfile>` [-h, --help]`\
`     mic create(cr) liveusb `<ksfile>` [-h, --help]`\
`     mic create(cr) loop `<ksfile>` [-h, --help][--shrink]`\
`                                  [--compress-image=COMPRESS_IMAGE]`\
`                                  [--compress-disk-image=COMPRESS_IMAGE]`\
`     mic create(cr) raw  `<ksfile>` [-h, --help]`\
`                                  [--fstab-entry=FSTAB_ENTRY]`\
`                                  [--generate-bmap]`\
`                                  [--compress-image=COMPRESS_IMAGE]`\
`                                  [--compress-disk-image=COMPRESS_IMAGE]`

Description
-----------

This command creates and manipulates images for Linux distributions.
With a variety of second level subcommands, \*\*mic-create\*\* enables
users to do the following:

### mic create auto

` Create an image with the format automatically detected from the magic line`\
``  which is wrapped by "`-*-mic2-options-*-`" in ksfile. ``

` Assuming the magic line in the ksfile is as follows:`

` ::`

`     # -*-mic2-options-*- -f loop --pack-to=@NAME@-rs.zip -*-mic2-options-*-`

` Then the result of running **mic cr auto *.ks** is equivalent to`\
` **mic cr loop *.ks --pack-to=@NAME@-rs.zip**.`

### mic create fs

` Create a file system image.`

` In this scenario, MIC installs all the Tizen files to the specified directory,`\
` which can be used directly as chroot environment.`

### mic create help <Second_Level_Subcommand>

` Show detailed help message of specific second level subcommand.`

### mic create livecd

` Create an image that can be burnt to CD, based on which a live system or`\
` installation UI can be booted up.`

### mic create liveusb

` Create an image that can be burnt to usbdisk, based on which a live system or`\
` installation UI can be booted up.`

### mic create loop

` Create a loop image for mobile devices.`

`   **Note:** Each loop corresponds to specific partition, multiple loop images`\
`   can be packed into a single archive file.`

` In this scenario, MIC generates multiple loop images for a configuration with`\
` multiple partitions specified in the ksfile.`

### mic create raw

` Create a raw image for IVI devices.`

` In this scenario, MIC creates a bootable image in raw format similar to`\
` disk dumping.`

Parameters
----------

### Mandatory Parameter

:   

    :   

`   `<ksfile>`            Specifies the ksfile that describes how to create`\
`                       an image.`

For more information, refer to \`Fedora ksfile\`\_.

### Optional Parameters for Subcommands

:   

    :   

`   -h, --help          Shows this help message and exit.`\
`   --logfile=LOGFILE   Specifies the path of logfile.`\
`   -c CONFIG, --config=CONFIG`\
`                       Specifies config file for MIC.`\
`   -k CACHEDIR, --cachedir=CACHEDIR`\
`                       Specifies cache directory to store downloaded files.`\
`   -o OUTDIR, --outdir=OUTDIR`\
`                       Specifies the output directory.`\
`   -A ARCH, --arch=ARCH`\
`                       Specifies repo architecture.`\
`   --release=RID       Specifies the repo with specific Release ID (RID) and`\
`                       adds the RID to the name of generated files.`\
`                       When @BUILD_ID@ is contained in kickstart file, it`\
`                       will be replaced by RID.`\
`   --record-pkgs=RECORD_PKGS`\
`                       Records the info of installed packages. Multiple values`\
`                       must be separated by comma. Valid values: name,`\
`                       content, license, vcs.`\
`   --pkgmgr=PKGMGR     Specifies backend package manager. Valid values:`\
`                       yum, zypp.`\
`   --local-pkgs-path=LOCAL_PKGS_PATH`\
`                       Specifies the installation path of local RPM packages.`\
`   --runtime=RUNTIME_MODE`\
`                       Sets runtime mode, the default value is bootstrap mode.`\
`                       Valid values: native, bootstrap. "native" indicates`\
`                       MIC uses localhost environment to create image, whereas`\
`                       "bootstrap" indicates MIC uses one tizen chroot`\
`                       environment to create image.`\
`   --pack-to=PACK_TO   Packs the images together into the specified achive,`\
`                       extension supported: .zip, .tar, .tar.gz, .tar.bz2,`\
`                       etc. The default value is .tar.`\
`   --copy-kernel       Copies kernel files from image /boot directory to the`\
`                       image output directory.`\
`   --install-pkgs=INSTALL_PKGS`\
`                       Specifies the type of packages to be installed. Valid`\
`                       values: source, debuginfo, debugsource.`\
`   --check-pkgs=CHECK_PKGS`\
`                       Checks whether the given packages will be installed,`\
`                       packages must be separated by comma.`\
`   --tmpfs             Sets up tmpdir as tmpfs to accelerate. This is`\
`                       experimental feature recommended to use when the memory`\
`                       of the host machine is more than 4G.`

### Optional Parameters for Second Level Subcommands

-   Parameters for \*\*mic create fs\*\*

` ::`

`   --include-src       Generates an image with source RPMs included.`

-   Parameters for \*\*mic create loop\*\*

` ::`

`   --shrink`\
`                       Specifies whether to shrink loop images to minimal size.`\
`   --compress-image=COMPRESS_IMAGE`\
`                       Sets the disk image compression. Note: The available`\
`                       values may depend on the file system type.`\
`   --compress-disk-image=COMPRESS_IMAGE`\
`                       Same with --compress-image.`

-   Parameters for \*\*mic create raw\*\*

` ::`

`   --fstab-entry=FSTAB_ENTRY`\
`                       Sets fstab entry. Valid values: name, uuid. "name"`\
`                       indicates MIC uses device names, "uuid" indicates MIC`\
`                       uses file system uuid.`\
`   --generate-bmap`\
`                       Generates the block map file.`\
`   --compress-image=COMPRESS_IMAGE`\
`                       Sets the disk image compression. Note: The available`\
`                       values may depend on the filesystem type.`\
`   --compress-disk-image=COMPRESS_IMAGE`\
`                       Same with --compress-image.`

Fedora ksfile: <http://fedoraproject.org/wiki/Anaconda/Kickstart>

[Category:Tool](Category:Tool "wikilink")
