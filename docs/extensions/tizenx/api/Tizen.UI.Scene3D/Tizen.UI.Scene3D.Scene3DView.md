### [Tizen.UI.Scene3D](Tizen.UI.Scene3D.md 'Tizen.UI.Scene3D')

## Scene3DView Class

[Scene3DView](Tizen.UI.Scene3D.Scene3DView.md 'Tizen.UI.Scene3D.Scene3DView') is a [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View') for displaying 3D [SceneObject](Tizen.UI.Scene3D.SceneObject.md 'Tizen.UI.Scene3D.SceneObject').

```csharp
public class Scene3DView : Tizen.UI.ViewGroup
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [Tizen.UI.NObject](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.NObject 'Tizen.UI.NObject') &#129106; [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View') &#129106; [Tizen.UI.ViewGroup](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.ViewGroup 'Tizen.UI.ViewGroup') &#129106; Scene3DView
### Constructors

<a name='Tizen.UI.Scene3D.Scene3DView.Scene3DView()'></a>

## Scene3DView() Constructor

Constructor of Scene3DView.

```csharp
public Scene3DView();
```

<a name='Tizen.UI.Scene3D.Scene3DView.Scene3DView(System.IntPtr,bool)'></a>

## Scene3DView(IntPtr, bool) Constructor

Constructor of Scene3DView with specified handle and ownership.

```csharp
public Scene3DView(System.IntPtr handle, bool ownsHandle);
```
#### Parameters

<a name='Tizen.UI.Scene3D.Scene3DView.Scene3DView(System.IntPtr,bool).handle'></a>

`handle` [System.IntPtr](https://docs.microsoft.com/en-us/dotnet/api/System.IntPtr 'System.IntPtr')

The handle of the scene view.

<a name='Tizen.UI.Scene3D.Scene3DView.Scene3DView(System.IntPtr,bool).ownsHandle'></a>

`ownsHandle` [System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

Whether the object takes ownership of the handle.
### Properties

<a name='Tizen.UI.Scene3D.Scene3DView.Cameras'></a>

## Scene3DView.Cameras Property

List of cameras in the scene.

```csharp
public System.Collections.Generic.IReadOnlyList&lt;Tizen.UI.Scene3D.Camera> Cameras { get; }
```

#### Property Value
[System.Collections.Generic.IReadOnlyList&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IReadOnlyList-1 'System.Collections.Generic.IReadOnlyList`1')[Camera](Tizen.UI.Scene3D.Camera.md 'Tizen.UI.Scene3D.Camera')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IReadOnlyList-1 'System.Collections.Generic.IReadOnlyList`1')

<a name='Tizen.UI.Scene3D.Scene3DView.DefaultCamera'></a>

## Scene3DView.DefaultCamera Property

The default camera of the scene.

```csharp
public Tizen.UI.Scene3D.Camera DefaultCamera { get; }
```

#### Property Value
[Camera](Tizen.UI.Scene3D.Camera.md 'Tizen.UI.Scene3D.Camera')

<a name='Tizen.UI.Scene3D.Scene3DView.ImageBasedLightScaleFactor'></a>

## Scene3DView.ImageBasedLightScaleFactor Property

Gets or sets the ImageBasedLight ScaleFactor.  
Scale factor controls light source intensity in [0.0f, 1.0f]

```csharp
public float ImageBasedLightScaleFactor { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Scene3D.Scene3DView.Lights'></a>

## Scene3DView.Lights Property

List of lights in the scene.

```csharp
public System.Collections.Generic.IReadOnlyList&lt;Tizen.UI.Scene3D.Light> Lights { get; }
```

#### Property Value
[System.Collections.Generic.IReadOnlyList&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IReadOnlyList-1 'System.Collections.Generic.IReadOnlyList`1')[Light](Tizen.UI.Scene3D.Light.md 'Tizen.UI.Scene3D.Light')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IReadOnlyList-1 'System.Collections.Generic.IReadOnlyList`1')

<a name='Tizen.UI.Scene3D.Scene3DView.Models'></a>

## Scene3DView.Models Property

List of models in the scene.

```csharp
public System.Collections.Generic.IReadOnlyList&lt;Tizen.UI.Scene3D.Model3D> Models { get; }
```

#### Property Value
[System.Collections.Generic.IReadOnlyList&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IReadOnlyList-1 'System.Collections.Generic.IReadOnlyList`1')[Model3D](Tizen.UI.Scene3D.Model3D.md 'Tizen.UI.Scene3D.Model3D')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IReadOnlyList-1 'System.Collections.Generic.IReadOnlyList`1')

<a name='Tizen.UI.Scene3D.Scene3DView.UseFramebuffer'></a>

## Scene3DView.UseFramebuffer Property

Gets or sets the UseFramebuffer.  
If this property is true, rendering result of Scene3DView is drawn on FBO and it is mapping on this SceneView plane.  
If this property is false, each item in Scene3DView is rendered on window directly.  
Default is false.

```csharp
public bool UseFramebuffer { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')
### Methods

<a name='Tizen.UI.Scene3D.Scene3DView.Add(Tizen.UI.Scene3D.SceneObject)'></a>

## Scene3DView.Add(SceneObject) Method

Adds a [SceneObject](Tizen.UI.Scene3D.SceneObject.md 'Tizen.UI.Scene3D.SceneObject') to the scene.

```csharp
public void Add(Tizen.UI.Scene3D.SceneObject sceneObject);
```
#### Parameters

<a name='Tizen.UI.Scene3D.Scene3DView.Add(Tizen.UI.Scene3D.SceneObject).sceneObject'></a>

`sceneObject` [SceneObject](Tizen.UI.Scene3D.SceneObject.md 'Tizen.UI.Scene3D.SceneObject')

The scene object to add.

<a name='Tizen.UI.Scene3D.Scene3DView.AnimateCameraTransition(Tizen.UI.Scene3D.Camera,int,Tizen.UI.AlphaFunction)'></a>

## Scene3DView.AnimateCameraTransition(Camera, int, AlphaFunction) Method

Transitions the [Camera](Tizen.UI.Scene3D.Camera.md 'Tizen.UI.Scene3D.Camera') to the specified camera.

```csharp
public void AnimateCameraTransition(Tizen.UI.Scene3D.Camera camera, int duration, Tizen.UI.AlphaFunction alpha=null);
```
#### Parameters

<a name='Tizen.UI.Scene3D.Scene3DView.AnimateCameraTransition(Tizen.UI.Scene3D.Camera,int,Tizen.UI.AlphaFunction).camera'></a>

`camera` [Camera](Tizen.UI.Scene3D.Camera.md 'Tizen.UI.Scene3D.Camera')

The camera to transit to.

<a name='Tizen.UI.Scene3D.Scene3DView.AnimateCameraTransition(Tizen.UI.Scene3D.Camera,int,Tizen.UI.AlphaFunction).duration'></a>

`duration` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The duration of the transition.

<a name='Tizen.UI.Scene3D.Scene3DView.AnimateCameraTransition(Tizen.UI.Scene3D.Camera,int,Tizen.UI.AlphaFunction).alpha'></a>

`alpha` [Tizen.UI.AlphaFunction](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.AlphaFunction 'Tizen.UI.AlphaFunction')

The alpha function to apply during the transition.

<a name='Tizen.UI.Scene3D.Scene3DView.GetCurrentCamera()'></a>

## Scene3DView.GetCurrentCamera() Method

Gets the current [Camera](Tizen.UI.Scene3D.Camera.md 'Tizen.UI.Scene3D.Camera') of the scene.

```csharp
public Tizen.UI.Scene3D.Camera GetCurrentCamera();
```

#### Returns
[Camera](Tizen.UI.Scene3D.Camera.md 'Tizen.UI.Scene3D.Camera')  
The current camera of the scene.

<a name='Tizen.UI.Scene3D.Scene3DView.Remove(Tizen.UI.Scene3D.SceneObject)'></a>

## Scene3DView.Remove(SceneObject) Method

Removes a [SceneObject](Tizen.UI.Scene3D.SceneObject.md 'Tizen.UI.Scene3D.SceneObject') from the scene.

```csharp
public void Remove(Tizen.UI.Scene3D.SceneObject sceneObject);
```
#### Parameters

<a name='Tizen.UI.Scene3D.Scene3DView.Remove(Tizen.UI.Scene3D.SceneObject).sceneObject'></a>

`sceneObject` [SceneObject](Tizen.UI.Scene3D.SceneObject.md 'Tizen.UI.Scene3D.SceneObject')

The scene object to remove.

<a name='Tizen.UI.Scene3D.Scene3DView.SetCurrentCamera(Tizen.UI.Scene3D.Camera)'></a>

## Scene3DView.SetCurrentCamera(Camera) Method

Sets the current [Camera](Tizen.UI.Scene3D.Camera.md 'Tizen.UI.Scene3D.Camera') of the scene.

```csharp
public void SetCurrentCamera(Tizen.UI.Scene3D.Camera camera);
```
#### Parameters

<a name='Tizen.UI.Scene3D.Scene3DView.SetCurrentCamera(Tizen.UI.Scene3D.Camera).camera'></a>

`camera` [Camera](Tizen.UI.Scene3D.Camera.md 'Tizen.UI.Scene3D.Camera')

The camera to set as the current camera.

<a name='Tizen.UI.Scene3D.Scene3DView.SetImageBasedLightingSource(string,string,float)'></a>

## Scene3DView.SetImageBasedLightingSource(string, string, float) Method

Sets the image-based lighting source.

```csharp
public void SetImageBasedLightingSource(string diffuseUrl, string specularUrl, float scaleFactor=1f);
```
#### Parameters

<a name='Tizen.UI.Scene3D.Scene3DView.SetImageBasedLightingSource(string,string,float).diffuseUrl'></a>

`diffuseUrl` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The URL of the diffuse texture.

<a name='Tizen.UI.Scene3D.Scene3DView.SetImageBasedLightingSource(string,string,float).specularUrl'></a>

`specularUrl` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The URL of the specular texture.

<a name='Tizen.UI.Scene3D.Scene3DView.SetImageBasedLightingSource(string,string,float).scaleFactor'></a>

`scaleFactor` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The scale factor of the lighting.

<a name='Tizen.UI.Scene3D.Scene3DView.SetKeyEventRouteTarget(Tizen.UI.Scene3D.Model3D)'></a>

## Scene3DView.SetKeyEventRouteTarget(Model3D) Method

Sets the Model3D target to route key event.

```csharp
public void SetKeyEventRouteTarget(Tizen.UI.Scene3D.Model3D model);
```
#### Parameters

<a name='Tizen.UI.Scene3D.Scene3DView.SetKeyEventRouteTarget(Tizen.UI.Scene3D.Model3D).model'></a>

`model` [Model3D](Tizen.UI.Scene3D.Model3D.md 'Tizen.UI.Scene3D.Model3D')
### Events

<a name='Tizen.UI.Scene3D.Scene3DView.CameraTransitionFinished'></a>

## Scene3DView.CameraTransitionFinished Event

Occurs when the camera transition is finished.

```csharp
public event EventHandler CameraTransitionFinished;
```

#### Event Type
[System.EventHandler](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler 'System.EventHandler')

<a name='Tizen.UI.Scene3D.Scene3DView.ResourceReady'></a>

## Scene3DView.ResourceReady Event

Occurs when the resource is ready.

```csharp
public event EventHandler ResourceReady;
```

#### Event Type
[System.EventHandler](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler 'System.EventHandler')





































