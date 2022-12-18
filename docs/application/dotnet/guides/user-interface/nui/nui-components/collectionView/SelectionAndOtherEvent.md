## Selection in Collection View

CollectionView provide item selection features. Selection can be controlled by `SelectionMode` which can choose single or multiple selection.

**Table: ItemSelectionMode **
| Mode           | Description                                                                                   |
|----------------|-----------------------------------------------------------------------------------------------|
| `None`         | None of the items can be selected.                                                            |
| `Single`       | Single selection. Select item exclusively so previous selected item will be unselected.       |
| `SingleAlways` | Single selection always. It's not possible to unselect all, so after user selects an item,<br>there is always exactly one item selected. To deselect item, clear selection forcely.|
| `Multiple`     | Multiple selections. Select multiple items and previous selected item still remains selected. |


1. Single Selection

2. Multiple Selection

## Propagate selection






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


`GroupHeader` and `GroupFooter` also can be created with [`DataTemplate`](/application/dotnet/api/TizenFX/latest/api/Tizen.NUI.Binding.DataTemplate.html).


## Set Layout on CollectionView

[`CollectionView`](/application/dotnet/api/TizenFX/latest/api/Tizen.NUI.Components.CollectionView.html) allow layout flexibly by [`ItemsLayouter`](/application/dotnet/api/TizenFX/latest/api/Tizen.NUI.Components.ItemsLayouter.html).

NUI provide fallowing pre-defined ItemsLayouter:


| Class                     | Figure                     | Description                                                              |
|---------------------------|----------------------------|--------------------------------------------------------------------------|
| `LinearLayouter`          |![linearLayouter](./media/listview-small.png) | The layouter to layout items on linear position such as list view.       |
| `GridLayouter`            |![gridLayouter](./media/gridview-small.png)     | The layouter to layout items on grid row and columns.<br>row and column count will be automatically calculated by item's size. |


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



## Related information

- Dependencies
  -   Tizen 7.0 and Higher


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
    document.getElementById("AbsoluteLayout-Example-CSharp").click();
</script>
