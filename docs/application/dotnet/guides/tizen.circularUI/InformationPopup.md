---
uid: Tizen.Wearable.CircularUI.doc.InformationPopup
summary: InformationPopup control guide
---

# InformationPopup
`InformationPopup` can represent 3 types of Tizen Wearable EFL popup style. InformationPopup is useful to show any information or warning.

*`InformationPopup` is displayed separately from any control. So you can't set this in XAML file.*


| ![information_popup1](data/information_popup1.png)| ![information_popup2](data/information_popup2.png) | ![information_popup3](data/information_popup3.png) |
|:---------:|:-----------:|:------:|
|Single text|Bottom button|Progress|

## Create single text InformationPopup
Single text `InformationPopup` is used for displaying text. It is similar to `Toast` popup. But this popup doesn't disappear automatically.

 `Text` property can be set with text. `BackButtonPressed` event occurs when user press back button of the device. If you want to dismiss popup when this event occurred, you should add `Dismiss()` in `BackButtonPressed` event handle code.

_This guide's code example uses WearableUIGallery's TCInformationPopup code at the test\WearableUIGallery\WearableUIGallery\TC\TCInformationPopup.xaml.cs_

For more information. Please refer to [InformationPopup  API reference](https://samsung.github.io/Tizen.CircularUI/api/Tizen.Wearable.CircularUI.Forms.InformationPopup.html)

**C# file**
```cs
            _textPopUp = new InformationPopup();
            _textPopUp.Text = "This is text popup test";

            _textPopUp.BackButtonPressed += (s, e) =>
            {
                _textPopUp.Dismiss();
                label1.Text = "text popup is dismissed";
            };
```

## Create bottom button InformationPopup
You can set `BottomButton` property with `MenuItem`. The bottom button is used for confirmation of user.
InformationPopup has `Title` property for displaying title.
`BottomButton.Clicked` event occurs when user press bottom button.

**C# file**
```cs
            var bottomButton = new MenuItem()
            {
                Text = "OK",
                Command = new Command(() =>
                {
                     /* must insert code when user press left button */
                })
            };

            _textButtonPopUp = new InformationPopup();
            _textButtonPopUp.Title = "Popup title";
            _textButtonPopUp.Text = "This is text and button popup test";
            _textButtonPopUp.BottomButton = bottomButton;

            _textButtonPopUp.BottomButton.Clicked += (s, e) =>
            {
                _textButtonPopUp.Dismiss();
                label1.Text = "text&button is dismissed";
            };
```

## Create progress InformationPopup
`InformationPopup`  has `IsProgressRunning` property. If this property sets `true`, small circle progress bar is displayed center of the screen.

**C# file**
```cs
            _progressPopUp = new InformationPopup();
            _progressPopUp.Title = "Popup title";
            _progressPopUp.Text = "This is progress test";
            _progressPopUp.IsProgressRunning = true;
```
