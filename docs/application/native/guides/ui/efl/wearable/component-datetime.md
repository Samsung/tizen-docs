# Datetime

This feature is supported in wearable applications only.

The datetime component displays date and time values.

For more information, see the [Datetime](../../../../api/wearable/latest/group__Elm__Datetime.html) API.

**Figure: Datetime component**

![Datetime component](./media/datetime_wn.png)

**Figure: Datetime hierarchy**

![Datetime hierarchy](./media/datetime_tree.png)

## Adding a Datetime Component

To create a datetime component:

1. Add the datetime component with the `elm_datetime_add()` function.
2. Select the visible fields with the `elm_datetime_field_visible_set()` function.

   The visibility of the following fields can be controlled:
   - `ELM_DATETIME_YEAR`: Year field
   - `ELM_DATETIME_MONTH`: Month field
   - `ELM_DATETIME_DATE`: Date field
   - `ELM_DATETIME_HOUR`: Hour field
   - `ELM_DATETIME_MINUTE`: Minute field
   - `ELM_DATETIME_AMPM`: AM/PM field

## Using the Datetime Styles

The datetime has the following styles:

- `datepicker_layout`
- `timepicker_layout`

To set the style to, for example, `datepicker_layout`:

```
elm_object_style_set(datetime, "datepicker_layout");
```

## Setting the Datetime Format

The date and time format can be configured with the `elm_datetime_format_set()` function using a combination of allowed Libc date format specifiers.

To set the format to "HH : MM":

```
elm_object_style_set(datetime, "timepicker_layout");
elm_datetime_format_set(datetime, "%d/%b/%Y%I:%M");
```

For a complete list of available specifiers, see the [Datetime](../../../../api/wearable/latest/group__Elm__Datetime.html) API.

## Using the Datetime Callbacks

To receive notifications about the datetime events, listen for the following signals:

- `changed`: The datetime field values are changed.
- `language,changed`: The system locale changes.

> **Note**
>
> The signal list in the API reference can be more extensive, but only the above signals are actually supported in Tizen.

In both these signals, the `event_info` callback parameter is `NULL`.

To register and define a callback for the `changed` signal:

```
{
    evas_object_smart_callback_add(datetime, "changed", changed_cb, data);
}

/* Callback for the "changed" signal */
/* Called when the datetime fields change */
void
changed_cb(void *data, Evas_Object *obj, void *event_info)
{
    dlog_print(DLOG_INFO, LOG_TAG, "Datetime field changed. \n");
}
```

> **Note**
>
> Except as noted, this content is licensed under [LGPLv2.1+](http://opensource.org/licenses/LGPL-2.1).

## Related Information
- Dependencies
  - Tizen 2.3.1 and Higher for Wearable
