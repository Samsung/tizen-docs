### [Tizen.UI.Components.Recycler](Tizen.UI.Components.Recycler.md 'Tizen.UI.Components.Recycler')

## IItemDecoration Interface

Interface for item decoration. It provides additional information about item's position

```csharp
public interface IItemDecoration
```

Derived  
&#8627; [IGridRelativeSizeHelper](Tizen.UI.Components.Recycler.IGridRelativeSizeHelper.md 'Tizen.UI.Components.Recycler.IGridRelativeSizeHelper')  
&#8627; [IGridSpanHelper](Tizen.UI.Components.Recycler.IGridSpanHelper.md 'Tizen.UI.Components.Recycler.IGridSpanHelper')  
&#8627; [ItemTouchHelper](Tizen.UI.Components.Recycler.ItemTouchHelper.md 'Tizen.UI.Components.Recycler.ItemTouchHelper')
### Methods

<a name='Tizen.UI.Components.Recycler.IItemDecoration.GetItemOffsets(Tizen.UI.View,int,Tizen.UI.Components.Recycler.RecyclerView)'></a>

## IItemDecoration.GetItemOffsets(View, int, RecyclerView) Method

Get item offsets. The method to get the item offsets. It is called when the item view is laid out.

```csharp
Tizen.UI.Thickness GetItemOffsets(Tizen.UI.View view, int position, Tizen.UI.Components.Recycler.RecyclerView recyclerView);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.IItemDecoration.GetItemOffsets(Tizen.UI.View,int,Tizen.UI.Components.Recycler.RecyclerView).view'></a>

`view` Tizen.UI.View

The view to retrieve the offset from.

<a name='Tizen.UI.Components.Recycler.IItemDecoration.GetItemOffsets(Tizen.UI.View,int,Tizen.UI.Components.Recycler.RecyclerView).position'></a>

`position` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The position

<a name='Tizen.UI.Components.Recycler.IItemDecoration.GetItemOffsets(Tizen.UI.View,int,Tizen.UI.Components.Recycler.RecyclerView).recyclerView'></a>

`recyclerView` [RecyclerView](Tizen.UI.Components.Recycler.RecyclerView.md 'Tizen.UI.Components.Recycler.RecyclerView')

The recyclerView

#### Returns
Tizen.UI.Thickness  
The extra drawing space for the item view.



























































