### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## CornerRadius Struct

Struct representing the radius of each corner of a rectangle.

```csharp
public struct CornerRadius
```
### Constructors

<a name='Tizen.UI.CornerRadius.CornerRadius(float)'></a>

## CornerRadius(float) Constructor

Initializes a new instance of the [CornerRadius](Tizen.UI.CornerRadius.md 'Tizen.UI.CornerRadius') struct with the specified uniform radius.

```csharp
public CornerRadius(float uniformRadius);
```
#### Parameters

<a name='Tizen.UI.CornerRadius.CornerRadius(float).uniformRadius'></a>

`uniformRadius` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The uniform radius of all four corners.

<a name='Tizen.UI.CornerRadius.CornerRadius(float,float,float,float)'></a>

## CornerRadius(float, float, float, float) Constructor

Initializes a new instance of the [CornerRadius](Tizen.UI.CornerRadius.md 'Tizen.UI.CornerRadius') struct with the specified radii for each corner.

```csharp
public CornerRadius(float topLeft, float topRight, float bottomLeft, float bottomRight);
```
#### Parameters

<a name='Tizen.UI.CornerRadius.CornerRadius(float,float,float,float).topLeft'></a>

`topLeft` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The radius of the top left corner.

<a name='Tizen.UI.CornerRadius.CornerRadius(float,float,float,float).topRight'></a>

`topRight` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The radius of the top right corner.

<a name='Tizen.UI.CornerRadius.CornerRadius(float,float,float,float).bottomLeft'></a>

`bottomLeft` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The radius of the bottom left corner.

<a name='Tizen.UI.CornerRadius.CornerRadius(float,float,float,float).bottomRight'></a>

`bottomRight` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The radius of the bottom right corner.
### Fields

<a name='Tizen.UI.CornerRadius.Zero'></a>

## CornerRadius.Zero Field

The CornerRadius at {0,0,0,0}.

```csharp
public static readonly CornerRadius Zero;
```

#### Field Value
[CornerRadius](Tizen.UI.CornerRadius.md 'Tizen.UI.CornerRadius')
### Properties

<a name='Tizen.UI.CornerRadius.BottomLeft'></a>

## CornerRadius.BottomLeft Property

The radius of the bottom left corner of the rectangle.

```csharp
public readonly float BottomLeft { get; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.CornerRadius.BottomRight'></a>

## CornerRadius.BottomRight Property

The radius of the bottom right corner of the rectangle.

```csharp
public readonly float BottomRight { get; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.CornerRadius.IsNaN'></a>

## CornerRadius.IsNaN Property

Gets a value indicating whether any value has a width of NaN.

```csharp
public bool IsNaN { get; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.CornerRadius.IsRelative'></a>

## CornerRadius.IsRelative Property

Gets whether a value is relative.

```csharp
public readonly bool IsRelative { get; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.CornerRadius.IsZero'></a>

## CornerRadius.IsZero Property

Whether both TopLeft, TopRight, BottomLeft and BottomRight are 0.

```csharp
public bool IsZero { get; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
true if both TopLeft, TopRight, BottomLeft and BottomRight are 0.0.

<a name='Tizen.UI.CornerRadius.TopLeft'></a>

## CornerRadius.TopLeft Property

The radius of the top left corner of the rectangle.

```csharp
public readonly float TopLeft { get; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.CornerRadius.TopRight'></a>

## CornerRadius.TopRight Property

The radius of the top right corner of the rectangle.

```csharp
public readonly float TopRight { get; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')
### Methods

<a name='Tizen.UI.CornerRadius.Deconstruct(float,float,float,float)'></a>

## CornerRadius.Deconstruct(float, float, float, float) Method

Deconstructs the CornerRadius struct into its individual values.

```csharp
public void Deconstruct(out float topLeft, out float topRight, out float bottomLeft, out float bottomRight);
```
#### Parameters

<a name='Tizen.UI.CornerRadius.Deconstruct(float,float,float,float).topLeft'></a>

`topLeft` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The top left corner radius.

<a name='Tizen.UI.CornerRadius.Deconstruct(float,float,float,float).topRight'></a>

`topRight` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The top right corner radius.

<a name='Tizen.UI.CornerRadius.Deconstruct(float,float,float,float).bottomLeft'></a>

`bottomLeft` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The bottom left corner radius.

<a name='Tizen.UI.CornerRadius.Deconstruct(float,float,float,float).bottomRight'></a>

`bottomRight` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The bottom right corner radius.

<a name='Tizen.UI.CornerRadius.Equals(object)'></a>

## CornerRadius.Equals(object) Method

Indicates whether this instance and a specified object are equal.

```csharp
public override bool Equals(object obj);
```
#### Parameters

<a name='Tizen.UI.CornerRadius.Equals(object).obj'></a>

`obj` [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object')

The object to compare with the current instance.

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
[true](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/bool 'https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/bool') if [obj](Tizen.UI.CornerRadius.md#Tizen.UI.CornerRadius.Equals(object).obj 'Tizen.UI.CornerRadius.Equals(object).obj') and this instance are the same type and represent the same value; otherwise, [false](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/bool 'https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/bool').

<a name='Tizen.UI.CornerRadius.GetHashCode()'></a>

## CornerRadius.GetHashCode() Method

Returns the hash code for this instance.

```csharp
public override int GetHashCode();
```

#### Returns
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')  
A 32-bit signed integer that is the hash code for this instance.

<a name='Tizen.UI.CornerRadius.ToString()'></a>

## CornerRadius.ToString() Method

Returns a string that represents the current object.

```csharp
public override string ToString();
```

#### Returns
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')  
A string that represents the current object.
### Operators

<a name='Tizen.UI.CornerRadius.op_ImplicitTizen.UI.CornerRadius(float)'></a>

## CornerRadius.implicit operator CornerRadius(float) Operator

Implicitly converts a [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single') value to a [CornerRadius](Tizen.UI.CornerRadius.md 'Tizen.UI.CornerRadius') instance with the specified uniform radius.

```csharp
public static Tizen.UI.CornerRadius implicit operator CornerRadius(float uniformRadius);
```
#### Parameters

<a name='Tizen.UI.CornerRadius.op_ImplicitTizen.UI.CornerRadius(float).uniformRadius'></a>

`uniformRadius` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The uniform radius of all four corners.

#### Returns
[CornerRadius](Tizen.UI.CornerRadius.md 'Tizen.UI.CornerRadius')






