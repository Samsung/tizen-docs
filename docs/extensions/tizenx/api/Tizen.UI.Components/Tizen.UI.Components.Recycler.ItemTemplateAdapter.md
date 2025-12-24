### [Tizen.UI.Components.Recycler](Tizen.UI.Components.Recycler.md 'Tizen.UI.Components.Recycler')

## ItemTemplateAdapter Class

The apdater using ViewTemplate for creates items.

```csharp
public class ItemTemplateAdapter : Tizen.UI.Components.Recycler.Adapter,
Tizen.UI.Components.Recycler.IDividerProvider
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [Adapter](Tizen.UI.Components.Recycler.Adapter.md 'Tizen.UI.Components.Recycler.Adapter') &#129106; ItemTemplateAdapter

Derived  
&#8627; [GroupItemTemplateAdapter](Tizen.UI.Components.Recycler.GroupItemTemplateAdapter.md 'Tizen.UI.Components.Recycler.GroupItemTemplateAdapter')

Implements [IDividerProvider](Tizen.UI.Components.Recycler.IDividerProvider.md 'Tizen.UI.Components.Recycler.IDividerProvider')
### Constructors

<a name='Tizen.UI.Components.Recycler.ItemTemplateAdapter.ItemTemplateAdapter()'></a>

## ItemTemplateAdapter() Constructor

Constructor for ItemTemplateAdapter.

```csharp
public ItemTemplateAdapter();
```
### Properties

<a name='Tizen.UI.Components.Recycler.ItemTemplateAdapter.DividerTemplate'></a>

## ItemTemplateAdapter.DividerTemplate Property

The template for creating divider views. It can be ViewTemplate or ViewTemplateSelector.

```csharp
public Tizen.UI.ViewTemplate DividerTemplate { get; set; }
```

#### Property Value
Tizen.UI.ViewTemplate

<a name='Tizen.UI.Components.Recycler.ItemTemplateAdapter.HasDivider'></a>

## ItemTemplateAdapter.HasDivider Property

The flag that indicates whether the adapter has a divider or not.

```csharp
public bool HasDivider { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.Recycler.ItemTemplateAdapter.ItemCount'></a>

## ItemTemplateAdapter.ItemCount Property

The count of items.

```csharp
public override int ItemCount { get; }
```

#### Property Value
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

<a name='Tizen.UI.Components.Recycler.ItemTemplateAdapter.ItemsSource'></a>

## ItemTemplateAdapter.ItemsSource Property

The enumerable data source of items.  
Use INotifyCollectionChanged to observe the changes of collection.

```csharp
public System.Collections.IEnumerable ItemsSource { get; set; }
```

#### Property Value
[System.Collections.IEnumerable](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.IEnumerable 'System.Collections.IEnumerable')

<a name='Tizen.UI.Components.Recycler.ItemTemplateAdapter.ItemTemplate'></a>

## ItemTemplateAdapter.ItemTemplate Property

The template for creating item views. It can be ViewTemplate or ViewTemplateSelector.

```csharp
public Tizen.UI.ViewTemplate ItemTemplate { get; set; }
```

#### Property Value
Tizen.UI.ViewTemplate
### Methods

<a name='Tizen.UI.Components.Recycler.ItemTemplateAdapter.GetItemOnPosition(int)'></a>

## ItemTemplateAdapter.GetItemOnPosition(int) Method

Get item object from position.

```csharp
public override object GetItemOnPosition(int position);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.ItemTemplateAdapter.GetItemOnPosition(int).position'></a>

`position` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The index position of item.

#### Returns
[System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object')  
The item object.

<a name='Tizen.UI.Components.Recycler.ItemTemplateAdapter.GetItemViewType(int)'></a>

## ItemTemplateAdapter.GetItemViewType(int) Method

Get the type of View that will be created by [OnCreateViewHolder(int)](Tizen.UI.Components.Recycler.Adapter.md#Tizen.UI.Components.Recycler.Adapter.OnCreateViewHolder(int) 'Tizen.UI.Components.Recycler.Adapter.OnCreateViewHolder(int)') for the specified item.

```csharp
public override int GetItemViewType(int position);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.ItemTemplateAdapter.GetItemViewType(int).position'></a>

`position` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The position of the item within the adapter's data set

#### Returns
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

<a name='Tizen.UI.Components.Recycler.ItemTemplateAdapter.GetSourceIndexFromPosition(int)'></a>

## ItemTemplateAdapter.GetSourceIndexFromPosition(int) Method

Get the index of source from position. If there is no divider, it returns the same value. If there is divider, it returns the index without divider.

```csharp
public int GetSourceIndexFromPosition(int position);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.ItemTemplateAdapter.GetSourceIndexFromPosition(int).position'></a>

`position` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The index position of item.

#### Returns
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')  
The original source index.

<a name='Tizen.UI.Components.Recycler.ItemTemplateAdapter.IsDividerPosition(int)'></a>

## ItemTemplateAdapter.IsDividerPosition(int) Method

Check the position is divider position or not.

```csharp
public virtual bool IsDividerPosition(int position);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.ItemTemplateAdapter.IsDividerPosition(int).position'></a>

`position` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The index position of item.

Implements [IsDividerPosition(int)](Tizen.UI.Components.Recycler.IDividerProvider.md#Tizen.UI.Components.Recycler.IDividerProvider.IsDividerPosition(int) 'Tizen.UI.Components.Recycler.IDividerProvider.IsDividerPosition(int)')

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
True if the position is divider position, otherwise false.

<a name='Tizen.UI.Components.Recycler.ItemTemplateAdapter.OnBindViewHolder(Tizen.UI.Components.Recycler.ViewHolder,int)'></a>

## ItemTemplateAdapter.OnBindViewHolder(ViewHolder, int) Method

Called when [BindViewHolder(ViewHolder, int)](Tizen.UI.Components.Recycler.Adapter.md#Tizen.UI.Components.Recycler.Adapter.BindViewHolder(Tizen.UI.Components.Recycler.ViewHolder,int) 'Tizen.UI.Components.Recycler.Adapter.BindViewHolder(Tizen.UI.Components.Recycler.ViewHolder, int)') binds [ViewHolder](Tizen.UI.Components.Recycler.ViewHolder.md 'Tizen.UI.Components.Recycler.ViewHolder').  
Derivated class must implement this method to bind viewholder.

```csharp
public override void OnBindViewHolder(Tizen.UI.Components.Recycler.ViewHolder holder, int position);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.ItemTemplateAdapter.OnBindViewHolder(Tizen.UI.Components.Recycler.ViewHolder,int).holder'></a>

`holder` [ViewHolder](Tizen.UI.Components.Recycler.ViewHolder.md 'Tizen.UI.Components.Recycler.ViewHolder')

The view holder to bind.

<a name='Tizen.UI.Components.Recycler.ItemTemplateAdapter.OnBindViewHolder(Tizen.UI.Components.Recycler.ViewHolder,int).position'></a>

`position` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The position of data.

<a name='Tizen.UI.Components.Recycler.ItemTemplateAdapter.OnCreateViewHolder(int)'></a>

## ItemTemplateAdapter.OnCreateViewHolder(int) Method

Called when [CreateViewHolder(int)](Tizen.UI.Components.Recycler.Adapter.md#Tizen.UI.Components.Recycler.Adapter.CreateViewHolder(int) 'Tizen.UI.Components.Recycler.Adapter.CreateViewHolder(int)') creates [ViewHolder](Tizen.UI.Components.Recycler.ViewHolder.md 'Tizen.UI.Components.Recycler.ViewHolder').  
Derivated class must implement this method to create viewholder.

```csharp
public override Tizen.UI.Components.Recycler.ViewHolder OnCreateViewHolder(int viewType);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.ItemTemplateAdapter.OnCreateViewHolder(int).viewType'></a>

`viewType` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The type of the view.

#### Returns
[ViewHolder](Tizen.UI.Components.Recycler.ViewHolder.md 'Tizen.UI.Components.Recycler.ViewHolder')

<a name='Tizen.UI.Components.Recycler.ItemTemplateAdapter.SetItemsSource(System.Collections.IEnumerable)'></a>

## ItemTemplateAdapter.SetItemsSource(IEnumerable) Method

Set the items source.

```csharp
public virtual void SetItemsSource(System.Collections.IEnumerable items);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.ItemTemplateAdapter.SetItemsSource(System.Collections.IEnumerable).items'></a>

`items` [System.Collections.IEnumerable](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.IEnumerable 'System.Collections.IEnumerable')

Enumerable source.



























































