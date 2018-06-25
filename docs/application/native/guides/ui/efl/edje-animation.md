# Edje Animations

One of the greatest strengths of EFL and Edje is the ability to create animations. You can [use predefined animations](elementary-animation.md) through `Elm_Transit`, or create your own animations with the Edje library.

The Edje animations are based on a simple principle of moving from one state to another. To animate something with Edje:

1. Define 2 states for a part with description blocks.
2. Define a program block with both an action that sets a new state and the details of the state transition.
3. Manage the signal that starts the program (and consequently the animation).

## Starting an Animation

To start an animation, a program must receive a signal from a source. Edje handles many kinds of signals, including mouse events.

> **Note**
>
> To show the signals used in a specific EDJ file, use the `edje_player -p <filename>.edj` command.

<a name="create_animation"></a>
For example, to start an animation to change the color and position of a rectangle when the rectangle is clicked, the program must receive a `mouse,clicked,1` signal. To create this animation:

1. Define a new state that changes the color and position of the rectangle:

   ```
   /* Within the rectangle part */
   description {
      state: "color" 0.0;
      rel1 {relative: 0.3 0.3;}
      rel2 {relative: 0.7 0.4;}
      color: 255 0 0 255;
   }
   ```

2. Create a program to start when the rectangle is clicked.

   The program changes the state of the rectangle part to `"color"`, and performs the change using a 2-second sinusoidal transition. For more information on transitions, see [Using Program Transitions](#using-program-transitions).

   ```
   program {
      name: "animation,color";
      source: "rectangle";
      signal: "mouse,clicked,1";
      action: STATE_SET "color" 0.0;
      target: "rectangle";
      transition: SIN 2;
   }
   ```

To use signals to start animations, you need to both send a signal from your application and create a program that waits for that signal. For example:

- Create a program that changes the state of the `menu/side` target to `"default" 1.0`. The program waits for the `hide,sidemenu` signal emitted by a `MenuButton` source.

  ```
  program {
     name: "animation,menu_side,hide";
     source: "MenuButton";
     signal: "hide,sidemenu";
     action: STATE_SET "default" 1.0;
     target: "menu/side";
     transition: LINEAR 0.2;
  }
  ```

- Send the signal from the application using the `edje_object_signal_emit()` function, which emits a signal to an `Evas_Object` part of the application. The following code sends a `hide,sidemenu` signal with a `MenuButton` source to the layout object:

  ```
  edje_object_signal_emit(layout, "hide,sidemenu", "MenuButton");
  ```

  If you use the Elementary library in the application, you can use the `elm_object_signal_emit()` function. It works the same way as the `edje_object_signal_emit()` function with the same parameters.

## Using Program Actions

The Edje programs are not designed only for state change animations. You can use the programs to perform other actions as well, such as stopping a program or emitting a signal:

- The `STATE_SET` action (the usual animation action) changes the state of the part specified by the `target` property.

  In the following example, the state of the `"image"` part changes to `"default" 0.0`:

  ```
  program {
     name: "animate";
     signal: "animate";
     action: STATE_SET "default" 0.0;
     transition: LINEAR 3.0;
     target: "image";
  }
  ```

- The `ACTION_STOP` action stops the program specified by the `target` property.

  The following example stops the `animate_loop` program, and runs when receiving the `animate_stop` signal:

  ```
  program {
     name: "animate_stop";
     signal: "animate_stop";
     action: ACTION_STOP;
     target: "animate_loop";
  }
  ```

- The `SIGNAL_EMIT` action emits a signal that is used to communicate with the application directly from the theme.

  The following example emits a `"frame_move" "start"` signal when it receives the `mouse,down,*` signal from the `video_mover` part. In other words, it sends the `"frame_move" "start"` signal when the user presses the mouse in the `video_mover` part.

  ```
  program {
     name: "video_move_start";
     signal: "mouse,down,*";
     source: "video_mover";
     action: SIGNAL_EMIT "frame_move" "start";
  }
  ```

## Using Program Transitions

The following types of transitions can be added to the programs to create effects for the state changes:

- `LIN` or `LINEAR`: Makes a linear transition and takes the duration in seconds as a parameter
- `SIN` or `SINUSOIDAL`: Makes a sinusoidal transition and takes the duration in seconds as a parameter
- `ACCEL` or `ACCELERATE`: Makes an accelerated transition and takes the duration in seconds as a parameter
- `DECEL` or `DECELERATE`: Makes a decelerated transition and takes the duration in seconds as a parameter
- `ACCEL_FAC` or `ACCELERATE_FACTOR`: Makes an accelerated transition and takes the duration and the factor as a parameters
- `DECEL_FAC` or `DECELERATE_FACTOR`: Makes a decelerated transition and takes the duration and the factor as a parameters
- `SIN_FAC` or `SINUSOIDAL_FACTOR`: Makes a sinusoidal transition and takes the duration and the factor as a parameters
- `DIVIS` or `DIVISOR_INTERP`: Makes an interpolated transition and takes 3 parameters:
  - Duration
  - Initial gradient start (for example, 0.0 is horizontal, 1.0 is diagonal (linear), and 2.0 is twice the gradient of linear)
  - Integer factor that defines how much the value swings outside the gradient to come back to the final resting spot at the end. 0.0 is equivalent to linear interpolation. Note that DIVIS can exceed 1.0.
- `BOUNCE`: Makes a bounce transition and takes 3 parameters:
  - Duration
  - Bounce decay, with 0.0 giving a linear decay per bounce, and higher values giving more decay
  - Number of bounces (rounded down to the nearest integer value)
- `SPRING`: Makes a spring transition and takes 3 parameters:
  - Duration
  - Decay, with the level exceeding 1.0 on the outer swings
  - Number of spring swings

For graphical representations of these effects, see the [position mappings in Ecore animations](ecore-animation.md#table_position_mappings).

## Chaining Multiple Programs Together

To perform multiple animations in a sequence, chain Edje programs together so that they are executed one after another.

The following example uses the [same rectangle as before](#create_animation). The original program changed to the rectangle state to `"color" 0.0`. This example adds a new program that returns the state to `"default" 0.0` and chains the 2 programs together.

To chain programs:

1. Define the first program block, and use the `after` property to define the name of the program that must be run when the first program is finished:

   ```
   program {
      name: "animation,color";
      source: "rectangle";
      signal: "mouse,clicked,1";
      action: STATE_SET "color" 0.0;
      target: "rectangle";
      transition: SIN 2;
      after: "animation,state0";
   }
   ```

2. Define the second program block that returns the rectangle to its original position and color using a bounce transition with a decay factor of 1.8 and 6 bounces. Since this program is only used in a chain at the end of the first program, it has no `signal` or `source` property.

   ```
   program {
      name: "animation,state0";
      source: "";
      signal: "";
      action: STATE_SET "default" 0.0;
      target: "rectangle";
      transition: BOUNCE 5 1.8 6;
   }
   ```

> **Note**
>
> Except as noted, this content is licensed under [LGPLv2.1+](http://opensource.org/licenses/LGPL-2.1).

## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
