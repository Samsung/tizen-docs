### [Tizen.UI.Layouts](Tizen.UI.Layouts.md 'Tizen.UI.Layouts')

## ScrollLayout Class

A scrollable view that can be scrolled.

```csharp
public class ScrollLayout : Tizen.UI.Layouts.Layout,
Tizen.UI.IDescendantFocusObserver,
Tizen.UI.IScrollable
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [Tizen.UI.NObject](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.NObject 'Tizen.UI.NObject') &#129106; [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View') &#129106; [Tizen.UI.ViewGroup](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.ViewGroup 'Tizen.UI.ViewGroup') &#129106; [Layout](Tizen.UI.Layouts.Layout.md 'Tizen.UI.Layouts.Layout') &#129106; ScrollLayout

Implements [Tizen.UI.IDescendantFocusObserver](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.IDescendantFocusObserver 'Tizen.UI.IDescendantFocusObserver'), [Tizen.UI.IScrollable](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.IScrollable 'Tizen.UI.IScrollable')
### Constructors

<a name='Tizen.UI.Layouts.ScrollLayout.ScrollLayout()'></a>

## ScrollLayout() Constructor

Initializes a new instance of the [ScrollLayout](Tizen.UI.Layouts.ScrollLayout.md 'Tizen.UI.Layouts.ScrollLayout') class.

```csharp
public ScrollLayout();
```
### Properties

<a name='Tizen.UI.Layouts.ScrollLayout.Content'></a>

## ScrollLayout.Content Property

Gets or sets the content of the scroll view.

```csharp
public Tizen.UI.View Content { get; set; }
```

#### Property Value
[Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')

<a name='Tizen.UI.Layouts.ScrollLayout.HorizontalScrollBarVisibility'></a>

## ScrollLayout.HorizontalScrollBarVisibility Property

Gets or sets the visibility of the horizontal scroll bar.

```csharp
public Tizen.UI.ScrollBarVisibility HorizontalScrollBarVisibility { get; set; }
```

#### Property Value
[Tizen.UI.ScrollBarVisibility](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.ScrollBarVisibility 'Tizen.UI.ScrollBarVisibility')

<a name='Tizen.UI.Layouts.ScrollLayout.IsScrolling'></a>

## ScrollLayout.IsScrolling Property

Gets a value indicating whether the scroll is currently in progress.

```csharp
public bool IsScrolling { get; set; }
```

Implements [IsScrolling](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.IScrollable.IsScrolling 'Tizen.UI.IScrollable.IsScrolling')

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Layouts.ScrollLayout.ScrollBar'></a>

## ScrollLayout.ScrollBar Property

Gets or sets the scroll bar.

```csharp
public Tizen.UI.IScrollBar ScrollBar { get; set; }
```

#### Property Value
[Tizen.UI.IScrollBar](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.IScrollBar 'Tizen.UI.IScrollBar')

<a name='Tizen.UI.Layouts.ScrollLayout.ScrollDirection'></a>

## ScrollLayout.ScrollDirection Property

Gets or sets the direction of the scroll.

```csharp
public Tizen.UI.ScrollDirection ScrollDirection { get; set; }
```

#### Property Value
[Tizen.UI.ScrollDirection](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.ScrollDirection 'Tizen.UI.ScrollDirection')

<a name='Tizen.UI.Layouts.ScrollLayout.ScrollingDestinationHandler'></a>

## ScrollLayout.ScrollingDestinationHandler Property

The ScrollingDestinationHandler property sets or gets a function that handles the scrolling destination calculation.

```csharp
public System.Func&lt;Tizen.UI.Point,Tizen.UI.Point> ScrollingDestinationHandler { get; set; }
```

#### Property Value
[System.Func&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-2 'System.Func`2')[Tizen.UI.Point](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Point 'Tizen.UI.Point')[,](https://docs.microsoft.com/en-us/dotnet/api/System.Func-2 'System.Func`2')[Tizen.UI.Point](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Point 'Tizen.UI.Point')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-2 'System.Func`2')

<a name='Tizen.UI.Layouts.ScrollLayout.ScrollPosition'></a>

## ScrollLayout.ScrollPosition Property

Gets the current scroll position.

```csharp
public Tizen.UI.Point ScrollPosition { get; }
```

#### Property Value
[Tizen.UI.Point](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Point 'Tizen.UI.Point')

<a name='Tizen.UI.Layouts.ScrollLayout.ScrollSize'></a>

## ScrollLayout.ScrollSize Property

Gets or sets the size of the scrollable content.

```csharp
public Tizen.UI.Size ScrollSize { get; set; }
```

#### Property Value
[Tizen.UI.Size](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Size 'Tizen.UI.Size')

<a name='Tizen.UI.Layouts.ScrollLayout.VerticalScrollBarVisibility'></a>

## ScrollLayout.VerticalScrollBarVisibility Property

Gets or sets the visibility of the vertical scroll bar.

```csharp
public Tizen.UI.ScrollBarVisibility VerticalScrollBarVisibility { get; set; }
```

#### Property Value
[Tizen.UI.ScrollBarVisibility](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.ScrollBarVisibility 'Tizen.UI.ScrollBarVisibility')

<a name='Tizen.UI.Layouts.ScrollLayout.ViewPort'></a>

## ScrollLayout.ViewPort Property

Gets the scroll bounds of the ScrollView content.

```csharp
public Tizen.UI.Rect ViewPort { get; }
```

Implements [ViewPort](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.IScrollable.ViewPort 'Tizen.UI.IScrollable.ViewPort')

#### Property Value
[Tizen.UI.Rect](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Rect 'Tizen.UI.Rect')
### Methods

<a name='Tizen.UI.Layouts.ScrollLayout.ScrollTo(float,bool)'></a>

## ScrollLayout.ScrollTo(float, bool) Method

Scrolls the content to the specified position.

```csharp
public System.Threading.Tasks.Task ScrollTo(float position, bool animation);
```
#### Parameters

<a name='Tizen.UI.Layouts.ScrollLayout.ScrollTo(float,bool).position'></a>

`position` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The position to which the content will be scrolled.

<a name='Tizen.UI.Layouts.ScrollLayout.ScrollTo(float,bool).animation'></a>

`animation` [System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

Whether to play an animation while scrolling.

#### Returns
[System.Threading.Tasks.Task](https://docs.microsoft.com/en-us/dotnet/api/System.Threading.Tasks.Task 'System.Threading.Tasks.Task')  
A task that represents the asynchronous operation.

<a name='Tizen.UI.Layouts.ScrollLayout.ScrollTo(Tizen.UI.Point,bool)'></a>

## ScrollLayout.ScrollTo(Point, bool) Method

Scrolls the content to the specified position.

```csharp
public System.Threading.Tasks.Task ScrollTo(Tizen.UI.Point position, bool animation);
```
#### Parameters

<a name='Tizen.UI.Layouts.ScrollLayout.ScrollTo(Tizen.UI.Point,bool).position'></a>

`position` [Tizen.UI.Point](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Point 'Tizen.UI.Point')

The position to which the content will be scrolled.

<a name='Tizen.UI.Layouts.ScrollLayout.ScrollTo(Tizen.UI.Point,bool).animation'></a>

`animation` [System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

Whether to play an animation while scrolling.

#### Returns
[System.Threading.Tasks.Task](https://docs.microsoft.com/en-us/dotnet/api/System.Threading.Tasks.Task 'System.Threading.Tasks.Task')  
A task that represents the asynchronous operation.

<a name='Tizen.UI.Layouts.ScrollLayout.ScrollTo(Tizen.UI.View,bool,Tizen.UI.ScrollToPosition)'></a>

## ScrollLayout.ScrollTo(View, bool, ScrollToPosition) Method

Scrolls the content to the specified child view.

```csharp
public System.Threading.Tasks.Task ScrollTo(Tizen.UI.View child, bool animation, Tizen.UI.ScrollToPosition scrollToPosition);
```
#### Parameters

<a name='Tizen.UI.Layouts.ScrollLayout.ScrollTo(Tizen.UI.View,bool,Tizen.UI.ScrollToPosition).child'></a>

`child` [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')

The child view to which the content will be scrolled.

<a name='Tizen.UI.Layouts.ScrollLayout.ScrollTo(Tizen.UI.View,bool,Tizen.UI.ScrollToPosition).animation'></a>

`animation` [System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

Whether to play an animation while scrolling.

<a name='Tizen.UI.Layouts.ScrollLayout.ScrollTo(Tizen.UI.View,bool,Tizen.UI.ScrollToPosition).scrollToPosition'></a>

`scrollToPosition` [Tizen.UI.ScrollToPosition](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.ScrollToPosition 'Tizen.UI.ScrollToPosition')

The position to which the child view will be scrolled.

#### Returns
[System.Threading.Tasks.Task](https://docs.microsoft.com/en-us/dotnet/api/System.Threading.Tasks.Task 'System.Threading.Tasks.Task')  
A task that represents the asynchronous operation.

<a name='Tizen.UI.Layouts.ScrollLayout.UpdateLayout(Tizen.UI.Rect)'></a>

## ScrollLayout.UpdateLayout(Rect) Method

Updates the layout with the specified bounds.

```csharp
public override Tizen.UI.Size UpdateLayout(Tizen.UI.Rect bounds);
```
#### Parameters

<a name='Tizen.UI.Layouts.ScrollLayout.UpdateLayout(Tizen.UI.Rect).bounds'></a>

`bounds` [Tizen.UI.Rect](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Rect 'Tizen.UI.Rect')

The bounds to update the layout with.

#### Returns
[Tizen.UI.Size](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Size 'Tizen.UI.Size')  
The size of the layout after updating.
### Events

<a name='Tizen.UI.Layouts.ScrollLayout.DragFinished'></a>

## ScrollLayout.DragFinished Event

Event handler for when the dragging of the ScrollView ends.

```csharp
public event EventHandler&lt;DragEventArgs> DragFinished;
```

Implements [DragFinished](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.IScrollable.DragFinished 'Tizen.UI.IScrollable.DragFinished')

#### Event Type
[System.EventHandler&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')[Tizen.UI.DragEventArgs](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.DragEventArgs 'Tizen.UI.DragEventArgs')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')

<a name='Tizen.UI.Layouts.ScrollLayout.Dragging'></a>

## ScrollLayout.Dragging Event

Event handler for the Dragging event.

```csharp
public event EventHandler&lt;DragEventArgs> Dragging;
```

Implements [Dragging](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.IScrollable.Dragging 'Tizen.UI.IScrollable.Dragging')

#### Event Type
[System.EventHandler&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')[Tizen.UI.DragEventArgs](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.DragEventArgs 'Tizen.UI.DragEventArgs')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')

<a name='Tizen.UI.Layouts.ScrollLayout.DragStarted'></a>

## ScrollLayout.DragStarted Event

Event handler for the ScrollView drag started event.

```csharp
public event EventHandler&lt;DragEventArgs> DragStarted;
```

Implements [DragStarted](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.IScrollable.DragStarted 'Tizen.UI.IScrollable.DragStarted')

#### Event Type
[System.EventHandler&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')[Tizen.UI.DragEventArgs](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.DragEventArgs 'Tizen.UI.DragEventArgs')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')

<a name='Tizen.UI.Layouts.ScrollLayout.ScrollFinished'></a>

## ScrollLayout.ScrollFinished Event

Occurs when the scroll finishes.

```csharp
public event EventHandler&lt;ScrollEventArgs> ScrollFinished;
```

Implements [ScrollFinished](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.IScrollable.ScrollFinished 'Tizen.UI.IScrollable.ScrollFinished')

#### Event Type
[System.EventHandler&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')[Tizen.UI.ScrollEventArgs](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.ScrollEventArgs 'Tizen.UI.ScrollEventArgs')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')

<a name='Tizen.UI.Layouts.ScrollLayout.Scrolling'></a>

## ScrollLayout.Scrolling Event

Occurs while scrolling.

```csharp
public event EventHandler&lt;ScrollEventArgs> Scrolling;
```

Implements [Scrolling](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.IScrollable.Scrolling 'Tizen.UI.IScrollable.Scrolling')

#### Event Type
[System.EventHandler&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')[Tizen.UI.ScrollEventArgs](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.ScrollEventArgs 'Tizen.UI.ScrollEventArgs')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')

<a name='Tizen.UI.Layouts.ScrollLayout.ScrollStarted'></a>

## ScrollLayout.ScrollStarted Event

Occurs when the scroll starts.

```csharp
public event EventHandler&lt;ScrollEventArgs> ScrollStarted;
```

Implements [ScrollStarted](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.IScrollable.ScrollStarted 'Tizen.UI.IScrollable.ScrollStarted')

#### Event Type
[System.EventHandler&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')[Tizen.UI.ScrollEventArgs](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.ScrollEventArgs 'Tizen.UI.ScrollEventArgs')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')






























































