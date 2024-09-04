![SDWire](SDWire.png "SDWire"){width="700"}

Overview
========

**SDWire** is a small board with 2 features:

-   SD card reader
-   SD card MUX

There is only one micro USB socket for connecting to host PC. Both USB
mass storage and MUX control are served through the same USB connection.

The PCB board is designed in such way that it fits into micro SD card
slots. Thanks to this, there is no need for special cables with micro SD
adapter and connection to SD slot on a device is very short.

Hardware design
===============

Design of this board is based on [SD MUX](SD_MUX "wikilink"). SDWire
does not have power switch or USB switch but has built in USB SD card
reader. SD card multiplexer itself is exactly the same in both devices.

There are four LEDs on the board:

-   red - power presence from USB
-   blue - USB reader activity
-   blue - card connected to TS
-   green - card connected to DUT

All LEDs are present on both sides of the board to make them visible no
matter which side of the board will be facing you.

LED positions are showed in the image below.

![](SDWire-leds.png "SDWire-leds.png")

The PCB board has to be 0.8 mm thick to make it possible to put it into
standard micro SD card socket.

Version 1.4
-----------

In this version, SDWire is equipped with EEPROM connected to USB2640 IC.
It enables user to change serial number of this IC. This in turn makes
it possible to distinguish one SDWires from another. This is very useful
in automated systems where more than one SDWire is used in one USB host.
Without this EEPROM each device has the same serial number which does
not allow to tell which USB card reader is connected to which device.
Using simple UDEV rules and unique serial numbers solves the problem.

Software
========

There are two USB interfaces (physically one connection):

-   USB mass storage - which support is built in every modern operating
    system.
-   control interface - which allows to control SD MUX functionality.
    This interface is handled with exactly the same software
    (sd-mux-ctrl) which is used for SD MUX. Go to [SD MUX
    software](SD_MUX#Software "wikilink") for details.

Version 1.4
-----------

In this version we can use EEPROM memory to distinguish SDWire devices
form each other. But before that the unique serial number has to be set.
The only known method is to use USBDM software form Microchip company.
It is Windows software that can be downloaded from here:
<http://ww1.microchip.com/downloads/en//softwarelibrary/usbdm%20tool/usbdm.zip>

Update of the serial number is quite a straightforward process. Just
install the tool and run it. Connect SDWire and when you see its
information on the \"Info\" tab, switch to \"Branding\" tab, change
\"Serial Number String\" to whatever you want and fits requirements and
then click \"Update Now\" button. After few seconds tab \"Info\" should
automatically become active and the new serial number should appear.

Note: On Windows 10 it might be a little bit hard to find the tool
location after installation. If yes then try to find it in following or
similar location: C:\\ProgramData\\Microsoft\\Windows\\Start
Menu\\Programs\\USBDM\\USBDM.exe

Files
=====

-   Main board schematic:
    ![](SDWire-v1.4-sch.pdf "fig:SDWire-v1.4-sch.pdf")
-   Main board PCB fabrication files:
    [SDWire-fabrication-v1.4.zip](https://git.tizen.org/cgit/tools/testlab/sd-mux/plain/doc/hardware/SDWire/SDWire-fabrication-v1.4.zip)
-   Main assembly files:
    [SDWire-assembly-v1.4.zip](https://git.tizen.org/cgit/tools/testlab/sd-mux/plain/doc/hardware/SDWire/SDWire-assembly-v1.4.zip)
-   The hardware and software sources: [SD-MUX on
    Tizen](https://git.tizen.org/cgit/tools/testlab/sd-mux/)

Known problems
==============

First revision of the device was built on a 2-layer PCB. In most cases
it worked fine but there were devices that couldn\'t write to micro SD
card - a lot of I/O errors would happen. On-board USB SD card reader
worked flawlessly in both reading and writing modes. The problem was
related to external devices into which SDWire was inserted. In order to
overcome the problem the PCB was redesigned and 4 layer stack was used.
Now devices that couldn\'t write to SD card can do it without a problem.
However I didn\'t test SDWire with all existing readers, devices or
micro SD cards.

**Note**: SDWire is a device that uses analog multiplexer to switch SD
signals either to integrated reader or external device. It means that
the signals are slightly degraded and this can cause some compatibility
problems between SD card and external device. All depends on quality of
card, device, clock speed, signal levels, etc. You have take into
consideration that kind of problems.

Above problem applies to SD-MUX and MuxPi as well. However, it can be
usually solved by changing micro SD card to one which works fine with
multiplexer and the device.

[Category:Tool](Category:Tool "wikilink")
[Category:Testlab](Category:Testlab "wikilink")
[Category:Hardware](Category:Hardware "wikilink")
[Category:Common](Category:Common "wikilink")
