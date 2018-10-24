# Circle Genlist

This feature is supported in wearable applications only.

The circle genlist component is used to visualize and utilize the scroll effect for the [genlist](component-genlist.md) component (`elm_genlist`). While the `elm_genlist` component provides a scrollbar with straight horizontal and vertical movement, the circle genlist provides a scrollbar with circular movement. It is also operated with rotary events to move to the next or previous item.

For more information, see the [Efl Extension Circle Genlist](../../../../api/wearable/latest/group__CAPI__EFL__EXTENSION__CIRCLE__GENLIST__MODULE.html) API.

**Figure: Circle genlist component**

![Circle genlist component](./media/circle_genlist.png)

## Adding a Circle Genlist Component

To create a circle genlist component, use the `eext_circle_object_genlist_add()` function. Pass a genlist and [circle surface](component-circle-surface.md) to the function as parameters.

```
Evas_Object *genlist;
Evas_Object *circle_genlist;
Evas_Object *parent;

genlist = elm_genlist_add(parent);
circle_genlist = eext_circle_object_genlist_add(genlist, surface);
```

## Configuring the Circle Genlist

To set the circle genlist scroller policy, use the `eext_circle_object_genlist_scroller_policy_set()` function. The scroller policy can be:

- `ELM_SCROLLER_POLICY_AUTO`: Scrollbar is made visible if it is needed, and otherwise kept hidden.
- `ELM_SCROLLER_POLICY_ON`: Scrollbar is always visible.
- `ELM_SCROLLER_POLICY_OFF`: Scrollbar is always hidden.

The following example sets the horizontal scrollbar off and the vertical scrollbar always on:

```
eext_circle_object_genlist_scroller_policy_set(circle_genlist,
                                               ELM_SCROLLER_POLICY_OFF,
                                               ELM_SCROLLER_POLICY_ON);
```

## Activating a Rotary Event

To activate or deactivate the circle genlist, use the `eext_rotary_object_event_activated_set()` function:

```
eext_rotary_object_event_activated_set(circle_genlist, EINA_TRUE);
```

If the second parameter is `EINA_TRUE`, the circle genlist can receive rotary events.

## Configuring the Circle Properties

To configure the circle properties of the circle genlist:

- You can modify the circle object within the circle genlist component using the following functions:

  - `eext_circle_object_line_width_set()`
  - `eext_circle_object_line_width_get()`
  - `eext_circle_object_radius_set()`
  - `eext_circle_object_radius_get()`
  - `eext_circle_object_color_set()`
  - `eext_circle_object_color_get()`
  - `eext_circle_object_disabled_set()`
  - `eext_circle_object_disabled_get()`

- You can modify the circle genlist item properties with the `eext_circle_object_item_XXX()` functions.

  The circle genlist has the following items:

  - `default`: Default circle item that draws a vertical scroll bar.
  - `vertical,scroll,bg`: Vertical scroll background circle item.

For more information, see [Circle Object](component-circle-object.md) and the [Efl Extension Circle Object](../../../../api/wearable/latest/group__CAPI__EFL__EXTENSION__CIRCLE__OBJECT__MODULE.html) API.

## Related Information
- Dependencies
  - Tizen 2.3.1 and Higher for Wearable
