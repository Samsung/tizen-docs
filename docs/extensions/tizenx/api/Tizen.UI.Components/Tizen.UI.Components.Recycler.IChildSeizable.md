### [Tizen.UI.Components.Recycler](Tizen.UI.Components.Recycler.md 'Tizen.UI.Components.Recycler')

## IChildSeizable Interface

Interface that Layouter child can be seized and un-handled by layouter or recycled.  
This interface will be used on [ItemTouchHelper](Tizen.UI.Components.Recycler.ItemTouchHelper.md 'Tizen.UI.Components.Recycler.ItemTouchHelper').

```csharp
public interface IChildSeizable
```

Derived  
&#8627; [LinearLayoutManager](Tizen.UI.Components.Recycler.LinearLayoutManager.md 'Tizen.UI.Components.Recycler.LinearLayoutManager')
### Methods

<a name='Tizen.UI.Components.Recycler.IChildSeizable.GetSeized(int)'></a>

## IChildSeizable.GetSeized(int) Method

Get seized item view holder.

```csharp
Tizen.UI.Components.Recycler.ViewHolder GetSeized(int position);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.IChildSeizable.GetSeized(int).position'></a>

`position` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The item position.

#### Returns
[ViewHolder](Tizen.UI.Components.Recycler.ViewHolder.md 'Tizen.UI.Components.Recycler.ViewHolder')  
seized view holder.

<a name='Tizen.UI.Components.Recycler.IChildSeizable.GetSeizedCount()'></a>

## IChildSeizable.GetSeizedCount() Method

Get the count of seized item.

```csharp
int GetSeizedCount();
```

#### Returns
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')  
seized item count.

<a name='Tizen.UI.Components.Recycler.IChildSeizable.IsSeized(int)'></a>

## IChildSeizable.IsSeized(int) Method

Check whether this item is seized or not.

```csharp
bool IsSeized(int position);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.IChildSeizable.IsSeized(int).position'></a>

`position` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The item position.

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
true if position item is seized.

<a name='Tizen.UI.Components.Recycler.IChildSeizable.ReleaseChild(Tizen.UI.Components.Recycler.ViewHolder)'></a>

## IChildSeizable.ReleaseChild(ViewHolder) Method

Release the view holder.  
view holder is released from user, will be re-layout, recycled from now on.

```csharp
void ReleaseChild(Tizen.UI.Components.Recycler.ViewHolder viewHolder);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.IChildSeizable.ReleaseChild(Tizen.UI.Components.Recycler.ViewHolder).viewHolder'></a>

`viewHolder` [ViewHolder](Tizen.UI.Components.Recycler.ViewHolder.md 'Tizen.UI.Components.Recycler.ViewHolder')

The viewholer to be released.

<a name='Tizen.UI.Components.Recycler.IChildSeizable.SeizeChild(Tizen.UI.Components.Recycler.ViewHolder)'></a>

## IChildSeizable.SeizeChild(ViewHolder) Method

Seize the view holder.  
view holder is seized by user, will not be re-layout, recycled until it is released.

```csharp
void SeizeChild(Tizen.UI.Components.Recycler.ViewHolder viewHolder);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.IChildSeizable.SeizeChild(Tizen.UI.Components.Recycler.ViewHolder).viewHolder'></a>

`viewHolder` [ViewHolder](Tizen.UI.Components.Recycler.ViewHolder.md 'Tizen.UI.Components.Recycler.ViewHolder')

The viewholer to be seized.


























































