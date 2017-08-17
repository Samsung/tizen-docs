# Creating Tizen Images with MIC

This topic provides information on how to create a Tizen image.

You must read, understand, and correctly follow the instructions in the following documents before creating images:

- [Setting up Development Environment](https://source.tizen.org/documentation/setting-development-environment)
- [Installing Development Tools](https://source.tizen.org/documentation/installing-development-tools)
- [Cloning Tizen Source Files](https://source.tizen.org/documentation/developer-guide/cloning-tizen-source)
- [Building Packages Locally with GBS](https://source.tizen.org/documentation/developer-guide/building-packages-locally)

## Preparing the Kickstart File

Image creation requires a kickstart file that describes how to create an image. To prepare the kickstart file:

1. Download the original kickstart file:

   ```
   $ wget <Snapshot_date_URL>/builddata/images/<Repository>/image-configurations/<kickstart_file>
   ```

   - For example:

     - Tizen: 4.0: Unified / standard/ `mobile-wayland-armv7l-tm1.ks`

       ```
       $ wget http://download.tizen.org/releases/daily/tizen/unified/tizen-unified_20170627.1/builddata/images/standard/image-configurations/mobile-wayland-armv7l-tm1.ks
       ```

     - Tizen: 4.0: Unified / emulator/ `tv-emulator32-wayland.ks`

       ```
       $ wget http://download.tizen.org/releases/daily/tizen/unified/tizen-unified_20170627.1/builddata/images/emulator/image-configurations/tv-emulator32-wayland.ks
       ```

     - Tizen: 3.0: Wearable / target-circle/ `wearable-wayland-armv7l-circle.ks`

       ```
       $ wget http://download.tizen.org/releases/daily/tizen/3.0-wearable/tizen-3.0-wearable_20170627.1/builddata/images/target-circle/image-configurations/wearable-wayland-armv7l-circle.ks
       ```

2. Modify the original kickstart file to include locally built RPMs into the Tizen image.

   For example: Tizen: 4.0: Unified / standard/ `mobile-wayland-armv7l-tm1.ks`

   - The `repo` section of the original kickstart file:

     ```
     repo --name=unified-standard --baseurl=http://download.tizen.org/snapshots/tizen/unified/@BUILD_ID@/repos/standard/packages/ --ssl_verify=norepo --name=base_arm --baseurl=http://download.tizen.org/snapshots/tizen/base/latest/repos/arm/packages/ --ssl_verify=no
     ```

   - The `repo` section of the modified kickstart file:

     ```
     repo --name=unified-standard --baseurl=http://download.tizen.org/snapshots/tizen/unified/@BUILD_ID@/repos/standard/packages/ --ssl_verify=no --priority=99repo --name=base_arm --baseurl=http://download.tizen.org/snapshots/tizen/base/latest/repos/arm/packages/ --ssl_verify=no --priority=99repo --name=local --baseurl=file:///home/<User>/GBS-ROOT/local/repos/tizen3.0-tm1/armv7l/ --priority=1
     ```

   **Note:**The `baseurl` property of the `local` repo specifies the file path where locally built RPMs are located.Setting the priority of the `local` repository at 1 and the priorities of remote repositories at 99 guarantees that MIC uses the packages that exist in the local repo with a higher priority if packages are available in both remote and local repositories.To add new packages into a Tizen image, add the new packages' names into the `%package` section, and add them into the `local` repo.

## Creating a Tizen Image

To create a Tizen image, execute the following command:

```
$ gbs createimage --ks-file=mobile-wayland-armv7l-tm1.ks
```

If you have more than 4 GB of RAM available, use the `--tmpfs` option to speed up the image creation:

```
$ gbs createimage --ks-file=mobile-wayland-armv7l-tm1.ks --tmpfs
```

The following example shows the `gbs createimage` command output:

```
...Info: Running scripts ...kickstart post script startInfo: Checking filesystem /var/tmp/mic/build/imgcreate-Rii2MC/tmp-pVQesQ/platform.imgInfo: Checking filesystem /var/tmp/mic/build/imgcreate-Rii2MC/tmp-pVQesQ/data.imgInfo: Checking filesystem /var/tmp/mic/build/imgcreate-Rii2MC/tmp-pVQesQ/ums.imgInfo: Pack all loop images together to TM1-new-201609030819.tar.gzInfo: The new image can be found here:/home/<User>/tizen/mic-output/TM1-201609030819.tar.gz/home/<User>/tizen/mic-output/TM1-201609030833.packages/home/<User>/tizen/mic-output/TM1-201609030819.xmlInfo: Finished.
```

`TM1-201609030819.tar.gz` is the image file and `TM1-201609030833.packages` contains package info integrated in the image, including package name, version, and VCS information.

Once the Tizen image is created, the final step is to flash the image to a target device for verification. For more information, see [Flash an Image to Device](https://source.tizen.org/documentation/reference/flash-device).