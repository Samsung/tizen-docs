### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## RotationGesture Class

The RotationGesture class represents a rotation gesture.

```csharp
public class RotationGesture : Tizen.UI.Gesture
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [NObject](Tizen.UI.NObject.md 'Tizen.UI.NObject') &#129106; [Gesture](Tizen.UI.Gesture.md 'Tizen.UI.Gesture') &#129106; RotationGesture
### Constructors

<a name='Tizen.UI.RotationGesture.RotationGesture(System.IntPtr,bool)'></a>

## RotationGesture(IntPtr, bool) Constructor

Initializes a new instance of the RotationGesture class with the specified handle and whether it owns the handle or not.

```csharp
public RotationGesture(System.IntPtr handle, bool ownsHandle);
```
#### Parameters

<a name='Tizen.UI.RotationGesture.RotationGesture(System.IntPtr,bool).handle'></a>

`handle` [System.IntPtr](https://docs.microsoft.com/en-us/dotnet/api/System.IntPtr 'System.IntPtr')

The handle of the native gesture object.

<a name='Tizen.UI.RotationGesture.RotationGesture(System.IntPtr,bool).ownsHandle'></a>

`ownsHandle` [System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

Whether the handle is owned by the new instance or not.
### Properties

<a name='Tizen.UI.RotationGesture.Center'></a>

## RotationGesture.Center Property

Gets the center point of the gesture in local coordinates.

```csharp
public Tizen.UI.Point Center { get; }
```

#### Property Value
[Point](Tizen.UI.Point.md 'Tizen.UI.Point')

<a name='Tizen.UI.RotationGesture.Rotation'></a>

## RotationGesture.Rotation Property

Gets the rotation angle of the gesture in degrees.

```csharp
public float Rotation { get; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.RotationGesture.ScreenCenter'></a>

## RotationGesture.ScreenCenter Property

Gets the center point of the gesture in screen coordinates.

```csharp
public Tizen.UI.Point ScreenCenter { get; }
```

#### Property Value
[Point](Tizen.UI.Point.md 'Tizen.UI.Point')






