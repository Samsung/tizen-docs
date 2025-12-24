### [Tizen.UI.Components.Recycler](Tizen.UI.Components.Recycler.md 'Tizen.UI.Components.Recycler')

## GroupItemTemplateAdapter Class

The apdater using ViewTemplate for creates items and groups.

```csharp
public class GroupItemTemplateAdapter : Tizen.UI.Components.Recycler.ItemTemplateAdapter,
Tizen.UI.Components.Recycler.IGroupedAdapter
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [Adapter](Tizen.UI.Components.Recycler.Adapter.md 'Tizen.UI.Components.Recycler.Adapter') &#129106; [ItemTemplateAdapter](Tizen.UI.Components.Recycler.ItemTemplateAdapter.md 'Tizen.UI.Components.Recycler.ItemTemplateAdapter') &#129106; GroupItemTemplateAdapter

Implements [IGroupedAdapter](Tizen.UI.Components.Recycler.IGroupedAdapter.md 'Tizen.UI.Components.Recycler.IGroupedAdapter')
### Constructors

<a name='Tizen.UI.Components.Recycler.GroupItemTemplateAdapter.GroupItemTemplateAdapter()'></a>

## GroupItemTemplateAdapter() Constructor

Constructor for GroupItemTemplateAdapter.

```csharp
public GroupItemTemplateAdapter();
```
### Properties

<a name='Tizen.UI.Components.Recycler.GroupItemTemplateAdapter.GroupBodyTemplate'></a>

## GroupItemTemplateAdapter.GroupBodyTemplate Property

Template for the group body.

```csharp
public Tizen.UI.ViewTemplate GroupBodyTemplate { get; set; }
```

#### Property Value
Tizen.UI.ViewTemplate

<a name='Tizen.UI.Components.Recycler.GroupItemTemplateAdapter.GroupCount'></a>

## GroupItemTemplateAdapter.GroupCount Property

The count of groups.

```csharp
public int GroupCount { get; }
```

Implements [GroupCount](Tizen.UI.Components.Recycler.IGroupedAdapter.md#Tizen.UI.Components.Recycler.IGroupedAdapter.GroupCount 'Tizen.UI.Components.Recycler.IGroupedAdapter.GroupCount')

#### Property Value
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

<a name='Tizen.UI.Components.Recycler.GroupItemTemplateAdapter.GroupFooterTemplate'></a>

## GroupItemTemplateAdapter.GroupFooterTemplate Property

Template for the group footer.

```csharp
public Tizen.UI.ViewTemplate GroupFooterTemplate { get; set; }
```

#### Property Value
Tizen.UI.ViewTemplate

<a name='Tizen.UI.Components.Recycler.GroupItemTemplateAdapter.GroupHeaderTemplate'></a>

## GroupItemTemplateAdapter.GroupHeaderTemplate Property

Template for the group header.

```csharp
public Tizen.UI.ViewTemplate GroupHeaderTemplate { get; set; }
```

#### Property Value
Tizen.UI.ViewTemplate

<a name='Tizen.UI.Components.Recycler.GroupItemTemplateAdapter.HasGroupBody'></a>

## GroupItemTemplateAdapter.HasGroupBody Property

Boolean flag to indicate whether the group has body or not.  
If it is true, the group will have a body view. Otherwise, the group will only have children views. Default value is false.

```csharp
public bool HasGroupBody { get; }
```

Implements [HasGroupBody](Tizen.UI.Components.Recycler.IGroupedAdapter.md#Tizen.UI.Components.Recycler.IGroupedAdapter.HasGroupBody 'Tizen.UI.Components.Recycler.IGroupedAdapter.HasGroupBody')

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.Recycler.GroupItemTemplateAdapter.IsStickyHeader'></a>

## GroupItemTemplateAdapter.IsStickyHeader Property

Boolean flag to determine whether the header is sticky or not. Default is false.

```csharp
public bool IsStickyHeader { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')
### Methods

<a name='Tizen.UI.Components.Recycler.GroupItemTemplateAdapter.BindBodyHolder(Tizen.UI.Components.Recycler.ViewHolder,int)'></a>

## GroupItemTemplateAdapter.BindBodyHolder(ViewHolder, int) Method

Bind the group's body view holder.

```csharp
public virtual void BindBodyHolder(Tizen.UI.Components.Recycler.ViewHolder holder, int group);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.GroupItemTemplateAdapter.BindBodyHolder(Tizen.UI.Components.Recycler.ViewHolder,int).holder'></a>

`holder` [ViewHolder](Tizen.UI.Components.Recycler.ViewHolder.md 'Tizen.UI.Components.Recycler.ViewHolder')

View holder for group body.

<a name='Tizen.UI.Components.Recycler.GroupItemTemplateAdapter.BindBodyHolder(Tizen.UI.Components.Recycler.ViewHolder,int).group'></a>

`group` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The group index.

Implements [BindBodyHolder(ViewHolder, int)](Tizen.UI.Components.Recycler.IGroupedAdapter.md#Tizen.UI.Components.Recycler.IGroupedAdapter.BindBodyHolder(Tizen.UI.Components.Recycler.ViewHolder,int) 'Tizen.UI.Components.Recycler.IGroupedAdapter.BindBodyHolder(Tizen.UI.Components.Recycler.ViewHolder, int)')

<a name='Tizen.UI.Components.Recycler.GroupItemTemplateAdapter.CreateBody(int)'></a>

## GroupItemTemplateAdapter.CreateBody(int) Method

Create the group's body view holder.

```csharp
public virtual Tizen.UI.Components.Recycler.ViewHolder CreateBody(int type);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.GroupItemTemplateAdapter.CreateBody(int).type'></a>

`type` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The type of group body.

Implements [CreateBody(int)](Tizen.UI.Components.Recycler.IGroupedAdapter.md#Tizen.UI.Components.Recycler.IGroupedAdapter.CreateBody(int) 'Tizen.UI.Components.Recycler.IGroupedAdapter.CreateBody(int)')

#### Returns
[ViewHolder](Tizen.UI.Components.Recycler.ViewHolder.md 'Tizen.UI.Components.Recycler.ViewHolder')  
View holder for group body.

<a name='Tizen.UI.Components.Recycler.GroupItemTemplateAdapter.GetBodyType(int)'></a>

## GroupItemTemplateAdapter.GetBodyType(int) Method

Get the group body's type.

```csharp
public virtual int GetBodyType(int group);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.GroupItemTemplateAdapter.GetBodyType(int).group'></a>

`group` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The group index.

Implements [GetBodyType(int)](Tizen.UI.Components.Recycler.IGroupedAdapter.md#Tizen.UI.Components.Recycler.IGroupedAdapter.GetBodyType(int) 'Tizen.UI.Components.Recycler.IGroupedAdapter.GetBodyType(int)')

#### Returns
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')  
Body type.

<a name='Tizen.UI.Components.Recycler.GroupItemTemplateAdapter.GetChildrenCount(int)'></a>

## GroupItemTemplateAdapter.GetChildrenCount(int) Method

Get the child items count of the group.

```csharp
public virtual int GetChildrenCount(int group);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.GroupItemTemplateAdapter.GetChildrenCount(int).group'></a>

`group` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The group index.

Implements [GetChildrenCount(int)](Tizen.UI.Components.Recycler.IGroupedAdapter.md#Tizen.UI.Components.Recycler.IGroupedAdapter.GetChildrenCount(int) 'Tizen.UI.Components.Recycler.IGroupedAdapter.GetChildrenCount(int)')

#### Returns
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')  
The count of group children.

<a name='Tizen.UI.Components.Recycler.GroupItemTemplateAdapter.GetGroupAndIndex(int)'></a>

## GroupItemTemplateAdapter.GetGroupAndIndex(int) Method

Get the group index and item index in the group.

```csharp
public virtual (int groupIndex,int inGroupIndex) GetGroupAndIndex(int position);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.GroupItemTemplateAdapter.GetGroupAndIndex(int).position'></a>

`position` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The index position of item.

Implements [GetGroupAndIndex(int)](Tizen.UI.Components.Recycler.IGroupedAdapter.md#Tizen.UI.Components.Recycler.IGroupedAdapter.GetGroupAndIndex(int) 'Tizen.UI.Components.Recycler.IGroupedAdapter.GetGroupAndIndex(int)')

#### Returns
[&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.ValueTuple 'System.ValueTuple')[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')[,](https://docs.microsoft.com/en-us/dotnet/api/System.ValueTuple 'System.ValueTuple')[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.ValueTuple 'System.ValueTuple')  
Group index and item's index in the group.

<a name='Tizen.UI.Components.Recycler.GroupItemTemplateAdapter.GetGroupItem(int)'></a>

## GroupItemTemplateAdapter.GetGroupItem(int) Method

Get the group item.

```csharp
public virtual object GetGroupItem(int group);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.GroupItemTemplateAdapter.GetGroupItem(int).group'></a>

`group` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

Group index.

Implements [GetGroupItem(int)](Tizen.UI.Components.Recycler.IGroupedAdapter.md#Tizen.UI.Components.Recycler.IGroupedAdapter.GetGroupItem(int) 'Tizen.UI.Components.Recycler.IGroupedAdapter.GetGroupItem(int)')

#### Returns
[System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object')  
Group item object.

<a name='Tizen.UI.Components.Recycler.GroupItemTemplateAdapter.GetItemViewType(int)'></a>

## GroupItemTemplateAdapter.GetItemViewType(int) Method

Get the type of View that will be created by [OnCreateViewHolder(int)](Tizen.UI.Components.Recycler.Adapter.md#Tizen.UI.Components.Recycler.Adapter.OnCreateViewHolder(int) 'Tizen.UI.Components.Recycler.Adapter.OnCreateViewHolder(int)') for the specified item.

```csharp
public override int GetItemViewType(int position);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.GroupItemTemplateAdapter.GetItemViewType(int).position'></a>

`position` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The position of the item within the adapter's data set

#### Returns
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

<a name='Tizen.UI.Components.Recycler.GroupItemTemplateAdapter.IsSticky(int)'></a>

## GroupItemTemplateAdapter.IsSticky(int) Method

Called when RecyclerView need to determine whether the item is sticky or not.  
If it returns true, the item will be sticked. Otherwise, it will not be sticked.

```csharp
public override bool IsSticky(int position);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.GroupItemTemplateAdapter.IsSticky(int).position'></a>

`position` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The position of data.

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.Recycler.GroupItemTemplateAdapter.SetItemsSource(System.Collections.IEnumerable)'></a>

## GroupItemTemplateAdapter.SetItemsSource(IEnumerable) Method

Set the items source.

```csharp
public override void SetItemsSource(System.Collections.IEnumerable items);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.GroupItemTemplateAdapter.SetItemsSource(System.Collections.IEnumerable).items'></a>

`items` [System.Collections.IEnumerable](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.IEnumerable 'System.Collections.IEnumerable')

Enumerable source.



























































