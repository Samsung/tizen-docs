### [Tizen.UI.Scene3D](Tizen.UI.Scene3D.md 'Tizen.UI.Scene3D')

## FieldOfViewPropertyValue&lt;T> Class

Represents a property value for a field of view animation.

```csharp
public class FieldOfViewPropertyValue&lt;T> : Tizen.UI.Scene3D.Animatable3DPropertyValue&lt;T>
    where T : Tizen.UI.NObject
```
#### Type parameters

<a name='Tizen.UI.Scene3D.FieldOfViewPropertyValue_T_.T'></a>

`T`

The type of the view to which the property value will be applied.

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [Tizen.UI.Scene3D.Animatable3DPropertyValue&lt;](Tizen.UI.Scene3D.Animatable3DPropertyValue_T_.md 'Tizen.UI.Scene3D.Animatable3DPropertyValue&lt;T>')[T](Tizen.UI.Scene3D.FieldOfViewPropertyValue_T_.md#Tizen.UI.Scene3D.FieldOfViewPropertyValue_T_.T 'Tizen.UI.Scene3D.FieldOfViewPropertyValue&lt;T>.T')[&gt;](Tizen.UI.Scene3D.Animatable3DPropertyValue_T_.md 'Tizen.UI.Scene3D.Animatable3DPropertyValue&lt;T>') &#129106; FieldOfViewPropertyValue&lt;T>
### Constructors

<a name='Tizen.UI.Scene3D.FieldOfViewPropertyValue_T_.FieldOfViewPropertyValue(float)'></a>

## FieldOfViewPropertyValue(float) Constructor

Initializes a new instance of the [FieldOfViewPropertyValue&lt;T&gt;](Tizen.UI.Scene3D.FieldOfViewPropertyValue_T_.md 'Tizen.UI.Scene3D.FieldOfViewPropertyValue&lt;T>') class.

```csharp
public FieldOfViewPropertyValue(float fieldOfView);
```
#### Parameters

<a name='Tizen.UI.Scene3D.FieldOfViewPropertyValue_T_.FieldOfViewPropertyValue(float).fieldOfView'></a>

`fieldOfView` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The field of view value in degrees.
### Properties

<a name='Tizen.UI.Scene3D.FieldOfViewPropertyValue_T_.FieldOfView'></a>

## FieldOfViewPropertyValue&lt;T>.FieldOfView Property

Gets the field of view value in degrees.

```csharp
public float FieldOfView { get; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Scene3D.FieldOfViewPropertyValue_T_.Value'></a>

## FieldOfViewPropertyValue&lt;T>.Value Property

Gets the value of the property.

```csharp
public override Tizen.UI.NativeHandle.PropertyValueHandle Value { get; }
```

#### Property Value
[Tizen.UI.NativeHandle.PropertyValueHandle](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.NativeHandle.PropertyValueHandle 'Tizen.UI.NativeHandle.PropertyValueHandle')
### Methods

<a name='Tizen.UI.Scene3D.FieldOfViewPropertyValue_T_.GetTargetProperty(T)'></a>

## FieldOfViewPropertyValue&lt;T>.GetTargetProperty(T) Method

Gets the target property for the animation.

```csharp
public override Tizen.UI.NativeHandle.AnimatablePropertyHandle GetTargetProperty(T view);
```
#### Parameters

<a name='Tizen.UI.Scene3D.FieldOfViewPropertyValue_T_.GetTargetProperty(T).view'></a>

`view` [T](Tizen.UI.Scene3D.FieldOfViewPropertyValue_T_.md#Tizen.UI.Scene3D.FieldOfViewPropertyValue_T_.T 'Tizen.UI.Scene3D.FieldOfViewPropertyValue&lt;T>.T')

The view to which the property value will be applied.

#### Returns
[Tizen.UI.NativeHandle.AnimatablePropertyHandle](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.NativeHandle.AnimatablePropertyHandle 'Tizen.UI.NativeHandle.AnimatablePropertyHandle')  
The handle of the target property.





































