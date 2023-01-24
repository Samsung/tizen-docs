# Deep Learning Based Face Recognition

Using deep learning based face recognition, you can perceive and understand faces within your application. This document is a guide on how to register a new face, unregister a face that is registered with a given label, and recognize a given face.

## Prerequisites

To enable your application for using the deep learning based face recognition functionality, create [DeepLearningFaceRecognizer](/application/dotnet/api/TizenFX/latest/api/Tizen.Multimedia.Vision.DeepLearningFaceRecognizer.html) instance.

```csharp
var deepLearningFaceRecognizer = new DeepLearningFaceRecognizer();
```

## Register a new face
To register a new face image with a given label, follow these steps:

1. Prepare an input source to register. In this example, we use [ImageUtil](/application/dotnet/api/TizenFX/latest/api/Tizen.Multimedia.Util.ImageUtil.html) APIs to get the image buffer.

   ```csharp
    MediaVisionSource inputSource = null;

    using (JpegDecoder jpegDecoder = new JpegDecoder())
    {
        jpegDecoder.SetColorSpace(ColorSpace.Rgb888);

        var frame = (await jpegDecoder.DecodeAsync("path")).FirstOrDefault();

        inputSource = new MediaVisionSource(frame.Buffer, (uint)frame.Size.Width, (uint)frame.Size.Height, ColorSpace.Rgb888);
    }
    ```

    > [!NOTE]
    > The input source for `DeepLearningFaceRecognizer` should be RGB data.

2. Now we can register a new face. This is a process where the face recognition framework trains and generates an internal model file with the given face data and its label. You could repeat this step to train the internal model file with more faces. For best accuracy, we recommend training at least three images per face.

    ```csharp
    deepLearningFaceRecognizer.RegisterFace(inputSource, "FaceName1");
    inputSource.Dispose();
    ```

    You can unregister the face from `DeepLearningFaceRecognizer` internal model.
    ```csharp
    deepLearningFaceRecognizer.UnregisterFace("FaceName1");
    ```

## Recognize face
To recognize a given face image, follow these steps:

1. Prepare a target image source. In this example, we use [ImageUtil](/application/dotnet/api/TizenFX/latest/api/Tizen.Multimedia.Util.ImageUtil.html) APIs to get the image buffer.
    ```csharp
    MediaVisionSource targetSource = null;

    using (JpegDecoder jpegDecoder = new JpegDecoder())
    {
        jpegDecoder.SetColorSpace(ColorSpace.Rgb888);

        var frame = (await jpegDecoder.DecodeAsync("path")).FirstOrDefault();

        targetSource = new MediaVisionSource(frame.Buffer, (uint)frame.Size.Width, (uint)frame.Size.Height, ColorSpace.Rgb888);
    }
    ```

2. Recognize a given face image.

    ```csharp
    var result = deepLearningFaceRecognizer.Recognize(targetSource);

    // The result have Label property for recognized face.
    Log.Info("Vision", result.Label);

    targetSource.Dispose();
    ```

## Related information
- Dependencies
  - Tizen 7.0 and Higher