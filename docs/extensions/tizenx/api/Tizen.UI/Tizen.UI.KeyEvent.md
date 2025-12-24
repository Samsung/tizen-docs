### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## KeyEvent Class

KeyEvent is a class that represents a key event.

```csharp
public class KeyEvent : Tizen.UI.NObject
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [NObject](Tizen.UI.NObject.md 'Tizen.UI.NObject') &#129106; KeyEvent
### Constructors

<a name='Tizen.UI.KeyEvent.KeyEvent()'></a>

## KeyEvent() Constructor

Initializes a new instance of the KeyEvent class.

```csharp
public KeyEvent();
```

<a name='Tizen.UI.KeyEvent.KeyEvent(System.IntPtr,bool)'></a>

## KeyEvent(IntPtr, bool) Constructor

Initializes a new instance of the KeyEvent class with specified handle and ownership.

```csharp
public KeyEvent(System.IntPtr handle, bool hasOwnership);
```
#### Parameters

<a name='Tizen.UI.KeyEvent.KeyEvent(System.IntPtr,bool).handle'></a>

`handle` [System.IntPtr](https://docs.microsoft.com/en-us/dotnet/api/System.IntPtr 'System.IntPtr')

The handle of the key event.

<a name='Tizen.UI.KeyEvent.KeyEvent(System.IntPtr,bool).hasOwnership'></a>

`hasOwnership` [System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

Whether this instance owns the handle or not.
### Properties

<a name='Tizen.UI.KeyEvent.DeviceClass'></a>

## KeyEvent.DeviceClass Property

Gets the device class of the key event.

```csharp
public Tizen.UI.KeyDeviceClass DeviceClass { get; }
```

#### Property Value
[KeyDeviceClass](Tizen.UI.KeyDeviceClass.md 'Tizen.UI.KeyDeviceClass')

<a name='Tizen.UI.KeyEvent.DeviceName'></a>

## KeyEvent.DeviceName Property

Gets the device name of the key event.

```csharp
public string DeviceName { get; }
```

#### Property Value
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.KeyEvent.DeviceSubClass'></a>

## KeyEvent.DeviceSubClass Property

Gets the device sub class of the key event.

```csharp
public Tizen.UI.KeyDeviceSubClass DeviceSubClass { get; }
```

#### Property Value
[KeyDeviceSubClass](Tizen.UI.KeyDeviceSubClass.md 'Tizen.UI.KeyDeviceSubClass')

<a name='Tizen.UI.KeyEvent.IsAltModifier'></a>

## KeyEvent.IsAltModifier Property

Gets whether the alt modifier is on or not.

```csharp
public bool IsAltModifier { get; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.KeyEvent.IsCtrlModifier'></a>

## KeyEvent.IsCtrlModifier Property

Gets whether the ctrl modifier is on or not.

```csharp
public bool IsCtrlModifier { get; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.KeyEvent.IsShiftModifier'></a>

## KeyEvent.IsShiftModifier Property

Gets whether the shift modifier is on or not.

```csharp
public bool IsShiftModifier { get; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.KeyEvent.KeyCode'></a>

## KeyEvent.KeyCode Property

Gets or sets the key code of the key event.

```csharp
public int KeyCode { get; set; }
```

#### Property Value
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

<a name='Tizen.UI.KeyEvent.KeyModifier'></a>

## KeyEvent.KeyModifier Property

Gets or sets the key modifier of the key event.

```csharp
public int KeyModifier { get; set; }
```

#### Property Value
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

<a name='Tizen.UI.KeyEvent.KeyPressedName'></a>

## KeyEvent.KeyPressedName Property

Gets or sets the key pressed name of the key event.

```csharp
public string KeyPressedName { get; set; }
```

#### Property Value
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.KeyEvent.LogicalKey'></a>

## KeyEvent.LogicalKey Property

Gets the logical key of the key event.

```csharp
public string LogicalKey { get; }
```

#### Property Value
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.KeyEvent.State'></a>

## KeyEvent.State Property

Gets or sets the state of the key event.

```csharp
public Tizen.UI.KeyState State { get; set; }
```

#### Property Value
[KeyState](Tizen.UI.KeyState.md 'Tizen.UI.KeyState')

<a name='Tizen.UI.KeyEvent.Time'></a>

## KeyEvent.Time Property

Gets or sets the time of the key event.

```csharp
public uint Time { get; set; }
```

#### Property Value
[System.UInt32](https://docs.microsoft.com/en-us/dotnet/api/System.UInt32 'System.UInt32')






