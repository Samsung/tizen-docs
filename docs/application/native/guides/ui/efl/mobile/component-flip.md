# Flip

The flip UI component is used for a transition effect, which can hold 2 `Evas_Objects` and flip between them using several predefined animations. For more information, see the [Flip](../../../../api/mobile/latest/group__Elm__Flip.html) API.

This feature is supported in mobile applications only.

**Figure: Flip hierarchy**

![Flip hierarchy](./media/flip_tree.png)

## Basic Usage

To use a flip component in your application:

1. Add a flip with the `elm_flip_add()` function:

   ```
   Evas_Object *flip;

   flip = elm_flip_add(parent);
   ```

2. Add content to the flip using the `elm_object_part_content_set()` function. Use the `front` and `back` part names to define the 2 `Evas_Objects` used as content:

   ```
   elm_object_part_content_set(flip, "front", content1);
   elm_object_part_content_set(flip, "back", content2);
   ```

3.  Run a flip animation using the `elm_flip_go()` function. The `ELM_FLIP_CUBE_UP` animation mode flips up the `front` content object as if it was on a side of a cube, letting the down facing side of the cube appear with the `back` content object. For a complete list of animation modes, see [elm\_flip\_go() Remarks](../../../../api/mobile/latest/group__Elm__Flip.html#ga24518d66196b5b634a207fd02e09250e).

   ```
   elm_flip_go(flip, ELM_FLIP_CUBE_UP);
   ```

4. Register the [callback](#callbacks) functions.

   The following example shows how to define and register a callback for the `animate,begin` signal.

   ```
   evas_object_smart_callback_add(entry, "animate,begin", anim_start_cb, data);

   void
   anim_start_cb(void *data, Evas_Object *obj, void *event_info)
   {
       dlog_print(DLOG_INFO, LOG_TAG, "Animation starts\n");
   }
   ```

## User Interactions

By default, the user cannot interact with the flip. You can set the interaction to be possible, but you have to define some interaction settings as well.

To set interaction settings to enable the user to interact with the flip:

- Select which animation appears on the interaction.

  To set the rotation animation:

  ```
  elm_flip_interaction_set(flip, ELM_FLIP_INTERACTION_ROTATE);
  ```

  For a complete list of interaction modes, see [elm\_flip\_interaction\_set() Remarks](../../../../api/mobile/latest/group__Elm__Flip.html#ga9d1b9214b24f3eb7c5066f2980780e23).

- Select which interaction directions are enabled.

  To enable the right and left directions only:

  ```
  elm_flip_interaction_direction_enabled_set(flip, ELM_FLIP_DIRECTION_LEFT, EINA_TRUE);
  elm_flip_interaction_direction_enabled_set(flip, ELM_FLIP_DIRECTION_RIGHT, EINA_TRUE);
  ```

- Set the amount of the flip that is sensitive to user interaction.

  To set the entire flip sensitive (to make the flip easy to interact with), use the amount `1`:

  ```
  elm_flip_interaction_direction_hitsize_set(flip, ELM_FLIP_DIRECTION_LEFT, 1);
  elm_flip_interaction_direction_hitsize_set(flip, ELM_FLIP_DIRECTION_RIGHT, 1);
  ```

## Callbacks

You can register callback functions connected to the following signals for a flip object.

**Table: Flip callback signals**

| Signal          | Description                     | `event_info` |
|---------------|-------------------------------|------------|
| `animate,begin` | The flip animation is started.  | `NULL`       |
| `animate,done`  | The flip animation is finished. | `NULL`       |

> **Note**  
> The signal list in the API reference can be more extensive, but only the above signals are actually supported in Tizen.

> **Note**  
> Except as noted, this content is licensed under [LGPLv2.1+](http://opensource.org/licenses/LGPL-2.1).

## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
