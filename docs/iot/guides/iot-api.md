# IoT APIs

> ![Attention](media/attention_icon.png) 
> 
> Samsung has discontinued support for ARTIK.
>
> In case you are still using ARTIK, we recommend that you migrate to Raspberry Pi 3 for headless-type IoT devices. Information on [Raspberry Pi 3 for Tizen IoT](../get-started/rpi3-5.0.md) will help you at it.
> The documentation for Tizen IoT with respect to ARTIK will be available only until August 2019.
>
> Thank you for your interest and support as always.

The Tizen IoT API provides a common set of interfaces allowing you to build compelling IoT device applications which achieve native performance. The characteristics include:

-   **Common set API**, which means that the Tizen IoT API is based on the Tizen 5.0 common profile. The API supports the common set of mobile, wearable, and TV profiles and allows you to make IoT applications, such as network audio applications.
-   **Available platform binaries**, which allow you to efficiently create an IoT application. Tizen Common Headed binaries for Raspberry Pi 3 have passed the API test verification, which means that you can create IoT applications with a productive quality.

The following table lists the IoT-specific Tizen platform API group.

**Table: Tizen IoT API group**

| IoT-specific API                                             | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [Things SDK API](things-api-5.0.md) | The SmartThings&trade; Things SDK APIs help you to create new Things applications on IoT devices. For the full specification, see the [Things SDK API Reference](../api/latest/things-sdk/index.html){:target="_blank"}. |
| [Peripheral I/O API](peripheral-io-api.md) | The Peripheral I/O native APIs are designed specifically for making  IoT devices control peripherals, such as actuators and sensors. For the full specification, see the [Tizen Common Headed API Reference](../api/latest/tizen-iot-headed/index.html){:target="_blank"} and [Tizen Common Headless API Reference](../api/latest/tizen-iot-headless/index.html){:target="_blank"}. |
| [ZigBee API](zigbee.md) | The Zigbee native APIs help you to create, destroy, and manage the Zigbee network. |

> **Note**
>
> Tizen IoT Extension SDK version 1.0 is not compatible with Tizen IoT Preview 2.
