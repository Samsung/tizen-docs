# RadioButton
RadioButton is a common component and describes what action will occur when you select it.  
A RadioButton can contain both, an icon and text, and can be created using styles.

![RadioButton1](./media/RadioButton1.png)

## Create RadioButton

To create a radio button, follow these steps:

1. Create RadioButton:

    ```xaml
    <comp:RadioButton x:Name="radio"/>
    ```

## Create RadioButton with style

1. Apply style to RadioButton:

    ```csharp
    ButtonStyle utilityStyle = new ButtonStyle
    {
        Icon = new ImageViewStyle
        {
            Size =  new Size(48, 48),
            ResourceUrl = new Selector<string>
            {
                Normal = "btn_radio_off.png",
                Selected = "btn_radio_on.png",
                Disabled = "btn_radio_off.png",
                DisabledSelected = "btn_radio_on.png",
            }
        }
    }
    radio.ApplyStyle(utilityStyle);
    ```

The following output is generated when a radio button is created using style:

![RadioButton2](./media/RadioButton2.png)


## Respond to clicked event
When you click a RadioButton, the radio button instance receives a clicked event.
You can declare the clicked event handler as follows:

```xaml
<comp:RadioButton x:Name="radio" Clicked="OnClicked"/>
```

```csharp
private void OnClicked(object sender, ClickedEventArgs e)
{
    // Do something in response to RadioButton click
}
```

## Respond to state changed event
RadioButton has eight different states as: `Normal`, `Focused`, `Disabled`, `Selected`, `Pressed`, `DisabledFocused`, `SelectedFocused`, and `DisabledSelected`.  
When you change the radio button state to focus or disable, the RadioButton instance receives a state changed event:

```xaml
<comp:RadioButton x:Name="radio" WidthSpecification="48" HeightSpecification="48" StateChangedEvent="OnStateChange"/>
```

```csharp
private void OnStateChange(object sender, Control.ControlStateChangedEventArgs e)
{
    // Do something in response to state change
}
```


## Related information

- Dependencies
  -   Tizen 6.5 and Higher 
