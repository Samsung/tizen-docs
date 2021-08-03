---
keyword: camera, CameraView, NUI, ResourceUrl, volume, CameraView.DisplayType
---

# CameraView

The [CameraView](/application/dotnet/api/TizenFX/latest/api/Tizen.NUI.BaseComponents.CameraView.html) class is the NUI view that display [Tizen.Multimedia.Camera](../../multimedia/camera.md)


## Create a CameraView

The following basic example shows how to create a `CameraView` object:

**Figure: Basic CameraView**

![Basic CameraView](./media/camera_images.png)

1.  To use the `CameraView` class, add the following namespaces:

    ```csharp
    using Tizen.NUI;
    using Tizen.NUI.BaseComponents;
    ```	    
  
2.   The CameraView needs a handle of [Tizen.Multimedia.Camera](../../multimedia/camera.md):

      ```csharp
      Tizen.Multimedia.Camera camera = new Tizen.Multimedia.Camera(Tizen.Multimedia.CameraDevice.Front);
      CameraView cameraView = new CameraView(camera.Handle);
      cameraView.WidthResizePolicy = ResizePolicyType.FillToParent;
      cameraView.HeightResizePolicy = ResizePolicyType.DimensionDependency;
      Window.Instance.Add(cameraView);
      camera.StartPreview();
      ```
> [!NOTE]  
> The `CameraView` does not controls Tizen.Multimedia.Camera.
> You need to control `Tizen.Multimedia.Camera`.

3. You can choose the display type `DisplayType.Window` or `DisplayType.Image`.
     ```csharp
     Tizen.Multimedia.Camera camera = new Tizen.Multimedia.Camera(Tizen.Multimedia.CameraDevice.Front);
      CameraView cameraView = new CameraView(camera.Handle, CameraView.DisplayType.Image);
      Window.Instance.Add(cameraView);
     ```
> [!NOTE]  
> Default type is `DisplayType.Window`.


## CameraView methods

  You should call when the camera view needs to be updated if the camera display setting is changed:

  - The `Update()` method updates CameaView:

      ```csharp
      camera.DisplaySettings.Rotation = Tizen.Multimedia.Rotation.Rotate90;
      cameraView.Update();
      ```

## Related information
- Dependencies
  -   Tizen 6.5 and Higher
