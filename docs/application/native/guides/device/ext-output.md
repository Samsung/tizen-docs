# External Output Devices


The External Output Manager (EOM) is a module for controlling the external output devices.

The main features of the External Output Manager API include:

- Managing modes

  - The mirror mode is the default mode. If a mode is not specified, the EOM uses the mirror mode when an external output device is connected.

    **Figure: Mirror mode**

    ![Mirror mode](./media/eom_mirror_mode.png)

  - The presentation mode can be set by an application. If the application wants to display an image or video only on an external output device, the presentation mode must be used.

    **Figure: Presentation mode**

    ![Presentation mode](./media/eom_presentation_mode.png)

    You must use the EOM attributes to set the presentation mode by defining the EOM priority. With these attributes, you can display a fullscreen window on the external output device.

    **Table: Presentation mode attributes**

    | Attribute                              | Description                              |
    |----------------------------------------|------------------------------------------|
    | `EOM_OUTPUT_ATTRIBUTE_NORMAL`          | This priority can be set, if the current priority is none (mirror mode) or `NORMAL`.<br> This priority cannot be set, if the current priority is `EXCLUSIVE_SHARE` or `EXCLUSIVE`. |
    | `EOM_OUTPUT_ATTRIBUTE_EXCLUSIVE_SHARE` | This priority can be set, if the current priority is none (mirror mode), `NORMAL`, or `EXCLUSIVE_SHARE`.<br> This priority cannot be set, if the current priority is `EXCLUSIVE`. |
    | `EOM_OUTPUT_ATTRIBUTE_EXCLUSIVE`       | This priority can be set, if the current priority is none (mirror mode), `NORMAL`, or `EXCLUSIVE`.<br> This priority cannot be set, if the current priority is `EXCLUSIVE_SHARE`. |

    In most applications, the `EOM_OUTPUT_ATTRIBUTE_NORMAL` priority is the best option.

- Receiving notifications

  The EOM can send a notification event to the application. The EOM tracks several changes, such as additions and removals in the external output, mode changes, and attribute state changes, and can notify the application about them.

- Getting information about the external output device

  You can [get information about the external output device](#getstatus) by using various functions. For example, to [get the ID of the external output device](#getid), use the `eom_get_eom_output_ids()` function, and to get attribute information, use the `eom_get_output_attribute()` function.

- Setting the external output

  The application can set information (such as attributes and window size) in the EOM.

  Use the `eom_set_output_attribute()` function to [set the presentation mode](#presentation), and use the `eom_set_output_window()` function to [set the window to the external output](#setwin) with the best resolution of the external output device.

## Prerequisites

To enable your application to use the EOM functionality:

1. To use the functions and data types of the External Output Manager API (in [mobile](../../api/mobile/latest/group__CAPI__UI__EOM__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__UI__EOM__MODULE.html) applications), include the `<eom.h>` header file in your application:

    ```
    #include <eom.h>
    ```

2. Initialize the application with the `eom_init()` function.

<a name="getid"></a>
## Getting the Output ID

To retrieve the output ID, use the `eom_get_eom_output_ids()` function. You need the ID to get information about the output device and to control the external window.

```
int
sample_get_output_id(const char *output_name)
{
    eom_output_id *output_ids = NULL;
    eom_output_id output_id = 0;
    eom_output_type_e output_type = EOM_OUTPUT_TYPE_UNKNOWN;
    int id_cnt = 0;
    int i;

    output_ids = eom_get_eom_output_ids(&id_cnt);
    if (id_cnt == 0) {
        printf("no external outputs supported\n");

        return 0;
    }

    for (i = 0; i < id_cnt; i++) {
        eom_get_output_type(output_ids[i], &output_type);
        if (!strncmp(output_name, "HDMI", 4)) {
            if (output_type == EOM_OUTPUT_TYPE_HDMIA || output_type == EOM_OUTPUT_TYPE_HDMIB) {
                output_id = output_ids[i];
                break;
            }
        } else if (!strncmp(output_name, "Virtual", 7)) {
            if (output_type == EOM_OUTPUT_TYPE_VIRTUAL) {
                output_id = output_ids[i];
                break;
            }
        }
    }

    if (output_ids)
        free(output_ids);

    return output_id;
}
```

<a name="presentation"></a>
## Setting the Presentation Mode

To connect to an external output device in the presentation mode, use the `eom_set_output_attribute()` function to set the presentation mode priority attribute.

If the setting is successful, the External Output Manager module uses the presentation mode when the external output device connected.

```
int
set_attribute()
{
    m_output_id output_id = 0;
    int ret;

    output_id = sample_get_output_id("HDMI");

    ret = eom_set_output_attribute(output_id, EOM_OUTPUT_ATTRIBUTE_NORMAL);
    if (ret != EOM_ERROR_NONE) {
        /* Attribute setting failed, the external output device cannot be used */
        /* Deinitializing */
        eom_deinit();

        return -1;
    }

    return 0;
}
```

If the `EOM_ERROR_NONE` response is received from the `eom_set_output_attribute()` function, the application can use the external output device.

<a name="setwin"></a>
## Setting the External Window

To set an external window, use the `eom_set_output_window()` function. This function moves the window to the external output and automatically resizes it to the best resolution of the external output device.

Before calling this function, you must receive a success return from the `eom_set_output_attribute()` function.

```
int
make_external_window()
{
    Evas_Object *window;
    window = elm_win_add(NULL, "external_window", ELM_WIN_BASIC);
    if (eom_set_output_window(output_id, window) == EOM_ERROR_NONE) {
        return 0;
    } else {
        evas_object_del(window);

        return -1;
    }
}
```

<a name="getstatus"></a>
## Getting the Status of the External Output Device

To get information about the external output device:

- You can retrieve information about the external output device details with the following functions:

  - `eom_get_output_type()`: Get the connection type of the external output.
  - `eom_get_output_mode()`: Get the external output mode.

    The mirror mode is the default mode. If the `eom_set_output_attribute()` function has executed successfully, the external output works in the presentation mode.
  - `eom_get_output_attribute()`: Get the presentation mode priority attribute information.
  - `eom_get_output_attribute_state()`: Get the attribute state information.

    If the application sets the attribute, the EOM sends the current attribute state to the application:
      - `ACTIVE`: The application can use the external output.
      - `INACTIVE`: The application was disconnected from the external output.
      - `LOST`: The application cannot use the external output because another application has set the attribute. The application cannot receive the attribute state anymore.

  - `eom_get_output_resolution()`: Get the best resolution of the external output device.
  - `eom_get_output_physical_size()`: Get the physical size of the external output device.

- You can receive notifications about state changes on the external output device:

  1. Define the callbacks for various state changes:

     ```
     struct _SampleInfo {
         Evas_Object *external_window;
         int output_id;
     };
     typedef struct _SampleInfo SampleInfo;

     /* Triggered when the external output is connected */
     static void
     sample_notify_cb_output_add(eom_output_id output_id, void *user_data)
     {
         SampleInfo *info = (SampleInfo*)user_data;
         if (!info->external_window) {
             /* Create the external window */
             make_external_window(info->external_window);
         }
     }

     /* Triggered when the external output is disconnected */
     static void
     sample_notify_cb_output_remove(eom_output_id output_id, void *user_data)
     {
         SampleInfo *info = (SampleInfo*)user_data;
         if (!info->external_window) {
             evas_object_del(info->external_window)
             info->external_window = NULL;
         }
     }

     /* Triggered when the state of the EOM output attribute changes */
     static void
     sample_notify_cb_attribute_changed(eom_output_id output_id, void *user_data)
     {
         SampleInfo *info = (SampleInfo*)user_data;
         eom_output_attribute_e attribute = EOM_OUTPUT_ATTRIBUTE_NONE;
         eom_output_attribute_state_e state = EOM_OUTPUT_ATTRIBUTE_STATE_NONE;

         eom_get_output_attribute(output_id, &attribute);
         eom_get_output_attribute_state(output_id, &state);

         if (state == EOM_OUTPUT_ATTRIBUTE_STATE_ACTIVE) {
             /*
                Start displaying the image to the external output
                (info->external_window);
             */
         } else if (state == EOM_OUTPUT_ATTRIBUTE_STATE_INACTIVE) {
             /* Stop displaying the image */
             /* Destroy the external_window */
             if (info->external_window) {
                 evas_object_del(info->external_window);
                 info->external_window = NULL;
             }
         } else if (state == EOM_OUTPUT_ATTRIBUTE_STATE_LOST) {
             /* Stop displaying the image */
             /* Destroy the external_window */
             if (info->external_window) {
                 evas_object_del(info->external_window);
                 info->external_window = NULL;
             }
             /* Remove the callbacks */
             eom_unset_output_added_cb(sample_notify_cb_output_add);
             eom_unset_output_removed_cb(sample_notify_cb_output_remove);
             eom_unset_attribute_changed_cb(sample_notify_cb_attribute_changed);
             eom_deinit();
         }
     }
     ```

     You can also define the `eom_mode_change_cb` callback to be triggered when the EOM output mode changes.

  2. Register the callbacks:

     ```
     int
     elm_main()
     {
         SampleInfo *info;
         eom_output_mode_e output_mode = EOM_OUTPUT_MODE_NONE;
         int ret;

         info = calloc(sizeof(SampleInfo));

         eom_init();
         info->output_id = sample_get_output_id("HDMI");

         ret = eom_set_output_attribute(info->hdmi_output_id, EOM_OUTPUT_ATTRIBUTE_NORMAL);
         if (ret != EOM_ERROR_NONE) {
             /* Cannot use the external output device */
             eom_deinit();
         } else {
             eom_get_output_mode(info->output_id, &output_mode);
             if (output_mode != EOM_OUTPUT_MODE_NONE) {
                 /* Create the external window */
                 make_external_window(info->external_window);
             }

             /* Add the callbacks */
             eom_set_output_added_cb(sample_notify_cb_output_add, info);
             eom_set_output_removed_cb(sample_notify_cb_output_remove, info);
             eom_set_attribute_changed_cb(sample_notify_cb_attribute_changed, info);
         }

         elm_run();
     ```

     To register the `eom_mode_change_cb` callback, use the `eom_set_mode_changed_cb()` function.

  3. When no longer needed, delete the callbacks:

     ```
         eom_unset_output_added_cb(sample_notify_cb_output_add);
         eom_unset_output_removed_cb(sample_notify_cb_output_remove);
         eom_unset_attribute_changed_cb(sample_notify_cb_attribute_changed);
         eom_deinit();
         elm_shutdown();

         return 0;
     }
     ```

     To delete the `eom_mode_change_cb` callback, use the `eom_unset_mode_changed_cb()` function.


## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 3.0 and Higher for Wearable
