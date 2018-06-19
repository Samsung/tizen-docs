# Service Applications


Service applications are Tizen native applications with no graphical user interface that run in the background. They can be very useful in performing activities (such as getting sensor data in the background) that need to run periodically or continuously, but do not require any user intervention.

The main Service Application API features include:

- Application states

  A Tizen native service application has several different [states which it transitions through](#states) during its life-cycle.

- Event callbacks

  The service application can receive both basic system events and application state change events. You can register [callbacks for these events](#register) to react to them.

- Application behavior attributes

  You can [determine your application behavior](#attribute) at boot time and after abnormal terminations by using specific attributes which you can set in the application manifest file.

Service applications can be explicitly launched by a UI application. They can also be launched conditionally.

The user can check the running service applications in the task switcher; however, no events occur if the user selects a service application from the task switcher. The main menu does not contain icons for service applications. Multiple service applications can be running simultaneously with other service and UI applications.

<a name="states"></a>
## Application States

The following figure and table describe the service application states.

**Figure: Running service applications**

![Running service applications](./media/app_run.png)

**Table: Service application states**

| State        | Description                         |
|--------------|-------------------------------------|
| `READY`      | Application is launched.            |
| `CREATED`    | Application starts the main loop.   |
| `RUNNING`    | Application runs in the background. |
| `TERMINATED` | Application is terminated.          |

Because a service application has no UI, neither does it have a pause state. Since Tizen 2.4, the service application can go into the suspended state. Basically, the service application is running in the background by its nature; so the platform does not allow running the service application unless the application has a background category defined in its manifest file. However, when the UI application that is packaged with the service application is running on the foreground, the service application is also regarded as a foreground application and it can be run without a designated background category. For more information on using and defining a background category, see [Background Categories](efl-ui-app.md#allow_bg).

<a name="register"></a>
## Event Callbacks

You can control the service application execution by [monitoring and reacting to application state change and system events](#callback).

The following table lists the application state change events.

**Table: Application states**

| Callback                     | Description                              |
|------------------------------|------------------------------------------|
| `service_app_create_cb()`    | Used to take necessary actions before the main event loop starts. Place the initialization code (such as setting up the dbus connection) here. |
| `service_app_control_cb()`   | Used to take necessary actions when a service call arrives from another application. |
| `service_app_terminate_cb()` | Used to take necessary actions when the application is terminating. Release all resources, especially any allocations and shared resources, so that other running applications can fully any shared resources. |

The following table lists the system events.

**Table: System events**

| Callback                       | Description                              |
|--------------------------------|------------------------------------------|
| `service_app_low_memory_cb()`  | Used to take necessary actions in low memory situations.<br> Save data in the main memory to a persistent memory or storage, to avoid data loss in case the Tizen platform Low Memory Killer kills your application to get more free memory. Release any cached data in the main memory to secure more free memory. |
| `service_app_low_battery_cb()` | Used to take necessary actions in low battery situations.<br> Save data in the main memory to a persistent memory or storage, to avoid data loss in case the power goes off completely. Stop heavy CPU consumption or power consumption activities to save the remaining power. |

<a name="attribute"></a>
## Application Attributes

Describe your service application attributes in the manifest file. The attributes determine the application behavior. The following code example illustrates how you can define the attributes:

```
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns="http://tizen.org/ns/packages" package="org.tizen.message" version="0.2.7"
          install-location="internal-only">
   <label>Message</label>
   <description>Message Application</description>
   <service-application appid="org.tizen.message" exec="/usr/apps/org.tizen.message/bin/message"
                        nodisplay="true" multiple="false" type="capp" taskmanage="false">
      <icon>org.tizen.message.png</icon>
      <label>Message</label>
   </service-application>
</manifest>
```

Pay specific attention to the following attributes:

- `auto-restart`

  If set to `true`, the application restarts whenever it terminates abnormally. If the application is running, it is launched after installing or updating the package.

  > **Note**
  >
  > This attribute is not supported on Tizen wearable devices. Since Tizen 2.4, this attribute is not supported on all Tizen devices. Because of this, the `auto-restart` attribute used in a lower API version package than 2.4 is ignored on devices with the Tizen platform version 2.4 and higher.

- `on-boot`

  If set to `true`, the application launches on boot time, and after installing or updating the package. The application does not start if this attribute is removed after updating the package.

  > **Note**
  >
  > This attribute is not supported on Tizen wearable devices. Since Tizen 2.4, this attribute is not supported on all Tizen devices. Because of this, the `on-boot` attribute used in a lower API version package than 2.4 is ignored on devices with the Tizen platform version 2.4 and higher.

The following table defines the behaviors resulting from the attribute combinations:

**Table: Attribute combinations**

| `auto-restart` | `on-boot` | After normal termination   | On forced close            | On Reboot                           | After package installation | After package update       |
|----------------|-----------|----------------------------|----------------------------|-------------------------------------|----------------------------|----------------------------|
| `FALSE`        | `FALSE`   | Not launched automatically | Not launched automatically | Not launched after reboot           | Not launched               | Not launched automatically |
| `FALSE`        | `TRUE`    | Not launched automatically | Not launched automatically | Launched automatically after reboot | Launched                   | Launched automatically     |
| `TRUE`         | `FALSE`   | Launched automatically     | Launched automatically     | Not launched after reboot           | Not launched               | Launched automatically     |
| `TRUE`         | `TRUE`    | Launched automatically     | Launched automatically     | Launched automatically after reboot | Launched                   | Launched automatically     |

## Prerequisites

To use the functions and data types of the Service Application API (in [mobile](../../api/mobile/latest/group__CAPI__SERVICE__APP__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__SERVICE__APP__MODULE.html) applications), include the `<service_app.h>` header file in your application:

```
#include <service_app.h>
```

<a name="callback"></a>
## Monitoring Events

To monitor application state change and system events:

1. Add callbacks for application state change events:

   - Service application initialization callback

     This callback is called when the application is launched. Use the callback to write the necessary initialization code, such as setting up the dbus connection.

     The callback returns a Boolean value. If there is a critical error during the launch, the return is `false`, thereby cancelling the launch. Otherwise, the return is `true`.

     ```
     bool
     service_app_create(void *data)
     {
         dlog_print(DLOG_DEBUG, LOG_TAG, "%s", __func__);

         return true;
     }
     ```

   - Service application termination callback

     This callback is called when the application terminates. Use the callback to release all resources, especially any allocations and shared resources used by other applications.

     The `service_app_exit()` function quits the application main loop internally.

     ```
     void
     service_app_terminate(void *data)
     {
         dlog_print(DLOG_DEBUG, LOG_TAG, "%s", __func__);
         service_app_exit();

         return;
     }
     ```

   - Service request callback

     This callback is called when the service application receives an `app_control` service request from another application.

     ```
     void
     service_app_control(app_control_h app_control, void *data)
     {
         dlog_print(DLOG_DEBUG, LOG_TAG, "%s", __func__);
         service_app_exit();

         return;
     }
     ```

2. Add callbacks for system events:

   - Low memory callback

     This callback is called when the device is low on memory.

     ```
     void
     service_app_low_memory_callback(void *data)
     {
         dlog_print(DLOG_DEBUG, LOG_TAG, "%s", __func__);
         service_app_exit();

         return;
     }
     ```

   - Low battery callback

     This callback is called when the device is low on battery power.

     ```
     void
     service_app_low_battery_callback(void *data)
     {
         dlog_print(DLOG_DEBUG, LOG_TAG, "%s", __func__);
         service_app_exit();

         return;
     }
     ```

3. Set the application state change event callbacks in the `service_app_event_callback_s` structure. The structure is passed to the function that starts the service application.

   You can register the system event callbacks with the `service_app_add_event_handler()` function.

   ```
   int
   main(int argc, char* argv[])
   {
       appdata_s ad = {0,};
       service_app_lifecycle_callback_s event_callback = {0,};

       dlog_print(DLOG_DEBUG, LOG_TAG, "%s", __func__);

       event_callback.create = service_app_create;
       event_callback.terminate = service_app_terminate;
       event_callback.app_control = service_app_control;

       dlog_print(DLOG_DEBUG, LOG_TAG, "service_app_main() is called.");

       return service_app_main(argc, argv, &event_callback, &ad);
   }
   ```

## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
