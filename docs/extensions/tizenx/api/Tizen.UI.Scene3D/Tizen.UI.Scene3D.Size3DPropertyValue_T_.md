### [Tizen.UI.Scene3D](Tizen.UI.Scene3D.md 'Tizen.UI.Scene3D')

## Size3DPropertyValue&lt;T> Class

Represents a 3D size property value that can be animated.

```csharp
public class Size3DPropertyValue&lt;T> : Tizen.UI.Scene3D.Animatable3DPropertyValue&lt;T>
    where T : Tizen.UI.NObject
```
#### Type parameters

<a name='Tizen.UI.Scene3D.Size3DPropertyValue_T_.T'></a>

`T`

The type of view that the property value applies to.

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [Tizen.UI.Scene3D.Animatable3DPropertyValue&lt;](Tizen.UI.Scene3D.Animatable3DPropertyValue_T_.md 'Tizen.UI.Scene3D.Animatable3DPropertyValue&lt;T>')[T](Tizen.UI.Scene3D.Size3DPropertyValue_T_.md#Tizen.UI.Scene3D.Size3DPropertyValue_T_.T 'Tizen.UI.Scene3D.Size3DPropertyValue&lt;T>.T')[&gt;](Tizen.UI.Scene3D.Animatable3DPropertyValue_T_.md 'Tizen.UI.Scene3D.Animatable3DPropertyValue&lt;T>') &#129106; Size3DPropertyValue&lt;T>
### Constructors

<a name='Tizen.UI.Scene3D.Size3DPropertyValue_T_.Size3DPropertyValue(float,float,float)'></a>

## Size3DPropertyValue(float, float, float) Constructor

Initializes a new instance of the [Size3DPropertyValue&lt;T&gt;](Tizen.UI.Scene3D.Size3DPropertyValue_T_.md 'Tizen.UI.Scene3D.Size3DPropertyValue&lt;T>') class with the specified values.

```csharp
public Size3DPropertyValue(float x, float y, float z);
```
#### Parameters

<a name='Tizen.UI.Scene3D.Size3DPropertyValue_T_.Size3DPropertyValue(float,float,float).x'></a>

`x` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The width component of the size.

<a name='Tizen.UI.Scene3D.Size3DPropertyValue_T_.Size3DPropertyValue(float,float,float).y'></a>

`y` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The height component of the size.

<a name='Tizen.UI.Scene3D.Size3DPropertyValue_T_.Size3DPropertyValue(float,float,float).z'></a>

`z` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The depth component of the size.

<a name='Tizen.UI.Scene3D.Size3DPropertyValue_T_.Size3DPropertyValue(Tizen.UI.Scene3D.Size3D)'></a>

## Size3DPropertyValue(Size3D) Constructor

Initializes a new instance of the [Size3DPropertyValue&lt;T&gt;](Tizen.UI.Scene3D.Size3DPropertyValue_T_.md 'Tizen.UI.Scene3D.Size3DPropertyValue&lt;T>') class with the specified size.

```csharp
public Size3DPropertyValue(Tizen.UI.Scene3D.Size3D size);
```
#### Parameters

<a name='Tizen.UI.Scene3D.Size3DPropertyValue_T_.Size3DPropertyValue(Tizen.UI.Scene3D.Size3D).size'></a>

`size` [Size3D](Tizen.UI.Scene3D.Size3D.md 'Tizen.UI.Scene3D.Size3D')

The size to use.
### Properties

<a name='Tizen.UI.Scene3D.Size3DPropertyValue_T_.Size'></a>

## Size3DPropertyValue&lt;T>.Size Property

Gets the size represented by this property value.

```csharp
public Tizen.UI.Scene3D.Size3D Size { get; }
```

#### Property Value
[Size3D](Tizen.UI.Scene3D.Size3D.md 'Tizen.UI.Scene3D.Size3D')

<a name='Tizen.UI.Scene3D.Size3DPropertyValue_T_.Value'></a>

## Size3DPropertyValue&lt;T>.Value Property

Gets the value of the property.

```csharp
public override Tizen.UI.NativeHandle.PropertyValueHandle Value { get; }
```

#### Property Value
[Tizen.UI.NativeHandle.PropertyValueHandle](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.NativeHandle.PropertyValueHandle 'Tizen.UI.NativeHandle.PropertyValueHandle')
### Methods

<a name='Tizen.UI.Scene3D.Size3DPropertyValue_T_.GetTargetProperty(T)'></a>

## Size3DPropertyValue&lt;T>.GetTargetProperty(T) Method

Gets the target property for the animation.

```csharp
public override Tizen.UI.NativeHandle.AnimatablePropertyHandle GetTargetProperty(T view);
```
#### Parameters

<a name='Tizen.UI.Scene3D.Size3DPropertyValue_T_.GetTargetProperty(T).view'></a>

`view` [T](Tizen.UI.Scene3D.Size3DPropertyValue_T_.md#Tizen.UI.Scene3D.Size3DPropertyValue_T_.T 'Tizen.UI.Scene3D.Size3DPropertyValue&lt;T>.T')

The view to which the property value will be applied.

#### Returns
[Tizen.UI.NativeHandle.AnimatablePropertyHandle](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.NativeHandle.AnimatablePropertyHandle 'Tizen.UI.NativeHandle.AnimatablePropertyHandle')  
The handle of the target property.





































