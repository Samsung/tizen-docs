# Camera

You can use the camera features in the Tizen wearable Web applications.

This feature is supported in wearable applications only.

The main features of the Camera API (Tizen Extension) API include:

- Accessing the camera device    

  You can [access the camera device](#accessing-the-camera-device) retrieving the media stream from the camera.

- Managing the camera    

  You can [manage the camera features](#managing-the-camera) in many ways:

  - You can record videos and capture images.
  - You can access and set the camera settings, such as the file name for the recorded video or captured image.

- Deallocating the camera preview stream    

  You can [deallocate the camera preview stream resources](#deallocating-the-camera-preview-stream) when the application is invisible so that the preview stream can be assigned to another Web application.

## Accessing the Camera Device

To take advantage of the camera features, you must learn to access the camera device:

1. Access the camera with the stream that you can receive from the `getUserMedia()` method. The second parameter for that method is an event handler that is triggered when the stream is successfully retrieved.

   ```
   var stream;
   navigator.webkitGetUserMedia({video: true, audio: false}, gotStreamCallback,
                                noStreamCallback);
   function gotStream(rStream) {
       stream = rStream;
   }
   ```

2. Use the received stream as the first parameter for the `createCameraControl()` method, which returns the `cameraControl` object. The `createCameraControl()` method is a member object of `tizCamera` from the navigator.

   ```
   navigator.tizCamera.createCameraControl(stream, gotCameraCallback, noCameraCallback);
   ```

3. You can use the `cameraControl` in the success event handler of the `createCameraControl()` method, where it is provided as a parameter:

   ```
   function gotCameraCallback(cameraControl) {}
   ```

## Managing the Camera

To take advantage of the camera features, you must learn to manage the camera:

- You can record videos with the `cameraControl` object.   
  Use the `start()` to start the recording, and the `stop()` method to stop the recording:

  ```
  cameraControl.recorder.start(recordingStartSuccess, recordingStartError);
  cameraControl.recorder.stop(recordingStopSuccess, recordingStopError);
  ```

- Use the `takePicture()` method to capture an image and write it in a file:

  ```
  cameraControl.image.takePicture(takePictureSuccess, takePictureError);
  ```

- Use the `applySettings()` method to modify the camera settings (to set the file name of the recorded video or captured image):

  ```
  var recordingSetting = {
      fileName: 'sample.3gp';
  }
  cameraControl.recorder.applySettings(recordingSetting,
                                       recorderSettingSuccessCallback,
                                       recorderSettingErrorCallback);
  ```

> **Note**  
> If a setting cannot be set, the error callback is called to resolve the issue.

## Deallocating the Camera Preview Stream

To take advantage of the camera features, you must learn to deallocate the camera preview stream resources when the application is invisible, so that the preview stream can be assigned to another application:

1. Access the camera preview stream using the `getUserMedia()` method:

   ```
   function initCameraPreview() {
       navigator.webkitGetUserMedia({video: true, audio: false},
                                    onPreviewStream,
                                    onPreviewStreamError);
   }

   function onPreviewStream(stream) {
       cameraStream = stream;
   }
   ```

2. Use the `onVisibilityChange()` event listener to detect changes in the visibility state of the application. When the application becomes invisible, the `cameraStream.stop()` method is called to release the preview stream. When the application becomes visible again, the preview stream is re-initialized.

   ```
   function onVisibilityChange() {
       if (document.visibilityState !== 'visible') {
           cameraStream.stop();
       } else {
           initCameraPreview();
       }
   }
   ```

## Related Information
* Dependencies   
   - Tizen 2.3.1 and Higher for Wearable
