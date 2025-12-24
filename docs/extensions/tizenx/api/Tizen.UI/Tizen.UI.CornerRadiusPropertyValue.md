### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## CornerRadiusPropertyValue Class

The CornerRadiusPropertyValue class represents a property value of CornerRadius type.

```csharp
public class CornerRadiusPropertyValue : Tizen.UI.AnimatablePropertyValue
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [AnimatablePropertyValue](Tizen.UI.AnimatablePropertyValue.md 'Tizen.UI.AnimatablePropertyValue') &#129106; CornerRadiusPropertyValue
### Constructors

<a name='Tizen.UI.CornerRadiusPropertyValue.CornerRadiusPropertyValue(Tizen.UI.CornerRadius)'></a>

## CornerRadiusPropertyValue(CornerRadius) Constructor

Initializes a new instance of the CornerRadiusPropertyValue class with the specified CornerRadius value.

```csharp
public CornerRadiusPropertyValue(Tizen.UI.CornerRadius cornerRadius);
```
#### Parameters

<a name='Tizen.UI.CornerRadiusPropertyValue.CornerRadiusPropertyValue(Tizen.UI.CornerRadius).cornerRadius'></a>

`cornerRadius` [CornerRadius](Tizen.UI.CornerRadius.md 'Tizen.UI.CornerRadius')

The CornerRadius value to set.
### Properties

<a name='Tizen.UI.CornerRadiusPropertyValue.CornerRadius'></a>

## CornerRadiusPropertyValue.CornerRadius Property

Gets the CornerRadius value of the property.

```csharp
public Tizen.UI.CornerRadius CornerRadius { get; }
```

#### Property Value
[CornerRadius](Tizen.UI.CornerRadius.md 'Tizen.UI.CornerRadius')

<a name='Tizen.UI.CornerRadiusPropertyValue.Value'></a>

## CornerRadiusPropertyValue.Value Property

Gets the value of the property.

```csharp
public override Tizen.UI.NativeHandle.PropertyValueHandle Value { get; }
```

#### Property Value
[PropertyValueHandle](Tizen.UI.NativeHandle.PropertyValueHandle.md 'Tizen.UI.NativeHandle.PropertyValueHandle')
### Methods

<a name='Tizen.UI.CornerRadiusPropertyValue.GetTargetProperties(Tizen.UI.View)'></a>

## CornerRadiusPropertyValue.GetTargetProperties(View) Method

Gets the target properties for the given view.

```csharp
public override System.Collections.Generic.IEnumerable&lt;(Tizen.UI.NativeHandle.AnimatablePropertyHandle Property,Tizen.UI.NativeHandle.PropertyValueHandle Value)> GetTargetProperties(Tizen.UI.View view);
```
#### Parameters

<a name='Tizen.UI.CornerRadiusPropertyValue.GetTargetProperties(Tizen.UI.View).view'></a>

`view` [View](Tizen.UI.View.md 'Tizen.UI.View')

The view to get the target properties for.

#### Returns
[System.Collections.Generic.IEnumerable&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IEnumerable-1 'System.Collections.Generic.IEnumerable`1')[&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.ValueTuple 'System.ValueTuple')[AnimatablePropertyHandle](Tizen.UI.NativeHandle.AnimatablePropertyHandle.md 'Tizen.UI.NativeHandle.AnimatablePropertyHandle')[,](https://docs.microsoft.com/en-us/dotnet/api/System.ValueTuple 'System.ValueTuple')[PropertyValueHandle](Tizen.UI.NativeHandle.PropertyValueHandle.md 'Tizen.UI.NativeHandle.PropertyValueHandle')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.ValueTuple 'System.ValueTuple')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IEnumerable-1 'System.Collections.Generic.IEnumerable`1')  
An enumeration of tuples containing the target property handle and its corresponding value handle.

<a name='Tizen.UI.CornerRadiusPropertyValue.GetTargetProperty(Tizen.UI.View)'></a>

## CornerRadiusPropertyValue.GetTargetProperty(View) Method

Gets the target property handle for the animation.

```csharp
public override Tizen.UI.NativeHandle.AnimatablePropertyHandle GetTargetProperty(Tizen.UI.View view);
```
#### Parameters

<a name='Tizen.UI.CornerRadiusPropertyValue.GetTargetProperty(Tizen.UI.View).view'></a>

`view` [View](Tizen.UI.View.md 'Tizen.UI.View')

The view to which the property belongs.

#### Returns
[AnimatablePropertyHandle](Tizen.UI.NativeHandle.AnimatablePropertyHandle.md 'Tizen.UI.NativeHandle.AnimatablePropertyHandle')  
The target property handle.






