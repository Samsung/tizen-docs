### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## LongPressGesture Class

The LongPressGesture class represents a long press gesture.

```csharp
public class LongPressGesture : Tizen.UI.Gesture
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [NObject](Tizen.UI.NObject.md 'Tizen.UI.NObject') &#129106; [Gesture](Tizen.UI.Gesture.md 'Tizen.UI.Gesture') &#129106; LongPressGesture
### Constructors

<a name='Tizen.UI.LongPressGesture.LongPressGesture(System.IntPtr,bool)'></a>

## LongPressGesture(IntPtr, bool) Constructor

Initializes a new instance of the LongPressGesture class with the specified handle and whether it owns the handle or not.

```csharp
public LongPressGesture(System.IntPtr handle, bool ownsHandle);
```
#### Parameters

<a name='Tizen.UI.LongPressGesture.LongPressGesture(System.IntPtr,bool).handle'></a>

`handle` [System.IntPtr](https://docs.microsoft.com/en-us/dotnet/api/System.IntPtr 'System.IntPtr')

The handle of the long press gesture.

<a name='Tizen.UI.LongPressGesture.LongPressGesture(System.IntPtr,bool).ownsHandle'></a>

`ownsHandle` [System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

Whether the handle is owned by the new instance or not.
### Properties

<a name='Tizen.UI.LongPressGesture.NumberOfTouches'></a>

## LongPressGesture.NumberOfTouches Property

Gets the number of touches associated with the long press gesture.

```csharp
public int NumberOfTouches { get; }
```

#### Property Value
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

<a name='Tizen.UI.LongPressGesture.Position'></a>

## LongPressGesture.Position Property

Gets the local position of the long press gesture.

```csharp
public Tizen.UI.Point Position { get; }
```

#### Property Value
[Point](Tizen.UI.Point.md 'Tizen.UI.Point')

<a name='Tizen.UI.LongPressGesture.ScreenPosition'></a>

## LongPressGesture.ScreenPosition Property

Gets the screen position of the long press gesture.

```csharp
public Tizen.UI.Point ScreenPosition { get; }
```

#### Property Value
[Point](Tizen.UI.Point.md 'Tizen.UI.Point')






