# Popup
Popup is a common component that is used as a popup window. You can manage a popup button count, head title, and content area.

A popup can be created using property.

![PopupProperty](./media/PopupProperty.PNG)

> [!NOTE]
> Popup is deprecated since Tizen 6.0 and will be removed after two releases.

## Add namespace
To implement popup, include `Tizen.NUI.Components` namespace in your application:

```cs
using Tizen.NUI;
using Tizen.NUI.Components;
```

## Create with Property

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
