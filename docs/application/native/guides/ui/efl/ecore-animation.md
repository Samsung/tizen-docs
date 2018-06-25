# Ecore Animations

Ecore provides an `Ecore_Animator` facility for animations. Ecore animators use the Ecore main loop for creating animations, running a specific action on each tick of a timer in the main loop. To create an Ecore animation, you have to determine the duration of the animation and define a callback function that performs the animation with that duration.

To use Ecore animators, include the `<Ecore.h>` header file in the application. This file is included by default if you are already using the `<Elementary.h>` header file in the application.

The following example illustrates a basic Ecore animation:

- You can declare an `Ecore_Animator` variable to allow you to control the running of the animation with the `ecore_animator_freeze()`, `ecore_animator_thaw()`, and `ecore_animator_del()` functions.
- You need a callback, which performs the actual animation. In this case, the `_do_animation()` callback moves the `my_evas_object` object linearly from position (0,0) to position (100,100).
- You create the animator in the main loop, defining the animation duration as 2 seconds.
- If the callback returns with the `ECORE_CALLBACK_RENEW` value, the animation is not automatically deleted. To delete it when no longer needed, use the `ecore_animator_del()` function with the `Ecore_Animator` variable.

```
static Ecore_Animator *anim;

static Eina_Bool
_do_animation(void *data, double pos)
{
    evas_object_move(data, 100 * pos, 100 * pos);
    /* Do some more animating */

    return ECORE_CALLBACK_RENEW;
}
anim = ecore_animator_timeline_add(2, _do_animation, my_evas_object);

ecore_animator_del(anim);
```

## Starting a Finite Animation

The `ecore_animator_timeline_add()` function allows you to define an animator that is automatically deleted after the animation is finished:

- The first parameter is the duration of the animation in seconds. The duration is not affected by the frame rate.

- The second parameter is the callback function that performs the actual animation.

- The third parameter is the data passed to the callback function. This is usually the Evas object to animate.

> **Note**
>
> The function returns a pointer to an `Ecore_Animator` object, which you can use to control the animation execution.

The following example performs a linear horizontal move of 500 pixels (from 0 to 500 on the X axis) in 8 seconds, while keeping the Y axis position unchanged:

```
static Eina_Bool
_my_animation(void *data, double pos)
{
    Evas_Object *obj = data; /* Get the target object */
    /* Target object geometry */
    int x;
    int y;
    int w;
    int h;
    evas_object_geometry_get(obj, &x, &y, &w, &h); /* Get the current position and size */
    evas_object_move(obj, 500 * pos, y); /* Linear move of the Evas object */
}
/* Run the animation in 8 seconds */
ecore_animator_timeline_add(8, _my_animation, my_evas_object);
```

> **Note**
>
> The callback function can return `ECORE_CALLBACK_RENEW` to keep the animator running, or `ECORE_CALLBACK_CANCEL` to stop the animator and delete it automatically at any time. If the callback returns `ECORE_CALLBACK_CANCEL` (or `0`), the animator is automatically deleted from the list of pointers to free up the allocated memory.
>
> The callback function receives a timeline position (second parameter) with a value between 0.0 (start) to 1.0 (end) to indicate where along the timeline the animator is running.

## Starting an Infinite Animation

To create an animation that runs for an unspecified amount of time, use the `ecore_animator_add()` function:

- The first parameter is the callback function that performs the actual animation.
- The second parameter is the data passed to the callback function. This is usually the Evas object to animate.

This function works the same way as the `ecore_animation_timeline_add()` function, except that its interval is based on the frame rate. Using the frame rate as a basis benefits performance, especially in the case of multiple animations, since it enables you to use a different timer for each callback function.

> **Note**
>
> The function returns a pointer to an Ecore_Animator object, which you can use to control the animation execution.

The following example creates a rectangle sliding from left to right and back again. When the rectangle hits the edge of the screen, it changes direction.

```
static Eina_Bool
_slide_back_and_forth(void *data)
{
    typedef enum {LEFT, RIGHT} direction_t; /* Direction datatype */
    static int x = 0; /* Initial position */
    static direction_t direction = RIGHT; /* Initial direction */
    if (x >= 250)
        direction = LEFT; /* Change direction */
    else if (x <= 0)
        direction = RIGHT; /* Change direction */
    if (direction == RIGHT)
        evas_object_move(data, ++x, 350); /* Slide to right */
    else if (direction == LEFT)
        evas_object_move(data, --x, 350); /* Slide to left */

    return EINA_TRUE;
}

anim = ecore_animator_add(_slide_back_and_forth, rectangle);

if (anim != NULL)
    ecore_animator_del(anim);
```

> **Note**
>
> The callback function can return `ECORE_CALLBACK_RENEW` or `EINA_TRUE` to keep the animator running, or `ECORE_CALLBACK_CANCEL` or `EINA_FALSE` to stop the animator and delete it automatically at any time.
>
> If the callback returns `ECORE_CALLBACK_RENEW` or `EINA_TRUE`, you must delete the animator manually when it is no longer needed. Use the `ecore_animator_del()` function, which frees the memory allocated to the `Ecore_Animator` object by deleting the pointer.

## Starting a Delayed Animation

Delaying an animation can be useful if, for example, you want to start an animation only after another one has finished.

To play 2 animations in a sequence, use the `ecore_timer_add()` function to set a delay for the second animation that is equal to the duration of the first animation:

```
static int runtime = 5;
static int delay = runtime;

/* First animation */
static Eina_Bool
_start_fold_animation(void *data)
{
    ecore_animator_timeline_add(runtime, _fold_animation, data);

    return EINA_FALSE;
}

/* Second animation */
static Eina_Bool
_start_unfold_animation(void *data)
{
    ecore_animator_timeline_add(runtime, _unfold_animation, data);

    return EINA_FALSE;
}

/* Start the first animation */
_start_fold_animation(my_evas_object);

/* Start the second animation with the delay */
ecore_timer_add(delay, _start_unfold_animation, my_evas_object);
```

## Pausing and Resuming Animations

You can pause and resume Ecore animations:

- To pause a running animation, use the `ecore_animator_freeze()` function with the `Ecore_Animator` variable as a parameter.
- To resume the paused animation, use the `ecore_animator_thaw()` function with the `Ecore_Animator` variable as a parameter.

The following example pauses an animation after 5 seconds and resumes it after 5 more seconds:

```
static Eina_Bool
_freeze_animation(void *data)
{
    ecore_animator_freeze(data);

    return EINA_FALSE;
}

static Eina_Bool
_thaw_animation(void *data)
{
    ecore_animator_thaw(data);

    return EINA_FALSE;
}

/* Start the animation */
animator = ecore_animator_add(_slide_back_and_forth, rectangle);

/* Pause the animation after 5 seconds */
ecore_timer_add(5, _freeze_animation, animator);

/* Resume the animation after 5 more seconds */
ecore_timer_add(10, _thaw_animation, animator);
```

## Using Position Mappings

Position mappings allow you to create various non-linear changes in your animation to implement the evolution of a given position according to the desired effects. You can apply dynamic changes to any attribute of the Evas object, such as position, width, height, scale, angle, and color.

When you use the animation callback function with the `ecore_animator_timeline_add()` function, the animator passes to the callback a timeline position parameter with a value between 0.0 (start) and 1.0 (end) to indicate where along the timeline the animator is running. To create a non-linear animation, you can map the position value to one of several curves and mappings using the `ecore_animator_pos_map()` function:

- The first parameter is the current position value, which ranges from 0.0 to 1.0.
- The second parameter is the position mapping you want to apply, defined with the `_Ecore_Pos_Map` enumerator (in [mobile](../../../api/mobile/latest/group__Ecore__Animator__Group.html#ga2db0d0f0f3973829c7f700e5af3e041c) and [wearable](../../../api/wearable/latest/group__Ecore__Animator__Group.html#ga2db0d0f0f3973829c7f700e5af3e041c) applications).
- The third (`v1`) and fourth (`v2`) parameters are specific to the chosen position mapping, and provide additional configuration for it.

The following table lists the supported position mappings, and describes how the third (`v1`) and fourth (`v2`) parameters of the `ecore_animator_pos_map()` function are used with each mapping.

<a name="table_position_mappings"></a>
**Table: Position mappings**

<table id="position_mappings">
	<thead>
		<tr>
			<th>Position mapping type
			<p>(<code>_Ecore_Pos_Map</code> enumerator value)</p>
			</th>
			<th>Description</th>
			<th>Parameters</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td><code>ECORE_POS_MAP_LINEAR</code></td>
			<td>Linear 0.0 - 1.0
			<p><img alt="Position mappings" src="media/pos_map_linear.png" /></p>
			</td>
			<td><code>v1</code>: Not used
			<p><code>v2</code>: Not used</p>
			</td>
		</tr>
		<tr>
			<td><code>ECORE_POS_MAP_ACCELERATE</code></td>
			<td>Start slow, then speed up
			<p><img alt="Position mappings" src="media/pos_map_accelerate.png" /></p>
			</td>
			<td><code>v1</code>: Not used
			<p><code>v2</code>: Not used</p>
			</td>
		</tr>
		<tr>
			<td><code>ECORE_POS_MAP_DECELERATE</code></td>
			<td>Start fast, then slow down
			<p><img alt="Position mappings" src="media/pos_map_decelerate.png" /></p>
			</td>
			<td><code>v1</code>: Not used
			<p><code>v2</code>: Not used</p>
			</td>
		</tr>
		<tr>
			<td><code>ECORE_POS_MAP_SINUSOIDAL</code></td>
			<td>Start slow, speed up, then slow down at the end
			<p><img alt="Position mappings" src="media/pos_map_sinusoidal.png" /></p>
			</td>
			<td><code>v1</code>: Not used
			<p><code>v2</code>: Not used</p>
			</td>
		</tr>
		<tr>
			<td><code>ECORE_POS_MAP_BOUNCE</code></td>
			<td>Start at 0.0, then drop like a ball bouncing to the ground at 1.0, and bounce <code>v2</code> times, with a decay factor of <code>v1</code>
			<p><img alt="Position mappings" src="media/pos_map_bounce.png" /></p>
			</td>
			<td><code>v1</code>: Bounce decay factor
			<p><code>v2</code>: Number of bounces</p>
			</td>
		</tr>
		<tr>
			<td><code>ECORE_POS_MAP_SPRING</code></td>
			<td>Start at 0.0, then wobble like a spring until rest position at 1.0, and wobble <code>v2</code> times, with a decay factor of <code>v1</code>
			<p><img alt="Position mappings" src="media/pos_map_spring.png" /></p>
			</td>
			<td><code>v1</code>: Wobble decay factor
			<p><code>v2</code>: Number of wobbles</p>
			</td>
		</tr>
		<tr>
			<td><code>ECORE_POS_MAP_ACCELERATE_FACTOR</code></td>
			<td>Start slow, then speed up</td>
			<td><code>v1</code>: Power factor:
			<ul>
				<li>0.0 is linear</li>
				<li>1.0 is standard acceleration</li>
				<li>2.0 is a much more pronounced acceleration (squared)</li>
				<li>4.0 is cubed</li>
			</ul>
			<p><code>v2</code>: Not used</p>
			</td>
		</tr>
		<tr>
			<td><code>ECORE_POS_MAP_DECELERATE_FACTOR</code></td>
			<td>Start fast, then slow down</td>
			<td><code>v1</code>: Power factor:
			<ul>
				<li>0.0 is linear</li>
				<li>1.0 is standard deceleration</li>
				<li>2.0 is a much more pronounced deceleration (squared)</li>
				<li>3.0 is cubed</li>
			</ul>
			<p><code>v2</code>: Not used</p>
			</td>
		</tr>
		<tr>
			<td><code>ECORE_POS_MAP_SINUSOIDAL_FACTOR</code></td>
			<td>Start slow, speed up, then slow down at the end</td>
			<td><code>v1</code>: Power factor:
			<ul>
				<li>0.0 is linear</li>
				<li>1.0 is a standard sinusoidal</li>
				<li>2.1 is a much more pronounced sinusoidal (squared)</li>
				<li>3.0 is cubed</li>
			</ul>
			<p><code>v2</code>: Not used</p>
			</td>
		</tr>
		<tr>
			<td><code>ECORE_POS_MAP_DIVISOR_INTERP</code></td>
			<td>Start at gradient <code>v1</code>, interpolated using the power of the <code>v2</code> curve</td>
			<td><code>v1</code>: Multiplication factor for the gradient
			<p><code>v2</code>: Curve value</p>
			</td>
		</tr>
	</tbody>
</table>

The following example performs an animation where the `my_evas_object` object is moved 600 pixels downwards, bouncing back 7 times over 5 seconds, each bounce diminishing by a factor of 1.8:

```
static Eina_Bool
_my_animation_callback(void *data, double pos)
{
    Evas_Object *obj = data; /* Get the target object */
    /* Target object geometry */
    int x;
    int y;
    int w;
    int h;
    double frame = pos; /* Actual position variation */
    /* Get the frame relative position depending on desired effect */
    /*
       Use the ECORE_POS_MAP_BOUNCE position mapping type with
       7 bounces and the bounce decay factor of 1.8
    */
    frame = ecore_animator_pos_map(pos, ECORE_POS_MAP_BOUNCE, 1.8, 7);
    /* Get current object position and size attributes */
    evas_object_geometry_get(obj, &x, &y, &w, &h);
    /* Move the Evas object 600 pixels down */
    evas_object_move(obj, x, 600 * frame);

    return EINA_TRUE;
}

/* Run the animation for 5 seconds */
ecore_animator_timeline_add(5, _my_animation_callback, my_evas_object);
```

## Using Timers

To use a timer, first define the timer source with the `ecore_animator_source_set()` function. To determine the current timer source, use the `ecore_animator_source_get()` function.

Tizen supports default and custom timer sources:

- The default timer, used in most cases, is `ECORE_ANIMATOR_SOURCE_TIMER`. It ticks every "frametime" seconds and allows you to perform transitions within a predefined timeline. The timer uses the system clock to tick over every nth second, with the default being 1/30th of a second.

  To tweak the performance, change the frametime value using the `ecore_animator_frametime_set()` function with the new frametime as the parameter.

  > **Note**
  >
  > If the value is too small, it can cause performance issues, whereas a too high value can cause the animation to seem jerky.

  To get the current frametime value, use the `ecore_animator_frametime_get()` function.

- The custom timer is `ECORE_ANIMATOR_SOURCE_CUSTOM`. It is used to match the animation to third-party events by allowing you to control when it ticks.

  For example, the filling speed of a progress bar mainly depends on the time it takes for a task to complete and the velocity at which the remaining time estimation evolves. This kind of animation requires a custom timer.

  To set up a custom timer:

  1. Set the time source to a custom timer.
  2. Trigger a tick over one frame using the `ecore_animator_custom_tick()` function.

  The following example creates a custom timer for a progress bar that is refreshed every time some progress occurs:

  ```
  ecore_animator_source_set(ECORE_ANIMATOR_SOURCE_CUSTOM);

  void
  _on_progress_update()
  {
      /* Called when some progress occurs */
      ecore_animator_custom_tick(); /* Tick (next frame in progress bar animation) */
  }
  ```

  To drive the timer based on an input tick source (such as another application using the IPC or a vertical blanking interrupt), you can use the `ecore_animator_custom_source_tick_begin_callback_set()` and `ecore_animator_custom_source_tick_end_callback_set()` functions. These functions define callbacks that are called when the tick starts and ends, allowing you to set the functions to start and stop the ticking source.

> **Note**
>
> Except as noted, this content is licensed under [LGPLv2.1+](http://opensource.org/licenses/LGPL-2.1).

## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
