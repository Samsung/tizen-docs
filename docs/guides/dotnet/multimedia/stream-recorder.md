Media Stream Recording
======================

## Dependencies

- Tizen 4.0 and Higher

You can record audio and video from a stream, and control the recording
process through various settings. With the stream recorder, live audio
and video can be kept on your target.

The main features of the `Tizen.Multimedia.StreamRecorder` class
include:

-   Creating a media packet

    You must [create a media packet](#packet) for the stream recording
    using raw data from the source. The media packet must be created for
    each buffer captured from the source and passed to the
    `PushBuffer()` method of the
    `Tizen.Multimedia.StreamRecorder` class.

- Recording audio and video, and controlling the recording

    You can [record a stream, pause, stop, and cancel the
    recording](#record_stream), and push the buffer.

- Managing recording options

    You can [manage various recording details](#manage), such as the
    bitrate, codec, maximum recording length, and filename:

    -   You can encode files in various formats:

        -   Video: MP4 and 3GP
        -   Audio: AMR, AAC, and WAV

        The supported file formats are defined in the
        [Tizen.Multimedia.StreamRecorderFileFormat](https://developer.tizen.org/dev-guide/csapi/namespaceTizen_1_1Multimedia.html#af6f995366abb82b115610e8bebca886c) enumeration.

    - You can use various video and audio encoders.

        The available video and audio codecs are defined in the
        [Tizen.Multimedia.StreamRecorderVideoCodec](https://developer.tizen.org/dev-guide/csapi/namespaceTizen_1_1Multimedia.html#aee3cc1eff93fd449ec54c9e6442ccc64)
        and
        [Tizen.Multimedia.StreamRecorderAudioCodec](https://developer.tizen.org/dev-guide/csapi/namespaceTizen_1_1Multimedia.html#ac2a9d3752357fdf9bd3f8aab627c7d08) enumerations.

Valid input sources consist of external sources, such as a live buffer
passed by the application. Most operations of the stream recorder work
synchronously.

The following figure illustrates general stream recorder state changes.
Use the stream recorder methods according to pre and post conditions, by
following the state changes.

**Figure: Stream recorder state changes**

![Stream recorder state
changes](./media/streamrecorder_states_cs.png)


Prerequisites
-------------

To use the methods and properties of the
[Tizen.Multimedia.StreamRecorder](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1Multimedia_1_1StreamRecorder.html)
class, include the
[Tizen.Multimedia](https://developer.tizen.org/dev-guide/csapi/namespaceTizen_1_1Multimedia.html)
namespace in your application:

``` {.prettyprint}
using Tizen.Multimedia;
```


Managing Recording Options <a id="manage"></a>
--------------------------

To define recording options for video recording:
1.  Create an instance of the
    [Tizen.Multimedia.StreamRecorderOptions](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1Multimedia_1_1StreamRecorderOptions.html)
    class with the output path and file format for the recorded media
    stream:

    ``` {.prettyprint}
    var options = new StreamRecorderOptions(SavePath, RecorderFileFormat.Mp4);
    ```

    You can check which file formats the device supports using the
    `GetSupportedFileFormats()` method of the
    [Tizen.Multimedia.StreamRecorder.Capabilities](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1Multimedia_1_1StreamRecorder_1_1Capabilities.html) class.

2. Define the video recording options in the `Video` property of the
    `Tizen.Multimedia.StreamRecorderOptions` class, using an instance of
    the
    [Tizen.Multimedia.StreamRecorderVideoOptions](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1Multimedia_1_1StreamRecorderVideoOptions.html)
    class:

    ``` {.prettyprint}
    options.Video = new StreamRecorderVideoOptions(codec: RecorderVideoCodec.H263,
                                                   resolution: new Size(1920, 1080),
                                                   sourceFormat: StreamRecorderVideoFormat.Nv12,
                                                   frameRate: 30,
                                                   bitRate: 288000);
    ```

    To get a list of video codecs the device supports, use the
    `GetSupportedVideoEncodings()` method of the
    `Tizen.Multimedia.StreamRecorder.Capabilities` class. The following
    example retrieves the first supported codec found:

    ``` {.prettyprint}
    var streamRecorder = new StreamRecorder();

    var videoCodec = streamRecorder.Capabilities.GetSupportedVideoEncodings().First();
    ```

    **Note** Even if a higher bitrate is set, the recording bitrate is
    limited by that of the stream buffer pushed.


Similarly, to record an audio stream, define the audio recording options
in the `Audio` property of the `StreamRecorderOptions` class instance,
using an instance of the
[Tizen.Multimedia.StreamRecorderAudioOptions](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1Multimedia_1_1StreamRecorderAudioOptions.html)
class.


Creating a Media Packet <a id="packet"></a>
-----------------------

When the stream recorder is configured, create the media packet using
the raw data from the source:

``` {.prettyprint}
byte[] rawbuffer; /// Data to be passed for recording

var videoFormat = new VideoMediaFormat(MediaFormatVideoMimeType.Mpeg4SP, new Size(640, 480));
var mediaPacket = MediaPacket.Create(videoFormat);

mediaPacket.CopyFrom(rawbuffer, 0, rawbuffer.length);
```

The media packet must be created for each buffer captured from the
source and passed to the `PushBuffer()` method of the
[Tizen.Multimedia.StreamRecorder](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1Multimedia_1_1StreamRecorder.html)
class when the stream recorder is prepared to record.


Recording a Stream <a id="record_stream"></a>
------------------

To record a stream:

1.  Call the `Prepare()` method of the
    [Tizen.Multimedia.StreamRecorder](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1Multimedia_1_1StreamRecorder.html)
    class with a
    [Tizen.Multimedia.StreamRecorderOptions](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1Multimedia_1_1StreamRecorderOptions.html)
    instance:

    ``` {.prettyprint}
    streamRecorder.Prepare(options);
    ```

    The stream recorder state changes to `Ready`.

2. Start recording by calling the `Start()` method:

    ``` {.prettyprint}
    streamRecorder.Start();
    ```

    Once the recording starts, if you set the file path to an existing
    file, the file is removed automatically and replaced with a new one.

    You can only call the `Start()` method in the `Ready` or
    `Paused` state. After starting, the state changes to `Recording`.

    Push the media packet to record audio or video, using the
    `PushBuffer()` method:

    ``` {.prettyprint}
    streamRecorder.PushBuffer(mediaPacket);
    ```

3. During the recording, you can pause or stop it:
    -   To pause recording, use the `Pause()` method:

        ``` {.prettyprint}
        streamRecorder.Pause();
        ```

        The stream recorder state changes from `Recording` to `Paused`.

        To resume recording, use the `Start()` method.

        Alternatively, you can stop pushing the stream buffers. In this
        case, the stream recorder remains in the `Recording` state, and
        continues waiting for buffers. It creates the same effect as a
        pause in the recording.

    - To stop recording and save the result, use the
        `Commit()` method. The recording result is saved to the file
        path defined in the
        `Tizen.Multimedia.StreamRecorderOptions` instance.

        ``` {.prettyprint}
        streamRecorder.Commit();
        ```

        You can only call the `Start()` method in the `Recording` or
        `Paused` state. After committing, the state changes to `Ready`.

    - To stop recording without saving the result, use the
        `Cancel()` method.

        The only difference between this method and the `Commit()`
        method is that the recording data is not written to the file.

        ``` {.prettyprint}
        streamRecorder.Cancel();
        ```

4. When you have finished recording, use the `Unprepare()` method to
    reset the stream recorder:

    ``` {.prettyprint}
    streamRecorder.Unprepare();
    ```

    The stream recorder state changes from `Ready` to `Idle`.
