# Flashing an Image to Device

The instructions for flashing depend on the type of device you are using. Instructions are available for the following devices:
- TM1 reference device

To flash the Tizen image to the TM1 reference device:

1. Boot the device into download mode:

   1. Make sure the device is powered off.
   1. Press the **Volume down**, **Home**, and **Power** keys simultaneously.  
      The device boots up and the download mode image is displayed on the screen.

1. Connect the device to the Linux PC with a USB cable.

1. Flash the image.

   To flash the image, execute the `lthor` command in a console on the Linux PC:
   ```bash
   $ sudo ./lthor TM1-201609030819.tar.gz
   ```

1. Wait until files are downloaded on to the device. The device is automatically rebooted after a successful download.

> **Note**
>
> Tizen images of version 2.4 and higher do not contain the TM1-hardware-dependent binaries by default. To make TM1 function correctly, you must install the additional binaries manually. For more information, see [Tizen Device Firmware](http://developer.samsung.com/tizendevice/firmware).
