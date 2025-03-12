# DatePicker

DatePicker is a class which provides a function that allows the user to select a date through a scrolling motion by expressing the specified value as a list. DatePicker expresses the current date using the locale information of the system. Year range is 1970~2038 (glibc time_t struct min, max value)

![DatePicker](./media/DatePicker.png)

## Add namespace

To implement DatePicker, include `Tizen.NUI.Components` and namespace in your application:

```xaml
xmlns:comp="clr-namespace:Tizen.NUI.Components;assembly=Tizen.NUI.Components"
```

## Create with property

To create a DatePicker, follow these steps:

1. Create DatePicker in XAML:

    ```xaml
    <comp:DatePicker WidthSpecification="-1" HeightSpecification="-1"/>
    ```

2. Set the DatePicker format property:

    ```xaml
    <comp:DatePicker x:Name="picker" Format="yyyy/MM/dd"/>
    ```

The following output is generated when the DatePicker is created using property:

![DatePicker](./media/DatePicker.png)

## Respond to value changed event

When you touch or pan a DatePicker, the DatePicker instance receives a value changed event.
You can declare the value changed event handler as follows:

```xaml
<comp:DatePicker x:Name="picker" ValueChanged="OnValueChanged"/>
```

```csharp
private void OnValueChanged(object sender, ValueChangedEventArgs args)
{
    // Do something in response to DatePicker click
}
```

## Respond to date changed event

When you change date in DatePicker, the DatePicker instance receives a date changed event.
You can declare the date changed event handler as follows:

```xaml
<comp:DatePicker x:Name="picker" DateChanged="OnDateChanged"/>
```

```csharp
private void OnDateChanged(object sender, DateChangedEventArgs args)
{
    // Do something in response to DatePicker click
}
```

## Related information

- Dependencies
  - Tizen 6.5 and Higher 

- API References
  - [DatePicker API](/application/dotnet/api/TizenFX/latest/api/Tizen.NUI.Components.DatePicker.html)

