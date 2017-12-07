# Creating Tizen Images with MIC

This topic provides information on how to create a Tizen image.

Before creating an image, study the following instructions:

- [Setting up the Development Environment](setting-up.md)
- [Installing Development Tools](installing.md)
- [Cloning Tizen Source Files](cloning.md)
- [Building Packages Locally with GBS](building.md)

## Preparing the Kickstart File

Image creation requires a kickstart file that describes how to create an image. To prepare the kickstart file:

1. Download the original kickstart file:

   ```bash
   $ wget <Snapshot_date_URL>/builddata/images/<Repository>/image-configurations/<kickstart_file>
   ```

   - For example:

     - Tizen: 4.0: Unified / standard / `mobile-wayland-armv7l-tm1.ks`

       ```bash
       $ wget http://download.tizen.org/releases/daily/tizen/unified/tizen-unified_20170627.1/builddata/images/standard/image-configurations/mobile-wayland-armv7l-tm1.ks
       ```

     - Tizen: 4.0: Unified / emulator / `tv-emulator32-wayland.ks`

       ```bash
       $ wget http://download.tizen.org/releases/daily/tizen/unified/tizen-unified_20170627.1/builddata/images/emulator/image-configurations/tv-emulator32-wayland.ks
       ```

     - Tizen: 3.0: Wearable / target-circle / `wearable-wayland-armv7l-circle.ks`

       ```bash
       $ wget http://download.tizen.org/releases/daily/tizen/3.0-wearable/tizen-3.0-wearable_20170627.1/builddata/images/target-circle/image-configurations/wearable-wayland-armv7l-circle.ks
       ```

2. Modify the original kickstart file to include locally built RPMs into the Tizen image.

   For example: Tizen: 4.0: Unified / standard / `mobile-wayland-armv7l-tm1.ks`

   - The `repo` section of the original kickstart file:

     ```
     repo --name=unified-standard --baseurl=http://download.tizen.org/snapshots/tizen/unified/@BUILD_ID@/repos/standard/packages/ --ssl_verify=no  
     repo --name=base_arm --baseurl=http://download.tizen.org/snapshots/tizen/base/latest/repos/arm/packages/ --ssl_verify=no
     ```

   - The `repo` section of the modified kickstart file:

     ```
     repo --name=unified-standard --baseurl=http://download.tizen.org/snapshots/tizen/unified/@BUILD_ID@/repos/standard/packages/ --ssl_verify=no --priority=99
     repo --name=base_arm --baseurl=http://download.tizen.org/snapshots/tizen/base/latest/repos/arm/packages/ --ssl_verify=no --priority=99
     repo --name=local --baseurl=file:///home/<User>/GBS-ROOT/local/repos/tizen3.0-tm1/armv7l/ --priority=1
     ```

   > **Note**
   >
   > - The `baseurl` property of the `local` repo specifies the file path where locally built RPMs are located.
   > - Setting the priority of the `local` repository at 1 and the priorities of remote repositories at 99 guarantees that MIC uses the packages that exist in the local repository with a higher priority, when packages are available in both remote and local repositories.
   > - To add new packages into a Tizen image, add the new packages' names into the `%package` section, and add them into the `local` repository.

## Creating a Tizen Image

To create a Tizen image:

```bash
$ gbs createimage --ks-file=mobile-wayland-armv7l-tm1.ks
```

If you have more than 4 GB of RAM available, use the `--tmpfs` option to speed up the image creation:

```bash
$ gbs createimage --ks-file=mobile-wayland-armv7l-tm1.ks --tmpfs
```

The following example shows the `gbs createimage` command output:

```
...
Info: Running scripts ...
kickstart post script start
Info: Checking filesystem /var/tmp/mic/build/imgcreate-Rii2MC/tmp-pVQesQ/platform.img
Info: Checking filesystem /var/tmp/mic/build/imgcreate-Rii2MC/tmp-pVQesQ/data.img
Info: Checking filesystem /var/tmp/mic/build/imgcreate-Rii2MC/tmp-pVQesQ/ums.img
Info: Pack all loop images together to TM1-new-201609030819.tar.gz
Info: The new image can be found here:
/home/<User>/tizen/mic-output/TM1-201609030819.tar.gz
/home/<User>/tizen/mic-output/TM1-201609030833.packages
/home/<User>/tizen/mic-output/TM1-201609030819.xml
Info: Finished.
```

`TM1-201609030819.tar.gz` is the image file and `TM1-201609030833.packages` contains package info integrated in the image, including package name, version, and VCS information.

Once the Tizen image is created, the final step is to flash the image to a target device for verification. For more information, see [Flashing an Image to Device](flashing.md).
