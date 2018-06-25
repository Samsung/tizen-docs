# Voice-Control-Engine


Voice-Control-Engine (VCE) is an engine to recognize sound data. The user records this data and sends the result as a predefined command.

VCE developers can provide VCE service users, to apply VCE with functions that is necessary to operate the engine.

The main features of the VCE API include:

- Preparing the VCE service for use

  You can connect the VCE service application. [Basic VCE Processes](#basic) and [Prerequisites](#prerequisites) are defined.

- VCE Parameters

  You can [set information](#parameters), which includes language and state.

- VCE Retrieval information

  You can [get information](#info_retrieval), which includes command count and audio type.

- VCE Control Recording

  You can control VCE recording to the engine service user. [VCE Control Recording](#control_record), is defined.

- VCE Send results

  You can send the results to the engine service user. [VCE Send Results](#send_result), is defined.


<a name="prerequisites"></a>
## Prerequisites

To enable your application to use the VCE functionality:

1. To use the VCE API (in [mobile](../../api/mobile/latest/group__CAPI__UIX__VOICE__CONTROL__ENGINE__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__UIX__VOICE__CONTROL__ENGINE__MODULE.html) applications), the application has to request permission by adding the following privilege to the `tizen-manifest.xml` file:

   ```
   <privileges>
      <privilege>http://tizen.org/privilege/recorder</privilege>
   </privileges>
   ```

2. To use the functions and data types of the VCE API (in [mobile](../../api/mobile/latest/group__CAPI__UIX__VOICE__CONTROL__ENGINE__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__UIX__VOICE__CONTROL__ENGINE__MODULE.html) applications), include the `<vce.h>` header file in your application:

    ```
    #include <vce.h>
    ```

3. Create a structure `vce_request_callback_s`:

    ```
    vce_request_callback_s callback = {0,};
    ```

4. Register callback functions using `vce_main()` function (The registered callback functions will be invoked when the VCE service users request the VCE services).

    ```
    vce_main(argc, argv, &callback);
    ```


<a name="basic"></a>
## VCE Basic Processes

Using VCE, you can:

1. Create a structure using the `vce_request_callback_s` function.

2. Implement callback functions.

   [Add Event Callbacks](#add_event_callbacks), sets language, sets command, starts recognition and, so on by registered callback functions.

3. Register callback functions using `vce_main()` function.


<a name="add_event_callbacks"></a>
## Add Event Callbacks

To register and define event callbacks for the VCE service application:

1. The VCE developer must register the `initialize()`, `deinitialize()`, `get_info()`, `get_recording_format()`, `foreach_langs()`, `is_lang_supported()`, `set_language()`, `set_commands()`, `unset_commands()`, `start()`, `set_recording()`, `stop()`, `cancel()`, `set_audio_type()`, `set_domain()`, `process_text()`, `process_list_event()`, `process_haptic_event()` callbacks.

   - Add the callbacks to the vce_request_callback_s structure (in [mobile](../../api/mobile/latest/group__CAPI__UIX__VOICE__CONTROL__ENGINE__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__UIX__VOICE__CONTROL__ENGINE__MODULE.html)  applications), and pass the structure as a parameter to the vce_main() function:

      ```
       static int initialize(void);
       static int deinitialize(void);
       static int get_info(char** engine_uuid, char** engine_name, char** engine_settings_app_id, bool* use_network);
       static int get_recording_format(const char* audio_id, vce_audio_type_e* types, int* rate, int* channels);
       static int foreach_langs(vce_supported_language_cb callback, void* user_data);
       static bool is_lang_supported(const char* lang);
       static int set_language(const char* language);
       static int set_commands(vce_cmd_h vc_command);
       static int unset_commands(void);
       static int start(bool stop_by_silence);
       static int set_recording(const void* data, unsigned int length, vce_speech_detect_e* silence_detected);
       static int stop(void);
       static int cancel(void);
       static int set_audio_type(const char* audio_type);
       static int set_domain(const char* domain);
       static int process_text(const char* text);
       static int process_list_event(const char* event);
       static int process_haptic_event(const char* event);

       void
       int main(int argc, char* argv[])
       {
           vce_request_callback_s callback = {0,};

           callback.version = 1;

           callback.initialize	= initialize;
           callback.deinitialize	= deinitialize;

           callback.get_info	= get_info;
           callback.get_recording_format	= get_recording_format;
           callback.foreach_langs	= foreach_langs;
           callback.is_lang_supported	= is_lang_supported;

           callback.set_language	= set_language;
           callback.set_commands	= set_commands;
           callback.unset_commands	= unset_commands;

           callback.start		= start;
           callback.set_recording	= set_recording;
           callback.stop		= stop;
           callback.cancel		= cancel;

           callback.set_audio_type	= set_audio_type;
           callback.set_domain	= set_domain;
           callback.process_text	= process_text;
           callback.process_list_event	= process_list_event;
           callback.process_haptic_event	= process_haptic_event;

           vce_main(argc, argv, &callback);
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
    get_info(char** engine_uuid, char** engine_name, char** engine_settings_app_id, bool* use_network)
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
    get_recording_format(const char* audio_id, vce_audio_type_e* types, int* rate, int* channels)
    {
        /* Your code */
        return 0;	/* supported langs */
    }

    static int
    foreach_langs(vce_supported_language_cb callback, void* user_data)
    {
        /* Your code */
        return 0;	/* supported langs */
    }

    static bool
    is_lang_supported(const char* lang)
    {
        /* Your code */
        return true;	/* supported language */

        return false;	/* Not supported language */
    }

    static int
    set_language(const char* language)
    {
        /* Your code */
        return 0;	/* set_language succeed */
    }

    static int
    set_commands(vce_cmd_h vc_command)
    {
        /* Your code */
        return 0;	/* set_commands succeed */
    }

    static int
    unset_commands(void)
    {
        /* Your code */
        return 0;	/* unset_commands succeed */
    }

    static int
    start(bool stop_by_silence)
    {
        /* Your code */
        return 0;	/* start succeed */
    }

    static int
    set_recording(const void* data, unsigned int length, vce_speech_detect_e* silence_detected)
    {
        /* Your code */
        return 0;	/* set_recording succeed */
    }

    static int
    stop(void)
    {
        /* Your code */
        return 0;	/* stop succeed */
    }

    static int
    cancel(void)
    {
        /* Your code */
        return 0;	/* cancel succeed */
    }

    static int
    set_audio_type(const char* audio_type)
    {
        /* Your code */
        return 0;	/* set_audio_type succeed */
    }

    static int
    set_domain(const char* domain)
    {
        /* Your code */
        return 0;	/* set_domain succeed */
    }

    static int
    process_text(const char* text)
    {
        /* Your code */
        return 0;	/* process_text succeed */
    }

    static int
    process_list_event(const char* event)
    {
        /* Your code */
        return 0;	/* process_list_event succeed */
    }

    static int
    process_haptic_event(const char* event)
    {
        /* Your code */
        return 0;	/* process_haptic_event succeed */
    }
   ```

3. Implement the optional callbacks, as needed:

   - You can register optional callbacks with the `vce_set_private_data_set_cb()`, `vce_set_private_data_requested_cb()`, `vce_set_nlu_base_info_requested_cb()` functions:

      ```
       static int private_data_set_cb(const char* key, const char* data);
       static int private_data_requested_cb(const char* key, char** data);
       static int nlu_base_info_requested_cb(const char* key, char** value);

       void
       int main(int argc, char* argv[])
       {
           vce_request_callback_s callback = {
               /* Add the mandatory callbacks */
           };

           vce_set_private_data_set_cb(private_data_set_cb);
           vce_set_private_data_requested_cb(private_data_requested_cb);
           vce_set_nlu_base_info_requested_cb(nlu_base_info_requested_cb);

           vce_main(argc, argv, &callback);
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

    static int
    nlu_base_info_requested_cb(const char* key, char** value)
    {
        /* found key */
        *value = strdup("value");
        return 0;	/* nlu base info value set succeed */
    }
   ```

<a name="parameters"></a>
## VCE Parameters

You can set the following parameters about the VCE:

- Send the current state using the `vce_send_error()` function and send the error to a engine service user.

  ```
    void
    send_error(void)
    {
        int ret = VCE_ERROR_NONE;

        ret = vce_send_error(VCE_ERROR_NONE, "msg", NULL);
        if(VCE_ERROR_NONE != ret)
            /* Error handling */
    }
  ```

- Send the current state using the `vce_set_private_data()` function. Set private data to a engine service user.

  ```
    void
    set_private_data(void)
    {
        int ret = VCE_ERROR_NONE;

        ret = vce_set_private_data("key", "data");
        if(VCE_ERROR_NONE != ret)
            /* Error handling */
    }
  ```


<a name="info_retrieval"></a>
## VCE Information Retrieval

You can get the following information about the VCE:

- Get all commands using the `vce_get_foreach_command()` function.

  ```
    bool
    command_cb(int id, int type, int format, const char* command, const char* param, int domain, void* user_data)
    {
        /* Callback command data */
        /* Your code */
    }

    void
    get_foreach_command(void)
    {
        int ret = VCE_ERROR_NONE;
        int g_vce_command;

        ret = vce_get_foreach_command(g_vce_command, command_cb, NULL);
        if(VCE_ERROR_NONE != ret)
            /* Error handling */
    }
  ```

- Get command length using the `vce_get_command_count()` function. Get `g_vce_command` data from set_commands() function.

  ```
    void
    get_command_count(void)
    {
        int ret = VCE_ERROR_NONE;
        int count = 0;

        ret = vce_get_command_count(g_vce_command, &count);
        if(VCE_ERROR_NONE != ret)
            /* Error handling */
    }
  ```

- Get current audio type using the `vce_get_audio_type()` function.

  ```
    void
    get_audio_type(void)
    {
        int ret = VCE_ERROR_NONE;
        char *audio_type = NULL;

        ret = vce_get_audio_type(&audio_type);
        if(VCE_ERROR_NONE != ret)
            /* Error handling */
        if(NULL != audio_type) {
            /* Memory release */
            free(audio_type);
            audio_type = NULL;
        }
    }
  ```

- Get private data from a voice manager client using the `vce_get_private_data()` function.

  ```
    void
    get_private_data(void)
    {
        int ret = VCE_ERROR_NONE;
        char *data = NULL;

        ret = vce_get_private_data("key", &data);
        if(VCE_ERROR_NONE != ret)
            /* Error handling */
        if(NULL != data) {
            /* Memory release */
            free(data);
            data = NULL;
        }
    }
  ```


<a name="control_record"></a>
## VCE Control Recording

You can control recording of the following information about the VCE:

- Start recording voice using the `vce_start_recording()` function. If the function call is successful, you can receive recording data from `set_recording` function.

  ```
    void
    start_recording(void)
    {
        int ret = VCE_ERROR_NONE;

        ret = vce_start_recording();
        if(VCE_ERROR_NONE != ret)
            /* Error handling */
    }
  ```

- Stop recording voice using the `vce_stop_recording()` function. If the function call is successful, you can not receive recording data from `set_recording` function.

  ```
    void
    stop_recording(void)
    {
        int ret = VCE_ERROR_NONE;

        ret = vce_stop_recording();
        if(VCE_ERROR_NONE != ret)
            /* Error handling */
    }
  ```

<a name="send_result"></a>
## VCE Send Results

You can send the following result information about the VCE:

- Send the command result to the engine service user using the `vce_send_result()` function.

  ```
    void
    send_result(void)
    {
        int ret = VCE_ERROR_NONE;
        int is_consumed;

        ret = vce_send_result(VCE_RESULT_EVENT_SUCCESS, NULL, 0, "text", NULL, NULL, VC_RESULT_MESSAGE_NONE, &is_consumed, NULL);
        if(VCE_ERROR_NONE != ret)
            /* Error handling */
    }
  ```

- Send the Automatic Speech Recognition (ASR) result to the engine service user using the `vce_send_asr_result()` function.

  ```
    void
    send_asr_result(void)
    {
        int ret = VCE_ERROR_NONE;
        ret = vce_send_asr_result(VCE_ASR_RESULT_EVENT_FINAL_RESULT, "asr_result", NULL);
        if(VCE_ERROR_NONE != ret)
            /* Error handling */
    }
  ```

- Send the Natural Language Generation (NLG) result to the engine service user using the `vce_send_nlg_result()` function.

  ```
    void
    send_nlg_result(void)
    {
        int ret = VCE_ERROR_NONE;
        ret = vce_send_nlg_result("nlg_result", NULL);
        if(VCE_ERROR_NONE != ret)
            /* Error handling */
    }
  ```


## Related Information
- Dependencies
  - Tizen 5.0 and Higher for Mobile
  - Tizen 5.0 and Higher for Wearable
