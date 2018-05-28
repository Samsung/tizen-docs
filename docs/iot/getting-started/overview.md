# Tizen IoT

Tizen is commercialized for smart TV, smart phone, smart watch, and smart home appliances with three profiles: TV, mobile, and wearable. Tizen IoT supports any type of special-purpose IoT devices based on the Linux kernel.

Tizen IoT Preview 2 is released from Tizen Studio 2.3. Tizen IoT Preview 1 was the first preview release of Tizen for the development of IoT devices, which are connected easily and securely with legacy IoT ecosystems such as SmartThings&trade;. In addtion to the features of Tizen IoT Preview 1, Tizen IoT Preview 2 provides the customized platform features and the support for ARTIK 530s. Tizen IoT Preview 2 consists of platform images, development environments, samples for getting started, and customized platform.

-   Hardware targets: Raspberry Pi 3, ARTIK 530, and ARTIK 530s are supported as reference hardware.

-   Platform image
    -   Headless: Platform image for headless-type IoT devices without a display. In IoT Preview 2, Raspberry Pi 3, ARTIK 530, and ARTIK 530s can be used with the headless platform image.

    -   Headed: Platform image for headed-type IoT devices with a display. In IoT Preview 2, ARTIK 530 and ARTIK 530s can be used with the headed platform image.

-   Development environment

    -   IoT Setup Manager: The IoT Setup Manager is a computer application for easily setting up Tizen IoT on hardware targets. (In IoT Preview 1, it was IoT Setup Wizard.) In Preview 2, flashing a platform image into an SD card for Raspberry Pi 3 and ARTIK 530 is supported with the IoT Setup Manager for both Linux and Windows computer environments.

    -   Tizen Studio 2.0 (or higher) is used as the IDE for developing IoT applications with the Tizen IoT Platform on Raspberry Pi 3, ARTIK 530, and ARTIK 530s.

    -   [IoT API](../guides/iot-api.md)
        -   Things SDK for SmartThings&trade;: Using Things SDK API for [SmartThings&trade;](https://smartthings.developer.samsung.com/), you can create your IoT devices with the SmartThings Cloud. The Things SDK API enables you to integrate, control, and monitor your IoT devices through the SmartThings Cloud with the SmartThings application.

        -   Peripheral I/O: Using the Tizen Peripheral I/O Native API for IoT devices, you can control peripherals, such as sensors and actuators, using industry-standard protocols and interfaces.

    -   [Craftroom](https://craftroom.tizen.org/): Craftroom is a new website for creating your own development community using a Tizen platform image. Craftroom can generate a new platform image by adding IoT applications made in the Tizen Studio. It provides a new functionality by combining Tizen packages, and allows you to create a new customized Tizen platform image for IoT devices in the next platform release.

    To get started with developing your own Tizen IoT applications:

    1.  [Install Tizen Studio](tizen-studio-install.md).
    2.  [Flash a Tizen image](tizen-image-download-flash.md).
    3.  [Set up the hardware](hardware-configuration.md).
    4.  [Develop an application](things-app-development.md).
    5.  [Set up the SmartThings Cloud](things-cloud-setup.md).
    6.  [Test the application with SmartThings app](cloud-app-test.md).
-   [Samples](../sample/iot-sample.md): In Tizen IoT Preview 1 and 2, currently only the network audio sample application is supported. The number of online samples is set to extend in the future.

-   [Customized Platform Guide](../customized-platform/overview.md): New feature in Tizen IoT Preview 2. This feature helps the developers to create a customized platform image and selectively aggregate features and set of Tizen platform APIs.

