# Multimedia


Multimedia features introduce how you can use multimedia features in your application.

You can use the following multimedia features in your .NET applications:

-   [Media Content](media-content.md)

    You can update database details due to file (or folder) creation or deletion. If a received file (or folder) does not exist in the file system, it is removed from the database. You can also retrieve a list of media folders, retrieve a list of media items, and monitor changes in the media database. You can search for specific media folders and read their information, and retrieve media folder content.

-   [Metadata](metadata.md)

    You can manage audio file attributes, extract metadata from media files, and retrieve various information related to the MIME type.

-   [Image Editing](image-edit.md)

    You can view and process bitmap images in JPEG format. The processing includes decoding, encoding, converting, and compressing images.

-   [Thumbnail Images](thumbnail-images.md)

    You can create a thumbnail from an input media file. The thumbnail can be a video or image, but not an audio file. You can also customize the size of the thumbnail.

-   [Visual Detection and Recognition](media-vision.md)

    You can detect or generate various barcodes. You can also track how faces or image objects move in consecutive camera preview images as well as perceive faces or objects in still images.

-   [Audio Management](audio.md)

    You can control the audio behavior of the application.

-   [Media Playback](media-playback.md)

    You can manage the playback of different media file types. You can play audio and video files, and tones. You can also manage the state of the media player.

-   [Media Recording](media-recording.md)

    You can manage the recording of different media file types. You can record audio data to a file and generate compressed video files using video data from a camera and audio data from an audio input device.

-   [Raw Audio Playback and Recording](raw-audio.md)

    You can play and record uncompressed audio data both synchronously and asynchronously. You can record audio data from a microphone type input device to a file.

-   [Media Controller](media-controller.md)

    You can communicate between the media controller server and the client. The client can send requests to the server to modify the media, and the server can respond to the requests by modifying the media directly as requested. For the media controller feature to work, you must create both the client and server applications.

-   [Media Conversions](media-conversions.md)

    You can perform various media conversions through codecs. You can encode and decode video and audio data, and you can also use video transcoding features, such as multi-format codec and output format.

-   [Screen Mirroring](screen-mirroring.md)

    You can mirror the device screen and sound to another device wirelessly. Tizen supports the screen mirroring feature as a sink that receives shared data from a source device that supports the Wi-Fi Display Technical Specification and displays it.

-   [Radio](radio.md)

    You can allow the user to listen to the FM radio on the device. You can control the radio playback, scan for available frequencies, and change between found frequencies.

-   [Camera](camera.md)

    You can use the camera to preview and capture images. You can capture still images with the device's internal camera and keep images on your target device.

-   [WebRTC](webrtc.md)

    You can have real-time audio/video communication with a remote peer. You can also send and receive generic data with a remote peer.


## Related information
- Dependencies
  -   Tizen 4.0 and Higher

- API References
  - [Tizen.Content.MediaContent](/application/dotnet/api/TizenFX/latest/api/Tizen.Content.MediaContent.html) namespace
    - APIs for MediaContent
  - [Tizen.Multimedia](/application/dotnet/api/TizenFX/latest/api/Tizen.Multimedia.html) namespace
    - APIs for AudioIO, AudioManager, Camera, MediaPlayer, MediaTool, MetadataEditor, MetadataExtractor, Radio, Recorder TonePlayer, WavPlayer, Common Data types
  - [Tizen.Multimedia.MediaCodec](/application/dotnet/api/TizenFX/latest/api/Tizen.Multimedia.MediaCodec.html) namespace
    - APIs for MediaCodec
  - [Tizen.Multimedia.Remoting](/application/dotnet/api/TizenFX/latest/api/Tizen.Multimedia.Remoting.html) namespace
    - APIs for MediaController, ScreenMirroring, WebRTC
  - [Tizen.Multimedia.Util](/application/dotnet/api/TizenFX/latest/api/Tizen.Multimedia.Util.html) namespace
    - APIs for ImageUtil, ThumbnailExtractor
  - [Tizen.Multimedia.Vision](/application/dotnet/api/TizenFX/latest/api/Tizen.Multimedia.Vision.html) namespace
    - APIs for MediaVision