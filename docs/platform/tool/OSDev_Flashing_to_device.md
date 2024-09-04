Process to flash to device
--------------------------

-   [RD-210](Reference_Device-210 "wikilink") aka lb 2012
-   [RD-PQ](Reference_Device-PQ "wikilink") 2013
-   [Reference\_Device](Reference_Device "wikilink") :
    [TM1](TM1 "wikilink") 2015

Current Know working Setup
--------------------------

-   <http://download.tizen.org/releases/2.1/tizen-2.1/images/RD-210/tizen-2.1_20130517.6_RD-210.tar.gz>
-   <https://wiki.tizen.org/wiki/Enable_3D_Acceleration_on_Tizen>

### Downloads

-   Download or build an image such as one from
    <http://download.tizen.org/snapshots/1.0/latest/images/>
    [1](http://download.tizen.org/snapshots/1.0/latest/images/) which
    will be in a \*.tar.gz file

1.  Such as the lb-tizen-1.0\_20120613.10-rs.tar.gz image for lunchbox

-   Download the lthor tool for Linux PCs available online (was at
    <http://download.tizen.org/tools/lthor-tool/> )

Before the [lthor](lthor "wikilink") binary was pre-compiled in 32-bit
environment, so you need to install some 32-bit libraries in your host,
for example in [Ubuntu](Ubuntu "wikilink") 12.04 :

#### Ubuntu 12.04

Update : Use 64bit binary ie :

<http://download.tizen.org/tools/archive/13.03/Ubuntu_12.10/amd64/lthor_1.0_amd64.deb>

1\. Install 32-bit libs

` sudo apt-get install ia32-libs-multiarch`

2\. Install libarchive in i386 flavor

` sudo apt-get install libarchive12:i386`

3\. \"Fix\" libarchive symlink

` sudo ln -s /usr/lib/i386-linux-gnu/libarchive.so.12.0.3 /usr/lib/i386-linux-gnu/libarchive.so.2`

#### Debian

Similar procedure , read <http://wiki.debian.org/Multiarch/HOWTO>

` sudo ln -fs libarchive.so.12  /usr/lib/i386-linux-gnu/libarchive.so.2`

### Flashing the Tizen image

Step 1. Boot the phone into download mode.

1.  Make sure the phone is powered-off.
2.  Press <volume-down> + <power> key simultaneously.
3.  Phone will boot-up and download mode image will be displayed on the
    phone.

-   Step 2. Connect the phone to Linux PC with USB cable.

<!-- -->

-   Step 3. Flashing image

1.  Execute lthor in a console on the Linux PC as follows, make sure
    you\'re running lthor in 32-bit environment (if flash hang, try
    unzip and flash the \*.tar file):

<!-- -->

     $ sudo ./lthor lb-tizen-1.0_20120613.10-rs.tar.gz
     or
     $ sudo ./lthor lb-tizen-1.0_20120613.10-rs.tar

-   Step 4. Wait until all files are downloaded on to the phone.

The phone will be automatically rebooted after successful downloading.

Reset device with Tizen 1.0 image
---------------------------------

**This method is only valid for Tizen reference target devices. Because
it may cause some problems for other devices, we do not recommend to use
it for other devices.**

### Downloads

-   Download the tizen downloader for Linux PCs available at
    download.tizen.org/tools/tizen-downloader/
    [2](http://download.tizen.org/tools/tizen-downloader/)

The tizen-download binary is pre-compiled in 32-bit environment, so you
need to install some 32-bit libraries in your host, for example in
Ubuntu 12.04:

#### Ubuntu 12.04

1\. Install libcurl3

` sudo apt-get install libcurl3`

### Flashing the Tizen image

Step 1. Boot the phone into download mode.

1.  Make sure the phone is powered-off.
2.  Press <volume-down> + <power> key simultaneously.
3.  Phone will boot-up and download mode image will be displayed on the
    phone.

-   Step 2. Connect the phone to Linux PC with USB cable.

<!-- -->

-   Step 3. Flashing image

1.  Execute tizen-download in a console on the Linux PC as follows, make
    sure you\'re running tizen-download in 32-bit environment:

<!-- -->

     $ sudo ./tizen-download -u https://secured-download.tizen.org/references/1.0/ \
       s-boot-mmc.bin u-boot-mmc.bin uImage modules.img platform.img data.img ums.img

-   Step 4. Wait until all files are downloaded on to the phone.

The phone will be automatically rebooted after successful downloading.

Tips
----

### ssh into target device(USB Debugging Mode)

Once the phone is flashed and booted up. Choose the usb mode to \"USB
debugging\" by doing this:

`Settings ->`\
`Press "All" to show all the settings items ->`\
`"USB utilities" ->`\
`Choose "USB debugging"`

Then the device will export a usbnet device, it\'s addr: 192.168.129.3

<b>(In your host)</b> configure your ip address of usb0:

`# ifconfig usb0 192.168.129.4`

Then you can ssh into the target device (root, pwd: tizen):

`# ssh root@192.168.129.3`

### ssh into target device(Using SDB)

With Tizen SDK properly installed and \"sdb\" is on your path
environment variable,

`# sdb -d shell`

More
----

-   <http://tizentalk.com/forum/threads/questions-about-the-dev-phone.17/#post-124>
-   <https://wiki.tizen.org/wiki/Flash_Tizen_2.2_Image_to_Reference_Device>

[Category:Tool](Category:Tool "wikilink")
[Category:Hardware](Category:Hardware "wikilink")
