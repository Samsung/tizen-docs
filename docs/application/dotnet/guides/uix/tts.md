# Text-to-speech


TTS (text-to-speech) features include synthesizing text into sound data as utterances and playing them. It is also possible to pause and stop playback.

When your application creates a handle and prepares the TTS service, the TTS service is invoked and connected for background work. This service and your application communicate as the server and the client, respectively.

The main features of the Tizen.Uix.Tts namespace includes the following:

-   Preparing the TTS service for use

    You can [connect the background TTS service](#prepare) to be able to operate TTS.

-   Using basic TTS processes

    The [basic TTS processes](#basic_tts) allow you to register event handlers, add text, set the mode, and control the playback. You can also [set TTS parameters](#parameter_tts).

-   Retrieving TTS information

    You can [get information](#info_tts) on the supported voices, and the current state and voice.

<a name="basic_tts"></a>
## Basic TTS processes

Using TTS, you can, you can accomplish the following tasks:

-   Create a handle and register event handlers.
    -   Create a TTS handle which is used for distinguishing your application from other applications also using TTS.
    -   To get notifications about state changes, language changes, starting or finishing utterances, and errors, [register event handlers](#set).
-   Add text and set the mode.
    -   [Add the text](#text) that you want to have read aloud by the TTS module. The requested text is handled as an utterance. You can add several texts, and they are managed using a queue.
    -   There is a limit on the maximum text length for one utterance, and the time spent for synthesizing is dependent on the text length.
    -   [Get and set the TTS mode](#mode) to manage audio mixing with other sources.
-   Play, pause, and stop playback.
    -   [Synthesize the text in the queue and play the sound data after synthesizing](#control).
    -   You can also pause and stop the playback. If you call the method to stop the playback, all requested data (both the sound data and text in the queue) is deleted.

The TTS life-cycle is described in the following figure.

**Figure: TTS life-cycle**

![TTS life-cycle](./media/csapi_tts.png)

<a name="parameter_tts"></a>
## TTS parameters

You can set the following parameters about TTS:

-   Credential

    The credential is a key to verify the authorization for using the TTS engine. The necessity of the credential depends on the TTS engine. If the TTS engine requests the credential, you can set it using the `SetCredential()` method of the [Tizen.Uix.Tts.TtsClient](/application/dotnet/api/TizenFX/latest/api/Tizen.Uix.Tts.TtsClient.html) class.

-   Private data

    The private data is a setting parameter for applying keys provided by the TTS engine. Using the `SetPrivateData()` method of the `Tizen.Uix.Tts.TtsClient` class, you can set the private data as the corresponding key of the TTS engine.

<a name="info_tts"></a>
## TTS information retrieval

You can get the following information about TTS:

-   [Get the current TTS state](#get). The state is also applied as a precondition for each method.
-   Get the current TTS service state. The service state is changed by the internal behavior of the TTS service.
-   Get the default voice.
    -   In TTS, the voice is defined as a combination of the language and the type, such as male or female.
    -   You can request the synthesis of the text with a specific voice, using the parameters of the `AddText()` method of the [Tizen.Uix.Tts.TtsClient](/application/dotnet/api/TizenFX/latest/api/Tizen.Uix.Tts.TtsClient.html) class. However, if you do not set a specific voice, TTS synthesizes the text with the default voice.
    -   The user can change the default voice in the device settings by modifying the display language or the TTS default language status. If the display language is changed to a non-supported language, the TTS language is changed to UK English.
-   Get a list of supported voices to check whether the language and voice type you want are supported.
-   Get the error message when the error event handler is invoked.
-   Get private data from the TTS engine.

## Prerequisites

To enable your application to use the TTS functionality, follow the steps below:

1.  To use the methods and properties of the [Tizen.Uix.Tts.TtsClient](/application/dotnet/api/TizenFX/latest/api/Tizen.Uix.Tts.TtsClient.html) class, include it in your application:

    ```csharp
    using Tizen.Uix.Tts.TtsClient;
    ```

2.  To use the TTS library, create a TTS handle

    The TTS handle is used in other TTS methods as a parameter. After the handle creation, the TTS state changes to `Created`:

    > [!NOTE]
    > TTS is not thread-safe and depends on the Ecore main loop. Implement TTS within the Ecore main loop and do not use it in a thread.


    ```csharp
    void CreateTtsClient()
    {
        try
        {
            TtsClient tts_inst = new TtsClient();
        }
        catch (Exception e)
        {
            /// Error handling
        }
    }
    ```

3.  When you no longer need the TTS library, destroy the TTS handle by using the `Dispose()` method of the `Tizen.Uix.Tts.TtsClient` class:

    ```csharp
    void DestroyTtsClient()
    {
        try
        {
            tts_inst.Dispose();
        }
        catch (Exception e)
        {
            /// Error handling
        }
    }
    ```

    > [!NOTE]
    > Do not use the `Dispose()` method inside an event handler. Within an event handler, the `Dispose()` method fails and invokes the `OperationFailed` error with the `ErrorOccurred` event of the `Tizen.Uix.Tts.TtsClient` class.

<a name="set"></a>
## Register event handlers

TTS provides event handlers to get various information, such as state changes and the start or completion of an utterance.

You can only register event handlers when the TTS state is `Created`.

Event handlers can be set for the following events of the [Tizen.Uix.Tts.TtsClient](/application/dotnet/api/TizenFX/latest/api/Tizen.Uix.Tts.TtsClient.html) class:

-   State changed

    To get a notification when the TTS state changes, register an event handler for the `StateChanged` event:

    ```csharp
    /// Event handler
    void TtsStateChanged(object sender, StateChangedEventArgs e)
    {
        /// Your code
    }

    void SetUnsetStateChangedCb()
    {
        try
        {
            /// Register the event handler for the StateChanged event
            tts_inst.StateChanged += TtsStateChanged;

            /// Deregister the event handler
            tts_inst.StateChanged -= TtsStateChanged;
        }
        catch (Exception e)
        {
            /// Error handling
        }
    }
    ```

-   Service State changed

    To get a notification when the TTS service state changes, register an event handler for the `ServiceStateChanged` event:

    ```csharp
    /// Event handler
    void TtsServiceStateChanged(object sender, ServiceStateChangedEventArgs e)
    {
        /// Your code
    }

    void SetUnsetServiceStateChangedCb()
    {
        try
        {
            /// Register the event handler for the ServiceStateChanged event
            tts_inst.ServiceStateChanged += TtsServiceStateChanged;

            /// Deregister the event handler
            tts_inst.ServiceStateChanged -= TtsServiceStateChanged;
        }
        catch (Exception e)
        {
            /// Error handling
        }
    }
    ```

-   Default voice changed

    In the TTS library, the voice includes the language used and the voice type, such as male or female. The default voice of the TTS is changed either when the system language is changed, or through the TTS settings. To get a notification of a voice change, register an event handler for the `DefaultVoiceChanged` event:

    ```csharp
    /// Event handler
    void TtsDefaultVoiceChanged(object sender, DefaultVoiceChangedEventArgs e)
    {
        /// Your code
    }

    void SetUnsetDefaultVoiceChangedCb()
    {
        try
        {
            /// Register the event handler for the DefaultVoiceChanged event
            tts_inst.DefaultVoiceChanged += TtsDefaultVoiceChanged;

            /// Deregister the event handler
            tts_inst.DefaultVoiceChanged -= TtsDefaultVoiceChanged;
        }
        catch (Exception e)
        {
            /// Error handling
        }
    }
    ```

-   Engine changed

    To get a notification when the engine is changed by TTS, register an event handler for the `EngineChanged` event:

    ```csharp
    /// Event handler
    void TtsEngineChanged(object sender, EngineChangedEventArgs e)
    {
        /// Your code
    }

    void SetUnsetEngineChangedCb()
    {
        try
        {
            /// Register the event handler for the EngineChanged event
            tts_inst.EngineChanged += TtsEngineChanged;

            /// Deregister the event handler
            tts_inst.EngineChanged -= TtsEngineChanged;
        }
        catch (Exception e)
        {
            /// Error handling
        }
    }
    ```

-   Utterance started or completed

    If you add text in TTS, that text is handled as an utterance and it obtains its own ID. After you request the TTS process to start, the text is synthesized by an engine and played. Each event handler is invoked in the following cases:
    
     |     Event handler    |               Invoked when                | TTS state |
     | :------------------: | :---------------------------------------: | :-------: |
     |  `UtteranceStarted`  | Playing the synthesized audio is started  | `Ready` > `Playing` |
     | `UtteranceCompleted` | Playing the synthesized audio is finished | `Playing` (The state is NOT changed until `Stop()` is called.) |

    > [!NOTE]
    > `UtteranceCompleted` is NOT invoked when the following occurs:
    >
    > (1) Your application calls `Stop()`.
    >
    > (2) Playing the synthesized audio is stopped by another application.
    >
    > Although the `UtteranceCompleted` event handler is not invoked, a `StateChanged` event handler will be invoked. (The state will be changed from `Playing` to `Ready`.)
    
    
    To get a notification when an utterance is started or completed, register event handlers for the `UtteranceStarted` and `UtteranceCompleted` events, respectively:

    ```csharp
    /// Utterance started event handler
    void TtsUtteranceStarted(object sender, UtteranceEventArgs e)
    {
        /// Your code
    }

    /// Utterance completed event handler
    void TtsUtteranceCompleted(object sender, UtteranceEventArgs e)
    {
        /// Your code
    }

    void SetUnsetUtteranceCb()
    {
        try
        {
            /// Register the event handlers for the UtteranceStarted and UtteranceCompleted events
            tts_inst.UtteranceStarted += TtsUtteranceStarted;
            tts_inst.UtteranceCompleted += TtsUtteranceCompleted;

            /// Deregister the event handlers
            tts_inst.UtteranceStarted -= TtsUtteranceStarted;
            tts_inst.UtteranceCompleted -= TtsUtteranceCompleted;
        }
        catch (Exception e)
        {
            /// Error handling
        }
    }
    ```

-   Error

    To get a notification when an error occurs, register an event handler for the `ErrorOccurred` event:

    ```csharp
    /// Event handler
    void TtsErrorOccurred(object sender, ErrorOccurredEventArgs e)
    {
        /// Your code
    }

    void SetUnsetErrorOccurredCb()
    {
        try
        {
            /// Register the event handler for the ErrorOccurred event
            tts_inst.ErrorOccurred += TtsErrorOccurred;

            /// Deregister the event handler
            tts_inst.ErrorOccurred -= TtsErrorOccurred;
        }
        catch (Exception e)
        {
            /// Error handling
        }
    }
    ```

-   Synthesized PCM

    To get a notification when a synthesized PCM data is received from a TTS service, register an event handler for `SynthesizedPcm` event:

    ```csharp
    /// Event handler
    void TtsSynthesizedPcm(object sender, SynthesizedPcmEventArgs e)
    {
        /// Your code
    }

    void SetUnsetSynthesizedPcmCb()
    {
        try
        {
            /// Register the event handler for the SynthesizedPcm event
            tts_inst.SynthesizedPcm += TtsSynthesizedPcm;

            /// Deregister the event handler
            tts_inst.SynthesizedPcm -= TtsSynthesizedPcm;
        }
        catch (Exception e)
        {
            /// Error handling
        }
    }
    ```

<a name="get"></a>
## Get information

To obtain the current state, the supported voice list, and the current voice, follow the steps below:

-   Retrieve the current TTS state by using the `CurrentState` property of the [Tizen.Uix.Tts.TtsClient](/application/dotnet/api/TizenFX/latest/api/Tizen.Uix.Tts.TtsClient.html) class.

    The TTS state is changed by various TTS methods, and it is applied as a precondition for each method:

    ```csharp
    void GetState()
    {
        try
        {
            State current_state;
            current_state = TtsClient.CurrentState;
        }
        catch (Exception e)
        {
            /// Error handling
        }
    }
    ```

-   Retrieve the current TTS service state by using the `CurrentServiceState` property of the [Tizen.Uix.Tts.TtsClient](/application/dotnet/api/TizenFX/latest/api/Tizen.Uix.Tts.TtsClient.html) class:

    ```csharp
    void GetServiceState()
    {
        try
        {
            ServiceState current_service_state;
            current_service_state = TtsClient.CurrentServiceState;
        }
        catch (Exception e)
        {
            /// Error handling
        }
    }
    ```

-   Obtain a list of TTS-supported voices by using the `GetSupportedVoices()` method of the `Tizen.Uix.Tts.TtsClient` class:

    ```csharp
    void GetSupportedVoice()
    {
        try
        {
            List<SupportedVoice> voicesList = new List<SupportedVoice>();
            voiceList = tts_inst.GetSupportedVoices();
        }
        catch (Exception e)
        {
            /// Error handling
        }
    }
    ```

-   Get the default voice by using the `DefaultVoice` property

    TTS synthesizes the text using the default voice, if you do not set the language and the voice type as parameters of the `AddText()` method of the `Tizen.Uix.Tts.TtsClient` class:

    ```csharp
    void GetDefaultVoice()
    {
        try
        {
            SupportedVoice default_voice = tts_inst.DefaultVoice;
        }
        catch (Exception e)
        {
            /// Error handling
        }
    }
    ```

    You can get a notification about changes to the default voice by registering an event handler for the `DefaultVoiceChanged` event of the `Tizen.Uix.Tts.TtsClient` class.

<a name="mode"></a>
## Get and set the mode

There are 3 different TTS modes available. The main difference is audio mixing with other sources. The default mode is `Default`, used for normal applications, such as e-books. If you set this mode and play your text, it can be interrupted when other sounds, such as ringtone or other TTS sounds, are played.

> [!NOTE]
> The `Notification` and `ScreenReader` modes are mixed with other sound sources, but they are used only for platform-specific features. Do not use them for normal applications.

Get and set the mode in the `Created` state:

```csharp
void SetMode(Mode mode)
{
    try
    {
        tts_inst.CurrentMode = mode;
    }
    catch (Exception e)
    {
        /// Error handling
    }
}

void GetMode(Mode* mode)
{
    try
    {
        *mode = tts_inst.CurrentMode;
    }
    catch (Exception e)
    {
        /// Error handling
    }
}
```

<a name="prepare"></a>
## Connect and disconnect TTS

To operate TTS, follow these steps:

1.  After you create the TTS handle, connect the background TTS service with the `Prepare()` method of the [Tizen.Uix.Tts.TtsClient](/application/dotnet/api/TizenFX/latest/api/Tizen.Uix.Tts.TtsClient.html) class.

    The TTS service synthesizes the text with the engine and plays the resulting sound data. The method is asynchronous and the TTS state changes to `Ready`:

    ```csharp
    void PrepareTtsClient()
    {
        try
        {
            tts_inst.Prepare();
        }
        catch (Exception e)
        {
            /// Error handling
        }
    }
    ```

    > [!NOTE]
    > If the error event handler is invoked after calling the `Prepare()` method, TTS is not available.

2.  When the connection is no longer needed, use the `Unprepare()` method to disconnect TTS and change the TTS state to `Created`:

    ```csharp
    void UnprepareTtsClient()
    {
        try
        {
            tts_inst.Unprepare();
        }
        catch (Exception e)
        {
            /// Error handling
        }
    }
    ```

<a name="engine"></a>
## Set and get TTS engine options

To set and get TTS engine options, follow these steps:

-   Set the credential

    The credential is a key to verify the authorization for using the TTS engine. The necessity of the credential depends on the engine. If the engine requests the credential, you can set it using the `SetCredential()` method of the [Tizen.Uix.Tts.TtsClient](/application/dotnet/api/TizenFX/latest/api/Tizen.Uix.Tts.TtsClient.html) class:

    ```csharp
    void SetCredential(string credential)
    {
        try
        {
            tts_inst.SetCredential(credential);
        }
        catch (Exception e)
        {
            /// Error handling
        }
    }
    ```

-   Set and get the private data

    The private data is a setting parameter for applying keys provided by the TTS engine. To set the private data and use the corresponding key of the engine, use the `SetPrivateData()` method:

    > [!NOTE]
    > The key and data are determined by the TTS engine. To set and get the private data, see the engine instructions.

    ```csharp
    void SetPrivateData(string key, string data)
    {
        try
        {
            tts_inst.SetPrivateData(key, data);
        }
        catch (Exception e)
        {
            /// Error handling
        }
    }
    ```

    To get the private data which corresponds to a specific key from the engine, use the `GetPrivateData()` method:

    ```csharp
    void GetPrivateData(string key)
    {
        try
        {
            string privatedata;

            privatedata = tts_inst.GetPrivateData(key);
        }
        catch (Exception e)
        {
            /// Error handling
        }
    }
    ```

<a name="text"></a>
## Add text

To add text, follow these steps:

-   You can request the TTS library to read your own text using the `AddText()` method of the [Tizen.Uix.Tts.TtsClient](/application/dotnet/api/TizenFX/latest/api/Tizen.Uix.Tts.TtsClient.html) class. The TTS library manages added text using queues, so it is possible to add several texts simultaneously. Each obtained text receives an utterance ID, which is used for synthesizing and playing the sound data.

    > [!NOTE]
    > If the added text is too long, some engines need a long time for synthesis. It is recommended to only use proper length text clips.

    If the `language` parameter is `NULL`, the default language is used for synthesizing the text.

    You can add text to TTS at any point after the `Prepare()` method changes the TTS state to `Ready`:

    ```csharp
    void AddText()
    {
        try
        {
            string text = "tutorial"; /// Text to be read
            string language = "en_US"; /// Language
            int voice_type = Voice.Female; /// Voice type
            int speed = 0; /// Read speed; 0 for Auto

            tts_inst.AddText(text, language, voice_type, speed);
        }
        catch (Exception e)
        {
            /// Error handling
        }
    }
    ```

-   There is a length limit for added text in the engine. To retrieve the maximum value, use the `MaxTextSize` property of the `Tizen.Uix.Tts.TtsClient` class in the `Ready` state:

    ```csharp
    void GetMaximumTextSize()
    {
        try
        {
            int max_text_size = tts_inst.MaxTextSize;
        }
        catch (Exception e)
        {
            /// Error handling
        }
    }
    ```

<a name="control"></a>
## Control playback

To start, pause, and stop the playback, follow the steps below:

-   To start synthesizing the text added in the queue and play the resulting sound data in sequence, use the `Play()` method of the [Tizen.Uix.Tts.TtsClient](/application/dotnet/api/TizenFX/latest/api/Tizen.Uix.Tts.TtsClient.html) class.

    The TTS state is changed to `Playing`, and the playback continues until you call the `Stop()` or the `Pause()` method.

    If there is no text in the queue, TTS stays in the `Playing` state for text to be added. In that case, when text is added, TTS starts synthesizing and playing it immediately. There is no need to change the state to `Ready` by using the `Stop()` method even when there is no text in the queue. It will continue to stay in the `Playing` state:

    > [!NOTE]
    > If the TTS state changed event handler is invoked, state change can occur without any controlling methods being called. In this case, the state change takes place only when other applications request TTS play, the audio session requests TTS pause or the TTS engine changes.

    ```csharp
    void Start()
    {
        try
        {
            tts_inst.Play();
        }
        catch (Exception e)
        {
            /// Error handling
        }
    }
    ```


-   To pause the playback, use the `Pause()` method.

    The TTS state is changed to `Paused`. To resume playback, use the `Play()` method:

    ```csharp
    void Pause()
    {
        try
        {
            tts_inst.Pause();
        }
        catch (Exception e)
        {
            /// Error handling
        }
    }
    ```

-   To stop the playback, use the `Stop()` method.

    All the texts in the queue are removed, and the TTS state is changed to `Ready`:

    ```csharp
    void Stop()
    {
        try
        {
            tts_inst.Stop();
        }
        catch (Exception e)
        {
            /// Error handling
        }
    }
    ```


-   To repeat the last added text, use the `Repeat()` method.

    The `Repeat()` method returns the information about the last added text and the TTS state is changed to `Playing`.

    If no text has been added before, an exception occurs. To handle the exception, contain a block of code as follow:

    ```csharp
    void Repeat()
    {
        try
        {
            string text = "tutorial"; /// Text to be read
            string language = "en_US"; /// Language
            int voice_type = Voice.Female; /// Voice type
            int speed = 0; /// Read speed; 0 for Auto

            tts_inst.AddText(text, language, voice_type, speed);
            tts_inst.Play();

            ...

            tts_inst.Stop();
            RepeatedText text = tts_inst.Repeat();
        }
        catch (Exception e)
        {
            /// Error handling
        }
    }
    ```

<a name="playing_mode"></a>
## Playing mode

Playing mode determines which process, either TTS service or TTS client, plays the synthesized PCM data. Described below are the 2 different types of playing modes:

> [!NOTE]
> Playing mode is different from TTS mode. Playing mode only determines a subject to play PCM data.

- `ByService`: TTS service plays the synthesized PCM data. If you do not set playing mode, it will be set as `ByService`.
- `ByClient`: TTS client receives the synthesized PCM data from the TTS service and plays it directly.

To decide between the client-side playback mode and the service-side playback mode, follow the step below:

-   Set the playing mode

    If the application wants to play the PCM data directly instead of playing the one that the application requested for synthesis in the TTS service, you can set the playback mode to `ByClient`. If the playback mode is not set by the user, the TTS service will synthesize the text and play it using the default value `ByService`:

    > [!NOTE]
    > If the playing mode is `ByService`, you don't need to set an event handler. It will be played automatically by the TTS service. If you set the mode to `ByClient`, you can receive the synthesized PCM data via `SynthesizedPcm` event and only change playing mode when TTS client state is `Created`. If you want to use both playing modes, it would be better to create 2 TTS handles.

    ```csharp
    void SetPlayingMode()
    {
        try
        {
            tts_inst.PlayingMode = PlayingMode.ByClient;
        }
        catch (Exception e)
        {
            /// Error handling
        }
    }
    ```


## Related information
- Dependencies
  - Tizen 4.0 and Higher

- API References
  - [Tizen.Uix.Tts.TtsClient](/application/dotnet/api/TizenFX/latest/api/Tizen.Uix.Tts.TtsClient.html)