# Web View


The Web view features include accessing Web pages and Web content in your application.

The WebView API implements the EFL WebKit (EWK), which covers various features for Web browsing, such as loading and displaying Web pages and navigating through the browsing history. The EFL APIs (in [mobile](../../api/mobile/latest/group__EFL.html) and [wearable](../../api/wearable/latest/group__EFL.html) applications), such as `evas_*`, `elm_*`, and `eina_*`, are used to build up a complete application supporting Web browsing.

Use the Web features to create a simple Web browser:

1. [Create a window object](#window), and [set the window layout and view](#layout).

   Later, you can use various helper functions to [find the created window](#helper).

2. [Show the window and set the focus](#show).

   You can [handle key and mouse events](#keymouse) in the window.

3. When no longer needed, [terminate the window](#finalize).

## Prerequisites

To enable your application to use the Web view functionality:

1. To use the Web API (in [mobile](../../api/mobile/latest/group__CAPI__WEB__FRAMEWORK.html) and [wearable](../../api/wearable/latest/group__CAPI__WEB__FRAMEWORK.html) applications), the application has to request permission by adding the following privileges to the `tizen-manifest.xml` file:

   ```
   <privileges>
      <!--To launch another application conditionally-->
      <privilege>http://tizen.org/privilege/appmanager.launch</privilege>
      <!--To create, update, and delete content-->
      <privilege>http://tizen.org/privilege/content.write</privilege>
      <!--To use the Internet connection-->
      <privilege>http://tizen.org/privilege/internet</privilege>
      <!--To provide user notifications, such as messages and badges-->
      <privilege>http://tizen.org/privilege/notification</privilege>
      <!--To use the user location data-->
      <privilege>http://tizen.org/privilege/location</privilege>
      <!--To manage the device cameras to preview and capture pictures-->
      <privilege>http://tizen.org/privilege/camera</privilege>
      <!--To access, read, and write to the external storage-->
      <privilege>http://tizen.org/privilege/externalstorage</privilege>
      <!--To access the display-->
      <privilege>http://tizen.org/privilege/display</privilege>
      <!--To create a network connection-->
      <privilege>http://tizen.org/privilege/network.get</privilege>
   </privileges>
   ```

2. To use the functions and data types of the WebView API (in [mobile](../../api/mobile/latest/group__WEBVIEW.html) and [wearable](../../api/wearable/latest/group__WEBVIEW.html) applications), include the `<EWebKit.h>` header file in your application:

    ```
    #include <Ecore.h>
    #include <Ecore_Evas.h>
    #include <Ecore_Getopt.h>
    #include <Eet.h>
    #include <Eina.h>
    #include <Elementary.h>
    #include <Evas.h>
    #include <EWebKit.h>
    #include <app.h>
    ```

   The sample browser created in this guide also requires the `<Ecore.h>`, `<Ecore_Evas.h>`, `<Ecore_Getopt.h>`, `<Eet.h>`, `<Eina.h>`, `<Elementary.h>`, `<Evas.h>`, and `<app.h>` header files.

3. The sample browser uses several Evas objects to build the browser UI. To easily manage the UI elements, store the browser window data (including the `Evas_Object` instances) in the `Browser_window` data structure:

    ```
    struct _Browser_Window {
        Evas_Object *elm_window;
        Evas_Object *ewk_view;
        Evas_Object *back_button;
        Evas_Object *forward_button;
    };
    typedef struct _Browser_Window Browser_Window;

    EXPORT_API int
    main(int argc, char *argv[])
    {
        int args = 1;
        Browser_Window window;
        memset(&window, 0x00, sizeof(Browser_Window));

        ui_app_lifecycle_callback_s ops;
        memset(&ops, 0x00, sizeof(ui_app_lifecycle_callback_s));

        ops.create = br_app_create;

        return ui_app_main(argc, argv, &ops, &window);
    }
    ```

4. To create a window, call the `window_create()` function in the `br_app_create()` life-cycle callback function:

    ```
    window = window_create(NULL, 0, 0, EINA_FALSE);
    ```

<a name="window"></a>    
## Creating a Window Object

To create a window object:

1. To create a window object, use the `elm_win_add()` function:

    ```
    static Browser_Window*
    window_create(Evas_Object *opener, int width, int height, Eina_Bool view_mode)
    {
        /* Allocate memory */
        Browser_Window *window = calloc(1, sizeof(Browser_Window));
        if (!window) {
            /* "ERROR: could not create browser window." */
            return NULL;
        }

        /* If you want to use GPU acceleration, use the following function */
        /* elm_config_accel_preference_set("opengl:depth24:stencil8"); */

        /* Create window */
        window->elm_window = elm_win_add(NULL, "minibrowser-window", ELM_WIN_BASIC);
    ```

2. Add a smart callback to the window to handle the window deletion event.

   In the callback, call the `window_close()` function for the object returned from the `window_find_with_elm_window()` function call.

   ```
       evas_object_smart_callback_add(window->elm_window, "delete,request", on_window_deletion, &window);
   }

   static void
   on_window_deletion(void *user_data, Evas_Object *elm_window, void *event_info)
   {
       window_close(window_find_with_elm_window(elm_window));
   }
   ```

<a name="layout"></a>
## Setting the Window Layout and View

Create the layout for the browser window. The layout contains 2 boxes:

- `vertical_layout` contains the view object that displays the browser pages.
- `horizontal_layout` is a top bar that contains the buttons used to move between browser pages.

**Figure: Window layout**

![Window layout](./media/window_layout.png)

1. Create new boxes:

   1. Add the boxes using the `elm_box_add()` function.
   2. Set the hints for the object weight using the `evas_object_size_hint_weight_set()` function.

      The `EVAS_HINT_EXPAND` and `EVAS_HINT_FILL` are macro definitions for the values 1.0 and -1.0.

   3. Add the `vertical_layout` box as a resize subobject of the window using the `elm_win_resize_object_add()` function.

      The resize subobject size and position are controlled by the window directly.

   4. Add a subobject at the end of the pack list using the `elm_box_pack_end()` function.
   5. Make the object visible using the `evas_object_show()` function.

   ```
   /* Create vertical layout */
   Evas_Object *vertical_layout = elm_box_add(window->elm_window);
   elm_box_padding_set(vertical_layout, 0, 2);
   evas_object_size_hint_weight_set(vertical_layout, EVAS_HINT_EXPAND, EVAS_HINT_EXPAND);
   elm_win_resize_object_add(window->elm_window, vertical_layout);
   evas_object_show(vertical_layout);

   /* Create horizontal layout for top bar */
   Evas_Object *horizontal_layout = elm_box_add(window->elm_window);
   elm_box_horizontal_set(horizontal_layout, EINA_TRUE);
   evas_object_size_hint_weight_set(horizontal_layout, EVAS_HINT_EXPAND, 0.0);
   evas_object_size_hint_align_set(horizontal_layout, EVAS_HINT_FILL, 0.0);
   elm_box_pack_end(vertical_layout, horizontal_layout);
   evas_object_show(horizontal_layout);
   ```

2. Create a window view to display the browser pages and set the user agent:

   - To create the view, use the `ewk_view_add()` function.
   - To set the user agent, use the `ewk_view_user_agent_set()` function.

   ```
   static Browser_Window*
   window_create(Evas_Object *opener, int width, int height, Eina_Bool view_mode)
   {
       Evas *evas = evas_object_evas_get(window->elm_window);
       window->ewk_view = ewk_view_add(evas);

       ewk_view_user_agent_set(window->ewk_view, user_agent_string);
   }
   ```

<a name="keymouse"></a>
## Handling Key and Mouse Events

To handle mouse or key events in the window:

1. Set callbacks for the mouse and key events using the `evas_object_event_callback_add()` function:

    ```
    static Browser_Window*
    window_create(Evas_Object *opener, int width, int height, Eina_Bool view_mode)
    {
        /* Key down event */
        evas_object_event_callback_add(window->ewk_view, EVAS_CALLBACK_KEY_DOWN, on_key_down, window);
        /* Mouse down event */
        evas_object_event_callback_add(window->ewk_view, EVAS_CALLBACK_MOUSE_DOWN, on_mouse_down, window);
    }
    ```

2. Define the key event down callback.

   The `ev->key` instance contains the name of the key that caused the event.

   To handle pressed key modifiers, such as **Ctrl** or **Alt**, use the `evas_key_modifier_is_set()` function. To get the `Evas_Modifier` object that contains information about which key modifiers are registered, call the `evas_key_modifier_get()` function, passing the `Evas` canvas object as a parameter.

   ```
   static void
   on_key_down(void *user_data, Evas *e, Evas_Object *ewk_view, void *event_info)
   {
       Browser_Window *window = (Browser_Window *)user_data;
       Evas_Event_Key_Down *ev = (Evas_Event_Key_Down*)event_info;

       const Evas_Modifier *mod = evas_key_modifier_get(e);
       Eina_Bool ctrlPressed = evas_key_modifier_is_set(mod, "Control");
       Eina_Bool altPressed = evas_key_modifier_is_set(mod, "Alt");
   }
   ```

   For example, if the **Alt + Left Arrow** key combination is pressed, the `(!strcmp(ev->key, "Left") && altPressed)` statement must evaluate to `TRUE`.

   The following table shows how the key combinations match to specific view functions.

   **Table: Key behavior**

   | Key                   | Behavior                                 | API                       |
   |-----------------------|------------------------------------------|---------------------------|
   | **Alt + Left Arrow**  | Go to the previous view in the browsing history. | `ewk_view_back()`         |
   | **Alt + Right Arrow** | Go to the next view in the browsing history. | `ewk_view_forward()`      |
   | **F5**                | Reload the view.                         | `ewk_view_reload()`       |
   | **Alt + F5**          | Reload the view bypassing the cache.     | `ewk_view_bypass_cache()` |
   | **F6**                | Stop loading the view.                   | `ewk_view_stop()`         |

3. Define the mouse down event callback.

   The mouse down event information is stored in the `Evas_Event_Mouse_Down` instance. Similarly as in the key events, the `ev->button` instance contains information on which button was pressed.

   In the following example, pressing the first button calls the `view_focus_set()` function to update the focus:

   ```
   static void
   on_mouse_down(void *user_data, Evas *e, Evas_Object *ewk_view, void *event_info)
   {
       Browser_Window *window = (Browser_Window *)user_data;
       Evas_Event_Mouse_Down *ev = (Evas_Event_Mouse_Down *)event_info;

       if (ev->button == 1)
           view_focus_set(window, EINA_TRUE);
   }
   ```

<a name="show"></a>
## Showing the Window and Setting the Focus

In EFL, the UI focus control is implemented in an Elementary, not Evas, object. Therefore, the application using EWK derived from an `Evas_Object` must control the focus itself.

To show the window with the view object (`ewk_view`) and set the focus to the view:

1. Steal focus away from the `elm_window` object and give it to the `ewk_view`.

   Unfocus the window with the `elm_object_focus_set()` function, and move the focus to the view with the `evas_object_focus_set()` function:

   ```
   static void
   view_focus_set(Browser_Window *window, Eina_Bool focus)
   {
       /*
          You steal focus away from the elm focus model and start to do things
          manually, so elm has no clue what is up. Tell elm to unfocus
          the top-level UI component
       */
       elm_object_focus_set(elm_object_top_widget_get(window->elm_window), EINA_FALSE);
       evas_object_focus_set(window->ewk_view, focus);
   };
   ```

2. Within the `window_create()` function, use the `evas_object_show()` function to make the window visible, and call the `view_focus_set()` function to perform the focus change defined above:

   ```
   window_create()
   {
       elm_win_resize_object_add(window->elm_window, window->ewk_view);
       evas_object_show(window->ewk_view);

       evas_object_show(window->elm_window);

       view_focus_set(window, EINA_TRUE);

       return window;
   }
   ```

<a name="helper"></a>
## Finding a Window

You can use helper functions to find window structures:

- The `window_find_with_elm_window()` helper function takes the `elm_window` as a parameter and returns a pointer to the `Browser_Window` object that the window is part of.
- The `window_find_with_ewk_view()` function does the same for `ewk_view`.

Both functions use the `EINA_LIST_FOREACH` macro to iterate over the window list.

```
static Browser_Window*
window_find_with_elm_window(Evas_Object *elm_window)
{
    Eina_List *l;
    void *data;

    if (!elm_window)
        return NULL;

    EINA_LIST_FOREACH(windows, l, data) {
        Browser_Window *window = (Browser_Window *)data;
        if (window->elm_window == elm_window)
            return window;
    }

    return NULL;
}

static Browser_Window*
window_find_with_ewk_view(Evas_Object *ewk_view)
{
    Eina_List *l;
    void *data;

    if (!ewk_view)
        return NULL;

    EINA_LIST_FOREACH(windows, l, data) {
        Browser_Window *window = (Browser_Window *)data;
        if (window->ewk_view == ewk_view)
            return window;
    }

    return NULL;
}
```

<a name="finalize"></a>
## Finalizing the Application

To close the application correctly:

1. To clean up any resources your application has allocated, use the `ewk_shutdown()` function in the termination life-cycle callback:

    ```
    static void
    br_app_terminate(void *app_data)
    {
        ewk_shutdown();
    }
    ```

2. In the `main()` function, register the termination callback:

   ```
   main()
   {
       ops.create = br_app_create;
       ops.terminate = br_app_terminate;

       return ui_app_main(argc, argv, &ops, &window);
   }
   ```

## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
