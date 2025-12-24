### [Tizen.UI.Components.Recycler](Tizen.UI.Components.Recycler.md 'Tizen.UI.Components.Recycler')

## RecyclerView Class

RecyclerView class.  
It provides a flexible view for displaying large data sets that can be scrolled very efficiently by maintaining a limited number of views.  
This class also supports smooth scrolling and animations. The RecyclerView works with a LayoutManager to position the items and Adapter to create them.  
RecyclerView also has built-in support for animations.

```csharp
public class RecyclerView : Tizen.UI.ViewGroup,
Tizen.UI.IDescendantFocusObserver,
Tizen.UI.IScrollable
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [Tizen.UI.NObject](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.NObject 'Tizen.UI.NObject') &#129106; [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View') &#129106; [Tizen.UI.ViewGroup](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.ViewGroup 'Tizen.UI.ViewGroup') &#129106; RecyclerView

Implements [Tizen.UI.IDescendantFocusObserver](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.IDescendantFocusObserver 'Tizen.UI.IDescendantFocusObserver'), [Tizen.UI.IScrollable](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.IScrollable 'Tizen.UI.IScrollable')
### Constructors

<a name='Tizen.UI.Components.Recycler.RecyclerView.RecyclerView()'></a>

## RecyclerView() Constructor

Constructor of RecyclerView.

```csharp
public RecyclerView();
```
### Properties

<a name='Tizen.UI.Components.Recycler.RecyclerView.Adapter'></a>

## RecyclerView.Adapter Property

The adapter of RecyclerView. It is used to provide the data and create the views for the RecyclerView.

```csharp
public Tizen.UI.Components.Recycler.Adapter Adapter { get; set; }
```

#### Property Value
[Adapter](Tizen.UI.Components.Recycler.Adapter.md 'Tizen.UI.Components.Recycler.Adapter')

<a name='Tizen.UI.Components.Recycler.RecyclerView.HasSticky'></a>

## RecyclerView.HasSticky Property

Indicates whether the RecyclerView has a sticky item or not. If it has, the sticky item will be displayed at the top or left of the RecyclerView.

```csharp
public bool HasSticky { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.Recycler.RecyclerView.HorizontalEdgeEffect'></a>

## RecyclerView.HorizontalEdgeEffect Property

[IEdgeEffect](Tizen.UI.Components.IEdgeEffect.md 'Tizen.UI.Components.IEdgeEffect') of horizontal scroll direction.  
            edge effect will be come when scroll over the edge of horizontal direction.

```csharp
public Tizen.UI.Components.IEdgeEffect HorizontalEdgeEffect { get; set; }
```

#### Property Value
[IEdgeEffect](Tizen.UI.Components.IEdgeEffect.md 'Tizen.UI.Components.IEdgeEffect')

<a name='Tizen.UI.Components.Recycler.RecyclerView.InnerScroller'></a>

## RecyclerView.InnerScroller Property

The inner scroller of RecyclerView. It is used to handle the scrolling behavior of the RecyclerView.

```csharp
public Tizen.UI.Components.Recycler.RecycleScroller InnerScroller { get; }
```

#### Property Value
[RecycleScroller](Tizen.UI.Components.Recycler.RecycleScroller.md 'Tizen.UI.Components.Recycler.RecycleScroller')

<a name='Tizen.UI.Components.Recycler.RecyclerView.InnerStickArea'></a>

## RecyclerView.InnerStickArea Property

The inner sticky area of RecyclerView. It is used to manage the sticky items in the RecyclerView.

```csharp
public Tizen.UI.Components.Recycler.StickyArea InnerStickArea { get; }
```

#### Property Value
[StickyArea](Tizen.UI.Components.Recycler.StickyArea.md 'Tizen.UI.Components.Recycler.StickyArea')

<a name='Tizen.UI.Components.Recycler.RecyclerView.IsScrolledToEnd'></a>

## RecyclerView.IsScrolledToEnd Property

Gets a value indicating whether the scrollable content has reached the end position.

```csharp
public bool IsScrolledToEnd { get; }
```

Implements [IsScrolledToEnd](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.IScrollable.IsScrolledToEnd 'Tizen.UI.IScrollable.IsScrolledToEnd')

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.Recycler.RecyclerView.IsScrolledToStart'></a>

## RecyclerView.IsScrolledToStart Property

Gets a value indicating whether the scrollable content has been scrolled to the start position.

```csharp
public bool IsScrolledToStart { get; }
```

Implements [IsScrolledToStart](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.IScrollable.IsScrolledToStart 'Tizen.UI.IScrollable.IsScrolledToStart')

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.Recycler.RecyclerView.IsScrolling'></a>

## RecyclerView.IsScrolling Property

Gets a value indicating whether the scroll is currently in progress.

```csharp
public bool IsScrolling { get; set; }
```

Implements [IsScrolling](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.IScrollable.IsScrolling 'Tizen.UI.IScrollable.IsScrolling')

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.Recycler.RecyclerView.ItemDecorations'></a>

## RecyclerView.ItemDecorations Property

The list of decoration helper for items.

```csharp
public System.Collections.Generic.IList&lt;Tizen.UI.Components.Recycler.IItemDecoration> ItemDecorations { get; }
```

#### Property Value
[System.Collections.Generic.IList&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1 'System.Collections.Generic.IList`1')[IItemDecoration](Tizen.UI.Components.Recycler.IItemDecoration.md 'Tizen.UI.Components.Recycler.IItemDecoration')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1 'System.Collections.Generic.IList`1')

<a name='Tizen.UI.Components.Recycler.RecyclerView.LastViewPort'></a>

## RecyclerView.LastViewPort Property

The last view port of RecyclerView. It represents the previous scroll area of the RecyclerView.

```csharp
public Tizen.UI.Rect LastViewPort { get; set; }
```

#### Property Value
[Tizen.UI.Rect](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Rect 'Tizen.UI.Rect')

<a name='Tizen.UI.Components.Recycler.RecyclerView.LayoutManager'></a>

## RecyclerView.LayoutManager Property

The layout manager of RecyclerView. It is used to define the layout strategy for the items in the RecyclerView.

```csharp
public Tizen.UI.Components.Recycler.LayoutManager LayoutManager { get; set; }
```

#### Property Value
[LayoutManager](Tizen.UI.Components.Recycler.LayoutManager.md 'Tizen.UI.Components.Recycler.LayoutManager')

<a name='Tizen.UI.Components.Recycler.RecyclerView.OverScrollMode'></a>

## RecyclerView.OverScrollMode Property

Set over scroll mode as type of [OverScrollMode](Tizen.UI.Components.Recycler.RecyclerView.md#Tizen.UI.Components.Recycler.RecyclerView.OverScrollMode 'Tizen.UI.Components.Recycler.RecyclerView.OverScrollMode').  
Default mode is [ContentScrolls](Tizen.UI.Components.OverScrollMode.md#Tizen.UI.Components.OverScrollMode.ContentScrolls 'Tizen.UI.Components.OverScrollMode.ContentScrolls').

```csharp
public Tizen.UI.Components.OverScrollMode OverScrollMode { get; set; }
```

#### Property Value
[OverScrollMode](Tizen.UI.Components.OverScrollMode.md 'Tizen.UI.Components.OverScrollMode')

<a name='Tizen.UI.Components.Recycler.RecyclerView.PrefetchBaseSize'></a>

## RecyclerView.PrefetchBaseSize Property

The prefetch base size of RecyclerView. It determines the size of the area that will be preloaded before and after the current view port.

```csharp
public float PrefetchBaseSize { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Components.Recycler.RecyclerView.RecycledPoolSize'></a>

## RecyclerView.RecycledPoolSize Property

Set maximum size of recylcing view holder pool.  
The pool size is applied for each view type.

```csharp
public int RecycledPoolSize { get; set; }
```

#### Property Value
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

<a name='Tizen.UI.Components.Recycler.RecyclerView.ScrollDirection'></a>

## RecyclerView.ScrollDirection Property

Gets or sets the direction of the scroll.

```csharp
public Tizen.UI.ScrollDirection ScrollDirection { get; }
```

#### Property Value
[Tizen.UI.ScrollDirection](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.ScrollDirection 'Tizen.UI.ScrollDirection')

<a name='Tizen.UI.Components.Recycler.RecyclerView.ScrollPosition'></a>

## RecyclerView.ScrollPosition Property

Gets the current scroll position.

```csharp
public Tizen.UI.Point ScrollPosition { get; }
```

#### Property Value
[Tizen.UI.Point](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Point 'Tizen.UI.Point')

<a name='Tizen.UI.Components.Recycler.RecyclerView.StickyCandidateVisible'></a>

## RecyclerView.StickyCandidateVisible Property

Indicates whether the sticky candidate item is visible or not. If it is visible, the sticky candidate item will be displayed in the RecyclerView.

```csharp
public bool StickyCandidateVisible { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.Recycler.RecyclerView.VerticalEdgeEffect'></a>

## RecyclerView.VerticalEdgeEffect Property

[IEdgeEffect](Tizen.UI.Components.IEdgeEffect.md 'Tizen.UI.Components.IEdgeEffect') of vertical scroll direction.  
            edge effect will be come when scroll over the edge of vertical direction.

```csharp
public Tizen.UI.Components.IEdgeEffect VerticalEdgeEffect { get; set; }
```

#### Property Value
[IEdgeEffect](Tizen.UI.Components.IEdgeEffect.md 'Tizen.UI.Components.IEdgeEffect')

<a name='Tizen.UI.Components.Recycler.RecyclerView.ViewPort'></a>

## RecyclerView.ViewPort Property

The view port of RecyclerView. It represents the scroll area of the RecyclerView.

```csharp
public Tizen.UI.Rect ViewPort { get; }
```

Implements [ViewPort](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.IScrollable.ViewPort 'Tizen.UI.IScrollable.ViewPort')

#### Property Value
[Tizen.UI.Rect](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Rect 'Tizen.UI.Rect')
### Methods

<a name='Tizen.UI.Components.Recycler.RecyclerView.ClearRecycledViewPool()'></a>

## RecyclerView.ClearRecycledViewPool() Method

Clear all recycled view holders from the recycled pool.

```csharp
public void ClearRecycledViewPool();
```

<a name='Tizen.UI.Components.Recycler.RecyclerView.FirstCompletelyVisibleItemPosition()'></a>

## RecyclerView.FirstCompletelyVisibleItemPosition() Method

Get the position of first completely visible items in the recyclerView.

```csharp
public int FirstCompletelyVisibleItemPosition();
```

#### Returns
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')  
The position of the first completely visible item.

<a name='Tizen.UI.Components.Recycler.RecyclerView.FirstRealizedPosition()'></a>

## RecyclerView.FirstRealizedPosition() Method

Get the position of first realized items in the recyclerView.

```csharp
public int FirstRealizedPosition();
```

#### Returns
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')  
The position of the first realized item.

<a name='Tizen.UI.Components.Recycler.RecyclerView.FirstVisibleItemPosition()'></a>

## RecyclerView.FirstVisibleItemPosition() Method

Get the position of first visible items in the recyclerView.

```csharp
public int FirstVisibleItemPosition();
```

#### Returns
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')  
The position of the first visible item.

<a name='Tizen.UI.Components.Recycler.RecyclerView.GetBodyForGroup(int)'></a>

## RecyclerView.GetBodyForGroup(int) Method

Get the body ViewHolder for the specified group. If the body is not realized, it creates a new one.

```csharp
public Tizen.UI.Components.Recycler.ViewHolder GetBodyForGroup(int group);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.RecyclerView.GetBodyForGroup(int).group'></a>

`group` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The position of the group within the adapter's data set

#### Returns
[ViewHolder](Tizen.UI.Components.Recycler.ViewHolder.md 'Tizen.UI.Components.Recycler.ViewHolder')  
A ViewHolder of body that displays the data at the specified position.

<a name='Tizen.UI.Components.Recycler.RecyclerView.GetItemViewType(int)'></a>

## RecyclerView.GetItemViewType(int) Method

Get the type of View for the specified item.

```csharp
public int GetItemViewType(int position);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.RecyclerView.GetItemViewType(int).position'></a>

`position` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The position of the item within the adapter's data set

#### Returns
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

<a name='Tizen.UI.Components.Recycler.RecyclerView.GetRealized(int)'></a>

## RecyclerView.GetRealized(int) Method

Get the realized view of the specified position. If the view is not realized, it returns null.

```csharp
public Tizen.UI.View GetRealized(int position);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.RecyclerView.GetRealized(int).position'></a>

`position` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The position of the item to get the view.

#### Returns
[Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')  
The realized view of the specified position.

<a name='Tizen.UI.Components.Recycler.RecyclerView.GetViewHolderForPosition(int)'></a>

## RecyclerView.GetViewHolderForPosition(int) Method

Get the ViewHolder for the specified position. If the view is not realized, it creates a new one.

```csharp
public Tizen.UI.Components.Recycler.ViewHolder GetViewHolderForPosition(int position);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.RecyclerView.GetViewHolderForPosition(int).position'></a>

`position` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The position of the item within the adapter's data set

#### Returns
[ViewHolder](Tizen.UI.Components.Recycler.ViewHolder.md 'Tizen.UI.Components.Recycler.ViewHolder')  
A ViewHolder that displays the data at the specified position.

<a name='Tizen.UI.Components.Recycler.RecyclerView.LastCompletelyVisibleItemPosition()'></a>

## RecyclerView.LastCompletelyVisibleItemPosition() Method

Get the position of last completely visible items in the recyclerView.

```csharp
public int LastCompletelyVisibleItemPosition();
```

#### Returns
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')  
The position of the last completely visible item.

<a name='Tizen.UI.Components.Recycler.RecyclerView.LastRealizedPosition()'></a>

## RecyclerView.LastRealizedPosition() Method

Get the position of last realized items in the recyclerView.

```csharp
public int LastRealizedPosition();
```

#### Returns
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')  
The position of the last realized item.

<a name='Tizen.UI.Components.Recycler.RecyclerView.LastVisibleItemPosition()'></a>

## RecyclerView.LastVisibleItemPosition() Method

Get the position of last visible items in the recyclerView.

```csharp
public int LastVisibleItemPosition();
```

#### Returns
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')  
The position of the last visible item.

<a name='Tizen.UI.Components.Recycler.RecyclerView.Measure(float,float)'></a>

## RecyclerView.Measure(float, float) Method

Measures the view based on the available width and height.

```csharp
public override Tizen.UI.Size Measure(float availableWidth, float availableHeight);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.RecyclerView.Measure(float,float).availableWidth'></a>

`availableWidth` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The available width for the view.

<a name='Tizen.UI.Components.Recycler.RecyclerView.Measure(float,float).availableHeight'></a>

`availableHeight` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The available height for the view.

#### Returns
[Tizen.UI.Size](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Size 'Tizen.UI.Size')  
The measured size of the view.

<a name='Tizen.UI.Components.Recycler.RecyclerView.RecycleViewHolder(Tizen.UI.Components.Recycler.ViewHolder)'></a>

## RecyclerView.RecycleViewHolder(ViewHolder) Method

Recycles the specified ViewHolder.  
It removes the view from the RecyclerView and hides it. Then, it puts the ViewHolder back into the recycled pool.

```csharp
public void RecycleViewHolder(Tizen.UI.Components.Recycler.ViewHolder viewholder);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.RecyclerView.RecycleViewHolder(Tizen.UI.Components.Recycler.ViewHolder).viewholder'></a>

`viewholder` [ViewHolder](Tizen.UI.Components.Recycler.ViewHolder.md 'Tizen.UI.Components.Recycler.ViewHolder')

The viewHolder to recycle.

<a name='Tizen.UI.Components.Recycler.RecyclerView.ScrollBy(float,float,bool)'></a>

## RecyclerView.ScrollBy(float, float, bool) Method

Scrolls the RecyclerView to the specified position with the given offset.

```csharp
public System.Threading.Tasks.Task ScrollBy(float x, float y, bool animation=true);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.RecyclerView.ScrollBy(float,float,bool).x'></a>

`x` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The x distance to scroll.

<a name='Tizen.UI.Components.Recycler.RecyclerView.ScrollBy(float,float,bool).y'></a>

`y` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The x distance to scroll.

<a name='Tizen.UI.Components.Recycler.RecyclerView.ScrollBy(float,float,bool).animation'></a>

`animation` [System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

Indicates whether the scrolling should be animated or not.

Implements [ScrollBy(float, float, bool)](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.IScrollable.ScrollBy#Tizen_UI_IScrollable_ScrollBy_System_Single,System_Single,System_Boolean_ 'Tizen.UI.IScrollable.ScrollBy(System.Single,System.Single,System.Boolean)')

#### Returns
[System.Threading.Tasks.Task](https://docs.microsoft.com/en-us/dotnet/api/System.Threading.Tasks.Task 'System.Threading.Tasks.Task')  
A task representing the asynchronous operation.

<a name='Tizen.UI.Components.Recycler.RecyclerView.ScrollTo(int,Tizen.UI.ScrollToPosition,bool)'></a>

## RecyclerView.ScrollTo(int, ScrollToPosition, bool) Method

Scrolls the RecyclerView to show the index position item in specified position with animation.

```csharp
public System.Threading.Tasks.Task ScrollTo(int position, Tizen.UI.ScrollToPosition scrollToPosition=Tizen.UI.ScrollToPosition.MakeVisible, bool animation=true);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.RecyclerView.ScrollTo(int,Tizen.UI.ScrollToPosition,bool).position'></a>

`position` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The position of the item to be shown.

<a name='Tizen.UI.Components.Recycler.RecyclerView.ScrollTo(int,Tizen.UI.ScrollToPosition,bool).scrollToPosition'></a>

`scrollToPosition` [Tizen.UI.ScrollToPosition](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.ScrollToPosition 'Tizen.UI.ScrollToPosition')

The position to scroll to. It can be Start, Center, or End.

<a name='Tizen.UI.Components.Recycler.RecyclerView.ScrollTo(int,Tizen.UI.ScrollToPosition,bool).animation'></a>

`animation` [System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

Indicates whether the scrolling should be animated or not.

#### Returns
[System.Threading.Tasks.Task](https://docs.microsoft.com/en-us/dotnet/api/System.Threading.Tasks.Task 'System.Threading.Tasks.Task')  
A task representing the asynchronous operation.
### Events

<a name='Tizen.UI.Components.Recycler.RecyclerView.DragFinished'></a>

## RecyclerView.DragFinished Event

Event for drag ended. Invoked when dragging ends.

```csharp
public event EventHandler&lt;DragEventArgs> DragFinished;
```

Implements [DragFinished](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.IScrollable.DragFinished 'Tizen.UI.IScrollable.DragFinished')

#### Event Type
[System.EventHandler&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')[Tizen.UI.DragEventArgs](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.DragEventArgs 'Tizen.UI.DragEventArgs')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')

<a name='Tizen.UI.Components.Recycler.RecyclerView.Dragging'></a>

## RecyclerView.Dragging Event

Event for dragging. Invoked when dragging happens.

```csharp
public event EventHandler&lt;DragEventArgs> Dragging;
```

Implements [Dragging](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.IScrollable.Dragging 'Tizen.UI.IScrollable.Dragging')

#### Event Type
[System.EventHandler&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')[Tizen.UI.DragEventArgs](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.DragEventArgs 'Tizen.UI.DragEventArgs')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')

<a name='Tizen.UI.Components.Recycler.RecyclerView.DragStarted'></a>

## RecyclerView.DragStarted Event

Event for drag started. Invoked when dragging starts.

```csharp
public event EventHandler&lt;DragEventArgs> DragStarted;
```

Implements [DragStarted](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.IScrollable.DragStarted 'Tizen.UI.IScrollable.DragStarted')

#### Event Type
[System.EventHandler&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')[Tizen.UI.DragEventArgs](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.DragEventArgs 'Tizen.UI.DragEventArgs')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')

<a name='Tizen.UI.Components.Recycler.RecyclerView.ScrollCanceled'></a>

## RecyclerView.ScrollCanceled Event

Event for scroll canceled. Invoked when scrolling canceled.

```csharp
public event EventHandler&lt;ScrollEventArgs> ScrollCanceled;
```

#### Event Type
[System.EventHandler&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')[Tizen.UI.ScrollEventArgs](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.ScrollEventArgs 'Tizen.UI.ScrollEventArgs')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')

<a name='Tizen.UI.Components.Recycler.RecyclerView.ScrollFinished'></a>

## RecyclerView.ScrollFinished Event

Event for scroll finished. Invoked when scrolling finishs.

```csharp
public event EventHandler&lt;ScrollEventArgs> ScrollFinished;
```

Implements [ScrollFinished](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.IScrollable.ScrollFinished 'Tizen.UI.IScrollable.ScrollFinished')

#### Event Type
[System.EventHandler&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')[Tizen.UI.ScrollEventArgs](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.ScrollEventArgs 'Tizen.UI.ScrollEventArgs')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')

<a name='Tizen.UI.Components.Recycler.RecyclerView.Scrolling'></a>

## RecyclerView.Scrolling Event

Event for scrolling. Invoked when scrolling happens.

```csharp
public event EventHandler&lt;ScrollEventArgs> Scrolling;
```

Implements [Scrolling](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.IScrollable.Scrolling 'Tizen.UI.IScrollable.Scrolling')

#### Event Type
[System.EventHandler&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')[Tizen.UI.ScrollEventArgs](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.ScrollEventArgs 'Tizen.UI.ScrollEventArgs')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')

<a name='Tizen.UI.Components.Recycler.RecyclerView.ScrollStarted'></a>

## RecyclerView.ScrollStarted Event

Event for scroll started. Invoked when scrolling starts.

```csharp
public event EventHandler&lt;ScrollEventArgs> ScrollStarted;
```

Implements [ScrollStarted](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.IScrollable.ScrollStarted 'Tizen.UI.IScrollable.ScrollStarted')

#### Event Type
[System.EventHandler&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')[Tizen.UI.ScrollEventArgs](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.ScrollEventArgs 'Tizen.UI.ScrollEventArgs')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')


























































