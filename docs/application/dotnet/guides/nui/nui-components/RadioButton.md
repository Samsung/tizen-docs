# RadioButton
RadioButton is a common component and describes what action will occur when you select it.  
A RadioButton can only contain an icon, and can be created using style.

![RadioButton1](./media/RadioButton1.png)

## Create with Style

To create a radio button using style, follow these steps:

1. Create RadioButton using the default constructor:

    ```cs
    RadioButton utilityRadioButton = new RadioButton();
    ```

2. Apply style to RadioButton:

    ```cs
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
    utilityRadioButton.ApplyStyle(utilityStyle);
    utilityRadioButton.Size = new Size(48, 48);
    root.Add(utilityRadioButton);
    ```

Following output is generated when a radio button is created using style:

![RadioButton2](./media/RadioButton2.png)


## Responding to Clicked
When you click a radio button, the radio button instance receives a clicked event.
You can declare the clicked event handler as follows:

```cs
RadioButton button = new RadioButton();
button.Clicked += OnClicked;
```

```cs
private void OnClicked(object sender, ClickedEventArgs e)
{
    // Do something in response to RadioButton click
}
```

## Responding to StateChangedEvent
RadioButton has the following eight states `Normal`, `Focused`, `Disabled`, `Selected`, `Pressed`, `DisabledFocused`, `SelectedFocused`, and `DisabledSelected`.  
When you change the radio button state to focus or disable, the radio button instance receives a state changed event:

```cs
RadioButton button = new RadioButton();
button.ControlStateChangedEvent += OnStateChange;
```

```cs
private void OnStateChange(object sender, Control.ControlStateChangedEventArgs e)
{
    // Do something in response to state change
}
```

## Related Information
- Dependencies
  -   Tizen 6.0 and Higher
