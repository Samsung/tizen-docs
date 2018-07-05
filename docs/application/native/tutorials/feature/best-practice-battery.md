
# Best Practices for Location

If you want to create applications that offer reduced battery drain features to the user, Tizen provides various options for you.

Reducing the battery drain due to location services can remarkably save battery life on the device.

When creating applications with reduced battery drain, you can implement the following features:

-   [Managing life-cycles](#app_battery_lifecycle)
    -   To handle location information, you must understand the location service state change logic.
    -   To save battery life, you must know about the application life-cycle and how to synchronize it with the location service.
-   [Optimizing power consumption](#app_battery_power)
    -   You can select the optimal location method to reduce power consumption.
    -   You can start and stop a location service instance according to the application life-cycle changes, and destroy it when it is no longer needed.
    -   You can use a timeout or an alarm to stop the location service to save battery life when the location service is not available.
    -   You can use a callback to stop the location service when the battery is low.


<a name="app_battery_lifecycle"></a>
## Managing Life-cycles

Using the location received from GPS is potentially one of your application's most significant causes of battery drain. To minimize the battery drain associated with location service activities, it is critical that you understand the life-cycles of your application and location service, and synchronize the states between the 2 processes: location server and location application.

### Application Life-cycle

The Tizen native application can be in one of several different states.  Typically, the application is launched by the user from the Launcher, or by another application. As the application is starting, the `app_create_cb()` callback is executed and the main event loop starts. The application now normally becomes the frontmost window, with focus.  When the application loses the frontmost or focus status, the `app_pause_cb()` callback is invoked and the application goes into a pause state. The pause state means that the application is not terminated, but is running in the background. When your application becomes visible again, the `app_resume_cb()` callback is invoked. When your application starts exiting, the `app_terminate_cb()` callback is invoked.

The application state changes are managed by the underlying framework. The following figure illustrates the application states.

**Figure: Application states**

![Application states](./media/multiple_apps.png)

The application states are described in the following table.

**Table: Application states**

| State        | Description                              |
|--------------|------------------------------------------|
| `READY`      | The application is launched.             |
| `CREATED`    | The application starts the main loop.    |
| `RUNNING`    | The application is running and visible to the user. |
| `PAUSED`     | The application is running but invisible to the user. |
| `TERMINATED` | The application is terminated.           |

Application state changes are managed by the underlying framework. For more information on application state transitions, see [Application States and Transitions](../../guides/app-management/efl-ui-app.md#application-states-and-transitions).

### Location Service Life-cycle

The location service is composed of a location daemon, known as the location server, that provides geographical location information received from the GPS chip, Wi-Fi location service, and mobile network cell tower information and the client API called by the applications.

The location server is alive while the device is turned on and working on the best effort basis to find the current location with various positioning sources by the location method requested by the client. The positioning sources fixing the current location are based on GNSS (Global Navigation Satellite System). GNSS includes systems, such as GPS (Global Positioning System) of USA, GLONASS (Global Orbiting Navigation Satellite System) of Russia, Galileo of Europe, Beidou of China, and QZSS (Quasi-Zenith Satellite System) of Japan, as well as Wi-Fi and mobile network cell tower information. Moreover, various sensors, such as the accelerometer, gyroscope, and compass, are used to determine the location.

The location server has several states according to the client requests.

**Table: Location states**

| State       | Description                              |
|-------------|------------------------------------------|
| Idle        | The location service daemon is waiting for requesting location. |
| Started     | The location service daemon is started to fix the location using GPS or WPS. |
| Unavailable | The location service temporarily unavailable. |
| Fixed       | The location is fixed by GPS or WPS.     |
| Stopped     | The location service is stopped. There are no clients requesting location. |
| Terminated  | The location service daemon is terminated. |

The running state is defined as all states except idle and terminated.  In the running state, power consumption is higher than in the other states because the server is working to find the location using various positioning sources.

The following figure illustrates the location service state changes.

**Figure: Location state changes**

![Location state changes](./media/location_states.png)

The location service can lose the current position temporarily although it provides continuous location information, for example, when the device goes through a tunnel or across an area where there are many buildings and skyscrapers. The device encounters the multipath phenomenon, which is when the signals coming from the positioning satellites bounce back and forth off building walls, making it difficult to fix the current location. The device can also lose the current location when it goes underground, where there are no Wi-Fi access points or mobile network cell tower information available. In this situation, the location state changes to unavailable.

### Life-cycle Synchronization

One good approach to optimizing power consumption is to synchronize the life-cycles of the application and the location service. When the application is paused, make sure that the location service is paused too. When the application is resumed, also resume the location service.

The following table shows how to synchronize the states between an application and location service.

**Table: State synchronization**

| Application state | Location state | Location state description            |
|-------------------|----------------|---------------------------------------|
| `READY`           | Idle           | Location handle has been initialized. |
| `CREATED`         | Idle           | Location handle has been created.     |
| `RUNNING`         | Started        | Location service is started.          |
| `RUNNING`         | Unavailable    | Location is not fixed yet.            |
| `RUNNING`         | Fixed          | Location is fixed.                    |
| `PAUSED`          | Stopped        | Location service has been stopped.    |
| `TERMINATED`      | Terminated     | Location handle has been destroyed.   |

<a name="app_battery_power"></a>
## Optimizing Power Consumption

To reduce power consumption, you must select the optimal location method for the location service to determine the device location. You must also carefully synchronize the application and location service states to ensure that the location service is only running when the application is on the foreground.

It is hard for the device to detect the location when the device is underground or there are no Wi-Fi APs or mobile network cell towers near the device. In those situations, it is better to stop the location service to save battery life. Otherwise, the life time of the device is dramatically reduced by consuming power in the hybrid or GPS mode.

### Selecting the Location Method

The power consumption and location accuracy vary depending on the location source. It is important for you to select the location method, as the location method decides which location sources are used to determine the device location.

The location service provides different methods for determining the location, as illustrated in the following table.

**Table: Location service methods**

| Method                    | Location source                 | Description                              |
|---------------------------|---------------------------------|------------------------------------------|
| `LOCATIONS_METHOD_HYBRID` | GPS, Wi-Fi AP, cell information | This method allows the device to use all location sources. It provides the best effort with the highest power consumption. |
| `LOCATIONS_METHOD_GPS`    | GPS                             | This method is used by navigation applications requiring high accuracy. The power consumption is lower than in the hybrid method but higher than in the WPS method. |
| `LOCATIONS_METHOD_WPS`    | Wi-Fi AP, cell information      | This method receives location information from an external positioning server that computes the approximate location based on the Wi-Fi AP or mobile network cell tower. It provides the lowest power consumption, and the weakest location accuracy. |

The following table shows approximately how much power is consumed by GPS in standalone mode, in the condition of no assistant GPS, such as a
SUPL (Secure User Plane Location) server.

**Table: GPS power consumption**

| Operation          | Power consumption | Description                              |
|--------------------|-------------------|------------------------------------------|
| Full acquisition   | 32~40 mA          | For the first fix, after 2 or 3 days have passed. |
| Tracking           | 13~16 mA          | For the first fix, while continuously tracking the location where the satellite signals are very strong. |
| Low power tracking | 3~5 mA            | GPS chipset supported in a low power mode. |

You must decide which method your application uses, based on the advantages and disadvantages:

-   Balance your need for accuracy with the amount of power you are willing to consume, and select the optimal location source for your application.
-   An application requiring high accuracy, such as navigation, must use a continuous location coming from GPS. In this case, the battery consumption is higher, but still recommended to achieve the best accuracy.

### Synchronizing Life-cycles

When using location services with your application, you can reduce power consumption by synchronizing the life-cycle of the location service to that of the application. Basically, create or destroy the location service at the same time as the application, and stop or restart the location service when the application is paused or resumed.

#### Required Privileges

To use the location service, the application must declare the required privileges in the `tizen-manifest.xml` file. For more information on the Tizen privileges, see [Security and API Privileges](../details/sec-privileges.md).

For this example, the application manifest must include the following privileges:

```xml
<privileges>
   <privilege>http://tizen.org/privilege/location</privilege>
   <privilege>http://tizen.org/privilege/appmanager.launch</privilege>
   <privilege>http://tizen.org/privilege/alarm.get</privilege>
   <privilege>http://tizen.org/privilege/alarm.set</privilege>
</privileges>
```

#### Creating and Destroying the Location Service

Create the location service after creating the application. When the application is terminated, destroy the location service.

```cpp
#include <locations.h>
#include <tizen.h>
#include <locations.h>

/* Main UI functions */
static Evas_Object*
create_panel_basic_content(Evas_Object *parent, appdata_s *ad)
{
    Evas_Object *table;

    table = elm_table_add(parent);
    elm_table_padding_set(table, 10, 0);

    /* Add button for starting location service */
    ad->create_btn = elm_button_add(table);
    evas_object_size_hint_weight_set(ad->create_btn, EVAS_HINT_EXPAND, EVAS_HINT_EXPAND);
    evas_object_size_hint_align_set(ad->create_btn, EVAS_HINT_FILL, EVAS_HINT_FILL);
    elm_object_text_set(ad->create_btn, "<font_size=30>Start</font_size>");
    elm_object_disabled_set(ad->create_btn, EINA_FALSE);
    evas_object_smart_callback_add(ad->create_btn, "clicked", _clicked_start_cb, ad);
    evas_object_show(ad->create_btn);
    elm_table_pack(table, ad->create_btn, 0, 0, 1, 1);

    ad->destroy_btn = elm_button_add(table);
    evas_object_size_hint_weight_set(ad->destroy_btn, EVAS_HINT_EXPAND, EVAS_HINT_EXPAND);
    evas_object_size_hint_align_set(ad->destroy_btn, EVAS_HINT_FILL, EVAS_HINT_FILL);
    elm_object_text_set(ad->destroy_btn, "<font_size=30>Stop</font_size>");
    elm_object_disabled_set(ad->destroy_btn, EINA_TRUE);
    evas_object_smart_callback_add(ad->destroy_btn, "clicked", _clicked_stop_cb, ad);
    evas_object_show(ad->destroy_btn);
    elm_table_pack(table, ad->destroy_btn, 1, 4, 1, 1);

    evas_object_show(table);

    return table;
}

static Evas_Object*
create_panel(Evas_Object *parent, appdata_s *ad)
{
    Evas_Object *panel;
    Evas_Object *grid;

    /* Panel */
    panel = elm_panel_add(parent);
    evas_object_show(panel);

    /* Grid */
    grid = elm_grid_add(panel);
    evas_object_size_hint_weight_set(grid, EVAS_HINT_EXPAND, EVAS_HINT_EXPAND);
    evas_object_size_hint_align_set(grid, EVAS_HINT_FILL, EVAS_HINT_FILL);
    elm_object_content_set(panel, grid);

    /* Panel basic content */
    ad->basic_content = create_panel_basic_content(grid, ad);
    evas_object_size_hint_weight_set(ad->basic_content, EVAS_HINT_EXPAND,
                                     EVAS_HINT_EXPAND);
    evas_object_size_hint_align_set(ad->basic_content, EVAS_HINT_FILL, EVAS_HINT_FILL);
    elm_grid_pack(grid, ad->basic_content, 3, 3, 94, 94);

    return panel;
}

/* Callback invoked by updating the position */
void
_position_updated_cb(double latitude, double longitude, double altitude,
                     time_t timestamp, void *data)
{
    char message[128];
    int ret = 0;
    appdata_s *ad = (appdata_s *) data;

    sprintf(message, "<align=left>[%ld] lat[%f] lon[%f] alt[%f] (ret=%d)\n</align>",
            timestamp, latitude, longitude, altitude, ret);
    elm_entry_entry_set(ad->entry, message);

    /* Stop the location service after updating the first position */
    stop_location_service(ad);
}

/* Create the location service */
static void
create_location_service(void *data)
{
    appdata_s *ad = (appdata_s *)data;
    location_h handle;
    int ret;

    /* Create the location service to use all positioning sources */
    ret = location_manager_create(LOCATIONS_METHOD_HYBRID, &manager);
    if (ret != LOCATIONS_ERROR_NONE) {
        dlog_print(DLOG_ERROR, LOG_TAG, "location_manager_create() failed.(%d)", ret);
    }
    else {
        ad->location = manager;
        ret = location_manager_set_position_updated_cb(manager, _position_updated_cb, 0,
                                                       (void *)manager);
    }
}

/* Destroy the location service */
static void
destroy_location_service(void *data)
{
    appdata_s *ad = (appdata_s *)data;
    int ret;

    ret = location_manager_destroy(ad->location);
    if (ret != LOCATIONS_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "location_manager_destroy() failed.(%d)", ret);
    else
        ad->location = NULL;
}

/* Callback invoked by creating an application */
static bool
app_create(void *data)
{
    appdata_s *ad = (appdata_s *)data;

    create_location_service(ad);

    /* Panel */
    panel = create_panel(grid, ad);

    return true;
}

/* Callback invoked by terminating an application */
static void
app_terminate(void *data)
{
    appdata_s *ad = (appdata_s *)data;

    /* Destroy the location handle */
    destroy_location_service(ad);
}

int
main(int argc, char *argv[])
{
    appdata_s ad;
    memset(&ad, 0x00, sizeof(appdata_s));

    ui_app_lifecycle_callback_s event_callback;
    memset(&event_callback, 0x00, sizeof(ui_app_lifecycle_callback_s));

    event_callback.create = app_create;
    event_callback.terminate = app_terminate;
    event_callback.pause = app_pause;
    event_callback.resume = app_resume;

    int ret = ui_app_main(argc, argv, &event_callback, &ad);
    if (ret != APP_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "ui_app_main() failed with error: %d", ret);

    return ret;
}
```

#### Starting and Stopping the Location Service

If you want to continuously track the location, stop the location service when the application is paused and restart it when the application is resumed.

```cpp
/* Start the location service */
static void
start_location_service(void *data)
{
    appdata_s *ad = (appdata_s *) data;

    ret = location_manager_start(ad->location);
    if (ret != LOCATIONS_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "location_manager_start() failed. (%d)", ret);
}

/* Stop the location service */
static void
stop_location_service(void *data)
{
    appdata_s *ad = (appdata_s *) data;

    ret = location_manager_stop(ad->location);
    if (ret != LOCATIONS_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "location_manager_stop() failed. (%d)", ret);
}

/* Callback invoked by user gesture */
static void
_clicked_start_cb(void *data, Evas_Object *obj EINA_UNUSED, void *event_info EINA_UNUSED)
{
    appdata_s *ad = (appdata_s *) data;
    char message[128];

    ret = location_manager_start(ad);
    sprintf(message, "<align=left>location service was started. (ret=%d\n)</align>", ret);
    elm_entry_entry_set(ad->entry, message);
}

/* Callback invoked by user gesture */
static void
_clicked_stop_cb(void *data, Evas_Object *obj EINA_UNUSED, void *event_info EINA_UNUSED)
{
    appdata_s *ad = (appdata_s *) data;

    ret = location_manager_stop(ad);
    elm_entry_entry_set(ad->entry, "<align=left>location service was stopped.</align>");
}

/* Callback invoked by pausing an application */
static void
app_pause(void *data)
{
    appdata_s *ad = (appdata_s *)data;

    stop_location_service(ad);
}

/* Callback invoked by resuming an application */
static void
app_resume(void *data)
{
    appdata_s *ad = (appdata_s *)data;

    start_location_service(ad);
}
```

### Handling the Location Unavailable State

You can save power by stopping the location service while the service is not available. You can do this by using a timeout, an alarm, or the low battery callback.

#### Using a Timeout

If you create a service application, you can stop the location service with an alarm and then restart the service after a specific time interval, because there are no pause and resume states for the service application. Finally, you can stop the location service when the current position is fixed after some seconds or minutes.

The following example demonstrates how you can stop the location service using the timer with the `ecore_timer_add()` function:

```cpp
#include <tizen.h>
#include <service_app.h>
#include "service.h" /* Auto-generated header file by the Tizen Studio */
#include <locations.h>
#include <Ecore.h>

struct appdata {
    location_manager_h location;
    Ecore_Timer *timer;
};
typedef struct appdata appdata_s;

/* Callback invoked by updating the position */
static void
_position_updated_cb(double latitude, double longitude, double altitude, time_t timestamp, void *data)
{
    dlog_print(DLOG_DEBUG, LOG_TAG, "[%ld] lat[%f] lon[%f] alt[%f]\n", timestamp,
               latitude, longitude, altitude);
}

/* Create the location service */
static void
create_location_service(void *data)
{
    appdata_s *ad = (appdata_s *)data;
    location_manager_h manager;
    int ret;

    ret = location_manager_create(LOCATIONS_METHOD_HYBRID, &manager);
    if (ret != LOCATIONS_ERROR_NONE) {
        dlog_print(DLOG_ERROR, LOG_TAG, "location_manager_create() failed.(%d)", ret);
    }
    else {
        ad->location = manager;
        ret = location_manager_set_position_updated_cb(manager, _position_updated_cb, 1,
                                                       (void *)manager);
    }
}

/* Destroy the location service */
static void
destroy_location_service(void *data)
{
    appdata_s *ad = (appdata_s *)data;
    int ret;

    if (ad->location) {
        ret = location_manager_destroy(ad->location);
        if (ret != LOCATIONS_ERROR_NONE)
            dlog_print(DLOG_ERROR, LOG_TAG,
                       "location_manager_destroy() failed.(%d)", ret);
        else
            ad->location = NULL;
    }
}

/* Stop the location service after updating the first position */
static void
stop_location_service(void *data)
{
    appdata_s *ad = (appdata_s *) data;
    int ret = 0;

    if (ad->location) {
        ret = location_manager_stop(ad->location);
        if (ret != LOCATIONS_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "location_manager_stop() failed: %d", ret);
        else
            dlog_print(DLOG_DEBUG, LOG_TAG, "location service was stopped.");
    }
}

/* Callback invoked by the expired timer */
static Eina_Bool
_timeout_cb(void *data)
{
    appdata_s *ad = (appdata_s *) data;

    /* Call stopping the location service when the specific time is expired */
    stop_location_service(ad);

    return ECORE_CALLBACK_CANCEL;
}

/* Start the location service and create a timer */
static void
start_location_service(void *data)
{
    appdata_s *ad = (appdata_s *) data;
    int ret = 0;

    ret = location_manager_start(ad->location);
    if (ad->location) {
        if (ret != LOCATIONS_ERROR_NONE)
            dlog_print(DLOG_ERROR, LOG_TAG, "location_manager_start() failed: %d", ret);
        else
            dlog_print(DLOG_DEBUG, LOG_TAG, "location service was started");
        /* Set the timeout */
        int TIMEOUT = 120;
        /* Create a timer and set a callback function called after TIMEOUT */
        Ecore_Timer *my_timer = ecore_timer_add(TIMEOUT, _timeout_cb, ad);
        if (my_timer != NULL)
            ad->timer = my_timer;
    }
}

bool
service_app_create(void *data)
{
    appdata_s *ad = (appdata_s *)data;

    create_location_service(&ad->location);
    if (ad->location)
        start_location_service(ad);

    return true;
}

void
service_app_terminate(void *data)
{
    appdata_s *ad = (appdata_s *)data;

    if (ad->location)
        destroy_location_service(ad);
    if (ad->timer)
        ecore_timer_del(ad->timer);

    return;
}


/* Assume that auto-generated functions from the Tizen Studio are here */

int
main(int argc, char* argv[])
{
    appdata_s ad = {0,};

    service_app_lifecycle_callback_s event_callback;
    app_event_handler_h handlers[5] = {NULL,};

    event_callback.create = service_app_create;
    event_callback.terminate = service_app_terminate;
    return service_app_main(argc, argv, &event_callback, &ad);
}
```

#### Using an Alarm

Tizen provides the Alarm API to trigger events whenever you want to. You can increase the life time of the device by stopping the location service with an alarm when you have no further need for the location information, or when the device cannot fix the current location for a long time because its location only has weak GPS satellite, Wi-Fi, and mobile network signals.

> **Note**
>
> The application control is supported in UI applications only, so the following example cannot be reused in service applications.


The following example demonstrates how you can stop the location service using an alarm:

```cpp
#include <tizen.h>
#include <service_app.h>
#include "service.h" /* Auto-generated header file by the Tizen Studio */
#include <locations.h>
#include <app_alarm.h>
#include <app_control.h>

/* Same as above example except for the following code */

struct appdata {
    location_manager_h location;
    int alarm_id;
};
typedef struct appdata appdata_s;

/* Stop the location service */
static void
stop_location_service(void *data)
{
    appdata_s *ad = (appdata_s *) data;
    int ret = 0;

    if (ad->location) {
        ret = location_manager_stop(ad->location);
        if (ret != LOCATIONS_ERROR_NONE)
            dlog_print(DLOG_ERROR, LOG_TAG, "location_manager_stop() failed: %d", ret);
        else
            dlog_print(DLOG_DEBUG, LOG_TAG, "location service was stopped.");
        if (ad->alarm_id) {
            alarm_cancel(ad->alarm_id);
            ad->alarm_id = 0;
        }
    }
}

/* Create an app control for the alarm */
static bool
_initialize_alarm(void *data)
{
    appdata_s *ad = (appdata_s *) data;

    int ret;
    /* Set the delay time */
    int DELAY = 120;
    int alarm_id;

    app_control_h app_control = NULL;
    ret = app_control_create(&app_control);
    ret = app_control_set_operation(app_control, APP_CONTROL_OPERATION_DEFAULT);

    /* Set app_id as the name of the application */
    ret = app_control_set_app_id(app_control, "org.example.clockui");

    /* Set the key ("location") and value ("stop") of a bundle */
    ret = app_control_add_extra_data(app_control, "location", "stop");

    /* In order to be called after DELAY */
    ret = alarm_schedule_once_after_delay(app_control, DELAY, &alarm_id);
    if (ret != ALARM_ERROR_NONE) {
        char *err_msg = get_error_message(ret);
        dlog_print(DLOG_ERROR, LOG_TAG,
                   "alarm_schedule_once_after_delay() failed.(%d)", ret);
        dlog_print(DLOG_INFO, LOG_TAG, "%s", err_msg);

        return false;
    }

    ad->alarm_id = alarm_id;

    ret = app_control_destroy(app_control);
    if (ret != APP_CONTROL_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "app_control_destroy() failed.(%d)", ret);
    else
        dlog_print(DLOG_DEBUG, LOG_TAG, "Set the triggered time with alarm_id: %d",
                   ad->alarm_id);

    return true;
}

/* Start the location service */
void
start_location_service(void *data)
{
    appdata_s *ad = (appdata_s *) data;
    int ret = 0;

    ret = location_manager_start(ad->location);
    if (ad->location) {
        if (ret != LOCATIONS_ERROR_NONE)
            dlog_print(DLOG_ERROR, LOG_TAG, "location_manager_start() failed: %d", ret);
        else
            dlog_print(DLOG_DEBUG, LOG_TAG, "location service was started");

        /* Create a app control for the alarm */
        ret = _initialize_alarm(ad);
    }
}

/* Callback invoked by calling an app control */
static void
app_control(app_control_h app_control, void *data)
{
    appdata_s *ad = (appdata_s *) data;
    char *value = NULL;

    dlog_print(DLOG_DEBUG, LOG_TAG, "app_control was called.");
    /* Check whether the key and value of the bundle are as expected */
    if (app_control_get_extra_data(app_control, "location",
                                   &value) == APP_CONTROL_ERROR_NONE) {
        if (!strcmp(value, "stop")) {
            if (ad->location)
                stop_location_service(ad);
        }
        free(value);
    }
}

/* Callback invoked by creating an application */
static bool
app_create(void *data)
{
    appdata_s *ad = data;

    create_base_gui(ad);

    create_location_service(ad);

    if (ad->location)
        start_location_service(ad);

    return true;
}

/* Callback invoked by terminating an application */
static void
app_terminate(void *data)
{
    /* Release all resources */
    appdata_s *ad = (appdata_s *)data;

    if (ad->location)
        destroy_location_service(ad);
}

/* Assume that auto-generated functions from the Tizen Studio are here */

int
main(int argc, char *argv[])
{
    appdata_s ad = {0,};
    int ret = 0;

    ui_app_lifecycle_callback_s event_callback = {0,};
    app_event_handler_h handlers[5] = {NULL,};

    event_callback.create = app_create;
    event_callback.terminate = app_terminate;
    event_callback.pause = app_pause;
    event_callback.resume = app_resume;
    event_callback.app_control = app_control;

    ret = ui_app_main(argc, argv, &event_callback, &ad);
    if (ret != APP_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "ui_app_main() is failed. err = %d", ret);

    return ret;
}
```

#### Using the Low Battery Callback

If you stop the location service when the device battery level becomes low, you can increase the life time of the device. You can stop the location service when the low battery callback is triggered. This is the best method for handling the location service in service applications.

The following example demonstrates how you can stop the location service when the device battery is low:

```cpp
/* Callback invoked by low battery event */
static void
service_app_low_battery(app_event_info_h event_info, void *user_data)
{
    /* APP_EVENT_LOW_BATTERY */
    appdata_s *ad = (appdata_s *) user_data;

    if (ad->location)
        stop_location_service(ad);
}

/* Assume that auto-generated functions from the Tizen Studio are here */

int
main(int argc, char* argv[])
{
    appdata_s ad = {0,};

    service_app_lifecycle_callback_s event_callback;
    app_event_handler_h handlers[5] = {NULL,};

    event_callback.create = service_app_create;
    event_callback.terminate = service_app_terminate;

    /* Set the callback for low battery event */
    service_app_add_event_handler(&handlers[APP_EVENT_LOW_BATTERY],
                                  APP_EVENT_LOW_BATTERY, service_app_low_battery, &ad);

    return service_app_main(argc, argv, &event_callback, &ad);
}
```
