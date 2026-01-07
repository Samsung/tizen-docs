### [Tizen.UI.Scene3D](Tizen.UI.Scene3D.md 'Tizen.UI.Scene3D')

## Camera Class

Represents a camera that projects a 3D scene onto a 2D surface.

```csharp
public class Camera : Tizen.UI.Scene3D.SceneObject
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; Tizen.UI.NObject &#129106; [SceneObject](Tizen.UI.Scene3D.SceneObject.md 'Tizen.UI.Scene3D.SceneObject') &#129106; Camera
### Constructors

<a name='Tizen.UI.Scene3D.Camera.Camera()'></a>

## Camera() Constructor

Initializes a new instance of the ProjectionCamera class with default settings.

```csharp
public Camera();
```
### Properties

<a name='Tizen.UI.Scene3D.Camera.AspectRatio'></a>

## Camera.AspectRatio Property

Gets or sets the aspect ratio of the camera.

```csharp
public float AspectRatio { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Scene3D.Camera.FarPlaneDistance'></a>

## Camera.FarPlaneDistance Property

Gets or sets the distance of the far plane of the camera.

```csharp
public float FarPlaneDistance { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Scene3D.Camera.FieldOfView'></a>

## Camera.FieldOfView Property

Gets or sets the field of view of the camera, in degrees.

```csharp
public float FieldOfView { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Scene3D.Camera.NearPlaneDistance'></a>

## Camera.NearPlaneDistance Property

Gets or sets the distance of the near plane of the camera.

```csharp
public float NearPlaneDistance { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Scene3D.Camera.OrthographicSize'></a>

## Camera.OrthographicSize Property

Gets or sets the size of the camera's viewing box.

```csharp
public float OrthographicSize { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Scene3D.Camera.ProjectionDirection'></a>

## Camera.ProjectionDirection Property

Gets or sets the projection direction of the camera.

```csharp
public Tizen.UI.Scene3D.ProjectionDirection ProjectionDirection { get; set; }
```

#### Property Value
[ProjectionDirection](Tizen.UI.Scene3D.ProjectionDirection.md 'Tizen.UI.Scene3D.ProjectionDirection')

<a name='Tizen.UI.Scene3D.Camera.UseOrthographicProjection'></a>

## Camera.UseOrthographicProjection Property

Gets or sets whether camera uses orthographic projection mode.  
UseOrthographicProjection defines how the camera shows 3D objects or scene on a 2D plane with projection.

```csharp
public bool UseOrthographicProjection { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')






































