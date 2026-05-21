### [Tizen.UI.Components](Tizen.UI.Components.md 'Tizen.UI.Components')

## ISelectionGroup Interface

Interface for a group of [IGroupSelectable](Tizen.UI.Components.IGroupSelectable.md 'Tizen.UI.Components.IGroupSelectable').

```csharp
public interface ISelectionGroup
```

Derived  
&#8627; [SelectionGroup](Tizen.UI.Components.SelectionGroup.md 'Tizen.UI.Components.SelectionGroup')  
&#8627; [SelectionGroupBox&lt;T&gt;](Tizen.UI.Components.SelectionGroupBox_T_.md 'Tizen.UI.Components.SelectionGroupBox&lt;T>')
### Properties

<a name='Tizen.UI.Components.ISelectionGroup.Selected'></a>

## ISelectionGroup.Selected Property

The selected child in the group.

```csharp
Tizen.UI.Components.IGroupSelectable Selected { get; }
```

#### Property Value
[IGroupSelectable](Tizen.UI.Components.IGroupSelectable.md 'Tizen.UI.Components.IGroupSelectable')
### Events

<a name='Tizen.UI.Components.ISelectionGroup.SelectionChanged'></a>

## ISelectionGroup.SelectionChanged Event

Occures when the selected item is changed.

```csharp
event EventHandler&lt;GroupSelectionChangedEventArgs> SelectionChanged;
```

#### Event Type
[System.EventHandler&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')[GroupSelectionChangedEventArgs](Tizen.UI.Components.GroupSelectionChangedEventArgs.md 'Tizen.UI.Components.GroupSelectionChangedEventArgs')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')


























































