### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## Thickness Struct

Defines the thickness of a border around a control.

```csharp
public struct Thickness
```
### Constructors

<a name='Tizen.UI.Thickness.Thickness(float)'></a>

## Thickness(float) Constructor

Initializes a new instance of the [Thickness](Tizen.UI.Thickness.md 'Tizen.UI.Thickness') struct with the specified uniform size.

```csharp
public Thickness(float uniformSize);
```
#### Parameters

<a name='Tizen.UI.Thickness.Thickness(float).uniformSize'></a>

`uniformSize` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The uniform size of the borders.

<a name='Tizen.UI.Thickness.Thickness(float,float)'></a>

## Thickness(float, float) Constructor

Initializes a new instance of the [Thickness](Tizen.UI.Thickness.md 'Tizen.UI.Thickness') struct with the specified horizontal and vertical sizes.

```csharp
public Thickness(float horizontalSize, float verticalSize);
```
#### Parameters

<a name='Tizen.UI.Thickness.Thickness(float,float).horizontalSize'></a>

`horizontalSize` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The horizontal size of the borders.

<a name='Tizen.UI.Thickness.Thickness(float,float).verticalSize'></a>

`verticalSize` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The vertical size of the borders.

<a name='Tizen.UI.Thickness.Thickness(float,float,float,float)'></a>

## Thickness(float, float, float, float) Constructor

Initializes a new instance of the [Thickness](Tizen.UI.Thickness.md 'Tizen.UI.Thickness') struct with the specified left, top, right, and bottom sizes.

```csharp
public Thickness(float left, float top, float right, float bottom);
```
#### Parameters

<a name='Tizen.UI.Thickness.Thickness(float,float,float,float).left'></a>

`left` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The width of the left border.

<a name='Tizen.UI.Thickness.Thickness(float,float,float,float).top'></a>

`top` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The width of the top border.

<a name='Tizen.UI.Thickness.Thickness(float,float,float,float).right'></a>

`right` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The width of the right border.

<a name='Tizen.UI.Thickness.Thickness(float,float,float,float).bottom'></a>

`bottom` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The width of the bottom border.
### Fields

<a name='Tizen.UI.Thickness.Zero'></a>

## Thickness.Zero Field

Represents a [Thickness](Tizen.UI.Thickness.md 'Tizen.UI.Thickness') with all values set to 0.

```csharp
public static Thickness Zero;
```

#### Field Value
[Thickness](Tizen.UI.Thickness.md 'Tizen.UI.Thickness')
### Properties

<a name='Tizen.UI.Thickness.Bottom'></a>

## Thickness.Bottom Property

Gets or sets the width of the bottom border.

```csharp
public float Bottom { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Thickness.HorizontalThickness'></a>

## Thickness.HorizontalThickness Property

Gets the total width of the horizontal borders.

```csharp
public float HorizontalThickness { get; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Thickness.IsEmpty'></a>

## Thickness.IsEmpty Property

Gets a value indicating whether all borders have a width of 0.

```csharp
public bool IsEmpty { get; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Thickness.IsNaN'></a>

## Thickness.IsNaN Property

Gets a value indicating whether any border has a width of NaN.

```csharp
public bool IsNaN { get; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Thickness.Left'></a>

## Thickness.Left Property

Gets or sets the width of the left border.

```csharp
public float Left { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Thickness.Right'></a>

## Thickness.Right Property

Gets or sets the width of the right border.

```csharp
public float Right { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Thickness.Top'></a>

## Thickness.Top Property

Gets or sets the width of the top border.

```csharp
public float Top { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Thickness.VerticalThickness'></a>

## Thickness.VerticalThickness Property

Gets the total height of the vertical borders.

```csharp
public float VerticalThickness { get; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')
### Methods

<a name='Tizen.UI.Thickness.Deconstruct(float,float,float,float)'></a>

## Thickness.Deconstruct(float, float, float, float) Method

Deconstructs the [Thickness](Tizen.UI.Thickness.md 'Tizen.UI.Thickness') into its individual components.

```csharp
public void Deconstruct(out float left, out float top, out float right, out float bottom);
```
#### Parameters

<a name='Tizen.UI.Thickness.Deconstruct(float,float,float,float).left'></a>

`left` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The width of the left border.

<a name='Tizen.UI.Thickness.Deconstruct(float,float,float,float).top'></a>

`top` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The width of the top border.

<a name='Tizen.UI.Thickness.Deconstruct(float,float,float,float).right'></a>

`right` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The width of the right border.

<a name='Tizen.UI.Thickness.Deconstruct(float,float,float,float).bottom'></a>

`bottom` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The width of the bottom border.

<a name='Tizen.UI.Thickness.Equals(object)'></a>

## Thickness.Equals(object) Method

Indicates whether this instance and a specified object are equal.

```csharp
public override bool Equals(object obj);
```
#### Parameters

<a name='Tizen.UI.Thickness.Equals(object).obj'></a>

`obj` [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object')

The object to compare with the current instance.

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
[true](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/bool 'https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/bool') if [obj](Tizen.UI.Thickness.md#Tizen.UI.Thickness.Equals(object).obj 'Tizen.UI.Thickness.Equals(object).obj') and this instance are the same type and represent the same value; otherwise, [false](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/bool 'https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/bool').

<a name='Tizen.UI.Thickness.GetHashCode()'></a>

## Thickness.GetHashCode() Method

Returns the hash code for this instance.

```csharp
public override int GetHashCode();
```

#### Returns
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')  
A 32-bit signed integer that is the hash code for this instance.
### Operators

<a name='Tizen.UI.Thickness.op_Addition(Tizen.UI.Thickness,float)'></a>

## Thickness.operator +(Thickness, float) Operator

Adds the specified [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single') to each component of the [Thickness](Tizen.UI.Thickness.md 'Tizen.UI.Thickness').

```csharp
public static Tizen.UI.Thickness operator +(Tizen.UI.Thickness left, float addend);
```
#### Parameters

<a name='Tizen.UI.Thickness.op_Addition(Tizen.UI.Thickness,float).left'></a>

`left` [Thickness](Tizen.UI.Thickness.md 'Tizen.UI.Thickness')

<a name='Tizen.UI.Thickness.op_Addition(Tizen.UI.Thickness,float).addend'></a>

`addend` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The value to add.

#### Returns
[Thickness](Tizen.UI.Thickness.md 'Tizen.UI.Thickness')  
A new [Thickness](Tizen.UI.Thickness.md 'Tizen.UI.Thickness') with the added values.

<a name='Tizen.UI.Thickness.op_Addition(Tizen.UI.Thickness,Tizen.UI.Thickness)'></a>

## Thickness.operator +(Thickness, Thickness) Operator

Adds the specified [Thickness](Tizen.UI.Thickness.md 'Tizen.UI.Thickness') to the current [Thickness](Tizen.UI.Thickness.md 'Tizen.UI.Thickness').

```csharp
public static Tizen.UI.Thickness operator +(Tizen.UI.Thickness left, Tizen.UI.Thickness right);
```
#### Parameters

<a name='Tizen.UI.Thickness.op_Addition(Tizen.UI.Thickness,Tizen.UI.Thickness).left'></a>

`left` [Thickness](Tizen.UI.Thickness.md 'Tizen.UI.Thickness')

<a name='Tizen.UI.Thickness.op_Addition(Tizen.UI.Thickness,Tizen.UI.Thickness).right'></a>

`right` [Thickness](Tizen.UI.Thickness.md 'Tizen.UI.Thickness')

The [Thickness](Tizen.UI.Thickness.md 'Tizen.UI.Thickness') to add.

#### Returns
[Thickness](Tizen.UI.Thickness.md 'Tizen.UI.Thickness')  
A new [Thickness](Tizen.UI.Thickness.md 'Tizen.UI.Thickness') with the added values.

<a name='Tizen.UI.Thickness.op_Equality(Tizen.UI.Thickness,Tizen.UI.Thickness)'></a>

## Thickness.operator ==(Thickness, Thickness) Operator

Compares two [Thickness](Tizen.UI.Thickness.md 'Tizen.UI.Thickness') objects for equality.

```csharp
public static bool operator ==(Tizen.UI.Thickness left, Tizen.UI.Thickness right);
```
#### Parameters

<a name='Tizen.UI.Thickness.op_Equality(Tizen.UI.Thickness,Tizen.UI.Thickness).left'></a>

`left` [Thickness](Tizen.UI.Thickness.md 'Tizen.UI.Thickness')

The first [Thickness](Tizen.UI.Thickness.md 'Tizen.UI.Thickness') object to compare.

<a name='Tizen.UI.Thickness.op_Equality(Tizen.UI.Thickness,Tizen.UI.Thickness).right'></a>

`right` [Thickness](Tizen.UI.Thickness.md 'Tizen.UI.Thickness')

The second [Thickness](Tizen.UI.Thickness.md 'Tizen.UI.Thickness') object to compare.

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
True if the objects are equal, otherwise false.

<a name='Tizen.UI.Thickness.op_ImplicitTizen.UI.Thickness(float)'></a>

## Thickness.implicit operator Thickness(float) Operator

Implicitly converts a float to a [Thickness](Tizen.UI.Thickness.md 'Tizen.UI.Thickness').

```csharp
public static Tizen.UI.Thickness implicit operator Thickness(float uniformSize);
```
#### Parameters

<a name='Tizen.UI.Thickness.op_ImplicitTizen.UI.Thickness(float).uniformSize'></a>

`uniformSize` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The uniform size to convert.

#### Returns
[Thickness](Tizen.UI.Thickness.md 'Tizen.UI.Thickness')

<a name='Tizen.UI.Thickness.op_ImplicitTizen.UI.Thickness(Tizen.UI.Size)'></a>

## Thickness.implicit operator Thickness(Size) Operator

Implicitly converts a [Size](Tizen.UI.Size.md 'Tizen.UI.Size') to a [Thickness](Tizen.UI.Thickness.md 'Tizen.UI.Thickness').

```csharp
public static Tizen.UI.Thickness implicit operator Thickness(Tizen.UI.Size size);
```
#### Parameters

<a name='Tizen.UI.Thickness.op_ImplicitTizen.UI.Thickness(Tizen.UI.Size).size'></a>

`size` [Size](Tizen.UI.Size.md 'Tizen.UI.Size')

The size to convert.

#### Returns
[Thickness](Tizen.UI.Thickness.md 'Tizen.UI.Thickness')

<a name='Tizen.UI.Thickness.op_Inequality(Tizen.UI.Thickness,Tizen.UI.Thickness)'></a>

## Thickness.operator !=(Thickness, Thickness) Operator

Compares two [Thickness](Tizen.UI.Thickness.md 'Tizen.UI.Thickness') objects for inequality.

```csharp
public static bool operator !=(Tizen.UI.Thickness left, Tizen.UI.Thickness right);
```
#### Parameters

<a name='Tizen.UI.Thickness.op_Inequality(Tizen.UI.Thickness,Tizen.UI.Thickness).left'></a>

`left` [Thickness](Tizen.UI.Thickness.md 'Tizen.UI.Thickness')

The first [Thickness](Tizen.UI.Thickness.md 'Tizen.UI.Thickness') object to compare.

<a name='Tizen.UI.Thickness.op_Inequality(Tizen.UI.Thickness,Tizen.UI.Thickness).right'></a>

`right` [Thickness](Tizen.UI.Thickness.md 'Tizen.UI.Thickness')

The second [Thickness](Tizen.UI.Thickness.md 'Tizen.UI.Thickness') object to compare.

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
True if the objects are not equal, otherwise false.

<a name='Tizen.UI.Thickness.op_Subtraction(Tizen.UI.Thickness,float)'></a>

## Thickness.operator -(Thickness, float) Operator

Subtracts the specified [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single') from each component of the [Thickness](Tizen.UI.Thickness.md 'Tizen.UI.Thickness').

```csharp
public static Tizen.UI.Thickness operator -(Tizen.UI.Thickness left, float addend);
```
#### Parameters

<a name='Tizen.UI.Thickness.op_Subtraction(Tizen.UI.Thickness,float).left'></a>

`left` [Thickness](Tizen.UI.Thickness.md 'Tizen.UI.Thickness')

<a name='Tizen.UI.Thickness.op_Subtraction(Tizen.UI.Thickness,float).addend'></a>

`addend` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

#### Returns
[Thickness](Tizen.UI.Thickness.md 'Tizen.UI.Thickness')  
A new [Thickness](Tizen.UI.Thickness.md 'Tizen.UI.Thickness') with the subtracted values.






