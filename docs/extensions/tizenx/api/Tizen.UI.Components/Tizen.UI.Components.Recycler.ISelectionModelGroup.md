### [Tizen.UI.Components.Recycler](Tizen.UI.Components.Recycler.md 'Tizen.UI.Components.Recycler')

## ISelectionModelGroup Interface

An interface for the group collection of [ISelectableModel](Tizen.UI.Components.Recycler.ISelectableModel.md 'Tizen.UI.Components.Recycler.ISelectableModel').  
The group can have multiple selected children.

```csharp
public interface ISelectionModelGroup :
System.Collections.IList,
System.Collections.ICollection,
System.Collections.IEnumerable
```

Derived  
&#8627; [ISelectionModelGroup&lt;T&gt;](Tizen.UI.Components.Recycler.ISelectionModelGroup_T_.md 'Tizen.UI.Components.Recycler.ISelectionModelGroup&lt;T>')  
&#8627; [SelectionModelGroup&lt;T&gt;](Tizen.UI.Components.Recycler.SelectionModelGroup_T_.md 'Tizen.UI.Components.Recycler.SelectionModelGroup&lt;T>')

Implements [System.Collections.IList](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.IList 'System.Collections.IList'), [System.Collections.ICollection](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.ICollection 'System.Collections.ICollection'), [System.Collections.IEnumerable](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.IEnumerable 'System.Collections.IEnumerable')
### Properties

<a name='Tizen.UI.Components.Recycler.ISelectionModelGroup.SelectedCount'></a>

## ISelectionModelGroup.SelectedCount Property

The count of the selected children.

```csharp
int SelectedCount { get; }
```

#### Property Value
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')


























































