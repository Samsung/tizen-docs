### [Tizen.UI.Components.Recycler](Tizen.UI.Components.Recycler.md 'Tizen.UI.Components.Recycler')

## LayoutManager Class

The base class for layout managers. A layout manager is responsible for positioning and sizing the child views in a recycler view.

```csharp
public abstract class LayoutManager
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; LayoutManager

Derived  
&#8627; [GridLayoutManager](Tizen.UI.Components.Recycler.GridLayoutManager.md 'Tizen.UI.Components.Recycler.GridLayoutManager')  
&#8627; [LinearLayoutManager](Tizen.UI.Components.Recycler.LinearLayoutManager.md 'Tizen.UI.Components.Recycler.LinearLayoutManager')
### Properties

<a name='Tizen.UI.Components.Recycler.LayoutManager.CanScrollHorizontally'></a>

## LayoutManager.CanScrollHorizontally Property

Check if the recycler view can scroll horizontally.

```csharp
public virtual bool CanScrollHorizontally { get; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.Recycler.LayoutManager.CanScrollVertically'></a>

## LayoutManager.CanScrollVertically Property

Check if the recycler view can scroll vertically.

```csharp
public virtual bool CanScrollVertically { get; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.Recycler.LayoutManager.LayoutViewPort'></a>

## LayoutManager.LayoutViewPort Property

The view port area where the item is placed

```csharp
public virtual Tizen.UI.Rect LayoutViewPort { get; set; }
```

#### Property Value
[Tizen.UI.Rect](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Rect 'Tizen.UI.Rect')

<a name='Tizen.UI.Components.Recycler.LayoutManager.RecyclerView'></a>

## LayoutManager.RecyclerView Property

The recycler view that uses this layout manager.  
This property is set by the recycler view when the layout manager is attached to it. It should not be set manually.

```csharp
public Tizen.UI.Components.Recycler.RecyclerView RecyclerView { get; set; }
```

#### Property Value
[RecyclerView](Tizen.UI.Components.Recycler.RecyclerView.md 'Tizen.UI.Components.Recycler.RecyclerView')
### Methods

<a name='Tizen.UI.Components.Recycler.LayoutManager.ComputeHorizontalScrollExtent(int,int)'></a>

## LayoutManager.ComputeHorizontalScrollExtent(int, int) Method

Compute the horizontal scroll extent.

```csharp
public abstract int ComputeHorizontalScrollExtent(int first, int last);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.LayoutManager.ComputeHorizontalScrollExtent(int,int).first'></a>

`first` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The first realized item index.

<a name='Tizen.UI.Components.Recycler.LayoutManager.ComputeHorizontalScrollExtent(int,int).last'></a>

`last` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The last realized item index.

#### Returns
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')  
The horizontal scroll extent.

<a name='Tizen.UI.Components.Recycler.LayoutManager.ComputeHorizontalScrollOffset(int,int)'></a>

## LayoutManager.ComputeHorizontalScrollOffset(int, int) Method

Compute the horizontal scroll offset.

```csharp
public abstract int ComputeHorizontalScrollOffset(int first, int last);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.LayoutManager.ComputeHorizontalScrollOffset(int,int).first'></a>

`first` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The first realized item index.

<a name='Tizen.UI.Components.Recycler.LayoutManager.ComputeHorizontalScrollOffset(int,int).last'></a>

`last` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The last realized item index.

#### Returns
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')  
The horizontal scroll offset.

<a name='Tizen.UI.Components.Recycler.LayoutManager.ComputeHorizontalScrollRange(int,int)'></a>

## LayoutManager.ComputeHorizontalScrollRange(int, int) Method

Compute the horizontal scroll range.

```csharp
public abstract int ComputeHorizontalScrollRange(int first, int last);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.LayoutManager.ComputeHorizontalScrollRange(int,int).first'></a>

`first` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The first realized item index.

<a name='Tizen.UI.Components.Recycler.LayoutManager.ComputeHorizontalScrollRange(int,int).last'></a>

`last` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The last realized item index.

#### Returns
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')  
The horizontal scroll range.

<a name='Tizen.UI.Components.Recycler.LayoutManager.ComputeVerticalScrollExtent(int,int)'></a>

## LayoutManager.ComputeVerticalScrollExtent(int, int) Method

Compute the vertical scroll extent.

```csharp
public abstract int ComputeVerticalScrollExtent(int first, int last);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.LayoutManager.ComputeVerticalScrollExtent(int,int).first'></a>

`first` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The first realized item index.

<a name='Tizen.UI.Components.Recycler.LayoutManager.ComputeVerticalScrollExtent(int,int).last'></a>

`last` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The last realized item index.

#### Returns
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')  
The vertical scroll extent.

<a name='Tizen.UI.Components.Recycler.LayoutManager.ComputeVerticalScrollOffset(int,int)'></a>

## LayoutManager.ComputeVerticalScrollOffset(int, int) Method

Compute the vertical scroll offset.

```csharp
public abstract int ComputeVerticalScrollOffset(int first, int last);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.LayoutManager.ComputeVerticalScrollOffset(int,int).first'></a>

`first` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The first realized item index.

<a name='Tizen.UI.Components.Recycler.LayoutManager.ComputeVerticalScrollOffset(int,int).last'></a>

`last` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The last realized item index.

#### Returns
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')  
The vertical scroll offset.

<a name='Tizen.UI.Components.Recycler.LayoutManager.ComputeVerticalScrollRange(int,int)'></a>

## LayoutManager.ComputeVerticalScrollRange(int, int) Method

Compute the vertical scroll range.

```csharp
public abstract int ComputeVerticalScrollRange(int first, int last);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.LayoutManager.ComputeVerticalScrollRange(int,int).first'></a>

`first` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The first realized item index.

<a name='Tizen.UI.Components.Recycler.LayoutManager.ComputeVerticalScrollRange(int,int).last'></a>

`last` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The last realized item index.

#### Returns
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')  
The vertical scroll range.

<a name='Tizen.UI.Components.Recycler.LayoutManager.Initialize()'></a>

## LayoutManager.Initialize() Method

Initialize the layout manager. This method is called when the layout manager is attached to the recycler view or data source is changed.

```csharp
public abstract void Initialize();
```

<a name='Tizen.UI.Components.Recycler.LayoutManager.LayoutPosition(int)'></a>

## LayoutManager.LayoutPosition(int) Method

Resets all created items and places the item in the specified position on the top left

```csharp
public abstract void LayoutPosition(int position);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.LayoutManager.LayoutPosition(int).position'></a>

`position` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The position of the view item to layout.

<a name='Tizen.UI.Components.Recycler.LayoutManager.MeasureUpdate(Tizen.UI.View)'></a>

## LayoutManager.MeasureUpdate(View) Method

Measure the size of the view item.

```csharp
public abstract Tizen.UI.Size MeasureUpdate(Tizen.UI.View itemView);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.LayoutManager.MeasureUpdate(Tizen.UI.View).itemView'></a>

`itemView` [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')

The view item to measure.

#### Returns
[Tizen.UI.Size](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Size 'Tizen.UI.Size')  
The measured size of the view item.

<a name='Tizen.UI.Components.Recycler.LayoutManager.OnChildrenChanged(System.Collections.Specialized.NotifyCollectionChangedEventArgs)'></a>

## LayoutManager.OnChildrenChanged(NotifyCollectionChangedEventArgs) Method

Called when change the chlidren of the recycler view.

```csharp
public abstract void OnChildrenChanged(System.Collections.Specialized.NotifyCollectionChangedEventArgs e);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.LayoutManager.OnChildrenChanged(System.Collections.Specialized.NotifyCollectionChangedEventArgs).e'></a>

`e` [System.Collections.Specialized.NotifyCollectionChangedEventArgs](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Specialized.NotifyCollectionChangedEventArgs 'System.Collections.Specialized.NotifyCollectionChangedEventArgs')

Collection changed

<a name='Tizen.UI.Components.Recycler.LayoutManager.OnLayoutChildren()'></a>

## LayoutManager.OnLayoutChildren() Method

Called when layout the children of the recycler view.

```csharp
public abstract void OnLayoutChildren();
```

<a name='Tizen.UI.Components.Recycler.LayoutManager.RecycleOutOfSightView()'></a>

## LayoutManager.RecycleOutOfSightView() Method

Recycle the out of sight view items. This method will remove all the views that are not visible anymore from the recycler view.  
These views will be recycled and can be reused by the adapter.  
This method should be called whenever the view port has changed. For example after scrolling or resizing the recycler view.

```csharp
public abstract void RecycleOutOfSightView();
```

<a name='Tizen.UI.Components.Recycler.LayoutManager.ScrollHorizontallyBy(int)'></a>

## LayoutManager.ScrollHorizontallyBy(int) Method

Layouts items to fill the requested direction.

```csharp
public abstract int ScrollHorizontallyBy(int dx);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.LayoutManager.ScrollHorizontallyBy(int).dx'></a>

`dx` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The amount of pixels to scroll by.

#### Returns
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')  
layouted size

<a name='Tizen.UI.Components.Recycler.LayoutManager.ScrollVerticallyBy(int)'></a>

## LayoutManager.ScrollVerticallyBy(int) Method

Layouts items to fill the requested direction.

```csharp
public abstract int ScrollVerticallyBy(int dy);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.LayoutManager.ScrollVerticallyBy(int).dy'></a>

`dy` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The amount of pixels to scroll by.

#### Returns
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')  
layouted size


























































