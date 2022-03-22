# Picker

Picker is a class which provides a function that allows the user to select scrolling motion by expressing the specified value as a list.

![Picker](./media/Picker.png)

## Add namespace

To implement Picker, include `Tizen.NUI.Components` and namespace in your application:

```xaml
xmlns:comp="clr-namespace:Tizen.NUI.Components;assembly=Tizen.NUI.Components"
```

## Create with property

To create a Picker, follow these steps:

1. Create Picker in XAML:

    ```xaml
    <comp:Picker x:Name="picker"/>
    ```
2. Set the Picker property:

    ```xaml
    <comp:Picker x:Name="picker"
	MinValue="0"
	MaxValue="100"
	CurrentValue="10"/>
    ```
3. Define Picker element manually:

    ```xaml
    <comp:Picker x:Name="picker">
        <Picker.Items>
            <x:String>0</x:String>
            <x:String>1</x:String>
            <x:String>2</x:String>
            <x:String>3</x:String>
            <x:String>4</x:String>
        </Picker.Items>
    </Picker>
    ```

The following output is generated when the Picker is created using property:

![Slider](./media/PickerProp.png)

## Respond to value changed event

When you touch or pan a Picker, the Picker instance receives a value changed event.
You can declare the value changed event handler as follows:

```xaml
<comp:Picker x:Name="picker" ValueChanged="OnValueChanged"/>
```

```csharp
private void OnValueChanged(object sender, ValueChangedEventArgs args)
{
    // Do something in response to Picker click
}
```

## Related information

- Dependencies
  -   Tizen 6.5 and Higher 


