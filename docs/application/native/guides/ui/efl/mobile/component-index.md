# Index

The index UI component gives you an index for quick access to a group of other UI items. The index component is hidden by default, but it appears when the user clicks over its reserved area on the canvas. For more information, see the [Index](../../../../api/mobile/latest/group__Elm__Index.html) API.

This feature is supported in mobile applications only.

## Basic Usage

To use an index component in your application:

1. Add an index with the `elm_index_add()` function:

   ```
   Evas_Object *index;

   index = elm_index_add(parent);
   ```

2. Configure the index and set its [style](#styles).

3. Append items to the index with the `elm_index_item_append()` function. The function takes 5 parameters: the pointer of the toolbar, a file path of an icon, a text, a callback function to call when the item is clicked, and the parameter passed to the callback.

   ```
   elm_index_item_append(index, "A", _item_selected_cb, NULL);
   ```

4. Register the [callback](#callbacks) functions.

The following example shows a simple use case of the index component.

**Example: Index use case**

![Index](./media/index1.png)

```
Evas_Object *win;
Evas_Object *conf;
Evas_Object *nf;
Evas_Object *index;
Elm_Object_Item *nf_it;
int i;
char buf[8];

/* Starting right after the basic EFL UI layout code */
/* win - conformant - naviframe */

index = elm_index_add(nf);

for (i = 0; i < 26; i++) {
    sprintf(buf, "%c", ('A' + i));
    elm_index_item_append(index, buf, NULL, NULL);
}

evas_object_show(index);
elm_naviframe_item_push(nf, "Index", NULL, NULL, index, NULL);
```

## Index Usage with a List

The most common usage of an index is with a list. When a list has many items, you can "bring in" a list item by touching the corresponding index item instead of scrolling the list. Remember that index and list are independent UI components. You need to do an extra job to use an index to control a list.

To connect index items with list items:

1. Overlap an index on the top of a list using a container object such as a layout or a table.

2. When appending an index item, pass a pointer to a list item to which you want to connect the index item.

   ```
   Elm_Object_Item *it;

   it = elm_list_item_append(list, "tizen", NULL, NULL, NULL, NULL);
   elm_index_item_append(index, "T", NULL, it);
   ```

3. Register a callback function to the index for the `changed` signal. Bring in the corresponding list item in the callback function. The `event_info` parameter is the changed index item and the `elm_object_item_data_get()` function retrieves the list item passed to `elm_index_item_append()` function.

   ```
   void
   index_changed_cb(void *data, Evas_Object *obj, void *event_info)
   {
       elm_list_item_bring_in(elm_object_item_data_get(event_info));
   }
   ```

The following example shows an index with a list.

**Example: Index with list**

![Index with list](./media/index2.png)

```
Evas_Object *win;
Evas_Object *conf;
Evas_Object *nf;
Evas_Object *table;
Evas_Object *list;
Evas_Object *index;
Elm_Object_Item *it;
char buf[8], str_buf[16];
int i;

/* Starting right after the basic EFL UI layout code */
/* win - conformant - naviframe */

table = elm_table_add(naviframe);
evas_object_show(table);

list = elm_list_add(table);
evas_object_size_hint_weight_set(list, EVAS_HINT_EXPAND, EVAS_HINT_EXPAND);
evas_object_size_hint_align_set(list, EVAS_HINT_FILL, EVAS_HINT_FILL);
elm_table_pack(table, list, 0, 0, 1, 1);
evas_object_show(list);

index = elm_index_add(table);
evas_object_size_hint_weight_set(index, EVAS_HINT_EXPAND, EVAS_HINT_EXPAND);
evas_object_size_hint_align_set(index, EVAS_HINT_FILL, EVAS_HINT_FILL);
elm_table_pack(table, index, 0, 0, 1, 1);
evas_object_show(index);

for (i = 0; i < 26; i++) {
    sprintf(buf, "%c", ('A' + i));
    sprintf(str_buf, "%s string", buf);
    it = elm_list_item_append(list, str_buf, NULL, NULL, NULL, NULL);

    elm_index_item_append(index, buf, NULL, it);
}

evas_object_smart_callback_add(index, "changed", index_changed_cb, list);
elm_naviframe_item_push(naviframe, "Index", NULL, NULL, table, NULL);

static void
index_changed_cb(void *data, Evas_Object *obj, void *event_info)
{
    elm_list_item_bring_in(elm_object_item_data_get(event_info));
}
```

## Styles

To set the style, use the `elm_object_style_set()` function:

```
elm_object_style_set(index, "pagecontrol");
```

The following table lists the available component styles.

**Table: Index styles**

| Style                                 | Sample                                   | Notes                                    |
|---------------------------------------|------------------------------------------|------------------------------------------|
| `elm/index/base/vertical/default`     | ![elm/index/base/vertical/default](./media/index_default.png) | This style has a one-finger-wide area on the right side of the index component's container. Generally, this style is used together with lists, generic lists, or generic grids. |
| `elm/index/base/vertical/pagecontrol` | ![elm/index/base/vertical/pagecontrol](./media/index_pagecontrol.png) | This style has a one-finger-high area on the bottom side of the index component container. Generally, this style is used together with a layout, and images which are located in a scrollable object. |

> **Note**
>
> Set the index orientation with the `elm_index_horizontal_set()` function.
> ```
> elm_index_horizontal_set(index, EINA_TRUE);
> ```
> For the `default` style, both orientations are supported, but for the `pagecontrol` style, only horizontal mode is available.

## Callbacks

You can register callback functions connected to the following signals for an index object.

**Table: Index callback signals**

| Signal          | Description                              | `event_info`                     |
|-----------------|------------------------------------------|----------------------------------|
| `changed`       | The selected index item changes.         | The selected item's data pointer |
| `delay,changed` | The selected index item changes, but after a small idling period. | The selected item's data pointer |
| `selected`      | The user selects an item by releasing the mouse button. | The selected item's data pointer |
| `level,up`      | The user moves a finger from the first level to the second level. | `NULL`                           |
| `level,down`    | The user moves a finger from the second level to the first level. | `NULL`                           |

> **Note**
>
> The signal list in the API reference can be more extensive, but only the above signals are actually supported in Tizen.

> **Note**
>
> Except as noted, this content is licensed under [LGPLv2.1+](http://opensource.org/licenses/LGPL-2.1).

## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
