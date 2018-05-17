---
uid: Tizen.Wearable.CircularUI.doc.TwoButtonPage
summary: TwoButtonPage control guide
---

# TwoButtonPage
`TwoButtonPage` derives from [Xamarin.Forms.Page](https://developer.xamarin.com/api/type/Xamarin.Forms.Page/). TwonButtonPage has two semicircular buttons that are located at the left side and the right side of the circle.

|![twobutton_page](data/twobutton_page.png)|![twobutton_page_overlay](data/twobutton_page_overlap.png)
|:------------:|:--------:|
|Non-overlapped|Overlapped|

## Create TwoButtonPage
You can set control in the `TwoButtonPage.Content`. In this example, long text Label and two buttons were set for Content.
If `Overlap` property is `true`, the `Content` area occupies the whole of the screen. If `Overlap` property is `false`, the `Content` area occupies screen that is excluded button's area. The default value of `Overlap` property is `false`.
`TwoButtonPage.firstButton` sets left side button. `TwoButtonPage.SecondButton` sets right side button. You can add buttons using `MenuItem`.

_This guide's code example uses WearableUIGallery's TCTwoButtonPage code at the test\WearableUIGallery\WearableUIGallery\TC\TCTwoButtonPage.xaml_

For more information. Please refer to below links
- [TwoButtonPage  API reference](https://samsung.github.io/Tizen.CircularUI/api/Tizen.Wearable.CircularUI.Forms.TwoButtonPage.html)
- [Xamarin.Forms.Page guide](https://docs.microsoft.com/en-us/xamarin/xamarin-forms/user-interface/controls/pages)
- [Xamarin.Forms.MenuItem API reference](https://developer.xamarin.com/api/type/Xamarin.Forms.MenuItem/)

**XAML file**
```xml
<?xml version="1.0" encoding="utf-8" ?>
<w:TwoButtonPage
    x:Class="WearableUIGallery.TC.TCTwoButtonPage"
    xmlns="http://xamarin.com/schemas/2014/forms"
    xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
    xmlns:local="clr-namespace:WearableUIGallery.TC"
    xmlns:w="clr-namespace:Tizen.Wearable.CircularUI.Forms;assembly=Tizen.Wearable.CircularUI.Forms">
    <w:TwoButtonPage.BindingContext>
        <local:TCTwoButtonPageViewModel />
    </w:TwoButtonPage.BindingContext>
    <w:TwoButtonPage.Content>
        <ScrollView>
            <StackLayout HorizontalOptions="FillAndExpand" VerticalOptions="FillAndExpand">
                <Label
                    HorizontalOptions="FillAndExpand"
                    HorizontalTextAlignment="Center"
                    Text="{Binding Text}"
                    VerticalOptions="FillAndExpand" />
                <Button Clicked="OnRemove1" Text="Remove 1" />
                <Button Clicked="OnRemove2" Text="Remove 2" />
            </StackLayout>
        </ScrollView>
    </w:TwoButtonPage.Content>
    <w:TwoButtonPage.FirstButton>
        <MenuItem Command="{Binding Command1}" Icon="image/tw_ic_popup_btn_check.png" />
    </w:TwoButtonPage.FirstButton>
    <w:TwoButtonPage.SecondButton>
        <MenuItem Command="{Binding Command2}" Icon="image/tw_ic_popup_btn_delete.png" />
    </w:TwoButtonPage.SecondButton>
</w:TwoButtonPage>
```

