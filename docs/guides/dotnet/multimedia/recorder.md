
Media Recording
===============

## Dependencies

- Tizen 4.0 and Higher

You can use basic recorder features, including an audio and video
recorder.

The main media recording features include:

-   Recording audio

    You can [record audio](#record_audio) after you have [prepared the
    audio recorder](#prepare_audio).

- Recording video

    You can [record video](#record_video) after you have [prepared the
    video recorder](#prepare_video).

The following file formats are supported:

-   Video: MP4 and 3GP
-   Audio: M4A and AMR

Valid input sources consist of internal and external microphones and a
camera. The used input audio or video source depends on the currently
connected audio path and camera module of the device.

During testing, you can use the emulator to imitate audio or video
recording, as long as your computer has a proper input source device.


Prerequisites
-------------

To use the media recording functionality in your application:

1.  To use the audio and video recorders, the application has to request
    permission by adding the following privileges to the
    `tizen-manifest.xml` file:

    ``` {.prettyprint}
    <privileges>
       <!--Needed for audio and video recorder-->
       <privilege>http://tizen.org/privilege/recorder</privilege>
       <!--Needed for video recorder only-->
       <privilege>http://tizen.org/privilege/camera</privilege>
    </privileges>
    ```

2. To use the methods and properties of the
    [Tizen.Multimedia.Camera](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1Multimedia_1_1Camera.html)
    and
    [Tizen.Multimedia.Recorder](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1Multimedia_1_1Recorder.html)
    classes, include the
    [Tizen.Multimedia](https://developer.tizen.org/dev-guide/csapi/namespaceTizen_1_1Multimedia.html)
    namespace in your application:

    ``` {.prettyprint}
    using Tizen.Multimedia;
    ```



Preparing the Audio Recorder <a id="prepare_audio"></a>
----------------------------

1.  Create an instance of the
    [Tizen.Multimedia.AudioRecorder](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1Multimedia_1_1AudioRecorder.html)
    class, and pass the audio codec and file format of the recording
    as parameters.

    The possible audio codec values are defined in the
    [Tizen.Multimedia.RecorderAudioCodec](https://developer.tizen.org/dev-guide/csapi/namespaceTizen_1_1Multimedia.html#aeff5757e6b6faa400455658a1353d013)
    enumeration, and the possible file format values in the
    [Tizen.Multimedia.RecorderFileFormat](https://developer.tizen.org/dev-guide/csapi/namespaceTizen_1_1Multimedia.html#a1c2f595cf0e4c146e6b8b9ae31e4cc2a) enumeration.

    Set the correct file format based on the audio codec. For example,
    if you set the codec to `RecorderAudioCodec.Aac`, set the file
    format to `RecorderFileFormat.ThreeGp`.

    ``` {.prettyprint}
    AudioRecorder audioRecorder = new AudioRecorder(RecorderAudioCodec.Aac, RecorderFileFormat.ThreeGp);
    ```

    The recorder state is set to `Idle`.

2. Set various audio recorder settings, such as the file size limit,
    encoder bitrate, and audio device and sample rate:

    ``` {.prettyprint}
    /// Set the maximum file size to 1024 (kB)
    audioRecorder.SizeLimit = 1024;

    /// Set the audio encoder bitrate
    audioRecorder.AudioBitRate = 128000;

    /// Set the audio device as microphone
    audioRecorder.AudioDevice = RecorderAudioDevice.Mic;

    /// Set the audio sample rate
    audioRecorder.AudioSampleRate = 44100;
    ```

    **Note**
    In the emulator, set the sample rate to 44100 and use stereo audio
    with the AAC codec, or set the sample rate below 8000 and use mono
    audio with the AMR codec.

3. To receive a notification whenever the audio recorder state changes:

    1. Register an event handler for the `StateChanged` event of the 

       ```
       audioRecorder.StateChanged += OnStateChanged;
       ```

    2. Define the state changed event handler.

       The following example prints the previous and current audio recorder states:

       ```
       void OnStateChanged(object sender, RecorderStateChangedEventArgs e)
       {
           Tizen.Log.Info(LogTag, $"Previous state = {e.PreviousState }, Current State = {e.CurrentState}");
       }
       ```

4. To receive a notification when the audio recorder reaches its recording limit:

    1. Register an event handler for the `RecordingLimitReached` event of the `Tizen.Multimedia.Recorder` class:

       ```
       audioRecorder.RecordingLimitReached += OnRecordingLimitReached;
       ```

    2. Define the recording limit reached event handler.

       The following example prints the type of the reached recording limit:

       ```
       void OnRecordingLimitReached(object sender, RecordingLimitReachedEventArgs e)
       {
           Tizen.Log.Info(LogTag, $"Limit type = {e.Type}");
       }
       ```


Recording Audio <a id="record_audio"></a>
---------------

To record audio:

1.  Prepare the audio recorder by calling the `Prepare()` method of the
    [Tizen.Multimedia.Recorder](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1Multimedia_1_1Recorder.html)
    class:

    ``` {.prettyprint}
    audioRecorder.Prepare();
    ```

    The audio recorder state changes to `Ready`.

2. Start recording audio by using the `Start()` method. Based on the
    file format you have set for the recorder, define an applicable file
    name and pass the full path with the file name as a parameter to
    the method.

    ``` {.prettyprint}
    audioRecorder.Start(savePath);
    ```

    If the target file path and name have been set to an existing file,
    the existing file is replaced with a new file.

    The audio recorder state changes to `Recording`.

3. To pause and resume recording:

    1. Pause the recording using the `Pause()` method:

       ```
       audioRecorder.Pause();
       ```

       The audio recorder state changes to `Paused`.

    2. Resume the recording using the `Resume()` method:

       ```
       audioRecorder.Resume();
       ```

       The audio recorder state changes to `Recording`.

4. To stop recording:

    1. To stop the recording and save the recorded data, use the `Commit()` method:

       ```
       audioRecorder.Commit();
       ```

    2. To stop the recording and discard the recorded data, use the `Cancel()` method:

       ```
       audioRecorder.Cancel();
       ```

    The audio recorder state changes to `Ready`.

5. After you have finished recording, reset the audio recorder using the `Unprepare()` method and deregister all recorder event handlers:

    ```
    /// Reset the recorder
    audioRecorder.Unprepare();
    /// Deregister event handlers
    audioRecorder -= OnStateChanged;
    audioRecorder -= OnRecordingLimitReached;
    ```

    The audio recorder state changes to `Idle`.


Preparing the Video Recorder <a id="prepare_video"></a>
----------------------------

To initialize the video recorder for use:

1.  Create an instance of the
    [Tizen.Xamarin.Forms.Extension.MediaView](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1Xamarin_1_1Forms_1_1Extension_1_1MediaView.html)
    class, which provides a view of the camera on the screen.

    Create an instance of the
    [Tizen.Multimedia.Camera](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1Multimedia_1_1Camera.html)
    class and set the display of the camera to the `NativeView` property
    of the `Tizen.Xamarin.Forms.Extension.MediaView` instance:

    ``` {.prettyprint}
    /// Create a MediaView object and set the display of camera
    var formMediaView = new Tizen.Xamarin.Forms.Extension.MediaView();
    var camera = new Camera(CameraDevice.Rear);
    camera.Display = new Display((Tizen.Multimedia.MediaView)formMediaView.NativeView);
    ```

2. Check which video codecs and file formats the device supports:

    -   To check which video codecs the device supports, use the
        `GetSupportedVideoCodecs()` method of the
        [Tizen.Multimedia.Recorder](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1Multimedia_1_1Recorder.html) class.
        The possible video codec values are defined in the
        [Tizen.Multimedia.RecorderVideoCodec](https://developer.tizen.org/dev-guide/csapi/namespaceTizen_1_1Multimedia.html#a4bbdecfe3b3d1a15d13c6095960dd596) enumeration.
    -   To check which file formats the device supports, use the
        `GetSupportedFileFormats()` method of the
        `Tizen.Multimedia.Recorder` class. The possible file format
        values are defined in the
        [Tizen.Multimedia.RecorderFileFormat](https://developer.tizen.org/dev-guide/csapi/namespaceTizen_1_1Multimedia.html#a1c2f595cf0e4c146e6b8b9ae31e4cc2a) enumeration.

    ``` {.prettyprint}
    var videoCodec = VideoRecorder.GetSupportedVideoCodecs().FirstOrDefault();
    var fileFormat = VideoRecorder.GetSupportedFileFormats().FirstOrDefault();
    ```

3. Create an instance of the
    [Tizen.Multimedia.VideoRecorder](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1Multimedia_1_1VideoRecorder.html)
    class by passing the `Tizen.Multimedia.Camera` instance, and the
    video codec and file format of the recording to the
    class constructor.

    Make sure the file format matches the video codec.

    ``` {.prettyprint}
    var videoRecorder = new VideoRecorder(camera, videoCodec, fileFormat);
    ```

    The recorder state is set to `Idle`.

4. Set various video recorder settings, such as the file size limit,
    video/audio encoder bitrate, video motion rate, audio sample rate,
    and resolution:

    ``` {.prettyprint}
    /// Set the maximum file size to 1024 (kB)
    videoRecorder.SizeLimit = 1024;

    /// Set the video motion rate
    videoRecorder.VideoMotionRate = 1;

    /// Set the video bitrate
    videoRecorder.VideoBitRate = 288000;

    /// Set the audio encoder bitrate
    videoRecorder.AudioBitRate = 128000;

    /// Set the audio sample rate
    videoRecorder.AudioSampleRate = 44100;
    ```

5. To receive a notification when the video recorder reaches its recording limit:

    1. Register an event handler for the `RecordingLimitReached` event of the `Tizen.Multimedia.Recorder` class:

        ```
        videoRecorder.RecordingLimitReached += OnRecordingLimitReached;
        ```

    2. Define the recording limit reached event handler.The following example prints the type of the reached recording limit:

        ```
        void OnRecordingLimitReached(object sender, RecordingLimitReachedEventArgs e)
        {
            Tizen.Log.Info(LogTag, $"Limit type = {e.Type}");
        }
        ```

    You can add event handlers similarly to other video recorder events, such as the `StateChanged` and `RecordingStatusChanged` events of the `Tizen.Multimedia.Recorder` class.



Recording Video <a id="record_video"></a>
---------------

To record video:

1.  Prepare the video recorder by calling the `Prepare()` method of the
    [Tizen.Multimedia.Recorder](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1Multimedia_1_1Recorder.html)
    class:

    ``` {.prettyprint}
    videoRecorder.Prepare();
    ```

    The video recorder state changes to `Ready`.

2. Start recording video by using the `Start()` method. Based on the
    file format you have set for the recorder, define an applicable file
    name and pass the full path with the file name as a parameter to
    the method.

    ``` {.prettyprint}
    videoRecorder.Start(SavePath);
    ```

    If the target file path and name have been set to an existing file,
    the existing file is replaced with a new file.

    The video recorder state changes to `Recording`.

3. To pause and resume recording:

    1. Pause the recording using the `Pause()` method:

       ```
       videoRecorder.Pause();
       ```

       The video recorder state changes to `Paused`.

    2. Resume the recording using the `Resume` method:

       ```
       videoRecorder.Resume();
       ```

       The video recorder state changes to `Recording`.

4. To stop recording:

    1. To stop the recording and save the recorded data, use the `Commit()` method:

       ```
       videoRecorder.Commit();
       ```

    2. To stop the recording and discard the recorded data, use the `Cancel()` method:

       ```
       videoRecorder.Cancel();
       ```

    The video recorder state changes to `Ready`.

5. After you have finished recording, reset the video recorder using `Unprepare()` method and deregister all recorder event handlers:

    ```
    /// Reset the recorder
    videoRecorder.Unprepare();
    /// Deregister event handler
    videoRecorder.RecordingLimitReached -= OnRecordingLimitReached;
    ```

    The video recorder state changes to `Idle`.
