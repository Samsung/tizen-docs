# Applications

A Tizen .NET application is similar to a conventional C\# application, with some additional features optimized for Tizen devices. The additional features have constraints, such as a relatively small screen size and lack of system resources compared to a larger system. For example, for power management reasons, the application can take actions to reduce usage when it finds out that it has its display window covered over by another application window. State change events are delivered to make it possible to detect these situations.

<a name="app_models"></a>
## Tizen .NET Application Models

Tizen provides various application models to allow you to create applications targeted for specific tasks:

- UI Applications

  The UI application has a graphical user interface. You can create diverse applications with a variety of features, and design
  versatile applications and intriguing user interfaces with text and graphics while taking advantage of many device functionalities, such as sensors and call operations. In addition, you can, for example, manage content and media files, use network and social services, and provide messaging and embedded Web browsing functionality.

  The UI application is the most common Tizen .NET application model.

  - [Basic UI application](ui-app.md)

    A basic UI application provides a graphical user interface which allows the user to interact with the application.

  - [Watch application](watch-app.md) **in wearable applications only**

    A watch application provides a watch face with the current time (updated every second) as its user interface.

    The watch application is available for wearable devices only, and it is shown on the idle screen of the device. For low-powered wearable devices, the watch application supports a special ambient mode. The ambient mode reduces power consumption by showing a limited UI and updating the time on the screen only once per minute.

  - [Widget application](widget-app.md)

    A widget application (or widget) is a specialized application that provides the user a quick view of specific information from the parent application. In addition, the widget allows the user to access certain features without launching the parent application. Combined with the parent application, your widget can have various features to increase the usability of your application.
  
<a name="life-cycle"></a>
## Tizen .NET Application Life-Cycle

The Tizen .NET application model handles application life-cycle and system events. Tizen .NET application life-cycle is handled by the [Tizen.Applications](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Applications.html) namespace. It provides methods to manage the main event loop, the application state change events, and basic system events.

Applications in the same package follow the same installation life-cycle, which is handled by the application package manager. Each application in the package follows its own application life-cycle. Each application in an application package can be identified by its own ID.  

<a name="state_change"></a>
## Tizen .NET Application State Change Methods

A Tizen .NET application can be in one of several different states.  Typically, the application is launched by the user from the Launcher, or by another application. When the application is starting, the `OnCreate()` method is executed and the main event loop starts. The application is normally at the top of the window, with focus.

When the application loses the focus status, the `OnPause()` method is invoked. The application can go into the pause state, which means that your application is not terminated but continues to run in the background, when:

- A new application is launched by the request of your application.
- The user requests to go to the home screen.
- A system event (such as an incoming phone call) occurs and causes a resident application with a higher priority to become active and temporarily hide your application.
- An alarm is triggered for another application, which becomes the topmost window and hides your application.

The application in the background goes into a suspended state. In the suspended state, the application process is executed with limited CPU resources. In other words, the platform does not allow the running of background applications, except for some exceptional applications (such as Media and Download) that necessarily work in the background. In this case, you can [define a background category in the application manifest file](ui-app.md#allow_bg), to prevent the application from going into the suspended state.

When your application becomes visible again, the `OnResume()` method is invoked. The visibility returns, when:

- Another application requests your application to run (for example, the Task Navigator, which shows all running applications and lets the user select any application to run).
- All applications on top of your application in the window stack finish.
- An alarm is triggered for your application, bringing it to the front and hiding other applications.

When your application starts exiting, the `OnTerminate()` method is invoked. Your application can start the termination process, when:

- Your application itself requests to exit by calling the `Exit()` method to terminate the event loop.
- The low memory killer is killing your application in a low memory situation.

The following figure shows the UI application states.

**Figure: UI application states**

![UI application life-cycle](./media/ui_app_state_cs.png)

Application state changes are managed by the underlying framework. For
more information on application state transitions, see [Application
States and Transitions](ui-app.md#state_trans).


## Related Information
- Dependencies
  - Tizen 4.0 and Higher
