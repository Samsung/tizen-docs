### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## TouchPoint Class

TouchPoint represents a single point of contact on a touchscreen device.

```csharp
public class TouchPoint : Tizen.UI.NObject
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [NObject](Tizen.UI.NObject.md 'Tizen.UI.NObject') &#129106; TouchPoint
### Constructors

<a name='Tizen.UI.TouchPoint.TouchPoint(int,Tizen.UI.TouchState,float,float)'></a>

## TouchPoint(int, TouchState, float, float) Constructor

Initializes a new instance of the TouchPoint class with the specified device ID, state, screen X coordinate, and screen Y coordinate.

```csharp
public TouchPoint(int deviceId, Tizen.UI.TouchState state, float screenX, float screenY);
```
#### Parameters

<a name='Tizen.UI.TouchPoint.TouchPoint(int,Tizen.UI.TouchState,float,float).deviceId'></a>

`deviceId` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The ID of the device that generated the touch event.

<a name='Tizen.UI.TouchPoint.TouchPoint(int,Tizen.UI.TouchState,float,float).state'></a>

`state` [TouchState](Tizen.UI.TouchState.md 'Tizen.UI.TouchState')

The state of the touch point.

<a name='Tizen.UI.TouchPoint.TouchPoint(int,Tizen.UI.TouchState,float,float).screenX'></a>

`screenX` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The X coordinate of the touch point in screen coordinates.

<a name='Tizen.UI.TouchPoint.TouchPoint(int,Tizen.UI.TouchState,float,float).screenY'></a>

`screenY` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The Y coordinate of the touch point in screen coordinates.

<a name='Tizen.UI.TouchPoint.TouchPoint(System.IntPtr,bool)'></a>

## TouchPoint(IntPtr, bool) Constructor

Initializes a new instance of the TouchPoint class with the specified handle and whether to own the handle or not.

```csharp
public TouchPoint(System.IntPtr handle, bool ownsHandle);
```
#### Parameters

<a name='Tizen.UI.TouchPoint.TouchPoint(System.IntPtr,bool).handle'></a>

`handle` [System.IntPtr](https://docs.microsoft.com/en-us/dotnet/api/System.IntPtr 'System.IntPtr')

The handle of the touch point.

<a name='Tizen.UI.TouchPoint.TouchPoint(System.IntPtr,bool).ownsHandle'></a>

`ownsHandle` [System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

Whether to own the handle or not.
### Properties

<a name='Tizen.UI.TouchPoint.DeviceId'></a>

## TouchPoint.DeviceId Property

Gets or sets the ID of the device that generated the touch event.

```csharp
public int DeviceId { get; set; }
```

#### Property Value
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

<a name='Tizen.UI.TouchPoint.HitView'></a>

## TouchPoint.HitView Property

Gets or sets the view that passed the hit test.

```csharp
public Tizen.UI.View HitView { get; set; }
```

#### Property Value
[View](Tizen.UI.View.md 'Tizen.UI.View')

<a name='Tizen.UI.TouchPoint.Position'></a>

## TouchPoint.Position Property

Gets or sets the position of the touch point in local coordinates.

```csharp
public Tizen.UI.Point Position { get; set; }
```

#### Property Value
[Point](Tizen.UI.Point.md 'Tizen.UI.Point')

<a name='Tizen.UI.TouchPoint.ScreenPosition'></a>

## TouchPoint.ScreenPosition Property

Gets or sets the position of the touch point in screen coordinates.

```csharp
public Tizen.UI.Point ScreenPosition { get; set; }
```

#### Property Value
[Point](Tizen.UI.Point.md 'Tizen.UI.Point')

<a name='Tizen.UI.TouchPoint.State'></a>

## TouchPoint.State Property

Gets or sets the state of the touch point.

```csharp
public Tizen.UI.TouchState State { get; set; }
```

#### Property Value
[TouchState](Tizen.UI.TouchState.md 'Tizen.UI.TouchState')






