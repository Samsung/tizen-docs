### [Tizen.UI.Components.Recycler](Tizen.UI.Components.Recycler.md 'Tizen.UI.Components.Recycler')

## GridLayoutManager Class

Grid layout manager for grid view.

```csharp
public class GridLayoutManager : Tizen.UI.Components.Recycler.LayoutManager
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [LayoutManager](Tizen.UI.Components.Recycler.LayoutManager.md 'Tizen.UI.Components.Recycler.LayoutManager') &#129106; GridLayoutManager
### Constructors

<a name='Tizen.UI.Components.Recycler.GridLayoutManager.GridLayoutManager(uint)'></a>

## GridLayoutManager(uint) Constructor

Creates an instance of GridLayoutManager.

```csharp
public GridLayoutManager(uint spanCount=1u);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.GridLayoutManager.GridLayoutManager(uint).spanCount'></a>

`spanCount` [System.UInt32](https://docs.microsoft.com/en-us/dotnet/api/System.UInt32 'System.UInt32')

The number of columns or rows in the grid.
### Properties

<a name='Tizen.UI.Components.Recycler.GridLayoutManager.CanScrollHorizontally'></a>

## GridLayoutManager.CanScrollHorizontally Property

Check if the recycler view can scroll horizontally.

```csharp
public override bool CanScrollHorizontally { get; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.Recycler.GridLayoutManager.CanScrollVertically'></a>

## GridLayoutManager.CanScrollVertically Property

Check if the recycler view can scroll vertically.

```csharp
public override bool CanScrollVertically { get; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.Recycler.GridLayoutManager.IsHorizontal'></a>

## GridLayoutManager.IsHorizontal Property

Gets or sets whether this layout manager arranges items horizontally or vertically.

```csharp
public bool IsHorizontal { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.Recycler.GridLayoutManager.ItemAnimator'></a>

## GridLayoutManager.ItemAnimator Property

Gets or sets the ItemAnimator for this LayoutManager.

```csharp
public Tizen.UI.Components.Recycler.IItemAnimator ItemAnimator { get; set; }
```

#### Property Value
[IItemAnimator](Tizen.UI.Components.Recycler.IItemAnimator.md 'Tizen.UI.Components.Recycler.IItemAnimator')

<a name='Tizen.UI.Components.Recycler.GridLayoutManager.LayoutViewPort'></a>

## GridLayoutManager.LayoutViewPort Property

The view port area where the item is placed

```csharp
public override Tizen.UI.Rect LayoutViewPort { get; set; }
```

#### Property Value
[Tizen.UI.Rect](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Rect 'Tizen.UI.Rect')

<a name='Tizen.UI.Components.Recycler.GridLayoutManager.SpanCount'></a>

## GridLayoutManager.SpanCount Property

Gets or sets the number of columns or rows in the grid.

```csharp
public virtual uint SpanCount { get; set; }
```

#### Property Value
[System.UInt32](https://docs.microsoft.com/en-us/dotnet/api/System.UInt32 'System.UInt32')
### Methods

<a name='Tizen.UI.Components.Recycler.GridLayoutManager.ComputeHorizontalScrollExtent(int,int)'></a>

## GridLayoutManager.ComputeHorizontalScrollExtent(int, int) Method

Compute the horizontal scroll extent.

```csharp
public override int ComputeHorizontalScrollExtent(int first, int last);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.GridLayoutManager.ComputeHorizontalScrollExtent(int,int).first'></a>

`first` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The first realized item index.

<a name='Tizen.UI.Components.Recycler.GridLayoutManager.ComputeHorizontalScrollExtent(int,int).last'></a>

`last` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The last realized item index.

#### Returns
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')  
The horizontal scroll extent.

<a name='Tizen.UI.Components.Recycler.GridLayoutManager.ComputeHorizontalScrollOffset(int,int)'></a>

## GridLayoutManager.ComputeHorizontalScrollOffset(int, int) Method

Compute the horizontal scroll offset.

```csharp
public override int ComputeHorizontalScrollOffset(int first, int last);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.GridLayoutManager.ComputeHorizontalScrollOffset(int,int).first'></a>

`first` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The first realized item index.

<a name='Tizen.UI.Components.Recycler.GridLayoutManager.ComputeHorizontalScrollOffset(int,int).last'></a>

`last` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The last realized item index.

#### Returns
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')  
The horizontal scroll offset.

<a name='Tizen.UI.Components.Recycler.GridLayoutManager.ComputeHorizontalScrollRange(int,int)'></a>

## GridLayoutManager.ComputeHorizontalScrollRange(int, int) Method

Compute the horizontal scroll range.

```csharp
public override int ComputeHorizontalScrollRange(int first, int last);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.GridLayoutManager.ComputeHorizontalScrollRange(int,int).first'></a>

`first` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The first realized item index.

<a name='Tizen.UI.Components.Recycler.GridLayoutManager.ComputeHorizontalScrollRange(int,int).last'></a>

`last` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The last realized item index.

#### Returns
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')  
The horizontal scroll range.

<a name='Tizen.UI.Components.Recycler.GridLayoutManager.ComputeVerticalScrollExtent(int,int)'></a>

## GridLayoutManager.ComputeVerticalScrollExtent(int, int) Method

Compute the vertical scroll extent.

```csharp
public override int ComputeVerticalScrollExtent(int first, int last);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.GridLayoutManager.ComputeVerticalScrollExtent(int,int).first'></a>

`first` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The first realized item index.

<a name='Tizen.UI.Components.Recycler.GridLayoutManager.ComputeVerticalScrollExtent(int,int).last'></a>

`last` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The last realized item index.

#### Returns
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')  
The vertical scroll extent.

<a name='Tizen.UI.Components.Recycler.GridLayoutManager.ComputeVerticalScrollOffset(int,int)'></a>

## GridLayoutManager.ComputeVerticalScrollOffset(int, int) Method

Compute the vertical scroll offset.

```csharp
public override int ComputeVerticalScrollOffset(int first, int last);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.GridLayoutManager.ComputeVerticalScrollOffset(int,int).first'></a>

`first` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The first realized item index.

<a name='Tizen.UI.Components.Recycler.GridLayoutManager.ComputeVerticalScrollOffset(int,int).last'></a>

`last` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The last realized item index.

#### Returns
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')  
The vertical scroll offset.

<a name='Tizen.UI.Components.Recycler.GridLayoutManager.ComputeVerticalScrollRange(int,int)'></a>

## GridLayoutManager.ComputeVerticalScrollRange(int, int) Method

Compute the vertical scroll range.

```csharp
public override int ComputeVerticalScrollRange(int first, int last);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.GridLayoutManager.ComputeVerticalScrollRange(int,int).first'></a>

`first` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The first realized item index.

<a name='Tizen.UI.Components.Recycler.GridLayoutManager.ComputeVerticalScrollRange(int,int).last'></a>

`last` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The last realized item index.

#### Returns
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')  
The vertical scroll range.

<a name='Tizen.UI.Components.Recycler.GridLayoutManager.Fill(int,int)'></a>

## GridLayoutManager.Fill(int, int) Method

Fill the requested space with views. This method will try to fill the requested space with as many views as possible.  
It will stop when either all available views have been laid out or when there are no more views to recycle.  
The amount of space that was actually filled will be returned.

```csharp
public virtual int Fill(int requested, int position=-1);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.GridLayoutManager.Fill(int,int).requested'></a>

`requested` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The Requested space

<a name='Tizen.UI.Components.Recycler.GridLayoutManager.Fill(int,int).position'></a>

`position` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The item position

#### Returns
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')  
The filled space

<a name='Tizen.UI.Components.Recycler.GridLayoutManager.Initialize()'></a>

## GridLayoutManager.Initialize() Method

Initialize the layout manager. This method is called when the layout manager is attached to the recycler view or data source is changed.

```csharp
public override void Initialize();
```

<a name='Tizen.UI.Components.Recycler.GridLayoutManager.LayoutPosition(int)'></a>

## GridLayoutManager.LayoutPosition(int) Method

Resets all created items and places the item in the specified position on the top left

```csharp
public override void LayoutPosition(int position);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.GridLayoutManager.LayoutPosition(int).position'></a>

`position` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The position of the view item to layout.

<a name='Tizen.UI.Components.Recycler.GridLayoutManager.MeasureUpdate(Tizen.UI.View)'></a>

## GridLayoutManager.MeasureUpdate(View) Method

Measure the size of the view item.

```csharp
public override Tizen.UI.Size MeasureUpdate(Tizen.UI.View itemView);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.GridLayoutManager.MeasureUpdate(Tizen.UI.View).itemView'></a>

`itemView` [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')

The view item to measure.

#### Returns
[Tizen.UI.Size](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Size 'Tizen.UI.Size')  
The measured size of the view item.

<a name='Tizen.UI.Components.Recycler.GridLayoutManager.OnChildrenChanged(System.Collections.Specialized.NotifyCollectionChangedEventArgs)'></a>

## GridLayoutManager.OnChildrenChanged(NotifyCollectionChangedEventArgs) Method

Called when change the chlidren of the recycler view.

```csharp
public override void OnChildrenChanged(System.Collections.Specialized.NotifyCollectionChangedEventArgs e);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.GridLayoutManager.OnChildrenChanged(System.Collections.Specialized.NotifyCollectionChangedEventArgs).e'></a>

`e` [System.Collections.Specialized.NotifyCollectionChangedEventArgs](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Specialized.NotifyCollectionChangedEventArgs 'System.Collections.Specialized.NotifyCollectionChangedEventArgs')

Collection changed

<a name='Tizen.UI.Components.Recycler.GridLayoutManager.OnLayoutChildren()'></a>

## GridLayoutManager.OnLayoutChildren() Method

Called when layout the children of the recycler view.

```csharp
public override void OnLayoutChildren();
```

<a name='Tizen.UI.Components.Recycler.GridLayoutManager.RecycleOutOfSightView()'></a>

## GridLayoutManager.RecycleOutOfSightView() Method

Recycle the out of sight view items. This method will remove all the views that are not visible anymore from the recycler view.  
These views will be recycled and can be reused by the adapter.  
This method should be called whenever the view port has changed. For example after scrolling or resizing the recycler view.

```csharp
public override void RecycleOutOfSightView();
```

<a name='Tizen.UI.Components.Recycler.GridLayoutManager.ScrollHorizontallyBy(int)'></a>

## GridLayoutManager.ScrollHorizontallyBy(int) Method

Layouts items to fill the requested direction.

```csharp
public override int ScrollHorizontallyBy(int dx);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.GridLayoutManager.ScrollHorizontallyBy(int).dx'></a>

`dx` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The amount of pixels to scroll by.

#### Returns
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')  
layouted size

<a name='Tizen.UI.Components.Recycler.GridLayoutManager.ScrollVerticallyBy(int)'></a>

## GridLayoutManager.ScrollVerticallyBy(int) Method

Layouts items to fill the requested direction.

```csharp
public override int ScrollVerticallyBy(int dy);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.GridLayoutManager.ScrollVerticallyBy(int).dy'></a>

`dy` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The amount of pixels to scroll by.

#### Returns
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')  
layouted size


























































