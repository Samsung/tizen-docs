# Gengrid

The gengrid UI component is based on the same idea as [genlist](component-genlist.md). It aims to display objects on a grid layout and render only the visible ones. For more information, see the [Gengrid](../../../../api/mobile/latest/group__Elm__Gengrid.html) API.

This feature is supported in mobile applications only.

To save memory and speed up processing when many items exist, the gengrid uses the concept of "realization" when managing items. It means that a gengrid item creates its text and content (realizes) when the user scrolls the grid and the item shows up on the screen, and frees them (unrealizes) when the item is scrolled out of the screen. To enable the item realization, you must create and fill an `Elm_Gengrid_Item_Class` structure (gengrid item class) that informs the gengrid component which callbacks to call when an item is created or deleted. When the item is created, the text and content are retrieved by calling the `text_get` and `content_get` functions defined in the gengrid item class.

## Basic Usage

To use a gengrid component in your application:

1. Add a gengrid with the `elm_gengrid_add()` function:

   ```
   Evas_Object *gengrid;

   gengrid = elm_gengrid_add(parent);
   ```

2. Define the gengrid item class:

   1. Create a gengrid item class with the `elm_gengrid_item_class_new()` function, set a style to the item class, and register the callback functions.

      The gengrid item class must be freed manually with `elm_gengrid_item_class_free()` function after all items are appended.

      ```
      Elm_Gengrid_Item_Class *itc = elm_gengrid_item_class_new();

      itc->item_style = "default";
      itc->func.text_get = _item_label_get;
      itc->func.content_get = _item_content_get;
      itc->func.del = _item_del;
      ```

   2. Define the `text_get` function.

      When a gengrid item becomes realized, the `text_get` function is called repeatedly for all text parts in that item. After the text is set to the part, it is freed automatically. Do not free it manually.

      ```
      static char*
      _item_label_get(void *data, Evas_Object *obj, const char *part)
      {
          if (!strcmp(part, "elm.text"))
              return strdup("text");
          else
              return NULL;
      }
      ```

   3. Define the `content_get` function.

      The `content_get` function is called repeatedly for all swallow parts in the item. It must return a valid object handle to be set, or `NULL` when no content is desired. The object is deleted by the gengrid on its deletion or when the item is unrealized.

      ```
      static Evas_Object*
      _item_content_get(void *data, Evas_Object *obj, const char *part)
      {
          if (!strcmp(part, "elm.swallow.icon")) {
              Evas_Object *img = elm_image_add(obj);
              elm_image_file_Set(img, "sample.png", NULL);

              return img;
          } else {
              return NULL;
          }
      }
      ```

   4. Define the `del` function.

      This function is called when the gengrid item is deleted. It deletes any data that has been allocated at the item's creation.

      ```
      static void
      _item_del(void *data, Evas_Object *obj)
      {
          printf("item(%d) is now deleted", (int) data);
      }
      ```

3. Append items to the gengrid with the `elm_gengrid_item_append()` function.

   ```
   elm_gengrid_item_append(gengrid, /* Gengrid object */
                           itc, /* Gengrid item class */
                           (void *)i, /* Item data */
                           _item_selected_cb, /* "selected" callback */
                           (void *)i); /* Callback data */
   ```

4. Register the [callback](#callbacks) functions for the gengrid and its items.

   The following example shows how to define a callback for when the gengrid item is selected:

   ```
   static void
   _item_selected_cb(void *data, Evas_Object *obj, void *event_info)
   {
       printf("item(%d) is selected", (int) data);
   }
   ```

### Managing Gengrid Items

To manage the items:

- Add items:

  - To add an item to the end of the grid, use the `elm_gengrid_item_append()` function.
  - To add an item to the beginning of the grid, use the similar `elm_gengrid_item_prepend()` function.
  - To insert an item before the indicated item, use the `elm_gengrid_item_insert_before()` function.
  - To insert an item after the indicated item, use the `elm_gengrid_item_insert_after()` function.

- Set the orientation.

  A gengrid can display its items using a horizontal or vertical layout. In the horizontal layout, the items are displayed in columns from top to bottom, starting a new column when the space for the current column is filled. In the vertical layout, items are set in rows from left to right. By default, the vertical layout is used. To set the horizontal layout:

  ```
  elm_gengrid_horizontal_set(gengrid, EINA_TRUE);
  ```

- Delete items and clear the grid:

  - To delete a single gengrid item, use the `elm_object_item_del()` function.
  - To clear the grid and delete all items, use the `elm_gengrid_clear()` function.

  If a gengrid object is deleted by the `evas_object_del()` function, all items are deleted automatically. On item deletion, the `del()` function in the item class is called.

- Update items.

  If the content of an item changes, use the `elm_gengrid_item_update()` function for the gengrid to update the item. The gengrid re-realizes the item and calls the functions in the `_Elm_Gengrid_Item_Class` class for it.

  You can also use the `elm_gengrid_item_fields_update()` function to update only specific parts:

  - `ELM_GENGRID_ITEM_FIELD_TEXT`
  - `ELM_GENGRID_ITEM_FIELD_CONTENT`
  - `ELM_GENGRID_ITEM_FIELD_STATE`

- Select or disable items.

  To manually select an item, use the `elm_gengrid_item_selected_set()` function. To select multiple items, you must enable the multi-selection mode:

  ```
  elm_gengrid_multi_select_set(gengrid, EINA_TRUE);
  ```

  To retrieve the selected item, use the `elm_gengrid_selected_item_get()` function. When the multi-selection mode is enabled, you can retrieve the selected items with the `elm_gengrid_selected_items_get()` function, which returns a list of all selected items.

  To disable an item manually, use the `elm_object_item_disabled_set()` function.

## Styles

A gengrid item can have 0 or more texts, 0 or more contents, and 0 or more boolean states. The number of texts and contents depends on the Edje item theme style used for the gengrid items. In the `default` Tizen gengrid item theme style, the items can have 2 content parts that can be set with the `elm.swallow.icon` and `elm.swallow.end` part names.

The following gengrid styles and related item styles are supported:

- `default`
  - `default`
  - `type1` (identical to the `default` style in Tizen 2.4)
  - `type2`
- `popup`
  - `default`

To use the `popup` gengrid style with the `default` item style:

```
elm_object_style_set(gengrid, "popup");
gic->item_style = "default";
```

**Figure: Gengrid styles**

![Gengrid styles](./media/gengrid_styles.png)

The following table provides more information on the available gengrid item styles.

**Table: Gengrid item styles**

| Style                                    | Sample                                   | Text part  | Swallow part                        |
|------------------------------------------|------------------------------------------|------------|-------------------------------------|
| `elm/gengrid/item/default/default`<br> `elm/gengrid/item/type1/default` | ![elm/gengrid/item/default/default](./media/gengrid_default.png) | `elm.text` | `elm.swallow.icon`<br>`elm.swallow.end` |
| `elm/gengrid/item/type2/default`         | ![elm/gengrid/item/type2/default](./media/gengrid_default_type2.png) | `elm.text` | `elm.swallow.icon`<br>`elm.swallow.end` |
| `elm/gengrid/item/default/popup`         | ![elm/gengrid/item/default/popup](./media/gengrid_popup.png) | `elm.text` | `elm.swallow.icon`<br>`elm.swallow.end` |

## Callbacks

You can register callback functions connected to the following signals for a gengrid object.

**Table: Gengrid callback signals**

| Signal                    | Description                              | `event_info`                             |
|---------------------------|------------------------------------------|------------------------------------------|
| `activated`               | The item is double-clicked or pressed (enter &verbar; return &verbar; spacebar). | `Elm_Object_Item`                        |
| `clicked,double`          | The item is double-clicked.              | `Elm_Object_Item`                        |
| `selected`                | The item is selected.                    | `Elm_Object_Item`                        |
| `unselected`              | The item is unselected.                  | `Elm_Object_Item`                        |
| `realized`                | The item is created as a real evas object. | `Elm_Object_Item`                        |
| `unrealized`              | The item is going to be unrealized. Provided content objects are deleted and the item object is deleted or put into a floating cache. | `Elm_Object_Item`                        |
| `drag,start,up`           | The item in the grid is dragged (not scrolled) up. | `Elm_Object_Item`                        |
| `drag,start,down`         | The item in the grid is dragged (not scrolled) down. | `Elm_Object_Item`                        |
| `drag,start,left`         | The item in the grid is dragged (not scrolled) left. | `Elm_Object_Item`                        |
| `drag,start,right`        | The item in the grid is dragged (not scrolled) right. | `Elm_Object_Item`                        |
| `drag,stop`               | The item in the grid has stopped being dragged. | `Elm_Object_Item`                        |
| `drag`                    | The item in the grid is being dragged.   | `Elm_Object_Item` object that contains the dragged item |
| `scroll,drag,start`       | Dragging the content is started.         | `NULL`                                   |
| `scroll,drag,stop`        | Dragging the content is stopped.         | `NULL`                                   |
| `scroll`                  | Scrolling is ongoing.                    | `NULL`                                   |
| `edge,top`                | The gengrid is scrolled to the top edge. | `NULL`                                   |
| `edge,bottom`             | The gengrid is scrolled to the bottom edge. | `NULL`                                   |
| `edge,left`               | The gengrid is scrolled to the left edge. | `NULL`                                   |
| `edge,right`              | The gengrid is scrolled to the right edge. | `NULL`                                   |
| `moved`                   | The item is moved in the reorder mode.   | `Elm_Object_Item` object that contains the moved item |
| `pressed`                 | The item is pressed by mouse down.       | `Elm_Object_Item` object that contains the pressed item |
| `released`                | The item is released by mouse up.        | `Elm_Object_Item` object that contains the released item |
| `clicked,right`           | The item is right-clicked.               | Right-clicked gengrid item               |
| `longpressed`             | The item is pressed for a certain amount of time. By default, it is 1 second. |               -                           |
| `changed`                 | The item is added, removed, resized, or moved, and the gengrid is resized or has `horizontal` property changes. |       -                                   |
| `scroll,anim,start`       | The scrolling animation starts.          |         -                                 |
| `scroll,anim,stop`        | The scrolling animation stops.           |         -                                 |
| `scroll,page,changed`     | The visible page changes.                |           -                               |
| `item,reorder,anim,start` | The reorder animation starts.            |        -                                  |
| `item,reorder,anim,stop`  | The reorder animation stops.             |   -                                       |

> **Note**
>
> The signal list in the API reference can be more extensive, but only the above signals are actually supported in Tizen.

> **Note**
>
> Except as noted, this content is licensed under [LGPLv2.1+](http://opensource.org/licenses/LGPL-2.1).

## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
