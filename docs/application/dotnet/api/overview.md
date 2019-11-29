# Tizen .NET API Reference

Tizen .NET provides a rich set of interfaces allowing you to build compelling TV, mobile, and wearable applications which achieve native performance. The programming environment includes the following:

- **.NET Standard API**, which implements the .NET Base Class library, and allows you to use the well-known C# language base class libraries and features, such as collections, threading, file input/output (I/O), and Language Integrated Query (LINQ).
- **Xamarin.Forms**, which allows you to efficiently build a user interface from standard components in C# or XAML.
- **Tizen.Wearable.CircularUI**, which allows you to efficiently add Tizen wearable-specific user interfaces.
- **TizenFX API**, which allows you to access platform-specific features not covered by the generic .NET and Xamarin.Forms features, such as system information and status, battery status, sensor date, and account and connectivity services.
  For the full specification, see the [TizenFX API Reference](https://samsung.github.io/TizenFX/latest/).

## .NET Standard API

One of the major components of .NET Core is the .NET Standard. The .NET APIs provided by Tizen .NET follow the .NET Standard 2.0. The column titled as 2.0 in the [official list](https://docs.microsoft.com/en-us/dotnet/standard/net-standard) of the supported CoreFX APIs lists all the available .NET APIs.

There are limitations of .NET Standard API on Tizen. For more information, see [Limitations of .NET Standard API on Tizen](dotnet-standard-limitations.md).

## Xamarin.Forms

[Xamarin.Forms](https://developer.xamarin.com/guides/xamarin-forms/getting-started/) provides cross-platform APIs, which allow you to create user interfaces that can be shared across platforms. The Visual Studio Tools for Tizen enables Tizen support for Xamarin.Forms.

You can efficiently build your Tizen .NET application UI and its supporting logic using the Xamarin.Forms APIs. Extended details for these APIs are available on the [Xamarin Web site](https://developer.xamarin.com/api/namespace/Xamarin.Forms/).

Tizen .NET contains a few limitations on the Xamarin.Forms APIs; these limitations are to be eliminated in future releases. The following classes are not supported:

- `AppLinkEntry`
- `OpenGLView`

A list of limitations is available at [Current Xamarin.Forms limitations](xamarin-forms-limitations.md).

## Tizen.Wearable.CircularUI

[Tizen.Wearable.CircularUI](https://samsung.github.io/Tizen.CircularUI/index.html) provides Tizen wearable-specific user interfaces. It is a set of extension APIs of Xamarin.Forms. Tizen.Wearable.CircularUI APIs are supported only on Tizen wearable devices with Tizen .NET support, unlike the Xamarin.Forms which support cross platforms.

Using these APIs, you can easily and efficiently add Tizen wearable-specific user interfaces to your Tizen wearable application. For more information about these APIs, see [Tizen.Wearable.CircularUI GitHub](https://github.com/Samsung/Tizen.CircularUI).

## TizenFX API

TizenFX API allows applications to call into platform-specific functionality from the shared code. This functionality enables Xamarin.Forms applications to do things a native application can do, without causing the portable part of the application to become littered with operating system-specific details.

The following table specifies the API Level supported by each version of the Tizen platform:

| Platform Version | API Level | Notes                                                        |
| ---------------- | --------- | ------------------------------------------------------------ |
| Tizen 4.0 M2     | 4         | [TizenFX API Reference](https://samsung.github.io/TizenFX/API4/) |
| Tizen 5.0 M2     | 5         | [TizenFX API Reference](https://samsung.github.io/TizenFX/API5/) |
| Tizen 5.5 M2     | 6         | [TizenFX API Reference](https://samsung.github.io/TizenFX/API6/) |

The following table lists the supported TizenFX API namespaces. For the full specification, see the TizenFX API Reference:

| Namespace          | Description                              |
| ------------------ | ---------------------------------------- |
| Tizen.Account      | Provides Create, Read, Update, Delete (CRUD) account management functionality and the OAuth Core RFC 6749 protocol. |
| Tizen.Applications | Provides the Tizen Application framework, including application state change events, inter-application messaging, and notification services. |
| Tizen.Common       | Provides predefined color names.         |
| Tizen.Content      | Provides content management services, such as file and media downloads, storing and indexing audio and video content, and associating content types with helper applications. |
| Tizen.Context.AppHistory | Provides classes to retrieve the user's application usage patterns. | 
| Tizen.Internals.Errors | Provides functions that return the additional information about error codes.
| Tizen.Location     | Manages geographical location services and geofencing. |
| Tizen.Maps         | Maps API provides a developer with a set of functions, helping to create Maps aware applications. |
| Tizen.Messaging    | Provides functions to receive push notifications, email, and messages. |
| Tizen.Multimedia   | Interacts with media services, including audio playback, recording and device policy, cameras, and video players. |
| Tizen.NUI          | The Natural User Interface (NUI) is a toolkit for creating applications with rich GUI. These applications can run on a range of Tizen devices. NUI is built on a multi-threaded architecture enabling realistic smooth animations. In addition a range of optimisation techniques are utilised to obtain low CPU and GPU usage, further increasing graphics performance. |
| Tizen.Network      | Provides APIs to control connectivity devices, such as Bluetooth, NFC, Wi-Fi, and an IoT interface service. |
| Tizen.PhonenumberUtils | Provides the methods for parsing, formatting, and normalizing the phone numbers. |
| Tizen.Pims         | Provides calendar and contacts services. |
| Tizen.Security     | Provides access to secure storage for passwords, keys, certificates, and other sensitive data. |
| Tizen.Sensor       | Provides sensor types and sensor information. |
| Tizen.System       | Provides device-specific services, including status, system information and settings, control of haptic devices and sensor control and access. |
| Tizen.Telephony    | Provides call, modem, network, and SIM information. |
| Tizen.Uix          | Provides functions to recognize the speech and to synthesize voice from text and playing synthesized sound data. |
| Tizen.Webview      | Provides functions to access web pages and web contents. |
| ElmSharp           | ElmSharp is a simple c# wrapper of native EFL elementary which provides all the widget you need to build a full application. |
