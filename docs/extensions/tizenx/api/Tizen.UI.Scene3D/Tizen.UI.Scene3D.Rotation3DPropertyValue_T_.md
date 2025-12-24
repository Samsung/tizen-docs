### [Tizen.UI.Scene3D](Tizen.UI.Scene3D.md 'Tizen.UI.Scene3D')

## Rotation3DPropertyValue&lt;T> Class

Represents a 3D rotation property value for animating a view.

```csharp
public class Rotation3DPropertyValue&lt;T> : Tizen.UI.Scene3D.Animatable3DPropertyValue&lt;T>
    where T : Tizen.UI.NObject
```
#### Type parameters

<a name='Tizen.UI.Scene3D.Rotation3DPropertyValue_T_.T'></a>

`T`

The type of view to animate.

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [Tizen.UI.Scene3D.Animatable3DPropertyValue&lt;](Tizen.UI.Scene3D.Animatable3DPropertyValue_T_.md 'Tizen.UI.Scene3D.Animatable3DPropertyValue&lt;T>')[T](Tizen.UI.Scene3D.Rotation3DPropertyValue_T_.md#Tizen.UI.Scene3D.Rotation3DPropertyValue_T_.T 'Tizen.UI.Scene3D.Rotation3DPropertyValue&lt;T>.T')[&gt;](Tizen.UI.Scene3D.Animatable3DPropertyValue_T_.md 'Tizen.UI.Scene3D.Animatable3DPropertyValue&lt;T>') &#129106; Rotation3DPropertyValue&lt;T>
### Constructors

<a name='Tizen.UI.Scene3D.Rotation3DPropertyValue_T_.Rotation3DPropertyValue(Tizen.UI.Scene3D.Quaternion)'></a>

## Rotation3DPropertyValue(Quaternion) Constructor

Initializes a new instance of the [Rotation3DPropertyValue&lt;T&gt;](Tizen.UI.Scene3D.Rotation3DPropertyValue_T_.md 'Tizen.UI.Scene3D.Rotation3DPropertyValue&lt;T>') class.

```csharp
public Rotation3DPropertyValue(Tizen.UI.Scene3D.Quaternion quaternion);
```
#### Parameters

<a name='Tizen.UI.Scene3D.Rotation3DPropertyValue_T_.Rotation3DPropertyValue(Tizen.UI.Scene3D.Quaternion).quaternion'></a>

`quaternion` [Quaternion](Tizen.UI.Scene3D.Quaternion.md 'Tizen.UI.Scene3D.Quaternion')

The initial rotation value.
### Properties

<a name='Tizen.UI.Scene3D.Rotation3DPropertyValue_T_.Quaternion'></a>

## Rotation3DPropertyValue&lt;T>.Quaternion Property

Gets the current rotation value.

```csharp
public Tizen.UI.Scene3D.Quaternion Quaternion { get; }
```

#### Property Value
[Quaternion](Tizen.UI.Scene3D.Quaternion.md 'Tizen.UI.Scene3D.Quaternion')

<a name='Tizen.UI.Scene3D.Rotation3DPropertyValue_T_.Value'></a>

## Rotation3DPropertyValue&lt;T>.Value Property

Gets the value of the property.

```csharp
public override Tizen.UI.NativeHandle.PropertyValueHandle Value { get; }
```

#### Property Value
[Tizen.UI.NativeHandle.PropertyValueHandle](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.NativeHandle.PropertyValueHandle 'Tizen.UI.NativeHandle.PropertyValueHandle')
### Methods

<a name='Tizen.UI.Scene3D.Rotation3DPropertyValue_T_.GetTargetProperty(T)'></a>

## Rotation3DPropertyValue&lt;T>.GetTargetProperty(T) Method

Gets the target property for the animation.

```csharp
public override Tizen.UI.NativeHandle.AnimatablePropertyHandle GetTargetProperty(T view);
```
#### Parameters

<a name='Tizen.UI.Scene3D.Rotation3DPropertyValue_T_.GetTargetProperty(T).view'></a>

`view` [T](Tizen.UI.Scene3D.Rotation3DPropertyValue_T_.md#Tizen.UI.Scene3D.Rotation3DPropertyValue_T_.T 'Tizen.UI.Scene3D.Rotation3DPropertyValue&lt;T>.T')

The view to which the property value will be applied.

#### Returns
[Tizen.UI.NativeHandle.AnimatablePropertyHandle](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.NativeHandle.AnimatablePropertyHandle 'Tizen.UI.NativeHandle.AnimatablePropertyHandle')  
The handle of the target property.





































