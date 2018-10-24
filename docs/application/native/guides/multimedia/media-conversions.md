# Media Conversions


You can perform various media conversions through codecs. You can encode and decode video and audio data, and, in mobile applications, you can also use video transcoding features, such as multi-format codec and output format.

The main features of the Media Codec and Video Util API include:

- Media codecs

  You can prepare the [media codecs](#codecs), fill the media packet with data, and run the media codec.

- Video transcoding **in mobile applications only**

  You can prepare the video utilities, manage and monitor [video transcoding](#video), and set parameters.

<a name="codecs"></a>
## Media Codecs

You can encode and decode audio and video data with codecs.

To use codecs:

1. [Create a handle for the codec instance](#prepare) with the `mediacodec_create()` function. After a successful handle creation, your system can use the codec.

2. Set the codec configuration with the `mediacodec_set_codec()`, and `mediacodec_set_vdec_info()` or `mediacodec_set_venc_info()` functions.

   You can also prepare for the available ready state with the `mediacodec_prepare()` function.

3. Decode and encode with the `mediacodec_process_input()` and `mediacodec_get_output()` functions.

A single `MediaCodec` instance handles 1 specific type of data (such as aac audio or H.264 video), and can encode or decode. The codec operates on "raw" data, so strip off any file headers (such as ID3 tags).

The following figures illustrate the general media state changes.

**Figure: Media state changes**

![Media state changes](./media/codec_state.png)

After you have initialized the codecs, you can:

1. [Fill the media packet with data](#packet).
2. [Run the media codec](#management).

<a name="video"></a>
## Video Transcoding in Mobile Applications

Tizen offers the following video transcoding features:

- Make container and codec type changes

  Content compatibility is supported between same devices.

- Make scale and frame rate changes

  Since video file size and format changes are possible, there is attachment flexibility for email, MMS, and SMS messaging. You can also extract a thumbnail from certain video chapters, and chapter previews are available.

- Trim

  A trim chapter is available in the video editor.

With the Video Util API you can:

- [Set up the video utilities](#prepare)
- [Manage and monitor](#manage) the transcoding process
- [Set parameters](#set) for the video utilities
- [Retrieve information](#get) about the transcoding process

The following figure shows the result of the video file size change (due to scaling and container and codec format change).

**Figure: Transcoder**

![Transcoder](./media/transcoder.png)

The following table lists the supported audio and video codecs (decoder).

**Table: Decoders**

| Audio codec   | Video codec   |
|---------------|---------------|
| AAC LC        | MPEG-1        |
| AAC+          | MPEG-4 part 2 |
| Enhanced AAC+ | H.263         |
| MP3           | H.264         |
| WMA7 / 8      | VC-1 (WMV9)   |
| WAV           | On2 VP3       |
| Vorbis        | Theora        |
| AMR-NB        |               |
| AMR-WB        |               |

The following table lists the supported audio and video codecs (encoder).

**Table: Encoders**

| Audio codec | Video codec   |
|-------------|---------------|
| AAC LC      | MPEG-1        |
| Vorbis      | MPEG-4 part 2 |
| AMR-NB      | H.263         |
|             | H.264         |
|             | VC-1 (WMV9)   |
|             | On2 VP3       |
|             | Theora        |

## Prerequisites

To enable your application to use the media conversion functionalities:

1. To use the functions and data types of the Media Codec API (in [mobile](../../api/mobile/latest/group__CAPI__MEDIA__CODEC__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__MEDIA__CODEC__MODULE.html) applications), include the `<media_codec.h>` header file in your application:

   ```
   #include <media_codec.h>
   ```

2. To use the functions and data types of the [Video Util](../../api/mobile/latest/group__CAPI__MEDIA__VIDEO__UTIL__MODULE.html) API, include the `<video_util.h>` header file in your application:

   ```
   #include <video_util.h>
   ```
<a name="prepare"></a>
## Preparing Media Codecs

To prepare the media codecs:

1. Create a handle for the media codec using the `mediacodec_create()` function:

   ```
   mediacodec_h *mediacodec;
   ret = mediacodec_create(&mediacodec);
   ```

   The handle must be passed to all other Media Codec APIs.

2. Set the codec using the `mediacodec_set_codec()` function:

   ```
   ret = mediacodec_set_codec(mediacodec, (mediacodec_codec_type_e)codecid, flag);
   ```

   The `mediacodec_codec_type_e` (in [mobile](../../api/mobile/latest/group__CAPI__MEDIA__CODEC__MODULE.html#ga2e7775fb3609e4349c742b1d9eb5febc) and [wearable](../../api/wearable/latest/group__CAPI__MEDIA__CODEC__MODULE.html#ga2e7775fb3609e4349c742b1d9eb5febc) applications) and `mediacodec_support_type_e` (in [mobile](../../api/mobile/latest/group__CAPI__MEDIA__CODEC__MODULE.html#gab01ad3dbb4989537108a5c9f2062447a) and [wearable](../../api/wearable/latest/group__CAPI__MEDIA__CODEC__MODULE.html#gab01ad3dbb4989537108a5c9f2062447a) applications) enumerations define the media codec type and support type (second and third parameters).

3. To configure the video and audio encoder and decoder:

   ```
   /* Video encoder */
   ret = mediacodec_set_venc_info(mediacodec, width, height, fps, target_bits);
   /* Video decoder */
   ret = mediacodec_set_vdec_info(mediacodec, width, height);
   /* Audio encoder */
   ret = mediacodec_set_aenc_info(mediacodec, samplerate, channel, bit, bitrate);
   /* Audio decoder */
   ret = mediacodec_set_adec_info(mediacodec, samplerate, channel, bit);
   ```

4. To set callbacks for the input and output buffers:

   1. To receive notifications when the input buffers are used, register a callback using the `mediacodec_set_input_buffer_used_cb()` function. The callback is invoked when the input buffers are queued to the codec.

      ```
      ret = mediacodec_set_input_buffer_used_cb(mediacodec, _input_buffer_used_cb, NULL);
      ```

      If a `media_packet` is used, it must be destroyed when the callback is invoked:

      ```
      static void
      _input_buffer_used_cb(media_packet_h pkt, void *user_data)
      {
          media_packet_destroy(pkt);

          return;
      }
      ```

   2. To receive notifications when the output buffers are dequeued, register a callback using the `mediacodec_set_output_buffer_available_cb()` function. The callback is invoked when the output buffers are dequeued.

      ```
      ret = mediacodec_set_output_buffer_available_cb(mediacodec, _output_buffer_available_cb, mediacodec);
      ```

      If the `media_packet` is dequeued from the codec, this callback is invoked.

      Retrieve the output packet using the `mediacodec_get_output()` function inside the callback:

      ```
      static void
      _output_buffer_available_cb(media_packet_h pkt, void *user_data)
      {
          media_packet_h out_pkt;
          mediacodec_h mediacodec = (mediacodec_h)user_data;

          if (pkt != NULL) {
              mediacodec_get_output(mediacodec, &out_pkt, 0);
              media_packet_destroy(out_pkt);
          }

          return;
      }
      ```
<a name="packet"></a>
## Filling the Media Packet with Data

After the `media_packet` is allocated with corresponding codec MIME types, fill it with data:

1. Retrieve the data pointer from the `media_packet`, and set the buffer size on the preallocated packet:

   ```
   unsigned char nal[48] = {0x00, 0x00, 0x00, 0x01, 0x67, 0x4D, 0x40, 0x33,
                            0x9A, 0x73, 0x80, 0xA0, 0x08, 0xB4, 0x20, 0x00,
                            0x32, 0xE9, 0xE0, 0x09, 0x89, 0x68, 0x11, 0xE3,
                            0x06, 0x23, 0xC0, 0x00, 0x00, 0x00, 0x01, 0x68,
                            0xEE, 0x3C, 0x80, 0x00, 0x00, 0x00, 0x01, 0x65,
                            0x88, 0x80, 0x01, 0x48, 0x00, 0x06, 0x57, 0xFD};

   media_format_h fmt;
   media_packet_h pkt;
   void *data;

   ret = media_format_set_video_mime(fmt, MEDIA_FORMAT_H264_SP);
   ret = media_format_set_video_width(fmt, 1280);
   ret = media_format_set_video_height(fmt, 544);
   ret = media_packet_create_alloc(fmt, NULL, NULL, &pkt);

   ret = media_packet_get_buffer_data_ptr(pkt, &data);
   memcpy(data, nal, 48);
   ret = media_packet_set_buffer_size(pkt, 48);
   ```

2. If the memory buffer contains extra padding bytes after each pixel row, check whether the stride in the uncompressed video frame is the same as the video width. If it is not, make a strided copy:

   ```
   void
   _fill_buffer(media_packet_h pkt, unsigned char *yuv, int width, int height)
   {
       int i;

       /* Y plane */
       media_packet_get_video_stride_width(pkt, 0, &stride);
       media_packet_get_video_plane_data_ptr(pkt, 0, &data);

       for (i = 0; i < height; i++) {
           memcpy(data, yuv, width);
           data += stride;
       }
   }
   ```
<a name="management"></a>
## Running the Media Codec

After [preparing the medic codec](#prepare) and [filling the `media_packet` with data](#packet), run the media codec in the following loop:

1. When an input buffer is ready, read a chunk of input and copy it into the buffer to be encoded or decoded.

2. When an output buffer is ready, copy the encoded or decoded output from the buffer.

To run the media codec loop:

1. Prepare the media codec using the `mediacodec_prepare()` function:

   ```
   ret = mediacodec_prepare(mediacodec);
   ```

2. Set the `media_packet` flags using the `media_packet_set_flags()` function:

   - If the `media_packet` contains codec data, such as SPS or PPS for H.264, set the codec config flag:

     ```
     ret = media_packet_set_flags(pkt, MEDIA_PACKET_CODEC_CONFIG);
     ```

   - If the `media_packet` contains the end of the stream, set the end-of-stream (eos) flag:

     ```
     ret = media_packet_set_flags(pkt, MEDIA_PACKET_END_OF_STREAM);
     ```

     The eos callback is invoked if the eos packet is decoded or encoded and the eos callback is registered with the `mediacodec_set_eos_cb()` function.

   > **Note**
   >
   > You must set the flags before calling the `mediacodec_process_input()` function.

3. Start the media codec loop using the `mediacodec_process_input()` and `mediacodec_get_output()` functions:

   ```
   media_packet_h in_buf = NULL;
   ret = mediacodec_process_input(mediacodec, in_buf, 0);

   media_packet_h output_buf = NULL;
   ret = mediacodec_get_output(mediacodec, &output_buf, 0);
   ```

4. After calling the `mediacodec_get_output()` function, check the frame using the `media_packet`.

   To check whether the `media_packet` contains key frame or codec data:

   ```
   bool keyframe;
   bool codec_config;

   ret = media_packet_is_sync_frame(pkt, &keyframe);
   ret = media_packet_is_codec_config(pkt, &codec_config);
   ```

5. After the loop is over and you have finished working with the media codec, reset the codec and destroy the codec handle using the `mediacodec_unprepare()` and `mediacodec_destroy()` functions:

   ```
   ret = mediacodec_unprepare(mediacodec);

   ret = mediacodec_destroy(mediacodec);
   ```

   The media codec state changes to `MEDIACODEC_STATE_NONE`.

## Preparing the Video Utilities in Mobile Applications

To initialize the video utilities for use:

1. Create a video util handle for managing the transcoding:

   ```
   video_util_h video_h = NULL;
   ret = video_util_create(&video_h);
   ```

2. If the video util handle is successfully created, set the input file path using the `video_util_set_file_path()` function:

   ```
   ret = video_util_set_file_path(video_h, *path);
   ```

3. Set the file format using the `video_util_set_file_format()` function:

   ```
   ret = video_util_set_file_format(video_h, VIDEO_UTIL_FILE_FORMAT_3GP);
   ```

   The [video_util_file_format_e](../../api/mobile/latest/group__CAPI__MEDIA__VIDEO__UTIL__MODULE.html#gad9c070cbb59f3107cefd280ec06e2966) enumeration defines the available file formats.

4. Set the audio codec using the `video_util_set_audio_codec()` function:

   ```
   ret = video_util_set_audio_codec(video_h, VIDEO_UTIL_AUDIO_CODEC_AAC);
   ```

   The [video_util_audio_codec_e](../../api/mobile/latest/group__CAPI__MEDIA__VIDEO__UTIL__MODULE.html#ga48da7f77144a99f5733a90d62805c435) enumeration defines the available audio codecs.

5. Set the video codec using the `video_util_set_video_codec()` function:

   ```
   ret = video_util_set_video_codec(video_h, VIDEO_UTIL_VIDEO_CODEC_MPEG4);
   ```

   The [video_util_video_codec_e](../../api/mobile/latest/group__CAPI__MEDIA__VIDEO__UTIL__MODULE.html#gabadbb5a64155f42fe180bedac40f289e) enumeration defines the available video codecs.

6. Enable or disable the accurate seek mode using the `video_util_set_accurate_mode()` function.

   If you enable this mode, you can get an accurate frame for a given duration in the `video_util_start_transcoding()` function.

   ```
   ret = video_util_set_accurate_mode(video_h, 0);
   ```

7. Set the video resolution using the `video_util_set_resolution()` function:

   ```
   ret = video_util_set_resolution(video_h, 176, 144);
   ```

   If the transcoding is performed with the original input ("trim"), both the width and height are 0.

8. Set the video frame rate using the `video_util_set_fps()` function:

   ```
   ret = video_util_set_fps(video_h, 10);
   ```

9. When no longer needed, destroy the video util handle using the `video_util_destroy()` function:

   ```
   ret = video_util_destroy(video_h);
   ```
<a name="manage"></a>
## Managing Transcoding in Mobile Applications

To manage and monitor the transcoding process:

1. Start the transcoding using the `video_util_start_transcoding()` function:

   ```
   ret = video_util_start_transcoding(video_h);
   ```

2. Monitor and manage the transcoding:

   - To retrieve the current transcoding progress, use the `video_util_get_progress_transcoding()` function. The function returns the current transcoding position (second parameter) and the duration of the transcoding (third parameter).

     ```
     unsigned long current_position;
     unsigned long duration;
     ret = video_util_get_progress_transcoding(video_h, *current_position, *duration);
     ```

   - To cancel the transcoding process, use the `video_util_cancel_transcoding()` function. You must call this function before the transcoding complete callback is invoked.

     ```
     ret = video_util_cancel_transcoding(video_h);
     ```

3. After the transcoding complete callback is invoked, destroy the video util handle using the `video_util_destroy()` function:

   ```
   ret = video_util_destroy(video_h);
   ```

   The function destroys the handle of a completed transcoding. If the function is called during the transcoding process, the function also cancels the transcoding.

   > **Note**
   >
   > If you do not call the destroy function after the transcoding is complete, you cannot start a new transcoding process, and a memory crash can occur.

<a name="set"></a>
## Setting Parameters in Mobile Applications

To set parameters for the video utilities (for other parameters, see [Preparing the Video Utilities](#prepare)):

1. Set the file format:

   1. Check the supported file formats:

      1. Check the supported file formats using the `video_util_foreach_supported_file_format()` function:

         ```
         error_code = video_util_foreach_supported_file_format(handle, video_util_file_supported, NULL);
         ```

         The second parameter specifies the callback that is invoked separately for each supported file format.

      2. Define the callback:

         ```
         static bool
         video_util_file_supported(video_util_file_format_e format, void *user_data)
         {
             dlog_print(DLOG_INFO, LOG_TAG, "format %s\n",
                        format == VIDEO_UTIL_FILE_FORMAT_3GP? "VIDEO_UTIL_FILE_FORMAT_3GP":
                        format == VIDEO_UTIL_FILE_FORMAT_MP4? "VIDEO_UTIL_FILE_FORMAT_MP4":
                        "VIDEO_UTIL_FILE_FORMAT_MAX");

             return 0;
         }
         ```

         The [video_util_file_format_e](../../api/mobile/latest/group__CAPI__MEDIA__VIDEO__UTIL__MODULE.html#gad9c070cbb59f3107cefd280ec06e2966) enumeration defines the available file formats.

   2. Set the file format using the `video_util_set_file_format()` function:

      ```
      ret = video_util_set_file_format(video_h, VIDEO_UTIL_FILE_FORMAT_3GP);
      ```

2. Set the audio and video codec:

   1. Check the supported audio and video codecs:

      1. Check the supported audio and video codecs using the `video_util_foreach_supported_audio_codec()` and `video_util_foreach_supported_video_codec()` functions:

         ```
         video_util_foreach_supported_audio_codec(handle, video_util_audio_supported, NULL);

         video_util_foreach_supported_video_codec(handle, video_util_video_supported, NULL);
         ```

         The second parameter of both functions specifies the callback that is invoked separately for each supported codec.

      2. Define the callbacks:

         ```
         static bool
         video_util_audio_supported(video_util_audio_codec_e codec, void *user_data)
         {
             dlog_print(DLOG_INFO, LOG_TAG, "audio codec %s\n",
                        codec==VIDEO_UTIL_AUDIO_CODEC_AAC? "VIDEO_UTIL_AUDIO_CODEC_AAC":
                        codec==VIDEO_UTIL_AUDIO_CODEC_AMRNB? "VIDEO_UTIL_AUDIO_CODEC_AMRNB":
                        "VIDEO_UTIL_AUDIO_CODEC_NONE");

             return 0;
         }

         static bool
         video_util_video_supported(video_util_video_codec_e codec, void *user_data)
         {
             dlog_print(DLOG_INFO, LOG_TAG, "video codec %s\n",
                        codec == VIDEO_UTIL_VIDEO_CODEC_MPEG4? "VIDEO_UTIL_VIDEO_CODEC_MPEG4":
                        codec == VIDEO_UTIL_VIDEO_CODEC_H263? "VIDEO_UTIL_VIDEO_CODEC_H263":
                        codec == VIDEO_UTIL_VIDEO_CODEC_H264? "VIDEO_UTIL_VIDEO_CODEC_H264":
                        "VIDEO_UTIL_VIDEO_CODEC_NONE");

             return 0;
         }
         ```

         The [video_util_audio_codec_e](../../api/mobile/latest/group__CAPI__MEDIA__VIDEO__UTIL__MODULE.html#ga48da7f77144a99f5733a90d62805c435) and [video_util_video_codec_e](../../api/mobile/latest/group__CAPI__MEDIA__VIDEO__UTIL__MODULE.html#gabadbb5a64155f42fe180bedac40f289e) enumerations define the available audio and video codecs.

      To check the support for a specified codec, such as `VIDEO_UTIL_VIDEO_CODEC_MPEG4`:

      ```
      static bool
      video_util_video_supported(video_util_video_codec_e codec, void *user_data)
      {
          if (codec == VIDEO_UTIL_VIDEO_CODEC_MPEG4)
              user_data = true;

          return 0;
      }

      bool supported = false;
      video_util_foreach_supported_video_codec(handle, video_util_video_supported, &supported);
      dlog_print(DLOG_INFO, LOG_TAG, "MPEG4 codec %s", supported ? "supported" : "not supported");
      ```

   2. Set the audio and video codecs using the `video_util_set_audio_codec()` and `video_util_set_video_codec()` functions:

      ```
      error_code = video_util_set_audio_codec(handle, VIDEO_UTIL_AUDIO_CODEC_AAC);

      error_code = video_util_set_video_codec(handle, VIDEO_UTIL_VIDEO_CODEC_MPEG4);
      ```

3. Set the video resolution using the `video_util_set_resolution()` function:

   ```
   int error_code = video_util_set_resolution(handle, 640, 480);
   ```

4. Set the video frame rate using the `video_util_set_fps()` function:

   ```
   int error_code = video_util_set_fps(handle, 25);
   ```
<a name="get"></a>
## Monitoring the Transcoding Progress in Mobile Applications

To retrieve progress information about the transcoding process:

1. [Prepare the video utilities.](#prepare)

2. Start the transcoding using the `video_util_start_transcoding()` function:

   ```
   error_code = video_util_start_transcoding(handle, start, duration, *out_path, progress_cb, completed_cb, *user_data);
   ```

   The fifth parameter specifies the transcoding progress callback, which is invoked periodically during the transcoding process. The sixth parameter specifies the transcoding complete callback, which is invoked after the transcoding process is complete.

3. Retrieve the current transcoding progress using the `video_util_get_progress_transcoding()` function within the transcoding progress callback:

   ```
   error_code = video_util_get_progress_transcoding(handle, *current_position, *duration);
   ```

## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
