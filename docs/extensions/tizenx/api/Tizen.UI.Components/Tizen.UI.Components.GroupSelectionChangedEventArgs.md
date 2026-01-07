### [Tizen.UI.Components](Tizen.UI.Components.md 'Tizen.UI.Components')

## GroupSelectionChangedEventArgs Class

The event arguments for the GroupSelectionChangedEventArgs event.

```csharp
public class GroupSelectionChangedEventArgs : System.EventArgs
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [System.EventArgs](https://docs.microsoft.com/en-us/dotnet/api/System.EventArgs 'System.EventArgs') &#129106; GroupSelectionChangedEventArgs
### Constructors

<a name='Tizen.UI.Components.GroupSelectionChangedEventArgs.GroupSelectionChangedEventArgs(Tizen.UI.Components.IGroupSelectable,Tizen.UI.Components.IGroupSelectable)'></a>

## GroupSelectionChangedEventArgs(IGroupSelectable, IGroupSelectable) Constructor

GroupSelectionChangedEventArgs constructor.

```csharp
public GroupSelectionChangedEventArgs(Tizen.UI.Components.IGroupSelectable previous, Tizen.UI.Components.IGroupSelectable current);
```
#### Parameters

<a name='Tizen.UI.Components.GroupSelectionChangedEventArgs.GroupSelectionChangedEventArgs(Tizen.UI.Components.IGroupSelectable,Tizen.UI.Components.IGroupSelectable).previous'></a>

`previous` [IGroupSelectable](Tizen.UI.Components.IGroupSelectable.md 'Tizen.UI.Components.IGroupSelectable')

The old selected child.

<a name='Tizen.UI.Components.GroupSelectionChangedEventArgs.GroupSelectionChangedEventArgs(Tizen.UI.Components.IGroupSelectable,Tizen.UI.Components.IGroupSelectable).current'></a>

`current` [IGroupSelectable](Tizen.UI.Components.IGroupSelectable.md 'Tizen.UI.Components.IGroupSelectable')

The new selected child.
### Properties

<a name='Tizen.UI.Components.GroupSelectionChangedEventArgs.Current'></a>

## GroupSelectionChangedEventArgs.Current Property

Gets or sets the new selected child.

```csharp
public Tizen.UI.Components.IGroupSelectable Current { get; }
```

#### Property Value
[IGroupSelectable](Tizen.UI.Components.IGroupSelectable.md 'Tizen.UI.Components.IGroupSelectable')

<a name='Tizen.UI.Components.GroupSelectionChangedEventArgs.Previous'></a>

## GroupSelectionChangedEventArgs.Previous Property

Gets or sets the old selected child.

```csharp
public Tizen.UI.Components.IGroupSelectable Previous { get; }
```

#### Property Value
[IGroupSelectable](Tizen.UI.Components.IGroupSelectable.md 'Tizen.UI.Components.IGroupSelectable')


























































