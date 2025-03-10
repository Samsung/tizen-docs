# Thumbnail Images


You can create a thumbnail from an input media file.

The main features of the `Tizen.Multimedia.Util.ThumbnailExtractor` class include the following:

-   Video and image thumbnails

    You can [create thumbnails](#extract-a-thumbnail-synchronously) synchronously from video and image files. Audio files are not supported.

-   Custom size

    You can create the thumbnail using any size you like. The `Tizen.Multimedia.Util.ThumbnailExtractor` class outputs the results according to the size you have set. This means that the thumbnail can be generated even if the output size differs from the original aspect ratio.

The requested thumbnail is provided as a raw data type with the BGRA color space, not a JPG or PNG file. You can display the thumbnail on the screen as is. If you want to save the thumbnail to a file, you must encode it.

## Prerequisites

To use the methods and properties of the [Tizen.Multimedia.Util.ThumbnailExtractor](/application/dotnet/api/TizenFX/latest/api/Tizen.Multimedia.Util.ThumbnailExtractor.html) class, include the [Tizen.Multimedia.Util](/application/dotnet/api/TizenFX/latest/api/Tizen.Multimedia.Util.html) namespace in your application:

```csharp
using Tizen.Multimedia.Util;
```


> [!NOTE]
> The input media file can be common content in the device storage (internal or external) or private content in your application data.


## Extract a thumbnail synchronously

1.  To extract a thumbnail synchronously from a file, use the `Extract(string path, Size size)` or `Extract(string path)` method of the [Tizen.Multimedia.Util.ThumbnailExtractor](/application/dotnet/api/TizenFX/latest/api/Tizen.Multimedia.Util.ThumbnailExtractor.html) class:

```csharp
void Extract(string testImagePath, Size size)
{
    ThumbnailExtractionResult result = ThumbnailExtractor.Extract(testImagePath, size);

    Log.Info("Util", "Data size is " + result.RawData.Length);
}
```

2.  To extract a thumbnail synchronously from a file and save it to a file, use the `Extract(string path, Size size, string resultThumbnailPath)` or `Extract(string path, string resultThumbnailPath)` method of the [Tizen.Multimedia.Util.ThumbnailExtractor](/application/dotnet/api/TizenFX/latest/api/Tizen.Multimedia.Util.ThumbnailExtractor.html) class:
```csharp
void Extract(string testImagePath, Size size, string resultPath)
{
    ThumbnailExtractor.Extract(testImagePath, size, resultPath);

    if (File.Exists(resultPath))
    {
        Log.Error("Util", "Failed to extract thumbnail image");
    }
}
```

> [!NOTE]
> If you do not set the size, a default size of 320 x 240 is used.


## Related information
* Dependencies
  -   Tizen 4.0 and Higher