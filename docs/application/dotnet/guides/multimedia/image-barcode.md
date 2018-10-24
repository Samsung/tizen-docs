# Barcode Detection and Generation


You can perceive and understand an image or extract information from images in your application.

The main barcode detection and generation features include:

-   Handling images

    You can handle images with the [Tizen.Multimedia.Vision.MediaVisionSource](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Multimedia.Vision.MediaVisionSource.html) class. You can [create the source instance](#prepare) using raw buffer data or an instance of the [Tizen.Multimedia.MediaPacket](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Multimedia.MediaPacket.html) class.

-   Detecting barcodes

    You can [detect barcodes](#detect) in an image or from camera preview streams, and then decrypt them to display messages to the user.

    Before detecting a barcode, you must define the barcode detection target as a value of the [Tizen.Multimedia.Vision.BarcodeDetectionTarget](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Multimedia.Vision.BarcodeDetectionTarget.html) enumeration:

    -   Detect both 1D and 2D barcodes
    -   Detect 1D barcodes only
    -   Detect 2D barcodes only
-   Generating barcodes

    You can encrypt a given message, [generate a barcode](#generate) from it, and save it in a memory or as an image file.

    Before generating a barcode, you must define the text visibility as a value of the [Tizen.Multimedia.Visibility](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Multimedia.Visibility.html) enumeration:

    -   Generate barcode without an input message
    -   Generate barcode with an input message (supports only 1D barcodes)

    You must also define the following [barcode specifications](#spec):

    -   [Barcode type](#barcode)
    -   [QR code specification](#qrcode) (if the QR code barcode type is used)
    -   Image format (if the barcode is saved as a file)
        -   JPEG
        -   BMP
        -   PNG

    Optionally, you can change foreground or background color for the barcode by setting the `ForegroundColor` or `BackgroundColor` properties of the [Tizen.Multimedia.Vision.BarcodeGenerationConfiguration](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Multimedia.Vision.BarcodeGenerationConfiguration.html) class. Their default values are black and white, respectively.

## Prerequisites

To enable your application to use the barcode detection and generation functionality:

1.  Install the NuGet packages for Media Vision and Camera.
2.  To use the methods and properties of the barcode detection and generation classes and to handle camera preview, include the [Tizen.Multimedia](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Multimedia.html) and [Tizen.Multimedia.Vision](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Multimedia.Vision.html) namespaces in your application:

    ```
    using Tizen.Multimedia;
    using Tizen.Multimedia.Vision;
    ```

<a name="prepare"></a>
## Preparing the Barcode Engines

To initialize the barcode detection and generation engines for use:

-   For barcode detection:
    1.  Create an instance of the [Tizen.Multimedia.Vision.BarcodeDetectionConfiguration](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Multimedia.Vision.BarcodeDetectionConfiguration.html) class and set the `Target` property as a value of the [Tizen.Multimedia.Vision.BarcodeDetectionTarget](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Multimedia.Vision.BarcodeDetectionTarget.html) enumeration:

        ```
        static BarcodeDetectionConfiguration configDetection = new BarcodeDetectionConfiguration();

        /// To detect all barcode types
        configDetection.Target = BarcodeDetectionTarget.All;

        /// To detect only 1D barcodes
        /// configDetection.Target = BarcodeDetectionTarget.Barcode1D;
        /// To detect only 2D barcodes (QR codes)
        /// configDetection.Target = BarcodeDetectionTarget.Barcode2D;
        ```

    2.  Create an instance of the [Tizen.Multimedia.Vision.MediaVisionSource](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Multimedia.Vision.MediaVisionSource.html) class with raw image buffer data and its corresponding width, height, and color space:

        ```
        /// Assume that there is a decoded raw data buffer of the byte[] type, and
        /// it has 640x480 resolution with an RGB888 color space
        MediaVisionSource source = new MediaVisionSource(bytes, width, height, ColorSpace.Rgb888);
        ```

        The source stores the barcode to be detected and all related data.

    3.  To provide camera preview images, define a camera preview event handler for the `Preview` event of the [Tizen.Multimedia.Camera](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Multimedia.Camera.html) class and create an instance of that class:

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
            Log.Info("Barcode Sample", "NotSupported");
        }
        ```

    4.  Set the camera display, register the camera preview event handler, and start the camera preview with the `StartPreview()` method:

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

-   For barcode generation, create an instance of the [Tizen.Multimedia.Vision.BarcodeGenerationConfiguration](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Multimedia.Vision.BarcodeGenerationConfiguration.html) class and set its properties:

    ```
    static BarcodeGenerationConfiguration configGeneration = new BarcodeGenerationConfiguration();

    /// To show message on the generated barcode image
    configGeneration.TextVisibility = Visibility.Visible;

    /// To hide message on the generated barcode image
    /// configGeneration.TextVisibility = Visibility.Invisible;

    /// To change the foreground or background color
    /// For this example, the foreground and background are set as black and white, respectively
    configGeneration.ForegroundColor = Color.Black;
    configGeneration.BackgroundColor = Color.White;
    ```

<a name="detect"></a>
## Detecting Barcodes

To detect barcodes:

1.  To access the camera preview data from which to detect barcodes, create a new instance of the [Tizen.Multimedia.Vision.MediaVisionSource](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Multimedia.Vision.MediaVisionSource.html) class in the camera preview event handler:

    ```
    static void PreviewCallback(object sender, PreviewEventArgs e)
    {
        PreviewData preview = e.Preview;

        SinglePlane singlePlane = (SinglePlane)preview.Plane;
        if (preview.Format == CameraPixelFormat.Rgb888)
        {
            MediaVisionSource source = new MediaVisionSource(singlePlane.Data, preview.width, preview.height, ColorSpace.Rgb888);
        }
    ```

2.  Detect barcodes in the image using the `DetectAsync()` method of the [Tizen.Multimedia.Vision.BarcodeDetector](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Multimedia.Vision.BarcodeDetector.html) class:

    ```
        Point point = new Point(0,0);
        Size size = new Size((int)source.Width, (int)source.Height);

        Rectangle roi = new Rectangle(point, size);

        var barcodeLists = await BarcodeDetector.DetectAsync(source, roi, configDetection);

        foreach (Barcode barcode in barcodeLists)
        {
            Log.Info("Barcode sample", $"Barcode type is {barcode.Type}");
            Log.Info("Barcode sample", $"Barcode message is {barcode.Message}");
        }
    }
    ```

    The ROI (region of interest) feature allows you to define a rectangular region of the image in which to detect barcodes. In the above example, the whole image is set as the ROI.

3.  When barcode detection is no longer needed, deregister the camera preview event handler, stop the camera preview, and destroy the camera instance:

    ```
    camera.Preview -= PreviewCallback;

    camera.StopPreview();
    camera.Dispose();
    ```

    For more information, see the [Tizen.Multimedia.Camera](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Multimedia.Camera.html) class.

<a name="generate"></a>
## Generating Barcodes

To generate a barcode:

-   To generate the barcode into memory:
    -   To generate a 1D barcode, create a source instance using the `GenerateSource()` method of the [Tizen.Multimedia.Vision.BarcodeGenerator](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Multimedia.Vision.BarcodeGenerator.html) class with a message and a [barcode type](#barcode):

        ```
        string message = "0123455";

        /// For a Code 128 type barcode
        var source = BarcodeGenerator.GenerateSource(message, BarcodeType.Code128);

        /// If you want to change the barcode color or change the visibility of the text, give an instance
        /// of the Tizen.Multimedia.Vision.BarcodeGenerationConfiguration class as an additional parameter:
        /// var source = BarcodeGenerator.GenerateSource(message, BarcodeType.code128, configGeneration);
        ```

    -   To generate a QR code:
        1.  To create the QR code configuration, create an instance of the [Tizen.Multimedia.Vision.QrConfiguration](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Multimedia.Vision.QrConfiguration.html) class with the QR code encoding mode as a value of the [Tizen.Multimedia.Vision.QrMode](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Multimedia.Vision.QrMode.html) enumeration, the QR code error correction level as a value of the [Tizen.Multimedia.Vision.ErrorCorrectionLevel](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Multimedia.Vision.ErrorCorrectionLevel.html) enumeration, and the QR code version:

            ```
            string message = "Tizen QR";

            /// For the UTF8 encoding type
            QrConfiguration qrConfig = new QrConfiguration(QrMode.Utf8, ErrorCorrectionLevel.Medium, 30);
            ```

        2.  Create a source instance using the `GenerateSource()` method of the `Tizen.Multimedia.Vision.BarcodeGenerator` class with a message and the QR code configuration:

            ```
            var source = BarcodeGenerator.GenerateSource(message, qrConfig);

            /// If you want to change the QR code color, give an instance
            /// of the Tizen.Multimedia.Vision.BarcodeGenerationConfiguration class as an additional parameter:
            /// var source = BarcodeGenerator.GenerateSource(message, qrConfig, configGeneration);
            ```

-   To generate the barcode into a file:
    -   To generate a 1D barcode:
        1.  Create an instance of the [Tizen.Multimedia.Vision.BarcodeImageConfiguration](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Multimedia.Vision.BarcodeImageConfiguration.html) class with the file format as a value of the [Tizen.Multimedia.Vision.BarcodeImageFormat](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Multimedia.Vision.BarcodeImageFormat.html) enumeration, the image file resolution, and a path where the file is to be saved:

            ```
            int width = 300;
            int height = 100;
            BarcodeImageFormat format = BarcodeImageFormat.Jpeg;
            string path = "/tmp/tizen_barcode.jpg";
            BarcodeImageConfiguration imageConfig = new BarcodeImageConfiguration(width, height, path, format);
            ```

        2.  Generate the barcode using the `GenerateImage()` method of the `Tizen.Multimedia.Vision.BarcodeGenerator` class:

            ```
            string message = "0123455";
            BarcodeType type = BarcodeType.Code128;
            BarcodeGenerator.GenerateImage(message, type, imageConfig);
            ```

    -   To generate a QR code, create instances of the `Tizen.Multimedia.Vision.BarcodeImageConfiguration` and `Tizen.Multimedia.Vision.QrConfiguration` classes as above, and generate the QR code using the `GenerateImage()` method of the `Tizen.Multimedia.Vision.BarcodeGenerator` class:

        ```
        int width = 300;
        int height = 300;
        BarcodeImageFormat format = BarcodeImageFormat.Jpeg;
        string path = "/tmp/tizen_qr.jpg";
        BarcodeImageConfiguration imageConfig = new BarcodeImageConfiguration(width, height, path, format);
        Qrconfiguration qrConfig = new QrConfiguration(QrMode.Utf8, ErrorCorrectionLevel.Medium, 30);

        string message = "Tizen QR"
        BarcodeGenerator.GenerateImage(message, qrConfig, imageConfig);
        ```
<a name="spec"></a>
## Barcode Specifications

The following tables provide more information on the barcode generation specifications.

<a name="barcode"></a>
**Table: Supported barcode types**  

| 1D or 2D | Type               | Description                              | Example                                  |
|--------|------------------|----------------------------------------|----------------------------------------|
| 1-D      | UPC-A              | Universal product code with numeric 12-digit | ![UPC-A](./media/mediavision_upc_a.png)  |
| 1-D      | UPC-E              | Universal product code with numeric 6-digit | ![UPC-E](./media/mediavision_upc_e.png)  |
| 1-D      | EAN-8              | International article number with numeric 8-digit | ![EAN-8](./media/mediavision_ean_8.png)  |
| 1-D      | EAN-13             | International article number with numeric 13-digit | ![EAN-13](./media/mediavision_ean_13.png) |
| 1-D      | CODE-128           | Code 128; supports alphanumeric or numeric-only | ![CODE-128](./media/mediavision_code_128.png) |
| 1-D      | CODE-39            | Code 39; supports 34 characters consisting of uppercase letters (A to Z), numeric digits (0 to 9), and special characters (-, ., $, /, %, space) | ![CODE-39](./media/mediavision_code_39.png) |
| 1-D      | INTERLEAVED 2 of 5 | Interleaved 2 of 5 with numeric digits   | ![UPC-A](./media/mediavision_interleaved_2_5.png) |
| 2-D      | QR code            | Quick Response code                      | ![UPC-A](./media/mediavision_qr.png)     |

<a name="qrcode"></a>
**Table: Supported QR code specifications**  

| Specification                     | Support type | Description                              |
|---------------------------------|------------|----------------------------------------|
| Error Correction Code (ECC) Level | ECC Low      | Recovery up to 7% damage                 |
| Error Correction Code (ECC) Level | ECC Medium   | Recovery up to 15% damage                |
| Error Correction Code (ECC) Level | ECC Quartile | Recovery up 25% damage                   |
| Error Correction Code (ECC) Level | ECC High     | Recovery up to 30% damage                |
| Encoding mode                     | Numeric      | Numeric digits ('0', '1', ..., '9')      |
| Encoding mode                     | Alphanumeric | Alphanumeric characters: numeric (0, 1, ..., 9), characters (A, B, ..., Z), and punctuation (' ', $, %, *, +, -, '.', /, ':') |
| Encoding mode                     | Byte 8-bit   | Raw 8-bit bytes                          |
| Encoding mode                     | UTF-8        | Universal character set and Transformation Format 8-bit, encoding characters |




## Related Information
* Dependencies
  -   Tizen 4.0 and Higher
