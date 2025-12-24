### [Tizen.UI.Scene3D](Tizen.UI.Scene3D.md 'Tizen.UI.Scene3D')

## Scale3DPropertyValue&lt;T> Class

Represents a 3D scale property value that can be animated.

```csharp
public class Scale3DPropertyValue&lt;T> : Tizen.UI.Scene3D.Animatable3DPropertyValue&lt;T>
    where T : Tizen.UI.NObject
```
#### Type parameters

<a name='Tizen.UI.Scene3D.Scale3DPropertyValue_T_.T'></a>

`T`

The type of view to which the property value will be applied.

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [Tizen.UI.Scene3D.Animatable3DPropertyValue&lt;](Tizen.UI.Scene3D.Animatable3DPropertyValue_T_.md 'Tizen.UI.Scene3D.Animatable3DPropertyValue&lt;T>')[T](Tizen.UI.Scene3D.Scale3DPropertyValue_T_.md#Tizen.UI.Scene3D.Scale3DPropertyValue_T_.T 'Tizen.UI.Scene3D.Scale3DPropertyValue&lt;T>.T')[&gt;](Tizen.UI.Scene3D.Animatable3DPropertyValue_T_.md 'Tizen.UI.Scene3D.Animatable3DPropertyValue&lt;T>') &#129106; Scale3DPropertyValue&lt;T>
### Constructors

<a name='Tizen.UI.Scene3D.Scale3DPropertyValue_T_.Scale3DPropertyValue(float,float,float)'></a>

## Scale3DPropertyValue(float, float, float) Constructor

Initializes a new instance of the [Scale3DPropertyValue&lt;T&gt;](Tizen.UI.Scene3D.Scale3DPropertyValue_T_.md 'Tizen.UI.Scene3D.Scale3DPropertyValue&lt;T>') class.

```csharp
public Scale3DPropertyValue(float x, float y, float z);
```
#### Parameters

<a name='Tizen.UI.Scene3D.Scale3DPropertyValue_T_.Scale3DPropertyValue(float,float,float).x'></a>

`x` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The X component of the scale.

<a name='Tizen.UI.Scene3D.Scale3DPropertyValue_T_.Scale3DPropertyValue(float,float,float).y'></a>

`y` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The Y component of the scale.

<a name='Tizen.UI.Scene3D.Scale3DPropertyValue_T_.Scale3DPropertyValue(float,float,float).z'></a>

`z` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The Z component of the scale.
### Properties

<a name='Tizen.UI.Scene3D.Scale3DPropertyValue_T_.Scale'></a>

## Scale3DPropertyValue&lt;T>.Scale Property

Gets the scale of the property value.

```csharp
public Tizen.UI.Scene3D.Size3D Scale { get; }
```

#### Property Value
[Size3D](Tizen.UI.Scene3D.Size3D.md 'Tizen.UI.Scene3D.Size3D')

<a name='Tizen.UI.Scene3D.Scale3DPropertyValue_T_.Value'></a>

## Scale3DPropertyValue&lt;T>.Value Property

Gets the value of the property.

```csharp
public override Tizen.UI.NativeHandle.PropertyValueHandle Value { get; }
```

#### Property Value
[Tizen.UI.NativeHandle.PropertyValueHandle](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.NativeHandle.PropertyValueHandle 'Tizen.UI.NativeHandle.PropertyValueHandle')
### Methods

<a name='Tizen.UI.Scene3D.Scale3DPropertyValue_T_.GetTargetProperty(T)'></a>

## Scale3DPropertyValue&lt;T>.GetTargetProperty(T) Method

Gets the target property for the animation.

```csharp
public override Tizen.UI.NativeHandle.AnimatablePropertyHandle GetTargetProperty(T view);
```
#### Parameters

<a name='Tizen.UI.Scene3D.Scale3DPropertyValue_T_.GetTargetProperty(T).view'></a>

`view` [T](Tizen.UI.Scene3D.Scale3DPropertyValue_T_.md#Tizen.UI.Scene3D.Scale3DPropertyValue_T_.T 'Tizen.UI.Scene3D.Scale3DPropertyValue&lt;T>.T')

The view to which the property value will be applied.

#### Returns
[Tizen.UI.NativeHandle.AnimatablePropertyHandle](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.NativeHandle.AnimatablePropertyHandle 'Tizen.UI.NativeHandle.AnimatablePropertyHandle')  
The handle of the target property.





































