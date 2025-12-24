### [Tizen.UI.Components.Material](Tizen.UI.Components.Material.md 'Tizen.UI.Components.Material')

## IPager Interface

A Pager interface.

```csharp
public interface IPager
```

Derived  
&#8627; [PageScroller](Tizen.UI.Components.Material.PageScroller.md 'Tizen.UI.Components.Material.PageScroller')
### Properties

<a name='Tizen.UI.Components.Material.IPager.CurrentPage'></a>

## IPager.CurrentPage Property

Gets sets the current page.

```csharp
int CurrentPage { get; }
```

#### Property Value
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

<a name='Tizen.UI.Components.Material.IPager.PageAdapter'></a>

## IPager.PageAdapter Property

Adapter who connects pager and indicator.

```csharp
Tizen.UI.Components.Material.PageAdapter PageAdapter { get; set; }
```

#### Property Value
[PageAdapter](Tizen.UI.Components.Material.PageAdapter.md 'Tizen.UI.Components.Material.PageAdapter')

<a name='Tizen.UI.Components.Material.IPager.PageCount'></a>

## IPager.PageCount Property

Gets sets the page count.

```csharp
int PageCount { get; }
```

#### Property Value
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

<a name='Tizen.UI.Components.Material.IPager.this[int]'></a>

## IPager.this[int] Property

Gets sets the page on index.

```csharp
Tizen.UI.View this[int index] { get; }
```
#### Parameters

<a name='Tizen.UI.Components.Material.IPager.this[int].index'></a>

`index` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

#### Property Value
[Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')
### Methods

<a name='Tizen.UI.Components.Material.IPager.ShowPage(int,bool)'></a>

## IPager.ShowPage(int, bool) Method

Show page in pager.

```csharp
System.Threading.Tasks.Task ShowPage(int pageIndex, bool animation);
```
#### Parameters

<a name='Tizen.UI.Components.Material.IPager.ShowPage(int,bool).pageIndex'></a>

`pageIndex` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The page index to be shown.

<a name='Tizen.UI.Components.Material.IPager.ShowPage(int,bool).animation'></a>

`animation` [System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

Whether to play an animation.

#### Returns
[System.Threading.Tasks.Task](https://docs.microsoft.com/en-us/dotnet/api/System.Threading.Tasks.Task 'System.Threading.Tasks.Task')  
the visual object.













































