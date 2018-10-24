# Notify

The notify UI component displays a container in a particular region of the parent object. It can receive some content, and become automatically hidden after a certain amount of time. The [popup](component-popup.md) component is very similar to the notify component, but supports many common layouts. For more information, see the [Notify](../../../../api/mobile/latest/group__Elm__Notify.html) API.

This feature is supported in mobile applications only.

## Basic Usage

To use a notify component in your application:

1. Add a notify component with the `elm_notify_add()` function:

   ```
   Evas_Object *notify;

   notify = elm_notify_add(parent);
   ```

2. Fill the layout:

   - Add an object to fill the layout:

     ```
     Evas_Object *label = elm_label_add(parent);
     ```

   - Set an object to the notify component with the `elm_object_content_set()` function:

     ```
     elm_object_content_set(notify, label);
     ```

3. Register the [callback](#callbacks) functions.

   The following example shows how to define and register a callback for the `timeout` signal:

   ```
   evas_object_smart_callback_add(notify, "timeout", timeout_cb, data);

   void
   timeout_cb(void *data, Evas_Object *obj, void *event_info)
   {
       dlog_print(DLOG_INFO, LOG_TAG, "Notify timeout");
   }
   ```

The following example shows a simple use case of the notify component.

**Example: Notify use case**

![Notify](./media/notify1.png)

```
Evas_Object *win;
Evas_Object *conf;
Evas_Object *notify;
Evas_Object *label;

/* Starting right after the basic EFL UI layout code */
/* (win - conformant) */

/* Add a notify component to contain a label to the conformant */
notify = elm_notify_add(conf);
elm_notify_align_set(notify, ELM_NOTIFY_ALIGN_FILL, 1.0);
elm_notify_timeout_set(notify, 5.0);

/* Add a label to notify */
label = elm_label_add(notify);
elm_object_test_set(label, "A label in notify");
evas_object_show(label);
elm_object_content_set(notify, label);

evas_object_show(notify);
```

## Features

You can use the align and timeout features with the notify component:

- Align

  Using the `elm_notify_align_set()` function, you can set the notify component alignment.

  The second and third parameters have a value between 0.0 and 1.0, meaning the alignment of the notify component's position within the parent window. The `ELM_NOTIFY_ALIGN_FILL` value can be used to fill the notify component in each axis direction.

  To align the notify object to the bottom center of the parent object:

  ```
  elm_notify_align_set(notify, 0.5, 1.0);
  ```

- Timeout

  The notify component can set a timeout interval, after which the notify component is hidden.

  To set the timeout interval to 5 seconds:

  ```
  elm_notify_timeout_set(notify, 5.0);
  ```

## Callbacks

You can register callback functions connected to the following signals for a notify object.

**Table: Notify callback signals**

| Signal          | Description                              | `event_info` |
|-----------------|------------------------------------------|--------------|
| `timeout`       | The timeout count ends and the notify component is hidden. | `NULL`       |
| `block,clicked` | The user clicks outside the notify component. | `NULL`       |

> **Note**
>
> The signal list in the API reference can be more extensive, but only the above signals are actually supported in Tizen.

> **Note**
>
> Except as noted, this content is licensed under [LGPLv2.1+](http://opensource.org/licenses/LGPL-2.1).

## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
