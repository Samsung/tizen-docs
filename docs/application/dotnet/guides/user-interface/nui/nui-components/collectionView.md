---
keyword: CollectionView, RecyclerView, listview, gridview, itemsview
---

# CollectionView

CollectionView is a view for presenting collection of data using different layout specifications. It aims to provide a more flexible, and performant scrollable items view with lower memory usage.
CollectionView should be used for presenting collection of data that require scrolling or selection.
While CollectionView manages the apeareance of the layout, the appearance of each item is defined by a `DataTemplate` that uses a `RecyclerViewItem` to display items. NUI includes item types to display combinations of text and images, and you can also define custom items that display any content you want. CollectionView also includes support for displaying header, footer and grouped data.

**Figure: UI components**

![CollectionView linear layout](./media/collectionViewLinear.png) ![CollectionView grid layout](./media/collectionViewGrid.png)

## CollectionView Properties

The CollectionView class derives from the `RecyclerView` class, form which it inherits the following properties:

**Table: RecyclerView properties**

| Property                  | Type               | Description                                          |
|---------------------------|--------------------|------------------------------------------------------|
| `ItemSource`              | `IEnumerable`      | The collection data source of items.                 |
| `ItemTemplate`            | `DataTemplate`     | The template to apply each item to be displayed.     |


CollectionView defines the following properties:


**Table: CollectionView properties**

| Property                  | Type               | Description                                                              |
|---------------------------|--------------------|--------------------------------------------------------------------------|
| `ItemsLayouter`           | `IItemsLayouter`   | The layouter to layout items flexibily with scrolling geometry.          |
| `Header`                  | `RecyclerViewItem` | The header of CollectionView. header item is also in the scrollable area.|
| `Footer`                  | `RecyclerViewItem` | The footer of CollectionView. footer item is also in the scrollable area.|
| `IsGrouped`               | `bool`             | The boolean flag to set group mode.                                      |
| `GroupHeaderTemplate`     | `DataTemplate`     | The template to apply each group header items.                           |
| `GroupFooterTemplate`     | `DataTemplate`     | The template to apply each group footer items.                           |
| `SelectionMode`           | `ItemSelectionMode`| The selection mode for single and multi selection.                       |
| `SelectedItem`            | `object`           | The last selected item.                                                  |
| `SelectedItems`           | `IList<object>`    | The list of selected items in multi selection mode.                      |



[Tizen.NUI.Components.ScrollableBase](/application/dotnet/api/TizenFX/latest/api/Tizen.NUI.Components.ScrollableBase.html) is the indirect base class of the CollectionView, and you can also use its properties and methods such as `ScrollingDirection` or `ScrollPosition`.


## Related information

- Dependencies
  -   Tizen 7.0 and Higher
