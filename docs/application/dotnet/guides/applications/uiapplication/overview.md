# UI Application

The UI application is the most common Tizen .NET application model.

  - [Basic UI Application](ui-app.md)

    A basic UI application provides a graphical user interface which allows the user to interact with the application.

  - [Watch Application](watch-app.md) **in wearable applications only**

    A watch application provides a watch face with the current time (updated every second) as its user interface.

    The watch application is available for wearable devices only, and it is shown on the idle screen of the device. For low-powered wearable devices, the watch application supports a special ambient mode. The ambient mode reduces power consumption by showing a limited UI and updating the time on the screen only once per minute.

  - [Widget Application](widget-app.md)

    A widget application (or widget) is a specialized application that provides the user a quick view of specific information from the parent application. In addition, the widget allows the user to access certain features without launching the parent application. Combined with the parent application, your widget can have various features to increase the usability of your application.

  - [Component Based Application](component-based-app.md)

    A component based application provides a way to implement multiple model applications. It means you can provide multiple service components, frame components, and widget components in one application process. The frame component has a window and a lifecycle to manage the user interfaces. The service component does not have a window and runs in the background. The widget component has widget instances. Every registered component can create multiple instances.

  - [NUI Widget Application](nui-widget-app.md)

    A NUI Widget application is a widget application for NUI. It can be created using components of NUI.