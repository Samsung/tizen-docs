### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## AnimatablePropertyValue Class

AnimatablePropertyValue is an abstract class that represents a property value that can be animated.

```csharp
public abstract class AnimatablePropertyValue :
System.IDisposable
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; AnimatablePropertyValue

Derived  
&#8627; [BackgroundPropertyValue](Tizen.UI.BackgroundPropertyValue.md 'Tizen.UI.BackgroundPropertyValue')  
&#8627; [CornerRadiusPropertyValue](Tizen.UI.CornerRadiusPropertyValue.md 'Tizen.UI.CornerRadiusPropertyValue')  
&#8627; [CustomPropertyValue](Tizen.UI.CustomPropertyValue.md 'Tizen.UI.CustomPropertyValue')  
&#8627; [OpacityPropertyValue](Tizen.UI.OpacityPropertyValue.md 'Tizen.UI.OpacityPropertyValue')  
&#8627; [PositionPropertyValue](Tizen.UI.PositionPropertyValue.md 'Tizen.UI.PositionPropertyValue')  
&#8627; [RotationPropertyValue](Tizen.UI.RotationPropertyValue.md 'Tizen.UI.RotationPropertyValue')  
&#8627; [ScalePropertyValue](Tizen.UI.ScalePropertyValue.md 'Tizen.UI.ScalePropertyValue')  
&#8627; [SizePropertyValue](Tizen.UI.SizePropertyValue.md 'Tizen.UI.SizePropertyValue')

Implements [System.IDisposable](https://docs.microsoft.com/en-us/dotnet/api/System.IDisposable 'System.IDisposable')
### Properties

<a name='Tizen.UI.AnimatablePropertyValue.Value'></a>

## AnimatablePropertyValue.Value Property

Gets the value of the property.

```csharp
public abstract Tizen.UI.NativeHandle.PropertyValueHandle Value { get; }
```

#### Property Value
[PropertyValueHandle](Tizen.UI.NativeHandle.PropertyValueHandle.md 'Tizen.UI.NativeHandle.PropertyValueHandle')
### Methods

<a name='Tizen.UI.AnimatablePropertyValue.CreateBackgroundColorValue(Tizen.UI.Color)'></a>

## AnimatablePropertyValue.CreateBackgroundColorValue(Color) Method

Creates a new instance of the BackgroundPropertyValue class with the specified background color.

```csharp
public static Tizen.UI.AnimatablePropertyValue CreateBackgroundColorValue(Tizen.UI.Color backgroundColor);
```
#### Parameters

<a name='Tizen.UI.AnimatablePropertyValue.CreateBackgroundColorValue(Tizen.UI.Color).backgroundColor'></a>

`backgroundColor` [Color](Tizen.UI.Color.md 'Tizen.UI.Color')

The background color to set.

#### Returns
[AnimatablePropertyValue](Tizen.UI.AnimatablePropertyValue.md 'Tizen.UI.AnimatablePropertyValue')  
A new instance of the BackgroundPropertyValue class with the specified background color.

<a name='Tizen.UI.AnimatablePropertyValue.CreateCornerRadiusValue(Tizen.UI.CornerRadius)'></a>

## AnimatablePropertyValue.CreateCornerRadiusValue(CornerRadius) Method

Creates a new instance of the AnimatablePropertyValue class with the specified CornerRadius value.

```csharp
public static Tizen.UI.AnimatablePropertyValue CreateCornerRadiusValue(Tizen.UI.CornerRadius cornerRadius);
```
#### Parameters

<a name='Tizen.UI.AnimatablePropertyValue.CreateCornerRadiusValue(Tizen.UI.CornerRadius).cornerRadius'></a>

`cornerRadius` [CornerRadius](Tizen.UI.CornerRadius.md 'Tizen.UI.CornerRadius')

The CornerRadius value to be used for the AnimatablePropertyValue.

#### Returns
[AnimatablePropertyValue](Tizen.UI.AnimatablePropertyValue.md 'Tizen.UI.AnimatablePropertyValue')  
A new instance of the AnimatablePropertyValue class with the specified CornerRadius value.

<a name='Tizen.UI.AnimatablePropertyValue.CreateCustomValue(string,object)'></a>

## AnimatablePropertyValue.CreateCustomValue(string, object) Method

Creates a new CustomPropertyValue object.

```csharp
public static Tizen.UI.AnimatablePropertyValue CreateCustomValue(string propertyName, object value);
```
#### Parameters

<a name='Tizen.UI.AnimatablePropertyValue.CreateCustomValue(string,object).propertyName'></a>

`propertyName` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The name of the custom property.

<a name='Tizen.UI.AnimatablePropertyValue.CreateCustomValue(string,object).value'></a>

`value` [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object')

The value of the custom property.

#### Returns
[AnimatablePropertyValue](Tizen.UI.AnimatablePropertyValue.md 'Tizen.UI.AnimatablePropertyValue')  
The new CustomPropertyValue object.

<a name='Tizen.UI.AnimatablePropertyValue.CreateCustomValue(string,Tizen.UI.NativeHandle.PropertyValueHandle)'></a>

## AnimatablePropertyValue.CreateCustomValue(string, PropertyValueHandle) Method

Creates a new CustomPropertyValue object.

```csharp
public static Tizen.UI.AnimatablePropertyValue CreateCustomValue(string propertyName, Tizen.UI.NativeHandle.PropertyValueHandle value);
```
#### Parameters

<a name='Tizen.UI.AnimatablePropertyValue.CreateCustomValue(string,Tizen.UI.NativeHandle.PropertyValueHandle).propertyName'></a>

`propertyName` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The name of the custom property.

<a name='Tizen.UI.AnimatablePropertyValue.CreateCustomValue(string,Tizen.UI.NativeHandle.PropertyValueHandle).value'></a>

`value` [PropertyValueHandle](Tizen.UI.NativeHandle.PropertyValueHandle.md 'Tizen.UI.NativeHandle.PropertyValueHandle')

The value of the custom property.

#### Returns
[AnimatablePropertyValue](Tizen.UI.AnimatablePropertyValue.md 'Tizen.UI.AnimatablePropertyValue')  
The new CustomPropertyValue object.

<a name='Tizen.UI.AnimatablePropertyValue.CreateOpacityValue(float)'></a>

## AnimatablePropertyValue.CreateOpacityValue(float) Method

Creates a new OpacityPropertyValue object.

```csharp
public static Tizen.UI.AnimatablePropertyValue CreateOpacityValue(float opacity);
```
#### Parameters

<a name='Tizen.UI.AnimatablePropertyValue.CreateOpacityValue(float).opacity'></a>

`opacity` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The opacity value.

#### Returns
[AnimatablePropertyValue](Tizen.UI.AnimatablePropertyValue.md 'Tizen.UI.AnimatablePropertyValue')  
The new OpacityPropertyValue object.

<a name='Tizen.UI.AnimatablePropertyValue.CreatePositionValue(float,float)'></a>

## AnimatablePropertyValue.CreatePositionValue(float, float) Method

Creates a new PositionPropertyValue object.

```csharp
public static Tizen.UI.AnimatablePropertyValue CreatePositionValue(float x, float y);
```
#### Parameters

<a name='Tizen.UI.AnimatablePropertyValue.CreatePositionValue(float,float).x'></a>

`x` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The x position.

<a name='Tizen.UI.AnimatablePropertyValue.CreatePositionValue(float,float).y'></a>

`y` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The y position.

#### Returns
[AnimatablePropertyValue](Tizen.UI.AnimatablePropertyValue.md 'Tizen.UI.AnimatablePropertyValue')  
The new PositionPropertyValue object.

<a name='Tizen.UI.AnimatablePropertyValue.CreatePositionValue(Tizen.UI.Point)'></a>

## AnimatablePropertyValue.CreatePositionValue(Point) Method

Creates a new PositionPropertyValue object.

```csharp
public static Tizen.UI.AnimatablePropertyValue CreatePositionValue(Tizen.UI.Point position);
```
#### Parameters

<a name='Tizen.UI.AnimatablePropertyValue.CreatePositionValue(Tizen.UI.Point).position'></a>

`position` [Point](Tizen.UI.Point.md 'Tizen.UI.Point')

The position.

#### Returns
[AnimatablePropertyValue](Tizen.UI.AnimatablePropertyValue.md 'Tizen.UI.AnimatablePropertyValue')  
The new PositionPropertyValue object.

<a name='Tizen.UI.AnimatablePropertyValue.CreateRotationValue(float,float,float)'></a>

## AnimatablePropertyValue.CreateRotationValue(float, float, float) Method

Creates a new RotationPropertyValue object.

```csharp
public static Tizen.UI.AnimatablePropertyValue CreateRotationValue(float rotationX, float rotationY, float rotationZ);
```
#### Parameters

<a name='Tizen.UI.AnimatablePropertyValue.CreateRotationValue(float,float,float).rotationX'></a>

`rotationX` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The x-axis rotation.

<a name='Tizen.UI.AnimatablePropertyValue.CreateRotationValue(float,float,float).rotationY'></a>

`rotationY` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The y-axis rotation.

<a name='Tizen.UI.AnimatablePropertyValue.CreateRotationValue(float,float,float).rotationZ'></a>

`rotationZ` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The z-axis rotation.

#### Returns
[AnimatablePropertyValue](Tizen.UI.AnimatablePropertyValue.md 'Tizen.UI.AnimatablePropertyValue')  
The new RotationPropertyValue object.

<a name='Tizen.UI.AnimatablePropertyValue.CreateScaleValue(float,float)'></a>

## AnimatablePropertyValue.CreateScaleValue(float, float) Method

Creates a new ScalePropertyValue object.

```csharp
public static Tizen.UI.AnimatablePropertyValue CreateScaleValue(float scaleX, float scaleY);
```
#### Parameters

<a name='Tizen.UI.AnimatablePropertyValue.CreateScaleValue(float,float).scaleX'></a>

`scaleX` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The x-axis scale.

<a name='Tizen.UI.AnimatablePropertyValue.CreateScaleValue(float,float).scaleY'></a>

`scaleY` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The y-axis scale.

#### Returns
[AnimatablePropertyValue](Tizen.UI.AnimatablePropertyValue.md 'Tizen.UI.AnimatablePropertyValue')  
The new ScalePropertyValue object.

<a name='Tizen.UI.AnimatablePropertyValue.CreateSizeValue(float,float)'></a>

## AnimatablePropertyValue.CreateSizeValue(float, float) Method

Creates a new SizePropertyValue object.

```csharp
public static Tizen.UI.AnimatablePropertyValue CreateSizeValue(float width, float height);
```
#### Parameters

<a name='Tizen.UI.AnimatablePropertyValue.CreateSizeValue(float,float).width'></a>

`width` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The width value.

<a name='Tizen.UI.AnimatablePropertyValue.CreateSizeValue(float,float).height'></a>

`height` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The height value.

#### Returns
[AnimatablePropertyValue](Tizen.UI.AnimatablePropertyValue.md 'Tizen.UI.AnimatablePropertyValue')  
The new SizePropertyValue object.

<a name='Tizen.UI.AnimatablePropertyValue.CreateSizeValue(Tizen.UI.Size)'></a>

## AnimatablePropertyValue.CreateSizeValue(Size) Method

Creates a new SizePropertyValue object.

```csharp
public static Tizen.UI.AnimatablePropertyValue CreateSizeValue(Tizen.UI.Size size);
```
#### Parameters

<a name='Tizen.UI.AnimatablePropertyValue.CreateSizeValue(Tizen.UI.Size).size'></a>

`size` [Size](Tizen.UI.Size.md 'Tizen.UI.Size')

The size value.

#### Returns
[AnimatablePropertyValue](Tizen.UI.AnimatablePropertyValue.md 'Tizen.UI.AnimatablePropertyValue')  
The new SizePropertyValue object.

<a name='Tizen.UI.AnimatablePropertyValue.Dispose()'></a>

## AnimatablePropertyValue.Dispose() Method

Disposes the AnimatablePropertyValue object.

```csharp
public void Dispose();
```

Implements [Dispose()](https://docs.microsoft.com/en-us/dotnet/api/System.IDisposable.Dispose 'System.IDisposable.Dispose')

<a name='Tizen.UI.AnimatablePropertyValue.GetTargetProperties(Tizen.UI.View)'></a>

## AnimatablePropertyValue.GetTargetProperties(View) Method

Gets the target properties for the given view.

```csharp
public virtual System.Collections.Generic.IEnumerable&lt;(Tizen.UI.NativeHandle.AnimatablePropertyHandle Property,Tizen.UI.NativeHandle.PropertyValueHandle Value)> GetTargetProperties(Tizen.UI.View view);
```
#### Parameters

<a name='Tizen.UI.AnimatablePropertyValue.GetTargetProperties(Tizen.UI.View).view'></a>

`view` [View](Tizen.UI.View.md 'Tizen.UI.View')

The view to get the target properties for.

#### Returns
[System.Collections.Generic.IEnumerable&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IEnumerable-1 'System.Collections.Generic.IEnumerable`1')[&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.ValueTuple 'System.ValueTuple')[AnimatablePropertyHandle](Tizen.UI.NativeHandle.AnimatablePropertyHandle.md 'Tizen.UI.NativeHandle.AnimatablePropertyHandle')[,](https://docs.microsoft.com/en-us/dotnet/api/System.ValueTuple 'System.ValueTuple')[PropertyValueHandle](Tizen.UI.NativeHandle.PropertyValueHandle.md 'Tizen.UI.NativeHandle.PropertyValueHandle')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.ValueTuple 'System.ValueTuple')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IEnumerable-1 'System.Collections.Generic.IEnumerable`1')  
An enumeration of tuples containing the target property handle and its corresponding value handle.

<a name='Tizen.UI.AnimatablePropertyValue.GetTargetProperty(Tizen.UI.View)'></a>

## AnimatablePropertyValue.GetTargetProperty(View) Method

Gets the target property handle for the animation.

```csharp
public abstract Tizen.UI.NativeHandle.AnimatablePropertyHandle GetTargetProperty(Tizen.UI.View view);
```
#### Parameters

<a name='Tizen.UI.AnimatablePropertyValue.GetTargetProperty(Tizen.UI.View).view'></a>

`view` [View](Tizen.UI.View.md 'Tizen.UI.View')

The view to which the property belongs.

#### Returns
[AnimatablePropertyHandle](Tizen.UI.NativeHandle.AnimatablePropertyHandle.md 'Tizen.UI.NativeHandle.AnimatablePropertyHandle')  
The target property handle.






