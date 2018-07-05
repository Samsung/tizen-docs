
# Receiving Content from Other Applications

The basic tasks involved in receiving content from other applications are advertising the features available in your application, handling the
incoming content, and managing any extra data sent with the content. The following sections provide you with the fundamental building blocks for receiving content that other applications want to share with you.

## Exporting Application Control Functionality

To allow other applications to find and use your application features implicitly without your application ID, you must advertise your application features to other applications. You can do this by declaring your application control information in the `tizen-manifest.xml` file.

The following example shows an advertisement for the `VIEW` and `CALL` application control operations:

```xml
<app-control>
   <mime name = "application/xhtml+xml"/>
   <operation name = "http://tizen.org/appcontrol/operation/view"/>
   <uri name = "http"/>
</app-control>
<app-control>
   <operation name = "http://tizen.org/appcontrol/operation/dial"/>
   <uri name = "tel"/>
</app-control>
```

> **Note**
>
> In the application manifest file, the valid operation name format is `http://tizen.org/appcontrol/operation/<verb>`. You cannot use the related macro name format: `APP_CONTROL_OPERATION_<VERB>`.

## Handling Incoming Content

When another application sends an application control request to your application, the application framework calls your application's `app_control_cb()` callback just after your application enters the main loop. This callback is passed to the handler, `app_control`, containing the reason why your application was launched. For example, your application can be launched to open a file that another application is sharing with you.

When an application control request arrives, your application is responsible for checking and responding to the `app_control` handler accordingly.

The following example shows how you can initialize the application to allow the application control callback to handle the request for the `APP_CONTROL_OPERATION_VIEW` operation:

```cpp
int
main(int argc, char *argv[])
{
    struct appdata ad;

    ui_app_lifecycle_callback_s event_callback;

    event_callback.create = app_create;
    event_callback.terminate = app_terminate;
    event_callback.pause = app_pause;
    event_callback.resume = app_resume;
    /* Register the app control callback */
    event_callback.app_control = app_control;

    memset(&ad, 0x0, sizeof(struct appdata));

    return ui_app_main(argc, argv, &event_callback, &ad);
}

/* App control callback */
static void
app_control(app_control_h app_control, void *user_data)
{
    struct appdata *ad = (struct appdata *)user_data;
    char *operation;
    char *uri;
    char *mime_type;

    app_control_get_operation(app_control, operation);

    if (!strcmp(operation, APP_CONTROL_OPERATION_VIEW)) {
        app_control_get_uri(app_control, &uri);
        app_control_get_mime(app_control, &mime_type);

        if (uri && !strcmp(mime_type, "image/jpg"))
                /* Display the image file the other application is sharing with you */
                display_image_file(ad, uri);
    }

    if (ad->win)
        elm_win_activate(ad->win);
}
```

## Managing Extra Data

Using the `app_control_foreach_extra_data()` function, you can read any extra data added to the `app_control` handle. This function calls the `_app_control_extra_data_cb()` callback once for each extra data key-value pair contained in the handle. When the callback returns `false`, the iteration ends.

```cpp
bool
_app_control_extra_data_cb(app_control_h app, const char *key, void *user_data)
{
    int ret;
    char *value;

    ret = app_control_get_extra_data(app, key, &value);
    if (ret == APP_CONTROL_ERROR_NONE)
        dlog_print(DLOG_DEBUG, LOG_TAG, "[value] %s", value);
    else
        dlog_print(DLOG_ERROR, LOG_TAG, "app_control_get_extra_data() failed. err = %d", ret);

    return true;
}

ret = app_control_foreach_extra_data(app, _app_control_extra_data_cb, 0);
if (ret != APP_CONTROL_ERROR_NONE)
    dlog_print(DLOG_ERROR, LOG_TAG, "app_control_foreach_extra_data() failed. err = %d", ret);
```
