# Switch
This tutorial describes how to create and use Switch.

## Overview
Switch is one kind of common component, it can be used as selector.

## Create with property
1. Create Switch by default constructor

~~~{.cs}
Switch[] utilitySwitch = new Switch[4];
~~~

2. Set switch property

~~~{.cs}
int num = 4;
for(int i = 0; i < num; i++)
{
    utilitySwitch[i] = new Switch();
    utilitySwitch[i].Size = new Size(96, 60);
    utilitySwitch[i].Position = new Position(300 + 100 * i, 300);
    utilitySwitch[i].SwitchHandlerImageSize = new Size(60, 60);
    utilitySwitch[i].SwitchBackgroundImageURLSelector = new StringSelector
    {
        Normal = "controller_switch_bg_off.png",
        Selected = "controller_switch_bg_on.png",
        Disabled = "controller_switch_bg_off_dim.png",
        DisabledSelected = "controller_switch_bg_on_dim.png",
    };
    utilitySwitch[i].SwitchHandlerImageURLSelector = new StringSelector
    {
        Normal = "controller_switch_handler.png",
        Selected = "controller_switch_handler.png",
        Disabled = "controller_switch_handler_dim.png",
        DisabledSelected = "controller_switch_handler_dim.png",
    };
    root.Add(utilitySwitch[i]);
}
utilitySwitch[0].IsSelected = true;
utilitySwitch[2].IsEnabled = false;
utilitySwitch[3].IsEnabled = false;
~~~

Switch created by property:

![SwitchProperty](./media/SwitchProperty.PNG)

## Responding to SelectedEvent
When user click switch, the Popup instance receives a SelectedEvent.
You can declare the event handler as following:

~~~{.cs}
Switch switchControl = new Switch();
switchControl.SelectedEvent += OnSelected;
~~~

~~~{.cs}
private void OnSelected(object sender, Switch.SelectEventArgs e)
{
    //Do something when user select the switch
}
~~~

## Related Information
- Dependencies
  -   Tizen 5.5 and Higher