---
keyword: camera, CameraView, NUI, CameraView.DisplayType
---

# CameraView

The [CameraView](/application/dotnet/api/TizenFX/API9/api/Tizen.NUI.BaseComponents.CameraView.html) class is the NUI view that displays [camera](/application/dotnet/guides/multimedia/camera.md).


## Create a CameraView

The following basic example shows how to create a `CameraView` object:

**Figure: Basic CameraView**

![Basic CameraView](../media/camera_images.png)

1. To use the `CameraView` class, add the following namespaces:

    ```csharp
    using Tizen.NUI;
    using Tizen.NUI.BaseComponents;
    ```

2. To create a `CameraView`, you need a handle of [Tizen.Multimedia.Camera](/application/dotnet/guides/multimedia/camera.md):

    ```csharp
    Tizen.Multimedia.Camera camera = new Tizen.Multimedia.Camera(Tizen.Multimedia.CameraDevice.Front);
    CameraView cameraView = new CameraView(camera.Handle);
    cameraView.WidthResizePolicy = ResizePolicyType.FillToParent;
    cameraView.HeightResizePolicy = ResizePolicyType.DimensionDependency;
    Window.Instance.Add(cameraView);
    camera.StartPreview();
    ```

    > [!NOTE]
    > You need to control the `Tizen.Multimedia.Camera` class, since the `CameraView` does not control the same.

3. To change display, you can choose the display type, `DisplayType.Window` or `DisplayType.Image`:

    ```csharp
    Tizen.Multimedia.Camera camera = new Tizen.Multimedia.Camera(Tizen.Multimedia.CameraDevice.Front);
    CameraView cameraView = new CameraView(camera.Handle, CameraView.DisplayType.Image);
    Window.Instance.Add(cameraView);
    ```

    > [!NOTE]
    > The default display type is `DisplayType.Window`.


## CameraView methods

When the camera display setting changes, to update the `CameraView`, you must call the `Update()` method:

```csharp
camera.DisplaySettings.Rotation = Tizen.Multimedia.Rotation.Rotate90;
cameraView.Update();
```

## Related information
- Dependencies
  -   Tizen 6.5 and Higher
