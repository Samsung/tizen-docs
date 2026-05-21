### [Tizen.UI.Layouts](Tizen.UI.Layouts.md 'Tizen.UI.Layouts')

## GridRowColumns Class

Provides a series of extension methods that support configuring a [Grid](Tizen.UI.Layouts.Grid.md 'Tizen.UI.Layouts.Grid').

```csharp
public static class GridRowColumns
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; GridRowColumns
### Properties

<a name='Tizen.UI.Layouts.GridRowColumns.Auto'></a>

## GridRowColumns.Auto Property

Represents an automatic grid row or column size.

```csharp
public static Tizen.UI.Layouts.GridLength Auto { get; }
```

#### Property Value
[GridLength](Tizen.UI.Layouts.GridLength.md 'Tizen.UI.Layouts.GridLength')

<a name='Tizen.UI.Layouts.GridRowColumns.Star'></a>

## GridRowColumns.Star Property

Represents a star-sized grid row or column size.

```csharp
public static Tizen.UI.Layouts.GridLength Star { get; }
```

#### Property Value
[GridLength](Tizen.UI.Layouts.GridLength.md 'Tizen.UI.Layouts.GridLength')
### Methods

<a name='Tizen.UI.Layouts.GridRowColumns.All_TEnum_()'></a>

## GridRowColumns.All&lt;TEnum>() Method

Returns the number of rows or columns that can be addressed using the specified enum type.

```csharp
public static int All&lt;TEnum>()
    where TEnum : System.Enum;
```
#### Type parameters

<a name='Tizen.UI.Layouts.GridRowColumns.All_TEnum_().TEnum'></a>

`TEnum`

The type of the enum.

#### Returns
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')  
The number of rows or columns that can be addressed using the specified enum type.

<a name='Tizen.UI.Layouts.GridRowColumns.Last_TEnum_()'></a>

## GridRowColumns.Last&lt;TEnum>() Method

Returns the last row or column index that can be addressed using the specified enum type.

```csharp
public static int Last&lt;TEnum>()
    where TEnum : System.Enum;
```
#### Type parameters

<a name='Tizen.UI.Layouts.GridRowColumns.Last_TEnum_().TEnum'></a>

`TEnum`

The type of the enum.

#### Returns
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')  
The last row or column index that can be addressed using the specified enum type.

<a name='Tizen.UI.Layouts.GridRowColumns.Stars(float)'></a>

## GridRowColumns.Stars(float) Method

Creates a star-sized grid row or column size with the specified weight.

```csharp
public static Tizen.UI.Layouts.GridLength Stars(float value);
```
#### Parameters

<a name='Tizen.UI.Layouts.GridRowColumns.Stars(float).value'></a>

`value` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The weight of the star-sized grid row or column.

#### Returns
[GridLength](Tizen.UI.Layouts.GridLength.md 'Tizen.UI.Layouts.GridLength')  
A star-sized grid row or column size with the specified weight.






























































