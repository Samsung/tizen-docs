# Flash an Image to RPI

This topic describes how to flash Tizen on an SD card and setting up Raspberry Pi 4.
> [!NOTE]
> Raspberry Pi 3 was not supported since Tizen 8.0. Raspberry Pi 5 (64bit-only) can be using for experimental.

## Supported systems

|Division	|Ubuntu	|Windows	|
|:---:		|:---:	|:---:		|
|Headless 32-bit|Yes	|No			|
|Headless 64-bit|Yes	|No			|
|Headed 32-bit|Yes	|No		|
|Headed 64-bit|Yes	|No			|

## Prerequisites

### Operating system

Ubuntu 18.04 LTS and later (Recommended to use Ubuntu 20.04 / 22.04)

### Update EEPROM on RPi target

Tizen is using GPT partition since Tizen 7.0. It has to update the EEPROM that is supported GPT partition.
   > [!IMPORTANT]
   > (If eeprom is upper than 2022.04.26 version, This step can be optional.)

1.  Refer to https://github.com/raspberrypi/rpi-eeprom/releases

### Download binaries

You must have the supported binary images in your computer. To download the binary images, follow these steps:

1. Download images from [Downloads](http://download.tizen.org/releases/milestone/TIZEN){:target="_blank"}.
2. Select **Tizen-9.0 (or "Tizen" whichever is present) > Tizen-9.0-Unified (or "Tizen-unified" whichever is present) > latest > images > standard**.
3. Download the compressed file for different devices or profiles from:


     -   RPI4 Headless 32-bit:
          -   Boot Image: tizen-boot-armv7l-rpi4/
          -   Platform Image: tizen-headless-armv7l/

     -   RPI4 Headless 64-bit:
          -   Boot Image: tizen-boot-arm64-rpi4/
          -   Platform Image: tizen-headless-aarch64/

     -   RPI4 Headed 32-bit:
          -   Boot Image: tizen-boot-armv7l-rpi4/
          -   Platform Image: tizen-headed-armv7l/

     -   RPI4 Headed 64-bit:
          -   Boot Image: tizen-boot-arm64-rpi4/
          -   Platform Image: tizen-headed-aarch64/


### Flash through the command line

You can flash the SD card through the command line on a Linux computer.
To flash the SD card for Raspberry Pi 4 or 5, follow the steps below:

1.  Complete the following prerequisites:
    1.  Install the `pv` package in the Linux computer:

        ```
        $ sudo apt-get install pv
        ```

    2.  Ensure that you have an SD card of 16 GB or more.
    3.  Verify whether the binary image files are in your computer.
    4.  Fusing-script for Raspberry Pi 4 (fusing script is same for RPI5):

        ```
        $ wget https://git.tizen.org/cgit/platform/kernel/u-boot/plain/scripts/tizen/sd_fusing.py?h=tizen --output-document=sd_fusing.py
        $ chmod +x sd_fusing.py
        ```

2.  Flash the SD card to ensure it is ready to be used for Tizen:
    1.  Insert an SD card to the Linux computer and verify its device node.
        > [!WARNING]
        > It MUST check the device node of SD-card  on host PC side. Otherwise, other block device can be formatted.
        > Follow the below step. To verify the device node:
        >
        > 1.  Run the following command before inserting the SD card into the Linux computer:
        >
        >     ```
        >     $ ls -al /dev/sd*
        >     ```
        >
        >     For example:
        >
        >     ```
        >     $ ls -al /dev/sd*
        >     brw-rw---- 1 root disk 8, 0  9 18 09:08 /dev/sda
        >     brw-rw---- 1 root disk 8, 1  9 18 09:08 /dev/sda1
        >     brw-rw---- 1 root disk 8, 2  9 18 09:08 /dev/sda2
        >     brw-rw---- 1 root disk 8, 5  9 18 09:08 /dev/sda5
        >     ```
        >
        > 2.  Insert the SD card and type the same command again:
        >
        >     ```
        >     $ ls -al /dev/sd*
        >     ```
        >
        >     For example:
        >
        >     ```
        >     $ ls -al /dev/sd*
        >     brw-rw---- 1 root disk 8,  0  9 18 09:08 /dev/sda
        >     brw-rw---- 1 root disk 8,  1  9 18 09:08 /dev/sda1
        >     brw-rw---- 1 root disk 8,  2  9 18 09:08 /dev/sda2
        >     brw-rw---- 1 root disk 8,  5  9 18 09:08 /dev/sda5
        >     brw-rw---- 1 root disk 8, 16  9 22 14:59 /dev/sdb
        >     brw-rw---- 1 root disk 8, 17  9 22 14:59 /dev/sdb1
        >     brw-rw---- 1 root disk 8, 18  9 22 14:59 /dev/sdb2
        >     brw-rw---- 1 root disk 8, 19  9 22 14:59 /dev/sdb3
        >     brw-rw---- 1 root disk 8, 20  9 22 14:59 /dev/sdb4
        >     brw-rw---- 1 root disk 8, 21  9 22 14:59 /dev/sdb5
        >     brw-rw---- 1 root disk 8, 22  9 22 14:59 /dev/sdb6
        >     brw-rw---- 1 root disk 8, 23  9 22 14:59 /dev/sdb7
        >     ```
        >
        >     The new `sdX` node (where X is a letter) is the device node for the SD card.
        >
        >     In this example, the device node for the SD card is `sdb`.

	2.  [Download](#download-binaries) compatible boot and platform image according to target device.
	3.  Run the following commands:

        ```
        $ sudo ./sd_fusing.py -d <SD card device node> -t <Target Board> --format
        $ sudo ./sd_fusing.py -d <SD card device node> -b <Boot Image> <Platform Image> -t <Target Board>
        ```

        For example:

        ```
        $ sudo ./sd_fusing.py -d /dev/sdb -t rpi4 --format
        $ sudo ./sd_fusing.py -d /dev/sdb -b tizen-unified_20241125.014042_tizen-boot-armv7l-rpi4.tar.gz tizen-unified_20241125.014042_tizen-headed-armv7l.tar.gz -t rpi4
        ```

3.  Open the Smart Development Bridge (SDB) connection. For more information, see [Set up Raspberry Pi 4](#set-up-raspberry-pi-4).

    > [!NOTE]
    > Repeat `sdb connect 192.168.1.11` in the Linux shell (Linux) or the command window (Windows) whenever you power cycle the device, in order to reconnect the SDB tool.

## Set up Raspberry Pi  4

### Connect the board to the PC

To configure the Raspberry Pi board, follow the steps below:

1.  Insert the SD card, in which Tizen Platform binaries and the drivers are flashed into the Raspberry Pi board.
2.  For the serial communication connection:
    1.  Connect the host computer to the Raspberry Pi with a **UART-to-USB** dongle such as PL2303 or FT232 USB UART board.

        To use the PL2303, connect the Raspberry Pi TXD0 pin (pin 8) to RXD on the UART board, RXD0 (pin 10) to TXD on the UART board, and the ground (pin 6) to GND on the UART board, and set the jumper switch to 3.3V (pin 1).

        > [!NOTE]
        > Before using a UART-to-USB dongle, familiarize yourself with any hardware limitations it has by visiting the manufacturer's website.

    2.  Execute a terminal program such as Minicom or PuTTY.

        -   Minicom example:

            Minicom can be used in Linux computer. Run the following command to run Minicom:

            ```
            $ sudo minicom -c on
            ```

            To configure Minicom:

            1.   Go to the Minicom configuration settings menu by consecutively pressing `Ctrl + A`, `Z`, and `O` (the letter O).
            2.  In the `Serial Device` field, set the correct USB port for serial communication. The format is `/dev/ttyUSBX` where `X` equals the number of the port.
            3. Modify the `Hardware Flow Control` field to `No`.

            ```
            +-----------------------------------------------------------------------+
            | A -    Serial Device      : /dev/ttyUSBX                              |
            | B - Lockfile Location     : /var/lock                                 |
            | C -   Callin Program      :                                           |
            | D -  Callout Program      :                                           |
            | E -    Bps/Par/Bits       : 115200 8N1                                |
            | F - Hardware Flow Control : No                                        |
            | G - Software Flow Control : No                                        |
            ```

            In the serial shell, log in with `root/tizen`:

            ```
            localhost login: root
            Password: tizen
            Welcome to Tizen
            ```

        -   PuTTY example:

            Download PuTTY from the Internet and launch PuTTY.

            ![PuTTY Config](media/putty_config.png)

            To configure PuTTY, follow the steps below:

            1.   Select `Serial` connection type.
            2.   Enter the serial line number for the board connected to your computer (it can be COM`N` where `N` is a natural number such as COM1, COM4, and so on) in the `Serial line` field.
            3.   Type 115200 in the `Speed` field.
            4.   Click `Open`.

            In the serial shell, log in with `root/tizen`:

            ```
            localhost login: root
            Password: tizen
            Welcome to Tizen
            ```

3.  For the SDB connection:
    1.  Connect the host computer to the Raspberry Pi through an Ethernet cable.

        > [!NOTE]
        > If Ethernet ports are not available in the host computer or the Raspberry Pi, you can also use an `Ethernet-to-USB` dongle.

    2.  Set a new network interface in the host computer as shown in the following figures. This is a one time activity:

         -   Linux computer.

             ![Linux Network Configuration](media/network_setting.png)

         -   Windows computer.

             ![Windows Network Configuration](media/win_net_config.png)

         If you are using the **Ethernet-to-USB** dongle, you must install the proper driver for the dongle. If the network cable is connected correctly, you can find a new connection in Network and Sharing Center. In the new connection, enter the properties of IPv4, and configure as shown in the Windows computer figure.

4.  Verify the IP address for eth0.

    ```
    ifconfig
    ```

    If the IP address for eth0 is 192.168.1.11, go to step 5. If not, set an IP address for the SDB connection in the serial shell of the Raspberry Pi using the `ifconfig` command:

    ```
    ifconfig eth0 192.168.1.11
    ```

5.  Connect Smart Development Bridge (SDB) in the Linux shell (Linux) or Command window (Windows) of the host computer:

    ```
    sdb connect 192.168.1.11
    sdb root on
    ```

    For example, for Linux computer:

    ```
    ~$ sdb connect 192.168.1.11
    * server not running. starting it now on port 26099 *
    * server started successfully *
    connecting to 192.168.1.11:26101 ...
    connected to 192.168.1.11:26101
    ~$ sdb root on
    Switched to 'root' account mode
    ~$
    ```

6.  Enter the `sdb help` command in the Linux shell (Linux) or Command window (Windows) of the host computer, for more information.

    > [!NOTE]
    > `sdb` execution file is available in the `tools` sub-directory of the directory where Tizen Studio is installed.


### Install drivers

1.  Connect Smart Development Bridge (SDB) as described in [Connect the board to the PC](#connect-the-board-to-the-pc).
2.  Install the connectivity drivers for each board:
    -   **Raspberry Pi 4**
        1.  Download the plugin zip file from the **Raspberry Pi 4(9.0) Plugin** section at [Tizen Device Firmware](http://developer.samsung.com/tizendevice/firmware){:target="_blank"} and follow the instructions.

        2.  For the case of the Linux shell (Linux), run the `sh` script given in the instructions. For example:

            ```
            $ ./install_with_SDB.sh
            ```

## Set up Wi-Fi

This section is not applicable if you want to connect your device to the SmartThings Cloud. In case of SmartThings devices, the device enables SoftAP mode during setup. Therefore, you need not switch to Wi-Fi separately.

You can set up a Wi-Fi connection by running `wifi_manager_test` and entering the options `1 > 3 > 9 > b > c`. If you set up the connection once, it reconnects automatically the next time you power cycle the device.

```
# wifi_manager_test
Test Thread created...<Enter>
Event received from stdin
Network Connection API Test App
Options..
1   - Wi-Fi init and set callbacks
2   - Wi-Fi deinit(unset callbacks automatically)
3   - Activate Wi-Fi device
4   - Deactivate Wi-Fi device
5   - Is Wi-Fi activated?
6   - Get connection state
7   - Get MAC address
8   - Get Wi-Fi interface name
9   - Scan request
a   - Get Connected AP
b   - Get AP list
c   - Connect
d   - Disconnect
e   - Connect by wps pbc
f   - Forget an AP
g   - Set & connect EAP
h   - Set IP method type
i   - Set Proxy method type
j   - Get Ap info
k   - Connect Specific AP
l   - Load configuration
m   - Save configuration
n   - Remove configuration
o   - TDLS Discover
p   - TDLS Connect
q   - TDLS Connected peer
r   - TDLS Disconnect
s   - Connect Hidden AP
t   - Connect WPS PBC without SSID
u   - Connect WPS PIN without SSID
v   - Cancel WPS Request
w   - Set Auto Scan Enable-Disable
x   - Set Auto Scan Mode
y   - Get wifi scanning state
z   - Get Auto Scan Enable-Disable
A   - Get Auto Scan Mode
B   - Enable TDLS Channel Switch Request
C   - Disable TDLS Channel Switch Request
D   - Get Wi-Fi Module State
E   - BSSID Scan
F   - Add VSIE
G   - Get VSIE
H   - Remove VSIE
I   - Start Multi Scan
J   - Flush BSS
K   - Set auto connect mode
L   - Get auto connect mode
0   - Exit
ENTER  - Show options menu.......
Operation succeeded!
1
Event received from stdin
Wifi init succeeded
Operation succeeded!
3
Event received from stdin
Wi-Fi Activation Succeeded
Operation succeeded!
9
Event received from stdin
Interface name : wlan0
Operation succeeded!
b
Event received from stdin
AP name : crash_messaging, state : Disconnected
AP name : dnet1, state : Disconnected
... < list of APs > ...
Get AP list finished
Operation succeeded!
Background Scan Completed, error code : NONE
c
Event received from stdin
Input a part of AP name to connect : <AP name>
Passphrase required : TRUE
Input passphrase for dnet1 : <Password>
```

