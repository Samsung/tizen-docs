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

![Running Component-Based applications](./media/application_lifecycle.jpg)

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

You can control the Component-Based application execution by [monitoring and reacting to application state events](#application_monitoring).

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

![Running Frame-Component](./media/frame_lifecycle.jpg)


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

You can control the Frame-Component lifecycle by [monitoring and reacting to Frame-Component state events](#frame_component_monitoring).

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
| `frame_component_action_cb()` | Used to take necessary actions when another application sended launch request. To receive action event you should [register action](#register_action).|

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

![Running Service-Component](./media/service_lifecycle.jpg)


**Table: Service-Component states**

| State        | Description                         |
|--------------|-------------------------------------|
| `CREATE`      | Service-Component instance is created.            |
| `PROCESS COMMAND`    | Service-Component instance handling requested command.   |
| `DESTROY` | Service-Component instance is destroyed.          |


<a name="service_component_callbacks"></a>
## Service-Component Event Callbacks

You can control the Service-Component lifecycle by [monitoring and reacting to Service-Component state events](#service_component_monitoring).

The following table lists the Service-Component state change events.

**Table: Service-Component callbacks**

| Callback                     | Description                              |
|------------------------------|------------------------------------------|
| `service_component_create_cb()`    | Used to take necessary actions before the Service-Component instance's lifecycle starts. Place the initialization code here. It will be called once in the instance's lifecycle. |
| `service_component_restore_content_cb()`    | Used to restore instance's latest state. The data that stored in the last `service_component_save_content_cb` will be passed by parameter. |
| `service_component_start_command_cb()`    | Used to start instance. A requested `app_control_h` will be passed by parameter. |
| `service_component_save_content_cb()`    | Used to take necessary actions when there is some data need to be stored and restored for the next instnace launching. This callback will be called right before `service_component_destroy_cb`|
| `service_component_destroy_cb()` | Used to take necessary actions when the Frame-Component instance is terminating. Release all resources, especially any allocations and shared resources. |
| `service_component_action_cb()` | Used to take necessary actions when another application sended launch request.  To receive action event you should [register action](#register_action)|

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

- `main`

  The Component-Based Applications are able to have multiple components and there is one main component. The main component is the component that created when the Component-Based Application received launch request without specific component ID. You can set main component by set this attribute "true"


## Prerequisites

To use the functions and data types of the Component-Based Application API (in mobile and wearable applications), include the `<component_based_app.h>` header file in your application:

```
#include <component_based_app.h>
```

<a name="application_monitoring"></a>
## Run Component-Based Application

To run a Component-Based Application, you should register the Component-Based Application callbacks and start a main event loop as following codes:

```
component_class_h __app_create_cb(void *user_data)
{
     component_class_h comp_class = NULL;
    return comp_class;
}

void __app_terminate_cb(void *user_data)
{
}

int main(int argc, char** argv)
{
    int ret;
    component_based_app_lifecycle_callback_s callback = {
        .create = __app_create_cb,
        .terminate = __app_terminate_cb
    };

    ret = component_based_app_main(argc, argv, &callback, NULL);
    if (ret != APP_ERROR_NONE)
        return ret;

    return 0;
}
```

<a name="frame_component_monitoring"></a>
## Managing Frame-Component

To add and manage Frame-Component, you should add Frame-Component and registering Frame-Component callbacks.

1. Declaring a Frame-Component in the manifest file
    ```
    <component-based-application appid="org.tizen.base-component" exec="@BINDIR@/base-component" nodisplay="false" multiple="false" type="capp">
        <label>Base-component Application</label>
        <icon>@DESKTOP_ICON@</icon>
        <frame-component id="base-frame" launch_mode="caller" main="true" icon-display="false" taskmanage="true">
            <icon>org.tizen.sample.png</icon>
            <label>base-frame</label>
            <label xml:lang="en-us">base-frame</label>
            <label xml:lang="ko-kr">base-frame[KOR]</label>
        </frame-component>
    </component-based-application>
    ```

2. Adding a Frame-Component to the Component-Based Application
    ```
    component_class_h frame_component_add(component_class_h comp_class,
            const char *component_id, void *user_data)
    {
        frame_component_lifecycle_callback_s callback = {
            .create = __frame_component_create_cb,
            .start = __frame_component_start_cb,
            .resume = __frame_component_resume_cb,
            .pause = __frame_component_pause_cb,
            .stop = __frame_component_stop_cb,
            .destroy = __frame_component_destroy_cb,
            .restore_content = __frame_component_restore_content_cb,
            .save_content = __frame_component_save_content_cb,
            .action = __frame_component_action_cb,
            .device_orientation_changed = __frame_component_device_orientation_changed_cb,
            .language_changed = __frame_component_language_changed_cb,
            .region_format_changed = __frame_component_region_format_changed_cb,
            .low_battery = __frame_component_low_battery_cb,
            .low_memory = __frame_component_low_memory_cb,
            .suspended_state_changed = __frame_component_suspended_state_changed_cb,
        };

        return component_based_app_add_frame_component(comp_class,
                component_id, &callback, user_data);
    }

    component_class_h __app_create_cb(void *user_data)
    {
         component_class_h comp_class = NULL;
         comp_class = frame_component_add(comp_class, "base-frame", NULL);
        return comp_class;
    }

    void __app_terminate_cb(void *user_data)
    {
    }

    int main(int argc, char** argv)
    {
        int ret;
        component_based_app_lifecycle_callback_s callback = {
            .create = __app_create_cb,
            .terminate = __app_terminate_cb
        };

        ret = component_based_app_main(argc, argv, &callback, NULL);
        if (ret != APP_ERROR_NONE)
            return ret;

        return 0;
    }
    ```

<a name="service_component_monitoring"></a>
## Managing Service-Component

To add and manage Service-Component, you should add Service-Component and registering Service-Component callbacks.

1. Declaring a Service-Component in the manifest file
    ```
    <component-based-application appid="org.tizen.base-component" exec="@BINDIR@/base-component" nodisplay="false" multiple="false" type="capp">
        <label>Base-component Application</label>
        <icon>@DESKTOP_ICON@</icon>
        <service-component id="base-service" launch_mode="caller" main="false" icon-display="false" taskmanage="true">
            <icon>org.tizen.sample.png</icon>
            <label>base-service</label>
            <label xml:lang="en-us">base-service</label>
            <label xml:lang="ko-kr">base-service[KOR]</label>
        </service-component>
    </component-based-application>
    ```

2. Adding a Service-Component to the Component-Based Application
    ```
    component_class_h service_component_add(component_class_h comp_class,
            const char *component_id, void *user_data)
    {
        service_component_lifecycle_callback_s callback = {
            .create = __service_component_create_cb,
            .start_command = __service_component_start_command_cb,
            .destroy = __service_component_destroy_cb,
            .restore_content = __service_component_restore_content_cb,
            .save_content = __service_component_save_content_cb,
            .action = __service_component_action_cb,
            .device_orientation_changed = __service_component_device_orientation_changed_cb,
            .language_changed = __service_component_language_changed_cb,
            .region_format_changed = __service_component_region_format_changed_cb,
            .low_battery = __service_component_low_battery_cb,
            .low_memory = __service_component_low_memory_cb,
            .suspended_state_changed = __service_component_suspended_state_changed_cb,
        };

        return component_based_app_add_service_component(comp_class,
                component_id, &callback, user_data);
    }

    component_class_h __app_create_cb(void *user_data)
    {
         component_class_h comp_class = NULL;
         comp_class = frame_component_add(comp_class, "base-frame", NULL);
         comp_class = service_component_add(comp_class, "base-service", NULL);
        return comp_class;
    }

    void __app_terminate_cb(void *user_data)
    {
    }

    int main(int argc, char** argv)
    {
        int ret;
        component_based_app_lifecycle_callback_s callback = {
            .create = __app_create_cb,
            .terminate = __app_terminate_cb
        };

        ret = component_based_app_main(argc, argv, &callback, NULL);
        if (ret != APP_ERROR_NONE)
            return ret;

        return 0;
    }
    ```

<a name="register_action"></a>
## Managing Actions

The Component-Based Application can register actions and receive action event. You can send an action event to another application using app-control.

1. The app-control declaration in the manifest file
    ```
    <component-based-application appid="org.tizen.base-component" exec="@BINDIR@/base-component" nodisplay="false" multiple="false" type="capp">
        <label>Base-component Application</label>
        <icon>@DESKTOP_ICON@</icon>
        <app-control id="dial">
            <operation name="http://tizen.org/appcontrol/operation/dial"/>
            <mime name="*"/>
        </app-control>
        <app-control id="dial-for-excel">
            <operation name="http://tizen.org/appcontrol/operation/dial"/>
            <mime name="application/vnd.ms-excel"/>
        </app-control>
    ```

2.  Registering an action

    To receive action events, each component instance should register the action.
    You can registering an action as follows.
    ```
    static void __frame_component_action_cb(component_h context,
            const char *action, app_control_h app_control,
            void *user_data)
    {
    }

    static Evas_Object *__frame_component_create_cb(component_h context, void *user_data)
    {
        component_register_action(context, "dial-for-excel")
        return frame_get_window(ad->frame);
    }

    component_class_h app_control_component_add(component_class_h comp_class,
            const char *component_id, void *user_data)
    {
        frame_component_lifecycle_callback_s callback = {
            .create = __frame_component_create_cb,
            .action = __frame_component_action_cb,
        };

        return component_based_app_add_frame_component(comp_class,
                component_id, &callback, user_data);
    }
    ```

3.  Sending an action event to another application

    Actions are declared in the manifest files. To send a proper action, you should carefully set app-control values according to the manifest file app-control specification. In this example, the app-control will be set for "dial-for-excel" action.
    ```
    static int __app_control_send(const char *app_id, const char *component_id,
            void *user_data)
    {
        app_control_h handle = NULL;
        int ret;

        ret = app_control_create(&handle);
        if (ret != APP_CONTROL_ERROR_NONE)
            return ret;

        ret = app_control_set_operation(handle, "http://tizen.org/appcontrol/operation/dial");
        if (ret != APP_CONTROL_ERROR_NONE) {
            app_control_destroy(handle);
            return ret;
        }

        ret = app_control_set_mime(handle, "application/vnd.ms-excel");
        if (ret != APP_CONTROL_ERROR_NONE) {
            app_control_destroy(handle);
            return ret;
        }

        ret = app_control_send_launch_request_async(handle,
                __app_control_result_cb, NULL, user_data);
        if (ret != APP_CONTROL_ERROR_NONE) {
            app_control_destroy(handle);
            return ret;
        }
        return 0;
    }

    static void __button_clicked_cb(void *data, Evas_Object *obj,
        void *event_info) {
        __app_control_send("org.tizen.base-component", "base-frame", NULL);
    }
    ```


<a name="launch_application"></a>
## Launch a Component-Based Application

To launch a Component-Based Application:

1. Declaring launch privilege in the manifest file
    ```
    <?xml version="1.0" encoding="utf-8"?>
    <manifest xmlns="http://tizen.org/ns/packages" api-version="5.5" package="@PACKAGE_NAME@" install-location="internal-only" version="0.1.1">
        <label>Sample</label>
        <author email="tizenappfw@tizen.com" href="www.tizen.org">Tizen App Framework</author>
        <description>Sample</description>
        <ui-application appid="org.tizen.sample" exec="@BINDIR@/sample" nodisplay="false" multiple="false" type="capp" taskmanage="true" launch_mode="caller">
            <label>Sample</label>
            <icon>@DESKTOP_ICON@</icon>
        </ui-application>
        <privileges>
            <privilege>http://tizen.org/privilege/appmanager.launch</privilege>
        </privileges>
    </manifest>
    ```

2.  Sending launch request

    You can send launch request using app_control_h. The app_control_h will contains the Component-Based Application's ID and the component ID. The component ID is optional, if you do not set the component ID, then the main component instance will be created.

    You can launch a Component-Based application as follow.
    ```
    static int __app_control_send(const char *app_id, const char *component_id,
            void *user_data)
    {
        app_control_h handle = NULL;
        int ret;

        ret = app_control_create(&handle);
        if (ret != APP_CONTROL_ERROR_NONE)
            return ret;

        ret = app_control_set_app_id(handle, app_id);
        if (ret != APP_CONTROL_ERROR_NONE)
            return ret;

        if (component_id) {
            ret = app_control_set_component_id(handle, component_id);
            if (ret != APP_CONTROL_ERROR_NONE) {
                app_control_destroy(handle);
                return ret;
            }
        }

        ret = app_control_set_launch_mode(handle,
                APP_CONTROL_LAUNCH_MODE_GROUP);
        if (ret != APP_CONTROL_ERROR_NONE) {
            app_control_destroy(handle);
            return ret;
        }

        ret = app_control_send_launch_request_async(handle,
                __app_control_result_cb, NULL, user_data);
        if (ret != APP_CONTROL_ERROR_NONE) {
            app_control_destroy(handle);
            return ret;
        }

        return 0;
    }

    static void __button_clicked_cb(void *data, Evas_Object *obj,
        void *event_info) {
        __app_control_send("org.tizen.base-component", "base-frame", NULL);
    }
    ```

<a name="group_launch"></a>
## Group Launching Management

The Component-Based Application also provides an [application group feature](../app-management/app-controls.md#group). You can use it as follows.

1. Declaring launch privilege in the manifest file
    ```
    <component-based-application appid="org.tizen.base-component" exec="@BINDIR@/base-component" nodisplay="false" multiple="false" type="capp">
        <frame-component id="base-frame" launch_mode="caller" main="true" icon-display="false" taskmanage="true">
          <icon>org.tizen.sample.png</icon>
          <label>FrameComponent</label>
          <label xml:lang="en-us">FrameComponent</label>
          <label xml:lang="ko-kr">FrameComponent[KOR]</label>
        </frame-component>FrameComponent</label>
        <icon>FrameComponent.png</icon>
      </component-based-application>
      <privileges>
        <privilege>http://tizen.org/privilege/appmanager.launch</privilege>
      </privileges>
    </manifest>
    ```

2.  Sending launch request using component_h

    You have to send launch request with component_h so that application framework can tell which component instance request group launch.
    ```
    static void __launch_clicked_cb(void *user_data, Evas_Object *obj, void *event_info) {
        component_h context = (component_h)user_data;
        app_control_h handle = NULL;
        int ret;

        ret = app_control_create(&handle);
        if (ret != APP_CONTROL_ERROR_NONE)
            return;

        ret = app_control_set_app_id(handle, "org.tizen.group_app");
        if (ret != APP_CONTROL_ERROR_NONE) {
            app_control_destroy(handle);
            return;
        }

        ret = app_control_set_component_id(handle, "base-frame");
        if (ret != APP_CONTROL_ERROR_NONE)
            return;

        ret = app_control_set_launch_mode(handle, APP_CONTROL_LAUNCH_MODE_GROUP);
        if (ret != APP_CONTROL_ERROR_NONE) {
            app_control_destroy(handle);
            return;
        }

        ret = component_send_launch_request_async(context, handle,
                    __app_control_result_cb, NULL, NULL);
        if (ret != APP_CONTROL_ERROR_NONE) {
            app_control_destroy(handle);
            return;
        }
        app_control_destroy(handle);
    }
    ```

## Related Information
- Dependencies
  - Tizen 5.5 and Higher for Mobile
  - Tizen 5.5 and Higher for Wearable
