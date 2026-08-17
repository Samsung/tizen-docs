
# Touch & Gesture

## Overview

`NUI` and `Tizen.UI` have different touch system by default. The table below summarizes the key distinguishing features.

Feature           | NUI | OneUI
--                | --  | --   
<b>Touch Event Propagation</b><br/>How touch event being propagated when hit object does not consume. | <b>Relation based</b><br/>Propagate `child` to `parent` | <b>Geometry based</b><br/>Propagate to `below` object.
<b>Gesture Relation</b><br/>The relation of Touch & Gesture | <b>Independent</b><br/>Touch and gesture events are invoked independently. Which means even if a view consumed a touch event the below view can get a gesture detected event. | <b>Dependent</b><br/>Gestures are being controlled by Touch events. If a view consumed a touch event, the below view can not get gesture detected event.

## Gesture detection

In new touch system, the gesture should be handled by touch event.

### Basic usage

```C#
TapGestureDetector tapDetector = new ();

tapDetector.Detected += (s, e)
{
    // Tab gesture detected!
};

view.TouchEvent += (s, e) =>
{
    tapDetector.HandleEvent(view, e.Touch); // Feed touch data to gesture detector
    return true;
};
```

### Support legacy API : `Attach`

To support legacy way that uses `Attach` method of gesture detector, OneUI also provide this way.

```C#
TapGestureDetector tapDetector = new ();

tapDetector.Detected += (s, e)
{
    // Tab gesture detected!
};

tapDetector.Attach(view);
view.TouchEvent += (_, _) => true;
```

Note that, gesture can be detected when the target view is consuming touch event.
