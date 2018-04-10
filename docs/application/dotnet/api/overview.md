# Tizen .NET API Reference

Tizen .NET provides a rich set of interfaces allowing you to build compelling TV, mobile, and wearable(preview) applications which achieve native performance. The programming environment includes the following:

- **.NET Standard API**, which implements the .NET Base Class library, allows you to use the well known C# language base class libraries and features, such as collections, threading, file I/O, and LINQ.
- **Xamarin.Forms**, which allows you to efficiently build a user interface from standard components in C# or XAML.
- **TizenFX API**,
   which allows you to access platform-specific features not covered by the generic .NET and Xamarin.Forms features,  such as system information  and status, battery status, sensor date, and account and connectivity services.  For the full specification, see the <a href="tizenfx/index.html" target="api">TizenFX API Reference</a>

## .NET Standard API

One of the major components of .NET Core is the .NET Standard. The .NET APIs provided by Tizen .NET follow the .NET Standard 2.0. The column titled "2.0" in the [official list](https://docs.microsoft.com/en-us/dotnet/standard/net-standard) of supported CoreFX APIs lists all the available .NET APIs.

## Xamarin.Forms

[Xamarin.Forms](https://developer.xamarin.com/guides/xamarin-forms/getting-started/) provides cross-platform APIs, which allow you to create user interfaces that can be shared across platforms. The Tizen.NET Visual Studio extension enables Tizen support for Xamarin.Forms.

You can efficiently build your Tizen .NET application UI and its supporting logic using the Xamarin.Forms APIs. Extended details for these APIs are available on the [Xamarin Web site](https://developer.xamarin.com/api/namespace/Xamarin.Forms/).

The Tizen.NET contains a few limitations on the Xamarin.Forms APIs; these limitations are to be eliminated in future releases. The following classes are not supported:

- `AppLinkEntry`
- `OpenGLView`

A list of limitations is available at [Current Xamarin.Forms limitations](xamarin.forms-limitations.html).

## TizenFX API

The Tizen Platform-Specific API allows applications to call into platform-specific functionality from the shared code. This functionality enables Xamarin.Forms applications to do things a native application can do, without causing the portable part of the application to become littered with operating system-specific details.

The following table specifies the API Level supported by each version of the Tizen platform.

| Platform Version | API Level | Notes                                    |
| ---------------- | --------- | ---------------------------------------- |
| Tizen 4.0 M2     | 4         | [Platform Highlights](https://developer.tizen.org/tizen/tizen/tizen-4.0) |

The following table lists the supported Tizen platform-specific API namespaces. For the full specification, see the <a href="tizenfx/index.html" target="api">TizenFX API Reference</a>

| Namespace          | Description                              |
| ------------------ | ---------------------------------------- |
| Tizen.Account      | Provides CRUD (Create, Read, Update, Delete) account management functionality and the OAuth Core RFC 6749 protocol. |
| Tizen.Applications | Provides the Tizen application framework, including application state change events, inter-application messaging, and notification services. |
| Tizen.Common       | Provides predefined color names.         |
| Tizen.Content      | Provides content management services, such as file and media downloads, storing and indexing audio and video content, and associating content types with helper applications. |
| Tizen.Location     | Manages geographical location services and geofencing. |
| Tizen.Maps         | Maps API provides a developer with a set of functions, helping to create Maps aware applications. |
| Tizen.Messaging    | Provides functions to receive push notifications, email, and messages |
| Tizen.Multimedia   | Interacts with media services, including audio playback, recording and device policy, cameras, and video players. |
| Tizen.Network      | Provides APIs to control connectivity devices, such as Bluetooth, NFC, Wi-Fi, and an IoT interface service. |
| Tizen.NUI          | The Natural User Interface (NUI) is a toolkit for creating applications with rich GUI. These applications can run on a range of Tizen devices. NUI is built on a multi-threaded architecture enabling realistic smooth animations. In addition a range of optimisation techniques are utilised to obtain low CPU and GPU usage, further increasing graphics performance. |
| Tizen.Pims         | Provides calendar and contacts services. |
| Tizen.Security     | Provides access to secure storage for passwords, keys, certificates, and other sensitive data. |
| Tizen.Sensor       | Provides sensor types and sensor information. |
| Tizen.System       | Provides device-specific services, including status, system information and settings, control of haptic devices and sensor control and access. |
| Tizen.Telephony    | Provides call, modem, network, and SIM information. |
| Tizen.Uix          | Provides functions to recognize the speech and to synthesize voice from text and playing synthesized sound data. |
| Tizen.Webview      | Provides functions to access web pages and web contents. |
