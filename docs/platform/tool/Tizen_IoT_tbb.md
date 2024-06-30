Introduction
============

**Tizen Building Block Tool** is a tool to make a Tizen IoT Image
easily.\
**It is experimental.**\
Tizen makes some building-blocks according to API reference category.\
A developer can make a Tizen IoT image to select some building-blocks
with **tbb**.\
It is based on kconfig of Linux.\
**tbb** supports Raspberry pi3/4 and ARTIK 530 reference boards.

Prerequisites
=============

It works on Ubuntu 16.04.\
libncurses5-dev, mic, libxml2-utils(xmllint), wget, gzip\
how to install mic and gbs\
<https://source.tizen.org/documentation/developer-guide/getting-started-guide/installing-development-tools>\
Connected to internet (download.tizen.org)\

How to download tbb
===================

Cloning tbb from review.tizen.org
---------------------------------

\$ git clone <https://git.tizen.org/cgit/tools/tbb>\
\$ git checkout tizen

Usage
-----

1\. Cleanning configurations and build output\
\$ make distclean

2\. Cleanning build output & sdk extension\
\$ make clean

3\. Selecting configurations\
\$ make menuconfig

4\. Making a image (After selecting configurations)\
\$ make

5\. Making a sdk extension (After making a image)\
\$ make configsdk

6\. Saving a configuration file (After selection configurations)\
\$ cp .config configs/xxx\_defconfig\
xxx : configuration name

7\. Loading a configuration\
\$ make xxx\_defconfig

8\. Help\
\$ make help

How to make a Tizen IoT image
=============================

**It is simple**.\
A developer runs tbb UI, select some configurations and make a image.

Running menuconfig UI
---------------------

In tbb directory, execute the below command\
**\$ make menuconfig**\
![](Tbb_FirstPage.jpg "fig:Tbb_FirstPage.jpg"){width="790"}

Selecting configurations
------------------------

**1. Platform Version (Can use the default)**\
- You should select 6.0.

**2. Snapshot ID (Can use the default)**\
- Tizen repo snapshot id. Its format is yyyymmdd.n.\
- You can check it on
<http://download.tizen.org/snapshots/tizen/unified/>.

**3. Image Name (Can use the default)**\
- You can change the prefix of output image name.

**4. Select Board**\
- You must select a board. (Currently ARTIK530, RPI3/4 are supported)\
- You can see next menu when selecting a board.\
![](Tbb_SelectBoard.jpg "fig:Tbb_SelectBoard.jpg"){width="790"}

**5. HW & HAL Features**\
- You should select some HW and HAL features which you add to a device.\
- **According to selection, Post menu configuration will be
different**.\
![](Tbb_Select_HW_HAL.jpg "fig:Tbb_Select_HW_HAL.jpg"){width="790"}

**6. Select Partition**\
- You must select a partition.\
- You can see next menu when selecting a partition.\
![](Tbb_Select_Partition.jpg "fig:Tbb_Select_Partition.jpg"){width="790"}
**→**
![](Tbb_Select_Partition_2.jpg "fig:Tbb_Select_Partition_2.jpg"){width="790"}

**7. Tizen IoT Preset**\
- You should select a Tizen IoT Preset.\
- If you are a export, you can select no preset and packages directly in
\"Advanced Configuration\" menu.\
- There are two presets. (Tizne IoT Core and Tizen IoT Headed). You can
see Tizen IoT Headed preset only when selecting Display Server in \"HW &
HAL Features\" menu.\
- You can see next menu when selecting a preset.\
![](Tbb_Select_Preset.jpg "fig:Tbb_Select_Preset.jpg"){width="790"}
**→**
![](Tbb_Select_Preset_HL.jpg "fig:Tbb_Select_Preset_HL.jpg"){width="790"}

**8. Tizen Native API Sets**\
- You should select API which you add to a device.\
![](Tbb_Select_API.jpg "fig:Tbb_Select_API.jpg"){width="790"}\
![](Tbb_Select_API_2.jpg "fig:Tbb_Select_API_2.jpg"){width="790"} **→**
![](Tbb_Select_API_mm.jpg "fig:Tbb_Select_API_mm.jpg"){width="790"}

Optionally

**9. Tizen Platform Internal Feature Sets**

**10. Tizen IoT Reference Application**

**11. Advanced Configuration**\
- You can select some individual packages.

**12. Custom repository for your rpm packages**.\
Adding your repository to private repository menu if needed.\
- local repo - <file:///directory>\
- http(s) repo - <http://URL> or <https://URL>

Making a image
--------------

After selecting configurations, execute the below command.\
**\$ make**\
After complete, you can see the output into the directory of
\"output/build\"\
tizen-iot-img-4.0-20171214.5\_armv7l.tar.gz : image file\

How to update a image
=====================

ARTIK 530 (under construction)
------------------------------

**1. Changing the boot and partition for Tizen environment.**\
**2. Updating boot image and platform image**.\
**3. Installing plugin**\
- After updating a firmware, Do the below.\
- Booting the device.\
- Downloading the plugin on
<http://developer.samsung.com/tizendevice/firmware>.\
- Unzip and Install the plugin of artik530.\
\$ ./ARTIK\_530\_plugin\_tizen4.0.sh\
![](Artik530_plugin.jpg "fig:Artik530_plugin.jpg")

Raspberry pi3
-------------

**1. Prerequisites**\
\$ sudo apt-get install pv

**2. Downloading the fusing-script for Raspberry pi3**\
\$ wget
<https://git.tizen.org/cgit/platform/kernel/u-boot/plain/scripts/tizen/sd_fusing_rpi3.sh?h=tizen>
\--output-document=sd\_fusing\_rpi3.sh\
\$ chmod 755 sd\_fusing\_rpi3.sh

**3. Updating new firmware to sdcard**\
- Insert a sd-card to Linux host PC.\
- Check the device node of the sd-card. (ex. sdx : x is alphabet)\
- Download a boot image.\
(http://download.tizen.org/snapshots/tizen/4.0-unified/tizen-4.0-unified\_20171214.5/images/standard/iot-boot-arm64-rpi3/tizen-4.0-unified\_20171214.5\_iot-boot-arm64-rpi3.tar.gz)\
- Update new firmwares.\
\$ sudo ./sd\_fusing\_rpi3.sh -d /dev/sdx -b
tizen-iot-img-4.0-20171214.5.tar.gz
tizen-4.0-unified\_20171214.5\_iot-boot-arm64-rpi3.tar.gz \--format

**4. Installing plugin**\
- After updating a firmware, Do the below.\
- Downloading the plugin on
<http://developer.samsung.com/tizendevice/firmware>\
- Insert a sd-card to Linux host PC.\
- Check the device node of the sd-card. (ex. sdx : x is alphabet)\
- Install the plugin of rpi3\
\$ sudo RPI3\_plugin\_tizen4.0 /dev/sdx\
![](Rpi3_plugin.jpg "fig:Rpi3_plugin.jpg")

Structure of Building Blocks
============================

The structure of Building Blocks is almost same as the structure of
Tizen Native API.\
<https://developer.tizen.org/development/api-references/native-application>

    Building Blocks─┬─Account─┬AccountManager
                     │           ├FIDO Client
                     │           ├OAuth2
                     │           ├Sync Manager
                     │           └libOauth
                     ├─AppFW──┬Alarm
                     │           ├Attach-Pannel
                     │           ├Badge
                     │           ├Data Contorl
                     │           ├App Event
                     │           ├Package management in externel storage SD card
                     │           ├Media Key
                     │           ├Message Port
                     │           ├Native EFL UI app model
                     │           ├EFL widget App model
                     │           ├Notification
                     │           ├Shortcut
                     │           └TPK package management
                     ├─Base ──┬C++ Standard library
                     │           ├Common Error
                     │           ├Glib
                     │           ├Glibc
                     │           ├LibXML
                     │           ├Minizip
                     │           ├OpenMP
                     │           ├Sqlite
                     │           ├Base-Utils
                     │           └zlib
                     ├─Content─┬Download
                     │           ├MIME Type
                     │           └Media Content
                     ├─Context─┬ActivityGeusture Recognition
                     │           ├Contextual History
                     │           └Contextual Trigger
                     ├─Location ┬Geofence Manager
                     │           └Location Manager
                     ├─Maps ──┬Here_Plugin
                     │           ├Maps_Service
                     │           └Mapzen_Plugin
                     ├─Messaging┬Email
                     │           ├Messages
                     │           └Push Client
                     ├─Multimedia┬AudioCore
                     │            ├Audio_IO
                     │            ├Camera
                     │            ├Configuration
                     │            ├Image_Util
                     │            ├Media_Codec
                     │            ├Media_Controller
                     │            ├Media_Demuxer
                     │            ├Media_Muxer
                     │            ├Media_Streamer
                     │            ├Media_Tool
                     │            ├Media_Vision_Barcode
                     │            ├Media_Vision_Face
                     │            ├Media_Vision_Image
                     │            ├Media_Vision_Surveillance
                     │            ├Metadata_Editor
                     │            ├Metadata_Extractor
                     │            ├OpenAL
                     │            ├Player
                     │            ├Radio
                     │            ├Recorder
                     │            ├Screen_Mirroring
                     │            ├Sound_Manager
                     │            ├Stream Recorder
                     │            ├Thumbnail_Util
                     │            ├Tone_Player
                     │            ├Video_Util
                     │            ├WAV_Player
                     │            └libEXIF
                     ├─Network─┬ASP
                     │           ├Bluetooth_BREDR
                     │           ├Bluetooth_Call_Audio
                     │           ├Bluetooth_LE
                     │           ├Bluetooth_Media_Audio
                     │           ├Bluetooth_Transfer
                     │           ├Connection
                     │           ├Curl
                     │           ├DNS-SD
                     │           ├HTTP
                     │           ├IoTCon
                     │           ├MTP
                     │           ├NFC
                     │           ├SSDP
                     │           ├STC
                     │           ├Smartcard
                     │           ├VPN_Service
                     │           ├WiFi
                     │           ├WiFi_Direct
                     │           └WiFi_Manager
                     ├─Security ┬CSR
                     │           ├Device Certificate
                     │           ├Device Policy
                     │           ├Key Manager
                     │           ├OpenSSL
                     │           ├Privilege Info
                     │           └YACA
                     ├─Social ─┬Calendar
                     │           ├Contacts
                     │           └Phonenumber utils
                     ├─System ─┬Device_Battery
                     │           ├Device_Callback
                     │           ├Device_Display
                     │           ├Device_Haptic
                     │           ├Device_IR
                     │           ├Device_Led
                     │           ├Device_Power
                     │           ├Feedback
                     │           ├Runtime information with Resourced
                     │           ├Runtime information with Resourced-headless
                     │           ├Runtime information with Resourced-light
                     │           ├Sensor_Listener
                     │           ├Sensor_Recorder
                     │           ├Storage
                     │           ├System information
                     │           ├System_Settings
                     │           ├T_Trace
                     │           ├USB_Host
                     │           └dlog
                     ├─Telephony
                     ├─UI ───┬Cairo
                     │           ├Clipboard History Manager
                     │           ├DALi
                     │           ├Display_Server
                     │           ├Display_ServerHeadless
                     │           ├EFL_ELM_Accessbility
                     │           ├EFL_Extension
                     │           ├EFL_MainLoop
                     │           ├EFL_NativeUIToolkit
                     │           ├External_Output_Manager
                     │           ├FontConfig
                     │           ├Freetype
                     │           ├HarfBuzz
                     │           ├Minicontrol
                     │           ├OpenGL ES with SDL
                     │           ├Vulkan with SDL
                     │           ├TBM_Surface
                     │           ├Tizen_WS_Shell
                     │           ├ViewManager
                     │           └Vulkan
                     ├─UIX───┬Input Method
                     │           ├STT
                     │           ├TTS
                     │           ├Voice control
                     │           └Voice control elementary
                     └─Web──┬WebView
                                └json glib

[Category:Tizen](Category:Tizen "wikilink")
[Category:IoT](Category:IoT "wikilink")
[Category:Tool](Category:Tool "wikilink")
[Category:ARTIK](Category:ARTIK "wikilink")
[Category:Hardware](Category:Hardware "wikilink")
