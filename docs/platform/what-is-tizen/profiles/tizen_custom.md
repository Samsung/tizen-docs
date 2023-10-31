# Tizen Custom Devices

Tizen  allows developers to make various kinds of Tizen devices and develop applications for the devices.
Tizen Headed and Headless binaries support any type of devices based on the Linux kernel.

## Development environment for Tizen custom device
Tizen supports the following environment for development:
- Hardware targets
    - Raspberry Pi 4 as the official reference boards
- Platform images
    - Headless image for Tizen devices without a display
    - Headed image for Tizen devices with a display

## Develop applications for Tizen custom device
To develop applications for Tizen custom device, refer to the following:
- [Create Your First Tizen .NET Application](../../../application/dotnet/get-started/first-app.md)
- [Create Your First Tizen Native Service Application](../../../application/native/get-started/iot/first-app.md)

## Create Tizen custom images
Tizen provides a building block pool of components mainly based on the [Tizen Native API sets](../../../application/native/api/iot-headed/latest/index.html)

**Building block presets for Tizen core:**
- The minimum set of bootable modules that make up the Tizen platform image for Tizen devices.
- The preset contains core components that are required for a basic system image to boot.

**Building block presets for Headless:**
- The set of modules that make up the Tizen platform image for headless Tizen devices without a display.
- The preset contains Tizen core presets with other components specifically required for headless images.
- Example of specific components for a headless image includes Audio modules, Bluetooth modules, and so on.

**Building block presets for Headed:**
- The set of modules that make up the Tizen platform image for headed Tizen devices with a display.
- The preset contains Tizen core presets with other components specifically required for headed images.
- Example of specific components for a headed image includes Notification API, graphic modules, and so on.

Tizen custom images can be created by combining API building blocks in various ways as per the requirements. Required packages are installed based on the dependencies related to the specified building blocks.

![tizen_building_block](media/iot_building_block_new.png)

To create images for custom tizen device, refer to the following:
- [Creating Tizen Images with MIC](../../developing/creating.md)
- [Creating Tizen Images with TIC](../../developing/creating-tic.md)
