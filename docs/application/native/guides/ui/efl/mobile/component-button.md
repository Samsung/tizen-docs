# Button

The button UI component works as a clickable input element to trigger events. For more information, see the [Button](../../../../api/mobile/latest/group__Elm__Button.html) API.

This feature is supported in mobile applications only.

## Basic Usage

To use a button component in your application:

1. Add a button with the `elm_button_add()` function:

   ```
   Evas_Object *button;

   button = elm_button_add(parent);
   ```

2. Set a [style](#styles) and fill the button with a text or an image according to the style:

   - Set a style to the button with the `elm_object_style_set()` function. If you use the default style, you can skip this step.

     ```
     elm_object_style_set(button, "circle");
     ```

   - Set a label to the button with the `elm_object_text_set()` function, if the style supports a text part.

     ```
     elm_object_text_set(button, "Home");
     ```

   - Set an image object to the button with the `elm_object_part_content_set()` function, if the style supports a swallow part.

     ```
     Evas_Object *icon;

     elm_object_part_content_set(button, "icon", icon);
     ```

3. Register the [callback](#callbacks) functions.

   The following example shows how to define and register a callback for the `clicked` signal:

   ```
   evas_object_smart_callback_add(button, "clicked", clicked_cb, data);

   void
   clicked_cb(void *data, Evas_Object *obj, void *event_info)
   {
       dlog_print(DLOG_INFO, LOG_TAG, "Button clicked\n");
   }
   ```

The following example shows a simple use case of the button component.

**Example: Button use case**

 ![Button](./media/button1.png)

```
Evas_Object *win;
Evas_Object *conf;
Evas_Object *nf;
Evas_Object *box;
Evas_Object *button;
Evas_Object *icon;

/* Starting right after the basic EFL UI layout code */
/* (win - conformant - naviframe) */

/* Add a box to contain a button and push the box into the naviframe */
box = elm_box_add(nf);
evas_object_show(box);
elm_naviframe_item_push(nf, "Button", NULL, NULL, box, NULL);

/* Add a button and set a style */
button = elm_button_add(box);
elm_object_style_set(button, "circle");

/* Set a text to the button */
elm_object_text_set(button, "Home");

/* Add an icon and set it as a content */
icon = elm_icon_add(button);
elm_icon_standard_set(icon, "home");
elm_object_part_content_set(button, "icon", icon);

evas_object_show(button);
elm_box_pack_end(box, button);
```

## Features

You can use the autorepeat feature in your application. Once a button is pressed, a `repeated` signal is emitted repeatedly until the button is released.

- To disable the autorepeat feature:

  ```
  elm_button_autorepeat_set(button, EINA_FALSE);
  ```

- To set the initial timeout before the `repeated` signal is emitted:

  ```
  elm_button_autorepeat_initial_timeout_set(button, 5.0);
  ```

- To set the interval between 2 `repeated` signals:

  ```
  elm_button_autorepeat_gap_timeout_set(button, 0.5);
  ```

## Styles

The following table lists the available component styles.

**Table: Button styles**

| Style                                    | Sample                                   | Text part | Swallow part |
|---------------|:------------:|---------|------------|
| `default`                                | ![elm/button/base/default](./media/button_default.png) | `default` | `icon`       |
| `circle`                                 | ![elm/button/base/circle](./media/button_circle.png) | `default` | `icon`       |
| `editfield_clear`                        | ![elm/button/base/editfield_clear](./media/button_editfield_clear.png) | N/A       | `icon`       |
| `bottom`                                 | ![elm/button/base/bottom](./media/bottom.png) | `default` | `icon`       |
| `icon_reorder`                           |  -                                        | N/A       | N/A          |
| `icon_expand_add`                        | -                                          | N/A       | N/A          |
| `icon_expand_delete`                     | ![elm/button/base/icon_expand_delete](./media/icon_expand_delete.png) | N/A       | N/A          |
| `naviframe/title_left`                   | ![elm/button/base/naviframe/title_left](./media/button_title_left.png) | `default` | N/A          |
| `naviframe/title_right`                  | ![elm/button/base/naviframe/title_right](./media/button_title_right.png) | `default` | N/A          |
| `naviframe/back_btn/default`             | ![elm/button/base/naviframe/back_btn/default](./media/button_back_btn.png) | N/A       | N/A          |
| `dropdown`                               | ![elm/button/base/dropdown](./media/button_dropdown.png) | `default` | N/A          |
| `contacts` (Tizen 2.3 only style)        |      -                                    | `default` | N/A          |
| `naviframe/title_done` (Tizen 2.3 only style) | ![elm/button/base/naviframe/title_done](./media/button_title_done_23.png) | N/A       | N/A          |
| `naviframe/title_cancel` (Tizen 2.3 only style) | ![elm/button/base/naviframe/title_cancel](./media/button_title_cancel_23.png) | N/A       | N/A          |
| `naviframe/drawers` (Tizen 2.3 only style) |      -                                    | N/A       | N/A          |
| `option` (Tizen-2.3 only style)          |      -                                    | N/A       | N/A          |

## Callbacks

You can register callback functions connected to the following signals for a button object.

**Table: Button callback signals**

| Signal      | Description                              | `event_info` |
|-----------|----------------------------------------|------------|
| `clicked`   | The button is clicked (press and release). | `NULL`       |
| `repeated`  | The button is pressed without releasing it. | `NULL`       |
| `pressed`   | The button is pressed.                   | `NULL`       |
| `unpressed` | The button is released after being pressed. | `NULL`       |

> **Note**
>
> The signal list in the API reference can be more extensive, but only the above signals are actually supported in Tizen.

> **Note**
>
> Except as noted, this content is licensed under [LGPLv2.1+](http://opensource.org/licenses/LGPL-2.1).

## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
