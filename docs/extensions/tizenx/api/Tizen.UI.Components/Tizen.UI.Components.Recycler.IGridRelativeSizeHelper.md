### [Tizen.UI.Components.Recycler](Tizen.UI.Components.Recycler.md 'Tizen.UI.Components.Recycler')

## IGridRelativeSizeHelper Interface

Interface for [GridView](https://docs.microsoft.com/en-us/dotnet/api/GridView 'GridView') sizing item by aspect ratio.

```csharp
public interface IGridRelativeSizeHelper :
Tizen.UI.Components.Recycler.IItemDecoration
```

Implements [IItemDecoration](Tizen.UI.Components.Recycler.IItemDecoration.md 'Tizen.UI.Components.Recycler.IItemDecoration')
### Methods

<a name='Tizen.UI.Components.Recycler.IGridRelativeSizeHelper.GetAspectRatio(Tizen.UI.View,int,Tizen.UI.Components.Recycler.RecyclerView)'></a>

## IGridRelativeSizeHelper.GetAspectRatio(View, int, RecyclerView) Method

Gets the aspect ratio of the item at the given position. The length of item on scroll-cross-axis will be determined by span size,  
but if scroll-axis also want to be determined by span size, use aspect ratio.  
By default, ratio is 0, measured size will be the length of item on scroll-axis.

```csharp
float GetAspectRatio(Tizen.UI.View view, int position, Tizen.UI.Components.Recycler.RecyclerView recyclerView);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.IGridRelativeSizeHelper.GetAspectRatio(Tizen.UI.View,int,Tizen.UI.Components.Recycler.RecyclerView).view'></a>

`view` [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')

<a name='Tizen.UI.Components.Recycler.IGridRelativeSizeHelper.GetAspectRatio(Tizen.UI.View,int,Tizen.UI.Components.Recycler.RecyclerView).position'></a>

`position` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The index poisition of item.

<a name='Tizen.UI.Components.Recycler.IGridRelativeSizeHelper.GetAspectRatio(Tizen.UI.View,int,Tizen.UI.Components.Recycler.RecyclerView).recyclerView'></a>

`recyclerView` [RecyclerView](Tizen.UI.Components.Recycler.RecyclerView.md 'Tizen.UI.Components.Recycler.RecyclerView')

#### Returns
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')  
The aspect ratio of item.


























































