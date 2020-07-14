# Metadata

You can extract metadata information from multimedia files.

The main feature of the Metadata API is extraction of a metadata from a file. You can [extract metadata](#extract-metadata) from multimedia files using the `get()` method.


## Prerequisites

To access files using the Metadata API (in [mobile](../../api/latest/device_api/mobile/tizen/metadata.html), [wearable](../../api/latest/device_api/wearable/tizen/metadata.html), and [tv](../../api/latest/device_api/tv/tizen/metadata.html) applications), the application has to request storage privileges by adding the following privileges to the `config.xml` file:


```xml
<!-- for accessing internal storage only -->
<tizen:privilege name="http://tizen.org/privilege/mediastorage"/>
<!-- for accessing external storage only -->
<tizen:privilege name="http://tizen.org/privilege/externalstorage"/>
```


Additionally, to access files using the Metadata API (in [mobile](../../api/latest/device_api/mobile/tizen/metadata.html) and [wearable](../../api/latest/device_api/wearable/tizen/metadata.html) applications), the application has to request [proper storage permissions](../security/privacy-related-permissions.md) using the PPM API.


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
When all the needed metadata is extracted, the file handle needs to be released using the`release()` method:

   ```javascript
   fileHandle.release();
   ```


## Related Information
- Dependencies
  - Tizen 6.0 and Higher for Mobile
  - Tizen 6.0 and Higher for Wearable
  - Tizen 6.0 and Higher for TV
