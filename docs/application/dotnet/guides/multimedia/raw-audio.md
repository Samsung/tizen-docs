# Raw Audio Playback and Recording


Pulse Code Modulated (PCM) data contains uncompressed audio. You can play and record uncompressed audio data both synchronously and asynchronously.

The main uncompressed audio management features are:

-   Playing uncompressed audio

    You can [play uncompressed audio](#play_pcm) in your application.

-   Recording uncompressed audio

    You can [record uncompressed audio](#record_pcm) synchronously or asynchronously.

<a name="play_pcm"></a>
## Audio Output

The [Tizen.Multimedia.AudioPlayback](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Multimedia.AudioPlayback.html) class enables your application to play uncompressed audio. You can [play audio synchronously](#simple_playback), or [do it asynchronously](#async_playback).

Your application must define the following PCM data settings:

-   Audio channels:
    -   Mono (1 channel)
    -   Stereo (2 channels)
-   Audio sample type:
    -   Unsigned 8-bit PCM
    -   Signed 16-bit little endian PCM
-   Audio sample rate:
    -   8000 \~ 48000 Hz

To support various low-end Tizen devices, the application must follow certain guidelines:

-   Do not use excessive instances of the `Tizen.Multimedia.AudioPlayback` class.

    Using many `Tizen.Multimedia.AudioPlayback` class instances decreases application performance, because processing audio data for re-sampling and mixing imposes a heavy burden on the system.

-   Use the device-preferred PCM format.

    To reduce the processing overhead, select the PCM format based on the target device preference (for example, signed 16-bit little endian, stereo, 44100 Hz).

    Using the preferred format reduces internal operations, such as converting audio samples from mono to stereo or re-sampling audio frequency to fit the target device's input sample rate.

-   Reduce event delay and remove glitches.

    The `Tizen.Multimedia.AudioPlayback` class instance works recursively, using events. The smaller the buffer size, the more often events are generated. If you use a small buffer in addition to other resources (for example, a timer or sensor), application performance decreases because the events cause delays. To prevent problems, set an appropriate write buffer size.

    To guarantee that the events of the `Tizen.Multimedia.AudioPlayback` class work independently, create a `Tizen.Multimedia.AudioPlayback` class instance in the event thread.

-   Use double buffering.

    Use the double-buffering mechanism to reduce latency. It works by first writing the data twice before starting playback. After starting, whenever the event handler is called, you can write additional data.

-   Save power.

    If audio playback has stopped for a long time, such as because the screen has switched off or there is no audio data, call the `Unprepare()` method of the `Tizen.Multimedia.AudioPlayback` class to pause the stream and save power. The device cannot go into the sleep mode while the `Tizen.Multimedia.AudioPlayback` instance is in the `Running` state.

<a name="record_pcm"></a>
## Audio Input

You can enable your application to record uncompressed audio from a microphone-type input device. You can [record audio synchronously](#simple_recording) with the [Tizen.Multimedia.AudioCapture](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Multimedia.AudioCapture.html) class, or [do it asynchronously](#async_recording) with the [Tizen.Multimedia.AsyncAudioCapture](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Multimedia.AsyncAudioCapture.html) class.

Audio data is captured periodically. To receive the audio PCM data from the input device, you must implement the audio capture interface to notify the application of audio data events, such as when the audio data buffer is full.

Before recording audio, you must define the following PCM data settings:

-   Input device type:
    -   Microphone
-   Audio channels:
    -   Mono (1 channel)
    -   Stereo (2 channels)
-   Audio sample type:
    -   Unsigned 8-bit PCM
    -   Signed 16-bit little endian PCM
-   Audio sample rate:
    -   8000 \~ 48000 Hz

## Prerequisites


To make your application visible in the Tizen Store only for devices that support a microphone, the application must specify the following feature in the `tizen-manifest.xml` file:

```
<feature name="http://tizen.org/feature/microphone"/>
```

<a name="simple_playback"></a>
## Managing Synchronous Playback

Because the synchronous playback process blocks other processes running in the same thread, launching a playback process from the application main thread can make the application unresponsive. To prevent this, launch the playback process from its own thread.

To play audio:

1.  Prepare the audio output device and start the playback process using the `Prepare()` method of the [Tizen.Multimedia.AudioPlayback](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Multimedia.AudioPlayback.html) class:

    ```
    var audioPlayback = new AudioPlayback(44100, AudioChannel.Mono, AudioSampleType.S16Le);

    /// Prepare the audio output device (start the hardware playback process)
    audioPlayback.Prepare();
    ```

    The hardware device prepares its internal output buffer for playback. Playback begins when the internal output buffer starts receiving audio data.

2.  To start playing the recorded audio, copy the audio data from the local buffer to the internal output buffer using the `Write()` method of the `Tizen.Multimedia.AudioCapture` class:

    ```
    int bytesWritten = audioPlayback.Write(buffer);
    ```

    The returned value represents the number of bytes written to the internal output buffer.

3.  Stop the playback process using the `Unprepare()` method of the `Tizen.Multimedia.AudioCapture` class:

    ```
    audioPlayback.Unprepare();
    ```

<a name="async_playback"></a>
## Managing Asynchronous Playback

The asynchronous playback process uses the `BufferAvailable` event of the [Tizen.Multimedia.AudioPlayback](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Multimedia.AudioPlayback.html) class to play the recorded audio. The event is raised for each recorded audio chunk. In the following example, the audio data is read from a stream.

To start playing the recorded audio:

1.  Add an event handler for the `BufferAvailable` event:

    ```
    audioPlayback.BufferAvailable += OnBufferAvailable;
    ```

2.  Prepare the audio output device and start the playback process using the `Prepare()` method of the `Tizen.Multimedia.AudioCapture` class:

    ```
    audioPlayback.Prepare();
    ```

    The hardware device prepares its internal output buffer for playback.

3.  Play audio from a stream.

    Read audio data from the stream and write it to the internal output buffer using the `Write()` method of the `Tizen.Multimedia.AudioPlayback` class. Playback begins when the internal output buffer starts receiving the audio data.

    ```
    Stream stream;

    void OnBufferAvailable(object sender, AudioPlaybackBufferAvailableEventArgs args)
    {
        if (args.Length > 0)
        {
            try
            {
                /// Allocate a local buffer for reading the audio data from the stream
                byte[] buffer = new byte[args.Length];

                /// Read audio data from the stream and store it in the local buffer
                stream.Read(buffer, 0, args.Length);

                /// Copy the audio data from the local buffer
                /// to the internal output buffer (starts playback)
                audioPlayback.Write(buffer);
            }
            catch(Exception e)
            {
                Tizen.Log.Error(LOG_TAG, "Failed to write. " + e);
            }
        }
    }
    ```

4.  Stop the playback process using the `Unprepare()` method of the `Tizen.Multimedia.AudioCapture` class:

    ```
    /// Stop the hardware playback process
    audioPlayback.Unprepare(output);
    ```

    The device no longer raises the event.

<a name="simple_recording"></a>
## Managing Synchronous Recording

Before starting the synchronous recording process, you need to know the size of the buffer where the recorded audio data is to be saved, based on the expected recording duration. The recording process ends once it has read the specified number of bytes.

To calculate and set the required buffer size, use one of the following options:

-   Calculate the buffer size based on the recommendation of the sound server, such as PulseAudio:

    1.  Retrieve the recommended buffer size using the `GetBufferSize()` method of the [Tizen.Multimedia.AudioCapture](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Multimedia.AudioCapture.html) class:

        ```
        var audioCapture = new AudioCapture(44100, AudioChannel.Mono, AudioSampleType.S16Le);

        int bufferSize = audioCapture.GetBufferSize();
        ```

        If no exception is thrown, the method returns the preferred size in bytes, based on the specified audio parameters.

        The recommended buffer size depends on the device. The size can be different for mobile, wearable, and TV devices.

    2.  Set the buffer size to correspond to the desired recording duration.

        For the device in this example, the `GetBufferSize()` method returns the recommended buffer size for 100 milliseconds of recording time. To determine the total recommended buffer size, multiply the recommended buffer size by 10 (to get the buffer size per second) and by the length of the recording in seconds:

        ```
        const int RecordingSec = 5;

        bufferSize *= 10 * RecordingSec;
        ```

-   Calculate the required buffer size explicitly:

    ```
    int bufferSize = AudioCapture.SampleRate * (audioCapture.Channel == AudioChannel.Stereo ? 2 : 1) *
        (audioCapture.SampleType == AudioSampleType.S16Le ? 2 : 1);

    bufferSize *= RecordingSec;
    ```

The synchronous recording process blocks other processes running in the same thread. Launching a recording process from the application main thread can make the application unresponsive. To prevent this, launch the recording process from its own thread.

To record audio:

1.  Prepare the audio input device and start the recording process using the `Prepare()` method of the `Tizen.Multimedia.AudioCapture` class:

    ```
    audioCapture.Prepare();
    ```

    The hardware device starts buffering the audio recorded by the audio input device. The audio data is buffered to the internal input buffer.

2.  Read the audio data from the internal input buffer using the `Read()` method:

    ```
    byte[] buffer = audioCapture.Read(bufferSize);
    ```

    The `Read()` method can behave in the following ways:

    -   If the method is called immediately after preparing the audio input device, it blocks the thread that it was launched from until it reads bytes specified.
    -   If the method is called with a delay long enough to allow the internal input buffer to store more audio data than the specified size, the method returns immediately without blocking its thread.

3.  Stop the recording process using the `Unprepare()` method:

    ```
    audioCapture.Unprepare();
    ```

<a name="async_recording"></a>
## Managing Asynchronous Recording

The asynchronous recording process uses an event to store the audio recorded by the audio input device. The event is raised for each recorded audio chunk. In this use case, the audio data is stored in a stream.

To start recording audio:

1.  Add an event handler for the `DataAvailable` event of the [Tizen.Multimedia.AsyncAudioCapture](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Multimedia.AsyncAudioCapture.html) class:

    ```
    var asyncAudioCapture = new AsyncAudioCapture(44100, AudioChannel.Mono, AudioSampleType.S16Le);

    /// Add an event handler invoked asynchronously for each recorded audio chunk
    asyncAudioCapture.DataAvailable += OnDataAvailable;
    ```

2.  Prepare the audio input device and start the recording process using the `Prepare()` method of the `Tizen.Multimedia.AsyncAudioCapture` class:

    ```
    asyncAudioCapture.Prepare();
    ```

    The hardware device starts buffering the audio recorded by the audio input device. The audio data is buffered to the internal input buffer. The event is raised for each audio data chunk.

3.  To store the recorded audio data:

    ```
    Stream stream;

    /// Event handler invoked for each recorded audio chunk
    void OnDataAvailable(object sender, AudioDataAvailableEventArgs args)
    {
        /// Write the recorded audio data to the stream
        stream.Write(args.Data, 0, args.Data.Length);
    }
    ```

4.  Stop the recording process using the `Unprepare()` method:

    ```
    asyncAudioCapture.Unprepare();
    ```

    The device no longer raises the event.


## Related Information
* Dependencies
  -   Tizen 4.0 and Higher
