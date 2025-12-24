
## Tizen.UI.Components.Recycler Namespace

| Classes | |
| :--- | :--- |
| [Adapter](Tizen.UI.Components.Recycler.Adapter.md 'Tizen.UI.Components.Recycler.Adapter') | Adapter provide a binding from an app-specific data set to views that<br/>are displayed within a [RecyclerView](Tizen.UI.Components.Recycler.Adapter.md#Tizen.UI.Components.Recycler.Adapter.RecyclerView 'Tizen.UI.Components.Recycler.Adapter.RecyclerView'). |
| [AnimationFinishedEventArgs](Tizen.UI.Components.Recycler.AnimationFinishedEventArgs.md 'Tizen.UI.Components.Recycler.AnimationFinishedEventArgs') | Event arguments for when an animation completes. |
| [DefaultItemAnimator](Tizen.UI.Components.Recycler.DefaultItemAnimator.md 'Tizen.UI.Components.Recycler.DefaultItemAnimator') | Default implementation of IItemAnimator. |
| [ExclusiveSelectionModelGroup&lt;T&gt;](Tizen.UI.Components.Recycler.ExclusiveSelectionModelGroup_T_.md 'Tizen.UI.Components.Recycler.ExclusiveSelectionModelGroup&lt;T>') | An abstract class for the observable group collection of [ISelectableModel](Tizen.UI.Components.Recycler.ISelectableModel.md 'Tizen.UI.Components.Recycler.ISelectableModel').<br/>The group can only have one selected children exclusively. |
| [GridLayoutManager](Tizen.UI.Components.Recycler.GridLayoutManager.md 'Tizen.UI.Components.Recycler.GridLayoutManager') | Grid layout manager for grid view. |
| [GroupInfo](Tizen.UI.Components.Recycler.GroupInfo.md 'Tizen.UI.Components.Recycler.GroupInfo') | The information data of the groups. |
| [GroupItemSource](Tizen.UI.Components.Recycler.GroupItemSource.md 'Tizen.UI.Components.Recycler.GroupItemSource') | The class that provides the grouped data source for adapter. |
| [GroupItemTemplateAdapter](Tizen.UI.Components.Recycler.GroupItemTemplateAdapter.md 'Tizen.UI.Components.Recycler.GroupItemTemplateAdapter') | The apdater using ViewTemplate for creates items and groups. |
| [HolderExtensions](Tizen.UI.Components.Recycler.HolderExtensions.md 'Tizen.UI.Components.Recycler.HolderExtensions') | View holder extension method. |
| [HolderInfo](Tizen.UI.Components.Recycler.HolderInfo.md 'Tizen.UI.Components.Recycler.HolderInfo') | The information data of the view holder. |
| [ItemTemplateAdapter](Tizen.UI.Components.Recycler.ItemTemplateAdapter.md 'Tizen.UI.Components.Recycler.ItemTemplateAdapter') | The apdater using ViewTemplate for creates items. |
| [ItemTouchHelper](Tizen.UI.Components.Recycler.ItemTouchHelper.md 'Tizen.UI.Components.Recycler.ItemTouchHelper') | Item touch helper for [RecyclerView](Tizen.UI.Components.Recycler.RecyclerView.md 'Tizen.UI.Components.Recycler.RecyclerView').<br/>This is a utility class to add touch action support to [RecyclerView](Tizen.UI.Components.Recycler.RecyclerView.md 'Tizen.UI.Components.Recycler.RecyclerView')..<br/>It works with a [RecyclerView](Tizen.UI.Components.Recycler.RecyclerView.md 'Tizen.UI.Components.Recycler.RecyclerView'). and a [ItemTouchHelperCallback](Tizen.UI.Components.Recycler.ItemTouchHelperCallback.md 'Tizen.UI.Components.Recycler.ItemTouchHelperCallback'). class, which configures what type of interactions<br/>are enabled and also receives events when user performs these actions.<br/>Depending on which functionality you support, you should override methods in [ItemTouchHelperCallback](Tizen.UI.Components.Recycler.ItemTouchHelperCallback.md 'Tizen.UI.Components.Recycler.ItemTouchHelperCallback'). |
| [ItemTouchHelperCallback](Tizen.UI.Components.Recycler.ItemTouchHelperCallback.md 'Tizen.UI.Components.Recycler.ItemTouchHelperCallback') | This class is the contract between ItemTouchHelper and your application. It lets you control<br/>which touch behaviors are enabled per each ViewHolder and also receive callbacks when user performs these actions.<br/>o control which actions user can take on each view, you should override<br/>[GetMovementPolicy(RecyclerView, ViewHolder)](Tizen.UI.Components.Recycler.ItemTouchHelperCallback.md#Tizen.UI.Components.Recycler.ItemTouchHelperCallback.GetMovementPolicy(Tizen.UI.Components.Recycler.RecyclerView,Tizen.UI.Components.Recycler.ViewHolder) 'Tizen.UI.Components.Recycler.ItemTouchHelperCallback.GetMovementPolicy(Tizen.UI.Components.Recycler.RecyclerView, Tizen.UI.Components.Recycler.ViewHolder)') and return appropriate set of direction flags. |
| [LayoutManager](Tizen.UI.Components.Recycler.LayoutManager.md 'Tizen.UI.Components.Recycler.LayoutManager') | The base class for layout managers. A layout manager is responsible for positioning and sizing the child views in a recycler view. |
| [LinearLayoutManager](Tizen.UI.Components.Recycler.LinearLayoutManager.md 'Tizen.UI.Components.Recycler.LinearLayoutManager') | A linear layout manager that arranges items in a single row or column. |
| [LinearSwapCallback](Tizen.UI.Components.Recycler.LinearSwapCallback.md 'Tizen.UI.Components.Recycler.LinearSwapCallback') | The simple abstract calss of [ItemTouchHelperCallback](Tizen.UI.Components.Recycler.ItemTouchHelperCallback.md 'Tizen.UI.Components.Recycler.ItemTouchHelperCallback') for swap actions.<br/>You have to override [OnMove(RecyclerView, ViewHolder, ViewHolder)](Tizen.UI.Components.Recycler.ItemTouchHelperCallback.md#Tizen.UI.Components.Recycler.ItemTouchHelperCallback.OnMove(Tizen.UI.Components.Recycler.RecyclerView,Tizen.UI.Components.Recycler.ViewHolder,Tizen.UI.Components.Recycler.ViewHolder) 'Tizen.UI.Components.Recycler.ItemTouchHelperCallback.OnMove(Tizen.UI.Components.Recycler.RecyclerView, Tizen.UI.Components.Recycler.ViewHolder, Tizen.UI.Components.Recycler.ViewHolder)') methods. |
| [RecyclerView](Tizen.UI.Components.Recycler.RecyclerView.md 'Tizen.UI.Components.Recycler.RecyclerView') | RecyclerView class.<br/>It provides a flexible view for displaying large data sets that can be scrolled very efficiently by maintaining a limited number of views.<br/>This class also supports smooth scrolling and animations. The RecyclerView works with a LayoutManager to position the items and Adapter to create them.<br/>RecyclerView also has built-in support for animations. |
| [RecycleScroller](Tizen.UI.Components.Recycler.RecycleScroller.md 'Tizen.UI.Components.Recycler.RecycleScroller') | RecyclerView Scroller class. It handles the scrolling behavior of the RecyclerView. |
| [SelectableModel](Tizen.UI.Components.Recycler.SelectableModel.md 'Tizen.UI.Components.Recycler.SelectableModel') | An abstract selectable data model which implements [ISelectableModel](Tizen.UI.Components.Recycler.ISelectableModel.md 'Tizen.UI.Components.Recycler.ISelectableModel'). |
| [SelectionModelGroup&lt;T&gt;](Tizen.UI.Components.Recycler.SelectionModelGroup_T_.md 'Tizen.UI.Components.Recycler.SelectionModelGroup&lt;T>') | An abstract class for the observable group collection of [ISelectableModel](Tizen.UI.Components.Recycler.ISelectableModel.md 'Tizen.UI.Components.Recycler.ISelectableModel').<br/>The group can have multiple selected children. |
| [StickyArea](Tizen.UI.Components.Recycler.StickyArea.md 'Tizen.UI.Components.Recycler.StickyArea') | Sticky area of RecyclerView. |
| [ViewHolder](Tizen.UI.Components.Recycler.ViewHolder.md 'Tizen.UI.Components.Recycler.ViewHolder') | ViewHolder is a class that holds the view of an item. |
| [ViewModel](Tizen.UI.Components.Recycler.ViewModel.md 'Tizen.UI.Components.Recycler.ViewModel') | View model which implements [System.ComponentModel.INotifyPropertyChanged](https://docs.microsoft.com/en-us/dotnet/api/System.ComponentModel.INotifyPropertyChanged 'System.ComponentModel.INotifyPropertyChanged') with helper methods. |
| [ViewModelGroup&lt;T&gt;](Tizen.UI.Components.Recycler.ViewModelGroup_T_.md 'Tizen.UI.Components.Recycler.ViewModelGroup&lt;T>') | View model group for [System.ComponentModel.INotifyPropertyChanged](https://docs.microsoft.com/en-us/dotnet/api/System.ComponentModel.INotifyPropertyChanged 'System.ComponentModel.INotifyPropertyChanged') with helper methods. |

| Interfaces | |
| :--- | :--- |
| [IChildSeizable](Tizen.UI.Components.Recycler.IChildSeizable.md 'Tizen.UI.Components.Recycler.IChildSeizable') | Interface that Layouter child can be seized and un-handled by layouter or recycled.<br/>This interface will be used on [ItemTouchHelper](Tizen.UI.Components.Recycler.ItemTouchHelper.md 'Tizen.UI.Components.Recycler.ItemTouchHelper'). |
| [IDividerProvider](Tizen.UI.Components.Recycler.IDividerProvider.md 'Tizen.UI.Components.Recycler.IDividerProvider') | The interface for a divider adapter. It is used to provide data for the RecyclerView. |
| [IGridRelativeSizeHelper](Tizen.UI.Components.Recycler.IGridRelativeSizeHelper.md 'Tizen.UI.Components.Recycler.IGridRelativeSizeHelper') | Interface for [GridView](https://docs.microsoft.com/en-us/dotnet/api/GridView 'GridView') sizing item by aspect ratio. |
| [IGridSpanHelper](Tizen.UI.Components.Recycler.IGridSpanHelper.md 'Tizen.UI.Components.Recycler.IGridSpanHelper') | [GridView](https://docs.microsoft.com/en-us/dotnet/api/GridView 'GridView') span helper interface. It provides additional information about item's span. |
| [IGroupedAdapter](Tizen.UI.Components.Recycler.IGroupedAdapter.md 'Tizen.UI.Components.Recycler.IGroupedAdapter') | The interface for a grouped adapter. It is used to provide data for the RecyclerView. |
| [IGroupedItem](Tizen.UI.Components.Recycler.IGroupedItem.md 'Tizen.UI.Components.Recycler.IGroupedItem') | Interface for grouped item.<br/>This interface is not mendatory to implement, but if you want to update the item's by the group position, you can use this interface. |
| [IItemAnimator](Tizen.UI.Components.Recycler.IItemAnimator.md 'Tizen.UI.Components.Recycler.IItemAnimator') | An interface to animate changes to the views in a RecyclerView. |
| [IItemDecoration](Tizen.UI.Components.Recycler.IItemDecoration.md 'Tizen.UI.Components.Recycler.IItemDecoration') | Interface for item decoration. It provides additional information about item's position |
| [ISelectableModel](Tizen.UI.Components.Recycler.ISelectableModel.md 'Tizen.UI.Components.Recycler.ISelectableModel') | Interface for model which provides data selectable. |
| [ISelectionModelGroup](Tizen.UI.Components.Recycler.ISelectionModelGroup.md 'Tizen.UI.Components.Recycler.ISelectionModelGroup') | An interface for the group collection of [ISelectableModel](Tizen.UI.Components.Recycler.ISelectableModel.md 'Tizen.UI.Components.Recycler.ISelectableModel').<br/>The group can have multiple selected children. |
| [ISelectionModelGroup&lt;T&gt;](Tizen.UI.Components.Recycler.ISelectionModelGroup_T_.md 'Tizen.UI.Components.Recycler.ISelectionModelGroup&lt;T>') | An generic interface for the group collection of [ISelectableModel](Tizen.UI.Components.Recycler.ISelectableModel.md 'Tizen.UI.Components.Recycler.ISelectableModel').<br/>The group can have multiple selected children. |

| Enums | |
| :--- | :--- |
| [AnimationType](Tizen.UI.Components.Recycler.AnimationType.md 'Tizen.UI.Components.Recycler.AnimationType') | Types of animations. |
| [TouchActionState](Tizen.UI.Components.Recycler.TouchActionState.md 'Tizen.UI.Components.Recycler.TouchActionState') | Touch Action State.<br/>This enum indicate what action is on ItemTouchHelper. |
| [TouchDirection](Tizen.UI.Components.Recycler.TouchDirection.md 'Tizen.UI.Components.Recycler.TouchDirection') | The direction of Touch. |



























































