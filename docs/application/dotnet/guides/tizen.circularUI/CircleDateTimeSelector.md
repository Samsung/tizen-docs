---
uid: Tizen.Wearable.CircularUI.doc.CircleDateTimeSelector
summary: CircleDateTimeSelector control guide
---

# CircleDateTimeSelector

`CircleDateTimeSelector` is a view for Date Picker and Time Picker.
You can rotate the bezel to explore the screen using the [Bezel interaction](https://developer.tizen.org/design/wearable/interaction/bezel-interactions).
The view of this selector covers the entire screen.
To receive [Rotary event](https://developer.tizen.org/development/training/native-application/understanding-tizen-programming/event-handling#rotary), it must be registered as `RotaryFocusObject`, property of [CirclePage](xref:Tizen.Wearable.CircularUI.doc.CirclePage).

The Date display screen is a touch screen. You can set the value of the year: month: day by touch and by rotating the bezel.
The Time display screen is also a touch screen. You can set the value of the hour: minute: AM / PM by touch and by rotating the bezel.

 |![Date](data/CircleDateTimeSelector_DatePicker.png) | ![Time](data/CircleDateTimeSelector_TimePicker.png)|
 |:--------------------------------------------------:|:--------------------------------------------------:|
 |                      Date                          |                           Time                     |

**WARNING: [CircleListView](xref:Tizen.Wearable.CircularUI.doc.CircleListView), [CircleDateTimeSelector](xref:Tizen.Wearable.CircularUI.doc.CircleDateTimeSelector), [CircleScrollView](xref:Tizen.Wearable.CircularUI.doc.CircleScrollView), [CircleStepper](xref:Tizen.Wearable.CircularUI.doc.CircleStepper) must be confined in the `CirclePage` container or [Page](https://developer.xamarin.com/api/type/Xamarin.Forms.Page/) with [CircleSurfaceEffectBehavior](xref:Tizen.Wearable.CircularUI.doc.CircleSurfaceEffectBehavior). If you add these controls in any other way,  it may cause an exception or cannot display the controls.**

## Add CircleDateTimeSelector in CirclePage

You can set `CircleDateTimeSelector` in the [CirclePage.Content](xref:Tizen.Wearable.CircularUI.doc.CirclePage). For more information on how to add a [CirclePage](xref:Tizen.Wearable.CircularUI.doc.CirclePage), see [CirclePage guide](https://samsung.github.io/Tizen.CircularUI/guide/CirclePage.html#create-circlepage).
`RotaryFocusTargetName` property sets the currently focused control using the rotating interaction, and displays the focused control's circle object.
If the value is not set properly, the control will not receive the [Rotary Event](https://developer.tizen.org/development/training/native-application/understanding-tizen-programming/event-handling#rotary).

`CircleDateTimeSelector` has the following properties:

- ValueType : The value of time is changed in Time, and the value of date is changed in Date.
- DateTime : Sets or gets date/time.
- MaximumDate : Sets or gets maximum date.
- MimimumDate : Sets or gets minimum date.

The following example explains how to set a timepicker. Assign `ValueType` value for "Time" and set the current time to the `DateTime` property.
When the code is executed, the current time will be displayed on the screen. Since the focussed area on the screen shows the hour item, the hour item is changed when the bezel is turned. To change the minutes, touch the minute item and turn the bezel.

For more information, see [CircleDateTimeSelector API reference](https://samsung.github.io/Tizen.CircularUI/api/Tizen.Wearable.CircularUI.Forms.CircleDateTimeSelector.html).

_The code example of this guide uses CircleDateTime code of XUIComponent. The code is available in sample\XUIComponents\UIComponents\UIComponents\Samples\CircleDateTime/DateTimeViewModel.cs and CircleTime.xaml_

The following code shows CirclePage with CircleDateTimeSelector:

**C# file**

```cs
    public class DateTimeViewModel : INotifyPropertyChanged
    {
        static DateTime _dateTime = DateTime.Now;

        public DateTime Datetime
        {
            get => _dateTime;
            set
            {
                //Console.WriteLine($"Set Datetime value : {value.ToString()}");
                if (_dateTime == value) return;
                _dateTime = value;
                OnPropertyChanged();
            }
        }

```

**XAML file**

```xml
<w:CirclePage
    x:Class="UIComponents.Samples.CircleDateTime.CircleTime"
    xmlns="http://xamarin.com/schemas/2014/forms"
    xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
    xmlns:local="clr-namespace:UIComponents.Samples.CircleDateTime"
    xmlns:sys="clr-namespace:System;assembly=netstandard"
    xmlns:w="clr-namespace:Tizen.Wearable.CircularUI.Forms;assembly=Tizen.Wearable.CircularUI.Forms"
    RotaryFocusTargetName="timeSelector">
    <w:CirclePage.BindingContext>
        <local:DateTimeViewModel />
    </w:CirclePage.BindingContext>
    <w:CirclePage.Content>
        <StackLayout
            BackgroundColor="Black"
            HorizontalOptions="FillAndExpand"
            Orientation="Vertical"
            VerticalOptions="FillAndExpand">
            <w:CircleDateTimeSelector
                x:Name="timeSelector"
                DateTime="{Binding Datetime, Mode=TwoWay}"
                MaximumDate="1/1/2022"
                MinimumDate="1/12/2010"
                ValueType="Time" />
        </StackLayout>
    </w:CirclePage.Content>
    <w:CirclePage.ActionButton>
        <w:ActionButtonItem Command="{Binding ButtonPressedExit}" Text="OK" />
    </w:CirclePage.ActionButton>
</w:CirclePage>

```