### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## CustomPropertyValue Class

Represents a custom property value that can be animated.

```csharp
public class CustomPropertyValue : Tizen.UI.AnimatablePropertyValue
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [AnimatablePropertyValue](Tizen.UI.AnimatablePropertyValue.md 'Tizen.UI.AnimatablePropertyValue') &#129106; CustomPropertyValue
### Constructors

<a name='Tizen.UI.CustomPropertyValue.CustomPropertyValue(string,Tizen.UI.NativeHandle.PropertyValueHandle)'></a>

## CustomPropertyValue(string, PropertyValueHandle) Constructor

Initializes a new instance of the [CustomPropertyValue](Tizen.UI.CustomPropertyValue.md 'Tizen.UI.CustomPropertyValue') class.

```csharp
public CustomPropertyValue(string propertyName, Tizen.UI.NativeHandle.PropertyValueHandle value);
```
#### Parameters

<a name='Tizen.UI.CustomPropertyValue.CustomPropertyValue(string,Tizen.UI.NativeHandle.PropertyValueHandle).propertyName'></a>

`propertyName` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The name of the property.

<a name='Tizen.UI.CustomPropertyValue.CustomPropertyValue(string,Tizen.UI.NativeHandle.PropertyValueHandle).value'></a>

`value` [PropertyValueHandle](Tizen.UI.NativeHandle.PropertyValueHandle.md 'Tizen.UI.NativeHandle.PropertyValueHandle')

The value of the property.
### Properties

<a name='Tizen.UI.CustomPropertyValue.Value'></a>

## CustomPropertyValue.Value Property

Gets the value of the property.

```csharp
public override Tizen.UI.NativeHandle.PropertyValueHandle Value { get; }
```

#### Property Value
[PropertyValueHandle](Tizen.UI.NativeHandle.PropertyValueHandle.md 'Tizen.UI.NativeHandle.PropertyValueHandle')
### Methods

<a name='Tizen.UI.CustomPropertyValue.GetTargetProperty(Tizen.UI.View)'></a>

## CustomPropertyValue.GetTargetProperty(View) Method

Gets the target property handle for the specified view.

```csharp
public override Tizen.UI.NativeHandle.AnimatablePropertyHandle GetTargetProperty(Tizen.UI.View view);
```
#### Parameters

<a name='Tizen.UI.CustomPropertyValue.GetTargetProperty(Tizen.UI.View).view'></a>

`view` [View](Tizen.UI.View.md 'Tizen.UI.View')

The view.

#### Returns
[AnimatablePropertyHandle](Tizen.UI.NativeHandle.AnimatablePropertyHandle.md 'Tizen.UI.NativeHandle.AnimatablePropertyHandle')  
The target property handle.






