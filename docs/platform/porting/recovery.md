# System Recovery

Tizen 4.0 comes with 3 different root filesystems, each designed for a different purpose.

**Table: Root filesystems**

| Label | Purpose |
| ----- | ------- |
| `rootfs` | Main root filesystem |
| `ramdisk` | Regular boot ramdisk |
| `ramdisk-recovery` | System recovery ramdisk |

This topic describes operation and customization options of the system
recovery ramdisk.

The following steps describe the boot process:

1. The boot process starts with a bootloader (u-boot or s-boot) loading
appropriate kernel and ramdisk images dedicated for the system
recovery process (methods for controlling bootloader actions are beyond the
scope of this document). With both images loaded into RAM, the kernel
initialization begins. When the initialization is complete, the kernel passes
control to the init process, such as `/sbin/init` (PID#1).

2. In the case of the recovery ramdisk, `/sbin/init` is a symlink to
`/usr/libexec/initrd-recovery/init` (a shell script that comes
from the `initrd-recovery` package). The script mounts several kernel
filesystems and the inform partition (if it exists), and parses the
kernel command line options (`/proc/cmdline`) to find the `bootmode`
parameter. If the parameter is present, one of the `/sbin/*-init` scripts is
started. If the boot mode is set to `recovery`,
`/usr/libexec/system-recovery/recovery-init` is started.

3. The `recovery-init` script mounts the real root filesystem under
the `/system` directory, and other filesystems (such as `/opt` and
`/opt/usr`) below the `/system` directory. The script starts a shell on the serial console and launches the
`system-recovery` program.

4. The `system-recovery` program searches the removable storage for `tizen-recovery.img`
which has the compressed partition image and config file.
The `system-recovery` program decompress `tizen-recovery.img`,
and dumps the partition image to the appropriate block as mentioned in the config file.

## Adding New Files to the `ramdisk-recovery` Partition

The `ramdisk-recovery` partition is created along with the `rootfs`
partition (methods for creating images are beyond the scope of this
document):

- Files to be added to the `ramdisk-recovery` partition must
be available in Tizen RPM packages.
- Files are added to the partition by the `mkinitrd-recovery.sh` script, which is started
automatically as a part of the `%posttrans` RPM script of the `initrd-recovery` package.

To install a selected file in the recovery
image, its RPM needs to be installed before `initrd-recovery` is run. The
easiest way to make sure this happens is to list the package as a
dependency in the `initrd-recovery.spec` file.

The `mkinitrd-recovery.sh` script copies or moves files from the
`rootfs` partition to the `initrd-recovery` partition according to
directions provided in configuration files stored in the
`/usr/share/initrd-recovery/initrd.list.d` directory. These files
must be packaged in the RPM packages together with the
files to be put on the `initrd-recovery` partition. The configuration files are
interpreted as shell scripts and can be used to set the following
variables:

- `DIRECTORIES`: Create directories.
- `DIR_SYMLINKS`: Create symbolic links to directories.
- `LIBONLYS`: Copy **only** the libraries required by the listed executable files.
- `MVWITHLIBS`: Move the listed executable files and copy the required libraries.
- `SYMLINKS`: Create symbolic links.
- `VERBATIMS`: Copy the listed files. List non-executable files here.
- `WITHLIBS`: Copy the listed executable files and the required libraries.

The `SYMLINKS` and `DIR_SYMLINKS` variables contain pairs of filenames separated with
colons.

The following section contains examples of the above variables:

```
DIRECTORIES="
/var/tmp
/usr/lib/odbc
"

# LinkFileName:Target
DIR_SYMLINKS="
/lib:usr/lib
/opt:system/opt
"

LIBONLYS="
/bin/bash
/bin/kill
"

MVWITHLIBS="
/usr/libexec/initrd-recovery/minireboot
/usr/libexec/system-recovery/system-recovery.gui
"

WITHLIBS="
/usr/bin/sync
/usr/bin/touch
"

VERBATIMS="
/usr/share/system-recovery/res/images/font.png
/usr/share/system-recovery/res/images/menu-title.png
/usr/share/system-recovery/system-recovery.cfg
"

# LinkFileName:Target
SYMLINKS="
/sbin/recovery-init:/usr/libexec/system-recovery/recovery-init
/usr/lib/bufmgr/libtbm_default.so:libtbm_sprd.so
"
```

The following real-world example comes from the `initrd-recovery`
package. Following this configuration, `mkinitrd-recovery.sh` copies
some basic tools to the `initrd-recovery` partition, moves `init` and
`minireboot`, and creates some symlinks:

```
MVWITHLIBS="
/usr/libexec/initrd-recovery/init
/usr/libexec/initrd-recovery/minireboot
"

WITHLIBS="
/usr/bin/bash
/usr/bin/cat
/usr/bin/mkdir
/usr/bin/mount
/usr/bin/sleep
/usr/bin/sync
/usr/bin/umount
/usr/sbin/blkid
"

# LinkFileName:Target
SYMLINKS="
/bin/sh:bash
/sbin/init:/usr/libexec/initrd-recovery/init
/sbin/minireboot:/usr/libexec/initrd-recovery/minireboot
/sbin/reboot:/usr/libexec/initrd-recovery/minireboot
"
```
