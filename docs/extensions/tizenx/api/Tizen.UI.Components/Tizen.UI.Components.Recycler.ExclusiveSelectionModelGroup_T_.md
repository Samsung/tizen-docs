### [Tizen.UI.Components.Recycler](Tizen.UI.Components.Recycler.md 'Tizen.UI.Components.Recycler')

## ExclusiveSelectionModelGroup&lt;T> Class

An abstract class for the observable group collection of [ISelectableModel](Tizen.UI.Components.Recycler.ISelectableModel.md 'Tizen.UI.Components.Recycler.ISelectableModel').  
The group can only have one selected children exclusively.

```csharp
public abstract class ExclusiveSelectionModelGroup&lt;T> : System.Collections.ObjectModel.ObservableCollection&lt;T>
    where T : Tizen.UI.Components.Recycler.ISelectableModel
```
#### Type parameters

<a name='Tizen.UI.Components.Recycler.ExclusiveSelectionModelGroup_T_.T'></a>

`T`

The child object who implements ISelectableModel

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [System.Collections.ObjectModel.Collection&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.ObjectModel.Collection-1 'System.Collections.ObjectModel.Collection`1')[T](Tizen.UI.Components.Recycler.ExclusiveSelectionModelGroup_T_.md#Tizen.UI.Components.Recycler.ExclusiveSelectionModelGroup_T_.T 'Tizen.UI.Components.Recycler.ExclusiveSelectionModelGroup&lt;T>.T')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.ObjectModel.Collection-1 'System.Collections.ObjectModel.Collection`1') &#129106; [System.Collections.ObjectModel.ObservableCollection&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.ObjectModel.ObservableCollection-1 'System.Collections.ObjectModel.ObservableCollection`1')[T](Tizen.UI.Components.Recycler.ExclusiveSelectionModelGroup_T_.md#Tizen.UI.Components.Recycler.ExclusiveSelectionModelGroup_T_.T 'Tizen.UI.Components.Recycler.ExclusiveSelectionModelGroup&lt;T>.T')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.ObjectModel.ObservableCollection-1 'System.Collections.ObjectModel.ObservableCollection`1') &#129106; ExclusiveSelectionModelGroup&lt;T>
### Properties

<a name='Tizen.UI.Components.Recycler.ExclusiveSelectionModelGroup_T_.IsSelectable'></a>

## ExclusiveSelectionModelGroup&lt;T>.IsSelectable Property

Boolean value for whether this group is selectable or not.  
The value only propagates to the children when it set.  
so even though, all children are selectable, group selectable still can be false.  
default value is true.

```csharp
public bool IsSelectable { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.Recycler.ExclusiveSelectionModelGroup_T_.Selected'></a>

## ExclusiveSelectionModelGroup&lt;T>.Selected Property

The selected child.  
When the selected child changed, previous selected child will be deselected.

```csharp
public T Selected { get; set; }
```

#### Property Value
[T](Tizen.UI.Components.Recycler.ExclusiveSelectionModelGroup_T_.md#Tizen.UI.Components.Recycler.ExclusiveSelectionModelGroup_T_.T 'Tizen.UI.Components.Recycler.ExclusiveSelectionModelGroup&lt;T>.T')


























































