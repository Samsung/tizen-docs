# WebRTC

You can have real-time audio/video communication with a remote peer. You can send and receive multimedia sources and generic data with a remote peer. The multimedia sources include audio/video stream from microphone, camera or media file. The generic data includes string or byte data.

The main features of the WebRTC API include:

- Managing media sources

  You can [manage media sources](#media_source) which can be transferred to a remote peer. You can add/remove/mute/pause media sources.

- Controlling data channels

  You can [create/destroy data channels and send/receive generic data](#data_channel) to a remote peer.

- Manipulating state and establishing connection

  You can [use functions for session description and ICE candidates](#establish_connection) to establish network connection with a remote peer properly.

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

You can create a data channel to a webrtc handle. It is also possible to get notified when you have new data channel requested by a remote peer. You can send or receive data to or from these data channels by using functions as below.

1. To create a data channel, use `webrtc_create_data_channel()` function before calling `webrtc_start()` function:

    ```c
    int ret;
    webrtc_h webrtc;
    webrtc_data_channel_h channel;

    ret = webrtc_create(&webrtc);
    ret = webrtc_create_data_channel(webrtc, "data_channel_label", NULL, &channel);
    ...
    ret = webrtc_start(webrtc);
    ```

2. To get notified when a data channel is created by a remote peer, use `webrtc_set_data_channel_cb()` function. The callback function will be invoked when it is created after negotiation:

    ```c
    void _data_channel_cb(webrtc_h webrtc, webrtc_data_channel_h channel, void *user_data)
    {
        /* New data channel is created by remote peer request */
    }

    void webrtc_func(void)
    {
        int ret;
        webrtc_h webrtc;
        webrtc_data_channel_h channel;

        ret = webrtc_create(&webrtc);
        ret = webrtc_set_data_channel_cb(webrtc, _data_channel_cb, user_data);
        ...
        ret = webrtc_start(webrtc);
    }
    ```

3. Once you get a data channel as above, it is recommended to set callbacks to handle events from the data channel:

    ```c
    void _data_channel_open_cb(webrtc_data_channel_h channel, void *user_data)
    {
        /* Data channel is opened */
    }

    void _data_channel_message_cb(webrtc_data_channel_h channel, webrtc_data_channel_type_e type, void *message, void *user_data)
    {
        /* Message arrived */
        switch (type) {
        case WEBRTC_DATA_CHANNEL_TYPE_STRING:
            printf("%s\n", (char *)message);
            break;

        case WEBRTC_DATA_CHANNEL_TYPE_BYTES: {
            webrtc_bytes_data_h *data = message;
            const char *data_ptr;
            unsigned long size;

            webrtc_get_data(data, &data_ptr, &size);
            printf("bytes message[%p, size:%lu]\n", data_ptr, size);
            break;
        }
        }
    }

    void _data_channel_close_cb(webrtc_data_channel_h channel, void *user_data)
    {
        /* Data channel is closed */
    }

    void _data_channel_error_cb(webrtc_data_channel_h channel, webrtc_error_e error, void *user_data)
    {
        /* An error occurs on the data channel */
    }

    void data_channel_set_callbacks(webrtc_data_channel_h channel, void *user_data)
    {
        webrtc_data_channel_set_open_cb(channel, _data_channel_open_cb, user_data);
        webrtc_data_channel_set_message_cb(channel, _data_channel_message_cb, user_data);
        webrtc_data_channel_set_error_cb(channel, _data_channel_error_cb, user_data);
        webrtc_data_channel_set_close_cb(channel, _data_channel_close_cb, user_data);
    }
    ```

4. To send string data to the data channel, use `webrtc_data_channel_send_string()`:

    ```c
    ret = webrtc_data_channel_send_string(channel, "string_to_send");
    ```

5. To send bytes data to the data channel, use `webrtc_data_channel_send_bytes()`:

    ```c
    char buffer[BUFFER_SIZE] = {0, };
    unsigned int data_size;

    /* Some works to fill the buffer with data */

    ret = webrtc_data_channel_send_bytes(channel, buffer, data_size);
    ```

<a name="establish_connection"></a>
## Manipulating State and Establishing Connection

You can change state of the webrtc handle. If you are ready for media sources that need to be sent to a remote peer, you can start the handle. Once you get the state of negotiation, you can utilize functions to create offer or answer description, to set local or remote description and to add ICE candidates from remote peer. Finally, you can get the playing state of the handle as well as a connection between peers is established.

1. To get the state of negotiation, use `webrtc_start()` function:

    ```c
    void _ice_candidate_cb(webrtc_h webrtc, const char *candidate, void *user_data)
    {
        /* Gather candidates or send candidate to the remote peer via signaling server */
    }

    void _state_changed_cb(webrtc_h webrtc, webrtc_state_e previous, webrtc_state_e current, void *user_data)
    {
        /* After webrtc_start(), current state will be changed to WEBRTC_STATE_NEGOTIATING */
    }

    void webrtc_func(void)
    {
        int ret;
        webrtc_h webrtc;
        unsigned int a_src_id;
        unsigned int v_src_id;

        ret = webrtc_create(&webrtc);
        ret = webrtc_add_media_source(webrtc, WEBRTC_MEDIA_SOURCE_TYPE_AUDIOTEST, &a_src_id);
        ret = webrtc_add_media_source(webrtc, WEBRTC_MEDIA_SOURCE_TYPE_VIDEOTEST, &v_src_id);
        ...
        ret = webrtc_set_ice_candidate_cb(webrtc, _ice_candidate_cb, user_data);
        ret = webrtc_set_state_changed_cb(webrtc, _state_changed_cb, user_data);
        ...
        ret = webrtc_start(webrtc);
    }
    ```

2. If the handle is an offerer, to create offer description, use `webrtc_create_offer()` or `webrtc_create_offer_async()` function:
    ```c
    int ret;
    webrtc_h webrtc;
    char *offer_desc;
    ...
    ret = webrtc_start(webrtc);
    ret = webrtc_create_offer(webrtc, NULL, &offer_desc);
    ...
    /* After sending this offer description to the remote peer */
    free(offer_desc);
    ```

3. If the handle is an answerer, to create answer description, use `webrtc_create_answer()` or `webrtc_create_answer_async()` function:
    ```c
    int ret;
    webrtc_h webrtc;
    char *answer_desc;
    ...
    ret = webrtc_start(webrtc);
    ...
    /* After receiving an offer description from the remote peer */
    ret = webrtc_set_remote_description(webrtc, offer_desc_from_remote);
    ret = webrtc_create_answer(webrtc, NULL, &answer_desc);
    ...
    /* After sending this answer description to the remote peer */
    free(offer_desc);
    ```

4. To gather ICE candidates, use `webrtc_set_local_description()` function:
    ```c
    void _ice_candidate_cb(webrtc_h webrtc, const char *candidate, void *user_data)
    {
        /* Gather candidates or send candidate to the remote peer via signaling server */
    }

    void _ice_gathering_state_change_cb(webrtc_h webrtc, webrtc_ice_gathering_state_e state, void *user_data)
    {
        /* Until the state is changed to WEBRTC_ICE_GATHERING_STATE_COMPLETE, _ice_candidate_cb() will be called */
    }

    void webrtc_func(void)
    {
        int ret;
        webrtc_h webrtc;
        char *local_desc;
        ...
        ret = webrtc_set_ice_candidate_cb(webrtc, _ice_candidate_cb, user_data);
        ret = webrtc_set_state_changed_cb(webrtc, _state_changed_cb, user_data);
        ret = webrtc_set_ice_gathering_state_change_cb(webrtc, _ice_gathering_state_change_cb, user_data);
        ...
        ret = webrtc_start(webrtc);
        ...
        /* local_desc can be obtained from calling webrtc_create_offer() or webrtc_create_answer() */
        ret = webrtc_set_local_description(webrtc, local_desc);
    }
    ```

5. To finish the negotiation, use `webrtc_add_ice_candidate()`, `webrtc_set_local_description()` or `webrtc_set_remote_description()` function:

    ```c
    /* After receiving all of ICE candidates from remote peer */
    ret = webrtc_add_ice_candidate(webrtc, candidate);
    ...
    /* In case of an answerer */
    ret = webrtc_set_local_description(webrtc, answer_desc);
    ... or ...
    /* In case of an offerer */
    ret = webrtc_set_remote_description(webrtc, answer_desc);
    ...
    /* If the connection is established successfully, you'll get notified of WEBRTC_STATE_PLAYING by _state_changed_cb() */
    ```
6. To get notified of various negotiation states, set callbacks by using `webrtc_set_peer_connection_state_change_cb()`, `webrtc_set_signaling_state_change_cb()`, `webrtc_set_ice_gathering_state_change_cb()` and `webrtc_set_ice_connection_state_change_cb()` function:
   ```c
    void _peer_connection_state_change_cb(webrtc_h webrtc, webrtc_peer_connection_state_e state, void *user_data)
    {
        /* After setting both description and ICE candidates from remote peer, it'll be changed from WEBRTC_PEER_CONNECTION_STATE_CONNECTING to WEBRTC_PEER_CONNECTION_STATE_CONNECTED. */
    }

    void _signaling_state_change_cb(webrtc_h webrtc, webrtc_signaling_state_e state, void *user_data)
    {
        /* After setting local or remote description it'll be changed to WEBRTC_SIGNALING_STATE_HAVE_LOCAL_OFFER or WEBRTC_SIGNALING_STATE_HAVE_REMOTE_OFFER respectively. Both descriptions are set, it'll be changed to WEBRTC_SIGNALING_STATE_STABLE. */
    }

    void _ice_gathering_state_change_cb(webrtc_h webrtc, webrtc_ice_gathering_state_e state, void *user_data)
    {
        /* When setting local description, it'll be changed to WEBRTC_ICE_GATHERING_STATE_GATHERING. If the gathering work is done, it'll be changed to WEBRTC_ICE_GATHERING_STATE_COMPLETE. */
    }

    void _ice_connection_state_change_cb(webrtc_h webrtc, webrtc_ice_connection_state_e state, void *user_data)
    {
        /* After setting both description and ICE candidates from remote peer, it'll be changed from WEBRTC_ICE_CONNECTION_STATE_CHECKING to WEBRTC_ICE_CONNECTION_STATE_COMPLETED. */
    }

    void webrtc_func(void)
    {
        int ret;
        webrtc_h webrtc;
        char *local_desc;
        ...
        ret = webrtc_set_peer_connection_state_change_cb(webrtc, _peer_connection_state_change_cb, user_data);
        ret = webrtc_set_signaling_state_change_cb(webrtc, _signaling_state_change_cb, user_data);
        ret = webrtc_set_ice_gathering_state_change_cb(webrtc, _ice_gathering_state_change_cb, user_data);
        ret = webrtc_set_ice_connection_state_change_cb(webrtc, _ice_connection_state_change_cb, user_data);
        ...
        ret = webrtc_start(webrtc);
        /* Do negotiation */
    }
    ```

<a name="media_render"></a>
## Rendering Receiving Data

To be filled.


## Related Information
- Dependencies
  - Tizen 6.5 and Higher for Mobile
  - Tizen 6.5 and Higher for Wearable
  - Tizen 6.5 and Higher for IoT Headed
