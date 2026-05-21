### [Tizen.UI.Components.Recycler](Tizen.UI.Components.Recycler.md 'Tizen.UI.Components.Recycler')

## IGroupedAdapter Interface

The interface for a grouped adapter. It is used to provide data for the RecyclerView.

```csharp
public interface IGroupedAdapter
```

Derived  
&#8627; [GroupItemTemplateAdapter](Tizen.UI.Components.Recycler.GroupItemTemplateAdapter.md 'Tizen.UI.Components.Recycler.GroupItemTemplateAdapter')
### Properties

<a name='Tizen.UI.Components.Recycler.IGroupedAdapter.GroupCount'></a>

## IGroupedAdapter.GroupCount Property

The count of groups.

```csharp
int GroupCount { get; }
```

#### Property Value
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

<a name='Tizen.UI.Components.Recycler.IGroupedAdapter.HasGroupBody'></a>

## IGroupedAdapter.HasGroupBody Property

Boolean flag to indicate whether the group has body or not.  
If it is true, the group will have a body view. Otherwise, the group will only have children views. Default value is false.

```csharp
bool HasGroupBody { get; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')
### Methods

<a name='Tizen.UI.Components.Recycler.IGroupedAdapter.BindBodyHolder(Tizen.UI.Components.Recycler.ViewHolder,int)'></a>

## IGroupedAdapter.BindBodyHolder(ViewHolder, int) Method

Bind the group's body view holder.

```csharp
void BindBodyHolder(Tizen.UI.Components.Recycler.ViewHolder holder, int group);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.IGroupedAdapter.BindBodyHolder(Tizen.UI.Components.Recycler.ViewHolder,int).holder'></a>

`holder` [ViewHolder](Tizen.UI.Components.Recycler.ViewHolder.md 'Tizen.UI.Components.Recycler.ViewHolder')

View holder for group body.

<a name='Tizen.UI.Components.Recycler.IGroupedAdapter.BindBodyHolder(Tizen.UI.Components.Recycler.ViewHolder,int).group'></a>

`group` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The group index.

<a name='Tizen.UI.Components.Recycler.IGroupedAdapter.CreateBody(int)'></a>

## IGroupedAdapter.CreateBody(int) Method

Create the group's body view holder.

```csharp
Tizen.UI.Components.Recycler.ViewHolder CreateBody(int type);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.IGroupedAdapter.CreateBody(int).type'></a>

`type` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The type of group body.

#### Returns
[ViewHolder](Tizen.UI.Components.Recycler.ViewHolder.md 'Tizen.UI.Components.Recycler.ViewHolder')  
View holder for group body.

<a name='Tizen.UI.Components.Recycler.IGroupedAdapter.GetBodyType(int)'></a>

## IGroupedAdapter.GetBodyType(int) Method

Get the group body's type.

```csharp
int GetBodyType(int group);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.IGroupedAdapter.GetBodyType(int).group'></a>

`group` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The group index.

#### Returns
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')  
Body type.

<a name='Tizen.UI.Components.Recycler.IGroupedAdapter.GetChildrenCount(int)'></a>

## IGroupedAdapter.GetChildrenCount(int) Method

Get the child items count of the group.

```csharp
int GetChildrenCount(int group);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.IGroupedAdapter.GetChildrenCount(int).group'></a>

`group` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The group index.

#### Returns
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')  
The count of group children.

<a name='Tizen.UI.Components.Recycler.IGroupedAdapter.GetGroupAndIndex(int)'></a>

## IGroupedAdapter.GetGroupAndIndex(int) Method

Get the group index and item index in the group.

```csharp
(int groupIndex,int inGroupIndex) GetGroupAndIndex(int position);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.IGroupedAdapter.GetGroupAndIndex(int).position'></a>

`position` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The index position of item.

#### Returns
[&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.ValueTuple 'System.ValueTuple')[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')[,](https://docs.microsoft.com/en-us/dotnet/api/System.ValueTuple 'System.ValueTuple')[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.ValueTuple 'System.ValueTuple')  
Group index and item's index in the group.

<a name='Tizen.UI.Components.Recycler.IGroupedAdapter.GetGroupItem(int)'></a>

## IGroupedAdapter.GetGroupItem(int) Method

Get the group item.

```csharp
object GetGroupItem(int group);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.IGroupedAdapter.GetGroupItem(int).group'></a>

`group` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

Group index.

#### Returns
[System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object')  
Group item object.


























































