# Win

Win stands for window, and the win component is a graphical control element containing the graphical user interface of a program. The window component is the bottommost UI component in an EFL application. In most cases, when an application is launched, a window that fits into the device screen is created and shown. For more information, see the [Win](../../../../api/mobile/latest/group__Elm__Win.html) API.

This feature is supported in mobile applications only.

## Basic Usage

A window is created automatically when you create a Tizen native UI application project with a template. The following example is a part of the template code handling a window component and the corresponding screenshot.

**Example: Win use case**

![Window](./media/window_mn.png)

```
static void
create_base_gui(appdata_s *ad)
{
    /* Window */
    /*
       Create and initialize elm_win,
       which is mandatory to manipulate the window
    */
    ad->win = elm_win_util_standard_add(PACKAGE, PACKAGE);
    elm_win_autodel_set(ad->win, EINA_TRUE);

    if (elm_win_wm_rotation_supported_get(ad->win)) {
        int rots[4] = {0, 90, 180, 270};
        elm_win_wm_rotation_available_rotations_set(ad->win, (const int *)(&rots), 4);
    }

    evas_object_smart_callback_add(ad->win, "delete,request", win_delete_request_cb, NULL);
    eext_object_event_callback_add(ad->win, EEXT_CALLBACK_BACK, win_back_cb, ad);

    /* Conformant */
    /*
       Create and initialize elm_conformant,
       which is mandatory for the base GUI to have a proper size
       when the indicator or virtual keypad is visible
    */
    ad->conform = elm_conformant_add(ad->win);
    elm_win_indicator_mode_set(ad->win, ELM_WIN_INDICATOR_SHOW);
    evas_object_size_hint_weight_set(ad->conform, EVAS_HINT_EXPAND, EVAS_HINT_EXPAND);
    elm_win_resize_object_add(ad->win, ad->conform);
    evas_object_show(ad->conform);

    evas_object_show(ad->win);
}

static void
win_delete_request_cb(void *data, Evas_Object *obj, void *event_info)
{
    ui_app_exit();
}

static void
win_back_cb(void *data, Evas_Object *obj, void *event_info)
{
    appdata_s *ad = data;
    /* Let the window go to the hide state */
    elm_win_lower(ad->win);
}
```

The basic template code includes the following steps:

1. Add a window with the `elm_win_util_standard_add()` function.

   The first parameter is the name of the window used by the window manager for identifying the window uniquely amongst all the windows within the application (and all instances of the application). The second parameter is the title of the window.

   The `elm_win_util_standard_add()` function is a shortcut of the `elm_win_add()`, `elm_win_title_set()`, and `elm_bg_add()` functions. It creates a basic window with a title and adds a standard background to the window.

   ```
   Evas_Object *win;
   Evas_Object *bg;

   /* Add a window */
   win = elm_win_add(NULL, "name", ELM_WIN_BASIC);
   /* Set a title to the window */
   elm_win_title_set(win, "title");
   /* Add a background and set it as the contents of the window */
   bg = elm_bg_add(win);
   evas_object_size_hint_weight_set(bg, EVAS_HINT_EXPAND, EVAS_HINT_EXPAND);
   elm_win_resize_object_add(win, bg);
   evas_object_show(bg);
   ```

2. Enable auto deletion with the `elm_win_autodel_set()` function.

   When closing the window in any way outside the program control, a `delete,request` signal is emitted to indicate that this event occurred. If you enable auto deletion, the window is automatically destroyed after the signal is emitted. If auto deletion is disabled, the window is not destroyed and the program has to handle it.

3. Register a callback function connected to the `delete,request` signal. You can register extra [callback](#callbacks) functions, if necessary.

4. Show or hide an indicator with the `elm_win_indicator_mode_set()` function.

5. Add a conformant to the window with the `elm_win_resize_object_add()` function.

   In most cases, you want the content of the window to be resized every time the window is resized due to rotation. To match the content size with the window size, make the content expand to fit the container size with the `evas_object_size_hint_weight_set()` function and add it to the window with the `elm_win_resize_object_add()` function.

   ```
   Evas_Object *win;
   Evas_Object *obj;

   evas_object_size_hint_weight_set(obj, EVAS_HINT_EXPAND, EVAS_HINT_EXPAND);
   elm_win_resize_object_add(win, obj);
   ```

6. Call the `evas_object_show()` function after all the properties are set.

## Callbacks

You can register callback functions connected to the following signals for a win object.

**Table: Win callback signals**

| Signal                   | Description                              | `event_info` |
|--------------------------|------------------------------------------|--------------|
| `delete,request`         | The window is deleted.                   | `NULL`       |
| `focused`                | The window received focus.               | `NULL`       |
| `unfocused`              | The window lost focus.                   | `NULL`       |
| `moved`                  | The window that holds the canvas is moved. | `NULL`       |
| `withdrawn`              | The window is managed normally but is removed from the view. | `NULL`       |
| `iconified`              | The window is minimized (for example, into an icon or taskbar). | `NULL`       |
| `normal`                 | The window is in the normal state (not withdrawn or iconified). | `NULL`       |
| `stick`                  | The window shows on all desktops.        | `NULL`       |
| `unstick`                | The window shows only on 1 desktop.      | `NULL`       |
| `fullscreen`             | The window is fullscreen.                | `NULL`       |
| `unfullscreen`           | The window stops being fullscreen.       | `NULL`       |
| `maximized`              | The window is maximized.                 | `NULL`       |
| `unmaximized`            | The window is diminished.                | `NULL`       |
| `ioerr`                  | A low-level I/O error occurred in the display system. | `NULL`       |
| `wm,rotation,changed`    | The rotation of the window is changed by the Window Manager. | `NULL`       |
| `indicator,prop,changed` | The property, or indicator mode and indicator opacity are changed. | `NULL`       |
| `rotation,changed`       | The rotation of the window is changed.   | `NULL`       |
| `profile,changed`        | The profile of the window is changed.    | `NULL`       |
| `aux,hint,allowed`       | The window auxiliary hint is allowed.    | `NULL`       |

> **Note**
>
> The signal list in the API reference can be more extensive, but only the above signals are actually supported in Tizen.

> **Note**
>
> Except as noted, this content is licensed under [LGPLv2.1+](http://opensource.org/licenses/LGPL-2.1).

## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
