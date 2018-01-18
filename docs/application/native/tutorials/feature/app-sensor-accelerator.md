
# Accelerator Sensor Usage

The accelerator sensor can measure acceleration in the directions of the
X, Y, and Z axes. Before attempting to measure the acceleration values,
you need to know whether the device supports the accelerator sensor.


## Determining Whether the Sensor Is Supported

To determine whether the accelerator sensor is supported on the device:

1.  Create a new project in the Tizen Studio with the **Basic UI**
    template, and specify the project name as **SensorAccelerator**.

    For more information on how to create a project, see Creating a
    Project (in [mobile](../../getting-started/mobile/first-app.md#create) and
    [wearable](../../getting-started/wearable/first-app.md#creating-a-project) applications).

2. In the new project, open the `sensoraccelerator.c` source file in
    the `src` folder and add the required library header file and
    variables:

    -   The `sensor.h` file is a header file for various
        sensor libraries.
    -   The purpose of the application is to display whether the
        accelerator sensor is supported, the current acceleration value,
        and the maximum value of acceleration. As a result, a variable
        is defined for each of these values.

    ```c++
    #include "sensoraccelerator.h"
    #include <sensor.h>

    struct appdata {
        Evas_Object *win;
        Evas_Object *conform;
        Evas_Object *label0; /* Whether the accelerator sensor is supported */
        Evas_Object *label1; /* Current acceleration value */
        Evas_Object *label2; /* Maximum acceleration value */
    };
    typedef struct appdata appdata_s;
    ```

3. Create 2 new functions on top of the `create_base_gui()` function:

    -   The `show_is_supported()` function identifies whether the
        accelerator sensor is supported, and displays the result in the
        first label component.

        The `sensor_is_supported()` function requests the
        support information. Passing `SENSOR_ACCELEROMETER` as the first
        parameter makes the second parameter return the accelerator
        support information.

    - The `my_box_pack()` function adds a UI component to a
        box container.

    ```c++
    static void
    show_is_supported(appdata_s *ad)
    {
        char buf[PATH_MAX];
        bool is_supported = false;
        sensor_is_supported(SENSOR_ACCELEROMETER, &is_supported);
        sprintf(buf, "Acceleration Sensor is %s", is_supported ? "support" : "not support");
        elm_object_text_set(ad->label0, buf);
    }

    static void
    my_box_pack(Evas_Object *box, Evas_Object *child,
                double h_weight, double v_weight, double h_align, double v_align)
    {
        /* Tell the child packed into the box to be able to expand */
        evas_object_size_hint_weight_set(child, h_weight, v_weight);
        /* Fill the expanded area (above) as opposed to centering in it */
        evas_object_size_hint_align_set(child, h_align, v_align);
        /* Set the child as the box content and show it */
        evas_object_show(child);
        elm_object_content_set(box, child);

        /* Put the child into the box */
        elm_box_pack_end(box, child);
        /* Show the box */
        evas_object_show(box);
    }
    ```

4. To create the box, add the first and second label to the box, and
    call the `show_is_supported()` function to determine the sensor
    support, you must modify the source code at the bottom of the
    `create_base_gui()` function as follows:

    ```c++
    /* Conformant */
    /*
       Create and initialize elm_conformant
       elm_conformant is mandatory for the base GUI to have a proper size
       when the indicator or virtual keypad is visible
    */
    ad->conform = elm_conformant_add(ad->win);
    elm_win_indicator_mode_set(ad->win, ELM_WIN_INDICATOR_SHOW);
    elm_win_indicator_opacity_set(ad->win, ELM_WIN_INDICATOR_OPAQUE);
    evas_object_size_hint_weight_set(ad->conform, EVAS_HINT_EXPAND, EVAS_HINT_EXPAND);
    elm_win_resize_object_add(ad->win, ad->conform);
    evas_object_show(ad->conform);

    /* Box can contain other elements in a vertical line (by default) */
    Evas_Object *box = elm_box_add(ad->win);
    evas_object_size_hint_weight_set(box, EVAS_HINT_EXPAND, EVAS_HINT_EXPAND);
    evas_object_size_hint_align_set(box, EVAS_HINT_EXPAND, EVAS_HINT_EXPAND);
    elm_object_content_set(ad->conform, box);
    evas_object_show(box);

    /* First label (for the sensor support) */
    ad->label0 = elm_label_add(ad->conform);
    elm_object_text_set(ad->label0, "Msg -");
    my_box_pack(box, ad->label0, 1.0, 0.0, -1.0, -1.0);

    /* Second label (for the current acceleration value) */
    ad->label1 = elm_label_add(ad->conform);
    elm_object_text_set(ad->label1, "Value -");
    my_box_pack(box, ad->label1, 1.0, 1.0, -1.0, -1.0);

    /* Show the window after the base GUI is set up */
    evas_object_show(ad->win);

    /* Check the sensor support */
    show_is_supported(ad);
    ```

5. Build (in [mobile](../../getting-started/mobile/first-app.md#build) and
    [wearable](../../getting-started/wearable/first-app.md#building-your-application) applications) and run
    (in [mobile](../../getting-started/mobile/first-app.md#run) and
    [wearable](../../getting-started/wearable/first-app.md#running-your-application) applications)
    the application. If the accelerator sensor is supported, the
    **Accelerator Sensor is support** message is shown on the
    device screen.

    Not all smartphones support this sensor. In that case, test the
    application on the emulator.

    ![Accelerator Sensor is
    supported](./media/sensor_accelerator_supported.png)


## Requesting Sensor Events

To implement a feature that requests the corresponding event as you
shake the device, and displays the acceleration value on the screen:

1.  Add a structure for the sensor and a global variable to the top of
    the `sensoraccelerator.c` source file:

    -   The `sensorinfo_s` structure includes a sensor handle and an
        event listener variable.
    -   The `sensor_info` is a global variable of the
        `sensorinfo_s` structure.

    ```c++
    struct appdata {
        Evas_Object *win;
        Evas_Object *conform;
        Evas_Object *label0;
        Evas_Object *label1;
        Evas_Object *label2;
    };
    typedef struct appdata appdata_s;

    struct _sensor_info {
        sensor_h sensor; /* Sensor handle */
        sensor_listener_h sensor_listener; /* Sensor listener */
    };
    typedef struct _sensor_info sensorinfo_s;

    static sensorinfo_s sensor_info;
    ```

2. To request sensor events, you need a sensor handle and an event
    listener, and must start the listener. Create 2 new functions above
    the `create_base_gui()` function:

    -   The `_new_sensor_value()` function is an event callback for the
        accelerator sensor, and it outputs a new sensor value to
        the screen.

        The sensor data is passed to the second parameter, and the
        `values[0]` field contains the X axis data, `values[1]` contains
        the Y axis data, and `values[2]` contains the Z axis data.

    - The `start_accelerator_sensor()` function starts the accelerator
        sensor and specifies the event callback function:
        -   The `sensor_get_default_sensor()` function gets a specific
            sensor handle. Passing `SENSOR_ACCELEROMETER` to the first
            parameter returns an accelerator sensor handle to the
            second parameter.
        -   The `sensor_create_listener()` function creates an
            event listener. Passing a sensor handle to the first
            parameter returns a listener object to the second parameter.
        -   The `sensor_listener_set_event_cb()` function specifies a
            callback function to the listener. The parameters follow
            this order: event listener, interval (in milliseconds),
            callback function name, and user data.
        -   The `sensor_listener_start()` function starts the listener.

    ```c++
    static void
    _new_sensor_value(sensor_h sensor, sensor_event_s *sensor_data, void *user_data)
    {
        if (sensor_data->value_count < 3)
            return;
        char buf[PATH_MAX];
        appdata_s *ad = (appdata_s*)user_data;

        sprintf(buf, "Value -X : %0.1f / Y : %0.1f / Z : %0.1f",
                sensor_data->values[0], sensor_data->values[1], sensor_data->values[2]);
        elm_object_text_set(ad->label1, buf);
    }

    static void
    start_accelerator_sensor(appdata_s *ad)
    {
        sensor_error_e err = SENSOR_ERROR_NONE;
        sensor_get_default_sensor(SENSOR_ACCELEROMETER, &sensor_info.sensor);
        err = sensor_create_listener(sensor_info.sensor, &sensor_info.sensor_listener);
        sensor_listener_set_event_cb(sensor_info.sensor_listener, 100, _new_sensor_value, ad);
        sensor_listener_start(sensor_info.sensor_listener);
    }
    ```

3. To operate the event listener automatically when the application
    starts running, invoke the above `start_accelerator_sensor()`
    function at the end of the `create_base_gui()` function:

    ```c++
    /* Show the window after the base GUI is set up */
    evas_object_show(ad->win);

    show_is_supported(ad);
    start_accelerator_sensor(ad);
    ```

4. Run the application again. To test it on your smartphone, simply
    shake the device.

    To test on the emulator, use the [control
    panel](../../../tizen-studio/common-tools/emulator-control-panel.md):

    a.  Right-click the emulator and select **Control Panel**.

      ![Emulator Control        Panel](./media/sensor_accelerator_emulator.png)

    b. Click **Next** in the lower-right corner until you see the        **3-Axis** box.  
    c. Click the box and select the **Acceleration** tab.  
    d. Drag the 3 sliders one at a time. If the X, Y, and Z values        change on the application screen, it means you have correctly        received the acceleration data in your application.

      ![3-Axis Sensors](./media/sensor_accelerator_axis.png)


## Requesting the Maximum Acceleration Value

If you try to test the maximum acceleration value with your smartphone,
the characters are hardly visible when you are shaking the device. When
you stop shaking to see the value, the downward direction is 9.8, and
the rest show 0. For that reason, you need a separate feature that saves
the maximum value when testing on the device.

To access the maximum acceleration value:

1.  Declare an array variable in a number format at the top of the
    `sensoraccelerator.c` source file and reset it to 0. This variable
    saves the maximum acceleration value.

    ```c++
    struct _sensor_info {
        sensor_h sensor;
        sensor_listener_h sensor_listener;
    };
    typedef struct _sensor_info sensorinfo_s;

    static sensorinfo_s sensor_info;

    static float max_acc_value[3] = {0.f, 0.f, 0.f};
    ```

2. To create the third label and a button, add new code to the
    `create_base_gui()` function.

    When clicked, the button resets the maximum value to 0.

    ```c++
    /* Second label (for the current acceleration value) */
    ad->label1 = elm_label_add(ad->conform);
    elm_object_text_set(ad->label1, "Value -");
    my_box_pack(box, ad->label1, 1.0, 1.0, -1.0, -1.0);

    /* Button */
    Evas_Object *btn = elm_button_add(ad->conform);
    elm_object_text_set(btn, "Init Max Value");
    evas_object_smart_callback_add(btn, "clicked", btn_clicked_init_max_acc_value, ad);
    my_box_pack(box, btn, 1.0, 0.0, -1.0, -1.0);

    /* Third label (for the maximum value) */
    ad->label2 = elm_label_add(ad->conform);
    elm_object_text_set(ad->label2, "Max -");
    my_box_pack(box, ad->label2, 1.0, 1.0, 0.5, -1.0);
    ```

3. Create 2 new functions and add new code to the `_new_sensor_value()`
    function:

    -   The `get_absolute_max()` function compares 2 values and returns
        the higher one by changing 2 real numbers to absolute values.
    -   The new code in the `_new_sensor_value()` function saves the
        maximum values of the X, Y, and Z axis acceleration in the
        global variable and outputs them to the third label component.
    -   The `btn_clicked_init_max_acc_value()` function resets the
        maximum value saved in the global variable to 0 when you click
        the button.

    ```c++
    static float
    get_absolute_max(float value1, float value2)
    {
        float v1 = value1 > 0.f ? value1 : -value1;
        float v2 = value2 > 0.f ? value2 : -value2;
        float result = v1 > v2 ? v1 : v2;

        return result;
    }

    static void
    _new_sensor_value(sensor_h sensor, sensor_event_s *sensor_data, void *user_data)
    {
        if (sensor_data->value_count < 3)
            return;
        char buf[PATH_MAX];
        appdata_s *ad = (appdata_s*)user_data;

        sprintf(buf, "Value -X : %0.1f / Y : %0.1f / Z : %0.1f",
                sensor_data->values[0], sensor_data->values[1], sensor_data->values[2]);
        elm_object_text_set(ad->label1, buf);

        for (int i = 0; i < 3; i++)
            max_acc_value[i] = get_absolute_max(max_acc_value[i], sensor_data->values[i]);

        sprintf(buf, "Max -X: %0.1f / Y: %0.1f / Z: %0.1f",
                max_acc_value[0], max_acc_value[1], max_acc_value[2]);
        elm_object_text_set(ad->label2, buf);
    }

    /* Button click event function */
    static void
    btn_clicked_init_max_acc_value(void *data, Evas_Object *obj, void *event_info)
    {
        for (int i = 0; i < 3; i++)
            max_acc_value[i] = 0.f;
    }
    ```

4. Run the application again and shake the phone. When you stop
    shaking, the value in the second label is reset, but the maximum
    value remains intact in the third label.

    To measure a new value, click the button and shake again.

    ![Emulator Control
    Panel](./media/sensor_accelerator_max_value.png)
