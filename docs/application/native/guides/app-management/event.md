# Event Broadcast and Subscription


The application can broadcast its own events to all listeners, and subscribe to events. The events can be either predefined system [events from the platform](#platform) (only platform modules can broadcast system events) or user-defined events (broadcast by UI and service applications).

The main features of the Event API are:

- Event publication

  You can [publish an event](#broadcast) using the `event_publish_app_event()` and `event_publish_trusted_app_event()` functions. The `event_publish_trusted_app_event()` function publishes a trusted event which can only be received by the application that has the same signature as the publishing application.

- Event subscription

  You can [subscribe to an event](#manage) using the `event_add_event_handler()` function. When no longer needed, unsubscribe the event with the `event_remove_event_handler()` function.

- Launch-On-Events

  Service applications can be [launched when a desired target event occurs](#launch).

The application can be suspended while in the background, causing a pause in event handling. Since the application cannot receive events in the suspended state, they are all delivered in series after the application exits the suspended state. Consider how to manage this situation and prevent the application from being flooded with events:

- To handle events in the background without going to a suspended state, [declare a background category](efl-ui-app.md#allow_bg).
- To avoid receiving any events that are triggered while the application is suspended, remove the event handler before entering the suspended state and add it back after exiting the suspended state. You can [manage the event handler](efl-ui-app.md#callback) addition and removal in the `APP_EVENT_SUSPENDED_STATE_CHANGED` event callback, which is triggered each time the application enters and exist the suspended state.

## Prerequisites

To enable your application to use the event functionality:

1. To use the functions and data types of the Event API (in [mobile](../../api/mobile/latest/group__CAPI__EVENT__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__EVENT__MODULE.html) applications), include the `<app_event.h>` header file in your application:

   ```
   #include <app_event.h>
   ```

2. To use Launch-On-Events in your application, define the `http://tizen.org/appcontrol/operation/launch_on_event` operation in the `tizen-manifest.xml` file.

   The URI name for the operation represents the event name in the Launch-On-Event format (`event://{Event_Name}`).

   ```
   <app-control>
      <operation name="http://tizen.org/appcontrol/operation/launch_on_event"/>
      <uri name="event://tizen.system.event.battery_charger_status"/>
   </app-control>
   ```

<a name="broadcast"></a>
## Publishing an Event

To publish an event to all listeners:

1. Create the callback for handling the event:

   ```
   static void
   user_event_cb(const char *event_name, bundle *event_data, void *user_data)
   {
       dlog_print(DLOG_INFO, LOG_TAG, "user_event_cb: %s \n", event_name);

       return;
   }
   ```

2. Register the event handler and create the bundle for handling the event data:

   ```
   int ret = EVENT_ERROR_NONE;
   event_handler_h event_handler;
   bundle *event_data = NULL;

   ret = event_add_event_handler("event.org.tizen.senderapp.user_event",
                                 user_event_cb, "CUSTOM_EVENT_KEY", &event_handler);

   if (ret != EVENT_ERROR_NONE)
       dlog_print(DLOG_ERROR, LOG_TAG, "err: [%d]", ret);

   event_data = bundle_create();

   ret = bundle_add_str(event_data, user_data_key, user_data);
   ```

3. Use the `event_publish_app_event()` function to publish the event:

   ```
   ret = event_publish_app_event("event.org.tizen.senderapp.user_event", event_data);

   if (ret != EVENT_ERROR_NONE)
       dlog_print(DLOG_ERROR, LOG_TAG, "err: [%d]", ret);
   ```

4. When no longer needed, free the bundle:

   ```
   ret = bundle_free(event_data);
   ```

<a name="manage"></a>
## Subscribing to an Event

To subscribe to a predefined system event or user-defined event:

1. Add an event handler.

   One event can have multiple event handlers, and one handler can be registered multiple times.

   - Add an event handler for a system event:

     ```
     static void
     battery_event_callback(const char *event_name, bundle *event_data, void *user_data)
     {
         /* event_name is the event name */
         dlog_print(DLOG_INFO, LOG_TAG, "event_name is [%s]", event_name);

         /* event_data is the event data, its type is bundle */
         char *battery_level_status = NULL;
         battery_level_status = bundle_get_val(event_data, EVENT_KEY_BATTERY_LEVEL_STATUS);
     }

     event_handler_h handler;

     /* Register the event handler */
     int ret = event_add_event_handler(SYSTEM_EVENT_BATTERY_LEVEL_STATUS,
                                       (event_cb)battery_event_cb, user_data, &handler);
     if (ret != EVENT_ERROR_NONE)
         dlog_print(DLOG_ERROR, LOG_TAG, "err: [%d]", ret);
     ```

   - Add an event handler for a user-defined event:

     When defining an event name for a user event (such as `event.org.tizen.senderapp.user_event`), the name format is `event.{sender appid}.{user-defined name}`. The `{user-defined name}` must:

     - Contain only the ASCII characters "[A-Z][a-z][0-9]_" and not begin with a digit.
     - Not contain the '.' (period) character.
     - Not exceed the maximum name length (127 bytes).
     - Be at least 1 byte in length.

     ```
     ret = event_add_event_handler("event.org.tizen.senderapp.user_event",
                                   utc_event_cb_with_valid_check,
                                   "CUSTOM_EVENT_KEY", &event_handler);

     if (ret != EVENT_ERROR_NONE)
         dlog_print(DLOG_ERROR, LOG_TAG, "err: [%d]", ret);
     ```

2. When no longer needed, remove the event handler.

   A registered handler can be removed when application is running, and all registered handlers are removed when the application is terminated.

   ```
   ret = event_remove_event_handler(handler);
   if (ret != EVENT_ERROR_NONE)
       dlog_print(DLOG_ERROR, LOG_TAG, "err: [%d]", ret);
   ```

<a name="launch"></a>
## Managing Launch-On-Events

To register an interest in a Launch-On-Event, define the `http://tizen.org/appcontrol/operation/launch_on_event` operation in the `tizen-manifest.xml` file.

> **Note**
>
> Only service applications can register and receive Launch-On-Events.
>
> The Launch-On-Event operation cannot be requested using the `app_control_send_launch_request()` function, unlike other application control operations.

The following table shows the system events that support Launch-On-Event.

**Table: System events supporting Launch-On-Event**

| Name                                     | Condition                                |
|------------------------------------------|------------------------------------------|
| `tizen.system.event.battery_charger_status` | When the charger state is `"connected"`. |
| `tizen.system.event.usb_status`          | When the USB state is `"connected"`.     |
| `tizen.system.event.earjack_status`      | When the earjack status is `"connected"`. |
| `tizen.system.event.incoming_msg`        | When the `msg_type` and `msg_id` exist.  |
| `tizen.system.event.wifi_state`          | When the Wi-Fi state is `"connected"`.   |

To receive the Launch-On-Event:

```
static void
*app_control(app_control_h app_control, void *data)
{
    char *event_uri = "event://tizen.system.event.battery_charger_status";
    char *operation;
    char *uri;
    char *event_value;
    ret = app_control_get_operation(app_control, &operation);

    if (ret == APP_CONTROL_ERROR_NONE && operation &&
        strcmp(operation, APP_CONTROL_OPERATION_LAUNCH_ON_EVENT) == 0) {
        ret = app_control_get_uri(app_control, &uri);
        if (ret == APP_CONTROL_ERROR_NONE && uri) {
            if (strncmp(uri, event_uri, strlen(event_uri) + 1) == 0) {
                ret = app_control_get_extra_data(app_control, "battery_charger_status", &event_value);
                if (ret == APP_CONTROL_ERROR_NONE && event_value)
                    free(event_value);
                /* Use event_add_event_handler() for further event subscriptions here */
            }
            free(uri);
        }
        free(operation);
    }
}
```

The application can get the event name and data in the first `app_control_cb()` callback, which is called after the application state changes to `created`.

<a name="platform"></a>
## Platform Event Types

The following table lists the platform event types.

**Table: Platform event types**

| Module | Category | Event name | Event data Key | Event data Value | Condition | Notes |
|--------|--------|--------|--------|--------|--------|--------|
| capi-system-device | battery      | `tizen.system.event.battery_charger_status` | `battery_charger_status`  | - `"disconnected"`: Charger is not connected<br>- `"connected"`: Charger is connected<br>- `"charging"`: Charging is enabled<br>- `"discharging"`: Charging is disabled (for example, 100% full  state) | When the  charger has been connected or disconnected, or when the charging state has  changed (charging or not). | If there is an  earlier occurrence regarding this event, you receive the event as soon as you  register an event handler for this event. You can use this earlier event data  as the initial value. |
| capi-system-device | battery      | `tizen.system.event.battery_level_status`  | `battery_level_status`    | - `"empty"` <br>- `"critical"` <br>- `"low"` <br>- `"high"` <br>- `"full"` | When the  battery level has changed.     | You can get the  current value with the `device_battery_get_level_status()` function. |
| deviced            | usb          | `tizen.system.event.usb_status`            | `usb_status`              | - `"disconnected"`:  USB cable is not connected<br>- `"connected"`: USB cable is connected, but the service is not  available<br>-  `"available"`: USB service is available (for example, mtp or SDB) | When the USB  cable has been connected or disconnected, or when the USB service state has  changed. | You can get the  current value with the `RUNTIME_INFO_KEY_USB_CONNECTED` key. |
| deviced            | earjack      | `tizen.system.event.earjack_status`       | `earjack_status`                 | - `"disconnected"`:  Earjack is not connected <br>- `"connected"`: Earjack is connected | When the  earjack connection state has changed. | You can get the  current value with the `RUNTIME_INFO_KEY_AUDIO_JACK_STATUS` key. |
| deviced            | display      | `tizen.system.event.display_state`         | `display_state`           | - `"normal"`:  Display on, normal brightness<br>- `"dim"`: Display on, dimmed brightness<br>- `"off"`: Display off | When the  display state has changed.     | You can get the  current value with the `device_display_get_state()` function. |
| systemd            | system       | `tizen.system.event.boot_completed`        | N/A                     | N/A                                      | When the  platform has completed booting. | You can treat  the initial value as `false`  before you receive this event. If the application is already in a  boot-completed state before you register an event handler, you receive the  event as soon as you register the event handler. |
| systemd            | system       | `tizen.system.event.system_shutdown`       | N/A                     | N/A                                      | When  the system power-off has been started. | You  can treat the initial value as `false` before you receive this event. If the application is already  in a shutting-down state before you register an event handler, you receive  the event as soon as you register the event handler. |
| resourced          | ram memory   | `tizen.system.event.low_memory`            | `low_memory`              | - `"normal"`:  Available > 200MB <br> - `"soft_warning"`: 100MB < available <= 200MB <br>- `"hard_warning"`: Available <= 100MB    <br> **Note**<br> The above numbers can vary depending on the total RAM size of the  target device. | When  the size of available memory has changed. | If  there is an earlier occurrence regarding this event, you receive the event as  soon as you register an event handler for this event. You can use this  earlier event data as the initial value. |
| network            | connectivity | `tizen.system.event.wifi_state`            | `wifi_state`              | - `"on"`:  Wi-Fi on <br>-  `"off"`: Wi-Fi off <br>- `"connected"`: Wi-Fi connection established | When the Wi-Fi  state has changed.       | You can get the  current value with the `connection_get_wifi_state()` function. |
| network            | connectivity | `tizen.system.event.bt_state`              | `bt_state`                | - `"off"`:  Legacy Bluetooth off <br>-  `"on"`: Legacy Bluetooth on | When the  Bluetooth state has changed.   | You can get the  current value with the `bt_adapter_get_state()` function. |
| network            | connectivity | `tizen.system.event.bt_state`              | `bt_le_state`             | - `"off"`:  LE function off <br>- `"on"`: LE function on | When Bluetooth  LE state has changed.    |   -                                       |
| network            | connectivity | `tizen.system.event.bt_state`              | `bt_transfering_state`    | - `"non_transfering"`:  Idle state  <br>-  `"transfering"`: File is transferring | When the file  transfer state has changed. | -                                         |
| libslp-location    | location     | `tizen.system.event.location_enable_state` | `location_enable_state`   | - `"disabled"`:  Location disabled <br>-  `"enabled"`: Location enabled | When the `location-enable_state` has been  changed, for example, by the user toggling the location setting in the  settings menu or quick panel. | You can get the  current value with the `location_manager_is_enabled_method()` function. |
| libslp-location    | location     | `tizen.system.event.gps_enable_state`      | `gps_enable_state`        | - `"disabled"`:  GPS disabled  <br>- `"enabled"`: GPS enabled | When the `gps-enable_state` has changed.   | You can get the  current value with the `location_manager_is_enabled_method()` function. |
| libslp-location    | location     | `tizen.system.event.nps_enable_state`      | `nps_enable_state`        | - `"disabled"`:  NPS disabled <br>-  `"enabled"`: NPS enabled | When the NPS  setting has been changed, for example, by the user toggling the location  settings. | You can get the  current value with the `location_manager_is_enabled_method()` function. |
| msg-service        | message      | `tizen.system.event.incoming_msg`          | `msg_type`                | - `"sms"`:  SMS-type message <br>-  `"push"`: Push-type message <br>-  `"cb"`: Cb-type message | When an SMS,  push, or CB message has been received. |       -                                   |
| msg-service        | message      | `tizen.system.event.incoming_msg`          | `msg_id`                  | `msg_id`: Message ID of the received message (string of the unsigned `int` type value) | -                                         |           -                               |
| alarm-manager      | time         | `tizen.system.event.time_changed`          | N/A                     | N/A                                      | When  the system time setting has changed. | You  can get the current value with the `alarm_get_current_time()` function. |
| setting            | time         | `tizen.system.event.time_zone`             | `time_zone`               | The  value of this key is the time zone value of the time zone database, for  example, "Asia/Seoul", "America/New_York". For more  information, see the IANA Time Zone Database. | When  the time zone has changed.         | You  can get the current value with the `SYSTEM_SETTINGS_KEY_LOCALE_TIMEZONE` key. |
| setting            | locale       | `tizen.system.event.hour_format`           | `hour_format`             | - `"12"` <br>- `"24"`                             | When  the `hour_format` has changed,  for example, by the user toggling the date and time settings for the 24-hour  clock (where **OFF** stands  for the 12-hour clock). | You  can get the current value with the `SYSTEM_SETTINGS_KEY_LOCALE_TIMEFORMAT_24HOUR` key. |
| setting            | locale       | `tizen.system.event.language_set`          | `language_set`            | The value of  this key is the full name of the locale, for example, `ko_KR.UTF8` for Korean and `en_US.UTF8` for American English. For more information, see the Linux  locale information. | When the `language_set` has changed.       | You can get the  current value with the `SYSTEM_SETTINGS_KEY_LOCALE_LANGUAGE` key. |
| setting            | locale       | `tizen.system.event.region_format`         | `region_format`           | The  value of this key is the full name of the locale, for example, `ko_KR.UTF8` for the Korean region  format and `en_US.UTF8`  for the USA region format. For more information, see the Linux locale  information. | When  the `region_format` has changed.     | You  can get the current value with the `SYSTEM_SETTINGS_KEY_LOCALE_COUNTRY` key. |
| setting            | sound        | `tizen.system.event.silent_mode`           | `silent_mode`             | - `"on"` <br> - `"off"`                            | When  the ringtone has been changed to 0 or another mode. For example, if the call  slider has been changed to 0, `silent_mode` is `"on"`. Otherwise, `silent_mode` is `"off"`. | You  can get the current value with the `SYSTEM_SETTINGS_KEY_SOUND_SILENT_MODE` key. |
| setting            | vibration    | `tizen.system.event.vibration_state`       | `vibration_state`         | - `"on"` <br> - `"off"`                           | When the  vibration state has changed.   | You can get the  current value with the `RUNTIME_INFO_KEY_VIBRATION_ENABLED` key. |
| setting            | screen       | `tizen.system.event.screen_autorotate_state` | `screen_autorotate_state` | - `"on"` <br> - `"off"`                       | When the `screen_autorotate_state` has been  changed, for example, by the user toggling the display settings. | You can get the  current value with the `SYSTEM_SETTINGS_KEY_DISPLAY_SCREEN_ROTATION_AUTO` key. |
| setting            | mobile       | `tizen.system.event.mobile_data_state`     | `mobile_data_state`       | - `"on"` <br> - `"off"`            | When the `mobile_data_state` has been changed,  for example, by the user toggling the network settings. | You can get the  current value with the `SYSTEM_SETTINGS_KEY_3G_DATA_NETWORK_ENABLED` key. |
| setting            | mobile       | `tizen.system.event.data_roaming_state`    | `data_roaming_state`      | - `"on"` <br> - `"off"`                   | When the `data_roaming_state` has been changed,  for example, by the user toggling the network settings. | You can get the  current value with the `RUNTIME_INFO_KEY_DATA_ROAMING_ENABLED` key. |
| setting            | font         | `tizen.system.event.font_set`              | `font_set`                | The value of  this key is the font name of the string type by font-config. | When the font  has changed.              | You can get the  current value with the `SYSTEM_SETTINGS_KEY_FONT_TYPE` key. |

## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 3.0 and Higher for Wearable
