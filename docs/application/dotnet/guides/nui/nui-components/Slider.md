# Slider
A slider enables you to select a value from a continuous or discrete range of values by moving the slider thumb.

Sliders are classified into a horizontal type and a vertical type, depending on their orientation, and the number of sliders that are adjusted simultaneously.

Using a slider you can adjust the steps or strength of settings, such as brightness and contrast.

![Slider](./media/slider.png) ![Slider](./media/slider2.png)

## Create with Property

To create a slider using property, follow these steps:

1. Create slider using the default constructor:

    ```cs
    utilityBasicSlider = new Slider();
    ```

2. Set the slider property:

    ```cs
    utilityBasicSlider.TrackThickness = 4;
    utilityBasicSlider.BgTrackColor = new Color(0, 0, 0, 0.1f);
    utilityBasicSlider.SlidedTrackColor = new Color(0.05f, 0.63f, 0.9f, 1);
    utilityBasicSlider.ThumbImageURLSelector = new StringSelector
    {
        Normal = "controller_btn_slide_handler_normal.png",
        Pressed = "controller_btn_slide_handler_press.png",
    };
    utilityBasicSlider.ThumbSize = new Size(60, 60);
    utilityBasicSlider.Direction = Slider.DirectionType.Horizontal;
    utilityBasicSlider.MinValue = 0;
    utilityBasicSlider.MaxValue = 100;
    utilityBasicSlider.CurrentValue = 10;
    root.Add(utilityBasicSlider);
    ```

Following output is generated when the slider is created using property:

![Slider](./media/slider.gif)

## Responding to ValueChangedEvent
When you touch or pan a slider, the slider instance receives a value changed event.
You can declare the value changed event handler as follows:

```cs
Slider slider = new Slider();
slider.ValueChangedEvent += OnValueChanged;
```

```cs
private void OnValueChanged(object sender, Slider.ValueChangedArgs args)
{
    // Do something in response to slider click
}
```

## Responding to StateChangedEvent
Slider has the following eight states: `Normal`, `Focused`, `Disabled`, `Selected`, `Pressed`, `DisabledFocused`, `SelectedFocused`, and `DisabledSelected`.  
When you change the slider state as change focus or disable a slider, the slider instance receives a state changed event. You can declare the state changed event handler as follows:

```cs
Slider slider = new Slider();
slider.StateChangedEvent += OnStateChanged;
```

```cs
private void OnStateChanged(object sender, Slider.StateChangedArgs args)
{
    // Do something in response to state change
}
```

## Responding to SlidingFinishedEvent
As you finish a touch or a pan operate on a slider, the slider instance receives a slide finished event. You can declare the slide finished event handler as follows:

```cs
Slider slider = new Slider();
slider.SlidingFinishedEvent += OnSlidingFinished;
```

```cs
private void OnSlidingFinished(object sender, Slider.SlidingFinishedArgs args)
{
    // Do something in response to slide finished
}
```

## Related Information
- Dependencies
  -   Tizen 5.5 and Higher