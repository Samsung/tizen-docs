### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## Size Struct

Struct defining height and width as a pair of floats.

```csharp
public struct Size :
System.IEquatable&lt;Tizen.UI.Size>
```

Implements [System.IEquatable&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.IEquatable-1 'System.IEquatable`1')[Size](Tizen.UI.Size.md 'Tizen.UI.Size')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.IEquatable-1 'System.IEquatable`1')
### Constructors

<a name='Tizen.UI.Size.Size(float,float)'></a>

## Size(float, float) Constructor

Creates a new Size object with width and height.

```csharp
public Size(float width, float height);
```
#### Parameters

<a name='Tizen.UI.Size.Size(float,float).width'></a>

`width` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The width of the new size.

<a name='Tizen.UI.Size.Size(float,float).height'></a>

`height` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The height of the new size.
### Fields

<a name='Tizen.UI.Size.Zero'></a>

## Size.Zero Field

The Size whose values for height and width are 0.0.

```csharp
public static readonly Size Zero;
```

#### Field Value
[Size](Tizen.UI.Size.md 'Tizen.UI.Size')
### Properties

<a name='Tizen.UI.Size.Height'></a>

## Size.Height Property

Magnitude along the vertical axis, in platform-specific units.

```csharp
public float Height { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Size.IsZero'></a>

## Size.IsZero Property

Whether the Size has Height and Width of 0.0.

```csharp
public bool IsZero { get; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Size.Width'></a>

## Size.Width Property

Magnitude along the horizontal axis, in platform-defined units.

```csharp
public float Width { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')
### Methods

<a name='Tizen.UI.Size.Deconstruct(float,float)'></a>

## Size.Deconstruct(float, float) Method

Deconstructs the Size object into its individual components (width and height).

```csharp
public void Deconstruct(out float width, out float height);
```
#### Parameters

<a name='Tizen.UI.Size.Deconstruct(float,float).width'></a>

`width` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The width component of the Size object.

<a name='Tizen.UI.Size.Deconstruct(float,float).height'></a>

`height` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The height component of the Size object.

<a name='Tizen.UI.Size.Equals(object)'></a>

## Size.Equals(object) Method

Whether thisSize is equivalent to obj.

```csharp
public override bool Equals(object obj);
```
#### Parameters

<a name='Tizen.UI.Size.Equals(object).obj'></a>

`obj` [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object')

The object to which this is being compared.

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
true if obj is a Size whose values are identical to thisSize's Height and Width.

<a name='Tizen.UI.Size.Equals(Tizen.UI.Size)'></a>

## Size.Equals(Size) Method

Whether thisSize is equivalent to other.

```csharp
public bool Equals(Tizen.UI.Size other);
```
#### Parameters

<a name='Tizen.UI.Size.Equals(Tizen.UI.Size).other'></a>

`other` [Size](Tizen.UI.Size.md 'Tizen.UI.Size')

The Size to which this is being compared.

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
true if other's values are identical to thisSize's Height and Width.

<a name='Tizen.UI.Size.GetHashCode()'></a>

## Size.GetHashCode() Method

Returns a hash value for the Size.

```csharp
public override int GetHashCode();
```

#### Returns
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')  
A value intended for efficient insertion and lookup in hashtable-based data structures.

<a name='Tizen.UI.Size.ToString()'></a>

## Size.ToString() Method

Returns a human-readable representation of the Size.

```csharp
public override string ToString();
```

#### Returns
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')  
The format has the pattern "\{Width=\{0} Height=\{1}}".
### Operators

<a name='Tizen.UI.Size.op_Addition(Tizen.UI.Size,Tizen.UI.Size)'></a>

## Size.operator +(Size, Size) Operator

Returns a new Size whose Height and Width are the sum of the component's height and width.

```csharp
public static Tizen.UI.Size operator +(Tizen.UI.Size s1, Tizen.UI.Size s2);
```
#### Parameters

<a name='Tizen.UI.Size.op_Addition(Tizen.UI.Size,Tizen.UI.Size).s1'></a>

`s1` [Size](Tizen.UI.Size.md 'Tizen.UI.Size')

A Size to be added.

<a name='Tizen.UI.Size.op_Addition(Tizen.UI.Size,Tizen.UI.Size).s2'></a>

`s2` [Size](Tizen.UI.Size.md 'Tizen.UI.Size')

A Size to be added.

#### Returns
[Size](Tizen.UI.Size.md 'Tizen.UI.Size')  
A Size whose Width is equal to s1.Width + s2.Width and whose Height is equal to sz1.Height + sz2.Height.

<a name='Tizen.UI.Size.op_Equality(Tizen.UI.Size,Tizen.UI.Size)'></a>

## Size.operator ==(Size, Size) Operator

Whether two Sizes have equal values.

```csharp
public static bool operator ==(Tizen.UI.Size s1, Tizen.UI.Size s2);
```
#### Parameters

<a name='Tizen.UI.Size.op_Equality(Tizen.UI.Size,Tizen.UI.Size).s1'></a>

`s1` [Size](Tizen.UI.Size.md 'Tizen.UI.Size')

A Size to be compared.

<a name='Tizen.UI.Size.op_Equality(Tizen.UI.Size,Tizen.UI.Size).s2'></a>

`s2` [Size](Tizen.UI.Size.md 'Tizen.UI.Size')

A Size to be compared.

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
true if s1 and s2 have equal values for Height and Width.

<a name='Tizen.UI.Size.op_ExplicitTizen.UI.Point(Tizen.UI.Size)'></a>

## Size.explicit operator Point(Size) Operator

Returns a new Point based on a Size.

```csharp
public static Tizen.UI.Point explicit operator Point(Tizen.UI.Size size);
```
#### Parameters

<a name='Tizen.UI.Size.op_ExplicitTizen.UI.Point(Tizen.UI.Size).size'></a>

`size` [Size](Tizen.UI.Size.md 'Tizen.UI.Size')

The Size to be converted to a Point.

#### Returns
[Point](Tizen.UI.Point.md 'Tizen.UI.Point')  
A Point whose X and Y are equal to size's Width and Height, respectively.

<a name='Tizen.UI.Size.op_Inequality(Tizen.UI.Size,Tizen.UI.Size)'></a>

## Size.operator !=(Size, Size) Operator

Whether two Sizes have unequal values.

```csharp
public static bool operator !=(Tizen.UI.Size s1, Tizen.UI.Size s2);
```
#### Parameters

<a name='Tizen.UI.Size.op_Inequality(Tizen.UI.Size,Tizen.UI.Size).s1'></a>

`s1` [Size](Tizen.UI.Size.md 'Tizen.UI.Size')

The first Size to compare.

<a name='Tizen.UI.Size.op_Inequality(Tizen.UI.Size,Tizen.UI.Size).s2'></a>

`s2` [Size](Tizen.UI.Size.md 'Tizen.UI.Size')

The second Size to compare.

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
true if s1 and s2 have unequal values for either Height or Width.

<a name='Tizen.UI.Size.op_Multiply(Tizen.UI.Size,float)'></a>

## Size.operator *(Size, float) Operator

Scales both Width and Height.

```csharp
public static Tizen.UI.Size operator *(Tizen.UI.Size s1, float value);
```
#### Parameters

<a name='Tizen.UI.Size.op_Multiply(Tizen.UI.Size,float).s1'></a>

`s1` [Size](Tizen.UI.Size.md 'Tizen.UI.Size')

A Size to be scaled.

<a name='Tizen.UI.Size.op_Multiply(Tizen.UI.Size,float).value'></a>

`value` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

A factor by which to multiple s1's Width and Height values.

#### Returns
[Size](Tizen.UI.Size.md 'Tizen.UI.Size')  
A new Size whose Width and Height have been scaled by value.

<a name='Tizen.UI.Size.op_Subtraction(Tizen.UI.Size,Tizen.UI.Size)'></a>

## Size.operator -(Size, Size) Operator

Returns a new Size whose Height and Width are s1's height and width minus the values in s2.

```csharp
public static Tizen.UI.Size operator -(Tizen.UI.Size s1, Tizen.UI.Size s2);
```
#### Parameters

<a name='Tizen.UI.Size.op_Subtraction(Tizen.UI.Size,Tizen.UI.Size).s1'></a>

`s1` [Size](Tizen.UI.Size.md 'Tizen.UI.Size')

A Size from whose values a size will be subtracted.

<a name='Tizen.UI.Size.op_Subtraction(Tizen.UI.Size,Tizen.UI.Size).s2'></a>

`s2` [Size](Tizen.UI.Size.md 'Tizen.UI.Size')

The Size to subtract from s1.

#### Returns
[Size](Tizen.UI.Size.md 'Tizen.UI.Size')  
A Size whose Width is equal to s1.Width - s2.Width and whose Height is equal to sz1.Height - sz2.Height.






