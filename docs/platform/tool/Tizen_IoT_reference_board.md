**Eagleye Board**\

![](Eagleye_530s.jpg "fig:Eagleye_530s.jpg")\
After getting an Eagleye 530s board, you should migrate the boot image
for tizen to it.\

Prerequisite 
-------------

\$ sudo apt-get install android-tools-fastboot lthor\

Migrate boot image for tizen. 
------------------------------

**Target Side**\
1. Enter boot mode.\
2. Enter fastboot mode.\
*ARTIK\# fastboot 0\
*

**Host Side**\
1. Download the tool - compressed file. (file :
<https://github.com/playchang22/tizeniot/raw/master/Migration_artik533s_tizen_usb_recovery.tar.gz>)\
2. Extract it on Host PC(Ubuntu linux)\
3. Move to artik533s/os\_3.2.0\
4. Execute \"flash\_boot\_for\_tizen.sh\"\
*\$ ./flash\_boot\_for\_tizen.sh*\

How to download tizen images. 
------------------------------

1\. Getting images.\
Boot Image : a
tarball(tizen-unified\_<snapshotid>\_iot-boot-armv7l-artik533s.tar.gz)
on
<http://download.tizen.org/snapshots/tizen/unified/latest/images/standard/iot-boot-armv7l-artik533s/>\
Platform Image : a
tarball(tizen-unified\_<snapshotid>\_iot-headless-2parts-armv7l-artik530\_710.tar.gz)
on
<http://download.tizen.org/snapshots/tizen/unified/latest/images/standard/iot-headless-2parts-armv7l-artik530_710/>\
2. Downloading image to a target\
**Target Side**\
artik530\# thordown\
{\| class=\"wikitable\" \|- \|

    U-Boot 2016.01-g1aec83841-TIZEN.org (Jun 01 2018 - 02:02:19 +0000)

    Model: Samsung artik533 board based on Nexell s5p4418

    Board: ARTIK533 Raptor
    DRAM:  992 MiB
    HW Revision:    6
    MMC:   NEXELL DWMMC: 0, NEXELL DWMMC: 1
    In:    serial
    Out:   serial
    Err:   serial
    Writing to MMC(0)... done
    Net:   eth0: ethernet@c0060000
    Hit any key to stop autoboot:  0
    artik530#
    artik530# thordown
    TIZEN "THOR" Downloader
    Download request from the Host PC
    ##File System is consistent
    file found deleting
    update journal finished
    File System is consistent
    update journal finished
    45918 bytes written in 87 ms (514.6 KiB/s)
    #File System is consistent
    file found deleting
    update journal finished
    File System is consistent
    update journal finished
    6344432 bytes written in 751 ms (8.1 MiB/s)
    #File System is consistent
    file found deleting
    update journal finished
    File System is consistent
    update journal finished
    49898 bytes written in 89 ms (546.9 KiB/s)
    U-Boot signature: "artik533_raptor"
    bootloader.img signature: "artik533_raptor". OK!
    Target version : 3.2.0
    Image  version : 3.2.0
    ###File System is consistent
    file found deleting
    update journal finished
    File System is consistent
    update journal finished
    7340032 bytes written in 844 ms (8.3 MiB/s)
    ###########File System is consistent
    file found deleting
    update journal finished
    File System is consistent
    update journal finished
    7732224 bytes written in 881 ms (8.4 MiB/s)
    resetting ...

\|} **Host Side**\
\$ lthor tizen-unified\_20180629.3\_iot-boot-armv7l-artik533s.tar.gz
tizen-unified\_20180629.3\_iot-headless-2parts-armv7l-artik530\_710.tar.gz

+-----------------------------------------------------------------------+
|     $ lthor tizen-unified_20180629.3_iot-boot-armv7l-artik533s.tar.gz |
|  tizen-unified_20180629.3_iot-headless-2parts-armv7l-artik530_710.tar |
| .gz                                                                   |
|                                                                       |
|     Linux Thor downloader, version 2.0                                |
|     Authors: Jaehoon You <jaehoon.you@samsung.com>                    |
|              Krzysztof Opasiak <k.opasiak@samsung.com>                |
|                                                                       |
|     tizen-unified_20180629.3_iot-boot-armv7l-artik533s.tar.gz :       |
|     [modules.img]    20480k                                           |
|     [s5p4418-artik533-compy.dtb]     44k                              |
|     [zImage]         6195k                                            |
|     [s5p4418-artik533-raptor-rev00.dtb]      48k                      |
|     [bootloader.img]         1024k                                    |
|     [params.bin]     16k                                              |
|     tizen-unified_20180629.3_iot-headless-2parts-armv7l-artik530_710. |
| tar.gz :                                                              |
|     [ramdisk.img]    7168k                                            |
|     [rootfs.img]     243084k                                          |
|     [system-data.img]        61012k                                   |
|     [ramdisk-recovery.img]   7551k                                    |
|     -------------------------                                         |
|             total : 338.50MB                                          |
|                                                                       |
|                                                                       |
|     Download files from tizen-unified_20180629.3_iot-boot-armv7l-arti |
| k533s.tar.gz                                                          |
|                                                                       |
|     [modules.img]   | sending  20480k/ 20480k 100% block 20     [avg  |
| 39.89 MB/s]                                                           |
|     [s5p4418-artik53\ sending     44k/    44k 100% block 1      [avg  |
| 1.69 MB/s]                                                            |
|     [zImage]        | sending   6195k/  6195k 100% block 7      [avg  |
| 34.25 MB/s]                                                           |
|     [s5p4418-artik53\ sending     48k/    48k 100% block 1      [avg  |
| 1.77 MB/s]                                                            |
|     [bootloader.img]| sending   1024k/  1024k 100% block 1      [avg  |
| 30.61 MB/s]                                                           |
|     [params.bin]    - sending     16k/    16k 100% block 1      [avg  |
| 0.60 MB/s]                                                            |
|                                                                       |
|     Download files from tizen-unified_20180629.3_iot-headless-2parts- |
| armv7l-artik530_710.tar.gz                                            |
|                                                                       |
|     [ramdisk.img]   | sending   7168k/  7168k 100% block 7      [avg  |
| 39.51 MB/s]                                                           |
|     [rootfs.img]    | sending 243084k/243084k 100% block 238    [avg  |
| 12.45 MB/s]                                                           |
|     [system-data.img\ sending  61012k/ 61012k 100% block 60     [avg  |
| 18.40 MB/s]                                                           |
|     [ramdisk-recover/ sending   7551k/  7551k 100% block 8      [avg  |
| 35.96 MB/s]                                                           |
|                                                                       |
|     request target reboot : success                                   |
+-----------------------------------------------------------------------+

Reference Site: 
----------------

<http://wiki.seeedstudio.com/Eagleye_530s/>

[Category:Tizen](Category:Tizen "wikilink")
[Category:IoT](Category:IoT "wikilink")
[Category:Tool](Category:Tool "wikilink")
[Category:ARTIK](Category:ARTIK "wikilink")
[Category:Hardware](Category:Hardware "wikilink")
