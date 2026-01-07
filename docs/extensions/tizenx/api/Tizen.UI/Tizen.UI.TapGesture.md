### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## TapGesture Class

The TapGesture class represents a gesture that recognizes a single tap on the screen.

```csharp
public class TapGesture : Tizen.UI.Gesture
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [NObject](Tizen.UI.NObject.md 'Tizen.UI.NObject') &#129106; [Gesture](Tizen.UI.Gesture.md 'Tizen.UI.Gesture') &#129106; TapGesture
### Constructors

<a name='Tizen.UI.TapGesture.TapGesture(System.IntPtr,bool)'></a>

## TapGesture(IntPtr, bool) Constructor

Initializes a new instance of the TapGesture class with the specified handle and ownership flag.

```csharp
public TapGesture(System.IntPtr handle, bool ownsHandle);
```
#### Parameters

<a name='Tizen.UI.TapGesture.TapGesture(System.IntPtr,bool).handle'></a>

`handle` [System.IntPtr](https://docs.microsoft.com/en-us/dotnet/api/System.IntPtr 'System.IntPtr')

The handle of the native Tap gesture.

<a name='Tizen.UI.TapGesture.TapGesture(System.IntPtr,bool).ownsHandle'></a>

`ownsHandle` [System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

Whether the handle is owned by the new instance.
### Properties

<a name='Tizen.UI.TapGesture.NumberOfTaps'></a>

## TapGesture.NumberOfTaps Property

Gets the number of taps recognized by the gesture.

```csharp
public int NumberOfTaps { get; }
```

#### Property Value
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

<a name='Tizen.UI.TapGesture.Position'></a>

## TapGesture.Position Property

Gets the local position of the tap gesture.

```csharp
public Tizen.UI.Point Position { get; }
```

#### Property Value
[Point](Tizen.UI.Point.md 'Tizen.UI.Point')

<a name='Tizen.UI.TapGesture.ScreenPosition'></a>

## TapGesture.ScreenPosition Property

Gets the screen position of the tap gesture.

```csharp
public Tizen.UI.Point ScreenPosition { get; }
```

#### Property Value
[Point](Tizen.UI.Point.md 'Tizen.UI.Point')






