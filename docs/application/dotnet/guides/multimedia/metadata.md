# Metadata


You can access, add, and edit metadata in media files.

The main metadata features include the following:

-   Metadata editing (Deprecated since API Level 12)

    You can [edit the metadata](#editing) of several popular audio formats using the metadata editor. You can add and remove album art, or update the information for the audio file.

    The metadata editor supports editing the [metadata](#attribute) of audio files in the MP3 and MP4 file formats. Image and video file editing is not supported.

-   Metadata extraction

    Media files, such as MP3 and MP4 files, contain [extractable metadata](#attribute2). You can [retrieve metadata](#metadata_extractor) from such media files with the metadata extractor.

    The metadata extractor can be used with video and audio files only. It is not supported for image files.

-   MIME type handling

    You can [get the MIME type](#mime_type) for a file extension and [get a list of file extensions](#mime_extension) associated, for example, with an image or the JPEG MIME type.

## Prerequisites

To enable your application to use the metadata functionality, proceed as follows:

1.  To access media files on the device, the application has to request permission by adding the following privileges to the `tizen-manifest.xml` file:

    ```XML
    <privileges>
       <!--To access media storage-->
       <privilege>http://tizen.org/privilege/mediastorage</privilege>
       <!--To access external storage-->
       <privilege>http://tizen.org/privilege/externalstorage</privilege>
    </privileges>
    ```

2.  To use the methods and properties of the [Tizen.Multimedia.MetadataEditor](/application/dotnet/api/TizenFX/latest/api/Tizen.Multimedia.MetadataEditor.html) and [Tizen.Multimedia.MetadataExtractor](/application/dotnet/api/TizenFX/latest/api/Tizen.Multimedia.MetadataExtractor.html) classes, include the [Tizen.Multimedia](/application/dotnet/api/TizenFX/latest/api/Tizen.Multimedia.html) namespace in your application:

    ```csharp
    using Tizen.Multimedia;
    ```

<a name="editing"></a>
## Edit metadata and artwork (Deprecated since API Level 12)
To add and edit metadata in an audio file, proceed as follows:

1.  Create an instance of the [Tizen.Multimedia.MetadataEditor](/application/dotnet/api/TizenFX/latest/api/Tizen.Multimedia.MetadataEditor.html) class with the path of the file to be edited. Make sure you have access to the file whose metadata and artwork you want to edit:

    ```csharp
    var metadataEditor = new MetadataEditor(mediaPath);
    ```

2.  Edit the metadata by using various properties of the `Tizen.Multimedia.MetadataEditor` class:

    ```csharp
    /// Set the title of the audio file
    metadataEditor.Title = "My Song";

    /// Set the artist of the audio file
    metadataEditor.Artist = "Artist";
    ```

3.  To add images to the audio file:
    -   Add an image to the audio file using the `AddPicture()` method of the `Tizen.Multimedia.MetadataEditor` class with an image path containing the artwork:

        The image to be added must be in JPEG or PNG format. The image is added to the first free index position. You can add multiple image files to the same audio file.

        ```csharp
        metadataEditor.AddPicture(artworkpath);
        ```

    -   To remove an image from the file, use the `RemovePicture()` method with the index number of image file to be removed:

        ```csharp
        int index = 5;
        metadataEditor.RemovePicture(index);
        ```

    -   To retrieve the number of images added to the file, use the `PictureCount` property of the `Tizen.Multimedia.MetadataEditor` class and to retrieve a specific image, use the `GetPicture()` method with the index number of the desired image:

        ```csharp
        /// Get the number of images associated with the file
        int pictureCount = metadataEditor.PictureCount;

        /// Retrieve a specific image
        Artwork artwork = metadataEditor.GetPicture(pictureCount - 1);
        ```

4.  Apply the metadata and artwork changes to the audio file using the `Commit()` method:

    ```csharp
    metadataEditor.Commit();
    ```

<a name="metadata_extractor"></a>
## Retrieve metadata

To retrieve metadata from a file, proceed as follows:

1.  Create an instance of the [Tizen.Multimedia.MetadataExtractor](/application/dotnet/api/TizenFX/latest/api/Tizen.Multimedia.MetadataExtractor.html) class and pass the path of the file or buffer whose metadata you want to retrieve as a parameter:
    -   Create a `Tizen.Multimedia.MetadataExtractor` instance with a file path parameter:

        ```csharp
        var metadataExtractor = new MetadataExtractor(mediaPath);
        ```

    - Create a `Tizen.Multimedia.MetadataExtractor` instance with a buffer parameter:

        ```csharp
        var buffer = File.ReadAllBytes(mediaPath);
        var metadataExtractor = new MetadataExtractor(buffer);
        ```

2.  Retrieve the metadata:
    -   Retrieve the metadata from the file by using the `GetMetadata()` method of the `Tizen.Multimedia.MetadataExtractor` class, which returns an instance of the [Tizen.Multimedia.Metadata](/application/dotnet/api/TizenFX/latest/api/Tizen.Multimedia.Metadata.html) class containing all the metadata of the file.

        The following example retrieves the artist and title of the media file:

        ```csharp
        /// Get Artist and Title metadata of the file
        Metadata metadata = metadataExtractor.GetMetadata();

        Tizen.Log.Info(LogTag, "Artist: " + metadata.Artist);
        Tizen.Log.Info(LogTag, "Title: " + metadata.Title);
        ```

        You can retrieve other metadata in the same way.

    -   For an audio file, retrieve the artwork from the file using the `GetArtwork()` method, which returns an instance of the [Tizen.Multimedia.Artwork](/application/dotnet/api/TizenFX/latest/api/Tizen.Multimedia.Artwork.html) class containing the encoded artwork image and the MIME type of the artwork:

        ```csharp
        var artWork = metadataExtractor.GetArtwork();
        ```

    -   For an audio file, retrieve the synchronized lyrics from the file using the `GetSyncLyrics()` method with an index number as a parameter.

        To retrieve the synchronized lyrics index number, use the `SyncLyricsCount` property of the `Tizen.Multimedia.Metadata` class.

        The following example code retrieves the synchronized lyrics from index number 1 and prints the time information and lyrics:

        ```csharp
        /// Retrieve the synchronized lyrics of the file
        Metadata metadata = metadataExtractor.GetMetadata();

        SyncLyrics syncLyrics = metadataExtractor.GetSyncLyrics(1);

        Tizen.Log.Info(LogTag, $"Lyrics = {syncLyrics.Lyrics}, Timestamp = {syncLyrics.Timestamp}");
        ```

    - For a video file, retrieve frames from the file in one of the following ways:
        -   To retrieve a frame without specifying the time when the frame appears, use the `GetVideoThumbnail()` method:

            ```csharp
            byte[] thumbnail = metadataExtractor.GetVideoThumbnail();
            ```

        - To retrieve a frame with a timestamp, use the `GetFrameAt()` method with the timestamp in milliseconds. To capture the exact frame desired, the second parameter must be set to `true`, otherwise, the method returns the I-frame nearest to the desired timestamp:

            ```csharp
            byte[] videoFrame = metadataExtractor.GetFrameAt(100, true);
            ```

<a name="mime_type"></a>
## Retrieve the MIME type for a file extension

To retrieve the MIME type for a given file extension, use the `GetMimeType()` method of the [Tizen.Content.MimeType.MimeUtil](/application/dotnet/api/TizenFX/latest/api/Tizen.Content.MimeType.MimeUtil.html) class.

If the given file extension is not associated with any specific file format, the MIME type is `application/octet-stream`:

```csharp
string mimeType = MimeUtil.GetMimeType("png");
```

<a name="mime_extension"></a>
## Retrieve file extensions for a MIME type

To retrieve the file extensions for a given MIME type, use `GetFileExtension()` method of the [Tizen.Content.MimeType.MimeUtil](/application/dotnet/api/TizenFX/latest/api/Tizen.Content.MimeType.MimeUtil.html) class:

```csharp
/// Retrieve a list of file extensions for a given MIME type
IEnumerable<string> ext = MimeUtil.GetFileExtension("video/mpeg");
foreach(string ex in ext)
{
    Tizen.Log.Info(LogTag, "Extension = " + ex);
}
```

<a name="attribute"></a>
## Editable metadata attributes

The following table lists the metadata you can edit.

**Table: Editable metadata attributes**

| Attribute     | Description                        | Property or method of the Tizen.Multimedia.MetadataEditor class |
|-------------|----------------------------------|----------------------------------------|
| Artist        | Artist of the audio content        | `Artist` (Deprecated since API Level 12) |
| Title         | Title of the audio content         | `Title` (Deprecated since API Level 12) |
| Album         | Album of the audio content         | `Album` (Deprecated since API Level 12)  |
| Genre         | Genre of the audio content         | `Genre` (Deprecated since API Level 12) |
| Composer        | Composer of the audio content        | `Composer` (Deprecated since API Level 12) |
| Copyright     | Copyright of the audio content     | `Copyright` (Deprecated since API Level 12) |
| Date          | Date of the audio content          | `Date` (Deprecated since API Level 12) |
| Description   | Description of the audio content   | `Description` (Deprecated since API Level 12) |
| Comment       | Comment of the audio content       | `Comment` (Deprecated since API Level 12) |
| TrackNumber   | Track number of the audio content  | `TrackNumber` (Deprecated since API Level 12) |
| Picture       | Picture of the audio content       | `PictureCount` (Deprecated since API Level 12)<br>`GetPicture() (Deprecated since API Level 12)`<br>`AddPicture() (Deprecated since API Level 12)`<br>`RemovePicture()` (Deprecated since API Level 12) |
| Conductor     | Conductor of the audio content     | `Conductor` (Deprecated since API Level 12) |
| Unsync lyrics | Unsync lyrics of the audio content | `UnsyncLyrics` (Deprecated since API Level 12) |

<a name="attribute2"></a>
## Extractable metadata attributes

The following table lists the extractable metadata.

The metadata is available with the properties and methods of the [Tizen.Multimedia.AudioMetadata](/application/dotnet/api/TizenFX/latest/api/Tizen.Multimedia.AudioMetadata.html), [Tizen.Multimedia.Metadata](/application/dotnet/api/TizenFX/latest/api/Tizen.Multimedia.Metadata.html), [Tizen.Multimedia.MetadataExtractor](/application/dotnet/api/TizenFX/latest/api/Tizen.Multimedia.MetadataExtractor.html), [Tizen.Multimedia.SyncLyrics](/application/dotnet/api/TizenFX/latest/api/Tizen.Multimedia.SyncLyrics.html), and [Tizen.Multimedia.VideoMetadata](/application/dotnet/api/TizenFX/latest/api/Tizen.Multimedia.VideoMetadata.html) classes.

**Table: Metadata extractor attributes**

| Attribute            | Description                            | Property or method                       |
|--------------------|--------------------------------------|----------------------------------------|
| Duration             | Duration of the content                | `Metadata.Duration`                      |
| Video bit rate       | Bit rate of the video content          | `VideoMetadata.BitRate`                  |
| Video FPS            | FPS of the video content               | `VideoMetadata.Fps`                      |
| Video codec          | Codec of the video content             | `VideoMetadata.Codec`                    |
| Video stream count   | Number of streams of the video content | `VideoMetadata.StreamCount`              |
| Video resolution     | Resolution of the video content        | `VideoMetadata.Width`<br>`VideoMetadata.Height` |
| Audio bit rate       | Bit rate of the audio content          | `AudioMetadata.BitRate`                  |
| Audio channels       | Channel of the audio content           | `AudioMetadata.Channels`                 |
| Audio sample rate    | Sample rate of the audio content       | `AudioMetadata.SampleRate`               |
| Audio bit per sample | Bit per sample of the audio content    | `AudioMetadata.BitPerSample`             |
| Audio codec          | Codec of the audio content             | `AudioMetadata.Codec`                    |
| Audio stream count   | Number of streams of the audio content | `AudioMetadata.StreamCount`              |
| Artist               | Artist of the content                  | `Metadata.Artist`                        |
| Title                | Title of the content                   | `Metadata.Title`                         |
| Album                | Album of the content                   | `Metadata.Album`                         |
| Album artist         | Album artist of the content            | `Metadata.AlbumArtist`                   |
| Genre                | Genre of the content                   | `Metadata.Genre`                         |
| Composer               | Composer of the content                  | `Metadata.Composer`                        |
| Copyright            | Copyright of the content               | `Metadata.Copyright`                     |
| Date                 | Date of the content                    | `Metadata.Date`                          |
| Description          | Description of the content             | `Metadata.Description`                   |
| Comment              | Comment about the content              | `Metadata.Comment`                       |
| TrackNumber          | Track number of the content            | `Metadata.TrackNumber`                   |
| Classification       | Classification of the content          | `Metadata.Classification`                |
| Rating               | Rating of the content                  | `Metadata.Rating`                        |
| Longitude            | Longitude of the content               | `Metadata.Longitude`                     |
| Latitude             | Latitude of the content                | `Metadata.Latitude`                      |
| Altitude             | Altitude of the content                | `Metadata.Altitude`                      |
| Conductor            | Conductor of the content               | `Metadata.Conductor`                     |
| Unsync lyrics        | Asynchronous lyrics of the content     | `Metadata.UnsyncLyrics`                  |
| Sync lyrics          | Synchronous lyrics of the content      | `Metadata.SyncLyricsCount`<br>`MetadataExtractor.GetSyncLyrics()`<br>`SyncLyrics.Lyrics`<br>`SyncLyrics.Timestamp` |
| Recorded date        | Recorded date of the content           | `Metadata.DateRecorded`                  |
| Duration             | Orientation of the content             | `Metadata.Rotation`                      |


## Related information
* Dependencies
  -   Tizen 4.0 and Higher
