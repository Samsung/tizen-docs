# Camera


You can use basic camera features, including preview and capture. You can capture still images with the device's internal camera and keep images on your target device.

**Figure: Camera image examples**

![Camera image examples](./media/camera_images.png)

The main features of the `Tizen.Multimedia.Camera` class include:

-   Configuring the camera

    You can [configure the camera](#configuring-the-camera) and set the camera and autofocus event handlers.

-   Setting the display for the camera preview

    You can preview images in real time with the `StartPreview()` method of the `Tizen.Multimedia.Camera` class.
    Camera provides support for the following features:

    -   Pixel formats, such as NV12, NV12T, NV16, NV21, YUYV, UYVY, YUV420P, I420, Yv12, Rgb565, Rgb888, Rgba, Argb, Jpeg, H264 and Invz
    -   Preview at the frame rate, which you can set by `PreviewFps` property.
    -   Rotation and flip of the preview

    You can also [customize the display settings for the camera preview](#setting-the-display-for-the-camera-preview).

-   Capturing and saving images

    You can start the camera preview and [capture an image](#taking-a-photo).

-   Setting camera attributes

    You can [control the following camera settings](#setting-camera-attributes):

    -   Contrast
    -   Exposure
    -   Brightness
    -   Effects
    -   ISO
    -   White balance
    -   Zoom
    -   Flash
    -   Focus
    -   Metering
    -   EXIF tag (geo, orientation, software information and description)
    -   Scene mode, HDR, theater
    -   Image quality

    Depending on the camera device type, the device supports different orientations, resolutions, or preview and capture formats. You can obtain this information from the device using the `SupportedPreviewResolutions`, `SupportedCapturePixelFormats`, or other `SupportedXXX` properties of the [Tizen.Multimedia.CameraCapabilities](/application/dotnet/api/TizenFX/latest/api/Tizen.Multimedia.CameraCapabilities.html) class.

    Since devices can have multiple camera sensors with different capabilities, create a `Tizen.Multimedia.Camera` instance with a proper [Tizen.Multimedia.CameraDevice](/application/dotnet/api/TizenFX/latest/api/Tizen.Multimedia.CameraDevice.html) enumeration value, determining which camera sensor is used. Usually the primary sensor is located on the back side and the secondary sensor on the front side of the device. Once the camera sensor is selected, the selected sensor starts working.

    > **Note**
    >
    > Simultaneous use of multiple camera sensors is not allowed.  
    > The target device often supports more functionalities than the emulator.  
    > The behavior of the shutter sound can vary depending on the legislation of each country.


-   Releasing resources

    When you have finished working with the camera, you can [release the resources](#releasing-resources).

The following figure illustrates the camera state changes in normal mode.

**Figure: Camera states in normal mode**

![Camera states in normal mode](./media/using_camera_states_dotnet.png)

## Prerequisites

To enable your application to use the camera functionality:

1.  Create a camera instance:

    ```csharp
    try
    {
        Camera camera = new Camera(CameraDevice.Rear);
    }
    catch (Exception ex)
    {
        Log.Error("Camera", "Creating camera instance failed. " + ex.ToString());
    }
    ```

    The `CameraDevice.Rear` parameter means that the currently activated device camera is the primary camera. You can select between the rear (primary) and front (secondary) camera. The available parameter values are defined in the [Tizen.Multimedia.CameraDevice](/application/dotnet/api/TizenFX/latest/api/Tizen.Multimedia.CameraDevice.html) enumeration.

2.  Check the current state of the camera using the `State` property of the [Tizen.Multimedia.Camera](/application/dotnet/api/TizenFX/latest/api/Tizen.Multimedia.Camera.html) class:

    ```csharp
    CameraState state;

    /// Check the camera state after creating the camera
    state = camera.State;
    ```

    The returned state is one of the values defined in the [Tizen.Multimedia.CameraState](/application/dotnet/api/TizenFX/latest/api/Tizen.Multimedia.CameraState.html) enumeration. If the state is not `Created`, re-initialize the camera by recreating the instance.

## Configuring the Camera

After setting up the necessary prerequisites, configure the camera and set the camera preview event handler.

To configure the camera:

1.  Set the image quality using the `ImageQuality` property of the [Tizen.Multimedia.CameraSettings](/application/dotnet/api/TizenFX/latest/api/Tizen.Multimedia.CameraSettings.html) class:

    ```csharp
    camera.Settings.ImageQuality = 100;
    ```

    The image quality value can range from 1 (lowest quality) to 100 (highest quality).

2.  Set the display for showing preview images by using the `Display` property of the [Tizen.Multimedia.Camera](/application/dotnet/api/TizenFX/latest/api/Tizen.Multimedia.Camera.html) class with 1 of the camera display types (`ElmSharp.Window` overlay or `Tizen.Multimedia.MediaView` EVAS surface).

    The following examples set the display according to the display types. The camera state must be in the `Created`:

    ```csharp
    /// Overlay display type
    camera.Display = new Display(new Window("CameraWindow"));

    /// EVAS surface display type
    camera.Display = new Display(new MediaView(new Window("CameraWindow")));
    ```

3.  Set the camera preview resolution using the `PreviewResolution` property of the `Tizen.Multimedia.CameraSettings` class. You must set this property before previewing.

    To find out which resolutions can be set for the camera preview on a specific device, use the `SupportedPreviewResolutions` property of the [Tizen.Multimedia.CameraCapabilities](/application/dotnet/api/TizenFX/latest/api/Tizen.Multimedia.CameraCapabilities.html) class. This property returns an `IEnumerable` variable.

    The following example sets the camera preview resolution to the first found supported resolution:

    ```csharp
    IList supportedResolutions = _camera.Capabilities.SupportedPreviewResolutions.ToList();
    foreach(Size resolution in supportedResolutions)
    {
        camera.Settings.PreviewResolution = resolution;
        break;
    }
    ```

4.  Set the capture format using the `CapturePixelFormat` property of the `Tizen.Multimedia.CameraSettings` class:

    ```csharp
    camera.Settings.CapturePixelFormat = CameraPixelFormat.Jpeg;
    ```

    The [Tizen.Multimedia.CameraPixelFormat](/application/dotnet/api/TizenFX/latest/api/Tizen.Multimedia.CameraPixelFormat.html) enumeration defines the available capture formats.

5.  Register event handlers for managing various events of the `Tizen.Multimedia.Camera` class, related to the camera preview, autofocus, and capturing:
    -   <a name="callbacks_preview"></a>To handle the camera preview, register an event handler for the `Preview` event. The event handler is invoked once per frame during a preview.

        ```csharp
        public static void PreviewEventHandler(object sender, PreviewEventArgs e)
        {
            if (e.Preview.PlaneType == PlaneType.RgbPlane)
            {
                /// Do something
            }
        }

        camera.Settings.PreviewPixelFormat = CameraPixelFormat.Rgba;
        camera.Preview += PreviewEventHandler;
        ```

    -   <a name="callbacks_focus"></a>To receive notifications about autofocus state changes, register an event handler for the `FocusStateChanged` event. The event handler is invoked every time the autofocus state changes.

        ```csharp
        public static void FocusStateChangedEventHandler(object sender, CameraFocusStateChangedEventArgs e)
        {
            Log.Info("Camera", "Focus state is changed to " + e.State.ToString());
        }

        camera.FocusStateChanged += FocusStateChangedEventHandler;
        ```

        Before autofocusing starts, the autofocus state is `Released`. After the `StartFocusing()` method is called, the camera starts autofocusing and the state changes to `Ongoing`. If autofocusing finishes successfully, the state changes to `Focused`. If autofocusing fails, the state changes to `Failed`.

    -   To receive a captured still image, register an event handler for the `Capturing` event. The event handler is invoked once for each captured frame, and is used to get information about the captured image.

        The image is saved in the format set by the `CapturePixelFormat` property of the `Tizen.Multimedia.CameraSettings` class in the previous step.

        The following event handler example saves the captured frame as a JPEG image:

        ```csharp
        public static void CapturingEventHandler(object sender, CameraCapturingEventArgs e)
        {
            if (e.MainImage != null)
            {
                /// PostView and Thumbnail can be null
                if (e.MainImage.Data.Length > 0)
                {
                    File.WriteAllBytes("StillImage.jpg", e.MainImage.Data);
                }
            }
        }

        camera.Capturing += CapturingEventHandler;
        ```

    -   To receive a notification when the image has been captured, register an event handler for the `CaptureCompleted` event. The event handler is invoked after the event handler of the `Capturing` event completes, and is used for notification and for restarting the camera preview.

        The following event handler example restarts the camera preview:

        ```csharp
        public static void CaptureCompletedEventHandler(object sender, EventArgs e)
        {
            camera.StartPreview();
        }

        camera.CaptureCompleted += CaptureCompletedEventHandler;
        ```

## Setting the Display for the Camera Preview

Before displaying the camera preview on the screen, check the camera display settings. You can use the default display settings provided by the Camera framework, or you can customize the display settings to meet your needs.

To customize the display settings:

-   Camera selection and orientation

    Before you can correctly customize the display settings, you need to know which camera is active (front or back) and at what angle the physical camera is being held (orientation):

    -   To determine the active camera, check the [Tizen.Multimedia.CameraDevice](/application/dotnet/api/TizenFX/latest/api/Tizen.Multimedia.CameraDevice.html) enumeration value:

        ```csharp
        public enum CameraDevice
        {
            Rear, /// Rear camera
            Front /// Front camera
        }
        ```

        The rear camera is usually the primary camera, and the front camera is usually the secondary camera. If, for example, you created the camera instance for the primary camera, the camera preview shows the rear camera view.

    -   To determine the current camera angle, use the `LensOrientation` property of the [Tizen.Multimedia.CameraSettings](/application/dotnet/api/TizenFX/latest/api/Tizen.Multimedia.CameraSettings.html) class:

        ```csharp
        int angle = camera.Settings.LensOrientation;
        ```

        The returned value of the `angle` variable is in degrees.

    Once you know the active camera and its current orientation angle (or tilt), you can calculate how to rotate the display to match the camera orientation, and whether and how to flip the display to create the mirror effect if the front camera is active.

    To correctly rotate the display as the camera orientation changes, think about the orientation and direction of the physical camera lens, relative to the display. If the camera faces away from the display, the camera orientation is calculated clockwise across the display. If the camera faces the same way as the display, the camera orientation is calculated counter-clockwise across the display. For example, if the camera and display face in opposite directions, the right side of the image is at 90 degrees, and if the camera and display face in the same direction, the right side is at 270 degrees (360 - 90).

-   Display rotation

    The display rotation setting is preset to a default value for each camera. Before changing the display rotation value, retrieve the default value using the `Rotation` property of the [Tizen.Multimedia.CameraDisplaySettings](/application/dotnet/api/TizenFX/latest/api/Tizen.Multimedia.CameraDisplaySettings.html) class:

    ```csharp
    Rotation rotation = camera.DisplaySettings.Rotation;
    ```

    Calculate and set a new display rotation value based on the current camera orientation:

    ```csharp
    int lengOrientation;
    int displayRotationAngle;
    Rotation displayRotation = Rotation.Rotate0;

    /// Get the recommended display rotation value
    lengOrientation = camera.Settings.LensOrientation;
    displayRotationAngle = (360 - lengOrientation) % 360;

    /// Convert the display rotation value to an enumerator type
    switch (displayRotationAngle)
    {
        case 0:
            displayRotation = Rotation.Rotate0;
            break;
        case 90:
            displayRotation = Rotation.Rotate90;
            break;
        case 180:
            displayRotation = Rotation.Rotate180;
            break;
        case 270:
            displayRotation = Rotation.Rotate270;
            break;
        default:
            displayRotation = Rotation.Rotate0;
            break;
    }

    /// Set the display rotation
    camera.DisplaySettings.Rotation = displayRotation;
    ```

-   Display flip

    The display flip setting is preset to a default value for each camera. For example, to support the mirror mode, the secondary (front) camera is set as flipped by default.

    Before changing the display flip value, retrieve the default value using the `Flip` property of the `Tizen.Multimedia.CameraDisplaySettings` class:

    ```csharp
    Flips displayFlip = camera.DisplaySettings.Flip;
    ```

    Calculate and set a new display flip value based on the direction the camera is facing and the current camera orientation:

    ```csharp
    /// If the camera is facing in the same direction as the display,
    /// apply flip to the front camera because of the mirror effect

    int lengOrientation;
    int displayRotationAngle;
    Flips displayFlip = Flips.None;

    /// Get the recommended display rotation value
    lengOrientation = camera.Settings.LensOrientation;
    displayRotationAngle = (360 - lengOrientation) % 360;

    /// Set the mirror display
    if (displayRotationAngle == 90 || displayRotationAngle == 270)
    {
        displayFlip = Flips.Vertical;
    }
    else
    {
        displayFlip = Flips.Horizontal;
    }

    /// Set the display flip
    camera.DisplaySettings.Flip = displayFlip;
    ```

    The system applies display flip after display rotation, so you must always calculate the correct display flip value after determining the display rotation.

> **Note**
>
> For an overlay surface, when the device orientation changes, the displayed camera preview does not rotate automatically. If you want to rotate the display according to the device orientation, use the `Rotation` property of the `Tizen.Multimedia.CameraDisplaySettings` class.  
>
> For an Evas surface, the Evas object for the camera display is rotated by the window manager used by the application, not by the `Rotation` property.

## Taking a Photo

To take a photo:

1.  [After configuring the camera](#configuring-the-camera), start the camera preview using the `StartPreview()` method of the [Tizen.Multimedia.Camera](/application/dotnet/api/TizenFX/latest/api/Tizen.Multimedia.Camera.html) class:

    ```csharp
    camera.StartPreview();
    ```

    The camera preview draws preview frames on the screen and allows you to capture frames as still images.

    After starting the camera preview, the application flows as follows:

    1.  During the camera preview, the application calls the [camera preview event handler](#callbacks_preview) for each frame.
    2.  The camera preview event handler calls the `StartFocusing()` method, which starts the autofocusing process.
    3.  During autofocusing, as the autofocus state changes, the application calls the [camera autofocus event handler](#callbacks_focus).

2.  When the preview and autofocus processes are completed, the application can start image capturing.

    To capture an image, use the `StartCapture()` method:

    ```csharp
    camera.StartCapture();
    ```

## Setting Camera Attributes

You can set various camera attributes with the [Tizen.Multimedia.CameraSettings](/application/dotnet/api/TizenFX/latest/api/Tizen.Multimedia.CameraSettings.html) class.

To set some attributes:

-   Camera preview attributes:

    The camera preview attributes are a group of attributes that you can set before starting the preview. The following example sets the FPS and image quality attributes:

    ```csharp
    camera.Settings.PreviewFps = CameraFps.Auto;

    camera.Settings.ImageQuality = 100;
    ```

-   Camera zoom attribute:

    Retrieve the range of available zoom level values using the `ZoomRange` property, and set the zoom level using the `ZoomLevel` property. The following example retrieves the available zoom level range and sets the zoom level to minimum:

    ```csharp
    Range zoomRange = camera.Settings.ZoomRange;

    camera.Settings.ZoomLevel = zoomRange.Min;
    ```

-   Camera brightness attribute:

    Retrieve the range of available brightness level values using the `BrightnessRange` property, and the current brightness level using the `Brightness` property. The following example retrieves the available brightness level range and sets the brightness level to minimum:

    ```csharp
    Range brightnessRange = camera.Settings.BrightnessRange;
    int brightness = camera.Settings.Brightness;

    /// Set a new brightness level
    camera.Settings.Brightness = brightnessRange.Min;
    ```

## Releasing Resources

After you have finished working with the camera, stop the camera and clean up the application environment:

1.  If autofocus is switched on, switch if off using the `StopFocusing()` method of the [Tizen.Multimedia.Camera](/application/dotnet/api/TizenFX/latest/api/Tizen.Multimedia.Camera.html) class:

    ```csharp
    camera.StopFocusing();
    ```

2.  Stop the camera preview using the `StopPreview()` method:

    ```csharp
    camera.StopPreview();
    ```

3.  Destroy the camera handle and release all its resources using the `Dispose()` method:

    ```csharp
    camera.Dispose();
    ```


## Related Information
* Dependencies
  -   Tizen 4.0 and Higher
