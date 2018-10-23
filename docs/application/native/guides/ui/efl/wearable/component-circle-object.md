# Circle Object

This feature is supported in wearable applications only.

The circle object component extends Elementary components in a form of the circular design. Sometimes, the circle object merely provides additional UI features to an Elementary component, and sometimes it works as an independent component with its own UI and functionalities.

For more information, see the [Efl Extension Circle Object](../../../../api/wearable/latest/group__CAPI__EFL__EXTENSION__CIRCLE__OBJECT__MODULE.html) API.

## Adding a Circle Object Component

To create a circle object component, use the `eext_circle_object_add()` function:

```
Evas_Object *circle_obj;

circle_obj = eext_circle_object_add(parent, surface);
```

When creating a circle object, you can select whether the circle object is rendered by itself or by the [circle surface](component-circle-surface.md):

- If the circle surface is passed as the second parameter, a circle object connected with a circle surface is created, and it is rendered by the circle surface.
- If `NULL` is passed as the second parameter, the new circle object is managed and rendered by itself.

To create a circle object without a circle surface, and show it in a size of 360 x 360:

```
Evas_Object *circle_obj;

circle_obj = eext_circle_object_add(parent, NULL);
evas_object_size_hint_min_set(circle_obj, 360, 360);
evas_object_show(circle_obj);
```

## Setting the Value and Value Limits

To set the value details of the circle object:

- Set the maximum and minimum value:

  - To set the minimum and maximum values of the circle object, use the `eext_circle_object_value_min_max_set()` function.

    In the following example, a circle object with a surface is created and its minimum and maximum values are set to 0.0 and 10.0 degrees:

    ```
    Evas_Object *circle_obj;

    circle_obj = eext_circle_object_add(parent, surface);
    eext_circle_object_value_min_max_set(circle_obj, 0.0, 10.0);
    ```

    To get the current minimum and maximum values of the circle object, use the `eext_circle_object_value_min_max_get()` function.

  - To set the value of a certain item in a circle object, use the `eext_circle_object_item_angle_min_max_set()` function.

    If the name of the item is passed as `default`, the function works the same way as the `eext_circle_object_value_min_max_set()` function. Similar to the above example, the following example creates a circle object with the minimum and maximum values of 0.0 and 10.0 degrees:

    ```
    Evas_Object *circle_obj;

    circle_obj = eext_circle_object_add(parent, surface);
    eext_circle_object_item_value_min_max_set(circle_obj, "default", 0.0, 10.0);
    ```

    To get the current minimum and maximum values of the item, use the `eext_circle_object_item_value_min_max_get()` function.

- Set the value:

  > **Note**  
  > The value cannot be lower than the minimum value or higher than the maximum value.

  - To set the value of the circle object, use the `eext_circle_object_value_set()` function.

    In the following example, a circle object with a surface is created and its value is set to 5.0 degrees:

    ```
    Evas_Object *circle_obj;

    circle_obj = eext_circle_object_add(parent, surface);
    eext_circle_object_value_set(circle_obj, 5.0);
    ```

    To get the current value of the circle object, use the `eext_circle_object_value_get()` function.

  - To set the value of a certain item in a circle object, use the `eext_circle_object_item_value_set()` function.

    If the name of the item is passed as `default`, the function works the same way as the `eext_circle_object_value_set()` function. Similar to the above example, the following example creates a circle object with a surface and sets its value to 5.0 degrees:

    ```
    Evas_Object *circle_obj;

    circle_obj = eext_circle_object_add(parent, surface);
    eext_circle_object_item_value_set(circle_obj, "default", 5.0);
    ```

    To get the current value of the item, use the `eext_circle_object_item_value_get()` function.

## Setting the Angle Details

To set the angle details of the circle object:

- Set the angle:

  - To set the angle of the circle object, use the `eext_circle_object_angle_set()` function.

    In the following example, a circle object with a surface is created and its angle is set to 45.0 degrees:

    ```
    Evas_Object *circle_obj;

    circle_obj = eext_circle_object_add(parent, surface);
    eext_circle_object_angle_set(circle_obj, 45.0);
    ```

    To get the current angle of a circle object, use the `eext_circle_object_angle_get()` function.

  - To set the angle of a certain item in a circle object, use the `eext_circle_object_item_angle_set()` function.

    If the name of the item is passed as `default`, the function works the same way as the `eext_circle_object_angle_set()` function. Similar to the above example, the following example creates a circle object with a surface and sets its angle to 45.0 degrees:

    ```
    Evas_Object *circle_obj;

    circle_obj = eext_circle_object_add(parent, surface);
    eext_circle_object_item_angle_set(circle_obj, "default", 45.0);
    ```

    To get the current angle of the item, use the `eext_circle_object_item_angle_get()` function.

- Set the angle offset:

  - To set the angle offset of the circle object, use the `eext_circle_object_angle_offset_set()` function.

    In the following example, a circle object with a 45.0 degree angle is created and its angle offset is set to 30.0 degrees. As a result, the circle object has an arch of a 45.0 degree angle line starting from 30.0 degrees to 75.0 degrees.

    ```
    Evas_Object *circle_obj;

    circle_obj = eext_circle_object_add(parent, surface);
    eext_circle_object_angle_set(circle_obj, 45.0);
    eext_circle_object_angle_offset_set(circle_obj, 30.0);
    ```

    To get the current angle offset of a circle object, use the `eext_circle_object_angle_offset_get()` function.

  - To set the angle offset of a certain item in a circle object, use the `eext_circle_object_item_angle_offset_set()` function.

    If the name of the item is passed as `default`, the function works the same way as the `eext_circle_object_angle_offset_set()` function. The following example works the same way as the above example:

    ```
    Evas_Object *circle_obj;

    circle_obj = eext_circle_object_add(parent, surface);
    eext_circle_object_item_angle_set(circle_obj, "default", 45.0);
    eext_circle_object_item_angle_offset_set(circle_obj, "default", 30.0);
    ```

    To get the current angle of the item, use the `eext_circle_object_item_angle_offset_get()` function.

- Set the minimum and maximum angles:

  - To set the minimum and maximum angles of the circle object, use the `eext_circle_object_angle_min_max_set()` function.

    In the following example, a circle object with a surface is created and its minimum and maximum angles are set to 0.0 and 90.0 degrees:

    ```
    Evas_Object *circle_obj;

    circle_obj = eext_circle_object_add(parent, surface);
    eext_circle_object_angle_min_max_set(circle_obj, 0.0, 90.0);
    ```

    To get the current minimum and maximum angles of the circle object, use the `eext_circle_object_angle_min_max_get()` function.

  - To set the minimum and maximum angles of a certain item in a circle object, use the `eext_circle_object_item_angle_min_max_set()` function.

    If the name of the item is passed as `default`, the function works the same way as the `eext_circle_object_angle_min_max_set()` function. Similar to the above example, the following example creates a circle object with the minimum and maximum angles of 0.0 and 90.0:

    ```
    Evas_Object *circle_obj;

    circle_obj = eext_circle_object_add(parent, surface);
    eext_circle_object_item_angle_min_max_set(circle_obj, "default", 0.0, 90.0);
    ```

    To get the current minimum and maximum angles of the item, use the `eext_circle_object_item_angle_min_max_get()` function.

## Setting the Line Width, Color, and Radius

To set the line width, color, and radius of the circle object:

- Set the line width:

  - To set the line width of the circle object, use the `eext_circle_object_line_width_set()` function.

    In the following example, a circle object with a surface is created and its line width is set to 20:

    ```
    Evas_Object *circle_obj;

    circle_obj = eext_circle_object_add(parent, surface);
    eext_circle_object_line_width_set(circle_obj, 20);
    ```

    To get the current line width of a circle object, use the `eext_circle_object_line_width_get()` function.

  - To set the line width of a certain item in a circle object, use the `eext_circle_object_item_line_width_set()` function.

    If the name of the item is passed as `default`, the function works the same way as the `eext_circle_object_line_width_set()` function. Similar to the above example, the following example creates a circle object with a surface and sets its line width to 20:

    ```
    Evas_Object *circle_obj;

    circle_obj = eext_circle_object_add(parent, surface);
    eext_circle_object_item_line_width_set(circle_obj, "default", 20);
    ```

    To get the current line width of the item, use the `eext_circle_object_item_line_width_get()` function.

- Set the color:

  - To set the color of the circle object, use the `eext_circle_object_color_set()` function.

    To set the color, the red, green, blue, and alpha values in a range from 0 to 255 must be passed. In the following example, a circle object with a surface is created and its color is set to red:

    ```
    Evas_Object *circle_obj;

    circle_obj = eext_circle_object_add(parent, surface);
    eext_circle_object_color_set(circle_obj, 255, 0, 0, 255);
    ```

    To get the current color of the circle object, use the `eext_circle_object_color_get()` function.

  - To set the color of a certain item in a circle object, use the `eext_circle_object_item_color_set()` function.

    If the name of the item is passed as `default`, the function works the same way as the `eext_circle_object_color_set()` function. Similar to the above example, the following example creates a circle object with a surface and sets its color to red:

    ```
    Evas_Object *circle_obj;

    circle_obj = eext_circle_object_add(parent, surface);
    eext_circle_object_item_value_set(circle_obj, "default", 255, 0, 0, 255);
    ```

    To get the current color of the item, use the `eext_circle_object_item_color_get()` function.

- Set the radius:

  - To set the radius of the circle object, use the `eext_circle_object_radius_set()` function.

    In the following example, a circle object with a radius of 50.0 is created:

    ```
    Evas_Object *circle_obj;

    circle_obj = eext_circle_object_add(parent, surface);
    eext_circle_object_radius_set(circle_obj, 50.0);
    ```

    To get the current radius of the circle object, use the `eext_circle_object_radius_get()` function.

  - To set the radius of a certain item in a circle object, use the `eext_circle_object_item_radius_set()` function.

    If the name of the item is passed as `default`, the function works the same way as the `eext_circle_object_radius_set()` function. Similar to the above example, the following example creates a circle object with a radius of 50.0:

    ```
    Evas_Object *circle_obj;

    circle_obj = eext_circle_object_add(parent, surface);
    eext_circle_object_item_radius_set(circle_obj, "default", 50.0);
    ```

    To get the current radius of the item, use the `eext_circle_object_item_radius_get()` function.

## Disabling the Circle Object

To disable the circle object, use the `eext_circle_object_disabled_set()` function:

```
Evas_Object *circle_obj;

circle_obj = eext_circle_object_add(parent, surface);
eext_circle_object_disabled_set(circle_obj, EINA_TRUE);
```

To enable a disabled circle object, use the same function with the `EINA_FALSE` parameter.

To get the current disabled status of the circle object, use the `eext_circle_object_disabled_get()` function.

## Related Information
- Dependencies
  - Tizen 2.3.1 and Higher for Wearable
