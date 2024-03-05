![SD-MUX](Sdmux-v1.png "SD-MUX"){width="700"}

Overview
========

**SD MUX** stands for Secure Digital Multiplexer. This is a custom board
designed to aid operation of [test lab device](Laboratory "wikilink").
The device was meant to be a simple switch for SD memory cards. It was
to switch the card either to DUT (Device Under Test) or to TS (Test
Server). The main purpose of that was possibility to write image to SD
card and then boot tested device from this card without any manual
activity. Tested devices usually have micro SD card slot and test server
need to have micro SD card reader (usually connected over USB). So the
memory card must be connected once to the slot of a DUT and once to the
reader of a TS. To achieve such goal we could see three possible
solutions:

-   A kind of robot taking out the the card out of USB reader and
    putting it into device\'s slot, and in reverse
-   SD memory card emulator
-   SD card multiplexer able to connect the card to one of two devices
    at the same time

**The first solution (the robot)** seems to be good project for CNC
maniacs but not for this task. It is hard to build such contraption,
hard to program it and hard to maintain. Unquestionable advantage of
such approach is that only one such robot is enough for the whole test
lab.

**Second solution (emulator)** would have been very good one if it had
existed. At the time we were facing the problem there was no any
emulator market and probably still isn\'t. Killer feature of emulator is
that there is no way to wear it out like physical ones. As history shows
SD cards wear out quite fast. After few hundreds flashes they become
worn out. But the problem of SD emulator is that requires a lot of fast
memory, usually RAM, and this inconvenience rules out this approach.

**And finally third solution (multiplexer)** seems to be the obvious
choice. In comparison to robot and emulator it is easy to design and
build it, and it is quite cheap.

Hardware design
===============

SD-MUX was designed entirely in [KiCad](http://kicad-pcb.org/) a free
tool for hardware design. Project files are published on Tizen git
server. It is open-hardware device and everyone is welcome to comment
and make contributions to this project.

Main board
----------

Currently, version 2nd of sd-mux is in use. The differences between 1st
and 2nd are:

-   First version had full SD card slot while second revision has micro
    SD slot which let to reduce the size of PCB.
-   First version didn\'t have switch on USB-A ports. Second version is
    able turn on and off power which helps TS to discover
    (dis)connecting micro SD card reader.
-   Dimensions of first revision were 150x50mm while of the second one
    are 114x50mm.

Below pictures show the first and the second version of SD-MUX.
![Alt=Akuku Panie Kruku\|The first version of SD-MUX
board](sd-mux-v1.jpg "fig:Alt=Akuku Panie Kruku|The first version of SD-MUX board")
![Alt=Akuku Panie Kruku\|The second version of SD-MUX
board](sd-mux-v2.jpg "fig:Alt=Akuku Panie Kruku|The second version of SD-MUX board")

Cable
-----

Micro SD card slot of tested devices and USB card reader are connected
to SD-MUX board through a flat cable. The cable is soldered to dedicated
micro sd adapter on one side and crimped to 2x4 IDC connector on the
oder side. ![Alt=Akuku Panie Kruku\|Micro SD adapter \<-\> SD-MUX
cable](cable.jpg "fig:Alt=Akuku Panie Kruku|Micro SD adapter <-> SD-MUX cable")
The adapter is made of thin (0.8mm), one-sided PCB coated with gold. It
has exact shape of micro sd card. ![Alt=Akuku Panie Kruku\|Micro SD
adapter](adapter.jpg "fig:Alt=Akuku Panie Kruku|Micro SD adapter") Two
pieces of such cable are used per one SD-MUX board. One of them connects
SD-MUX to tested device and the second one connects SD-MUX to micro sd
usb card reader.

DyPer
-----

DyPer (DYNamic jumPER) is a simple low-current switch which may be
controlled via SD-MUX. This is another electromagnetic relay (for the
same reasons as in SD-MUX) which may be used for connecting two signals.
These signals might be configuration pins, normally connected using
standard jumper, or reset input of device or any other low current
signals. Such functionality might be needed for example on board which
cannot be rebooted only by switching its power supply. Example of such
board is Artik development board. This feature is made as an add-on for
SD-MUX board. SD-MUX is not prepared for add-ons so it has not any
dedicated connector or mechanical slots thus DyPer must be glued to
SD-MUX and its wires must be directly soldered to FTDI chip of SD-MUX.
DyPer is very simple circuit and it does not require any pcb. Currently
we use only two such devices so we didn\'t need to make pcbs. It
consistsof four elements: relay, N-MOS transistor, diode and pull-up
resistor. All of them are soldered together without any PCB. ![Dyper
schematic](Dyper-sch.png "fig:Dyper schematic") One channel is able to
connect two independent signals at the same time. Both of these signals
are controlled by one steering signal. Such approach might be helpful
when two unrelated jumpers must be switched on. It doesn\'t happen very
frequently but it happens. One complete DyPer may be used to switch two
pairs of such signals and each pair may be controlled independently as
there are two independent steering signals per each channel.

FAQ
---

Q: Why did you use electromagnetic relay?

A: Electromagnetic relay is used for ensuring that there is no any
relation between steering and operating signals. Semiconductor relays
have such relations and we didn\'t want to depend on it as we didn\'t
know what kind of power supply would be used for particular device
board.

Q: Why did you use such large relay?

A: We did want to use bistable relays as they don\'t get power for coil
when are in stable state. Also we did want relays with two coils as it
is much easier to steer the relay with one coil. Putting these
conditions together the answer is very prosaic. We bought what we could
:) Of all accessible (in stores those days) relays only this one met the
requirements.

Software
========

SD-MUX has dedicated software which is a simple tool meant to control
the hardware. Source code of the tool is published on [tizen
git](https://git.tizen.org/cgit/tools/testlab/sd-mux/) server.

This is simple to use, command-line utility software written in C and
based on open-source libFTDI library. It has dedicated [ manual
page](SD_MUX/manpage "wikilink") and bash completion script.

First use
---------

If SD-MUX comes preconfigured then there is no need to perform action in
this section. To check whether the device is configured or not just run:

`sudo  sd-mux-ctrl --list`

If the device is connected and configured then it will be shown in the
output. It means it can be used without any configuration right now.

Otherwise if the device is connected and not shown in the list then the
first configuration has to be done before it can be used. A valid serial
number, device type, VENDOR ID and PRODUCT ID of the device must be set.

Devices of SD-MUX family are built with FTDI chips so their initial
VENDOR and PRODUCT IDs has to be used to identify them. First of all
disconnect all FTDI devices from USB host machine. Then connect one of
your new SD-MUXes and execute:

`sudo sd-mux-ctrl --list --vendor=0x0403 --product=0x6001`

Use demsg or lsusb output to get vendor and product numbers because
product number might differ for different devices from SD-MUX family.
Currently PRODUCT ID is 0x6001 (SD-MUX, SDWire) or 0x6015 (USB-MUX) NOTE
that at this moment there must not be connected any other device with
such vendor ID and product ID 6001 (0403:6001) ex. FTDI USB\<-\>UART
converters! Otherwise one will not be able to tell which device is the
one he is interested in.

Above command will give all devices with ID 0403:6001 and there should
be only one such device. Again, pay attention not to connect anything
else with such ID. At this point one can set new serial number. At the
same time, sd-mux-ctrl will set vendor ID to the new one (0x04e8 -
Samsung ID). Product ID will be set to 0x6001.

`sudo sd-mux-ctrl --device-serial=AL018T40 --vendor=0x0403 --product=0x6001 --device-type=sd-mux --set-serial=odroid_u3_1`

Where AL018T40 is the serial number read from result of \--list command
and odroid\_u3\_1 is the new serial number. From this moment \--vendor
or \--product option must not be used when \"talking\" to the device. Of
course \--vendor=0x04e8 might be used but there is no use to do that
because 0x04e8 is the default value. From now on the device is ready to
operate along with the software as a part of automated laboratory.

Everyday use
------------

Typical scenario is:

1.  Disconnect power supply from device under test
2.  Disconnect micro SD card from DUT and connect it to TS
3.  Disconnect USB port from DUT and connect it to micro SD card reader
4.  Flash SD card with new image
5.  Disconnect SD card from TS and connect it to DUT
6.  Connect USB port to USB OTG on DUT board to establish SDB connection
7.  Connect power supply to DUT
8.  If needed do extra power supply tick (for example needed by Odroid
    U3 devices)
9.  Wait for coming up of the tested device (SDB connection active) and
    if it hasn\'t happened, repeat the whole procedure.

Steps 1 & 2 & 3 can be done with one command. Steps 5 & 6 & 7 can be
done with one command.

Above procedure (steps 1 - 7) can be done as follows:

`sudo sd-mux-ctrl --device-serial=odroid_u3_1 --ts`\
`... - do the flashing things`\
`sudo sd-mux-ctrl --device-serial=odroid_u3_1 --dut`

And potential extra reset by power switch:

`sudo sd-mux-ctrl --device-serial=odroid_u3_1 --tick`

Files
=====

<span style="color:red">NOTE! Don\'t build the device. It has design
flaw in SD card power switching circuitry. It can power up DUT even if
TS side is selected. Also TS is powered if DUT side is the active one.
Proper fix is applied to SDWire and MuxPi but not yet in SD-MUX.</span>

-   Main board schematic: ![](Sdmux.pdf "fig:Sdmux.pdf")
-   Main board fabrication files:
    [sd-mux-fabrication-v2\_1.zip](https://git.tizen.org/cgit/tools/testlab/sd-mux/plain/doc/hardware/fabrication/sd-mux-fabrication-v2_1.zip)
-   Micro SD card adapter fabrication files:
    [usd-adapter-v1.zip](https://git.tizen.org/cgit/tools/testlab/sd-mux/plain/doc/hardware/fabrication/usd-adapter-fabrication-v1.zip)
-   The hardware and software sources: [SD-MUX on
    Tizen](https://git.tizen.org/cgit/tools/testlab/sd-mux/)

[Category:Tool](Category:Tool "wikilink")
[Category:Testlab](Category:Testlab "wikilink")
[Category:Hardware](Category:Hardware "wikilink")
[Category:Common](Category:Common "wikilink")
