# Flashing an Image to Device

The instructions for flashing depend on what type of device you're using.
Instructions are available for the following devices:
- TM1 Reference Devices

## Flashing the Tizen image

**1. Boot the phone into download mode.**

1. Make sure the phone is powered off.
2. Press <volume down> + <home> + <power> keys simultaneously.
   The phone boots up and the download mode image is displayed on the phone.

**2. Connect the phone to the Linux PC with a USB cable.**

**3. Flash the image.**

Execute lthor in a console on the Linux PC as follows.
```bash
$ sudo ./lthor TM1-201609030819.tar.gz
```

**4. Wait until files are downloaded.**

Wait until all files are downloaded on to the phone. The phone is automatically rebooted after a successful download.

NOTE: The Tizen 2.4 and higher images don't contain the TM1-hardware-dependent binaries. You must install the additional binaries in order to make TM1 function correctly. For more information, see **[Tizen Device Firmware](http://developer.samsung.com/tizendevice/firmware)**
