# Animation

You can use animations to move objects around and change their properties over a specified duration. NUI implements an easy-to-use animation framework that allows you to create visually-rich applications. The `Tizen.NUI.Animation` class can be used to animate the [animatable properties](#animatableproperties) of any number of objects, typically view objects.

NUI animations [occur in a dedicated thread](#multithreading). This allows animations to run smoothly, regardless of the time taken to process the input, events, and other factors in the application code.

The following figure shows the NUI class hierarchy:

-   The `Tizen.NUI.Animatable` class contains methods related to animation properties, such as the `GetProperty()` and `IsPropertyAnimatable()` methods.
-   The `Tizen.NUI.Animation` class contains animation methods, such as the `AnimateBy()` and `AnimateTo()` methods.

**Figure: NUI class hierarchy**

![NUI class hierarchy](media/NUI_Class_Hierarchy.png)

To implement a basic animation object, specify the animation duration in milliseconds. You can do this in 2 ways:

```
_animation = new Animation(2000);

/// OR

_animation = new Animation
{
    Duration = 2000;
};
```

<a name="animatableproperties"></a>
## Animation Properties

Some view properties are "animatable", such as `Position`, `Orientation`, `Scale`, and `Color`.

In controls derived from the [Tizen.NUI.BaseComponents.CustomView](https://developer.tizen.org/dev-guide/csapi/api/Tizen.NUI.BaseComponents.CustomView.html) class, you can set a property to be "animatable". For standard controls, you can query whether a property is animatable (using the `IsPropertyAnimatable()` method of the [Tizen.NUI.Animatable](https://developer.tizen.org/dev-guide/csapi/api/Tizen.NUI.Animatable.html) class), but cannot change the animatable state.

To animate a property in NUI, you can use 2 distinct methods of the [Tizen.NUI.Animation](https://developer.tizen.org/dev-guide/csapi/api/Tizen.NUI.Animation.html) class:

-   `AnimateTo()` animates a property to a target value during a given time.

    ```
    /// view1 is first located in (10.0f, 10.0f, 0.0f)
    animation.AnimateTo(view1, "Position", Vector3(10.0f, 50.0f, 0.0f));
    /// view1 position changes to (10.0f, 50.0f, 0.0f)
    ```

-   `AnimateBy()` animates a property by the specified amount during a given time.

    ```
    /// view2 is first located in (10.0f, 10.0f, 0.0f)
    animation.AnimateBy(view2, "Position", Vector3(10.0f, 50.0f, 0.0f);
    /// view2 position changes by (10.0f, 50.0f, 0.0f) to (20.0f, 60.0f, 0.0f)
    ```

The following example provides a more complex animation:

```
_animation.AnimateTo(_text, "Orientation", new Rotation(new Radian(new Degree(180.0f)), PositionAxis.X), 0, 500, new AlphaFunction(AlphaFunction.BuiltinFunctions.EaseInOutSine));
_animation.AnimateTo(_text, "Orientation", new Rotation(new Radian(new Degree(0.0f)), PositionAxis.X), 500, 1000, new AlphaFunction(AlphaFunction.BuiltinFunctions.EaseInOutSine));

_animation.AnimateBy(_text, "ScaleX", 3, 1000, 1500);
_animation.AnimateBy(_text, "ScaleY", 4.0f, 1500, 2000);
```

You can also pass properties to an animation method through the `Property` class instantiation:

```
_animation.AnimateTo(new Property(_text, View.Property.ORIENTATION), new Property.Value(new Rotation(new Radian(new Degree(180.0f)), ...)));
```

For more information on properties in general and animatable "scriptable properties" in particular, see [Managing Properties](creating-custom-view-controls.md#properties) and [Creating Transitions](creating-custom-view-controls.md#creatingtransitions).

<a name="control"></a>
## Playback and Events

After the animation is created, you can control its playback:

-   To play the animation:

    ```
    animation.Play();
    ```

- To pause or stop the animation:

    ```
    animation.Pause();
    animation.Stop();
    ```

- To loop the animation:

    ```
    animation.Looping = true;
    ```

- By default, when the animation ends, the properties that it was animating are baked (saved). To discard the property changes when the animation ends or is stopped:

    ```
    animation.EndAction = Animations.EndActions.Discard;
    ```

During the playback, you can receive notifications at various stages of the animation:

-   When the animation has reached a specific percentage progress:

    ```
    /// Trigger the 'progress reached' event at 50% of animation time
    _animation.ProgressNotification = 0.5;

    _animation.ProgressReached += progressReached;
    ```

-   When the animation finishes:

    ```
    public void AnimationFinished(object sender, EventArgs e)
    {
        Tizen.Log.Debug("NUI", "AnimationFinished()");
    }

    _animation.Finished += AnimationFinished;
    ```

<a name="alphafunctions"></a>
## Alpha Functions

In animations, alpha functions are used to specify the animation parameter's rate of change over time. This allows the animation to be, for example, accelerated, decelerated, repeated, or bounced. The [Tizen.NUI.AlphaFunction.BuiltinFunctions](https://developer.tizen.org/dev-guide/csapi/api/Tizen.NUI.AlphaFunction.BuiltinFunctions.html) enumeration lists the built-in alpha functions.

You can specify a different alpha function for each animator in an animation object:

```
animation.AnimateTo(view1, "Position", Vector3(10.0f, 50.0f, 0.0f), new AlphaFunction.BuiltinFunctions.Linear);
```

You can also create your own alpha function in 2 ways:

-   By setting the default alpha function:

    ```
    float alphafunc(float progress)
    {
        if ((progress > 0.2f) && (progress < 0.7f))
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

    /// Declare the user alpha function delegate
    [UnmanagedFunctionPointer(CallingConvention.StdCall)]
    delegate float UserAlphaFunctionDelegate(float progress);

    _user_alpha_func = new UserAlphaFunctionDelegate(alphafunc);

    _animation.AnimateTo(_view2, "Position", new Vector3(150.0f, 150.0f, 0.0f), 5000, 10000, new AlphaFunction(_user_alpha_func));
    ```

<a name="keyframe"></a>
## Creating Key Frame Animations

You can animate between multiple defined values, or key frames. A key frame defines the property values at a specific animation progress value, from 0.0f (0%) to 1.0f (100%).

To create a key frame animation:
1.  Define the key frames:

    ```
    KeyFrames keyFrames = new KeyFrames();
    keyFrames.Add(0.0f, new Vector3(10.0f, 10.0f, 10.0f));
    keyFrames.Add(0.7f, new Vector3(200.0f, 200.0f, 200.0f));
    keyFrames.Add(1.0f, new Vector3(100.0f, 100.0f, 100.0f));
    ```

2.  Add the key frames to the animation:

    ```
    animation.AnimateBetween(view1, "Position", keyFrames);
    ```

    When you play the animation, NUI animates the position of `view1` between the specified key frames. In this animation, `view1` spends 70% of the animation time animating from (10.0f, 10.0f, 10.0f) to (200.0f, 200.0f, 200.0f), and the remaining time animating back to (100.0f, 100.0f, 100.0f).

    By specifying a key frame at 0%, the animation starts from position (10.0f, 10.0f, 10.0f), regardless of where `view1` was before the animation starts. If `AnimateTo()` is used instead of specifying the 0% key frame, the start position is `view1`'s current position.

The following example illustrates the key frame usage in a focus effect implementation:

```
focusData.ImageItem.Size = new Size(100.0f, 100.0f, 0.0f);
parentItem.Add(focusData.ImageItem);

Size targetSize = focusData.TargetSize;
Size initSize = focusData.InitSize;

KeyFrames keyFrames = new KeyFrames();

keyFrames.Add(0.0f, initSize);
keyFrames.Add(focusData.KeyFrameStart, initSize);
keyFrames.Add(focusData.KeyFrameEnd, targetSize);

/// For a halo effect, add an extra key frame to shrink the object for 20% of the animation time
if (focusData.Name == "halo")
{
    keyFrames.Add(focusData.KeyFrameEnd + 0.2f, initSize);
}

_animation.AnimateBetween(focusData.ImageItem, "Size", keyFrames, Animation.Interpolation.Linear, new AlphaFunction(AlphaFunction.BuiltinFunctions.EaseOutSine));
```

<a name="path"></a>
## Creating Path Animations

You can animate a view's position and orientation along a parametric curve, using the [Tizen.NUI.Path](https://developer.tizen.org/dev-guide/csapi/api/Tizen.NUI.Path.html) class. For example, in the following figure, the DALi logo travels along the path between the black points. The red points are control points expressing the curvature of the path.

**Figure: Path animation**

![Path animation](media/animated-path.png)

To create a path animation:

1.  Define the black points on the curve:

    ```
    Animation animation = new Animation();

    Path path = new Path();
    path.AddPoint(new Position(50.0f, 10.0f, 0.0f));
    path.AddPoint(new Position(90.0f, 50.0f, 0.0f));
    path.AddPoint(new Position(10.0f, 90.0f, 0.0f));
    ```

2.  Define the control points.

    The `GenerateControlPoints()` method of the `Tizen.NUI.Path` class generates control points based on the specified curvature, resulting in a smooth join between the splines of each segment:

    ```
    path.GenerateControlPoints(0.25f);
    ```

    Alternatively, you can add control points manually using the `AddControlPoint()` method.

3.  Animate `view1` along the defined path:

    ```
    animation.AnimatePath(view1, path, new Position(0.0f, 0.0f, 0.0f));
    ```

    The third parameter is the forward vector, using a local space coordinate system, oriented to the path's tangent direction.

The following example illustrates a path animation with manually-added control points:

```
/// Black points
Position position0 = new Position(200.0f, 200.0f, 0.0f);
Position position1 = new Position(300.0f, 300.0f, 0.0f);
Position position2 = new Position(400.0f, 400.0f, 0.0f);

Path path = new Path();
path.AddPoint(position0);
path.AddPoint(position1);
path.AddPoint(position2);

/// Control points for first segment
path.AddControlPoint(new Vector3(39.0f, 90.0f, 0.0f));
path.AddControlPoint(new Vector3(56.0f, 119.0f, 0.0f));

/// Control points for second segment
path.AddControlPoint(new Vector3(78.0f, 120.0f, 0.0f));
path.AddControlPoint(new Vector3(93.0f, 104.0f, 0.0f));

Animation animation = new Animation();
animation.AnimatePath(view, path, Vector3.XAxis, 0, 5000, new AlphaFunction(AlphaFunction.BuiltinFunctions.Linear)); /// X axis
animation.Play();
```

<a name="multithreading"></a>
## Animation Multithreading

NUI animations and rendering occur in a dedicated rendering thread, which allows the animations to run smoothly, regardless of the time taken to process input events in the application code. Internally, NUI contains a scene-graph that mirrors the view hierarchy. The scene graph objects perform the actual animation and rendering, while the views provide thread-safe access.

The following figure shows a view hierarchy in which one of the views is being animated. The green objects are created by the application code, while the blue private objects are used in the dedicated rendering thread.

**Figure: Animation view hierarchy**

![Animation view hierarchy](media/multi-threaded-animation.png)

<a name="readvalue"></a>
### Reading Animated Values

When a property is animatable, it can only be modified in the rendering thread. The value returned from a 'get' property is the value used to render the previous frame.

For example, `view.Position` has the position value at which the view was last rendered. Since defining a new position for `view.Position` is asynchronous, it does not immediately return the new value.

```
View view = new View();
Window.Instance.Add(view); /// Initial position is 0,0,0
view.Position = new Position(10, 10, 10);

Position current = view.Position;
Console.WriteLine("Current position: " + current.X + ", " + current.Y + ", " + current.Z);
Console.WriteLine("...");

/// Handle another event

current = view.Position;
Console.WriteLine("Current position: " + current.X + ", " + current.Y + ", " + current.Z);
```

The above example code is likely to output:

```
Current position: 0, 0, 0
...
Current position: 10, 10, 10
```

<a name="propsetting"></a>
### Setting Properties During Animations

When a property is being animated, the animation overrides all values set using other methods.

The order of execution in the render thread is:

1.  Process the message and call the `SetPosition()` method.
2.  Apply the animation and call the `SetPosition()` method.
3.  Render the frame.

<a name="sample"></a>
## Sample Animation

You can use an `animation-hello-world.cs` sample to see in practice how the `AnimateBy()` and `AnimateTo()` methods, and alpha functions work.

After setting up your NUI development environment and building the NUI source code, download the [sample file](nui-example-code/animation-hello-world-tutorial.cs), copy it to your `nuirun` or `nuirun/tutorials` folder, and run the sample application.
