# Event Types

EFL provides various event types that you can use to monitor and react to user interactions and system events in the UI.

## Ecore Events

Ecore events are used for low-level handling of events, such as key presses, network connections, and communication with sub-processes. For shortcuts, the low-level handling of key presses is particularly useful: instead of adding a signal handler to a specific graphical element, you can add one globally to guarantee that no matter which UI component is currently receiving events, the shortcut is caught correctly.

Ecore events can also be used to implement new graphical back-ends. However, they are low-level and not useful for most applications.

In addition to using predefined Ecore events, you can create your own events with the `ecore_event_type_new()` function. The function generates a new unique identifier, which you can use as the event type parameter when managing your events and event handlers.

### Shortcut Events

The following Ecore events are available for shortcuts. The event callbacks receive additional data through a `void*` object, whose type depends on the received event.

- `ECORE_EVENT_KEY_DOWN` and `ECORE_EVENT_KEY_UP`:

  ```
  typedef struct _Ecore_Event_Key Ecore_Event_Key;

  struct _Ecore_Event_Key {
      const char *keyname;
      const char *key;
      const char *string;
      const char *compose;
      Ecore_Window window;
      Ecore_Window root_window;
      Ecore_Window event_window;

      unsigned int timestamp;
      unsigned int modifiers;

      int same_screen;
  };
  ```

- `ECORE_EVENT_MOUSE_BUTTON_DOWN` and `ECORE_EVENT_MOUSE_BUTTON_UP`:

  ```
  typedef struct _Ecore_Event_Mouse_Button Ecore_Event_Mouse_Button;

  struct _Ecore_Event_Mouse_Button {
      Ecore_Window window;
      Ecore_Window root_window;
      Ecore_Window event_window;

      unsigned int timestamp;
      unsigned int modifiers;
      unsigned int buttons;
      unsigned int double_click;
      unsigned int triple_click;
      int same_screen;

      int x;
      int y;
      struct {
          int x;
          int y;
      } root;

      struct {
          /*
             0 if normal mouse, 1+ for other mouse-devices
             (such as multi-touch - other fingers)
          */
          int device;
          /*
             Radius of press point - radius_x and radius_y
             if it is an ellipse (radius is the average of the 2)
          */
          double radius;
          double radius_x;
          double radius_y;
          /* Pressure - 1.0 == normal, > 1.0 == more, 0.0 == none */
          double pressure;
          /* Angle relative to perpendicular (0.0 == perpendicular), in degrees */
          double angle;
          /* Same as x, y, root.x, root.y, but with sub-pixel precision, if available */
          double x;
          double y;
          struct {
              double x;
              double y;
          } root;
      } multi;
  };
  ```

- `ECORE_EVENT_MOUSE_MOVE` and `ECORE_EVENT_MOUSE_WHEEL`:

  ```
  typedef struct _Ecore_Event_Mouse_Wheel Ecore_Event_Mouse_Wheel;

  struct _Ecore_Event_Mouse_Wheel {
      Ecore_Window window;
      Ecore_Window root_window;
      Ecore_Window event_window;

      unsigned int timestamp;
      unsigned int modifiers;

      int same_screen;
      int direction;
      int z;

      int x;
      int y;
      struct {
          int x;
          int y;
      } root;
  };
  ```

- `ECORE_EVENT_MOUSE_IN` and `ECORE_EVENT_MOUSE_OUT`:

  ```
  typedef struct _Ecore_Event_Mouse_Move Ecore_Event_Mouse_Move;

  struct _Ecore_Event_Mouse_Move {
      Ecore_Window window;
      Ecore_Window root_window;
      Ecore_Window event_window;

      unsigned int timestamp;
      unsigned int modifiers;

      int same_screen;

      int x;
      int y;
      struct {
          int x;
          int y;
      } root;

      struct {
          /*
             0 if normal mouse, 1+ for other mouse-devices
             (such as multi-touch - other fingers)
          */
          int device;
          /*
             Radius of press point - radius_x and radius_y
             if it is an ellipse (radius is the average of the 2)
          */
          double radius;
          double radius_x;
          double radius_y;
          /* Pressure - 1.0 == normal, > 1.0 == more, 0.0 == none */
          double pressure;
          /* Angle relative to perpendicular (0.0 == perpendicular), in degrees */
          double angle;
          /* Same as x, y, root.x, root.y, but with sub-pixel precision, if available */
          double x;
          double y;
          struct {
              double x;
              double y;
          } root;
      } multi;
  };
  ```

### Managing Ecore Event Handlers

To manage Ecore event handlers:

1. To add an Ecore event handler, register a callback for a specific event with the `ecore_event_handler_add()` function.

   The function takes as parameters the event type (such as `ECORE_EVENT_KEY_DOWN` for key presses), callback function, and additional data delivered to the callback. The function returns an event handler pointer, which you can use to remove the handler later.

2. Define the `Ecore_Event_Handler_Cb()` callback function.

   The function takes as parameters the additional data defined in the `ecore_event_handler_add()` function parameters, the event type, and the event object (`Ecore_Event_Key`, `Ecore_Event_Mouse_Button`, `Ecore_Event_Mouse_Wheel`, or `Ecore_Event_Mouse_Move`). The function returns `ECORE_CALLBACK_PASS_ON` to allow other callbacks for that event be called, or `ECORE_CALLBACK_DONE` to not call them.

3. When no longer needed, remove the event handler with the `ecore_event_handler_del()` function, using the event handler pointer as a parameter.

   The following example shows how you can set a global variable to `EINA_TRUE` when the **Ctrl** key is pressed:

   ```
   Eina_Bool ctrl_pressed = EINA_FALSE;

   static Eina_Bool
   _key_down_cb(void *data __UNUSED__, int type __UNUSED__, void *ev)
   {
       /*
          Callback is used with the ECORE_EVENT_KEY_DOWN signal: the
          parameter "void *ev" is therefore of the actual type Ecore_Event_Key
          Following renders its fields accessible
       */
       Ecore_Event_Key *event = ev;

       /* Test whether the key that is pressed is Ctrl */
       if (!strcmp("Control_L", event->key)) {
           /* If it is, store that piece of information */
           ctrl_pressed = EINA_TRUE;
       }

       /* Let the event continue to other callbacks which have not been called yet */
       return ECORE_CALLBACK_PASS_ON;
   }

   ecore_event_handler_add(ECORE_EVENT_KEY_DOWN, _key_down_cb, NULL);
   ```

### Sending Ecore Events to the Main Loop

You can send Ecore events to the main loop yourself to handle actions of various origins through the same codepath. This is a thread-safe operation.

To send an event, use the `ecore_event_add()` function. The function takes as parameters the event type (such as `ECORE_EVENT_KEY_DOWN` for key presses), additional data delivered to the callback, the `Ecore_End_Cb()` function used to free the additional data after it is delivered to the callback function, and the pointer to additional data delivered to the free function. The free function and the pointer to its additional data are optional; use `NULL` if you do not need them.

## Edje Events

Edje [themes](./component-custom.md#style-theme-and-edc) have program blocks in the EDC file, which are triggered upon the reception of a signal that can execute actions, such as changing the state of an Edje part and running another program.

### Managing a Single Signal Emitter

The following example shows a program block of an Edje file. The program is called `"change_color"`, and it is triggered on mouse clicks on the current part. It emits a `"got.a.click"` signal where the source is set to `"color_changer"`.

```
program {
   name: "change_color";
   signal: "mouse,clicked,*";
   source: "*";
   action: SIGNAL_EMIT "got.a.click" "color_changer";
}
```

To catch the emitted signal in the application code, use either the `edje_object_signal_callback_add()` or `elm_object_signal_callback_add()` function. Their only difference is that the previous one operates on an Edje object and the latter one on an Elementary object. Unless you do not use the Elementary library at all, use the Elementary variant.

Both the functions take as parameters the object emitting the signal, the signal name, the signal source, the `Edje_Signal_Cb()` callback function called when the signal name and source match, and additional data delivered to the callback. For the signal name and source, `"*"` acts as a wildcard. The additional data is optional; use `NULL` if you do not need it.

The callback function takes as parameters the additional data defined in the `edje_object_signal_callback_add()` or `elm_object_signal_callback_add()` function parameters, the object emitting the signal, the signal name, and the signal source.

### Managing Multiple Signal Emitters in Layouts

Most of the time, Edje and Elementary are used together. In particular, you can define a group in Edje and use it as a [layout](./container-layout.md) (containing several parts) in Elementary. The layouts enable you to perform theming and object placement in Edje while benefiting from the higher-level functions of Elementary.

Since the layout contains multiple parts, you cannot use the `elm_object_signal_callback_add()` and `edje_object_signal_callback_add()` functions, as they require a single emitter object. The solution is to use the dedicated `elm_layout_signal_callback_add()` function.

The `elm_layout_signal_callback_add()` function works similarly as the `elm_object_signal_callback_add()` and `edje_object_signal_callback_add()` functions. The only difference is the type of the object in the first parameter. For `elm_layout_signal_callback_add()`, it is a pointer to an `Evas_Object`, which is obtained through the `elm_layout_add()` function. For more information, see [Layout](./container-layout.md).

## Evas Events

Evas events happen on a canvas as a whole. These events are too low-level for writing applications, and are mostly used when writing the graphical toolkit itself.

### Managing Evas Event Handlers

Register and remove callback functions with the `evas_event_callback_add()` and `evas_event_callback_add()` functions. The `evas_event_callback_add()` function takes as parameters the Evas canvas on which the event happens (to obtain the canvas, use the `Evas_Object` through the `evas_object_evas_get()` function), the event type, the `Evas_Event_Cb` callback function, and the pointer to the additional data delivered to the callback. The additional data is optional; use `NULL` if you do not need it.

The callback function takes as parameters the additional data defined in the `evas_event_callback_add()` function parameters, the canvas where the event happened, and the event info data, which depends on the object type and the event at play.

```
void
evas_event_callback_add(Evas *e, Evas_Callback_Type type,
                        Evas_Event_Cb func, const void *data);

void
(* Evas_Event_Cb)(void *data, Evas *e, void *event_info);
```

### Evas Event Types

The following table lists the available Evas event types.

**Table: Evas event types**

| Event type                              | Description                              |
|---------------------------------------|----------------------------------------|
| `EVAS_CALLBACK_RENDER_FLUSH_PRE`        | Rendering on the canvas is about to be updated. |
| `EVAS_CALLBACK_RENDER_FLUSH_POST`       | Rendering on the canvas is updated.      |
| `EVAS_CALLBACK_CANVAS_FOCUS_IN`         | Canvas receives focus.                   |
| `EVAS_CALLBACK_CANVAS_FOCUS_OUT`        | Canvas loses focus.                      |
| `EVAS_CALLBACK_CANVAS_OBJECT_FOCUS_IN`  | Any object on the canvas receives focus.<br> Instead of this event type, use the `EVAS_CALLBACK_FOCUS_IN` type with the `evas_object_event_callback_add()` function. |
| `EVAS_CALLBACK_CANVAS_OBJECT_FOCUS_OUT` | Any object on the canvas loses focus.<br> Instead of this event type, use the `EVAS_CALLBACK_FOCUS_OUT` type with the `evas_object_event_callback_add()` function. |
| `EVAS_CALLBACK_RENDER_PRE`              | Rendering on the canvas starts.          |
| `EVAS_CALLBACK_RENDER_POST`             | Rendering on the canvas finishes.        |

## Evas Object Events

Each Evas object on a specific Evas canvas can be manipulated independently. Each object can send events, which you can handle by registering callback functions for them. The events all relate to single objects, not the whole canvas.

### Managing Evas Object Event Handlers

Register and remove callback functions with the `evas_object_event_callback_add()` and `evas_object_event_callback_del()` functions. The `evas_object_event_callback_add()` function takes as parameters the `Evas_Object_Event_Cb` callback function and the pointer to the additional data delivered to the callback.

The callback function takes as parameters the additional data defined in the `evas_event_callback_add()` function parameters, the canvas where the event happened, the object to which the event happened, and the event info data, which depends on the object type and the event at play.

```
void
evas_object_event_callback_add(Evas_Object *obj, Evas_Callback_Type type,
                               Evas_Object_Event_Cb func, const void *data);

void
(* Evas_Object_Event_Cb)(void *data, Evas *e, Evas_Object *obj, void *event_info);
```

### Evas Object Event Types

The following table lists the available Evas object event types.

**Table: Evas object event types**

| Event type                         | Description                              | `event_info`             |
|----------------------------------|----------------------------------------|------------------------|
| `EVAS_CALLBACK_MOUSE_IN`           | Pointer got over an object (with no other object between the 2).         This takes place no matter how the pointer becomes directly above the object. | `Evas_Event_Mouse_In`    |
| `EVAS_CALLBACK_MOUSE_OUT`          | Triggered similarly to the `EVAS_CALLBACK_MOUSE_IN` event, but when the pointer goes outside the object area. | `Evas_Event_Mouse_Out`   |
| `EVAS_CALLBACK_MOUSE_DOWN`         | Mouse button is pressed while the object is receiving events (either because the pointer is on top of the object or because the object had focus). | `Evas_Event_Mouse_Down`  |
| `EVAS_CALLBACK_MOUSE_UP`           | Triggered similarly to the `EVAS_CALLBACK_MOUSE_DOWN` event. | `Evas_Event_Mouse_Up`    |
| `EVAS_CALLBACK_MOUSE_MOVE`         | Triggered similarly to the `EVAS_CALLBACK_MOUSE_DOWN` event. | `Evas_Event_Mouse_Move`  |
| `EVAS_CALLBACK_MOUSE_WHEEL`        | Triggered similarly to the `EVAS_CALLBACK_MOUSE_DOWN` event. | `Evas_Event_Mouse_Wheel` |
| `EVAS_CALLBACK_MULTI_DOWN`         | Triggered similarly to the `EVAS_CALLBACK_MOUSE_DOWN` event. | `Evas_Event_Multi_Down`  |
| `EVAS_CALLBACK_MULTI_UP`           | Triggered similarly to the `EVAS_CALLBACK_MOUSE_DOWN` event. | `Evas_Event_Multi_Up`    |
| `EVAS_CALLBACK_MULTI_MOVE`         | Triggered similarly to the `EVAS_CALLBACK_MOUSE_DOWN` event. | `Evas_Event_Multi_Move`  |
| `EVAS_CALLBACK_KEY_DOWN`           | Triggered similarly to the `EVAS_CALLBACK_MOUSE_DOWN` event. | `Evas_Event_Key_Down`    |
| `EVAS_CALLBACK_KEY_UP`             | Triggered similarly to the `EVAS_CALLBACK_MOUSE_DOWN` event. | `Evas_Event_Key_Up`      |
| `EVAS_CALLBACK_FOCUS_IN`           | Object gained focus.                     | `Evas_Event_Mouse_In`    |
| `EVAS_CALLBACK_FOCUS_OUT`          | Object lost focus.                       | `Evas_Event_Mouse_In`    |
| `EVAS_CALLBACK_SHOW`               | Object is shown by a call to the `evas_object_show()` function. | `NULL`                   |
| `EVAS_CALLBACK_HIDE`               | Object is hidden by a call to the `evas_object_hide()` function. | `NULL`                   |
| `EVAS_CALLBACK_MOVE`               | Object origin was moved (origin is the top-left corner at the creation time of the object). | `NULL`                   |
| `EVAS_CALLBACK_RESIZE`             | Object is resized.                       | `NULL`                   |
| `EVAS_CALLBACK_RESTACK`            | Object is re-stacked by the `evas_object_stack_below()` or `evas_object_stack_above()` function, or other events. | `NULL`                   |
| `EVAS_CALLBACK_DEL`                | Object is deleted.                       | `NULL`                   |
| `EVAS_CALLBACK_FREE`               | For internal use only.<br> Do not use (the object resources are about to be freed). | `NULL`                   |
| `EVAS_CALLBACK_HOLD`               | For internal use only.                   | `Evas_Event_Hold`        |
| `EVAS_CALLBACK_CHANGED_SIZE_HINTS` | Object size hints changed.               | `NULL`                   |
| `EVAS_CALLBACK_IMAGE_PRELOADED`    | Image preloaded through the `evas_object_image_preload()` function is loaded. | `NULL`                   |
| `EVAS_CALLBACK_IMAGE_UNLOADED`     | Image data is unloaded.                  | `NULL`                   |

The following example shows a scenario with an image and an `EVAS_CALLBACK_MOUSE_UP` event callback, where the callback is used to print out the location where a touch up event occurs over the image. The callback uses the `EVAS_EVENT_FLAG_ON_HOLD` event flag to check whether the event is usable: if the `EVAS_EVENT_FLAG_ON_HOLD` event flag is set, the event is on hold and must not be used to perform any actions.

```
static void
_mouse_up(void *data EINA_UNUSED, Evas *e EINA_UNUSED, Evas_Object *o EINA_UNUSED,
          void *event_info)
{
    Evas_Event_Mouse_Up *ev = event_info;

    if (ev->button != 1) return;
    if (ev->event_flags & EVAS_EVENT_FLAG_ON_HOLD) return;

    printf("MOUSE: up @ %4i %4i\n", ev->canvas.x, ev->canvas.y);
}

static void
_add_mouse_up(Evas_Object *window)
{
    Evas_Object *image;

    image = elm_image_add(win);
    evas_object_event_callback_add(image, EVAS_CALLBACK_MOUSE_UP, _mouse_up, NULL);
    evas_object_show(image);
}
```

## Evas Smart Object Events

Evas smart object events are the most widely-used type of events in graphical applications, since they are used for signals, such as `"clicked"`, `"clicked,double"` (double-click), and `"pressed"`. They are identified by strings, and each smart object is able to define its own events (although the names follow conventions).

### Managing Evas Smart Object Event Handlers

1. To add an Evas smart object event handler, register a callback for a specific event to an object with the `evas_object_smart_callback_add()` function.

   The function takes as parameters the object to which the callback is added, the event name, the callback function, and additional data delivered to the callback. The additional data is optional; use `NULL` if you do not need it.

2. Define the `Evas_Smart_Cb()` callback function.

   The function takes as parameters the additional data defined in the `evas_object_smart_callback_add()` function parameters, the object to which the event happened, and the event info data, which depends on the object type and the event at play.

   If some of the parameters are not used by the callback function, the compiler can raise the "unused parameter" warning. To avoid it, annotate the parameter with the `__UNUSED__` macro, which is a compiler-independent way to let the compiler know that the parameter is unused willingly, rather than by a mistake:

   ```
   void cb(void *data __UNUSED__, Evas_Object *obj, void *event_info __UNUSED__);
   ```

3. When no longer needed, remove the event handler with the `evas_object_smart_callback_del()` function.

   The function removes the first match for the given event and callback, and returns the data pointer that was used in the corresponding call to the `evas_object_smart_callback_add()` function.

For a specific object and event, callbacks are called in the order they have been registered. The `evas_object_smart_callback_add()` function does not execute any special processing, if it is called several times with the same callback function or data. Callbacks are called as many times as they have been added and in the order they have been added.

### Example

The following example shows a button with a callback for the `clicked` signal. Clicking the button removes the callback:

```
static void
_button_clicked(void *data __UNUSED__, Evas_Object *obj, void *event_info __UNUSED__)
{
    fprintf(stdout, "Button clicked.\n");
    fflush(stdout);
    evas_object_smart_callback_del(obj, "clicked", _button_clicked);
}

static void
_add_button(Evas_Object *window)
{
    Evas_Object *button;

    button = elm_button_add(window);
    elm_object_text_set(button, "Click Me!");
    evas_object_smart_callback_add(button, "clicked", _button_clicked, NULL);

    evas_object_show(button);
}
```

> **Note**
>
> Except as noted, this content is licensed under [LGPLv2.1+](http://opensource.org/licenses/LGPL-2.1).

## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
