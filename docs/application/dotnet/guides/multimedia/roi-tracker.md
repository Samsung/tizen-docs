# ROI Tracker

ROI Tracker is a new feature of the Media Vision API since Tizen 7.0 (C# API10). The [RoiTracker](/application/dotnet/api/TizenFX/latest/api/Tizen.Multimedia.Vision.RoiTracker.html) API allows users to obtain the proper ROI coordinates that users want to track in an image. For example, when an image and ROI coordinates are provided as input to this API, the Media Vision framework will process the given image and ROI coordinates from the decoded image data and will provide ROI coordinates within the given image.

## Prerequisites

To enable your application to use the ROI tracker and generation functionality, follow the steps below:

1.  Install the NuGet packages for Media Vision.
2.  To use ROI Tracker, include the [Tizen.Multimedia](/application/dotnet/api/TizenFX/latest/api/Tizen.Multimedia.html) and [Tizen.Multimedia.Vision](/application/dotnet/api/TizenFX/latest/api/Tizen.Multimedia.Vision.html) namespaces in your application:

    ```csharp
    using Tizen.Multimedia;
    using Tizen.Multimedia.Vision;
    ```

## Prepare a MediaVisionSource

Prepare an input source to track. In this example, we use [ImageUtil](/application/dotnet/api/TizenFX/latest/api/Tizen.Multimedia.Util.ImageUtil.html) APIs to get the image buffer.

```csharp
MediaVisionSource inputSource = null;
using (JpegDecoder jpegDecoder = new JpegDecoder())
{
    jpegDecoder.SetColorSpace(ColorSpace.Rgb888);
    var frame = (await jpegDecoder.DecodeAsync("path")).FirstOrDefault();
    inputSource = new MediaVisionSource(frame.Buffer, (uint)frame.Size.Width, (uint)frame.Size.Height, ColorSpace.Rgb888);
}
```

## Track ROI area
To track an ROI area, follow the steps below:

1. Prepare a `RoiTracker` configuration.

    ```csharp
    var roiTrackingConfiguration = new RoiTrackingConfiguration();

    // If you don't set TrackerType, it will be RoiTrackerType.Balance.
    roiTrackingConfiguration.TrackerType = RoiTrackerType.Accuracy;

    // Roi should be set.
    // If you don't set Roi property before calling TrackAsync, TrackAsync method will throws ArgumentException.
    roiTrackingConfiguration.Roi = new Rectangle(10, 10, 100, 100);
    ```

2. Track an ROI area.

    ```csharp
    var result = await RoiTracker.TrackAsync(inputSource, roiTrackingConfiguration);

    Log.Info("RoiTracker", $"X={result.X}, Y={result.Y}, Width={result.Width}, Height={result.Height}, ");
    ```

    > [!NOTE]
    > If you want to change `Roi` area after calling `TrackAsync`, you should create `RoiTrackingConfiguration` again.

3. Dispose of `MediaVisionSource` and `RoiTrackingConfiguration` instances, after using them.

    ```csharp
    inputSource?.Dispose();
    roiTrackingConfiguration?.Dispose();
    ```

## Related information
- Dependencies
  - Tizen 7.0 and Higher
