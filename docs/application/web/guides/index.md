# Tizen Web APIs

Using the Tizen Web API modules, you can develop rich Web applications and build great application experiences with well-known Web programming languages: HTML, CSS, and JavaScript. Like every major browser in the market, the Tizen Web API modules support the latest HTML5 capabilities, such as animation, offline, audio, and video. By utilizing the standard HTML5 capabilities, your Web applications are ready to run across various devices and platforms with minimal customization. In addition to the JavaScript-based Tizen Device API, you can also enable advanced device access from your Web applications, such as Bluetooth and NFC.

The Tizen platform supports hybrid applications (1 Web application and 1 or more native applications). A hybrid application package is very useful for Web applications that need background processing or monitoring. With a hybrid application package, you can register the included applications in the official site for Tizen applications and install, update, and uninstall them using a single hybrid package. For more information on developing hybrid Web applications with Tizen devices, see [Packaging Hybrid Applications](../tutorials/process/app-dev-process.md#hybrid).

Tizen provides a wide range of Web API modules that allow you to take full advantage of various Tizen features.

> [!NOTE]
> The feature support differs depending on the application profile (TV, IoT, and other).

The following table lists the features provided by the [TV Web Device API Reference](../api/latest/device_api/tv/index.html).

**Table: Device API features provided for TV applications**

<table>
<tr>
<th>Feature</th>
<th>Purpose</th>
<th>Documentation</th>
</tr>
<tr>
<td>Base</td>
<td>These APIs contain classes and interfaces that provide a set of basic definitions and interfaces that are used in the Tizen Device API.<br>
You can manage common files and ZIP archive files, and define filters and sorting modes for queries. You can also use generic success and error event handlers, in addition to a generic error interface and a simple coordinate interface for defining location information.
</td>
<td>

- Guides:<br>
  [Data Storage and Management](data/data.md)<br>
  [Error Handling](error/error.md)
- API Reference: [Base](../api/latest/device_api/tv/index.html#Base)
</td>
</tr>
<tr>
<td>Application Framework</td>
<td>These APIs contain classes and interfaces that enable you to manage alarm, application, and package features.<br>
You can schedule an application to be run at a specific time, retrieve information about the applications installed or running on the device, and enable package management.
</td>
<td>

- Guides:<br>
  [Alarms](alarm/alarms.md) <br>
  [Applications](applications/overview.md)
  [Application Management](app-management/overview.md) <br>

- API Reference: [Application Framework](../api/latest/device_api/tv/index.html#Application%20Framework)
</td>
</tr>
<tr>
<td>Content</td>
<td>These APIs contain classes and interfaces that enable you to manage content and download features.<br>
You can search and manage multimedia content locally, manipulate EXIF data in JPEG files, download files from the Internet, and monitor the download progress and status.
</td>
<td>

- Guides:<br>
  [Connectivity and Wireless](connectivity/connectivity.md)<br>
  [Data Storage and Management](data/data.md)<br>
  [Media and Camera](multimedia/overview.md)
- API Reference: [Content](../api/latest/device_api/tv/index.html#Content)
</td>
</tr>
<tr>
<td>Messaging</td>
<td>This API contains classes and interfaces that enable you to manage push messaging.<br>
You can receive push notifications from a push server.
</td>
<td>

- Guides: [Messaging](messaging/overview.md)
- API Reference: [Messaging](../api/latest/device_api/tv/index.html#Messaging)
</td>
</tr>
<tr>
<td>Network</td>
<td>This API contains classes and interfaces that enable you to manage IoT connectivity.<br>
You can create a client and server, and manage their resources locally and remotely.
</td>
<td>

- Guides: [Connectivity and Wireless](connectivity/connectivity.md)
- API Reference: [Network](../api/latest/device_api/tv/index.html#Network)
</td>
</tr>
<tr>
<td>Security</td>
<td>This API contains classes and interfaces that enable you to manage secure keys in your application.<br>
You can use security functionalities, such as storing and recalling private data.
</td>
<td>

- Guides: [Security](security/security.md)
- API Reference: [Security](../api/latest/device_api/tv/index.html#Security)
</td>
</tr>
<tr>
<td>System</td>
<td>These APIs contain classes and interfaces that enable you to manage system information, time, and Web setting features.<br>
You can access the device system information and use locale-specific calendar features by retrieving date and time information. You can also set Web view properties, such as setting Web view user agents and deleting Web view cookies.
</td>
<td>

- Guides: [Device Settings and Systems](device/device.md)
- API Reference: [System](../api/latest/device_api/tv/index.html#System)
</td>
</tr>
<tr>
<td>UIX</td>
<td>This API contain classes and interfaces that enable you to set voice commands.<br>
You can allow the user to control the Web application through their voice.
</td>
<td>

- Guides: [Text Input and Voice](text-input/text-input.md)
- API Reference: [UIX](../api/latest/device_api/tv/index.html#UIX)
</td>
</tr>
<tr>
<td>Cordova</td>
<td>These APIs contain classes and interfaces that enable you use common functionalities in creating Tizen Web applications.<br>
You can manage the device filesystem, individual files, and various events, access device and network information and the device accelerometer, create dialog boxes and system log entries, and play audio files.
</td>
<td>

- Guides: [Cordova](cordova/cordova.md)
- API Reference: [Cordova](../api/latest/device_api/tv/index.html#Cordova)
</td>
</tr>
<tr>
<td>TV Controls</td>
<td>These APIs contain classes and interfaces that enable you control the TV functionalities, such as audio and settings.<br>
You can modify the volume level, and manage TV settings. You can also access 3D mode information, monitor remote control key events, and control the main and PIP window on the TV screen.
</td>
<td>

- API Reference: [TV Controls](../api/latest/device_api/tv/index.html#TV%20Controls)
</td>
</tr>

</table>

> [!NOTE]
> In Tizen Web Device APIs, there are two types of APIs: mandatory and optional.
>
> The mandatory APIs are always available on all Tizen devices. The optional APIs provide functionality that depends on the available device hardware or software capabilities, and they may not be available on all Tizen devices. For example, the Bluetooth and NFC API hardware features are optional, and not supported on all devices.
>
> To determine the availability of optional APIs, use the `tizen.systeminfo.getCapability()` method of the System Information API (in [TV](../api/latest/device_api/tv/tizen/systeminfo.html) applications).
>
> Note that all mandatory APIs are supported on the Tizen emulators, while the optional APIs may or may not be supported. For more information on support for each API, see [TV Web Device API Reference](../api/latest/device_api/tv/index.html).
>
