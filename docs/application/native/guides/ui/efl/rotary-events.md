# Managing Rotary Events

Rotary events are fired from a rotary device and delivered to a suitable target when the device is rotated clockwise or counter-clockwise.

This feature is supported in wearable applications only.

There are 2 ways to receive the rotary events:

- Rotary event handler
- Rotary object event callback

## Rotary Event Handler

Use the rotary event handler when you do not want to take care of an Evas object, or when the application is not implemented using an Evas object.

The handler is implemented like the [Ecore event](./event-types.md#ecore-events) in EFL:

1. Register the handler with the `eext_rotary_event_handler_add()` function and define the handler function.
2. When no longer needed, remove the handler with the `eext_rotary_event_handler_del()` function.

The rotary event handlers are treated "first come first served". This means that the first registered handler is called first when a rotary event occurs. If that handler returns `EINA_TRUE`, the next handler is called. The loop continues until a handler returns `EINA_FALSE` or all handlers have been called.

## Rotary Object Event Callback

Use the rotary object event callback when you want the EFL Extension API to handle the event delivery between objects. This means that EFL Extension manages callback and object lists, and decides which object's callback must be called when a rotary event occurs.

The callback is implemented as follows:

1. Register the callback with the `eext_rotary_object_event_callback_add()` function and define the callback.
2. When no longer needed, remove the callback with the `eext_rotary_object_event_callback_del()` function.

The callbacks are treated based on the callback priority. If you register multiple callbacks for the same object, the callback with the lowest priority number is called first. If that callback returns `EINA_TRUE`, the next higher priority number is called. The loop continues until a callback returns `EINA_FALSE` or all callbacks have been called.

The `eext_rotary_object_event_callback_add()` function registers the rotary event callback with a default priority number (0). To use another priority, define it with the `eext_rotary_object_event_callback_priority_add()` function.

### Activated Objects

The rotary event is delivered to a specific object called **activated object**. If no activated object exists, the event is not delivered anywhere. To set an object as the activated object (and automatically deactivate any previously activated object), use the `eext_rotary_object_event_activated_set()` function with the second parameter set to `EINA_TRUE`. The `EINA_FALSE` parameter value deactivates the object.

If the activated object has registered callbacks that all return `EINA_TRUE`, the rotary event is also delivered to the upper parents of the activated object, until a callback returns `EINA_FALSE` or the top parent object is reached.

When an object is activated or deactivated, a `rotary,activated` or `rotary,deactivated` signal is sent. You can [register callbacks for the signals](../../../api/wearable/latest/group__Evas__Smart__Object__Group.html) with the `evas_object_smart_callback_add()` function.

## Managing Rotary Events

To receive and manage rotary events:

- Implement a rotary event handler.

  In the following example, a rotary event causes a log entry to be printed based on the rotation direction.

  1. Create the application window and register a rotary event handler:

     ```
     static void
     create_base_gui(appdata_s *ad)
     {
         Evas_Object *win = NULL;

         /* Create the window */
         win = elm_win_util_standard_add(NULL, "extension circle sample");
         elm_win_autodel_set(win, EINA_TRUE);
         evas_object_smart_callback_add(win, "delete,request", win_delete_request_cb, NULL);

         /* Register the handler */
         eext_rotary_event_handler_add(_rotary_handler_cb, NULL);

         /* Show the window after the base GUI is set up */
         evas_object_show(win);
     }
     ```

  2. Define the handler function:

     ```
     Eina_Bool
     _rotary_handler_cb(void *data, Eext_Rotary_Event_Info *ev)
     {
         if (ev->direction == EEXT_ROTARY_DIRECTION_CLOCKWISE) {
             dlog_print(DLOG_DEBUG, LOG_TAG,
                        "Rotary device rotated in clockwise direction");
         } else {
             dlog_print(DLOG_DEBUG, LOG_TAG,
                        "Rotary device rotated in counter-clockwise direction");
         }

         return EINA_FALSE;
     }
     ```

  3. When no longer needed, remove the rotary event handler and release all resources:

     ```
     static void
     app_terminate(void *data)
     {
         /* Release all resources */

         /* Remove the handler */
         eext_rotary_event_handler_del(_rotary_handler_cb);
     }
     ```

- Implement a rotary event callback for a normal Evas object.

  In the following example, a rotary event causes the slider value to be adjusted accordingly.

  1. Create the application window and add a slider component to the window:

     ```
     static void
     create_base_gui(appdata_s *ad)
     {
         Evas_Object *win = NULL, *slider = NULL;

         /* Window */
         win = elm_win_util_standard_add(NULL, "extension sample");
         elm_win_autodel_set(win, EINA_TRUE);
         evas_object_smart_callback_add(win, "delete,request", win_delete_request_cb, NULL);

         /* Slider */
         slider = elm_slider_add(win);
         evas_object_size_hint_weight_set(slider, EVAS_HINT_EXPAND, EVAS_HINT_EXPAND);
         elm_slider_min_max_set(slider, 0, 50);
         elm_slider_step_set(slider, 1.0);
         evas_object_show(slider);
         elm_win_resize_object_add(win, slider);
     ```

  2. Register a rotary event callback and set the slider as the activated object:

     ```
         /* Register the callback */
         ext_rotary_object_event_callback_add(slider, _rotary_event_cb, NULL);
         /* Set the slider as activated */
         eext_rotary_object_event_activated_set(slider, EINA_TRUE);

         /* Show the window after the base GUI is set up */
         evas_object_show(win);
     }
     ```

  3. Define the callback function:

     ```
     Eina_Bool
     _rotary_event_cb(void *data, Evas_Object *obj, Eext_Rotary_Event_Info *ev)
     {
         Evas_Object *slider = obj;
         /* Retrieve the current slider value */
         int val = elm_slider_value_get(slider);

         /* Increase the slider value based on a clockwise rotary event */
         if (ev->direction == EEXT_ROTARY_DIRECTION_CLOCKWISE) {
             elm_slider_value_set(slider, val + 1);
         } else {
             /* Decrease the slider value based on a counter-clockwise rotary event */
             elm_slider_value_set(slider, val - 1);
         }

         return EINA_FALSE;
     }
     ```

- Implement a rotary event callback for an EFL Extension object.

  In the following example, a rotary event causes the slider value to be adjusted accordingly.

  1. Create the application window, add a conformant to the window, and add a circle surface and slider to the conformant:

     ```
     static void
     create_base_gui(appdata_s *ad)
     {
         Evas_Object *win = NULL;
         Evas_Object *conform = NULL;
         Eext_Circle_Surface *sur = NULL;

         /* Window */
         win = elm_win_util_standard_add(NULL, "extension circle sample");
         elm_win_autodel_set(win, EINA_TRUE);
         evas_object_smart_callback_add(win, "delete,request", win_delete_request_cb, NULL);

         /* Conformant */
         conform = elm_conformant_add(win);
         elm_win_indicator_mode_set(win, ELM_WIN_INDICATOR_SHOW);
         elm_win_indicator_opacity_set(win, ELM_WIN_INDICATOR_OPAQUE);
         evas_object_size_hint_weight_set(conform, EVAS_HINT_EXPAND, EVAS_HINT_EXPAND);
         elm_win_resize_object_add(win, conform);
         evas_object_show(conform);

         /* Surface */
         sur = eext_circle_surface_conformant_add(conform);

         /* Slider */
         slider = eext_circle_object_slider_add(conform, sur);
         eext_circle_object_value_min_max_set(slider, 0.0, 30.0);
         eext_circle_object_value_set(slider, 0.0);
     ```

  2. Set the slider as the activated object, and define the slider step.

     The slider step defines how much a rotary event increases or decreases the slider value.

		> **Note**  
		> Since the EFL Extension API is used to create the slider component, the rotary event callbacks are registered internally and automatically change the slider value based on the slider step. To receive a rotary event for an EFL Extension object, you only need to set the object as activated.

     ```
         /* Set the slider as activated */
         /* Its value increases or decreases based on rotary events */
         eext_rotary_object_event_activated_set(slider, EINA_TRUE);
         /* Each rotary event increases or decreases the slider value by 1 */
         eext_circle_object_slider_step_set(slider, 1.0);

         /* Show the window after the base GUI is set up */
         evas_object_show(win);
     }
     ```

## Related Information
- Dependencies     
  - Tizen 2.3.1 and Higher for Wearable
