### [Tizen.UI.Components.Material](Tizen.UI.Components.Material.md 'Tizen.UI.Components.Material')

## PageIndicator Class

A Page indicator component.

```csharp
public class PageIndicator : Tizen.UI.ContentView,
Tizen.UI.Components.Material.IPageIndicator
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; Tizen.UI.NObject &#129106; Tizen.UI.View &#129106; Tizen.UI.ContentView &#129106; PageIndicator

Implements [IPageIndicator](Tizen.UI.Components.Material.IPageIndicator.md 'Tizen.UI.Components.Material.IPageIndicator')
### Constructors

<a name='Tizen.UI.Components.Material.PageIndicator.PageIndicator()'></a>

## PageIndicator() Constructor

Constructs a page indicator.

```csharp
public PageIndicator();
```

<a name='Tizen.UI.Components.Material.PageIndicator.PageIndicator(Tizen.UI.Components.Material.PageIndicatorVariables)'></a>

## PageIndicator(PageIndicatorVariables) Constructor

Constructs a page indicator with variables

```csharp
public PageIndicator(Tizen.UI.Components.Material.PageIndicatorVariables variables);
```
#### Parameters

<a name='Tizen.UI.Components.Material.PageIndicator.PageIndicator(Tizen.UI.Components.Material.PageIndicatorVariables).variables'></a>

`variables` [PageIndicatorVariables](Tizen.UI.Components.Material.PageIndicatorVariables.md 'Tizen.UI.Components.Material.PageIndicatorVariables')
### Properties

<a name='Tizen.UI.Components.Material.PageIndicator.CurrentPage'></a>

## PageIndicator.CurrentPage Property

Gets sets the current page.

```csharp
public int CurrentPage { get; set; }
```

Implements [CurrentPage](Tizen.UI.Components.Material.IPageIndicator.md#Tizen.UI.Components.Material.IPageIndicator.CurrentPage 'Tizen.UI.Components.Material.IPageIndicator.CurrentPage')

#### Property Value
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

<a name='Tizen.UI.Components.Material.PageIndicator.PageAdapter'></a>

## PageIndicator.PageAdapter Property

Adapter who connects pager and indicator.

```csharp
public Tizen.UI.Components.Material.PageAdapter PageAdapter { get; set; }
```

Implements [PageAdapter](Tizen.UI.Components.Material.IPageIndicator.md#Tizen.UI.Components.Material.IPageIndicator.PageAdapter 'Tizen.UI.Components.Material.IPageIndicator.PageAdapter')

#### Property Value
[PageAdapter](Tizen.UI.Components.Material.PageAdapter.md 'Tizen.UI.Components.Material.PageAdapter')

<a name='Tizen.UI.Components.Material.PageIndicator.PageCount'></a>

## PageIndicator.PageCount Property

Gets sets the page count.

```csharp
public int PageCount { get; }
```

Implements [PageCount](Tizen.UI.Components.Material.IPageIndicator.md#Tizen.UI.Components.Material.IPageIndicator.PageCount 'Tizen.UI.Components.Material.IPageIndicator.PageCount')

#### Property Value
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

<a name='Tizen.UI.Components.Material.PageIndicator.PageDotTemplate'></a>

## PageIndicator.PageDotTemplate Property

View template of page dot.  
If view implments ISelectable, Select state will be updated on the view,  
when the indexed page are changed.

```csharp
public Tizen.UI.ViewTemplate PageDotTemplate { get; set; }
```

#### Property Value
Tizen.UI.ViewTemplate

<a name='Tizen.UI.Components.Material.PageIndicator.Spacing'></a>

## PageIndicator.Spacing Property

Gets or sets the spacing between the indicator dots.

```csharp
public float Spacing { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Components.Material.PageIndicator.this[int]'></a>

## PageIndicator.this[int] Property

Gets a content view with index.

```csharp
public Tizen.UI.View this[int index] { get; set; }
```
#### Parameters

<a name='Tizen.UI.Components.Material.PageIndicator.this[int].index'></a>

`index` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

#### Property Value
Tizen.UI.View
### Methods

<a name='Tizen.UI.Components.Material.PageIndicator.AddPage(int)'></a>

## PageIndicator.AddPage(int) Method

Add page at the end.

```csharp
public void AddPage(int index);
```
#### Parameters

<a name='Tizen.UI.Components.Material.PageIndicator.AddPage(int).index'></a>

`index` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

Implements [AddPage(int)](Tizen.UI.Components.Material.IPageIndicator.md#Tizen.UI.Components.Material.IPageIndicator.AddPage(int) 'Tizen.UI.Components.Material.IPageIndicator.AddPage(int)')

<a name='Tizen.UI.Components.Material.PageIndicator.RemovePage(int)'></a>

## PageIndicator.RemovePage(int) Method

Remove page.

```csharp
public void RemovePage(int pageIndex);
```
#### Parameters

<a name='Tizen.UI.Components.Material.PageIndicator.RemovePage(int).pageIndex'></a>

`pageIndex` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The removing page index.

Implements [RemovePage(int)](Tizen.UI.Components.Material.IPageIndicator.md#Tizen.UI.Components.Material.IPageIndicator.RemovePage(int) 'Tizen.UI.Components.Material.IPageIndicator.RemovePage(int)')














































