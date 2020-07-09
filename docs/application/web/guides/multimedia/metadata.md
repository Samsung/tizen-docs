# Metadata

You can extract metadata information from multimedia files.

The main features of the Metadata API include:

- Extraction of a metadata from a file
  You can [extract metadata](#extract-metadata) from multimedia files using `get()` method.


## Prerequisites

To access files using the Metadata API (in [mobile](../../api/latest/device_api/mobile/tizen/metadata.html), [wearable](../../api/latest/device_api/wearable/tizen/metadata.html)), the application has to request [proper storage permissions](../security/privacy-related-permissions.md).

## Extract metadata

1. Create a file handle using `createFileHandle()` method:

   ```javascript
   var filePath = "videos/sample_video.mp4";
   var fileHandle = tizen.metadata.createFileHandle(filePath);
   ```

2. When the file handle is properly created metadata can be extracted:

   ```javascript
   console.log("Video duration is: " + fileHandle.get("DURATION") + " milliseconds");
   console.log("Video title is: " + fileHandle.get("TITLE"));
   ```

3. For better performance, FileHandle does not release underlying resources after every metadata extraction. On first extraction, data is decoded, thanks to that next metadata extractions are faster.
When all needed metadata are extracted, handle need to be released using `release()` method:

   ```javascript
   fileHandle.release();
   ```


## Related Information
- Dependencies
  - Tizen 6.0 and Higher for Mobile
  - Tizen 6.0 and Higher for Wearable
  - Tizen 6.0 and Higher for TV
