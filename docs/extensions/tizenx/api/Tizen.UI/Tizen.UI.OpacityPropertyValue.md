### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## OpacityPropertyValue Class

OpacityPropertyValue is a class that represents the opacity property value for an AnimatableProperty.

```csharp
public class OpacityPropertyValue : Tizen.UI.AnimatablePropertyValue
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [AnimatablePropertyValue](Tizen.UI.AnimatablePropertyValue.md 'Tizen.UI.AnimatablePropertyValue') &#129106; OpacityPropertyValue
### Constructors

<a name='Tizen.UI.OpacityPropertyValue.OpacityPropertyValue(float)'></a>

## OpacityPropertyValue(float) Constructor

Initializes a new instance of the OpacityPropertyValue class.

```csharp
public OpacityPropertyValue(float opacity);
```
#### Parameters

<a name='Tizen.UI.OpacityPropertyValue.OpacityPropertyValue(float).opacity'></a>

`opacity` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The opacity value.
### Properties

<a name='Tizen.UI.OpacityPropertyValue.Opacity'></a>

## OpacityPropertyValue.Opacity Property

Gets the opacity value.

```csharp
public float Opacity { get; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.OpacityPropertyValue.Value'></a>

## OpacityPropertyValue.Value Property

Gets the value of the property.

```csharp
public override Tizen.UI.NativeHandle.PropertyValueHandle Value { get; }
```

#### Property Value
[PropertyValueHandle](Tizen.UI.NativeHandle.PropertyValueHandle.md 'Tizen.UI.NativeHandle.PropertyValueHandle')
### Methods

<a name='Tizen.UI.OpacityPropertyValue.GetTargetProperty(Tizen.UI.View)'></a>

## OpacityPropertyValue.GetTargetProperty(View) Method

Gets the target property for the animation.

```csharp
public override Tizen.UI.NativeHandle.AnimatablePropertyHandle GetTargetProperty(Tizen.UI.View view);
```
#### Parameters

<a name='Tizen.UI.OpacityPropertyValue.GetTargetProperty(Tizen.UI.View).view'></a>

`view` [View](Tizen.UI.View.md 'Tizen.UI.View')

The view to animate.

#### Returns
[AnimatablePropertyHandle](Tizen.UI.NativeHandle.AnimatablePropertyHandle.md 'Tizen.UI.NativeHandle.AnimatablePropertyHandle')  
The AnimatablePropertyHandle for the target property.






