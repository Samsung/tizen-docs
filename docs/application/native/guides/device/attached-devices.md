# Attached Devices


You can control attached devices and monitor device changes in your application.

The main features of the Device API include:

- Battery information

  You can [get battery details](#battery), such as the current percentage, the charging state, and the current level state, using the Battery API (in [mobile](../../api/mobile/latest/group__CAPI__SYSTEM__DEVICE__BATTERY__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__SYSTEM__DEVICE__BATTERY__MODULE.html) applications).

- Device control

  You can manage various components and elements on the device:

  - Display

    You can [get and set display details](#display), such as the number of displays, the maximum brightness of the display, the current brightness, and the display state, using the Display API (in [mobile](../../api/mobile/latest/group__CAPI__SYSTEM__DEVICE__DISPLAY__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__SYSTEM__DEVICE__DISPLAY__MODULE.html) applications).

  - Haptic

    You can [manage haptic devices](#haptic) by, for example, getting the number of haptic devices, opening or closing the haptic handle, and requesting vibration effect playback, with the Haptic API (in [mobile](../../api/mobile/latest/group__CAPI__SYSTEM__DEVICE__HAPTIC__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__SYSTEM__DEVICE__HAPTIC__MODULE.html) applications).

  - IR

    You can [manage IR devices](#ir) by, for example, determining whether an IR device is available and transmitting an IR pattern, using the IR API (in [mobile](../../api/mobile/latest/group__CAPI__SYSTEM__DEVICE__IR__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__SYSTEM__DEVICE__IR__MODULE.html) applications).

  - LED

    You can [manage the camera flash LED](#led) by, for example, getting the maximum and current brightness of the LED. You can also change the current brightness of the camera flash LED, and request the service LED to play effects using the Led API (in [mobile](../../api/mobile/latest/group__CAPI__SYSTEM__DEVICE__LED__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__SYSTEM__DEVICE__LED__MODULE.html) applications).

  - Power

    You can [request the power state](#power) to be locked or unlocked using the Power API (in [mobile](../../api/mobile/latest/group__CAPI__SYSTEM__DEVICE__POWER__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__SYSTEM__DEVICE__POWER__MODULE.html) applications).

- Change monitoring

  You can [register a callback to monitor device changes](#changes).

## Prerequisites

To enable your application to use the device functionality:

1. To use the Device API submodules (in [mobile](../../api/mobile/latest/group__CAPI__SYSTEM__DEVICE__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__SYSTEM__DEVICE__MODULE.html) applications), the application has to request permission by adding the following privileges to the `tizen-manifest.xml` file:

   ```
   <privileges>
      <!--To use the Display API-->
      <privilege>http://tizen.org/privilege/display</privilege>
      <!--To use the Haptic API-->
      <privilege>http://tizen.org/privilege/haptic</privilege>
      <!--To use the Led API-->
      <privilege>http://tizen.org/privilege/led</privilege>
   </privileges>
   ```

2. To use the functions and data types of the Device API submodules, include the related header files in your application:

   - For the Battery API (in [mobile](../../api/mobile/latest/group__CAPI__SYSTEM__DEVICE__BATTERY__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__SYSTEM__DEVICE__BATTERY__MODULE.html) applications), include `<device/battery.h>`.
   - For the Display API (in [mobile](../../api/mobile/latest/group__CAPI__SYSTEM__DEVICE__DISPLAY__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__SYSTEM__DEVICE__DISPLAY__MODULE.html) applications), include `<device/display.h>`.
   - For the Haptic API (in [mobile](../../api/mobile/latest/group__CAPI__SYSTEM__DEVICE__HAPTIC__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__SYSTEM__DEVICE__HAPTIC__MODULE.html) applications), include `<device/haptic.h>`.
   - For the IR API (in [mobile](../../api/mobile/latest/group__CAPI__SYSTEM__DEVICE__IR__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__SYSTEM__DEVICE__IR__MODULE.html) applications), include `<device/ir.h>`.
   - For the Led API (in [mobile](../../api/mobile/latest/group__CAPI__SYSTEM__DEVICE__LED__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__SYSTEM__DEVICE__LED__MODULE.html) applications), include `<device/led.h>`.
   - For the Power API (in [mobile](../../api/mobile/latest/group__CAPI__SYSTEM__DEVICE__POWER__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__SYSTEM__DEVICE__POWER__MODULE.html) applications), include `<device/power.h>`.
   - For the Callback API (in [mobile](../../api/mobile/latest/group__CAPI__SYSTEM__DEVICE__CALLBACK__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__SYSTEM__DEVICE__CALLBACK__MODULE.html) applications), include `<device/callback.h>`.

   ```
   /* To retrieve battery information */
   #include <device/battery.h>
   /* To control the display */
   #include <device/display.h>
   /* To control haptic devices */
   #include <device/haptic.h>
   /* To control IR devices */
   #include <device/ir.h>
   /* To control LED devices */
   #include <device/led.h>
   /* To control the power state */
   #include <device/power.h>
   /* To monitor device changes */
   #include <device/callback.h>
   ```

<a name="battery"></a>
## Retrieving Battery Information

To retrieve battery information:

- Get the battery charge percentage with the `device_battery_get_percent()` function.

  The function returns the current battery percentage as an integer value from 0 to 100 that indicates the remaining battery charge as a percentage of the maximum level.

    ```
    int error;
    int pct;
    error = device_battery_get_percent(&pct);
    ```

- Get the current battery charging state with the `device_battery_is_charging()` function:

    ```
    int error;
    bool charging;
    error = device_battery_is_charging(&charging);
    ```

- Get the current battery level with the `device_battery_get_level_status()` function.

  The `device_battery_level_e` enumerator (in [mobile](../../api/mobile/latest/group__CAPI__SYSTEM__DEVICE__BATTERY__MODULE.html#ga63913a4983cc34e35dcdd670e8fe99e4) and [wearable](../../api/wearable/latest/group__CAPI__SYSTEM__DEVICE__BATTERY__MODULE.html#ga63913a4983cc34e35dcdd670e8fe99e4) applications) defines the available battery levels.

    ```
    int error;
    device_battery_level_e level;
    error = device_battery_get_level_status(&level);
    ```

<a name="display"></a>
## Controlling the Display

To retrieve and set display properties:

- Get the number of display devices with the `device_display_get_numbers()` function:

    ```
    int error;
    int num;
    error = device_display_get_numbers(&num);
    ```

- Get the maximum possible brightness with the `device_display_get_max_brightness()` function.

  The function returns the maximum brightness value that can be set.

    ```
    int error;
    int max;
    error = device_display_get_max_brightness(0, &max);
    ```

- Get and set the display brightness with the `device_display_get_brightness()` and `device_display_set_brightness()` functions:

    ```
    int error;
    int brt;
    error = device_display_get_brightness(0, &brt);

    error = device_display_set_brightness(0, 100);
    ```

- Get and set the display state with the `device_display_get_state()` and `device_display_change_state()` functions.

  The `display_state_e` enumerator (in [mobile](../../api/mobile/latest/group__CAPI__SYSTEM__DEVICE__DISPLAY__MODULE.html#ga93a9434f07b3db52ec85fe58b79c529f) and [wearable](../../api/wearable/latest/group__CAPI__SYSTEM__DEVICE__DISPLAY__MODULE.html#ga93a9434f07b3db52ec85fe58b79c529f) applications) defines the available display states.

    ```
    int error;
    display_state_e state;
    error = device_display_get_state(&state);

    error = device_display_change_state(DISPLAY_STATE_NORMAL);
    ```

<a name="haptic"></a>
## Controlling Haptic Devices

To control haptic devices:

1. Get the number of haptic devices with the `device_haptic_get_count()` function:

    ```
    int error;
    int num;
    error = device_haptic_get_count(&num);
    ```

2. To manage a haptic device:
   1. Initialize the haptic device with the `device_haptic_open()` function.

      The function opens a haptic-vibration device and returns the handle to it. It makes a connection to the vibrator.

      ```
      int error;
      haptic_device_h handle;
      error = device_haptic_open(0, &handle);
      ```

   2. Play and stop an effect on the device with the `device_haptic_vibrate()` and `device_haptic_stop()` functions.

      The device vibrates for a specified time with a constant intensity. The effect handle can be 0.

      ```
      int error;
      haptic_effect_h effect_handle;
      error = device_haptic_vibrate(handle, 1000, 100, &effect_handle);

      error = device_haptic_stop(handle, &effect_handle);
      ```

   3. When no longer needed, deinitialize the haptic device with the `device_haptic_close()` function.

      The function closes the haptic handle and disconnects the connection to the vibrator.

      ```
      int error;
      error = device_haptic_close(0, handle);
      ```

<a name="ir"></a>
## Controlling IR Devices

To control an IR device:

1. Determine whether IR is available on the device using the `device_ir_is_available()` function:

    ```
    bool avail;
    int error;
    error = device_ir_is_available(&avail);
    ```

2. Transmit an IR pattern with a specific carrier frequency using the `device_ir_transmit()` function:

    ```
    int error;
    int carrier_frequency;
    int *pattern;
    error = device_ir_transmit(carrier_frequency, pattern, size);
    ```

<a name="led"></a>
## Controlling LED Devices

To control a LED device:

- Get the maximum brightness value of a torch LED with the `device_flash_get_max_brightness()` function.

  The function returns the maximum brightness value of the torch LED located next to the camera.

    ```
    int error;
    int max;
    error = device_flash_get_max_brightness(&max);
    ```

- Get and set the current brightness value of a torch LED with the `device_flash_get_brightness()` and `device_flash_set_brightness()` functions:

    ```
    int error;
    int val;
    error = device_flash_get_brightness(&val);

    error = device_flash_set_brightness(1);
    ```

- Play and stop a custom effect on the service LED with the `device_led_play_custom()` and `device_led_stop_custom()` functions.

  The `led_custom_flags` enumerator (in [mobile](../../api/mobile/latest/group__CAPI__SYSTEM__DEVICE__LED__MODULE.html#ga2065bc82e5ecf7e2acba8629c0d75e3b) and [wearable](../../api/wearable/latest/group__CAPI__SYSTEM__DEVICE__LED__MODULE.html#ga2065bc82e5ecf7e2acba8629c0d75e3b) applications) defines the available custom effects.

  The custom effect plays on the service LED that is located on the front of the device.

    ```
    int error;
    error = device_led_play_custom(1000, 500, 0xFFFF0000, LED_CUSTOM_DEFAULT);

    error = device_led_stop_custom();
    ```

<a name="power"></a>
## Controlling the Power State

To lock and unlock the power state:

- Lock the power state with the `device_power_request_lock()` function.

  The function locks the specific lock type for a specified time. After the given timeout, the lock type is unlocked automatically. If the process is destroyed, every lock is removed.

  The `power_lock_e` enumerator (in [mobile](../../api/mobile/latest/group__CAPI__SYSTEM__DEVICE__POWER__MODULE.html#gabc47c58cfcfdaaba177f6004d6395af2) and [wearable](../../api/wearable/latest/group__CAPI__SYSTEM__DEVICE__POWER__MODULE.html#gabc47c58cfcfdaaba177f6004d6395af2) applications) defines the available lock types.

    ```
    int error;
    error = device_power_request_lock(POWER_LOCK_CPU, 0);
    ```

- Unlock the power state with the `device_power_release_lock()` function.

  The function releases the specific lock type locked before.

    ```
    int error;
    error = device_power_release_lock(POWER_LOCK_CPU);
    ```

<a name="changes"></a>
## Monitoring Device Changes

To monitor device changes in, for example, the device display state:

1. Define a callback, which is called when the device status changes.

   The `device_callback_e` enumerator (in [mobile](../../api/mobile/latest/group__CAPI__SYSTEM__DEVICE__CALLBACK__MODULE.html#gaa55ba4e8bf4d8877b500686e1d78f2d7) and [wearable](../../api/wearable/latest/group__CAPI__SYSTEM__DEVICE__CALLBACK__MODULE.html#gaa55ba4e8bf4d8877b500686e1d78f2d7) applications) defines the available callback types.

   ```
   static void
   changed_cb(device_callback_e type, void *value, void *user_data)
   {
       int val;
       if (type != DEVICE_CALLBACK_DISPLAY_STATE)
           return;
       val = (int)value;
       dlog_print(DLOG_DEBUG, LOG_TAG, "current display state: %d", val);
   }
   ```

2. Register the callback function.

   To monitor the display state changes, use the `DEVICE_CALLBACK_DISPLAY_STATE` callback type.

   ```
   int error;
   error = device_add_callback(DEVICE_CALLBACK_DISPLAY_STATE, changed_cb, NULL);
   ```

3. When no longer needed, deregister the callback function:

   ```
   int error;
   error = device_remove_callback(DEVICE_CALLBACK_DISPLAY_STATE, changed_cb);
   ```

## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
