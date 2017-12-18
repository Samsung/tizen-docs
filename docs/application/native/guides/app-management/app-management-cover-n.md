# Application Management
## Dependencies
- Tizen 2.4 and Higher for Mobile
- Tizen 2.3.1 and Higher for Wearable

The application management features cover the various application models available for native applications. They describe the application life-cycle and resources, and the communication methods available for the application.

You can use the following application management features in your native applications:

- [Applications](applications-n.md)
The application life-cycle consists of various states the application moves through based on system events and user actions. You can manage the application life-cycle through various state change and system events, enabling the application to transition smoothly through its event loop.Tizen provides various application models to allow you to create applications targeted for specific tasks. You can create UI applications to run on the foreground, and service applications to run in the background. You can also create specific applications to function as the watch face for the device clock, or as a widget available on the home screen.

- [Application Resources](app-resources-n.md)
You can define different resources to be used by the application depending on the device on which the application is run. Efficient resource management allows you to create an application that can be run on various devices with different configurations, such as different screen sizes.

- [Application Preferences](app-preferences-n.md)
You can set and get application preferences. You can also share stored preference data among applications in the same package.

- [Application Icons](app-icons-n.md)
You can show the application icon as a shortcut on the home screen to allow the user to easily access it. In the device application list, you can show a badge with the application icon to provide additional information about the application state or notifications to the user.

- [Application Controls](app-controls-n.md)
The application controls allow you to share an application's functionality. Using another application's features through application controls reduces the time and effort needed to develop your own application. You can also allow other applications to share your functionality by exporting your application control functionalities.

- [Application Data Exchange](app-communication-n.md)
The application can communicate with other applications in various ways. You can exchange data between applications through message ports and data controls, and use data bundles to package the data to be communicated.

- [Application Manager](app-manager-n.md)
You can retrieve information about the applications installed on the device. You can also get information about the currently-running application.

- [Package Manager](package-manager-n.md)
You can retrieve information about the packages installed on the device. You can also monitor for changes in the device packages.

- [Event Broadcast and Subscription](event-n.md)
You can use events to advertise your application activities, or listen for events from other applications or the system. You can broadcast events from your application to all who want to listen. You can also subscribe to events to keep track of what is happening in the system or other applications.