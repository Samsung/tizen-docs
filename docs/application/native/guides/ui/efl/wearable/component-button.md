# Button

This feature is supported in wearable applications only.

The button component is a simple push button, which is composed of a label icon and an icon object. The button supports the autorepeat feature.

For more information, see the [Button](../../../../api/wearable/latest/group__Elm__Button.html) API.

**Figure: Button component**

![Button component](./media/button_wn.png)

**Figure: Button hierarchy**

![Button hierarchy](./media/button_tree.png)

## Adding a Button Component

To create a button, use the `elm_button_add()` function:

```
Evas_Object *button;
Evas_Object *parent;

/* Create a button */
button = elm_button_add(parent);
```

You can add an icon or text inside the button:

- To add an icon, use the `elm_object_part_content_set()` function with the `icon` part name:

  ```
  Evas_Object *ic;
  ic = elm_icon_add(button);
  elm_image_file_set(ic, "icon.png", NULL);
  elm_object_part_content_set(button, "icon", ic);
  ```

- To add text to the label, use the `elm_object_text_set()` function:

  ```
  elm_object_text_set(button, "Click me!");
  ```

## Using the Button Styles

You can set a style for the button:

- The following styles are available for a rectangular screen:
  - `default`
  - `green`
  - `orange`
  - `red`
  - `nextdepth`

- The following styles are available for a circular screen:
  - `default`
  - `bottom`

```
/* Rectangular screen button style */
elm_object_style_set(button, "nextdepth");

/* Circular screen button style */
elm_object_style_set(button, "bottom");
```

## Using the Button Callbacks

To receive notifications about the button events, listen for the following signals:

- `clicked`: The button is clicked (press/release).
- `repeated`: The button is pressed without releasing it.
- `pressed`: The button is pressed.
- `unpressed`: The button is released after being pressed.

> **Note**  
> The signal list in the API reference can be more extensive, but only the above signals are actually supported in Tizen.

In all cases, the `event_info` callback parameter is `NULL`.

To register and define a callback for the `clicked` signal:

```
{
    evas_object_smart_callback_add(button, "clicked", clicked_cb, data);
}

/* Callback for the "clicked" signal */
/* Called when the button is clicked by the user */
void
clicked_cb(void *data, Evas_Object *obj, void *event_info)
{
    dlog_print(DLOG_INFO, LOG_TAG, "Button clicked\n");
}
```

## Using the Autorepeat Feature

The autorepeat feature means that the `repeated` signal is called repeatedly while the user keeps the button pressed.

To manage the autorepeat feature:

- You can enable and disable the autorepeat feature. It is enabled by default.

  To disable the feature:

  ```
  elm_button_autorepeat_set(button, EINA_FALSE);
  ```

- You can set the initial timeout before the `repeated` signal is emitted.

  To set the timeout to 5 seconds:

  ```
  elm_button_autorepeat_initial_timeout_set(button, 5.0);
  ```

- You can set the interval between 2 `repeated` signals.

  To set the interval to 0.5 seconds:

  ```
  elm_button_autorepeat_gap_timeout_set(button, 0.5);
  ```

> **Note**  
> Except as noted, this content is licensed under [LGPLv2.1+](http://opensource.org/licenses/LGPL-2.1).

## Related Information
- Dependencies
  - Tizen 2.3.1 and Higher for Wearable
