# Tizen Web APIs

Using the Tizen Web API modules, you can develop rich Web applications and build great application experiences with well-known Web programming languages: HTML, CSS, and JavaScript. Like every major browser in the market, the Tizen Web API modules support the latest HTML5 capabilities, such as animation, offline, audio, and video. By utilizing the standard HTML5 capabilities, your Web applications are ready to run across various devices and platforms with minimal customization. In addition to the JavaScript-based Tizen Device API, you can also enable advanced device access from your Web applications, such as Bluetooth and NFC.

The Tizen platform supports hybrid applications (1 Web application and 1 or more native applications). A hybrid application package is very useful for Web applications that need background processing or monitoring. With a hybrid application package, you can register the included applications in the Tizen Store and install, update, and uninstall them using a single hybrid package. For more information on developing hybrid Web applications with Tizen devices, see [Packaging Hybrid Applications](../tutorials/process/app-dev-process.md#hybrid).

Tizen provides a wide range of Web API modules that allow you to take full advantage of various Tizen features.

The following table lists the features provided by the [Mobile Web Device API Reference](../api/latest/device_api/mobile/index.html).

**Table: Device API features provided for mobile applications**

<table>
<tr>
<th>Feature</th>
<th>Purpose</th>
<th>Documentation</th>
</tr>

<tr>
<td>Base</td>
<td>These APIs contain classes and interfaces that provide a set of basic definitions and interfaces that are used in the Tizen Device API.<BR>
You can manage common files and ZIP archive files, and define filters and sorting modes for queries. You can also use generic success and error event handlers, in addition to a generic error interface and a simple coordinate interface for defining location information.
</td>
<td>

- Guides: <br>
  [Data Storage and Management](data/data.md)<br>
  [Error Handling](error/error.md)<br>
- API Reference:
  [Base](../api/latest/device_api/mobile/index.html#Base)
</td>
</tr>
<tr>
<td>Account</td>
<td>This API contains classes and interfaces that enable you to manage account features.<br>
You can use existing configured on-line accounts and providers, and create new accounts of known types.
</td>
<td>

- Guides: [Personal Data](personal/personal.md)<br>
- API Reference: [Account](../api/latest/device_api/mobile/index.html#Account)
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
  [Application Management](app-management/applications.md) <br>
  [Notifications](notification/notification.md)<br>
- API Reference: [Application Framework](../api/latest/device_api/mobile/index.html#Application)

</td>
</tr>
<tr>
<td>Content</td>
<td>These APIs contain classes and interfaces that enable you to manage content and download features.<br>
You can search and manage multimedia content locally, download files from the Internet, and monitor the download progress and status.
</td>
<td>

- Guides:<br>
  [Connectivity and Wireless](connectivity/connectivity.md)<br>
  [Data Storage and Management](data/data.md)   <br>
- API Reference: [Content](../api/latest/device_api/mobile/index.html#Contents)

</td>
</tr>
<tr>
<td>Messaging</td>
<td>These APIs contain classes and interfaces that enable you to manage SMS, MMS, and email messages.<br>
You can send and receive messages, and receive push notifications from a push server.
</td>
<td>

- Guides: [Messaging](messaging/messaging.md)
- API Reference: [Messaging](../api/latest/device_api/mobile/index.html#Messaging)

</td>
</tr>
<tr>
<td>Multimedia</td>
<td>These APIs contain classes and interfaces that enable you to manage multimedia-related features.<br>
You can change and monitor playback volume level, and listen to the FM radio.
</td>
<td>

- Guides: [Media and Camera](multimedia/media.md)
- API Reference: [Multimedia](../api/latest/device_api/mobile/index.html#Multimedia)
</td>
</tr>
<tr>
<td>Network</td>
<td>These APIs contain classes and interfaces that enable you to manage Bluetooth, NFC (Near Field Communication), and secure element features.<br>
You can transfer data over a Bluetooth connection, share contacts, photos, and videos using NFC, and access secure elements, such as SIM card and secure SD card, in a device.
</td>
<td>

- Guides: [Connectivity and Wireless](connectivity/connectivity.md)
- API Reference: [Network](../api/latest/device_api/mobile/index.html#Network)
</td>
</tr>
<tr>
<td>Security</td>
<td>This API contains classes and interfaces that enable you to manage secure keys in your application.<br>
You can use security functionalities, such as storing and recalling private data.
</td>
<td>

- Guides: [Security](security/security.md)
- API Reference: [Security](../api/latest/device_api/mobile/index.html#Security)
</td>
</tr>
<tr>
<td>Social</td>
<td>These APIs contain classes and interfaces that enable you to manage bookmark, calendar, call history, contact, and data synchronization features.<br>
You can manage the Tizen Web browser bookmark list, calendar events and tasks, call history, and address books and contacts on a device, and you can synchronize device data, such as contacts and calendar events, with the OMA DS server.
</td>
<td>

- Guides: [Personal Data](personal/personal.md)
- API Reference: [Social](../api/latest/device_api/mobile/index.html#Social)
</td>
</tr>
<tr>
<td>System</td>
<td>These APIs contain classes and interfaces that enable you to manage power, system information and setting, time, and Web setting features.<br>
You can access the state of the device power resource, device system information, and device wallpaper settings. You can use locale-specific calendar features by retrieving date and time information, and set feedback patterns for specified actions. You can also manage time features, and set Web view properties, such as setting Web view user agents and deleting Web view cookies.
</td>
<td>

- Guides:<br>
  [Device Settings and Systems](device/device.md) <br>
  [Media and Camera](multimedia/media.md) <br>
  [Sensors](sensors/sensors.md)<br>
- API Reference: [System](../api/latest/device_api/mobile/index.html#System)
</td>
</tr>
<tr>
<td>UIX</td>
<td>This API contain classes and interfaces that enable you to set voice commands.<br>
You can allow the user to control the Web application through their voice.
</td>
<td>

- Guides: [Text Input and Voice](text-input/text-input.md)
- API Reference: [UIX](../api/latest/device_api/mobile/index.html#UIX)
</td>
</tr>
<tr>
<td>Cordova</td>
<td>These APIs contain classes and interfaces that enable you use common functionalities in creating Tizen Web applications.<br>
You can manage the device filesystem, individual files, and various events, access device and network information and the device accelerometer, create dialog boxes and system log entries, and play audio files.
</td>
<td>

- Guides: [Cordova](cordova/cordova.md)
- API Reference: [Cordova](../api/latest/device_api/mobile/index.html#Cordova)
</td>
</tr>
<tr>
<td>Web UI Framework</td>
<td>These APIs contain classes and interfaces that enable you to manage the Tizen Advanced UI (TAU) features.<br>
You can create and manage various kinds of UI components.
</td>
<td>

- Guides: [Tizen Advanced UI](tau/tau.md)
- API Reference: [Advanced UI Framework](../api/latest/ui_fw_api/ui_fw_api_cover.htm)
</td>
</tr>

</table>


The following table lists the features provided by the [Wearable Web Device API Reference](../api/latest/device_api/wearable/index.html).

**Table: Device API features provided for wearable applications**

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
  [Data Storage and Management](data/data.md)
  [Error Handling](error/error.md)
- API Reference: [Base](../api/latest/device_api/wearable/index.html#Base)
</td>
</tr>
<tr>
<td>Account</td>
<td>This API contains classes and interfaces that enable you to manage account features.<br>
You can use existing configured on-line accounts and providers, and create new accounts of known types.
</td>
<td>

- Guides: [Personal Data](personal/personal.md)
- API Reference: [Account](../api/latest/device_api/wearable/index.html#Account)
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
  [Application Management](app-management/applications.md) <br>
  [Notifications](notification/notification.md)<br>
- API Reference: [Application Framework](../api/latest/device_api/wearable/index.html#Application)
</td>
</tr>
<tr>
<td>Content</td>
<td>These APIs contain classes and interfaces that enable you to manage content and download features.<br>
You can search and manage multimedia content locally, download files from the Internet, and monitor the download progress and status.
</td>
<td>

- Guides:<br>
  [Connectivity and Wireless](connectivity/connectivity.md)<br>
  [Data Storage and Management](data/data.md)
- API Reference:  [Content](../api/latest/device_api/wearable/index.html#Contents)
</td>
</tr>
<tr>
<td>Messaging</td>
<td>This API contains classes and interfaces that enable you to manage push messaging.<br>
You can receive push notifications from a push server.
</td>
<td>

- Guides: [Messaging](messaging/messaging.md)
- API Reference: [Messaging](../api/latest/device_api/wearable/index.html#Messaging)
</td>
</tr>
<tr>
<td>Multimedia</td>
<td>These APIs contain classes and interfaces that enable you to manage multimedia-related features.<br>
You can change and monitor playback volume level, and listen to the FM radio.
</td>
<td>

- Guides: [Media and Camera](multimedia/media.md)
- API Reference: [Multimedia](../api/latest/device_api/wearable/index.html#Multimedia)
</td>
</tr>
<tr>
<td>Network</td>
<td>These APIs contain classes and interfaces that enable you to manage Bluetooth, NFC (Near Field Communication), and secure element features.<br>
You can transfer data over a Bluetooth connection, share contacts, photos, and videos using NFC, and access secure elements, such as SIM card and secure SD card, in a device.
</td>
<td>

- Guides: [Connectivity and Wireless](connectivity/connectivity.md)
- API Reference: [Network](../api/latest/device_api/wearable/index.html#Network)
</td>
</tr>
<tr>
<td>Security</td>
<td>This API contains classes and interfaces that enable you to manage secure keys in your application.<br>
You can use security functionalities, such as storing and recalling private data.
</td>
<td>

- Guides: [Security](security/security.md)
- API Reference: [Security](../api/latest/device_api/wearable/index.html#Security)
</td>
</tr>
<tr>
<td>Social</td>
<td>These APIs contain classes and interfaces that enable you to manage calendar and contact features.<br>
You can manage calendar events and tasks, address books, and contacts on a device.
</td>
<td>

- Guides: [Personal Data](personal/personal.md)
- API Reference: [Social](../api/latest/device_api/wearable/index.html#Social)
</td>
</tr>
<tr>
<td>System</td>
<td>These APIs contain classes and interfaces that enable you to manage power, system information and setting, and time features.<br>
You can access the state of the device power resource, device system information, and device wallpaper settings. You can use locale-specific calendar features by retrieving date and time information, and set feedback patterns for specified actions. You can also manage time features.
</td>
<td>

- Guides:<br>
  [Device Settings and Systems](device/device.md) <br>
  [Media and Camera](multimedia/media.md)<br>
  [Sensors](sensors/sensors.md)<br>
- API Reference: [System](../api/latest/device_api/wearable/index.html#System)
</td>
</tr>
<tr>
<td>UIX</td>
<td>This API contain classes and interfaces that enable you to set voice commands.<br>
You can allow the user to control the Web application through their voice.
</td>
<td>

- Guides: [Text Input and Voice](text-input/text-input.md)
- API Reference: [UIX](../api/latest/device_api/wearable/index.html#UIX)

</td>
</tr>
<tr>
<td>Cordova</td>
<td>These APIs contain classes and interfaces that enable you use common functionalities in creating Tizen Web applications.<br>
You can manage the device filesystem, individual files, and various events, access device and network information and the device accelerometer, create dialog boxes and system log entries, and play audio files.
</td>
<td>

- Guides: [Cordova](cordova/cordova.md)
- API Reference: [Cordova](../api/latest/device_api/wearable/index.html#Cordova)
</td>
</tr>
<tr>
<td>Web UI Framework</td>
<td>These APIs contain classes and interfaces that enable you to manage the Tizen Advanced UI (TAU) features.<br>
You can create and manage various kinds of UI components.
</td>
<td>

- Guides: [Tizen Advanced UI](tau/tau.md)
- API Reference: [Advanced UI Framework](../api/latest/ui_fw_api/ui_fw_api_cover.htm)
</td>
</tr>
</table>

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
- API Reference: [Base](../api/latest/device_api/tv/index.html#Tizen)
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
  [Application Management](app-management/applications.md)

- API Reference: [Application Framework](../api/latest/device_api/tv/index.html#Application)
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
  [Media and Camera](multimedia/media.md)
- API Reference: [Content](../api/latest/device_api/tv/index.html#Contents)
</td>
</tr>
<tr>
<td>Messaging</td>
<td>This API contains classes and interfaces that enable you to manage push messaging.<br>
You can receive push notifications from a push server.
</td>
<td>

- Guides: [Messaging](messaging/messaging.md)
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
<td>These APIs contain classes and interfaces that enable you control the TV functionalities, such as channels and audio.<br>
You can modify the volume level, switch TV channels, get program guide information, and manage TV settings. You can also access 3D mode information, monitor remote control key events, and control the main and PIP window on the TV screen.
</td>
<td>

- API Reference: [TV Controls](../api/latest/device_api/tv/index.html#TV%20Control)
</td>
</tr>

</table>

<!-- W3C docs are outdated -->
<!--
The following table lists the features provided by the [Mobile Web W3C/HTML5 and Supplementaries API Reference](../api/latest/w3c_api/w3c_api_m.html).

**Table: W3C/HTML5 and some supplementary API features provided for mobile applications**

<table>
<tr>
<th>Feature</th>
<th>Purpose</th>
<th>Documentation</th>
</tr>
<tr>
<td>DOM, Forms and Styles</td>
<td>These APIs enable you to create animations, specify the border and background styles of HTML elements, apply styles to HTML documents, specify the color and opacity of HTML elements, create flexible and multi-column layouts for Web applications, move, rotate, stretch, and scale elements, and add effects using CSS3 properties. They also enable you to use CSS and JavaScript code effectively with HTML elements, implement Web forms for user input, define media features for specific output devices, select element nodes in the DOM tree, and store information about the page that the user has viewed.</td>
<td>

- Guides: [User Interface](w3c/ui/ui-guide.md)
- API Reference: [DOM, Forms and Styles](../api/latest/w3c_api/w3c_api_m.html#dom)
</td>
</tr>
<tr>
<td>Device</td>
<td>These APIs enable you to retrieve the battery status and detect changes in it, detect rotation and acceleration motions, manage screen orientation, implement and control various types of touch events, and implement different vibration patterns on a Tizen device.</td>
<td>

- Guides: [Device](w3c/device/device-guide.md)
- API Reference: [Device](../api/latest/w3c_api/w3c_api_m.html#device)
</td>
</tr>
<tr>
<td>Graphics</td>
<td>These APIs enable you to create images, shapes, and text using the HTML5 canvas element and HTML canvas 2D context, and create and modify SVG elements in your application.</td>
<td>

- Guides: [Graphics](w3c/graphics/graphics-guide.md)
- API Reference: [Graphics](../api/latest/w3c_api/w3c_api_m.html#graphics)
</td>
</tr>
<tr>
<td>Media</td>
<td>These APIs enable you to access a local device to generate a multimedia stream, access the media capture capabilities based on their type, control multimedia playback and check supported media formats, and play audio content.</td>
<td>

- Guides: [Media](w3c/multimedia/media-guide.md)
- API Reference: [Media](../api/latest/w3c_api/w3c_api_m.html#media)
</td>
</tr>
<tr>
<td>Communication</td>
<td>These APIs enable you to send and receive data between Web sites and through a message channel, exchange push data with the server, connect to the socket server to send and receive data, and use cross-origin resource sharing (CORS) to request and send data of various content types.</td>
<td>

- Guides: [Communication](w3c/communication/comm-guide.md)
- API Reference: [Communication](../api/latest/w3c_api/w3c_api_m.html#communication)
</td>
</tr>
<tr>
<td>Storage</td>
<td>These APIs enable you to retrieve file content and information, slice data objects, manage sandboxed file systems, activate project resource caching and manage the cached resources, create an object store and save data in it, create databases and access them using SQL statements, and use session storage and local storage.</td>
<td>

- Guides: [Storage](w3c/storage/storage-guide.md)
- API Reference: [Storage](../api/latest/w3c_api/w3c_api_m.html#storage)
</td>
</tr>
<tr>
<td>Security</td>
<td>These APIs enable you to allow or block specific HTML elements on a Web page, and make cross-origin requests to resources, allowing a client-side Web application to obtain data retrieved from another origin.</td>
<td>

- Guides: [Security](w3c/security/security-guide.md)
- API Reference: [Security](../api/latest/w3c_api/w3c_api_m.html#security)
</td>
</tr>
<tr>
<td>UI</td>
<td>These APIs enable you to copy content and paste it in an editable area, create and manage draggable elements, and implement drag events.</td>
<td>

- Guides: [User Interface](w3c/ui/ui-guide.md)
- API Reference:  [UI](../api/latest/w3c_api/w3c_api_m.html#ui)

</td>
</tr>
<tr>
<td>Performance and Optimization</td>
<td>These APIs enable you to retrieve the visibility status of a Web document and detect changes in it, control animation frame rate, and create and manage HTML5 Web Workers to run an independent JavaScript thread in the background.</td>
<td>

- Guides: [Performance and Optimization](w3c/perf-opt/performance-guide.md)
- API Reference: [Performance and Optimization](../api/latest/w3c_api/w3c_api_m.html#performance)
</td>
</tr>
<tr>
<td>Location</td>
<td>These APIs enable you to retrieve and update position information.</td>
<td>

- Guides: [Location](w3c/location/location-guide.md)
- API Reference: [Location](../api/latest/w3c_api/w3c_api_m.html#location)
</td>
</tr>
<tr>
<td>Supplementary</td>
<td>These APIs enable you to manage some supplementary features, such as displaying an element on full screen, accessing binary data in JavaScript, and using the WebGL™ graphics library to create 3D visual elements.</td>
<td>

- Guides: [Supplementary Features](w3c/supplement/supplement-guide.md)
- API Reference: [Supplementary](../api/latest/w3c_api/w3c_api_m.html#Supplementary)
</td>
</tr>

</table>

The following table lists the features provided by the [Wearable Web W3C/HTML5 and Supplementaries API Reference](../api/latest/w3c_api/w3c_api_w.html).

**Table: W3C/HTML5 and some supplementary API features provided for wearable applications**


<table>
<tr>
<th>Feature</th>
<th>Purpose</th>
<th>Documentation</th>
</tr>
<tr>
<td>DOM, Forms and Styles</td>
<td>These APIs enable you to create animations, specify the border and background styles of HTML elements, apply styles to HTML documents, specify the color and opacity of HTML elements, create flexible layouts for Web applications, move, rotate, stretch, and scale elements, and add effects using CSS3 properties. They also enable you to use CSS and JavaScript code effectively with HTML elements, implement Web forms for user input, define media features for specific output devices, select element nodes in the DOM tree, and store information about the page that the user has viewed.</td>
<td>

- Guides: [User Interface](w3c/ui/ui-guide.md)
- API Reference: [DOM, Forms and Styles](../api/latest/w3c_api/w3c_api_w.html#dom)
</td>
</tr>
<tr>
<td>Device</td>
<td>These APIs enable you to retrieve the battery status and detect changes in it, detect rotation and acceleration motions, implement and control various types of touch events, and implement different vibration patterns on a Tizen wearable device.</td>
<td>

- Guides: [Device](w3c/device/device-guide.md)
- API Reference: [Device](../api/latest/w3c_api/w3c_api_w.html#device)
</td>
</tr>
<tr>
<td>Graphics</td>
<td>These APIs enable you to create images, shapes, and text using the HTML5 canvas element and HTML canvas 2D context.</td>
<td>

- Guides: [Graphics](w3c/graphics/graphics-guide.md)
- API Reference: [Graphics](../api/latest/w3c_api/w3c_api_w.html#graphics)
</td>
</tr>
<tr>
<td>Media</td>
<td>These APIs enable you to access a local device to generate a multimedia stream, control multimedia playback and check supported media formats, and play audio content.</td>
<td>

- Guides: [Media](w3c/multimedia/media-guide.md)
- API Reference: [Media](../api/latest/w3c_api/w3c_api_w.html#media)
</td>
</tr>
<tr>
<td>Communication</td>
<td>These APIs enable you to send and receive data between Web sites and through a message channel, and connect to the socket server to send and receive data.</td>
<td>

- Guides: [Communication](w3c/communication/comm-guide.md)
- API Reference: [Communication](../api/latest/w3c_api/w3c_api_w.html#communication)
</td>
</tr>
<tr>
<td>Storage</td>
<td>These APIs enable you to retrieve file content and information, create an object store and save data in it, and use session storage and local storage.</td>
<td>

- Guides: [Storage](w3c/storage/storage-guide.md)
- API Reference: [Storage](../api/latest/w3c_api/w3c_api_w.html#storage)
</td>
</tr>
<tr>
<td>Security</td>
<td>These APIs enable you to allow or block specific HTML elements on a Web page.</td>
<td>

- Guides: [Security](w3c/security/security-guide.md)
- API Reference: [Security](../api/latest/w3c_api/w3c_api_w.html#security)
</td>
</tr>
<tr>
<td>Performance and Optimization</td>
<td>These APIs enable you to retrieve the visibility status of a Web document and detect changes in it, control animation frame rate, and create and manage HTML5 Web Workers to run an independent JavaScript thread in the background.</td>
<td>

- Guides: [Performance and Optimization](w3c/perf-opt/performance-guide.md)
- API Reference: [Performance and Optimization](../api/latest/w3c_api/w3c_api_w.html#performance)
</td>
</tr>
<tr>
<td>Location</td>
<td>These APIs enable you to retrieve and update position information.</td>
<td>

- Guides: [Location](w3c/location/location-guide.md)
- API Reference: [Location](../api/latest/w3c_api/w3c_api_w.html#location)
</td>
</tr>
<tr>
<td>Supplementary</td>
<td>These APIs enable you to manage some supplementary features, such as managing the device camera, accessing binary data in JavaScript, and using the WebGL™ graphics library to create 3D visual elements.</td>
<td>

- Guides: [Supplementary Features](w3c/supplement/supplement-guide.md)
- API Reference: [Supplementary](../api/latest/w3c_api/w3c_api_w.html#Supplementary)
</td>
</tr>
</table>
-->
