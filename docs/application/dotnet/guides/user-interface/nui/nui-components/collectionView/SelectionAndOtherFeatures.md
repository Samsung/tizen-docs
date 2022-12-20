## Selection in Collection View

The [`CollectionView`](/application/dotnet/api/TizenFX/latest/api/Tizen.NUI.Components.CollectionView.html) provide item selection features. Selection can be controlled by [`SelectionMode`](application/dotnet/api/TizenFX/latest/api/Tizen.NUI.Components.ItemSelectionMode.html) which can choose single or multiple selection.

**Table: ItemSelectionMode **
| Mode           | Description                                                                                   |
|----------------|-----------------------------------------------------------------------------------------------|
| `None`         | None of the items can be selected. default mode.                                              |
| `Single`       | Single selection. Select item exclusively so previous selected item will be unselected.       |
| `SingleAlways` | Single selection always. It's not possible to unselect all, so after user selects an item,<br>there is always exactly one item selected. To deselect item, clear selection forcely.|
| `Multiple`     | Multiple selections. Select multiple items and previous selected item still remains selected. |

Selection can handled by user interactions such as key or touch inputs.
Changing selection will be fired [`SelectionChanged`](application/dotnet/api/TizenFX/latest/api/Tizen.NUI.Components.CollectionView.html#Tizen_NUI_Components_CollectionView_SelectionChanged) event.<br>
The [`SelectionChangedEventArgs`](application/dotnet/api/TizenFX/latest/api/Tizen.NUI.Components.SelectionChangedEventArgs.html) object that accompanies the [`SelectionChanged`](application/dotnet/api/TizenFX/latest/api/Tizen.NUI.Components.CollectionView.html#Tizen_NUI_Components_CollectionView_SelectionChanged) event has two properties, both of type [`IReadOnlyList<object>`](https://learn.microsoft.com/en-us/dotnet/api/system.collections.generic.ireadonlylist-1?view=net-7.0):

- `PreviousSelection` : the list of items that were selected, before the selection changed.
- `CurrentSelection` : the list of items that are selected, after the selection change.


1. Single Selection

    [`SelectionMode`](application/dotnet/api/TizenFX/latest/api/Tizen.NUI.Components.ItemSelectionMode.html) is `Single` or `SingleAlways`, [`CollectionView`](/application/dotnet/api/TizenFX/latest/api/Tizen.NUI.Components.CollectionView.html) only select single item and previously selected item will be deselected.
    To get or set current selected item, use [`SelectedItem`](application/dotnet/api/TizenFX/latest/api/Tizen.NUI.Components.CollectionView.html#Tizen_NUI_Components_CollectionView_SelectedItem_) Property.

    ```csharp
    var collectionView = new CollectionView()
    {
        ItemSource = animalSource;
        SelectionMode = ItemSelectionMode.Single, // itemSelectionMode.SingleAlways,
        SelectedItem = animalSource[10]; // 10th item will be selected.
    }

    collectionView.SelectionChanged = ((object o, SelectionChangedEventArgs ev) => {
        Animal animal = null;
        // Single Selection Only have 1 or nil object in the list.
        foreach (object item in ev.PreviousSelection)
        {
            animal = item as Animal;
            if (animal == null) break;

            Console.WriteLine($"Previous selected item {animal.Name}");
        }
        foreach (object item in ev.CurrentSelection)
        {
            animal = item as Animal;
            if (animal == null) break;

            Console.WriteLine($"Current selected item {animal.Name}");
        }
    });
   ```


2. Multiple Selection

    [`SelectionMode`](application/dotnet/api/TizenFX/latest/api/Tizen.NUI.Components.ItemSelectionMode.html) is `Multiple`, [`CollectionView`](/application/dotnet/api/TizenFX/latest/api/Tizen.NUI.Components.CollectionView.html) select multiple items.<br>
    To get current selected items, use [`SelectedItems`](application/dotnet/api/TizenFX/latest/api/Tizen.NUI.Components.CollectionView.html#Tizen_NUI_Components_CollectionView_SelectedItems_) Property.<br>
    To set new selection, use [`UpdateSelectedItems()`](application/dotnet/api/TizenFX/latest/api/Tizen.NUI.Components.CollectionView.html#Tizen_NUI_Components_CollectionView_UpdateSelectedItems_) method.<br>

    ```csharp
    var collectionView = new CollectionView()
    {
        ItemSource = animalSource;
        SelectionMode = ItemSelectionMode.Multiple,
    }

    collectionView.SelectionChanged = ((object o, SelectionChangedEventArgs ev) => {
        Animal animal = null;
        foreach (object item in ev.PreviousSelection)
        {
            animal = item as Animal;
            if (animal == null) break;

            Console.WriteLine($"Previous selected item {animal.Name}");
        }
        foreach (object item in ev.CurrentSelection)
        {
            animal = item as Animal;
            if (animal == null) break;

            Console.WriteLine($"Current selected item {animal.Name}");
        }
    });

    var newSelection = new List<Animal>();
    for(int i = 3; int i < 10; i++)
    {
        newSelection.Add(animalSource[i]);
    }

    collectionView.UpdateSelectedItems(newSelection);
   ```

 ## Other Features

[`CollectionView`](/application/dotnet/api/TizenFX/latest/api/Tizen.NUI.Components.CollectionView.html) can use not only scroll related features and events as it is descendant of [`ScrollableBase`](/application/dotnet/api/TizenFX/latest/api/Tizen.NUI.Components.ScrollableBase.html), also provide extended method of [`ScrollTo()`](/application/dotnet/api/TizenFX/latest/api/Tizen.NUI.Components.CollectionView.html#Tizen_NUI_Components_CollectionView_ScrollTo_) which requires [`ItemScrollTo`](/application/dotnet/api/TizenFX/latest/api/Tizen.NUI.Components.CollectionView.ItemScrollTo.html) Type.

```csharp
var collectionView = new CollectionView();
collectionView.ScrollTo(10, true, ItemScrollTo.Nearest);
```


## Related information

- Dependencies
  -   Tizen 7.0 and Higher