# Conformant

The conformant container accounts for the space taken by the indicator, virtual keyboard, and softkey windows. The content area of the conformant is resized and positioned based on the space available. For more information, see the Conformant API (in [mobile](../../../api/mobile/latest/group__Elm__Conformant.html) and [wearable](../../../api/wearable/latest/group__Elm__Conformant.html) applications).

**Figure: Conformant component structure**

![Conformant component structure](./media/conformant.png)

## Basic Usage

To build a layout with a conformant:

1. Add a conformant with the `elm_conformant_add()` function:

   ```
   Evas_Object *conformant;

   conformant = elm_conformant_add(parent);
   ```

2. Add an object to the conformant with the `elm_object_content_set()` function:

   ```
   Evas_Object *main_view;

   elm_object_content_set(conformant, main_view);
   ```

## Callbacks

You can register callback functions connected to the following signals for a conformant object.

**Table: Conformant callback signals**

| Signal                       | Description                              | `event_info` |
|----------------------------|----------------------------------------|------------|
| `virtualkeypad,state,on`     | The virtual keyboard has been switched on. | `NULL`       |
| `virtualkeypad,state,off`    | The virtual keyboard has been switched off. | `NULL`       |
| `virtualkeypad,size,changed` | The virtual keyboard size has changed.   | `NULL`       |
| `clipboard,state,on`         | The clipboard has been switched on.      | `NULL`       |
| `clipboard,state,off`        | The clipboard has been switched off.     | `NULL`       |

> **Note**  
> The signal list in the API reference can be more extensive, but only the above signals are actually supported in Tizen.

> **Note**  
> Except as noted, this content is licensed under [LGPLv2.1+](http://opensource.org/licenses/LGPL-2.1).

## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
