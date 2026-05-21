### [Tizen.UI.Layouts](Tizen.UI.Layouts.md 'Tizen.UI.Layouts')

## GridLength Struct

Used to define the size of Grid ColumnDefinition and RowDefinition.

```csharp
public readonly struct GridLength
```
### Constructors

<a name='Tizen.UI.Layouts.GridLength.GridLength(float)'></a>

## GridLength(float) Constructor

Initializes a new absolute GridLength.

```csharp
public GridLength(float value);
```
#### Parameters

<a name='Tizen.UI.Layouts.GridLength.GridLength(float).value'></a>

`value` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The value of the new grid length.

<a name='Tizen.UI.Layouts.GridLength.GridLength(float,Tizen.UI.Layouts.GridUnitType)'></a>

## GridLength(float, GridUnitType) Constructor

Initializes a new GridLength.

```csharp
public GridLength(float value, Tizen.UI.Layouts.GridUnitType type);
```
#### Parameters

<a name='Tizen.UI.Layouts.GridLength.GridLength(float,Tizen.UI.Layouts.GridUnitType).value'></a>

`value` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The size of the GridLength.

<a name='Tizen.UI.Layouts.GridLength.GridLength(float,Tizen.UI.Layouts.GridUnitType).type'></a>

`type` [GridUnitType](Tizen.UI.Layouts.GridUnitType.md 'Tizen.UI.Layouts.GridUnitType')

The GridUnitType (Auto, Star, Absolute) of the GridLength.

#### Exceptions

[System.ArgumentException](https://docs.microsoft.com/en-us/dotnet/api/System.ArgumentException 'System.ArgumentException')
### Fields

<a name='Tizen.UI.Layouts.GridLength.Auto'></a>

## GridLength.Auto Field

A ready to reuse GridLength of GridUnitType.Auto.

```csharp
public static readonly GridLength Auto;
```

#### Field Value
[GridLength](Tizen.UI.Layouts.GridLength.md 'Tizen.UI.Layouts.GridLength')

<a name='Tizen.UI.Layouts.GridLength.Star'></a>

## GridLength.Star Field

A ready to reuse GridLength of GridUnitType.Star with a Value of 1.

```csharp
public static readonly GridLength Star;
```

#### Field Value
[GridLength](Tizen.UI.Layouts.GridLength.md 'Tizen.UI.Layouts.GridLength')
### Properties

<a name='Tizen.UI.Layouts.GridLength.IsAbsolute'></a>

## GridLength.IsAbsolute Property

Gets whether or not the GridUnitType of the GridLength is GridUnitType.Absolute.

```csharp
public bool IsAbsolute { get; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Layouts.GridLength.IsAuto'></a>

## GridLength.IsAuto Property

Gets whether or not the GridUnitType of the GridLength is GridUnitType.Auto.

```csharp
public bool IsAuto { get; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Layouts.GridLength.IsStar'></a>

## GridLength.IsStar Property

Gets a value that indicates whether the GridUnitType of the GridLength is GridUnitType.Star.

```csharp
public bool IsStar { get; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Layouts.GridLength.Value'></a>

## GridLength.Value Property

Gets the Value of the GridLength.

```csharp
public float Value { get; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')
### Methods

<a name='Tizen.UI.Layouts.GridLength.Equals(object)'></a>

## GridLength.Equals(object) Method

Indicates whether this instance and a specified object are equal.

```csharp
public override bool Equals(object? obj);
```
#### Parameters

<a name='Tizen.UI.Layouts.GridLength.Equals(object).obj'></a>

`obj` [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object')

The object to compare with the current instance.

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
[true](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/bool 'https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/bool') if [obj](Tizen.UI.Layouts.GridLength.md#Tizen.UI.Layouts.GridLength.Equals(object).obj 'Tizen.UI.Layouts.GridLength.Equals(object).obj') and this instance are the same type and represent the same value; otherwise, [false](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/bool 'https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/bool').

<a name='Tizen.UI.Layouts.GridLength.GetHashCode()'></a>

## GridLength.GetHashCode() Method

Returns the hash code for this instance.

```csharp
public override int GetHashCode();
```

#### Returns
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')  
A 32-bit signed integer that is the hash code for this instance.

<a name='Tizen.UI.Layouts.GridLength.ToString()'></a>

## GridLength.ToString() Method

Returns the fully qualified type name of this instance.

```csharp
public override string ToString();
```

#### Returns
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')  
The fully qualified type name.






























































