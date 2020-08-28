# Application Management

The application management features cover the various methods how to set or get appliction properties. They describe the application resources, preference, and icons. You can also use other application's functionlity using common application controls.

You can use the following application information and controls features in your native applications:

- [Application Resources](app-resources.md)

  You can define different resources to be used by the application depending on the device on which the application is run. Efficient resource management allows you to create an application that can be run on various devices with different configurations, such as different screen sizes.

- [Application Preferences](app-preferences.md)

  You can set and get application preferences. You can also share stored preference data among applications in the same package.

- [Application Icons](app-icons.md)

  You can show the application icon as a shortcut on the home screen to allow the user to easily access it. In the device application list, you can show a badge with the application icon to provide additional information about the application state or notifications to the user.

- [Application Controls](app-controls.md)

  The application controls allow you to share an application's functionality. Using another application's features through application controls reduces the time and effort needed to develop your own application. You can also allow other applications to share your functionality by exporting your application control functionalities.

- [Common Application Controls](common-appcontrols.md)

  The common application introduces the required parameters, such as a specific operation, URI, MIME type, and extra data when the application launches other applications with App Control API.

- [Component Manager](component-manager.md)

  You can retrieve information about the components installed on the device. You can also get information about the currently running components.

- [Application Manager](app-manager.md)

  You can retrieve information about the applications installed on the device. You can also get information about the currently-running application.

- [Package Manager](package-manager.md)

  You can retrieve information about the packages installed on the device. You can also monitor for changes in the device packages.

- [Event Broadcast and Subscription](event.md)

  You can use events to advertise your application activities, or listen for events from other applications or the system. You can broadcast events from your application to all who want to listen. You can also subscribe to events to keep track of what is happening in the system or other applications.

You can use the following application data exchange features in your native applications:

- [Message Port](message-port.md)

  Applications communicate with each other using message ports. You can send and receive messages using the map data format and trusted or untrusted message port instances.

- [Data Control](data-control.md)

  You can exchanging SQL- or key-value-type data between applications. All applications can request data shared by other applications, but only service applications can provide their own data.

- [Data Bundle](data-bundles.md)

  You can package data with a bundle, which is a string-based dictionary abstract data type. You can create bundles, manage their content, access their content through iteration, and encode and decode them.

- [PRC Port](rpc-port.md)

  Tizen applications can communicate with each other using RPC Port APIs, which allows applications to send and receive data after a connection is established.

- [TIDL](tidl.md)

  You can define interface with TIDL, which is a programming language to define interfaces for communicating among applications in Tizen.

- [Sticker](sticker.md)

  You can provide sticker information to an application that wants to read the sticker information, as a standard method. You can also retrieve the sticker information stored by the provider application.

- [Widget Viewer](widget-viewer.md)

  You can display Tizen widget applications, manage life-cycle of its instances, and retrieve widget information.

## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
