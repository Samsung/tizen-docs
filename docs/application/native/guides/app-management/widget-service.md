# Widget Service

The Widget Service API provides functionality to get the information of installed widgets.

The main features of the Widget Service API include:

- Retrieving information of widgets

  You can [retrieve the information](#retrieve) of an installed widget application.

- Communicating with running widget instances

  You can [communicate](#communicate) with running widget instances.

> [!NOTE]
> This API will work only if the widget and application are packaged together.

## Prerequisites

1.  To use the [Widget Service API](../../api/common/latest/group__CAPI__WIDGET__SERVICE__MODULE.html), the application has to request permission by adding the following privilege to the `tizen-manifest.xml` file:

    ```xml
    <privileges>
       <privilege>http://tizen.org/privilege/widget.viewer</privilege>
    </privileges>
    ```

2.  To use the functions of the Widget Service API, include the `<widget_service.h>` header file in your application:

    ```cpp
    #include <widget_service.h>
    ```

<a name="retrieve"></a>
## Retrieve the information

Widget Service API provides functions to get the information about widget related properties.

1. Gets the pixel size of given size type:

    ```cpp
    int ret;
    int w;
    int h;

    ret = widget_service_get_size(WIDGET_SIZE_TYPE_2x2, &w, &h);
    ```

2. Gets the supported list of sizes:

    ```cpp
    int ret;
    int cnt = 20;
    int *w;
    int *h;

    ret = widget_service_get_supported_sizes("pkg_id", &cnt, &w, &h);
    ```

3. Gets the ID of a widget by the given ID of package or UI app:

    ```cpp
    char *id;
    int result;
    
    id = widget_service_get_widget_id("pkg_id");
    ```

<a name="communicate"></a>
## Communicate with widget instances

Widget Service API provides functions to trigger the event that changes the state of the widget.

1. Triggers the update event for a given widget instance:

    ```cpp
    int ret;
    int force = 0;
    Bundle data;

    data = bundle_create();
    
    ret = widget_service_trigger_update("widget_id", "instance_id", data, force);
    ```

2. Changes the update period of the given widget instance:

    ```cpp
    int ret;

    ret = widget_service_change_period("widget_id", "instance_id", 1.0);
    ```

3. Gets and Sets the disabled state of a widget:

    ```cpp
    void _widget_disable_event_cb(const char *widget_id, bool is_disabled, void *user_data)
    {
    }
    ```
    ```cpp
    int ret;
    bool is_disabled = true;

    ret = widget_service_get_widget_disabled(SAMPLE_PKGNAME, &is_disabled);
    ret = widget_service_set_disable_event_cb(_widget_disable_event_cb, NULL);

    ret = widget_service_set_widget_disabled("widget_id", true);
    ```

    > [!NOTE]
    > 'widget_service_set_widget_disabled' is not for use by third-party applications.


## Related information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
- API Reference
  - [Widget Service](../../api/common/latest/group__CAPI__WIDGET__SERVICE__MODULE.html)
