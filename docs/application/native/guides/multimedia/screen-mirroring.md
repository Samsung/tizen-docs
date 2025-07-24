# Screen Mirroring


You can mirror the device screen and sound to another device wirelessly using the screen mirroring feature. Tizen follows the Wi-Fi Display Technical Specification and supports the feature as a sink, which receives shared data from a source device that supports the Wi-Fi Display, and displays it. Remember to prepare your application to use the screen mirroring sink functionality and set up the necessary callbacks before you start, and release the resources when you are done.

This feature is supported in mobile applications only.

The main features of the Screen Mirroring API include:

- Managing the connection to the screen mirroring source

  You can [connect to a screen mirroring source](#connect), and start, pause, and resume the screen mirroring sink. [Disconnect and release the resources](#release) when you are done.

- Setting the properties

  You can [set the resolution or display for the mirror](#prepare).

- Monitoring state changes in the screen mirroring sink

  To track state changes, you can register a callback with the `scmirroring_sink_set_state_changed_cb()` function. The callback is triggered when the screen mirroring state changes or an error occurs.

  Since all functions that change the state are synchronous (except for `scmirroring_sink_connect()`, `scmirroring_sink_start()`, `scmirroring_sink_pause()`, and `scmirroring_sink_resume()`) most function results are passed to the application through the callback mechanism.

  You can also [handle exceptions](#handle) if any occur.

The following figures illustrates the state and function call diagrams of the screen mirroring sink.

**Figure: State diagram**

![State diagram](./media/capi_media_screen_mirroring_sink_state_diagram.png)

**Figure: Function call diagram**

![Function call diagram](./media/screen_mirroring_sink_call_diagram.png)

## Prerequisites

To enable your application to use the screen mirroring functionality:

1. To use the functions and data types of the [Screen Mirroring](../../api/mobile/latest/group__CAPI__MEDIA__SCREEN__MIRRORING__MODULE.html) API, include the `<scmirroring_type.h>` and `<scmirroring_sink.h>` header files in your application:

   ```
   #include <scmirroring_type.h>
   #include <scmirroring_sink.h>
   ```

2. Create a handle for the screen mirroring sink using the `scmirroring_sink_create()` function.

   The function sets the screen mirroring state to `SCMIRRORING_STATE_NULL`.

   ```
   static scmirroring_sink_h g_scmirroring;

   static int
   init_scmirroring_sink()
   {
       int ret = SCMIRRORING_ERROR_NONE;
       ret = scmirroring_sink_create(&g_scmirroring);
       if (ret != SCMIRRORING_ERROR_NONE) {
           dlog_print(DLOG_ERROR, LOG_TAG, "scmirroring_sink_create failed [%d]", ret);

           return FALSE;
       }

       return TRUE;
   }
   ```

<a name="prepare"></a>
## Preparing the Screen Mirroring Sink

To prepare the screen mirroring sink:

1. Register and define a callback for checking the screen mirroring sink state using the `scmirroring_sink_set_state_changed_cb()` function:

   ```
   static void
   scmirroring_state_callback(scmirroring_error_e error_code, scmirroring_state_e state, void *user_data)
   {
       dlog_print(DLOG_ERROR, LOG_TAG, "Received Callback error code[%d], state[%d]", error_code, state);

       switch (state) {
       case SCMIRRORING_STATE_NULL:
           break;
       case SCMIRRORING_STATE_PREPARED:
           break;
       case SCMIRRORING_STATE_CONNECTED:
           break;
       case SCMIRRORING_STATE_PLAYING:
           break;
       case SCMIRRORING_STATE_PAUSED:
           break;
       case SCMIRRORING_STATE_DISCONNECTED:
           break;
       case SCMIRRORING_STATE_NONE:
           break;
       default:
           dlog_print(DLOG_ERROR, LOG_TAG, "state[%d] Invalid State", state);
           break;
       }

       return;
   }

   static int
   prepare_scmirroring_sink(scmirroring_display_type_e display_type)
   {
       ret = scmirroring_sink_set_state_changed_cb(g_scmirroring, scmirroring_state_callback, NULL);
       if (ret != SCMIRRORING_ERROR_NONE) {
           dlog_print(DLOG_ERROR, LOG_TAG, "scmirroring_sink_set_state_changed_cb failed [%d]", ret);

           return FALSE;
       }
   ```

2. Set a display object using the `scmirroring_sink_set_display()` function:

   ```
       switch (display_type) {
       case SCMIRRORING_DISPLAY_TYPE_EVAS:
           if (g_eo == NULL) {
               dlog_print(DLOG_ERROR, LOG_TAG, "g_eo is NULL");

               return FALSE;
           }
           ret = scmirroring_sink_set_display(g_scmirroring, SCMIRRORING_DISPLAY_TYPE_EVAS, (void*)g_eo);
           if (ret != SCMIRRORING_ERROR_NONE) {
               dlog_print(DLOG_ERROR, LOG_TAG,
                          "scmirroring_sink_set_display failed [%d], display type [%d]",
                          ret, display_type);

               return FALSE;
           }
           break;
       case SCMIRRORING_DISPLAY_TYPE_OVERLAY:
           if (g_win == NULL) {
               dlog_print(DLOG_ERROR, LOG_TAG, "g_win is NULL");

               return FALSE;
           }
           ret = scmirroring_sink_set_display(g_scmirroring, SCMIRRORING_DISPLAY_TYPE_OVERLAY, (void*)g_win);
           if (ret != SCMIRRORING_ERROR_NONE) {
               dlog_print(DLOG_ERROR, LOG_TAG,
                          "scmirroring_sink_set_display failed [%d], display type [%d]",
                          ret, display_type);

               return FALSE;
           }
           break;
       default:
           dlog_print(DLOG_ERROR, LOG_TAG, "Invalid display type [%d].", display_type);

           return FALSE;
       }
   }
   ```

3. Create the display object based on the applicable [scmirroring_display_type_e](../../api/mobile/latest/group__CAPI__MEDIA__SCREEN__MIRRORING__MODULE.html#ga2c7d012d260b35e0e550618c2546f751) enumerator value:

   ```
   #define PACKAGE_NAME "SCREEN_MIRRORING_SINK_APP"
   #define WINDOW_WIDTH 800
   #define WINDOW_HEIGHT 1200

   static Evas_Object *g_win = NULL;
   static Evas_Object *g_evas = NULL;
   static Evas_Object *g_eo = NULL;
   static Evas_Object *g_rect = NULL;

   static void
   create_base_gui(scmirroring_display_type_e display_type)
   {
       g_win = elm_win_add(NULL, PACKAGE_NAME, ELM_WIN_BASIC);

       evas_object_resize(g_win, WINDOW_WIDTH, WINDOW_HEIGHT);
       evas_object_move(g_win, 0, 0);
       elm_win_autodel_set(g_win, EINA_TRUE);

       switch (display_type) {
       case SCMIRRORING_DISPLAY_TYPE_EVAS:
           g_evas = evas_object_evas_get(g_win);
           /* Set an Evas image object for drawing */
           g_eo = evas_object_image_add(g_evas);
           evas_object_image_size_set(g_eo, WINDOW_WIDTH, WINDOW_HEIGHT);
           evas_object_image_fill_set(g_eo, 0, 0, WINDOW_WIDTH, WINDOW_HEIGHT);
           evas_object_resize(g_eo, WINDOW_WIDTH, WINDOW_HEIGHT);
           /* Show the window after the base GUI is set up */
           evas_object_show(g_eo);
           evas_object_show(g_win);
           break;
       case SCMIRRORING_DISPLAY_TYPE_OVERLAY:
           g_rect = evas_object_rectangle_add(g_evas);
           evas_object_resize(g_rect, WINDOW_WIDTH, WINDOW_HEIGHT);
           evas_object_move(g_rect, 0, 0);
           evas_object_color_set(g_rect, 0, 0, 0, 0);
           evas_object_render_op_set(g_rect, EVAS_RENDER_COPY);
           evas_object_size_hint_weight_set(g_rect, EVAS_HINT_EXPAND, EVAS_HINT_EXPAND);
           /* Show the window after the base GUI is set up */
           evas_object_show(g_win);
           break;
       default:
           break;
       }
   }
   ```

4. Prepare the screen mirroring sink using the `scmirroring_sink_prepare()` function.

   The function sets the screen mirroring state to `SCMIRRORING_STATE_PREPARED`.

   ```
   ret = scmirroring_sink_prepare(g_scmirroring);
   if (ret != SCMIRRORING_ERROR_NONE) {
       dlog_print(DLOG_ERROR, LOG_TAG, "scmirroring_sink_prepare failed [%d]", ret);

       return FALSE;
   }

   return TRUE;
   ```

<a name="connect"></a>
## Connecting and Starting the Screen Mirroring Sink

To connect and start the screen mirroring sink:

1. Set the IP address and port number using the `scmirroring_sink_set_ip_and_port()` function:

   ```
   static int
   start_scmirroring_sink(const char* peer_ip, const char* peer_port)
   {
       int ret;
       ret = scmirroring_sink_set_ip_and_port(g_scmirroring, peer_ip, peer_port);
       if (ret != SCMIRRORING_ERROR_NONE) {
           dlog_print(DLOG_ERROR, LOG_TAG, "scmirroring_sink_set_ip_and_port failed [%d]", ret);

           return FALSE;
       }
   ```

2. Connect the screen mirroring sink to the screen mirroring source using the `scmirroring_sink_connect()` function.

   The function sets the screen mirroring state to `SCMIRRORING_STATE_CONNECTED` asynchronously. Monitor the state changes using the state callback.

   ```
       ret = scmirroring_sink_connect(g_scmirroring);
       if (ret != SCMIRRORING_ERROR_NONE) {
           dlog_print(DLOG_ERROR, LOG_TAG, "scmirroring_sink_connect failed [%d]", ret);

           return FALSE;
       }

       return TRUE;
   }
   ```

3. When the screen mirroring state is `SCMIRRORING_STATE_CONNECTED`, start the screen mirroring sink using the `scmirroring_sink_start()` function.

   The function sets the screen mirroring state to `SCMIRRORING_STATE_PLAYING` asynchronously.

   ```
   static void
   scmirroring_state_callback(scmirroring_error_e error_code, scmirroring_state_e state, void *user_data)
   {
       int ret;
       dlog_print(DLOG_ERROR, LOG_TAG, "Received Callback error code[%d], state[%d]", error_code, state);

       switch (state) {
       /* Other cases */
       case SCMIRRORING_STATE_CONNECTED:
           ret = scmirroring_sink_start(g_scmirroring);
           if (ret != SCMIRRORING_ERROR_NONE) {
               dlog_print(DLOG_ERROR, LOG_TAG, "scmirroring_sink_start failed [%d]", ret);

               return;
           }
           break;
       /* Other cases */
       }

       return;
   }
   ```

<a name="release"></a>
## Releasing Resources

After you have finished working with the screen mirroring sink, disconnect it and release all its resources:

1. Disconnect the screen mirroring sink using `scmirroring_sink_disconnect()` function.

   The function sets the screen mirroring state to `SCMIRRORING_STATE_DISCONNECTED`.

   ```
   static int
   destroy_scmirroring_sink()
   {
       ret = scmirroring_sink_disconnect(g_scmirroring);
       if (ret != SCMIRRORING_ERROR_NONE) {
           dlog_print(DLOG_ERROR, LOG_TAG, "scmirroring_sink_disconnect failed [%d]", ret);

           return FALSE;
       }
   ```

2. Unprepare the screen mirroring sink using the `scmirroring_sink_unprepare()` function.

   The function sets the screen mirroring state to `SCMIRRORING_STATE_NULL`.

   ```
       ret = scmirroring_sink_unprepare(g_scmirroring);
       if (ret != SCMIRRORING_ERROR_NONE) {
           dlog_print(DLOG_ERROR, LOG_TAG, "scmirroring_sink_unprepare failed [%d]", ret);

           return FALSE;
       }
   ```

3. Release the screen mirroring sink resources using the `scmirroring_sink_destroy()` function.

   The function sets the screen mirroring state to `SCMIRRORING_STATE_NONE`.

   ```
       ret = scmirroring_sink_destroy(g_scmirroring);
       if (ret != SCMIRRORING_ERROR_NONE) {
           dlog_print(DLOG_ERROR, LOG_TAG, "scmirroring_sink_destroy failed [%d]", ret);

           return FALSE;
       }

       return TRUE;
   }
   ```

<a name="handle"></a>
## Handling Screen Mirroring Sink Exceptions

If the state callback returns an error or the `SCMIRRORING_STATE_DISCONNECTED` state, [release the screen mirroring sink and its allocated resources](#release). This exception is caused by an internal error in the screen mirroring sink, or by the source device disconnecting the session.

```
static void
scmirroring_state_callback(scmirroring_error_e error_code, scmirroring_state_e state, void *user_data)
{
    int ret;
    dlog_print(DLOG_ERROR, LOG_TAG, "Received Callback error code[%d], state[%d]", error_code, state);

    if (error_code != SCMIRRORING_ERROR_NONE) {
        ret = destroy_scmirroring_sink();
        if (ret != TRUE) {
            dlog_print(DLOG_ERROR, LOG_TAG, "destroy_scmirroring_sink failed");

            return;
        }
    }

    switch (state) {
    /* Other cases */
    case SCMIRRORING_STATE_DISCONNECTED:
        ret = scmirroring_sink_unprepare(g_scmirroring);
        if (ret != SCMIRRORING_ERROR_NONE) {
            dlog_print(DLOG_ERROR, LOG_TAG, "scmirroring_sink_unprepare failed [%d]", ret);

            return;
        }
        /* Do something */
        break;
    /* Other cases */
    }

    return;
}
```

## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
