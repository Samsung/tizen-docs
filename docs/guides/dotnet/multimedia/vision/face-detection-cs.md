
Face Detection, Recognition, and Tracking
=========================================

## Dependencies

- Tizen 4.0 and Higher

You can detect a face in an image, or track a face in the device camera
preview.

The main face detection, recognition, and tracking features include:

-   Detecting faces

    You can decode an image file and [detect faces](#detect) on it.

- Recognizing faces

    You can [recognize faces](#recognize) in an image with a set of
    example faces.

- Tracking faces

    You can [track faces](#track) using the camera preview images,
    starting from a specific location in the image.



Prerequisites
-------------

To enable your application to use the face detection, recognition, and
tracking functionality:

1.  Install the Nuget packages for Media Vision and Camera.
2. To use the methods and properties of the face detection, tracking,
    and recognition classes and to handle camera preview, include the
    [Tizen.Multimedia](https://developer.tizen.org/dev-guide/csapi/namespaceTizen_1_1Multimedia.html)
    namespace in your application:

    ``` {.prettyprint}
    using Tizen.Multimedia;
    ```

3. Define the configuration settings:
    -   For face detection, create an instance of the
        [Tizen.Multimedia.FaceDetectionConfiguration](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1Multimedia_1_1FaceDetectionConfiguration.html)
        class and set its properties accordingly:

        ``` {.prettyprint}
        static FaceDetectionConfiguration configDetection = new FaceDetectionConfiguration();

        /// Set a model path if you want to save your own model in a certain place
        configDetection.ModelFilePath = "app_path/your_own_model";

        /// Set a minimum face size if you want to detect only larger faces
        configDetection.MinWidth = 50;
        configDetection.MinHeight = 50;

        /// Set a region of interest if you want to detect in a specific region
        configDetection.Roi = new Rectangle(10, 10, 20, 30);
        ```

    - For face recognition, create an instance of the
        [Tizen.Multimedia.FaceRecognitionConfiguration](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1Multimedia_1_1FaceRecognitionConfiguration.html)
        class and set its properties accordingly:

        ``` {.prettyprint}
        static FaceRecognitionConfiguration configRecog = new FaceRecognitionConfiguration();

        /// Set the face recognition learning model algorithm to one of the
        /// values of the Tizen.Multimedia.FaceRecognitionModelType enumeration
        configRecog.ModelType = FaceRecognitionModelType.lbph;
        ```

    - For face tracking, no configuration is needed.



Detecting Faces <a id="detect"></a>
---------------

To detect faces:

1.  Create an instance of the
    [Tizen.Multimedia.MediaVisionSource](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1Multimedia_1_1MediaVisionSource.html)
    class with raw image buffer data and its corresponding width,
    height, and color space parameters:

    ``` {.prettyprint}
    /// Assume that there is a decoded raw data buffer of the byte[] type, and
    /// it has 640x480 resolution with an RGB888 color space

    MediaVisionSource source = new MediaVisionSource(bytes, width, height, ColorSpace.Rgb888);
    ```

2. To detect faces, use the `DetectAsync()` method of the
    [Tizen.Multimedia.FaceDetector](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1Multimedia_1_1FaceDetector.html)
    class:

    ``` {.prettyprint}
    var faceLists = await FaceDetector.DetectAsync(source);

    /// If you want to change the face detection configuration, use an instance
    /// of the Tizen.Multimedia.FaceDetectionConfiguration class as a
    /// parameter for the DetectAsync() method
    /// For example,
    /// var faceLists = await FaceDetector.DetectAsync(source, configDetection);

    foreach (Rectangle location in faceLists)
    {
        Log.Info("Face detection sample", $"location is {location}");
    }
    ```



Recognizing Faces <a id="recognize"></a>
-----------------

To recognize faces:

1.  Create an instance of the
    [Tizen.Multimedia.FaceRecognitionModel](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1Multimedia_1_1FaceRecognitionModel.html)
    class and add face examples to it with the `Add()` method.

    Face examples need to be of the same person but captured at
    different angles. The example assumes that 10 face samples are used
    and that the face area in each example covers approximately 95\~100%
    of the image. The face to be recognized is given the label "1".

    ``` {.prettyprint}
    static FaceRecognitionModel model = new FaceRecognitionModel();

    /// faceExamples contains 10 face examples as instances
    /// of the Tizen.Multimedia.MediaVisionSource class
    foreach (MediaVisionSource example in faceExamples)
    {
        model.add(example, 1);
    }
    ```

2. Learn the face recognition model based on the provided examples with
    the `Learn()` method:

    ``` {.prettyprint}
    model.Learn();
    ```

3. To recognize a face, use the `RecognizeAsync()` method of the
    [Tizen.Multimedia.FaceRecognizer](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1Multimedia_1_1FaceRecognizer.html)
    class:

    ``` {.prettyprint}
    /// whoFaceSource is an instance of the Tizen.Multimedia.MediaVisionSource class
    /// that contains the face to be recognized
    /// whoFaceRoi is an instance of the Tizen.Multimedia.Rectangle struct that defines
    /// a region of interest containing the face to be recognized
    var result = await FaceRecognizer.RecognizeAsync(whoFaceSource, model, whoFaceRoi);

    Log.Info("Face recognition sample", $"confidence is {result.Confidence}");
    Log.Info("Face recognition sample", $"success is {result.Success}");
    if (result.Success)
    {
        Log.info("Face recognition sample", $"label is {result.Label}");
    }
    ```



Tracking Faces <a id="track"></a>
--------------

To track faces:

1.  Prepare the camera:
    a.  Define a camera preview event handler for the `Preview` event of the
    [Tizen.Multimedia.Camera](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1Multimedia_1_1Camera.html)
    class and create an instance of that class:

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
        Log.Info("Face Detection Sample", "NotSupported");
    }
    ```

    b.  Set the camera display, register the camera preview event handler, and start the camera preview with the `StartPreview()` method of the `Tizen.Multimedia.Camera` class:

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

2. Manage face tracking:
    a.  Set the initial tracking location. In the following example, the `DetectAsync()` method of the [Tizen.Multimedia.FaceDetector](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1Multimedia_1_1FaceDetector.html) class is used to detect a face and provide its initial location:

    ```
    var faceLocation = await FaceDetector.DetectAsync(source);

    Point[] initialPoint =
    {
        new Point(faceLocation.Left, FaceLocation.Top),
        new Point(faceLocation.Right, FaceLocation.Top),
        new Point(faceLocation.Right, FaceLocation.Bottom),
        new Point(faceLocation.Left, FaceLocation.Bottom)
    };
    ```

    b.  Create an instance of the [Tizen.Multimedia.FaceTrackingModel](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1Multimedia_1_1FaceTrackingModel.html) class and prepare the model with the initial location:

    ```
     Quadrangle faceLocation = new Quadrangle(initialPoint);

    static FaceTrackingModel model = new FaceTrackingModel();

    model.Prepare(source, faceLocation);xxxxxxxxxx 
    ```

    c. To track the face, use the `TrackAsync()` method of the [Tizen.Multimedia.FaceTracker](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1Multimedia_1_1FaceTracker.html) class:

    ```
    var result = await FaceTracker.TrackAsync(source, model, false);
    if (result.Region != null)
    {
        Log.Info("Face tracking sample", $"location is {result.Region}");
    }
    ```

    d.  When face tracking is no longer needed, deregister the camera preview event handler, stop the camera preview, and destroy the camera instance:

    ```
    camera.Preview -= PreviewCallback;

    camera.StopPreview();
    camera.Dispose();
    ```
