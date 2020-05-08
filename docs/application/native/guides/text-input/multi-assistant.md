# Multi-assistant


Multi-assistant allows the user to install and use multiple voice assistants on the same machine.

The Multi-assistant framework manages voice assistants that are built with Multi-assistant client library and activates one among them when either the wake word is detected or the voice key is pressed.

The main features of the Multi-assistant API include:

- Retrieving information

  You can [get various information](#info) from the Multi-assistant framework:

  - Client state

    The client state is changed by functions and applied as a precondition for each API.

  - Service state

    The service state is changed when the user starts or stops interacting with the installed voice assistants.

  - Active state

    Active state indicates whether the current client application is expected to serve as an active voice assistant for the user or not. An active voice assistant is responsible for responding to the user utterance and must provide appropriate feedback.

  - Audio Data

    When the assistant gets activated, it retrieves the user utterance audio data from the Multi-assistant framework in order to process user's voice command.

- Updating result information

  - ASR result

    To provide visual feedback while processing the voice command, text representation that are converted from audio data needs to be updated as frequently as possible before the final result is retrieved.

  - Result

    Represents the final response to the user's query, including the summarized text information that will be displayed on the Multi-assistant panel if the device supports it.

  - Recognition Result

    Specifies whether the processing was successful or not.

- Sending requests

  - Adjust background volume

When a voice assistant starts playing the voice feedback, it can request to adjust the background volume for making the voice feedback more audible.

To use functionalities of the Multi-assistant framework:

1. Set up Multi-assistant client library and [register callbacks](#callback).

   The initialization allows the Multi-assistant framework to distinguish your application from any other applications also using the framework. The registered callbacks allow you to receive notifications about changes in the client state, service state and active state, and enables retrieving user utterance audio data from the framework.

2. Prepare the Multi-assistant client library.

   The preparation connects the client application to the Multi-assistant service to start exchanging messages with Mutli-assistant framework and wakeup engines.

3. Retrieve audio data when activated.

   If the registered active state changed event callback function is called with the ACTIVE parameter, then you must ask for the user utterance data so that the query could be processed by your voice assistant.

4. Send the result.

   While you are processing the user utterance, it is recomended to update the partially converted ASR result to the Multi-assistant framework so that it can display the visual feedback to the user.

   When the processing work is finished, you can send the final result to the Multi-assistant framework to display the result, and also send recognition result to report whether the audio data processing has succeeded or not.

5. When no longer needed, unprepare and deinitialize the Multi-assistant client library.

   You must disconnect from the Multi-assistant service and deinitialize the client library using `ma_unprepare()` and `ma_deinitialize()`.


## Prerequisites

To enable your application to use the Multi-assistant functionality:

1. To use the functions and data types of the Multi-assistant API (in [mobile](../../api/mobile/latest/group__CAPI__UIX__MULTI__ASSISTANT__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__UIX__MULTI__ASSISTANT__MODULE.html) applications), include the `<multi_assistant.h>` header file in your application:

   ```c
   #include <multi_assistant.h>
   ```

2. Initialize the Multi-assistant client library with `ma_initialize()`:

   ```c
   void
   initialize_multi_assistant()
   {
       int ret;
       ret = ma_initialize();
       if (MA_ERROR_NONE != result)
           /* Error handling */
   }
   ```

   If the function call is successful, the client state changes to `MA_STATE_INITIALIZED`.

   > [!NOTE]
   > The Mutli-assistant client feature is not thread-safe and depends on the Ecore main loop. Implement Multi-assistant within the Ecore main loop and do not use it in a thread.

3. Prepare Multi-assistant with `ma_prepare()`, which connects the client application to the Multi-assistant service. The Multi-assistant service records user utterance and manages wakeup engines to detect the wake word from the audio data.

   ```c
   void
   prepare_multi_assistant()
   {
       int ret;
       ret = ma_prepare();
       if (MA_ERROR_NONE != ret)
           /* Error handling */
   }
   ```

   `ma_prepare()` is asynchronous and when the preparation succeeds, the client state changes from `MA_STATE_INITIALIZED` to `MA_STATE_READY`. If `ma_prepare()` fails, the error callback is triggered.

4. When the Multi-assistant is no longer needed, unprepare and deinitialize it:

   ```c
   void
   unprepared_multi_assistant()
   {
       int ret;
       ret = ma_unprepare();
       if (MA_ERROR_NONE != ret)
           /* Error handling */
   }

   void
   deinitialize_multi_assistant()
   {
       int ret;
       ret = ma_deinitialize();
       if (MA_ERROR_NONE != result)
           /* Error handling */
   }
   ```

   When `ma_unprepare()` succeeds, the client state changes from `MA_STATE_READY` to `MA_STATE_INITIALIZED`.

   > [!NOTE]
   > Do not call `ma_deinitialize()` in a callback. Within a callback, `ma_deinitialize()` fails and returns `MA_ERROR_OPERATION_FAILED`.


<a name="callback"></a>
## Manage callbacks

For more information on the callback functions, see the `multi_assistant_common.h` header file, where they are defined.

To set and unset callbacks to get notifications about state changes, errors and audio data retrieval:

> [!NOTE]
> Set and unset all callbacks when the client state is `MA_STATE_INITIALIZED`.

- Set the state change callback to be invoked when the client state changes:

  ```c
  /* Callback */
  void
  state_changed_cb(ma_state_e previous, ma_state_e current, void* user_data)
  {
      /* Your code */
  }

  /* Set */
  void
  set_state_changed_cb()
  {
      int ret;
      ret = ma_set_state_changed_cb(state_changed_cb, NULL);
      if (MA_ERROR_NONE != ret)
          /* Error handling */
  }

  /* Unset */
  void
  unset_state_changed_cb()
  {
      int ret;
      ret = ma_unset_state_changed_cb();
      if (MA_ERROR_NONE != ret)
          /* Error handling */
  }
  ```

- Set the service state change callback to be invoked when the Multi-assistant service state changes:

  User controls the Multi-assistant service state. In a general scenario:

  1. If the system is configured to use the Multi-assistant feature, then after the system boots the Multi-assistant service will have the `MA_SERVICE_STATE_LISTENING` state.
  2. User starts giving the voice command to the system by saying the wake word or pressing the voice button. If the start is successful, the Multi-assistant service state changes to `MA_SERVICE_STATE_UTTERANCE`.
  3. After recording, the service state changes to `MA_SERVICE_STATE_PROCESSING` for recognition processing.
  4. After the recognition is completed, the service state returns to `MA_SERVICE_STATE_LISTENING`.

  If the system configuration changes and because of this if the Multi-assistant feature is not available, then the Multi-assistant service state can be changed to `MA_SERVICE_STATE_INACTIVE`.

  ```c
  /* Callback */
  void
  __service_state_changed_cb(ma_service_state_e previous, ma_service_state_e current, void* user_data)
  {
      /* Your code */
  }

  /* Set */
  void
  set_service_state_changed_cb()
  {
      int ret;
      ret = ma_set_service_state_changed_cb(__service_state_changed_cb, NULL);
      if (MA_ERROR_NONE != ret)
          /* Error handling */
  }

  /* Unset */
  void
  unset_service_state_changed_cb()
  {
      int ret;
      ret = ma_unset_service_state_changed_cb();
      if (MA_ERROR_NONE != ret)
          /* Error handling */
  }
  ```

- Set the active state change callback to be invoked when the active state of current voice assistant changes:

  ```c
  /* Callback */
  void
  __active_state_changed_cb(ma_active_state_e previous, ma_active_state_e current, void* user_data)
  {
      /* Your code */
  }

  /* Set */
  void
  set_active_state_changed_cb()
  {
      int ret;
      ret = ma_set_active_state_changed_cb(__active_state_changed_cb, NULL);
      if (MA_ERROR_NONE != ret)
          /* Error handling */
  }

  /* Unset */
  void
  unset_active_state_changed_cb()
  {
      int ret;
      ret = ma_unset_active_state_changed_cb();
      if (MA_ERROR_NONE != ret)
          /* Error handling */
  }
  ```

- Set the audio streaming callback to be invoked when the Multi-assistant framework sends user utterance audio data:

  ```c
  /* Callback */
  void
  __audio_streaming_cb(ma_audio_streaming_event_e event, char* buffer, int len, void* user_data);
  {
      /* Your code */
  }

  /* Set */
  void
  set_audio_streaming_cb()
  {
      int ret;
      ret = ma_set_audio_streaming_cb(__audio_streaming_cb, NULL);
      if (MA_ERROR_NONE != ret)
          /* Error handling */
  }

  /* Unset */
  void
  unset_audio_streaming_cb()
  {
      int ret;
      ret = ma_unset_audio_streaming_cb();
      if (MA_ERROR_NONE != ret)
          /* Error handling */
  }
  ```

- Set the error callback to be invoked when an error occurs while processing the Multi-assistant related tasks:

  ```c
  /* Callback */
  void
  __error_cb(ma_error_e reason, void* user_data)
  {
      /* Your code */
  }

  /* Set */
  void
  set_error_cb(ma_h vc)
  {
      int ret;
      ret = ma_set_error_cb(__error_cb, NULL);
      if (MA_ERROR_NONE != ret)
          /* Error handling */
  }

  /* Unset */
  void
  unset_error_cb(ma_h vc)
  {
      int ret;
      ret = ma_unset_error_cb();
      if (MA_ERROR_NONE != ret)
          /* Error handling */
  }
  ```

<a name="info"></a>
## Retrieve Multi-assistant information

To get information about the current client state and current language:

- Get the current client state using `ma_get_state()`.

  The client state changes according to function calls when the Multi-assistant client library is, for example, initialized and prepared:

  ```c
  void
  get_state()
  {
      ma_state_e current_state;
      int ret;
      ret = ma_get_state(&current_state);
      if (MA_ERROR_NONE != ret)
          /* Error handling */
  }
  ```

- Get the current language with `ma_get_current_language()`. The wake word detection works for the current (default) language. Use the language change callback to get language change notifications.

    ```c
    void
    get_current_language()
    {
        int ret;
        char* current_lang = NULL;
        ret = ma_get_current_language(&current_lang);
        if (MA_ERROR_NONE != ret)
            /* Error handling */
    }
    ```

## Monitor language change

To monitor the system or application language changes:

- Set the current language change callback to be invoked when the system or application language changes:

  ```c
  /* Callback */
  void
  __language_changed_cb(const char* previous, const char* current, void* user_data)
  {
      /* Your code */
  }

  /* Set */
  void
  set_language_changed_cb()
  {
      int ret;
      ret = ma_set_language_changed_cb(__language_changed_cb, NULL);
      if (MA_ERROR_NONE != ret)
          /* Error handling */
  }

  /* Unset */
  void
  unset_language_changed_cb()
  {
      int ret;
      ret = ma_unset_language_changed_cb();
      if (MA_ERROR_NONE != ret)
          /* Error handling */
  }
  ```


## Update result information

To keep the Multi-assistant framework updated about the current progress on voice command processing, voice assistants need to update various types of result information.

1. When the audio data is translated into text using the ASR technology, it is recommended to update the partial ASR result to the Multi-assistant framework so that the partial ASR result is displayed as a visual feedback to the user utterance:

   ```c
   void
   on_asr_result_updated(const char* asr_result)
   {
       int ret;
       ret = ma_send_asr_result(MA_ASR_RESULT_EVENT_PARTIAL_RESULT, asr_result);
       if (MA_ERROR_NONE != ret)
           /* Error handling */
   }
   ```

2. When the voice assistant completed processing user utterance and the final response is made, it can be sent to the Multi-assistant framework to display as the final result:

   ```c
   void
   on_final_result_updated(const char* display_text, const char* utterance_text, const char* result_json)
   {
       int ret;
       ret = ma_send_result(display_text, utterance_text, result_json);
       if (MA_ERROR_NONE != ret)
           /* Error handling */
   }
   ```

3. It is possible to let the Multi-assistant framework know about the recognition result, indicating whether the recognition succeeded or not:

   ```c
   void
   on_recognition_result_updated(const char* result_type)
   {
       ma_recognition_result_event_e result = MA_RECOGNITION_RESULT_ERROR;
       if (strcmp(result_type, "Success") == 0) {
           result = MA_RECOGNITION_RESULT_EVENT_SUCCESS;
       } else if (strcmp(result_type, "Empty Text") == 0) {
           result = MA_RECOGNITION_RESULT_EVENT_EMPTY_TEXT;
       } else if (strcmp(result_type, "False Trigger") == 0) {
           result = MA_RECOGNITION_RESULT_EVENT_FALSE_TRIGGER;
       }
       ret = ma_send_recognition_result(result);
       if (MA_ERROR_NONE != ret)
           /* Error handling */
   }
   ```

## Related information
- Dependencies
  - Tizen 5.5 and Higher for Mobile
  - Tizen 5.5 and Higher for Wearable
