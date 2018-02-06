# Animation Types

NUI supports key frame and path animation.

[Key Frame Animation](#1)<br>
[Path Animation](#2)<br>

<a name="1"></a>
## Key Frame Animation

NUI provides support for animating between several different values, or key frames.
A key frame takes a progress value between 0.0f and 1.0f (0 and 100% respectively) and portrays the value of the property when the animation has progressed that much.
You can create several key frames:

```
KeyFrames _keyFrames = new KeyFrames();
_keyFrames.Add(0.0f, new Size(0.0f, 0.0f, 0.0f));
_keyFrames.Add(0.3f, new Size(window.Size.Width * 0.7f, window.Size.Height * 0.7f, 0.0f));
_keyFrames.Add(1.0f, new Size(window.Size));

KeyFrames keyFrames = KeyFrames::New();
keyFrames.Add( 0.0f, Vector3( 10.0f, 10.0f, 10.0f ) );
keyFrames.Add( 0.7f, Vector3( 200.0f, 200.0f, 200.0f ) );
keyFrames.Add( 1.0f, Vector3( 100.0f, 100.0f, 100.0f ) );
```

Next, you can add the key frames to your animation.

```
_animation.AnimateBetween(_imageView, "Size", _keyFrames, 4000, 6000, Animation.Interpolation.Linear);
```


<a name="2"></a>
## Path Animation

The `Path` class can be used to animate the position and orientation of actors. (a 3D parametric curve)

The black points in the following figure are points where the 'dali' logo travels to. The red points are the control points which express the curvature of the path on the black points.

**Figure: Path animation**

![Path animation](./media/path_animation.png)

The following code presents the black points:

```
Path path = new Path();
path.AddPoint(new Vector3( 50.0f, 10.0f, 0.0f ));
path.AddPoint(new Vector3( 90.0f, 50.0f, 0.0f ));
path.AddPoint(new Vector3( 10.0f, 90.0f, 0.0f ));
```

The control points can be added manually using `AddControlPoint`. The `Path` class can also auto-generate the control points for you.

```
path.GenerateControlPoints( 0.25f );
```
Here 0.25f represents the curvature of the path you require.

To animate `view1` along this path, use the following function:

```
_animation.AnimatePath( view1, path, Vector3::ZERO );
```

The third parameter is the forward vector (in a local space coordinate system) that is oriented with the path's tangent direction.

## Related Information
* Dependencies
  -   Tizen 4.0 and Higher
