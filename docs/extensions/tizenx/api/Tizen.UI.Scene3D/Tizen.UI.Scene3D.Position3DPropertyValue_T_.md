### [Tizen.UI.Scene3D](Tizen.UI.Scene3D.md 'Tizen.UI.Scene3D')

## Position3DPropertyValue&lt;T> Class

```csharp
public class Position3DPropertyValue&lt;T> : Tizen.UI.Scene3D.Animatable3DPropertyValue&lt;T>
    where T : Tizen.UI.NObject
```
#### Type parameters

<a name='Tizen.UI.Scene3D.Position3DPropertyValue_T_.T'></a>

`T`

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [Tizen.UI.Scene3D.Animatable3DPropertyValue&lt;](Tizen.UI.Scene3D.Animatable3DPropertyValue_T_.md 'Tizen.UI.Scene3D.Animatable3DPropertyValue&lt;T>')[T](Tizen.UI.Scene3D.Position3DPropertyValue_T_.md#Tizen.UI.Scene3D.Position3DPropertyValue_T_.T 'Tizen.UI.Scene3D.Position3DPropertyValue&lt;T>.T')[&gt;](Tizen.UI.Scene3D.Animatable3DPropertyValue_T_.md 'Tizen.UI.Scene3D.Animatable3DPropertyValue&lt;T>') &#129106; Position3DPropertyValue&lt;T>
### Constructors

<a name='Tizen.UI.Scene3D.Position3DPropertyValue_T_.Position3DPropertyValue(float,float,float)'></a>

## Position3DPropertyValue(float, float, float) Constructor

Initializes a new instance of the [Position3DPropertyValue](https://docs.microsoft.com/en-us/dotnet/api/Position3DPropertyValue 'Position3DPropertyValue') class.

```csharp
public Position3DPropertyValue(float x, float y, float z);
```
#### Parameters

<a name='Tizen.UI.Scene3D.Position3DPropertyValue_T_.Position3DPropertyValue(float,float,float).x'></a>

`x` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The x-coordinate of the position.

<a name='Tizen.UI.Scene3D.Position3DPropertyValue_T_.Position3DPropertyValue(float,float,float).y'></a>

`y` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The y-coordinate of the position.

<a name='Tizen.UI.Scene3D.Position3DPropertyValue_T_.Position3DPropertyValue(float,float,float).z'></a>

`z` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The z-coordinate of the position.
### Properties

<a name='Tizen.UI.Scene3D.Position3DPropertyValue_T_.Value'></a>

## Position3DPropertyValue&lt;T>.Value Property

Gets the value of the property.

```csharp
public override Tizen.UI.NativeHandle.PropertyValueHandle Value { get; }
```

#### Property Value
[Tizen.UI.NativeHandle.PropertyValueHandle](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.NativeHandle.PropertyValueHandle 'Tizen.UI.NativeHandle.PropertyValueHandle')

<a name='Tizen.UI.Scene3D.Position3DPropertyValue_T_.X'></a>

## Position3DPropertyValue&lt;T>.X Property

Gets the x-coordinate of the position.

```csharp
public float X { get; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Scene3D.Position3DPropertyValue_T_.Y'></a>

## Position3DPropertyValue&lt;T>.Y Property

Gets the y-coordinate of the position.

```csharp
public float Y { get; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Scene3D.Position3DPropertyValue_T_.Z'></a>

## Position3DPropertyValue&lt;T>.Z Property

Gets the z-coordinate of the position.

```csharp
public float Z { get; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')
### Methods

<a name='Tizen.UI.Scene3D.Position3DPropertyValue_T_.GetTargetProperty(T)'></a>

## Position3DPropertyValue&lt;T>.GetTargetProperty(T) Method

Gets the target property of the view.

```csharp
public override Tizen.UI.NativeHandle.AnimatablePropertyHandle GetTargetProperty(T view);
```
#### Parameters

<a name='Tizen.UI.Scene3D.Position3DPropertyValue_T_.GetTargetProperty(T).view'></a>

`view` [T](Tizen.UI.Scene3D.Position3DPropertyValue_T_.md#Tizen.UI.Scene3D.Position3DPropertyValue_T_.T 'Tizen.UI.Scene3D.Position3DPropertyValue&lt;T>.T')

The view.

#### Returns
[Tizen.UI.NativeHandle.AnimatablePropertyHandle](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.NativeHandle.AnimatablePropertyHandle 'Tizen.UI.NativeHandle.AnimatablePropertyHandle')  
The target property handle.





































