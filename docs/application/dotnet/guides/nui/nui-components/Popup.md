# Popup
This tutorial describes how to create and use Popup.

## Overview
Popup is one kind of common component, it can be used as popup window.
User can handle Popup button count, head title and content area.

## Create with property
1. Create Popup by default constructor

~~~{.cs}
Popup popup = new Popup();
~~~

2. Set popup property

~~~{.cs}
//set Popup property
NPatchVisual nvisual = new NPatchVisual();
nvisual.URL = "popup_background.png";
nvisual.Border = new Rectangle(0, 0, 81, 81);
popup.MinimumSize = new Size2D(1032, 184);
popup.Size = new Size(1032, 400);
popup.Position = new Position(200, 100);

//set Popup title property
popup.TitlePointSize = 25;
popup.TitleTextColor = Color.Black;
popup.TitleHeight = 68;
popup.TitleTextHorizontalAlignment = HorizontalAlignment.Begin;
popup.TitleTextPosition = new Position(64, 52);
popup.TitleText = "Popup Title";

popup.ButtonTextColor = color[index];
popup.ButtonHeight = 132;
popup.ButtonCount = 2;
popup.SetButtonText(0, "Yes");
popup.SetButtonText(1, "Exit");
root.Add(popup);
~~~

Popup created by property:

![PopupProperty](./media/PopupProperty.PNG)

## Responding to PopupButtonClickEvent
When user click popup button, the Popup instance receives a PopupButtonClickEvent.
You can declare the event handler as following:

~~~{.cs}
Popup popup = new Popup();
popup.PopupButtonClickEvent += PopupButtonClickEvent;
private void PopupButtonClickEvent(object sender, Tizen.NUI.CommonUI.Popup.ButtonClickEventArgs e)
{
    Tizen.Log.Info("CommonUI", "Button index " + e.ButtonIndex + " is clicked");
}
~~~

## Related Information
- Dependencies
  -   Tizen 5.5 and Higher