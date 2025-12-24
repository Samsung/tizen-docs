### [Tizen.UI.Components.Material](Tizen.UI.Components.Material.md 'Tizen.UI.Components.Material')

## AdapterView Class

A loopable scroll view that displays recycling items in specific layouts with adapter.

```csharp
public abstract class AdapterView : Tizen.UI.ContentView
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [Tizen.UI.NObject](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.NObject 'Tizen.UI.NObject') &#129106; [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View') &#129106; [Tizen.UI.ContentView](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.ContentView 'Tizen.UI.ContentView') &#129106; AdapterView

Derived  
&#8627; [LoopedAdapterView](Tizen.UI.Components.Material.LoopedAdapterView.md 'Tizen.UI.Components.Material.LoopedAdapterView')
### Constructors

<a name='Tizen.UI.Components.Material.AdapterView.AdapterView()'></a>

## AdapterView() Constructor

Creates a new instance of a AdapterView.

```csharp
public AdapterView();
```
### Properties

<a name='Tizen.UI.Components.Material.AdapterView.InnerMargin'></a>

## AdapterView.InnerMargin Property

The margin offset of recycler view.  
ScrollBar will not be affected. To place all contents, use [Padding](Tizen.UI.Components.Material.AdapterView.md#Tizen.UI.Components.Material.AdapterView.Padding 'Tizen.UI.Components.Material.AdapterView.Padding')

```csharp
public Tizen.UI.Thickness InnerMargin { get; set; }
```

#### Property Value
[Tizen.UI.Thickness](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Thickness 'Tizen.UI.Thickness')

<a name='Tizen.UI.Components.Material.AdapterView.ItemDecorations'></a>

## AdapterView.ItemDecorations Property

The list of decoration helper for items.

```csharp
public System.Collections.Generic.IList&lt;Tizen.UI.Components.Recycler.IItemDecoration> ItemDecorations { get; }
```

#### Property Value
[System.Collections.Generic.IList&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1 'System.Collections.Generic.IList`1')[Tizen.UI.Components.Recycler.IItemDecoration](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.Recycler.IItemDecoration 'Tizen.UI.Components.Recycler.IItemDecoration')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1 'System.Collections.Generic.IList`1')

<a name='Tizen.UI.Components.Material.AdapterView.ItemsSource'></a>

## AdapterView.ItemsSource Property

The data source for the view. The data source is a collection of items that will be displayed in the view.  
The items must implement the INotifyPropertyChanged interface to notify the view of changes. Default is null.

```csharp
public System.Collections.IEnumerable ItemsSource { get; set; }
```

#### Property Value
[System.Collections.IEnumerable](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.IEnumerable 'System.Collections.IEnumerable')

<a name='Tizen.UI.Components.Material.AdapterView.ItemTemplate'></a>

## AdapterView.ItemTemplate Property

The item template for the view. The item template is a data template that defines how each item will be displayed in the.

```csharp
public Tizen.UI.ViewTemplate ItemTemplate { get; set; }
```

#### Property Value
[Tizen.UI.ViewTemplate](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.ViewTemplate 'Tizen.UI.ViewTemplate')

<a name='Tizen.UI.Components.Material.AdapterView.Padding'></a>

## AdapterView.Padding Property

The padding of the view.  
If you want to modify the place with an offset on RecyclerView, use [InnerMargin](Tizen.UI.Components.Material.AdapterView.md#Tizen.UI.Components.Material.AdapterView.InnerMargin 'Tizen.UI.Components.Material.AdapterView.InnerMargin').

```csharp
public Tizen.UI.Thickness Padding { get; set; }
```

#### Property Value
[Tizen.UI.Thickness](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Thickness 'Tizen.UI.Thickness')

<a name='Tizen.UI.Components.Material.AdapterView.PrefetchBaseSize'></a>

## AdapterView.PrefetchBaseSize Property

The prefetch base size for the view. The prefetch base size determines how many items are preloaded before and after the visible area. Default is 300.0f.

```csharp
public float PrefetchBaseSize { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Components.Material.AdapterView.ScrollBarVisibility'></a>

## AdapterView.ScrollBarVisibility Property

The visibility of the scroll bar for the grid view. The scroll bar visibility can be set to Always, Auto, or Never. Default is Never.

```csharp
public Tizen.UI.ScrollBarVisibility ScrollBarVisibility { get; set; }
```

#### Property Value
[Tizen.UI.ScrollBarVisibility](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.ScrollBarVisibility 'Tizen.UI.ScrollBarVisibility')
### Methods

<a name='Tizen.UI.Components.Material.AdapterView.SetScrollBar(Tizen.UI.IScrollBar)'></a>

## AdapterView.SetScrollBar(IScrollBar) Method

Sets the scroll bar for the view. The scroll bar can be used to indicate the current position and range of the scrollable content. Default is null.

```csharp
public void SetScrollBar(Tizen.UI.IScrollBar scrollBar);
```
#### Parameters

<a name='Tizen.UI.Components.Material.AdapterView.SetScrollBar(Tizen.UI.IScrollBar).scrollBar'></a>

`scrollBar` [Tizen.UI.IScrollBar](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.IScrollBar 'Tizen.UI.IScrollBar')

The scroll bar to set.
### Events

<a name='Tizen.UI.Components.Material.AdapterView.DragFinished'></a>

## AdapterView.DragFinished Event

Event for drag ended. Invoked when dragging ends.

```csharp
public event EventHandler&lt;DragEventArgs> DragFinished;
```

#### Event Type
[System.EventHandler&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')[Tizen.UI.DragEventArgs](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.DragEventArgs 'Tizen.UI.DragEventArgs')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')

<a name='Tizen.UI.Components.Material.AdapterView.Dragging'></a>

## AdapterView.Dragging Event

Event for dragging. Invoked when dragging happens.

```csharp
public event EventHandler&lt;DragEventArgs> Dragging;
```

#### Event Type
[System.EventHandler&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')[Tizen.UI.DragEventArgs](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.DragEventArgs 'Tizen.UI.DragEventArgs')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')

<a name='Tizen.UI.Components.Material.AdapterView.DragStarted'></a>

## AdapterView.DragStarted Event

Event for drag started. Invoked when dragging starts.

```csharp
public event EventHandler&lt;DragEventArgs> DragStarted;
```

#### Event Type
[System.EventHandler&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')[Tizen.UI.DragEventArgs](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.DragEventArgs 'Tizen.UI.DragEventArgs')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')

<a name='Tizen.UI.Components.Material.AdapterView.ScrollFinished'></a>

## AdapterView.ScrollFinished Event

Event for scroll finished. Invoked when scrolling finishs.

```csharp
public event EventHandler&lt;ScrollEventArgs> ScrollFinished;
```

#### Event Type
[System.EventHandler&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')[Tizen.UI.ScrollEventArgs](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.ScrollEventArgs 'Tizen.UI.ScrollEventArgs')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')

<a name='Tizen.UI.Components.Material.AdapterView.Scrolling'></a>

## AdapterView.Scrolling Event

Event for scrolling. Invoked when scrolling happens.

```csharp
public event EventHandler&lt;ScrollEventArgs> Scrolling;
```

#### Event Type
[System.EventHandler&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')[Tizen.UI.ScrollEventArgs](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.ScrollEventArgs 'Tizen.UI.ScrollEventArgs')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')

<a name='Tizen.UI.Components.Material.AdapterView.ScrollStarted'></a>

## AdapterView.ScrollStarted Event

Event for scroll started. Invoked when scrolling starts.

```csharp
public event EventHandler&lt;ScrollEventArgs> ScrollStarted;
```

#### Event Type
[System.EventHandler&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')[Tizen.UI.ScrollEventArgs](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.ScrollEventArgs 'Tizen.UI.ScrollEventArgs')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')













































