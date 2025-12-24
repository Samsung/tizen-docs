### [Tizen.UI.Components.Recycler](Tizen.UI.Components.Recycler.md 'Tizen.UI.Components.Recycler')

## ItemTouchHelperCallback Class

This class is the contract between ItemTouchHelper and your application. It lets you control  
which touch behaviors are enabled per each ViewHolder and also receive callbacks when user performs these actions.  
o control which actions user can take on each view, you should override  
[GetMovementPolicy(RecyclerView, ViewHolder)](Tizen.UI.Components.Recycler.ItemTouchHelperCallback.md#Tizen.UI.Components.Recycler.ItemTouchHelperCallback.GetMovementPolicy(Tizen.UI.Components.Recycler.RecyclerView,Tizen.UI.Components.Recycler.ViewHolder) 'Tizen.UI.Components.Recycler.ItemTouchHelperCallback.GetMovementPolicy(Tizen.UI.Components.Recycler.RecyclerView, Tizen.UI.Components.Recycler.ViewHolder)') and return appropriate set of direction flags.

```csharp
public abstract class ItemTouchHelperCallback
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; ItemTouchHelperCallback

Derived  
&#8627; [LinearSwapCallback](Tizen.UI.Components.Recycler.LinearSwapCallback.md 'Tizen.UI.Components.Recycler.LinearSwapCallback')
### Properties

<a name='Tizen.UI.Components.Recycler.ItemTouchHelperCallback.BoundingBoxMargin'></a>

## ItemTouchHelperCallback.BoundingBoxMargin Property

When finding views under a dragged view, by default, ItemTouchHelper searches for views That overlap with the dragged View.  
By set this value, you can extend or shrink the search box. default is 0.

```csharp
public float BoundingBoxMargin { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Components.Recycler.ItemTouchHelperCallback.IsLongpressDragEnabled'></a>

## ItemTouchHelperCallback.IsLongpressDragEnabled Property

whether ItemTouchHelper should start a drag and drop operation if an item is long pressed.  
default is true.

```csharp
public bool IsLongpressDragEnabled { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')
### Methods

<a name='Tizen.UI.Components.Recycler.ItemTouchHelperCallback.CanDropOver(Tizen.UI.Components.Recycler.RecyclerView,Tizen.UI.Components.Recycler.ViewHolder,Tizen.UI.Components.Recycler.ViewHolder)'></a>

## ItemTouchHelperCallback.CanDropOver(RecyclerView, ViewHolder, ViewHolder) Method

Return true if the current ViewHolder can be dropped over the the target ViewHolder.  
This method is used when selecting drop target for the dragged View.  
After Views are eliminated either via bounds check or via this method,  
resulting set of views will be passed to [ChooseDropTarget(ViewHolder, List&lt;ViewHolder&gt;, Point)](Tizen.UI.Components.Recycler.ItemTouchHelperCallback.md#Tizen.UI.Components.Recycler.ItemTouchHelperCallback.ChooseDropTarget(Tizen.UI.Components.Recycler.ViewHolder,System.Collections.Generic.List_Tizen.UI.Components.Recycler.ViewHolder_,Tizen.UI.Point) 'Tizen.UI.Components.Recycler.ItemTouchHelperCallback.ChooseDropTarget(Tizen.UI.Components.Recycler.ViewHolder, System.Collections.Generic.List&lt;Tizen.UI.Components.Recycler.ViewHolder>, Tizen.UI.Point)').  
Default implementation returns true.

```csharp
public virtual bool CanDropOver(Tizen.UI.Components.Recycler.RecyclerView recyclerView, Tizen.UI.Components.Recycler.ViewHolder current, Tizen.UI.Components.Recycler.ViewHolder target);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.ItemTouchHelperCallback.CanDropOver(Tizen.UI.Components.Recycler.RecyclerView,Tizen.UI.Components.Recycler.ViewHolder,Tizen.UI.Components.Recycler.ViewHolder).recyclerView'></a>

`recyclerView` [RecyclerView](Tizen.UI.Components.Recycler.RecyclerView.md 'Tizen.UI.Components.Recycler.RecyclerView')

The RecyclerView to which ItemTouchHelper is attached to.

<a name='Tizen.UI.Components.Recycler.ItemTouchHelperCallback.CanDropOver(Tizen.UI.Components.Recycler.RecyclerView,Tizen.UI.Components.Recycler.ViewHolder,Tizen.UI.Components.Recycler.ViewHolder).current'></a>

`current` [ViewHolder](Tizen.UI.Components.Recycler.ViewHolder.md 'Tizen.UI.Components.Recycler.ViewHolder')

The ViewHolder that user is dragging.

<a name='Tizen.UI.Components.Recycler.ItemTouchHelperCallback.CanDropOver(Tizen.UI.Components.Recycler.RecyclerView,Tizen.UI.Components.Recycler.ViewHolder,Tizen.UI.Components.Recycler.ViewHolder).target'></a>

`target` [ViewHolder](Tizen.UI.Components.Recycler.ViewHolder.md 'Tizen.UI.Components.Recycler.ViewHolder')

The ViewHolder which is below the dragged ViewHolder.

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.Recycler.ItemTouchHelperCallback.ChooseDropTarget(Tizen.UI.Components.Recycler.ViewHolder,System.Collections.Generic.List_Tizen.UI.Components.Recycler.ViewHolder_,Tizen.UI.Point)'></a>

## ItemTouchHelperCallback.ChooseDropTarget(ViewHolder, List&lt;ViewHolder>, Point) Method

Called by ItemTouchHelper to select a drop target from the list of ViewHolders that  
are under the dragged View.  
Default implementation filters the View with which dragged item have changed position in the drag direction.  
For instance, if the view is dragged UP, it compares the top of the two views before and after drag started.  
If that value is different, the target view passes the filter.  
Among these Views which pass the test, the one closest to the dragged view is chosen.

```csharp
public virtual Tizen.UI.Components.Recycler.ViewHolder ChooseDropTarget(Tizen.UI.Components.Recycler.ViewHolder selected, System.Collections.Generic.List&lt;Tizen.UI.Components.Recycler.ViewHolder> dropTargets, Tizen.UI.Point currentPosition);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.ItemTouchHelperCallback.ChooseDropTarget(Tizen.UI.Components.Recycler.ViewHolder,System.Collections.Generic.List_Tizen.UI.Components.Recycler.ViewHolder_,Tizen.UI.Point).selected'></a>

`selected` [ViewHolder](Tizen.UI.Components.Recycler.ViewHolder.md 'Tizen.UI.Components.Recycler.ViewHolder')

The ViewHolder being dragged by the user.

<a name='Tizen.UI.Components.Recycler.ItemTouchHelperCallback.ChooseDropTarget(Tizen.UI.Components.Recycler.ViewHolder,System.Collections.Generic.List_Tizen.UI.Components.Recycler.ViewHolder_,Tizen.UI.Point).dropTargets'></a>

`dropTargets` [System.Collections.Generic.List&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.List-1 'System.Collections.Generic.List`1')[ViewHolder](Tizen.UI.Components.Recycler.ViewHolder.md 'Tizen.UI.Components.Recycler.ViewHolder')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.List-1 'System.Collections.Generic.List`1')

The list of ViewHolder that are under the dragged View and candidate as a drop.

<a name='Tizen.UI.Components.Recycler.ItemTouchHelperCallback.ChooseDropTarget(Tizen.UI.Components.Recycler.ViewHolder,System.Collections.Generic.List_Tizen.UI.Components.Recycler.ViewHolder_,Tizen.UI.Point).currentPosition'></a>

`currentPosition` [Tizen.UI.Point](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Point 'Tizen.UI.Point')

The updated position value of the dragged View

#### Returns
[ViewHolder](Tizen.UI.Components.Recycler.ViewHolder.md 'Tizen.UI.Components.Recycler.ViewHolder')

<a name='Tizen.UI.Components.Recycler.ItemTouchHelperCallback.GetMovementPolicy(Tizen.UI.Components.Recycler.RecyclerView,Tizen.UI.Components.Recycler.ViewHolder)'></a>

## ItemTouchHelperCallback.GetMovementPolicy(RecyclerView, ViewHolder) Method

Should return a composite policy which defines the enabled move directions in each state.

```csharp
public abstract int GetMovementPolicy(Tizen.UI.Components.Recycler.RecyclerView recyclerView, Tizen.UI.Components.Recycler.ViewHolder viewholder);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.ItemTouchHelperCallback.GetMovementPolicy(Tizen.UI.Components.Recycler.RecyclerView,Tizen.UI.Components.Recycler.ViewHolder).recyclerView'></a>

`recyclerView` [RecyclerView](Tizen.UI.Components.Recycler.RecyclerView.md 'Tizen.UI.Components.Recycler.RecyclerView')

The RecyclerView to which ItemTouchHelper is attached.

<a name='Tizen.UI.Components.Recycler.ItemTouchHelperCallback.GetMovementPolicy(Tizen.UI.Components.Recycler.RecyclerView,Tizen.UI.Components.Recycler.ViewHolder).viewholder'></a>

`viewholder` [ViewHolder](Tizen.UI.Components.Recycler.ViewHolder.md 'Tizen.UI.Components.Recycler.ViewHolder')

The ViewHolder for which the movement information is necessary.

#### Returns
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

<a name='Tizen.UI.Components.Recycler.ItemTouchHelperCallback.GetSMoveThreshold(Tizen.UI.Components.Recycler.ViewHolder)'></a>

## ItemTouchHelperCallback.GetSMoveThreshold(ViewHolder) Method

Returns the fraction that the user should move the View to be considered as it is dragged.  
After a view is moved this portion, ItemTouchHelper starts checking for Views below it for a possible drop.  
Default is 0.25f.

```csharp
public virtual float GetSMoveThreshold(Tizen.UI.Components.Recycler.ViewHolder viewholder);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.ItemTouchHelperCallback.GetSMoveThreshold(Tizen.UI.Components.Recycler.ViewHolder).viewholder'></a>

`viewholder` [ViewHolder](Tizen.UI.Components.Recycler.ViewHolder.md 'Tizen.UI.Components.Recycler.ViewHolder')

The new ViewHolder for get threshold.

#### Returns
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Components.Recycler.ItemTouchHelperCallback.HasDragPolicy(Tizen.UI.Components.Recycler.RecyclerView,Tizen.UI.Components.Recycler.ViewHolder)'></a>

## ItemTouchHelperCallback.HasDragPolicy(RecyclerView, ViewHolder) Method

Gets whether this viewholder has drag policy on direction or not.

```csharp
public bool HasDragPolicy(Tizen.UI.Components.Recycler.RecyclerView recyclerView, Tizen.UI.Components.Recycler.ViewHolder viewholder);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.ItemTouchHelperCallback.HasDragPolicy(Tizen.UI.Components.Recycler.RecyclerView,Tizen.UI.Components.Recycler.ViewHolder).recyclerView'></a>

`recyclerView` [RecyclerView](Tizen.UI.Components.Recycler.RecyclerView.md 'Tizen.UI.Components.Recycler.RecyclerView')

The RecyclerView instance to which ItemTouchHelper is attached to.

<a name='Tizen.UI.Components.Recycler.ItemTouchHelperCallback.HasDragPolicy(Tizen.UI.Components.Recycler.RecyclerView,Tizen.UI.Components.Recycler.ViewHolder).viewholder'></a>

`viewholder` [ViewHolder](Tizen.UI.Components.Recycler.ViewHolder.md 'Tizen.UI.Components.Recycler.ViewHolder')

The viewholer to check drag policy.

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.Recycler.ItemTouchHelperCallback.InterpolateOutOfBoundsScroll(Tizen.UI.Components.Recycler.RecyclerView,float,float,float,long)'></a>

## ItemTouchHelperCallback.InterpolateOutOfBoundsScroll(RecyclerView, float, float, float, long) Method

Called by the ItemTouchHelper when user is dragging a view out of bounds.  
You can override this method to decide how much RecyclerView should scroll in response to this action.  
Default implementation calculates a value based on the amount of View out of bounds and the time it spent there.  
The longer user keeps the View out of bounds, the faster the list will scroll.  
Similarly, the larger portion of the View is out of bounds, the faster the RecyclerView will scroll.

```csharp
public virtual float InterpolateOutOfBoundsScroll(Tizen.UI.Components.Recycler.RecyclerView recyclerView, float viewSize, float viewSizeOutOfBounds, float totalSize, long msSinceStartScroll);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.ItemTouchHelperCallback.InterpolateOutOfBoundsScroll(Tizen.UI.Components.Recycler.RecyclerView,float,float,float,long).recyclerView'></a>

`recyclerView` [RecyclerView](Tizen.UI.Components.Recycler.RecyclerView.md 'Tizen.UI.Components.Recycler.RecyclerView')

The RecyclerView instance to which ItemTouchHelper is attached to.

<a name='Tizen.UI.Components.Recycler.ItemTouchHelperCallback.InterpolateOutOfBoundsScroll(Tizen.UI.Components.Recycler.RecyclerView,float,float,float,long).viewSize'></a>

`viewSize` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The total size of the View in scroll direction, excluding item decorations.

<a name='Tizen.UI.Components.Recycler.ItemTouchHelperCallback.InterpolateOutOfBoundsScroll(Tizen.UI.Components.Recycler.RecyclerView,float,float,float,long).viewSizeOutOfBounds'></a>

`viewSizeOutOfBounds` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The total size of the View that is out of bounds.

<a name='Tizen.UI.Components.Recycler.ItemTouchHelperCallback.InterpolateOutOfBoundsScroll(Tizen.UI.Components.Recycler.RecyclerView,float,float,float,long).totalSize'></a>

`totalSize` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The total size of RecyclerView in the scroll direction.

<a name='Tizen.UI.Components.Recycler.ItemTouchHelperCallback.InterpolateOutOfBoundsScroll(Tizen.UI.Components.Recycler.RecyclerView,float,float,float,long).msSinceStartScroll'></a>

`msSinceStartScroll` [System.Int64](https://docs.microsoft.com/en-us/dotnet/api/System.Int64 'System.Int64')

The time passed since View is kept out of bounds.

#### Returns
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Components.Recycler.ItemTouchHelperCallback.MakePolicy(Tizen.UI.Components.Recycler.TouchActionState,Tizen.UI.Components.Recycler.TouchDirection)'></a>

## ItemTouchHelperCallback.MakePolicy(TouchActionState, TouchDirection) Method

Shifts the given direction flags to the offset of the given action state.

```csharp
public static int MakePolicy(Tizen.UI.Components.Recycler.TouchActionState actionState, Tizen.UI.Components.Recycler.TouchDirection directions);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.ItemTouchHelperCallback.MakePolicy(Tizen.UI.Components.Recycler.TouchActionState,Tizen.UI.Components.Recycler.TouchDirection).actionState'></a>

`actionState` [TouchActionState](Tizen.UI.Components.Recycler.TouchActionState.md 'Tizen.UI.Components.Recycler.TouchActionState')

The action state you want to get policy in.

<a name='Tizen.UI.Components.Recycler.ItemTouchHelperCallback.MakePolicy(Tizen.UI.Components.Recycler.TouchActionState,Tizen.UI.Components.Recycler.TouchDirection).directions'></a>

`directions` [TouchDirection](Tizen.UI.Components.Recycler.TouchDirection.md 'Tizen.UI.Components.Recycler.TouchDirection')

The direction policy. Can be composed [TouchDirection](Tizen.UI.Components.Recycler.TouchDirection.md 'Tizen.UI.Components.Recycler.TouchDirection')

#### Returns
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

<a name='Tizen.UI.Components.Recycler.ItemTouchHelperCallback.OnMove(Tizen.UI.Components.Recycler.RecyclerView,Tizen.UI.Components.Recycler.ViewHolder,Tizen.UI.Components.Recycler.ViewHolder)'></a>

## ItemTouchHelperCallback.OnMove(RecyclerView, ViewHolder, ViewHolder) Method

Called when ItemTouchHelper wants to move the dragged item from its old position to the new position.  
If this method returns true, ItemTouchHelper assumes viewholer has been moved to the adapter position of target ViewHolder.

```csharp
public abstract bool OnMove(Tizen.UI.Components.Recycler.RecyclerView recyclerView, Tizen.UI.Components.Recycler.ViewHolder viewholder, Tizen.UI.Components.Recycler.ViewHolder target);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.ItemTouchHelperCallback.OnMove(Tizen.UI.Components.Recycler.RecyclerView,Tizen.UI.Components.Recycler.ViewHolder,Tizen.UI.Components.Recycler.ViewHolder).recyclerView'></a>

`recyclerView` [RecyclerView](Tizen.UI.Components.Recycler.RecyclerView.md 'Tizen.UI.Components.Recycler.RecyclerView')

The RecyclerView to which ItemTouchHelper is attached to.

<a name='Tizen.UI.Components.Recycler.ItemTouchHelperCallback.OnMove(Tizen.UI.Components.Recycler.RecyclerView,Tizen.UI.Components.Recycler.ViewHolder,Tizen.UI.Components.Recycler.ViewHolder).viewholder'></a>

`viewholder` [ViewHolder](Tizen.UI.Components.Recycler.ViewHolder.md 'Tizen.UI.Components.Recycler.ViewHolder')

The ViewHolder which is being dragged by the user.

<a name='Tizen.UI.Components.Recycler.ItemTouchHelperCallback.OnMove(Tizen.UI.Components.Recycler.RecyclerView,Tizen.UI.Components.Recycler.ViewHolder,Tizen.UI.Components.Recycler.ViewHolder).target'></a>

`target` [ViewHolder](Tizen.UI.Components.Recycler.ViewHolder.md 'Tizen.UI.Components.Recycler.ViewHolder')

The ViewHolder over which the currently active item is being dragged.

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.Recycler.ItemTouchHelperCallback.OnMoved(Tizen.UI.Components.Recycler.RecyclerView,Tizen.UI.Components.Recycler.ViewHolder,int,Tizen.UI.Components.Recycler.ViewHolder,int,Tizen.UI.Point)'></a>

## ItemTouchHelperCallback.OnMoved(RecyclerView, ViewHolder, int, ViewHolder, int, Point) Method

Called when [OnMove(RecyclerView, ViewHolder, ViewHolder)](Tizen.UI.Components.Recycler.ItemTouchHelperCallback.md#Tizen.UI.Components.Recycler.ItemTouchHelperCallback.OnMove(Tizen.UI.Components.Recycler.RecyclerView,Tizen.UI.Components.Recycler.ViewHolder,Tizen.UI.Components.Recycler.ViewHolder) 'Tizen.UI.Components.Recycler.ItemTouchHelperCallback.OnMove(Tizen.UI.Components.Recycler.RecyclerView, Tizen.UI.Components.Recycler.ViewHolder, Tizen.UI.Components.Recycler.ViewHolder)') returns true.

```csharp
public virtual void OnMoved(Tizen.UI.Components.Recycler.RecyclerView recyclerView, Tizen.UI.Components.Recycler.ViewHolder viewholder, int fromPos, Tizen.UI.Components.Recycler.ViewHolder target, int toPos, Tizen.UI.Point currentPosition);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.ItemTouchHelperCallback.OnMoved(Tizen.UI.Components.Recycler.RecyclerView,Tizen.UI.Components.Recycler.ViewHolder,int,Tizen.UI.Components.Recycler.ViewHolder,int,Tizen.UI.Point).recyclerView'></a>

`recyclerView` [RecyclerView](Tizen.UI.Components.Recycler.RecyclerView.md 'Tizen.UI.Components.Recycler.RecyclerView')

The RecyclerView controlled by the ItemTouchHelper.

<a name='Tizen.UI.Components.Recycler.ItemTouchHelperCallback.OnMoved(Tizen.UI.Components.Recycler.RecyclerView,Tizen.UI.Components.Recycler.ViewHolder,int,Tizen.UI.Components.Recycler.ViewHolder,int,Tizen.UI.Point).viewholder'></a>

`viewholder` [ViewHolder](Tizen.UI.Components.Recycler.ViewHolder.md 'Tizen.UI.Components.Recycler.ViewHolder')

The ViewHolder under user's control.

<a name='Tizen.UI.Components.Recycler.ItemTouchHelperCallback.OnMoved(Tizen.UI.Components.Recycler.RecyclerView,Tizen.UI.Components.Recycler.ViewHolder,int,Tizen.UI.Components.Recycler.ViewHolder,int,Tizen.UI.Point).fromPos'></a>

`fromPos` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The previous adapter position of the dragged item (before it wasmoved).

<a name='Tizen.UI.Components.Recycler.ItemTouchHelperCallback.OnMoved(Tizen.UI.Components.Recycler.RecyclerView,Tizen.UI.Components.Recycler.ViewHolder,int,Tizen.UI.Components.Recycler.ViewHolder,int,Tizen.UI.Point).target'></a>

`target` [ViewHolder](Tizen.UI.Components.Recycler.ViewHolder.md 'Tizen.UI.Components.Recycler.ViewHolder')

The ViewHolder on which the currently active item has been dropped.

<a name='Tizen.UI.Components.Recycler.ItemTouchHelperCallback.OnMoved(Tizen.UI.Components.Recycler.RecyclerView,Tizen.UI.Components.Recycler.ViewHolder,int,Tizen.UI.Components.Recycler.ViewHolder,int,Tizen.UI.Point).toPos'></a>

`toPos` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The new adapter position of the dragged item.

<a name='Tizen.UI.Components.Recycler.ItemTouchHelperCallback.OnMoved(Tizen.UI.Components.Recycler.RecyclerView,Tizen.UI.Components.Recycler.ViewHolder,int,Tizen.UI.Components.Recycler.ViewHolder,int,Tizen.UI.Point).currentPosition'></a>

`currentPosition` [Tizen.UI.Point](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Point 'Tizen.UI.Point')

The updated point value of the dragged View after drag translations are applied.

<a name='Tizen.UI.Components.Recycler.ItemTouchHelperCallback.OnSelectedChanged(Tizen.UI.Components.Recycler.ViewHolder,Tizen.UI.Components.Recycler.TouchActionState)'></a>

## ItemTouchHelperCallback.OnSelectedChanged(ViewHolder, TouchActionState) Method

```csharp
public void OnSelectedChanged(Tizen.UI.Components.Recycler.ViewHolder viewholder, Tizen.UI.Components.Recycler.TouchActionState actionState);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.ItemTouchHelperCallback.OnSelectedChanged(Tizen.UI.Components.Recycler.ViewHolder,Tizen.UI.Components.Recycler.TouchActionState).viewholder'></a>

`viewholder` [ViewHolder](Tizen.UI.Components.Recycler.ViewHolder.md 'Tizen.UI.Components.Recycler.ViewHolder')

The new ViewHolder that is being selected. Might be null if it is cleared.

<a name='Tizen.UI.Components.Recycler.ItemTouchHelperCallback.OnSelectedChanged(Tizen.UI.Components.Recycler.ViewHolder,Tizen.UI.Components.Recycler.TouchActionState).actionState'></a>

`actionState` [TouchActionState](Tizen.UI.Components.Recycler.TouchActionState.md 'Tizen.UI.Components.Recycler.TouchActionState')

The touch action state on view holder.


























































