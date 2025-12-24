### [Tizen.UI.Scene3D](Tizen.UI.Scene3D.md 'Tizen.UI.Scene3D')

## OpacityPropertyValue&lt;T> Class

Represents the opacity property value for an [Animatable3DPropertyValue&lt;T&gt;](Tizen.UI.Scene3D.Animatable3DPropertyValue_T_.md 'Tizen.UI.Scene3D.Animatable3DPropertyValue&lt;T>').

```csharp
public class OpacityPropertyValue&lt;T> : Tizen.UI.Scene3D.Animatable3DPropertyValue&lt;T>
    where T : Tizen.UI.NObject
```
#### Type parameters

<a name='Tizen.UI.Scene3D.OpacityPropertyValue_T_.T'></a>

`T`

The type of the object.

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [Tizen.UI.Scene3D.Animatable3DPropertyValue&lt;](Tizen.UI.Scene3D.Animatable3DPropertyValue_T_.md 'Tizen.UI.Scene3D.Animatable3DPropertyValue&lt;T>')[T](Tizen.UI.Scene3D.OpacityPropertyValue_T_.md#Tizen.UI.Scene3D.OpacityPropertyValue_T_.T 'Tizen.UI.Scene3D.OpacityPropertyValue&lt;T>.T')[&gt;](Tizen.UI.Scene3D.Animatable3DPropertyValue_T_.md 'Tizen.UI.Scene3D.Animatable3DPropertyValue&lt;T>') &#129106; OpacityPropertyValue&lt;T>
### Properties

<a name='Tizen.UI.Scene3D.OpacityPropertyValue_T_.Opacity'></a>

## OpacityPropertyValue&lt;T>.Opacity Property

Gets the opacity value.

```csharp
public float Opacity { get; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Scene3D.OpacityPropertyValue_T_.Value'></a>

## OpacityPropertyValue&lt;T>.Value Property

Gets the value of the property.

```csharp
public override Tizen.UI.NativeHandle.PropertyValueHandle Value { get; }
```

#### Property Value
Tizen.UI.NativeHandle.PropertyValueHandle
### Methods

<a name='Tizen.UI.Scene3D.OpacityPropertyValue_T_.GetTargetProperty(T)'></a>

## OpacityPropertyValue&lt;T>.GetTargetProperty(T) Method

Gets the target property for the animation.

```csharp
public override Tizen.UI.NativeHandle.AnimatablePropertyHandle GetTargetProperty(T view);
```
#### Parameters

<a name='Tizen.UI.Scene3D.OpacityPropertyValue_T_.GetTargetProperty(T).view'></a>

`view` [T](Tizen.UI.Scene3D.OpacityPropertyValue_T_.md#Tizen.UI.Scene3D.OpacityPropertyValue_T_.T 'Tizen.UI.Scene3D.OpacityPropertyValue&lt;T>.T')

The view to animate.

#### Returns
Tizen.UI.NativeHandle.AnimatablePropertyHandle  
The AnimatablePropertyHandle for the target property.






































