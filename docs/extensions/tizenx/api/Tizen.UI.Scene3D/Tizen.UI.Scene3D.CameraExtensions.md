### [Tizen.UI.Scene3D](Tizen.UI.Scene3D.md 'Tizen.UI.Scene3D')

## CameraExtensions Class

Provides extension methods for the Camera class.

```csharp
public static class CameraExtensions
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; CameraExtensions
### Methods

<a name='Tizen.UI.Scene3D.CameraExtensions.ConvertFovFromHorizontalToVertical(thisTizen.UI.Scene3D.Camera,float,float)'></a>

## CameraExtensions.ConvertFovFromHorizontalToVertical(this Camera, float, float) Method

Converts the horizontal field of view (FOV) to a vertical FOV based on the given aspect ratio.

```csharp
public static float ConvertFovFromHorizontalToVertical(this Tizen.UI.Scene3D.Camera camera, float aspect, float fieldOfView);
```
#### Parameters

<a name='Tizen.UI.Scene3D.CameraExtensions.ConvertFovFromHorizontalToVertical(thisTizen.UI.Scene3D.Camera,float,float).camera'></a>

`camera` [Camera](Tizen.UI.Scene3D.Camera.md 'Tizen.UI.Scene3D.Camera')

The camera object.

<a name='Tizen.UI.Scene3D.CameraExtensions.ConvertFovFromHorizontalToVertical(thisTizen.UI.Scene3D.Camera,float,float).aspect'></a>

`aspect` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The aspect ratio of the camera.

<a name='Tizen.UI.Scene3D.CameraExtensions.ConvertFovFromHorizontalToVertical(thisTizen.UI.Scene3D.Camera,float,float).fieldOfView'></a>

`fieldOfView` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The horizontal field of view in radians.

#### Returns
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')  
The vertical field of view in radians.

<a name='Tizen.UI.Scene3D.CameraExtensions.ConvertFovFromVerticalToHorizontal(thisTizen.UI.Scene3D.Camera,float,float)'></a>

## CameraExtensions.ConvertFovFromVerticalToHorizontal(this Camera, float, float) Method

Converts the vertical field of view (FOV) to a horizontal FOV based on the given aspect ratio.

```csharp
public static float ConvertFovFromVerticalToHorizontal(this Tizen.UI.Scene3D.Camera camera, float aspect, float fieldOfView);
```
#### Parameters

<a name='Tizen.UI.Scene3D.CameraExtensions.ConvertFovFromVerticalToHorizontal(thisTizen.UI.Scene3D.Camera,float,float).camera'></a>

`camera` [Camera](Tizen.UI.Scene3D.Camera.md 'Tizen.UI.Scene3D.Camera')

The camera object.

<a name='Tizen.UI.Scene3D.CameraExtensions.ConvertFovFromVerticalToHorizontal(thisTizen.UI.Scene3D.Camera,float,float).aspect'></a>

`aspect` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The aspect ratio of the camera.

<a name='Tizen.UI.Scene3D.CameraExtensions.ConvertFovFromVerticalToHorizontal(thisTizen.UI.Scene3D.Camera,float,float).fieldOfView'></a>

`fieldOfView` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The vertical field of view in radians.

#### Returns
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')  
The horizontal field of view in radians.





































