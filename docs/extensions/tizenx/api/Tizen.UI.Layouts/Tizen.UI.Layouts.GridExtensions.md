### [Tizen.UI.Layouts](Tizen.UI.Layouts.md 'Tizen.UI.Layouts')

## GridExtensions Class

Provides a series of extension methods that support configuring a [Grid](Tizen.UI.Layouts.Grid.md 'Tizen.UI.Layouts.Grid').

```csharp
public static class GridExtensions
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; GridExtensions
### Methods

<a name='Tizen.UI.Layouts.GridExtensions.Column_TView,TColumn_(thisTView,TColumn)'></a>

## GridExtensions.Column&lt;TView,TColumn>(this TView, TColumn) Method

Sets the column index of the specified view using an enum value.<br/>  
This only works if the [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View') is included in the  [Grid](Tizen.UI.Layouts.Grid.md 'Tizen.UI.Layouts.Grid') and used.

```csharp
public static TView Column&lt;TView,TColumn>(this TView view, TColumn column)
    where TView : Tizen.UI.View
    where TColumn : System.Enum;
```
#### Type parameters

<a name='Tizen.UI.Layouts.GridExtensions.Column_TView,TColumn_(thisTView,TColumn).TView'></a>

`TView`

The type of the view.

<a name='Tizen.UI.Layouts.GridExtensions.Column_TView,TColumn_(thisTView,TColumn).TColumn'></a>

`TColumn`

The type of the column enum.
#### Parameters

<a name='Tizen.UI.Layouts.GridExtensions.Column_TView,TColumn_(thisTView,TColumn).view'></a>

`view` [TView](Tizen.UI.Layouts.GridExtensions.md#Tizen.UI.Layouts.GridExtensions.Column_TView,TColumn_(thisTView,TColumn).TView 'Tizen.UI.Layouts.GridExtensions.Column&lt;TView,TColumn>(this TView, TColumn).TView')

The view to set the column index for.

<a name='Tizen.UI.Layouts.GridExtensions.Column_TView,TColumn_(thisTView,TColumn).column'></a>

`column` [TColumn](Tizen.UI.Layouts.GridExtensions.md#Tizen.UI.Layouts.GridExtensions.Column_TView,TColumn_(thisTView,TColumn).TColumn 'Tizen.UI.Layouts.GridExtensions.Column&lt;TView,TColumn>(this TView, TColumn).TColumn')

The column enum value to set.

#### Returns
[TView](Tizen.UI.Layouts.GridExtensions.md#Tizen.UI.Layouts.GridExtensions.Column_TView,TColumn_(thisTView,TColumn).TView 'Tizen.UI.Layouts.GridExtensions.Column&lt;TView,TColumn>(this TView, TColumn).TView')  
The view with the specified column index.

<a name='Tizen.UI.Layouts.GridExtensions.Column_TView,TColumn_(thisTView,TColumn,TColumn)'></a>

## GridExtensions.Column&lt;TView,TColumn>(this TView, TColumn, TColumn) Method

Sets the column index and column span of the specified view using enum values.<br/>  
This only works if the [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View') is included in the  [Grid](Tizen.UI.Layouts.Grid.md 'Tizen.UI.Layouts.Grid') and used.

```csharp
public static TView Column&lt;TView,TColumn>(this TView view, TColumn column, TColumn last)
    where TView : Tizen.UI.View
    where TColumn : System.Enum;
```
#### Type parameters

<a name='Tizen.UI.Layouts.GridExtensions.Column_TView,TColumn_(thisTView,TColumn,TColumn).TView'></a>

`TView`

The type of the view.

<a name='Tizen.UI.Layouts.GridExtensions.Column_TView,TColumn_(thisTView,TColumn,TColumn).TColumn'></a>

`TColumn`

The type of the column enum.
#### Parameters

<a name='Tizen.UI.Layouts.GridExtensions.Column_TView,TColumn_(thisTView,TColumn,TColumn).view'></a>

`view` [TView](Tizen.UI.Layouts.GridExtensions.md#Tizen.UI.Layouts.GridExtensions.Column_TView,TColumn_(thisTView,TColumn,TColumn).TView 'Tizen.UI.Layouts.GridExtensions.Column&lt;TView,TColumn>(this TView, TColumn, TColumn).TView')

The view to set the column index and column span for.

<a name='Tizen.UI.Layouts.GridExtensions.Column_TView,TColumn_(thisTView,TColumn,TColumn).column'></a>

`column` [TColumn](Tizen.UI.Layouts.GridExtensions.md#Tizen.UI.Layouts.GridExtensions.Column_TView,TColumn_(thisTView,TColumn,TColumn).TColumn 'Tizen.UI.Layouts.GridExtensions.Column&lt;TView,TColumn>(this TView, TColumn, TColumn).TColumn')

The column enum value to set.

<a name='Tizen.UI.Layouts.GridExtensions.Column_TView,TColumn_(thisTView,TColumn,TColumn).last'></a>

`last` [TColumn](Tizen.UI.Layouts.GridExtensions.md#Tizen.UI.Layouts.GridExtensions.Column_TView,TColumn_(thisTView,TColumn,TColumn).TColumn 'Tizen.UI.Layouts.GridExtensions.Column&lt;TView,TColumn>(this TView, TColumn, TColumn).TColumn')

The last column enum value.

#### Returns
[TView](Tizen.UI.Layouts.GridExtensions.md#Tizen.UI.Layouts.GridExtensions.Column_TView,TColumn_(thisTView,TColumn,TColumn).TView 'Tizen.UI.Layouts.GridExtensions.Column&lt;TView,TColumn>(this TView, TColumn, TColumn).TView')  
The view with the specified column index and column span.

<a name='Tizen.UI.Layouts.GridExtensions.Column_TView_(thisTView,int)'></a>

## GridExtensions.Column&lt;TView>(this TView, int) Method

Sets the column index of the specified view.<br/>  
This only works if the [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View') is included in the  [Grid](Tizen.UI.Layouts.Grid.md 'Tizen.UI.Layouts.Grid') and used.

```csharp
public static TView Column&lt;TView>(this TView view, int column)
    where TView : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.Layouts.GridExtensions.Column_TView_(thisTView,int).TView'></a>

`TView`

The type of the view.
#### Parameters

<a name='Tizen.UI.Layouts.GridExtensions.Column_TView_(thisTView,int).view'></a>

`view` [TView](Tizen.UI.Layouts.GridExtensions.md#Tizen.UI.Layouts.GridExtensions.Column_TView_(thisTView,int).TView 'Tizen.UI.Layouts.GridExtensions.Column&lt;TView>(this TView, int).TView')

The view to set the column index for.

<a name='Tizen.UI.Layouts.GridExtensions.Column_TView_(thisTView,int).column'></a>

`column` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The column index to set.

#### Returns
[TView](Tizen.UI.Layouts.GridExtensions.md#Tizen.UI.Layouts.GridExtensions.Column_TView_(thisTView,int).TView 'Tizen.UI.Layouts.GridExtensions.Column&lt;TView>(this TView, int).TView')  
The view with the specified column index.

<a name='Tizen.UI.Layouts.GridExtensions.Column_TView_(thisTView,int,int)'></a>

## GridExtensions.Column&lt;TView>(this TView, int, int) Method

Sets the column index and column span of the specified view.<br/>  
This only works if the [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View') is included in the  [Grid](Tizen.UI.Layouts.Grid.md 'Tizen.UI.Layouts.Grid') and used.

```csharp
public static TView Column&lt;TView>(this TView view, int column, int span)
    where TView : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.Layouts.GridExtensions.Column_TView_(thisTView,int,int).TView'></a>

`TView`

The type of the view.
#### Parameters

<a name='Tizen.UI.Layouts.GridExtensions.Column_TView_(thisTView,int,int).view'></a>

`view` [TView](Tizen.UI.Layouts.GridExtensions.md#Tizen.UI.Layouts.GridExtensions.Column_TView_(thisTView,int,int).TView 'Tizen.UI.Layouts.GridExtensions.Column&lt;TView>(this TView, int, int).TView')

The view to set the column index and column span for.

<a name='Tizen.UI.Layouts.GridExtensions.Column_TView_(thisTView,int,int).column'></a>

`column` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The column index to set.

<a name='Tizen.UI.Layouts.GridExtensions.Column_TView_(thisTView,int,int).span'></a>

`span` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The column span to set.

#### Returns
[TView](Tizen.UI.Layouts.GridExtensions.md#Tizen.UI.Layouts.GridExtensions.Column_TView_(thisTView,int,int).TView 'Tizen.UI.Layouts.GridExtensions.Column&lt;TView>(this TView, int, int).TView')  
The view with the specified column index and column span.

<a name='Tizen.UI.Layouts.GridExtensions.ColumnSpan_TView_(thisTView,int)'></a>

## GridExtensions.ColumnSpan&lt;TView>(this TView, int) Method

Sets the column span of the specified view.<br/>  
This only works if the [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View') is included in the  [Grid](Tizen.UI.Layouts.Grid.md 'Tizen.UI.Layouts.Grid') and used.

```csharp
public static TView ColumnSpan&lt;TView>(this TView view, int span)
    where TView : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.Layouts.GridExtensions.ColumnSpan_TView_(thisTView,int).TView'></a>

`TView`

The type of the view.
#### Parameters

<a name='Tizen.UI.Layouts.GridExtensions.ColumnSpan_TView_(thisTView,int).view'></a>

`view` [TView](Tizen.UI.Layouts.GridExtensions.md#Tizen.UI.Layouts.GridExtensions.ColumnSpan_TView_(thisTView,int).TView 'Tizen.UI.Layouts.GridExtensions.ColumnSpan&lt;TView>(this TView, int).TView')

The view to set the column span for.

<a name='Tizen.UI.Layouts.GridExtensions.ColumnSpan_TView_(thisTView,int).span'></a>

`span` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The column span to set.

#### Returns
[TView](Tizen.UI.Layouts.GridExtensions.md#Tizen.UI.Layouts.GridExtensions.ColumnSpan_TView_(thisTView,int).TView 'Tizen.UI.Layouts.GridExtensions.ColumnSpan&lt;TView>(this TView, int).TView')  
The view with the specified column span.

<a name='Tizen.UI.Layouts.GridExtensions.Row_TView,TRow_(thisTView,TRow)'></a>

## GridExtensions.Row&lt;TView,TRow>(this TView, TRow) Method

Sets the row index of the specified view using an enum value.<br/>  
This only works if the [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View') is included in the  [Grid](Tizen.UI.Layouts.Grid.md 'Tizen.UI.Layouts.Grid') and used.

```csharp
public static TView Row&lt;TView,TRow>(this TView view, TRow row)
    where TView : Tizen.UI.View
    where TRow : System.Enum;
```
#### Type parameters

<a name='Tizen.UI.Layouts.GridExtensions.Row_TView,TRow_(thisTView,TRow).TView'></a>

`TView`

The type of the view.

<a name='Tizen.UI.Layouts.GridExtensions.Row_TView,TRow_(thisTView,TRow).TRow'></a>

`TRow`

The type of the row enum.
#### Parameters

<a name='Tizen.UI.Layouts.GridExtensions.Row_TView,TRow_(thisTView,TRow).view'></a>

`view` [TView](Tizen.UI.Layouts.GridExtensions.md#Tizen.UI.Layouts.GridExtensions.Row_TView,TRow_(thisTView,TRow).TView 'Tizen.UI.Layouts.GridExtensions.Row&lt;TView,TRow>(this TView, TRow).TView')

The view to set the row index for.

<a name='Tizen.UI.Layouts.GridExtensions.Row_TView,TRow_(thisTView,TRow).row'></a>

`row` [TRow](Tizen.UI.Layouts.GridExtensions.md#Tizen.UI.Layouts.GridExtensions.Row_TView,TRow_(thisTView,TRow).TRow 'Tizen.UI.Layouts.GridExtensions.Row&lt;TView,TRow>(this TView, TRow).TRow')

The row enum value to set.

#### Returns
[TView](Tizen.UI.Layouts.GridExtensions.md#Tizen.UI.Layouts.GridExtensions.Row_TView,TRow_(thisTView,TRow).TView 'Tizen.UI.Layouts.GridExtensions.Row&lt;TView,TRow>(this TView, TRow).TView')  
The view with the specified row index.

<a name='Tizen.UI.Layouts.GridExtensions.Row_TView,TRow_(thisTView,TRow,TRow)'></a>

## GridExtensions.Row&lt;TView,TRow>(this TView, TRow, TRow) Method

Sets the row index and row span of the specified view using enum values.<br/>  
This only works if the [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View') is included in the  [Grid](Tizen.UI.Layouts.Grid.md 'Tizen.UI.Layouts.Grid') and used.

```csharp
public static TView Row&lt;TView,TRow>(this TView view, TRow row, TRow last)
    where TView : Tizen.UI.View
    where TRow : System.Enum;
```
#### Type parameters

<a name='Tizen.UI.Layouts.GridExtensions.Row_TView,TRow_(thisTView,TRow,TRow).TView'></a>

`TView`

The type of the view.

<a name='Tizen.UI.Layouts.GridExtensions.Row_TView,TRow_(thisTView,TRow,TRow).TRow'></a>

`TRow`

The type of the row enum.
#### Parameters

<a name='Tizen.UI.Layouts.GridExtensions.Row_TView,TRow_(thisTView,TRow,TRow).view'></a>

`view` [TView](Tizen.UI.Layouts.GridExtensions.md#Tizen.UI.Layouts.GridExtensions.Row_TView,TRow_(thisTView,TRow,TRow).TView 'Tizen.UI.Layouts.GridExtensions.Row&lt;TView,TRow>(this TView, TRow, TRow).TView')

The view to set the row index and row span for.

<a name='Tizen.UI.Layouts.GridExtensions.Row_TView,TRow_(thisTView,TRow,TRow).row'></a>

`row` [TRow](Tizen.UI.Layouts.GridExtensions.md#Tizen.UI.Layouts.GridExtensions.Row_TView,TRow_(thisTView,TRow,TRow).TRow 'Tizen.UI.Layouts.GridExtensions.Row&lt;TView,TRow>(this TView, TRow, TRow).TRow')

The row enum value to set.

<a name='Tizen.UI.Layouts.GridExtensions.Row_TView,TRow_(thisTView,TRow,TRow).last'></a>

`last` [TRow](Tizen.UI.Layouts.GridExtensions.md#Tizen.UI.Layouts.GridExtensions.Row_TView,TRow_(thisTView,TRow,TRow).TRow 'Tizen.UI.Layouts.GridExtensions.Row&lt;TView,TRow>(this TView, TRow, TRow).TRow')

The last row enum value.

#### Returns
[TView](Tizen.UI.Layouts.GridExtensions.md#Tizen.UI.Layouts.GridExtensions.Row_TView,TRow_(thisTView,TRow,TRow).TView 'Tizen.UI.Layouts.GridExtensions.Row&lt;TView,TRow>(this TView, TRow, TRow).TView')  
The view with the specified row index and row span.

<a name='Tizen.UI.Layouts.GridExtensions.Row_TView_(thisTView,int)'></a>

## GridExtensions.Row&lt;TView>(this TView, int) Method

Sets the row index of the specified view.<br/>  
This only works if the [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View') is included in the  [Grid](Tizen.UI.Layouts.Grid.md 'Tizen.UI.Layouts.Grid') and used.

```csharp
public static TView Row&lt;TView>(this TView view, int row)
    where TView : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.Layouts.GridExtensions.Row_TView_(thisTView,int).TView'></a>

`TView`

The type of the view.
#### Parameters

<a name='Tizen.UI.Layouts.GridExtensions.Row_TView_(thisTView,int).view'></a>

`view` [TView](Tizen.UI.Layouts.GridExtensions.md#Tizen.UI.Layouts.GridExtensions.Row_TView_(thisTView,int).TView 'Tizen.UI.Layouts.GridExtensions.Row&lt;TView>(this TView, int).TView')

The view to set the row index for.

<a name='Tizen.UI.Layouts.GridExtensions.Row_TView_(thisTView,int).row'></a>

`row` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The row index to set.

#### Returns
[TView](Tizen.UI.Layouts.GridExtensions.md#Tizen.UI.Layouts.GridExtensions.Row_TView_(thisTView,int).TView 'Tizen.UI.Layouts.GridExtensions.Row&lt;TView>(this TView, int).TView')  
The view with the specified row index.

<a name='Tizen.UI.Layouts.GridExtensions.Row_TView_(thisTView,int,int)'></a>

## GridExtensions.Row&lt;TView>(this TView, int, int) Method

Sets the row index and row span of the specified view.<br/>  
This only works if the [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View') is included in the  [Grid](Tizen.UI.Layouts.Grid.md 'Tizen.UI.Layouts.Grid') and used.

```csharp
public static TView Row&lt;TView>(this TView view, int row, int span)
    where TView : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.Layouts.GridExtensions.Row_TView_(thisTView,int,int).TView'></a>

`TView`

The type of the view.
#### Parameters

<a name='Tizen.UI.Layouts.GridExtensions.Row_TView_(thisTView,int,int).view'></a>

`view` [TView](Tizen.UI.Layouts.GridExtensions.md#Tizen.UI.Layouts.GridExtensions.Row_TView_(thisTView,int,int).TView 'Tizen.UI.Layouts.GridExtensions.Row&lt;TView>(this TView, int, int).TView')

The view to set the row index and row span for.

<a name='Tizen.UI.Layouts.GridExtensions.Row_TView_(thisTView,int,int).row'></a>

`row` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The row index to set.

<a name='Tizen.UI.Layouts.GridExtensions.Row_TView_(thisTView,int,int).span'></a>

`span` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The row span to set.

#### Returns
[TView](Tizen.UI.Layouts.GridExtensions.md#Tizen.UI.Layouts.GridExtensions.Row_TView_(thisTView,int,int).TView 'Tizen.UI.Layouts.GridExtensions.Row&lt;TView>(this TView, int, int).TView')  
The view with the specified row index and row span.

<a name='Tizen.UI.Layouts.GridExtensions.RowSpan_TView_(thisTView,int)'></a>

## GridExtensions.RowSpan&lt;TView>(this TView, int) Method

Sets the row span of the specified view.<br/>  
This only works if the [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View') is included in the  [Grid](Tizen.UI.Layouts.Grid.md 'Tizen.UI.Layouts.Grid') and used.

```csharp
public static TView RowSpan&lt;TView>(this TView view, int span)
    where TView : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.Layouts.GridExtensions.RowSpan_TView_(thisTView,int).TView'></a>

`TView`

The type of the view.
#### Parameters

<a name='Tizen.UI.Layouts.GridExtensions.RowSpan_TView_(thisTView,int).view'></a>

`view` [TView](Tizen.UI.Layouts.GridExtensions.md#Tizen.UI.Layouts.GridExtensions.RowSpan_TView_(thisTView,int).TView 'Tizen.UI.Layouts.GridExtensions.RowSpan&lt;TView>(this TView, int).TView')

The view to set the row span for.

<a name='Tizen.UI.Layouts.GridExtensions.RowSpan_TView_(thisTView,int).span'></a>

`span` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The row span to set.

#### Returns
[TView](Tizen.UI.Layouts.GridExtensions.md#Tizen.UI.Layouts.GridExtensions.RowSpan_TView_(thisTView,int).TView 'Tizen.UI.Layouts.GridExtensions.RowSpan&lt;TView>(this TView, int).TView')  
The view with the specified row span.






























































