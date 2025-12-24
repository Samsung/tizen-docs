### [Tizen.UI.Scene3D](Tizen.UI.Scene3D.md 'Tizen.UI.Scene3D')

## Animatable3DPropertyValue&lt;T> Class

Animatable3DPropertyValue is an abstract class that represents a property value that can be animated in 3D.

```csharp
public abstract class Animatable3DPropertyValue&lt;T> :
System.IDisposable
    where T : Tizen.UI.NObject
```
#### Type parameters

<a name='Tizen.UI.Scene3D.Animatable3DPropertyValue_T_.T'></a>

`T`

The type of view that the property value belongs to.

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; Animatable3DPropertyValue&lt;T>

Derived  
&#8627; [CustomPropertyValue&lt;T&gt;](Tizen.UI.Scene3D.CustomPropertyValue_T_.md 'Tizen.UI.Scene3D.CustomPropertyValue&lt;T>')  
&#8627; [FieldOfViewPropertyValue&lt;T&gt;](Tizen.UI.Scene3D.FieldOfViewPropertyValue_T_.md 'Tizen.UI.Scene3D.FieldOfViewPropertyValue&lt;T>')  
&#8627; [OpacityPropertyValue&lt;T&gt;](Tizen.UI.Scene3D.OpacityPropertyValue_T_.md 'Tizen.UI.Scene3D.OpacityPropertyValue&lt;T>')  
&#8627; [OrthographicSizePropertyValue&lt;T&gt;](Tizen.UI.Scene3D.OrthographicSizePropertyValue_T_.md 'Tizen.UI.Scene3D.OrthographicSizePropertyValue&lt;T>')  
&#8627; [Position3DPropertyValue&lt;T&gt;](Tizen.UI.Scene3D.Position3DPropertyValue_T_.md 'Tizen.UI.Scene3D.Position3DPropertyValue&lt;T>')  
&#8627; [Rotation3DPropertyValue&lt;T&gt;](Tizen.UI.Scene3D.Rotation3DPropertyValue_T_.md 'Tizen.UI.Scene3D.Rotation3DPropertyValue&lt;T>')  
&#8627; [Scale3DPropertyValue&lt;T&gt;](Tizen.UI.Scene3D.Scale3DPropertyValue_T_.md 'Tizen.UI.Scene3D.Scale3DPropertyValue&lt;T>')  
&#8627; [Size3DPropertyValue&lt;T&gt;](Tizen.UI.Scene3D.Size3DPropertyValue_T_.md 'Tizen.UI.Scene3D.Size3DPropertyValue&lt;T>')

Implements [System.IDisposable](https://docs.microsoft.com/en-us/dotnet/api/System.IDisposable 'System.IDisposable')
### Properties

<a name='Tizen.UI.Scene3D.Animatable3DPropertyValue_T_.Value'></a>

## Animatable3DPropertyValue&lt;T>.Value Property

Gets the [Tizen.UI.NativeHandle.PropertyValueHandle](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.NativeHandle.PropertyValueHandle 'Tizen.UI.NativeHandle.PropertyValueHandle') of the property.

```csharp
public abstract Tizen.UI.NativeHandle.PropertyValueHandle Value { get; }
```

#### Property Value
[Tizen.UI.NativeHandle.PropertyValueHandle](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.NativeHandle.PropertyValueHandle 'Tizen.UI.NativeHandle.PropertyValueHandle')
### Methods

<a name='Tizen.UI.Scene3D.Animatable3DPropertyValue_T_.CreateCustomValue(string,object,bool)'></a>

## Animatable3DPropertyValue&lt;T>.CreateCustomValue(string, object, bool) Method

Creates a new [Tizen.UI.CustomPropertyValue](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.CustomPropertyValue 'Tizen.UI.CustomPropertyValue') object with the given property name and value.

```csharp
public static Tizen.UI.AnimatablePropertyValue CreateCustomValue(string propertyName, object value, bool useVector3=false);
```
#### Parameters

<a name='Tizen.UI.Scene3D.Animatable3DPropertyValue_T_.CreateCustomValue(string,object,bool).propertyName'></a>

`propertyName` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The name of the custom property.

<a name='Tizen.UI.Scene3D.Animatable3DPropertyValue_T_.CreateCustomValue(string,object,bool).value'></a>

`value` [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object')

The value of the custom property.

<a name='Tizen.UI.Scene3D.Animatable3DPropertyValue_T_.CreateCustomValue(string,object,bool).useVector3'></a>

`useVector3` [System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

#### Returns
[Tizen.UI.AnimatablePropertyValue](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.AnimatablePropertyValue 'Tizen.UI.AnimatablePropertyValue')  
The new CustomPropertyValue object.

<a name='Tizen.UI.Scene3D.Animatable3DPropertyValue_T_.CreateCustomValue(string,Tizen.UI.NativeHandle.PropertyValueHandle)'></a>

## Animatable3DPropertyValue&lt;T>.CreateCustomValue(string, PropertyValueHandle) Method

Creates a new [Tizen.UI.CustomPropertyValue](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.CustomPropertyValue 'Tizen.UI.CustomPropertyValue') object with the given property name and value.

```csharp
public static Tizen.UI.Scene3D.Animatable3DPropertyValue&lt;T> CreateCustomValue(string propertyName, Tizen.UI.NativeHandle.PropertyValueHandle value);
```
#### Parameters

<a name='Tizen.UI.Scene3D.Animatable3DPropertyValue_T_.CreateCustomValue(string,Tizen.UI.NativeHandle.PropertyValueHandle).propertyName'></a>

`propertyName` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The name of the custom property.

<a name='Tizen.UI.Scene3D.Animatable3DPropertyValue_T_.CreateCustomValue(string,Tizen.UI.NativeHandle.PropertyValueHandle).value'></a>

`value` [Tizen.UI.NativeHandle.PropertyValueHandle](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.NativeHandle.PropertyValueHandle 'Tizen.UI.NativeHandle.PropertyValueHandle')

The value of the custom property.

#### Returns
[Tizen.UI.Scene3D.Animatable3DPropertyValue&lt;](Tizen.UI.Scene3D.Animatable3DPropertyValue_T_.md 'Tizen.UI.Scene3D.Animatable3DPropertyValue&lt;T>')[T](Tizen.UI.Scene3D.Animatable3DPropertyValue_T_.md#Tizen.UI.Scene3D.Animatable3DPropertyValue_T_.T 'Tizen.UI.Scene3D.Animatable3DPropertyValue&lt;T>.T')[&gt;](Tizen.UI.Scene3D.Animatable3DPropertyValue_T_.md 'Tizen.UI.Scene3D.Animatable3DPropertyValue&lt;T>')  
The new CustomPropertyValue object.

<a name='Tizen.UI.Scene3D.Animatable3DPropertyValue_T_.CreateOpacityValue(float)'></a>

## Animatable3DPropertyValue&lt;T>.CreateOpacityValue(float) Method

Creates a new [Tizen.UI.OpacityPropertyValue](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.OpacityPropertyValue 'Tizen.UI.OpacityPropertyValue') object with the given value.

```csharp
public static Tizen.UI.Scene3D.Animatable3DPropertyValue&lt;T> CreateOpacityValue(float opacity);
```
#### Parameters

<a name='Tizen.UI.Scene3D.Animatable3DPropertyValue_T_.CreateOpacityValue(float).opacity'></a>

`opacity` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The opacity value.

#### Returns
[Tizen.UI.Scene3D.Animatable3DPropertyValue&lt;](Tizen.UI.Scene3D.Animatable3DPropertyValue_T_.md 'Tizen.UI.Scene3D.Animatable3DPropertyValue&lt;T>')[T](Tizen.UI.Scene3D.Animatable3DPropertyValue_T_.md#Tizen.UI.Scene3D.Animatable3DPropertyValue_T_.T 'Tizen.UI.Scene3D.Animatable3DPropertyValue&lt;T>.T')[&gt;](Tizen.UI.Scene3D.Animatable3DPropertyValue_T_.md 'Tizen.UI.Scene3D.Animatable3DPropertyValue&lt;T>')  
The new OpacityPropertyValue object.

<a name='Tizen.UI.Scene3D.Animatable3DPropertyValue_T_.CreateOrthographicSizeValue(float)'></a>

## Animatable3DPropertyValue&lt;T>.CreateOrthographicSizeValue(float) Method

Creates a new [OrthographicSizePropertyValue](https://docs.microsoft.com/en-us/dotnet/api/OrthographicSizePropertyValue 'OrthographicSizePropertyValue') object with the given value.

```csharp
public static Tizen.UI.Scene3D.Animatable3DPropertyValue&lt;T> CreateOrthographicSizeValue(float orthographicSize);
```
#### Parameters

<a name='Tizen.UI.Scene3D.Animatable3DPropertyValue_T_.CreateOrthographicSizeValue(float).orthographicSize'></a>

`orthographicSize` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The orthographic size value.

#### Returns
[Tizen.UI.Scene3D.Animatable3DPropertyValue&lt;](Tizen.UI.Scene3D.Animatable3DPropertyValue_T_.md 'Tizen.UI.Scene3D.Animatable3DPropertyValue&lt;T>')[T](Tizen.UI.Scene3D.Animatable3DPropertyValue_T_.md#Tizen.UI.Scene3D.Animatable3DPropertyValue_T_.T 'Tizen.UI.Scene3D.Animatable3DPropertyValue&lt;T>.T')[&gt;](Tizen.UI.Scene3D.Animatable3DPropertyValue_T_.md 'Tizen.UI.Scene3D.Animatable3DPropertyValue&lt;T>')  
The new OrthographicSizePropertyValue object.

<a name='Tizen.UI.Scene3D.Animatable3DPropertyValue_T_.CreatePosition3DValue(float,float,float)'></a>

## Animatable3DPropertyValue&lt;T>.CreatePosition3DValue(float, float, float) Method

Creates a new [Position3DPropertyValue&lt;T&gt;](Tizen.UI.Scene3D.Position3DPropertyValue_T_.md 'Tizen.UI.Scene3D.Position3DPropertyValue&lt;T>') object with the given values.

```csharp
public static Tizen.UI.Scene3D.Animatable3DPropertyValue&lt;T> CreatePosition3DValue(float x, float y, float z);
```
#### Parameters

<a name='Tizen.UI.Scene3D.Animatable3DPropertyValue_T_.CreatePosition3DValue(float,float,float).x'></a>

`x` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The x-coordinate of the position.

<a name='Tizen.UI.Scene3D.Animatable3DPropertyValue_T_.CreatePosition3DValue(float,float,float).y'></a>

`y` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The y-coordinate of the position.

<a name='Tizen.UI.Scene3D.Animatable3DPropertyValue_T_.CreatePosition3DValue(float,float,float).z'></a>

`z` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The z-coordinate of the position.

#### Returns
[Tizen.UI.Scene3D.Animatable3DPropertyValue&lt;](Tizen.UI.Scene3D.Animatable3DPropertyValue_T_.md 'Tizen.UI.Scene3D.Animatable3DPropertyValue&lt;T>')[T](Tizen.UI.Scene3D.Animatable3DPropertyValue_T_.md#Tizen.UI.Scene3D.Animatable3DPropertyValue_T_.T 'Tizen.UI.Scene3D.Animatable3DPropertyValue&lt;T>.T')[&gt;](Tizen.UI.Scene3D.Animatable3DPropertyValue_T_.md 'Tizen.UI.Scene3D.Animatable3DPropertyValue&lt;T>')  
The new Position3DPropertyValue object.

<a name='Tizen.UI.Scene3D.Animatable3DPropertyValue_T_.CreateScale3DValue(Tizen.UI.Scene3D.Size3D)'></a>

## Animatable3DPropertyValue&lt;T>.CreateScale3DValue(Size3D) Method

Creates a new [CreateScale3DValue(Size3D)](Tizen.UI.Scene3D.Animatable3DPropertyValue_T_.md#Tizen.UI.Scene3D.Animatable3DPropertyValue_T_.CreateScale3DValue(Tizen.UI.Scene3D.Size3D) 'Tizen.UI.Scene3D.Animatable3DPropertyValue&lt;T>.CreateScale3DValue(Tizen.UI.Scene3D.Size3D)') object with the given values.

```csharp
public static Tizen.UI.Scene3D.Animatable3DPropertyValue&lt;T> CreateScale3DValue(Tizen.UI.Scene3D.Size3D scale);
```
#### Parameters

<a name='Tizen.UI.Scene3D.Animatable3DPropertyValue_T_.CreateScale3DValue(Tizen.UI.Scene3D.Size3D).scale'></a>

`scale` [Size3D](Tizen.UI.Scene3D.Size3D.md 'Tizen.UI.Scene3D.Size3D')

The scale values.

#### Returns
[Tizen.UI.Scene3D.Animatable3DPropertyValue&lt;](Tizen.UI.Scene3D.Animatable3DPropertyValue_T_.md 'Tizen.UI.Scene3D.Animatable3DPropertyValue&lt;T>')[T](Tizen.UI.Scene3D.Animatable3DPropertyValue_T_.md#Tizen.UI.Scene3D.Animatable3DPropertyValue_T_.T 'Tizen.UI.Scene3D.Animatable3DPropertyValue&lt;T>.T')[&gt;](Tizen.UI.Scene3D.Animatable3DPropertyValue_T_.md 'Tizen.UI.Scene3D.Animatable3DPropertyValue&lt;T>')  
The new Scale3DPropertyValue object.

<a name='Tizen.UI.Scene3D.Animatable3DPropertyValue_T_.CreateSize3DValue(float,float,float)'></a>

## Animatable3DPropertyValue&lt;T>.CreateSize3DValue(float, float, float) Method

Creates a new [Size3DPropertyValue](https://docs.microsoft.com/en-us/dotnet/api/Size3DPropertyValue 'Size3DPropertyValue') object with the given values.

```csharp
public static Tizen.UI.Scene3D.Animatable3DPropertyValue&lt;T> CreateSize3DValue(float x, float y, float z);
```
#### Parameters

<a name='Tizen.UI.Scene3D.Animatable3DPropertyValue_T_.CreateSize3DValue(float,float,float).x'></a>

`x` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The x-coordinate of the size.

<a name='Tizen.UI.Scene3D.Animatable3DPropertyValue_T_.CreateSize3DValue(float,float,float).y'></a>

`y` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The y-coordinate of the size.

<a name='Tizen.UI.Scene3D.Animatable3DPropertyValue_T_.CreateSize3DValue(float,float,float).z'></a>

`z` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The z-coordinate of the size.

#### Returns
[Tizen.UI.Scene3D.Animatable3DPropertyValue&lt;](Tizen.UI.Scene3D.Animatable3DPropertyValue_T_.md 'Tizen.UI.Scene3D.Animatable3DPropertyValue&lt;T>')[T](Tizen.UI.Scene3D.Animatable3DPropertyValue_T_.md#Tizen.UI.Scene3D.Animatable3DPropertyValue_T_.T 'Tizen.UI.Scene3D.Animatable3DPropertyValue&lt;T>.T')[&gt;](Tizen.UI.Scene3D.Animatable3DPropertyValue_T_.md 'Tizen.UI.Scene3D.Animatable3DPropertyValue&lt;T>')  
The new Size3DPropertyValue object.

<a name='Tizen.UI.Scene3D.Animatable3DPropertyValue_T_.CreateSize3DValue(Tizen.UI.Scene3D.Size3D)'></a>

## Animatable3DPropertyValue&lt;T>.CreateSize3DValue(Size3D) Method

Creates a new [Size3DPropertyValue](https://docs.microsoft.com/en-us/dotnet/api/Size3DPropertyValue 'Size3DPropertyValue') object with the given values.

```csharp
public static Tizen.UI.Scene3D.Animatable3DPropertyValue&lt;T> CreateSize3DValue(Tizen.UI.Scene3D.Size3D size);
```
#### Parameters

<a name='Tizen.UI.Scene3D.Animatable3DPropertyValue_T_.CreateSize3DValue(Tizen.UI.Scene3D.Size3D).size'></a>

`size` [Size3D](Tizen.UI.Scene3D.Size3D.md 'Tizen.UI.Scene3D.Size3D')

The size values.

#### Returns
[Tizen.UI.Scene3D.Animatable3DPropertyValue&lt;](Tizen.UI.Scene3D.Animatable3DPropertyValue_T_.md 'Tizen.UI.Scene3D.Animatable3DPropertyValue&lt;T>')[T](Tizen.UI.Scene3D.Animatable3DPropertyValue_T_.md#Tizen.UI.Scene3D.Animatable3DPropertyValue_T_.T 'Tizen.UI.Scene3D.Animatable3DPropertyValue&lt;T>.T')[&gt;](Tizen.UI.Scene3D.Animatable3DPropertyValue_T_.md 'Tizen.UI.Scene3D.Animatable3DPropertyValue&lt;T>')  
The new Size3DPropertyValue object.

<a name='Tizen.UI.Scene3D.Animatable3DPropertyValue_T_.Dispose()'></a>

## Animatable3DPropertyValue&lt;T>.Dispose() Method

Disposes the Animatable3DPropertyValue object.

```csharp
public void Dispose();
```

Implements [Dispose()](https://docs.microsoft.com/en-us/dotnet/api/System.IDisposable.Dispose 'System.IDisposable.Dispose')

<a name='Tizen.UI.Scene3D.Animatable3DPropertyValue_T_.GetTargetProperty(T)'></a>

## Animatable3DPropertyValue&lt;T>.GetTargetProperty(T) Method

Gets the [Tizen.UI.NativeHandle.AnimatablePropertyHandle](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.NativeHandle.AnimatablePropertyHandle 'Tizen.UI.NativeHandle.AnimatablePropertyHandle') for the animation.

```csharp
public abstract Tizen.UI.NativeHandle.AnimatablePropertyHandle GetTargetProperty(T view);
```
#### Parameters

<a name='Tizen.UI.Scene3D.Animatable3DPropertyValue_T_.GetTargetProperty(T).view'></a>

`view` [T](Tizen.UI.Scene3D.Animatable3DPropertyValue_T_.md#Tizen.UI.Scene3D.Animatable3DPropertyValue_T_.T 'Tizen.UI.Scene3D.Animatable3DPropertyValue&lt;T>.T')

The view to which the property belongs.

#### Returns
[Tizen.UI.NativeHandle.AnimatablePropertyHandle](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.NativeHandle.AnimatablePropertyHandle 'Tizen.UI.NativeHandle.AnimatablePropertyHandle')  
The target property handle.





































