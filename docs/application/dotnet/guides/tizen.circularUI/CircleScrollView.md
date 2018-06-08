---
uid: Tizen.Wearable.CircularUI.doc.CircleScrollView
summary: CircleScrollView control guide
---
# CircleScrollView

`CircleScrollView` is to ensure that larger views display well on smaller wearable devices.
It is an extension of [Xamarin.Forms.ScrollView](https://developer.xamarin.com/api/type/Xamarin.Forms.ScrollView/). Similar to [Xamarin.Forms.ScrollView](https://developer.xamarin.com/api/type/Xamarin.Forms.ScrollView/), but the Scroller is rendered to [CircleSurface](https://developer.tizen.org/development/guides/native-application/user-interface/efl/ui-components/wearable-ui-components/circle-surface). Scrolling is possible with [Bezel interaction](https://developer.tizen.org/design/wearable/interaction/bezel-interactions).
To receive [Rotary event](https://developer.tizen.org/development/training/native-application/understanding-tizen-programming/event-handling#rotary), it must be registered as `RotaryFocusObject`, property of [CirclePage](xref:Tizen.Wearable.CircularUI.doc.CirclePage).

|![Horizontal](data/CircleScrollView_Horizontal.png)|![Vertical](data/CircleScrollView_Vertical.png)|
|:-----------------------------------------------:|:-----------------------------------------------:|
|                      Horizontal                 |                    Vertical                     |

**WARNING: [CircleListView](xref:Tizen.Wearable.CircularUI.doc.CircleListView), [CircleDateTimeSelector](xref:Tizen.Wearable.CircularUI.doc.CircleDateTimeSelector), [CircleScrollView](xref:Tizen.Wearable.CircularUI.doc.CircleScrollView), [CircleStepper](xref:Tizen.Wearable.CircularUI.doc.CircleStepper) must be confined in the `CirclePage` container or [Page](https://developer.xamarin.com/api/type/Xamarin.Forms.Page/) with [CircleSurfaceEffectBehavior](xref:Tizen.Wearable.CircularUI.doc.CircleSurfaceEffectBehavior). If you add these controls in any other way,  it may cause an exception or cannot display the controls.**

## Add CircleScrollView in CirclePage

You can set `CircleScrollView` in [CirclePage.Content](xref:Tizen.Wearable.CircularUI.doc.CirclePage). For more information about how to add a [CirclePage](xref:Tizen.Wearable.CircularUI.doc.CirclePage), see [CirclePage guide](https://samsung.github.io/Tizen.CircularUI/guide/CirclePage.html#create-circlepage).
The following XAML code shows [CirclePage](xref:Tizen.Wearable.CircularUI.doc.CirclePage) with `CircleScrollView`.
`RotaryFocusTargetName` property sets the currently focused control that is handled by rotating and displays the circle object of focused control.
If the value is not set properly, the control does not receive the [Rotary Event](https://developer.tizen.org/development/training/native-application/understanding-tizen-programming/event-handling#rotary).

The direction of the scroller depends on the setting of the `Orientation` value.

In the following example, the `Orientation` of the `CircleScrollView` is set to `Horizontal` and is placed in the `StackLayout` to contain many images:

For more information, see the following links:

- [CircleScrollView API reference](https://samsung.github.io/Tizen.CircularUI/api/Tizen.Wearable.CircularUI.Forms.CircleScrollView.html)
- [Xamarin.Forms.ScrollView API reference](https://developer.xamarin.com/api/type/Xamarin.Forms.ScrollView/)
- [Xamarin.Forms.ScrollView Guide](https://docs.microsoft.com/en-us/xamarin/xamarin-forms/user-interface/layouts/scroll-view)

_The code example of this guide uses HorizontalScroller.xaml code of XUIComponent. The code is available in sample\XUIComponents\UIComponents\UIComponents\Samples\CircleScroller/HorizontalScroller.xaml_

The following code shows CirclePage with CircleScrollView:

**XAML file**

```xml
<w:CirclePage
    x:Class="UIComponents.Samples.CircleScroller.HorizontalScroller"
    xmlns="http://xamarin.com/schemas/2014/forms"
    xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
    xmlns:local="clr-namespace:UIComponents.Samples.CircleScroller"
    xmlns:sys="clr-namespace:System;assembly=netstandard"
    xmlns:w="clr-namespace:Tizen.Wearable.CircularUI.Forms;assembly=Tizen.Wearable.CircularUI.Forms"
    RotaryFocusTargetName="myscroller">
    <w:CirclePage.Content>
        <w:CircleScrollView x:Name="myscroller" Orientation="Horizontal">
            <StackLayout
                HorizontalOptions="FillAndExpand"
                Orientation="Horizontal"
                VerticalOptions="FillAndExpand">
                <Image Source="tw_btn_delete_holo_dark.png" VerticalOptions="CenterAndExpand" />
                <Image Source="tw_number_controller_icon_ringtone_mute.png" VerticalOptions="CenterAndExpand" />
                <Image Source="tw_ic_popup_btn_check.png" VerticalOptions="CenterAndExpand" />
                <Image Source="tw_number_controller_icon_alert.png" VerticalOptions="CenterAndExpand" />
                <Image Source="tw_number_controller_icon_bell.png" VerticalOptions="CenterAndExpand" />
                <Image Source="tw_number_controller_icon_ringtone_sound.png" VerticalOptions="CenterAndExpand" />
                <Image Source="tw_btn_delete_holo_dark.png" VerticalOptions="CenterAndExpand" />
                <Image Source="tw_number_controller_icon_ringtone_mute.png" VerticalOptions="CenterAndExpand" />
                <Image Source="tw_ic_popup_btn_check.png" VerticalOptions="CenterAndExpand" />
                <Image Source="tw_number_controller_icon_alert.png" VerticalOptions="CenterAndExpand" />
                <Image Source="tw_number_controller_icon_bell.png" VerticalOptions="CenterAndExpand" />
                <Image Source="tw_number_controller_icon_ringtone_sound.png" VerticalOptions="CenterAndExpand" />
                <Image Source="tw_btn_delete_holo_dark.png" VerticalOptions="CenterAndExpand" />
                <Image Source="tw_number_controller_icon_ringtone_mute.png" VerticalOptions="CenterAndExpand" />
                <Image Source="tw_ic_popup_btn_check.png" VerticalOptions="CenterAndExpand" />
                <Image Source="tw_number_controller_icon_alert.png" VerticalOptions="CenterAndExpand" />
                <Image Source="tw_number_controller_icon_bell.png" VerticalOptions="CenterAndExpand" />
                <Image Source="tw_number_controller_icon_ringtone_sound.png" VerticalOptions="CenterAndExpand" />
            </StackLayout>
        </w:CircleScrollView>
    </w:CirclePage.Content>
</w:CirclePage>

```