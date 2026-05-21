### [Tizen.UI.Layouts](Tizen.UI.Layouts.md 'Tizen.UI.Layouts')

## Grid Class

A layout that arranges views in rows and columns.

```csharp
public class Grid : Tizen.UI.Layouts.Layout,
Tizen.UI.Layouts.IGridLayout,
Tizen.UI.Layouts.ILayout
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; Tizen.UI.NObject &#129106; Tizen.UI.View &#129106; Tizen.UI.ViewGroup &#129106; [Layout](Tizen.UI.Layouts.Layout.md 'Tizen.UI.Layouts.Layout') &#129106; Grid

Implements [IGridLayout](Tizen.UI.Layouts.IGridLayout.md 'Tizen.UI.Layouts.IGridLayout'), [ILayout](Tizen.UI.Layouts.ILayout.md 'Tizen.UI.Layouts.ILayout')
### Properties

<a name='Tizen.UI.Layouts.Grid.ColumnDefinitions'></a>

## Grid.ColumnDefinitions Property

Provides the interface for the bound property that gets or sets the collection of ColumnDefinitions objects that control the heights of each column.

```csharp
public System.Collections.Generic.IList&lt;Tizen.UI.Layouts.GridColumnDefinition> ColumnDefinitions { get; set; }
```

Implements [ColumnDefinitions](Tizen.UI.Layouts.IGridLayout.md#Tizen.UI.Layouts.IGridLayout.ColumnDefinitions 'Tizen.UI.Layouts.IGridLayout.ColumnDefinitions')

#### Property Value
[System.Collections.Generic.IList&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1 'System.Collections.Generic.IList`1')[GridColumnDefinition](Tizen.UI.Layouts.GridColumnDefinition.md 'Tizen.UI.Layouts.GridColumnDefinition')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1 'System.Collections.Generic.IList`1')

<a name='Tizen.UI.Layouts.Grid.ColumnSpacing'></a>

## Grid.ColumnSpacing Property

Gets or sets the amount of space between columns in the Grid.

```csharp
public float ColumnSpacing { get; set; }
```

Implements [ColumnSpacing](Tizen.UI.Layouts.IGridLayout.md#Tizen.UI.Layouts.IGridLayout.ColumnSpacing 'Tizen.UI.Layouts.IGridLayout.ColumnSpacing')

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Layouts.Grid.RowDefinitions'></a>

## Grid.RowDefinitions Property

Provides the interface for the bound property that gets or sets the collection of RowDefinition objects that control the heights of each row.

```csharp
public System.Collections.Generic.IList&lt;Tizen.UI.Layouts.GridRowDefinition> RowDefinitions { get; set; }
```

Implements [RowDefinitions](Tizen.UI.Layouts.IGridLayout.md#Tizen.UI.Layouts.IGridLayout.RowDefinitions 'Tizen.UI.Layouts.IGridLayout.RowDefinitions')

#### Property Value
[System.Collections.Generic.IList&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1 'System.Collections.Generic.IList`1')[GridRowDefinition](Tizen.UI.Layouts.GridRowDefinition.md 'Tizen.UI.Layouts.GridRowDefinition')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1 'System.Collections.Generic.IList`1')

<a name='Tizen.UI.Layouts.Grid.RowSpacing'></a>

## Grid.RowSpacing Property

Gets or sets the amount of space between rows in the Grid.

```csharp
public float RowSpacing { get; set; }
```

Implements [RowSpacing](Tizen.UI.Layouts.IGridLayout.md#Tizen.UI.Layouts.IGridLayout.RowSpacing 'Tizen.UI.Layouts.IGridLayout.RowSpacing')

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')
### Methods

<a name='Tizen.UI.Layouts.Grid.Add(Tizen.UI.View,int,int)'></a>

## Grid.Add(View, int, int) Method

Adds a view to the grid at the specified row and column with a row span of 1 and a column span of 1.

```csharp
public void Add(Tizen.UI.View view, int row, int col);
```
#### Parameters

<a name='Tizen.UI.Layouts.Grid.Add(Tizen.UI.View,int,int).view'></a>

`view` Tizen.UI.View

The view to add.

<a name='Tizen.UI.Layouts.Grid.Add(Tizen.UI.View,int,int).row'></a>

`row` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The row index where the view should be added.

<a name='Tizen.UI.Layouts.Grid.Add(Tizen.UI.View,int,int).col'></a>

`col` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The column index where the view should be added.

<a name='Tizen.UI.Layouts.Grid.Add(Tizen.UI.View,int,int,int,int)'></a>

## Grid.Add(View, int, int, int, int) Method

Adds a view to the grid at the specified row and column position, with the specified row and column span.

```csharp
public void Add(Tizen.UI.View view, int row, int rowSpan, int col, int colSpan);
```
#### Parameters

<a name='Tizen.UI.Layouts.Grid.Add(Tizen.UI.View,int,int,int,int).view'></a>

`view` Tizen.UI.View

The view to add to the grid.

<a name='Tizen.UI.Layouts.Grid.Add(Tizen.UI.View,int,int,int,int).row'></a>

`row` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The row index where the view should be added.

<a name='Tizen.UI.Layouts.Grid.Add(Tizen.UI.View,int,int,int,int).rowSpan'></a>

`rowSpan` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The number of rows the view should span.

<a name='Tizen.UI.Layouts.Grid.Add(Tizen.UI.View,int,int,int,int).col'></a>

`col` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The column index where the view should be added.

<a name='Tizen.UI.Layouts.Grid.Add(Tizen.UI.View,int,int,int,int).colSpan'></a>

`colSpan` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The number of columns the view should span.































































