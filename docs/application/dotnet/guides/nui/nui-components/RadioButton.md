# RadioButton
RadioButton is a common component and describes what action will occur when you select it.  
A RadioButton can only contain an icon, and can be created using style.

![RadioButton1](./media/RadioButton1.png)

## Create with Style

To create a RadioButton applying style, follow these steps:

1. Create RadioButton using the default constructor:

    ```cs
    RadioButton utilityRadioButton = new RadioButton();
    ```

2. Apply style to the RadioButton:

    ```cs
    ButtonStyle utilityStyle = new ButtonStyle
    {
        Icon = new ImageViewStyle
        {
            Size =  new Size(48, 48),
            ResourceUrl = new Selector<string>
            {
                Normal = CommonResource.GetFHResourcePath() + "9. Controller/controller_btn_radio_off.png",
                Selected = CommonResource.GetFHResourcePath() + "9. Controller/controller_btn_radio_on.png",
                Disabled = CommonResource.GetFHResourcePath() + "9. Controller/controller_btn_radio_off.png",
                DisabledSelected = CommonResource.GetFHResourcePath() + "9. Controller/controller_btn_radio_on.png",
            }
        }
    }
    utilityRadioButton.ApplyStyle(utilityStyle);
    utilityRadioButton.Size = new Size(48, 48);
    root.Add(utilityRadioButton);
    ```

Following output is generated when the RadioButton applying style:

![RadioButton2](./media/RadioButton2.png)


## Responding to ClickEvent
When you click a RadioButton, the RadioButton instance receives a click event.
You can declare the click event handler as follows:

```cs
RadioButton button = new RadioButton();
button.ClickEvent += OnClick;
```

```cs
private void OnClick(object sender, Button.ClickEventArgs e)
{
    // Do something in response to RadioButton click
}
```

## Responding to StateChangedEvent
RadioButton has the following eight states `Normal`, `Focused`, `Disabled`, `Selected`, `Pressed`, `DisabledFocused`, `SelectedFocused`, and `DisabledSelected`.  
When you change the RadioButton state to focus or disable, the RadioButton instance receives a state changed event:

```cs
RadioButton button = new RadioButton();
button.StateChangedEvent += OnStateChange;
```

```cs
private void OnStateChange(object sender, Button.StateChangeEventArgs e)
{
    // Do something in response to state change
}
```

## Related Information
- Dependencies
  -   Tizen 5.5 and Higher
