### [Tizen.UI.Layouts](Tizen.UI.Layouts.md 'Tizen.UI.Layouts')

## FlexBasis Struct

Specifies the initial size of the flex item.

```csharp
public struct FlexBasis :
System.IEquatable&lt;Tizen.UI.Layouts.FlexBasis>
```

Implements [System.IEquatable&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.IEquatable-1 'System.IEquatable`1')[FlexBasis](Tizen.UI.Layouts.FlexBasis.md 'Tizen.UI.Layouts.FlexBasis')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.IEquatable-1 'System.IEquatable`1')
### Constructors

<a name='Tizen.UI.Layouts.FlexBasis.FlexBasis(float,bool)'></a>

## FlexBasis(float, bool) Constructor

Initializes a new instance of the FlexBasis class with the specified length.

```csharp
public FlexBasis(float length, bool isRelative=false);
```
#### Parameters

<a name='Tizen.UI.Layouts.FlexBasis.FlexBasis(float,bool).length'></a>

`length` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Layouts.FlexBasis.FlexBasis(float,bool).isRelative'></a>

`isRelative` [System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')
### Fields

<a name='Tizen.UI.Layouts.FlexBasis.Auto'></a>

## FlexBasis.Auto Field

Automatic sizing.

```csharp
public static readonly FlexBasis Auto;
```

#### Field Value
[FlexBasis](Tizen.UI.Layouts.FlexBasis.md 'Tizen.UI.Layouts.FlexBasis')
### Properties

<a name='Tizen.UI.Layouts.FlexBasis.Length'></a>

## FlexBasis.Length Property

Gets the length of the FlexBasis.

```csharp
public readonly float Length { get; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')
### Methods

<a name='Tizen.UI.Layouts.FlexBasis.Equals(object)'></a>

## FlexBasis.Equals(object) Method

Indicates whether this instance and a specified object are equal.

```csharp
public override bool Equals(object? obj);
```
#### Parameters

<a name='Tizen.UI.Layouts.FlexBasis.Equals(object).obj'></a>

`obj` [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object')

The object to compare with the current instance.

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
[true](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/bool 'https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/bool') if [obj](Tizen.UI.Layouts.FlexBasis.md#Tizen.UI.Layouts.FlexBasis.Equals(object).obj 'Tizen.UI.Layouts.FlexBasis.Equals(object).obj') and this instance are the same type and represent the same value; otherwise, [false](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/bool 'https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/bool').

<a name='Tizen.UI.Layouts.FlexBasis.Equals(Tizen.UI.Layouts.FlexBasis)'></a>

## FlexBasis.Equals(FlexBasis) Method

Compares two FlexBasis objects for equality.

```csharp
public bool Equals(Tizen.UI.Layouts.FlexBasis other);
```
#### Parameters

<a name='Tizen.UI.Layouts.FlexBasis.Equals(Tizen.UI.Layouts.FlexBasis).other'></a>

`other` [FlexBasis](Tizen.UI.Layouts.FlexBasis.md 'Tizen.UI.Layouts.FlexBasis')

The FlexBasis object to compare with the current FlexBasis object.

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
True if the FlexBasis objects are equal; otherwise, false.

<a name='Tizen.UI.Layouts.FlexBasis.GetHashCode()'></a>

## FlexBasis.GetHashCode() Method

Returns the hash code for this instance.

```csharp
public override int GetHashCode();
```

#### Returns
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')  
A 32-bit signed integer that is the hash code for this instance.
### Operators

<a name='Tizen.UI.Layouts.FlexBasis.op_ImplicitTizen.UI.Layouts.FlexBasis(float)'></a>

## FlexBasis.implicit operator FlexBasis(float) Operator

Defines an implicit conversion of a float value to a [FlexBasis](Tizen.UI.Layouts.FlexBasis.md 'Tizen.UI.Layouts.FlexBasis') instance.

```csharp
public static Tizen.UI.Layouts.FlexBasis implicit operator FlexBasis(float length);
```
#### Parameters

<a name='Tizen.UI.Layouts.FlexBasis.op_ImplicitTizen.UI.Layouts.FlexBasis(float).length'></a>

`length` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The length of the basis.

#### Returns
[FlexBasis](Tizen.UI.Layouts.FlexBasis.md 'Tizen.UI.Layouts.FlexBasis')






























































