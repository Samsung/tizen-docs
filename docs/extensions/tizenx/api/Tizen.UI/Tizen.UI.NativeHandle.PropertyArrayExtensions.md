### [Tizen.UI.NativeHandle](Tizen.UI.NativeHandle.md 'Tizen.UI.NativeHandle')

## PropertyArrayExtensions Class

Extension methods for the PropertyArrayHandle class.

```csharp
public static class PropertyArrayExtensions
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; PropertyArrayExtensions
### Methods

<a name='Tizen.UI.NativeHandle.PropertyArrayExtensions.Add(thisTizen.UI.NativeHandle.PropertyArrayHandle,Tizen.UI.NativeHandle.PropertyValueHandle)'></a>

## PropertyArrayExtensions.Add(this PropertyArrayHandle, PropertyValueHandle) Method

Adds a new property value to the end of the array.

```csharp
public static void Add(this Tizen.UI.NativeHandle.PropertyArrayHandle handle, Tizen.UI.NativeHandle.PropertyValueHandle value);
```
#### Parameters

<a name='Tizen.UI.NativeHandle.PropertyArrayExtensions.Add(thisTizen.UI.NativeHandle.PropertyArrayHandle,Tizen.UI.NativeHandle.PropertyValueHandle).handle'></a>

`handle` [PropertyArrayHandle](Tizen.UI.NativeHandle.PropertyArrayHandle.md 'Tizen.UI.NativeHandle.PropertyArrayHandle')

The PropertyArrayHandle instance.

<a name='Tizen.UI.NativeHandle.PropertyArrayExtensions.Add(thisTizen.UI.NativeHandle.PropertyArrayHandle,Tizen.UI.NativeHandle.PropertyValueHandle).value'></a>

`value` [PropertyValueHandle](Tizen.UI.NativeHandle.PropertyValueHandle.md 'Tizen.UI.NativeHandle.PropertyValueHandle')

The PropertyValueHandle instance to add.

<a name='Tizen.UI.NativeHandle.PropertyArrayExtensions.GetAt(thisTizen.UI.NativeHandle.PropertyArrayHandle,int)'></a>

## PropertyArrayExtensions.GetAt(this PropertyArrayHandle, int) Method

Gets the property value at the specified index.

```csharp
public static Tizen.UI.NativeHandle.PropertyValueHandle GetAt(this Tizen.UI.NativeHandle.PropertyArrayHandle handle, int index);
```
#### Parameters

<a name='Tizen.UI.NativeHandle.PropertyArrayExtensions.GetAt(thisTizen.UI.NativeHandle.PropertyArrayHandle,int).handle'></a>

`handle` [PropertyArrayHandle](Tizen.UI.NativeHandle.PropertyArrayHandle.md 'Tizen.UI.NativeHandle.PropertyArrayHandle')

The PropertyArrayHandle instance.

<a name='Tizen.UI.NativeHandle.PropertyArrayExtensions.GetAt(thisTizen.UI.NativeHandle.PropertyArrayHandle,int).index'></a>

`index` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The index of the property value to get.

#### Returns
[PropertyValueHandle](Tizen.UI.NativeHandle.PropertyValueHandle.md 'Tizen.UI.NativeHandle.PropertyValueHandle')  
The PropertyValueHandle instance at the specified index.




