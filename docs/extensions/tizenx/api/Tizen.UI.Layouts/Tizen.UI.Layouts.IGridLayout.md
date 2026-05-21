### [Tizen.UI.Layouts](Tizen.UI.Layouts.md 'Tizen.UI.Layouts')

## IGridLayout Interface

Defines the contract for a grid-based layout.

```csharp
public interface IGridLayout :
Tizen.UI.Layouts.ILayout
```

Derived  
&#8627; [Grid](Tizen.UI.Layouts.Grid.md 'Tizen.UI.Layouts.Grid')

Implements [ILayout](Tizen.UI.Layouts.ILayout.md 'Tizen.UI.Layouts.ILayout')
### Properties

<a name='Tizen.UI.Layouts.IGridLayout.ColumnDefinitions'></a>

## IGridLayout.ColumnDefinitions Property

Gets the collection of ColumnDefinitions objects that control the widths of each column.

```csharp
System.Collections.Generic.IList&lt;Tizen.UI.Layouts.GridColumnDefinition> ColumnDefinitions { get; }
```

#### Property Value
[System.Collections.Generic.IList&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1 'System.Collections.Generic.IList`1')[GridColumnDefinition](Tizen.UI.Layouts.GridColumnDefinition.md 'Tizen.UI.Layouts.GridColumnDefinition')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1 'System.Collections.Generic.IList`1')

<a name='Tizen.UI.Layouts.IGridLayout.ColumnSpacing'></a>

## IGridLayout.ColumnSpacing Property

Gets or sets the amount of space between columns in the Grid.

```csharp
float ColumnSpacing { get; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Layouts.IGridLayout.RowDefinitions'></a>

## IGridLayout.RowDefinitions Property

Gets the collection of RowDefinition objects that control the heights of each row.

```csharp
System.Collections.Generic.IList&lt;Tizen.UI.Layouts.GridRowDefinition> RowDefinitions { get; }
```

#### Property Value
[System.Collections.Generic.IList&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1 'System.Collections.Generic.IList`1')[GridRowDefinition](Tizen.UI.Layouts.GridRowDefinition.md 'Tizen.UI.Layouts.GridRowDefinition')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1 'System.Collections.Generic.IList`1')

<a name='Tizen.UI.Layouts.IGridLayout.RowSpacing'></a>

## IGridLayout.RowSpacing Property

Gets or sets the amount of space between rows in the Grid.

```csharp
float RowSpacing { get; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')






























































