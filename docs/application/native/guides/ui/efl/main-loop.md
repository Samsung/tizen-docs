# Handling the Main Loop

The EFL is event-driven. This means that the application polls for data, and listens for events to interact with it.

The Ecore library provides the main loop abstraction. It gets data when data is available and sends the events so that costly polling threads are not needed. Ecore manages polling, timers, events, and file descriptors. When there is no ongoing event, the main loop automatically enters an idle mode, minimizing the power consumption. The loop wakes up when needed.

## Starting the Main Loop

To start the Ecore main loop and move your application into the running state, call the `ui_app_main()` function. The Ecore main loop handles all general events, such as touch, mouse, key, and network events.

```
int
main(int argc, char *argv[])
{
    ret = ui_app_main(argc, argv, &event_callback, &ad);

    return ret;
}
```

When your application is running:

1. Create a window and organize the UI components inside the window.
2. Create the application logic code to be called when callbacks or timed events occurs (for example, animators for animations and timers for timeouts).

## Timers

Ecore provides timers, which schedule events that are executed later at a specific time. The event can occur once or several times at specific intervals.

A timer callback prototype looks like the `my_timed_cb()` callback function. This function receives data from the application, and returns a Boolean value to specify whether it is called again or completed. The following macros are also provided:

- `ECORE_CALLBACK_RENEW`: the function is called again after the timeout.
- `ECORE_CALLBACK_CANCEL`: the function is not called again, Ecore destroys automatically everything associated with the timer.

To create and destroy a timer:

- To create a timer, use the `ecore_timer_add()` function. The interval, specified in seconds, indicates when the given function is called, and receives the specified data as a parameter. It returns an `Ecore_Timer` object.

  In the following example, the `my_timed_cb()` function is run after 2 seconds and it receives `my_data`. It is renewed while its count variable value is under 5, and stops after that.

  ```
  Eina_Bool
  my_timed_cb(void *data)
  {
      static int count = 0;
      count++;

      if (count < 5)
          return ECORE_CALLBACK_RENEW;

      return ECORE_CALLBACK_CANCEL;
  }
  ecore_timer_add(2.0, my_timed_cb, my_data);
  ```

- To delete the timer, use the `ecore_timer_del()` function. The timer to delete must still be running, that is, it has not returned a `false` value. If the timer is not running, the function cannot be called.

To manage a timer:

- To change the timer's interval, use the `ecore_timer_interval_set()` function. The interval is specified in seconds. If set during a timer call, this affects the next interval. Use the `ecore_timer_interval_get()` function to get the timer's current interval.
- To get the timer's pending time, use the `ecore_timer_pending_get()` function.
- To delay the timer's next occurrence, use the `ecore_timer_delay()` function. The function adds the specified time to the current interval. It does not change the future occurrences' interval. You can also reset the current interval to its full value by using the `ecore_timer_reset()` function.
- To pause the currently-running timer, use the `ecore_timer_freeze()` function. The remaining time is saved and used again when the timer is resumed with the `ecore_timer_thaw()` function.
- To query the current value of the defined timer infrastructure precision, use the `ecore_timer_precision_get()` function. A higher delay means that more timers can be run together. It diminishes the need to use system wake-ups and thus lowers the power consumption.

 To set the precision, use the `ecore_timer_precision_set()` function. This sets the precision for all timers. For example, there are 2 timers, one that expires in 2.0 seconds and another that expires in 2.1 seconds. If the precision is set to 0.1 seconds, Ecore requests the next expiration to happen in 2.1 seconds and runs both callbacks at once, instead of one at 2.0 seconds and the other one 0.1 seconds later. However, if there is no timer expiring in 2.1 seconds, the timeout is at the minimum interval, 2 seconds.

## Animators

Animators are a specific type of timer, specially designed for on-screen animation purposes:

- The time interval is usually known when they are created.
- They are called at each screen refresh and their interval can vary. The interval can depend on the system load, the target power consumption, and other factors. The exact interval is not relevant.

To implement animators, Ecore provides the Ecore animator subsystem.

### Forever-running Animator

To create an animation that runs for an indefinite time:

```
Eina_Bool
my_anim_cb(void *data)
{
    static int count = 0;
    count++;
    if (count < 5)
        return ECORE_CALLBACK_RENEW;

    return ECORE_CALLBACK_CANCEL;
}
ecore_animator_add(my_anim_cb, my_data);
```

This example looks the same as the one using an Ecore timer. The `ecore_animator_add()` function takes the callback function and data to pass to it, and returns an `Ecore_Animator` object. The function is called at a system-defined interval until it returns `ECORE_CALLBACK_CANCEL` instead of `ECORE_CALLBACK_RENEW`.

### Specific-duration Animator

An animator callback for an animator running a specific time has a different prototype than the forever running animator.

This callback function receives both data and a position which represents the current time among the full timeline, 0 meaning the beginning of the animation, and 1 meaning the end of the animation, returning `ECORE_CALLBACK_CANCEL` to abort, or `ECORE_CALLBACK_RENEW` to continue.

To create and destroy the animator:

- To create the animator, use the `ecore_animator_timeline_add()` function. The first parameter specifies the animator duration, the second parameter is the callback function, and the third parameter is the data to pass to the callback. The data parameter is optional.

  ```
  Eina_Bool
  my_anim_cb(void *data, double position)
  {
      if (position < .5)
          return ECORE_CALLBACK_RENEW;

      return ECORE_CALLBACK_CANCEL;
  }
  ecore_animator_timeline_add(5., my_anim_cb, my_data);
  ```

  In this example, the animator is specified to run for 5 seconds. The function returns `ECORE_CALLBACK_CANCEL` as soon as the position among the timeline passes half of the duration, 2.5 seconds.

  Ecore can generate a virtual position from the original one using `ecore_animator_pos_map(position, map, v1, v2)`. Several maps are available:

  - `ECORE_POS_MAP_LINEAR`: linear from 0.0 to 1.0.

  - `ECORE_POS_MAP_ACCELERATE`: start slow, then speed up.

  - `ECORE_POS_MAP_DECELERATE`: start fast, then slow down.

  - `ECORE_POS_MAP_SINUSOIDAL`: start slow, speed up, then slow down at the end.

  - `ECORE_POS_MAP_ACCELERATE_FACTOR`: start slow, then speed up, `v1` being a power factor: 0.0 is linear, 1.0 is standard acceleration, 2.0 is a much more pronounced acceleration (squared), and 3.0 is cubed.

  - `ECORE_POS_MAP_DECELERATE_FACTOR`: start fast, then slow down, `v1` being a power factor: 0.0 is linear, 1.0 is standard deceleration, 2.0 is a much more pronounced deceleration (squared), and 3.0 is cubed.

  - `ECORE_POS_MAP_SINUSOIDAL_FACTOR`: start slow, speed up, then slow down at the end, `v1` being a power factor: 0.0 is linear, 1.0 is a standard sinusoidal, 2.0 is a much more pronounced sinusoidal (squared), and 3.0 is cubed.

  - `ECORE_POS_MAP_DIVISOR_INTERP`: start at gradient `* v1`, interpolated with the power of `v2` curve.

  - `ECORE_POS_MAP_BOUNCE`: start at 0.0, then drop like a ball bouncing to the ground at 1.0, and bounce `v2` times, with a decay factor of `v1`.

  - `ECORE_POS_MAP_SPRING`: start at 0.0, then wobble like a spring to the rest position 1.0, and wobble `v2` times, with a decay factor of `v1`.

    **Figure: Position maps**![Position maps](./media/pos_map_all.png)

- To destroy the animator, use the `ecore_animator_del()` function. The animator to destroy must be running, that is, it has not returned a `false` value. If the animator is not running, the function cannot be called.

To manage the animator:

- To pause the currently-running animator, use the `ecore_animator_freeze()` function. Note that time continues ticking even if the animator is frozen, and that resuming the animation using the `ecore_animator_thaw()` function does not actually resume, if the full runtime has been passed in the meanwhile.
- To query Ecore for the interval between 2 animator calls, use the `ecore_animator_frametime_get()` function.
- To change the interval, use the `ecore_animator_frametime_set(interval)` function. Note that too small a value causes performance and power consumption issues, and too high a value makes the animation jerky.

## File Descriptors

Ecore provides an infrastructure to monitor file descriptors, so that files do not have to be blocked or polled to read or write on them. Instead, monitor sockets, pipes, or other streams are used to get a file descriptor.

To manage the file descriptors:

- To set a callback, use the `_my_cb_func()` function. Its first parameter is the data passed to it (optional), and the second one is the Ecore file descriptor handler. Its return value is, as in most Ecore callbacks, `ECORE_CALLBACK_RENEW` or `ECORE_CALLBACK_CANCEL`. It tells Ecore whether it wants to be called again or whether its treatment is finished.

- To listen for events, use the `ecore_main_fd_handler_add()` function.

- To wait for incoming data (that is, to read data) on the `my_fd` file descriptor, passing `my_data`:

  ```
  Eina_Bool
  my_fd_cb(void *data, Ecore_Fd_Handler *handler)
  {
      int fd;
      fd = ecore_main_fd_handler_fd_get(handler);
      count = read(fd, buf, sizeof(buf)); /* This is guaranteed not to block */

      return ECORE_CALLBACK_RENEW;
  }
  ecore_main_fd_handler_add(my_fd, ECORE_FD_READ, my_fd_cb, my_data, NULL, NULL);
  ```

- To delete a file descriptor handler, use the `ecore_main_fd_handler_del()` function. This does not close the file descriptor. Always delete the handlers before closing the actual file descriptors.

- To get the handler's file descriptor, use the `ecore_main_fd_handler_fd_get()` function.

- To select whether a flag is active on a handler, use the `ecore_main_fd_handler_active_get()` function. For example, the handler is set to monitor both `ECORE_FD_READ` and `ECORE_FD_ERROR`. The following example finds out whether the function was called because of an error:

  ```
  Eina_Bool
  my_fd_cb(void *data, Ecore_Fd_Handler *handler)
  {
      int fd;
      fd = ecore_main_fd_handler_fd_get(handler);
      if (ecore_main_fd_handler_active_get(handler, ECORE_FD_ERROR) == EINA_TRUE) {
          /* We have an error! */

          return ECORE_CALLBACK_CANCEL;
      }
      count = read(fd, buf, sizeof(buf)); /* This is guaranteed not to block */

      return ECORE_CALLBACK_RENEW;
  }
  ecore_main_fd_handler_add(my_fd, ECORE_FD_READ | ECORE_FD_ERROR, my_fd_cb, my_data, NULL, NULL);
  ```

- To change the flags the handler is monitoring, use the `ecore_main_fd_handler_active_set()` function.

## Threads

EFL is not entirely thread-safe. This means that if a task is running in another thread and, for example, an Evas object shows the status progress of this task, the object cannot be updated from within the thread. Updating can only be done from the main thread that runs the main loop.

Ecore provides a facility to perform tasks on separate worker threads. It is not a simple wrapper around standard threads provided by the operating system. With Ecore threads, it is easier to dispatch a worker function to perform some heavy tasks and get the result once it completes. It does not block the application UI. It is also easy to cancel and reschedule threads. Several threads can be launched simultaneously, since Ecore schedules them according to the number of processors the system has and the maximum amount of concurrent threads set for the application.

Ecore has 2 kinds of threads:

- Short jobs do not give any kind of information on their status to the parent. They are best used for short computing-intensive snippets of code.
- Feedback jobs give information on their status to the parent. They are best used for longer snippets requiring a feedback loop, such as an ongoing file download.

Ecore creates a pool of worker threads. The exact count is computed from the number of CPUs or cores, or it can be specified by the application itself.

When a worker thread is idle, it picks a job to execute from the waiting list until there is none left. In the following example, there are 2 threads defined by `my_short_job()` and `my_feedback_job()`. Both threads take 2 parameters: some data passed to them, and the actual thread running. Call a callback when the jobs end, whether they are cancelled (`my_job_cancel()`) or end normally (`my_job_end()`).

```
struct feedback_msg {
    int pos;
};

void
my_short_job(void *data, Ecore_Thread *thread)
{
    usleep(200000);
}

void
my_feedback_job(void *data, Ecore_Thread *thread)
{
    int i;
    for (i = 0; i < 100; i++) {
        usleep(50000); /* You can have some real computation done */
        struct feedback_msg *message = malloc(sizeof(struct feedback_msg));
        if (message) {
            message->pos = i;
            ecore_thread_feedback(thread, message);
        }
        if (ecore_thread_check(thread))
            return;
    }
}

void
my_feedback_job_notify(void *data, Ecore_Thread *thread, void *msg)
{
    struct feedback_msg *message = msg;
    free(message);
}

void
my_job_end(void *data, Ecore_Thread *thread)
{
    dlog_print(DLOG_INFO, LOG_TAG, "Thread has normally ended.\n");
}

void
my_job_cancel(void *data, Ecore_Thread *thread)
{
    dlog_print(DLOG_INFO, LOG_TAG, "Thread has been cancelled.\n");
}

ecore_thread_run(my_short_job, my_job_end, my_job_cancel, my_data);
ecore_thread_feedback_run(my_feedback_job, my_feedback_job_notify, my_job_end,
                          my_job_cancel, my_data, EINA_FALSE);
```

To manage threads:

- To cancel a thread, use the `ecore_thread_cancel()` function. However, note that this is done cooperatively: the thread continues to run until it exists. Call the `ecore_thread_check()` function regularly to check whether the thread has been marked for cancellation and exit if `true`.

- To run threads that are not accounted for in the worker thread pool, use the `ecore_thread_feedback_run()` function with the last parameter set to `EINA_TRUE`.

  The feedback message a thread sends as notification can be any kind of data. In the above example, it is a simple integer, but it can be as complex as needed.

- To execute a thread later, use the `ecore_thread_reschedule()` function. This function is added to the end of the pending tasks.

- To get the maximum number of concurrent threads, use the `ecore_thread_max_get()` function. If needed, set it by using the `ecore_thread_max_set()` function, or reset the default value using the `ecore_thread_max_reset()` function.

- To query the number of active threads, use the `ecore_thread_active_get()` function. To query the number of available worker threads, use the `ecore_thread_available_get()` function, which is basically the same as the `ecore_thread_max_get()` - `ecore_thread_active_get()`.

## Idlers

When the rendering is done and all work is finished, the main loop enters its idle state until the next loop. You can get the functions of your application called back before the main loop enters or exits the idle state, or when it is in the idle state. They are respectively called `Ecore_Idle_Enterer`, `Ecore_Idle_Exiter`, and `Ecore_Idler`.

**Figure: Idle loop**

![Idle loop](./media/idlers.png)

The idle enterers, exiters, and idlers all have the same prototype, `my_idler()`, which receives data and returns `ECORE_CALLBACK_RENEW` or `ECORE_CALLBACK_CANCEL` to tell Ecore whether it wants to be called again or is finished.

To manage the idlers:

- To add an idler, use the `ecore_idler_add()` function.
- To delete an idler, use the `ecore_idler_del()` function.
- To add and delete idle exiters, use the `ecore_idle_exiter_add()` and `ecore_idle_exiter_del()` functions.
- To add and delete idle enterers, use the `ecore_idle_enterer_add()` and `ecore_idle_enterer_del()` functions. The `ecore_idle_enterer_before_add()` function is also available, if you want your function to be added at the top of the list so that it is called before the others.

```
Eina_Bool
my_idle_enterer_cb(void *data)
{
    return ECORE_CALLBACK_RENEW;
}

Eina_Bool
my_idle_exiter_cb(void *data)
{
    return ECORE_CALLBACK_CANCEL;
}

Eina_Bool
my_idler(void *data)
{
    return ECORE_CALLBACK_RENEW;
}

ecore_idle_enterer_add(my_idle_enterer_cb, my_data);
ecore_idle_exiter_add(my_idle_exiter_cb, my_data);
ecore_idler_add(my_idler_cb, my_data);
```

> **Note**
>
> Except as noted, this content is licensed under [LGPLv2.1+](http://opensource.org/licenses/LGPL-2.1).

## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
