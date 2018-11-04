# Multimedia


Multimedia features introduce how you can handle multimedia resources, such as media files, images, audio, video, camera and radio.

You can use the following multimedia features in your native applications:

- [Media Content and Metadata](media-content-metadata.md)

  You can manage and search for various media content on the device, such as media files, bookmarks, albums, and playlists. You can also access the MIME type information, and extract and edit the metadata of the media files.

- [Image Editing](image-edit.md)

  You can view and process bitmap images in JPEG format. The processing includes decoding, encoding, converting, and compressing images.

- [Thumbnail Images](thumbnail-images.md)

  You can create a thumbnail from an input media file. The thumbnail can be a video or image, but not an audio file. You can also customize the size of the thumbnail.

- [Visual Detection and Recognition](media-vision.md)

  You can detect or generate various barcodes. You can also track how faces or image objects move in consecutive camera preview images as well as perceive faces or objects in still images.

- [Media Playback](media-playback.md)

  You can manage the playback of different media file types. You can play audio and video files, and tones. You can also manage the state of the media player.

- [Media Recording](media-recording.md)

  You can manage the recording of different media file types. You can record audio data to a file and generate compressed video files using video data from a camera and audio data from an audio input device.

- [Raw Audio Playback and Recording](raw-audio.md)

  You can play and record uncompressed audio data both synchronously and asynchronously. You can record audio data from a microphone type input device to a file.

- [Sound Manager](sound-manager.md)

  You can control the output volume of a specific volume type (aka sound type). You can define which stream type is used for a playback or recording handle in your application. You can manage sound conflict senarios by using stream focus. You can also query for various information related to the connected sound devices, for example, type, name, id, direction and state.

- [Sound Pools](sound-pool.md)

  You can use sound pools, which are basically collections of sounds. You can load multiple sound sources to a sound pool and manage their playback as a group.

- [OpenAL](openal.md)

  You can use OpenAL software interface to audio hardware for a variety of audio playback tasks (such as sound effects in games). You can create a context, request a source and buffer, and control the audio stream with OpenAL.

- [Media Controller](media-controller.md)

  You can communicate between the media controller server and client. The client can send requests to the server to modify the media, and the server can respond to the requests by modifying the media directly as requested. For the media controller feature to work, you must create both the client and server applications.

- [Media Conversions](media-conversions.md)

  You can perform various media conversions through codecs. You can encode and decode video and audio data, and you can also use video transcoding features, such as multi-format codec and output format.

- [Media Handle Management](media-handle.md)

  You can manage media handles to specify video or audio information. You can also include metadata and allocate a buffer to the heap or TBM surface.

- [Media Key Events](media-key.md)

  You can handle media keys in your application to control multimedia playback. When the user clicks a media key, you can detect the event in the application and adjust the media playback accordingly.

- [Screen Mirroring](screen-mirroring.md) **in mobile applications only**

  You can mirror the device screen and sound to another device wirelessly. Tizen supports the screen mirroring feature as a sink, which receives shared data from a source device that supports the Wi-Fi Display Technical Specification, and displays it.

- [Media Muxing](media-muxing.md)

  You can mux encoded media into a multiplexed stream and parse multiplexed media streams. You can use various types of media streams, such as audio, video, and text.

- [Media Stream Playback](media-streams.md)

  You can play and stream audio and video content. You can play audio and video content locally, or stream content from a server using IP protocol.

- [Media Stream Recording](stream-recorder.md)

  You can record audio and video from a stream, and control the recording process through various settings. You can also access details, such as file names of the recordings.

- [Radio](radio.md)

  You can allow the user to listen to the FM radio on the device. You can control the radio playback, scan for available frequencies, and change between found frequencies.

- [Camera](camera.md)

  You can use the camera to preview and capture images. You can capture still images with the device's internal camera and keep images on your target device.

## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
