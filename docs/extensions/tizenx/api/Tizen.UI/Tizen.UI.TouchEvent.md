### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## TouchEvent Class

The TouchEvent class represents a touch event that contains information about the touch points.

```csharp
public class TouchEvent : Tizen.UI.NObject
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [NObject](Tizen.UI.NObject.md 'Tizen.UI.NObject') &#129106; TouchEvent
### Constructors

<a name='Tizen.UI.TouchEvent.TouchEvent()'></a>

## TouchEvent() Constructor

Creates a new TouchEvent object

```csharp
public TouchEvent();
```

<a name='Tizen.UI.TouchEvent.TouchEvent(System.IntPtr,bool)'></a>

## TouchEvent(IntPtr, bool) Constructor

Creates a new TouchEvent object using the specified handle.

```csharp
public TouchEvent(System.IntPtr handle, bool ownshandle);
```
#### Parameters

<a name='Tizen.UI.TouchEvent.TouchEvent(System.IntPtr,bool).handle'></a>

`handle` [System.IntPtr](https://docs.microsoft.com/en-us/dotnet/api/System.IntPtr 'System.IntPtr')

The native handle of the touch event.

<a name='Tizen.UI.TouchEvent.TouchEvent(System.IntPtr,bool).ownshandle'></a>

`ownshandle` [System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

True if the object takes ownership of the handle, false otherwise.
### Properties

<a name='Tizen.UI.TouchEvent.Count'></a>

## TouchEvent.Count Property

Gets the number of touch points in the touch event.

```csharp
public int Count { get; }
```

#### Property Value
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

<a name='Tizen.UI.TouchEvent.this[int]'></a>

## TouchEvent.this[int] Property

Gets the touch point at the specified index.

```csharp
public Tizen.UI.Touch this[int i] { get; }
```
#### Parameters

<a name='Tizen.UI.TouchEvent.this[int].i'></a>

`i` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The index of the touch point.

#### Property Value
[Touch](Tizen.UI.Touch.md 'Tizen.UI.Touch')

<a name='Tizen.UI.TouchEvent.Time'></a>

## TouchEvent.Time Property

Gets the time when the touch event occurred.

```csharp
public uint Time { get; }
```

#### Property Value
[System.UInt32](https://docs.microsoft.com/en-us/dotnet/api/System.UInt32 'System.UInt32')






