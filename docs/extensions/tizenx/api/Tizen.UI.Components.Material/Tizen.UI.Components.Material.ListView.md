### [Tizen.UI.Components.Material](Tizen.UI.Components.Material.md 'Tizen.UI.Components.Material')

## ListView Class

A scroll view that displays recycling items in a linear layout.  
It supports horizontal and vertical scrolling. The items can be bound to a data source using an item template.  
The list view can be customized with various properties such as prefetch base size, and scroll bar visibility.  
The list view uses a recycler view internally to efficiently manage the display of items.

```csharp
public class ListView : Tizen.UI.Components.Material.LoopedAdapterView
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; Tizen.UI.NObject &#129106; Tizen.UI.View &#129106; Tizen.UI.ContentView &#129106; [AdapterView](Tizen.UI.Components.Material.AdapterView.md 'Tizen.UI.Components.Material.AdapterView') &#129106; [LoopedAdapterView](Tizen.UI.Components.Material.LoopedAdapterView.md 'Tizen.UI.Components.Material.LoopedAdapterView') &#129106; ListView
### Constructors

<a name='Tizen.UI.Components.Material.ListView.ListView()'></a>

## ListView() Constructor

Creates a new instance of a list view.

```csharp
public ListView();
```
### Properties

<a name='Tizen.UI.Components.Material.ListView.DividerTemplate'></a>

## ListView.DividerTemplate Property

The divider template for the list view. This template defines the appearance of the dividers between items. Default is null.

```csharp
public Tizen.UI.ViewTemplate DividerTemplate { get; set; }
```

#### Property Value
Tizen.UI.ViewTemplate

<a name='Tizen.UI.Components.Material.ListView.GroupBodyTemplate'></a>

## ListView.GroupBodyTemplate Property

The group body template for the list view. This template defines the appearance of the group bodies. Default is null.

```csharp
public Tizen.UI.ViewTemplate GroupBodyTemplate { get; set; }
```

#### Property Value
Tizen.UI.ViewTemplate

<a name='Tizen.UI.Components.Material.ListView.GroupFooterTemplate'></a>

## ListView.GroupFooterTemplate Property

The group footer template for the list view. This template defines the appearance of the group footers. Default is null.

```csharp
public Tizen.UI.ViewTemplate GroupFooterTemplate { get; set; }
```

#### Property Value
Tizen.UI.ViewTemplate

<a name='Tizen.UI.Components.Material.ListView.GroupHeaderTemplate'></a>

## ListView.GroupHeaderTemplate Property

The group header template for the list view. This template defines the appearance of the group headers. Default is null.

```csharp
public Tizen.UI.ViewTemplate GroupHeaderTemplate { get; set; }
```

#### Property Value
Tizen.UI.ViewTemplate

<a name='Tizen.UI.Components.Material.ListView.HasDivider'></a>

## ListView.HasDivider Property

Boolean property indicating whether the list view has dividers between items. Default is false.

```csharp
public bool HasDivider { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.Material.ListView.HorizontalEdgeEffect'></a>

## ListView.HorizontalEdgeEffect Property

Tizen.UI.Components.IEdgeEffect of horizontal scroll direction.  
            edge effect will be come when scroll over the edge of horizontal direction.

```csharp
public Tizen.UI.Components.IEdgeEffect HorizontalEdgeEffect { get; set; }
```

#### Property Value
Tizen.UI.Components.IEdgeEffect

<a name='Tizen.UI.Components.Material.ListView.IsGrouped'></a>

## ListView.IsGrouped Property

Boolean property indicating whether the list view is grouped. Default is false.

```csharp
public bool IsGrouped { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.Material.ListView.IsHorizontal'></a>

## ListView.IsHorizontal Property

Boolean property indicating whether the list view is arranged horizontally or vertically. Default is false.

```csharp
public bool IsHorizontal { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.Material.ListView.IsStickyHeader'></a>

## ListView.IsStickyHeader Property

Boolean property indicating whether the list view has sticky headers.  
Default is false. When true, the first item in each group will stick to the top of the list view when scrolling.

```csharp
public bool IsStickyHeader { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.Material.ListView.ItemAnimator'></a>

## ListView.ItemAnimator Property

Gets or sets the ItemAnimator for the items animation.

```csharp
public Tizen.UI.Components.Recycler.IItemAnimator ItemAnimator { get; set; }
```

#### Property Value
Tizen.UI.Components.Recycler.IItemAnimator

<a name='Tizen.UI.Components.Material.ListView.ItemTouchHelper'></a>

## ListView.ItemTouchHelper Property

The touch helper for item touch actions. see[ItemTouchHelper](Tizen.UI.Components.Material.ListView.md#Tizen.UI.Components.Material.ListView.ItemTouchHelper 'Tizen.UI.Components.Material.ListView.ItemTouchHelper').

```csharp
public Tizen.UI.Components.Recycler.ItemTouchHelper ItemTouchHelper { get; set; }
```

#### Property Value
Tizen.UI.Components.Recycler.ItemTouchHelper

<a name='Tizen.UI.Components.Material.ListView.OverScrollMode'></a>

## ListView.OverScrollMode Property

Set over scroll mode as type of [OverScrollMode](Tizen.UI.Components.Material.ListView.md#Tizen.UI.Components.Material.ListView.OverScrollMode 'Tizen.UI.Components.Material.ListView.OverScrollMode').  
Default mode is Tizen.UI.Components.OverScrollMode.ContentScrolls.

```csharp
public Tizen.UI.Components.OverScrollMode OverScrollMode { get; set; }
```

#### Property Value
Tizen.UI.Components.OverScrollMode

<a name='Tizen.UI.Components.Material.ListView.VerticalEdgeEffect'></a>

## ListView.VerticalEdgeEffect Property

Tizen.UI.Components.IEdgeEffect of vertical scroll direction.  
            edge effect will be come when scroll over the edge of vertical direction.

```csharp
public Tizen.UI.Components.IEdgeEffect VerticalEdgeEffect { get; set; }
```

#### Property Value
Tizen.UI.Components.IEdgeEffect
### Methods

<a name='Tizen.UI.Components.Material.ListView.ScrollTo(int,Tizen.UI.ScrollToPosition,bool)'></a>

## ListView.ScrollTo(int, ScrollToPosition, bool) Method

Scrolls the RecyclerView to show the index position item in specified position with animation.

```csharp
public System.Threading.Tasks.Task ScrollTo(int position, Tizen.UI.ScrollToPosition scrollToPosition=Tizen.UI.ScrollToPosition.MakeVisible, bool animation=true);
```
#### Parameters

<a name='Tizen.UI.Components.Material.ListView.ScrollTo(int,Tizen.UI.ScrollToPosition,bool).position'></a>

`position` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The position of the item to be shown.

<a name='Tizen.UI.Components.Material.ListView.ScrollTo(int,Tizen.UI.ScrollToPosition,bool).scrollToPosition'></a>

`scrollToPosition` Tizen.UI.ScrollToPosition

The position to scroll to. It can be Start, Center, or End.

<a name='Tizen.UI.Components.Material.ListView.ScrollTo(int,Tizen.UI.ScrollToPosition,bool).animation'></a>

`animation` [System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

Indicates whether the scrolling should be animated or not.

#### Returns
[System.Threading.Tasks.Task](https://docs.microsoft.com/en-us/dotnet/api/System.Threading.Tasks.Task 'System.Threading.Tasks.Task')  
A task representing the asynchronous operation.














































