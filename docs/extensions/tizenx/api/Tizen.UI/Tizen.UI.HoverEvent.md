### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## HoverEvent Class

The HoverEvent class represents a hover event that contains information about the hover points.

```csharp
public class HoverEvent : Tizen.UI.NObject
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [NObject](Tizen.UI.NObject.md 'Tizen.UI.NObject') &#129106; HoverEvent
### Constructors

<a name='Tizen.UI.HoverEvent.HoverEvent()'></a>

## HoverEvent() Constructor

Initializes a new instance of the HoverEvent class

```csharp
public HoverEvent();
```

<a name='Tizen.UI.HoverEvent.HoverEvent(System.IntPtr,bool)'></a>

## HoverEvent(IntPtr, bool) Constructor

Initializes a new instance of the HoverEvent class with the specified handle and ownership flag.

```csharp
public HoverEvent(System.IntPtr handle, bool ownsHandle);
```
#### Parameters

<a name='Tizen.UI.HoverEvent.HoverEvent(System.IntPtr,bool).handle'></a>

`handle` [System.IntPtr](https://docs.microsoft.com/en-us/dotnet/api/System.IntPtr 'System.IntPtr')

The handle of the hover event.

<a name='Tizen.UI.HoverEvent.HoverEvent(System.IntPtr,bool).ownsHandle'></a>

`ownsHandle` [System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

True if the object takes ownership of the handle, false otherwise.
### Properties

<a name='Tizen.UI.HoverEvent.Count'></a>

## HoverEvent.Count Property

Gets the number of hover points in the hover event.

```csharp
public int Count { get; }
```

#### Property Value
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

<a name='Tizen.UI.HoverEvent.this[int]'></a>

## HoverEvent.this[int] Property

Gets the hover point at the specified index.

```csharp
public Tizen.UI.Hover this[int i] { get; }
```
#### Parameters

<a name='Tizen.UI.HoverEvent.this[int].i'></a>

`i` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The index of the hover point to get.

#### Property Value
[Hover](Tizen.UI.Hover.md 'Tizen.UI.Hover')

<a name='Tizen.UI.HoverEvent.Time'></a>

## HoverEvent.Time Property

Gets the time when the hover event occurred.

```csharp
public uint Time { get; }
```

#### Property Value
[System.UInt32](https://docs.microsoft.com/en-us/dotnet/api/System.UInt32 'System.UInt32')






