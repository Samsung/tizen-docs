# Activity Recognition

The activity recognizer can monitor user activities. You can [detect walking and running activity](#activity). You can also recognize the stationary state and activities on a moving vehicle.

> **Note**  
> You can test the activity recognition functionality only on a target device. The emulator does not support this feature.

## Prerequisites

To use the functions and data types of the Activity Recognition API (in [mobile](../../api/mobile/latest/group__CAPI__CONTEXT__ACTIVITY__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__CONTEXT__ACTIVITY__MODULE.html) applications), include the `<activity_recognition.h>` header file in your application:

```
#include <activity_recognition.h>
```

<a name="activity"></a>
## Detecting Activities

To set and unset callback functions for the activity monitor and retrieve details from the received activity data:

1. Create a handle for activity monitoring using the `activity_create()` function:

    ```
    activity_h handle;
    activity_create(&handle);
    ```

2. To subscribe to notifications about specific activity state changes, invoke the `activity_start_recognition()` function to register a callback function.

    When specific activity data is received, the registered callback is invoked.

    The following example starts the activity monitor to receive notifications when the `ACTIVITY_WALK` activity is detected. Any of the `activity_type_e` enumerators (in [mobile](../../api/mobile/latest/group__CAPI__CONTEXT__ACTIVITY__MODULE.html#gae17e97a1a51a9d5d5d8330f29f4a895d) and [wearable](../../api/wearable/latest/group__CAPI__CONTEXT__ACTIVITY__MODULE.html#gae17e97a1a51a9d5d5d8330f29f4a895d) applications) can be used in place of the `ACTIVITY_WALK` value.

    ```
    activity_start_recognition(handle, ACTIVITY_WALK, example_activity_callback, NULL);
    ```

3. When the registered callback is invoked, the current activity is delivered as a parameter, and you can extract the accuracy of the recognized activity:

   ```
   void
   example_activity_callback(activity_type_e activity, const activity_data_h data,
                             double timestamp, activity_error_e error, void *user_data)
   {
       int result;

       activity_accuracy_e accuracy;
       result = activity_get_accuracy(data, &accuracy);

       if (result != ACTIVITY_ERROR_NONE)
           /* Error handling */
   }
   ```

4. When activity monitoring is no longer needed, unset the callback function and destroy the handle:

   ```
   activity_stop_recognition(handle);
   activity_release(handle);
   ```

## Related Information
* Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
