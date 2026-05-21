### [Tizen.UI.Components.Recycler](Tizen.UI.Components.Recycler.md 'Tizen.UI.Components.Recycler')

## IGroupedItem Interface

Interface for grouped item.  
This interface is not mendatory to implement, but if you want to update the item's by the group position, you can use this interface.

```csharp
public interface IGroupedItem
```
### Properties

<a name='Tizen.UI.Components.Recycler.IGroupedItem.IsFirstOfGroup'></a>

## IGroupedItem.IsFirstOfGroup Property

Boolean flag that indicates whether this item is first of group or not.

```csharp
bool IsFirstOfGroup { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.Recycler.IGroupedItem.IsLastOfGroup'></a>

## IGroupedItem.IsLastOfGroup Property

Boolean flag that indicates whether this item is last of group or not.

```csharp
bool IsLastOfGroup { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')
### Methods

<a name='Tizen.UI.Components.Recycler.IGroupedItem.UpdateByPosition(int)'></a>

## IGroupedItem.UpdateByPosition(int) Method

Update the item by the group position.

```csharp
void UpdateByPosition(int position);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.IGroupedItem.UpdateByPosition(int).position'></a>

`position` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The index position of item.


























































