#  TizenWeb Guides

## Dependencies

- Tizen 2.4 and Higher for Mobile
- Tizen 2.3.1 and Higher for Wearable
- Tizen 3.0 and Higher for TV

Tizen Web guides introduce various features for Web applications. The features are supported in the Web APIs, and you can use them in creating Tizen applications.
> **Note**  
> The feature support differs depending on the application profile (mobile, wearable, or TV). For a complete list of APIs and their supported profiles, see [Web API References](../../../../org.tizen.web.apireference/html/web_api_reference.htm).

Select the feature you are interested in and see what Tizen offers for your application:

- [Application Management](./app-management/app-management-cover-w.md)

  The application management features cover the application models available for Web applications. They describe the application life-cycle and resources, and the communication methods available for the application.

- [Cordova](./cordova/cordova-cover-w.md)

  Cordova features include common functionalities useful in creating Tizen Web applications.

- [Tizen Advanced UI](./ui/tau/tau-w.md) **in mobile and wearable applications only**

  The Tizen Advanced UI (TAU) features provide various aspects of creating a visual outlook for the user application to ensure the best possible user experience.

- [Localization](./localization/localization-w.md) **in mobile and wearable applications only**

  The localization features define how you can ensure that your application works around the world in different locales. You can provide the UI texts in your application in multiple languages.

- [Notifications](./notification/notification-w.md) **in mobile and wearable applications only**

  The notification features define how you can inform the user of important events. You can create simple and progress notifications and display them in the status bar.

- [Alarms](./alarm/alarms-w.md)

  The alarm features introduce how you can define and store alarms. You can use the alarm trigger to launch applications as and when the user needs them.

- [Media and Camera](./media/media-cover-w.md)

  The media and camera features cover everything related to multimedia. You can record and play various media formats, use the device camera to take pictures, and listen to the radio.

- [Connectivity and Wireless](./connectivity/connectivity-cover-w.md)

  The connectivity features define how you can connect your application to the outside world, and send and receive data. You can create connections to various networks, servers, and other devices.

- [Messaging](./messaging/messaging-cover-w.md) **in mobile and wearable applications only**

  The messaging features introduce how you can send and receive text and multimedia messages, and manage emails. You can also use the push service to deliver push messages to the application.

- [Sensors](./sensors/sensors-cover-w.md) **in mobile and wearable applications only**

  The sensor features provide information about the surrounding environment of the device. You can access data from various device sensors, which provide information on the physical environment the device is in, and the gestures and activities the user is engages in.

- [Text Input and Voice](./text-input/text-input-cover-w.md) **in mobile and wearable applications only**

  The text input and Voice features introduce how you can provide customized keyboards and Voice commands. You can also define keyboard commands to trigger specific actions.

- [Personal Data](./personal/personal-cover-w.md) **in mobile and wearable applications only**

  The personal data features cover the handling of secure data related to the user. You can manage and sync user accounts, and handle call history and bookmarks. You can also manage various user data on the device, such as contact and calendar information.

- [Data Storage and Management](./data/data-cover-w.md)

  The data storage and management features cover the methods you can use to handle data in your applications. You can access data from the device system and various storages. You can store data in various ways, and use filtering and sorting for effective data handling.

- [Device Settings and Systems](./device/device-cover-w.md)

  The device settings and systems features introduce how you can manage the device settings. You can set the time and date of the device, and manage the system information and power settings.

- [Security](./security/security-cover-w.md)

  The security features introduce how you can store and recall data in a secure manner in your application. You can use a repository to manage secure keys.

- [Error Handling](./error/error-w.md)

  The error handling features are needed when everything does not go as planned. You can handle exceptions and other error situations in your application code.

- [W3C/HTML5/Supplementary Features](./w3c/w3c-cover-w.md)

  The W3C, HTML5, and supplementary features cover various functionalities you can use in your application. You can use graphics, media, storage, and location features, as well as manage communication and security. These features also enable you to create an application UI using HTML and CSS.
​
> **Note**  
> In Tizen Web Device APIs, there are 2 types of APIs: mandatory and optional.
The mandatory APIs are always available on all Tizen devices. The optional APIs provide functionality that depends on the available device hardware or software capabilities, and they may not be available on all Tizen devices. For example, the Bluetooth and NFC API hardware features are optional, and not supported on all devices.

To determine the availability of optional APIs, use the `tizen.systeminfo.getCapability()` method of the System Information API (in [mobile](../../../org.tizen.web.apireference/html/device_api/mobile/tizen/systeminfo.html), [wearable](../../../org.tizen.web.apireference/html/device_api/wearable/tizen/systeminfo.html), and [TV](../../../org.tizen.web.apireference/html/device_api/tv/tizen/systeminfo.html) applications).

Note that all mandatory APIs are supported on the Tizen Emulators, while the optional APIs may or may not be supported. For more information on support for each API, see [Tizen Web Device API Reference](../../../org.tizen.web.apireference/html/device_api/device_api_cover.html).

To compare API support between Web Device API modules and native API modules, see [Tizen 3.0 Native and Web API Modules](attachments/Tizen-3.0-Native-Web-API-Modules.pdf).
