### [Tizen.UI.Components.Material](Tizen.UI.Components.Material.md 'Tizen.UI.Components.Material')

## IPageIndicator Interface

A Page indicator interface.

```csharp
public interface IPageIndicator
```

Derived  
&#8627; [PageIndicator](Tizen.UI.Components.Material.PageIndicator.md 'Tizen.UI.Components.Material.PageIndicator')
### Properties

<a name='Tizen.UI.Components.Material.IPageIndicator.CurrentPage'></a>

## IPageIndicator.CurrentPage Property

Gets sets the current page.

```csharp
int CurrentPage { get; set; }
```

#### Property Value
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

<a name='Tizen.UI.Components.Material.IPageIndicator.PageAdapter'></a>

## IPageIndicator.PageAdapter Property

Adapter who connects pager and indicator.

```csharp
Tizen.UI.Components.Material.PageAdapter PageAdapter { get; set; }
```

#### Property Value
[PageAdapter](Tizen.UI.Components.Material.PageAdapter.md 'Tizen.UI.Components.Material.PageAdapter')

<a name='Tizen.UI.Components.Material.IPageIndicator.PageCount'></a>

## IPageIndicator.PageCount Property

Gets sets the page count.

```csharp
int PageCount { get; }
```

#### Property Value
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')
### Methods

<a name='Tizen.UI.Components.Material.IPageIndicator.AddPage(int)'></a>

## IPageIndicator.AddPage(int) Method

Add page at the end.

```csharp
void AddPage(int pageIndex);
```
#### Parameters

<a name='Tizen.UI.Components.Material.IPageIndicator.AddPage(int).pageIndex'></a>

`pageIndex` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The adding page index.

<a name='Tizen.UI.Components.Material.IPageIndicator.RemovePage(int)'></a>

## IPageIndicator.RemovePage(int) Method

Remove page.

```csharp
void RemovePage(int pageIndex);
```
#### Parameters

<a name='Tizen.UI.Components.Material.IPageIndicator.RemovePage(int).pageIndex'></a>

`pageIndex` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The removing page index.













































