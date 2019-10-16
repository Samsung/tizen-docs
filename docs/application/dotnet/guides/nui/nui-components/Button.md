# Button
This tutorial describes how to create and use button.

## Overview
Button is one kind of common component and clearly describes what action will occur when user select it.

- Button can contain text or icon.
- Button can be created by property.

## Create with property
1. Create Button by default constructor

~~~{.cs}
utilityBasicButton = new Button();
~~~

2. Set button property

~~~{.cs}
NPatchVisual nvisual = new NPatchVisual();
nvisual.URL = "rectangle_point_btn_normal.png";
nvisual.Border = new Rectangle(5, 5, 5, 5);
utilityBasicButton.IsSelectable = true;
utilityBasicButton.Background = nvisual.OutputVisualMap;

utilityBasicButton.TextColorSelector = new ColorSelector
{
    Normal = new Color(0, 0, 0, 1),
    Pressed = new Color(0, 0, 0, 0.7f),
    Selected = new Color(0.058f, 0.631f, 0.92f, 1),
    Disabled = new Color(0, 0, 0, 0.4f)
};

utilityBasicButton.Size = new Size2D(300, 80);
utilityBasicButton.Position = new Position2D(100, 300);
utilityBasicButton.PointSize = 20;
utilityBasicButton.Text = "UtilityBasicButton";
root.Add(utilityBasicButton);
~~~

Button created by property:

![ButtonProperty](./media/ButtonProperty.PNG)


## Responding to ClickEvent
When user click a button, the Button instance receives a click event.
You can declare the click event handler as following:

~~~{.cs}
Button button = new Button();
button.ClickEvent += OnClick;
~~~

~~~{.cs}
private void OnClick(object sender, Button.ClickEventArgs e)
{
    // Do something in response to button click
}
~~~

## Responding to StateChangedEvent
Button has 8 states including Normal, Focused, Disabled, Selected, Pressed, DisabledFocused, SelectedFocused and DisabledSelected.
When the user change button state ( change focus or disable a button), the Button instance receives an StateChangedEvent.

~~~{.cs}
Button button = new Button();
button.StateChangedEvent += OnStateChange;
~~~

~~~{.cs}
private void OnStateChange(object sender, Button.StateChangeEventArgs e)
{
    // Do something in response to state change
}
~~~

## Related Information
- Dependencies
  -   Tizen 5.5 and Higher
