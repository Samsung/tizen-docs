### [Tizen.UI.Scene3D](Tizen.UI.Scene3D.md 'Tizen.UI.Scene3D')

## CustomPropertyValue&lt;T> Class

Represents a custom property value that can be animated in 3D.

```csharp
public class CustomPropertyValue&lt;T> : Tizen.UI.Scene3D.Animatable3DPropertyValue&lt;T>
    where T : Tizen.UI.NObject
```
#### Type parameters

<a name='Tizen.UI.Scene3D.CustomPropertyValue_T_.T'></a>

`T`

The type of the object.

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [Tizen.UI.Scene3D.Animatable3DPropertyValue&lt;](Tizen.UI.Scene3D.Animatable3DPropertyValue_T_.md 'Tizen.UI.Scene3D.Animatable3DPropertyValue&lt;T>')[T](Tizen.UI.Scene3D.CustomPropertyValue_T_.md#Tizen.UI.Scene3D.CustomPropertyValue_T_.T 'Tizen.UI.Scene3D.CustomPropertyValue&lt;T>.T')[&gt;](Tizen.UI.Scene3D.Animatable3DPropertyValue_T_.md 'Tizen.UI.Scene3D.Animatable3DPropertyValue&lt;T>') &#129106; CustomPropertyValue&lt;T>
### Constructors

<a name='Tizen.UI.Scene3D.CustomPropertyValue_T_.CustomPropertyValue(string,Tizen.UI.NativeHandle.PropertyValueHandle)'></a>

## CustomPropertyValue(string, PropertyValueHandle) Constructor

Initializes a new instance of the [Tizen.UI.CustomPropertyValue](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.CustomPropertyValue 'Tizen.UI.CustomPropertyValue') class.

```csharp
public CustomPropertyValue(string propertyName, Tizen.UI.NativeHandle.PropertyValueHandle value);
```
#### Parameters

<a name='Tizen.UI.Scene3D.CustomPropertyValue_T_.CustomPropertyValue(string,Tizen.UI.NativeHandle.PropertyValueHandle).propertyName'></a>

`propertyName` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The name of the property.

<a name='Tizen.UI.Scene3D.CustomPropertyValue_T_.CustomPropertyValue(string,Tizen.UI.NativeHandle.PropertyValueHandle).value'></a>

`value` [Tizen.UI.NativeHandle.PropertyValueHandle](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.NativeHandle.PropertyValueHandle 'Tizen.UI.NativeHandle.PropertyValueHandle')

The value of the property.
### Properties

<a name='Tizen.UI.Scene3D.CustomPropertyValue_T_.Value'></a>

## CustomPropertyValue&lt;T>.Value Property

Gets the value of the property.

```csharp
public override Tizen.UI.NativeHandle.PropertyValueHandle Value { get; }
```

#### Property Value
[Tizen.UI.NativeHandle.PropertyValueHandle](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.NativeHandle.PropertyValueHandle 'Tizen.UI.NativeHandle.PropertyValueHandle')
### Methods

<a name='Tizen.UI.Scene3D.CustomPropertyValue_T_.GetTargetProperty(T)'></a>

## CustomPropertyValue&lt;T>.GetTargetProperty(T) Method

Gets the target property handle for the specified view.

```csharp
public override Tizen.UI.NativeHandle.AnimatablePropertyHandle GetTargetProperty(T view);
```
#### Parameters

<a name='Tizen.UI.Scene3D.CustomPropertyValue_T_.GetTargetProperty(T).view'></a>

`view` [T](Tizen.UI.Scene3D.CustomPropertyValue_T_.md#Tizen.UI.Scene3D.CustomPropertyValue_T_.T 'Tizen.UI.Scene3D.CustomPropertyValue&lt;T>.T')

The view.

#### Returns
[Tizen.UI.NativeHandle.AnimatablePropertyHandle](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.NativeHandle.AnimatablePropertyHandle 'Tizen.UI.NativeHandle.AnimatablePropertyHandle')  
The target property handle.





































