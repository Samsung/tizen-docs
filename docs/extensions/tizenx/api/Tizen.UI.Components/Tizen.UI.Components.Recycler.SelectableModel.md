### [Tizen.UI.Components.Recycler](Tizen.UI.Components.Recycler.md 'Tizen.UI.Components.Recycler')

## SelectableModel Class

An abstract selectable data model which implements [ISelectableModel](Tizen.UI.Components.Recycler.ISelectableModel.md 'Tizen.UI.Components.Recycler.ISelectableModel').

```csharp
public abstract class SelectableModel : Tizen.UI.Components.Recycler.ViewModel,
Tizen.UI.Components.Recycler.ISelectableModel,
System.ComponentModel.INotifyPropertyChanged
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [ViewModel](Tizen.UI.Components.Recycler.ViewModel.md 'Tizen.UI.Components.Recycler.ViewModel') &#129106; SelectableModel

Implements [ISelectableModel](Tizen.UI.Components.Recycler.ISelectableModel.md 'Tizen.UI.Components.Recycler.ISelectableModel'), [System.ComponentModel.INotifyPropertyChanged](https://docs.microsoft.com/en-us/dotnet/api/System.ComponentModel.INotifyPropertyChanged 'System.ComponentModel.INotifyPropertyChanged')
### Constructors

<a name='Tizen.UI.Components.Recycler.SelectableModel.SelectableModel()'></a>

## SelectableModel() Constructor

SelectableModel constructor. initalize the property value.

```csharp
public SelectableModel();
```
### Properties

<a name='Tizen.UI.Components.Recycler.SelectableModel.IsSelectable'></a>

## SelectableModel.IsSelectable Property

Boolean value whether this model can be selectable or not.

```csharp
public bool IsSelectable { get; set; }
```

Implements [IsSelectable](Tizen.UI.Components.Recycler.ISelectableModel.md#Tizen.UI.Components.Recycler.ISelectableModel.IsSelectable 'Tizen.UI.Components.Recycler.ISelectableModel.IsSelectable')

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.Recycler.SelectableModel.IsSelected'></a>

## SelectableModel.IsSelected Property

Boolean value whether this model is selected or not.

```csharp
public bool IsSelected { get; set; }
```

Implements [IsSelected](Tizen.UI.Components.Recycler.ISelectableModel.md#Tizen.UI.Components.Recycler.ISelectableModel.IsSelected 'Tizen.UI.Components.Recycler.ISelectableModel.IsSelected')

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')


























































