# Ctxpopup

This feature is supported in wearable applications only.

The context popup (ctxpopup) component is a contextual popup that can show a list of items inside it.

For more information, see the [Ctxpopup](../../../../api/wearable/latest/group__Elm__Ctxpopup.html) API.

**Figure: Ctxpopup component**

![Ctxpopup component](./media/ctxpopup_wn.png)

**Figure: Ctxpopup hierarchy**

![Ctxpopup hierarchy](./media/ctxpopup_tree.png)

## Adding a Ctxpopup Component

To create a ctxpopup component, use the `elm_ctxpopup_add()` function:

```
Evas_Object *ctxpopup;
Evas_Object *parent;

/* Create a ctxpopup */
ctxpopup = elm_ctxpopup_add(parent);
```

When shown, the ctxpopup automatically selects an area inside its parent object's view to optimally fit into it. Set the object view with the `elm_ctxpopup_hover_parent_set()` function.

## Using the Ctxpopup Styles

The ctxpopup has the following styles for the rectangular screen:

- `default`

  The ctxpopup has the following styles for the circular screen:

- `select_mode`

- `select_mode/top`, `select_mode/bottom`

  These 2 styles can be used as a pair.

To set the style to, for example, `default`:

```
elm_object_style_set(ctxpopup, "default");
```

## Configuring the Ctxpopup

To configure the ctxpopup:

- Set the ctxpopup orientation with the `elm_ctxpopup_horizontal_set()` function.

  In the following example, the orientation is set to horizontal:

  ```
  elm_ctxpopup_horizontal_set(ctxpopup, EINA_TRUE);
  ```

- Disable auto hiding.

  The ctxpopup can be hidden automatically when its parent is resized. The auto hide functionality is enabled by default. You can disable auto hiding by calling the `elm_ctxpopup_auto_hide_disabled_set()` function with `EINA_TRUE`:

  ```
  elm_ctxpopup_auto_hide_disabled_set(ctxpopup, EINA_TRUE);
  ```

## Managing the Ctxpopup Items

The ctxpopup can contain a small number of items. Each item can have a label, an icon, or both.

To manage the ctxpopup items:

1. Add an item with the `elm_ctxpopup_item_append()` function.

   To append an item with a `test` label, no icon, and the `clicked` callback (`_ctxpopup_item_cb`):

   ```
   Elm_Object_Item *it;

   it = elm_ctxpopup_item_append(ctxpopup, "test", NULL, _ctxpopup_item_cb, NULL);
   ```

2. Change the item label and icon:

   - To change the item label to `New label`:
     ```
     elm_object_item_part_text_set(it, "default", "New label");
     ```

   - To set the icon to the standard `home` icon:

     ```
     Evas_Object *home_icon = elm_icon_add(ctxpopup);
     elm_icon_standard_set(home_icon, "home");

     elm_object_item_part_content_set(it, "icon", home_icon);
     ```

3. Define a callback that is triggered when the item is clicked:

   ```
   static void
   _ctxpopup_item_cb(void *data, Evas_Object *obj, void *event_info)
   {
       dlog_print(DLOG_INFO, LOG_TAG, "ctxpopup item selected\n");
   }
   ```

## Using the Ctxpopup Callbacks

To receive notifications about the ctxpopup events, listen for the `dismissed` signal, which is called when the ctxpopup is dismissed.

> **Note**
>
> The signal list in the API reference can be more extensive, but only the above signals are actually supported in Tizen.

The `event_info` callback parameter is `NULL`.

To register and define a callback for the `dismissed` signal:

```
{
    evas_object_smart_callback_add(ctxpopup, "dismissed", dismissed_cb, data);
}

/* Callback for the "dismissed" signal */
/* Called when the ctxpopup is dismissed */
void
dismissed_cb(void *data, Evas_Object *obj, void *event_info)
{
    dlog_print(DLOG_INFO, LOG_TAG, "Ctxpopup dismissed\n");
}
```

> **Note**
>
> Except as noted, this content is licensed under [LGPLv2.1+](http://opensource.org/licenses/LGPL-2.1).

## Related Information
- Dependencies
  - Tizen 2.3.1 and Higher for Wearable
