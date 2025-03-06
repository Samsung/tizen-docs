# Applications

A Tizen .NET application is similar to a conventional C\# application, with some additional features optimized for Tizen devices. The additional features have constraints, such as relatively small screen size and lack of system resources compared to a larger system. For example, for power management reasons, the application can take action to reduce usage when it finds out that it has its display window covered over by another application window. State change events are delivered to make it possible to detect these situations.

<a name="app_models"></a>
## Tizen .NET application models

Tizen provides various application models to allow you to create applications targeted for specific tasks, which are described below:

- [UI Application](./uiapplication/overview.md)

  The UI application has a graphical user interface. You can create diverse applications with a variety of features, and design
  versatile applications and intriguing user interfaces with text and graphics while taking advantage of many device functionalities, such as sensors and call operations. In addition, you can, for example, manage content and media files, use network and social services, and provide messaging and embedded web browsing functionality.

- [Service Application](./service_application.md)

  The service application has no graphical user interface that runs in the background. They can be very useful in performing activities (such as getting sensor data in the background) that need to run periodically or continuously, but do not require any user intervention.

## Related information
- Dependencies
  - Tizen 4.0 and Higher
- API Reference
  - [Tizen.NUI.NUIApplication](/application/dotnet/api/TizenFX/latest/api/Tizen.NUI.NUIApplication.html) class
  - [Tizen.Applications.CoreUIApplication](/application/dotnet/api/TizenFX/latest/api/Tizen.Applications.CoreUIApplication.html) class
  - [Tizen.Applications.ServiceApplication](/application/dotnet/api/TizenFX/latest/api/Tizen.Applications.ServiceApplication.html) class
  - [Tizen.Applications.CoreApplication](/application/dotnet/api/TizenFX/latest/api/Tizen.Applications.CoreApplication.html) class
  - [Tizen.Applications.Application](/application/dotnet/api/TizenFX/latest/api/Tizen.Applications.Application.html) class
