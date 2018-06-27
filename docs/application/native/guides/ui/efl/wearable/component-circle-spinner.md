# Circle Spinner

This feature is supported in wearable applications only.

The circle spinner component extends the spinner component (`elm_spinner`) by visualizing its value. The circle spinner increases or decreases the value of the `elm_spinner` through a clockwise or counter-clockwise rotary event.

**Figure: Circle spinner component**

![Circle spinner component](./media/circle_spinner.png)

## Adding a Circle Spinner Component

To create a circle spinner component:

1. Create an `elm_spinner` object:

   ```
   Evas_Object *spinner;
   Evas_Object *circle_spinner;

   spinner = elm_spinner_add(parent);
   ```

2. Set the object style as `circle`:

   ```
   elm_object_style_set(spinner, "circle");
   ```

3. Create an `eext_spinner` object using the `eext_circle_object_spinner_add()` function.

   Pass a [circle surface](component-circle-surface.md) as the second parameter.

   ```
   circle_spinner = eext_circle_object_spinner_add(spinner, surface);
   ```

The circle spinner component is created with the `default` style.

## Configuring the Circle Spinner

The circle spinner shows the `elm_spinner` value through a marker, which indicates the value in the round. It has internal minimum and maximum spinner values, and it calculates the minimum and maximum angles to draw the marker. The current value of the circle spinner is calculated internally as well.

To handle the circle spinner value, use the `elm_spinner` functions. They are automatically synchronized with the user values. You can also use the `elm_spinner` callback functions.

To customize the angle offset of the marker to not to follow the internally-calculated system value:

1. Set the custom circle spinner angle value using the `eext_circle_object_spinner_angle_set()` function.

   In the following example, the circle spinner angle value is set to 2.0:

   ```
   eext_circle_object_spinner_angle_set(circle_spinner, 2.0);
   ```

2. After the `eext_circle_object_spinner_angle_set()` function has been executed, the calculation formula for the angle offset is changed:

   ```
   /* Formula for calculating the default angle offset */
   (360/ max - min) * step

   /* Formula for calculating the angle offset with the new angle value */
   (360/ max - min) * step * 2.0
   ```

You can also use the above function to define the angle offset per each rotary callback.

## Activating a Rotary Event

To activate or deactivate the circle spinner, use the `eext_rotary_object_event_activated_set()` function:

```
eext_rotary_object_event_activated_set(circle_spinner, EINA_TRUE);
```

If the second parameter is `EINA_TRUE`, the circle spinner can receive rotary events.

## Configuring the Circle Properties

To configure the circle properties of the circle spinner:

- You can modify the circle object within the circle spinner component using the various functions, such as:

  - `eext_circle_object_value_min_max_set()`
  - `eext_circle_object_value_min_max_get()`
  - `eext_circle_object_value_set()`
  - `eext_circle_object_value_get()`

- You can modify the circle spinner `default` item, which draws the marker.

  To change the item properties, use the `eext_circle_object_item_XXX()` functions.

For more information, see [Circle Object](component-circle-object.md) and the [Efl Extension Circle Object](../../../../api/wearable/latest/group__CAPI__EFL__EXTENSION__CIRCLE__OBJECT__MODULE.html) API.

## Related Information
- Dependencies
  - Tizen 2.3.1 and Higher for Wearable
