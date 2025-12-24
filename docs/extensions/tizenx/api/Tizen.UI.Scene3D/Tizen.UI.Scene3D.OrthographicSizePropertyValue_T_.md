### [Tizen.UI.Scene3D](Tizen.UI.Scene3D.md 'Tizen.UI.Scene3D')

## OrthographicSizePropertyValue&lt;T> Class

Represents a property value for an animatable 3D object that specifies the orthographic size.

```csharp
public class OrthographicSizePropertyValue&lt;T> : Tizen.UI.Scene3D.Animatable3DPropertyValue&lt;T>
    where T : Tizen.UI.NObject
```
#### Type parameters

<a name='Tizen.UI.Scene3D.OrthographicSizePropertyValue_T_.T'></a>

`T`

The type of the 3D object.

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [Tizen.UI.Scene3D.Animatable3DPropertyValue&lt;](Tizen.UI.Scene3D.Animatable3DPropertyValue_T_.md 'Tizen.UI.Scene3D.Animatable3DPropertyValue&lt;T>')[T](Tizen.UI.Scene3D.OrthographicSizePropertyValue_T_.md#Tizen.UI.Scene3D.OrthographicSizePropertyValue_T_.T 'Tizen.UI.Scene3D.OrthographicSizePropertyValue&lt;T>.T')[&gt;](Tizen.UI.Scene3D.Animatable3DPropertyValue_T_.md 'Tizen.UI.Scene3D.Animatable3DPropertyValue&lt;T>') &#129106; OrthographicSizePropertyValue&lt;T>
### Constructors

<a name='Tizen.UI.Scene3D.OrthographicSizePropertyValue_T_.OrthographicSizePropertyValue(float)'></a>

## OrthographicSizePropertyValue(float) Constructor

Initializes a new instance of the [OrthographicSizePropertyValue&lt;T&gt;](Tizen.UI.Scene3D.OrthographicSizePropertyValue_T_.md 'Tizen.UI.Scene3D.OrthographicSizePropertyValue&lt;T>') class.

```csharp
public OrthographicSizePropertyValue(float orthographicSize);
```
#### Parameters

<a name='Tizen.UI.Scene3D.OrthographicSizePropertyValue_T_.OrthographicSizePropertyValue(float).orthographicSize'></a>

`orthographicSize` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The orthographic size.
### Properties

<a name='Tizen.UI.Scene3D.OrthographicSizePropertyValue_T_.OrthographicSize'></a>

## OrthographicSizePropertyValue&lt;T>.OrthographicSize Property

Gets the orthographic size.

```csharp
public float OrthographicSize { get; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Scene3D.OrthographicSizePropertyValue_T_.Value'></a>

## OrthographicSizePropertyValue&lt;T>.Value Property

Gets the value of the property.

```csharp
public override Tizen.UI.NativeHandle.PropertyValueHandle Value { get; }
```

#### Property Value
[Tizen.UI.NativeHandle.PropertyValueHandle](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.NativeHandle.PropertyValueHandle 'Tizen.UI.NativeHandle.PropertyValueHandle')
### Methods

<a name='Tizen.UI.Scene3D.OrthographicSizePropertyValue_T_.GetTargetProperty(T)'></a>

## OrthographicSizePropertyValue&lt;T>.GetTargetProperty(T) Method

Gets the target property for the animation.

```csharp
public override Tizen.UI.NativeHandle.AnimatablePropertyHandle GetTargetProperty(T view);
```
#### Parameters

<a name='Tizen.UI.Scene3D.OrthographicSizePropertyValue_T_.GetTargetProperty(T).view'></a>

`view` [T](Tizen.UI.Scene3D.OrthographicSizePropertyValue_T_.md#Tizen.UI.Scene3D.OrthographicSizePropertyValue_T_.T 'Tizen.UI.Scene3D.OrthographicSizePropertyValue&lt;T>.T')

The view to which the property value will be applied.

#### Returns
[Tizen.UI.NativeHandle.AnimatablePropertyHandle](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.NativeHandle.AnimatablePropertyHandle 'Tizen.UI.NativeHandle.AnimatablePropertyHandle')  
The handle of the target property.





































