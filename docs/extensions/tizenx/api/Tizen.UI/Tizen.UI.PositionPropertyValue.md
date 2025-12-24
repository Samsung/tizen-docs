### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## PositionPropertyValue Class

Represents a property value for position animation.

```csharp
public class PositionPropertyValue : Tizen.UI.AnimatablePropertyValue
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [AnimatablePropertyValue](Tizen.UI.AnimatablePropertyValue.md 'Tizen.UI.AnimatablePropertyValue') &#129106; PositionPropertyValue
### Constructors

<a name='Tizen.UI.PositionPropertyValue.PositionPropertyValue(float,float)'></a>

## PositionPropertyValue(float, float) Constructor

Initializes a new instance of the [PositionPropertyValue](Tizen.UI.PositionPropertyValue.md 'Tizen.UI.PositionPropertyValue') class.

```csharp
public PositionPropertyValue(float x, float y);
```
#### Parameters

<a name='Tizen.UI.PositionPropertyValue.PositionPropertyValue(float,float).x'></a>

`x` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The x-coordinate of the position.

<a name='Tizen.UI.PositionPropertyValue.PositionPropertyValue(float,float).y'></a>

`y` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The y-coordinate of the position.
### Properties

<a name='Tizen.UI.PositionPropertyValue.Value'></a>

## PositionPropertyValue.Value Property

Gets the native value of the position property value.

```csharp
public override Tizen.UI.NativeHandle.PropertyValueHandle Value { get; }
```

#### Property Value
[PropertyValueHandle](Tizen.UI.NativeHandle.PropertyValueHandle.md 'Tizen.UI.NativeHandle.PropertyValueHandle')

<a name='Tizen.UI.PositionPropertyValue.X'></a>

## PositionPropertyValue.X Property

Gets the x-coordinate of the position.

```csharp
public float X { get; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.PositionPropertyValue.Y'></a>

## PositionPropertyValue.Y Property

Gets the y-coordinate of the position.

```csharp
public float Y { get; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')
### Methods

<a name='Tizen.UI.PositionPropertyValue.GetTargetProperty(Tizen.UI.View)'></a>

## PositionPropertyValue.GetTargetProperty(View) Method

Gets the target property handle for the position animation.

```csharp
public override Tizen.UI.NativeHandle.AnimatablePropertyHandle GetTargetProperty(Tizen.UI.View view);
```
#### Parameters

<a name='Tizen.UI.PositionPropertyValue.GetTargetProperty(Tizen.UI.View).view'></a>

`view` [View](Tizen.UI.View.md 'Tizen.UI.View')

The view to which the property value is applied.

#### Returns
[AnimatablePropertyHandle](Tizen.UI.NativeHandle.AnimatablePropertyHandle.md 'Tizen.UI.NativeHandle.AnimatablePropertyHandle')  
The target property handle.






