### [Tizen.UI.NativeHandle](Tizen.UI.NativeHandle.md 'Tizen.UI.NativeHandle')

## PropertyValueHandle Class

Represents a handle to a property value.

```csharp
public class PropertyValueHandle : System.Runtime.InteropServices.SafeHandle
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [System.Runtime.ConstrainedExecution.CriticalFinalizerObject](https://docs.microsoft.com/en-us/dotnet/api/System.Runtime.ConstrainedExecution.CriticalFinalizerObject 'System.Runtime.ConstrainedExecution.CriticalFinalizerObject') &#129106; [System.Runtime.InteropServices.SafeHandle](https://docs.microsoft.com/en-us/dotnet/api/System.Runtime.InteropServices.SafeHandle 'System.Runtime.InteropServices.SafeHandle') &#129106; PropertyValueHandle
### Constructors

<a name='Tizen.UI.NativeHandle.PropertyValueHandle.PropertyValueHandle()'></a>

## PropertyValueHandle() Constructor

Initializes a new instance of the [PropertyValueHandle](Tizen.UI.NativeHandle.PropertyValueHandle.md 'Tizen.UI.NativeHandle.PropertyValueHandle') class.

```csharp
public PropertyValueHandle();
```

<a name='Tizen.UI.NativeHandle.PropertyValueHandle.PropertyValueHandle(System.IntPtr,bool)'></a>

## PropertyValueHandle(IntPtr, bool) Constructor

Initializes a new instance of the [PropertyValueHandle](Tizen.UI.NativeHandle.PropertyValueHandle.md 'Tizen.UI.NativeHandle.PropertyValueHandle') class with the specified handle and ownership.

```csharp
public PropertyValueHandle(System.IntPtr handle, bool ownsHandle);
```
#### Parameters

<a name='Tizen.UI.NativeHandle.PropertyValueHandle.PropertyValueHandle(System.IntPtr,bool).handle'></a>

`handle` [System.IntPtr](https://docs.microsoft.com/en-us/dotnet/api/System.IntPtr 'System.IntPtr')

The handle to the property value.

<a name='Tizen.UI.NativeHandle.PropertyValueHandle.PropertyValueHandle(System.IntPtr,bool).ownsHandle'></a>

`ownsHandle` [System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

A value indicating whether the handle is owned by this instance.
### Properties

<a name='Tizen.UI.NativeHandle.PropertyValueHandle.IsInvalid'></a>

## PropertyValueHandle.IsInvalid Property

Gets a value indicating whether the handle is invalid.

```csharp
public override bool IsInvalid { get; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')




