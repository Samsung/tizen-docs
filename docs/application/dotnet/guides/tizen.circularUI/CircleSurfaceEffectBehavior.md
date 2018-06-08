---
uid: Tizen.Wearable.CircularUI.doc.CircleSurfaceEffectBehavior
summary: CircleSurfaceEffectBehavior guide
---

# CircleSurfaceEffectBehavior
The `CircleSurfaceEffectBehavior` is an effect, which allows you to attach the `CircleSurface` to the [Xamarin.Forms.Page](https://developer.xamarin.com/api/type/Xamarin.Forms.Page/). [CircleSurface](https://developer.tizen.org/development/guides/native-application/user-interface/efl/ui-components/wearable-ui-components/circle-surface) is a Tizen specific component that manages [circle objects](https://developer.tizen.org/development/guides/native-application/user-interface/efl/ui-components/wearable-ui-components/circle-object).

Following are the two ways to add circle control such as [CircleListView](xref:Tizen.Wearable.CircularUI.doc.CircleListView), [CircleDateTimeSelector](xref:Tizen.Wearable.CircularUI.doc.CircleDateTimeSelector), [CircleScrollView](xref:Tizen.Wearable.CircularUI.doc.CircleScrollView) and [CircleStepper](xref:Tizen.Wearable.CircularUI.doc.CircleStepper) at `Page` in Tizen Xamarin Forms application:

- Inserting these controls to `CirclePage`.
- Adding `CircleSurfaceEffectBehavior` in `Page` that includes circle control.

## Add CircleSurfaceEffectBehavior in Page

Add the `CircleSurfaceEffectBehavior` in the `<Page.Behaviors>` and set `RotaryFocusTargetName` property with circle control name.
The `RotaryFocusTargetName` sets the currently focused control that is handled by rotating and display the focused control's circle object.

For more information, see the following links:
- [CircleSurfaceEffectBehavior API reference](https://samsung.github.io/Tizen.CircularUI/api/Tizen.Wearable.CircularUI.Forms.CircleSurfaceEffectBehavior.html)
- [Xamarin.Forms.Page guide](https://docs.microsoft.com/en-us/xamarin/xamarin-forms/user-interface/controls/pages)
- [Consuming a Xamarin.Forms Behavior](https://docs.microsoft.com/en-us/xamarin/xamarin-forms/app-fundamentals/behaviors/creating#consuming-a-xamarinforms-behavior)

_The code example of this guide uses TCListAppender code of WearableUIGallery. The code is available in test\WearableUIGallery\WearableUIGallery\TC\TCListAppender.xaml_

**XAML file**
```xml
<w:TwoButtonPage xmlns="http://xamarin.com/schemas/2014/forms"
                 xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
                 xmlns:w="clr-namespace:Tizen.Wearable.CircularUI.Forms;assembly=Tizen.Wearable.CircularUI.Forms"
                 x:Class="WearableUIGallery.TC.TCListAppender">
    <w:TwoButtonPage.`CircleSurfaceEffectBehavior` at>
        <w:CircleSurfaceEffectBehavior RotaryFocusTargetName="mylist"/>
    </w:TwoButtonPage.Behaviors>
    <w:TwoButtonPage.Content>
        <w:CircleListView x:Name="mylist"  HorizontalOptions="FillAndExpand" VerticalOptions="FillAndExpand">

    </w:TwoButtonPage.Content>
    <w:TwoButtonPage.FirstButton>
        <MenuItem Clicked="DoAdd" Icon="image/tw_ic_popup_btn_check.png" />
    </w:TwoButtonPage.FirstButton>
    <w:TwoButtonPage.SecondButton>
        <MenuItem Clicked="DoDel" Icon="image/tw_ic_popup_btn_delete.png" />
    </w:TwoButtonPage.SecondButton>
</w:TwoButtonPage>
```

