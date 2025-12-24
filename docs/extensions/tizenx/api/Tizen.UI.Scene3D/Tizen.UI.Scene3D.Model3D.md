### [Tizen.UI.Scene3D](Tizen.UI.Scene3D.md 'Tizen.UI.Scene3D')

## Model3D Class

Provides functionality for 3-D models.

```csharp
public class Model3D : Tizen.UI.Scene3D.SceneObjectGroup&lt;Tizen.UI.Scene3D.SceneObject>
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; Tizen.UI.NObject &#129106; [SceneObject](Tizen.UI.Scene3D.SceneObject.md 'Tizen.UI.Scene3D.SceneObject') &#129106; [Tizen.UI.Scene3D.SceneObjectGroup&lt;](Tizen.UI.Scene3D.SceneObjectGroup_T_.md 'Tizen.UI.Scene3D.SceneObjectGroup&lt;T>')[SceneObject](Tizen.UI.Scene3D.SceneObject.md 'Tizen.UI.Scene3D.SceneObject')[&gt;](Tizen.UI.Scene3D.SceneObjectGroup_T_.md 'Tizen.UI.Scene3D.SceneObjectGroup&lt;T>') &#129106; Model3D
### Constructors

<a name='Tizen.UI.Scene3D.Model3D.Model3D()'></a>

## Model3D() Constructor

Initializes a new instance of the Model3D class.

```csharp
public Model3D();
```

<a name='Tizen.UI.Scene3D.Model3D.Model3D(string,string)'></a>

## Model3D(string, string) Constructor

Initializes a new instance of the Model3D class with a specified model URL and resource directory URL.

```csharp
public Model3D(string modelUrl, string resourceDirectoryUrl="");
```
#### Parameters

<a name='Tizen.UI.Scene3D.Model3D.Model3D(string,string).modelUrl'></a>

`modelUrl` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The URL of the model file.

<a name='Tizen.UI.Scene3D.Model3D.Model3D(string,string).resourceDirectoryUrl'></a>

`resourceDirectoryUrl` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The URL of the directory containing the model's resources.
### Properties

<a name='Tizen.UI.Scene3D.Model3D.IsResourceReady'></a>

## Model3D.IsResourceReady Property

Queries if all resources required by a Model3D are loaded and ready.

```csharp
public bool IsResourceReady { get; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Scene3D.Model3D.MultipliedColor'></a>

## Model3D.MultipliedColor Property

Gets or sets the multiplied color of the model.

```csharp
public Tizen.UI.Color MultipliedColor { get; set; }
```

#### Property Value
Tizen.UI.Color

<a name='Tizen.UI.Scene3D.Model3D.RootNode'></a>

## Model3D.RootNode Property

Retrieves root ModelNode of this Model.

```csharp
public Tizen.UI.Scene3D.ModelNode RootNode { get; }
```

#### Property Value
[ModelNode](Tizen.UI.Scene3D.ModelNode.md 'Tizen.UI.Scene3D.ModelNode')
### Methods

<a name='Tizen.UI.Scene3D.Model3D.ApplyCamera(int,Tizen.UI.Scene3D.Camera)'></a>

## Model3D.ApplyCamera(int, Camera) Method

Applies the camera at the specified index to the specified camera.

```csharp
public bool ApplyCamera(int index, Tizen.UI.Scene3D.Camera camera);
```
#### Parameters

<a name='Tizen.UI.Scene3D.Model3D.ApplyCamera(int,Tizen.UI.Scene3D.Camera).index'></a>

`index` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The index of the camera to apply.

<a name='Tizen.UI.Scene3D.Model3D.ApplyCamera(int,Tizen.UI.Scene3D.Camera).camera'></a>

`camera` [Camera](Tizen.UI.Scene3D.Camera.md 'Tizen.UI.Scene3D.Camera')

The camera to apply the camera to.

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
True if the camera was applied successfully, false otherwise.

<a name='Tizen.UI.Scene3D.Model3D.GetAnimation(int)'></a>

## Model3D.GetAnimation(int) Method

Gets the animation at the specified index.

```csharp
public Tizen.UI.Scene3D.Animation3D GetAnimation(int index);
```
#### Parameters

<a name='Tizen.UI.Scene3D.Model3D.GetAnimation(int).index'></a>

`index` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The index of the animation.

#### Returns
[Animation3D](Tizen.UI.Scene3D.Animation3D.md 'Tizen.UI.Scene3D.Animation3D')  
The animation at the specified index.

<a name='Tizen.UI.Scene3D.Model3D.GetAnimation(string)'></a>

## Model3D.GetAnimation(string) Method

Gets the animation at the specified name.

```csharp
public Tizen.UI.Scene3D.Animation3D GetAnimation(string name);
```
#### Parameters

<a name='Tizen.UI.Scene3D.Model3D.GetAnimation(string).name'></a>

`name` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The name of the animation.

#### Returns
[Animation3D](Tizen.UI.Scene3D.Animation3D.md 'Tizen.UI.Scene3D.Animation3D')  
The animation at the specified name.

<a name='Tizen.UI.Scene3D.Model3D.GetAnimationCount()'></a>

## Model3D.GetAnimationCount() Method

Gets the number of animations in the model.

```csharp
public int GetAnimationCount();
```

#### Returns
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')  
The number of animations in the model.

<a name='Tizen.UI.Scene3D.Model3D.GetCameraCount()'></a>

## Model3D.GetCameraCount() Method

Gets the number of cameras in the model.

```csharp
public int GetCameraCount();
```

#### Returns
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')  
The number of cameras in the model.

<a name='Tizen.UI.Scene3D.Model3D.LoadMotionDataAnimation(Tizen.UI.Scene3D.IMotionData)'></a>

## Model3D.LoadMotionDataAnimation(IMotionData) Method

Generate animation by MotionData.

```csharp
public Tizen.UI.Scene3D.Animation3D LoadMotionDataAnimation(Tizen.UI.Scene3D.IMotionData motionData);
```
#### Parameters

<a name='Tizen.UI.Scene3D.Model3D.LoadMotionDataAnimation(Tizen.UI.Scene3D.IMotionData).motionData'></a>

`motionData` [IMotionData](Tizen.UI.Scene3D.IMotionData.md 'Tizen.UI.Scene3D.IMotionData')

Source motion data.

#### Returns
[Animation3D](Tizen.UI.Scene3D.Animation3D.md 'Tizen.UI.Scene3D.Animation3D')  
Generated animation from then given motion data, or null if there is no animatable item in [motionData](Tizen.UI.Scene3D.Model3D.md#Tizen.UI.Scene3D.Model3D.LoadMotionDataAnimation(Tizen.UI.Scene3D.IMotionData).motionData 'Tizen.UI.Scene3D.Model3D.LoadMotionDataAnimation(Tizen.UI.Scene3D.IMotionData).motionData')
### Events

<a name='Tizen.UI.Scene3D.Model3D.KeyEvent'></a>

## Model3D.KeyEvent Event

Occurs when a key event is received by the Model3D.

```csharp
public event EventHandler&lt;KeyEventArgs> KeyEvent;
```

#### Event Type
[System.EventHandler&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')Tizen.UI.KeyEventArgs[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')

<a name='Tizen.UI.Scene3D.Model3D.ResourceReady'></a>

## Model3D.ResourceReady Event

Occurs when the resources required by the model are ready.

```csharp
public event EventHandler ResourceReady;
```

#### Event Type
[System.EventHandler](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler 'System.EventHandler')

<a name='Tizen.UI.Scene3D.Model3D.TouchEvent'></a>

## Model3D.TouchEvent Event

Occurs when a touch event is received by the scene object.

```csharp
public event EventHandler&lt;TouchEventArgs> TouchEvent;
```

#### Event Type
[System.EventHandler&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')Tizen.UI.TouchEventArgs[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')






































