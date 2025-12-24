### [Tizen.UI.Components.Recycler](Tizen.UI.Components.Recycler.md 'Tizen.UI.Components.Recycler')

## LinearLayoutManager Class

A linear layout manager that arranges items in a single row or column.

```csharp
public class LinearLayoutManager : Tizen.UI.Components.Recycler.LayoutManager,
Tizen.UI.Components.Recycler.IChildSeizable
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [LayoutManager](Tizen.UI.Components.Recycler.LayoutManager.md 'Tizen.UI.Components.Recycler.LayoutManager') &#129106; LinearLayoutManager

Implements [IChildSeizable](Tizen.UI.Components.Recycler.IChildSeizable.md 'Tizen.UI.Components.Recycler.IChildSeizable')
### Constructors

<a name='Tizen.UI.Components.Recycler.LinearLayoutManager.LinearLayoutManager()'></a>

## LinearLayoutManager() Constructor

Creates a new instance of a LinearLayoutManager.

```csharp
public LinearLayoutManager();
```
### Properties

<a name='Tizen.UI.Components.Recycler.LinearLayoutManager.CanScrollHorizontally'></a>

## LinearLayoutManager.CanScrollHorizontally Property

Check if the recycler view can scroll horizontally.

```csharp
public override bool CanScrollHorizontally { get; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.Recycler.LinearLayoutManager.CanScrollVertically'></a>

## LinearLayoutManager.CanScrollVertically Property

Check if the recycler view can scroll vertically.

```csharp
public override bool CanScrollVertically { get; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.Recycler.LinearLayoutManager.IsHorizontal'></a>

## LinearLayoutManager.IsHorizontal Property

Specifies whether the layout should be horizontal or vertical.

```csharp
public bool IsHorizontal { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.Recycler.LinearLayoutManager.ItemAnimator'></a>

## LinearLayoutManager.ItemAnimator Property

Gets or sets the ItemAnimator for this LayoutManager.

```csharp
public Tizen.UI.Components.Recycler.IItemAnimator ItemAnimator { get; set; }
```

#### Property Value
[IItemAnimator](Tizen.UI.Components.Recycler.IItemAnimator.md 'Tizen.UI.Components.Recycler.IItemAnimator')

<a name='Tizen.UI.Components.Recycler.LinearLayoutManager.LayoutViewPort'></a>

## LinearLayoutManager.LayoutViewPort Property

The view port area where the item is placed

```csharp
public override Tizen.UI.Rect LayoutViewPort { get; set; }
```

#### Property Value
Tizen.UI.Rect
### Methods

<a name='Tizen.UI.Components.Recycler.LinearLayoutManager.ComputeHorizontalScrollExtent(int,int)'></a>

## LinearLayoutManager.ComputeHorizontalScrollExtent(int, int) Method

Compute the horizontal scroll extent.

```csharp
public override int ComputeHorizontalScrollExtent(int first, int last);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.LinearLayoutManager.ComputeHorizontalScrollExtent(int,int).first'></a>

`first` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The first realized item index.

<a name='Tizen.UI.Components.Recycler.LinearLayoutManager.ComputeHorizontalScrollExtent(int,int).last'></a>

`last` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The last realized item index.

#### Returns
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')  
The horizontal scroll extent.

<a name='Tizen.UI.Components.Recycler.LinearLayoutManager.ComputeHorizontalScrollOffset(int,int)'></a>

## LinearLayoutManager.ComputeHorizontalScrollOffset(int, int) Method

Compute the horizontal scroll offset.

```csharp
public override int ComputeHorizontalScrollOffset(int first, int last);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.LinearLayoutManager.ComputeHorizontalScrollOffset(int,int).first'></a>

`first` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The first realized item index.

<a name='Tizen.UI.Components.Recycler.LinearLayoutManager.ComputeHorizontalScrollOffset(int,int).last'></a>

`last` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The last realized item index.

#### Returns
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')  
The horizontal scroll offset.

<a name='Tizen.UI.Components.Recycler.LinearLayoutManager.ComputeHorizontalScrollRange(int,int)'></a>

## LinearLayoutManager.ComputeHorizontalScrollRange(int, int) Method

Compute the horizontal scroll range.

```csharp
public override int ComputeHorizontalScrollRange(int first, int last);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.LinearLayoutManager.ComputeHorizontalScrollRange(int,int).first'></a>

`first` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The first realized item index.

<a name='Tizen.UI.Components.Recycler.LinearLayoutManager.ComputeHorizontalScrollRange(int,int).last'></a>

`last` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The last realized item index.

#### Returns
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')  
The horizontal scroll range.

<a name='Tizen.UI.Components.Recycler.LinearLayoutManager.ComputeVerticalScrollExtent(int,int)'></a>

## LinearLayoutManager.ComputeVerticalScrollExtent(int, int) Method

Compute the vertical scroll extent.

```csharp
public override int ComputeVerticalScrollExtent(int first, int last);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.LinearLayoutManager.ComputeVerticalScrollExtent(int,int).first'></a>

`first` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The first realized item index.

<a name='Tizen.UI.Components.Recycler.LinearLayoutManager.ComputeVerticalScrollExtent(int,int).last'></a>

`last` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The last realized item index.

#### Returns
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')  
The vertical scroll extent.

<a name='Tizen.UI.Components.Recycler.LinearLayoutManager.ComputeVerticalScrollOffset(int,int)'></a>

## LinearLayoutManager.ComputeVerticalScrollOffset(int, int) Method

Compute the vertical scroll offset.

```csharp
public override int ComputeVerticalScrollOffset(int first, int last);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.LinearLayoutManager.ComputeVerticalScrollOffset(int,int).first'></a>

`first` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The first realized item index.

<a name='Tizen.UI.Components.Recycler.LinearLayoutManager.ComputeVerticalScrollOffset(int,int).last'></a>

`last` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The last realized item index.

#### Returns
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')  
The vertical scroll offset.

<a name='Tizen.UI.Components.Recycler.LinearLayoutManager.ComputeVerticalScrollRange(int,int)'></a>

## LinearLayoutManager.ComputeVerticalScrollRange(int, int) Method

Compute the vertical scroll range.

```csharp
public override int ComputeVerticalScrollRange(int first, int last);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.LinearLayoutManager.ComputeVerticalScrollRange(int,int).first'></a>

`first` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The first realized item index.

<a name='Tizen.UI.Components.Recycler.LinearLayoutManager.ComputeVerticalScrollRange(int,int).last'></a>

`last` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The last realized item index.

#### Returns
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')  
The vertical scroll range.

<a name='Tizen.UI.Components.Recycler.LinearLayoutManager.Fill(int,int)'></a>

## LinearLayoutManager.Fill(int, int) Method

Fill the requested space with views.This method will try to fill the requested space with as many views as possible.  
It will stop when either all available views have been laid out or when there are no more views to recycle.  
The amount of space that was actually filled will be returned.

```csharp
public virtual int Fill(int requested, int position=-1);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.LinearLayoutManager.Fill(int,int).requested'></a>

`requested` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The Requested space

<a name='Tizen.UI.Components.Recycler.LinearLayoutManager.Fill(int,int).position'></a>

`position` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The item position

#### Returns
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')  
The filled space

<a name='Tizen.UI.Components.Recycler.LinearLayoutManager.GetSeized(int)'></a>

## LinearLayoutManager.GetSeized(int) Method

Get seized item view holder.

```csharp
public Tizen.UI.Components.Recycler.ViewHolder GetSeized(int position);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.LinearLayoutManager.GetSeized(int).position'></a>

`position` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The item position.

Implements [GetSeized(int)](Tizen.UI.Components.Recycler.IChildSeizable.md#Tizen.UI.Components.Recycler.IChildSeizable.GetSeized(int) 'Tizen.UI.Components.Recycler.IChildSeizable.GetSeized(int)')

#### Returns
[ViewHolder](Tizen.UI.Components.Recycler.ViewHolder.md 'Tizen.UI.Components.Recycler.ViewHolder')  
seized view holder.

<a name='Tizen.UI.Components.Recycler.LinearLayoutManager.GetSeizedCount()'></a>

## LinearLayoutManager.GetSeizedCount() Method

Get the count of seized item.

```csharp
public int GetSeizedCount();
```

Implements [GetSeizedCount()](Tizen.UI.Components.Recycler.IChildSeizable.md#Tizen.UI.Components.Recycler.IChildSeizable.GetSeizedCount() 'Tizen.UI.Components.Recycler.IChildSeizable.GetSeizedCount()')

#### Returns
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')  
seized item count.

<a name='Tizen.UI.Components.Recycler.LinearLayoutManager.Initialize()'></a>

## LinearLayoutManager.Initialize() Method

Initialize the layout manager. This method is called when the layout manager is attached to the recycler view or data source is changed.

```csharp
public override void Initialize();
```

<a name='Tizen.UI.Components.Recycler.LinearLayoutManager.IsSeized(int)'></a>

## LinearLayoutManager.IsSeized(int) Method

Check whether this item is seized or not.

```csharp
public bool IsSeized(int position);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.LinearLayoutManager.IsSeized(int).position'></a>

`position` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The item position.

Implements [IsSeized(int)](Tizen.UI.Components.Recycler.IChildSeizable.md#Tizen.UI.Components.Recycler.IChildSeizable.IsSeized(int) 'Tizen.UI.Components.Recycler.IChildSeizable.IsSeized(int)')

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
true if position item is seized.

<a name='Tizen.UI.Components.Recycler.LinearLayoutManager.LayoutPosition(int)'></a>

## LinearLayoutManager.LayoutPosition(int) Method

Resets all created items and places the item in the specified position on the top left

```csharp
public override void LayoutPosition(int position);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.LinearLayoutManager.LayoutPosition(int).position'></a>

`position` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The position of the view item to layout.

<a name='Tizen.UI.Components.Recycler.LinearLayoutManager.MeasureUpdate(Tizen.UI.View)'></a>

## LinearLayoutManager.MeasureUpdate(View) Method

Measure the size of the view item.

```csharp
public override Tizen.UI.Size MeasureUpdate(Tizen.UI.View itemView);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.LinearLayoutManager.MeasureUpdate(Tizen.UI.View).itemView'></a>

`itemView` Tizen.UI.View

The view item to measure.

#### Returns
Tizen.UI.Size  
The measured size of the view item.

<a name='Tizen.UI.Components.Recycler.LinearLayoutManager.OnChildrenChanged(System.Collections.Specialized.NotifyCollectionChangedEventArgs)'></a>

## LinearLayoutManager.OnChildrenChanged(NotifyCollectionChangedEventArgs) Method

Called when change the chlidren of the recycler view.

```csharp
public override void OnChildrenChanged(System.Collections.Specialized.NotifyCollectionChangedEventArgs e);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.LinearLayoutManager.OnChildrenChanged(System.Collections.Specialized.NotifyCollectionChangedEventArgs).e'></a>

`e` [System.Collections.Specialized.NotifyCollectionChangedEventArgs](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Specialized.NotifyCollectionChangedEventArgs 'System.Collections.Specialized.NotifyCollectionChangedEventArgs')

Collection changed

<a name='Tizen.UI.Components.Recycler.LinearLayoutManager.OnLayoutChildren()'></a>

## LinearLayoutManager.OnLayoutChildren() Method

Called when layout the children of the recycler view.

```csharp
public override void OnLayoutChildren();
```

<a name='Tizen.UI.Components.Recycler.LinearLayoutManager.RecycleOutOfSightView()'></a>

## LinearLayoutManager.RecycleOutOfSightView() Method

Recycle the out of sight view items. This method will remove all the views that are not visible anymore from the recycler view.  
These views will be recycled and can be reused by the adapter.  
This method should be called whenever the view port has changed. For example after scrolling or resizing the recycler view.

```csharp
public override void RecycleOutOfSightView();
```

<a name='Tizen.UI.Components.Recycler.LinearLayoutManager.ReleaseChild(Tizen.UI.Components.Recycler.ViewHolder)'></a>

## LinearLayoutManager.ReleaseChild(ViewHolder) Method

Release the view holder.  
view holder is released from user, will be re-layout, recycled from now on.

```csharp
public void ReleaseChild(Tizen.UI.Components.Recycler.ViewHolder viewHolder);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.LinearLayoutManager.ReleaseChild(Tizen.UI.Components.Recycler.ViewHolder).viewHolder'></a>

`viewHolder` [ViewHolder](Tizen.UI.Components.Recycler.ViewHolder.md 'Tizen.UI.Components.Recycler.ViewHolder')

The viewholer to be released.

Implements [ReleaseChild(ViewHolder)](Tizen.UI.Components.Recycler.IChildSeizable.md#Tizen.UI.Components.Recycler.IChildSeizable.ReleaseChild(Tizen.UI.Components.Recycler.ViewHolder) 'Tizen.UI.Components.Recycler.IChildSeizable.ReleaseChild(Tizen.UI.Components.Recycler.ViewHolder)')

<a name='Tizen.UI.Components.Recycler.LinearLayoutManager.ScrollHorizontallyBy(int)'></a>

## LinearLayoutManager.ScrollHorizontallyBy(int) Method

Layouts items to fill the requested direction.

```csharp
public override int ScrollHorizontallyBy(int dx);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.LinearLayoutManager.ScrollHorizontallyBy(int).dx'></a>

`dx` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The amount of pixels to scroll by.

#### Returns
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')  
layouted size

<a name='Tizen.UI.Components.Recycler.LinearLayoutManager.ScrollVerticallyBy(int)'></a>

## LinearLayoutManager.ScrollVerticallyBy(int) Method

Layouts items to fill the requested direction.

```csharp
public override int ScrollVerticallyBy(int dy);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.LinearLayoutManager.ScrollVerticallyBy(int).dy'></a>

`dy` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The amount of pixels to scroll by.

#### Returns
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')  
layouted size

<a name='Tizen.UI.Components.Recycler.LinearLayoutManager.SeizeChild(Tizen.UI.Components.Recycler.ViewHolder)'></a>

## LinearLayoutManager.SeizeChild(ViewHolder) Method

Seize the view holder.  
view holder is seized by user, will not be re-layout, recycled until it is released.

```csharp
public void SeizeChild(Tizen.UI.Components.Recycler.ViewHolder viewHolder);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.LinearLayoutManager.SeizeChild(Tizen.UI.Components.Recycler.ViewHolder).viewHolder'></a>

`viewHolder` [ViewHolder](Tizen.UI.Components.Recycler.ViewHolder.md 'Tizen.UI.Components.Recycler.ViewHolder')

The viewholer to be seized.

Implements [SeizeChild(ViewHolder)](Tizen.UI.Components.Recycler.IChildSeizable.md#Tizen.UI.Components.Recycler.IChildSeizable.SeizeChild(Tizen.UI.Components.Recycler.ViewHolder) 'Tizen.UI.Components.Recycler.IChildSeizable.SeizeChild(Tizen.UI.Components.Recycler.ViewHolder)')



























































