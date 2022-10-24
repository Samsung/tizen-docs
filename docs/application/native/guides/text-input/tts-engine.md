# Text-to-speech Engine


Text-to-speech Engine (TTSE) is an engine to synthesize voice from input texts and to send the synthesized sound data to TTS framework. 

TTSE developers can provide TTSE service users, to apply TTSE with functions that is necessary to operate the engine.

The main features of the TTSE API include:

- Preparing the TTSE service for use

  You can connect the TTSE service application. [Basic TTSE Processes](#basic) and [Prerequisites](#prerequisites) are defined.

- TTSE Parameters

  You can [set information](#parameters), which includes language and state.

- TTSE Retrieval information

  You can [get information](#info_retrieval), which includes command count and audio type.

- TTSE Send results

  You can send the results to the engine service user. [TTSE Send results](#send_result), is defined.


<a name="prerequisites"></a>
## Prerequisites

To enable your application to use the TTSE functionality:

1. To use the functions and data types of the TTSE API (in [mobile](../../api/mobile/latest/group__CAPI__UIX__TTSE__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__UIX__TTSE__MODULE.html) applications), include the `<ttse.h>` header file in your application:

    ```
    #include <ttse.h>
    ```

2. Create a structure `ttse_request_callback_s`:

    ```
    ttse_request_callback_s callback = {0,};
    ```

3. Register callback functions using `ttse_main()` function (The registered callback functions will be invoked when the TTSE service users request the TTSE services).

    ```
    ttse_main(argc, argv, &callback);
    ```


<a name="basic"></a>
## TTSE Basic Processes

Using TTSE, you can:

1. Create a structure using the `ttse_request_callback_s` function.

2. Implement callback functions.

    [Add Event Callbacks](#add_event_callbacks), sets pitch, load/unload voice, starts synthesizing and, so on by registered callback functions.

3. Register callback functions using `ttse_main()` function.


<a name="add_event_callbacks"></a>
## Add Event Callbacks

To register and define event callbacks for the TTSE service application:

1. The TTSE developer must register the `initialize()`, `deinitialize()`, `get_info()`, `foreach_voices()`, `is_valid_voice()`, `set_pitch()`, `load_voice()`, `unload_voice()`, `start_synth()`, `cancel_synth()`, `check_app_agreed()`, `need_app_credential()` callbacks.

    - Add the callbacks to the ttse_request_callback_s structure (in [mobile](../../api/mobile/latest/group__CAPI__UIX__TTSE__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__UIX__TTSE__MODULE.html)  applications), and pass the structure as a parameter to the ttse_main() function:

        ```
        static int initialize(void);
        static int deinitialize(void);
        static int get_info(char** engine_uuid, char** engine_name, char** engine_setting, bool* use_network);
        static int foreach_voices(ttse_supported_voice_cb callback, void* user_data);
        static int is_valid_voice(const char* language, int type, bool* is_valid);
        static int set_pitch(int pitch);
        static int load_voice(const char* language, int type);
        static int unload_voice(const char* language, int type);
        static int start_synth(const char* language, int type, const char* text, int speed, void* user_data);
        static int cancel_synth(void);
        static int check_app_agreed(const char* appid, bool* is_agreed);
        static bool need_app_credential(void);

        void
        int main(int argc, char* argv[])
        {
            ttse_request_callback_s callback = {0,};

            callback.version = 1;

            callback.initialize	= initialize;
            callback.deinitialize	= deinitialize;

            callback.get_info	= get_info;
            callback.foreach_voices	= foreach_voices;
            callback.is_valid_voice	= is_valid_voice;

            callback.set_pitch	= set_pitch;
            callback.load_voice	= load_voice;
            callback.unload_voice	= unload_voice;

            callback.start_synth		= start_synth;
            callback.cancel_synth	= cancel_synth;

            callback.check_app_agreed	= check_app_agreed;
            callback.need_app_credential	= need_app_credential;

           ttse_main(argc, argv, &callback);
       }
      ```


2. Define the callbacks:

    ```
    static int
    initialize(void)
    {
        /* Your code */
        return 0;	/* initialize succeed */
    }

    static int
    deinitialize(void)
    {
        /* Your code */
        return 0;	/* deinitialize succeed */
    }

    static int
    get_info(char** engine_uuid, char** engine_name, char** engine_setting, bool* use_network)
    {
        /* Your code */
        *engine_uuid = strdup("engine_uuid");
        *engine_name = strdup("engine_name");
        *engine_setting = strdup("engine_settings_app_id");	/* the engine settings application (the UI application) */
        *use_network = true;	/* Need network */

        *use_network = false;	/* Not to need network */
        return 0;
    }

    static int
    foreach_voices(ttse_supported_voice_cb callback, void* user_data)
    {
        /* Your code */
        return 0;	/* supported voices */
    }

    static int
    is_valid_voice(const char* language, int type, bool* is_valid)
    {
        /* Your code */
        return 1;	/* supported voice */

        return 0;	/* Not supported voice */
    }

    static int
    set_pitch(int pitch)
    {
        /* Your code */
        return 0;	/* set_pitch succeed */
    }

    static int
    load_voice(const char* language, int type)
    {
        /* Your code */
        return 0;	/* load_voice succeed */
    }

    static int
    unload_voice(const char* language, int type)
    {
        /* Your code */
        return 0;	/* unload_voice succeed */
    }

    static int
    start_synth(const char* language, int type, const char* text, int speed, void* user_data)
    {
        /* Your code */
        return 0;	/* start_synth succeed */
    }

    static int
    cancel_synth(void)
    {
        /* Your code */
        return 0;	/* cancel_synth succeed */
    }

    static int
    check_app_agreed(const char* appid, bool* is_agreed)
    {
        /* Your code */
        return 0;	/* check_app_agreed succeed */
    }

    static bool
    need_app_credential(void)
    {
        /* Your code */
        return true;	/* app credential is necessary */

        return false;	/* app credential is not necessary */
    }
    ```

3. Implement the optional callbacks, as needed:

    - You can register optional callbacks with the `ttse_set_private_data_set_cb()`, `ttse_set_private_data_requested_cb()`, `ttse_set_activated_mode_changed_cb()` functions:

        ```
        static int private_data_set_cb(const char* key, const char* data);
        static int private_data_requested_cb(const char* key, char** data);
        static void activated_mode_changed_cb(int activated_mode);

        void
        int main(int argc, char* argv[])
        {
            ttse_request_callback_s callback = {
                /* Add the mandatory callbacks */
            };

            ttse_main(argc, argv, &callback);

            ttse_set_private_data_set_cb(private_data_set_cb);
            ttse_set_private_data_requested_cb(private_data_requested_cb);
            ttse_set_activated_mode_changed_cb(activated_mode_changed_cb);

            ...
        }
        ```

4. Define the optional callbacks:
    ```
    static int
    private_data_set_cb(const char* key, const char* data)
    {
        return 0;	/* private data save succeed */
    }

    static int
    private_data_requested_cb(const char* key, char** data)
    {
        /* found key */
        *data = strdup("data");
        return 0;	/* private data set succeed */
    }

    static void
    activated_mode_changed_cb(int activated_mode)
    {
        return ;	/* get activated modes changed succeed */
    }
    ```


<a name="parameters"></a>
## TTSE Parameters

You can set the following parameters about the TTSE:

- Send the current state using the `ttse_send_error()` function and send the error to a engine service user.

    ```
    void
    send_error(void)
    {
        int ret = TTSE_ERROR_NONE;

        ret = ttse_send_error(TTSE_ERROR_NONE, "msg", NULL);
        if(TTSE_ERROR_NONE != ret)
            /* Error handling */
    }
    ```


<a name="info_retrieval"></a>
## TTSE Information Retrieval

You can get the following information about the TTSE:

- Get the speed range using the `ttse_get_speed_range()` function.

    ```
    void
    get_speed_range(void)
    {
        int ret = TTSE_ERROR_NONE;
        int min_speed = 0;
        int normal_speed = 0;
        int max_speed = 0;

        ret = ttse_get_speed_range(&min_speed, &normal_speed, &max_speed);
        if(TTSE_ERROR_NONE != ret)
            /* Error handling */
    }
    ```

- Get the pitch range using the `ttse_get_pitch_range()` function.

    ```
    void
    get_pitch_range(void)
    {
        int ret = TTSE_ERROR_NONE;
        int min_pitch = 0;
        int normal_pitch = 0;
        int max_pitch = 0;

        ret = ttse_get_pitch_range(&min_pitch, &normal_pitch, &max_pitch);
        if(TTSE_ERROR_NONE != ret)
            /* Error handling */
    }
    ```

- Get the activated modes using the `ttse_get_activated_mode()` function. According to modes of TTS clients connected to TTS engine service, the output argument `activated_mode` of `ttse_get_activated_mode()` is a bit sequence as `#TTSE_MODE_MASK_DEFAULT | #TTSE_MODE_MASK_SCREEN_READER`.

    ```
    void
    get_activated_modes(void)
    {
        int ret = TTSE_ERROR_NONE;
        int activated_mode;

        ret = ttse_get_activated_mode(&activated_mode);
        if(TTSE_ERROR_NONE != ret)
            /* Error handling */
    }
    ```


<a name="send_result"></a>
## TTSE Send results

You can send the following result information about the TTSE:

- Send the synthesized sound data to the engine service user using the `ttse_send_result()` function.

    ```
    void
    send_result(void)
    {
        int ret = TTSE_ERROR_NONE;
        void* pcms;
        unsigned int pcm_size;
        int rate = 16000;

		...

        ret = ttse_send_result(TTSE_RESULT_EVENT_START, pcms, pcm_size, TTSE_AUDIO_TYPE_RAW_S16, rate, NULL);

        if(TTSE_ERROR_NONE != ret)
            /* Error handling */
    }
    ```


## Related Information
- Dependencies
  - Tizen 3.0 and Higher for Mobile
  - Tizen 3.0 and Higher for Wearable
