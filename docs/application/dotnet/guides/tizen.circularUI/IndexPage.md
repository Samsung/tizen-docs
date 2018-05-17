---
uid: Tizen.Wearable.CircularUI.doc.IndexPage
summary: IndexPage control guide
---
# IndexPage

`IndexPage` allows you to know in advance how many pages you have when you configure your application on multiple pages, and  to show you how many pages you are viewing.
It is extension of [Xamarin.Forms.MultiPage](https://developer.xamarin.com/api/type/Xamarin.Forms.MultiPage%3CT%3E/).
When [Page](https://docs.microsoft.com/en-us/xamarin/xamarin-forms/user-interface/controls/pages) is added and removed at [Xamarin.Forms.MultiPage](https://developer.xamarin.com/api/type/Xamarin.Forms.MultiPage%3CT%3E/), the number of dot marks increases or decreases automatically at the top of window.
It is similar to [CarouselPage](https://docs.microsoft.com/en-us/xamarin/xamarin-forms/user-interface/controls/pages#carouselpage) in Xamarin.Forms, with the addition of `Index`.
When [Page](https://docs.microsoft.com/en-us/xamarin/xamarin-forms/user-interface/controls/pages) is scrolled, `Index` operates select internally.

![](data/IndexPage_action.png)

## Adding IndexPage

To create a new index component, use the following XAML code.
If you add as many pages as you want, you will increase the number of dot mark by index accordingly. In the example below, 3 pages have been added. The number of dot mark is 3. Because it is on the first page, only the first dot mark is shown as white, and the remaining dot marks are shown as grey.

For more information. Please refer to below links

- [IndexPage  API reference](https://samsung.github.io/Tizen.CircularUI/api/Tizen.Wearable.CircularUI.Forms.IndexPage.html)
- [Xamarin.Forms.MultiPage  API reference](https://developer.xamarin.com/api/type/Xamarin.Forms.MultiPage%3CT%3E/)

_This guide's code example use WearableUIGallery's TCIndexPage.xaml code at the test\WearableUIGallery\WearableUIGallery\TC\TCIndexPage.xaml_

**XAML file**

```xml

<?xml version="1.0" encoding="utf-8" ?>
<w:IndexPage
    x:Class="WearableUIGallery.TC.TCIndexPage"
    xmlns="http://xamarin.com/schemas/2014/forms"
    xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
    xmlns:local="clr-namespace:WearableUIGallery"
    xmlns:w="clr-namespace:Tizen.Wearable.CircularUI.Forms;assembly=Tizen.Wearable.CircularUI.Forms">
    <ContentPage>
        <StackLayout>
            <BoxView VerticalOptions="FillAndExpand" Color="Red" />
            <Label HorizontalOptions="CenterAndExpand" Text="Red" />
        </StackLayout>
    </ContentPage>
    <ContentPage>
        <StackLayout>
            <BoxView VerticalOptions="FillAndExpand" Color="Green" />
            <Label HorizontalOptions="CenterAndExpand" Text="Green" />
        </StackLayout>
    </ContentPage>
    <ContentPage>
        <StackLayout>
            <BoxView VerticalOptions="FillAndExpand" Color="Blue" />
            <Label HorizontalOptions="CenterAndExpand" Text="Blue" />
        </StackLayout>
    </ContentPage>
</w:IndexPage>
```

**Screenshot**

![IndexPage](data/IndexPage.png)