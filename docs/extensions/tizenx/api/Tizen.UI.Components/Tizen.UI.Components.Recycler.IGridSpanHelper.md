### [Tizen.UI.Components.Recycler](Tizen.UI.Components.Recycler.md 'Tizen.UI.Components.Recycler')

## IGridSpanHelper Interface

[GridView](https://docs.microsoft.com/en-us/dotnet/api/GridView 'GridView') span helper interface. It provides additional information about item's span.

```csharp
public interface IGridSpanHelper :
Tizen.UI.Components.Recycler.IItemDecoration
```

Implements [IItemDecoration](Tizen.UI.Components.Recycler.IItemDecoration.md 'Tizen.UI.Components.Recycler.IItemDecoration')
### Methods

<a name='Tizen.UI.Components.Recycler.IGridSpanHelper.GetSpanIndex(int,Tizen.UI.Components.Recycler.RecyclerView)'></a>

## IGridSpanHelper.GetSpanIndex(int, RecyclerView) Method

Gets the span index of the item at the given position. The span index indicates which span of the grid the item is placed in.  
By default, items are placed starting from the leftmost span. Implement this method to customize the span index of items.

```csharp
int GetSpanIndex(int position, Tizen.UI.Components.Recycler.RecyclerView recyclerView);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.IGridSpanHelper.GetSpanIndex(int,Tizen.UI.Components.Recycler.RecyclerView).position'></a>

`position` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

<a name='Tizen.UI.Components.Recycler.IGridSpanHelper.GetSpanIndex(int,Tizen.UI.Components.Recycler.RecyclerView).recyclerView'></a>

`recyclerView` [RecyclerView](Tizen.UI.Components.Recycler.RecyclerView.md 'Tizen.UI.Components.Recycler.RecyclerView')

#### Returns
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')  
The span index. if value is negative, index will be default value.

<a name='Tizen.UI.Components.Recycler.IGridSpanHelper.GetSpanSize(int,Tizen.UI.Components.Recycler.RecyclerView)'></a>

## IGridSpanHelper.GetSpanSize(int, RecyclerView) Method

Gets the span size of the item at the given position. The span size determines how many spans of the grid the item will occupy.  
By default, each item occupies one span. Implement this method to customize the span size of items.

```csharp
uint GetSpanSize(int position, Tizen.UI.Components.Recycler.RecyclerView recyclerView);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.IGridSpanHelper.GetSpanSize(int,Tizen.UI.Components.Recycler.RecyclerView).position'></a>

`position` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The index poisition of item.

<a name='Tizen.UI.Components.Recycler.IGridSpanHelper.GetSpanSize(int,Tizen.UI.Components.Recycler.RecyclerView).recyclerView'></a>

`recyclerView` [RecyclerView](Tizen.UI.Components.Recycler.RecyclerView.md 'Tizen.UI.Components.Recycler.RecyclerView')

#### Returns
[System.UInt32](https://docs.microsoft.com/en-us/dotnet/api/System.UInt32 'System.UInt32')  
The span size.


























































