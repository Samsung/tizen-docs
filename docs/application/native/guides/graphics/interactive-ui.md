# Interactive UI


The 2D canvas in Tizen (the `Evas object`) has been designed to draw scenes optimally. This means that when drawing a new frame, it does not always read the `Evas_Object` data. This mechanism can cause a problem for a 3D scene, because the 3D scene is updated by the external module, such as the GPU, and `Evas` does not know whether the 3D scene is updated.

To solve the problem, GLView provides the `elm_glview_changed_set()` function to notify Evas that the 3D scene must be updated in the next frame. The `draw_glview()` callback is then invoked while Evas renders the next frame. The application must call the `elm_glview_changed_set()` function whenever necessary:

- [Touch Event Handling](#touch) updates the scene by touch event, and you have to invoke the `elm_glview_changed_set()` function.
- [Automatic Update](#update) must be enabled to be used, and also requires calling the `elm_glview_changed_set()` function.

<a name="touch"></a>
## Touch Event Handling

To handle touch events in Tizen, you must connect the event callback functions with `Evas_object`. The functions are registered by the `evas_object_event_callback_add()` function for a set of specific events which are already defined in EFL. To learn more about EFL event handling, see the [Event Handling](../ui/efl/event-handling.md).

The following examples show how to register callback functions for handling touch information and rotating a cube object:

1. Registering callback functions

   The following code shows how to add callback functions to `Evas_object`. The parameters, `EVAS_CALLBACK_MOUSE_DOWN`, `EVAS_CALLBACK_MOUSE_UP`, and `EVAS_CALLBACK_MOUSE_MOVE`, represent the specific events for which callbacks must be called. These events are defined in `Evas_Callback_Type`.

   ```
   static Evas_Object*
   add_glview(Evas_Object *parent, appdata_s *ad)
   {
       Evas_Object *glview;

       /* Create and initialize GLView */
       glview = elm_glview_add(parent);

       /* Initialize elm_GLView and set the rendering callback functions */

       evas_object_event_callback_add(glview, EVAS_CALLBACK_MOUSE_DOWN, mouse_down_cb, ad);
       evas_object_event_callback_add(glview, EVAS_CALLBACK_MOUSE_UP, mouse_up_cb, ad);
       evas_object_event_callback_add(glview, EVAS_CALLBACK_MOUSE_MOVE, mouse_move_cb, ad);
   }
   ```

2. Handling touch events in callback functions

   The following code shows how to define the registered callback functions:

   ```
   static void
   mouse_down_cb(void *data, Evas *e, Evas_Object *obj, void *event_info)
   {
       appdata_s *ad = (appdata_s *)data;
       ad->mouse_down = EINA_TRUE;
       elm_glview_changed_set(obj);
   }

   static void
   mouse_move_cb(void *data, Evas *e, Evas_Object *obj, void *event_info)
   {
       Evas_Event_Mouse_Move *ev;
       ev = (Evas_Event_Mouse_Move *)event_info;
       appdata_s *ad = (appdata_s *)data;

       float dx = 0, dy = 0;

       if (ad->mouse_down) {
           dx = ev->cur.canvas.x - ev->prev.canvas.x;
           dy = ev->cur.canvas.y - ev->prev.canvas.y;
           ad->xangle += dy;
           ad->yangle += dx;
       }
       elm_glview_changed_set(obj);
   }

   static void
   mouse_up_cb(void *data, Evas *e, Evas_Object *obj, void *event_info)
   {
       appdata_s *ad = (appdata_s *)data;

       ad->mouse_down = EINA_FALSE;
       elm_glview_changed_set(obj);
   }
   ```

   Each callback function has the `void *event_info` parameter in their signature. However, the parameter works differently depending on the registered events. In the `mouse_move_cb()` function, the void pointer `event_info` is cast to the `Evas_Event_Mouse_Move` type, which is associated with `EVAS_CALLBACK_MOUSE_MOVE`. Therefore, you can get the information about the screen point when the user touches the screen. Using this information, the angles, `xangle` and `yangle`, are accumulated and the accumulated data are used for calculating the rotation matrix in the `draw_glview()` callback functions.

   Notice the `elm_glview_changed_set()` function. It notifies EFL that there has been a change in GLView. Then, the main loop of EFL invokes the rendering callback functions in GLView.

<a name="update"></a>
## Automatic Update

In order to allow GLView to update scenes continuously, you must trigger the GLView rendering at every frame. The `Ecore_Animator` represents a method to enable the automatic update. It invokes the registered callback at every `N` seconds where `N` is the frametime interval set by the `ecore_animator_frametime_set()` function. Then you can call the `elm_glview_changed_set()` function at the animator's callback to keep the 3D scene being rendered while the animator works.

The `Ecore_Animator` instance can be replaced by `Ecore_Timer`, which produces the same result as `Ecore_Animator`. However, since `Ecore_Animator` provides more advantages in maintaining the update loop, preferably use `Ecore_Animator` instead of `Ecore_Timer`. For more information, see the Ecore Animator API (in [mobile](../../api/mobile/latest/group__Ecore__Animator__Group.html) and [wearable](../../api/wearable/latest/group__Ecore__Animator__Group.html) applications).

The following example adds and deletes an animator with the callback function:

1. Adding `Ecore_Animator`

    ```
    /*
       Add an animator so that the app regularly
       triggers updates of the GLView using elm_glview_changed_set()
    */

    /*
       NOTE: If you delete OpenGL ES, the animator keeps running trying to access it
       To prevent this, delete the animator with ecore_animator_del()
    */

    Ecore_Animator *ani = ecore_animator_add(anim_cb, glview);
    evas_object_data_set(glview, "ani", ani);
    evas_object_event_callback_add(glview, EVAS_CALLBACK_DEL, del_anim_cb, ad);
    ```

2. Setting up callback functions

   ```
   static void
   del_anim_cb(void *data, Evas *evas, Evas_Object *obj, void *event_info)
   {
       Ecore_Animator *ani = (Ecore_Animator *)evas_object_data_get(obj, "ani");
       ecore_animator_del(ani);
   }

   static Eina_Bool
   anim_cb(void *data)
   {
       elm_glview_changed_set((Evas_Object *)data);

       return EINA_TRUE;
   }
   ```

   The animator callback function is also triggered when the display is off. Use the `ecore_animator_freeze()` and `ecore_animator_thaw()` functions in the `app_pause_cb()` and `app_resume_cb()` callbacks for power saving.

## Integrating 3D Scene and 2D UI Components

GLView can be used together with Elementary UI components. The following example creates a GLView and Elementary button component together in a simple box container. It is also possible to support interactions between 2D components and 3D scene.

```
/* Create the box */
Evas_Object *box = elm_box_add(parent);

/* Set the box to vertical */
elm_box_horizontal_set(box, EINA_FALSE);
/* Box expands when its contents need more space */
evas_object_size_hint_weight_set(box, EVAS_HINT_EXPAND, EVAS_HINT_EXPAND);
/* Box fills the available space */
evas_object_size_hint_align_set(box, EVAS_HINT_FILL, EVAS_HINT_FILL);

/* Add glview to the box container */
ad->glview = add_glview(box, ad);
elm_box_pack_end(box, ad->glview);

/* Add button to the box container */
Evas_Object *button = elm_button_add(box);
evas_object_size_hint_weight_set(button, EVAS_HINT_EXPAND, EVAS_HINT_FILL);
evas_object_size_hint_align_set(button, EVAS_HINT_FILL, 1);
elm_object_text_set(button, "Reset Animation");
evas_object_smart_callback_add(button, "clicked", clicked_cb, ad);
evas_object_show(button);
elm_box_pack_end(box, button);

static void
clicked_cb(void *user_data, Evas_Object *obj, void *event_info)
{
    appdata_s *ad = (appdata_s *)user_data;

    /*
       It is possible to change the 3D scene
       For example, start animator to rotate the cube
    */
    if (!ad->reset_anim) {
        ad->reset_anim = EINA_TRUE;

        /* Setting animation angle for 0.75 seconds */
        ad->tic_xangle = (ad->xangle - 45.0f) / 45.0f;
        ad->tic_yangle = (ad->yangle - 45.0f) / 45.0f;

        /*
           Add animator which calls elm_glview_changed_set() per frame
           This rotates the object tic_x(y)angle along X(Y) axis
           until object reaches the initial angle
        */
        ad->ani = ecore_animator_add(anim_cb, ad);
        evas_object_event_callback_add(ad->glview, EVAS_CALLBACK_DEL, del_anim, ad);
    }
}
```

## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
