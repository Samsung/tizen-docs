# UI Application

The UI application is the most common Tizen .NET application model, described below are the UI applications:

  - [Basic UI Application](ui-app.md)

    A basic UI application provides a graphical user interface which allows the user to interact with the application.

  - [Component Based Application](component-based-app.md)

    A component based application provides a way to implement multiple model applications. It means you can provide multiple service components, frame components, and widget components in one application process. The frame component has a window and a life cycle to manage the user interfaces. The service component does not have a window and runs in the background. The widget component has widget instances. Every registered component can create multiple instances.

  - [Application Life Cycle](application_lifecycle.md)

    The Tizen .NET application model handles application life cycle and system events. It provides methods to manage the main event loop and the application state change.

  - [Watch Application](watch-app.md) **in wearable applications only**

    A watch application provides a watch face with the current time (updated every second) as its user interface.

    The watch application is available for wearable devices only, and it is shown on the idle screen of the device. For low-powered wearable devices, the watch application supports a special ambient mode. The ambient mode reduces power consumption by showing a limited UI and updating the time on the screen only once per minute.

  - [Widget Application](widget-app.md)

    A widget application (or widget) is a specialized application that provides the user with a quick view of specific information from the parent application. In addition, the widget allows the user to access certain features without launching the parent application. Combined with the parent application, your widget can have various features to increase the usability of your application.

## Related information
- API Reference
  - [Tizen.NUI.NUIApplication](/application/dotnet/api/TizenFX/latest/api/Tizen.NUI.NUIApplication.html) class
  - [Tizen.Applications.CoreUIApplication](/application/dotnet/api/TizenFX/latest/api/Tizen.Applications.CoreUIApplication.html) class
  - [Tizen.NUI.NUIWidgetApplication](/application/dotnet/api/TizenFX/latest/api/Tizen.NUI.NUIWidgetApplication.html) class
  - [Tizen.Applications.WidgetApplication](/application/dotnet/api/TizenFX/latest/api/Tizen.Applications.WidgetApplication.html) class
  - [Tizen.NUI.NUIWatchApplication](/application/dotnet/api/TizenFX/latest/api/Tizen.NUI.NUIWatchApplication.html) class
  - [Tizen.Applications.WatchApplication](/application/dotnet/api/TizenFX/latest/api/Tizen.Applications.WatchApplication.html) class
  - [Tizen.Applications.ComponentBased.Common.ComponentBasedApplication](/application/dotnet/api/TizenFX/latest/api/Tizen.Applications.ComponentBased.Common.ComponentBasedApplication.html) class
  - [Tizen.Applications.Application](/application/dotnet/api/TizenFX/latest/api/Tizen.Applications.Application.html) class
