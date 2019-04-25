# Tizen IoT

Tizen is commercialized for smart TV, smart phone, smart watch, and smart home appliances with three profiles: TV, mobile, and wearable. Tizen IoT Headed and Headless binary support any type of special-purpose IoT devices based on the Linux kernel. Tizen IoT Extension SDK supports for the developers to develop an application running on the Tizen IoT Headed and Headless binary. Also, using Tizen IoT extension SDK, the developers can develop the IoT devices which are connected easily and securely with legacy IoT ecosystems such as SmartThings&trade;. 

Tizen IoT Extension SDK version 1.0 is released from Tizen Studio 3.0 for Tizen 5.0. The following features are supported:

-   Hardware targets: ARTIK 530 and ARTIK 530s are supported as the official reference hardwares.Raspberry Pi 3 is also supported

-   Platform image
    -   Headless: Tizen 5.0 platform image for headless-type IoT devices without a display. Raspberry Pi 3, ARTIK 530, and ARTIK 530s can be used with the headless platform image.

    -   Headed: Tizen 5.0 platform image for headed-type IoT devices with a display. ARTIK 530 and ARTIK 530s can be used with the headed platform image.

-   Development environment

    -   IoT Setup Manager: The IoT Setup Manager is a computer application for easily setting up Tizen IoT on hardware targets. Both Linux and Windows computer environments are supported. 

    -   Tizen Studio 3.0 (or higher) is used as the IDE for developing IoT applications with the Tizen IoT Platform on Raspberry Pi 3, ARTIK 530, and ARTIK 530s.

    -   [IoT API](../guides/iot-api.md)
        -   Things SDK for SmartThings&trade;: Using Things SDK API for [SmartThings&trade;](https://smartthings.developer.samsung.com/), you can create your IoT devices with the SmartThings Cloud. The Things SDK API enables you to integrate, control, and monitor your IoT devices through the SmartThings Cloud with the SmartThings application. 

        > **Note**
        >
        > that the API set for Tizen IoT Extension SDK version 1 for Tizne 5.0 is not compatable to the API set for Tizen IoT Preview 2 for Tizen 4.0.

        -   Peripheral I/O: Using the Tizen Peripheral I/O Native API for IoT devices, you can control peripherals, such as sensors and actuators, using industry-standard protocols and interfaces.

    To get started with developing your own Tizen IoT applications:

    1.  [Setup the board](setting-up-board.md).
    2.  [Develop an application](things-app-development-5.0.md).
    3.  [Set up the SmartThings Cloud](things-cloud-setup.md).
    4.  [Test the application with SmartThings app](cloud-app-test.md).

Tizen IoT Preview 2, which has been released from Tizen Studio 2.3, is also supported in Tizen Studio 3.0. For details of Tizen IoT Preview 2, see [Tizen IoT Preview 2.](../preview2/getting-started/overview.md)


