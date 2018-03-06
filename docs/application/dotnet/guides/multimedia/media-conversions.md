# Media Conversions

You can perform various media conversions through codecs. You can encode and decode video and audio data.

The main features of the Tizen.Multimedia.MediaCodec namespace include:

-   Preparing media codecs

    [Configure the audio and video codecs](#PrepareCodec) and set them as encoders or decoders.

-   Filling media packets

    [Fill the media packet with data](#FillPacket) by reading data chunks from the input file and writing them to the media packet.

-   Running the media codec

    [Run the media codec loop](#RunCodec) and retrieve the output packet.

<a name="PrepareCodec"></a>
## Preparing Media Codecs

To prepare the media codecs:

1.  Create an instance of the [Tizen.Multimedia.MediaCodec.MediaCodec](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Multimedia.MediaCodec.MediaCodec.html) class:

    ```
    var mediaCodec = new MediaCodec();
    ```

2.  Configure the audio and video encoder and decoder, using the `Configure()` method of the `Tizen.Multimedia.MediaCodec.MediaCodec` class:

    -   To set a codec as the encoder, pass `true` as the second parameter of the `Configure()` method:

        ```
        /// Configure an audio encoder
        var audioFormat = new AudioMediaFormat(MediaFormatAudioMimeType.Aac, 2, 48000, 16, 128);
        mediaCodec.Configure(audioFormat, true, MediaCodecTypes.Software);
        ```

    -   To set a codec as the decoder, pass `false` as the second parameter of the `Configure()` method:

        ```
        /// Configure a video decoder
        var videoFormat = new VideoMediaFormat(MediaFormatVideoMimeType.H264SP, 640, 480);
        mediaCodec.Configure(videoFormat, false, MediaCodecTypes.Software);
        ```

3.  To receive notifications whenever the input or output buffers are changed:

    1.  To receive notifications when the input buffer is processed, register an event handler for the `InputProcessed` event of the `Tizen.Multimedia.MediaCodec.MediaCodec` class.

        The event handler receives the currently-processing input packet:

        ```
        mediaCodec.InputProcessed += OnInputProcessed;

        void OnInputProcessed(object sender, InputProcessedEventArgs e)
        {
            Tizen.Log.Info(LogTag, $"The packet format is {e.Packet.Format} and buffer written length is {e.Packet.BufferWrittenLength}");
        }
        ```

    2.  To receive notifications when the output buffers are dequeued, register an event handler for the `OutputAvailable` event of the `Tizen.Multimedia.MediaCodec.MediaCodec` class.

        The event handler receives the result packet:

        ```
        mediaCodec.OutputAvailable += OnOutputAvailable;

        void OnOutputAvailable(object sender, OutputAvailableEventArgs e)
        {
            Tizen.Log.Info(LogTag, $"The packet format is {e.Packet.Format} and buffer written length is {e.Packet.BufferWrittenLength}");

            e.Packet.Dispose();
        }
        ```

<a name="FillPacket"></a>
## Filling Media Packets

To create a media packet and fill it with data:

1.  Create an instance of the [Tizen.Multimedia.MediaPacket](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Multimedia.MediaPacket.html) class:

    ```
    var format = new AudioMediaFormat(MediaFormatAudioMimeType.Pcm, 2, 48000, 16, 128000);
    var packet = MediaPacket.Create(format);
    ```

2.  Read the data from the input file and fill the packet:

    ```
    using (var fs = File.OpenRead(filePath)
    {
        int readSize = 1024 * 2 * 2 * 2;
        byte[] arr = new byte[readSize];
        fs.Read(arr, 0, readSize);

        packet.Buffer.CopyFrom(arr, 0, readSize);
        packet.BufferWrittenLength = readSize;
    }
    ```

<a name="RunCodec"></a>
## Running Media Codecs

After [preparing the media codec](#PrepareCodec) and [filling the media packet with data](#FillPacket), run the media codec in the following loop:

1.  When an input buffer is ready, read a chunk of input and copy it into the buffer to be encoded or decoded.
2.  When an output buffer is ready, copy the encoded or decoded output from the buffer.

To run the media codec loop:

1.  Prepare the media codec using the `Prepare()` method of the [Tizen.Multimedia.MediaCodec.MediaCodec](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Multimedia.MediaCodec.MediaCodec.html) class:

    ```
    mediaCodec.Prepare();
    ```

2.  Set the media packet buffer flag using the `BufferFlags` property of the [Tizen.Multimedia.MediaPacket](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Multimedia.MediaPacket.html) class:

    ```
    /// If the MediaPacket contains codec-specific data, such as SPS or PPS for H.264, set the CodecConfig flag
    packet.BufferFlags |= MediaPacketBufferFlags.CodecConfig;

    /// If the MediaPacket contains the end of stream, set the EOS flag
    packet.BufferFlags |= MediaPacketBufferFlags.EndOfStream;
    ```

3.  To encode or decode packets, start the media codec loop and call the `ProcessInput()` method:

    ```
    mediaCodec.ProcessInput(packet);
    ```

4.  To receive the output packet whenever it is available, register an event handler for the `OutputAvailable` event of the `Tizen.Multimedia.MediaCodec.MediaCodec` class.

    Within the event handler, check whether the output media packet contains key frame or codec data:

    ```
    /// Register an event handler to receive output packet
    mediaCodec.OutputAvailable += OnOutputAvailable;

    /// Define the event handler
    void OnOutputAvailable(object sender, OutputAvailableEventArgs e)
    {
        if (e.Packet.BufferFlags.HasFlag(MediaPacketBufferFlags.SyncFrame))
        {
            Tizen.Log.Info(LogTag, "The packet contains key frame");
        }

        if (e.Packet.BufferFlags.HasFlag(MediaPacketBufferFlags.CodecConfig))
        {
            Tizen.Log.Info(LogTag, "The packet contains codec frame");
        }

        e.Packet.Dispose();
    }
    ```

5.  After the loop is over and you have finished working with the media codec, reset the codec using the `Unprepare()` method:

    ```
    mediaCodec.Unprepare();
    ```

## Related Information
* Dependencies
  -   Tizen 4.0 and Higher
