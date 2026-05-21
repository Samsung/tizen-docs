### [Tizen.UI.Components](Tizen.UI.Components.md 'Tizen.UI.Components')

## Scrollable Class

A scrollable view that can be scrolled.

```csharp
public class Scrollable : Tizen.UI.Layouts.Layout,
Tizen.UI.IDescendantFocusObserver,
Tizen.UI.IScrollable
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; Tizen.UI.NObject &#129106; Tizen.UI.View &#129106; Tizen.UI.ViewGroup &#129106; Tizen.UI.Layouts.Layout &#129106; Scrollable

Implements Tizen.UI.IDescendantFocusObserver, Tizen.UI.IScrollable
### Constructors

<a name='Tizen.UI.Components.Scrollable.Scrollable()'></a>

## Scrollable() Constructor

Initializes a new instance of the [Scrollable](Tizen.UI.Components.Scrollable.md 'Tizen.UI.Components.Scrollable') class.

```csharp
public Scrollable();
```
### Properties

<a name='Tizen.UI.Components.Scrollable.CanScrollHorizontally'></a>

## Scrollable.CanScrollHorizontally Property

Check whether scroller can scroll horizontally or not.

```csharp
public bool CanScrollHorizontally { get; }
```

Implements CanScrollHorizontally

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.Scrollable.CanScrollVertically'></a>

## Scrollable.CanScrollVertically Property

Check whether scroller can scroll Vertically or not.

```csharp
public bool CanScrollVertically { get; }
```

Implements CanScrollVertically

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.Scrollable.Content'></a>

## Scrollable.Content Property

Gets or sets the content of the scroll view.

```csharp
public Tizen.UI.View Content { get; set; }
```

#### Property Value
Tizen.UI.View

<a name='Tizen.UI.Components.Scrollable.HorizontalEdgeEffect'></a>

## Scrollable.HorizontalEdgeEffect Property

[IEdgeEffect](Tizen.UI.Components.IEdgeEffect.md 'Tizen.UI.Components.IEdgeEffect') of horizontal scroll direction.  
            edge effect will be come when scroll over the edge of horizontal direction.

```csharp
public Tizen.UI.Components.IEdgeEffect HorizontalEdgeEffect { get; set; }
```

#### Property Value
[IEdgeEffect](Tizen.UI.Components.IEdgeEffect.md 'Tizen.UI.Components.IEdgeEffect')

<a name='Tizen.UI.Components.Scrollable.HorizontalScrollBarVisibility'></a>

## Scrollable.HorizontalScrollBarVisibility Property

Gets or sets the visibility of the horizontal scroll bar.

```csharp
public Tizen.UI.ScrollBarVisibility HorizontalScrollBarVisibility { get; set; }
```

#### Property Value
Tizen.UI.ScrollBarVisibility

<a name='Tizen.UI.Components.Scrollable.IsScrolledToEnd'></a>

## Scrollable.IsScrolledToEnd Property

Gets a value indicating whether the scrollable content has reached the end position.

```csharp
public bool IsScrolledToEnd { get; }
```

Implements IsScrolledToEnd

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.Scrollable.IsScrolledToStart'></a>

## Scrollable.IsScrolledToStart Property

Gets a value indicating whether the scrollable content has been scrolled to the start position.

```csharp
public bool IsScrolledToStart { get; }
```

Implements IsScrolledToStart

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.Scrollable.IsScrolling'></a>

## Scrollable.IsScrolling Property

Gets a value indicating whether the scroll is currently in progress.

```csharp
public bool IsScrolling { get; set; }
```

Implements IsScrolling

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.Scrollable.OverScrollMode'></a>

## Scrollable.OverScrollMode Property

Set over scroll mode as type of [OverScrollMode](Tizen.UI.Components.Scrollable.md#Tizen.UI.Components.Scrollable.OverScrollMode 'Tizen.UI.Components.Scrollable.OverScrollMode').  
Default mode is [ContentScrolls](Tizen.UI.Components.OverScrollMode.md#Tizen.UI.Components.OverScrollMode.ContentScrolls 'Tizen.UI.Components.OverScrollMode.ContentScrolls').

```csharp
public Tizen.UI.Components.OverScrollMode OverScrollMode { get; set; }
```

#### Property Value
[OverScrollMode](Tizen.UI.Components.OverScrollMode.md 'Tizen.UI.Components.OverScrollMode')

<a name='Tizen.UI.Components.Scrollable.ScrollableHeight'></a>

## Scrollable.ScrollableHeight Property

Gets or sets the height of the scrollable content.

```csharp
public float ScrollableHeight { get; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Components.Scrollable.ScrollableWidth'></a>

## Scrollable.ScrollableWidth Property

Gets or sets the width of the scrollable content.

```csharp
public float ScrollableWidth { get; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Components.Scrollable.ScrollBar'></a>

## Scrollable.ScrollBar Property

Gets or sets the scroll bar.

```csharp
public Tizen.UI.IScrollBar ScrollBar { get; set; }
```

#### Property Value
Tizen.UI.IScrollBar

<a name='Tizen.UI.Components.Scrollable.ScrollDirection'></a>

## Scrollable.ScrollDirection Property

Gets or sets the direction of the scroll.

```csharp
public Tizen.UI.ScrollDirection ScrollDirection { get; set; }
```

#### Property Value
Tizen.UI.ScrollDirection

<a name='Tizen.UI.Components.Scrollable.ScrollingDestinationHandler'></a>

## Scrollable.ScrollingDestinationHandler Property

The ScrollingDestinationHandler property sets or gets a function that handles the scrolling destination calculation.

```csharp
public System.Func&lt;Tizen.UI.Point,Tizen.UI.Point> ScrollingDestinationHandler { get; set; }
```

#### Property Value
[System.Func&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-2 'System.Func`2')Tizen.UI.Point[,](https://docs.microsoft.com/en-us/dotnet/api/System.Func-2 'System.Func`2')Tizen.UI.Point[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-2 'System.Func`2')

<a name='Tizen.UI.Components.Scrollable.ScrollPosition'></a>

## Scrollable.ScrollPosition Property

Gets the current scroll position.

```csharp
public Tizen.UI.Point ScrollPosition { get; }
```

#### Property Value
Tizen.UI.Point

<a name='Tizen.UI.Components.Scrollable.ScrollSize'></a>

## Scrollable.ScrollSize Property

Gets or sets the size of the scrollable content.

```csharp
public Tizen.UI.Size ScrollSize { get; set; }
```

#### Property Value
Tizen.UI.Size

<a name='Tizen.UI.Components.Scrollable.VerticalEdgeEffect'></a>

## Scrollable.VerticalEdgeEffect Property

[IEdgeEffect](Tizen.UI.Components.IEdgeEffect.md 'Tizen.UI.Components.IEdgeEffect') of vertical scroll direction.  
            edge effect will be come when scroll over the edge of vertical direction.

```csharp
public Tizen.UI.Components.IEdgeEffect VerticalEdgeEffect { get; set; }
```

#### Property Value
[IEdgeEffect](Tizen.UI.Components.IEdgeEffect.md 'Tizen.UI.Components.IEdgeEffect')

<a name='Tizen.UI.Components.Scrollable.VerticalScrollBarVisibility'></a>

## Scrollable.VerticalScrollBarVisibility Property

Gets or sets the visibility of the vertical scroll bar.

```csharp
public Tizen.UI.ScrollBarVisibility VerticalScrollBarVisibility { get; set; }
```

#### Property Value
Tizen.UI.ScrollBarVisibility

<a name='Tizen.UI.Components.Scrollable.ViewPort'></a>

## Scrollable.ViewPort Property

Gets the scroll bounds of the Scrollable content.

```csharp
public Tizen.UI.Rect ViewPort { get; }
```

Implements ViewPort

#### Property Value
Tizen.UI.Rect
### Methods

<a name='Tizen.UI.Components.Scrollable.IsScrollableOnDirection(Tizen.UI.ScrollDirection)'></a>

## Scrollable.IsScrollableOnDirection(ScrollDirection) Method

Whether is scrollable on horizontal direction.

```csharp
public bool IsScrollableOnDirection(Tizen.UI.ScrollDirection direction);
```
#### Parameters

<a name='Tizen.UI.Components.Scrollable.IsScrollableOnDirection(Tizen.UI.ScrollDirection).direction'></a>

`direction` Tizen.UI.ScrollDirection

scroll direction.

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.Scrollable.ScrollTo(float,bool)'></a>

## Scrollable.ScrollTo(float, bool) Method

Scrolls the content to the specified position.

```csharp
public System.Threading.Tasks.Task ScrollTo(float position, bool animation);
```
#### Parameters

<a name='Tizen.UI.Components.Scrollable.ScrollTo(float,bool).position'></a>

`position` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The position to which the content will be scrolled.

<a name='Tizen.UI.Components.Scrollable.ScrollTo(float,bool).animation'></a>

`animation` [System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

Whether to play an animation while scrolling.

#### Returns
[System.Threading.Tasks.Task](https://docs.microsoft.com/en-us/dotnet/api/System.Threading.Tasks.Task 'System.Threading.Tasks.Task')  
A task that represents the asynchronous operation.

<a name='Tizen.UI.Components.Scrollable.ScrollTo(Tizen.UI.Point,bool)'></a>

## Scrollable.ScrollTo(Point, bool) Method

Scrolls the content to the specified position.

```csharp
public System.Threading.Tasks.Task ScrollTo(Tizen.UI.Point position, bool animation);
```
#### Parameters

<a name='Tizen.UI.Components.Scrollable.ScrollTo(Tizen.UI.Point,bool).position'></a>

`position` Tizen.UI.Point

The position to which the content will be scrolled.

<a name='Tizen.UI.Components.Scrollable.ScrollTo(Tizen.UI.Point,bool).animation'></a>

`animation` [System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

Whether to play an animation while scrolling.

#### Returns
[System.Threading.Tasks.Task](https://docs.microsoft.com/en-us/dotnet/api/System.Threading.Tasks.Task 'System.Threading.Tasks.Task')  
A task that represents the asynchronous operation.

<a name='Tizen.UI.Components.Scrollable.ScrollTo(Tizen.UI.View,bool,Tizen.UI.ScrollToPosition)'></a>

## Scrollable.ScrollTo(View, bool, ScrollToPosition) Method

Scrolls the content to the specified child view.

```csharp
public System.Threading.Tasks.Task ScrollTo(Tizen.UI.View child, bool animation, Tizen.UI.ScrollToPosition scrollToPosition);
```
#### Parameters

<a name='Tizen.UI.Components.Scrollable.ScrollTo(Tizen.UI.View,bool,Tizen.UI.ScrollToPosition).child'></a>

`child` Tizen.UI.View

The child view to which the content will be scrolled.

<a name='Tizen.UI.Components.Scrollable.ScrollTo(Tizen.UI.View,bool,Tizen.UI.ScrollToPosition).animation'></a>

`animation` [System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

Whether to play an animation while scrolling.

<a name='Tizen.UI.Components.Scrollable.ScrollTo(Tizen.UI.View,bool,Tizen.UI.ScrollToPosition).scrollToPosition'></a>

`scrollToPosition` Tizen.UI.ScrollToPosition

The position to which the child view will be scrolled.

#### Returns
[System.Threading.Tasks.Task](https://docs.microsoft.com/en-us/dotnet/api/System.Threading.Tasks.Task 'System.Threading.Tasks.Task')  
A task that represents the asynchronous operation.

<a name='Tizen.UI.Components.Scrollable.UpdateLayout(Tizen.UI.Rect)'></a>

## Scrollable.UpdateLayout(Rect) Method

Updates the layout with the specified bounds.

```csharp
public override Tizen.UI.Size UpdateLayout(Tizen.UI.Rect bounds);
```
#### Parameters

<a name='Tizen.UI.Components.Scrollable.UpdateLayout(Tizen.UI.Rect).bounds'></a>

`bounds` Tizen.UI.Rect

The bounds to update the layout with.

#### Returns
Tizen.UI.Size  
The size of the layout after updating.
### Events

<a name='Tizen.UI.Components.Scrollable.DragFinished'></a>

## Scrollable.DragFinished Event

Event handler for when the dragging of the Scrollable finished.

```csharp
public event EventHandler&lt;DragEventArgs> DragFinished;
```

Implements DragFinished

#### Event Type
[System.EventHandler&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')Tizen.UI.DragEventArgs[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')

<a name='Tizen.UI.Components.Scrollable.Dragging'></a>

## Scrollable.Dragging Event

Event handler for the Dragging event.

```csharp
public event EventHandler&lt;DragEventArgs> Dragging;
```

Implements Dragging

#### Event Type
[System.EventHandler&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')Tizen.UI.DragEventArgs[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')

<a name='Tizen.UI.Components.Scrollable.DragStarted'></a>

## Scrollable.DragStarted Event

Event handler for the Scrollable drag started event.

```csharp
public event EventHandler&lt;DragEventArgs> DragStarted;
```

Implements DragStarted

#### Event Type
[System.EventHandler&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')Tizen.UI.DragEventArgs[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')

<a name='Tizen.UI.Components.Scrollable.ScrollFinished'></a>

## Scrollable.ScrollFinished Event

Occurs when the scroll finishes.

```csharp
public event EventHandler&lt;ScrollEventArgs> ScrollFinished;
```

Implements ScrollFinished

#### Event Type
[System.EventHandler&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')Tizen.UI.ScrollEventArgs[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')

<a name='Tizen.UI.Components.Scrollable.Scrolling'></a>

## Scrollable.Scrolling Event

Occurs while scrolling.

```csharp
public event EventHandler&lt;ScrollEventArgs> Scrolling;
```

Implements Scrolling

#### Event Type
[System.EventHandler&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')Tizen.UI.ScrollEventArgs[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')

<a name='Tizen.UI.Components.Scrollable.ScrollStarted'></a>

## Scrollable.ScrollStarted Event

Occurs when the scroll starts.

```csharp
public event EventHandler&lt;ScrollEventArgs> ScrollStarted;
```

Implements ScrollStarted

#### Event Type
[System.EventHandler&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')Tizen.UI.ScrollEventArgs[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')



























































