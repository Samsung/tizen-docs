### [Tizen.UI.Components.Recycler](Tizen.UI.Components.Recycler.md 'Tizen.UI.Components.Recycler')

## Adapter Class

Adapter provide a binding from an app-specific data set to views that  
are displayed within a [RecyclerView](Tizen.UI.Components.Recycler.Adapter.md#Tizen.UI.Components.Recycler.Adapter.RecyclerView 'Tizen.UI.Components.Recycler.Adapter.RecyclerView').

```csharp
public abstract class Adapter :
System.Collections.Specialized.INotifyCollectionChanged
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; Adapter

Derived  
&#8627; [ItemTemplateAdapter](Tizen.UI.Components.Recycler.ItemTemplateAdapter.md 'Tizen.UI.Components.Recycler.ItemTemplateAdapter')

Implements [System.Collections.Specialized.INotifyCollectionChanged](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Specialized.INotifyCollectionChanged 'System.Collections.Specialized.INotifyCollectionChanged')
### Properties

<a name='Tizen.UI.Components.Recycler.Adapter.ItemCount'></a>

## Adapter.ItemCount Property

The count of items in the data source.

```csharp
public abstract int ItemCount { get; }
```

#### Property Value
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

<a name='Tizen.UI.Components.Recycler.Adapter.RecyclerView'></a>

## Adapter.RecyclerView Property

The recyclerView for adapter.

```csharp
public Tizen.UI.Components.Recycler.RecyclerView RecyclerView { get; set; }
```

#### Property Value
[RecyclerView](Tizen.UI.Components.Recycler.RecyclerView.md 'Tizen.UI.Components.Recycler.RecyclerView')
### Methods

<a name='Tizen.UI.Components.Recycler.Adapter.BindViewHolder(Tizen.UI.Components.Recycler.ViewHolder,int)'></a>

## Adapter.BindViewHolder(ViewHolder, int) Method

Called by RecyclerView to display the data at the specified position.  
This method should update the contents of the [ViewHolder](Tizen.UI.Components.Recycler.ViewHolder.md 'Tizen.UI.Components.Recycler.ViewHolder')  
to reflect the item at the given position

```csharp
public void BindViewHolder(Tizen.UI.Components.Recycler.ViewHolder holder, int position);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.Adapter.BindViewHolder(Tizen.UI.Components.Recycler.ViewHolder,int).holder'></a>

`holder` [ViewHolder](Tizen.UI.Components.Recycler.ViewHolder.md 'Tizen.UI.Components.Recycler.ViewHolder')

The view holder to bind.

<a name='Tizen.UI.Components.Recycler.Adapter.BindViewHolder(Tizen.UI.Components.Recycler.ViewHolder,int).position'></a>

`position` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The position of data.

<a name='Tizen.UI.Components.Recycler.Adapter.CreateViewHolder(int)'></a>

## Adapter.CreateViewHolder(int) Method

Called when RecyclerView needs a new [ViewHolder](Tizen.UI.Components.Recycler.ViewHolder.md 'Tizen.UI.Components.Recycler.ViewHolder') of the given type to represent an item.

```csharp
public Tizen.UI.Components.Recycler.ViewHolder CreateViewHolder(int viewType);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.Adapter.CreateViewHolder(int).viewType'></a>

`viewType` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The type of the view.

#### Returns
[ViewHolder](Tizen.UI.Components.Recycler.ViewHolder.md 'Tizen.UI.Components.Recycler.ViewHolder')

<a name='Tizen.UI.Components.Recycler.Adapter.GetItemOnPosition(int)'></a>

## Adapter.GetItemOnPosition(int) Method

Get item object from position.

```csharp
public abstract object GetItemOnPosition(int position);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.Adapter.GetItemOnPosition(int).position'></a>

`position` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The index position of item.

#### Returns
[System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object')  
The item object.

<a name='Tizen.UI.Components.Recycler.Adapter.GetItemViewType(int)'></a>

## Adapter.GetItemViewType(int) Method

Get the type of View that will be created by [OnCreateViewHolder(int)](Tizen.UI.Components.Recycler.Adapter.md#Tizen.UI.Components.Recycler.Adapter.OnCreateViewHolder(int) 'Tizen.UI.Components.Recycler.Adapter.OnCreateViewHolder(int)') for the specified item.

```csharp
public virtual int GetItemViewType(int position);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.Adapter.GetItemViewType(int).position'></a>

`position` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The position of the item within the adapter's data set

#### Returns
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

<a name='Tizen.UI.Components.Recycler.Adapter.GetViewPosition(Tizen.UI.View)'></a>

## Adapter.GetViewPosition(View) Method

Get the position for the view.

```csharp
public virtual int GetViewPosition(Tizen.UI.View view);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.Adapter.GetViewPosition(Tizen.UI.View).view'></a>

`view` Tizen.UI.View

The view to get the position.

#### Returns
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

<a name='Tizen.UI.Components.Recycler.Adapter.IsSticky(int)'></a>

## Adapter.IsSticky(int) Method

Called when RecyclerView need to determine whether the item is sticky or not.  
If it returns true, the item will be sticked. Otherwise, it will not be sticked.

```csharp
public virtual bool IsSticky(int position);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.Adapter.IsSticky(int).position'></a>

`position` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The position of data.

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.Recycler.Adapter.OnBindViewHolder(Tizen.UI.Components.Recycler.ViewHolder,int)'></a>

## Adapter.OnBindViewHolder(ViewHolder, int) Method

Called when [BindViewHolder(ViewHolder, int)](Tizen.UI.Components.Recycler.Adapter.md#Tizen.UI.Components.Recycler.Adapter.BindViewHolder(Tizen.UI.Components.Recycler.ViewHolder,int) 'Tizen.UI.Components.Recycler.Adapter.BindViewHolder(Tizen.UI.Components.Recycler.ViewHolder, int)') binds [ViewHolder](Tizen.UI.Components.Recycler.ViewHolder.md 'Tizen.UI.Components.Recycler.ViewHolder').  
Derivated class must implement this method to bind viewholder.

```csharp
public abstract void OnBindViewHolder(Tizen.UI.Components.Recycler.ViewHolder holder, int position);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.Adapter.OnBindViewHolder(Tizen.UI.Components.Recycler.ViewHolder,int).holder'></a>

`holder` [ViewHolder](Tizen.UI.Components.Recycler.ViewHolder.md 'Tizen.UI.Components.Recycler.ViewHolder')

The view holder to bind.

<a name='Tizen.UI.Components.Recycler.Adapter.OnBindViewHolder(Tizen.UI.Components.Recycler.ViewHolder,int).position'></a>

`position` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The position of data.

<a name='Tizen.UI.Components.Recycler.Adapter.OnCreateViewHolder(int)'></a>

## Adapter.OnCreateViewHolder(int) Method

Called when [CreateViewHolder(int)](Tizen.UI.Components.Recycler.Adapter.md#Tizen.UI.Components.Recycler.Adapter.CreateViewHolder(int) 'Tizen.UI.Components.Recycler.Adapter.CreateViewHolder(int)') creates [ViewHolder](Tizen.UI.Components.Recycler.ViewHolder.md 'Tizen.UI.Components.Recycler.ViewHolder').  
Derivated class must implement this method to create viewholder.

```csharp
public abstract Tizen.UI.Components.Recycler.ViewHolder OnCreateViewHolder(int viewType);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.Adapter.OnCreateViewHolder(int).viewType'></a>

`viewType` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The type of the view.

#### Returns
[ViewHolder](Tizen.UI.Components.Recycler.ViewHolder.md 'Tizen.UI.Components.Recycler.ViewHolder')
### Events

<a name='Tizen.UI.Components.Recycler.Adapter.CollectionChanged'></a>

## Adapter.CollectionChanged Event

The event that invoked when the collection changes.

```csharp
public event NotifyCollectionChangedEventHandler CollectionChanged;
```

Implements [CollectionChanged](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Specialized.INotifyCollectionChanged.CollectionChanged 'System.Collections.Specialized.INotifyCollectionChanged.CollectionChanged')

#### Event Type
[System.Collections.Specialized.NotifyCollectionChangedEventHandler](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Specialized.NotifyCollectionChangedEventHandler 'System.Collections.Specialized.NotifyCollectionChangedEventHandler')


























































