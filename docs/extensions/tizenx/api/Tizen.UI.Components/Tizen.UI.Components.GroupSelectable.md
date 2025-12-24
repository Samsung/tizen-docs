### [Tizen.UI.Components](Tizen.UI.Components.md 'Tizen.UI.Components')

## GroupSelectable Class

Group selectable component is a component that can be selected among the [SelectionGroup](Tizen.UI.Components.SelectionGroup.md 'Tizen.UI.Components.SelectionGroup').

```csharp
public class GroupSelectable : Tizen.UI.Components.Selectable,
Tizen.UI.Components.IGroupSelectable,
Tizen.UI.Components.ISelectable
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; Tizen.UI.NObject &#129106; Tizen.UI.View &#129106; Tizen.UI.ContentView &#129106; [Pressable](Tizen.UI.Components.Pressable.md 'Tizen.UI.Components.Pressable') &#129106; [Clickable](Tizen.UI.Components.Clickable.md 'Tizen.UI.Components.Clickable') &#129106; [Selectable](Tizen.UI.Components.Selectable.md 'Tizen.UI.Components.Selectable') &#129106; GroupSelectable

Derived  
&#8627; [GroupSelectableBox](Tizen.UI.Components.GroupSelectableBox.md 'Tizen.UI.Components.GroupSelectableBox')

Implements [IGroupSelectable](Tizen.UI.Components.IGroupSelectable.md 'Tizen.UI.Components.IGroupSelectable'), [ISelectable](Tizen.UI.Components.ISelectable.md 'Tizen.UI.Components.ISelectable')
### Constructors

<a name='Tizen.UI.Components.GroupSelectable.GroupSelectable()'></a>

## GroupSelectable() Constructor

Constructs a new group selectable.

```csharp
public GroupSelectable();
```
### Properties

<a name='Tizen.UI.Components.GroupSelectable.Group'></a>

## GroupSelectable.Group Property

The group of selectable.

```csharp
public Tizen.UI.Components.SelectionGroup Group { get; }
```

Implements [Group](Tizen.UI.Components.IGroupSelectable.md#Tizen.UI.Components.IGroupSelectable.Group 'Tizen.UI.Components.IGroupSelectable.Group')

#### Property Value
[SelectionGroup](Tizen.UI.Components.SelectionGroup.md 'Tizen.UI.Components.SelectionGroup')

<a name='Tizen.UI.Components.GroupSelectable.GroupName'></a>

## GroupSelectable.GroupName Property

The name of [SelectionGroup](Tizen.UI.Components.SelectionGroup.md 'Tizen.UI.Components.SelectionGroup').

```csharp
public string GroupName { get; set; }
```

Implements [GroupName](Tizen.UI.Components.IGroupSelectable.md#Tizen.UI.Components.IGroupSelectable.GroupName 'Tizen.UI.Components.IGroupSelectable.GroupName')

#### Property Value
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.Components.GroupSelectable.IsGrouped'></a>

## GroupSelectable.IsGrouped Property

Boolean value indicating whether the group selectable is grouped.

```csharp
public bool IsGrouped { get; }
```

Implements [IsGrouped](Tizen.UI.Components.IGroupSelectable.md#Tizen.UI.Components.IGroupSelectable.IsGrouped 'Tizen.UI.Components.IGroupSelectable.IsGrouped')

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')



























































