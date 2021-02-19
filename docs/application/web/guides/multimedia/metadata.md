# Metadata

You can extract metadata information from multimedia files. Metadata is the information about multimedia files.

The main features of the Metadata API include:

- Extracting simple metadata informations

  You can [extract metadata](#extract-metadata) from multimedia files using the `get()` method.

- Extracting artwork of a multimedia file

  You can [extract artwork](#extract-artwork) from multimedia files using the `getArtwork()` method to get *Blob* object containing the artwork.

- Extracting thumbnail frame of a video file

  You can [extract thumbnail frame](#extract-thumbnail-frame) from video files using the `getThumbnailFrame()` method to get *Blob* object containing the frame.

- Extracting frame of a video file for a specified time

  You can [extract certain frame](#extract-certain-frame) from video files using the `getFrameAtTime()` method to get *Blob* object containing the frame.

- Extracting synchronized lyrics of a multimedia file

  You can [extract lyrics](#extract-lyrics) from multimedia files using the ` getSyncLyrics()` method to get timestamp and lyrics pairs.

## Prerequisites

To access files using the Metadata API (in [mobile](../../api/latest/device_api/mobile/tizen/metadata.html), [wearable](../../api/latest/device_api/wearable/tizen/metadata.html), and [tv](../../api/latest/device_api/tv/tizen/metadata.html) applications), the application has to request storage privileges by adding the following privileges to the `config.xml` file:


```xml
<!-- for accessing internal storage only -->
<tizen:privilege name="http://tizen.org/privilege/mediastorage"/>
<!-- for accessing external storage only -->
<tizen:privilege name="http://tizen.org/privilege/externalstorage"/>
```


Additionally, to access files using the Metadata API (in [mobile](../../api/latest/device_api/mobile/tizen/metadata.html) and [wearable](../../api/latest/device_api/wearable/tizen/metadata.html) applications), the application has to request [proper storage permissions](../security/privacy-related-permissions.md) using the PPM API (in [mobile](../../api/latest/device_api/mobile/tizen/ppm.html) and [wearable](../../api/latest/device_api/wearable/tizen/ppm.html) applications).


## Extract metadata

1. Create a file handle using the `createFileHandle()` method:

   ```javascript
   var filePath = "videos/sample_video.mp4";
   var fileHandle = tizen.metadata.createFileHandle(filePath);
   ```

2. When the file handle is properly created, metadata can be extracted:

   ```javascript
   console.log("Video duration is: " + fileHandle.get("DURATION") + " milliseconds");
   console.log("Video title is: " + fileHandle.get("TITLE"));
   ```

3. For better performance, the file handle does not release underlying resources after every metadata extraction. The data is decoded on the first extraction, which helps in speeding up the next metadata extractions.
When all the needed metadata is extracted, the file handle needs to be released using the `release()` method:

   ```javascript
   fileHandle.release();
   ```

## Extract artwork

1. Create a file handle using the `createFileHandle()` method. Your file needs to have an artwork included.

   ```javascript
   var filePath = "videos/sample.mp3";
   var fileHandle = tizen.metadata.createFileHandle(filePath);
   ```

2. When the file handle is properly created, artwork can be extracted:

   ```javascript
   var artwork = fileHandle.getArtwork();
   ```

3. *Blob* object can be easily shown in your application in html *&lt;img&gt;* tag

   ```javascript
   var elem = document.getElementById("blobImage");
   elem.src = URL.createObjectURL(artwork);
   ```

4. After use, remember to release fileHandle.

## Extract thumbnail frame

1. Create a file handle using the `createFileHandle()` method for a video file.

   ```javascript
   var filePath = "videos/sample_video.mp4";
   var fileHandle = tizen.metadata.createFileHandle(filePath);
   ```

2. When the file handle is properly created, thumbnail frame can be extracted:

   ```javascript
   var thumbnail = fileHandle.getThumbnailFrame();
   ```

3. *Blob* object can be easily shown in your application in html *&lt;img&gt;* tag

   ```javascript
   var elem = document.getElementById("blobImage");
   elem.src = URL.createObjectURL(thumbnail);
   ```

4. After use, remember to release fileHandle.

## Extract certain frame

1. Create a file handle using the `createFileHandle()` method for a video file.

   ```javascript
   var filePath = "videos/sample_video.mp4";
   var fileHandle = tizen.metadata.createFileHandle(filePath);
   ```

2. When the file handle is properly created, thumbnail frame can be extracted. You need to provide timestamp information (in milliseconds) and flag indicating to return frame from exact given time (true) or the user can only get the nearest <a href="https://en.wikipedia.org/wiki/Video_compression_picture_types">I-frame</a> of the video (false). Gathering nearest I-frame has better performance.

   ```javascript
   var timestamp = 2000;
   var returnExactFrame = true;
   var frame = fileHandle.getFrameAtTime(timestamp, returnExactFrame);
   ```

3. *Blob* object can be easily shown in your application in html *&lt;img&gt;* tag

   ```javascript
   var elem = document.getElementById("blobImage");
   elem.src = URL.createObjectURL(frame);
   ```

4. After use, remember to release fileHandle.

## Extract lyrics

1. Create a file handle using the `createFileHandle()` method. Lyrics need to be included in multimedia file as SYLT metadata tag. Supported formats of encoding are at least <a href="http://www.ietf.org/rfc/rfc2279.txt">UTF-8</a> and <a href="http://en.wikipedia.org/wiki/ISO/IEC_8859-1">ISO-8859-1</a>. Other formats can be ignored depending on the platform.

   ```javascript
   var filePath = "videos/sample.mp3";
   var fileHandle = tizen.metadata.createFileHandle(filePath);
   ```

2. When the file handle is properly created, one need to check how much lyrics are included.

   ```javascript
   var lyricsNum = fileHandle.get("SYNCLYRICS_NUM");
   ```

3. Lyrics then can be gathered and printed:

   ```javascript
   for (var i = 0; i < lyricsNum; ++i) {
      var lyrics = fileHandle.getSyncLyrics(i);
      console.log("Lyrics " + i + " (" + lyrics.timestamp  + "ms): " + lyrics.lyrics);
   }
   ```

4. After use, remember to release fileHandle.

## Related Information
- Dependencies
  - Tizen 6.0 and Higher for Mobile
  - Tizen 6.0 and Higher for Wearable
  - Tizen 6.0 and Higher for TV
