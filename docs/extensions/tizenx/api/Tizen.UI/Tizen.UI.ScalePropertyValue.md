### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## ScalePropertyValue Class

Represents a property value that represents the scale of a view.

```csharp
public class ScalePropertyValue : Tizen.UI.AnimatablePropertyValue
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [AnimatablePropertyValue](Tizen.UI.AnimatablePropertyValue.md 'Tizen.UI.AnimatablePropertyValue') &#129106; ScalePropertyValue
### Constructors

<a name='Tizen.UI.ScalePropertyValue.ScalePropertyValue(float,float)'></a>

## ScalePropertyValue(float, float) Constructor

Initializes a new instance of the [ScalePropertyValue](Tizen.UI.ScalePropertyValue.md 'Tizen.UI.ScalePropertyValue') class.

```csharp
public ScalePropertyValue(float x, float y);
```
#### Parameters

<a name='Tizen.UI.ScalePropertyValue.ScalePropertyValue(float,float).x'></a>

`x` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The x-coordinate of the scale.

<a name='Tizen.UI.ScalePropertyValue.ScalePropertyValue(float,float).y'></a>

`y` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The y-coordinate of the scale.
### Properties

<a name='Tizen.UI.ScalePropertyValue.Scale'></a>

## ScalePropertyValue.Scale Property

Gets the scale of the property value.

```csharp
public Tizen.UI.Size Scale { get; }
```

#### Property Value
[Size](Tizen.UI.Size.md 'Tizen.UI.Size')

<a name='Tizen.UI.ScalePropertyValue.Value'></a>

## ScalePropertyValue.Value Property

Gets the value of the property.

```csharp
public override Tizen.UI.NativeHandle.PropertyValueHandle Value { get; }
```

#### Property Value
[PropertyValueHandle](Tizen.UI.NativeHandle.PropertyValueHandle.md 'Tizen.UI.NativeHandle.PropertyValueHandle')
### Methods

<a name='Tizen.UI.ScalePropertyValue.GetTargetProperty(Tizen.UI.View)'></a>

## ScalePropertyValue.GetTargetProperty(View) Method

Gets the target property handle for the animation.

```csharp
public override Tizen.UI.NativeHandle.AnimatablePropertyHandle GetTargetProperty(Tizen.UI.View view);
```
#### Parameters

<a name='Tizen.UI.ScalePropertyValue.GetTargetProperty(Tizen.UI.View).view'></a>

`view` [View](Tizen.UI.View.md 'Tizen.UI.View')

The view to which the property belongs.

#### Returns
[AnimatablePropertyHandle](Tizen.UI.NativeHandle.AnimatablePropertyHandle.md 'Tizen.UI.NativeHandle.AnimatablePropertyHandle')  
The target property handle.






