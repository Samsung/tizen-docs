---
uid: Tizen.Wearable.CircularUI.doc.PopupEntry
summary:  PopupEntry control guide
---

# Popup Entry

[PopupEntry](xref:Tizen.Wearable.CircularUI.Forms.PopupEntry) is a [Entry](https://developer.xamarin.com/api/type/Xamarin.Forms.Entry/) that allows you to enter text with the IME when you click the entry.

# Overview

This control has exactly the same usage as the `Entry`.
However, in the case of a regular `Entry` in a circular screen, the input text may not be displayed correctly due to the IME at the time of input.
Therefore, the `PopupEntry` allows to input on a pop-up which the written text is completely visible.

Below image is a screen that has the normal `Entry` and a screen with IME after click the `Entry`.

![Normal Entry](data/entry.png)
![Normal Entry with IME](data/entry_with_IME.png)

The `Entry` is not visible because it is masked by the IME.

![Popup Entry](data/PopupEntry.png)
![Popup entry with IME](data/PopupEntry_with_IME.png)

The above image is the same as using `PopupEntry`, It can type text while watching it properly.

The `BackgroundColor` of the input pop-up is the same as the `BackgroundColor` of the `PopupEntry`
and `TextColor` inside the input pop-up is also the same as the `TextColor` of the `PopupEntry` also [IsPassword](https://developer.xamarin.com/api/property/Xamarin.Forms.Entry.IsPassword/) property is kept the same.

# How to use

This is exactly the same as the `Entry`.

```xml
<?xml version="1.0" encoding="utf-8" ?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:w="clr-namespace:Tizen.Wearable.CircularUI.Forms;assembly=Tizen.Wearable.CircularUI.Forms"
             x:Class="WearableUIGallery.TC.TCPopupEntry">
    <ContentPage.Content>
        <w:CircleStackLayout>
            <w:PopupEntry BackgroundColor="Gray" TextColor="Blue" VerticalOptions="CenterAndExpand" HorizontalOptions="CenterAndExpand" />
            <w:PopupEntry Placeholder="Foobar" VerticalOptions="CenterAndExpand" HorizontalOptions="CenterAndExpand" />
            <w:PopupEntry IsPassword="True" VerticalOptions="CenterAndExpand" HorizontalOptions="CenterAndExpand" />
        </w:CircleStackLayout>
    </ContentPage.Content>
</ContentPage>
```