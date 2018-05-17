---
uid: Tizen.Wearable.CircularUI.doc.Radio
summary: Radio control guide
---

# Radio
`Radio` displays 1 or more option and allows a user to select 1 of them.
`Radio` can select only 1 item among items having same `GroupName` property.

![radio](data/radio.png)

## Create Radio
`GroupName`property specifies which `Radio` controls are mutually exclusive. If a user selected one Radio control of radio control group, other items are not selected.
`IsSelected` property sets default selected value of Radio control. `Selected` event occurs when the Radio selection was changed.
`Value` property sets any value of Radio control. `Value` property is useful to distinguish which item was selected if all Radio control has the same `Selected` event handler. Please refer to below code.

For more information. Please refer to [Radio  API reference](https://samsung.github.io/Tizen.CircularUI/api/Tizen.Wearable.CircularUI.Forms.Radio.html)

_This guide's code example uses WearableUIGallery's TCRadio code at the test\WearableUIGallery\WearableUIGallery\TC\TCRadio.xaml.cs_

**XAML file**

```xml
   <w:CirclePage.Content>
        <w:CircleScrollView x:Name="myscroller" Orientation="Vertical">
            <StackLayout Padding="50,50" Orientation="Vertical">
                <Label
                    x:Name="label"
                    FontSize="Medium"
                    HorizontalOptions="CenterAndExpand"
                    Text="Selected : Sound" />
                <StackLayout Orientation="Horizontal">
                    <Label
                        HorizontalOptions="CenterAndExpand"
                        Text="Sound"
                        VerticalOptions="Center" />
                    <w:Radio
                        GroupName="SoundMode"
                        HorizontalOptions="End"
                        IsSelected="True"
                        Selected="OnSelected"
                        Value="Sound" />
                </StackLayout>

                <StackLayout Orientation="Horizontal">
                    <Label
                        HorizontalOptions="CenterAndExpand"
                        Text="Vibrate"
                        VerticalOptions="Center" />
                    <w:Radio
                        GroupName="SoundMode"
                        HorizontalOptions="End"
                        Selected="OnSelected"
                        Value="Vibrate" />
                </StackLayout>

                <StackLayout Orientation="Horizontal">
                    <Label
                        HorizontalOptions="CenterAndExpand"
                        Text="Mute"
                        VerticalOptions="Center" />
                    <w:Radio
                        GroupName="SoundMode"
                        HorizontalOptions="End"
                        Selected="OnSelected"
                        Value="Mute" />
                </StackLayout>
            </StackLayout>
        </w:CircleScrollView>
    </w:CirclePage.Content>
```

**C# file**
```cs
        public void OnSelected(object sender, SelectedEventArgs args)
        {
            Console.WriteLine($"OnSoundSelected!! value:{args.Value}");
            Radio radio = sender as Radio;
            if (radio != null)
            {
                if (args.Value) label.Text = "Selected : " + radio.Value;
            }
        }
```