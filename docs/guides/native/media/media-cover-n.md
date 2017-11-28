# Media and Camera
## Dependencies
- Tizen 2.4 and Higher for Mobile
- Tizen 2.3.1 and Higher for Wearable

The media and camera features introduce how you can use multimedia features in your application.

You can use the following media and camera features in your native applications:

- [Media Content and Metadata](media-content-metadata-n.md)
You can manage and search for various media content on the device, such as media files, bookmarks, albums, and playlists. You can also access the MIME type information, and extract and edit the metadata of the media files.

- [Image Editing](image-edit-n.md)
You can view and process bitmap images in JPEG format. The processing includes decoding, encoding, converting, and compressing images.

- [Thumbnail Images](thumbnail-images-n.md)
You can create a thumbnail from an input media file. The thumbnail can be a video or image, but not an audio file. You can also customize the size of the thumbnail.

- [Visual Detection and Recognition](media-vision-n.md)
You can detect or generate various barcodes. You can also track how faces or image objects move in consecutive camera preview images as well as perceive faces or objects in still images.

- [Audio Management](audio-n.md)
You can control the audio behavior of the application. You can control the output volume and sound session types, and query various information from sound devices. You can also use OpenAL to specify the objects and operations in producing high-quality audio output.

- [Media Playback](media-playback-n.md)
You can manage the playback of different media file types. You can play audio and video files, and tones. You can also manage the state of the media player.

- [Media Recording](media-recording-n.md)
You can manage the recording of different media file types. You can record audio data to a file and generate compressed video files using video data from a camera and audio data from an audio input device.

- [Raw Audio Playback and Recording](raw-audio-n.md)
You can play and record uncompressed audio data both synchronously and asynchronously. You can record audio data from a microphone type input device to a file.

- [Media Controller](media-controller-n.md)
You can communicate between the media controller server and client. The client can send requests to the server to modify the media, and the server can respond to the requests by modifying the media directly as requested. For the media controller feature to work, you must create both the client and server applications.

- [Media Conversions](media-conversions-n.md)
You can perform various media conversions through codecs. You can encode and decode video and audio data, and you can also use video transcoding features, such as multi-format codec and output format.

- [Media Handle Management](media-handle-n.md)
You can manage media handles to specify video or audio information. You can also include metadata and allocate a buffer to the heap or TBM surface.

- [Media Key Events](media-key-n.md)
You can handle media keys in your application to control multimedia playback. When the user clicks a media key, you can detect the event in the application and adjust the media playback accordingly.

- [Screen Mirroring](screen-mirroring-n.md) **in mobile applications only**
You can mirror the device screen and sound to another device wirelessly. Tizen supports the screen mirroring feature as a sink, which receives shared data from a source device that supports the Wi-Fi Display Technical Specification, and displays it.

- [Media Muxing](media-muxing-n.md)
You can mux encoded media into a multiplexed stream and parse multiplexed media streams. You can use various types of media streams, such as audio, video, and text.

- [Media Stream Playback](media-streams-n.md)
You can play and stream audio and video content. You can play audio and video content locally, or stream content from a server using IP protocol.

- [Media Stream Recording](stream-recorder-n.md)
You can record audio and video from a stream, and control the recording process through various settings. You can also access details, such as file names of the recordings.

- [Radio](radio-n.md)
You can allow the user to listen to the FM radio on the device. You can control the radio playback, scan for available frequencies, and change between found frequencies.

- [Camera](camera-n.md)
You can use the camera to preview and capture images. You can capture still images with the device's internal camera and keep images on your target device.