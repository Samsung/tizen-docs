---
uid: Tizen.Wearable.CircularUI.doc.CircleSurfaceEffectBehavior
summary: CircleSurfaceEffectBehavior guide
---

# CircleSurfaceEffectBehavior
`CircleSurfaceEffectBehavior` is an effect which allows to attach `CircleSurface` to [Xamarin.Forms.Page](https://developer.xamarin.com/api/type/Xamarin.Forms.Page/). [CircleSurface](https://developer.tizen.org/development/guides/native-application/user-interface/efl/ui-components/wearable-ui-components/circle-surface) is Tizen specific component that manages [circle objects](https://developer.tizen.org/development/guides/native-application/user-interface/efl/ui-components/wearable-ui-components/circle-object).
If you need to add `circle control`(such as [CircleListView](xref:Tizen.Wearable.CircularUI.doc.CircleListView), [CircleDateTimeSelector](xref:Tizen.Wearable.CircularUI.doc.CircleDateTimeSelector), [CircleScrollView](xref:Tizen.Wearable.CircularUI.doc.CircleScrollView), [CircleStepper](xref:Tizen.Wearable.CircularUI.doc.CircleStepper)) at `Page` in Tizen Xamarin Forms application, there are two ways. One is inserting these controls to `CirclePage`, the other is adding `CircleSurfaceEffectBehavior` at `Page` that includes `circle control`.

## Adding CircleSurfaceEffectBehavior at Page
Add `CircleSurfaceEffectBehavior` at `<Page.Behaviors>`. And then set `RotaryFocusTargetName` property with `circle control` name. `RotaryFocusTargetName` sets the currently focused control that is handled by rotating and display the focused control's circle object. Please refer to below sample code.

_This guide's code example uses WearableUIGallery's TCListAppender code at the test\WearableUIGallery\WearableUIGallery\TC\TCListAppender.xaml_

For more information. Please refer to below links
- [CircleSurfaceEffectBehavior API reference](https://samsung.github.io/Tizen.CircularUI/api/Tizen.Wearable.CircularUI.Forms.CircleSurfaceEffectBehavior.html)
- [Xamarin.Forms.Page guide](https://docs.microsoft.com/en-us/xamarin/xamarin-forms/user-interface/controls/pages)
- [Consuming a Xamarin.Forms Behavior](https://docs.microsoft.com/en-us/xamarin/xamarin-forms/app-fundamentals/behaviors/creating#consuming-a-xamarinforms-behavior)

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

