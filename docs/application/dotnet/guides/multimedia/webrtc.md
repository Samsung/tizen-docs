# WebRTC

You can have real-time audio/video communication with a remote peer. You can send and receive multimedia sources and generic data with a remote peer. The multimedia sources include audio/video streams from a microphone, camera, or media file. The generic data includes string or byte data.

The main features of WebRTC include the following:

- Managing media sources

  You can [manage media sources](#media_source) that can be transferred to a remote peer. You can add/remove/mute/pause media sources.

- Controlling data channels

  You can [create/destroy data channels and send/receive generic data](#data_channel) to a remote peer.

- Manipulating state and establishing a connection

  You can [use functions for session description and ICE candidates](#establish_connection) to establish a network connection with a remote peer properly.

- Rendering audio/video data

  You can [decide how to render audio/video streaming data](#media_render).

- Statistics

  You can [get the statistics information about WebRTC](#statistics_info).


<a name="media_source"></a>
## Manage media sources

You can add media sources to the WebRTC. Once you get the media source instance, you can manage various functions of the media source by using the steps below:

1. To add a media source to the WebRTC, use `AddSource()` or `AddSources()` before calling `Start()` or `StartAsync()`:

    ```csharp
    var webRtc = new WebRTC();

    // In case of MediaCameraSource
    var mediaSource = new MediaCameraSource();
    ... or ...
    // In case of MediaFileSource
    var mediaSource = new MediaFileSource("file_source_path");
    ... or ...
    // In case of MediaMicrophoneSource
    var mediaSource = new MediaMicrophoneSource();
    ... or ...
    // In case of MediaNullSource
    var mediaSource = new MediaNullSource();
    ... or ...
    // In case of audio MediaPacketSource
    var mediaSource = new MediaPacketSource(new AudioMediaFormat(MediaFormatAudioMimeType.Opus, 2, 440000, 16, 64000));
    ... or ...
    // In case of video MediaPacketSource
    var mediaSource = new MediaPacketSource(new VideoMediaFormat(MediaFormatVideoMimeType.H264SP, 640, 480));
    ... or ...
    // In case of MediaTestSource
    var mediaSource = new MediaScreenSource();
    ... or ...
    // In case of audio MediaTestSource
    var mediaSource = new MediaTestSource(MediaType.Audio);
    ... or ...
    // In case of video MediaTestSource
    var mediaSource = new MediaTestSource(MediaType.Video);

    webRtc.AddSource(mediaSource);

    // In case of MediaFileSource
    mediaSource.IsLooping = true;
    ...
    await webRtc.StartAsync();
    ```

2. To set or get the direction of the media source, use `TransceiverDirection` property.

    Default transceiver direction of a media source is `TransceiverDirection.SendRecv`.

    In the following example code, it tries to change the direction to `TransceiverDirection.SendOnly` before it starts:

    ```csharp
    mediaSource.TransceiverDirection = TransceiverDirection.SendOnly;
    ...
    await webRtc.StartAsync();
    ```

3. To set or get the codec of the media source, use `TransceiverCodec` property.

    Supported codecs can be obtained by calling `SupportedTransceiverCodecs` property.

    In the following example code, it tries to change the codec to `TransceiverCodec.Pcmu` before it starts:

    ```csharp
    var webRtc = new WebRTC();

    var mediaSource = new MediaTestSource(MediaType.Audio);
    webRtc.AddSource(mediaSource);

    if (mediaSource.SupportedTransceiverCodecs.Contains(TransceiverCodec.Pcmu))
    {
        mediaSource.TransceiverCodec = TransceiverCodec.Pcmu;
    }
    ```

    In the following example code, it creates an offer description which includes an audio stream with OPUS codec of `TransceiverDirection.SendRecv` and a video stream with H264 codec of `TransceiverDirection.RecvOnly`:

    ```csharp
    var webRtc = new WebRTC();

    var audioSource = new MediaMicrophoneSource();  // Default direction is TransceiverDirection.SendRecv
    var videoSource = new MediaNullSource();        // Default direction is TransceiverDirection.RecvOnly

    audioSource.TransceiverCodec = TransceiverCodec.Opus;
    videoSource.SetTransceiverCodec(MediaType.Video, TransceiverCodec.H264);
    ...
    await webRtc.StartAsync();
    var offer = await webRtc.CreateOfferAsync();
    ```
    > [!NOTE]
    > It is recommended to use `MediaNullSource` when you need to set `TransceiverDirection.RecvOnly` of a transceiver which currently belongs to a media source. If so, the media source of this type could give you more codec selection because it does not require to consider encoder situation on the local target device.

4. To pause a media source, use the `Pause` property:

    ```csharp
    mediaSource.Pause = true;
    ```
    > [!NOTE]
    > Pausing a media source means it does not send the data to a remote peer. Pause or resume of a media source is also possible in `WebRTCState.Playing` state.
    > `MediaNullSource` does not support this functionality.

5. To mute a media source, use the `Mute` property:

    ```csharp
    mediaSource.Mute = true;
    ```
    > [!NOTE]
    > Muting a media source means it sends black video frames or silent audio frames to a remote peer. Muting or unmuting of a media source is also possible in the `WebRTCState.Playing` state.
    > Some types of media sources do not support this functionality, such as, `MediaFileSource`, `MediaPacketSource`, and `MediaNullSource`.

6. To set or get the encoder bitrate to a media source, use the `EncoderBitrate` property:

    ```csharp
    ...
    await webRtc.StartAsync();
    ...
    var encoderBitrate = mediaSource.EncoderBitrate;
    // some logic to increase or decrease the current target bitrate
    // e.g. var newEncoderBitrate = encoderBitrate / 2;
    mediaSource.EncoderBitrate = newEncoderBitrate;
    ```
    > [!NOTE]
    > Some types of media sources do not support this functionality, such as, `MediaFileSource`, `MediaPacketSource`, and `MediaNullSource`.

7. To set or get the video resolution to a media source, use the `VideoResolution` property:

    ```csharp
    mediaSource.VideoResolution = new Size(640, 480);
    ```
    > [!NOTE]
    > Some types of media sources support dynamic resolution change while streaming. Otherwise the `InvalidOperationException` exception will be thrown.

8. To set or get the video frame rate to a media source, use the `VideoFrameRate` property:

    ```csharp
    mediaSource.VideoFrameRate = 15;
    ```
    > [!NOTE]
    > If the input value is not supported by the media source, the `ErrorOccurred` event will be invoked.

9. To set the device ID to a media source for camera, use the `CameraDeviceId` property before calling `Start()` or `StartAsync()`:

    ```csharp
    ...
    var cameraSource = new MediaCameraSource();
    webRtc.AddSource(cameraSource);
    ...
    cameraSource.CameraDeviceId = 1;
    ...
    await webRtc.StartAsync();
    ```
    > [!NOTE]
    > If the device ID is not valid, `StartAsync()` or `Start` will throw `InvalidOperationException` exception.

<a name="data_channel"></a>
## Control data channels

You can create a data channel to the WebRTC. It is also possible to be notified when you have a new data channel requested by a remote peer. You can send, or receive data, to or from these data channels by using the APIs below.

1. To create a data channel, use `WebRTCDataChannel` class before calling `Start()` or `StartAsync()`:

    ```csharp
    var webRtc = new WebRTC();
    var dataChannel = new WebRTCDataChannel(webRtc, "data_channel_label");
    ...
    await webRtc.StartAsync();
    ```

2. To be notified when a data channel is created by a remote peer, use the `DataChannel` event. The event will be invoked when it is created after the negotiation:

    ```csharp
    webRtc.DataChannel += (s, e) => Log.Info("WebRTC", "DataChannel is created");

    await webRtc.StartAsync();
    ```

3. Once you get a data channel as above, you can handle the following events:

    ```csharp
    webRtc.DataChannel += (s, e) =>
    {
        e.DataChannel.Opened += (s, e) => Log.Info("WebRTC", "Opened");
        e.DataChannel.Closed += (s, e) => Log.Info("WebRTC", "Closed");
        e.DataChannel.ErrorOccurred += (s, e) => Log.Info("WebRTC", $"{e.Error}");
        e.DataChannel.MessageReceived += (s, e) =>
        {
            switch(e.Type)
            {
                case DataChannelType.Strings:
                    Log.Info("WebRTC", $"{e.Message}");
                    break;
                case DataChannelType.Bytes:
                    var data = e.Data;
                    // do something
                    break;
                default:
                    break;
            }
        }
    }

    await webRtc.StartAsync();
    ```

4. To send string data to the data channel, use `Send()`:

    ```csharp
    dataChannel.Send("string_to_send");
    ```

5. To send byte data to the data channel, use `Send()`:

    ```csharp
    var data = new byte[10];

    // Some works to fill the buffer with data

    dataChannel.Send(data);
    ```

6. To be notified when the number of bytes currently queued for sending data falls to the specific threshold value, use `BufferedAmountLow` event. Note that you should set `BufferedAmountLowThreshold` property first before register `BufferedAmountLow` event:

    ```csharp
    // BufferedAmountLow event will be invoked whenever the size of remaining data in sending queue falls to (128 * 1024) bytes.
    dataChannel.BufferedAmountLowThreshold = 128 * 1024;

    dataChannel.BufferedAmountLow += (s, e) =>
    {
        var data = new byte[10];
        // Some works to fill the buffer with data, and send it again

        dataChannel.Send(data);
    }

    ```

<a name="establish_connection"></a>
## Manipulate state and establish connection

You can change the state of the WebRTC. If you are ready for media sources that need to be sent to a remote peer, you can start the WebRTC. Once you get the state of negotiation, you can utilize functions to create an offer or answer the description, to set a local or remote description, and to add ICE candidates from the remote peer. Finally, you can get the playing state of the handle, as well as a connection between peers is established.

1. To change SDP BUNDLE policy, use `BundlePolicy` property before calling `Start()` or `StartAsync()`:

    ```csharp
    var webRtc = new WebRTC();
    // Default value is WebRTCBundlePolicy.MaxBundle.
    // If the remote endpoint is not BUNDLE-aware, set it as below.
    webRtc.BundlePolicy = WebRTCBundlePolicy.None;
    ...
    await webRtc.StartAsync();
    ```

2. To set STUN or TURN server, use `StunServer` property of `SetTurnServer()`, `SetTurnServers()` before calling `Start()` or `StartAsync()`:

    ```csharp
    var webRtc = new WebRTC();
    webRtc.StunServer = "stun://example.stun.url:1234";
    webRtc.SetTurnServer("turn://id:pw@example.turn.url:1234");
    ...
    await webRtc.StartAsync();
    ```
    > [!IMPORTANT]
    > STUN server URL form must be `stun://host:port`.
    > TURN server URL form must be `turn://username:password@host:port` or `turns://username:password@host:port`.

3. To change ICE transport policy, use `IceTransportPolicy` property before calling `Start()` or `StartAsync()`:

    ```csharp
    var webRtc = new WebRTC();
    // Default value is IceTransportPolicy.All.
    // When it needs to gather only ICE candidates whose IP addresses are being relayed, set it as below.
    webRtc.IceTransportPolicy = IceTransportPolicy.Relay;
    ...
    await webRtc.StartAsync();
    ```

4. To get the state of negotiation, use `Start()` or `StartAsync()`:

    ```csharp
    var webRtc = new WebRTC();

    webRtc.AddSources(new MediaTestSource(MediaType.Audio), new MediaTestSource(MediaType.Video));

    webRtc.IceCandidate += (s, e) =>
    {
        // Gather candidates or send candidate to the remote peer via signaling server
    }
    ...
    // If you use StartAsync() method, we ensure WebRTC state will be changed to WebRTCState.Negotiating.
    // If you use Start() method, you should check WebRTC state using StateChanged event.
    await webRtc.StartAsync();
    ```

5. If the WebRTC client is an offerer, to create an offer description, use `CreateOfferAsync()`:

    ```csharp
    ...
    await webRtc.StartAsync();
    var offerSdp = await webRtc.CreateOfferAsync();
    ```

6. If the WebRTC client is an answerer, to create an answer description, use `CreateAnswerAsync()`:

    ```csharp
    ...
    await webRtc.StartAsync();
    ...
    // After receiving an offer description from the remote peer
    webRtc.SetRemoteDescription(offerSdp);
    ...
    var answerSdp = await webRtc.CreateAnswerAsync();
    ```

7. To gather ICE candidates, use `SetLocalDescription()`:

    ```csharp
    webRtc.IceCandidate += (s, e) =>
    {
        // Gather candidates or send candidate to the remote peer via signaling server.
    }
    webRtc.IceGatheringStateChanged += (s, e) =>
    {
        // You can stop waiting IceCandidate event when the State of this event is changed to WebRTCIceGatheringState.Completed.
    }
    ...
    await webRtc.StartAsync();
    ...
    // The `sdp` can be obtained from calling CreateOfferAsync() or CreateAnswerAsync()
    webRtc.SetLocalDescription(sdp);
    ```

8. To finish the negotiation, use `AddIceCandidate()` or `AddIceCandidates()`, `SetLocalDescription()` or `SetRemoteDescription()`:

    ```csharp
    // After receiving all of ICE candidates from the remote peer
    webRtc.AddIceCandidate(iceCandidate);
    ...
    // In case of an answerer
    webRtc.SetLocalDescription(answerSdp);
    ... or ...
    // In case of an offerer
    webRtc.SetRemoteDescription(answerSdp);
    ...
    // If the connection is established successfully, you'll be notified of the WebRTCState.Playing by the StateChanged event
    ```

9. To be notified of various negotiation states, register event handlers to `PeerConnectionStateChanged`, `SignalingStateChanged`, `IceGatheringStateChanged`, and `IceConnectionStateChanged` events:

    ```csharp
    ...
    webRtc.PeerConnectionStateChanged += (s, e) =>
    {
        // After setting both description and ICE candidates from the remote peer, it'll be changed from
        // WebRTCPeerConnectionState.Connecting to WebRTCPeerConnectionState.Connected.
    }
    webRtc.SignalingStateChanged += (s, e) =>
    {
        // After setting local or remote description it'll be changed to WebRTCSignalingState.HaveLocalOffer or
        // WebRTCSignalingState.HaveRemoteOffer respectively. Both descriptions are set, it'll be changed to WebRTCSignalingState.Stable.
    }
    webRtc.IceGatheringStateChanged += (s, e) =>
    {
        // When setting local description, it'll be changed to WebRTCIceGatheringState.Gathering.
        // If the gathering work is done, it'll be changed to WebRTCIceGatheringState.Completed.
    }
    webRtc.IceConnectionStateChanged += (s, e) =>
    {
        // After setting both description and ICE candidates from the remote peer,
        // it'll be changed from WebRTCIceConnectionState.Checking to WebRTCIceConnectionState.Completed.
    }
    ...
    await webRtc.StartAsync();
    ```

<a name="media_render"></a>
## Render audio/video data

You can decide how to handle audio/video streaming data received from a remote peer by using the functions provided in this API set. You can also render the sending audio/video data on the local target device.

1. To be notified of the creation of an audio or video track from a remote peer, use the `TrackAdded` event:

    ```csharp
    webRtc.TrackAdded += (s, e) =>
    {
        switch (e.Type)
        {
            case MediaType.Audio:
                var policy = new AudioStreamPolicy(AudioStreamType.Media);
                e.MediaStreamTrack.ApplyAudioStreamPolicy(policy);
                break;
            case MediaType.Video:
                e.MediaStreamTrack.Display = new Display(window);
                break;
            default:
                break;
        }
    }
    ...
    await webRtc.StartAsync();
    // After finishing negotiation, TrackAdded event could be invoked if receiving audio/video data from the remote peer exists
    ```
    > [!IMPORTANT]
    > `ApplyAudioStreamPolicy()` or `Display` must be called inside of the callback set by the `TrackAdded` event handler, if you want to output the audio or video track from the remote peer to the local target device's audio device or video display.

2. To get a media packet handle that packs the audio or video data from a remote peer, use the `AudioFrameEncoded` or `VideoFrameEncoded` event:

    ```csharp
    webRtc.AudioFrameEncoded += (s, e) =>
    {
        // Use media packet - copy it's data or pass it to another API.
        // Unref MediaPacket after use.
    }
    webRtc.VideoFrameEncoded += (s, e) =>
    {
        // Use media packet - copy it's data or pass it to another API.
        // Unref MediaPacket after use.
    }
    ...
    await webRtc.StartAsync();
    // After finishing negotiation, AudioFrameEncoded or VideoFrameEncoded event handler could be called if receiving audio/video data from the remote peer exists
    ```

3. To render sending audio/video data on the local target device, use `EnableAudioLoopback()` or `EnableVideoLoopback()`:

    ```csharp
    ...
    var audioSource = new MediaMicrophoneSource();
    var videoSource = new MediaCameraSource();

    webRtc.AddSource(audioSource);
    webRtc.AddSource(videoSource);

    audioSource.EnableAudioLoopback(new AudioStreamPolicy(AudioStreamType.Media));
    videoSource.EnableVideoLoopback(new Display(window));
    ...
    await webRtc.StartAsync();
    ```

4. To change display mode or display visibility, use `MediaStreamTrack.DisplayMode` or `MediaStreamTrack.DisplayVisible` property.

    Three types of display modes exist, `WebRTCDisplayMode.LetterBox`, `WebRTCDisplayMode.OriginSize`, and `WebRTCDisplayMode.Full`.
    These properties are also available for any `MediaStreamTrack` of video loopback.
    In the following example code, it tries to change the mode to `WebRTCDisplayMode.OriginSize` after the display is set and change the visibility in an event function:

    ```csharp
    webRtc.TrackAdded += (s, e) =>
    {
        if (e.MediaStreamTrack.Type == MediaType.Video)
        {
            // You should create or get window instance to display video.
            e.MediaStreamTrack.Display = new Display(window);
            e.MediaStreamTrack.DisplayMode = WebRTCDisplayMode.OriginSize;
            e.MediaStreamTrack.DisplayVisible = true;
        }
    }
    ...
    await webRtc.StartAsync();
    ```

<a name="statistics_info"></a>
## Get statistics information

To get the statistics information of WebRTC, use `GetStatistics()`. This method is possible in the `WebRTCState.Playing` state:
```csharp
...
// WebRTCState is changed to Playing
...
var stats = webRtc.GetStatistics(WebRTCStatisticsCategory.All);
foreach (var stat in stats)
{
    // do something
}
```

## Related information
- Dependencies
  - Tizen 6.5 and Higher
