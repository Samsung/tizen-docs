# Slider
A slider lets users select a value from a continuous or discrete range of values by moving the slider thumb.

![Slider](./media/slider.png) ![Slider](./media/slider2.png)

## Overview
Slider is a kind of common component and lets users select a value from a continuous or discrete range of values by moving the slider thumb.

- Use a slider to adjust the steps or strength of settings, such as the brightness and contrast.
- Sliders are classified into a horizontal type, vertical type depending on their orientation and the number of sliders that are adjusted simultaneously.

## Create with property
1. Create Slider by default constructor

~~~{.cs}
utilityBasicSlider = new Slider();
~~~

2. Set slider property

~~~{.cs}
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
root.Add(utilityBasicSlider);
utilityBasicSlider.MinValue = 0;
utilityBasicSlider.MaxValue = 100;
utilityBasicSlider.CurrentValue = 10;
~~~

Slider created by property:

![Slider](./media/slider.gif)

## Responding to ValueChangedEvent
When user touch or pan a slider, the Slider instance receives a value changed event.
You can declare the value changed event handler as following:

~~~{.cs}
Slider slider = new Slider();
slider.ValueChangedEvent += OnValueChanged;
private void OnValueChanged(object sender, Slider.ValueChangedArgs args)
{
    // Do something in response to slider click
}
~~~

## Responding to StateChangedEvent
Slider has 8 states including Normal, Focused, Disabled, Selected, Pressed, DisabledFocused, SelectedFocused and DisabledSelected.
When the user change slider state ( change focus or disable a slider), the Slider instance receives an state changed event. You can declare the state changed event handler as following:

~~~{.cs}
Slider slider = new Slider();
slider.StateChangedEvent += OnStateChanged;
private void OnStateChanged(object sender, Slider.StateChangedArgs args)
{
    // Do something in response to state change
}
~~~

## Responding to SlidingFinishedEvent
When user finish a touch or pan operate on a slider, the Slider instance receives a slide finished event. You can declare the slide finished event handler as following:

~~~{.cs}
Slider slider = new Slider();
slider.SlidingFinishedEvent += OnSlidingFinished;
private void OnSlidingFinished(object sender, Slider.SlidingFinishedArgs args)
{
    // Do something in response to slide finished
}
~~~

## Related Information
- Dependencies
  -   Tizen 5.5 and Higher