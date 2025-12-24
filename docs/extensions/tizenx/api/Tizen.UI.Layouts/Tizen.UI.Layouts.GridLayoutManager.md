### [Tizen.UI.Layouts](Tizen.UI.Layouts.md 'Tizen.UI.Layouts')

## GridLayoutManager Class

Provides a layout manager for a grid layout.

```csharp
public class GridLayoutManager : Tizen.UI.Layouts.LayoutManager
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [LayoutManager](Tizen.UI.Layouts.LayoutManager.md 'Tizen.UI.Layouts.LayoutManager') &#129106; GridLayoutManager
### Constructors

<a name='Tizen.UI.Layouts.GridLayoutManager.GridLayoutManager(Tizen.UI.Layouts.IGridLayout)'></a>

## GridLayoutManager(IGridLayout) Constructor

Initializes a new instance of the [GridLayoutManager](Tizen.UI.Layouts.GridLayoutManager.md 'Tizen.UI.Layouts.GridLayoutManager') class.

```csharp
public GridLayoutManager(Tizen.UI.Layouts.IGridLayout layout);
```
#### Parameters

<a name='Tizen.UI.Layouts.GridLayoutManager.GridLayoutManager(Tizen.UI.Layouts.IGridLayout).layout'></a>

`layout` [IGridLayout](Tizen.UI.Layouts.IGridLayout.md 'Tizen.UI.Layouts.IGridLayout')

The grid layout.
### Properties

<a name='Tizen.UI.Layouts.GridLayoutManager.Grid'></a>

## GridLayoutManager.Grid Property

Gets the grid layout.

```csharp
public Tizen.UI.Layouts.IGridLayout Grid { get; }
```

#### Property Value
[IGridLayout](Tizen.UI.Layouts.IGridLayout.md 'Tizen.UI.Layouts.IGridLayout')
### Methods

<a name='Tizen.UI.Layouts.GridLayoutManager.ArrangeChildren(Tizen.UI.Rect)'></a>

## GridLayoutManager.ArrangeChildren(Rect) Method

Arranges the children of the grid layout.

```csharp
public override Tizen.UI.Size ArrangeChildren(Tizen.UI.Rect bounds);
```
#### Parameters

<a name='Tizen.UI.Layouts.GridLayoutManager.ArrangeChildren(Tizen.UI.Rect).bounds'></a>

`bounds` [Tizen.UI.Rect](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Rect 'Tizen.UI.Rect')

The bounds of the grid layout.

Implements [ArrangeChildren(Rect)](Tizen.UI.Layouts.ILayoutManager.md#Tizen.UI.Layouts.ILayoutManager.ArrangeChildren(Tizen.UI.Rect) 'Tizen.UI.Layouts.ILayoutManager.ArrangeChildren(Tizen.UI.Rect)')

#### Returns
[Tizen.UI.Size](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Size 'Tizen.UI.Size')  
The actual size of the arranged grid layout.

<a name='Tizen.UI.Layouts.GridLayoutManager.Measure(float,float)'></a>

## GridLayoutManager.Measure(float, float) Method

Measures the size of the grid layout.

```csharp
public override Tizen.UI.Size Measure(float widthConstraint, float heightConstraint);
```
#### Parameters

<a name='Tizen.UI.Layouts.GridLayoutManager.Measure(float,float).widthConstraint'></a>

`widthConstraint` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The width constraint.

<a name='Tizen.UI.Layouts.GridLayoutManager.Measure(float,float).heightConstraint'></a>

`heightConstraint` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The height constraint.

Implements [Measure(float, float)](Tizen.UI.Layouts.ILayoutManager.md#Tizen.UI.Layouts.ILayoutManager.Measure(float,float) 'Tizen.UI.Layouts.ILayoutManager.Measure(float, float)')

#### Returns
[Tizen.UI.Size](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Size 'Tizen.UI.Size')  
The measured size of the grid layout.






























































