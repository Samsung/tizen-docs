using System;
using Tizen.NUI;
using Tizen.NUI.BaseComponents;
using Tizen.NUI.Components;

namespace NUIXamlSimpleApp
{
public partial class XamlPage : ContentPage
{
    public XamlPage()
    {
        InitializeComponent();
        StringSelector s1 = new StringSelector
        {
            Normal = ImageURL + "switch/controller_switch_bg_off.png",
            Selected = ImageURL + "switch/controller_switch_bg_on.png",
            Disabled = ImageURL + "switch/controller_switch_bg_off_dim.png",
            DisabledSelected = ImageURL + "switch/controller_switch_bg_on_dim.png",
        };


        StringSelector s2 = new StringSelector
        {
            Normal = ImageURL + "switch/controller_switch_handler.png",
            Selected = ImageURL + "switch/controller_switch_handler.png",
            Disabled = ImageURL + "switch/controller_switch_handler_dim.png",
            DisabledSelected = ImageURL + "switch/controller_switch_handler_dim.png",
        };

        switch1.SwitchBackgroundImageURLSelector = s1;
        switch1.SwitchHandlerImageURLSelector = s2;

        switch2.SwitchBackgroundImageURLSelector = s1;
        switch2.SwitchHandlerImageURLSelector = s2;

        switch3.SwitchBackgroundImageURLSelector = s1;
        switch3.SwitchHandlerImageURLSelector = s2;

        switch4.SwitchBackgroundImageURLSelector = s1;
        switch4.SwitchHandlerImageURLSelector = s2;
    }
}
}
