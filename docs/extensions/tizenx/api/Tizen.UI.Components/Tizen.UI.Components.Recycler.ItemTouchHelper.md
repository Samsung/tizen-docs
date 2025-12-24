### [Tizen.UI.Components.Recycler](Tizen.UI.Components.Recycler.md 'Tizen.UI.Components.Recycler')

## ItemTouchHelper Class

Item touch helper for [RecyclerView](Tizen.UI.Components.Recycler.RecyclerView.md 'Tizen.UI.Components.Recycler.RecyclerView').  
This is a utility class to add touch action support to [RecyclerView](Tizen.UI.Components.Recycler.RecyclerView.md 'Tizen.UI.Components.Recycler.RecyclerView')..  
It works with a [RecyclerView](Tizen.UI.Components.Recycler.RecyclerView.md 'Tizen.UI.Components.Recycler.RecyclerView'). and a [ItemTouchHelperCallback](Tizen.UI.Components.Recycler.ItemTouchHelperCallback.md 'Tizen.UI.Components.Recycler.ItemTouchHelperCallback'). class, which configures what type of interactions  
are enabled and also receives events when user performs these actions.  
Depending on which functionality you support, you should override methods in [ItemTouchHelperCallback](Tizen.UI.Components.Recycler.ItemTouchHelperCallback.md 'Tizen.UI.Components.Recycler.ItemTouchHelperCallback').

```csharp
public class ItemTouchHelper :
Tizen.UI.Components.Recycler.IItemDecoration
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; ItemTouchHelper

Implements [IItemDecoration](Tizen.UI.Components.Recycler.IItemDecoration.md 'Tizen.UI.Components.Recycler.IItemDecoration')
### Constructors

<a name='Tizen.UI.Components.Recycler.ItemTouchHelper.ItemTouchHelper(Tizen.UI.Components.Recycler.ItemTouchHelperCallback)'></a>

## ItemTouchHelper(ItemTouchHelperCallback) Constructor

Creates an ItemTouchHelper that will work with the given [ItemTouchHelperCallback](Tizen.UI.Components.Recycler.ItemTouchHelperCallback.md 'Tizen.UI.Components.Recycler.ItemTouchHelperCallback').

```csharp
public ItemTouchHelper(Tizen.UI.Components.Recycler.ItemTouchHelperCallback callback);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.ItemTouchHelper.ItemTouchHelper(Tizen.UI.Components.Recycler.ItemTouchHelperCallback).callback'></a>

`callback` [ItemTouchHelperCallback](Tizen.UI.Components.Recycler.ItemTouchHelperCallback.md 'Tizen.UI.Components.Recycler.ItemTouchHelperCallback')
### Methods

<a name='Tizen.UI.Components.Recycler.ItemTouchHelper.AttachToRecyclerView(Tizen.UI.Components.Recycler.RecyclerView)'></a>

## ItemTouchHelper.AttachToRecyclerView(RecyclerView) Method

Attach the touch helper to RecyclerView.

```csharp
public void AttachToRecyclerView(Tizen.UI.Components.Recycler.RecyclerView view);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.ItemTouchHelper.AttachToRecyclerView(Tizen.UI.Components.Recycler.RecyclerView).view'></a>

`view` [RecyclerView](Tizen.UI.Components.Recycler.RecyclerView.md 'Tizen.UI.Components.Recycler.RecyclerView')

The recycler view.

<a name='Tizen.UI.Components.Recycler.ItemTouchHelper.DetachToRecyclerView()'></a>

## ItemTouchHelper.DetachToRecyclerView() Method

Detach the touch helper to RecyclerView.

```csharp
public void DetachToRecyclerView();
```

<a name='Tizen.UI.Components.Recycler.ItemTouchHelper.GetItemOffsets(Tizen.UI.View,int,Tizen.UI.Components.Recycler.RecyclerView)'></a>

## ItemTouchHelper.GetItemOffsets(View, int, RecyclerView) Method

Get item offsets. The method to get the item offsets. It is called when the item view is laid out.

```csharp
public Tizen.UI.Thickness GetItemOffsets(Tizen.UI.View view, int position, Tizen.UI.Components.Recycler.RecyclerView recyclerView);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.ItemTouchHelper.GetItemOffsets(Tizen.UI.View,int,Tizen.UI.Components.Recycler.RecyclerView).view'></a>

`view` [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')

The view to retrieve the offset from.

<a name='Tizen.UI.Components.Recycler.ItemTouchHelper.GetItemOffsets(Tizen.UI.View,int,Tizen.UI.Components.Recycler.RecyclerView).position'></a>

`position` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The position

<a name='Tizen.UI.Components.Recycler.ItemTouchHelper.GetItemOffsets(Tizen.UI.View,int,Tizen.UI.Components.Recycler.RecyclerView).recyclerView'></a>

`recyclerView` [RecyclerView](Tizen.UI.Components.Recycler.RecyclerView.md 'Tizen.UI.Components.Recycler.RecyclerView')

The recyclerView

Implements [GetItemOffsets(View, int, RecyclerView)](Tizen.UI.Components.Recycler.IItemDecoration.md#Tizen.UI.Components.Recycler.IItemDecoration.GetItemOffsets(Tizen.UI.View,int,Tizen.UI.Components.Recycler.RecyclerView) 'Tizen.UI.Components.Recycler.IItemDecoration.GetItemOffsets(Tizen.UI.View, int, Tizen.UI.Components.Recycler.RecyclerView)')

#### Returns
[Tizen.UI.Thickness](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Thickness 'Tizen.UI.Thickness')  
The extra drawing space for the item view.

<a name='Tizen.UI.Components.Recycler.ItemTouchHelper.StartDrag(Tizen.UI.Components.Recycler.ViewHolder)'></a>

## ItemTouchHelper.StartDrag(ViewHolder) Method

Let the Viewholder start the drag action by force.

```csharp
public void StartDrag(Tizen.UI.Components.Recycler.ViewHolder viewHolder);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.ItemTouchHelper.StartDrag(Tizen.UI.Components.Recycler.ViewHolder).viewHolder'></a>

`viewHolder` [ViewHolder](Tizen.UI.Components.Recycler.ViewHolder.md 'Tizen.UI.Components.Recycler.ViewHolder')

The view holder for drag.


























































