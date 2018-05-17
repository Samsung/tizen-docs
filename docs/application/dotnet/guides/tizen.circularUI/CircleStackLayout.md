---
uid: Tizen.Wearable.CircularUI.doc.CircleStackLayout
summary: CircleStackLayout control guide
---
# CircleStackLayout

`CircleStackLayout` organizes views in a one-dimensional line ("stack"), either horizontally or vertically.
It is the same as [Xamarin.Forms.StackLayout](https://developer.xamarin.com/api/type/Xamarin.Forms.StackLayout/), but it arranges internal components in a form that fits the circular screen.
Rectangular components are placed in close proximity to the circle, and margin is calculated after placement.

If you don't set `Orientation`, `Vertical` will be used.
The larger the `Spacing` value, the greater the distance between the components placed.
At the right end of the figure below, the `Spacing` value is 50.

|![Horizontal](data/CircleStackLayout_Horizontal.png)|![Vertical](data/CircleStackLayout_Vertical.png)|![Spacing](data/CircleStackLayout_Spacing.png)|
|:--------------------------------------------------:|:----------------------------------------------:|:--------------------------------------------:|
|                   Horizontal                       |                     Vertical                   |                     Spacing                  |

## Adding CircleStackLayout at ContentPage

You can set `CircleStackLayout` at [ContentPage](https://developer.xamarin.com/api/type/Xamarin.Forms.ContentPage/). To create a new component, use the following XAML code.

In the example below, the number of [BoxView](https://docs.microsoft.com/en-us/xamarin/xamarin-forms/user-interface/boxview) is large, so the entire contents are larger than the screen size.
 So we use `CircleStackLayout` in [ScrollView](https://docs.microsoft.com/en-us/xamarin/xamarin-forms/user-interface/layouts/scroll-view).

For more information. Please refer to below links

- [CircleStackLayout API reference](https://samsung.github.io/Tizen.CircularUI/api/Tizen.Wearable.CircularUI.Forms.CircleStackLayout.html)
- [Xamarin.Forms.StackLayout API reference](https://developer.xamarin.com/api/type/Xamarin.Forms.StackLayout/)
- [Xamarin.Forms.StackLayout Guide](https://docs.microsoft.com/en-us/xamarin/xamarin-forms/user-interface/layouts/stack-layout)

_This guide's code example uses WearableUIGallery's TCCircleStackLayout.xaml code at the test\WearableUIGallery\WearableUIGallery\TC\TCCircleStackLayout.xaml_

**XAML file**

```xml
<?xml version="1.0" encoding="utf-8" ?>
<w:IndexPage
    x:Class="WearableUIGallery.TC.TCCircleStackLayout"
    xmlns="http://xamarin.com/schemas/2014/forms"
    xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
    xmlns:local="clr-namespace:WearableUIGallery"
    xmlns:w="clr-namespace:Tizen.Wearable.CircularUI.Forms;assembly=Tizen.Wearable.CircularUI.Forms">
    ...
    <ContentPage>
        <ScrollView>
            <w:CircleStackLayout>
                <BoxView BackgroundColor="Red" />
                <BoxView BackgroundColor="Orange" />
                <BoxView BackgroundColor="Yellow" />
                <BoxView BackgroundColor="Green" />
                <BoxView BackgroundColor="Blue" />
                <BoxView BackgroundColor="Navy" />
                <BoxView BackgroundColor="Purple" />
                <BoxView BackgroundColor="Red" />
                <BoxView BackgroundColor="Orange" />
                <BoxView BackgroundColor="Yellow" />
                <BoxView BackgroundColor="Green" />
                <BoxView BackgroundColor="Blue" />
                <BoxView BackgroundColor="Navy" />
                <BoxView BackgroundColor="Purple" />
            </w:CircleStackLayout>
        </ScrollView>
    </ContentPage>
    ...
</w:IndexPage>
```