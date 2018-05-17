---
uid: Tizen.Wearable.CircularUI.doc.ConfirmPopupEffect
summary: ConfirmPopupEffect guide
---
# ConfirmPopupEffect

`ConfirmPopupEffect` is an [Effect](https://developer.xamarin.com/api/type/Xamarin.Forms.Effect/) for Xamarin.Forms that is used to make the [CirclePage](xref:Tizen.Wearable.CircularUI.doc.CirclePage) have one button or two buttons.
Accept button has one default, and "Ok" text is displayed in Accept as default.

When `ConfirmVisibility` becomes `True`, it appears on the screen,
The command given at the time of Accept or Cancel is executed and disappears automatically, and `ConfirmVisibility` becomes `False`.
Also, when you touch the outside of the popup, the popup is automatically canceled. (Cancel command is performed similarly.)
You can change the position by adjusting the X and Y value of Offset.

*If you want to display context popup separately from any control, please use [ContextPopup](xref:Tizen.Wearable.CircularUI.doc.ContextPopup) instead.*

![](data/ConfirmPopupEffect.png)

## Adding popup with ConfirmPopupEffect at CirclePage

You can set popup with `ConfirmPopupEffect` at [CirclePage.Content](xref:Tizen.Wearable.CircularUI.doc.CirclePage). If you want to know how to add [CirclePage](xref:Tizen.Wearable.CircularUI.doc.CirclePage), please refer to [CirclePage guide](https://samsung.github.io/Tizen.CircularUI/guide/CirclePage.html#create-circlepage). To create a new popup, use the following code.

`ConfirmPopupEffect` has the following properties:

- AcceptCommand : [System.Windows.Input.ICommand](https://developer.xamarin.com/api/type/System.Windows.Input.ICommand/). Command to be executed when Accept
- CancelCommand : [System.Windows.Input.ICommand](https://developer.xamarin.com/api/type/System.Windows.Input.ICommand/). Command is executed at the time of cancellation, even if the popup disappears by selecting outside the popup.
- ConfirmVisibility : Popup appears if `ConfirmVisibility` is True, and disappears when it becomes False. `CancelCommand` works even if it disappears to False.
- PositionOption : Position type of popup
  - `BottomOfView` : The popup appears at the bottom of the View using the Effect. The position is changed by Offset in the center of View.
  - `CenterOfParent` : In the center of the screen, move by the Offset in the Popup.
  - `Absolute` : The value of Offset is X, Y and popup is placed on the screen.
  - `Relative` : Set Offset.X * Window.Width, Offset.Y * Window.Height.

In the example below, a check with `ConfirmPopupEffect` in the `StackLayout` is set into the `CirclePage`. I have set the texts to be shown in `AcceptText` and `CancelText`, and defined the commands to execute when each item is selected in `AcceptCommand` and `CancelCommand`. Accept will change the background color to green and Cancel if it will be red.
I set the position by assigning `CenterOfParent` to the `PositionOption`. `ConfirmVisibility` value set to be bound to `IsToggled`.

|![BottomOfView](data/ConfirmPopupEffect_BottomOfView.png)|![CenterOfParent](data/ConfirmPopupEffect_2.png)|![3rd scene when selects 'Yes'](data/ConfirmPopupEffect_Absolute.png)|
|:----------------------------------------------------:|:--------------------------------------------------:|:-----------------------------:|
|                       BottomOfView                   |                    CenterOfParent                  |         Absolute/Relative     |

For more information. Please refer to below links

- [ConfirmPopupEffect  API reference](https://samsung.github.io/Tizen.CircularUI/api/Tizen.Wearable.CircularUI.Forms.ConfirmPopupEffect.html)
- [Xamarin.Forms.RoutingEffect  API reference](https://developer.xamarin.com/api/type/Xamarin.Forms.RoutingEffect/)
- [Xamarin.Forms.Effect Guide](https://docs.microsoft.com/en-us/xamarin/xamarin-forms/app-fundamentals/effects/)

_This guide's code example use WearableUIGallery's TCConfirm.xaml and TCConfirm.xaml.cs code at the test\WearableUIGallery\WearableUIGallery\TC\TCConfirm.xaml_

**C# file**

```cs
    [XamlCompilation(XamlCompilationOptions.Compile)
    public partial class TCConfirm : CirclePage
    {
        public TCConfirm ()
        {
            AcceptedCommand = new Command(() => BackgroundColor = Color.Green);
            CancelCommand = new Command(() => BackgroundColor = Color.Red);

            InitializeComponent ();
        }

        public ICommand AcceptedCommand { get; private set; }
        public ICommand CancelCommand { get; private set; }
    }
```

**XAML file**

```xml
<?xml version="1.0" encoding="utf-8" ?>
<w:CirclePage
    x:Class="WearableUIGallery.TC.TCConfirm"
    xmlns="http://xamarin.com/schemas/2014/forms"
    xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
    xmlns:w="clr-namespace:Tizen.Wearable.CircularUI.Forms;assembly=Tizen.Wearable.CircularUI.Forms"
    x:Name="mypage">
    <ContentPage.Content>
        <AbsoluteLayout>
            <w:Check
                x:Name="confirm3"
                w:ConfirmPopupEffect.AcceptCommand="{Binding AcceptedCommand, Source={x:Reference mypage}}"
                w:ConfirmPopupEffect.AcceptText="Yes"
                w:ConfirmPopupEffect.CancelCommand="{Binding CancelCommand, Source={x:Reference mypage}}"
                w:ConfirmPopupEffect.CancelText="No"
                w:ConfirmPopupEffect.ConfirmVisibility="{Binding IsToggled, Source={x:Reference confirm3}, Mode=TwoWay}"
                w:ConfirmPopupEffect.PositionOption="CenterOfParent"
                AbsoluteLayout.LayoutBounds="0.5, 0.2, 1, 0.25"
                AbsoluteLayout.LayoutFlags="All"
                HorizontalOptions="CenterAndExpand"
                IsToggled="False"
                VerticalOptions="CenterAndExpand">
                <w:Check.Effects>
                    <w:ConfirmPopupEffect />
                </w:Check.Effects>
            </w:Check>
        </AbsoluteLayout>
    </ContentPage.Content>
</w:CirclePage>
```

**Screenshot**

|![1st scene with Check](data/ConfirmPopupEffect_1.png)| ![2nd scene with ConfirmPopupEffect](data/ConfirmPopupEffect_2.png)|![3rd scene when selects 'Yes'](data/ConfirmPopupEffect_3.png)|
|:----------------------------------------------------:|:-------------------------------------------------------------------:|:-----------------------------------------:|
|                       1st scene with Check            |                    2nd scene with ConfirmPopupEffect                |         3rd scene when selects 'Yes' |

