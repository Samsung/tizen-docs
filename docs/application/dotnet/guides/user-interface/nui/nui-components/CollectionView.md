---
keyword: CollectionView, RecyclerView, listview, gridview, itemsview
---

# CollectionView

[`CollectionView`](/application/dotnet/api/TizenFX/latest/api/Tizen.NUI.Components.CollectionView.html) is a view for presenting collection of data using different layout specifications. It aims to provide a more flexible, and performant scrollable items view with lower memory usage.
CollectionView should be used for presenting collection of data that require scrolling or selection.
While CollectionView manages the apeareance of the layout, the appearance of each item is defined by a [`Tizen.NUI.Binding.DataTemplate`](/application/dotnet/api/TizenFX/latest/api/Tizen.NUI.Binding.DataTemplate.html) that uses a [`Tizen.NUI.Components.RecyclerViewItem`](/application/dotnet/api/TizenFX/latest/api/Tizen.NUI.Components.RecyclerViewItem.html) to display items. NUI includes item types to display combinations of text and images, and you can also define custom items that display any content you want. CollectionView also includes support for displaying header, footer and grouped data.

**Figure: UI components**

![CollectionView linear layout](./media/listview.png) ![CollectionView grid layout](./media/gridview.png)

## CollectionView Properties

The CollectionView class derives from the [`Tizen.NUI.Components.RecyclerView`](/application/dotnet/api/TizenFX/latest/api/Tizen.NUI.Components.RecyclerView.html) class, form which it inherits the following properties:

**Table: RecyclerView properties**

| Property                  | Type               | Description                                          |
|---------------------------|--------------------|------------------------------------------------------|
| `ItemSource`              | `IEnumerable`      | The collection data source of items.                 |
| `ItemTemplate`            | `DataTemplate`     | The template to apply each item to be displayed.     |


CollectionView defines the following properties:


**Table: CollectionView properties**

| Property                  | Type               | Description                                                              |
|---------------------------|--------------------|--------------------------------------------------------------------------|
| `ItemsLayouter`           | `ItemsLayouter`    | The layouter to layout items flexibily with scrolling geometry.          |
| `Header`                  | `RecyclerViewItem` | The header of CollectionView. header item is also in the scrollable area.|
| `Footer`                  | `RecyclerViewItem` | The footer of CollectionView. footer item is also in the scrollable area.|
| `IsGrouped`               | `bool`             | The boolean flag to set group mode.                                      |
| `GroupHeaderTemplate`     | `DataTemplate`     | The template to apply each group header items.                           |
| `GroupFooterTemplate`     | `DataTemplate`     | The template to apply each group footer items.                           |
| `SelectionMode`           | `ItemSelectionMode`| The selection mode for single and multi selection.                       |
| `SelectedItem`            | `object`           | The last selected item.                                                  |
| `SelectedItems`           | `IList<object>`    | The list of selected items in multi selection mode.                      |



[`Tizen.NUI.Components.ScrollableBase`](/application/dotnet/api/TizenFX/latest/api/Tizen.NUI.Components.ScrollableBase.html) is the indirect base class of the CollectionView, and you can also use its properties and methods such as `ScrollingDirection` or `ScrollPosition`.


## Create item source

To use [`CollectionView`](/application/dotnet/api/TizenFX/latest/api/Tizen.NUI.Components.CollectionView.html), item source need to be created firstly. Item source is the collection of data on each item, which can notify the changes on demands.

1. Create an model class of item data:
    ```csharp
    class Animal
    {
        private string _name;
        private string _scientificName;
        private string _imageResource;
        private string _imageUrl = Tizen.Applications.Application.Current.DirectoryInfo.Resource + "/animals/";

        public Animal(string name, string scientificName, string imageResource)
        {
            _name = name;
            _scientificName = scientificName;
            _imageResource = imageResource;
        }

        public string Name
        {
            get => _name;
            set => _name = value;
        }

        public string ScientificName
        {
            get => _scientificName;
            set => _scientificName = value;
        }

        public string ImagePath
        {
            get => _imageUrl + _imageResource;
        }
    }
    ```
    To apply properties changes dynamically in the CollectionView, you need to implement [`System.ComponentModel.INotifyPropertyChanged`](https://learn.microsoft.com/En-us/dotnet/api/system.componentmodel.inotifypropertychanged?view=netstandard-2.0) interface.

    ```csharp
    class Animal : INotifyPropertyChanged
    {
        public event PropertyChangedEventHandler PropertyChanged;

        public string Name
        {
            get => _name;
            set
            {
                _name = value;
                //Invoke property changed event when property changed.
                PropertyChanged?.Invoke(this, new PropertyChangedEventArgs("Name"));
            }
        }
    }
    ```

2. Create [`System.Collections.Generic.IEnumerable`](https://learn.microsoft.com/en-us/dotnet/api/system.collections.ienumerable?view=netstandard-2.0) data collection for items. for simple collection, [`System.Collections.Generic.List<T>`](https://learn.microsoft.com/En-us/dotnet/api/system.collections.generic.list-1?view=netstandard-2.0) can be useful:

    ```csharp
    var animals = new List<Animal>();
    animals.Add(new Animal("Cat", "Felis catus", "cat.png"));
    animals.Add(new Animal("Dog", "Canis lupus familiaris", "dog.png"));
    animals.Add(new Animal("Fox", "Vulpes" "fox.png"));
    animals.Add(new Animal("Horse", "Equus ferus", "horse.png"));
    ```

    To apply data changes dynamically in the CollectionView, you need to implement [`System.ComponentModel.INotifyPropertyChanged`](https://learn.microsoft.com/En-us/dotnet/api/system.componentmodel.inotifypropertychanged?view=netstandard-2.0) and [`System.Collections.Specialized.INotifyCollectionChanged`](https://learn.microsoft.com/en-us/dotnet/api/system.collections.specialized.inotifycollectionchanged?view=netstandard-2.0) interface.
   [`System.Collections.ObjectModel.ObservableCollection<T>`](https://learn.microsoft.com/en-us/dotnet/api/system.collections.objectmodel.observablecollection-1?view=netstandard-2.0) can be useful for this purpose.

    ```csharp
    var animals = new ObservableCollection<Animal>();
    ```

## Create grouped item source

CollectionView support grouped item source with  [`System.Collections.ObjectModel.ObservableCollection<T>`](https://learn.microsoft.com/en-us/dotnet/api/system.collections.objectmodel.observablecollection-1?view=netstandard-2.0):
1. Create   [`System.Collections.ObjectModel.ObservableCollection<T>`](https://learn.microsoft.com/en-us/dotnet/api/system.collections.objectmodel.observablecollection-1?view=netstandard-2.0) data collection for group:

    ```csharp
    class Family : ObservableCollection<Animal>
    {
        private string _name;
        public Family(string name)
        {
            _name = name;
        }

        public Name
        {
            get => _name;
            set
            {
                _name = value;
                OnPropertyChanged(new PropertyChangedEventArgs("Name"));
            }
        }
    }
   ```
2. add group into group collection:

    ```csharp

    var families = new ObservableCollection<Family>();

    var falidae = new Family("Falidae");
    falidae.Add(new Animal("Cat", "Felis catus", "cat.png"));
    falidae.Add(new Animal("Cheetah", "Acinonyx jubatus", "cheetah.png"));
    falidae.Add(new Animal("Leopard", "Panthera pardus", "leopard.png"));
    falidae.Add(new Animal("Lion", "Panthera leo", "lion.png"));
    falidae.Add(new Animal("Tiger", "Panthera tigris", "tiger.png"));
    families.Add(falidae);

    var canidae = new Family("Canidae");
    canidae.Add(new Animal("Coyote", "Canis latrans" "coyote.png"));
    canidae.Add(new Animal("Dog", "Canis lupus familiaris", "dog.png"));
    canidae.Add(new Animal("Fox", "Vulpes" "fox.png"));
    canidae.Add(new Animal("Raccoon dog", "Nyctereutes procyonoides" "raccoondog.png"));
    canidae.Add(new Animal("Wolf", "Canis lupus" "wolf.png"));
    families.Add(canidae);
    ```

To use grouped item source in [`CollectionView`](/application/dotnet/api/TizenFX/latest/api/Tizen.NUI.Components.CollectionView.html), `IsGrouped` property must be true.



## Create items

1. To create items in CollectionView, use [`Tizen.NUI.Binding.DataTemplate`](/application/dotnet/api/TizenFX/latest/api/Tizen.NUI.Binding.DataTemplate.html) as `ItemTemplate` of collectionView:

    <div id="TabSection1">
        <div class="sampletab " id="ProjectCreateTab">
            <button id="ItemTemplate-CSharp" class="tablinks " onclick="openTabSection(event, 'ItemTemplate-CSharp', 'TabSection1') ">C#</button>
            <button id="ItemTemplate-Xaml" class="tablinks " onclick="openTabSection(event, 'ItemTemplate-Xaml', 'TabSection1') ">Xaml</button>
        </div>
        <div id="ItemTemplate-CSharp" class="tabcontent">
            <table>
                <tbody>
                    <tr>
    <span style="display:block">

    ```csharp
    var collectionView = new CollectionView()
    {
        ItemTemplate = new DataTemplate(() =>
        {
            /// Create item here. This method is CreateContent() of DataTemplate.
        });
    }
   ```

    </span>
                    </tr>
                </tbody>
            </table>
        </div>
        <div id="ItemTemplate-Xaml" class="tabcontent">
            <table>
                <tbody>
                    <tr>
    <span style="display:block">


    ```xaml
    <CollectionView>
        <ItemTemplate>
            <DataTemplate>
                <!-- Create item here -->
            </DataTemplate>
        </ItemTemplate>
    </CollectionView>
    ```


    </span>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>

2. Create Item as a content of the [`Tizen.NUI.Binding.DataTemplate`](/application/dotnet/api/TizenFX/latest/api/Tizen.NUI.Binding.DataTemplate.html).<br>
    CollectionView accepts [`Tizen.NUI.Components.RecyclerViewItem`](/application/dotnet/api/TizenFX/latest/api/Tizen.NUI.Components.RecyclerViewItem.html) class as an item. Developer can create new class inherited from abstract [`Tizen.NUI.Components.RecyclerViewItem`](/application/dotnet/api/TizenFX/latest/api/Tizen.NUI.Components.RecyclerViewItem.html), or use pre-defined default item classes.<br>
    Fallowing classes are pre-defined default item classes :


    **Figure: Tizen.NUI.Components.DefaultLinearItem**

    ![`Tizen.NUI.Components.DefaultLinearItem`](./media/defaultlinearitem.png)

    `Tizen.NUI.Components.DefaultLinearItem` is for LinearLayout items. It provides fallowing contents:

    **Table: Tizen.NUI.Components.DefaultLinearItem**

    | Property                  | Type               | Description                                                              |
    |---------------------------|--------------------|--------------------------------------------------------------------------|
    | `Text`                    | `string`           | The main text. use `Label`for get `TextLabel` object.                    |
    | `SubText`                 | `string`           | The substitute text. `SubLabel`for get `TextLabel` object.               |
    | `Icon`                    | `View`             | The left icon content of item.                                           |
    | `Extra`                   | `View`             | The right icon content of item.                                          |



    **Figure: Tizen.NUI.Components.DefaultGridItem**

    ![Tizen.NUI.Components.DefaultGridItem](./media/defaultgriditem.png)

    `Tizen.NUI.Components.DefaultGridItem` is for GridLayout items. It provides fallowing contents:

    **Table: Tizen.NUI.Components.DefaultGridItem**

    | Property                  | Type               | Description                                                                     |
    |---------------------------|--------------------|---------------------------------------------------------------------------------|
    | `Text`                    | `string`           | The main text. use `Label`for get `TextLabel` object.                           |
    | `Image`                   | `ImageView`        | The image content of item. Read-Only. to set resource on image use ResourceUrl. |
    | `Badge`                   | `View`             | The top-right badge icon content of item.                                       |
    | `LabelOrientationType`    | `DefaultGridItem.LabelOrientation` | The enum type for label orientation. label can be placed (outer / inner) of image and (top / bottom) of image. |



    **Figure: Tizen.NUI.Components.DefaultTitleItem**

    ![Tizen.NUI.Components.DefaultTitleItem](./media/defaulttitleitem.png)

    `Tizen.NUI.Components.DefaultTitleItem` is for group header items. It provides fallowing contents:

    **Table: Tizen.NUI.Components.DefaultTitleItem**
    | Property                  | Type               | Description                                                              |
    |---------------------------|--------------------|--------------------------------------------------------------------------|
    | `Text`                    | `string`           | The main text. use `Label`for get `TextLabel` object.                    |
    | `Icon`                    | `View`             | The left icon content of item.                                           |
    | `Seperator`               | `View`             | The bottom seperator of group title for deviding from it's chlidren.     |


    Use data binding for property update.

    <div id="TabSection2">
        <div class="sampletab " id="ProjectCreateTab">
            <button id="ItemCreate-CSharp" class="tablinks " onclick="openTabSection(event, 'ItemCreate-CSharp', 'TabSection2') ">C#</button>
            <button id="ItemCreate-Xaml" class="tablinks " onclick="openTabSection(event, 'ItemCreate-Xaml', 'TabSection2') ">Xaml</button>
        </div>
        <div id="ItemCreate-CSharp" class="tabcontent">
            <table>
                <tbody>
                    <tr>
    <span style="display:block">


    ```csharp
    var collectionView = new CollectionView()
    {
        ItemTemplate = new DataTemplate(() =>
        {
            var item =  DefaultLinearItem()
            {
                WidthSpecification = LayoutParamPolicies.MatchParent
            };

            item.SetBinding(DefaultLinearItem.TextProperty, "Name");
            item.SetBinding(DefaultLinearItem.SubTextProperty, "ScientificName");
            item.Icon = new ImageView()
            {
                WidthSpecification = 80,
                HeightSpecification = 80,
            };
            item.Icon.SetBinding(ImageView.ResourceUrlProperty, "ImagePath");

            return item;
        });
    }
   ```

    </span>
                    </tr>
                </tbody>
            </table>
        </div>
        <div id="ItemCreate-Xaml" class="tabcontent">
            <table>
                <tbody>
                    <tr>
    <span style="display:block">

    ```xaml
    <CollectionView>
        <CollectionView.ItemTemplate>
            <DataTemplate>
                <DefaultLinearItem
                    WidthSpecification="{Static LayoutParamPolicies.MatchParent}"
                    Text="{Binding Path=Name}"
                    SubText="{Binding Path=ScientificName}">
                    <DefaultLinearItem.Icon>
                        <ImageView
                            WidthSpecification="80"
                            HeightSpecification="80"
                            ResourceUrl="{Binding Path=ImagePath}" />
                    </DefaultLinearItem.Icon>
                </DefaultLinearItem>
            </DataTemplate>
        </CollectionView.ItemTemplate>
    </CollectionView>
    ```

    </span>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>


`CreateContent()` will be performed internally with [`CollectionView`](/application/dotnet/api/TizenFX/latest/api/Tizen.NUI.Components.CollectionView.html) and [`Tizen.NUI.Components.ItemsLayouter`](/application/dotnet/api/TizenFX/latest/api/Tizen.NUI.Components.ItemsLayouter.html), and generated items can be cached, and recycled on different positions.

`GroupHeader` and `GroupFooter` also can be created with [`Tizen.NUI.Binding.DataTemplate`](/application/dotnet/api/TizenFX/latest/api/Tizen.NUI.Binding.DataTemplate.html).


## Set Layout on CollectionView

[`CollectionView`](/application/dotnet/api/TizenFX/latest/api/Tizen.NUI.Components.CollectionView.html) allow layout flexibly by [`Tizen.NUI.Components.ItemsLayouter`](/application/dotnet/api/TizenFX/latest/api/Tizen.NUI.Components.ItemsLayouter.html).

NUI provide fallowing pre-defined ItemsLayouter:

**Table: ItemsLayouter derivded class**

| Class                     | Figure                     | Description                                                              |
|---------------------------|----------------------------|--------------------------------------------------------------------------|
| [`Tizen.NUI.Components.LinearLayouter`](/application/dotnet/api/TizenFX/latest/api/Tizen.NUI.Components.LinearLayouter.html) |![linearLayouter](./media/listview-small.png) | The layouter to layout items on linear position such as list view.       |
| [`Tizen.NUI.Components.GridLayouter`](/application/dotnet/api/TizenFX/latest/api/Tizen.NUI.Components.GridLayouter.html) |![gridLayouter](./media/gridview-small.png)     | The layouter to layout items on grid row and columns.<br>row and column count will be automatically calculated by item's size. |


<div id="TabSection3">
    <div class="sampletab " id="ProjectCreateTab">
        <button id="ItemLayouter-CSharp" class="tablinks " onclick="openTabSection(event, 'ItemLayouter-CSharp', 'TabSection3') ">C#</button>
        <button id="ItemLayouter-Xaml" class="tablinks " onclick="openTabSection(event, 'ItemLayouter-Xaml', 'TabSection3') ">Xaml</button>
    </div>
    <div id="ItemLayouter-CSharp" class="tabcontent">
        <table>
            <tbody>
                <tr>
<span style="display:block">


```csharp
var collectionView = new CollectionView()
{
    ItemsLayouter = new LinearLayouter(),
    ScrollingDirection = Tizen.NUI.Components.ScrollableBase.Direction.Vertical
}
```

</span>
                </tr>
            </tbody>
        </table>
    </div>
    <div id="ItemLayouter-Xaml" class="tabcontent">
        <table>
            <tbody>
                <tr>
<span style="display:block">

```xaml
<CollectionView ScrollingDirection="Vertical">
    <ItemsLayouter>
        <LinearLayouter />
    </ItemsLayouter>
</CollectionView>
```

</span>
                </tr>
            </tbody>
        </table>
    </div>
</div>


<script>
    function openTabSection(evt, profileName, sectionId) {
        var i, tabcontent, tablinks, section;
        let selected = 0;

        section = document.getElementById(sectionId);
        tabcontent = section.getElementsByClassName("tabcontent");
        for (i = 0; i < tabcontent.length; i++) {
            tabcontent[i].style.display = "none";
            if (tabcontent[i].id == profileName) {
                selected = i;
            }
        }

        tablinks = section.getElementsByClassName("tablinks");

        for (i = 0; i < tablinks.length; i++) {
            tablinks[i].className = tablinks[i].className.replace(" active", "");
        }

        tabcontent[selected].style.display = "block";
        evt.currentTarget.className += " active";
    }
    document.getElementById("ItemTemplate-CSharp").click();
    document.getElementById("ItemCreate-CSharp").click();
    document.getElementById("ItemLayouter-CSharp").click();
</script>





## Selection in Collection View

The [`CollectionView`](/application/dotnet/api/TizenFX/latest/api/Tizen.NUI.Components.CollectionView.html) provide item selection features. Selection can be controlled by [`SelectionMode`](/application/dotnet/api/TizenFX/latest/api/Tizen.NUI.Components.CollectionView.html#Tizen_NUI_Components_CollectionView_SelectionMode) which can choose single or multiple selection.

**Table: ItemSelectionMode**
| Mode           | Description                                                                                   |
|----------------|-----------------------------------------------------------------------------------------------|
| `None`         | None of the items can be selected. default mode.                                              |
| `Single`       | Single selection. Select item exclusively so previous selected item will be unselected.       |
| `SingleAlways` | Single selection always. It's not possible to unselect all, so after user selects an item,<br>there is always exactly one item selected. To deselect item, clear selection forcely.|
| `Multiple`     | Multiple selections. Select multiple items and previous selected item still remains selected. |

Selection can handled by user interactions such as key or touch inputs.
Changing selection will be fired [`SelectionChanged`](/application/dotnet/api/TizenFX/latest/api/Tizen.NUI.Components.CollectionView.html#Tizen_NUI_Components_CollectionView_SelectionChanged) event.<br>
The [`Tizen.NUI.Components.SelectionChangedEventArgs`](/application/dotnet/api/TizenFX/latest/api/Tizen.NUI.Components.SelectionChangedEventArgs.html) object that accompanies the [`SelectionChanged`](/application/dotnet/api/TizenFX/latest/api/Tizen.NUI.Components.CollectionView.html#Tizen_NUI_Components_CollectionView_SelectionChanged) event has two properties, both of type [`System.Collections.Generic.IReadOnlyList<object>`](https://learn.microsoft.com/en-us/dotnet/api/system.collections.generic.ireadonlylist-1?view=net-7.0):

- `PreviousSelection` : the list of items that were selected, before the selection changed.
- `CurrentSelection` : the list of items that are selected, after the selection change.


1. Single Selection

    [`SelectionMode`](/application/dotnet/api/TizenFX/latest/api/Tizen.NUI.Components.CollectionView.html#Tizen_NUI_Components_CollectionView_SelectionMode) is `Single` or `SingleAlways`, [`CollectionView`](/application/dotnet/api/TizenFX/latest/api/Tizen.NUI.Components.CollectionView.html) only select single item and previously selected item will be deselected.
    To get or set current selected item, use [`SelectedItem`](/application/dotnet/api/TizenFX/latest/api/Tizen.NUI.Components.CollectionView.html#Tizen_NUI_Components_CollectionView_SelectedItem) Property.

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

    [`SelectionMode`](/application/dotnet/api/TizenFX/latest/api/Tizen.NUI.Components.CollectionView.html#Tizen_NUI_Components_CollectionView_SelectionMode) is `Multiple`, [`CollectionView`](/application/dotnet/api/TizenFX/latest/api/Tizen.NUI.Components.CollectionView.html) select multiple items.<br>
    To get current selected items, use [`SelectedItems`](/application/dotnet/api/TizenFX/latest/api/Tizen.NUI.Components.CollectionView.html#Tizen_NUI_Components_CollectionView_SelectedItems) Property.<br>
    To set new selection, use [`UpdateSelectedItems()`](/application/dotnet/api/TizenFX/latest/api/Tizen.NUI.Components.CollectionView.html#Tizen_NUI_Components_CollectionView_UpdateSelectedItems_System_Collections_Generic_IList_System_Object__) method.<br>

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

[`CollectionView`](/application/dotnet/api/TizenFX/latest/api/Tizen.NUI.Components.CollectionView.html) can use not only scroll related features and events as it is descendant of [`Tizen.NUI.Components.ScrollableBase`](/application/dotnet/api/TizenFX/latest/api/Tizen.NUI.Components.ScrollableBase.html), also provide extended method of [`ScrollTo()`](/application/dotnet/api/TizenFX/latest/api/Tizen.NUI.Components.CollectionView.html#Tizen.NUI.Components.CollectionView.html#Tizen_NUI_Components_CollectionView_ScrollTo_System_Single_System_Boolean_) which requires [`ItemScrollTo`](/application/dotnet/api/TizenFX/latest/api/Tizen.NUI.Components.CollectionView.ItemScrollTo.html) Type.

```csharp
var collectionView = new CollectionView();
collectionView.ScrollTo(10, true, ItemScrollTo.Nearest);
```

## Related information

- Dependencies
  -   Tizen 7.0 and Higher
