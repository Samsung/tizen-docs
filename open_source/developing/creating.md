# Creating Tizen Images with MIC



## 1 Introduction

This document provides information about how to create a Tizen image. This document assumes that the instructions in the following documents have been read, well understood, and correctly followed:

- [Setting up Development Environment](https://source.tizen.org/documentation/setting-development-environment)
- [Installing Development Tools](https://source.tizen.org/documentation/installing-development-tools)
- [Cloning Tizen Source](https://source.tizen.org/documentation/developer-guide/cloning-tizen-source)
- [Building Packages Locally](https://source.tizen.org/documentation/developer-guide/building-packages-locally)

## 2 Preparing the Kickstart File

Image creation requires a kickstart file that describes how to create an image. To get the kickstart file ready, perform the following procedure:

1. Download the original kickstart file by executing one of the following commands, as appropriate:

   - armv7l

     ```
     $ wget http://download.tizen.org/snapshots/tizen/mobile/<snapshot_date>/builddata/image-configs/mobile-wayland-armv7l-tm1.ks
     ```

Examples of downloading original kickstart file from the release with Snapshot_ID "tizen-3.0" are shown below:

```
# kickstart file for armv7l$ wget http://download.tizen.org/snapshots/tizen/mobile/latest/builddata/images/target-TM1/image-configurations/mobile-wayland-armv7l-tm1.ks 
```

1. Enable local image creation function by updating the original kickstart file and performing appropriate replacement.

   Take the kickstart file from the release with Snapshot_ID "tizen-3.0" as an example, replace the repo section with one of the following, as appropriate:

   - armv7l

   - ```
     repo --name=Tizen-main --baseurl=http://download.tizen.org/snapshots/tizen/mobile/latest/repos/target-TM1/packages/ --save --ssl_verify=no --priority=99repo --name=Tizen-base --baseurl=http://download.tizen.org/snapshots/tizen/mobile/latest/repos/target-TM1/packages/ --save --ssl_verify=no --priority=99repo --name=local --baseurl=file:///home/<User>/GBS-ROOT/local/repos/tizen3.0-tm1/armv7l/ --priority=1repo --name=local-toolchain --baseurl=file:///<Tizen_Project>/pre-built/toolchain-arm/ --priority=2
     ```

   Then replace "<User>" with the actual value and replace "<Tizen_Project>" with the top directory of Tizen source code in which **repo sync** command is executed, respectively.

**Note:**

- By adding the "local-toolchain" repo, the packages excluded during the building process can be found during the image creation.
- Specifying the priorities of remote repo and local repo as 99 and 1, respectively, guarantees that MIC will use the packages that exist in the local repo with higher priority when the packages exist in the remote and local repo at the same time.

## 3 Creating a Tizen Image

To create a Tizen image, execute the following command:

```
$ gbs createimage --ks-file=mobile-wayland-armv7l-tm1.ks
```

If the size of the RAM is larger than 4G, use "--tmpfs" option to speed up the image creation:

```
$ gbs createimage --ks-file=mobile-wayland-armv7l-tm1.ks --tmpfs
```

Here's an example of output:

```
...Info: Running scripts ...kickstart post script startInfo: Checking filesystem /var/tmp/mic/build/imgcreate-Rii2MC/tmp-pVQesQ/platform.imgInfo: Checking filesystem /var/tmp/mic/build/imgcreate-Rii2MC/tmp-pVQesQ/data.imgInfo: Checking filesystem /var/tmp/mic/build/imgcreate-Rii2MC/tmp-pVQesQ/ums.imgInfo: Pack all loop images together to TM1-new-201609030819.tar.gzInfo: The new image can be found here:/home/<User>/tizen/mic-output/TM1-201609030819.tar.gz/home/<User>/tizen/mic-output/TM1-201609030833.packages/home/<User>/tizen/mic-output/TM1-201609030819.xmlInfo: Finished.
```

TM1-201609030819.tar.gz is the image file, and TM1-201609030833.packages contains packages info integrated in the image, including package name, version and VCS information. Once the Tizen image is created, the final step is to flash the image to target device for verification. Refer to the [Flash an Image to Device](https://source.tizen.org/documentation/reference/flash-device) for details.

 