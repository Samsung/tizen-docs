# Media Stream Recording


Tizen provides basic stream recorder features, including audio and video recording from a live buffer. With the stream recorder, live audio and video can be kept in your target.

The main features of the StreamRecorder API include:

- Creating a media packet

  You must [create a media packet](#packet) for the stream recording using raw data from the source. The media packet must be created for each buffer captured from source and passed to the `streamrecorder_push_stream_buffer()` function.

- Recording audio and video, and controlling the recording

  You can [record a stream, and stop, pause, and cancel the recording](#record_stream), and push the buffer.

- Encoding files

  You can [encode files](#encode) with various formats and codecs:

  - Supported file formats:

    - Video: `mp4` and `3gp`
    - Audio: `amr` and `aac`

    The supported file formats are defined in the `streamrecorder_file_format_e` enumeration (in [mobile](../../api/mobile/latest/group__CAPI__MEDIA__STREAMRECORDER__MODULE.html#gadb3d70e90207c780e1473785a712d90d) and [wearable](../../api/wearable/latest/group__CAPI__MEDIA__STREAMRECORDER__MODULE.html#gadb3d70e90207c780e1473785a712d90d) applications).

  - Video codec for encoding a video stream

    To set the video codec for encoding a video stream, use the `streamrecorder_set_video_encoder()` function.

    The available video codecs are defined in the `streamrecorder_video_codec_e` enumeration (in [mobile](../../api/mobile/latest/group__CAPI__MEDIA__STREAMRECORDER__MODULE.html#gae2912d9eceeac43640efa52f96556473) and [wearable](../../.api/wearable/latest/group__CAPI__MEDIA__STREAMRECORDER__MODULE.html#gae2912d9eceeac43640efa52f96556473) applications).

  - Audio codec for encoding an audio stream

    To set the audio codec for encoding an audio stream, use the `streamrecorder_set_audio_encoder()` function.

    The available audio codecs are defined in the `streamrecorder_audio_codec_e` enumeration (in [mobile](../../api/mobile/latest/group__CAPI__MEDIA__STREAMRECORDER__MODULE.html#ga46f244622314395be47eddb8d84fabd2) and [wearable](../../api/wearable/latest/group__CAPI__MEDIA__STREAMRECORDER__MODULE.html#ga46f244622314395be47eddb8d84fabd2) applications).

- Managing recording details

  You can manage various recording details, such as get and set the filename for the video and audio recording.

  You can manage the following attributes:

  - Audio codec for encoding the audio stream
  - Video codec for encoding the video stream
  - File format
  - File path to record
  - Time and file size limit of the recording file
  - Sampling rate of the audio stream
  - Bitrate of the audio or video encoder
  - Number of audio channels

Valid input sources consist of external sources, such as a live buffer passed by the application. Most operations of the stream recorder functions work in a synchronous mode, but some operations can work in an asynchronous mode, which means that callbacks are required to pass an event notification to the application.

The following figure illustrates the general stream recorder state changes. Use the stream recorder functions according to pre and post conditions, by following the state changes.

**Figure: Stream recorder state changes**

![Stream recorder state changes](./media/streamrecorder_states.png)

The stream recorder functions serve as the interface with the software. Input is processed through a handle.

## Prerequisites

To enable your application to use the stream recorder functionality:

1. To use the functions and data types of the StreamRecorder API (in [mobile](../../api/mobile/latest/group__CAPI__MEDIA__STREAMRECORDER__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__MEDIA__STREAMRECORDER__MODULE.html) applications), include the `<streamrecorder.h>` header file in your application:

   ```
   #include <streamrecorder.h>
   ```

2. Define a structure containing the stream recorder handle and media packet. You can also declare variables to keep the recording time, video file paths, bitrate, recording limits, flag, and return values.

   ```
   struct streamrecorder_data {
       streamrecorder_h streamrecorder;
       media_packet_h media_packet;
   };
   typedef struct streamrecorder_data streamrecdata;

   static streamrecdata streamrec_data;

   int error_code = 0;
   streamrec_data.streamrecorder = NULL;
   ```

3. Create the stream recorder handle using the `streamrecorder_create()` function. On success, the StreamRecorder state becomes `STREAMRECORDER_STATE_CREATED`.

   ```
   /* Create the streamrecorder handle */
   error_code = streamrecorder_create(&streamrec_data.streamrecorder);
   assert_eq(error_code, STREAMRECORDER_ERROR_NONE);
   ```

   You can get the stream recorder state using the `streamrecorder_get_state()` function after the handle is created.

4. To enable video recording using a live buffer as a source, you have to call the `streamrecorder_enable_source_buffer()` function. Additionally, you can enable other types of sources with the `streamrecorder_source_e` enumeration (in [mobile](../../api/mobile/latest/group__CAPI__MEDIA__STREAMRECORDER__MODULE.html#ga1d4c1835d2b7357850bdf706dd58b97e) and [wearable](../../api/wearable/latest/group__CAPI__MEDIA__STREAMRECORDER__MODULE.html#ga1d4c1835d2b7357850bdf706dd58b97e) applications).

    ```
    /* Set the video source as live buffer to be used for recording */
    error_code = streamrecorder_enable_source_buffer(&streamrec_data.streamrecorder,
                                                     STREAMRECORDER_SOURCE_VIDEO);
    assert_eq(error_code, STREAMRECORDER_ERROR_NONE);
    ```

5. To subscribe to notifications, use the `streamrecorder_set_notify_cb()` function to register a callback function. The parameters are a valid stream recorder handle, a callback function, and data passed to the callback.

    ```
    /* Set the streamrecorder notify callback */
    error_code = streamrecorder_set_notify_cb(streamrec_data.streamrecorder, streamrecorder_notify_cb,
                                              streamrec_data);
    assert_eq(error_code, STREAMRECORDER_ERROR_NONE);
    ```

	The callback function receives 4 parameters, which are the previous and current state of the stream recorder, the notification type, and user data.

    ```
    /*
       Stream recorder callback is invoked when
       the streamrecorder gets notifications
    */
    static void
    streamrecorder_set_notify_cb(streamrecorder_state_e previous, streamrecorder_state_e current,
                                 streamrecorder_notify_e notification, void *data)
    {
        fprintf(stderr, "streamrecorder_notify (prev: %d, curr: %d)\n", previous, current);
    }
    ```

<a name="encode"></a>
## Managing Encoding

To get and set information about video and audio encoding:

1. To get a list of video codecs your device supports, call the `streamrecorder_foreach_supported_video_encoder()` function. One of its parameters is a callback, which is called for each codec supported for the given stream recorder.

    In the following example, the codec of the stream recorder is set to the first found supported codec.

    ```
    streamrecorder_video_codec_supported_codec;
    static bool
    _video_encoder_cb(streamrecorder_video_codec_e codec, void *user_data)
    {
        streamrecorder_video_codec_e * supported_codec = (streamrecorder_video_codec_e*)user_data;
        supported_codec = codec;

        return false;
    }

    error_code = streamrecorder_foreach_supported_video_encoder(streamrec_data.streamrecorder,
                                                                _video_encoder_cb,&supported_codec);
    if (STREAMRECORDER_ERROR_NONE != error_code) {
        /* Error handling */
        assert_eq(error_code, STREAMRECORDER_ERROR_NONE);
    }

    /* Set the stream recorder video encoder */
    error_code = streamrecorder_set_video_encoder(streamrec_data.streamrecorder,supported_codec);
    if (STREAMRECORDER_ERROR_NONE != error_code) {
        /* Error handling */
        assert_eq(error_code, STREAMRECORDER_ERROR_NONE);
    }
    ```

2. You can set the bitrate of the video encoder with the `streamrecorder_set_video_encoder_bitrate()` function. Even if the bitrate was set, it can depend on the stream buffer which you push.

    You can also set the file format for the recording media stream by invoking the `streamrecorder_set_file_format()` function. Before setting the file format, check the file formats your device supports using the `streamrecorder_foreach_supported_file_format()` function.

    Finally, you need to set the file path to store the recorded data by invoking the `streamrecorder_set_filename()` function.

    ```
    staticintg_bitrate = 288000;
    static char *g_file = "/opt/media/Downloads/myvideo.mp4";

    /* Set bitrate of video encoder */
    error_code = streamrecorder_set_video_encoder_bitrate(streamrec_data.streamrecorder, g_bitrate);
    if (STREAMRECORDER_ERROR_NONE != error_code) {
        /* Error handling */
        assert_eq(error_code, STREAMRECORDER_ERROR_NONE);
    }

    /* Set recording file format */
    error_code = streamrecorder_set_file_format(streamrec_data.streamrecorder, STREAMRECORDER_FILE_FORMAT_MP4);
    if (STREAMRECORDER_ERROR_NONE != error_code) {
        /* Error handling */
        assert_eq(error_code, STREAMRECORDER_ERROR_NONE);
    }

    /* Set file path to store the recorded data */
    error_code = streamrecorder_set_filename(streamrec_data.streamrecorder, g_file);
    if (STREAMRECORDER_ERROR_NONE != error_code) {
        /* Error handling */
        assert_eq(error_code, STREAMRECORDER_ERROR_NONE);
    }
    ```

<a name="packet"></a>
## Creating a Media Packet

When the stream recorder is configured, create the media packet using the raw data from the source with the Media Tool API functions (in [mobile](../../api/wearable/latest/group__CAPI__MEDIA__TOOL__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__MEDIA__TOOL__MODULE.html) applications).

```
/* Create media packet to be passed to the push stream buffer API */
media_format_h fmt;
void *data;
void *rawbuffer; /* Data to be passed for recording */
int size; /* Size of each frame buffer */

error_code = media_format_set_video_mime(fmt, MEDIA_FORMAT_MPEG4_SP);
error_code = media_format_set_video_width(fmt, 640);
error_code = media_format_set_video_height(fmt, 480);
error_code = media_packet_create_alloc(fmt, NULL, NULL, &streamrecdata.streamrecorder);

error_code = media_packet_get_buffer_data_ptr(streamrecdata.streamrecorder, &data);
memcpy(data, rawbuffer, size);
error_code = media_packet_set_buffer_size(streamrecdata.streamrecorder, size);
```

The media packet must be created for each buffer captured from the source and passed to the `streamrecorder_push_stream_buffer()` function when the stream recorder is prepared to record.

<a name="record_stream"></a>
## Recording a Stream

To record a stream:

1. Call the `streamrecorder_prepare()` function with a valid stream recorder handle to change the stream recorder state to `STREAMRECORDER_STATE_PREPARED`. This is one of the states in which you are able to start recording by calling the `streamrecorder_start()` function.

    ```
    /* Prepare the streamrecorder, changing the state to STREAMRECORDER_STATE_PREPARED */
    error_code = streamrecorder_prepare(streamrec_data.streamrecorder);
    if (STREAMRECORDER_ERROR_NONE != error_code) {
        /* Error handling */
        assert_eq(error_code, STREAMRECORDER_ERROR_NONE);
    }
    ```

2. Start recording by calling the `streamrecorder_start()` function with a valid stream recorder handle:

    ```
    /* Start the stream recorder */
    error_code = streamrecorder_start(streamrec_data.streamrecorder);
    if (STREAMRECORDER_ERROR_NONE != error_code) {
        /* Error handling */
        assert_eq(error_code, STREAMRECORDER_ERROR_NONE);
    }
    ```

    Once the recording starts, the file is removed automatically and replaced with a new one, if you set the file path to an existing file.

    Note that you can only call the `streamrecorder_start()` function in the prepared state (`STREAMRECORDER_STATE_PREPARED`) and paused state (`STREAMRECORDER_STATE_PAUSED`).

    Call the `streamrecorder_push_stream_buffer()` function, which pushes the media packet to record audio or video.

    ```
    /* Push the stream buffer to record audio or video */
    error_code = streamrecorder_push_stream_buffer(streamrec_data.streamrecorder, streamrec_data.media_packet);
    if (STREAMRECORDER_ERROR_NONE != error_code) {
        /* Error handling */
        assert_eq(error_code, STREAMRECORDER_ERROR_NONE);
    }
    ```

3. During the recording, you can pause or stop it:

   - To stop recording and save the result, use the `streamrecorder_commit()` function with the valid stream recorder handle. The results of the recording are saved to a previously configured file path. This function can be called if the recorder is in the `STREAMRECORDER_STATE_RECORDING` or `STREAMRECORDER_STATE_PAUSED` state.

     ```
     /* Stop recording and save recorded data to the previously configured path */
     error_code = streamrecorder_commit(streamrec_data.streamrecorder);
     if (STREAMRECORDER_ERROR_NONE != error_code) {
         /* Error handling */
         assert_eq(error_code, STREAMRECORDER_ERROR_NONE);
     }
     ```

     After committing, the stream recorder state is changed to the `STREAMRECORDER_STATE_PREPARED` state.

     If you do not want to save your recording, use the `streamrecorder_cancel()` function with the proper stream recorder handle. The only difference between this function and the `streamrecorder_commit()` function is that the recording data are not written in the file.

     ```
     /* Stop recording but don not save the recorded data */
     error_code = streamrecorder_cancel(streamrec_data.streamrecorder);
     if (STREAMRECORDER_ERROR_NONE != error_code) {
         /* Error handling */
         assert_eq(error_code, STREAMRECORDER_ERROR_NONE);
     }
     ```

   - To pause recording, use the `streamrecorder_pause()` function with the valid stream recorder handle. To start recording again later, use the `streamrecorder_start()` function.

     This function can be called if the stream recorder is in the `STREAMRECORDER_STATE_RECORDING` state.

     ```
     /* Pause the recording */
     error_code = streamrecorder_pause(streamrec_data.streamrecorder);
     if (STREAMRECORDER_ERROR_NONE != error_code) {
         /* Error handling */
         assert_eq(error_code, STREAMRECORDER_ERROR_NONE);
     }
     ```

     After pausing, the stream recorder state is changed to `STREAMRECORDER_STATE_PAUSED`.

     As a special case, you can stop pushing the stream buffers. In this case, the stream recorder state is `STREAMRECORDER_STATE_RECORDING`, because the stream recorder is waiting for buffers. It can make the same effect as a pause in recording.

4. When you have finished recording, use the `streamrecorder_unprepare()` function to reset the stream recorder. The required state for this function is `STREAMRECORDER_STATE_PREPARED`. After calling the function, the recorder state is `STREAMRECORDER_STATE_CREATED`, which allows you to free all stream recorder resources with the `streamrecorder_destroy()` function.

    ```
    /* Unprepare the stream recorder */
    error_code = streamrecorder_unprepare(streamrec_data->streamrecorder);
    if (STREAMRECORDER_ERROR_NONE != error_code) {
        /* Error handling */
        assert_eq(error_code, STREAMRECORDER_ERROR_NONE);
    }

    /* Destroy the recorder */
    error_code = streamrecorder_destroy(streamrec_data.streamrecorder);
    if (STREAMRECORDER_ERROR_NONE != error_code) {
        /* Error handling */
        assert_eq(error_code, STREAMRECORDER_ERROR_NONE);
    }
    ```

    After this, the stream recorder is changed to the `STREAMRECORDER_STATE_NONE` state.

## Related Information
- Dependencies
  - Tizen 3.0 and Higher for Mobile
  - Tizen 3.0 and Higher for Wearable
