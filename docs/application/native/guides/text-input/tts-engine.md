# Text-to-speech Engine


Text-to-speech Engine (TTSE) is an engine to synthesize voice from input texts and to send the synthesized sound data to TTS framework. 

TTSE developers can provide TTSE service users with the functions that are necessary to operate the engine.

The main features of the TTSE API include the following:

- Preparing the TTSE service for use

  You can connect the TTSE service application. [Basic TTSE processes](#basic) and [prerequisites](#prerequisites) are defined.

- TTSE Parameters

  You can [set information](#parameters), which includes language and state.

- TTSE Retrieval information

  You can [get information](#info_retrieval), which includes command count and audio type.

- Send results

  You can [send the results](#send_result) to the engine service user.


<a name="prerequisites"></a>
## Prerequisites

To enable your application to use the TTSE functionality, follow these steps:

1. To use the functions and data types of the [TTSE API](../../api/common/latest/group__CAPI__UIX__TTSE__MODULE.html), include the `<ttse.h>` header file in your application:

    ```
    #include <ttse.h>
    ```

2. Create a structure `ttse_request_callback_s`:

    ```
    ttse_request_callback_s callback = {0,};
    ```

3. Register callback functions using `ttse_main()` function (The registered callback functions will be invoked when the TTSE service users request the TTSE services):

    ```
    ttse_main(argc, argv, &callback);
    ```


<a name="basic"></a>
## TTSE basic processes

Using TTSE, you can do the following:

1. Create a structure using the `ttse_request_callback_s` function.

2. Implement callback functions.

    [Add event callbacks](#add_event_callbacks), set pitch, load/unload voice, start synthesizing, and so on by registered callback functions.

3. Register callback functions using `ttse_main()` function.


<a name="add_event_callbacks"></a>
## Add event callbacks

To register and define event callbacks for the TTSE service application, follow these steps:

1. The TTSE developer must register the `initialize()`, `deinitialize()`, `get_info()`, `foreach_voices()`, `is_valid_voice()`, `set_pitch()`, `load_voice()`, `unload_voice()`, `start_synth()`, `cancel_synth()`, `check_app_agreed()`, `need_app_credential()` callbacks:

    - Add the callbacks to the ttse_request_callback_s structure by referring to [TTSE API](../../api/common/latest/group__CAPI__UIX__TTSE__MODULE.html), and pass the structure as a parameter to the ttse_main() function:

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

    - You can register optional callbacks with the `ttse_set_private_data_set_cb()`, `ttse_set_private_data_requested_cb()`, `ttse_set_activated_mode_changed_cb()`, `ttse_set_personal_tts_id_set_cb` functions:

        ```
        static int private_data_set_cb(const char* key, const char* data);
        static int private_data_requested_cb(const char* key, char** data);
        static void activated_mode_changed_cb(int activated_mode);
        static int personal_tts_id_set_cb(const char* ptts_id, void* user_data);

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
            ttse_set_personal_tts_id_set_cb(personal_tts_id_set_cb, NULL);

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

    static int
    personal_tts_id_set_cb(const char* ptts_id, void* user_data)
    {

    }
    ```


<a name="parameters"></a>
## TTSE parameters

You can set the following parameters about the TTSE:

- Send the current state using the `ttse_send_error()` function and send the error to an engine service user:

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
## TTSE information retrieval

You can get the following information about the TTSE:

- Get the speed range using the `ttse_get_speed_range()` function:

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

- Get the pitch range using the `ttse_get_pitch_range()` function:

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

- Get the activated modes using the `ttse_get_activated_mode()` function. According to modes of TTS clients connected to TTS engine service, the output argument `activated_mode` of `ttse_get_activated_mode()` is a bit sequence as `#TTSE_MODE_MASK_DEFAULT | #TTSE_MODE_MASK_SCREEN_READER`:

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
## Send results

You can send the following result information about the TTSE:

- Send the synthesized sound data to the engine service user using the `ttse_send_result()` function:

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

<a name="send_personal_voice"></a>
## Send personal voice

You can send the following personal voice information about the TTSE:

- Send the personal voice's information (ex, language, unique id, display name, device name) to the engine service user using the `ttse_send_result()` function:

    ```
    void
    send_personal_voice(void)
    {
        int ret = TTSE_ERROR_NONE;
        char* language = "en_US";
        char* unique_id = "12345678"
        char* display_name = "my_voice";
        char* device_name = "my_mobile";

		...

        ret = ttse_send_personal_voice(language, unique_id, display_name, device_name);

        if(TTSE_ERROR_NONE != ret)
            /* Error handling */
    }
    ```

## Related information
- Dependencies
  - Since Tizen 3.0
- API References
  - [TTSE API](../../api/common/latest/group__CAPI__UIX__TTSE__MODULE.html)
