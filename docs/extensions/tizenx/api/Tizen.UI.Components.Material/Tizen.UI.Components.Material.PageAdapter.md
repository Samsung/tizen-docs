### [Tizen.UI.Components.Material](Tizen.UI.Components.Material.md 'Tizen.UI.Components.Material')

## PageAdapter Class

A Page adapter who connects pager and indicator.

```csharp
public class PageAdapter
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; PageAdapter
### Properties

<a name='Tizen.UI.Components.Material.PageAdapter.PageIndicator'></a>

## PageAdapter.PageIndicator Property

Indicator of page.

```csharp
public Tizen.UI.Components.Material.IPageIndicator PageIndicator { get; set; }
```

#### Property Value
[IPageIndicator](Tizen.UI.Components.Material.IPageIndicator.md 'Tizen.UI.Components.Material.IPageIndicator')

<a name='Tizen.UI.Components.Material.PageAdapter.Pager'></a>

## PageAdapter.Pager Property

Pager.

```csharp
public Tizen.UI.Components.Material.IPager Pager { get; set; }
```

#### Property Value
[IPager](Tizen.UI.Components.Material.IPager.md 'Tizen.UI.Components.Material.IPager')
### Methods

<a name='Tizen.UI.Components.Material.PageAdapter.AddPage(Tizen.UI.View,int)'></a>

## PageAdapter.AddPage(View, int) Method

Add page in indicator

```csharp
public void AddPage(Tizen.UI.View page, int index);
```
#### Parameters

<a name='Tizen.UI.Components.Material.PageAdapter.AddPage(Tizen.UI.View,int).page'></a>

`page` Tizen.UI.View

<a name='Tizen.UI.Components.Material.PageAdapter.AddPage(Tizen.UI.View,int).index'></a>

`index` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

<a name='Tizen.UI.Components.Material.PageAdapter.OnPageChanged(int)'></a>

## PageAdapter.OnPageChanged(int) Method

Notify page changed.

```csharp
public virtual void OnPageChanged(int pageIndex);
```
#### Parameters

<a name='Tizen.UI.Components.Material.PageAdapter.OnPageChanged(int).pageIndex'></a>

`pageIndex` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The page index to be shown.

<a name='Tizen.UI.Components.Material.PageAdapter.RemovePage(Tizen.UI.View)'></a>

## PageAdapter.RemovePage(View) Method

Remove page in indicator

```csharp
public void RemovePage(Tizen.UI.View page);
```
#### Parameters

<a name='Tizen.UI.Components.Material.PageAdapter.RemovePage(Tizen.UI.View).page'></a>

`page` Tizen.UI.View

The added page.













































