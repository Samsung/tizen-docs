# Tizen .NET Features and Components

Tizen .NET enables you to build .NET applications with Xamarin.Forms and the Tizen .NET framework. Xamarin.Forms allows you to create a user interface. The TizenFX API provides numerous interfaces to the hardware in modern TV, mobile, wearable, and IoT devices.

**Figure: Tizen .NET architecture**

![Tizen .NET architecture](media/cs_overview.png)

Following are the main components of Tizen .NET:

## .NET Core

  .NET Core is a general-purpose development platform maintained by Microsoft and the .NET community on [GitHub](https://github.com/dotnet/core). It is a cross-platform that supports Windows&reg;, macOS, and Linux. It can be used in device, cloud, and embedded or IoT scenarios.

  .NET Core consists of the following parts:

  - The [.NET runtime](https://github.com/dotnet/coreclr), which provides basic services such as a type system, assembly loading, a garbage collector, and native interop.
  - A set of [framework libraries](https://github.com/dotnet/corefx), which provides primitive data types, application composition types, and fundamental utilities.
  - A [set of SDK tools](https://github.com/dotnet/cli) and [language compilers](https://github.com/dotnet/roslyn) that enables the base developer experience, available in the [.NET Core SDK](https://docs.microsoft.com/en-us/dotnet/articles/core/sdk).
  - The .NET application host, which is used to launch .NET Core applications. It selects and hosts the runtime, provides an assembly loading policy, and launches the application. The application host is also used to launch the SDK tools.

## Xamarin.Forms as UI framework

  Xamarin.Forms is a cross-platform UI toolkit, which allows you to efficiently create native user interface layouts that can be shared across iOS, Android&trade;, Windows Phone, and Universal Windows Platform (UWP) applications.

## TizenFX API

  Tizen .NET supports C# APIs, which exposes Tizen-specific features:

  - **Tizen.Account** provides CRUD (Create, Read, Update, Delete) account management functionality and the OAuth Core RFC 6749 protocol.
  - **Tizen.Applications** provides the Tizen application framework, including application state change events, inter-application messaging, and notification services.
  - **Tizen.Common** provides predefined color names.
  - **Tizen.Content** provides content management services such as files and media downloading, storing and indexing audio and video content, and associating content types with helper applications.
  - **Tizen.Location** manages geographical location services and geofencing.
  - **Tizen.Maps** provides methods to create map-aware applications.
  - **Tizen.Messaging** provides methods to receive push notifications.
  - **Tizen.Multimedia** interacts with media services, including audio playback, recording, and device policy.
  - **Tizen.Network** controls connectivity devices and retrieves network information.
  - **Tizen.NUI** (Natural User Interface) is a toolkit for creating applications with a rich GUI. The applications can run on a range of Tizen devices.
  - **Tizen.Security** provides access to secure storage for passwords, keys, certificates, and other sensitive data.
  - **Tizen.Sensor** provides sensor types and sensor information.
  - **Tizen.System** provides device-specific services, including status, system information and settings, feedback, and sensor control and access.
  - **Tizen.Telephony** provides call, modem, network, and SIM information.
  - **Tizen.Uix** provides methods to recognize speech, synthesize voice from text, and play synthesized sound data.
  - **Tizen.Log** provides methods to print log messages to the Tizen logging system.
  - **Tizen.Tracer** provides methods to write trace messages to the system trace buffer.