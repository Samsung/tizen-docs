# Pagination

Pagination is a common component supporting multiple pages. It shows the number of pages available and the currently active page.

![Pagination](./media/Pagination.PNG)

## Create with property

To create a Pagination using property, follow these steps:

1. Create Pagination using the default constructor:

    ```cs
    pagination = new Pagination();
    ```

2. Set the Pagination property:

    ```cs
    var indicatorImageUrlStyle = new PaginationStyle()
    {
        IndicatorImageUrl = new Selector<string>
        {
            Normal = "pagination_ic_nor.png",
            Selected = "pagination_ic_sel.png"
        }
    };
    pagination.ApplyStyle(indicatorImageUrlStyle);
    pagination.IndicatorSize = new Size(26, 26);
    pagination.IndicatorSpacing = 8;
    pagination.Name = "Pagination1";
    pagination.Size = new Size(300, 50);
    pagination.BackgroundColor = new Color(1.0f, 1.0f, 1.0f, 0.6f);
    pagination.IndicatorCount = 5;
    pagination.SelectedIndex = 1;
    root.Add(pagination);
    ```

Following output is generated when the Pagination is created using property:

![Pagination1](./media/Pagination1.PNG)

## Create with style

To create a Pagination using style, follow these steps:

1. Create a style for Pagination:

    ```cs
    PaginationStyle style = new PaginationStyle()
    {
        IndicatorSize = new Size(15, 15),
        IndicatorSpacing = 20,
        IndicatorImageUrl = new Selector<string>
        {
            Normal = "pagination_ic_nor.png",
            Selected = "pagination_ic_sel.png"
        },
        Name = "Pagination2",
        Size = new Size(300, 50),
        BackgroundColor = new Color(1.0f, 1.0f, 1.0f, 0.6f),
    };
    ```

2. Use the style to create a Pagination and add it to parent:

    ```cs
    pagination = new Pagination(style);
    pagination.IndicatorCount = 5;
    pagination.SelectedIndex = 2;
    root.Add(pagination);
    ```

Following output is generated when the Pagination is created using style:

![Pagination2](./media/Pagination2.PNG)

## Create with defined styles

You can define a style based on the user experience (UX) and then use this style to create a Pagination.

1. Define a custom style:

    ```cs
    internal class CustomPaginationStyle : StyleBase
    {
        protected override ViewStyle GetViewStyle()
        {
            PaginationStyle style = new PaginationStyle
            {
                IndicatorSize = new Size(15, 15),
                IndicatorSpacing = 20,
                IndicatorImageUrl = new Selector<string>
                {
                    Normal = "pagination_ic_nor.png",
                    Selected = "pagination_ic_sel.png"
                },
                Name = "Pagination2",
                Size = new Size(300, 50),
                BackgroundColor = new Color(1.0f, 1.0f, 1.0f, 0.6f),
            };
            return style;
        }
    }
    ```

2. Register your custom style:

    ```cs
    StyleManager.Instance.RegisterStyle("CustomPagination", null, typeof(YourNameSpace.CustomPaginationStyle));
    ```

3. Use your custom style to create a Pagination instance:

    ```cs
    pagination = new Pagination("CustomPagination");
    pagination.IndicatorCount = 5;
    pagination.SelectedIndex = 2;
    root.Add(pagination);
    ```

Following output is generated when the Pagination is created using the defined style:

![Pagination2](./media/Pagination2.PNG)

## Responding to window key event

When you press "left", the currently active page will change to previous page.
When you press "right", the currently active page will change to next page.
You can declare the window key event as follows:

```cs
Window window = NUIApplication.GetDefaultWindow();
window.KeyEvent += Window_KeyEvent;
```

```cs
private void Window_KeyEvent(object sender, Window.KeyEventArgs e)
{
    if (e.Key.State == Key.StateType.Down)
    {
        if (e.Key.KeyPressedName == "Left")
        {
            if (pagination.SelectedIndex > 0)
            {
                pagination.SelectedIndex = pagination.SelectedIndex - 1;
            }
        }
        else if (e.Key.KeyPressedName == "Right")
        {
            if (pagination.SelectedIndex < pagination.IndicatorCount - 1)
            {
                pagination.SelectedIndex = pagination.SelectedIndex + 1;
            }
        }
    }
}
```

## Related Information

- Dependencies
  -   Tizen 6.0 and Higher
