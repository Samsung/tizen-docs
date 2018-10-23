# Media Stream Playback


Tizen enables you to use media streamer functionalities, such as playing video content and streaming video and audio over an IP. Media streaming allows you to stream content in 1 or both directions.

**Figure: Video call**

![Video call](./media/media_streamer_phone.png)

The media streamer is an object that manages media data flow in a kind of pipeline. The Media Streamer API provides various types of media processing pipelines using a simple GStreamer wrapper (Tizen uses GStreamer as a fundamental multimedia framework). To use the media streamer, familiarize yourself with how the GStreamer works. For more information, see [http://gstreamer.freedesktop.org/](http://gstreamer.freedesktop.org/).

The media streamer works by using a collection of nodes, which are connected in a specific order to make a specific pipeline of multimedia data running through the nodes:

- The **source nodes** represent the source of the input data. The media streamer provides a common interface for getting a media stream from various source nodes, such as media files, network, and various input devices, such as cameras and microphones.
- The **topology nodes** (transforming nodes) are used to transform the data along the pipeline.
- The **sink nodes** are used to render the media stream data.

The main features of the Media Streamer API include:

- Creating the media streamer

  You can create a [media streamer](#create) handle used for linking content source and sink elements in [server](#create_server) and [client](#create_client) parts.

- Plugging media streamer nodes in manual or autoplug mode

  You can [create a chain of media streamer nodes](#plugin) to properly play a video file or combine the server and client parts for streaming the content. This can be done manually or automatically within the Media Streamer framework.

- Managing the media streamer parameters

  You can [set a number of parameters](#manage) to properly play a video file or combine the server and client parts for playing or streaming the content. You can also get a number of parameters from the media streamer nodes to find out the characteristics of playing or streaming the content.

- Playing files with the media streamer

  You can [play video files or launch content streaming over IP](#play).

- Destroying the media streamer

  When no longer needed, you can [destroy the media streamer](#destroy) handle used for linking content source and sink elements.

The Tizen Media Streamer framework can be used in many scenarios:

- Playing a local video file

  **Figure: Playing a local video file**

  ![Playing a local video file](./media/media_streamer_local_video.png)

- Playing a local video file with internal or external subtitles

  **Figure: Playing a local video file with subtitles**

  ![Playing a local video file with subtitles](./media/media_streamer_local_video_subtitles.png)

- Streaming a video file with or without internal subtitles through the IP protocol from the server part to the client part

  **Figure: Streaming a file through IP in the broadcast mode**

  ![Streaming a file through IP in the broadcast mode](./media/media_streamer_stream_broadcast.png)

- Streaming video and audio content through the IP protocol from 1 device (server part) to another device (client part) in 1 way (broadcast mode) or both ways (VOIP mode)

  **Figure: Streaming video and audio content through IP in the broadcast or VOIP mode**

  ![Streaming video and audio content through IP in the broadcast or VOIP mode](./media/media_streamer_stream_broadcast_or_voip.png)

<a name="create"></a>
## Media Streamer

The media streamer is created using the `media_streamer_create()`, `media_streamer_node_create_src()`, and `media_streamer_node_create_sink()` functions.

The following types are examples of the source nodes according to their functionalities:

- `MEDIA_STREAMER_NODE_SRC_TYPE_FILE`
- `MEDIA_STREAMER_NODE_SRC_TYPE_CAMERA`
- `MEDIA_STREAMER_NODE_SRC_TYPE_AUDIO_CAPTURE`

In the same concept, the following types are examples of the sink nodes:

- `MEDIA_STREAMER_NODE_SINK_TYPE_OVERLAY`
- `MEDIA_STREAMER_NODE_SINK_TYPE_AUDIO`

The media streamer RTP node is also created in a streaming scenario where data is transmitted or received through an IP.

After the nodes are created, they are uploaded into the media streamer pipeline where, in connection with other topology nodes, they construct a logic chain to be launched according to the chosen scenario. The `media_streamer_node_add()` function is used to add a node to the media streamer.

<a name="plugin"></a>
## Media Streamer Modes

The Media Streamer framework creates and links nodes for launching video encoding and decoding chains in manual or autoplug modes.

- In the manual mode, a user takes responsibility on creating and linking the appropriate encoding or decoding chain of nodes to launch the media streamer for the chosen scenario.

  The media streamer nodes are plugged in the manual mode using the `media_streamer_node_create()` and `media_streamer_node_add()` functions.

  Link the media streamer nodes with the `media_streamer_node_link()` function.

  The function attributes include `src_pad_name` and `sink_pad_name`, which can be `src` or `sink`, an income or outcome pads of the previous and the following nodes to be linked accordingly.

- In the autoplug mode, the video encoding and decoding chain of the media streamer is automatically constructed from the previously created source and sink nodes.

<a name="manage"></a>
## Media Streamer Parameters

The Media Streamer framework sets parameters onto the nodes for launching appropriate video encoding and decoding chains. It also gets parameters from the nodes to find out about the encoding and decoding characteristics of the node.

### Setting Parameters

A parameter is set onto the media streamer node using the `media_streamer_node_set_param()` function. The function sets a possible parameter for the given node with the appropriate value. The possible parameter can be found in the `media_streamer.h` header file. The parameter can be, for example, `MEDIA_STREAMER_PARAM_CAMERA_ID`, `MEDIA_STREAMER_PARAM_ROTATE`, or `MEDIA_STREAMER_PARAM_PORT`. You can also set a parameter list using a `bundle` structure.

The `media_streamer_node_set_pad_format()` function sets the media format onto the media streamer node pad. The pad of the media streamer node can be `sink` or `src`, which are income or outcome pads of the node. The following are examples of the format:

- `MEDIA_FORMAT_RAW`
- `MEDIA_FORMAT_ENCODED`
  - `MEDIA_FORMAT_H263`
  - `MEDIA_FORMAT_YV12`

You can use the following media streamer callbacks when setting parameters:

- The `media_streamer_set_error_cb()` and `media_streamer_unset_error_cb()` functions register and unregister an error callback function to be invoked when an error occurs.
- The `media_streamer_set_state_change_cb()` and `media_streamer_unset_state_change_cb()` functions register and unregister a callback to be invoked after the media streamer state changes.
- The `media_streamer_src_set_buffer_status_cb()` and `media_streamer_src_unset_buffer_status_cb()` functions register and unregister a callback function to be invoked when a buffer underrun or overflow occurs.
- The `media_streamer_sink_set_data_ready_cb()` and `media_streamer_sink_unset_data_ready_cb()` functions register and unregister a callback function to be invoked when the custom sink is ready for data processing.
- The `media_streamer_sink_set_eos_cb()` and `media_streamer_sink_unset_eos_cb()` functions register and unregister a callback function to be invoked when the custom sink detects the end-of-stream.

### Getting Parameters

Use the `media_streamer_node_get_param()` function to get a parameter from the media streamer node. The function gets a parameter possible for the given node with the appropriate value. The possible parameters returned can be found in the `media_streamer.h` header file. They can be, for example, `MEDIA_STREAMER_PARAM_CAMERA_ID`, `MEDIA_STREAMER_PARAM_ROTATE`, or `MEDIA_STREAMER_PARAM_PORT`.

You can also use the `media_streamer_node_get_params()` function to get the list of parameters from the created media streamer node in the `bundle` structure format.

The `media_streamer_node_get_pad_format()` function gets the media format from the media streamer node pad. The pad of the media streamer node can be `sink` or `src`, which are income or outcome pads of the node. The following are examples of the format:

- `MEDIA_FORMAT_RAW`
- `MEDIA_FORMAT_ENCODED`
  - `MEDIA_FORMAT_H263`
  - `MEDIA_FORMAT_YV12`

To get the name from the media streamer node pad, use the `media_streamer_node_get_pad_name()` function. The `src_pad_num` parameter defines the number of `src` pads in the previous node, and the `sink_pad_num` parameter defines the number of `sink` pads in the following node.

You can get the media streamer state using the `media_streamer_get_state()` function. The states of the media streamer node can be found in the `media_streamer.h` header file. The state can be, for example, `MEDIA_STREAMER_STATE_READY`.

<a name="play"></a>
## File Playing with Media Streamer

Before playing the media streamer, it must be prepared and the state of the media streamer nodes must be set to the `MEDIA_STREAMER_STATE_READY` state in [server](#prepare_server) and [client](#client_prepare) parts.

The `media_streamer_prepare()` function prepares the media streamer. With this function, the encoding chain of the media streamer nodes becomes fully constructed, if the autoplug mode is chosen within the streaming scenario.

To play or stream files with the media streamer, use the `media_streamer_play()` function in [server](#playing_server) and [client](#client_play) parts. The media streamer state changes to `MEDIA_STREAMER_STATE_PLAYING`. With this function, the decoding chain of the media streamer nodes becomes fully constructed, if the autoplug mode is chosen within the streaming or playing scenario. The media streamer starts playing or streaming content, and the appropriate content appears on the sink nodes.

You can control the playing status of the media streamer:

- Pause

  The `media_streamer_pause()` function sets the media streamer state to `MEDIA_STREAMER_STATE_PAUSED` in the playing mode or at the server part in the streaming mode. Playing or streaming of the content pauses, and this can be seen on the sink nodes.

- Stop

  The `media_streamer_stop()` function sets the media streamer state to `MEDIA_STREAMER_STATE_PAUSED` in the playing mode or at the server part in the streaming mode. The position of the content is set to the 0sec position. Playing or streaming of the content stops, and this can be seen on the sink nodes.

- Seek

  The `media_streamer_set_play_position()` function seeks the content at the appropriate playing position set in milliseconds in the playing mode or at the server part in the video file streaming mode. Playing or streaming of the content seeks to the appropriate position, and this can be seen on the sink nodes.

- Get info

  The `media_streamer_get_play_position()` and `media_streamer_get_duration()` functions get the media streamer playing position and duration of the content in milliseconds in the playing mode or at the server part in the video file streaming mode.

<a name="destroy"></a>
## Media Streamer Removal

Before destroying the media streamer, it must be unprepared using the `media_streamer_unprepare()` function, and the state of the media streamer nodes must be set to `MEDIA_STREAMER_STATE_IDLE`.

With the `media_streamer_unprepare()` function, the media streamer nodes within the encoding and decoding chains become disconnected, if the autoplug mode is chosen in the streaming or playing scenario. Any intermediate topology nodes between the source and sink nodes that have been automatically created are removed.

Use the `media_streamer_node_remove()` and `media_streamer_node_destroy()` functions to remove and destroy a media streamer node created in the manual mode.

To destroy the media streamer, use the `media_streamer_destroy()` function. The media streamer nodes that have not been removed manually from the media streamer are removed automatically.

## Prerequisites

The use cases in this guide demonstrate how you can use the media streamer functionality to stream video content in the form of Videotestsrc in the broadcast manual mode.

To launch streaming, you must create a server part media streamer on the first device and a client part media streamer on the second device. While creating the server part, you must indicate the IP address of the client part to stream to, in IPv4 format.

**Figure: Topology scheme of the media streamer Videotestsrc streaming scenario**

![Media streamer scenario](./media/media_streamer_scenario.png)

<a name="create_server"></a>
## Creating the Server Part

To create the server part:

1. Create the media streamer handle and call the `media_streamer_create()` function:

    ```
    media_streamer_h ms_streamer;
    int media_streamer_create(&ms_streamer);
    ```

	Memory is allocated for the given handle.

2. Create a source node of the video data stream to transfer to the client part.

   For example, the Videotest node is a checkerboard pattern of colors at the edge of the YCbCr gamut and nearby colors that are out of gamut.

   1. Create the `Videotestsrc` source node:

      ```
      media_streamer_node_h video_src = NULL;
      media_streamer_node_create_src(MEDIA_STREAMER_NODE_SRC_TYPE_VIDEO_TEST, &video_src);
      ```

   2. Add the `Videotestsrc` source node to the media streamer:

      ```
      media_streamer_node_add(ms_streamer, video_src);
      ```

3. To transfer data over an IP connection, create the final sending node on the server part and the first receiving node on the client part. The creation of the client part is described in [Creating the Client Part](#create_client).

    The Real Time Protocol (RTP) node is universal and unique at the same time, and capable of performing enormous work on the RTP packets for their truthful and confident transmission, such as RTP packet validation, maintenance of the SSRC participant database, scheduling of RR/SR RTCP packets, and parsing codec streams transmitted in the same RTP session.

	- Create the `rtp_bin` RTP node:

      ```
      media_streamer_node_h rtp_bin = NULL;
      media_streamer_node_create(MEDIA_STREAMER_NODE_TYPE_RTP, NULL, NULL, &rtp_bin);
      ```

	- Create a bundle and add the RTP node parameters to it:

      ```
      bundle *params = bundle_create();
      bundle_add_str(params, MEDIA_STREAMER_PARAM_VIDEO_OUT_PORT, "5000");
      bundle_add_str(params, MEDIA_STREAMER_PARAM_HOST, "127.0.0.1");
      media_streamer_node_set_params(rtp_bin, params);
      ```

	- Add the RTP node to the media streamer:

      ```
      media_streamer_node_add(ms_streamer, rtp_bin);
      ```

4. Create the encoding format.

   To turn raw video from Videotestsrc or captured video data into encoded video data, an encoder is needed. The conversion of raw video streams (scaling, frame rate conversion, color space conversion, and samplerate conversion) is one of the main tasks to conform to the profile output format. The encoding format can be H263 or H264, for example.

   ```
   media_format_h vfmt_encoded = NULL;
   /* Define encoded video format */
   media_format_create(&vfmt_encoded);
   if (media_format_set_video_mime(vfmt_encoded, MEDIA_FORMAT_H263) != MEDIA_FORMAT_ERROR_NONE)
       g_print("media_format_set_video_mime failed!");

   media_format_set_video_width(vfmt_encoded, 800);
   media_format_set_video_height(vfmt_encoded, 600);
   media_format_set_video_avg_bps(vfmt_encoded, 10000);
   media_format_set_video_max_bps(vfmt_encoded, 30000);
   ```

5. Create the video encoder node.

   The video converter, video scale, video encoder, video filter, and video parser elements are logically connected inside the video encoder node. They are all initially predefined in the `.ini` file.

   ```
   media_streamer_node_h video_enc = NULL;
   media_streamer_node_create(MEDIA_STREAMER_NODE_TYPE_VIDEO_ENCODER, NULL, vfmt_encoded, &video_enc);
   ```

   Add the video encoder node to the media streamer:

   ```
   media_streamer_node_add(ms_streamer, video_enc);
   ```

6. An encoded video from the encoder must be loaded in RTP packets for further transmission through the RTP protocol connection. It is used right before the RTP node, which sends the received RTP packets into the network source or before the UDP sink that pushes the UDP packets into the network.

   1. Create the video pay node:

      ```
      media_streamer_node_h video_pay = NULL;
      media_streamer_node_create(MEDIA_STREAMER_NODE_TYPE_VIDEO_PAY, NULL, vfmt_encoded, &video_pay);
      ```

   2. Add the video pay node to the media streamer:

      ```
      media_streamer_node_add(ms_streamer, video_pay);
      ```

7. To have a proper functionality for streaming nodes, link the nodes between each other into a logic chain.

   1. Find out the pad names of the nodes to be linked:

      ```
      char **src_pad_name = NULL;
      int src_pad_num = 0;
      char **sink_pad_name = NULL;
      int sink_pad_num = 0;
      media_streamer_node_get_pad_name(video_pay, &src_pad_name, src_pad_num, &sink_pad_name, &sink_pad_num);
      ```

   2. Link the nodes consequently into a line:

      ```
      media_streamer_node_link(video_src, "src", video_enc, "sink");
      media_streamer_node_link(video_enc, "src", video_pay, "sink");
      media_streamer_node_link(video_pay, "src", rtp_bin, "video_in");
      ```

<a name="prepare_server"></a>
## Preparing the Server Part

To prepare the server part of the media streamer, transfer the nodes from the `MEDIA_STREAMER_STATE_IDLE` state to the `MEDIA_STREAMER_STATE_READY` state.

Call the `media_streamer_prepare()` function to change the state:

```
int media_streamer_prepare(ms_streamer);
```

<a name="playing_server"></a>
## Playing the Server Part

To play the server part of the Media Streamer, transfer the nodes from the `MEDIA_STREAMER_STATE_READY` state to the `MEDIA_STREAMER_STATE_PLAYING` state.

Call the `media_streamer_play()` function to change the state and start playing:

```
int media_streamer_play(ms_streamer);
```

<a name="create_client"></a>
## Creating the Client Part

To create the client part on the 2nd device on which the server part device is intended to stream to through an IP:

1. Create the media streamer handle and call the `media_streamer_create()` function:

    ```
    media_streamer_h ms_streamer;
    int media_streamer_create(&ms_streamer);
    ```

    Memory is allocated for the given handle.

2. To enable video output, a proper video sink node must be present.

   1. Create the video sink node:

      ```
      media_streamer_node_h video_sink = NULL;
      media_streamer_node_create_sink(MEDIA_STREAMER_NODE_SINK_TYPE_OVERLAY, &video_src);
      ```

   2. Add the video sink node to the media streamer:

      ```
      media_streamer_node_add(ms_streamer, video_sink);
      ```

3. Create the encoding format.

   To receive video in a proper format, set it initially to have a proper video stream frame on the client part.

   ```
   media_format_h vfmt_encoded = NULL;
   /* Define the encoded video format */
   media_format_create(&vfmt_encoded);
   if (media_format_set_video_mime(vfmt_encoded, MEDIA_FORMAT_H263) != MEDIA_FORMAT_ERROR_NONE)
       g_print("media_format_set_video_mime failed!");

   media_format_set_video_width(vfmt_encoded, 800);
   media_format_set_video_height(vfmt_encoded, 600);
   media_format_set_video_avg_bps(vfmt_encoded, 10000);
   media_format_set_video_max_bps(vfmt_encoded, 30000);
   ```

4. To receive data over an IP connection, first create the receiving node on the client part to be able to receive RTP packets for their further decoding into a video stream.

   The RTP node is universal and unique at the same time, and capable of performing enormous work on RTP packets for their truthful and confident receiving, such as keeping per participant statistics based on received RTCP packets, allowing an application to easily receive and decode an RTP stream with multiple SSRCs, and reordering and removing duplicate RTP packets as they are received from a network source.

   1. Create the `rtp_bin` RTP node:
      ```
      media_streamer_node_h rtp_bin = NULL;
      media_streamer_node_create(MEDIA_STREAMER_NODE_TYPE_RTP, NULL, NULL, &rtp_bin);
      ```

   2. Create a bundle and add the RTP node parameters to it:

      ```
      bundle *params = bundle_create();
      bundle_add_str(params, MEDIA_STREAMER_PARAM_VIDEO_IN_PORT, "5005");
      media_streamer_node_set_params(rtp_bin, params);
      ```

   3. Set the incoming format for the RTP node:

      ```
      media_streamer_node_set_pad_format(rtp_node, "video_in_rtp", vfmt_encoded);
      ```

   4. Add the RTP node to the media streamer:

      ```
      media_streamer_node_add(ms_streamer, rtp_bin);
      ```

5. To extract raw video from RTP packets, depayload them for further decoding to get a valid video data stream. It is used right after the RTP node, which supplies the received RTP packets from the network source, or after the UDP source that reads the UDP packets from the network.

   1. Create the video depay node:

      ```
      media_streamer_node_h video_depay= NULL;
      media_streamer_node_create(MEDIA_STREAMER_NODE_TYPE_VIDEO_DEPAY, NULL, vfmt_encoded, &video_depay);
      ```

   2. Add the video depay node to the media streamer:

      ```
      media_streamer_node_add(ms_streamer, video_depay);
      ```

6. Create the video decoder node.

   The video decoder, video parser, video converter, and video scale elements are logically connected inside the video decider node. They are all initially predefined in the `.ini` file.

   ```
   media_streamer_node_h video_dec = NULL;
   media_streamer_node_create(MEDIA_STREAMER_NODE_TYPE_VIDEO_DECODER, NULL, vfmt_encoded, &video_dec);
   ```

   Add the video decoder node to the media streamer:

   ```
   media_streamer_node_add(ms_streamer, video_dec);
   ```

7. Create the video queue node:

   ```
   media_streamer_node_h video_queue= NULL;
   media_streamer_node_create(MEDIA_STREAMER_NODE_TYPE_QUEUE, NULL, vfmt_encoded, &video_queue);
   ```

   Add the video queue node to the media streamer:

   ```
   media_streamer_node_add(ms_streamer, video_queue);
   ```

8. To have a proper receiving node functionality, link the client nodes between each other into a logic chain:

   ```
   media_streamer_node_link(video_depay, "src", video_dec, "sink");
   media_streamer_node_link(video_dec, "src", video_queue, "sink");
   media_streamer_node_link(video_queue, "src", video_sink, "sink");
   ```

<a name="client_prepare"></a>
## Preparing the Client Part

To prepare the client part of the media streamer, transfer the nodes from the `MEDIA_STREAMER_STATE_IDLE` state to the `MEDIA_STREAMER_STATE_READY` state.

Call the `media_streamer_prepare()` function to change the state:

```
int media_streamer_prepare(ms_streamer);
```

<a name="client_play"></a>
## Playing the Client Part

To play the client part of the media streamer, transfer the nodes from the `MEDIA_STREAMER_STATE_READY` state to the `MEDIA_STREAMER_STATE_PLAYING` state.

Call the `media_streamer_play()` function to change the state and start playing:

```
int media_streamer_play(ms_streamer);
```

At this point, the VideoTest Streaming is shown on the client part device.

**Figure: Media streamer client part device receiving Videotestsrc streamed in the streaming scenario**

![Media streamer streaming media](./media/media_streamer_playing.png)

## Related Information
- Dependencies
  - Tizen 3.0 and Higher for Mobile
  - Tizen 3.0 and Higher for Wearable
