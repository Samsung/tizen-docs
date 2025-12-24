### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## IScrollBar Interface

Defines the interface for a scroll bar, which is responsible for displaying and controlling the scrolling of a target view.

```csharp
public interface IScrollBar :
System.IDisposable
```

Implements [System.IDisposable](https://docs.microsoft.com/en-us/dotnet/api/System.IDisposable 'System.IDisposable')
### Properties

<a name='Tizen.UI.IScrollBar.HorizontalScrollBarVisibility'></a>

## IScrollBar.HorizontalScrollBarVisibility Property

Gets or sets the visibility of the horizontal scroll bar.

```csharp
Tizen.UI.ScrollBarVisibility HorizontalScrollBarVisibility { get; set; }
```

#### Property Value
[ScrollBarVisibility](Tizen.UI.ScrollBarVisibility.md 'Tizen.UI.ScrollBarVisibility')

<a name='Tizen.UI.IScrollBar.Target'></a>

## IScrollBar.Target Property

Gets the target view for which the scroll bar is responsible.

```csharp
Tizen.UI.View Target { get; }
```

#### Property Value
[View](Tizen.UI.View.md 'Tizen.UI.View')

<a name='Tizen.UI.IScrollBar.VerticalScrollBarVisibility'></a>

## IScrollBar.VerticalScrollBarVisibility Property

Gets or sets the visibility of the vertical scroll bar.

```csharp
Tizen.UI.ScrollBarVisibility VerticalScrollBarVisibility { get; set; }
```

#### Property Value
[ScrollBarVisibility](Tizen.UI.ScrollBarVisibility.md 'Tizen.UI.ScrollBarVisibility')
### Methods

<a name='Tizen.UI.IScrollBar.OnAttachedToScrollable(Tizen.UI.IScrollable)'></a>

## IScrollBar.OnAttachedToScrollable(IScrollable) Method

Call when [IScrollable](Tizen.UI.IScrollable.md 'Tizen.UI.IScrollable') is attached to the ScrollBar.

```csharp
void OnAttachedToScrollable(Tizen.UI.IScrollable scrollable);
```
#### Parameters

<a name='Tizen.UI.IScrollBar.OnAttachedToScrollable(Tizen.UI.IScrollable).scrollable'></a>

`scrollable` [IScrollable](Tizen.UI.IScrollable.md 'Tizen.UI.IScrollable')

The scrollable.

<a name='Tizen.UI.IScrollBar.UpdateBarSize(Tizen.UI.Size,Tizen.UI.Size)'></a>

## IScrollBar.UpdateBarSize(Size, Size) Method

Updates the size of the scroll bar based on the given scroll area and viewport size.

```csharp
void UpdateBarSize(Tizen.UI.Size scrollArea, Tizen.UI.Size viewportSize);
```
#### Parameters

<a name='Tizen.UI.IScrollBar.UpdateBarSize(Tizen.UI.Size,Tizen.UI.Size).scrollArea'></a>

`scrollArea` [Size](Tizen.UI.Size.md 'Tizen.UI.Size')

The size of the scrollable area.

<a name='Tizen.UI.IScrollBar.UpdateBarSize(Tizen.UI.Size,Tizen.UI.Size).viewportSize'></a>

`viewportSize` [Size](Tizen.UI.Size.md 'Tizen.UI.Size')

The size of the view port.

<a name='Tizen.UI.IScrollBar.UpdateScrollPosition(Tizen.UI.Point)'></a>

## IScrollBar.UpdateScrollPosition(Point) Method

Updates the scroll position of the scroll bar based on the given position.

```csharp
void UpdateScrollPosition(Tizen.UI.Point position);
```
#### Parameters

<a name='Tizen.UI.IScrollBar.UpdateScrollPosition(Tizen.UI.Point).position'></a>

`position` [Point](Tizen.UI.Point.md 'Tizen.UI.Point')

The new scroll position.




