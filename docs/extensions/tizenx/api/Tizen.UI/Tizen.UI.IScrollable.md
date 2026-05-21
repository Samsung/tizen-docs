### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## IScrollable Interface

An interface describes the functionality of a scrollable component.

```csharp
public interface IScrollable
```
### Properties

<a name='Tizen.UI.IScrollable.CanScrollHorizontally'></a>

## IScrollable.CanScrollHorizontally Property

Gets whether this view can scroll horizontally.

```csharp
bool CanScrollHorizontally { get; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.IScrollable.CanScrollVertically'></a>

## IScrollable.CanScrollVertically Property

Gets whether this view can scroll vertically.

```csharp
bool CanScrollVertically { get; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.IScrollable.IsScrolledToEnd'></a>

## IScrollable.IsScrolledToEnd Property

Gets a value indicating whether the scrollable content has reached the end position.

```csharp
bool IsScrolledToEnd { get; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.IScrollable.IsScrolledToStart'></a>

## IScrollable.IsScrolledToStart Property

Gets a value indicating whether the scrollable content has been scrolled to the start position.

```csharp
bool IsScrolledToStart { get; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.IScrollable.IsScrolling'></a>

## IScrollable.IsScrolling Property

Gets a value indicating whether the scroll is currently in progress.

```csharp
bool IsScrolling { get; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.IScrollable.ViewPort'></a>

## IScrollable.ViewPort Property

Gets the scroll bounds of the scrollable content.

```csharp
Tizen.UI.Rect ViewPort { get; }
```

#### Property Value
[Rect](Tizen.UI.Rect.md 'Tizen.UI.Rect')
### Methods

<a name='Tizen.UI.IScrollable.ScrollBy(float,float,bool)'></a>

## IScrollable.ScrollBy(float, float, bool) Method

Scrolls the scrollable content by the specified offset in the x and y directions.

```csharp
System.Threading.Tasks.Task ScrollBy(float dx, float dy, bool animated);
```
#### Parameters

<a name='Tizen.UI.IScrollable.ScrollBy(float,float,bool).dx'></a>

`dx` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The x distance offset of the content will be scrolled.

<a name='Tizen.UI.IScrollable.ScrollBy(float,float,bool).dy'></a>

`dy` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The y distance offset of the content will be scrolled.

<a name='Tizen.UI.IScrollable.ScrollBy(float,float,bool).animated'></a>

`animated` [System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

#### Returns
[System.Threading.Tasks.Task](https://docs.microsoft.com/en-us/dotnet/api/System.Threading.Tasks.Task 'System.Threading.Tasks.Task')

<a name='Tizen.UI.IScrollable.ScrollTo(float,float,bool)'></a>

## IScrollable.ScrollTo(float, float, bool) Method

Scrolls the content to the specified position.

```csharp
System.Threading.Tasks.Task ScrollTo(float x, float y, bool animation);
```
#### Parameters

<a name='Tizen.UI.IScrollable.ScrollTo(float,float,bool).x'></a>

`x` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The x position to which the content will be scrolled.

<a name='Tizen.UI.IScrollable.ScrollTo(float,float,bool).y'></a>

`y` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The y position to which the content will be scrolled.

<a name='Tizen.UI.IScrollable.ScrollTo(float,float,bool).animation'></a>

`animation` [System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

Whether to play an animation while scrolling.

#### Returns
[System.Threading.Tasks.Task](https://docs.microsoft.com/en-us/dotnet/api/System.Threading.Tasks.Task 'System.Threading.Tasks.Task')  
A task that represents the asynchronous operation.
### Events

<a name='Tizen.UI.IScrollable.DragFinished'></a>

## IScrollable.DragFinished Event

Event that is triggered when the dragging of the scrollable content finished.

```csharp
event EventHandler&lt;DragEventArgs> DragFinished;
```

#### Event Type
[System.EventHandler&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')[DragEventArgs](Tizen.UI.DragEventArgs.md 'Tizen.UI.DragEventArgs')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')

<a name='Tizen.UI.IScrollable.Dragging'></a>

## IScrollable.Dragging Event

Event handler for the dragging state of the scrollable component.

```csharp
event EventHandler&lt;DragEventArgs> Dragging;
```

#### Event Type
[System.EventHandler&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')[DragEventArgs](Tizen.UI.DragEventArgs.md 'Tizen.UI.DragEventArgs')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')

<a name='Tizen.UI.IScrollable.DragStarted'></a>

## IScrollable.DragStarted Event

Event handler for the drag started event.

```csharp
event EventHandler&lt;DragEventArgs> DragStarted;
```

#### Event Type
[System.EventHandler&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')[DragEventArgs](Tizen.UI.DragEventArgs.md 'Tizen.UI.DragEventArgs')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')

<a name='Tizen.UI.IScrollable.ScrollFinished'></a>

## IScrollable.ScrollFinished Event

Occurs when the scroll finishes.

```csharp
event EventHandler&lt;ScrollEventArgs> ScrollFinished;
```

#### Event Type
[System.EventHandler&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')[ScrollEventArgs](Tizen.UI.ScrollEventArgs.md 'Tizen.UI.ScrollEventArgs')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')

<a name='Tizen.UI.IScrollable.Scrolling'></a>

## IScrollable.Scrolling Event

Occurs while scrolling.

```csharp
event EventHandler&lt;ScrollEventArgs> Scrolling;
```

#### Event Type
[System.EventHandler&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')[ScrollEventArgs](Tizen.UI.ScrollEventArgs.md 'Tizen.UI.ScrollEventArgs')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')

<a name='Tizen.UI.IScrollable.ScrollStarted'></a>

## IScrollable.ScrollStarted Event

Occurs when the scroll starts.

```csharp
event EventHandler&lt;ScrollEventArgs> ScrollStarted;
```

#### Event Type
[System.EventHandler&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')[ScrollEventArgs](Tizen.UI.ScrollEventArgs.md 'Tizen.UI.ScrollEventArgs')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')




