# Flipselector

The flipselector UI component has a set of text items and a selector that flips up or down to change the text on it. For more information, see the [Flipselector](../../../../api/mobile/latest/group__Elm__Flipselector.html) API.

This feature is supported in mobile applications only.

## Basic Usage

To use a flipselector component in your application:

1. Add a flipselector with the `elm_flipselector_add()` function:

   ```
   Evas_Object *flipselector;

   flipselector = elm_flipselector_add(parent);
   ```

2. Add items to the flipselector with the `elm_flipselector_item_append()` function:

   ```
   Elm_Object_Item *flip_it;

   flip_it = elm_flipselector_item_append(flipselector, "99", it_select_cb, NULL);

   /* Called when the flip_it object is selected */
   void
   it_select_cb(void *data, Evas_Object *obj, void *event_info)
   {
       dlog_print(DLOG_INFO, LOG_TAG, "flip_it selected\n");
   }
   ```

3. Register the [callback](#callbacks) functions.

   The following example shows how to define and register a callback for the `selected` signal:

   ```
   evas_object_smart_callback_add(flipselector, "selected", _flip_selected_cb, NULL);

   static void
   _flip_selected_cb(void *data, Evas_Object *obj, void *event_info)
   {
       Elm_Object_Item *flip_it = event_info;

       /* Code that does the desired action */
   }
   ```

The following example shows a simple use case of the flipselector component.

**Example: Flipselector use case**

![Flipselector](./media/flipselector1.png)

```
Evas_Object *win;
Evas_Object *conf;
Evas_Object *nf;
Evas_Object *flipselector;
char buf[8];
int i;

/* Starting right after the basic EFL UI layout code */
/* win - conformant - naviframe */

/* Add a flipselector */
flipselector = elm_flipselector_add(nf);

for (i = 0; i <= 99; i++) {
    snprintf(buf, 8, "%u", i);
    elm_flipselector_item_append(flipselector, buf, flipselector_item_select_cb, NULL);
}
elm_naviframe_item_push(nf, "Flipselector", NULL, NULL, flipselector, NULL);

void
flipselector_item_select_cb(void *data, Evas_Object *obj, void *event_info)
{
    Elm_Object_Item *it = event_info;
    printf("label of selected item is: %s\n", elm_object_item_text_get(it));
}
```

## Options

To set the flipselector options:

- First interval

  You can define the length of the first change interval when the user keeps the mouse button down for a longer period. After the first interval, the flipselector text is changed regularly while the mouse button remains down.

  To set the first interval, use the `elm_flipselector_first_interval_set()` function:

  ```
  elm_flipselector_first_interval_set(flipselector, 2.0);
  ```

- Flipselector value

  To change the value:

  - Show the next text using the `elm_flipselector_flip_next()` function:

    ```
    elm_flipselector_flip_next(flipselector);
    ```

  - Show the previous text using the `elm_flipselector_flip_prev()` function:

    ```
    elm_flipselector_flip_prev(flipselector);
    ```

  - Show the text of the specific item using the `elm_flipselector_item_selected_set()` function.

    If the second parameter is set to `EINA_FALSE`, the flipselector shows the text of the first item.

    ```
    elm_flipselector_item_selected_set(flip_it, EINA_TRUE);
    ```

## Styles

The following table lists the available component styles.

**Table: Flipselector styles**

| Style                           | Sample                                   |
|---------------------------------|------------------------------------------|
| `elm/flipselector/base/default` | ![elm/flipselector/base/default](./media/flipsel_default.png) |

## Callbacks

You can register callback functions connected to the following signals for a flipselector object.

**Table: Flipselector callback signals**

| Signal        | Description                              | `event_info` |
|---------------|------------------------------------------|--------------|
| `selected`    | The flipselector's selected text item changes. | `NULL`       |
| `overflowed`  | The flipselector's current selection changes from the first item to the last one. | `NULL`       |
| `underflowed` | The flipselector's current selection changes from the last item to the first one. | `NULL`       |

> **Note**
>
> The signal list in the API reference can be more extensive, but only the above signals are actually supported in Tizen.

> **Note**
>
> Except as noted, this content is licensed under [LGPLv2.1+](http://opensource.org/licenses/LGPL-2.1).

## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
