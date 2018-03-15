# Sound Manager


The sound manager allows you to control the audio behavior of your application.

The main features of the Sound Manager API include:

- Controlling the volume

  You can [control the output volume](#manage) by managing the sound type and its volume level.

- Querying sound devices

  You can [use the query functions](#query_device) to get various information, such as the state of the sound devices.

- Creating a sound stream information handle

  You can [create a sound stream information handle](#stream_policy) for your application's sound stream, specifying the behavior of the sound stream across the system, and allowing stream playback and recording APIs to access it.

- Managing stream focus

  You can [control the focus](#stream_focus) of your sound stream.

- Controlling manual stream routing

  You can manually [route your stream](#stream_routing) to a specific device.

## Prerequisites

To use the functions and data types of the Sound Manager API (in [mobile](../../api/mobile/latest/group__CAPI__MEDIA__SOUND__MANAGER__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__MEDIA__SOUND__MANAGER__MODULE.html) applications), include the `<sound_manager.h>` header file in your application:

```
#include <sound_manager.h>
```

<a name="manage"></a>
## Controlling the Volume

You can manage the volume level of a particular sound type. With the Sound Manager API (in [mobile](../../api/mobile/latest/group__CAPI__MEDIA__SOUND__MANAGER__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__MEDIA__SOUND__MANAGER__MODULE.html) applications), you can set and get a volume level and a maximum volume level of a particular sound type.

Normally, if there is an active output stream, the `sound_manager_get_current_sound_type()` function returns the sound type of that stream, and if not, it returns an error message.

To control the volume of your application:

1. To receive a notification whenever the volume changes:

   1. Register a callback using the `sound_manager_add_volume_changed_cb()` function:

      ```
      int id;
      int error_code;

      error_code = sound_manager_add_volume_changed_cb(_sound_manager_volume_changed_cb, NULL, &id);
      ```

   2. Define the volume change callback. When the volume changes, use the callback to determine which sound type has changed and what the new volume level is.

      ```
      #define MBUF 128

      static void
      _sound_manager_volume_changed_cb(sound_type_e type, unsigned int volume, void* user_data)
      {
          char buf[MBUF] = {0,};

          snprintf(buf, MBUF, "(%d) type volume changed to (%d)", type, volume);
          dlog_print(DLOG_INFO, "Sound Manager", "Volume Changed: %s", buf);
      }
      ```

2. To retrieve the current and maximum volume for a sound type:

   - Retrieve the current volume using the `sound_manager_get_volume()` function. The function takes as parameters the sound type and an integer variable where to return the current volume. You can call this function separately for each sound type.
   - Retrieve the maximum volume using the `sound_manager_get_max_volume()` function. The function takes similar parameters and works the same way as the `sound_manager_get_volume()` function.

   ```
   int ret;
   int cur_vol = 0;
   int max_vol = 0;

   ret = sound_manager_get_volume(SOUND_TYPE_MEDIA, &cur_vol);
   ret = sound_manager_get_max_volume(SOUND_TYPE_MEDIA, &max_vol);
   ```

3. To set the volume level, use the `sound_manager_set_volume()` function.

   In the following example code, the first parameter is the sound type and the second parameter is a value received from the slider in the application UI, with which the user sets the volume level.

   ```
   int ret;
   int value;

   /*
      Make sure the value is within the system maximum volume
      by using the sound_manager_get_max_volume() function
   */

   ret = sound_manager_set_volume(SOUND_TYPE_MEDIA, value);
   ```

<a name="query_device"></a>
## Querying Sound Devices

The audio behavior of your application must change depending on the sound devices that are connected.

Use the `sound_manager_get_device_list()` function to get the list handle of the currently connected sound devices. With the sequential search of this device list, you can get the device handle of each device on the list. You can use the `sound_manager_get_next_device()` and `sound_manager_get_prev_device()` functions for a sequential search of the device list.

To get a notification when the sound device connection has changed, register a callback using the `sound_manager_add_device_connection_changed_cb()` function.

To query sound device information:

1. To access the sound device information:

   1. Use the `sound_device_mask_e` enumerator (in [mobile](../../api/mobile/latest/group__CAPI__MEDIA__SOUND__MANAGER__DEVICE__MODULE.html#ga5938ab712f44677173b74ec226aa25b3) and [wearable](../../api/wearable/latest/group__CAPI__MEDIA__SOUND__MANAGER__DEVICE__MODULE.html#ga5938ab712f44677173b74ec226aa25b3) applications) to specify the sound devices that you want. With a combination of the masks, you can to narrow down the sound devices to those you actually need when getting a sound device list or setting callbacks.

      To only access the sound devices whose information you need, define a combination of masks:

      ```
      int ret;
      int _ret;
      sound_device_mask_e mask = SOUND_DEVICE_IO_DIRECTION_OUT_MASK |
                                 SOUND_DEVICE_IO_DIRECTION_BOTH_MASK |
                                 SOUND_DEVICE_STATE_ACTIVATED_MASK;
      ```

   2. Retrieve the sound device list handle and sound device handles.

      To query sound device information, you need a list of currently connected sound devices and a handle for each sound device you want to query. To retrieve the list handle, use the `sound_manager_get_device_list()` function. To retrieve the sound device handles, use `sound_manager_get_next_device()` and `sound_manager_get_prev_device()` functions with the list handle as a parameter.

      ```
      sound_device_list_h list;
      sound_device_h device;
      sound_device_type_e type;
      sound_device_io_direction_e direction;

      ret = sound_manager_get_device_list(mask, &list);
      ```

   3. Retrieve the sound device information.

      With the device handle, you can query the sound device information with the following functions:

      - `sound_manager_get_device_type()`: To get the device type.
      - `sound_manager_get_device_io_direction()`: To get the device IO direction.
      - `sound_manager_get_device_id()`: To get the device ID.
      - `sound_manager_get_device_name()`: To get the device name.

      When calling the query functions, use the sound device handle as the first parameter (input) and the device information type enumerator as the second parameter (output).

      The following example code shows how to retrieve information about sound device type and IO direction:

      ```
      while ((_ret = sound_manager_get_next_device(list, &device)) == SOUND_MANAGER_ERROR_NONE) {
          ret = sound_manager_get_device_type(device, &type);

          if (type == SOUND_DEVICE_BLUETOOTH)
              /* Sound device type is Bluetooth, handle accordingly */
          else if (type == SOUND_DEVICE_AUDIO_JACK)
              ret = sound_manager_get_device_io_direction(device, &direction);
          if (direction == BOTH)
              /* Sound device has both headphone and mic, handle accordingly */
          else
              /* Handle accordingly */
      }
      if (_ret == SOUND_MANAGER_ERROR_NO_DATA)
          /* End of the available devices, handle accordingly */
      ```

   4. Free the sound device list handle.

      When you are done retrieving all the devices, free the device list handle and all the list members with the `sound_manager_free_device_list()` function:

      ```
      ret = sound_manager_free_device_list(list);
      if (ret != SOUND_MANAGER_ERROR_NONE)
          /* Failed to free the device list*/
      ```

2. To receive a notification whenever the sound device connection state changes:

   1. Register a callback using the `sound_manager_add_device_connection_changed_cb()` function. Use the mask to filter the callback information.

      ```
      mask = SOUND_DEVICE_IO_DIRECTION_OUT_MASK | SOUND_DEVICE_IO_DIRECTION_BOTH_MASK;

      ret = sound_manager_add_device_connection_changed_cb(mask, _sound_device_connection_changed_cb, NULL);
      ```

      > **Note**  
	  > The initial state of the internal sound device is connected.

   2. Define the connection state changed callback:

      ```
      static void
      _sound_device_connection_changed_cb(sound_device_h device, bool is_connected, void* user_data)
      {
          int ret;
          sound_device_type_e type;

          if (is_connected) {
              ret = sound_manager_get_device_type(device, &type);
              if (type == SOUND_DEVICE_BLUETOOTH)
                  /* Connected sound device type is Bluetooth, handle accordingly */
              else
                  /* Handle accordingly */
          } else {
              ret = sound_manager_get_device_type(device, &type);
              if (type == SOUND_DEVICE_BLUETOOTH)
                  /* Disconnected sound device type is Bluetooth, handle accordingly */
              else
                  /* Handle accordingly */
          }
      }
      ```

<a name="stream_policy"></a>
## Creating a Sound Stream Handle

You can manage sound streams with sound stream information handles. Once a handle created, it is used in the stream playback and recording APIs, such as Player (in [mobile](../../api/mobile/latest/group__CAPI__MEDIA__PLAYER__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__MEDIA__PLAYER__MODULE.html) applications), WAV Player (in [mobile](../../api/mobile/latest/group__CAPI__MEDIA__WAV__PLAYER__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__MEDIA__WAV__PLAYER__MODULE.html) applications), and Audio I/O (in [mobile](../../api/mobile/latest/group__CAPI__MEDIA__AUDIO__IO__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__MEDIA__AUDIO_IO__MODULE.html) applications), to manage your sound streams. An application can have multiple stream information handles and each handle can have multiple sound streams.

When you create the handle, you also set the sound stream type and [register a callback for sound stream focus changes](#stream_focus).

The available sound stream types are defined in the `sound_stream_type_e` enumeration (in [mobile](../../api/mobile/latest/group__CAPI__MEDIA__SOUND__MANAGER__STREAM__POLICY__MODULE.html#gac33f64ee1b28af0529e2d0904c41e51f) and [wearable](../../api/wearable/latest/group__CAPI__MEDIA__SOUND__MANAGER__STREAM__POLICY__MODULE.html#gac33f64ee1b28af0529e2d0904c41e51f) applications). Fundamentally, the `SYSTEM`, `ALARM`, `NOTIFICATION`, `EMERGENCY`, `VOICE_INFORMATION`, and `RINGTONE_VOIP` types are treated as playback streams, and the `VOICE_RECOGNITION` type as a recording stream. The `MEDIA` type can be both a playback and a recording stream depending on how it is used, and the `VOIP` type has the characteristics of both playback and recording streams. The routing path and sound type of the sound stream are determined internally through the system based on the stream type.

As shown in the following table, the playback stream types are matched to sound types, which are used for volume control.

**Table: Corresponding sound type for each sound stream type**

| Sound stream type                     | Direction          | Sound type                |
|---------------------------------------|--------------------|---------------------------|
| `SOUND_STREAM_TYPE_ALARM`             | Playback           | `SOUND_TYPE_ALARM`        |
| `SOUND_STREAM_TYPE_MEDIA`             | Playback/recording | `SOUND_TYPE_MEDIA`        |
| `SOUND_STREAM_TYPE_NOTIFICATION`      | Playback           | `SOUND_TYPE_NOTIFICATION` |
| `SOUND_STREAM_TYPE_RINGTONE_VOIP`     | Playback           | `SOUND_TYPE_RINGTONE`     |
| `SOUND_STREAM_TYPE_SYSTEM`            | Playback           | `SOUND_TYPE_SYSTEM`       |
| `SOUND_STREAM_TYPE_VOICE_INFORMATION` | Playback           | `SOUND_TYPE_VOICE`        |
| `SOUND_STREAM_TYPE_VOICE_RECOGNITION` | Recording          | N/A                       |
| `SOUND_STREAM_TYPE_VOIP`              | Playback/recording | `SOUND_TYPE_VOIP`         |

To create a sound stream information handle, use the `sound_manager_create_stream_information()` function:

```
int error_code;
sound_stream_info_h stream_info;

error_code = sound_manager_create_stream_information(SOUND_STREAM_TYPE_MEDIA, sound_stream_focus_state_changed_cb,
                                                     NULL, &stream_info);
```

<a name="stream_focus"></a>
## Managing Stream Focus

Setting a sound stream type and acquiring focus gives you more control over the audio behavior of your application. You have the authority to control the sound stream across the system.

To activate a sound stream, you must acquire stream focus. Once focus has been acquired, you can start playing or recording sound. Acquiring stream focus is possible at any time after the stream information handle has been created. The Sound Manager offers stream focus for both playback and recording, allowing you to control the playback and recording streams independently. You can acquire both playback and recording focus for your stream at the same time.

To manage stream focus:

- Acquiring stream focus

  Acquire stream focus for your sound stream using the `sound_manager_acquire_focus()` function. Pass the stream information handle you have created to specify for which sound stream you want to acquire the focus. Once the focus has been acquired, you can activate your sound stream.

  To set the stream focus type, use the values of the `sound_stream_focus_mask_e` enumeration (in [mobile](../../api/mobile/latest/group__CAPI__MEDIA__SOUND__MANAGER__STREAM__POLICY__MODULE.html#ga7087e13ccf2fe610dd1a93b2226f2e72) and [wearable](../../api/wearable/latest/group__CAPI__MEDIA__SOUND__MANAGER__STREAM__POLICY__MODULE.html#ga7087e13ccf2fe610dd1a93b2226f2e72) applications).

  ```
  int error_code;
  int behavior = SOUND_BEHAVIOR_NONE;

  error_code = sound_manager_acquire_focus(stream_info, SOUND_STREAM_FOCUS_FOR_BOTH, behavior, NULL);
  if (!error_code)
      /* Activate your sound stream */
  ```

  Release the stream focus when you no longer need it by using the `sound_manager_release_focus()` function:

  ```
  /* Your sound stream has finished */
  error_code = sound_manager_release_focus(stream_info, SOUND_STREAM_FOCUS_FOR_BOTH, behavior, NULL);
  ```

- Subscribing to the stream focus change notifications

  To be informed when a stream focus change has occurred, define the `sound_stream_focus_state_changed_cb()` callback. The callback is registered when you [create the stream information handle](#stream_policy).

  To get the current state of your stream focus within the callback, call the `sound_manager_get_focus_state()` function.

  The following example uses a sound stream which has both playback and recording focus:

  ```
  static void
  sound_stream_focus_state_changed_cb(sound_stream_info_h stream_info, sound_stream_focus_mask_e focus_mask,
                                      sound_stream_focus_state_e focus_state, sound_stream_focus_change_reason_e reason_for_change,
                                      int sound_behavior, const char *additional_info, void *user_data)
  {
      int error_code;
      sound_stream_focus_state_e state_for_playback;
      sound_stream_focus_state_e state_for_recording;

      error_code = sound_manager_get_focus_state(stream_info, &state_for_playback, &state_for_recording);
      if (!error_code) {
          if (state_for_playback == SOUND_STREAM_FOCUS_STATE_RELEASED || state_for_recording == SOUND_STREAM_FOCUS_STATE_RELEASED)
              /* Focus lost, pause/stop the sound stream */
          if (state_for_playback == SOUND_STREAM_FOCUS_STATE_ACQUIRED && state_for_recording == SOUND_STREAM_FOCUS_STATE_ACQUIRED)
              /* Focus regained, you can resume the sound stream */
      }
      printf("The stream focus changed by [%d]", reason_for_change);
  }
  ```

- Reacquiring focus

  When a stream loses focus, it can reacquire it automatically. Focus reacquisition is enabled by default. To disable it, call the `sound_manager_set_focus_reacquisition()` function with the second parameter set to `false`.

  Consider the following example of 2 applications that both need to acquire playback focus to play their respective streams:

  1. Initially, application A has acquired playback focus.
  2. Application B requests to acquire playback focus. This releases the playback focus previously acquired by application A.
  3. After application B requests to release playback focus, application A reacquires it automatically if the reacquisition property has been enabled in its stream information.

  To disable the reacquisition property:

  ```
  bool enable;
  sound_manager_get_focus_reacquisition(stream_info, &enable);
  if (enable == true) {
      enable = false;
      sound_manager_set_focus_reacquisition(stream_info, enable);
  }
  ```
<a name="stream_routing"></a>
## Controlling Manual Stream Routing

Stream routing means selecting a device for the stream. Each sound stream has a routing type, which can be automatic or manual:

- In automatic stream routing, you cannot select a specific device. The Audio Framework controls automatic stream routing for all stream types, except `SOUND_STREAM_TYPE_VOIP` and `SOUND_STREAM_TYPE_MEDIA_EXTERNAL_ONLY`.
- In manual stream routing, you must select a particular device to be used for the steam. Manual stream routing is done for the `SOUND_STREAM_TYPE_VOIP` and `SOUND_STREAM_TYPE_MEDIA_EXTERNAL_ONLY` stream types. To add a device for manual stream routing, use the `sound_manager_add_device_for_stream_routing()` function, and apply stream routing with the `sound_manager_apply_stream_routing()` function.

To add an external USB device for stream routing:

1. Create a stream information handle with the `sound_manager_create_information()` function and a device list with the `sound_manager_get_device_list()` function:

   ```
   int ret;
   sound_device_list_h device_list;
   sound_device_h device;
   sound_device_type_e type;

   ret = sound_manager_create_stream_information(SOUND_STREAM_TYPE_MEDIA_EXTERNAL_ONLY, focus_cb,
                                                 cb_userdata, &stream_info);
   ret = sound_manager_get_device_list(SOUND_DEVICE_IO_DIRECTION_IN_MASK, &device_list);
   ```

2. Go through the device list to find the external USB device, then add it to the stream information handle with the `sound_manager_add_device_for_stream_routing()` function and apply the manual stream routing with the `sound_manager_apply_stream_routing()` function:

   ```
   while (!(ret = sound_manager_get_next_device(device_list, &device))) {
       ret = sound_manager_get_device_type(device, &type);
       ret = sound_manager_get_device_io_direction(device, &direction);
       if (/* Device type is USB */) {
           ret = sound_manager_add_device_for_stream_routing(stream_info, device);
           ret = sound_manager_apply_stream_routing(stream_info);
           break;
       }
   }
   ```

3. Once you have applied the stream routing, free the device list with the `sound_manager_free_device_list()` function:

   ```
   /* Free the device list */
   sound_manager_free_device_list(device_list);
   ```

## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
