# Toast

Toast is a common component and provides simple messages.

Unlike other popups, a Toast consists only of a body field as it is just used for providing simple feedback to the user’s actions.

You can use a Toast to provide simple messages when the user does not need to make an additional action or confirmation. A Toast will automatically disappear after a certain time.

![Toast](./media/toast.png)

## Create with property

To create a Toast using property, follow these steps:

1. Create Toast using the default constructor:

    ```cs
    utilityBasicToast = new Toast();
    ```

2. Set the Toast property:

    ```cs
    NPatchVisual nvisual = new NPatchVisual();
    nvisual.URL = "Poptoast_background.png";
    nvisual.Border = new Rectangle(64, 64, 4, 4);
    utilityBasicToast.Position = new Position(50, 350);
    utilityBasicToast.Size = new Size(512, 132);
    utilityBasicToast.TextArray = new string[1] { "null parameter" };
    utilityBasicToast.PointSize = 26;
    utilityBasicToast.TextColor = Color.White;
    utilityBasicToast.TextPadding = new Extents(96, 96, 38, 38);
    utilityBasicToast.Duration = 1500;
    root.Add(utilityBasicToast);
    ```

Following output is generated when the Toast is created using property:

![Toast](./media/toast.gif)

## Create with style

To create a Toast using style, follow these steps:

1. Create a style for Toast:

    ```cs
    ToastStyle style = new ToastStyle
    {
        Size = new Size(512, 132),
        Text = new TextLabelStyle
        {
            Padding = new Extents(96, 96, 38, 38),
            PointSize = 26,
            TextColor = Color.White,
        },
        BackgroundImage = "Poptoast_background.png",
        BackgroundImageBorder = new Rectangle(64, 64, 4, 4),
        Duration = 1500
    };
    ```

2. Use the style to create a Toast and add it to parent:

    ```cs
    utilityBasicToast = new Toast(style);
    utilityBasicToast.TextArray = new string[1] { "null parameter" };
    utilityBasicToast.Position = new Position(650, 350);
    root.Add(utilityBasicToast);
    ```

Following output is generated when the Toast is created using style:

![Toast](./media/toast.gif)

## Create with defined styles

You can define a style based on the user experience (UX) and then use this style to create a Toast.

1. Define a custom style:

    ```cs
    internal class CustomToastStyle : StyleBase
    {
        protected override ViewStyle GetViewStyle()
        {
            ToastStyle style = new ToastStyle
            {
                Size = new Size(512, 132),
                Text = new TextLabelStyle
                {
                    Padding = new Extents(96, 96, 38, 38),
                    PointSize = 26,
                    TextColor = Color.White,
                },
                BackgroundImage = "Poptoast_background.png",
                BackgroundImageBorder = new Rectangle(64, 64, 4, 4),
                Duration = 1500
            };
            return style;
        }
    }
    ```

2. Register your custom style:

    ```cs
    StyleManager.Instance.RegisterStyle("CustomToast", null, typeof(YourNameSpace.CustomToastStyle));
    ```

3. Use your custom style to create a Toast instance:

    ```cs
    utilityBasicToast = new Toast("CustomToast");
    utilityBasicToast.TextArray = new string[1] { "null parameter" };
    utilityBasicToast.Position = new Position(650, 350);
    root.Add(utilityBasicToast);
    ```

Following output is generated when the Toast is created using the defined style:

![Toast](./media/toast.gif)

## Related Information

- Dependencies
  -   Tizen 5.5 and Higher
