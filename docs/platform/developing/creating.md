# Create Tizen Images with MIC

This topic provides information on how to create a Tizen image.

Before creating an image, study the following instructions:

- [Setting up the Development Environment](setting-up.md)
- [Installing Development Tools](installing.md)
- [Cloning Tizen Source Files](cloning.md)
- [Building Packages Locally with GBS](building.md)

## MIC image creator

MIC is an image creator that is used to create images for Tizen. 

The tool offers three major functions as follows:
- Create an image in a specific format.
- Chroot into an image.
- Convert an image to another format.

For more information on the tool and its functions, see [MIC Image Creator](../reference/mic/mic-overview.md).

## Prepare the kickstart file

Image creation requires a kickstart file that describes how to create an image. To prepare the kickstart file, follow the steps below:

1. Download the original kickstart file:

   ```
   $ wget <Snapshot_date_URL>/images/<Repository>/<Image_name>/<kickstart_file>
   ```

   - For example:

     - Tizen: latest: Unified / standard / `mobile-wayland-armv7l-tm1.ks`

       ```
       $ wget http://download.tizen.org/releases/milestone/tizen/unified/tizen-unified_20211014.1/images/standard/mobile-wayland-armv7l-tm1/tizen-unified_20211014.1_mobile-wayland-armv7l-tm1.ks
       ```

2. Modify the original kickstart file to update the `baseurl` properties and to include locally built RPMs into the Tizen image.

   Add a --priority option to increase a local repository's priority for build.
   For example: Tizen: latest: Unified / standard / `mobile-wayland-armv7l-tm1.ks`

   - The `repo` section of the original kickstart file:

     ```
     repo --name=unified-standard --baseurl=http://download.tizen.org/snapshots/tizen/unified/tizen-unified_20211014.1/repos/standard/packages/ --ssl_verify=no
     repo --name=base_arm --baseurl=http://download.tizen.org/snapshots/tizen/base/latest/repos/standard/packages/ --ssl_verify=no
     ```

   - The `repo` section of the modified kickstart file
     (added a local repository and only added ***--priority*** option in the end of each line):

     ```
     repo --name=unified-standard --baseurl=http://download.tizen.org/releases/milestone/tizen/unified/tizen-unified_20211014.1/repos/standard/packages/ --ssl_verify=no --priority=99
     repo --name=base_arm --baseurl=http://download.tizen.org/releases/milestone/tizen/base/latest/repos/standard/packages/ --ssl_verify=no --priority=99
     repo --name=local --baseurl=file:///home/<User>/GBS-ROOT/local/repos/<gbs.conf_profile>/armv7l/ --priority=1
     ```

   > [!NOTE]
   >
   > - The `baseurl` property of the `local` repo specifies the file path where locally built RPMs are located.
   > - Setting the priority of the `local` repository at 1 and the priorities of remote repositories at 99 guarantees that MIC uses the packages that exist in the local repository with a higher priority when packages are available in both remote and local repositories.
   > - To add new packages to a Tizen image, add the new packages' names into the `%package` section, and add them into the `local` repository.
   >   You can check package's name in the `Name` section of the spec file.

## Create a Tizen image

To create a Tizen image, follow the steps below:

```
$ gbs createimage --ks-file=mobile-wayland-armv7l-tm1.ks
```

> [!NOTE]
>
> If you have more than 4 GB of RAM available, use the `--tmpfs` option to speed up the image creation:
>
> ```
> $ gbs createimage --ks-file=mobile-wayland-armv7l-tm1.ks --tmpfs
> ```

The following example shows the `gbs createimage` command output:

```
...
Info: Running scripts ...
kickstart post script start
Info: Checking filesystem /var/tmp/mic/build/imgcreate-Rii2MC/tmp-pVQesQ/platform.img
Info: Checking filesystem /var/tmp/mic/build/imgcreate-Rii2MC/tmp-pVQesQ/data.img
Info: Checking filesystem /var/tmp/mic/build/imgcreate-Rii2MC/tmp-pVQesQ/ums.img
Info: Pack all loop images together to mobile-wayland-armv7l-tm1-202106161915.tar.gz
Info: The new image can be found here:
/home/<User>/tizen/mic-output/mobile-wayland-armv7l-tm1-202106161915.tar.gz
/home/<User>/tizen/mic-output/mobile-wayland-armv7l-tm1-202106161915.packages
/home/<User>/tizen/mic-output/mobile-wayland-armv7l-tm1-202106161915.xml
/home/<User>/tizen/mic-output/manifest.xml
Info: Finished.
```

`mobile-wayland-armv7l-tm1-202106161915.tar.gz` is the image file and `mobile-wayland-armv7l-tm1-202106161915.packages` contains package info integrated in the image, including package name, version, and VCS information.

Once the Tizen image is created, the final step is to flash the image to a target device for verification. For more information, see [Flashing an Image to Device](flashing.md).
