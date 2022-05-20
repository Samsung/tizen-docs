# WebRTC

You can have real-time audio/video communication with a remote peer. You can send and receive multimedia sources and generic data with a remote peer. The multimedia sources include audio/video stream from microphone, camera or media file. The generic data includes string or byte data.

The main features of the WebRTC API include:

- Managing media sources

  You can [manage media sources](#media_source) which can be transferred to a remote peer. You can add/remove/mute/pause media sources.

- Controlling data channels

  You can [create/destroy data channels and send/receive generic data](#data_channel) to a remote peer.

- Manipulating state and establishing connection

  You can [use functions for session description and ICE candidates](#signaling) to establish network connection with a remote peer properly.

- Rendering receiving data

  You can [decide how to render receiving audio/video streaming data](#media_render).

## Prerequisites

To use the functions and data types of the WebRTC API (in [mobile](../../api/mobile/latest/group__CAPI__MEDIA__WEBRTC__MODULE.html), [wearable](../../api/wearable/latest/group__CAPI__MEDIA__WEBRTC__MODULE.html) and [IoT headed](../../api/iot-headed/latest/group__CAPI__MEDIA__WEBRTC__MODULE.html) applications), include the `<webrtc.h>` header file in your application:

```c
#include <webrtc.h>
```

<a name="media_source"></a>
## Managing Media Source

You can add media sources to a webrtc handle. Once you get source id of the media source, you can manage various functions of the media source with the source id.

1. To add a media source to the webrtc handle, use `webrtc_add_media_source()` function before calling `webrtc_start()` function:

    ```c
    int ret;
    webrtc_h webrtc;
    unsigned int a_src_id;
    unsigned int v_src_id;

    ret = webrtc_create(&webrtc);
    ret = webrtc_add_media_source(webrtc, WEBRTC_MEDIA_SOURCE_TYPE_AUDIOTEST, &a_src_id);
    ret = webrtc_add_media_source(webrtc, WEBRTC_MEDIA_SOURCE_TYPE_VIDEOTEST, &v_src_id);
    ...
    ret = webrtc_start(webrtc);
    ```

2. To set or get the direction of the media source, use `webrtc_media_source_set_transceiver_direction()` or `webrtc_media_source_get_transceiver_direction()` function:
   
    Default transceiver direction of a media source is `WEBRTC_TRANSCEIVER_DIRECTION_SENDRECV`.

    In the following example code, it tries to change the direction to `WEBRTC_TRANSCEIVER_DIRECTION_SENDONLY` before it starts.

    ```c
    ret = webrtc_media_source_set_transceiver_direction(webrtc, v_src_id, WEBRTC_MEDIA_TYPE_VIDEO, WEBRTC_TRANSCEIVER_DIRECTION_SENDONLY);
    ...
    ret = webrtc_start(webrtc);
    ```

3. To pause a media source, use the `webrtc_media_source_set_pause()` function:

    ```c
    ret = webrtc_media_source_set_pause(webrtc, a_src_id, WEBRTC_MEDIA_TYPE_AUDIO, true);
    ```
    > **Note**
    >
    > Pausing a media source means it does not send the data to a remote peer. Pause or resume of a media source is also possible in `WEBRTC_STATE_PLAYING`.

4. To mute a media source, use the `webrtc_media_source_set_mute()` function:

    ```c
    ret = webrtc_media_source_set_mute(webrtc, a_src_id, WEBRTC_MEDIA_TYPE_AUDIO, true);
    ret = webrtc_media_source_set_mute(webrtc, v_src_id, WEBRTC_MEDIA_TYPE_VIDEO, true);
    ```
    > **Note**
    >
    > Muting a media source means it sends black video frames or silent audio frames to a remote peer. Mute or un-mute of a media source is also possible in `WEBRTC_STATE_PLAYING`.
    > Some types of media sources do not support this functionality. For example, `WEBRTC_MEDIA_SOURCE_TYPE_FILE` and `WEBRTC_MEDIA_SOURCE_TYPE_MEDIA_PACKET`.

4. To set or get the video resolution to a media source, use the `webrtc_media_source_set_video_resolution()` or `webrtc_media_source_get_video_resolution()` function:

    ```c
    ret = webrtc_media_source_set_video_resolution(webrtc, v_src_id, 640, 480);
    ```
    > **Note**
    >
    > Some types of media sources support dynamic resolution change while streaming. Otherwise `WEBRTC_ERROR_INVALID_OPERATION` error will be returned.

<a name="data_channel"></a>
## Controlling Data Channels

To be filled.

<a name="signaling"></a>
## Manipulating State and Establishing Connection

To be filled.

<a name="media_render"></a>
## Rendering Receiving Data

To be filled.


## Related Information
- Dependencies
  - Tizen 6.5 and Higher for Mobile
  - Tizen 6.5 and Higher for Wearable
  - Tizen 6.5 and Higher for IoT Headed
