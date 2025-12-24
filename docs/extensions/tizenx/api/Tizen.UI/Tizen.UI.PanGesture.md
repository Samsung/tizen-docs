### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## PanGesture Class

The PanGesture class represents a pan gesture event.

```csharp
public class PanGesture : Tizen.UI.Gesture
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [NObject](Tizen.UI.NObject.md 'Tizen.UI.NObject') &#129106; [Gesture](Tizen.UI.Gesture.md 'Tizen.UI.Gesture') &#129106; PanGesture
### Constructors

<a name='Tizen.UI.PanGesture.PanGesture(System.IntPtr,bool)'></a>

## PanGesture(IntPtr, bool) Constructor

Initializes a new instance of the PanGesture class.

```csharp
public PanGesture(System.IntPtr handle, bool ownsHandle);
```
#### Parameters

<a name='Tizen.UI.PanGesture.PanGesture(System.IntPtr,bool).handle'></a>

`handle` [System.IntPtr](https://docs.microsoft.com/en-us/dotnet/api/System.IntPtr 'System.IntPtr')

The handle of the native pan gesture.

<a name='Tizen.UI.PanGesture.PanGesture(System.IntPtr,bool).ownsHandle'></a>

`ownsHandle` [System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

Whether the handle is owned by the new instance.
### Properties

<a name='Tizen.UI.PanGesture.Displacement'></a>

## PanGesture.Displacement Property

Gets the displacement of the pan gesture.

```csharp
public Tizen.UI.Point Displacement { get; }
```

#### Property Value
[Point](Tizen.UI.Point.md 'Tizen.UI.Point')

<a name='Tizen.UI.PanGesture.NumberOfTouches'></a>

## PanGesture.NumberOfTouches Property

Gets the number of touches of the pan gesture.

```csharp
public int NumberOfTouches { get; }
```

#### Property Value
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

<a name='Tizen.UI.PanGesture.Position'></a>

## PanGesture.Position Property

Gets the position of the pan gesture.

```csharp
public Tizen.UI.Point Position { get; }
```

#### Property Value
[Point](Tizen.UI.Point.md 'Tizen.UI.Point')

<a name='Tizen.UI.PanGesture.ScreenDisplacement'></a>

## PanGesture.ScreenDisplacement Property

Gets the screen displacement of the pan gesture.

```csharp
public Tizen.UI.Point ScreenDisplacement { get; }
```

#### Property Value
[Point](Tizen.UI.Point.md 'Tizen.UI.Point')

<a name='Tizen.UI.PanGesture.ScreenPosition'></a>

## PanGesture.ScreenPosition Property

Gets the screen position of the pan gesture.

```csharp
public Tizen.UI.Point ScreenPosition { get; }
```

#### Property Value
[Point](Tizen.UI.Point.md 'Tizen.UI.Point')

<a name='Tizen.UI.PanGesture.ScreenVelocity'></a>

## PanGesture.ScreenVelocity Property

Gets the screen velocity of the pan gesture.

```csharp
public Tizen.UI.Point ScreenVelocity { get; }
```

#### Property Value
[Point](Tizen.UI.Point.md 'Tizen.UI.Point')

<a name='Tizen.UI.PanGesture.Velocity'></a>

## PanGesture.Velocity Property

Gets the velocity of the pan gesture.

```csharp
public Tizen.UI.Point Velocity { get; }
```

#### Property Value
[Point](Tizen.UI.Point.md 'Tizen.UI.Point')






