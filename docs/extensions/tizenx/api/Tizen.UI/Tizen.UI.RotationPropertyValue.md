### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## RotationPropertyValue Class

Represents a property value that represents a rotation in three dimensions.

```csharp
public class RotationPropertyValue : Tizen.UI.AnimatablePropertyValue
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [AnimatablePropertyValue](Tizen.UI.AnimatablePropertyValue.md 'Tizen.UI.AnimatablePropertyValue') &#129106; RotationPropertyValue
### Constructors

<a name='Tizen.UI.RotationPropertyValue.RotationPropertyValue(float,float,float)'></a>

## RotationPropertyValue(float, float, float) Constructor

Initializes a new instance of the [RotationPropertyValue](Tizen.UI.RotationPropertyValue.md 'Tizen.UI.RotationPropertyValue') class.

```csharp
public RotationPropertyValue(float rotationX, float rotationY, float rotationZ);
```
#### Parameters

<a name='Tizen.UI.RotationPropertyValue.RotationPropertyValue(float,float,float).rotationX'></a>

`rotationX` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The angle of rotation around the X-axis, in degrees.

<a name='Tizen.UI.RotationPropertyValue.RotationPropertyValue(float,float,float).rotationY'></a>

`rotationY` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The angle of rotation around the Y-axis, in degrees.

<a name='Tizen.UI.RotationPropertyValue.RotationPropertyValue(float,float,float).rotationZ'></a>

`rotationZ` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The angle of rotation around the Z-axis, in degrees.
### Properties

<a name='Tizen.UI.RotationPropertyValue.RotationX'></a>

## RotationPropertyValue.RotationX Property

Gets the angle of rotation around the X-axis, in degrees.

```csharp
public float RotationX { get; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.RotationPropertyValue.RotationY'></a>

## RotationPropertyValue.RotationY Property

Gets the angle of rotation around the Y-axis, in degrees.

```csharp
public float RotationY { get; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.RotationPropertyValue.RotationZ'></a>

## RotationPropertyValue.RotationZ Property

Gets the angle of rotation around the Z-axis, in degrees.

```csharp
public float RotationZ { get; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.RotationPropertyValue.Value'></a>

## RotationPropertyValue.Value Property

Gets the value of the property.

```csharp
public override Tizen.UI.NativeHandle.PropertyValueHandle Value { get; }
```

#### Property Value
[PropertyValueHandle](Tizen.UI.NativeHandle.PropertyValueHandle.md 'Tizen.UI.NativeHandle.PropertyValueHandle')
### Methods

<a name='Tizen.UI.RotationPropertyValue.GetTargetProperty(Tizen.UI.View)'></a>

## RotationPropertyValue.GetTargetProperty(View) Method

Gets the target property for the animation.

```csharp
public override Tizen.UI.NativeHandle.AnimatablePropertyHandle GetTargetProperty(Tizen.UI.View view);
```
#### Parameters

<a name='Tizen.UI.RotationPropertyValue.GetTargetProperty(Tizen.UI.View).view'></a>

`view` [View](Tizen.UI.View.md 'Tizen.UI.View')

The view to which the property value will be applied.

#### Returns
[AnimatablePropertyHandle](Tizen.UI.NativeHandle.AnimatablePropertyHandle.md 'Tizen.UI.NativeHandle.AnimatablePropertyHandle')  
The handle of the target property.






