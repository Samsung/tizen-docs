# Application Management

The application management features cover application resources, the communication methods available for the application, and getting application information.

You can use the following application management features in your .NET applications:

- [Application Icons](app-icons.md)

  You can show the application icon as a shortcut on the home screen to allow the user to easily access it. In the device application list, you can show a badge with the application icon to provide additional information about the application state or notifications to the user.

- [Application Controls](app-controls.md)

  The application controls allow you to share an application's functionality. Using another application's features through application controls reduces the time and effort needed to develop your own application. You can also allow other applications to share your functionality by exporting your application control functionalities.

- [Application Manager](app-manager.md)

  You can retrieve information about the applications installed on the device. You can also get information about the currently-running application.

- [Event Manager](event.md)

  You can use events to advertise your application activities. You can also listen to events from other applications or from other systems. You can broadcast events from your application to all listeners who want to listen. You can also subscribe to events to keep track of what is happening in the system or other applications.

- [Component Manager](component-manager.md)

  You can retrieve information about the components installed on the device. You can also get information about the currently running components.

- [Package Manager](package-manager.md)

  You can retrieve information about the packages installed on the device. You can also monitor for changes in the device packages.

- [Widget Control](widget-control.md)

  You can send update requests to the widget applications. You can also listen widget lifecycle events, and retrieve details of running instance for the same package widget applications.

The application can communicate with other applications in various ways. You can exchange data between applications through message ports and data controls.

You can use the following application data exchange features in your .NET applications:

-   [Message Port](message-port.md)

    Applications communicate with each other using message ports. You can send and receive messages using the map data format and trusted or untrusted message port instances.

-   [Data Control](data-control.md)

    You can exchange SQL- or key-value-type data between applications. All applications can request data shared by other applications, but only service applications can provide their own data.


## Related Information
- Dependencies
  - Tizen 4.0 and Higher
