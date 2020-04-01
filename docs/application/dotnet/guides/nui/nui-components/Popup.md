# Popup

Popup is a common component that is used as a popup window. You can manage a popup button count, head title, and content area.

A popup can be created using property.

![PopupProperty](./media/PopupProperty.PNG)

## Create with property

To create a popup using property, follow these steps:

1. Create popup using the default constructor:

    ```cs
    Popup popup = new Popup();
    ```

2. Set the popup property:

    ```cs
    //set Popup property
    NPatchVisual nvisual = new NPatchVisual();
    nvisual.URL = "popup_background.png";
    nvisual.Border = new Rectangle(0, 0, 81, 81);
    popup.MinimumSize = new Size(1032, 184);
    popup.Size = new Size(1032, 400);
    popup.Position = new Position(200, 100);

    //set Popup title property
    popup.TitlePointSize = 25;
    popup.TitleTextColor = Color.Black;
    popup.TitleHeight = 68;
    popup.TitleTextHorizontalAlignment = HorizontalAlignment.Begin;
    popup.TitleTextPosition = new Position(64, 52);
    popup.TitleText = "Popup Title";

    popup.ButtonTextColor = new Color(0.05f, 0.63f, 0.9f, 1);
    popup.ButtonHeight = 132;
    popup.ButtonCount = 2;
    popup.SetButtonText(0, "Yes");
    popup.SetButtonText(1, "Exit");
    root.Add(popup);
    ```

Following output is generated when the popup is created using property:

![PopupProperty](./media/PopupProperty.PNG)

## Create with style

To create a popup using style, follow these steps:

1. Create a style for popup:

    ```cs
    PopupStyle style = new PopupStyle
    {
        MinimumSize = new Size(1032, 184),
        BackgroundImage = "popup_background.png",
        BackgroundImageBorder = new Rectangle(0, 0, 81, 81),
        Title = new TextLabelStyle
        {
            PointSize = 25,
            TextColor = Color.Black,
            Size = new Size(0, 68),
            HorizontalAlignment = HorizontalAlignment.Begin,
            Position = new Position(64, 52),
            Text = "Popup Title"
        },
        Buttons = new ButtonStyle
        {
            Text = new TextLabelStyle
            {
                TextColor = new Color(0.05f, 0.63f, 0.9f, 1)
            }
        }
    };
    ```

2. Use the style to create a popup and add it to parent:

    ```cs
    popup2 = new Popup(style);
    popup2.Size = new Size(1032, 400);
    popup2.Position = new Position(200, 600);
    popup2.ButtonHeight = 132;
    popup2.ButtonCount = 2;
    popup2.SetButtonText(0, "Yes");
    popup2.SetButtonText(1, "Exit");
    root.Add(popup2);
    ```

Following output is generated when the popup is created using style:

![PopupProperty](./media/PopupProperty.PNG)

## Create with defined styles

You can define a style based on the user experience (UX) and then use this style to create a popup.

1. Define a custom style:

    ```cs
    internal class CustomPopupStyle : StyleBase
    {
        protected override ViewStyle GetViewStyle()
        {
            PopupStyle style = new PopupStyle
            {
                MinimumSize = new Size(1032, 184),
                BackgroundImage = "popup_background.png",
                BackgroundImageBorder = new Rectangle(0, 0, 81, 81),
                Title = new TextLabelStyle
                {
                    PointSize = 25,
                    TextColor = Color.Black,
                    Size = new Size(0, 68),
                    HorizontalAlignment = HorizontalAlignment.Begin,
                    Position = new Position(64, 52),
                    Text = "Popup Title"
                },
                Buttons = new ButtonStyle
                {
                    Text = new TextLabelStyle
                    {
                        TextColor = new Color(0.05f, 0.63f, 0.9f, 1)
                    }
                }
            };
            return style;
        }
    }
    ```

2. Register your custom style:

    ```cs
    StyleManager.Instance.RegisterStyle("CustomPopup", null, typeof(YourNameSpace.CustomPopupStyle));
    ```

3. Use your custom style to create a popup instance:

    ```cs
    popup = new Tizen.NUI.CommonUI.Popup("CustomPopup");
    popup.Size = new Size(1032, 400);
    popup.Position = new Position(1200, 50);
    popup.ButtonHeight = 132;
    popup.ButtonCount = 2;
    popup.SetButtonText(0, "Yes");
    popup.SetButtonText(1, "Exit");
    root.Add(popup);
    ```

Following output is generated when the popup is created using the defined style:

![PopupProperty](./media/PopupProperty.PNG)

## Responding to PopupButtonClickEvent

When you click the popup button, the popup instance receives a PopupButtonClickEvent.
You can declare the event handler as follows:

```cs
Popup popup = new Popup();
popup.PopupButtonClickEvent += PopupButtonClickEvent;
```

```cs
private void PopupButtonClickEvent(object sender, Tizen.NUI.CommonUI.Popup.ButtonClickEventArgs e)
{
    Tizen.Log.Info("CommonUI", "Button index " + e.ButtonIndex + " is clicked");
}
```

## Related Information

- Dependencies
  -   Tizen 5.5 and Higher