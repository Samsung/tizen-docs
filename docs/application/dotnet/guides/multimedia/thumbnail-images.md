# Thumbnail Images


You can create a thumbnail from an input media file.

The main features of the `Tizen.Multimedia.Util.ThumbnailExtractor` class include:

-   Video and image thumbnails

    You can [create thumbnails](#get_thumbnail) from video and image files. Audio files are not supported.

-   Custom size

    You can create the thumbnail using any size you like. The `Tizen.Multimedia.Util.ThumbnailExtractor` class outputs the results according to the size you have set. This means that the thumbnail can be generated even if the output size differs from the original aspect ratio.

The requested thumbnail is provided as a raw data type with the BGRA color space, not a JPG or PNG file. You can display the thumbnail on the screen as is. If you want to save the thumbnail to a file, you must encode it.

## Prerequisites

To use the methods and properties of the [Tizen.Multimedia.Util.ThumbnailExtractor](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Multimedia.Util.ThumbnailExtractor.html) class, include the [Tizen.Multimedia.Util](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Multimedia.Util.html) namespace in your application:

```
using Tizen.Multimedia.Util;
```


> **Note**   
> The input media file can be common content in the device storage (internal or external) or private content in your application data.

<a name="get_thumbnail"></a>
## Extracting a Thumbnail

To extract a thumbnail from a file, use the `ExtractAsync()` method of the [Tizen.Multimedia.Util.ThumbnailExtractor](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Multimedia.Util.ThumbnailExtractor.html) class:

```
async Task Extract(string testImagePath)
{
    ThumbnailExtractionResult result = await ThumbnailExtractor.ExtractAsync(testImagePath, new Size(512, 288));

    Tizen.Log.Info("Data size is " + result.RawData.Length);
}
```

> **Note**   
> If you do not set the size, a default size of 320 x 240 is used.


## Related Information
* Dependencies
  -   Tizen 4.0 and Higher
