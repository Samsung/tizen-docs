### [Tizen.UI.Scene3D](Tizen.UI.Scene3D.md 'Tizen.UI.Scene3D')

## SceneObject Class

[SceneObject](Tizen.UI.Scene3D.SceneObject.md 'Tizen.UI.Scene3D.SceneObject') is a base class for all scene 3D objects.

```csharp
public abstract class SceneObject : Tizen.UI.NObject
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; Tizen.UI.NObject &#129106; SceneObject

Derived  
&#8627; [Camera](Tizen.UI.Scene3D.Camera.md 'Tizen.UI.Scene3D.Camera')  
&#8627; [Light](Tizen.UI.Scene3D.Light.md 'Tizen.UI.Scene3D.Light')  
&#8627; [Panel](Tizen.UI.Scene3D.Panel.md 'Tizen.UI.Scene3D.Panel')  
&#8627; [SceneObjectGroup&lt;T&gt;](Tizen.UI.Scene3D.SceneObjectGroup_T_.md 'Tizen.UI.Scene3D.SceneObjectGroup&lt;T>')
### Properties

<a name='Tizen.UI.Scene3D.SceneObject.IsVisible'></a>

## SceneObject.IsVisible Property

Gets or sets a value indicating whether the SceneObject is visible or not.

```csharp
public bool IsVisible { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Scene3D.SceneObject.Name'></a>

## SceneObject.Name Property

Gets or sets the name of the scene object.

```csharp
public string Name { get; set; }
```

#### Property Value
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.Scene3D.SceneObject.Opacity'></a>

## SceneObject.Opacity Property

Gets or sets the opacity of the scene object.

```csharp
public float Opacity { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Scene3D.SceneObject.Parent'></a>

## SceneObject.Parent Property

Gets the parent of the scene object.

```csharp
public Tizen.UI.Scene3D.SceneObject Parent { get; }
```

#### Property Value
[SceneObject](Tizen.UI.Scene3D.SceneObject.md 'Tizen.UI.Scene3D.SceneObject')

<a name='Tizen.UI.Scene3D.SceneObject.ParentObject'></a>

## SceneObject.ParentObject Property

Gets the parent object of the scene object.

```csharp
public Tizen.UI.NObject ParentObject { get; }
```

#### Property Value
Tizen.UI.NObject

<a name='Tizen.UI.Scene3D.SceneObject.ParentOrigin'></a>

## SceneObject.ParentOrigin Property

Gets or sets the parent origin of the scene object.

```csharp
public Tizen.UI.Scene3D.Point3D ParentOrigin { get; set; }
```

#### Property Value
[Point3D](Tizen.UI.Scene3D.Point3D.md 'Tizen.UI.Scene3D.Point3D')

<a name='Tizen.UI.Scene3D.SceneObject.PivotPoint'></a>

## SceneObject.PivotPoint Property

Gets or sets the pivot point of the scene object.

```csharp
public Tizen.UI.Scene3D.Point3D PivotPoint { get; set; }
```

#### Property Value
[Point3D](Tizen.UI.Scene3D.Point3D.md 'Tizen.UI.Scene3D.Point3D')

### Remarks
The pivot point is the center point around which the scene object rotates or scales. When a rotation or scaling operation is applied to the scene object,  
it is performed relative to the pivot point. By changing the pivot point, you can control the origin and behavior of the rotation or scaling.

<a name='Tizen.UI.Scene3D.SceneObject.Position'></a>

## SceneObject.Position Property

Gets or sets the position of the scene object.

```csharp
public Tizen.UI.Scene3D.Point3D Position { get; set; }
```

#### Property Value
[Point3D](Tizen.UI.Scene3D.Point3D.md 'Tizen.UI.Scene3D.Point3D')

<a name='Tizen.UI.Scene3D.SceneObject.PositionUsesPivotPoint'></a>

## SceneObject.PositionUsesPivotPoint Property

Gets or sets a value indicating whether the position of the scene object uses the pivot point.

```csharp
public bool PositionUsesPivotPoint { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Scene3D.SceneObject.Rotation'></a>

## SceneObject.Rotation Property

Gets or sets the rotation of the scene object.

```csharp
public Tizen.UI.Scene3D.Quaternion Rotation { get; set; }
```

#### Property Value
[Quaternion](Tizen.UI.Scene3D.Quaternion.md 'Tizen.UI.Scene3D.Quaternion')

<a name='Tizen.UI.Scene3D.SceneObject.Scale'></a>

## SceneObject.Scale Property

Gets or sets the scale factor applied to the scene object.

```csharp
public Tizen.UI.Scene3D.Size3D Scale { get; set; }
```

#### Property Value
[Size3D](Tizen.UI.Scene3D.Size3D.md 'Tizen.UI.Scene3D.Size3D')

<a name='Tizen.UI.Scene3D.SceneObject.Size'></a>

## SceneObject.Size Property

Gets or sets the size of the scene object.

```csharp
public Tizen.UI.Scene3D.Size3D Size { get; set; }
```

#### Property Value
[Size3D](Tizen.UI.Scene3D.Size3D.md 'Tizen.UI.Scene3D.Size3D')
### Methods

<a name='Tizen.UI.Scene3D.SceneObject.LookAt(Tizen.UI.Scene3D.Vector3D,Tizen.UI.Scene3D.Vector3D,Tizen.UI.Scene3D.Vector3D,Tizen.UI.Scene3D.Vector3D)'></a>

## SceneObject.LookAt(Vector3D, Vector3D, Vector3D, Vector3D) Method

Rotate the SceneObject look at specific position.  
It will change the SceneObject's orientation property.

```csharp
public void LookAt(Tizen.UI.Scene3D.Vector3D target, Tizen.UI.Scene3D.Vector3D up=default(Tizen.UI.Scene3D.Vector3D), Tizen.UI.Scene3D.Vector3D localForward=default(Tizen.UI.Scene3D.Vector3D), Tizen.UI.Scene3D.Vector3D localUp=default(Tizen.UI.Scene3D.Vector3D));
```
#### Parameters

<a name='Tizen.UI.Scene3D.SceneObject.LookAt(Tizen.UI.Scene3D.Vector3D,Tizen.UI.Scene3D.Vector3D,Tizen.UI.Scene3D.Vector3D,Tizen.UI.Scene3D.Vector3D).target'></a>

`target` [Vector3D](Tizen.UI.Scene3D.Vector3D.md 'Tizen.UI.Scene3D.Vector3D')

The target world position to look at.

<a name='Tizen.UI.Scene3D.SceneObject.LookAt(Tizen.UI.Scene3D.Vector3D,Tizen.UI.Scene3D.Vector3D,Tizen.UI.Scene3D.Vector3D,Tizen.UI.Scene3D.Vector3D).up'></a>

`up` [Vector3D](Tizen.UI.Scene3D.Vector3D.md 'Tizen.UI.Scene3D.Vector3D')

The up vector after target look at. If it is null, up vector become +Y axis

<a name='Tizen.UI.Scene3D.SceneObject.LookAt(Tizen.UI.Scene3D.Vector3D,Tizen.UI.Scene3D.Vector3D,Tizen.UI.Scene3D.Vector3D,Tizen.UI.Scene3D.Vector3D).localForward'></a>

`localForward` [Vector3D](Tizen.UI.Scene3D.Vector3D.md 'Tizen.UI.Scene3D.Vector3D')

The forward vector of scene object when it's orientation is not applied. If it is null, localForward vector become +Z axis

<a name='Tizen.UI.Scene3D.SceneObject.LookAt(Tizen.UI.Scene3D.Vector3D,Tizen.UI.Scene3D.Vector3D,Tizen.UI.Scene3D.Vector3D,Tizen.UI.Scene3D.Vector3D).localUp'></a>

`localUp` [Vector3D](Tizen.UI.Scene3D.Vector3D.md 'Tizen.UI.Scene3D.Vector3D')

The up vector of SceneObject when it's orientation is not applied. If it is null, localUp vector become +Y axis






































