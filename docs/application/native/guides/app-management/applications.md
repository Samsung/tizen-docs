# Applications

A Tizen native application is similar to a conventional Linux application, with some additional features optimized for mobile and wearable devices. The additional features have constraints, such as a relatively small screen size and lack of system resources compared to a larger system. For example, for power management reasons, the application can take actions to reduce usage when it finds out that it has its display window covered over by another application window. State change events are delivered to make it possible to detect these situations.

## Native Application Models

Tizen provides various application models to allow you to create applications targeted for specific tasks:

- [UI Applications](ui-app/index.md)

  The UI application has a graphical user interface. You can create diverse applications with a variety of features, and design versatile applications and intriguing user interfaces with text and graphics while taking advantage of many device functionalities, such as sensors and call operations. In addition, you can, for example, manage content and media files, use network and social services, and provide messaging and embedded Web browsing functionality.

  The UI application is the most common Tizen application model.

- [Service Applications](service-app.md)

  The service application is a Tizen native application without a graphical user interface that runs in the background. They can be very useful in performing activities (such as getting sensor data in the background) that need to run periodically or continuously, but do not require any user intervention.

## Native Application Life-Cycle

The Tizen native application model handles application life-cycle and system events. Tizen native application life-cycle is handled by the Application API (in [mobile](../../api/mobile/latest/group__CAPI__APPLICATION__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__APPLICATION__MODULE.html) applications). It provides functions to manage the main event loop, the application state change events, and basic system events.

Tizen supports both UI applications (which have a graphical user interface) and service applications (which have no graphical user interface). The UI and service applications can be packaged together, if necessary; however, a combined application package must contain only one UI application, while it can have several service applications.

Applications in the same package follow the same installation life-cycle, which is handled by the application package manager. Each application in the package follows its own application life-cycle. Each application (UI application or service application) in an application package can be identified by its own ID.

## Native Application State Change Callbacks

A Tizen native application can be in one of several different states. Typically, the application is launched by the user from the Launcher, or by another application. When the application is starting, the `app_create_cb()` function is executed and the main event loop starts. The application is normally at the top of the window, with focus.

When the application loses the focus status, the `app_pause_cb()` callback is invoked. The application can go into the pause state, which means that your application is not terminated but continues to run in the background, when:

- A new application is launched by the request of your application.
- The user requests to go to the home screen.
- A system event (such as an incoming phone call) occurs and causes a resident application with a higher priority to become active and temporarily hide your application.
- An alarm is triggered for another application, which becomes the topmost window and hides your application.

Since Tizen 2.4, an application in the background goes into a suspended state. In the suspended state, the application process is executed with limited CPU resources. In other words, the platform does not allow the running of the background applications, except for some exceptional applications (such as Media and Download) that necessarily work in the background. In this case, the application can [designate their background category as an allowed category](efl-ui-app.md#allow_bg) to avoid going into the suspended state.

When your application becomes visible again, the `app_resume_cb()` callback is invoked. The visibility returns, when:

- Another application requests your application to run (for example, the Task Navigator, which shows all running applications and lets the user select any application to run).
- All applications on top of your application in the window stack finish.
- An alarm is triggered for your application, bringing it to the front and hiding other applications.

When your application starts exiting, the `app_terminate_cb()` callback is invoked. Your application can start the termination process, when:

- Your application itself requests to exit by calling the `ui_app_exit()` or `service_app_exit()` function to terminate the event loop.
- The low memory killer is killing your application in a low memory situation.

The following figure shows the UI and service application states.

**Figure: UI and service application states**

![UI and service application life-cycle](./media/multiple_apps.png)

Because a service application has no UI, neither does it have a pause state. Since Tizen 2.4, a service application can go into the suspended state. Basically, the service application is running in the background by its nature; so the platform does not allow running the service application unless the application has a background category defined in its manifest file. However, when the UI application that is packaged with the service application is running on the foreground, the service application is also regarded as a foreground application and it can be run without a designated background category.

Application state changes are managed by the underlying framework. For more information on application state transitions, see [Application States and Transitions](efl-ui-app.md#state_trans).

## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
