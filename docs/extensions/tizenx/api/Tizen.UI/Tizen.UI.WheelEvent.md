### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## WheelEvent Class

WheelEvent class provides information about wheel events.

```csharp
public class WheelEvent : Tizen.UI.NObject
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [NObject](Tizen.UI.NObject.md 'Tizen.UI.NObject') &#129106; WheelEvent
### Constructors

<a name='Tizen.UI.WheelEvent.WheelEvent(System.IntPtr,bool)'></a>

## WheelEvent(IntPtr, bool) Constructor

Constructor for creating WheelEvent object from native handle.

```csharp
public WheelEvent(System.IntPtr handle, bool ownsHandle);
```
#### Parameters

<a name='Tizen.UI.WheelEvent.WheelEvent(System.IntPtr,bool).handle'></a>

`handle` [System.IntPtr](https://docs.microsoft.com/en-us/dotnet/api/System.IntPtr 'System.IntPtr')

Native handle of wheel event

<a name='Tizen.UI.WheelEvent.WheelEvent(System.IntPtr,bool).ownsHandle'></a>

`ownsHandle` [System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

Whether the object takes ownership of the handle
### Properties

<a name='Tizen.UI.WheelEvent.Delta'></a>

## WheelEvent.Delta Property

Gets the delta value of wheel event.

```csharp
public int Delta { get; }
```

#### Property Value
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

<a name='Tizen.UI.WheelEvent.Direction'></a>

## WheelEvent.Direction Property

Gets the direction of wheel event.

```csharp
public Tizen.UI.WheelDirection Direction { get; }
```

#### Property Value
[WheelDirection](Tizen.UI.WheelDirection.md 'Tizen.UI.WheelDirection')

<a name='Tizen.UI.WheelEvent.IsAltModifier'></a>

## WheelEvent.IsAltModifier Property

Checks if the alt modifier key is pressed.

```csharp
public bool IsAltModifier { get; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.WheelEvent.IsCtrlModifier'></a>

## WheelEvent.IsCtrlModifier Property

Checks if the ctrl modifier key is pressed.

```csharp
public bool IsCtrlModifier { get; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.WheelEvent.IsShiftModifier'></a>

## WheelEvent.IsShiftModifier Property

Checks if the shift modifier key is pressed.

```csharp
public bool IsShiftModifier { get; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.WheelEvent.Modifier'></a>

## WheelEvent.Modifier Property

Gets the modifier key of wheel event.

```csharp
public uint Modifier { get; }
```

#### Property Value
[System.UInt32](https://docs.microsoft.com/en-us/dotnet/api/System.UInt32 'System.UInt32')

<a name='Tizen.UI.WheelEvent.Position'></a>

## WheelEvent.Position Property

Gets the position of wheel event.

```csharp
public Tizen.UI.Point Position { get; }
```

#### Property Value
[Point](Tizen.UI.Point.md 'Tizen.UI.Point')

<a name='Tizen.UI.WheelEvent.Time'></a>

## WheelEvent.Time Property

Gets the time stamp of wheel event.

```csharp
public uint Time { get; }
```

#### Property Value
[System.UInt32](https://docs.microsoft.com/en-us/dotnet/api/System.UInt32 'System.UInt32')

<a name='Tizen.UI.WheelEvent.WheelType'></a>

## WheelEvent.WheelType Property

Gets the type of wheel event.

```csharp
public Tizen.UI.WheelType WheelType { get; }
```

#### Property Value
[WheelType](Tizen.UI.WheelType.md 'Tizen.UI.WheelType')






