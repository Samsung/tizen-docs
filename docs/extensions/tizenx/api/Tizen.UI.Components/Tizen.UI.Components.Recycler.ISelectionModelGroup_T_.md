### [Tizen.UI.Components.Recycler](Tizen.UI.Components.Recycler.md 'Tizen.UI.Components.Recycler')

## ISelectionModelGroup&lt;T> Interface

An generic interface for the group collection of [ISelectableModel](Tizen.UI.Components.Recycler.ISelectableModel.md 'Tizen.UI.Components.Recycler.ISelectableModel').  
The group can have multiple selected children.

```csharp
public interface ISelectionModelGroup&lt;T> :
System.Collections.Generic.IList&lt;T>,
System.Collections.Generic.ICollection&lt;T>,
System.Collections.Generic.IEnumerable&lt;T>,
System.Collections.IEnumerable,
Tizen.UI.Components.Recycler.ISelectionModelGroup,
System.Collections.IList,
System.Collections.ICollection
    where T : Tizen.UI.Components.Recycler.ISelectableModel
```
#### Type parameters

<a name='Tizen.UI.Components.Recycler.ISelectionModelGroup_T_.T'></a>

`T`

The child object who implements ISelectableModel

Derived  
&#8627; [SelectionModelGroup&lt;T&gt;](Tizen.UI.Components.Recycler.SelectionModelGroup_T_.md 'Tizen.UI.Components.Recycler.SelectionModelGroup&lt;T>')

Implements [System.Collections.Generic.IList&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1 'System.Collections.Generic.IList`1')[T](Tizen.UI.Components.Recycler.ISelectionModelGroup_T_.md#Tizen.UI.Components.Recycler.ISelectionModelGroup_T_.T 'Tizen.UI.Components.Recycler.ISelectionModelGroup&lt;T>.T')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1 'System.Collections.Generic.IList`1'), [System.Collections.Generic.ICollection&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.ICollection-1 'System.Collections.Generic.ICollection`1')[T](Tizen.UI.Components.Recycler.ISelectionModelGroup_T_.md#Tizen.UI.Components.Recycler.ISelectionModelGroup_T_.T 'Tizen.UI.Components.Recycler.ISelectionModelGroup&lt;T>.T')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.ICollection-1 'System.Collections.Generic.ICollection`1'), [System.Collections.Generic.IEnumerable&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IEnumerable-1 'System.Collections.Generic.IEnumerable`1')[T](Tizen.UI.Components.Recycler.ISelectionModelGroup_T_.md#Tizen.UI.Components.Recycler.ISelectionModelGroup_T_.T 'Tizen.UI.Components.Recycler.ISelectionModelGroup&lt;T>.T')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IEnumerable-1 'System.Collections.Generic.IEnumerable`1'), [System.Collections.IEnumerable](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.IEnumerable 'System.Collections.IEnumerable'), [ISelectionModelGroup](Tizen.UI.Components.Recycler.ISelectionModelGroup.md 'Tizen.UI.Components.Recycler.ISelectionModelGroup'), [System.Collections.IList](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.IList 'System.Collections.IList'), [System.Collections.ICollection](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.ICollection 'System.Collections.ICollection')
### Properties

<a name='Tizen.UI.Components.Recycler.ISelectionModelGroup_T_.SelectedChildren'></a>

## ISelectionModelGroup&lt;T>.SelectedChildren Property

The read only list of selected children.

```csharp
System.Collections.Generic.IReadOnlyCollection&lt;T> SelectedChildren { get; }
```

#### Property Value
[System.Collections.Generic.IReadOnlyCollection&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IReadOnlyCollection-1 'System.Collections.Generic.IReadOnlyCollection`1')[T](Tizen.UI.Components.Recycler.ISelectionModelGroup_T_.md#Tizen.UI.Components.Recycler.ISelectionModelGroup_T_.T 'Tizen.UI.Components.Recycler.ISelectionModelGroup&lt;T>.T')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IReadOnlyCollection-1 'System.Collections.Generic.IReadOnlyCollection`1')


























































