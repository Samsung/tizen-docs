# System Settings


You can [access the system configuration](#settings) related to user preferences, such as ringtone, wallpaper, and font, using the System Settings API with the [system setting keys](#details).

The System Settings API provides 2 function types listed in the following table. Certain functions support both types, whereas others only support the getter function.

**Table: System Settings API function types**

| Type       | Function                                 | Description                              |
|------------|------------------------------------------|------------------------------------------|
| `GETTER`   | `system_settings_get_value_bool()`<br> `system_settings_get_value_int()`<br> `system_settings_get_value_string()` | Get the user-defined values by data type (bool, int, or string). |
| `NOTIFIER` | `system_settings_set_changed_cb()`<br> `system_settings_unset_changed_cb()` | Register and deregister callback functions which are triggered when the `SETTER` related to the key is called. |

The following example shows a typical use case. An application sees the name of the current wallpaper and you want to print out a message when the wallpaper changes:

```
void
_img_cb(system_settings_key_e key, void *user_data)
{
    dlog_print(DLOG_INFO, LOG_TAG, "THIS IS CALLED BY USER APPLICATION WHEN THE WALLPAPER CHANGES \n");
}

/* NOTIFIER 1 - Registering a callback function */
system_settings_set_changed_cb(SYSTEM_SETTINGS_KEY_WALLPAPER_HOME_SCREEN, _img_cb, NULL);
char * path;

/* GETTER */
system_settings_get_value_string(SYSTEM_SETTINGS_KEY_WALLPAPER_HOME_SCREEN, &path);
dlog_print(DLOG_INFO, LOG_TAG, "path of the current wallpaper is %s \n", path);

/* NOTIFIER 2 - Deregistering a callback function */
system_settings_unset_changed_cb(SYSTEM_SETTINGS_KEY_WALLPAPER_HOME_SCREEN);
```

## Prerequisites

To use the functions and data types of the System Settings API (in [mobile](../../api/mobile/latest/group__CAPI__SYSTEM__SYSTEM__SETTINGS__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__SYSTEM__SYSTEM__SETTINGS__MODULE.html) applications), include the `<system_settings.h>` header file in your application:

```
#include <system_settings.h>
```

<a name="settings"></a>
## Managing System Settings

To manage system settings, which provide access to system variables:

1. Define auxiliary structures:

   ```
   struct _ret_type_define {
       system_settings_key_e key;
       int returns;
   };

   typedef
   enum {
       _RET_BOOL = 0,
       _RET_INT,
       _RET_STRING
   } _SYSTEM_SETTINGS_TYPES;

   struct _ret_type_define
   _ret_type[] = {
       {
           SYSTEM_SETTINGS_KEY_INCOMING_CALL_RINGTONE, _RET_STRING
       },
       {
           SYSTEM_SETTINGS_KEY_WALLPAPER_HOME_SCREEN, _RET_STRING
       },
       {
           SYSTEM_SETTINGS_KEY_WALLPAPER_LOCK_SCREEN, _RET_STRING
       },
       {
           SYSTEM_SETTINGS_KEY_FONT_SIZE, _RET_INT
       },
       {
           SYSTEM_SETTINGS_KEY_FONT_TYPE, _RET_STRING
       },
       {
           SYSTEM_SETTINGS_KEY_MOTION_ACTIVATION, _RET_BOOL
       },
       {
           /* Others */
       }
   };

   static const char*
   _info_key[SYS_INFO_COUNT] = {
       "SYSTEM_SETTINGS_KEY_INCOMING_CALL_RINGTONE",
       "SYSTEM_SETTINGS_KEY_WALLPAPER_HOME_SCREEN",
       "SYSTEM_SETTINGS_KEY_WALLPAPER_LOCK_SCREEN",
       "SYSTEM_SETTINGS_KEY_FONT_SIZE",
       "SYSTEM_SETTINGS_KEY_FONT_TYPE",
       "SYSTEM_SETTINGS_KEY_MOTION_ACTIVATION",
       /* Others */
   };
   ```

2. Obtain the setting data.

   The available settings are defined in the `system_settings_key_e` enumerator (in [mobile](../../api/mobile/latest/group__CAPI__SYSTEM__SYSTEM__SETTINGS__MODULE.html#ga56c8fa435516884c5648efecdd871eaa) and [wearable](../../api/wearable/latest/group__CAPI__SYSTEM__SYSTEM__SETTINGS__MODULE.html#ga56c8fa435516884c5648efecdd871eaa) applications).

   Read the data using the following functions, according to the data type of the value you want to read:

   - `system_settings_get_value_int()`
   - `system_settings_get_value_bool()`
   - `system_settings_get_value_double()`
   - `system_settings_get_value_string()`

   ```
   #define SYS_INFO_COUNT 6

   int i;
   for (i = 0; i < SYS_INFO_COUNT; i++) {
       dlog_print(DLOG_ERROR, LOG_TAG, "%d- System_settings: %s: ", i, _info_key[_ret_type[i].key]);

       if (_ret_type[i].returns==_RET_BOOL) {
           system_settings_get_value_bool(_ret_type[i].key, &_bool_ret);
           dlog_print(DLOG_ERROR, LOG_TAG, "%d", _bool_ret);
       } else if (_ret_type[i].returns==_RET_INT) {
           system_settings_get_value_int(_ret_type[i].key, &_int_ret);
           dlog_print(DLOG_ERROR, LOG_TAG, "%d", _int_ret);
       } else if (_ret_type[i].returns==_RET_STRING) {
           system_settings_get_value_string(_ret_type[i].key, &_string_ret);
           dlog_print(DLOG_ERROR, LOG_TAG, "%s", _string_ret);
           free(_string_ret);
       } else if (_ret_type[i].returns==_RET_DOUBLE) {
           system_settings_get_value_double(_ret_type[i].key, &_double_ret);
           dlog_print(DLOG_ERROR, LOG_TAG, "%f", _double_ret);
       } else {
           dlog_print(DLOG_ERROR, LOG_TAG, "Undefined return type");
       }
   }
   ```

3. Monitor changes in the setting values.

   1. To monitor when a system setting value changes, set a callback using the `system_settings_set_changed_cb()` function with the appropriate key as the first parameter:

      ```
      for (i = 0; i < SYS_INFO_COUNT; i++)
          system_settings_set_changed_cb(_ret_type[i].key, _system_settings_changed_cb, 0);
      ```

   2. Define the callback to be invoked after each change.

      The `system_settings_key_e` key refers to the key that has changed.

      ```
      static void
      _system_settings_changed_cb(system_settings_key_e key, void *user_data)
      {
          dlog_print(DLOG_ERROR, LOG_TAG, "Runtime Info changed: %s", _info_key[key]);
      }
      ```

   3. When the callbacks are no longer needed, unset them:

      ```
      for (i = 0; i < SYS_INFO_COUNT; i++)
          system_settings_unset_changed_cb(_ret_type[i].key, _system_settings_changed_cb, 0);
      ```

<a name="details"></a>
## System Setting Keys

The `system_settings_key_e` enumerator (in [mobile](../../api/mobile/latest/group__CAPI__SYSTEM__SYSTEM__SETTINGS__MODULE.html#ga56c8fa435516884c5648efecdd871eaa) and [wearable](../../api/wearable/latest/group__CAPI__SYSTEM__SYSTEM__SETTINGS__MODULE.html#ga56c8fa435516884c5648efecdd871eaa) applications) defines all enumerations that work as parameters for the System Settings API.

The following table lists the available system setting keys.

**Table: System settings keys**  

| Key                                      | Type     | Supported function type | Description                              |
|------------------------------------------|----------|-------------------------|------------------------------------------|
| `SYSTEM_SETTINGS_KEY_3G_DATA_NETWORK_ENABLED` | `bool`   | `GETTER, NOTIFIER`      | Indicates whether the 3G data network is enabled. |
| `SYSTEM_SETTINGS_KEY_ACCESSIBILITY_TTS`  | `bool`   | `GETTER, NOTIFIER`      | Indicates whether the accessibility TTS is enabled on the device. |
| `SYSTEM_SETTINGS_KEY_ADS_ID`             | `string` | `GETTER, NOTIFIER`      | Ads ID for each device.                  |
| `SYSTEM_SETTINGS_KEY_DEFAULT_FONT_TYPE`  | `string` | `GETTER`                | Current system default font type.        |
| `SYSTEM_SETTINGS_KEY_DEVICE_NAME`        | `string` | `GETTER, NOTIFIER`      | Device name.                             |
| `SYSTEM_SETTINGS_KEY_DISPLAY_SCREEN_ROTATION_AUTO` | `bool`   | `GETTER, NOTIFIER`      | Indicates whether rotation control is automatic. |
| `SYSTEM_SETTINGS_KEY_EMAIL_ALERT_RINGTONE` | `string` | `GETTER, NOTIFIER`      | File path of the current email alert ringtone. |
| `SYSTEM_SETTINGS_KEY_FONT_SIZE`          | `int`    | `GETTER, NOTIFIER`      | Current system font size.                |
| `SYSTEM_SETTINGS_KEY_FONT_TYPE`          | `string` | `GETTER, NOTIFIER`      | Current system font type.                |
| `SYSTEM_SETTINGS_KEY_INCOMING_CALL_RINGTONE` | `string` | `GETTER, NOTIFIER`      | File path of the current ringtone.       |
| `SYSTEM_SETTINGS_KEY_LOCALE_COUNTRY`     | `string` | `GETTER, NOTIFIER`      | Current country setting in the \<LANGUAGE\>_\<REGION\> syntax. The language is an ISO 639-2 code, and the region is an ISO 3166-1 alpha-2 code. |
| `SYSTEM_SETTINGS_KEY_LOCALE_LANGUAGE`    | `string` | `GETTER, NOTIFIER`      | Current language setting in the \<LANGUAGE\>_\<REGION\> syntax. The language is an ISO 639-2 code, and the region is an ISO 3166-1 alpha-2 code. |
| `SYSTEM_SETTINGS_KEY_LOCALE_TIMEFORMAT_24HOUR` | `bool`   | `GETTER, NOTIFIER`      | Indicates whether the 24-hour clock is used. If the value is `false`, the 12-hour clock is used. |
| `SYSTEM_SETTINGS_KEY_LOCALE_TIMEZONE`    | `string` | `GETTER, NOTIFIER`      | Current time zone.                       |
| `SYSTEM_SETTINGS_KEY_LOCKSCREEN_APP`     | `string` | `GETTER, NOTIFIER`      | Lockscreen application package name.     |
| `SYSTEM_SETTINGS_KEY_LOCK_STATE`         | `int`    | `GETTER, NOTIFIER`      | Current lock state.                      |
| `SYSTEM_SETTINGS_KEY_MOTION_ACTIVATION`  | `bool`   | `GETTER, NOTIFIER`      | Indicates whether the motion service is activated. |
| `SYSTEM_SETTINGS_KEY_MOTION_ENABLED`     | `bool`   | `GETTER, NOTIFIER`      | Indicates whether the device user has enabled the motion feature. |
| `SYSTEM_SETTINGS_KEY_NETWORK_FLIGHT_MODE` | `bool`   | `GETTER, NOTIFIER`      | Indicates whether the device is in the flight mode. |
| `SYSTEM_SETTINGS_KEY_NETWORK_WIFI_NOTIFICATION` | `bool`   | `GETTER, NOTIFIER`      | Indicates whether Wi-Fi-related notifications are enabled on the device. |
| `SYSTEM_SETTINGS_KEY_SCREEN_BACKLIGHT_TIME` | `int`    | `GETTER, NOTIFIER`      | Backlight time (in seconds). The following values can be used: 15, 30, 60, 120, 300, and 600. |
| `SYSTEM_SETTINGS_KEY_SOUND_LOCK`         | `bool`   | `GETTER, NOTIFIER`      | Indicates whether the screen lock sound is enabled on the device (for example, whether the LCD on/off sound is enabled). |
| `SYSTEM_SETTINGS_KEY_SOUND_NOTIFICATION` | `string` | `GETTER, NOTIFIER`      | File path of the current notification tone set by the user. |
| `SYSTEM_SETTINGS_KEY_SOUND_NOTIFICATION_REPETITION_PERIOD` | `int`    | `GETTER, NOTIFIER`      | Time period for notification repetitions. |
| `SYSTEM_SETTINGS_KEY_SOUND_SILENT_MODE`  | `bool`   | `GETTER, NOTIFIER`      | Indicates whether the device is in the silent mode. |
| `SYSTEM_SETTINGS_KEY_SOUND_TOUCH`        | `bool`   | `GETTER, NOTIFIER`      | Indicates whether the screen touch sound is enabled on the device. |
| `SYSTEM_SETTINGS_KEY_TIME_CHANGED`       | `int`    | `NOTIFIER`              | Event that occurs when the system changes time to notify you about the time change. |
| `SYSTEM_SETTINGS_KEY_ULTRA_DATA_SAVE`    | `int`    | `GETTER, NOTIFIER`      | Ultra Data Save status, which can be one of the `system_settings_uds_state_e` enumeration values (in [mobile](../../api/mobile/latest/group__CAPI__SYSTEM__SYSTEM__SETTINGS__MODULE.html#ga59ffa706c8964ee1f6c6ab03b4efdac1) and [wearable](../../api/wearable/latest/group__CAPI__SYSTEM__SYSTEM__SETTINGS__MODULE.html#ga59ffa706c8964ee1f6c6ab03b4efdac1) applications). |
| `SYSTEM_SETTINGS_KEY_ULTRA_DATA_SAVE_PKG_LIST` | `string` | `NOTIFIER`              | Ultra Data Save Package List, which is a string containing whitelisted package names separated with semicolons (;). |
| `SYSTEM_SETTINGS_KEY_USB_DEBUGGING_ENABLED` | `bool`   | `GETTER, NOTIFIER`      | Indicates whether the USB debugging is enabled. |
| `SYSTEM_SETTINGS_KEY_VIBRATION`          | `bool`   | `GETTER, NOTIFIER`      | Indicates whether vibration is enabled on the device. |
| `SYSTEM_SETTINGS_KEY_WALLPAPER_HOME_SCREEN` | `string` | `GETTER, NOTIFIER`      | File path of the current home screen wallpaper. |
| `SYSTEM_SETTINGS_KEY_WALLPAPER_LOCK_SCREEN` | `string` | `GETTER, NOTIFIER`      | File path of the current lock screen wallpaper. |

## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
