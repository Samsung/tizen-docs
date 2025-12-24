### [Tizen.UI.Components](Tizen.UI.Components.md 'Tizen.UI.Components')

## InputEventArgs Class

Event arguments for component input event.

```csharp
public class InputEventArgs : System.EventArgs
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [System.EventArgs](https://docs.microsoft.com/en-us/dotnet/api/System.EventArgs 'System.EventArgs') &#129106; InputEventArgs
### Constructors

<a name='Tizen.UI.Components.InputEventArgs.InputEventArgs(Tizen.UI.KeyDeviceClass)'></a>

## InputEventArgs(KeyDeviceClass) Constructor

Initializes a new instance of the [InputEventArgs](Tizen.UI.Components.InputEventArgs.md 'Tizen.UI.Components.InputEventArgs') class with the specified input device.

```csharp
public InputEventArgs(Tizen.UI.KeyDeviceClass device);
```
#### Parameters

<a name='Tizen.UI.Components.InputEventArgs.InputEventArgs(Tizen.UI.KeyDeviceClass).device'></a>

`device` [Tizen.UI.KeyDeviceClass](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.KeyDeviceClass 'Tizen.UI.KeyDeviceClass')

The input device.
### Properties

<a name='Tizen.UI.Components.InputEventArgs.Handled'></a>

## InputEventArgs.Handled Property

Gets or sets a value indicating whether the input event has been handled.

```csharp
public bool Handled { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.InputEventArgs.InputDevice'></a>

## InputEventArgs.InputDevice Property

Gets the input device

```csharp
public Tizen.UI.KeyDeviceClass InputDevice { get; set; }
```

#### Property Value
[Tizen.UI.KeyDeviceClass](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.KeyDeviceClass 'Tizen.UI.KeyDeviceClass')


























































