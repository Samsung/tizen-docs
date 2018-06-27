# Media Muxing


You can mux encoded media into a multiplexed stream and parse multiplexed media streams.

With the Media Muxer and Media Demuxer API you can:

- Prepare and manage the media muxer

  You can initialize and configure the [media muxer](#muxer) for use, and create threads to use the media muxer.

- Prepare and manage the media demuxer

  You can initialize and configure the [media demuxer](#demuxer) for use, and create threads to use the media demuxer.

<a name="muxer"></a>
## Media Muxer

You can [create audio and video content with a given container format type](#prepare_mux), such as MP4.

The main features of the Media Muxer API include:

- Video and audio elementary stream multiplexing
- MP4 multiplexing support

Tizen supports the MP4 multiplex output streams, and the following MP4 multiplex input elementary streams:

- AVC/H.264 video elementary stream
- MPEG-4 video elementary stream
- MPEG-2 video elementary stream
- MPEG audio elementary stream
- AAC audio elementary stream

A media muxer instance can be used to [mux encoded media into 1 multiplexed stream](#manage_mux). The media muxer can accommodate single or multiple encoded elementary streams of various types, such as audio, video, and text. A single instance of the media muxer can create 1 compatible container format by taking 1 or more elementary streams as input.

Before you start, remember to [prepare your application to use the media muxer functionality](#prerequisites).

The following figure illustrates the general media muxer state changes.

**Figure: Media muxer state changes**

![Media muxer state changes](./media/muxer.png)

> **Note**
>
> All file types and container formats are not guaranteed to support the Media Muxer API.

<a name="demuxer"></a>
## Media Demuxer

You can [demux any multiplexed media streams](#prepare_demux), such as MP4 and MP3.

The main features of the Media Demuxer API include:

- Video, audio, and subtitle demultiplexing
- MP4 demultiplexing support
- MP3 parsing support
- AAC parsing support
- AMR parsing support

Before you start, remember to [prepare your application to use the media demuxer functionality](#prerequisites).

Tizen supports the following MP4 demultiplex streams:

- Input streams:
  - MP4 (M4A, M4V)
  - MP3, AAC, AMR-NB, AMR-WB
- Output elementary streams:
  - AVC/H.264 Video Elementary stream
  - MPEG-4 Video Elementary stream
  - MPEG-2 Video Elementary stream
  - MPEG Audio Elementary stream
  - AAC Audio Elementary stream

A media demuxer instance can be used to parse 1 multiplexed stream. The multiplexed stream can contain single or multiple elementary streams of various types, such as audio, video, or text. A single instance of the media demuxer can [extract 1, more, or all of these elementary streams](#manage_demux).

The following figure illustrates the general media demuxer state changes.

**Figure: Media demuxer state changes**

![Media demuxer state changes](./media/demuxer.png)

> **Note**  
> All file types and container formats are not guaranteed to support the Media Demuxer API.

<a name="prerequisites"></a>
## Prerequisites

To enable your application to use the media muxing functionality:

- To use the functions and data types of the Media Muxer API (in [mobile](../../api/mobile/latest/group__CAPI__MEDIAMUXER__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__MEDIAMUXER__MODULE.html) applications), include the `<mediamuxer.h>` header file in your application:

  ```
  #include <mediamuxer.h>
  ```

- To use the functions and data types of the Media Demuxer API (in [mobile](../../api/mobile/latest/group__CAPI__MEDIADEMUXER__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__MEDIADEMUXER__MODULE.html) applications), include the `<mediademuxer.h>` header file in your application:

  ```
  #include <mediademuxer.h>

  #include <media_format.h>
  #include <media_packet.h>
  ```

  You also need the `<media_format.h>` and `<media_packet.h>` header files to identify and manage individual tracks within the media file.

<a name="prepare_mux"></a>
## Preparing the Media Muxer

To prepare the media muxer:

1. Define a handle for the media muxer and pass it to the `mediamuxer_create()` function. The same handle must be passed to the rest of the media muxer functions.

    ```
    mediamuxer_h *muxer;
    ret = mediamuxer_create(&muxer);
    if (ret != MEDIAMUXER_ERROR_NONE)
        return false;
    ```

2. If the handle is created normally, set the output file path by passing the absolute uri path to the `mediamuxer_set_data_sink()` function:

    ```
    char *path = "/home/media/myfile.mp4"
    mediamuxer_output_format_e format = MEDIAMUXER_CONTAINER_FORMAT_MP4;
    if (mediamuxer_set_data_sink(muxer, path, format)!= MEDIAMUXER_ERROR_NONE)
        printf("mediamuxer_set_data_sink failed\n");
    ```

3. Add the necessary media tracks to the media muxer. The following function shows adding a video elementary track to be muxed.

   A successful `mediamuxer_add_track()` function call returns a `track_index`. Whenever you have to deal with the track, the corresponding `track_index` must be used. Mapping a `track_index` to the corresponding media track is your responsibility.

   ```
   int
   test_mediamuxer_add_track_video()
   {
       int track_index_vid = -1;
       media_format_mimetype_e mimetype;
       int width;
       int height;
       int avg_bps;
       int max_bps;

       media_format_create(&media_format);
       media_format_set_video_mime(media_format, MEDIA_FORMAT_H264_SP);
       media_format_set_video_width(media_format, 640);
       media_format_set_video_height(media_format, 480);
       media_format_set_video_avg_bps(media_format, 256000);
       media_format_set_video_max_bps(media_format, 256000);

       /* Add the video track */
       mediamuxer_add_track(myMuxer, media_format, &track_index_vid);

       return 0;
   }
   ```

4. Once all the tracks are added, start the media muxer:

   ```
   if (mediamuxer_start(muxer) != MEDIAMUXER_ERROR_NONE)
       printf("mediamuxer_start API failed\n");
   ```

5. After a successful muxer start, call a write sample until all the samples of the respective track are written.

   The write sample is a specific track. It is your responsibility to use the appropriate `track_index` to choose the correct track, and to add the corresponding data to the muxer through the write sample. Repeat the same for the rest of the tracks. Before calling this function, create a valid handle for the `media_packet_h` handle to get the input samples. For more information, see [Media Handle Management](media-handle-n.md).

   ```
   if (mediamuxer_write_sample(muxer, track_index, in_buf) != MEDIAMUXER_ERROR_NONE)
       printf("mediamuxer_write_sample API for track %d failed\n", track_index);
   ```

6. Once the EOS (End Of Stream) of a particular track is reached, call `mediamuxer_close_track()` function to finalize the track:

    ```
    if (mediamuxer_close_track(muxer, track_index) != MEDIAMUXER_ERROR_NONE)
        printf("mediamuxer_close_track API failed\n");
    ```
<a name="manage_mux"></a>
## Managing the Media Muxer

To manage the media muxer, the `mediamuxer_write_sample()` function is called in a loop until the EOS is reached. You can use multi-threading, writing samples corresponding to different tracks in different threads.

1. You can create individual threads to manage each track simultaneously, but it is not mandatory. The following sample code explains how to call the `mediamuxer_write_sample()` function for a video track in a unique thread:

    ```
    int
    test_mediamuxer_write_sample()
    {
        pthread_t thread[1];
        pthread_attr_t attr;
        /* Initialize and set thread detached attribute */
        pthread_attr_init(&attr);
        pthread_attr_setdetachstate(&attr, PTHREAD_CREATE_DETACHED);
        pthread_create(&thread[0], &attr, _write_video_data, NULL);
        pthread_create(&thread[1], &attr, _write_audio_data, NULL);

        /* Add audio track, which is not given in this use case */

        pthread_attr_destroy(&attr);

        return 0;
    }

    void*
    _write_video_data()
    {
        gint is_eos = 0;
        int *status = (int *)g_malloc(sizeof(int) * 1);
        v*status = -1;
        int track_index_vid = 1; /* track_index = 1 for video */
        media_packet_h vid_pkt;
        while (!is_eos) {
            /*
               Read encoded video data
               Get the proper video media packet from,
               for example, mediacodec/mediademuxer
            */
            user_func_get_media_packet(&vid_pkt, &is_eos);
            if (!is_eos) {
                mediamuxer_write_sample(myMuxer, track_index_vid, vid_pkt);
                media_packet_destroy(vid_pkt);
            } else {
                g_print("\nVideo while done in the test suite");
                mediamuxer_close_track(myMuxer, track_index_vid);
            }
        }

        return (void *)status;
    }
    ```

2. After you have finished work with the media muxer handle, reset the media muxer and destroy the handle by using the `mediamuxer_stop()` and `mediamuxer_destroy()` functions.

    The media muxer state changes to `MEDIAMUXER_STATE_NONE`.

    ```
    ret = mediamuxer_stop(muxer);
    if (ret != MEDIAMUXER_ERROR_NONE)
        return false;
    ret = mediamuxer_destroy(muxer);
    if (ret != MEDIAMUXER_ERROR_NONE)
        return false;
    ```

<a name="prepare_demux"></a>
## Preparing the Media Demuxer

To prepare the media demuxer:

1. Define a handle for the media demuxer and pass it to the `mediademuxer_create()` function. The same handle must be passed to the rest of the media demuxer functions.

    ```
    mediademuxer_h *demuxer;
    ret = mediademuxer_create(&demuxer);
    if (ret != MEDIADEMUXER_ERROR_NONE)
        return false;
    ```

2. If the handle is created normally, set the input data source by passing the path to the `mediademuxer_set_data_source()` function:

    ```
    if (mediademuxer_set_data_source(demuxer, path)!= MEDIADEMUXER_ERROR_NONE)
        printf("mediademuxer_set_data_source API failed\n");
    ```

3. Call the `mediademuxer_prepare()` function to move the media demuxer into the ready state:

    ```
    if (mediademuxer_prepare(demuxer) != MEDIADEMUXER_ERROR_NONE)
        printf("mediademuxer_prepare API failed\n");
    ```

4. Once the media demuxer is in the ready state, get the total number of individual elementary streams present:

    ```
    if (mediademuxer_get_track_count(demuxer, &num_tracks) != MEDIADEMUXER_ERROR_NONE)
        printf("mediademuxer_get_track_count API failed\n");
    ```

5. Select all the tracks to be extracted:

    ```
    for (track = 0; track < num_tracks; track++) {
        if (mediademuxer_select_track(demuxer, track))
            g_print("mediademuxer_select track %d failed\n", track);
    }
    ```

6. Start the media demuxer:

    ```
    if (mediademuxer_start(demuxer))
        g_print("mediademuxer_start failed\n");
    ```

7. Once the total track counts are known, the media format for each track must be identified. Before calling the `media_format_create()` function, you must define and create a valid `media_format_h` handle (the `format` parameter in the given function).

    The following example retrieves the media format for each track:

    ```
    media_format_h *g_media_format = NULL;
    int track;
    g_media_format = (media_format_h *)g_malloc(sizeof(media_format_h) * num_tracks);
    for (track = 0; track < num_tracks; track++) {
        ret = media_format_create(&g_media_format[track]);
        if (ret == 0) {
            g_print("g_media_format[%d] is created successfully! \n", track);
            ret = mediademuxer_get_track_info(demuxer, track, g_media_format[track]);
            if (ret == 0) {
                if (media_format_get_video_info(g_media_format[track], &mime, &w, &h, NULL, NULL) == MEDIA_FORMAT_ERROR_NONE) {
                    g_print("media_format_get_video_info is success!\n");
                    vid_track = track;
                } else if (media_format_get_audio_info(g_media_format[track], &mime, &channel, &samplerate, NULL, NULL) == MEDIA_FORMAT_ERROR_NONE) {
                    g_print("media_format_get_audio_info is success!\n");
                    aud_track = track;
                } else {
                    g_print("Not supported yet");
                }
            } else {
                g_print("Error while getting mediademuxer_get_track_info\n");
            }
        } else {
            g_print("Error while creating media_format_create\n");
        }
    }
    ```
<a name="manage_demux"></a>
## Managing the Media Demuxer

To manage the media demuxer process:

1. You can create individual threads to manage each track simultaneously, but it is not mandatory. The following sample code explains how to extract the video track in a new thread:

   ```
   int
   test_mediademuxer_read_sample()
   {
       pthread_t thread[1];
       pthread_attr_t attr;
       /* Initialize and set thread detached attribute */
       pthread_attr_init(&attr);
       pthread_attr_setdetachstate(&attr, PTHREAD_CREATE_DETACHED);
       if (vid_track != -1) {
           g_print("In main: creating thread for video\n");
           pthread_create(&thread[0], &attr, _fetch_video_data, NULL);
       }
       pthread_attr_destroy(&attr);

       return 0;
   }

   void*
   _fetch_video_data(void *ptr)
   {
       int *status = (int *)g_malloc(sizeof(int) * 1);
       *status = -1;
       g_print("Video Data function\n");
       int count = 0;
       media_packet_h vidbuf;
       media_format_h vidfmt;
       if (media_format_create(&vidfmt)) {
           g_print("media_format_create failed\n");

           return (void *)status;
       }
       if (media_format_set_video_mime(vidfmt, MEDIA_FORMAT_H264_SP)) {
           g_print("media_format_set_video_mime failed\n");

           return (void *)status;
       }
       if (media_format_set_video_width(vidfmt, 760)) {
           g_print("media_format_set_video_width failed\n");

           return (void *)status;
       }
       if (media_format_set_video_height(vidfmt, 480)) {
           g_print("media_format_set_video_height failed\n");

           return (void *)status;
       }
       if (media_packet_create_alloc(vidfmt, NULL, NULL, &vidbuf)) {
           g_print("media_packet_create_alloc failed\n");
       }
       while (1) {
           int EOS = mediademuxer_read_sample(demuxer, vid_track, &vidbuf);
           if (EOS == MD_EOS || EOS != MD_ERROR_NONE)
               pthread_exit(NULL);
           count++;
           g_print("Read::[%d] video sample\n", count);
           /* Use the media packet and release the packet here */
           media_packet_destroy(vidbuf);
           /* Create a new packet for getting next frame of data */
           if (media_packet_create_alloc(vidfmt, NULL, NULL, &vidbuf)) {
               g_print("media_packet_create_alloc failed\n");
               break;
           }
       }
       *status = 0;

       return (void *)status;
   }
   ```

2. After you have finished work with the media demuxer, reset the media demuxer and destroy the handle by using the `mediademuxer_unprepare()` and `mediademuxer_destroy()` functions.

    The media demuxer state changes to `MEDIADEMUXER_STATE_NONE`.

    ```
    ret = mediademuxer_unprepare(demuxer);
    if (ret != MEDIADEMUXER_ERROR_NONE)
        return false;
    ret = mediademuxer_destroy(demuxer);
    if (ret != MEDIADEMUXER_ERROR_NONE)
        return false;
    ```

## Related Information
- Dependencies
  - Tizen 3.0 and Higher for Mobile
  - Tizen 3.0 and Higher for Wearable
