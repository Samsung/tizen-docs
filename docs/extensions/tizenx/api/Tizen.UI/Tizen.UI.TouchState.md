### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## TouchState Enum

The TouchState enum represents the possible states of a touch event.

```csharp
public enum TouchState
```
### Fields

<a name='Tizen.UI.TouchState.Down'></a>

`Down` 0

Screen touched.

<a name='Tizen.UI.TouchState.Finished'></a>

`Finished` 1

Touch or hover finished.

<a name='Tizen.UI.TouchState.Interrupted'></a>

`Interrupted` 5

A system event has occurred which has interrupted the touch or hover event sequence.

<a name='Tizen.UI.TouchState.Leave'></a>

`Leave` 3

Leave the boundary of an actor.

<a name='Tizen.UI.TouchState.Motion'></a>

`Motion` 2

Finger dragged or hovered.

<a name='Tizen.UI.TouchState.Started'></a>

`Started` 0

Touch or hover started.

<a name='Tizen.UI.TouchState.Stationary'></a>

`Stationary` 4

No change from last event. <br/>  
Useful when a multi-point event occurs where all points are sent, but indicates that this particular point has not changed since the last time.

<a name='Tizen.UI.TouchState.Up'></a>

`Up` 1

Touch stopped.






