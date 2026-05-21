### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## PinchGesture Class

The PinchGesture class represents a pinch gesture event.

```csharp
public class PinchGesture : Tizen.UI.Gesture
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [NObject](Tizen.UI.NObject.md 'Tizen.UI.NObject') &#129106; [Gesture](Tizen.UI.Gesture.md 'Tizen.UI.Gesture') &#129106; PinchGesture
### Constructors

<a name='Tizen.UI.PinchGesture.PinchGesture(System.IntPtr,bool)'></a>

## PinchGesture(IntPtr, bool) Constructor

Initializes a new instance of the PinchGesture class with the specified native handle and ownership flag.

```csharp
public PinchGesture(System.IntPtr handle, bool ownsHandle);
```
#### Parameters

<a name='Tizen.UI.PinchGesture.PinchGesture(System.IntPtr,bool).handle'></a>

`handle` [System.IntPtr](https://docs.microsoft.com/en-us/dotnet/api/System.IntPtr 'System.IntPtr')

handle of the pinch gesture.

<a name='Tizen.UI.PinchGesture.PinchGesture(System.IntPtr,bool).ownsHandle'></a>

`ownsHandle` [System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

Whether the new instance takes ownership of the native handle.
### Properties

<a name='Tizen.UI.PinchGesture.Center'></a>

## PinchGesture.Center Property

Gets the local center point of the pinch gesture.

```csharp
public Tizen.UI.Point Center { get; }
```

#### Property Value
[Point](Tizen.UI.Point.md 'Tizen.UI.Point')

<a name='Tizen.UI.PinchGesture.Scale'></a>

## PinchGesture.Scale Property

Gets the scale factor of the pinch gesture.

```csharp
public float Scale { get; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.PinchGesture.ScreenCenter'></a>

## PinchGesture.ScreenCenter Property

Gets the screen center point of the pinch gesture.

```csharp
public Tizen.UI.Point ScreenCenter { get; }
```

#### Property Value
[Point](Tizen.UI.Point.md 'Tizen.UI.Point')

<a name='Tizen.UI.PinchGesture.Speed'></a>

## PinchGesture.Speed Property

Gets the speed of the pinch gesture.

```csharp
public float Speed { get; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')






