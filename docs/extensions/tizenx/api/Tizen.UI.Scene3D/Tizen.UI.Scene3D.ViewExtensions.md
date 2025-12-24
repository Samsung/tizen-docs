### [Tizen.UI.Scene3D](Tizen.UI.Scene3D.md 'Tizen.UI.Scene3D')

## ViewExtensions Class

```csharp
public static class ViewExtensions
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; ViewExtensions
### Methods

<a name='Tizen.UI.Scene3D.ViewExtensions.GetRotation3D(thisTizen.UI.NObject)'></a>

## ViewExtensions.GetRotation3D(this NObject) Method

Gets the rotation of the NObject in the 3D space.

```csharp
public static Tizen.UI.Scene3D.Quaternion GetRotation3D(this Tizen.UI.NObject obj);
```
#### Parameters

<a name='Tizen.UI.Scene3D.ViewExtensions.GetRotation3D(thisTizen.UI.NObject).obj'></a>

`obj` Tizen.UI.NObject

The object to get the rotation for.

#### Returns
[Quaternion](Tizen.UI.Scene3D.Quaternion.md 'Tizen.UI.Scene3D.Quaternion')  
The rotation of the object

<a name='Tizen.UI.Scene3D.ViewExtensions.GetWorldRotation3D(thisTizen.UI.NObject)'></a>

## ViewExtensions.GetWorldRotation3D(this NObject) Method

Gets the world rotation of the NObject in the 3D space.

```csharp
public static Tizen.UI.Scene3D.Quaternion GetWorldRotation3D(this Tizen.UI.NObject obj);
```
#### Parameters

<a name='Tizen.UI.Scene3D.ViewExtensions.GetWorldRotation3D(thisTizen.UI.NObject).obj'></a>

`obj` Tizen.UI.NObject

The object to get the world rotation for.

#### Returns
[Quaternion](Tizen.UI.Scene3D.Quaternion.md 'Tizen.UI.Scene3D.Quaternion')  
The world rotation of the object

<a name='Tizen.UI.Scene3D.ViewExtensions.LookAt(thisTizen.UI.View,Tizen.UI.Scene3D.Vector3D,Tizen.UI.Scene3D.Vector3D,Tizen.UI.Scene3D.Vector3D,Tizen.UI.Scene3D.Vector3D)'></a>

## ViewExtensions.LookAt(this View, Vector3D, Vector3D, Vector3D, Vector3D) Method

Rotate the View look at specific position.  
It will change the View's rotation property.

```csharp
public static void LookAt(this Tizen.UI.View view, Tizen.UI.Scene3D.Vector3D target, Tizen.UI.Scene3D.Vector3D up=default(Tizen.UI.Scene3D.Vector3D), Tizen.UI.Scene3D.Vector3D localForward=default(Tizen.UI.Scene3D.Vector3D), Tizen.UI.Scene3D.Vector3D localUp=default(Tizen.UI.Scene3D.Vector3D));
```
#### Parameters

<a name='Tizen.UI.Scene3D.ViewExtensions.LookAt(thisTizen.UI.View,Tizen.UI.Scene3D.Vector3D,Tizen.UI.Scene3D.Vector3D,Tizen.UI.Scene3D.Vector3D,Tizen.UI.Scene3D.Vector3D).view'></a>

`view` Tizen.UI.View

<a name='Tizen.UI.Scene3D.ViewExtensions.LookAt(thisTizen.UI.View,Tizen.UI.Scene3D.Vector3D,Tizen.UI.Scene3D.Vector3D,Tizen.UI.Scene3D.Vector3D,Tizen.UI.Scene3D.Vector3D).target'></a>

`target` [Vector3D](Tizen.UI.Scene3D.Vector3D.md 'Tizen.UI.Scene3D.Vector3D')

The target world position to look at.

<a name='Tizen.UI.Scene3D.ViewExtensions.LookAt(thisTizen.UI.View,Tizen.UI.Scene3D.Vector3D,Tizen.UI.Scene3D.Vector3D,Tizen.UI.Scene3D.Vector3D,Tizen.UI.Scene3D.Vector3D).up'></a>

`up` [Vector3D](Tizen.UI.Scene3D.Vector3D.md 'Tizen.UI.Scene3D.Vector3D')

The up vector after target look at. If it is null, up vector become +Y axis

<a name='Tizen.UI.Scene3D.ViewExtensions.LookAt(thisTizen.UI.View,Tizen.UI.Scene3D.Vector3D,Tizen.UI.Scene3D.Vector3D,Tizen.UI.Scene3D.Vector3D,Tizen.UI.Scene3D.Vector3D).localForward'></a>

`localForward` [Vector3D](Tizen.UI.Scene3D.Vector3D.md 'Tizen.UI.Scene3D.Vector3D')

The forward vector of View when it's rotation is not applied. If it is null, localForward vector become +Z axis

<a name='Tizen.UI.Scene3D.ViewExtensions.LookAt(thisTizen.UI.View,Tizen.UI.Scene3D.Vector3D,Tizen.UI.Scene3D.Vector3D,Tizen.UI.Scene3D.Vector3D,Tizen.UI.Scene3D.Vector3D).localUp'></a>

`localUp` [Vector3D](Tizen.UI.Scene3D.Vector3D.md 'Tizen.UI.Scene3D.Vector3D')

The up vector of View when it's rotation is not applied. If it is null, localUp vector become +Y axis

<a name='Tizen.UI.Scene3D.ViewExtensions.SetParentOrigin3D(thisTizen.UI.View,Tizen.UI.Scene3D.Point3D)'></a>

## ViewExtensions.SetParentOrigin3D(this View, Point3D) Method

Sets the parent origin of the view in 3D space.

```csharp
public static void SetParentOrigin3D(this Tizen.UI.View view, Tizen.UI.Scene3D.Point3D point);
```
#### Parameters

<a name='Tizen.UI.Scene3D.ViewExtensions.SetParentOrigin3D(thisTizen.UI.View,Tizen.UI.Scene3D.Point3D).view'></a>

`view` Tizen.UI.View

<a name='Tizen.UI.Scene3D.ViewExtensions.SetParentOrigin3D(thisTizen.UI.View,Tizen.UI.Scene3D.Point3D).point'></a>

`point` [Point3D](Tizen.UI.Scene3D.Point3D.md 'Tizen.UI.Scene3D.Point3D')

The 3D point to set the parent origin for.

<a name='Tizen.UI.Scene3D.ViewExtensions.SetPivotPoint3D(thisTizen.UI.View,Tizen.UI.Scene3D.Point3D)'></a>

## ViewExtensions.SetPivotPoint3D(this View, Point3D) Method

Sets the pivot point of the view in 3D space.

```csharp
public static void SetPivotPoint3D(this Tizen.UI.View view, Tizen.UI.Scene3D.Point3D point);
```
#### Parameters

<a name='Tizen.UI.Scene3D.ViewExtensions.SetPivotPoint3D(thisTizen.UI.View,Tizen.UI.Scene3D.Point3D).view'></a>

`view` Tizen.UI.View

<a name='Tizen.UI.Scene3D.ViewExtensions.SetPivotPoint3D(thisTizen.UI.View,Tizen.UI.Scene3D.Point3D).point'></a>

`point` [Point3D](Tizen.UI.Scene3D.Point3D.md 'Tizen.UI.Scene3D.Point3D')

The 3D point to set the pivot point for.

<a name='Tizen.UI.Scene3D.ViewExtensions.SetPosition3D(thisTizen.UI.View,float,float,float)'></a>

## ViewExtensions.SetPosition3D(this View, float, float, float) Method

Sets the position of the view in the 3D space.

```csharp
public static void SetPosition3D(this Tizen.UI.View view, float x, float y, float z);
```
#### Parameters

<a name='Tizen.UI.Scene3D.ViewExtensions.SetPosition3D(thisTizen.UI.View,float,float,float).view'></a>

`view` Tizen.UI.View

The view to set the position for.

<a name='Tizen.UI.Scene3D.ViewExtensions.SetPosition3D(thisTizen.UI.View,float,float,float).x'></a>

`x` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The X position of the view.

<a name='Tizen.UI.Scene3D.ViewExtensions.SetPosition3D(thisTizen.UI.View,float,float,float).y'></a>

`y` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The Y position of the view.

<a name='Tizen.UI.Scene3D.ViewExtensions.SetPosition3D(thisTizen.UI.View,float,float,float).z'></a>

`z` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The Z position of the view.

<a name='Tizen.UI.Scene3D.ViewExtensions.SetPosition3D(thisTizen.UI.View,Tizen.UI.Scene3D.Point3D)'></a>

## ViewExtensions.SetPosition3D(this View, Point3D) Method

Sets the position of the view in the 3D space.

```csharp
public static void SetPosition3D(this Tizen.UI.View view, Tizen.UI.Scene3D.Point3D point);
```
#### Parameters

<a name='Tizen.UI.Scene3D.ViewExtensions.SetPosition3D(thisTizen.UI.View,Tizen.UI.Scene3D.Point3D).view'></a>

`view` Tizen.UI.View

The view to set the position for.

<a name='Tizen.UI.Scene3D.ViewExtensions.SetPosition3D(thisTizen.UI.View,Tizen.UI.Scene3D.Point3D).point'></a>

`point` [Point3D](Tizen.UI.Scene3D.Point3D.md 'Tizen.UI.Scene3D.Point3D')

The position of the view.

<a name='Tizen.UI.Scene3D.ViewExtensions.SetPositionZ(thisTizen.UI.View,float)'></a>

## ViewExtensions.SetPositionZ(this View, float) Method

Sets the Z position of the view in the 3D space.

```csharp
public static void SetPositionZ(this Tizen.UI.View view, float positionZ);
```
#### Parameters

<a name='Tizen.UI.Scene3D.ViewExtensions.SetPositionZ(thisTizen.UI.View,float).view'></a>

`view` Tizen.UI.View

The view to set the position for.

<a name='Tizen.UI.Scene3D.ViewExtensions.SetPositionZ(thisTizen.UI.View,float).positionZ'></a>

`positionZ` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The Z position of the view.

<a name='Tizen.UI.Scene3D.ViewExtensions.SetRotation3D(thisTizen.UI.View,Tizen.UI.Scene3D.Quaternion)'></a>

## ViewExtensions.SetRotation3D(this View, Quaternion) Method

Sets the rotation of the view in the 3D space.

```csharp
public static void SetRotation3D(this Tizen.UI.View view, Tizen.UI.Scene3D.Quaternion quaternion);
```
#### Parameters

<a name='Tizen.UI.Scene3D.ViewExtensions.SetRotation3D(thisTizen.UI.View,Tizen.UI.Scene3D.Quaternion).view'></a>

`view` Tizen.UI.View

The view to set the rotation for.

<a name='Tizen.UI.Scene3D.ViewExtensions.SetRotation3D(thisTizen.UI.View,Tizen.UI.Scene3D.Quaternion).quaternion'></a>

`quaternion` [Quaternion](Tizen.UI.Scene3D.Quaternion.md 'Tizen.UI.Scene3D.Quaternion')

The rotation of the view.

<a name='Tizen.UI.Scene3D.ViewExtensions.SetScale3D(thisTizen.UI.View,float,float,float)'></a>

## ViewExtensions.SetScale3D(this View, float, float, float) Method

Sets the scale of the view in the 3D space.

```csharp
public static void SetScale3D(this Tizen.UI.View view, float x, float y, float z);
```
#### Parameters

<a name='Tizen.UI.Scene3D.ViewExtensions.SetScale3D(thisTizen.UI.View,float,float,float).view'></a>

`view` Tizen.UI.View

The view to set the scale for.

<a name='Tizen.UI.Scene3D.ViewExtensions.SetScale3D(thisTizen.UI.View,float,float,float).x'></a>

`x` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The X scale of the view.

<a name='Tizen.UI.Scene3D.ViewExtensions.SetScale3D(thisTizen.UI.View,float,float,float).y'></a>

`y` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The Y scale of the view.

<a name='Tizen.UI.Scene3D.ViewExtensions.SetScale3D(thisTizen.UI.View,float,float,float).z'></a>

`z` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The Z scale of the view.

<a name='Tizen.UI.Scene3D.ViewExtensions.SetScale3D(thisTizen.UI.View,Tizen.UI.Scene3D.Size3D)'></a>

## ViewExtensions.SetScale3D(this View, Size3D) Method

Sets the scale of the view in the 3D space.

```csharp
public static void SetScale3D(this Tizen.UI.View view, Tizen.UI.Scene3D.Size3D scale);
```
#### Parameters

<a name='Tizen.UI.Scene3D.ViewExtensions.SetScale3D(thisTizen.UI.View,Tizen.UI.Scene3D.Size3D).view'></a>

`view` Tizen.UI.View

The view to set the scale for.

<a name='Tizen.UI.Scene3D.ViewExtensions.SetScale3D(thisTizen.UI.View,Tizen.UI.Scene3D.Size3D).scale'></a>

`scale` [Size3D](Tizen.UI.Scene3D.Size3D.md 'Tizen.UI.Scene3D.Size3D')

The scale of the view.

<a name='Tizen.UI.Scene3D.ViewExtensions.SetScaleZ(thisTizen.UI.View,float)'></a>

## ViewExtensions.SetScaleZ(this View, float) Method

Sets the Z scale of the view in the 3D space.

```csharp
public static void SetScaleZ(this Tizen.UI.View view, float scaleZ);
```
#### Parameters

<a name='Tizen.UI.Scene3D.ViewExtensions.SetScaleZ(thisTizen.UI.View,float).view'></a>

`view` Tizen.UI.View

The view to set the scale for.

<a name='Tizen.UI.Scene3D.ViewExtensions.SetScaleZ(thisTizen.UI.View,float).scaleZ'></a>

`scaleZ` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The Z scale of the view.

<a name='Tizen.UI.Scene3D.ViewExtensions.SetSize3D(thisTizen.UI.View,Tizen.UI.Scene3D.Size3D)'></a>

## ViewExtensions.SetSize3D(this View, Size3D) Method

Sets the size of the view in the 3D space.

```csharp
public static void SetSize3D(this Tizen.UI.View view, Tizen.UI.Scene3D.Size3D size);
```
#### Parameters

<a name='Tizen.UI.Scene3D.ViewExtensions.SetSize3D(thisTizen.UI.View,Tizen.UI.Scene3D.Size3D).view'></a>

`view` Tizen.UI.View

The view to set the size for.

<a name='Tizen.UI.Scene3D.ViewExtensions.SetSize3D(thisTizen.UI.View,Tizen.UI.Scene3D.Size3D).size'></a>

`size` [Size3D](Tizen.UI.Scene3D.Size3D.md 'Tizen.UI.Scene3D.Size3D')

The size of the view.






































