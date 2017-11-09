# Sound Manager
## Dependencies
- Tizen 2.4 and Higher for Mobile
- Tizen 2.3.1 and Higher for Wearable

The sound manager allows you to control the audio behavior of your application.

The main features of the Sound Manager API include:

- Setting sound session types

  You can [set the sound session type](#set), which specifies the behavior of your application sound across the system.

- Controlling the volume

  You can [control the output volume](#manage) by managing the sound type and its volume level.

- Querying sound devices

  You can [use the query functions](#query_device) to get various information, such as the state of the sound devices.

- Managing sound session parameters

  You can [retrieve and set basic sound session parameters](#session) to control the audio behavior of your application.

## Prerequisites

To use the functions and data types of the Sound Manager API (in [mobile](../../../../org.tizen.native.mobile.apireference/group__CAPI__MEDIA__SOUND__MANAGER__MODULE.html) and [wearable](../../../../org.tizen.native.wearable.apireference/group__CAPI__MEDIA__SOUND__MANAGER__MODULE.html) applications), include the `<sound_manager.h>` header file in your application:

```
#include <sound_manager.h>
```

## Setting the Sound Session Type

The Sound Manager API offers 5 different sound session types: media, alarm, notification, emergency and VOIP. According to these types, your application's audio works in a specific way to mix with sounds of other applications or to respond to an audio interruption made by another application.

The alarm, notification, emergency, and VOIP sessions are prioritized over the media session. For example, when an alarm is activated while you are playing a media file, the system pauses the media session, and the alarm session gets the permission to play its sound.

You can set options for how to start a new media session or respond to an audio interruption during an active media session using the `sound_session_option_for_start_e` (in [mobile](../../../../org.tizen.native.mobile.apireference/group__CAPI__MEDIA__SOUND__MANAGER__SESSION__MODULE.html#ga26a030df874992a461af04255c6c3eef) and [wearable](../../../../org.tizen.native.wearable.apireference/group__CAPI__MEDIA__SOUND__MANAGER__SESSION__MODULE.html#ga26a030df874992a461af04255c6c3eef) applications) and `sound_session_option_for_during_play_e` (in [mobile](../../../../org.tizen.native.mobile.apireference/group__CAPI__MEDIA__SOUND__MANAGER__SESSION__MODULE.html#ga132bd49bd7d0f5037cc292f9c7ad1c32) and [wearable](../../../../org.tizen.native.wearable.apireference/group__CAPI__MEDIA__SOUND__MANAGER__SESSION__MODULE.html#ga132bd49bd7d0f5037cc292f9c7ad1c32) applications) enumerators. A media session is not able to interrupt or block the other types of sound sessions, no matter what options you have set.

You can also set options for resuming the media session when the interruption ends by using the `sound_session_option_for_resumption_e` enumerator (in [mobile](../../../../org.tizen.native.mobile.apireference/group__CAPI__MEDIA__SOUND__MANAGER__SESSION__MODULE.html#ga20d1d7fa84dc322f03b58d42806cd9d9) and [wearable](../../../../org.tizen.native.wearable.apireference/group__CAPI__MEDIA__SOUND__MANAGER__SESSION__MODULE.html#ga20d1d7fa84dc322f03b58d42806cd9d9) applications). The sound system notifies the media session when the interruption ends, and you are able to resume your session.

To set the sound session type for your application and monitor sound session interruptions:

1. Set the sound session type using the `sound_manager_set_session_type()` function. The parameter defines the sounds session type using the `sound_session_type_e` enumeration (in [mobile](../../../../org.tizen.native.mobile.apireference/group__CAPI__MEDIA__SOUND__MANAGER__SESSION__MODULE.html#ga125699870d48881ea153a4fce7140958) and [wearable](../../../../org.tizen.native.wearable.apireference/group__CAPI__MEDIA__SOUND__MANAGER__SESSION__MODULE.html#ga125699870d48881ea153a4fce7140958) applications).

   ```
   int error_code;

   error_code = sound_manager_set_session_type(SOUND_SESSION_TYPE_MEDIA);
   ```

   The function sets the type across the system.

2. To receive a notification whenever the sound session is interrupted:

   1. Register a callback using the `sound_manager_set_session_interrupted_cb()` function:

      ```
      error_code = sound_manager_set_session_interrupted_cb(_sound_session_interrupted_cb, NULL);
      ```

   2. Define the session interrupt callback. The first parameter defines the interruption source using the `sound_session_interrupted_code_e` enumeration (in [mobile](../../../../org.tizen.native.mobile.apireference/group__CAPI__MEDIA__SOUND__MANAGER__SESSION__MODULE.html#ga9d7c723a05f1eab1b1d535bfad527b93) and [wearable](../../../../org.tizen.native.wearable.apireference/group__CAPI__MEDIA__SOUND__MANAGER__SESSION__MODULE.html#ga9d7c723a05f1eab1b1d535bfad527b93) applications).

      ```
      static void
      sound_session_interrupted_cb(sound_session_interrupted_code_e code, void *user_data)
      {
          if (code == SOUND_SESSION_INTERRUPTED_BY_MEDIA)
              /* Session interrupted by media application, handle accordingly */
          if (code == SOUND_SESSION_INTERRUPTED_COMPLETED)
              /* Interruption completed, handle accordingly */
      }
      ```

   3. When no longer needed, deregister the callback:

      ```
      error_code = sound_manager_unset_session_interrupted_cb();
      ```

## Controlling the Volume

You can manage the volume level of a particular sound type. With the Sound Manager API, you can set and get a volume level and a maximum volume level of a particular sound type.

Normally, if there is an active output stream, the `sound_manager_get_current_sound_type()` function returns the sound type of that stream, and if not, it returns an error message. However, you can set a particular sound type as current using the `sound_manager_set_current_sound_type()` function. This enables other applications, such as a volume application, to manage the volume level of the particular sound type even though it is not currently playing.

**Note**
Setting the current sound type affects the entire system. When no longer needed, unset the current sound type using the `sound_manager_unset_current_sound_type()` function.

To control the volume of your application:

1. To receive a notification whenever the volume changes:

   1. Register a callback using the `sound_manager_set_volume_changed_cb()` function:

      ```
      error_code = sound_manager_set_volume_changed_cb(_sound_manager_volume_changed_cb, NULL);
      ```

   2. Define the volume change callback. When the volume changes, use the callback to determine which sound type has changed and what the new volume level is.

      ```
      #define MBUF 128

      int error_code;

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
   sound_session_type_e type = SOUND_SESSION_TYPE_MEDIA;

   int cur_vol = 0;

   ret = sound_manager_get_volume(type, &cur_vol);

   int max_vol = 0;

   ret = sound_manager_get_max_volume(type, &max_vol);
   ```

3. To set the volume level, use the `sound_manager_set_volume()` function.

   In the following example code, the first parameter is the sound type and the second parameter is a value received from the slider in the application UI, with which the user sets the volume level.

   ```
   int ret;
   sound_session_type_e type = SOUND_SESSION_TYPE_MEDIA;
   int value;

   /*
      Make sure the value is within the system maximum volume
      by using the sound_manager_get_max_volume() function
   */

   ret = sound_manager_set_volume(type, value);
   ```

## Querying Sound Devices

The audio behavior of your application must change depending on the sound devices that are connected.

Use the `sound_manager_get_current_device_list()` function to get the list handle of the currently connected sound devices. With the sequential search of this device list, you can get the device handle of each device on the list. You can use the `sound_manager_get_next_device()` and `sound_manager_get_prev_device()` functions for a sequential search of the device list.

To get a notification when the sound device connection or information has changed, register the `sound_manager_set_device_connected_cb()` and `sound_manager_set_device_information_changed_cb()` callbacks. The initial state of the connected sound device is deactivated.

To query sound device information:

1. To access the sound device information:

   1. Use the `sound_device_mask_e` enumerator (in [mobile](../../../../org.tizen.native.mobile.apireference/group__CAPI__MEDIA__SOUND__MANAGER__DEVICE__MODULE.html#ga5938ab712f44677173b74ec226aa25b3) and [wearable](../../../../org.tizen.native.wearable.apireference/group__CAPI__MEDIA__SOUND__MANAGER__DEVICE__MODULE.html#ga5938ab712f44677173b74ec226aa25b3) applications) to specify the sound devices that you want. With a combination of the masks, you can to narrow down the sound devices to those you actually need when getting a sound device list or setting callbacks.

      To only access the sound devices whose information you need, define a combination of masks:

      ```
      int ret;
      int _ret;
      sound_device_mask_e mask = SOUND_DEVICE_IO_DIRECTION_OUT_MASK |
                                 SOUND_DEVICE_IO_DIRECTION_BOTH_MASK |
                                 SOUND_DEVICE_STATE_ACTIVATED_MASK;
      ```

   2. Retrieve the sound device list handle and sound device handles.

      To query sound device information, you need a list of currently connected sound devices and a handle for each sound device you want query. To retrieve the list handle, use the `sound_manager_get_current_device_list()` function. To retrieve the sound device handles, use `sound_manager_get_next_device()` and `sound_manager_get_prev_device()` functions with the list handle as a parameter.

      ```
      sound_device_list_h list;
      sound_device_h device;
      sound_device_type_e type;
      sound_device_io_direction_e direction;

      ret = sound_manager_get_current_device_list(mask, &list);
      ```

   3. Retrieve the sound device information.

      With the device handle, you can query the sound device information with the following functions:

      - `sound_manger_get_device_type()`: To get the device type.
      - `sound_manager_get_device_io_direction()`: To get the device IO direction.
      - `sound_manager_get_device_id()`: To get the device ID.
      - `sound_manager_get_device_name()`: To get the device name.
      - `sound_manager_get_device_state()`: To get the device state.

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

2. To receive a notification whenever the sound device connection state changes:

   1. Register a callback using the `sound_manager_set_device_connected_cb()` function. Use the mask to filter the callback information.

      ```
      mask = SOUND_DEVICE_IO_DIRECTION_OUT_MASK | SOUND_DEVICE_IO_DIRECTION_BOTH_MASK;

      ret = sound_manager_set_device_connected_cb(mask, _sound_device_connected_cb, NULL);
      ```

      **Note**
      The initial state of the connected sound device is deactivated.

   2. Define the state change callback:

      ```
      static void
      _sound_device_connected_cb(sound_device_h device, bool is_connected, void* user_data)
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

3. To receive a notification whenever the sound device information changes:

   1. Register a callback using the `sound_manager_set_device_information_changed_cb()` function. Use the mask to filter the callback information.

      ```
      mask = SOUND_DEVICE_IO_DIRECTION_OUT_MASK | SOUND_DEVICE_IO_DIRECTION_BOTH_MASK;

      ret = sound_manager_set_device_information_changed_cb(mask,
                                                            _sound_device_information_changed_cb,
                                                            NULL);
      ```

   2. Define the information change callback:

      ```
      static void
      _sound_device_information_changed_cb(sound_device_h device,
                                           sound_device_changed_info_e changed_info,
                                           void* user_data)
      {
          int ret;
          sound_device_type_e type;
          sound_device_state_e state;
          sound_device_io_direction_e direction;

          ret = sound_manager_get_device_type(device, &type);
          if (type == SOUND_DEVICE_BLUETOOTH) {
              if (changed_info == SOUND_DEVICE_CHANGED_INFO_STATE) {
                  ret = sound_manager_get_device_state(device, &state);
                  if (state == SOUND_DEVICE_STATE_DEACTIVATED)
                      /* Bluetooth device has been deactivated, handle accordingly */
                  else
                      /* Handle accordingly */
              } else {
                  ret = sound_manager_get_device_io_direction(device, &direction);
                  if (direction == SOUND_DEVICE_IO_DIRECTION_OUT)
                      /*
                         IO direction of the Bluetooth device is now out,
                         handle accordingly
                      */
                  else
                      /* Handle accordingly */
              }
          } else {
              /* Handle accordingly */
          }
      }
      ```

## Managing Sound Session Parameters

To retrieve and set basic sound session parameters:

1. To receive a notification whenever the sound session is interrupted:

   1. Register a callback using the `sound_manager_set_session_interrupted_cb()` function:

      ```
      sound_manager_set_session_interrupted_cb(_sound_session_interrupted_cb, NULL);
      ```

   2. Define the session interrupt callback. The first parameter defines the interruption source using the `sound_session_interrupted_code_e` enumeration (in [mobile](../../../../org.tizen.native.mobile.apireference/group__CAPI__MEDIA__SOUND__MANAGER__SESSION__MODULE.html#ga9d7c723a05f1eab1b1d535bfad527b93) and [wearable](../../../../org.tizen.native.wearable.apireference/group__CAPI__MEDIA__SOUND__MANAGER__SESSION__MODULE.html#ga9d7c723a05f1eab1b1d535bfad527b93) applications).

      ```
      void
      _sound_session_interrupted_cb(sound_session_interrupted_code_e code, void* userdata)
      {
          dlog_print(DLOG_INFO, LOG_TAG, "Interrupt code: %d\n", code);

          dlog_print(DLOG_INFO, LOG_TAG,
                     "SOUND_SESSION_INTERRUPTED_COMPLETED %d | "\
                     "SOUND_SESSION_INTERRUPTED_BY_MEDIA %d | "\
                     "SOUND_SESSION_INTERRUPTED_BY_CALL %d | "\
                     "SOUND_SESSION_INTERRUPTED_BY_EARJACK_UNPLUG %d | "\
                     "SOUND_SESSION_INTERRUPTED_BY_RESOURCE_CONFLICT %d | "\
                     "SOUND_SESSION_INTERRUPTED_BY_ALARM %d | "\
                     "SOUND_SESSION_INTERRUPTED_BY_EMERGENCY %d | "\
                     "SOUND_SESSION_INTERRUPTED_BY_NOTIFICATION %d\n\n",

                     SOUND_SESSION_INTERRUPTED_COMPLETED,
                     SOUND_SESSION_INTERRUPTED_BY_MEDIA,
                     SOUND_SESSION_INTERRUPTED_BY_CALL,
                     SOUND_SESSION_INTERRUPTED_BY_EARJACK_UNPLUG,
                     SOUND_SESSION_INTERRUPTED_BY_RESOURCE_CONFLICT,
                     SOUND_SESSION_INTERRUPTED_BY_ALARM,
                     SOUND_SESSION_INTERRUPTED_BY_EMERGENCY,
                     SOUND_SESSION_INTERRUPTED_BY_NOTIFICATION);
      }
      ```

2. Manage the session type.

   To start a sound session, this use case uses the Tone Player API (in [mobile](../../../../org.tizen.native.mobile.apireference/group__CAPI__MEDIA__TONE__PLAYER__MODULE.html) and [wearable](../../../../org.tizen.native.wearable.apireference/group__CAPI__MEDIA__TONE__PLAYER__MODULE.html) applications). For more information, see the [Tone Player](media_playback_n.htm#tone).

   To determine and change the session type, use the following functions. The `sound_session_type_e` enumeration (in [mobile](../../../../org.tizen.native.mobile.apireference/group__CAPI__MEDIA__SOUND__MANAGER__SESSION__MODULE.html#ga125699870d48881ea153a4fce7140958) and [wearable](../../../../org.tizen.native.wearable.apireference/group__CAPI__MEDIA__SOUND__MANAGER__SESSION__MODULE.html#ga125699870d48881ea153a4fce7140958) applications) defines the available sound session types.

   ```
   #include <tone_player.h>
   int id;
   sound_session_type_e type;

   tone_player_start(TONE_TYPE_ANSI_DIAL, SOUND_SESSION_TYPE_MEDIA, 10000, &id);

   sound_manager_get_session_type(&type);

   dlog_print(DLOG_INFO, LOG_TAG, "-Session type %d:\n"
              "SOUND_SESSION_TYPE_MEDIA %d | "\
              "SOUND_SESSION_TYPE_ALARM %d | "\
              "SOUND_SESSION_TYPE_NOTIFICATION %d | "\
              "SOUND_SESSION_TYPE_EMERGENCY %d \n",
              type,
              SOUND_SESSION_TYPE_MEDIA,
              SOUND_SESSION_TYPE_ALARM,
              SOUND_SESSION_TYPE_NOTIFICATION,
              SOUND_SESSION_TYPE_EMERGENCY);

   sound_manager_set_session_type(SOUND_SESSION_TYPE_NOTIFICATION);
   ```

3. Manage the session options.

   To specify the sound session behavior at playback start, during playback, and after an interruption, use the following functions:

   ```
   sound_session_option_for_starting_e start;
   sound_session_option_for_during_play_e play;
   sound_session_option_for_resumption_e res;

   sound_manager_get_media_session_option(&start, &play);
   sound_manager_get_media_session_resumption_option(&res);

   sound_manager_set_media_session_option(SOUND_SESSION_OPTION_PAUSE_OTHERS_WHEN_START,
                                          SOUND_SESSION_OPTION_INTERRUPTIBLE_DURING_PLAY);

   sound_manager_set_media_session_resumption_option(SOUND_SESSION_OPTION_RESUMPTION_BY_SYSTEM_OR_MEDIA_PAUSED);
   ```

   The `sound_session_option_for_starting_e` (in [mobile](../../../../org.tizen.native.mobile.apireference/group__CAPI__MEDIA__SOUND__MANAGER__SESSION__MODULE.html#ga26a030df874992a461af04255c6c3eef) and [wearable](../../../../org.tizen.native.wearable.apireference/group__CAPI__MEDIA__SOUND__MANAGER__SESSION__MODULE.html#ga26a030df874992a461af04255c6c3eef) applications), `sound_session_option_for_during_play_e` (in [mobile](../../../../org.tizen.native.mobile.apireference/group__CAPI__MEDIA__SOUND__MANAGER__SESSION__MODULE.html#ga132bd49bd7d0f5037cc292f9c7ad1c32) and [wearable](../../../../org.tizen.native.wearable.apireference/group__CAPI__MEDIA__SOUND__MANAGER__SESSION__MODULE.html#ga132bd49bd7d0f5037cc292f9c7ad1c32) applications), and `sound_session_option_for_resumption_e` (in [mobile](../../../../org.tizen.native.mobile.apireference/group__CAPI__MEDIA__SOUND__MANAGER__SESSION__MODULE.html#ga20d1d7fa84dc322f03b58d42806cd9d9) and [wearable](../../../../org.tizen.native.wearable.apireference/group__CAPI__MEDIA__SOUND__MANAGER__SESSION__MODULE.html#ga20d1d7fa84dc322f03b58d42806cd9d9)applications) enumerations define the available sound session options.

4. After you no longer need the session interrupt callback, deregister it:

   ```
   sound_manager_unset_session_interrupted_cb();
   ```