# Image Recognition and Tracking


You can extract features of an image object and recognize it from specific images. You can also track the image object in your application.

The main image recognition and tracking features include:

-   Recognizing images

    You can [recognize image objects](#recognize) in specific images, and extract image object features.

-   Tracking images

    You can [track image objects](#track) using the camera preview images and a specific image tracking model.

## Prerequisites

To enable your application to use the image recognition and tracking functionality:

1.  Install the NuGet packages for Media Vision and Camera.
2.  To use the methods and properties of the image recognition and tracking classes and to handle camera preview, include the [Tizen.Multimedia](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Multimedia.html) and [Tizen.Multimedia.Vision](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Multimedia.Vision.html) namespaces in your application:

    ```
    using Tizen.Multimedia;
    using Tizen.Multimedia.Vision;
    ```

3.  Define the configuration settings:
    -   For configuring image object and feature extraction, create an instance of the [Tizen.Multimedia.Vision.ImageFillConfiguration](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Multimedia.Vision.ImageFillConfiguration.html) class and set its attributes accordingly:

        ```
        static ImageFillConfiguration configFill = new ImageFillConfiguration();

        /// Set the scale factor of the image being recognized
        configFill.ObjectScaleFactor = 1.2;

        /// Set the maximum amount of image key points to be detected
        configFill.ObjectMaxKeyPoints = 1000;
        ```

    -   For image recognition, create an instance of the [Tizen.Multimedia.Vision.ImageRecognitionConfiguration](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Multimedia.Vision.ImageRecognitionConfiguration.html) class and set its attributes accordingly:

        ```
        static ImageRecognitionConfiguration configRecog = new ImageRecognitionConfiguration();

        /// Set the scene scale factor
        configRecog.SceneScaleFactor = 1.2;

        /// Set the maximum amount of key points to be detected in a scene
        configRecog.SceneMaxKeyPoints = 3000;
        ```

    -   For image tracking, create an instance of the [Tizen.Multimedia.Vision.ImageTrackingConfiguration](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Multimedia.Vision.ImageTrackingConfiguration.html) class and set its attributes accordingly:

        ```
        static ImageTrackingConfiguration configTrack = new ImageTrackingConfiguration();

        /// Set the history amount
        configTrack.HistoryAmount = 5;

        /// Set the expected offset
        configTrack.ExpectedOffset = 0.5;
        ```

<a name="recognize"></a>
## Recognizing Images

To recognize an image (the target) in another (the scene):

1.  To prepare the target image being recognized, create an instance of the [Tizen.Multimedia.Vision.MediaVisionSource](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Multimedia.Vision.MediaVisionSource.html) class with raw image buffer data and its corresponding width, height, and color space parameters:

    ```
    /// Assume that there is a decoded raw data buffer of the byte[] type, and
    /// it has 640x480 resolution with an RGB888 color space

    MediaVisionSource sourceTarget = new MediaVisionSource(bytes, width, height, ColorSpace.Rgb888);
    ```

2.  Create an instance of the [Tizen.Multimedia.Vision.ImageObject](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Multimedia.Vision.ImageObject.html) class and use its `Fill()` method to fill it with the `Tizen.Multimedia.Vision.MediaVisionSource` instance:

    ```
    static ImageObject obj = new ImageObject();

    obj.Fill(sourceTarget);

    /// If you want to apply configuration options to the fill operation:
    /// obj.Fill(sourceTarget, configFill);

    /// If you want a specific label for the ImageObject instance, set it manually
    /// Otherwise the label automatically increments with each fill operation
    obj.SetLabel(1);
    ```

3.  To prepare the scene where the target image is to be recognized, create a `Tizen.Multimedia.Vision.MediaVisionSource` instance which stores the scene:

    ```
    /// Assume that there is a decoded raw data buffer of the byte[] type, and
    /// it has 640x480 resolution with an RGB888 color space

    MediaVisionSource sourceScene  = new MediaVisionSource(bytes, width, height, ColorSpace.Rgb888);
    ```

4.  To recognize the target inside the scene, use the `RecognizeAsync()` method of the [Tizen.Multimedia.Vision.ImageRecognizer](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Multimedia.Vision.ImageRecognizer.html) class:

    ```
    /// You can recognize multiple targets
    ImageObject[] targets = new ImageObject[1] (obj);

    var results = await ImageRecognizer.RecognizeAsync(sourceScene, targets);

    foreach (ImageRecognitionResult imageResult in results)
    {
        if (imageResult.Success)
            Log.info(LogUtils.TAG, imageResult, Region.ToString();
        else
            Log.info(LogUtils.Tag, "ImageRecognition: " + imageResult.Success.ToString());
    }
    ```

<a name="track"></a>
## Tracking Images

To track images:

1.  To prepare the camera and create an image tracking model:
    1.  Define a camera preview event handler for the `Preview` event of the [Tizen.Multimedia.Camera](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Multimedia.Camera.html) class and create an instance of that class:

        ```
        /// Define a camera preview event handler
        static void PreviewCallback(object sender, PreviewEventArgs e)
        {
            PreviewData preview = e.Preview;

            SinglePlane singlePlane = (SinglePlane)preview.Plane;
            if (preview.Format == CameraPixelFormat.Rgb888)
            {
                MediaVisionSource source = new MediaVisionSource(singlePlane.Data, preview.width, preview.height, ColorSpace.Rgb888);
            }
        }

        /// Create the Tizen.Multimedia.Camera instance
        static Camera camera = null;
        try
        {
            camera = new Camera(CameraDevice.Rear);
        }
        catch (NotSupportedException)
        {
            Log.Info("Image Tracking Sample", "NotSupported");
        }
        ```

    2.  Set the camera display, register the camera preview event handler, and start the camera preview with the `StartPreview()` method:

        ```
        /// Set the camera display
        camera.Display = new Display(new Window("Preview"));

        /// Register the camera preview event handler
        camera.Preview += PreviewCallback;

        IList previewFormats = camera.Feature.SupportedPreviewPixelFormats.ToList();
        foreach (CameraPixelFormat previewFormat in previewFormats)
        {
            camera.Setting.PreviewPixelFormat = previewFormat;
            break;
        }

        /// Start the camera preview
        camera.StartPreview();
        ```

    3.  Create the image tracking model as an instance of the [Tizen.Multimedia.Vision.ImageTrackingModel](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Multimedia.Vision.ImageTrackingModel.html) class:

        ```
        static ImageTrackingModel model = new ImageTrackingModel();
        ```

2.  Create a target image as an instance of the [Tizen.Multimedia.Vision.MediaVisionSource](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Multimedia.Vision.MediaVisionSource.html) class.

    Create an instance of the [Tizen.Multimedia.Vision.ImageObject](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Multimedia.Vision.ImageObject.html) class and use its `Fill()` method to fill it with the target image.

    ```
    static MediaVisionSource sourceTarget = new MediaVisionSource(bytes, width, height, ColorSpace.Rgb888);

    static ImageObject obj = new ImageObject();
    obj.Fill(sourceTarget);
    ```

3.  Set the target of the image tracking model with the `SetTarget()` method of the `Tizen.Multimedia.Vision.ImageTrackingModel` class, which takes the `Tizen.Multimedia.Vision.ImageObject` instance as its parameter:

    ```
    model.SetTarget(obj)
    ```

4.  To track the target, use the `TrackAsync()` method of the [Tizen.Multimedia.Vision.ImageTracker](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Multimedia.Vision.ImageTracker.html) class:

    ```
    /// Assume that "frames" contains a sequence of decoded images as
    /// Tizen.Multimedia.Vision.MediaVisionSource instances

    foreach (MediaVisionSource frame in frames)
    {
        var result = await ImageTracker.TrackAsync(frame, model);

        /// If you want to apply configuration options to the tracking operation:
        /// var result = await ImageTracker.TrackAsync(frame, model, configTrack);

        if (result == null)
        {
            continue;
        }
    }
    ```

5.  When image tracking is no longer needed, deregister the camera preview event handler, stop the camera preview, and destroy the camera instance:

    ```
    camera.Preview -= PreviewCallback;

    camera.StopPreview();
    camera.Dispose();
    ```


## Related Information
* Dependencies
  -   Tizen 4.0 and Higher
