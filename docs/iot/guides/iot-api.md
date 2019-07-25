# IoT APIs

> ![Attention](media/attention_icon.png) 
> 
> Samsung has discontinued support for ARTIK.
>
> In case you are still using ARTIK, we recommend that you migrate to Raspberry Pi 3 for headless-type IoT devices. Information on [Raspberry Pi 3 for Tizen IoT](https://developer.tizen.org/development/iot-extension-sdk/getting-started/setting-up-your-board/raspberry-pi3-based-on-tizen-5.0) will help you at it.
> The documentation for Tizen IoT with respect to ARTIK will be available only until August 2019.
>
> Thank you for your interest and support as always.

The Tizen IoT API provides a common set of interfaces allowing you to build compelling IoT device applications which achieve native performance. The characteristics include:

-   **Common set API**, which means that the Tizen IoT API is based on the Tizen 5.0 common profile. The API supports the common set of mobile, wearable, and TV profiles and allows you to make IoT applications, such as network audio applications.
-   **Available platform binaries**, which allow you to efficiently create an IoT application. Tizen Common Headed binaries for ARTIK 530 and ARTIK 530s have passed the API test verification, which means that you can create IoT applications with a productive quality.

The following table lists the IoT-specific Tizen platform API group.

**Table: Tizen IoT API group**

| IoT-specific API                                             | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [Things SDK API](things-api-5.0.md) | The SmartThings&trade; Things SDK APIs help you to create new Things applications on IoT devices. For the full specification, see the [Things SDK API Reference](https://developer.tizen.org/dev-guide/things-sdk/latest). |
| [Peripheral I/O API](peripheral-io-api.md) | The Peripheral I/O native APIs are designed specifically for making  IoT devices control peripherals, such as actuators and sensors. For the full specification, see the [Tizen Common Headed API Reference](https://developer.tizen.org/dev-guide/tizen-iot-headed/latest) and [Tizen Common Headless API Reference](https://developer.tizen.org/dev-guide/tizen-iot-headless/latest). |
| [ZigBee API](zigbee.md) | The Zigbee native APIs help you to create, destroy, and manage the Zigbee network. |

> **Note**
>
>Tizen IoT Extension SDK version 1.0 is not compatible with Tizen IoT Preview 2. For Things SDK API of Tizen IoT Preview 2, please see [Things SDK API for Tizen IoT Preview 2(legacy)](../preview2/guides/things-api.md) and [Things SDK API Reference for Tizen IoT Preview 2](https://developer.tizen.org/dev-guide/things-sdk/4.0).For the full set of API reference for Tizen 4.0 IoT Headed and Headless profiles, see the [Tizen 4.0 Common Headed API Reference](https://developer.tizen.org/dev-guide/tizen-iot-headed/4.0) and [Tizen 4.0 Common Headless API Reference](https://developer.tizen.org/dev-guide/tizen-iot-headless/4.0).
>
