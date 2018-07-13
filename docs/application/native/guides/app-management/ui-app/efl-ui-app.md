# EFL Basic UI Application


To create an EFL basic UI application, you must:

- Define the [application fundamentals](#fundamentals), mainly the entry point and life-cycle callbacks.

  The entry point starts the event loop, which is mandatory for every Tizen native application. Within the event loop, the application can receive both basic system events and application state change events. You can register [callbacks for these events](#callback) to react to them.

- Manage [application states and transitions](#state_trans) during its life-cycle.

- Define a [background category](#allow_bg) for your application, if you want it to run in the background.

<a name="callback"></a>
## Event Callbacks

The following table lists the application state change events.

**Table: Application state change events**

| Callback             | Description                              |
|----------------------|------------------------------------------|
| `app_create_cb()`    | Used to take necessary actions before the main event loop starts. Place the UI generation code here to prevent missing any events from your application UI. |
| `app_pause_cb()`     | Used to take necessary actions when the application becomes invisible. For example, release memory resources so other applications can use them. Do not starve the foreground application that is interacting with the user. |
| `app_resume_cb()`    | Used to take necessary actions when the application becomes visible. If you relinquish anything in the `app_pause_cb()` callback, re-allocate those resources here before the application resumes. |
| `app_terminate_cb()` | Used to take necessary actions when the application is terminating. Release all resources, especially any allocations and shared resources, so that other running applications can fully use any shared resources. |

For more information, see [Application State and Transition Management](#state_trans).

To listen for system events, use the `ui_app_add_event_handler()` function. The system events are triggered with the `app_event_cb()` callback function. The following table lists the event types.

**Table: Event types**

| Event type                             | Description                              |
|----------------------------------------|------------------------------------------|
| `APP_EVENT_LOW_MEMORY`                 | Event type for the callback function that is responsible for saving data in the main memory to a persistent memory or storage to avoid data loss in case the Tizen platform Low Memory Killer kills your application to get more free memory. The callback function must also release any cached data in the main memory to secure more free memory. |
| `APP_EVENT_LOW_BATTERY`                | Event type for the callback function that is responsible for saving data in the main memory to a persistent memory or storage to avoid data loss in case the power goes off completely. The callback function must also stop heavy CPU consumption or power consumption activities to save the remaining power. |
| `APP_EVENT_DEVICE_ORIENTATION_CHANGED` | Event type for the callback function that is responsible for changing the display orientation to match the device orientation. |
| `APP_EVENT_LANGUAGE_CHANGED`           | Event type for the callback function that is responsible for refreshing the display into the new language. |
| `APP_EVENT_REGION_FORMAT_CHANGED`      | Event type for the callback function that is responsible for refreshing the display into the new time zone. |
| `APP_EVENT_SUSPENDED_STATE_CHANGED`    | Event type for the callback function that is responsible for taking necessary actions before entering the suspended state or after exiting from the state. (Supported since Tizen 2.4.) |

<a name="state_trans"></a>
## Application States and Transitions

The Tizen native application can be in one of several different [application states](applications.md#state_change).

The Application API defines 5 states with corresponding transition handlers. A state transition callback is triggered after each state change, whenever the application is created, starts running, or is paused, resumed, or terminated. The application must [react to each state change appropriately](#fundamentals).

**Table: Application states**

| State        | Description                              |
|--------------|------------------------------------------|
| `READY`      | Application is launched.                 |
| `CREATED`    | Application starts the main loop.        |
| `RUNNING`    | Application is running and visible to the user. |
| `PAUSED`     | Application is running but invisible to the user. |
| `TERMINATED` | Application is terminated.               |

The following figure illustrates the application state transitions.

**Figure: Application state transitions**

![Application state transitions](./media/app_state_transitions.png)

## Prerequisites

To use the functions and data types of the Application API (in [mobile](../../../api/mobile/latest/group__CAPI__APPLICATION__MODULE.html) and [wearable](../../../api/wearable/latest/group__CAPI__APPLICATION__MODULE.html) applications), include the `<app.h>` header file in your application:

```
#include <app.h>
```

<a name="fundamentals"></a>
## Handling the Application Fundamentals

The Application API is a simple framework all Tizen applications are based on. It only handles interactions between applications and the operating system. In order for an application to operate successfully, it must receive events from the platform. For this, it must start the main event loop - this is mandatory for all Tizen native applications.

To manage the application life-cycle:

1. Start the application with the `main()` function. It initializes the Application API and starts the main event loop with the `ui_app_main()` function. Before calling the `ui_app_main()` function, set up the `app_event_callback_s` structure variable, which is passed to the function.

   The following code is a minimal application using the Application API. It only builds and runs.

   ```
   int
   main(int argc, char *argv[])
   {
       /* Create a ui_app_lifecycle_callback_s object and initialize its contents to 0 */
       ui_app_lifecycle_callback_s event_callback = {0,};

       /* Run the application */
       return ui_app_main(&argc, &argv, &event_callback, NULL);
   }
   ```

2. Define the application state callbacks.

   The Application API has 2 classes of application state callbacks: those about the application life-cycle and those about the system.

   - Application life-cycle callbacks:
     - `create`: Called after the `ui_app_main()` function and used to initialize the UI.
     - `control`: Triggered when the application is started to do something. It can be called several times during the lifespan of an application, and it shows the screen for the action requested. It requires specific information given to the callback.
     - `terminate`: Saves work, releases resources, and exits.
     - `pause`: Sets the application window not visible and switches to a mode which uses less resources.
     - `resume`: Sets the application window to be visible again.
   - System-related events (handled with the `app_event_cb()` callback):
     - `APP_EVENT_LOW_MEMORY`: Used to save data in the main memory to a persistent memory or storage to avoid data loss in case the Tizen platform Low Memory Killer kills your application to get more free memory. The event is also used to release any cached data in the main memory to secure more free memory.
     - `APP_EVENT_LOW_BATTERY`: Used to save data in the main memory to a persistent memory or storage to avoid data loss in case the power goes off completely. The event is also used to stop heavy CPU consumption or power consumption activities to save the remaining power.
     - `APP_EVENT_DEVICE_ORIENTATION_CHANGED`: Used to change the display orientation to match the device orientation.
     - `APP_EVENT_LANGUAGE_CHANGED`: Used to refresh the display into a new language.
     - `APP_EVENT_REGION_FORMAT_CHANGED`: Used to refresh the display into a new time zone.

   The following example shows a basic application state callback implementation:

   ```
   /*
      Structure to store the data for application logic; it is given
      to each callback invoked through the Application API
   */
   struct appdata {
       char *several;
       char *fields;
   };
   typedef struct appdata appdata_s;

   static bool
   app_create(void *data)
   {
       /*
          Hook to take necessary actions before main event loop starts; this
          usually means initializing the UI and application data (the "data"
          parameter to this function)
       */

       appdata_s *ad = data;
       create_gui(ad);

       /* If this function returns true, the main loop starts */
       /* If this function returns false, the application is terminated */
       return true;
   }

   static void
   app_control(app_control_h app_control, void *data)
   {
       /*
          Handle the launch request, show the user the task requested through the
          "app_control" parameter (see the next step)
       */
   }

   static void
   app_pause(void *data)
   {
       /* Take necessary actions when application becomes invisible */
   }

   static void
   app_resume(void *data)
   {
       /* Take necessary actions when application becomes visible */
   }

   static void
   app_terminate(void *data)
   {
       /* Release all resources */
       appdata_s *ad = data;

       if (!ad)
           return;

       /*
          If specific steps are needed:
          destroy_gui(ad);
       */
   }

   int
   main(int argc, char *argv[])
   {
       appdata_s ad = {0,};
       ui_app_lifecycle_callback_s event_callback = {0,};

       /* Set the callbacks for the application logic */
       event_callback.create = app_create;
       event_callback.terminate = app_terminate;
       event_callback.pause = app_pause;
       event_callback.resume = app_resume;
       event_callback.app_control = app_control;

       /* Note the &ad below is how the struct is given to the callbacks */
       return ui_app_main(argc, argv, &event_callback, &ad);
   }
   ```

3. Define any required application controls. An app control is a mechanism through which the application receives additional information about why it was started and with which parameters.

   The application receives a handle to an app control object in the `app_control` callback. The `app_control_h` type is opaque and information can only be extracted from it through API functions, such as:

   - `app_control_get_operation()`: Retrieve a string describing which operation the application was started for.
   - `app_control_get_mime()`: Retrieve the MIME type of the data (such as image/jpg).
   - `app_control_get_app_extra_data()`: Get the string value associated with a given key.
   - `app_control_get_app_extra_data_array()`: Get the string array associated with a given key (first check with `app_control_is_extra_data_array()` whether the data associated with the key is an array).

   For other available functions, see the `app.h` header file.

   For more information on launching other applications from your application using application controls, see [Application Controls](../app-controls.md).

<a name="allow_bg"></a>
## Background Categories

Since Tizen 2.4, an application is not allowed to run in the background except when it is explicitly declared to do so. The following table lists the background categories that allow an application to run in the background.

<a name="allow_bg_table"></a>
**Table: Allowed background application policy**

| Background category            | Description                              | Related APIs                             | Manifest file \<background-category\> element value |
|--------------------------------|------------------------------------------|------------------------------------------|------------------------------------------|
| Media                          | Playing audio, recording, and outputting streaming video in the background | Multimedia API (in [mobile](../../../api/mobile/latest/group__CAPI__MEDIA__FRAMEWORK.html) and [wearable](../../../api/wearable/latest/group__CAPI__MEDIA__FRAMEWORK.html) applications) | `media`                                  |
| Download                       | Downloading data with the Tizen Download-manager API | Download API (in [mobile](../../../api/mobile/latest/group__CAPI__WEB__DOWNLOAD__MODULE.html) applications) | `download`                               |
| Background network             | Processing general network operations in the background (such as sync-manager, IM, and VOIP) | Sync Manager API (in [mobile](../../../api/mobile/latest/group__CAPI__SYNC__MANAGER__MODULE.html) applications), Socket, and Curl API (in [mobile](../../../api/mobile/latest/group__OPENSRC__CURL__FRAMEWORK.html) and [wearable](../../../api/wearable/latest/group__OPENSRC__CURL__FRAMEWORK.html) applications) | `background-network`                     |
| Location                       | Processing location data in the background | Location API (in [mobile](../../../api/mobile/latest/group__CAPI__LOCATION__FRAMEWORK.html) and [wearable](../../../api/wearable/latest/group__CAPI__LOCATION__FRAMEWORK.html) applications) | `location`                               |
| Sensor (context)               | Processing context data from the sensors, such as gesture | Sensor API (in [mobile](../../../api/mobile/latest/group__CAPI__SYSTEM__SENSOR__MODULE.html) and [wearable](../../../api/wearable/latest/group__CAPI__SYSTEM__SENSOR__MODULE.html) applications) | `sensor`                                 |
| IoT Communication/Connectivity | Communicating between external devices in the background (such as Wi-Fi and Bluetooth) | Wi-Fi (in [mobile](../../../api/mobile/latest/group__CAPI__NETWORK__WIFI__MODULE.html) and [wearable](../../../api/wearable/latest/group__CAPI__NETWORK__WIFI__MODULE.html) applications) and Bluetooth API (in [mobile](../../../api/mobile/latest/group__CAPI__NETWORK__BLUETOOTH__MODULE.html) and [wearable](../../../api/wearable/latest/group__CAPI__NETWORK__BLUETOOTH__MODULE.html) applications) | `iot-communication`                      |

### Describing the Background Category

An application with a background running capability must declare the background category in its manifest file:

```
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns="http://tizen.org/ns/packages" api-version="2.4" package="org.tizen.test" version="1.0.0">
   <ui-application appid="org.tizen.test" exec="text" type="capp" multiple="false" taskmanage="true" nodisplay="false">
      <icon>rest.png</icon>
      <label>rest</label>
      <!--For API version 2.4 and higher-->
      <background-category value="media"/>
      <background-category value="download"/>
      <background-category value="background-network"/>
   </ui-application>
   <service-application appid="org.tizen.test-service" exec="test-service" multiple="false" type="capp">
      <background-category value="background-network"/>
      <background-category value="location"/>
   </service-application>
</manifest>
```

> **Note**
>
> The `<background-category>` element is supported since the API version 2.4. An application with a `<background-category>` element declared can fail to be installed on devices with a Tizen version lower than 2.4. In this case, declare the background category as `<metadata key="http://tizen.org/metadata/background-category/<value>"/>`.
> ```
> <?xml version="1.0" encoding="utf-8"?>
> <manifest xmlns="http://tizen.org/ns/packages" api-version="2.3" package="org.tizen.test" version="1.0.0">
>    <ui-application appid="org.tizen.test" exec="text" type="capp" multiple="false" taskmanage="true" nodisplay="false">
>       <icon>rest.png</icon>
>       <label>rest</label>
>       <!--For API version lower than 2.4-->
>       <metadata key="http://tizen.org/metadata/background-category/media"/>
>       <metadata key="http://tizen.org/metadata/background-category/download"/>
>       <metadata key="http://tizen.org/metadata/background-category/background-network"/>
>    </ui-application>
>    <service-application appid="org.tizen.test-service" exec="test-service" multiple="false" type="capp">
>       <metadata key="http://tizen.org/metadata/background-category/background-network"/>
>       <metadata key="http://tizen.org/metadata/background-category/location"/>
>    </service-application>
> </manifest>
> ```
>
> The `<metadata key="http://tizen.org/metadata/bacgkround-category/<value>"/>` element has no effect on Tizen 2.3 devices, but on Tizen 2.4 and higher devices, it has the same effect as the `<background-category>` element.

The background category of your application can be specified in the [application project settings](../../../tutorials/process/setting-properties.md#manifest) in the Tizen Studio.

## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
