# JPEG File EXIF Information

You can access and modify EXIF information in a JPEG file (with the common `.jpg` extension).

The Exif API is mandatory for Tizen mobile, wearable, and TV profiles, which means that it is supported on all mobile, wearable, and TV devices. All mandatory APIs are supported on the Tizen Emulators.

The main features of the Exif API include:

- Loading EXIF information

  You can [retrieve EXIF information from a JPEG file](#loading-the-exif-data). You can also retrieve the thumbnail image of the file.

- Adding EXIF information

  You can [save EXIF information to  a JPEG file](#adding-exif-data) which currently has no EXIF information.

- Updating EXIF information

  You can [modify EXIF information in a JPEG file](#updating-the-exif-data) and save the file.

- Copying EXIF information

  You can [copy EXIF information from one JPEG file to another](#copying-the-exif-data).

## Loading the EXIF Data

Learning how to retrieve EXIF data from JPEG files is a useful content management skill:

1. To retrieve the EXIF data from an image file, you need the absolute URI of the file (for example `file:///opt/usr/media/Images/tizen.jpg`). The `tizen.filesystem.resolve()` and `toURI()` methods can be used to convert a virtual path to a URI.

   ```
   var fileURI = '';
   function resolveSuccess(file) {
       fileURI = file.toURI();
       console.log('Successfully resolved file: ' + fileURI);
   }

   function resolveFail(error) {
       console.log('resolve() error occurred: ' + error.name + ' with message: ' + error.message);
   }

   tizen.filesystem.resolve('images/tizen.jpg', resolveSuccess, resolveFail);
   ```

2. With a valid `File` object, use the `getExifInfo()` method of the `ExifManager` interface (in [mobile](../../api/latest/device_api/mobile/tizen/exif.html#ExifManager), [wearable](../../api/latest/device_api/wearable/tizen/exif.html#ExifManager), and [TV](../../api/latest/device_api/tv/tizen/exif.html#ExifManager) applications) and pass the URI to the method.

   ```
   function onSuccess(exifInfo) {
       console.log('Successfully got EXIF information object');
   }

   function onError(error) {
       console.log('Error occurred: ' + error.name + ' with message:' + error.message);
   }

   tizen.exif.getExifInfo(fileURI, onSuccess, onError);
   ```

   With a valid `exifInfo` object, you can access various `ExifInformation` attributes (in [mobile](../../api/latest/device_api/mobile/tizen/exif.html#ExifInformation), [wearable](../../api/latest/device_api/wearable/tizen/exif.html#ExifInformation), and [TV](../../api/latest/device_api/tv/tizen/exif.html#ExifInformation) applications), such as width, height, orientation, and flash.

3. To retrieve the EXIF thumbnail from the image:

   1. Resolve the input JPEG file:

      ```
      var fileURI = '';

      tizen.filesystem.resolve('images/tizen.jpg', resolveSuccess, resolveFail);
      ```

   2. Use the `getThumbnail()` method to retrieve the thumbnail:

      ```
      function onSuccess(thumbData) {
          console.log('Got thumbnail data from EXIF stored in JPEG file');
          if (thumbData) {
              var img = new Image();
              img.src = thumbData;
              document.body.appendChild(img);
         }
      }

      function onError(error) {
          console.log('Error occurred: ' + error.name + ' with message: ' + error.message);
      }

      function resolveSuccess(file) {
          fileURI = file.toURI();
          console.log('Successfully resolved file: ' + file.toURI());
          tizen.exif.getThumbnail(fileURI, onSuccess, onError);
      }
      ```

## Adding EXIF Data

Learning how to add EXIF data to JPEG files is a useful content management skill:

1. Create a new `ExifInformation` object (in [mobile](../../api/latest/device_api/mobile/tizen/exif.html#ExifInformation), [wearable](../../api/latest/device_api/wearable/tizen/exif.html#ExifInformation), and [TV](../../api/latest/device_api/tv/tizen/exif.html#ExifInformation) applications):

   ```
   var myNewExif = new tizen.ExifInformation();
   myNewExif.userComment = 'Photo taken on Charles Bridge in Prague';
   myNewExif.gpsLocation = new tizen.SimpleCoordinates(50.086447, 14.411856);
   ```

2. Resolve the virtual path to the output JPEG file and get the URI:

   ```
   var fileNoExifURI = '';
   function resolveSuccess(file) {
       fileNoExifURI = file.toURI();
       console.log('Successfully resolved file: ' + fileNoExifURI);
   }

   function resolveFail(error) {
       console.log('Error occurred: ' + error.name + ' with message: ' + error.message);
   }

   tizen.filesystem.resolve('images/image_without_exif.jpg', resolveSuccess, resolveFail);
   ```

3. When you have a valid URI to the file, set it in the `myNewExif` object and call the `saveExifInfo()` method of the  `ExifManager` interface (in [mobile](../../api/latest/device_api/mobile/tizen/exif.html#ExifManager), [wearable](../../api/latest/device_api/wearable/tizen/exif.html#ExifManager), and [TV](../../api/latest/device_api/tv/tizen/exif.html#ExifManager) applications):

   ```
   function onSaveSuccess() {
       console.log('Successfully saved EXIF information to JPEG file');
   }

   function onSaveError(error) {
       console.log('Error occurred:' + error.name + ' with message:' + error.message);
   }

   myNewExif.uri = fileNoExifURI;
   tizen.exif.saveExifInfo(myNewExif, onSaveSuccess, onSaveError);
   ```

## Updating the EXIF Data

Learning how to update EXIF data in JPEG files is a useful content management skill:

1. To update the EXIF data, load the `ExifInformation` object (in [mobile](../../api/latest/device_api/mobile/tizen/exif.html#ExifInformation), [wearable](../../api/latest/device_api/wearable/tizen/exif.html#ExifInformation), and [TV](../../api/latest/device_api/tv/tizen/exif.html#ExifInformation) applications) from the file and change the values of the object properties.

   You can remove information from the file by setting the property to `null`.

   ```
   function getSuccess(exifInfo) {
       exifInfo.orientation = 'FLIP_HORIZONTAL';
       exifInfo.userComment = 'Great times!';

       /* Remove basic GPS information */
       exifInfo.gpsLocation = null;
       exifInfo.gpsAltitude = null;
   }

   tizen.filesystem.resolve('images/photo.jpg', function(file) {
       tizen.exif.getExifInfo(file.toURI(), getSuccess);
   });
   ```

2. After updating the property values, use the `saveExifInfo()` method of the `ExifManager` interface (in [mobile](../../api/latest/device_api/mobile/tizen/exif.html#ExifManager), [wearable](../../api/latest/device_api/wearable/tizen/exif.html#ExifManager), and [TV](../../api/latest/device_api/tv/tizen/exif.html#ExifManager) applications) to save the changes to the file:

   ```
   function saveSuccess(exifInfo) {
       console.log('new EXIF saved');
   }

   tizen.exif.saveExifInfo(exifInfo, saveSuccess);
   ```

## Copying the EXIF Data

Learning how to copy EXIF data between JPEG files is a useful content management skill:

1. Get the `ExifInformation` object (in [mobile](../../api/latest/device_api/mobile/tizen/exif.html#ExifInformation), [wearable](../../api/latest/device_api/wearable/tizen/exif.html#ExifInformation), and [TV](../../api/latest/device_api/tv/tizen/exif.html#ExifInformation) applications) and resolve the output file, and then change the `sourceExifInfo.uri` attribute to point to the output JPEG file:

   ```
   var sourceExifInfo = null;

   function resolveOutSuccess(outFile) {
       console.log('Successfully resolved file: ' + outFile.toURI());
       sourceExifInfo.uri = outFile.toURI();
   }

   function resolveOutFail(error) {
       console.log('Error occurred: ' + error.name + ' with message: ' + error.message);
   }

   function onSuccess(exifInfo) {
       console.log('Successfully got EXIF information object');
       sourceExifInfo = exifInfo;
       tizen.filesystem.resolve('images/image_without_exif.jpg', resolveOutSuccess, resolveOutFail);
   }

   tizen.exif.getExifInfo(fileURI, onSuccess);
   ```

2. Use the `saveExifInfo()` method of the `ExifManager` interface (in [mobile](../../api/latest/device_api/mobile/tizen/exif.html#ExifManager), [wearable](../../api/latest/device_api/wearable/tizen/exif.html#ExifManager), and [TV](../../api/latest/device_api/tv/tizen/exif.html#ExifManager) applications) to save the changes in the output JPEG file:

   ```
   function onSaveSuccess() {
       console.log('Successfully saved EXIF information to JPEG file');
   }

   function onSaveError(error) {
       console.log('Error occurred:' + error.name + ' with message:' + error.message);
   }

   function resolveOutSuccess(outFile) {
       console.log('Successfully resolved file: ' + outFile.toURI());
       sourceExifInfo.uri = outFile.toURI();
       tizen.exif.saveExifInfo(sourceExifInfo, onSaveSuccess, onSaveError);
   }
   ```

## Related Information
* Dependencies   
   - Tizen 2.4 and Higher for Mobile
   - Tizen 2.3.1 and Higher for Wearable
   - Tizen 3.0 and Higher for TV
