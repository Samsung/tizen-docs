### [Tizen.UI.Components](Tizen.UI.Components.md 'Tizen.UI.Components')

## ScrollBarBase Class

A base class representing a scroll bar that can be used to control the scrolling of a view.

```csharp
public class ScrollBarBase : Tizen.UI.ViewGroup,
Tizen.UI.IScrollBar,
System.IDisposable
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [Tizen.UI.NObject](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.NObject 'Tizen.UI.NObject') &#129106; [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View') &#129106; [Tizen.UI.ViewGroup](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.ViewGroup 'Tizen.UI.ViewGroup') &#129106; ScrollBarBase

Implements [Tizen.UI.IScrollBar](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.IScrollBar 'Tizen.UI.IScrollBar'), [System.IDisposable](https://docs.microsoft.com/en-us/dotnet/api/System.IDisposable 'System.IDisposable')
### Constructors

<a name='Tizen.UI.Components.ScrollBarBase.ScrollBarBase()'></a>

## ScrollBarBase() Constructor

Initializes a new instance of the [Tizen.UI.Layouts.ScrollBar](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Layouts.ScrollBar 'Tizen.UI.Layouts.ScrollBar') class.

```csharp
public ScrollBarBase();
```
### Properties

<a name='Tizen.UI.Components.ScrollBarBase.BarColor'></a>

## ScrollBarBase.BarColor Property

Gets or sets the color of the scroll bar.

```csharp
public Tizen.UI.Color BarColor { get; set; }
```

#### Property Value
[Tizen.UI.Color](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Color 'Tizen.UI.Color')

<a name='Tizen.UI.Components.ScrollBarBase.BarCornerRadius'></a>

## ScrollBarBase.BarCornerRadius Property

Gets or sets the corner of the scroll bar.

```csharp
public Tizen.UI.CornerRadius BarCornerRadius { get; set; }
```

#### Property Value
[Tizen.UI.CornerRadius](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.CornerRadius 'Tizen.UI.CornerRadius')

<a name='Tizen.UI.Components.ScrollBarBase.BarMargin'></a>

## ScrollBarBase.BarMargin Property

Gets or sets the margin between the scroll bar and its target view.

```csharp
public Tizen.UI.Thickness BarMargin { get; set; }
```

#### Property Value
[Tizen.UI.Thickness](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Thickness 'Tizen.UI.Thickness')

<a name='Tizen.UI.Components.ScrollBarBase.BarMinSize'></a>

## ScrollBarBase.BarMinSize Property

Gets or sets the minimum size of the scroll bar.

```csharp
public float BarMinSize { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Components.ScrollBarBase.BarShadow'></a>

## ScrollBarBase.BarShadow Property

Gets or sets the shadow of scroll bar.

```csharp
public Tizen.UI.Shadow BarShadow { get; set; }
```

#### Property Value
[Tizen.UI.Shadow](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Shadow 'Tizen.UI.Shadow')

<a name='Tizen.UI.Components.ScrollBarBase.BarThickness'></a>

## ScrollBarBase.BarThickness Property

Gets or sets the thickness of the scroll bar.

```csharp
public float BarThickness { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Components.ScrollBarBase.HorizontalScrollBarVisibility'></a>

## ScrollBarBase.HorizontalScrollBarVisibility Property

Gets or sets the visibility of the horizontal scroll bar.

```csharp
public Tizen.UI.ScrollBarVisibility HorizontalScrollBarVisibility { get; set; }
```

Implements [HorizontalScrollBarVisibility](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.IScrollBar.HorizontalScrollBarVisibility 'Tizen.UI.IScrollBar.HorizontalScrollBarVisibility')

#### Property Value
[Tizen.UI.ScrollBarVisibility](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.ScrollBarVisibility 'Tizen.UI.ScrollBarVisibility')

<a name='Tizen.UI.Components.ScrollBarBase.ScrollPosition'></a>

## ScrollBarBase.ScrollPosition Property

Gets or sets the current scroll position of the target view.

```csharp
public Tizen.UI.Point ScrollPosition { get; set; }
```

#### Property Value
[Tizen.UI.Point](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Point 'Tizen.UI.Point')

<a name='Tizen.UI.Components.ScrollBarBase.Target'></a>

## ScrollBarBase.Target Property

Gets the target view of the scroll bar.

```csharp
public Tizen.UI.View Target { get; }
```

Implements [Target](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.IScrollBar.Target 'Tizen.UI.IScrollBar.Target')

#### Property Value
[Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')

<a name='Tizen.UI.Components.ScrollBarBase.VerticalScrollBarVisibility'></a>

## ScrollBarBase.VerticalScrollBarVisibility Property

Gets or sets the visibility of the vertical scroll bar.

```csharp
public Tizen.UI.ScrollBarVisibility VerticalScrollBarVisibility { get; set; }
```

Implements [VerticalScrollBarVisibility](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.IScrollBar.VerticalScrollBarVisibility 'Tizen.UI.IScrollBar.VerticalScrollBarVisibility')

#### Property Value
[Tizen.UI.ScrollBarVisibility](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.ScrollBarVisibility 'Tizen.UI.ScrollBarVisibility')
### Methods

<a name='Tizen.UI.Components.ScrollBarBase.UpdateBarSize(Tizen.UI.Size,Tizen.UI.Size)'></a>

## ScrollBarBase.UpdateBarSize(Size, Size) Method

Updates the size of the scroll bar based on the current scroll area and view port size.

```csharp
public virtual void UpdateBarSize(Tizen.UI.Size scrollArea, Tizen.UI.Size viewportSize);
```
#### Parameters

<a name='Tizen.UI.Components.ScrollBarBase.UpdateBarSize(Tizen.UI.Size,Tizen.UI.Size).scrollArea'></a>

`scrollArea` [Tizen.UI.Size](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Size 'Tizen.UI.Size')

The size of the scrollable area.

<a name='Tizen.UI.Components.ScrollBarBase.UpdateBarSize(Tizen.UI.Size,Tizen.UI.Size).viewportSize'></a>

`viewportSize` [Tizen.UI.Size](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Size 'Tizen.UI.Size')

The size of the view port.

Implements [UpdateBarSize(Size, Size)](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.IScrollBar.UpdateBarSize#Tizen_UI_IScrollBar_UpdateBarSize_Tizen_UI_Size,Tizen_UI_Size_ 'Tizen.UI.IScrollBar.UpdateBarSize(Tizen.UI.Size,Tizen.UI.Size)')

<a name='Tizen.UI.Components.ScrollBarBase.UpdateScrollPosition(Tizen.UI.Point)'></a>

## ScrollBarBase.UpdateScrollPosition(Point) Method

Updates the scroll position of the target view.

```csharp
public virtual void UpdateScrollPosition(Tizen.UI.Point position);
```
#### Parameters

<a name='Tizen.UI.Components.ScrollBarBase.UpdateScrollPosition(Tizen.UI.Point).position'></a>

`position` [Tizen.UI.Point](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Point 'Tizen.UI.Point')

The new scroll position.

Implements [UpdateScrollPosition(Point)](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.IScrollBar.UpdateScrollPosition#Tizen_UI_IScrollBar_UpdateScrollPosition_Tizen_UI_Point_ 'Tizen.UI.IScrollBar.UpdateScrollPosition(Tizen.UI.Point)')
### Explicit Interface Implementations

<a name='Tizen.UI.Components.ScrollBarBase.Tizen.UI.IScrollBar.OnAttachedToScrollable(Tizen.UI.IScrollable)'></a>

## ScrollBarBase.Tizen.UI.IScrollBar.OnAttachedToScrollable(IScrollable) Method

Call when [Tizen.UI.IScrollable](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.IScrollable 'Tizen.UI.IScrollable') is attached to the ScrollBar.

```csharp
void Tizen.UI.IScrollBar.OnAttachedToScrollable(Tizen.UI.IScrollable scrollable);
```
#### Parameters

<a name='Tizen.UI.Components.ScrollBarBase.Tizen.UI.IScrollBar.OnAttachedToScrollable(Tizen.UI.IScrollable).scrollable'></a>

`scrollable` [Tizen.UI.IScrollable](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.IScrollable 'Tizen.UI.IScrollable')

The scrollable.

Implements [OnAttachedToScrollable(IScrollable)](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.IScrollBar.OnAttachedToScrollable#Tizen_UI_IScrollBar_OnAttachedToScrollable_Tizen_UI_IScrollable_ 'Tizen.UI.IScrollBar.OnAttachedToScrollable(Tizen.UI.IScrollable)')


























































