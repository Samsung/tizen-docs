# Animation


You can use animation to allow your objects to move around and change their properties for a specified duration.

NUI provides a rich and easy to use animation framework which allows you to create visually rich applications. The `Animation` class can be used to animate the [animatable properties](#animatableproperties) of any number of objects, typically View objects.

NUI animations [occur in a dedicated thread](#multithreading). This allows animations to run smoothly, regardless of the time taken to process the input, events, and other factors in the application code.

The following figure shows the NUI class hierarchy. The `Animatable` class contains "property" methods such as `GetProperty()` and `IsPropertyAnimatable()`. The `Animation` class contains [animation methods](#animationclassmethods), such as `AnimateBy()` and `AnimateTo()`.

**Figure: NUI class hierarchy**

![NUI class hierarchy](media/NUI_Class_Hierarchy.png)

To implement a basic animation, create an animation object that takes place over 2 seconds:

```
_animation = new Animation( 2000 );
```

alternatively,

```
_animation = new Animation
{
    Duration = 2000;
};
```

<a name="animatableproperties"></a>
## Animatable Properties

Some View properties are "animatable", such as `Position`, `Orientation`, `Scale`, and `Color`. For "standard" controls, you can query whether a property is animatable, using `IsPropertyAnimatable()`, but cannot change the animatable state.

You can set a property to "animatable" in the derived classes of custom view controls.

For more information, see [Properties in Custom Views](creating-custom-view-controls.md#properties) and [Creating Transitions](creating-custom-view-controls.md#creatingtransitions), which describes the animatable 'Scriptable Properties'.

<a name="animatingproperties"></a>
## Animating Properties

To animate the properties within NUI, you can use 2 distinct methods:

-   `AnimateTo()`: Property animates TO the value in the given time.
-   `AnimateBy()`: Property animates BY the value in the given time (which means that it animates to a value that is the sum of the starting position and the given value).

In the following example, `view1` and `view2` are at the position 10.0f, 10.0f, 0.0f at the start of the animation.

```
// Animate the position of view1 TO 10.0f, 50.0f, 0.0f
animation.AnimateTo( view1, "Position", Vector3(10.0f, 50.0f, 0.0f) );  // End position: 10.0f, 50.0f, 0.0f

// Animate the position of view2 BY 10.0f, 50.0f, 0.0f
animation.AnimateBy( view2, "Position", Vector3(10.0f, 50.0f, 0.0f) );  // End position: 20.0f, 60.0f, 0.0f
```

Another example taken from the working example in this tutorial:

```
_animation.AnimateTo(_text, "Orientation", new Rotation(new Radian(new Degree(180.0f)), PositionAxis.X), 0, 500, new AlphaFunction(AlphaFunction.BuiltinFunctions.EaseInOutSine));
_animation.AnimateTo(_text, "Orientation", new Rotation(new Radian(new Degree(0.0f)), PositionAxis.X), 500, 1000, new AlphaFunction(AlphaFunction.BuiltinFunctions.EaseInOutSine));

_animation.AnimateBy(_text, "ScaleX", 3, 1000, 1500);
_animation.AnimateBy(_text, "ScaleY", 4.0f, 1500, 2000);
```

Properties can also be passed to an animation method through the `property` class instantiation:

```
_animation.AnimateTo(new Property(_text, View.Property.ORIENTATION), new Property.Value(new Rotation(new Radian(new Degree(180.0f)), ...
```

For a description of the parameters, see [Animation Class Methods](#animationclassmethods).

<a name="control"></a>
## Controlling Playback

After the animation is created, you can play it:

-   To play the animation:

    ```
    animation.Play();
    ```

- To pause or stop the animation:

    ```
    animation.Pause();
    animation.Stop();
    ```

- To loop the animation to play multiple times:

    ```
    animation.Looping = true;
    ```

- By default, when the animation ends, the properties that it was animating are baked (saved). To discard the property changes when the animation ends or is stopped:

    ```
    animation.EndAction = Animations.EndActions.Discard;
    ```

<a name="notifications"></a>
## Using Notifications

The application can be notified when the animation finishes:

```
_animation.Finished += AnimationFinished;
```

```
public void AnimationFinished(object sender, EventArgs e)
{
    Tizen.Log.Debug("NUI", "AnimationFinished()");
}
```

The application can be notified when the animation has reached a specific percentage progress:

```
_animation.ProgressNotification = 0.5; // Trigger the 'progress reached' event at 50% of animation time

_animation.ProgressReached += progressReached;
```

<a name="alphafunctions"></a>
## Using Alpha Functions

Alpha functions are used in animations to specify the rate of change of the animation parameter over time. This allows the animation to be, for example, accelerated, decelerated, repeated, or bounced. The built-in supported functions can be viewed in the `AlphaFunction` class.

You can specify a different alpha function for each animator in an Animation object:

```
animation.AnimateTo(view1, "Position", Vector3(10.0f, 50.0f, 0.0f), new AlphaFunction.BuiltinFunctions.Linear);
```

The `AnimateTo()` parameters are described in [Animation Class Methods](#animationclassmethods).

The built-in alpha functions are:

```
public enum BuiltinFunction
{
    Default,
    Linear,
    Reverse,
    EaseInSquare,
    EaseOutSquare,
    EaseIn,
    EaseOut,
    EaseInOut,
    EaseInSine,
    EaseOutSine,
    EaseInOutSine,
    Bounce,
    Sin,
    EaseOutBack,
    Count
}
```

The [sample animation](#sample) includes the use of a built-in alpha function.

You can also create your own alpha function in 2 ways:

-   By setting the default alpha function:

    ```
    float alphafunc(float progress)
    {
        if ( (progress > 0.2f) && (progress < 0.7f) )
        {
            return progress + 0.8f;
        }

        return progress;
    }

    AlphaFunction af(alphafunc);
    animation.SetDefaultAlphaFunction(af);
    ```

- By using delegates:

    ```
    private UserAlphaFunctionDelegate _user_alpha_func;

    // Declare user alpha function delegate
    [UnmanagedFunctionPointer(CallingConvention.StdCall)]
    delegate float UserAlphaFunctionDelegate(float progress);

    _user_alpha_func = new UserAlphaFunctionDelegate(alphafunc);

    _animation.AnimateTo(_view2, "Position", new Vector3(150.0f, 150.0f, 0.0f), 5000, 10000, new AlphaFunction(_user_alpha_func));
    ```

<a name="animationtypes"></a>
## Animation Types

NUI supports key frame and path animations.

### Key Frame Animation

NUI supports animating between several different values, or key frames. A key frame takes a progress value between 0.0f and 1.0f (0 and 100%, respectively) and portrays the value of the property when the animation has progressed that much. You can create several key frames:

```
KeyFrames keyFrames = new KeyFrames();
keyFrames.Add( 0.0f, new Vector3( 10.0f, 10.0f, 10.0f ) );
keyFrames.Add( 0.7f, new Vector3( 200.0f, 200.0f, 200.0f ) );
keyFrames.Add( 1.0f, new Vector3( 100.0f, 100.0f, 100.0f ) );
```

Next, you can add the key frames to your animation.

```
animation.AnimateBetween( view1, "Position", keyFrames );
```

When you play the animation, NUI animates the position of `view1` between the specified key frames. The `view1` animates from (10.0f, 10.0f, 10.0f) to (200.0f, 200.0f, 200.0f) for 70% of the animation time, and spends the remaining time animating back to (100.0f, 100.0f, 100.0f).

The advantage of specifying a key frame at 0% is that regardless of where the `view1` is, it starts from position (10.0f, 10.0f, 10.0f). If `AnimateTo()` is used, then the start position is the `view1`'s current position.

The following comprehensive example of key frame use is taken from `FocusEffect.cs`:

```
focusData.ImageItem.Size = new Size(100.0f, 100.0f, 0.0f);
parentItem.Add(focusData.ImageItem);

Size targetSize = focusData.TargetSize;
Size initSize = focusData.InitSize;

KeyFrames keyFrames = new KeyFrames();

keyFrames.Add(0.0f, initSize);
keyFrames.Add(focusData.KeyFrameStart, initSize);
keyFrames.Add(focusData.KeyFrameEnd, targetSize);

// For halo add an extra key frame to shrink it (in 20% of time after it has finished)
if (focusData.Name == "halo")
{
   keyFrames.Add(focusData.KeyFrameEnd + 0.2f, initSize);
}

_animation.AnimateBetween(focusData.ImageItem, "Size", keyFrames, Animation.Interpolation.Linear, new AlphaFunction(AlphaFunction.BuiltinFunctions.EaseOutSine));
```

### Path Animations

A `Path` can be used to animate the position and orientation of views.

The black points in the following figure are points where the DALi logo travels to. The red points are the control points which express the curvature of the path on the black points.

**Figure: Path animation**

![Path animation](media/animated-path.png)

The following code presents the black points:

```
Animation animation = new Animation();

Path path = new Path();
path.AddPoint( new Position( 50.0f, 10.0f, 0.0f ));
path.AddPoint( new Position( 90.0f, 50.0f, 0.0f ));
path.AddPoint( new Position( 10.0f, 90.0f, 0.0f ));
```

The control points can be added manually using `AddControlPoint()`. `Path` can also auto-generate the control points for you:

```
path.GenerateControlPoints(0.25f);
```

Here `0.25f` represents the curvature of the required path. The generated control points result in a smooth join between the splines of each segment.

To animate `view1` along this path:

```
animation.Animate( view1, path, new Position(0.0f, 0.0f, 0.0f) );
```

The third parameter is the forward vector (in a local space coordinate system) that is oriented with the path's tangent direction.

Another example:

```
// Black points
Position position0 = new Position(200.0f, 200.0f, 0.0f);
Position position1 = new Position(300.0f, 300.0f, 0.0f);
Position position2 = new Position(400.0f, 400.0f, 0.0f);

Path path = new Path();
path.AddPoint(position0);
path.AddPoint(position1);
path.AddPoint(position2);

// Control points for first segment
path.AddControlPoint(new Vector3(39.0f, 90.0f, 0.0f));
path.AddControlPoint(new Vector3(56.0f, 119.0f, 0.0f));

// Control points for second segment
path.AddControlPoint(new Vector3(78.0f, 120.0f, 0.0f));
path.AddControlPoint(new Vector3(93.0f, 104.0f, 0.0f));

Animation animation = new Animation();
animation.AnimatePath(view, path, Vector3.XAxis, 0, 5000, new AlphaFunction(AlphaFunction.BuiltinFunctions.Linear)); // X Axis
animation.Play();
```

> **Note**   
> `AnimatePath()` invokes `Animate`.

<a name="multithreading"></a>
## Animation Multithreading

NUI animations and rendering occur in a dedicated rendering thread. This allows animations to run smoothly, regardless of the time taken to process input events in the application code.

Internally, NUI contains a scene-graph, which mirrors the views hierarchy. The scene graph objects perform the actual animation and rendering, while the views provide thread-safe access.

The following figure shows a view hierarchy, in which one of the views is being animated. The green objects are created by the application code, while the blue private objects are used in the dedicated rendering thread.

**Figure: Actor hierarchy with an animation**

![Actor hierarchy with an animation](media/multi-threaded-animation.png)

### Reading an Animated Value

When a property is animatable, it can only be modified in the rendering thread. The value returned from a 'get' property is the value used when the previous frame was rendered.

For example, `pos = view.Position` returns the position at which the view was last rendered. Since setting a position with `view.Position = pos` is asynchronous, `pos = view.Position` does not immediately return the same value.

```
// While handling an event

View view = new View();
Window.Instance.Add(view); // Initial position is 0,0,0
view.Position = new Position(10, 10, 10);

Position current = view.Position;
Console.WriteLine("Current position: " + current.X + ", " + current.Y + ", " + current.Z);
Console.WriteLine("...");

// Whilst handling another event

current = view.Position;
Console.WriteLine("Current position: " + current.X + ", " + current.Y + ", " + current.Z);
```

The above code is likely to output:

```
Current position: 0, 0, 0
...
Current position: 10, 10, 10
```

### Setting a Property During an Animation

When a property is being animated, the animation overrides all values set with other methods.

**Figure: Actor hierarchy with an animated property**

![Actor hierarchy with an animated property](media/multi-threaded-animation-2.png)

The order of execution in the render thread is:

1.  Process the message and call the `SetPosition()` method.
2.  Apply the animation and call the `SetPosition()` method.
3.  Render the frame.

<a name="sample"></a>
## Sample Animation

A simple text animation example has been created to illustrate some of the principles outlined in this guide, including the use of the `AnimateBy()` and `AnimateTo()` methods, and an alphafunction.

Read the instructions in [Building the NUI Source Code](setup-ubuntu.md#buildsrc) of the Ubuntu setup guide, which includes an explanation of where to place the example files (the `nuirun` folder).

1.  Download the [Animation example source code](NUIsetup/animation-hello-world-tutorial.cs).
2. Copy this file to your `nuirun` folder (or `../nuirun/tutorials`):

    ```
    cp animation-hello-world.cs ~/DALiNUI/nuirun/tutorials
    ```

<a name="animationclassmethods"></a>
## Animation Class Methods

The `Animation` class provides various overloaded methods for property animation:

-   `AnimateBy()` animates a property value by a relative amount.

    ```
    public void AnimateBy(View target, string property, object relativeValue, AlphaFunction alphaFunction = null)

    public void AnimateBy(View target, string property, object relativeValue, int startTime, int endTime, AlphaFunction alphaFunction = null)
    ```

    The following table describes the `AnimateBy()` method parameters.

    **Table: AnimateBy() method parameters**

    | Parameter       | Description                              |
    |---------------|----------------------------------------|
    | `target`        | The target object to animate.            |
    | `property`      | The target property to animate, which can be an enumerator or string. |
    | `relativeValue` | The amount by which to change the property value. |
    | `alphaFunction` | The alpha function to apply.             |
    | `startTime`     | The animation start time.                |
    | `endTime`       | The animation end time.                  |

- `AnimateTo()` animates a property to a destination value.

    ```
    public void AnimateTo(View target, string property, object destinationValue, AlphaFunction alphaFunction = null)

    public void AnimateTo(View target, string property, object destinationValue, int startTime, int endTime, AlphaFunction alphaFunction = null)
    ```

    The following table describes the `AnimateTo()` method parameters.

    **Table: AnimateTo() method parameters**

    | Parameter          | Description            |
    |------------------|----------------------|
    | `destinationValue` | The destination value. |

- `AnimateBetween()` animates a property between [key frames](#animationtypes).

    ```
    public void AnimateBetween(View target, string property, KeyFrames keyFrames, Interpolation interpolation = Interpolation.Linear, AlphaFunction alphaFunction = null)

    public void AnimateBetween(View target, string property, KeyFrames keyFrames)
    ```

    The following table describes the `AnimateBetween()` method parameters.

    **Table: AnimateBetween() method parameters**

    | Parameter       | Description                              |
    |---------------|----------------------------------------|
    | `keyFrames`     | The set of time/value pairs between which to animate. |
    | `interpolation` | The method used to interpolate between values. |

- `AnimatePath()` animates a view's position and orientation through a predefined path.

    ```
    public void AnimatePath(View view, Path path, Vector3 forward, AlphaFunction alphaFunction = null)
    ```

    The following table describes the `AnimatePath()` method parameters.

    **Table: AnimatePath() method parameters**

    | Parameter | Description                              |
    |---------|----------------------------------------|
    | `path`    | The position and orientation.            |
    | `forward` | The vector (in local space coordinate system) oriented with the path's tangent direction. |

<a name="animationclassproperties"></a>
## Animation Class Properties

The following table lists the `Animation` class properties.

| Property               | Type              | Description                              |
|----------------------|-----------------|----------------------------------------|
| `Duration`             | `int`             | Gets/sets the animation duration in milliseconds. |
| `DefaultAlphaFunction` | `AlphaFunction`   | Gets/sets the default alpha function for the animation. |
| `State`                | `States`          | Queries the animation state (`Stopped`, `Playing`, or `Paused`). |
| `LoopCount`            | `int`             | Set: Defines the number of times to loop the animation. A value of 0 is the same as setting `Looping = true`, looping continuously.Get: Gets the loop count. |
| `Looping`              | `bool`            | Gets/sets whether the animation loops, which resets the loop count. The loop count is initially 1 for a single play. |
| `EndAction`            | `EndActions`      | Gets/sets the animation end action. The action is performed when the animation ends, or if it is stopped. |
| `CurrentLoop`          | `int`             | Gets the current loop count.             |
| `DisconnectAction`     | `EndAction`       | Gets/sets the disconnect action.         |
| `CurrentProgress`      | `float`           | Gets/sets the animation progress.        |
| `SpeedFactor`          | `float`           | Gets/sets a speed factor for the animation. |
| `PlayRange`            | `RelativeVector2` | Defines the values between which the animation plays. Both values (`range.x` and `range.y`) must be between 0 and 1. |
| `ProgressNotification` | `float`           | Gets/sets the progress notification marker that triggers the `ProgressReached` event. The value must be between 0 and 1. |
