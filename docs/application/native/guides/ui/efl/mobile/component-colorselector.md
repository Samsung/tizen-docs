# Colorselector

The colorselector UI component allows users to select a color. For more information, see the [Colorselector](../../../../api/mobile/latest/group__Elm__Colorselector.html) API.

This feature is supported in mobile applications only.

## Basic Usage

To use a colorselector component in your application:

1. Add a colorselector with the `elm_colorselector_add()` function:

   ```
   Evas_Object *colorsel;

   colorsel = elm_colorselector_add(parent);
   ```

2. Set a mode to the colorselector with the `elm_colorselector_mode_set()` function. Currently, only the palette mode is available in Tizen.

   ```
   elm_colorselector_mode_set(colorsel, ELM_COLORSELECTOR_PALETTE);
   ```

3. Set a name to the palette with the `elm_colorselector_palette_name_set()` function. If you use the default palette, you can skip this step.

4. Add colors to the palette. If you use the default style, you can skip this step, since the default palette already has the colors selected.

   The new palette is saved by the Elementary configuration and you can load it again later.

   The palette mode displays several color items for the user to select from. It is possible to add new items, or to update the color of the current item. The list of color items is called a palette, and it is associated with a unique identifier. You can create a new series of colors (a new palette) and save it under another identifier. By default, the palette mode uses the `default` palette, which contains 14 colors.

5. Register the [callback](#callbacks) functions.

   When a color in the colorselector is clicked, the color set to the colorselector component changes. Retrieve the currently selected color with the `elm_colorselector_color_set()` function.

   The following example shows how to define and register a callback for the `changed` signal:

   ```
   evas_object_smart_callback_add(colorselector, "changed", changed_cb, data);

   void
   changed_cb(void *data, Evas_Object *obj, void *event_info)
   {
       dlog_print(DLOG_INFO, LOG_TAG, "The color has changed\n");
   }
   ```

The following example shows a simple use case of the colorselector component.

**Example: Colorselector use case**

![Colorselector](./media/colorselector1.png)

```
Evas_Object *win;
Evas_Object *conf;
Evas_Object *nf;
Evas_Object *colsel;
Elm_Object_Item *nf_it;

/* Starting right after the basic EFL UI layout code */
/* win - conformant - naviframe */

colsel = elm_colorselector_add(nf);
elm_colorselector_mode_set(colsel, ELM_COLORSELECTOR_PALETTE);
evas_object_show(colsel);

elm_naviframe_item_push(nf, "Colorselector", NULL, NULL, colsel, NULL);
```

The following example shows how to add a new palette called `mypalette`, with 3 colors (red, green, and blue).

**Example: Customized colorselector**

![Colorselector](./media/colorselector2.png)

```
Evas_Object *win;
Evas_Object *conf;
Evas_Object *nf;
Evas_Object *colsel;
Elm_Object_Item *nf_it;

/* Starting right after the basic EFL UI layout code */
/* win - conformant - naviframe */

colsel = elm_colorselector_add(nf);
elm_colorselector_mode_set(colsel, ELM_COLORSELECTOR_PALETTE);
evas_object_show(colsel);

elm_naviframe_item_push(nf, "Colorselector", NULL, NULL, colsel, NULL);

elm_colorselector_palette_name_set(colorsel, "mypalette");
elm_colorselector_palette_color_add(colorsel, 255, 0, 0, 255);
elm_colorselector_palette_color_add(colorsel, 0, 255, 0, 255);
elm_colorselector_palette_color_add(colorsel, 0, 0, 255, 255);
```

## Styles

The following table lists the available component styles.

**Table: Colorselector styles**

| Style                                    | Sample                                   | Notes                                    |
|----------------------------------------|----------------------------------------|----------------------------------------|
| `elm/colorselector/item/color/colorplane` | ![elm/colorselector/item/color/colorplane](./media/color_colorplane.png) | Use the following command: <br>`elm_colorselector_mode_set(colorselector, ELM_COLORSELECTOR_PALETTE);` |

## Callbacks

You can register callback functions connected to the following signals for a colorselector object.

**Table: Colorselector callback signals**

| Signal                   | Description                              | `event_info`                |
|-----------------------|----------------------------------------|---------------------------|
| `changed`                | The color value changes on the selector. | `NULL`                      |
| `color,item,selected`    | The color item is pressed.               | The pressed color item      |
| `color,item,longpressed` | The color item is long-pressed.          | The long-pressed color item |

> **Note**
>
> The signal list in the API reference can be more extensive, but only the above signals are actually supported in Tizen.

> **Note**
>
> Except as noted, this content is licensed under [LGPLv2.1+](http://opensource.org/licenses/LGPL-2.1).

## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
