### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## SizePropertyValue Class

Represents a property value that represents the size of a view.

```csharp
public class SizePropertyValue : Tizen.UI.AnimatablePropertyValue
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [AnimatablePropertyValue](Tizen.UI.AnimatablePropertyValue.md 'Tizen.UI.AnimatablePropertyValue') &#129106; SizePropertyValue
### Constructors

<a name='Tizen.UI.SizePropertyValue.SizePropertyValue(float,float)'></a>

## SizePropertyValue(float, float) Constructor

Initializes a new instance of the [SizePropertyValue](Tizen.UI.SizePropertyValue.md 'Tizen.UI.SizePropertyValue') class.

```csharp
public SizePropertyValue(float width, float height);
```
#### Parameters

<a name='Tizen.UI.SizePropertyValue.SizePropertyValue(float,float).width'></a>

`width` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The width of the size.

<a name='Tizen.UI.SizePropertyValue.SizePropertyValue(float,float).height'></a>

`height` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The height of the size.

<a name='Tizen.UI.SizePropertyValue.SizePropertyValue(Tizen.UI.Size)'></a>

## SizePropertyValue(Size) Constructor

Initializes a new instance of the [SizePropertyValue](Tizen.UI.SizePropertyValue.md 'Tizen.UI.SizePropertyValue') class.

```csharp
public SizePropertyValue(Tizen.UI.Size size);
```
#### Parameters

<a name='Tizen.UI.SizePropertyValue.SizePropertyValue(Tizen.UI.Size).size'></a>

`size` [Size](Tizen.UI.Size.md 'Tizen.UI.Size')

The size to use.
### Properties

<a name='Tizen.UI.SizePropertyValue.Size'></a>

## SizePropertyValue.Size Property

Gets the size represented by this property value.

```csharp
public Tizen.UI.Size Size { get; }
```

#### Property Value
[Size](Tizen.UI.Size.md 'Tizen.UI.Size')

<a name='Tizen.UI.SizePropertyValue.Value'></a>

## SizePropertyValue.Value Property

Gets the value of the property.

```csharp
public override Tizen.UI.NativeHandle.PropertyValueHandle Value { get; }
```

#### Property Value
[PropertyValueHandle](Tizen.UI.NativeHandle.PropertyValueHandle.md 'Tizen.UI.NativeHandle.PropertyValueHandle')
### Methods

<a name='Tizen.UI.SizePropertyValue.GetTargetProperty(Tizen.UI.View)'></a>

## SizePropertyValue.GetTargetProperty(View) Method

Gets the target property handle for the animation.

```csharp
public override Tizen.UI.NativeHandle.AnimatablePropertyHandle GetTargetProperty(Tizen.UI.View view);
```
#### Parameters

<a name='Tizen.UI.SizePropertyValue.GetTargetProperty(Tizen.UI.View).view'></a>

`view` [View](Tizen.UI.View.md 'Tizen.UI.View')

The view to which the property belongs.

#### Returns
[AnimatablePropertyHandle](Tizen.UI.NativeHandle.AnimatablePropertyHandle.md 'Tizen.UI.NativeHandle.AnimatablePropertyHandle')  
The target property handle.






