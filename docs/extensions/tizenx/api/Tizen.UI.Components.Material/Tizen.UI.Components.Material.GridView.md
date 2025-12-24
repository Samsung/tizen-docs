### [Tizen.UI.Components.Material](Tizen.UI.Components.Material.md 'Tizen.UI.Components.Material')

## GridView Class

A scroll view that displays recycling items in a grid layout.  
It supports horizontal and vertical scrolling. The items can be bound to a data source using an item template.  
The grid view can be customized with various properties such as span count, prefetch base size, and scroll bar visibility.  
The grid view uses a recycler view internally to efficiently manage the display of items.  
The grid view can be used to create a variety of layouts such as a photo gallery or a product catalog.

```csharp
public class GridView : Tizen.UI.Components.Material.LoopedAdapterView
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [Tizen.UI.NObject](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.NObject 'Tizen.UI.NObject') &#129106; [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View') &#129106; [Tizen.UI.ContentView](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.ContentView 'Tizen.UI.ContentView') &#129106; [AdapterView](Tizen.UI.Components.Material.AdapterView.md 'Tizen.UI.Components.Material.AdapterView') &#129106; [LoopedAdapterView](Tizen.UI.Components.Material.LoopedAdapterView.md 'Tizen.UI.Components.Material.LoopedAdapterView') &#129106; GridView
### Constructors

<a name='Tizen.UI.Components.Material.GridView.GridView()'></a>

## GridView() Constructor

Creates a new instance of a GridView.

```csharp
public GridView();
```
### Properties

<a name='Tizen.UI.Components.Material.GridView.GroupBodyTemplate'></a>

## GridView.GroupBodyTemplate Property

The group body template for the list view. This template defines the appearance of the group bodies. Default is null.

```csharp
public Tizen.UI.ViewTemplate GroupBodyTemplate { get; set; }
```

#### Property Value
[Tizen.UI.ViewTemplate](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.ViewTemplate 'Tizen.UI.ViewTemplate')

<a name='Tizen.UI.Components.Material.GridView.GroupHeaderTemplate'></a>

## GridView.GroupHeaderTemplate Property

The group header template for the grid view. This template defines the appearance of the group headers. Default is null.

```csharp
public Tizen.UI.ViewTemplate GroupHeaderTemplate { get; set; }
```

#### Property Value
[Tizen.UI.ViewTemplate](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.ViewTemplate 'Tizen.UI.ViewTemplate')

<a name='Tizen.UI.Components.Material.GridView.HorizontalEdgeEffect'></a>

## GridView.HorizontalEdgeEffect Property

[Tizen.UI.Components.IEdgeEffect](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.IEdgeEffect 'Tizen.UI.Components.IEdgeEffect') of horizontal scroll direction.  
            edge effect will be come when scroll over the edge of horizontal direction.

```csharp
public Tizen.UI.Components.IEdgeEffect HorizontalEdgeEffect { get; set; }
```

#### Property Value
[Tizen.UI.Components.IEdgeEffect](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.IEdgeEffect 'Tizen.UI.Components.IEdgeEffect')

<a name='Tizen.UI.Components.Material.GridView.IsGrouped'></a>

## GridView.IsGrouped Property

Boolean property indicating whether the grid view is grouped. Default is false.

```csharp
public bool IsGrouped { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.Material.GridView.IsHorizontal'></a>

## GridView.IsHorizontal Property

Boolean property indicating whether the grid view is arranged horizontally or vertically. Default is false.

```csharp
public bool IsHorizontal { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.Material.GridView.ItemAnimator'></a>

## GridView.ItemAnimator Property

Gets or sets the ItemAnimator for the GridView.

```csharp
public Tizen.UI.Components.Recycler.IItemAnimator ItemAnimator { get; set; }
```

#### Property Value
[Tizen.UI.Components.Recycler.IItemAnimator](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.Recycler.IItemAnimator 'Tizen.UI.Components.Recycler.IItemAnimator')

<a name='Tizen.UI.Components.Material.GridView.OverScrollMode'></a>

## GridView.OverScrollMode Property

Set over scroll mode as type of [OverScrollMode](Tizen.UI.Components.Material.GridView.md#Tizen.UI.Components.Material.GridView.OverScrollMode 'Tizen.UI.Components.Material.GridView.OverScrollMode').  
Default mode is [Tizen.UI.Components.OverScrollMode.ContentScrolls](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.OverScrollMode.ContentScrolls 'Tizen.UI.Components.OverScrollMode.ContentScrolls').

```csharp
public Tizen.UI.Components.OverScrollMode OverScrollMode { get; set; }
```

#### Property Value
[Tizen.UI.Components.OverScrollMode](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.OverScrollMode 'Tizen.UI.Components.OverScrollMode')

<a name='Tizen.UI.Components.Material.GridView.SpanCount'></a>

## GridView.SpanCount Property

The span count for the grid view. The span count determines how many columns or rows are displayed in the grid. Default is 1.

```csharp
public uint SpanCount { get; set; }
```

#### Property Value
[System.UInt32](https://docs.microsoft.com/en-us/dotnet/api/System.UInt32 'System.UInt32')

<a name='Tizen.UI.Components.Material.GridView.VerticalEdgeEffect'></a>

## GridView.VerticalEdgeEffect Property

[Tizen.UI.Components.IEdgeEffect](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.IEdgeEffect 'Tizen.UI.Components.IEdgeEffect') of vertical scroll direction.  
            edge effect will be come when scroll over the edge of vertical direction.

```csharp
public Tizen.UI.Components.IEdgeEffect VerticalEdgeEffect { get; set; }
```

#### Property Value
[Tizen.UI.Components.IEdgeEffect](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.IEdgeEffect 'Tizen.UI.Components.IEdgeEffect')
### Methods

<a name='Tizen.UI.Components.Material.GridView.ScrollTo(int,Tizen.UI.ScrollToPosition,bool)'></a>

## GridView.ScrollTo(int, ScrollToPosition, bool) Method

Scrolls the RecyclerView to show the index position item in specified position with animation.

```csharp
public System.Threading.Tasks.Task ScrollTo(int position, Tizen.UI.ScrollToPosition scrollToPosition=Tizen.UI.ScrollToPosition.MakeVisible, bool animation=true);
```
#### Parameters

<a name='Tizen.UI.Components.Material.GridView.ScrollTo(int,Tizen.UI.ScrollToPosition,bool).position'></a>

`position` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The position of the item to be shown.

<a name='Tizen.UI.Components.Material.GridView.ScrollTo(int,Tizen.UI.ScrollToPosition,bool).scrollToPosition'></a>

`scrollToPosition` [Tizen.UI.ScrollToPosition](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.ScrollToPosition 'Tizen.UI.ScrollToPosition')

The position to scroll to. It can be Start, Center, or End.

<a name='Tizen.UI.Components.Material.GridView.ScrollTo(int,Tizen.UI.ScrollToPosition,bool).animation'></a>

`animation` [System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

Indicates whether the scrolling should be animated or not.

#### Returns
[System.Threading.Tasks.Task](https://docs.microsoft.com/en-us/dotnet/api/System.Threading.Tasks.Task 'System.Threading.Tasks.Task')  
A task representing the asynchronous operation.













































