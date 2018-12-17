# Tizen .NET Guides

Tizen .NET provides a rich set of interfaces allowing you to build compelling TV, mobile, and wearable (preview) applications which achieve native performance. The programming environment includes the following:

- **.NET Standard API**, which implements the .NET Base Class library, and allows you to use the well-known C# language base class libraries and features, such as collections, threading, file input/output (I/O), and Language Integrated Query (LINQ).
- **Xamarin.Forms**, which allows you to efficiently build a user interface from standard components in C# or XAML.
- **Tizen.Wearable.CircularUI**, which allows you to efficiently add Tizen wearable-specific user interfaces.
- **TizenFX API**, which allows you to access platform-specific features not covered by the generic .NET and Xamarin.Forms features, such as system information and status, battery status, sensor date, and account and connectivity services.
  For the full specification, see the [TizenFX API Reference](https://samsung.github.io/TizenFX/API5/).

## .NET Standard API

One of the major components of .NET Core is the .NET Standard. The .NET APIs provided by Tizen .NET follow the .NET Standard 2.0. The column titled as 2.0 in the [official list](https://docs.microsoft.com/en-us/dotnet/standard/net-standard) of the supported CoreFX APIs lists all the available .NET APIs.

There are limitations of .NET Standard API on Tizen. For more information, see [Limitations of .NET Standard API on Tizen](dotnet-standard-limitations.md).

## Xamarin.Forms

[Xamarin.Forms](https://developer.xamarin.com/guides/xamarin-forms/getting-started/) provides cross-platform APIs, which allow you to create user interfaces that can be shared across platforms. The Tizen.NET Visual Studio extension enables Tizen support for Xamarin.Forms.

You can efficiently build your Tizen .NET application UI and its supporting logic using the Xamarin.Forms APIs. Extended details for these APIs are available on the [Xamarin Web site](https://developer.xamarin.com/api/namespace/Xamarin.Forms/).

The Tizen.NET contains a few limitations on the Xamarin.Forms APIs; these limitations are to be eliminated in future releases. The following classes are not supported:

- `AppLinkEntry`
- `OpenGLView`

A list of limitations is available at [Current Xamarin.Forms limitations](xamarin-forms-limitations.md).

## Tizen.Wearable.CircularUI

[Tizen.Wearable.CircularUI](https://samsung.github.io/Tizen.CircularUI/index.html) provides Tizen wearable-specific user interfaces. It is a set of extension APIs of Xamarin.Forms. Tizen.Wearable.CircularUI APIs are supported only on Tizen wearable devices with Tizen .NET support, unlike the Xamarin.Forms which support cross platforms.

Using these APIs, you can easily and efficiently add Tizen wearable-specific user interfaces to your Tizen wearable application. For more information about these APIs, see [Tizen.Wearable.CircularUI GitHub](https://github.com/Samsung/Tizen.CircularUI).

## Tizen OpenTK
The Tizen OpenTK provides a set of fast and low-level C# bindings for OpenGL&reg; ES APIs. From Tizen 5.0, it is integrated with Tizen Application Framework. Therefore, it allows Tizen app developer to use C# OpenGL&reg; ES APIs in .Net application.

Using these APIs, you can quickly create graphic applications with the OpenGL&reg; ES 2.0, such as, Ambient app, Game, Dynamic partial, Physics effect, and so on. For more information about these APIs, see [Tizen OpenTK GitHub](https://github.com/TizenAPI/opentk).

## TizenFX API

The TizenFX API allows applications to call into platform-specific functionality from the shared code. This functionality enables Xamarin.Forms applications to do things a native application can do, without causing the portable part of the application to become littered with operating system-specific details.

The following table specifies the API Level supported by each version of the Tizen platform:

| Platform Version | API Level | Notes                                                        |
| ---------------- | --------- | ------------------------------------------------------------ |
| Tizen 4.0 M2     | 4         | [TizenFX API Reference](https://samsung.github.io/TizenFX/API4/) |
| Tizen 5.0 M2     | 5         | [TizenFX API Reference](https://samsung.github.io/TizenFX/API5/) |


### TizenFX API Guides

TizenFX API introduce various features for Tizen .NET applications. The TizenFX API allows applications to call into platform-specific functionality from the shared code. This functionality enables Xamarin.Forms applications to do things a native application can do, without causing the portable part of the application to become littered with operating system-specific details.

You can use the following TizenFX features in your .NET applications:

- [Applications](applications/overview.md)

  The applications feature covers various application models available for Tizen .NET applications. You can create UI applications to run on the foreground, and specific applications to function as the watch face for the device clock, or as a widget available on the home screen.

- [Application Management](app-management/overview.md)

  The application management feature introduces how to handle applications and packages. You can see application resources and communication methods between applications.

- [Natural User Interface](nui/overview.md)

  The Natural User Interface (NUI) features provide various aspects of creating a visual outlook for the user application to ensure the best user experience. NUI is a rich GUI library for creating a 2-dimensional or a 3-dimensional applications. These applications run on a range of Tizen devices, such as TVs and wearables. NUI is built on a multi-threaded architecture by enabling realistic smooth animations.

- [Wearable Circular UI](wcircularui/overview.md)

  The Wearable Circular UI feature introduces a set of helpful extensions of the <a href="https://docs.microsoft.com/en-us/xamarin/xamarin-forms/" target="_blank">Xamarin.Forms</a> framework.
  Its aim is to develop an open source software and to motivate software developers to create Tizen Wearable Xamarin.Forms application more easily and efficiently.

- [Localization](internationalization/localization.md)

  The localization feature ensures that your application is functional in different locations and time zones.

- [Notifications and Content Sharing](notification/overview.md)

  The notifications and content sharing features introduce how you can inform the user of important events and allow the user to share content between applications.

- [Alarms and Scheduling](alarm/alarms.md)

  The alarms and scheduling features introduce how you can define and store alarms.

- [Media and Camera](multimedia/overview.md)

  The media and camera features cover everything related to multimedia. You can record and play various media formats, use the device camera to take pictures, and listen to the radio. You can also handle media conversions and manage media streams.

- [Connectivity and Wireless](connectivity/overview.md)

  The connectivity features define how you can connect your application to the outside world, and send and receive data. You can create connections to various networks, servers, and other devices.

- [Messaging](messaging/overview.md)

  The messaging features introduce how you can send and receive text and multimedia messages, and manage emails. You can also create a push server to use the push messaging service to deliver push notifications to the application.

- [Location and Sensors](location-sensors/overview.md)

  The location and sensor features provide information about the geographical location and surrounding environment of the device. You can create location-based applications that track the user location and use maps. You can also access data from various device sensors, which provide information on the physical environment the device is in, and the gestures and activities the user engages in.

- [Text Input and Voice](text-input/overview.md)

  The text input and voice features introduce how you can convert speech to text and back to speech, or provide customized keyboards. You can also define commands to allow the user to control the application with their voice.

- [Personal Data](personal/overview.md)

  The personal data features cover the handling of secure data related to the user. You can manage and sync user accounts, and authenticate the user to allow them to access services. You can also manage various user data on the device, such as their application usage patterns.

- [Data Storage and Management](data/overview.md)

  The data storage and management features cover the methods you can use to handle data in your applications. You can access data from the device system and various storages.

- [Device Settings and Systems](device/overview.md)

  The device settings and systems features introduce how you can set and get information about the system. You can also access information about attached devices, and manage the sound and vibration feedback given to the user.

- [Security](security/overview.md)

  The security features ensure that private information remains private, and that the user knows when they are trying to access privileged information. You can use a repository to manage keys, certificates, and sensitive user data. When the user tries to access privileged information, you can display information about the data.

- [Natural Language Processing](nlp/overview.md)

  The natural language process features explains the methods by which you can handle all the sentences in your applications. You can get the results using the NLP service.

## Related Information

- Dependencies
  - Tizen 4.0 and Higher
