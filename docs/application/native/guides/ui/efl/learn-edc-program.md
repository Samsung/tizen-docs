# Program Block

The `program` block defines how your interface reacts to events. Programs can change the part state or trigger other events.

The events are handled as signals, which can be emitted between the application logic (code) and UI (theme). For more information, see [Signal Handling](./learn-edc-signal-handling.md).

**Figure: Program block**

![Program block](./media/diagram_program.png)

```
program {
   /* Set the name of the program */
   name: "programname";
   /* Set the signals which trigger the program */
   signal: "signalname";
   /* Filter incoming signals depending on the sender name */
   source: "partname";
   /* Filter incoming signals depending on the part's state */
   filter: "partname" "statename";
   /* Delay the program by X seconds plus a random time between 0 and Y */
   in: 0.3 0.0;
   /* Set the action to perform */
   action: STATE_SET "statename" state_value;
   /*
      If the action is STATE_SET,
      define a transition from the current to the target state
   */
   transition: LINEAR 0.5;
   /* If the action is SIGNAL_EMIT, set the name of the part which receives the signal */
   target: "partname";
   /* Run another program after the current one is done */
   after: "programname";
   after: "anotherprogram";
}
```

- `name [program name]`

  Sets the symbolic name of the program as a unique identifier.

- `signal [signal name]`

  Sets the signals that cause the program to run. The signal received must match the specified source to run. There can be several signals, but only one signal keyword per program can be used. Also, there are some predefined signals for touch event handling. The predefined signals are:

  - `hold,on`: Holding on the mouse event matching the source that starts the program
  - `hold,off`: Holding off the mouse event matching the source that starts the program
  - `focus,part,in`: Focusing in the matching source that starts the program
  - `focus,part,out`: Focusing out of the matching source that starts the program
  - `mouse,in`: Moving the mouse into the matching source that starts the program
  - `mouse,out`: Moving the mouse out of the matching source that starts the program
  - `mouse,move`: Moving the mouse in the matching source that starts the program
  - `mouse,down,*`: Pressing the mouse button in the matching source that starts the program
  - `mouse,up,*`: Releasing the mouse button in the matching source that starts the program
  - `mouse,clicked,*`: Clicking any mouse button in the matching source that starts the program
  - `mouse,wheel,0,*`: Moving the mouse wheel in the matching source that starts the program. A positive number moves up and a negative number moves down.
  - `drag,start`: Starting a drag of the mouse in the matching source that starts the program. This signal works only in the `draggable` part.
  - `drag,stop`: Stopping a drag of the mouse in the matching source that starts the program. This signal works only in the `draggable` part.
  - `drag`: Dragging the mouse in the matching source that starts the program. This signal works only in the `draggable` part.

- `source [source name]`

  Sets the source of an accepted signal. There can be several signals, but only one source keyword per program can be used. For example, `source: button-*` means that signals from any part or program named `button-*` are accepted.

- `filter [part] [state]`

  Filters the signals to be only accepted if the part is in the `[state]` state. Only 1 filter per program can be used. If the `[state]` parameter is not given, the source of the event is used instead.

- `in [from] [range]`

  Waits `[from]` seconds before executing the program and add a random number of seconds (from 0 to `[range]`) to the total waiting time.

- `action [type] (param1) (param2) (param3) (param4)`

  Sets the action to be performed by the program. The valid actions (only 1 can be specified) are:

  - `STATE_SET`: Set the `target part` state as `target state`
  - `ACTION_STOP`: Stop the ongoing transition
  - `SIGNAL_EMIT`: Emit a signal to the application level. The application can register a callback for handling actions based on the EDC state.
  - `DRAG_VAL_SET`: Set a value for the `draggable` part (x, y values)
  - `DRAG_VAL_STEP`: Set a step for the `draggable` part (x, y values)
  - `DRAG_VAL_PAGE`: Set a page for the `draggable` part (x, y values)
  - `FOCUS_SET`: Set the focus to the target group
  - `PLAY_SAMPLE "sample name" speed (channel)`: Play a music sample clip

    `PLAY_SAMPLE`'s (optional) channel can be one of:
    - `EFFECT/FX`
    - `BACKGROUND/BG`
    - `MUSIC/MUS`
    - `FOREGROUND/FG`
    - `INTERFACE/UI`
    - `INPUT`
    - `ALERT`
  - `PLAY_TONE "tone name" duration_in_seconds (Range 0.1 to 10.0)`: Play a predefined tone of a specific duration
  - `PLAY_VIBRATION "sample name" repeat (repeat count)`

- `transition [type] [length] (interp val 1) (interp val 2) (option)`

  Determines how transitions occur using the `STATE_SET` action. The `[type]` parameter is the style of the transition and the `[length]` parameter is a double specifying the number of seconds in which to perform the transition. The valid types are:

  - `LIN` or `LINEAR`
  - `SIN` or `SINUSOIDAL`
  - `ACCEL` or `ACCELERATE`
  - `DECEL` or `DECELERATE`
  - `ACCEL_FAC` or `ACCELERATE_FACTOR`
  - `DECEL_FAC` or `DECELERATE_FACTOR`
  - `SIN_FAC` or `SINUSOIDAL_FACTOR`
  - `DIVIS` or `DIVISOR_INTERP`
  - `BOUNCE`
  - `SPRING`

  The types have the following requirements:

  - `ACCEL_FAC`, `DECEL_FAC`, and `SIN_FAC` need the extra optional `interp val 1` to determine the `factor` of curviness. 1.0 is the same as their non-factor counterparts and 0.0 is equal to linear. Numbers higher than 1.0 make the curve angles steeper with a more pronounced curve point.
  - `DIVIS`, `BOUNCE`, and `SPRING` also require `interp val 2` in addition to `interp val 1`.
  - `DIVIS` uses `[val 1]` as the initial gradient start (for example, 0.0 is horizontal, 1.0 is diagonal (linear), and 2.0 is twice the gradient of linear). `[val 2]` is interpreted as an integer factor defining how much the value swings outside the gradient before going back to the final resting spot at the end. 0.0 for `[val 2]` is equivalent to a linear interpolation. Note that `DIVIS` can exceed 1.0.
  - `BOUNCE` uses `[val 2]` as the number of bounces (so it is rounded down to the nearest integer value), with `[val 1]` determining how much the bounce decays; 0.0 gives a linear decay per bounce and higher values give much more decay.
  - `SPRING` is similar to bounce; `[val 2]` specifies the number of spring swings and `[val 1]` specifies the decay, but it can exceed 1.0 on the outer swings.
  - The valid options are:
    - `CURRENT`: Causes the object to move from its current position. Can be used as the last parameter of any transition type.

- `target [target]`

  Sets the program or part on which the specified action acts.

- `after [after]`

  Determines the program that is run after the current program completes. The source and signal parameters of a program run as an `after` are ignored. Multiple `after` statements can be specified per program.

> **Note**
>
> Except as noted, this content is licensed under [LGPLv2.1+](http://opensource.org/licenses/LGPL-2.1).

## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
