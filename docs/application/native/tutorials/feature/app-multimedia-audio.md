
# Audio Playback and Recording

Tizen enables your application to manage audio content. It also provides
control functions for using audio resources. The resources can be media
files stored on the device or streamed from a server through the
network.

Tizen supports various audio formats, including MP3, AAC, WMA, M4A, 3GA,
WAV, and AMR. The available formats depend on the target device.


## Playing Audio

To play audio files stored on the device, use the Player API (in
[mobile](../../../../org.tizen.native.mobile./group__CAPI__MEDIA__PLAYER__MODULE.html)
and
[wearable](../../api/wearable/latest/group__CAPI__MEDIA__PLAYER__MODULE.html)
applications). The Player API also provides interfaces for getting
content information and controlling operations, such as playback, pause,
resume, and stop.

The following figure illustrates the player state changes.

**Figure: Player state changes**

![Player state changes](./media/player_state_changes_n.png)

### Initializing the Audio Player

You can create a player by calling the `player_create()` function, which
returns a player handle on success. You need the player handle in
setting which files to play and with which configuration. You also have
to register appropriate callback functions to handle notifications about
interruptions, ends, and errors during playback.

To prepare the player for playback, and to define the necessary
callbacks to handle playback events:

1.  To use the data types and functions of the Player API (in
    [mobile](../../api/mobile/latest/group__CAPI__MEDIA__PLAYER__MODULE.html)
    and
    [wearable](../../api/wearable/latest/group__CAPI__MEDIA__PLAYER__MODULE.html)
    applications), include the `<player.h>` header file in your
    application:

    ```c++
    #include <player.h>
    ```

2. Define a variable for the player handle, and create the handle:

    ```c++
    struct appdata {
        player_h player;
    };
    typedef struct appdata appdata_s;

    static void
    init_base_player(appdata_s *ad)
    {
        int error_code = 0;
        error_code = player_create(&ad->player);
        if (error_code != PLAYER_ERROR_NONE)
            dlog_print(DLOG_ERROR, LOG_TAG, "failed to create");

        /*
           Perform more playback configuration, such as setting callbacks,
           setting the source file URI, and preparing the player
        */
    }
    ```

3. Set configurations, such as the source file URI.

    To set a specific path for audio files to play, retrieve the default
    internal storage paths. To access and use internal storage, include
    the `<storage.h>` header file in your application.

    ```c++
    #include <storage.h>

    #define MP3_SAMPLE "SampleAudio.mp3";

    int internal_storage_id;
    char *audio_storage_path = NULL;
    char *audio_path = NULL;

    static bool
    storage_cb(int storage_id, storage_type_e type, storage_state_e state, const char *path, void *user_data)
    {
        if (type == STORAGE_TYPE_INTERNAL) {
            internal_storage_id = storage_id;

            return false;
        }

        return true;
    }

    void
    _get_storage_path()
    {
        int error_code = 0;
        char *path = NULL;

        error_code = storage_foreach_device_supported(storage_cb, NULL);
        error_code = storage_get_directory(internal_storage_id, STORAGE_DIRECTORY_MUSIC, &path);
        if (error_code != STORAGE_ERROR_NONE) {
            audio_storage_path = strdup(path);
            free(path);
        }

        error_code = storage_get_directory(internal_storage_id, STORAGE_DIRECTORY_VIDEOS, &path);
        if (error_code != STORAGE_ERROR_NONE) {
            video_storage_path = strdup(path);
            free(path);
        }
    }

    void
    _set_test_path()
    {
        int path_len = 0;

        path_len = strlen(audio_storage_path) + strlen(MP3_SAMPLE) + 1;
        audio_path = malloc(path_len);
        memset(audio_path, 0x0, path_len);

        strncat(audio_path, audio_storage_path, strlen(audio_storage_path));
        strncat(audio_path, MP3_SAMPLE, strlen(MP3_SAMPLE));
    }
    ```

    Once the storage path is set, you can specify the audio file to play
    using the `player_set_uri()` function with the player handle:

    ```c++
    error_code = player_set_uri(ad->player, audio_path);
    if (error_code != PLAYER_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "failed to set URI: error code = %d", error_code);
    ```

4. Create UI buttons and add callback functions for your application to
    control the playback:

    ```c++
    static void
    create_base_gui(appdata_s *ad)
    {
        /* Create a window */
        /* Create a button */
        /* Add a callback to the button */
        evas_object_smart_callback_add(button_init, "clicked", init_base_player, ad);
        evas_object_smart_callback_add(button_end, "clicked", release_base_player, ad);
        /* Create an Evas image object for the video surface */
    }

    static void
    app_create(void *data)
    {
        appdata_s *ad = data;
        create_base_gui(ad);

        return true;
    }
    ```

5. Register callback functions.

    To receive notifications, register and define appropriate callback
    functions for interruption, playback ending, and error events:

    -   Interruption notifications:

        ```c++
        static void
        _player_interrupted_cb(player_interrupted_code_e code, void *data)
        {
            appdata_s *ad = data;
            player_state_e state;

            /*
               All the interrupted_code_e is deprecated since Tizen 3.0
               except PLAYER_INTERRUPTED_BY_RESOURCE_CONFLICT
            */
            player_get_state(ad->player, &state);
            dlog_print(DLOG_INFO, LOG_TAG, "current player state = %d", state);
            /* If the state is PLAYER_STATE_PAUSED, update the UI (for example, button) */
        }

        static void
        init_base_player(appdata_s *ad)
        {
            /* Set an interruption callback if the application wants to know the reason */
            error_code = player_set_interrupted_cb(ad->player, _player_interrupted_cb, ad);
            if (error_code != PLAYER_ERROR_NONE)
                dlog_print(DLOG_ERROR, LOG_TAG, "failed to set interrupt cb");
        }
        ```

    - End notifications:

        ```c++
        static void
        _player_completed_cb(void *data)
        {
            dlog_print(DLOG_INFO, LOG_TAG, "Playback End");
        }

        static void
        init_base_player(appdata_s *ad)
        {
            /*
               Set a completed callback if the application wants to
               know when the playback ends
            */
            error_code = player_set_completed_cb(ad->player, _player_completed_cb, ad);

            if (error_code != PLAYER_ERROR_NONE)
                dlog_print(DLOG_ERROR, LOG_TAG, "failed to set completed cb");
        }
        ```

    - Error notifications:

        ```c++
        static void
        _player_error_cb(int error_code, void *user_data)
        {
            dlog_print(DLOG_ERROR, LOG_TAG, "playback failed, error = %x", error_code);
        }

        static void
        init_base_player(appdata_s *ad)
        {
            error_code = player_set_error_cb(ad->player, _player_error_cb, NULL);
            if (error_code != PLAYER_ERROR_NONE)
                dlog_print(DLOG_ERROR, LOG_TAG, "failed to set error cb");
        }
        ```

### Managing Audio Playback

When the player is created, it is in the `PLAYER_STATE_IDLE` state. To
start playback, it must be in the `PLAYER_STATE_READY` state.

To manage playback:

1.  Get the player ready for playback by calling the `player_prepare()`
    function, which changes the player state from `PLAYER_STATE_IDLE` to
    `PLAYER_STATE_READY`:

    ```c++
    error_code = player_prepare(ad->player);
    if (error_code != PLAYER_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "failed to prepare player: error code = %d", error_code);
    ```

2. Once the player is ready, start playing the audio file using the
    `player_start()` function. The player state changes to
    `PLAYER_STATE_PLAYING`.

    ```c++
    error_code = player_start(ad->player);
    if (error_code != PLAYER_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "failed to start player: error code = %d", error_code);
    ```

3. Stop playback by calling the `player_stop()` function. The player
    state changes back to `PLAYER_STATE_READY`.

    By calling the `player_pause()` function, you can pause playback and
    change the player state to `PLAYER_STATE_PAUSED`.

### Terminating the Audio Player

When you are finished using the player, release all the resources
allocated to it:

1.  Reset the player by calling the `player_unprepare()` function, which
    changes the player state to `PLAYER_STATE_IDLE`.
2.  Destroy the player handle using the `player_destroy()` function.

```c++
error_code = player_stop(ad->player);
error_code = player_unprepare(ad->player);
error_code = player_destroy(ad->player);

if (error_code != PLAYER_ERROR_NONE)
    dlog_print(DLOG_ERROR, LOG_TAG, "fail to destroy player: error code = %d", error_code);
```


## Recording Audio

To record audio, use the Recorder API (in
[mobile](../../api/mobile/latest/group__CAPI__MEDIA__RECORDER__MODULE.html)
and
[wearable](../../api/wearable/latest/group__CAPI__MEDIA__RECORDER__MODULE.html)
applications). The main features of the Recorder API include:

-   Basic recording functionalities: record, stop, pause, cancel, and
    mute
-   Setting the maximum recording time and size
-   Controlling the system volume level

The supported formats in audio recording are M4A and AMR.

The following figure illustrates the general recorder state changes.

**Figure: Recorder state changes**

![Recorder state changes](./media/recorder_state_changes_n.png)

### Initializing the Audio Recorder

To prepare the recorder for the recording session, and to define the
necessary callbacks to handle recording events:

1.  To use the data types and functions of the Recorder API (in
    [mobile](../../api/mobile/latest/group__CAPI__MEDIA__RECORDER__MODULE.html)
    and
    [wearable](../../api/wearable/latest/group__CAPI__MEDIA__RECORDER__MODULE.html)
    applications), include the `<recorder.h>` header file in your
    application:

    ```c++
    #include <recorder.h>
    ```

2. Create an audio recorder by calling the
    `recorder_create_audiorecorder()` function. On success, the function
    returns a handle for the audio recorder and the state of the audio
    recorder is set as `RECORDER_STATE_CREATED`.

    ```c++
    static recorder_h g_recorder;

    /* Create the audio recorder handle */
    int error_code = recorder_create_audiorecorder(&g_recorder);
    if (error_code != RECORDER_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "fail to create an Audio Recorder: error code = %d", error_code);
    ```

3. Register appropriate callback functions to receive notifications
    about recorder state changes or reaching the recording limit:

    -   The following example code implements a simple callback that
        prints the previous and current audio recorder states:

        ```c++
        error_code = recorder_set_state_changed_cb(g_recorder, _state_changed_cb, NULL);

        static void
        _state_changed_cb(recorder_state_e previous, recorder_state_e current, bool by_policy, void *user_data)
        {
            dlog_print(DLOG_INFO, LOG_TAG, "_recorder_state_changed_cb (prev: %d, curr: %d)\n", previous, current);
        }
        ```

    - The following example code implements a simple callback that
        prints a notification about reaching the recording limit:

        ```c++
        error_code = recorder_set_recording_limit_reached_cb(g_recorder, _recorder_recording_limit_reached_cb, NULL);

        static void
        _recorder_recording_limit_reached_cb(recorder_recording_limit_type_e type, void *user_data)
        {
            dlog_print(DLOG_DEBUG, LOG_TAG, "Recording limit reached: %d\n", type);
        }
        ```

4. You can set various attributes of audio recording, such as audio
    codec, file format, file name, file size limit, encoder bitrate,
    audio device, and sample rate:

    -   Set the audio codec for encoding the audio stream using the
        `recorder_set_audio_encoder()` function. The possible audio
        codec values are defined in the `recorder_audio_codec_e`
        enumeration (in
        [mobile](../../api/mobile/latest/group__CAPI__MEDIA__RECORDER__MODULE.html#ga431bd585d929f13a71ecefd58ed17d46)
        and
        [wearable](../../api/wearable/latest/group__CAPI__MEDIA__RECORDER__MODULE.html#ga431bd585d929f13a71ecefd58ed17d46) applications).

        ```c++
        #define FILENAME_PREFIX "AUDIO"
        struct tm localtime = {0};
        time_t rawtime = time(NULL);
        char filename[256] = {'\0'};
        size_t size;

        /* Set the audio encoder */
        error_code = recorder_set_audio_encoder(g_recorder, RECORDER_AUDIO_CODEC_AAC);
        ```

    - Use the `recorder_set_file_format()` function to set the correct
        file format based on the audio codec. For example, if you set
        the codec to AAC, set the file format to 3GP. The possible file
        format values are defined in the `recorder_file_format_e`
        enumeration (in
        [mobile](../../api/mobile/latest/group__CAPI__MEDIA__RECORDER__MODULE.html#ga7d3dbf7b0b3ef68101562b89e81ecf1e)
        and
        [wearable](../../api/wearable/latest/group__CAPI__MEDIA__RECORDER__MODULE.html#ga7d3dbf7b0b3ef68101562b89e81ecf1e) applications).

        ```c++
        /* Set the file format according to the audio encoder */
        error_code = recorder_set_file_format(g_recorder, RECORDER_FILE_FORMAT_3GP);
        ```

    - Based on the file format, define the correct file name, and set
        it using the `recorder_set_filename()` function. The parameters
        are the full path and the name of the file for the recorded
        audio data to be saved.

        ```c++
        /* Create the file name */
        if (localtime_r(&rawtime, &localtime) != NULL) {
            size = snprintf(filename, sizeof(filename), "%s/%s-%04i-%02i-%02i_%02i:%02i:%02i.3gp",
                            app_get_data_path(), FILENAME_PREFIX,
                            localtime.tm_year + 1900, localtime.tm_mon + 1, localtime.tm_mday,
                            localtime.tm_hour, localtime.tm_min, localtime.tm_sec);
        } else {
            /* Error handling */
        }

        /* Set the full path and file name */
        /* Set the file name according to the file format */
        error_code = recorder_set_filename(g_recorder, filename);
        ```

    - Set the file size limit, encoder bitrate, audio device, and
        sample rate. The possible audio device values are defined in the
        `recorder_audio_device_e` enumeration (in
        [mobile](../../api/mobile/latest/group__CAPI__MEDIA__RECORDER__MODULE.html#ga0e73accfbca1b992c29a2128acebbbf3)
        and
        [wearable](../../api/wearable/latest/group__CAPI__MEDIA__RECORDER__MODULE.html#ga0e73accfbca1b992c29a2128acebbbf3) applications).

        ```c++
        /* Set the maximum file size to 1024 (kB) */
        error_code = recorder_attr_set_size_limit(g_recorder, 1024);

        /* Set the audio encoder bitrate */
        error_code = recorder_attr_set_audio_encoder_bitrate(g_recorder, 28800);

        /* Set the audio device to microphone */
        error_code = recorder_attr_set_audio_device(g_recorder, RECORDER_AUDIO_DEVICE_MIC);

        /* Set the audio sample rate */
        error_code = recorder_attr_set_audio_samplerate(g_recorder, 44100);
        ```

### Managing Audio Recording

When the recorder handle is created, the audio recorder is in the
`RECORDER_STATE_CREATED` state. To start recording, the audio recorder
must be in the `RECORDER_STATE_READY` state.

To manage recording:

1.  Get the recorder ready by calling the `recorder_prepare()` function,
    which changes the player state from `RECORDER_STATE_CREATED` to
    `RECORDER_STATE_READY`:

    ```c++
    error_code = recorder_prepare(g_recorder);
    ```

2. Once the recorder is ready, start audio recording using the
    `recorder_start()` function. The recorder state changes to
    `RECORDER_STATE_RECORDING`.

    ```c++
    error_code = recorder_start(g_recorder);
    ```

3. In the `RECORDER_STATE_RECORDING` state, you can pause or stop
    recording:

    -   To pause recording, call the `recorder_pause()` function that
        changes the recorder state to `RECORDER_STATE_PAUSED`. In this
        state, you can resume or stop recording. To resume, call the
        `recorder_start()` function.

        ```c++
        error_code = recorder_pause(g_recorder);
        ```

    - You can stop recording either in the `RECORDER_STATE_RECORDING`
        or `RECORDER_STATE_PAUSED` state. In stopping recording, you can
        save or discard the recorded data. To save the recorded data,
        use the `recorder_commit()` function, and to discard, use the
        `recorder_cancel()` function. Both functions set the audio
        recorder state to `RECORDER_STATE_READY`.

        The following example code first checks the audio recorder
        state, and then stops the recorder and saves the data to a file:

        ```c++
        /* Check the audio recorder state */
        static bool
        _recorder_expect_state(recorder_h recorder, recorder_state_e expected_state)
        {
            recorder_state_e state;
            int error_code = recorder_get_state(recorder, &state);

            dlog_print(DLOG_INFO, LOG_TAG, "recorder state = %d, expected recorder state = %d", state, expected_state);
            if (state == expected_state)
                return TRUE;

            return FALSE;
        }

        /* Stop the recorder and save the recorded data to a file */
        if (_recorder_expect_state(g_recorder, RECORDER_STATE_RECORDING) || _recorder_expect_state(g_recorder, RECORDER_STATE_PAUSED)) {
            error_code = recorder_commit(g_recorder);
            if (error_code != RECORDER_ERROR_NONE) {
                dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);

                return true;
            }
        }
        ```

### Terminating the Audio Recorder

After you finish audio recording, release all the resources allocated to
the audio recorder:

1.  Reset the audio recorder by calling the `recorder_unprepare()`
    function, which changes the recorder state from
    `RECORDER_STATE_READY` to `RECORDER_STATE_CREATED`.
2.  Release the audio recorder resources by calling the
    `recorder_destroy()` function. The recorder state changes to
    `RECORDER_STATE_NONE`.

```c++
error_code = recorder_unprepare(g_recorder);
error_code = recorder_destroy(g_recorder);

if (error_code != RECORDER_ERROR_NONE)
    dlog_print(DLOG_ERROR, LOG_TAG, "fail to destroy recorder: error code = %d", error_code);
```
