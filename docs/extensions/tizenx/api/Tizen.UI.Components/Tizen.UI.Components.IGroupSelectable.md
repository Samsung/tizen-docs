### [Tizen.UI.Components](Tizen.UI.Components.md 'Tizen.UI.Components')

## IGroupSelectable Interface

Represents group selectable element.  
[SelectionGroup](Tizen.UI.Components.SelectionGroup.md 'Tizen.UI.Components.SelectionGroup') can control the selection of group selectable.

```csharp
public interface IGroupSelectable :
Tizen.UI.Components.ISelectable
```

Derived  
&#8627; [GroupSelectable](Tizen.UI.Components.GroupSelectable.md 'Tizen.UI.Components.GroupSelectable')

Implements [ISelectable](Tizen.UI.Components.ISelectable.md 'Tizen.UI.Components.ISelectable')
### Properties

<a name='Tizen.UI.Components.IGroupSelectable.Group'></a>

## IGroupSelectable.Group Property

The group of selectable.

```csharp
Tizen.UI.Components.SelectionGroup Group { get; }
```

#### Property Value
[SelectionGroup](Tizen.UI.Components.SelectionGroup.md 'Tizen.UI.Components.SelectionGroup')

<a name='Tizen.UI.Components.IGroupSelectable.GroupName'></a>

## IGroupSelectable.GroupName Property

The name of [SelectionGroup](Tizen.UI.Components.SelectionGroup.md 'Tizen.UI.Components.SelectionGroup').

```csharp
string GroupName { get; set; }
```

#### Property Value
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.Components.IGroupSelectable.IsGrouped'></a>

## IGroupSelectable.IsGrouped Property

Boolean value indicating whether the group selectable is grouped.

```csharp
bool IsGrouped { get; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.IGroupSelectable.Name'></a>

## IGroupSelectable.Name Property

Name of group selectable.

```csharp
string Name { get; }
```

#### Property Value
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')


























































