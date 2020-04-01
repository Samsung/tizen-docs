# Tab

Tab is a common component and it can be used as a menu label.

A Tab makes it easy to explore and switch between different views or functional aspects of an application or to browse categorized data sets.

You can handle a Tab by adding, inserting, or deleting a TabItem. A Tab can contain one or more TabItem with text, usually used as a menu label. A TabItem can have different lengths.

![Tab](./media/tab.png) ![Tab](./media/tab2.png)

## Create with property

To create a Tab using property, follow these steps:

1. Create Tab using the default constructor:

    ```cs
    utilityBasicTab = new Tab();
    ```

2. Set the Tab property:

    ```cs
    utilityBasicTab.IsSelectable = true;
    utilityBasicTab.Size = new Size(700, 108);
    utilityBasicTab.Position = new Position(100, 300);
    utilityBasicTab.BackgroundColor = new Color(1.0f, 1.0f, 1.0f, 0.5f);
    utilityBasicTab.UseTextNaturalSize = true;
    utilityBasicTab.ItemSpace = 40;
    utilityBasicTab.Space = new Extents(56, 56, 1, 0);
    utilityBasicTab.UnderLineSize = new Size(1, 3);
    utilityBasicTab.UnderLineBackgroundColor = color[0];
    utilityBasicTab.PointSize = 25;
    utilityBasicTab.TextColorSelector = new ColorSelector
    {
        Normal = Color.Black,
        Selected = color[0],
    };
    utilityBasicTab.ItemChangedEvent += TabItemChangedEvent;
    root.Add(utilityBasicTab);

    for (int i = 0; i < 3; i++)
    {
        Tab.TabItemData item = new Tab.TabItemData();
        item.Text = "Tab " + i;
        if(i == 1)
        {
            item.Text = "Long Tab " + i;
        }
        utilityBasicTab.AddItem(item);
    }
    utilityBasicTab.SelectedItemIndex = 0;
    ```

Following output is generated when the Tab is created using property:

![Tab](./media/tab.gif)

## Create with style

To create a Tab using style, follow these steps:

1. Create a style for Tab:

    ```cs
    TabStyle style = new TabStyle
    {
        ItemPadding = new Extents(56, 56, 1, 0),
        UnderLine = new ViewStyle
        {
            Size = new Size(1, 3),
            PositionUsesPivotPoint = true,
            ParentOrigin = Tizen.NUI.ParentOrigin.BottomLeft,
            PivotPoint = Tizen.NUI.PivotPoint.BottomLeft,
            BackgroundColor = color[0]
        },
        Text = new TextLabelStyle
        {
            PointSize = 25,
            TextColor = new Selector<Color>
            {
                Normal = Color.Black,
                Selected = color[0]
            }
        }
    };
    ```

2. Use the style to create a Tab and add it to parent:

    ```cs
    utilityBasicTab = new Tab(style);
    utilityBasicTab.Size = new Size(700, 108);
    utilityBasicTab.Position = new Position(900, 300);
    utilityBasicTab.BackgroundColor = new Color(1.0f, 1.0f, 1.0f, 0.5f);
    utilityBasicTab.ItemChangedEvent += TabItemChangedEvent;
    root.Add(utilityBasicTab);

    for (int i = 0; i < 3; i++)
    {
        Tab.TabItemData item = new Tab.TabItemData();
        item.Text = "Tab " + i;
        utilityBasicTab.AddItem(item);
    }
    utilityBasicTab.SelectedItemIndex = 0;
    ```

Following output is generated when the Tab is created using style:

![Tab](./media/tab.gif)

## Create with defined styles

You can define a style based on the user experience (UX) and then use this style to create a Tab.

1. Define a custom style:

    ```cs
    internal class CustomTabStyle : StyleBase
    {
        protected override ViewStyle GetViewStyle()
        {
            TabStyle style = new TabStyle
            {
                ItemPadding = new Extents(56, 56, 1, 0),
                UnderLine = new ViewStyle
                {
                    Size = new Size(1, 3),
                    PositionUsesPivotPoint = true,
                    ParentOrigin = Tizen.NUI.ParentOrigin.BottomLeft,
                    PivotPoint = Tizen.NUI.PivotPoint.BottomLeft,
                    BackgroundColor = color[0]
                },
                Text = new TextLabelStyle
                {
                    PointSize = 25,
                    TextColor = new Selector<Color>
                    {
                        Normal = Color.Black,
                        Selected = color[0]
                    }
                }
            };
            return style;
        }
    }
    ```

2. Register your custom style:

    ```cs
    StyleManager.Instance.RegisterStyle("CustomTab", null, typeof(YourNameSpace.CustomTabStyle));
    ```

3. Use your custom style to create a Tab instance:

    ```cs
    utilityBasicTab = new Tab("CustomTab");
    utilityBasicTab.Size = new Size(700, 108);
    utilityBasicTab.Position = new Position(900, 300);
    utilityBasicTab.BackgroundColor = new Color(1.0f, 1.0f, 1.0f, 0.5f);
    utilityBasicTab.ItemChangedEvent += TabItemChangedEvent;
    root.Add(utilityBasicTab);

    for (int i = 0; i < 3; i++)
    {
        Tab.TabItemData item = new Tab.TabItemData();
        item.Text = "Tab " + i;
        utilityBasicTab.AddItem(item);
    }
    utilityBasicTab.SelectedItemIndex = 0;
    ```

Following output is generated when the Tab is created using the defined style:

![Tab](./media/tab.gif)

## Responding to ItemChangedEvent

When you click an item on Tab, the Tab receives an item change event.
You can declare the item change event handler as follows:

```cs
Tab tab = new Tab();
tab.ItemChangedEvent += TabItemChangedEvent;
```

```cs
private void TabItemChangedEvent(object sender, Tab.ItemChangeEventArgs e)
{
    createText[0].Text = "Create Tab just by properties, Selected index from " + e.PreviousIndex + " to " + e.CurrentIndex;
}
```

## Related Information

- Dependencies
  -   Tizen 5.5 and Higher