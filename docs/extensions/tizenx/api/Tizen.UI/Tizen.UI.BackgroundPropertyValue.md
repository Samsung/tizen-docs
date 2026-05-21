### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## BackgroundPropertyValue Class

BackgroundPropertyValue is a class that represents the value of the background property of a View.

```csharp
public class BackgroundPropertyValue : Tizen.UI.AnimatablePropertyValue
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [AnimatablePropertyValue](Tizen.UI.AnimatablePropertyValue.md 'Tizen.UI.AnimatablePropertyValue') &#129106; BackgroundPropertyValue
### Constructors

<a name='Tizen.UI.BackgroundPropertyValue.BackgroundPropertyValue(Tizen.UI.Color)'></a>

## BackgroundPropertyValue(Color) Constructor

Initializes a new instance of the BackgroundPropertyValue class with the specified color.

```csharp
public BackgroundPropertyValue(Tizen.UI.Color color);
```
#### Parameters

<a name='Tizen.UI.BackgroundPropertyValue.BackgroundPropertyValue(Tizen.UI.Color).color'></a>

`color` [Color](Tizen.UI.Color.md 'Tizen.UI.Color')

The color of the background.
### Properties

<a name='Tizen.UI.BackgroundPropertyValue.Value'></a>

## BackgroundPropertyValue.Value Property

Gets the value of the property.

```csharp
public override Tizen.UI.NativeHandle.PropertyValueHandle Value { get; }
```

#### Property Value
[PropertyValueHandle](Tizen.UI.NativeHandle.PropertyValueHandle.md 'Tizen.UI.NativeHandle.PropertyValueHandle')
### Methods

<a name='Tizen.UI.BackgroundPropertyValue.GetTargetProperties(Tizen.UI.View)'></a>

## BackgroundPropertyValue.GetTargetProperties(View) Method

Gets the target properties for the given view.

```csharp
public override System.Collections.Generic.IEnumerable&lt;(Tizen.UI.NativeHandle.AnimatablePropertyHandle Property,Tizen.UI.NativeHandle.PropertyValueHandle Value)> GetTargetProperties(Tizen.UI.View view);
```
#### Parameters

<a name='Tizen.UI.BackgroundPropertyValue.GetTargetProperties(Tizen.UI.View).view'></a>

`view` [View](Tizen.UI.View.md 'Tizen.UI.View')

The view to get the target properties for.

#### Returns
[System.Collections.Generic.IEnumerable&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IEnumerable-1 'System.Collections.Generic.IEnumerable`1')[&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.ValueTuple 'System.ValueTuple')[AnimatablePropertyHandle](Tizen.UI.NativeHandle.AnimatablePropertyHandle.md 'Tizen.UI.NativeHandle.AnimatablePropertyHandle')[,](https://docs.microsoft.com/en-us/dotnet/api/System.ValueTuple 'System.ValueTuple')[PropertyValueHandle](Tizen.UI.NativeHandle.PropertyValueHandle.md 'Tizen.UI.NativeHandle.PropertyValueHandle')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.ValueTuple 'System.ValueTuple')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IEnumerable-1 'System.Collections.Generic.IEnumerable`1')  
An enumeration of tuples containing the target property handle and its corresponding value handle.

<a name='Tizen.UI.BackgroundPropertyValue.GetTargetProperty(Tizen.UI.View)'></a>

## BackgroundPropertyValue.GetTargetProperty(View) Method

Gets the target property handle for the animation.

```csharp
public override Tizen.UI.NativeHandle.AnimatablePropertyHandle GetTargetProperty(Tizen.UI.View view);
```
#### Parameters

<a name='Tizen.UI.BackgroundPropertyValue.GetTargetProperty(Tizen.UI.View).view'></a>

`view` [View](Tizen.UI.View.md 'Tizen.UI.View')

The view to which the property belongs.

#### Returns
[AnimatablePropertyHandle](Tizen.UI.NativeHandle.AnimatablePropertyHandle.md 'Tizen.UI.NativeHandle.AnimatablePropertyHandle')  
The target property handle.






