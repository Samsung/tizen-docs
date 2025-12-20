# Wav and Tone Player


You can simply play WAV format files or TONE sound in your application.

- Using the WAV player

  Enables you to play audio in the [WAVE format](#wav).

- Using the tone player

  Enables you to play [tones](#tone).

<a name="wav"></a>
## WAV Player

The [WAV Player API](../../api/common/latest/group__CAPI__MEDIA__WAV__PLAYER__MODULE.html) provides controlling functions for using audio resources (media files stored on the device). Use the WAV Player API to enable your application to play audio and control playback. You can use the WAV and OGG audio formats.

Tizen enables your application to play WAVE format audio in 1 of 2 ways:

- Through the multimedia application control

  When using the [multimedia application control](../app-management/common-appcontrols.md#multimedia), the device standard media player application is launched to play audio.

- With the WAV player functions

  When [using the WAV player functions](#start_wav), your application plays audio using its own user interface.

Most operations of the WAV Player API work in a synchronous mode. The WAV Player API requires a callback to notify the application of the operational status of the player. The callback must be implemented and passed to stop the WAV playback.

Multiple instances of the WAV player can be used to play several audio data streams concurrently. This means that your application can play multiple uncompressed audio files, such as WAV, at the same time.

The following figure illustrates the general WAV player state changes.

**Figure: WAV player state changes**

![WAV player state changes](./media/wav_player_state_changes.png)

<a name="tone"></a>
## Tone Player

Tizen enables your application to play a tone or a list of tones using the [Tone Player API](../../api/common/latest/group__CAPI__MEDIA__TONE__PLAYER__MODULE.html).

You can generate tones in 2 ways:

- Specify the frequency values. You can specify either 1 or 2 frequencies.
- Use a DTMF (Dual Tone Multi Frequency) preset frequency value of the [`tone_type_e`](../../api/common/latest/group__CAPI__MEDIA__TONE__PLAYER__MODULE.html#gaf12912b2c8f9ffe720518ce797506574) enumerator.

You can [start and stop playing a tone](#play_tone), and [play a tone for a specified duration](#duration).

The following figures illustrate the general tone player state changes.

**Figure: Tone player states**

![Tone player states](./media/tone.png)

## Prerequisites

To enable your application to use the playback functionality:

1. To start using the tone player, declare a player ID variable for identifying the tone player:

   ```
   int tone_player_id;
   ```

2. To use the functions and data types of the [WAV Player API](../../api/common/latest/group__CAPI__MEDIA__WAV__PLAYER__MODULE.html), include the `<wav_player.h>` header file in your application:

   ```
   #include <wav_player.h>
   #include <stdio.h>
   #include <sound_manager.h>
   ```

   In this guide, you also need the `<stdio.h>` and `<sound_manager.h>` header files to use standard file input and output functions and the [Sound Manager API](../../api/common/latest/group__CAPI__MEDIA__SOUND__MANAGER__MODULE.html) functions.

<a name="start_wav"></a>
## Starting and Stopping the WAV Player

To start and stop the WAV player:

1. Start playback using the `wav_player_start_new()` function.

   The second parameter should be sound information handle which can created by `sound_manager_create_stream_information()`.

   The third parameter defines a callback that is invoked when the player finishes playback. Implement the callback and handle any post-playback actions in it.

   The final parameter returns the WAV player ID, which you need to stop the player.

   ```
   static void
   _playback_completed_cb(int id, void *user_data)
   {
       const char* path = (const char*)user_data;
       dlog_print(DLOG_INFO, "WAV Player", "Completed! [id:%d, path:%s]", id, path);
   }

   void
   main()
   {
       int wav_player_id;
       wav_player_error_e ret;
       const char* wav_path = "PATH OF YOUR WAV FILE";
       sound_stream_info_h stream_info;

       sound_manager_create_stream_information(SOUND_STREAM_TYPE_MEDIA, NULL, NULL, &stream_info);

       ret = wav_player_start_new(wav_path, stream_info, _playback_completed_cb, (void*)wav_path, &wav_player_id);
   }
   ```

   To set the path of your WAV file, you may need to retrieve the default path for audio files. For more information, see the [Data Storages](../data/data-storages.md) guide.

2. To stop the WAV player, use the `wav_player_stop()` function with the ID of the WAV player:

   ```
   void
   my_stop()
   {
       wav_player_error_e ret;
       ret = wav_player_stop(wav_player_id);
   }
   ```

<a name="play_tone"></a>
## Playing a Tone

To start and stop playing a tone:

1. Start playback using the `tone_player_start_new()` function.

   The first parameter should be the [`tone_type_e`](../../api/common/latest/group__CAPI__MEDIA__TONE__PLAYER__MODULE.html#gaf12912b2c8f9ffe720518ce797506574) enumerators which can define the available values for the tone type.

   The second parameter should be sound information handle which can created by `sound_manager_create_stream_information()`.

   ```
   tone_player_start_new(TONE_TYPE_DEFAULT, stream_info, -1, &tone_player_id);
   ```

   The player ID is assigned and returned if the function succeeds. The ID of the tone player that starts first is 0, the ID of the second one is 1, and so on. If you set the player ID parameter to `NULL`, the ID is not returned.

2. To stop playback, use the `tone_player_stop()` function with the ID of the player you want to stop:

   ```
   tone_player_stop(tone_player_id);
   ```

<a name="duration"></a>
## Playing a Tone for a Specified Duration

To play a tone for a specified duration, use the `tone_player_start_new()` function with the duration (third parameter) set to the number of milliseconds you want playback to last:

```
tone_player_start_new(TONE_TYPE_SUP_CONGESTION, stream_info, 1000, &tone_player_id);
```

When you set the duration to a specified time, playback stops automatically after that time. You can also stop playback manually using the `tone_player_stop()` function.

## Related Information
- Dependencies
  - Since Tizen 2.4
