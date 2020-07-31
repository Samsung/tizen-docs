# CheckBox
CheckBox is a common component and describes what action will occur when you select it.  
A CheckBox can only contain an icon, and can be created using style.

![CheckBox1](./media/CheckBox1.png)

## Create with Style

To create a CheckBox applying style, follow these steps:

1. Create CheckBox using the default constructor:

    ```cs
    CheckBox utilityCheckBox = new CheckBox();
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
                Normal = "btn_check_off.png",
                Selected = "btn_check_on_24c447.png",
                Disabled = "btn_check_off.png",
                DisabledSelected = "btn_check_on_24c447.png",
            }
        }
    }
    utilityCheckBox.ApplyStyle(utilityStyle);
    utilityCheckBox.Size = new Size(48, 48);
    root.Add(utilityCheckBox);
    ```

Following output is generated when the CheckBox applying style:

![CheckBox2](./media/CheckBox2.png)


## Responding to ClickEvent
When you click a CheckBox, the CheckBox instance receives a click event.
You can declare the click event handler as follows:

```cs
CheckBox ck = new CheckBox();
ck.ClickEvent += OnClick;
```

```cs
private void OnClick(object sender, Button.ClickEventArgs e)
{
    // Do something in response to CheckBox click
}
```

## Responding to StateChangedEvent
CheckBox has the following eight states `Normal`, `Focused`, `Disabled`, `Selected`, `Pressed`, `DisabledFocused`, `SelectedFocused`, and `DisabledSelected`.  
When you change the CheckBox state to focus or disable, the CheckBox instance receives a state changed event:

```cs
CheckBox ck = new CheckBox();
ck.StateChangedEvent += OnStateChange;
```

```cs
private void OnStateChange(object sender, Button.StateChangeEventArgs e)
{
    // Do something in response to state change
}
```

## Related Information
- Dependencies
  -   Tizen 6.0 and Higher
