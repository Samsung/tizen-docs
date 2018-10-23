# Handling Touch Gestures

You can implement your application to recognize and react to different types of gestures provided by the EFL library.

The Elementary library provides a gesture layer for a wide range of touch gestures, such as tap, double tap, triple tap, long tap, momentum monitoring, line, flick, zoom, and rotate, which can be used by the application to build a dynamic user interface interaction which is simple and intuitive to use.

## Initializing Touch Gestures

To initialize the touch gestures:

1. Create a window for the application layout.

   The `evas_object_rectangle_add()` function adds a rectangle for getting user input in the same Evas with a window object.

   ```
   Evas_Object *win;
   /* Gesture layer transparent object */
   Evas_Object *r;
   /* Gesture layer object */
   Evas_Object *g;

   win = elm_win_util_standard_add("gesture_layer", "Gesture Layer");
   elm_win_autodel_set(win, EINA_TRUE);

   /* Gesture layer transparent object */
   r = evas_object_rectangle_add(evas_object_evas_get(win));
   evas_object_move(r, 0, 0);
   evas_object_color_set(r, 0, 0, 0, 0);
   elm_win_resize_object_add(win, r);
   ```

2. Create a new gesture layer with the `elm_gesture_layer_add()` function.

   The `elm_gesture_layer_attach()` function attaches a given gesture layer to an `Evas_Object`. This object listens for all mouse and key events, and reports the gestures made upon it.

   ```
   /* Gesture layer object */
   g = elm_gesture_layer_add(win);
   elm_gesture_layer_attach(g, r);
   evas_object_show(r);
   ```

## Implementing Tap Gestures

You can configure some properties of the tap gestures:

- Modify the timeout value for a long tap or double tap gesture.

  The default values are defined in the system policy. In Tizen, they are 0.5 seconds for a long tap, and 0.33 seconds for a double tap.

  ```
  /* Get or set the gesture layer long tap start timeout of an object */
  void elm_gesture_layer_long_tap_start_timeout_set(Evas_Object *obj, double long_tap_start_timeout);
  double elm_gesture_layer_long_tap_start_timeout_get(const Evas_Object *obj);

  /* Get or set the gesture layer double tap timeout of an object */
  void elm_gesture_layer_double_tap_timeout_set(Evas_Object *obj, double double_tap_timeout);
  double elm_gesture_layer_double_tap_timeout_get(const Evas_Object *obj);
  ```

- The gesture layer uses the finger size to detect a double and triple tap. If you do not set a finger size, the gesture layer uses the default `elm_config` finger size defined in the system policy. In Tizen, it is 40.

  You can also define the tolerance for each tap.

  ```
  /* Get or set the gesture layer finger size for taps */
  void elm_gesture_layer_tap_finger_size_set(Evas_Object *obj, Evas_Coord sz);
  Evas_Coord elm_gesture_layer_tap_finger_size_get(const Evas_Object *obj);
  ```

The gesture layer supports 4 types of tap gestures and 4 gesture states:

```
/* Gesture types */
ELM_GESTURE_N_TAPS, /* Single tap */
ELM_GESTURE_N_LONG_TAPS, /* Long tap */
ELM_GESTURE_N_DOUBLE_TAPS, /* Double tap */
ELM_GESTURE_N_TRIPLE_TAPS, /* Triple tap */

/* Gesture states */
ELM_GESTURE_STATE_START, /* Gesture started */
ELM_GESTURE_STATE_MOVE, /* Gesture ongoing */
ELM_GESTURE_STATE_END, /* Gesture completed */
ELM_GESTURE_STATE_ABORT /* Ongoing gesture aborted */
```

To use the various tap gestures:

- Single tap

  1. Use the `elm_gesture_layer_cb_set()` function to set callbacks to be notified about the change of the gesture state:

     ```
     elm_gesture_layer_cb_set(g, ELM_GESTURE_N_TAPS, ELM_GESTURE_STATE_START,
                              n_finger_tap_start, NULL);
     elm_gesture_layer_cb_set(g, ELM_GESTURE_N_TAPS, ELM_GESTURE_STATE_END,
                              n_finger_tap_end, NULL);
     elm_gesture_layer_cb_set(g, ELM_GESTURE_N_TAPS, ELM_GESTURE_STATE_ABORT,
                              n_finger_tap_abort, NULL);
     ```

  2. When a mouse down event occurs, the `n_finger_tap_start()` callback function is called:

     ```
     /* Start gesture callback */
     static Evas_Event_Flags
     n_finger_tap_start(void *data, void *event_info)
     {
         Elm_Gesture_Taps_Info *p = (Elm_Gesture_Taps_Info *)event_info;
         printf("N tap started <%p> x,y=<%d,%d> count=<%d> timestamp=<%d> \n",
                event_info, p->x, p->y, p->n, p->timestamp);

         return EVAS_EVENT_FLAG_ON_HOLD;
     }
     ```

     The function returns `EVAS_EVENT_FLAG_ON_HOLD`, if the component acted upon the event.

     The `event_info` attribute contains the tap information in the `_Elm_Gesture_Taps_Info` data structure. If the number of fingers is bigger than 2, the `x` and `y` values get the average value of each `x` and `y` geometry values.

     ```
     struct _Elm_Gesture_Taps_Info {
         Evas_Coord x, y; /* Center point between fingers */
         unsigned int n; /* Number of fingers tapped */
         unsigned int timestamp; /* Event timestamp */
     };
     ```

  3. When a mouse up event occurs, and the current tap gesture is in the `ELM_GESTURE_STATE_START` state, the `n_finger_tap_end()` callback function is called:

     ```
     static Evas_Event_Flags
     n_finger_tap_end(void *data, void *event_info)
     {
         Elm_Gesture_Taps_Info *p = (Elm_Gesture_Taps_Info *)event_info;

         printf("N tap started <%p> x,y=<%d,%d> count=<%d> timestamp=<%d> \n",
                event_info, p->x, p->y, p->n, p->timestamp);

         return EVAS_EVENT_FLAG_ON_HOLD;
     }
     ```

  4. When an unexpected event occurs after a mouse down event, the `n_finger_tap_abort()` callback function is called.

     For example, if a move event occurs after a tap start callback function is called, or a down event occurs after a long-press event.

     ```
     static Evas_Event_Flags
     n_finger_tap_abort(void *data, void *event_info)
     {
         Elm_Gesture_Taps_Info *p = (Elm_Gesture_Taps_Info *)event_info;
         printf("N tap abort\n");

         return EVAS_EVENT_FLAG_ON_HOLD;
     }
     ```

- Double tap

  1. Use the `elm_gesture_layer_cb_set()` function to set callbacks to be notified about the change of the gesture state:

     ```
     elm_gesture_layer_cb_set(g, ELM_GESTURE_N_DOUBLE_TAPS, ELM_GESTURE_STATE_START,
                              dbl_click_start, NULL);
     elm_gesture_layer_cb_set(g, ELM_GESTURE_N_DOUBLE_TAPS, ELM_GESTURE_STATE_MOVE,
                              dbl_click_move, NULL);
     elm_gesture_layer_cb_set(g, ELM_GESTURE_N_DOUBLE_TAPS, ELM_GESTURE_STATE_END,
                              dbl_click_end, NULL);
     elm_gesture_layer_cb_set(g, ELM_GESTURE_N_DOUBLE_TAPS, ELM_GESTURE_STATE_ABORT,
                              dbl_click_abort, NULL);
     ```

  2. A double tap gesture is started by calling the `dbl_click_start()` callback function when a mouse down event occurs.

     After a mouse down event occurs, a mouse up event has to occur within the `double_tap_timeout` time limit.

     In this case, the `dbl_click_move()` callback function is called, which means a double tap gesture event is ongoing. Otherwise, the abort callback function is called.

     If the mouse up is not called within the `double_tap_timeout` value, the touch event moves out of the area defined in the down event geometry.

  3. The `dbl_click_end()` callback function is called when the same area is clicked 2 times within the `double_tap_timeout` value (meaning that the `dbl_click_move()` callback function has been called 2 times).

     If any wrong gesture is detected during the double tap gesture detection, the `dbl_click_abort()` callback function is called.

- Triple tap

  1. Use the `elm_gesture_layer_cb_set()` function to set callbacks to be notified about the change of the gesture state:

     ```
     elm_gesture_layer_cb_set(g, ELM_GESTURE_N_TRIPLE_TAPS, ELM_GESTURE_STATE_START,
                              triple_click_start, NULL);
     elm_gesture_layer_cb_set(g, ELM_GESTURE_N_TRIPLE_TAPS, ELM_GESTURE_STATE_MOVE,
                              triple_click_move, NULL);
     elm_gesture_layer_cb_set(g, ELM_GESTURE_N_TRIPLE_TAPS, ELM_GESTURE_STATE_END,
                              triple_click_end, NULL);
     elm_gesture_layer_cb_set(g, ELM_GESTURE_N_TRIPLE_TAPS, ELM_GESTURE_STATE_ABORT,
                              triple_click_abort, NULL);
     ```

  2. The `triple_click_start()` callback function is called when a mouse down event occurs.

     After a mouse down occurs, a mouse up event has to occur within the `double_tap_timeout` value. If so, the `triple_click_move()` callback function is called, which means a triple tap gesture event is ongoing. Otherwise, the abort callback is called.

     If the mouse up is not called within the `double_tap_timeout` value, the touch event moves out of the area defined in the down event geometry.

  3. The `triple_click_end()` callback function is called if the same area is clicked 3 times within the `double_tap_timeout` value (meaning that the `triple_click_move()` callback function has been called 3 times: 1 tap start and move, 2 tap move and move, and 3 tap move and end).

     If any wrong gesture is detected during the triple tap gesture detection, the `triple_click_abort()` callback function is called.

- Long tap

  1. Use the `elm_gesture_layer_cb_set()` function to set callbacks to be notified about the change of the gesture state:

     ```
     elm_gesture_layer_cb_set(g, ELM_GESTURE_N_LONG_TAPS, ELM_GESTURE_STATE_START,
                              n_long_tap_start, NULL);
     elm_gesture_layer_cb_set(g, ELM_GESTURE_N_LONG_TAPS, ELM_GESTURE_STATE_MOVE,
                              n_long_tap_move, NULL);
     elm_gesture_layer_cb_set(g, ELM_GESTURE_N_LONG_TAPS, ELM_GESTURE_STATE_END,
                              n_long_tap_end, NULL);
     elm_gesture_layer_cb_set(g, ELM_GESTURE_N_LONG_TAPS, ELM_GESTURE_STATE_ABORT,
                              n_long_tap_abort, NULL);
     ```

  2. The `n_long_tap_start()` callback function is called when a mouse down event occurs.

     After a mouse down occurs, the mouse down state has to remain for a time defined in the `long_tap_timeout` value.

     The `n_long_tap_move()` callback function is called after the `long_tap_timeout` time. If the down gesture continues, the `n_long_tap_move()` callback function is called at the `long_tap_timeout` time value intervals, such as 0.5, 1.0, and 1.5.

  3. After the `n_long_tap_move()` callback function is called, if the mouse up event occurs in the same geometry with the down event, the `n_long_tap_end()` callback function is called.

     If any wrong gesture is detected during the long tap gesture detection, the `n_long_tap_abort()` callback function is called.

## Implementing Momentum Gestures

The momentum gesture is used for detecting any move events on the gesture layer and getting event information to make a meaningful gesture action. The momentum gesture is used for detecting line, zoom, and rotate gestures as well.

The momentum gesture states the same as in the [tap gesture](#implementing-tap-gestures).

To implement a momentum gesture:

1. Use the `elm_gesture_layer_cb_set()` function to set callbacks to be notified about the change of the gesture state:

   ```
   elm_gesture_layer_cb_set(g, ELM_GESTURE_MOMENTUM, ELM_GESTURE_STATE_START,
                            momentum_start, NULL);
   elm_gesture_layer_cb_set(g, ELM_GESTURE_MOMENTUM, ELM_GESTURE_STATE_END,
                            momentum_end, NULL);
   elm_gesture_layer_cb_set(g, ELM_GESTURE_MOMENTUM, ELM_GESTURE_STATE_ABORT,
                            momentum_abort, NULL);
   elm_gesture_layer_cb_set(g, ELM_GESTURE_MOMENTUM, ELM_GESTURE_STATE_MOVE,
                            momentum_move, NULL);
   ```

2. The `momentum_start()` callback function is called when a mouse move event occurs after a mouse down event:

   ```
   static Evas_Event_Flags
   momentum_start(void *data, void *event_info)
   {
       Elm_Gesture_Momentum_Info *p = (Elm_Gesture_Momentum_Info *)event_info;
       printf("momentum started x1,y1=<%d,%d> tx,ty=<%u,%u> n=<%u>\n",
              p->x1, p->y1, p->tx, p->ty, p->n);

       return EVAS_EVENT_FLAG_ON_HOLD;
   }
   ```

   The `event_info` attribute contains the momentum information in the `Elm_Gesture_Momentum_Info` data structure:

   ```
   /* Report line ends, timestamps, and momentum computed */
   struct _Elm_Gesture_Momentum_Info {
       Evas_Coord x1; /* Final-swipe direction with starting point on X */
       Evas_Coord y1; /* Final-swipe direction with starting point on Y */
       Evas_Coord x2; /* Final-swipe direction with ending point on X */
       Evas_Coord y2; /* Final-swipe direction with ending point on Y */

       unsigned int tx; /* Timestamp of the start of the final X swipe */
       unsigned int ty; /* Timestamp of the start of the final Y swipe */

       Evas_Coord mx; /* Momentum on X */
       Evas_Coord my; /* Momentum on Y */

       unsigned int n; /* Number of fingers */
   };
   ```

   The x1 and y1 coordinates are not necessarily in sync. The x1 coordinate holds the X value of the X direction starting point, and the y1 coordinate holds the same for Y. This is noticeable when doing a V-shaped movement.

3. The `momentum_move()` callback function is called whenever mouse move events are detected:

   ```
   static Evas_Event_Flags
   momentum_move(void *data, void *event_info)
   {
       Elm_Gesture_Momentum_Info *p = (Elm_Gesture_Momentum_Info *)event_info;
       printf("momentum move x1,y1=<%d,%d> x2,y2=<%d,%d> tx,ty=<%u,%u> mx=<%d> my=<%d> n=<%u>\n",
              p->x1, p->y1, p->x2, p->y2, p->tx, p->ty, p->mx, p->my, p->n);

       return EVAS_EVENT_FLAG_ON_HOLD;
   }
   ```

4. The mouse up event occurs after the mouse move events have been detected. The gesture layer checks the `mx` and `my` values internally. If `mx` and `my` have values, the `momentum_end()` callback function is called. Otherwise, `mx` and `my` have 0 values in the mouse up time, and the `momentum_abort()` callback function is called.

   ```
   static Evas_Event_Flags
   momentum_end(void *data, void *event_info)
   {
       Elm_Gesture_Momentum_Info *p = (Elm_Gesture_Momentum_Info *)event_info;
       printf("momentum ended x1,y1=<%d,%d> x2,y2=<%d,%d> tx,ty=<%u,%u> mx=<%d> my=<%d> n=>%u>\n",
              p->x1, p->y1, p->x2, p->y2, p->tx, p->ty, p->mx, p->my, p->n);

       return EVAS_EVENT_FLAG_ON_HOLD;
   }

   static Evas_Event_Flags
   momentum_abort(void *data, void *event_info)
   {
       printf("momentum abort\n");

       return EVAS_EVENT_FLAG_ON_HOLD;
   }
   ```

## Implementing Line Gestures

The line gesture is used for detecting mouse move events. The gesture layer checks each event to determine whether to draw a line.

You can configure some properties of the line gestures:

- Modify the minimum length and distance tolerance of a line.

  The default values are defined in the system policy. In Tizen, they are 40 for the minimum length, and 40 for the distance tolerance.

  ```
  /* Get or set the gesture layer line min length of an object */
  void elm_gesture_layer_line_min_length_set(Evas_Object *obj, int line_min_length);
  int elm_gesture_layer_line_min_length_get(const Evas_Object *obj);

  /* Get or set the gesture layer line distance tolerance of an object */
  void elm_gesture_layer_line_distance_tolerance_set(Evas_Object *obj, Evas_Coord line_distance_tolerance);
  Evas_Coord elm_gesture_layer_line_distance_tolerance_get(const Evas_Object *obj);
  ```

- Enable the continue mode to allow the line, flick, zoom, and rotate gesture to restart. The default value is `TRUE`.

  For example, when drawing a line, the finger can stop moving while the finger stays on the touch screen. This action makes the line end. After the finger continues to move, the line gesture restarts. When the continue mode is disabled, the finger has to be lifted off the touch screen to end a gesture, and then touch the screen again to start a new gesture.

  ```
  /* Get or set the gesture layer continue mode of an object */
  void elm_gesture_layer_continues_enable_set(Evas_Object *obj, Eina_Bool continues_enable);
  Eina_Bool elm_gesture_layer_continues_enable_get(const Evas_Object *obj);
  ```

The line gesture states are the same as in the [tap gesture](#implementing-tap-gestures).

To create a line gesture:

1. Use the `elm_gesture_layer_cb_set()` function to set callbacks to be notified about the change of the gesture state:

   ```
   elm_gesture_layer_cb_set(g, ELM_GESTURE_N_LINES, ELM_GESTURE_STATE_START,
                            line_start, NULL);
   elm_gesture_layer_cb_set(g, ELM_GESTURE_N_LINES, ELM_GESTURE_STATE_MOVE,
                            line_move, NULL);
   elm_gesture_layer_cb_set(g, ELM_GESTURE_N_LINES, ELM_GESTURE_STATE_END,
                            line_end, NULL);
   elm_gesture_layer_cb_set(g, ELM_GESTURE_N_LINES, ELM_GESTURE_STATE_ABORT,
                            line_abort, NULL);
   ```

2. The `line_start()` callback function is called when a mouse move event occurs after a mouse down event:

   ```
   static Evas_Event_Flags
   line_start(void *data, void *event_info)
   {
       Elm_Gesture_Line_Info *p = (Elm_Gesture_Line_Info *)event_info;
       printf("line started angle=<%lf> x1,y1=<%d,%d> x2,y2=<%d,%d> tx,ty=<%u,%u> n=<%u>\n",
              p->angle, p->momentum.x1, p->momentum.y1, p->momentum.x2, p->momentum.y2,
              p->momentum.tx, p->momentum.ty, p->momentum.n);

       return EVAS_EVENT_FLAG_ON_HOLD;
   }
   ```

   The `event_info` attribute contains the line information in the `Elm_Gesture_Line_Info` data structure:

   ```
   struct _Elm_Gesture_Line_Info {
       Elm_Gesture_Momentum_Info momentum; /* Line momentum info */
       double angle; /* Angle (direction) of the lines */
   };
   ```

3. The `line_move()` callback function is called on every mouse move event detected except when the line distance is outside the tolerance distance value.

   If the continue mode is enabled and the momentum value is 0, the callback is not called.

   ```
   static Evas_Event_Flags
   line_move(void *data, void *event_info)
   {
       Elm_Gesture_Line_Info *p = (Elm_Gesture_Line_Info *)event_info;
       printf("line move angle=<%lf> x1,y1=<%d,%d> x2,y2=<%d,%d> tx,ty=<%u,%u> n=<%u>\n",
              p->angle, p->momentum.x1, p->momentum.y1, p->momentum.x2, p->momentum.y2,
              p->momentum.tx, p->momentum.ty, p->momentum.n);

       return EVAS_EVENT_FLAG_ON_HOLD;
   }
   ```

4. The `line_end` callback function is called when a mouse up event occurs with a gesture that is longer than the line minimum length value. If the continue mode is enabled, the callback is called when the user stops drawing a line and the timing is started again. (Pause after the timing restart; either the end callback is called, or if the mouse up does not happen, the start callback is called again).

   ```
   static Evas_Event_Flags
   line_end(void *data, void *event_info)
   {
       Elm_Gesture_Line_Info *p = (Elm_Gesture_Line_Info *)event_info;
       printf("line end angle=<%lf> x1,y1=<%d,%d> x2,y2=<%d,%d> tx,ty=<%u,%u> n=<%u>,\n",
              p->angle, p->momentum.x1, p->momentum.y1, p->momentum.x2, p->momentum.y2,
              p->momentum.tx, p->momentum.ty, p->momentum.n);

       return EVAS_EVENT_FLAG_ON_HOLD;
   }
   ```

5. The `line_abort()` callback function is called when a mouse move event occurs and the geometry angle is outside the tolerance angle value and the line is shorter than the line minimum length value:

   ```
   static Evas_Event_Flags
   line_abort(void *data, void *event_info)
   {
       Elm_Gesture_Line_Info *p = (Elm_Gesture_Line_Info *)event_info;
       printf("line abort\n");

       return EVAS_EVENT_FLAG_ON_HOLD;
   }
   ```

## Implementing Flick Gestures

You can modify the flick time limit of the flick gesture.

The default value is defined in the system policy. In Tizen, it is 250 ms.

```
/* Get or set the gesture layer flick time limit (in milliseconds) of an object */
void elm_gesture_layer_flick_time_limit_ms_set(Evas_Object *obj, unsigned int flick_time_limit_ms);
unsigned int elm_gesture_layer_flick_time_limit_ms_get(const Evas_Object *obj);
```

The flick gesture states and the gesture info data structures are the same as in the [line gesture](#implementing-line-gestures).

To create a flick gesture:

1. Use the `elm_gesture_layer_cb_set()` function to set callbacks to be notified about the change of the gesture state:

   ```
   elm_gesture_layer_cb_set(g, ELM_GESTURE_N_FLICKS, ELM_GESTURE_STATE_START,
                            flick_start, NULL);
   elm_gesture_layer_cb_set(g, ELM_GESTURE_N_FLICKS, ELM_GESTURE_STATE_END,
                            flick_end, NULL);
   elm_gesture_layer_cb_set(g, ELM_GESTURE_N_FLICKS, ELM_GESTURE_STATE_ABORT,
                            flick_abort, NULL);
   ```

   The `flick_move()` callback function works the same way as the `line_move()` callback.

2. The `flick_start()` callback function is called when a mouse move event occurs after a mouse down event.

   After calling the `flick_start()` callback function, the gesture layer detects a line gesture on it. If so, it checks the flick time limit, and if the line event occurs within the limit, the `flick_end()` callback function is called. Otherwise, the `flick_abort()` callback function is called.

## Implementing Zoom Gestures

You can modify various zoom values, such as zoom step and distance tolerance.

The default values are defined in the system policy. In Tizen, they are:

- `zoom_step`: 0.0
- `zoom_finger_factor`: 1.0
- `zoom_wheel_factor`: 0.05
- `zoom_distance_tolerance`: 1.0

```
/* Get or set the step value for zoom action */
void elm_gesture_layer_zoom_step_set(Evas_Object *obj, double step);
double elm_gesture_layer_zoom_step_get(const Evas_Object *obj);

/* Get or set the gesture layer zoom distance tolerance of an object */
void elm_gesture_layer_zoom_distance_tolerance_set(Evas_Object *obj, Evas_Coord zoom_distance_tolerance);
Evas_Coord elm_gesture_layer_zoom_distance_tolerance_get(const Evas_Object *obj);

/* Get or set the gesture layer zoom wheel factor of an object */
void elm_gesture_layer_zoom_wheel_factor_set(Evas_Object *obj, double zoom_wheel_factor);
double elm_gesture_layer_zoom_wheel_factor_get(const Evas_Object *obj);

/* Get or set the gesture layer zoom finger factor of an object */
void elm_gesture_layer_zoom_finger_factor_set(Evas_Object *obj, double zoom_finger_factor);
double elm_gesture_layer_zoom_finger_factor_get(const Evas_Object *obj);
```

The zoom gesture states are the same as in the [tap gesture](#implementing-tap-gestures).

When using zoom gestures, pay attention to the following:

- The default zoom value is 1, when the zoom gesture starts. After every zoom gesture, the value is increased or decreased according to the internal calculation logic. The radius value is used for the calculation.
- If the mouse wheel events are sent with the **Ctrl** key on the gesture layer, the `zoom_start()` callback function is called with the default zoom value (1) and the zoom value (`zoom_finger_factor * zoom _wheel_factor`) is increased or decreased on every step to follow the wheel up or down.
- If a 2-finger down event points closer than the zoom distance tolerance value, the zoom gesture is not started. After the gap is bigger than the `zoom_distance_tolerance` value, the zoom gesture is started with the default value 1 and the event info gets a radius value and the gesture's momentum value.

To create a zoom gesture:

1. Use the `elm_gesture_layer_cb_set()` function to set callbacks to be notified about the change of the gesture state:

   ```
   elm_gesture_layer_cb_set(g, ELM_GESTURE_ZOOM, ELM_GESTURE_STATE_START,
                            zoom_start, NULL);
   elm_gesture_layer_cb_set(g, ELM_GESTURE_ZOOM, ELM_GESTURE_STATE_END,
                            zoom_end, NULL);
   elm_gesture_layer_cb_set(g, ELM_GESTURE_ZOOM, ELM_GESTURE_STATE_ABORT,
                            zoom_abort, NULL);
   elm_gesture_layer_cb_set(g, ELM_GESTURE_ZOOM, ELM_GESTURE_STATE_MOVE,
                            zoom_move, NULL);
   ```

2. When 2 mouse down events occur, the `zoom_start()` callback function is called with the zoom value (1), and the calculated radius and momentum for the current zoom gesture:

   ```
   static Evas_Event_Flags
   zoom_start(void *data, void *event_info)
   {
       Elm_Gesture_Zoom_Info *p = (Elm_Gesture_Zoom_Info *)event_info;
       printf("zoom started <%d,%d> zoom=<%f> radius=<%d> momentum=<%f>\n",
              p->x, p->y, p->zoom, p->radius, p->momentum);

       return EVAS_EVENT_FLAG_ON_HOLD;
   }
   ```

   The `event_info` attribute contains the zoom information in the `Elm_Gesture_Zoom_Info` data structure:

   ```
   struct _Elm_Gesture_Zoom_Info {
       Evas_Coord x, y; /* Zoom center point reported to the user */
       Evas_Coord radius; /* Radius between fingers reported to the user */
       double zoom; /* Zoom value: 1.0 means no zoom */
       double momentum; /* Zoom momentum: zoom growth per second (NOT YET SUPPORTED) */
   };
   ```

3. The `zoom_move()` callback function is called when the user moves 2 mouse down events, except that the gap of each mouse down point is smaller than the `zoom_distance_tolerance` value.

   The normal zoom gesture detecting logic:

   1. The gesture layer remembers the gap of each touched geometry.
   2. When the user moves each touched point, the gesture layer calculates the gap of each touched geometry for each move event.
   3. If the values (gap + `zoom_distance_tolerance`, gap – `zoom_distance_tolerance`) are bigger or smaller than the first calculated gap values, the gesture layer calls the `zoom_move()` callback function with the calculated result.

   ```
   static Evas_Event_Flags
   zoom_move(void *data, void *event_info)
   {
       Elm_Gesture_Zoom_Info *p = (Elm_Gesture_Zoom_Info *)event_info;
       printf("zoom move <%d,%d> zoom=<%f> radius=<%d> momentum=<%f>\n",
              p->x, p->y, p->zoom, p->radius, p->momentum);

       return EVAS_EVENT_FLAG_ON_HOLD;
   }
   ```

4. When the mouse up event occurs and the **Ctrl** key up signal is detected (when the user zooms using the mouse wheel and **Ctrl** key), the `zoom_end()` callback function is called:

   ```
   static Evas_Event_Flags
   zoom_end(void *data, void *event_info)
   {
       Elm_Gesture_Zoom_Info *p = (Elm_Gesture_Zoom_Info *)event_info;
       printf("zoom end <%d,%d> zoom=<%f> radius=<%d> momentum=<%f>\n",
              p->x, p->y, p->zoom, p->radius, p->momentum);

       return EVAS_EVENT_FLAG_ON_HOLD;
   }
   ```

5. When the down event count is bigger than 3, the `zoom_abort()` callback function is called.

   ```
   static Evas_Event_Flags
   zoom_abort(void *data, void *event_info EINA_UNUSED)
   {
       printf("zoom abort\n");

       return EVAS_EVENT_FLAG_ON_HOLD;
   }
   ```

## Implementing Rotate Gestures

You can modify the rotate step and tolerance.

The default values are defined in the system policy. In Tizen, they are 0.0 for the rotate step, and 0.0349 for the angular tolerance.

```
/* Get or set the step value for rotate action */
void elm_gesture_layer_rotate_step_set(Evas_Object *obj, double step);
double elm_gesture_layer_rotate_step_get(const Evas_Object *obj);

/* Get or set the gesture layer rotate angular tolerance of an object */
void elm_gesture_layer_rotate_angular_tolerance_set(Evas_Object *obj, double rotate_angular_tolerance);
double elm_gesture_layer_rotate_angular_tolerance_get(const Evas_Object *obj);
```

The rotate gesture states are the same as in the [tap gesture](#implementing-tap-gestures).

When using rotate gestures, pay attention to the following:

- When the gesture layer has detected 2 mouse down events, calculate the angle between the 2 points.

  Then the gesture layer detects every mouse move event for calculating the angle between the 2 points. If the angle value is bigger than the sum of the first calculated angle and `rotate_angular_tolerance`, the `rotate_move()` callback function is called with the result.

- If the step for the rotate gesture is set, the `rotate_move()` callback function is called on every step.

To create a rotate gesture:

1. Use the `elm_gesture_layer_cb_set()` function to set callbacks to be notified about the change of the gesture state:

   ```
   elm_gesture_layer_cb_set(g, ELM_GESTURE_ROTATE, ELM_GESTURE_STATE_START,
                            rotate_start, NULL);
   elm_gesture_layer_cb_set(g, ELM_GESTURE_ROTATE, ELM_GESTURE_STATE_END,
                            rotate_end, NULL);
   elm_gesture_layer_cb_set(g, ELM_GESTURE_ROTATE, ELM_GESTURE_STATE_ABORT,
                            rotate_abort, NULL);
   elm_gesture_layer_cb_set(g, ELM_GESTURE_ROTATE, ELM_GESTURE_STATE_MOVE,
                            rotate_move, NULL);
   ```

2. When 2 points of the gesture layer are tapped on, the `rotate_start()` callback function is called:

   ```
   static Evas_Event_Flags
   rotate_start(void *data, void *event_info)
   {
       Elm_Gesture_Rotate_Info *p = (Elm_Gesture_Rotate_Info *)event_info;
       printf("rotate started <%d,%d> base=<%f> angle=<%f> radius=<%d> momentum=<%f>\n",
              p->x, p->y, p->base_angle, p->angle, p->radius, p->momentum);

       return EVAS_EVENT_FLAG_ON_HOLD;
   }
   ```

   The `event_info` attribute contains the rotation information in the `Elm_Gesture_Rotate_Info` data structure:

   ```
   struct _Elm_Gesture_Rotate_Info {
       Evas_Coord x, y; /* Zoom center point reported to the user */
       Evas_Coord radius; /* Radius between fingers reported to the user */
       double base_angle; /* Holds the start angle */
       double angle; /* Rotation value: 0.0 means no rotation */
       double momentum; /* Rotation momentum: rotation done per second (NOT SUPPORTED) */
   };
   ```

3. The `rotate_move()` function is called for each detected point when a mouse move event occurs and its angle is bigger than the sum of the base angle and the angular tolerance:

   ```
   static Evas_Event_Flags
   rotate_move(void *data, void *event_info)
   {
       Elm_Gesture_Rotate_Info *p = (Elm_Gesture_Rotate_Info *)event_info;
       printf("rotate move <%d,%d> base=<%f> angle=<%f> radius=<%d> momentum=<%f>\n",
              p->x, p->y, p->base_angle, p->angle, p->radius, p->momentum);

       return EVAS_EVENT_FLAG_ON_HOLD;
   }
   ```

4. When a mouse up event occurs, the `rotate_end()` callback function is called:

   ```
   static Evas_Event_Flags
   rotate_end(void *data, void *event_info)
   {
       Elm_Gesture_Rotate_Info *p = (Elm_Gesture_Rotate_Info *)event_info;
       printf("rotate end <%d,%d> base=<%f> angle=<%f> radius=<%d> momentum=<%f>\n",
              p->x, p->y, p->base_angle, p->angle, p->radius, p->momentum);

       return EVAS_EVENT_FLAG_ON_HOLD;
   }
   ```

5. If a mouse down event count is higher than 3, the `rotate_abort()` callback function is called:

   ```
   static Evas_Event_Flags
   rotate_abort(void *data, void *event_info EINA_UNUSED)
   {
       printf("rotate abort\n");

       return EVAS_EVENT_FLAG_ON_HOLD;
   }
   ```

## Related Information
- Dependencies
   - Tizen 2.4 and Higher for Mobile
   - Tizen 2.3.1 and Higher for Wearable
