# Component-Based Applications


The Component-Based applications is one of the Tizen application model. It allows developers to create an application that provides multiple components in one process. In the Component-Based application model, components have two different types and each component type has it's own lifecycle. Developers are able to add components to the Component-Based applications and registered components will create instances when the Component-Based application receives launch request.

The main Service Application API features include:

- Application states

  A Tizen native Component-Based application has several different [states which it transitions through](#application_states) during its life-cycle.

- Application Event callbacks

  The Component-Based application can receive application state change events. You can register [callbacks for these events](#application_register) to react to them.

- Frame-Component states

  A Frame-Component has several different [states which it transitions through](#frame_component_states) during its life-cycle.

- Frame-Component Event callbacks

  The Component-Based application can receive Frame-Component state change events. You can register [callbacks for these events](#frame_component_callbacks) to react to them.

- Service-Component states

  A Service-Component has several different [states which it transitions through](#service_component_states) during its life-cycle.

- Service-Component Event callbacks

  The Component-Based application can receive Service-Component state change events. You can register [callbacks for these events](#service_component_callbacks) to react to them.

- Application behavior attributes

  You can [determine your application behavior](#attribute) at boot time and after abnormal terminations by using specific attributes which you can set in the application manifest file.


<a name="application_states"></a>
## Application States

The following figure and table describe the Component-Based application states.

**Figure: Running Component-Based applications**

![Running Component-Based applications](./media/app_run.png)

**Table: Component-Based application states**

| State        | Description                         |
|--------------|-------------------------------------|
| `READY`      | Application is launched.            |
| `CREATE`    | Application starts the main loop.   |
| `RUNNING`    | Application runs components. |
| `TERMINATE` | Application is terminated.          |

  > **Note**
  >
The Component-Based application is created with a first component create request and it will be terminated if there is no running instances.
In the `RUNNING` state, the Component-Based application create instances of registered components. Multiple intances can be created by one component.


<a name="application_register"></a>
## Application Event Callbacks

You can control the Component-Based application execution by monitoring and reacting to application state events.

The following table lists the application state change events.

**Table: Component-Based Application states**

| Callback                     | Description                              |
|------------------------------|------------------------------------------|
| `component_based_app_create_cb()`    | Used to take necessary actions before the main event loop starts. Place the initialization code (such as setting up the dbus connection) here. |
| `component_based_app_terminate_cb()` | Used to take necessary actions when the application is terminating. Release all resources, especially any allocations and shared resources, so that other running applications can fully any shared resources. |


<a name="frame_component_states"></a>
## Frame-Component States

The following figure and table describe the Frame-Component states.

**Figure: Running Frame-Component**

![Running Frame-Component](./media/app_run.png)


**Table: Frame-Component states**

| State        | Description                         |
|--------------|-------------------------------------|
| `CREATE`      | Frame-Component instance is created.            |
| `START`    | Frame-Component instance is started and ready to receive visibility events.   |
| `RESUME`    | Frame-Component instance is visible |
| `PAUSE`    | Frame-Component instance is invisible |
| `STOP`    | Frame-Component instance is stopped and stop receiving visibility events. |
| `DESTROY` | Frame-Component instance is destroyed.          |


<a name="frame_component_callbacks"></a>
## Frame-Component Event Callbacks

You can control the Frame-Component lifecycle by monitoring and reacting to Frame-Component state events.

The following table lists the Frame-Component state change events.

**Table: Frame-Component callbacks**

| Callback                     | Description                              |
|------------------------------|------------------------------------------|
| `frame_component_create_cb()`    | Used to take necessary actions before the Frame-Component instance's lifecycle starts. Place the initialization code here. It will be called once in the instance's lifecycle. |
| `frame_component_restore_content_cb()`    | Used to restore instance's latest state. The data that stored in the last `frame_component_save_content_cb` will be passed by parameter. |
| `frame_component_start_cb()`    | Used to start instance. A requested `app_control_h` will be passed by parameter. |
| `frame_component_resume_cb()`    | Used to take necessary actions when the application becomes visible. If you relinquish anything in the `frame_component_pause_cb()` callback, re-allocate those resources here before the application resumes. |
| `frame_component_pause_cb()`    | Used to take necessary actions when the application becomes invisible. For example, release memory resources so other applications can use them. |
| `frame_component_stop_cb()`    | Used to take necessary actions when the Frame-Component instance's window is lowered.  The window will be lowered when the Frame-Component window is not activated for a long time. |
| `frame_component_save_content_cb()`    | Used to take necessary actions when there is some data need to be stored and restored for the next instnace launching. This callback will be called right before `frame_component_destroy_cb`|
| `frame_component_destroy_cb()` | Used to take necessary actions when the Frame-Component instance is terminating. Release all resources, especially any allocations and shared resources. |
| `frame_component_action_cb()` | Used to take necessary actions when another application sended launch request. |


The Frame-Component intance also can receive some basic system events. The following table lists shows available system events callbacks.

**Table: Frame-Component system event callbacks**

| callback                             | Description                              |
|----------------------------------------|------------------------------------------|
| `frame_component_low_memory_cb`                 | Event type for the callback function that is responsible for saving data in the main memory to a persistent memory or storage to avoid data loss in case the Tizen platform Low Memory Killer kills your application to get more free memory. The callback function must also release any cached data in the main memory to secure more free memory. |
| `frame_component_low_battery_cb`                | Event type for the callback function that is responsible for saving data in the main memory to a persistent memory or storage to avoid data loss in case the power goes off completely. The callback function must also stop heavy CPU consumption or power consumption activities to save the remaining power. |
| `frame_component_device_orientation_changed_cb` | Event type for the callback function that is responsible for changing the display orientation to match the device orientation. |
| `frame_component_language_changed_cb`           | Event type for the callback function that is responsible for refreshing the display into the new language. |
| `frame_component_region_format_changed_cb`      | Event type for the callback function that is responsible for refreshing the display into the new time zone. |
| `frame_component_suspended_state_changed_cb`    | Event type for the callback function that is responsible for taking necessary actions before entering the suspended state or after exiting from the state. |



<a name="service_component_states"></a>
## Service-Component States

The following figure and table describe the Service-Component states.

**Figure: Running Service-Component**

![Running Service-Component](./media/app_run.png)


**Table: Service-Component states**

| State        | Description                         |
|--------------|-------------------------------------|
| `CREATE`      | Service-Component instance is created.            |
| `PROCESS COMMAND`    | Service-Component instance handling requested command.   |
| `DESTROY` | Service-Component instance is destroyed.          |


<a name="service_component_callbacks"></a>
## Service-Component Event Callbacks

You can control the Service-Component lifecycle by monitoring and reacting to Service-Component state events.

The following table lists the Service-Component state change events.

**Table: Service-Component callbacks**

| Callback                     | Description                              |
|------------------------------|------------------------------------------|
| `service_component_create_cb()`    | Used to take necessary actions before the Service-Component instance's lifecycle starts. Place the initialization code here. It will be called once in the instance's lifecycle. |
| `service_component_restore_content_cb()`    | Used to restore instance's latest state. The data that stored in the last `service_component_save_content_cb` will be passed by parameter. |
| `service_component_start_command_cb()`    | Used to start instance. A requested `app_control_h` will be passed by parameter. |
| `service_component_save_content_cb()`    | Used to take necessary actions when there is some data need to be stored and restored for the next instnace launching. This callback will be called right before `service_component_destroy_cb`|
| `service_component_destroy_cb()` | Used to take necessary actions when the Frame-Component instance is terminating. Release all resources, especially any allocations and shared resources. |
| `service_component_action_cb()` | Used to take necessary actions when another application sended launch request. |

The Service-Component intance also can receive some basic system events. The following table lists shows available system events callbacks.

**Table: Service-Component system event callbacks**

| Callback                             | Description                              |
|----------------------------------------|------------------------------------------|
| `service_component_low_memory_cb`                 | Event type for the callback function that is responsible for saving data in the main memory to a persistent memory or storage to avoid data loss in case the Tizen platform Low Memory Killer kills your application to get more free memory. The callback function must also release any cached data in the main memory to secure more free memory. |
| `service_component_low_battery_cb`                | Event type for the callback function that is responsible for saving data in the main memory to a persistent memory or storage to avoid data loss in case the power goes off completely. The callback function must also stop heavy CPU consumption or power consumption activities to save the remaining power. |
| `service_component_device_orientation_changed_cb` | Event type for the callback function that is responsible for changing the display orientation to match the device orientation. |
| `service_component_language_changed_cb`           | Event type for the callback function that is responsible for refreshing the display into the new language. |
| `service_component_region_format_changed_cb`      | Event type for the callback function that is responsible for refreshing the display into the new time zone. |
| `service_component_suspended_state_changed_cb`    | Event type for the callback function that is responsible for taking necessary actions before entering the suspended state or after exiting from the state. |



<a name="attribute"></a>
## Application Attributes

Describe your Component-Based application attributes in the manifest file. The attributes determine the application behavior. The following code example illustrates how you can define the attributes:

```
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns="http://tizen.org/ns/packages" api-version="5.5" package="@PACKAGE_NAME@" install-location="internal-only" version="0.1.1">
	<label>Sample</label>
	<author email="tizenappfw@samsung.com" href="www.samsung.com">Tizen App Framework</author>
	<description>Sample</description>
	<component-based-application appid="org.tizen.base-component" exec="@BINDIR@/base-component" nodisplay="false" multiple="false" type="capp">
		<label>Base-component Application</label>
		<icon>@DESKTOP_ICON@</icon>
		<service-component id="base-service" main="false">
			<label>base-service</label>
		</service-component>
		<frame-component id="base-frame" launch_mode="caller" main="true" icon-display="false" taskmanage="true">
			<icon>org.tizen.sample.png</icon>
			<label>base-frame</label>
			<label xml:lang="en-us">base-frame</label>
			<label xml:lang="ko-kr">base-frame[KOR]</label>
		</frame-component>
	</component-based-application>
	<privileges>
		<privilege>http://tizen.org/privilege/appmanager.launch</privilege>
	</privileges>
</manifest>

```

Pay specific attention to the following attributes:

- `id`

  Every component element has id attribute. The id has to be globally unique in device. If not, application installation would be failed. And this attribute will be used by other applications to tell which component should be created.

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
