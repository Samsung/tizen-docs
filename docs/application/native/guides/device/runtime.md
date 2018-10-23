# Runtime Information


You can access various runtime information and monitor changes in it.

The main features of the Runtime Information API include:

- Getting runtime information with a key-value pair

  You can [retrieve a runtime information value](#get) using its [key](#keys).

- Getting runtime information with a function

  You can [retrieve runtime information using a function](#get_function) specific to a certain information.

- Getting application runtime information

  You can [retrieve runtime information about running applications](#get_apps).

- Monitoring runtime information changes

  You can [register a callback function to monitor specific changes](#monitor) in the runtime information.

## Prerequisites

To use the functions and data types of the Runtime information API (in [mobile](../../api/mobile/latest/group__CAPI__SYSTEM__RUNTIME__INFO__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__SYSTEM__RUNTIME__INFO__MODULE.html) applications), include the `<runtime_info.h>` header file in your application:

```
#include <runtime_info.h>
```

<a name="get"></a>
## Getting Runtime Information with a Key-Value Pair

Some runtime information consists of key and value pairs.

To get information on, for example, whether Bluetooth is enabled or an audio jack connected:

- Check whether Bluetooth is enabled.

  Use the `RUNTIME_INFO_KEY_BLUETOOTH_ENABLED` key with the data type-specific get function.

  The Bluetooth enabled key data type is `bool`, which means that you need to use the `runtime_info_get_value_bool()` function.

  ```
  #include <stdbool.h>

  void
  func(void)
  {
      bool value;
      int ret;

      ret = runtime_info_get_value_bool(RUNTIME_INFO_KEY_BLUETOOTH_ENABLED, &value);
      if (ret != RUNTIME_INFO_ERROR_NONE) {
          /* Error handling */
          return;
      }
      dlog_print(DLOG_INFO, LOG_TAG, "Bluetooth: %s", value ? "Enabled" : "Disabled");
  }
  ```

- Get the audio jack connection status.

  Use the `RUNTIME_INFO_KEY_AUDIO_JACK_STATUS` key with the data type-specific get function.

  The audio jack status key data type is `integer`, which means that you need to use the `runtime_info_get_value_int()` function.

  ```
  void
  func(void)
  {
      int value;
      int ret;

      ret = runtime_info_get_value_int(RUNTIME_INFO_KEY_AUDIO_JACK_STATUS, &value);
      if (ret != RUNTIME_INFO_ERROR_NONE) {
          /* Error handling */
          return;
      }

      dlog_print(DLOG_INFO, LOG_TAG, "Audio jack status: %d", value);
      switch (value) {
      case RUNTIME_INFO_AUDIO_JACK_STATUS_UNCONNECTED:
          /* Audio jack is disconnected */
          break;
      case RUNTIME_INFO_AUDIO_JACK_STATUS_CONNECTED_3WIRE:
          /* 3-conductor wire is connected */
          break;
      case RUNTIME_INFO_AUDIO_JACK_STATUS_CONNECTED_4WIRE:
          /* 4-conductor wire is connected */
          break;
      }
  }
  ```

<a name="get_function"></a>
## Getting Runtime Information with a Function

Some runtime information can be retrieved by using a function.

To get information on, for example, the current frequency of the CPU core 0, retrieve the CPU core frequency with the `runtime_info_get_processor_current_frequency()` function:

```
void
func(void)
{
    int core_idx = 0;
    int freq;
    int ret;

    ret = runtime_info_get_processor_current_frequency(core_idx, &freq);
    if (ret != RUNTIME_INFO_ERROR_NONE) {
        /* Error handling */

        return;
    }
    dlog_print(DLOG_INFO, LOG_TAG, "The frequency of CPU core 0: %d", freq);
}
```

<a name="get_apps"></a>
## Getting Application Runtime Information

You can get runtime information on running applications.

To get information on, for example, the memory usage for each application:

```
void
print_memory_usage(void)
{
    int ret;
    int i;
    int count;
    app_usage_h mem_usage_handle;
    char *appid;
    unsigned int usage;

    ret = runtime_info_get_all_apps_memory_usage(&mem_usage_handle);
    if (ret != RUNTIME_INFO_ERROR_NONE)
        /* Error handling */


    ret = runtime_info_app_usage_get_count(mem_usage_handle, &count);
    if (ret != RUNTIME_INFO_ERROR_NONE)
        /* Error handling */


    for (i = 0; i < count; i++) {
        ret = runtime_info_app_usage_get_appid(mem_usage_handle, i, &appid);
        if (ret != RUNTIME_INFO_ERROR_NONE)
            /* Error handling */


        ret = runtime_info_app_usage_get_usage(mem_usage_handle, i, &usage);
        if (ret != RUNTIME_INFO_ERROR_NONE)
            /* Error handling */


        dlog_print(DLOG_INFO, LOG_TAG, "appid = %s, usage = %u KB\n", appid, usage);
        free(appid);
    }

    ret = runtime_info_app_usage_destroy(mem_usage_handle);
    if (ret != RUNTIME_INFO_ERROR_NONE)
        /* Error handling */

}
```

<a name="monitor"></a>
## Monitoring Runtime Information Changes

Applications can be notified about changes in the runtime information.

To monitor, for example, the connection state of the USB cable:

1. Use the `runtime_info_set_changed_cb()` function with the `RUNTIME_INFO_KEY_USB_CONNECTED` key to register a callback that is triggered each time the USB cable connection state changes:

    ```
    #include <stdbool.h>

    /* Callback */
    void
    usb_connection_changed(runtime_info_key_e key, void *user_data)
    {
        bool value;
        int ret;

        if (key != RUNTIME_INFO_KEY_USB_CONNECTED)
            return;

        ret = runtime_info_get_value_bool(key, &value);
        if (ret != RUNTIME_INFO_ERROR_NONE) {
            /* Error handling */
            return;
        }

        dlog_print(DLOG_INFO, LOG_TAG, "USB status: %s", value ? "Connected" : "Disconnected");
    }

    /* Register and deregister */
    void
    func(void)
    {
        int ret;
        void *data;

        ret = runtime_info_set_changed_cb(RUNTIME_INFO_KEY_USB_CONNECTED, usb_connection_changed, data);
        if (ret != RUNTIME_INFO_ERROR_NONE) {
            /* Error handling */
            return;
        }
    ```

2. When no longer needed, deregister the callback with the `runtime_info_unset_changed_cb()` function:

    ```
        ret = runtime_info_unset_changed_cb(RUNTIME_INFO_KEY_USB_CONNECTED);
        if (ret != RUNTIME_INFO_ERROR_NONE) {
            /* Error handling */
            return;
        }
    }
    ```

<a name="keys"></a>
## Runtime Information Keys

The following table lists the available runtime information keys.

**Table: Runtime information keys**  

| Key                                      | Type   | Description                              |
|------------------------------------------|--------|------------------------------------------|
| `RUNTIME_INFO_KEY_BLUETOOTH_ENABLED`     | `bool` | Indicates whether Bluetooth is enabled.  |
| `RUNTIME_INFO_KEY_WIFI_HOTSPOT_ENABLED`  | `bool` | Indicates whether a Wi-Fi hotspot is enabled. |
| `RUNTIME_INFO_KEY_BLUETOOTH_TETHERING_ENABLED` | `bool` | Indicates whether Bluetooth tethering is enabled. |
| `RUNTIME_INFO_KEY_USB_TETHERING_ENABLED` | `bool` | Indicates whether USB tethering is enabled. |
| `RUNTIME_INFO_KEY_LOCATION_SERVICE_ENABLED` | `bool` | Indicates whether the location service is allowed to use location data from GPS satellites. |
| `RUNTIME_INFO_KEY_LOCATION_NETWORK_POSITION_ENABLED` | `bool` | Indicates whether the location service is allowed to use location data from cellular and Wi-Fi. |
| `RUNTIME_INFO_KEY_PACKET_DATA_ENABLED`   | `bool` | Indicates whether the packet data through 3G network is enabled. |
| `RUNTIME_INFO_KEY_DATA_ROAMING_ENABLED`  | `bool` | Indicates whether data roaming is enabled. |
| `RUNTIME_INFO_KEY_VIBRATION_ENABLED`     | `bool` | Indicates whether vibration is enabled.  |
| `RUNTIME_INFO_KEY_AUDIO_JACK_CONNECTED`  | `bool` | Indicates whether an audio jack is connected. |
| `RUNTIME_INFO_KEY_GPS_STATUS`            | `int`  | Indicates the current status of GPS.     |
| `RUNTIME_INFO_KEY_BATTERY_IS_CHARGING`   | `bool` | Indicates whether the battery is currently charging. |
| `RUNTIME_INFO_KEY_TV_OUT_CONNECTED`      | `bool` | Indicates whether TV out is connected.   |
| `RUNTIME_INFO_KEY_AUDIO_JACK_STATUS`     | `int`  | Indicates the current status of the audio jack. |
| `RUNTIME_INFO_KEY_USB_CONNECTED`         | `bool` | Indicates whether USB is connected.      |
| `RUNTIME_INFO_KEY_CHARGER_CONNECTED`     | `bool` | Indicates whether a charger is connected. |
| `RUNTIME_INFO_KEY_AUTO_ROTATION_ENABLED` | `bool` | Indicates whether auto-rotation is enabled. |

## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
