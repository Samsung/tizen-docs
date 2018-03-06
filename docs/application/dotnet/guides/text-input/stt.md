# Speech-to-text


STT (speech-to-text) features enable recognizing sound data recorded by the user and sending the result as text.

When your application creates a handle and prepares the STT service, the STT daemon is invoked and connected for background work. This daemon and your application communicate as the server and the client.

The main features of the Tizen.Uix.Stt namespace include:

-   Preparing the STT service for use

    You can [connect the background STT daemon](#prepare) to be able to operate STT.

-   Using basic STT processes

    The [basic processes](#basic_stt) allow you to register event handlers, control the recording, and set options. You can also [set STT parameters](#parameter_stt).

-   Retrieving STT information

    You can [get information](#info_stt) that includes, for example, language and state.

<a name="basic_stt"></a>
## Basic STT Processes

Using STT, you can:

-   Create a handle and register event handlers.
    -   Create an STT handle, which is used for distinguishing your application from other applications also using STT.
    -   [Get notifications on state changes](#set), language changes, recognition results, and errors by registered event handlers.
-   Start, stop, and cancel recognition.
    -   [Start recording the user voice](#option) by microphone and analyze the recorded data as text.
    -   If you stop the recording manually, STT stops the recording and recognizes the sound data. The recognized text is then sent by the registered event handler.
    -   You also can set sounds which are played before STT recording starts or after it stops.
-   Get the recognition result.
    -   The recognition result is sent by the registered event handler.
    -   With a specific STT engine, you can obtain the time stamp information for the recognition result.
    -   Some STT engines send the recognition result partially during the user recording. You can get the result information using the parameter of the recognition result event handler.

The STT life-cycle is described in the following figure.

**Figure: STT life-cycle**

![STT life-cycle](./media/csapi_stt.png)

<a name="parameter_stt"></a>
## STT Parameters

You can set the following parameters about STT:

-   Credential

    The credential is a key to verify the authorization for using the STT engine. The necessity of the credential depends on the STT engine. If the STT engine requests the credential, you can set it using the `SetCredential()` method of the [Tizen.Uix.Stt.SttClient](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Uix.Stt.SttClient.html) class.

-   Private data

    The private data is a setting parameter for applying keys provided by the STT engine. Using the `SetPrivateData()` method of the `Tizen.Uix.Stt.SttClient` class, you can set the private data as the corresponding key of the STT engine.

<a name="info_stt"></a>
## STT Information Retrieval

You can get the following information about STT:

-   [Get the current STT state](#get). The state is also applied as a precondition for each method.
-   Get the default language.
    -   You can start recognition with the language that you want as a parameter of the `Start()` method of the [Tizen.Uix.Stt.SttClient](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Uix.Stt.SttClient.html) class. However, if you do not set a specific language, STT starts recording and uses the default language for recognition.
    -   The user can change the default language in the device settings, by modifying the display language or the STT default language status. If the display language is changed to a non-supported one, the STT language is changed to UK English.
-   Get a list of the supported languages to check whether the language you want is supported.
-   Get a list of the supported engines and the selection of current engines. Additional features, such as silence detection and partial result, are provided by specific engines.
-   Get the error message when the error event handler is invoked.
-   Get private data from the STT engine.

## Prerequisites

To enable your application to use the STT functionality:

1.  To use the methods and properties of the [Tizen.Uix.Stt](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Uix.Stt.html) namespace, include it in your application:

    ```
    using Tizen.Uix.Stt;
    ```

2.  To use the STT library and create an STT handle, create a new instance of the [Tizen.Uix.Stt.SttClient](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Uix.Stt.SttClient.html) class.

    The instance is used to launch other STT methods. After the instance has been created, the STT state changes to `Created`.


    > **Note**   
	> STT is not thread-safe and depends on the Ecore main loop. Implement STT within the Ecore main loop and do not use it in a thread.

    ```
    void CreateSttClient()
    {
        try
        {
            SttClient stt_inst = new SttClient();
        }
        catch (Exception e)
        {
            /// Error handling
        }
    }
    ```

3.  When you no longer need the STT library, destroy the STT client instance with the `Dispose()` method:

    ```
    void DestroySttClient()
    {
        try
        {
            stt_inst.Dispose();
        }
        catch (Exception e)
        {
            /// Error handling
        }
    }
    ```

    > **Note**   
	> Do not use the `Dispose()` method inside an event handler. Within an event handler, the `Dispose()` method fails and invokes the `OperationFailed` error with the `ErrorOccurred` event of the `Tizen.Uix.Stt.SttClient` class.

<a name="set"></a>
## Registering Event Handlers

STT provides event handlers to get various information, such as the recognition result, state changes, language changes, and errors.

You can only register event handlers when the STT state is `Created`.

Event handlers can be set for the following events of the [Tizen.Uix.Stt.SttClient](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Uix.Stt.SttClient.html) class:

-   State changed

    To get a notification when the STT stage changes, register an event handler for the `StateChanged` event:

    ```
    /// Event handler
    void SttStateChanged(object sender, StateChangedEventArgs e)
    {
        /// Your code
    }

    void SetUnsetStateChangedCb()
    {
        try
        {
            /// Register the event handler for the StateChanged event
            stt_inst.StateChanged += SttStateChanged;

            /// Deregister the event handler
            stt_inst.StateChanged -= SttStateChanged;
        }
        catch (Exception e)
        {
            /// Error handling
        }
    }
    ```

-   Default language changed

    The default language of STT is changed either when the system language is changed, or through the STT settings. To get a notification when the language changes, register an event handler for the `DefaultLanguageChanged` event:

    ```
    /// Event handler
    void SttDefaultLanguageChanged(object sender, DefaultLanguageChangedEventArgs e)
    {
        /// Your code
    }

    void SetUnsetDefaultLanguageChangedCb()
    {
        try
        {
            /// Register the event handler for the DefaultLanguageChanged event
            stt_inst.DefaultLanguageChanged += SttDefaultLanguageChanged;

            /// Deregister the event handler
            stt_inst.DefaultLanguageChanged -= SttDefaultLanguageChanged;
        }
        catch (Exception e)
        {
            /// Error handling
        }
    }
    ```

-   Recognition result

    To get the STT recognition result, register an event handler for the `RecognitionResult` event:

    ```
    /// Event handler
    void SttRecognitionResult(object sender, RecognitionResultEventArgs e)
    {
        /// Your code
    }

    void SetUnsetRecognitionResultCb()
    {
        try
        {
            /// Register the event handler for the RecognitionResult event
            stt_inst.RecognitionResult += SttRecognitionResult;

            /// Deregister the event handler
            stt_inst.RecognitionResult -= SttRecognitionResult;
        }
        catch (Exception e)
        {
            /// Error handling
        }
    }
    ```

-   Engine changed

    To get a notification when the engine is changed by STT, register an event handler for the `EngineChanged` event:

    ```
    /// Event handler
    void SttEngineChanged(object sender, EngineChangedEventArgs e)
    {
        /// Your code
    }

    void SetUnsetEngineChangedCb()
    {
        try
        {
            /// Register the event handler for the EngineChanged event
            stt_inst.EngineChanged += SttEngineChanged;

            /// Deregister the event handler
            stt_inst.EngineChanged -= SttEngineChanged;
        }
        catch (Exception e)
        {
            /// Error handling
        }
    }
    ```

-   Error

    To get a notification when an error occurs, register an event handler for the `ErrorOccurred` event:

    ```
    /// Event handler
    void SttErrorOccurred(object sender, ErrorOccurredEventArgs e)
    {
        /// Your code
    }

    void SetUnsetErrorOccurredCb()
    {
        try
        {
            /// Register the event handler for the ErrorOccurred event
            stt_inst.ErrorOccurred += SttErrorOccurred;

            /// Deregister the event handler
            stt_inst.ErrorOccurred -= SttErrorOccurred;
        }
        catch (Exception e)
        {
            /// Error handling
        }
    }
    ```

<a name="get"></a>
## Getting Information

To obtain the current STT state, the list of supported languages, and the current language:

-   Retrieve the current STT state by using the `CurrentState` property of the [Tizen.Uix.Stt.SttClient](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Uix.Stt.SttClient.html) class.

    The STT state is changed by various STT methods, and it is applied as a precondition for each method.

    ```
    void GetState()
    {
        State current_state;
        current_state = SttClient.CurrentState;
    }
    ```

-   Retrieve a list of languages supported by STT by using the `GetSupportedLanguages()` method:

    ```
    void GetSupportedLanguage()
    {
        try
        {
            List<string> list = (List<string>)stt_inst.GetSupportedLanguages();
        }
        catch (Exception e)
        {
            /// Error handling
        }
    }
    ```

-   Retrieve the default language by using the `DefaultLanguage` property of the `Tizen.Uix.Stt.SttClient` class:

    ```
    void GetDefaultLanguage()
    {
        try
        {
            string default_lang = stt_inst.DefaultLanguage;
        }
        catch (Exception e)
        {
            /// Error handling
        }
    }
    ```

    You can get a notification about default language changes by registering an event handler for the `DefaultLanguageChanged` event of the `Tizen.Uix.Stt.SttClient` class.

-   Retrieve a list of engines supported by STT by using the `GetSupportedEngines()` method of the `Tizen.Uix.Stt.SttClient` class:

    ```
    void GetSupportedEngine()
    {
        try
        {
            List<SupportedEngine> list = (List<SupportedEngine>)stt_inst.GetSupportedEngines();
        }
        catch (Exception e)
        {
            /// Error handling
        }
    }
    ```

-   Retrieve or set the current engine for STT recognition by using the `Engine` property of the `Tizen.Uix.Stt.SttClient` class.

    The supported language, silence detection, and supported recognition types depend on the STT engine.

    ```
    void SetGetCurrentEngine()
    {
        try
        {
            string current_engine_id = "stt-engine-default";

            /// Set the current engine
            stt_inst.Engine = current_engine_id;

            /// Get the current engine
            current_engine_id = stt_inst.Engine;
        }
        catch (Exception e)
        {
            /// Error handling
        }
    }
    ```

-   Check whether a recognition type is supported by the current engine, by using the `IsRecognitionTypeSupported()` method of the `Tizen.Uix.Stt.SttClient` class. Use the values of the [Tizen.Uix.Stt.RecognitionType](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Uix.Stt.RecognitionType.html) enumeration as a parameter.

    The normal recognition type, `Stt.RecognitionType.Free`, means that the whole recognition result is sent at the end of the recognition process. The `Stt.RecognitionType.Partial` recognition type is used to get a partial recognition result.

    ```
    void CheckSupportedRecognitionType()
    {
        try
        {
            bool support;

            support = stt_inst.IsRecognitionTypeSupported(Stt.RecognitionType.Partial);
        }
        catch (Exception e)
        {
            /// Error handling
        }
    }
    ```

<a name="prepare"></a>
## Connecting and Disconnecting STT

To operate STT:

1.  After you have initialized STT by creating the [Tizen.Uix.Stt.SttClient](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Uix.Stt.SttClient.html) class instance, connect the background STT daemon with the `Prepare()` method of that class.

    The method is asynchronous and the STT state changes to `Ready`.

    ```
    void PrepareSttClient()
    {
        try
        {
            stt_inst.Prepare();
        }
        catch (Exception e)
        {
            /// Error handling
        }
    }
    ```

    > **Note**   
	> If the error event handler is invoked after calling the `Tizen.Uix.Stt.SttClient.Prepare()` method, STT is not available.

2.  When the connection is no longer needed, disconnect STT and change the STT state to `Created`, by using the `Unprepare()` method:

    ```
    void UnprepareSttClient()
    {
        try
        {
            stt_inst.Unprepare();
        }
        catch (Exception e)
        {
            /// Error handling
        }
    }
    ```

<a name="engine"></a>
## Setting and Getting STT Engine Options

To set and get STT engine options:

-   Set the credential.

    The credential is a key to verify the authorization for using the STT engine. The necessity of the credential depends on the engine. If the engine requests the credential, you can set it using the `SetCredential()` method of the [Tizen.Uix.Stt.SttClient](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Uix.Stt.SttClient.html) class:

    ```
    void SetCredential(string credential)
    {
        try
        {
            stt_inst.SetCredential(credential);
        }
        catch (Exception e)
        {
            /// Error handling
        }
    }
    ```

-   Set and get the private data.

    The private data is a setting parameter for applying keys provided by the STT engine. To set the private data and use the corresponding key of the engine, use the `SetPrivateData()` method.


    > **Note**   
	> The key and data are determined by the STT engine. To set and get the private data, see the engine instructions.

    ```
    void SetPrivateData(string key, string data)
    {
        try
        {
            stt_inst.SetPrivateData(key, data);
        }
        catch (Exception e)
        {
            /// Error handling
        }
    }
    ```

    To get the private data which corresponds to a specific key from the engine, use the `GetPrivateData()` method:

    ```
    void GetPrivateData(string key)
    {
        try
        {
            string privatedata;

            privatedata = stt_inst.GetPrivateData(key);
        }
        catch (Exception e)
        {
            /// Error handling
        }
    }
    ```

<a name="option"></a>
## Setting Options and Controlling Recording

To set the STT options and control recording:

-   Set the silence detection.

    After STT starts recognizing sound, some STT engines can detect silence when the sound input from the user ends. If the silence detection is enabled, the STT library stops recognition automatically and sends the result. Otherwise, you can manually stop the recognition process using the `Stop()` method of the [Tizen.Uix.Stt.SttClient](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Uix.Stt.SttClient.html) class.

    To set the silence detection state, use the `SetSilenceDetection()` method, using values of the [Tizen.Uix.Stt.SilenceDetection](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Uix.Stt.SilenceDetection.html) enumeration as a parameter. If you set the silence detection as `SilenceDetection.Auto`, STT works according to the global STT setting. This option must be set when STT is in the `Ready` state.

    ```
    void SetSilenceDetection(SilenceDetection type)
    {
        try
        {
            /// Default type is SilenceDetection.Auto
            stt_inst.SetSilenceDetection(type);
        }
        catch (Exception e)
        {
            /// Error handling
        }
    }
    ```

-   Set or unset the start sound.

    To play a sound before STT recognition starts, call the `SetStartSound()` method in the `Ready` state.

    > **Note**   
	> The sound file path must be a full path. Only WAV format sound files are supported.

    ```
    void SetStartSound(string filename)
    {
        try
        {
            stt_inst.SetStartSound(filename);
        }
        catch (Exception e)
        {
            /// Error handling
        }
    }
    ```

    To unset the recording start sound, use the `UnsetStartSound()` method:

    ```
    void UnsetStartSound()
    {
        try
        {
            stt_inst.UnsetStartSound();
        }
        catch (Exception e)
        {
            /// Error handling
        }
    }
    ```

-   Set or unset the stop sound.

    To play a sound when STT recognition stops, use the `SetStopSound()` method in the `Ready` state:

    > **Note**   
	> The sound file path must be a full path. Only WAV format sound files are supported.

    ```
    void SetStopSound(string filename)
    {
        try
        {
            stt_inst.SetStopSound(filename);
        }
        catch (Exception e)
        {
            /// Error handling
        }
    }
    ```

    To unset the recording stop sound, use the `UnsetStopSound()` method:

    ```
    void UnsetStopSound()
    {
        try
        {
            stt_inst.UnsetStopSound();
        }
        catch (Exception e)
        {
            /// Error handling
        }
    }
    ```

-   To control the speech recognition:
    -   To start recording, use the `Start()` method.

        The connected STT daemon starts recording, and the STT state is changed to `Recording`.

        > **Note**   
		> If the `Start()` method fails, check the error code and take appropriate action.

        The language and recognition type must be supported by the current STT engine. If you set `NULL` as the language parameter, the STT default language is used based on the `DefaultLanguage` property of the currently-used `Tizen.Uix.Stt.SttClient` class instance.

        ```
        void Start(string language, RecognitionType type)
        {
            try
            {
                stt_inst.Start(language, type);
            }
            catch (Exception e)
            {
                /// Error handling
            }
        }
        ```

    -   While STT recording is in progress, you can retrieve the current recording volume using the `RecordingVolume` property of the `Tizen.Uix.Stt.SttClient` class.

        The volume value is retrieved periodically with the short-term recorded sound data as dB (decibels). The STT volume normally has a negative value, and 0 is the maximum value.

        ```
        void GetVolume()
        {
            try
            {
                float current_volume;

                current_volume = stt_inst.RecordingVolume;
            }
            catch (Exception e)
            {
                /// Error handling
            }
        }
        ```

    -   To stop the recording and get the recognition result, use the `Stop()` method.

        The recording stops and the STT state is changed to `Processing`. When the recognition result has been processed, the `RecognitionResult` event triggers, and the state changes back to `Ready`.

        ```
        void Stop()
        {
            try
            {
                stt_inst.Stop();
            }
            catch (Exception e)
            {
                /// Error handling
            }
        }
        ```

    -   To cancel the recording without getting the result, use the `Cancel()` method.

        The STT state changes to `Ready`.

        ```
        void Cancel()
        {
            try
            {
                stt_inst.Cancel();
            }
            catch (Exception e)
            {
                /// Error handling
            }
        }
        ```


## Related Information
* Dependencies
  -   Tizen 4.0 and Higher
