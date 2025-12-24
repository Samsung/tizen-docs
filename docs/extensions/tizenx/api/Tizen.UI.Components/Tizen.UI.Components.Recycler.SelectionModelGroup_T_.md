### [Tizen.UI.Components.Recycler](Tizen.UI.Components.Recycler.md 'Tizen.UI.Components.Recycler')

## SelectionModelGroup&lt;T> Class

An abstract class for the observable group collection of [ISelectableModel](Tizen.UI.Components.Recycler.ISelectableModel.md 'Tizen.UI.Components.Recycler.ISelectableModel').  
The group can have multiple selected children.

```csharp
public abstract class SelectionModelGroup&lt;T> : System.Collections.ObjectModel.ObservableCollection&lt;T>,
Tizen.UI.Components.Recycler.ISelectionModelGroup&lt;T>,
System.Collections.Generic.IList&lt;T>,
System.Collections.Generic.ICollection&lt;T>,
System.Collections.Generic.IEnumerable&lt;T>,
System.Collections.IEnumerable,
Tizen.UI.Components.Recycler.ISelectionModelGroup,
System.Collections.IList,
System.Collections.ICollection,
Tizen.UI.Components.Recycler.ISelectableModel,
System.ComponentModel.INotifyPropertyChanged
    where T : Tizen.UI.Components.Recycler.ISelectableModel
```
#### Type parameters

<a name='Tizen.UI.Components.Recycler.SelectionModelGroup_T_.T'></a>

`T`

The child object who implements ISelectableModel

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [System.Collections.ObjectModel.Collection&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.ObjectModel.Collection-1 'System.Collections.ObjectModel.Collection`1')[T](Tizen.UI.Components.Recycler.SelectionModelGroup_T_.md#Tizen.UI.Components.Recycler.SelectionModelGroup_T_.T 'Tizen.UI.Components.Recycler.SelectionModelGroup&lt;T>.T')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.ObjectModel.Collection-1 'System.Collections.ObjectModel.Collection`1') &#129106; [System.Collections.ObjectModel.ObservableCollection&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.ObjectModel.ObservableCollection-1 'System.Collections.ObjectModel.ObservableCollection`1')[T](Tizen.UI.Components.Recycler.SelectionModelGroup_T_.md#Tizen.UI.Components.Recycler.SelectionModelGroup_T_.T 'Tizen.UI.Components.Recycler.SelectionModelGroup&lt;T>.T')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.ObjectModel.ObservableCollection-1 'System.Collections.ObjectModel.ObservableCollection`1') &#129106; SelectionModelGroup&lt;T>

Implements [Tizen.UI.Components.Recycler.ISelectionModelGroup&lt;](Tizen.UI.Components.Recycler.ISelectionModelGroup_T_.md 'Tizen.UI.Components.Recycler.ISelectionModelGroup&lt;T>')[T](Tizen.UI.Components.Recycler.SelectionModelGroup_T_.md#Tizen.UI.Components.Recycler.SelectionModelGroup_T_.T 'Tizen.UI.Components.Recycler.SelectionModelGroup&lt;T>.T')[&gt;](Tizen.UI.Components.Recycler.ISelectionModelGroup_T_.md 'Tizen.UI.Components.Recycler.ISelectionModelGroup&lt;T>'), [System.Collections.Generic.IList&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1 'System.Collections.Generic.IList`1')[T](Tizen.UI.Components.Recycler.SelectionModelGroup_T_.md#Tizen.UI.Components.Recycler.SelectionModelGroup_T_.T 'Tizen.UI.Components.Recycler.SelectionModelGroup&lt;T>.T')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1 'System.Collections.Generic.IList`1'), [System.Collections.Generic.ICollection&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.ICollection-1 'System.Collections.Generic.ICollection`1')[T](Tizen.UI.Components.Recycler.SelectionModelGroup_T_.md#Tizen.UI.Components.Recycler.SelectionModelGroup_T_.T 'Tizen.UI.Components.Recycler.SelectionModelGroup&lt;T>.T')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.ICollection-1 'System.Collections.Generic.ICollection`1'), [System.Collections.Generic.IEnumerable&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IEnumerable-1 'System.Collections.Generic.IEnumerable`1')[T](Tizen.UI.Components.Recycler.SelectionModelGroup_T_.md#Tizen.UI.Components.Recycler.SelectionModelGroup_T_.T 'Tizen.UI.Components.Recycler.SelectionModelGroup&lt;T>.T')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IEnumerable-1 'System.Collections.Generic.IEnumerable`1'), [System.Collections.IEnumerable](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.IEnumerable 'System.Collections.IEnumerable'), [ISelectionModelGroup](Tizen.UI.Components.Recycler.ISelectionModelGroup.md 'Tizen.UI.Components.Recycler.ISelectionModelGroup'), [System.Collections.IList](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.IList 'System.Collections.IList'), [System.Collections.ICollection](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.ICollection 'System.Collections.ICollection'), [ISelectableModel](Tizen.UI.Components.Recycler.ISelectableModel.md 'Tizen.UI.Components.Recycler.ISelectableModel'), [System.ComponentModel.INotifyPropertyChanged](https://docs.microsoft.com/en-us/dotnet/api/System.ComponentModel.INotifyPropertyChanged 'System.ComponentModel.INotifyPropertyChanged')
### Properties

<a name='Tizen.UI.Components.Recycler.SelectionModelGroup_T_.IsSelectable'></a>

## SelectionModelGroup&lt;T>.IsSelectable Property

Boolean value for whether this group is selectable or not.  
The value only propagates to the children when it set.  
so even though, all children are selectable, group selectable still can be false.  
default value is true;

```csharp
public bool IsSelectable { get; set; }
```

Implements [IsSelectable](Tizen.UI.Components.Recycler.ISelectableModel.md#Tizen.UI.Components.Recycler.ISelectableModel.IsSelectable 'Tizen.UI.Components.Recycler.ISelectableModel.IsSelectable')

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.Recycler.SelectionModelGroup_T_.IsSelected'></a>

## SelectionModelGroup&lt;T>.IsSelected Property

Boolean value for whether this group is selected or not.  
All children will be propagated value when it set.  
If all children are selected, the value will be true.

```csharp
public bool IsSelected { get; set; }
```

Implements [IsSelected](Tizen.UI.Components.Recycler.ISelectableModel.md#Tizen.UI.Components.Recycler.ISelectableModel.IsSelected 'Tizen.UI.Components.Recycler.ISelectableModel.IsSelected')

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.Recycler.SelectionModelGroup_T_.SelectedChildren'></a>

## SelectionModelGroup&lt;T>.SelectedChildren Property

The read only list of selected children.

```csharp
public System.Collections.Generic.IReadOnlyCollection&lt;T> SelectedChildren { get; }
```

Implements [SelectedChildren](Tizen.UI.Components.Recycler.ISelectionModelGroup_T_.md#Tizen.UI.Components.Recycler.ISelectionModelGroup_T_.SelectedChildren 'Tizen.UI.Components.Recycler.ISelectionModelGroup&lt;T>.SelectedChildren')

#### Property Value
[System.Collections.Generic.IReadOnlyCollection&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IReadOnlyCollection-1 'System.Collections.Generic.IReadOnlyCollection`1')[T](Tizen.UI.Components.Recycler.SelectionModelGroup_T_.md#Tizen.UI.Components.Recycler.SelectionModelGroup_T_.T 'Tizen.UI.Components.Recycler.SelectionModelGroup&lt;T>.T')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IReadOnlyCollection-1 'System.Collections.Generic.IReadOnlyCollection`1')

<a name='Tizen.UI.Components.Recycler.SelectionModelGroup_T_.SelectedCount'></a>

## SelectionModelGroup&lt;T>.SelectedCount Property

The count of the selected children.  
If the groups are nested tree, it will return the count of selected leaf node.  
To get the selected children count in nested group, please use SelectedChildren.Count.

```csharp
public int SelectedCount { get; }
```

Implements [SelectedCount](Tizen.UI.Components.Recycler.ISelectionModelGroup.md#Tizen.UI.Components.Recycler.ISelectionModelGroup.SelectedCount 'Tizen.UI.Components.Recycler.ISelectionModelGroup.SelectedCount')

#### Property Value
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')


























































