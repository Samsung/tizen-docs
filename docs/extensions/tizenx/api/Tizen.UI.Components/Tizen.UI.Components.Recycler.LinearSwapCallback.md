### [Tizen.UI.Components.Recycler](Tizen.UI.Components.Recycler.md 'Tizen.UI.Components.Recycler')

## LinearSwapCallback Class

The simple abstract calss of [ItemTouchHelperCallback](Tizen.UI.Components.Recycler.ItemTouchHelperCallback.md 'Tizen.UI.Components.Recycler.ItemTouchHelperCallback') for swap actions.  
You have to override [OnMove(RecyclerView, ViewHolder, ViewHolder)](Tizen.UI.Components.Recycler.ItemTouchHelperCallback.md#Tizen.UI.Components.Recycler.ItemTouchHelperCallback.OnMove(Tizen.UI.Components.Recycler.RecyclerView,Tizen.UI.Components.Recycler.ViewHolder,Tizen.UI.Components.Recycler.ViewHolder) 'Tizen.UI.Components.Recycler.ItemTouchHelperCallback.OnMove(Tizen.UI.Components.Recycler.RecyclerView, Tizen.UI.Components.Recycler.ViewHolder, Tizen.UI.Components.Recycler.ViewHolder)') methods.

```csharp
public abstract class LinearSwapCallback : Tizen.UI.Components.Recycler.ItemTouchHelperCallback
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [ItemTouchHelperCallback](Tizen.UI.Components.Recycler.ItemTouchHelperCallback.md 'Tizen.UI.Components.Recycler.ItemTouchHelperCallback') &#129106; LinearSwapCallback
### Methods

<a name='Tizen.UI.Components.Recycler.LinearSwapCallback.GetMovementPolicy(Tizen.UI.Components.Recycler.RecyclerView,Tizen.UI.Components.Recycler.ViewHolder)'></a>

## LinearSwapCallback.GetMovementPolicy(RecyclerView, ViewHolder) Method

Should return a composite policy which defines the enabled move directions in each state.

```csharp
public override int GetMovementPolicy(Tizen.UI.Components.Recycler.RecyclerView recyclerView, Tizen.UI.Components.Recycler.ViewHolder viewholder);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.LinearSwapCallback.GetMovementPolicy(Tizen.UI.Components.Recycler.RecyclerView,Tizen.UI.Components.Recycler.ViewHolder).recyclerView'></a>

`recyclerView` [RecyclerView](Tizen.UI.Components.Recycler.RecyclerView.md 'Tizen.UI.Components.Recycler.RecyclerView')

The RecyclerView to which ItemTouchHelper is attached.

<a name='Tizen.UI.Components.Recycler.LinearSwapCallback.GetMovementPolicy(Tizen.UI.Components.Recycler.RecyclerView,Tizen.UI.Components.Recycler.ViewHolder).viewholder'></a>

`viewholder` [ViewHolder](Tizen.UI.Components.Recycler.ViewHolder.md 'Tizen.UI.Components.Recycler.ViewHolder')

The ViewHolder for which the movement information is necessary.

#### Returns
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')


























































