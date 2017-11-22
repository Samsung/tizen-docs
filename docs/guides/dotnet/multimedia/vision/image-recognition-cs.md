Image Recognition and Tracking
==============================

## Dependencies

- Tizen 4.0 and Higher

You can extract features of an image object and recognize it from
specific images. You can also track the image object in your
application.

The main image recognition and tracking features include:

-   Recognizing images

    You can [recognize image objects](#recognize) in specific images,
    and extract image object features.

- Tracking images

    You can [track image objects](#track) using the camera preview
    images and a specific image tracking model.


Prerequisites
-------------

To enable your application to use the image recognition and tracking
functionality:

1.  Install the Nuget packages for Media Vision and Camera.
2. To use the methods and properties of the image recognition and
    tracking classes and to handle camera preview, include the
    [Tizen.Multimedia](https://developer.tizen.org/dev-guide/csapi/namespaceTizen_1_1Multimedia.html)
    namespace in your application:

    ``` {.prettyprint}
    using Tizen.Multimedia;
    ```

3. Define the configuration settings:
    -   For configuring image object and feature extraction, create an
        instance of the
        [Tizen.Multimedia.ImageFillConfiguration](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1Multimedia_1_1ImageFillConfiguration.html)
        class and set its attributes accordingly:

        ``` {.prettyprint}
        static ImageFillConfiguration configFill = new ImageFillConfiguration();

        /// Set the scale factor of the image being recognized
        configFill.ObjectScaleFactor = 1.2;

        /// Set the maximum amount of image key points to be detected
        configFill.ObjectMaxKeyPoints = 1000;
        ```

    - For image recognition, create an instance of the
        [Tizen.Multimedia.ImageRecognitionConfiguration](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1Multimedia_1_1ImageRecognitionConfiguration.html)
        class and set its attributes accordingly:

        ``` {.prettyprint}
        static ImageRecognitionConfiguration configRecog = new ImageRecognitionConfiguration();

        /// Set the scene scale factor
        configRecog.SceneScaleFactor = 1.2;

        /// Set the maximum amount of key points to be detected in a scene
        configRecog.SceneMaxKeyPoints = 3000;
        ```

    - For image tracking, create an instance of the
        [Tizen.Multimedia.ImageTrackingConfiguration](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1Multimedia_1_1ImageTrackingConfiguration.html)
        class and set its attributes accordingly:

        ``` {.prettyprint}
        static ImageTrackingConfiguration configTrack = new ImageTrackingConfiguration();

        /// Set the history amount
        configTrack.HistroyAmount = 5;

        /// Set the expected offset
        configTrack.ExpectedOffset = 0.5;
        ```


Recognizing Images <a id="recognize"></a>
------------------

To recognize an image (the target) in another (the scene):

1.  To prepare the target image being recognized, create an instance of
    the
    [Tizen.Multimedia.MediaVisionSource](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1Multimedia_1_1MediaVisionSource.html)
    class with raw image buffer data and its corresponding width,
    height, and color space parameters:

    ``` {.prettyprint}
    /// Assume that there is a decoded raw data buffer of the byte[] type, and
    /// it has 640x480 resolution with an RGB888 color space

    MediaVisionSource sourceTarget = new MediaVisionSource(bytes, width, height, ColorSpace.Rgb888);
    ```

2. Create an instance of the
    [Tizen.Multimedia.ImageObject](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1Multimedia_1_1ImageObject.html)
    class and use its `Fill()` method to fill it with the
    `Tizen.Multimedia.MediaVisionSource` instance:

    ``` {.prettyprint}
    static ImageObject obj = new ImageObject();

    obj.Fill(sourceTarget);

    /// If you want to apply configuration options to the fill operation:
    /// obj.Fill(sourceTarget, configFill);

    /// If you want a specific label for the ImageObject instance, set it manually
    /// Otherwise the label automatically increments with each fill operation
    obj.setLabel(1);
    ```

3. To prepare the scene where the target image is to be recognized,
    create a `Tizen.Multimedia.MediaVisionSource` instance which stores
    the scene:

    ``` {.prettyprint}
    /// Assume that there is a decoded raw data buffer of the byte[] type, and
    /// it has 640x480 resolution with an RGB888 color space

    MediaVisionSource sourceScene  = new MediaVisionSource(bytes, width, height, ColorSpace.Rgb888);
    ```

4. To recognize the target inside the scene, use the `RecognizeAsync()`
    method of the
    [Tizen.Multimedia.ImageRecognizer](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1Multimedia_1_1ImageRecognizer.html)
    class:

    ``` {.prettyprint}
    /// You can recognize multiple targets
    ImageObject[] targets = new ImageObject[1] (obj);

    var results = await ImageRecognizer.RecognizeAsync(sourceScene, targets);

    foreach (ImageRecognitionResult imageResult in results)
    {
        if (imageResult.Success)
            Log.info(LogUtils.TAG, imageResult, Region.ToString();
        else
            Log.info(LogUtils.Tag, "ImageRecognition: + imageResult.Success.ToString()");
    }
    ```


Tracking Images <a id="track"></a>
---------------

To track images:

1.  To prepare the camera and create an image tracking model:

    1.  Define a camera preview event handler for the `Preview` event of the [Tizen.Multimedia.Camera](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1Multimedia_1_1Camera.html) class and create an instance of that class:

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

    2. Set the camera display, register the camera preview event handler, and start the camera preview with the `StartPreview()` method:

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


    3. Create the image tracking model as an instance of the [Tizen.Multimedia.ImageTrackingModel](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1Multimedia_1_1ImageTrackingModel.html) class:

       ```
       static ImageTrackingModel model = new ImageTrackingModel();
       ```

2.  Create a target image as an instance of the

    [Tizen.Multimedia.MediaVisionSource](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1Multimedia_1_1MediaVisionSource.html) class.

    Create an instance of the
    [Tizen.Multimedia.ImageObject](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1Multimedia_1_1ImageObject.html)
    class and use its `Fill()` method to fill it with the target image.

    ``` {.prettyprint}
    static MediaVisionSource sourceTarget = new MediaVisionSource(bytes, width, height, ColorSpace.Rgb888);

    static ImageObject obj = new ImageObject();
    obj.Fill(sourceTarget);
    ```

3. Set the target of the image tracking model with the `SetTarget()`
    method of the `Tizen.Multimedia.ImageTrackingModel` class, which
    takes the `Tizen.Multimedia.ImageObject` instance as its parameter:

    ``` {.prettyprint}
    model.SetTarget(obj)
    ```

4. To track the target, use the `TrackAsync()` method of the
    [Tizen.Multimedia.ImageTracker](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1Multimedia_1_1ImageTracker.html)
    class:

    ``` {.prettyprint}
    /// Assume that "frames" contains a sequence of decoded images as
    /// Tizen.Multimedia.MediaVisionSource instances

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

5. When image tracking is no longer needed, deregister the camera
    preview event handler, stop the camera preview, and destroy the
    camera instance:

    ``` {.prettyprint}
    camera.Preview -= PreviewCallback;

    camera.StopPreview();
    camera.Dispose();
    ```
