# Kernel

For information on how to set up the Tizen OS development environment, see [Setting up the Development Environment](../developing/setting-up.md).


## Kernel Build

To build the Tizen kernel for the TM1 board:

1. Install and set up cross-compile tools on your system if the host has a different architecture than the target (such as x86).
1. Prepare the kernel source code for TM1 from `profile/mobile/platform/kernel/linux-3.10-sc7730`:  
   ```
   git: https://review.tizen.org/git/?p=profile/mobile/platform/kernel/linux-3.10-sc7730.git
   branch: accepted/tizen_mobile
   ```
1. If your kernel source has been used to create binaries for another architecture, start by cleaning them up.
1. Set up the `.config` file for TM1:  
   ```bash
   $ make ARCH=arm tizen_tm1_defconfig
   ```
1. After reconfiguring your needs (such as `make ARCH=arm menuconfig`) or using the stock configuration (no modifications), build it:  
   ```bash
   $ make ARCH=arm zImage
   $ make ARCH=arm dtbs
   ```
1. Create a `devicetree` and `zImage` merged image with the image tools:
   ```bash
   $ scripts/sprd_dtbtool.sh -o arch/arm/boot/merged-dtb -p scripts/dtc/ -v arch/arm/boot/dts/
   $ scripts/sprd_mkdzimage.sh -o arch/arm/boot/dzImage -k arch/arm/boot/zImage -d arch/arm/boot/merged-dtb
   ```
1. Build and make the kernel module image as well. Note that you may need to do sudo first to let `sudo -n` work in the script:
   ```bash
   $ sudo ls
   $ scripts/mkmodimg.sh
   ```
1. Make a `.tar` archive from `dzImage` and `modules.img`. You can make your own `.tar` file from the 2 files:
   ```bash
   $ tar cf FILENAME_YOU_WANT.tar -C arch/arm/boot dzImage -C ../../../usr/tmp-mod modules.img
   ```
1. Send the `.tar` image to the target using `lthor`:  
   ```bash
   $ lthor FILENAME_YOU_WANT.tar
   ```

For information on how create an image by using MIC, see [MIC Image Creator](../reference/mic/mic-overview.md).



## Tizen Bootup Overview

This section provides a brief overview of the typical booting sequence, starting from the boot loader to the kernel and the platform.

**Figure: Tizen bootup sequence**

![Tizen bootup sequence](media/800px-boot-1.png)

The Tizen bootup process is the same as any other [Linux](https://wiki.tizen.org/Linux) kernel. Make sure that the correct machine ID and the boot arguments are passed from the boot loader.

After mounting the initial RAM disk image, `initramfs` hands over control to `systemd` as the Tizen platform system manager daemon. From this point, `systemd` is responsible for probing all remaining hardware, mounting all necessary file systems, and spawning all configured services. The system bootup process is split up into discrete steps. To synchronize point during start-up, target units (files whose names end in `.target`) are used for grouping units. The bootup process is highly parallelized in each target so that the order in which specific target units are reached is not determined. The `system-plugin-slp` is an OAL plugin for configuration settings, such as the mount point (`/etc/fstab`).

The following figure shows the early boot sequence after starting the kernel.

**Figure: Early boot sequence**

![Early boot sequence](media/706px-boot-2.png)

- `sysinit.target`  
  Special target unit for early boot-up scripts. It has dependencies on necessary services and targets, such as `local-fs.target`. At this point, most of the file systems, such as `/opt`, `/tmp`, and `/media`, are mounted and the `systemd`-related daemons, such as `systemd-journald`, are launched.
- `basic.target`  
  Special target unit for basic bootup. At this point, all necessary initialization for general purpose daemons, such as mount points, sockets, timers, and path units, is completed. Tizen-specific services (such as `vconf-setup` and `tizen-debug-level`) are also executed.
- `bootmode.target`  
  Special target unit for selecting the boot mode. If the kernel boot parameter (`/proc/cmdline`) has the `charger_detect_boot` option passed by a boot loader, such as `uboot`, the platform boots up in charging mode. In this mode, the system enters the low power mode and charges the battery. If the `charger_detect_boot` option is not included as a kernel boot parameter, a normal boot is started.

The following figure shows the overview of normal booting sequence in Tizen platform.

**Figure: Tizen platform boot sequence**

![Tizen platform boot sequence](media/710px-boot-3.png)

- `multi-user.target`  
  Special target unit for setting up a multi-user system with non-graphical support. On the Tizen platform, this target is used for launching platform infrastructure daemons, such as `dbus` (system session), power manager, GPS manager, telephony daemon, WRT (Web Run Time) security daemon, and the media server. Some `systemd`-related daemons (such as `systemd-logind`) are also started in this phase.
- `graphical.target`  
  Special target unit for setting up a graphical environment. Some important daemons (such as the access control and OMA DS agent servers) that must have root permission are launched at this point. The Tizen platform uses the `systemd` user session for App privilege daemons. Some daemons related to the graphics system, such as Enlightenment (window manager), are launched with the App privilege in this phase. The Tizen platform has its special target for middleware and mobile service: `tizen-middleware.target` starts the platform service daemons, such as calendar, contacts, email, message, sound, and download provider. `tizen-mobile-session.target` starts some service daemons related with the mobile session.

## BSP Customization

This section covers the basic configuration, setup, and build procedure required for building the boot loader and the kernel image for [ARM](https://wiki.tizen.org/ARM).

### Boot Loader

The boot loader is a small piece of software that is needed to perform the basic hardware and peripheral initialization and load the kernel and proper device tree binary for the device to RAM. For the Tizen platform, the boot loader comes in 2 parts, the primary boot loader and the secondary boot loader. The primary boot loader is proprietary, and the secondary boot loader is the open source `u-boot`, customized for the Tizen platform.

If your platform is already loaded with the compatible boot loader software, you can skip this section and move directly to the kernel section.

#### Boot Loader Setup and Build

To build the Tizen TM1 boot loader:

1. Install and set up cross-compile tools on your system if the host has a different architecture than the target (such as x86).
1. Start with cleaning up the `u-boot-tm1` source. Download the source from the [u-boot-tm1](https://review.tizen.org/git/?p=profile/mobile/platform/kernel/u-boot-tm1.git;a=summary) repository.  
   ```bash
   $ make distclean`
   ```
1. Set up the configuration for TM1.
1. Build `u-boot`:  
   ```bash
   $ make ARCH=arm
   ```
1. Once the build is successful, the `u-boot.bin` file is created. (This step is for preventing from flashing the other `u-boot.bin` file.)  
   ```bash
   $ tools/mkimage_signed.sh u-boot.bin "tizen_tm1"
   ```

   After the script is run, the `u-boot-mmc.bin` file is created.
1. Create a boot loader tarball to download the `u-boot` binary onto the target.  
   ```bash
   $ tar cvf bootloader.tar u-boot-mmc.bin`
   ```
>**Note**
>
>Be careful when modifying the boot loader: incorrect configuration can damage the device permanently.

#### Boot Loader Kernel Parameters

Command line parameters, such as the following example, can be passed from the boot loader to the [Linux](https://wiki.tizen.org/Linux) kernel:

```bash
console=ttyS1,115200n8
mem=1024M
loglevel=1
```

### Kernel

The kernel is the operating system that drives the platform. In this case, the kernel refers to the open source [Linux](https://wiki.tizen.org/Linux) kernel that is customized for the Tizen platform. The following section gives a brief overview about the Tizen kernel setup, configuration, and the build procedure for building a Linux kernel for your Tizen platform. The output of the kernel binary is a uImage that is suitable only for a `u-boot` boot loader. If you have chosen a secure booting configuration in your boot loader, this uImage must be compatible with your boot loader.

#### Kernel Configurations

To download the Tizen kernel source package, see [Getting Source Code and Build](https://wiki.tizen.org/Porting_Guide#Getting_Source_Code.26Build). To set up or modify your kernel configuration, use the appropriate `defconfig` file from `arch/arm/configs/` ([ARM](https://wiki.tizen.org/ARM) CPU).

For more information on the Tizen kernel configuration and kernel building, see [Kernel Build](https://wiki.tizen.org/Porting_Guide#Kernel_Build).

> **Note**
>
> Tizen uses `INOTIFY` instead of `DNOTIFY`. You must disable `DNOTIFY` from your kernel configuration.

If you want to use `initramfs`, you can use these configurations:

- `CONFIG_INITRAMFS_SOURCE`
- `CONFIG_INITRAMFS_ROOT_UID`
- `CONFIG_INITRAMFS_ROOT_GID`
- `CONFIG_INITRAMFS_COMPRESSION_NONE/GZIP/BZIP2/LZNA/LZO`

## Tizen File System

### Virtual Filesystem (VFS)

The virtual file system (VFS) is an abstraction layer on top of a physical file system (such as ext2, jfs, and ext4). The VFS provides a switching layer between the SCI (system call interface) and the file systems supported by the kernel, as shown in the following figure.

**Figure: Tizen file system**

![Tizen file system](media/800px-filesystem.png)

At the top of the VFS is a common API abstraction of functions, such as open, close, read, and write. At the bottom of the VFS are the file system abstractions that define how the upper-layer functions are implemented with respect to a specific file system.

Below the file system layer is the page cache, which provides a common set of functions to the file system layer (independent of any particular file system). This caching layer optimizes access to the physical devices by keeping data around for a short time (or speculatively reading ahead, so that the data is available when needed). Below the page cache are the device drivers, which implement the interface for the particular physical device.

#### Tizen Partition Layout

The following description is an example of the Tizen partition layout. The product vendor can modify the sequence or partition layout for their devices, as needed.

**Figure: Tizen partition layout**

![Tizen partition layout](media/800px-partitionlayout.png)

The `boot` partition is mounted in the `/boot` directory of `rootfs`. Here `s-boot`, `u-boot`, and the kernel image are saved as a file format, provided as `system.tar`.

1. The CSA (Configuration Saved Area) partition is for non-volatile data, such as the calibration value of modem.
1. The boot partition includes the kernel image, boot loader image, and modem image. Additionally, it can have device driver modules.
1. Third partition is reserved for the future.
1. The CSC (Customer Software Configuration) partition is mounted in the `/mnt/csc` directory. It can store the customer's software configuration, such as the default language and time zone.
1. The `platform` partition is mounted on the root directory. It contains fundamental frameworks for Tizen and some general utility for Linux. It can be provided as a `platform.img` file.
1. The `data` partition is mounted in the `/opt` directory and it includes applications, libraries of applications, and the platform database. It can be provided as a `data.img` file.
1. The UMS (USB Mass Storage) partition is mounted in the `/opt/media` directory and it includes default (media) contents. It can be provided as `ums.img`.

Each image file, `platform.img`, `data.img`, and `ums.img` can be zipped for downloading, for example, `<IMAGE_NAME>.tar.gz`.

Each partition has the hierarchy illustrated in the following figure.

**Figure: Tizen file system hierarchy**

![Tizen file system hierarchy](media/800px-filesystemhierarchy.png)

#### Supported File Systems

Tizen supports the Extended 4 (ext4) file system. The Tizen kernel has to be compiled to enable support for other file systems, such as JFS, XFS, BTRFS, and Reiserfs.

The Extended 4 (ext4) file system is configured as a default file system for Tizen.

#### Configuration

The following ext4 configuration options can be enabled in the kernel configuration file:

- `CONFIG_EXT4_FS=y`
- `CONFIG_EXT4_FS_XATTR=y`
- `CONFIG_EXT4_USE_FOR_EXT23=y`
- `CONFIG_EXT4_FS_SECURITY=y`

### MMC/SD/SDIO

Tizen supports MultiMediaCard, Secure Digital, and Secure Digital I/O Support. The MMC driver is implemented on top of a host controller (such as the SDHCI controller driver) and supports MMC, SD, SD High Speed, and SDHC cards.

If MMC is your booting device, read-write APIs, partition management, and flashing must be provided at the boot loader.

**Figure: Tizen MMC architecture**

![Tizen MMC architecture](media/800px-mmc.png)

The MMC/SD/SDIO driver supports the following features:

- Driver is built in-kernel
- MMC cards, including high speed cards
- SD cards, including SD high speed and SDHC cards

The MMC subsystem code structure in the kernel is located at `/driver/mmc` and divided into 3 parts:

- MMC block device driver located at `/driver/mmc/card/`
- Protocol stack for MMC, SD, SDIO located at `/driver/mmc/core/`
- Host controller driver located at `/driver/mmc/host/`

#### Hotplug MMC Event Handling

Based on the hotplug event handling, a notification is passed to `deviced` for device status changes. It detects, mounts, and monitors the status of the SD card.

#### Reference

The SDHCI controller is supported in the MMC/SD/SDIO interface. The Mobile Storage Host controller is only supported in the MMC interface.

- **Kernel configuration for MMC Interface**  
  `CONFIG_MMC_BLOCK`, `CONFIG_MMC`, `CONFIG_MSHCI` (for Mobile Storage Interface enable)  
  `sys interface: /dev/mmcblk0pX`
- **Kernel configuration for SD/SDIO Interface**  
  `CONFIG_MMC_BLOCK`, `CONFIG_MMC`  
  `CONFIG_MMC_SDHCI` (for SDHCI host Interface enable)  
  `CONFIG_MMC_SDHCI_S3C` (for Samsung SoC)  
  `sys interface: /dev/mmcblk1pX`

The `X` denotes the MMC partition number. Details of the partition mount point for Tizen are covered under [Tizen Partition Layout](#tizen-partition-layout).
