# UI Application

To create a basic UI application, you must:

-   Define the [application fundamentals](#fundamentals), mainly the
    entry point and life-cycle methods for event handling.

    The entry point starts the event loop, which is mandatory for every
    Tizen .NET application. Within the event loop, the application can
    receive both basic system events and application state
    change events. You can override the [methods triggered for these
    events](#callback) to react to them.

- Manage [application states and transitions](#state_trans) during the
    application life-cycle.
- Define a [background category](#allow_bg) for your application, if
    you want it to run in the background.


<a name="callback"></a>
## Event Handling

The following table lists the methods that are triggered when the
application state changes.

**Table: Application state change methods**

| Method          | Description                              |
|---------------|----------------------------------------|
| `OnCreate()`    | Used to take necessary actions before the main event loop starts. Place the UI generation code here to prevent missing any events from your application UI. |
| `OnPause()`     | Used to take necessary actions when the application becomes invisible. For example, release memory resources so other applications can use them. Do not starve the foreground application that is interacting with the user. |
| `OnResume()`    | Used to take necessary actions when the application becomes visible. If you relinquish anything in the `OnPause()` method, re-allocate those resources here before the application resumes. |
| `OnTerminate()` | Used to take necessary actions when the application is terminating. Release all resources, especially any allocations and shared resources, so that other running applications can fully use any shared resources. |

For more information, see [Application States and
Transitions](#state_trans).

To react to system events, override the methods that are triggered when
system events occur. The following table lists the related methods.

**Table: System event methods**

| Method                         | Description                              |
|------------------------------|----------------------------------------|
| `OnLowMemory()`                | This method is responsible for saving data in the main memory to a persistent memory or storage to avoid data loss in case the Tizen platform Low Memory Killer kills your application to get more free memory. The event handler must also release any cached data in the main memory to secure more free memory. |
| `OnLowBattery()`               | This method is responsible for saving data in the main memory to a persistent memory or storage to avoid data loss in case the power goes off completely. The method must also stop heavy CPU consumption or power consumption activities to save the remaining power. |
| `OnDeviceOrientationChanged()` | This method is responsible for changing the display orientation to match the device orientation. |
| `OnLocaleChanged()`            | This method is responsible for refreshing the display into the new language. |
| `OnRegionFormatChanged()`      | This method is responsible for refreshing the display into the new time zone. |

<a name="state_trans"></a>
## Application States and Transitions


The Tizen .NET application can be in one of several application states.

The
[Tizen.Applications](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Applications.html)
namespace defines 5 states with corresponding state change methods. A
state change method is triggered after each state change: whenever the
application is created, starts running, or is paused, resumed, or
terminated. The application must [react to each state change
appropriately](#fundamentals).

**Table: Application states**

| State        | Description                              |
|------------|----------------------------------------|
| `READY`      | Application is launched.                 |
| `CREATED`    | Application starts the main loop.        |
| `RUNNING`    | Application is running and visible to the user. |
| `PAUSED`     | Application is running but invisible to the user. |
| `TERMINATED` | Application is terminated.               |

The following figure illustrates the application state transitions.

**Figure: Application state transitions**

![Application state
transitions](./media/app_state_transitions_cs.png)


## Prerequisites

To use the methods and properties of the
[Tizen.Applications](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Applications.html)
namespace, include it in your application:

```
using Tizen.Applications;
```

<a name="fundamentals"></a>
## Handling the Application Fundamentals

The
[Tizen.Applications](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Applications.html)
namespace is a simple framework all Tizen .NET applications are based
on. It only handles interactions between applications and the operating
system. In order for an application to operate successfully, it must
receive events from the platform. For this, it must start the main event
loop - this is mandatory for all Tizen .NET applications.

To manage the application life-cycle:

1.  Make a class derived from the
    [Tizen.Applications.CoreUIApplication](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Applications.CoreUIApplication.html)
    class and start the application with the `Main()` method. The method
    initializes the application and starts the main event loop with the
    `Run()` method.

    The following code is a minimal application using the
    `Tizen.Applications` namespace. It only builds and runs.

    ```
    class App : CoreUIApplication
    {
        static void Main(string[] args)
        {
            /// Run the application
            App app = new App();
            app.Run(args);
        }
    }
    ```

2. Override the [methods triggered for application state changes and
    system events](#callback).

    The following example shows a basic implementation with overridden
    methods for application state change events:

    -   `OnCreate()`: Called after the `Run()` method and used to
        initialize the UI.
    -   `OnAppControlReceived()`: Triggered when the application is
        started to do something. It can be called several times during
        the lifespan of an application, and it shows the screen for the
        action requested. It requires specific information provided
        as parameters.
    -   `OnTerminate()`: Saves work, releases resources, and exits.
    -   `OnPause()`: Sets the application window not visible and
        switches to a mode which uses less resources.
    -   `OnResume()`: Sets the application window to be visible again.

    ```
    class App : CoreUIApplication
    {
        protected override void OnCreate()
        {
            /// Hook to take necessary actions before main event loop starts; this
            /// usually means initializing the UI

            base.OnCreate();
        }

        protected override void OnAppControlReceived(AppControlReceivedEventArgs e)
        {
            /// Handle the launch request, show the user the task requested through the
            /// "AppControlReceivedEventArgs" parameter

            base.OnAppControlReceived(e);
        }

        protected override void OnPause()
        {
            /// Take necessary actions when application becomes invisible

            base.OnPause();
        }

        protected override void OnResume()
        {
            /// Take necessary actions when application becomes visible

            base.OnResume();
        }

        protected override void OnTerminate()
        {
            /// Release all resources

            base.OnTerminate();
        }

        static void Main(string[] args)
        {
            App app = new App();
            app.Run(args);
        }
    }
    ```

3. Define any required application controls. The
    [Tizen.Applications.ReceivedAppControl](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Applications.ReceivedAppControl.html)
    class, derived from the
    [Tizen.Applications.AppControl](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Applications.AppControl.html)
    class, is a mechanism through which the application receives
    additional information about why it was started and with
    which parameters.

    The application receives a handle to an app control object in the
    `OnAppControlReceived()` method. The
    `Tizen.Applications.ReceivedAppControl` class is opaque and
    information can only be extracted from it through properties, such
    as:

    -   `Operation`: Retrieve a string describing which operation the
        application was started for.
    -   `Mime`: Retrieve the MIME type of the data, such as `image/jpg`.
    -   `ExtraData`: Retrieve the data associated with a given key,
        using the
        [Tizen.Applications.AppControl.ExtraDataCollection](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Applications.AppControl.ExtraDataCollection.html) class.
        First check whether the data is an array using the
        `IsCollection()` method of the
        `Tizen.Applications.AppControl.ExtraDataCollection` class.


<a name="allow_bg"></a>
## Background Categories

An application is not allowed to run in the background except when it is
explicitly declared to do so. The following table lists the background
categories that allow an application to run in the background.

**Table: Allowed background application policy**

| Background category            | Description                              | Related namespaces                       | Manifest file \<background-category\> element value |
|------------------------------|----------------------------------------|----------------------------------------|----------------------------------------|
| Media                          | Playing audio, recording, and outputting streaming video in the background | [Tizen.Multimedia](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Multimedia.html) | `media`                                  |
| Download                       | Downloading data with the classes and methods of the Tizen.Content.Download namespace | [Tizen.Content.Download](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Content.Download.html) | `download`                               |
| Background network             | Processing general network operations in the background (such as sync-manager, IM, and VOIP) | [Tizen.Account.SyncManager](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Account.SyncManager.html) | `background-network`                     |
| Location                       | Processing location data in the background | [Tizen.Location](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Location.html) <br> [Tizen.Location.Geofence](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Location.Geofence.html) <br> [Tizen.Maps](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Maps.html) | `location`                               |
| Sensor (context)               | Processing context data from the sensors, such as gesture | [Tizen.Sensor](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Sensor.html) | `sensor`                                 |
| IoT Communication/Connectivity | Communicating between external devices in the background (such as Wi-Fi and Bluetooth) | [Tizen.Network.WiFi](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.WiFi.html) <br> [Tizen.Network.Bluetooth](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Bluetooth.html) | `iot-communication`                      |

<a name="bg-category"></a>
### Describing the Background Category

An application with a background running capability must declare the
background category in its manifest file:

```
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns="http://tizen.org/ns/packages" api-version="4" package="org.tizen.example.TestApp" version="1.0.0">
   <profile name="common" />
   <ui-application appid="org.tizen.example.TestApp" exec="TestApp.dll" type="dotnet" multiple="false"
                   taskmanage="true" nodisplay="false" launch_mode="single">
     <label>TestApp</label>
     <icon>TestApp.png</icon>
     <background-category value="media"/>
     <background-category value="download"/>
     <background-category value="background-network"/>
   </ui-application>
</manifest>
```


## Related Information
  * Dependencies
    -   Tizen 4.0 and Higher
