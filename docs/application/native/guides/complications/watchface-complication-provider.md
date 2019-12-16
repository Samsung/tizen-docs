# Watch Face Complication Provider

The watch face complication provider application is a service application to provide complication data.
Complication provider application provides only data. The watch face application decides how to display the complications.
The complication provider application provides the complication data by using the watch face complication provider API to the watch face application.

## Prerequisites

To enable your application to use the watch face complication functionality:

1. To use the Watch Face Complication API to communicate with the watch face application, this application has to request permission by adding
the following privilege to the `tizen-manifest.xml` file:

    ```xml
    <privileges>
        <privilege>http://tizen.org/privilege/datasharing</privilege>
    </privileges>
    ```

2. To use the functions and data types for the Watch Face Complication Provider API, include the `<watchface-complication-provider.h>` header file in your application:

    ```cpp
    #include <watchface-complication-provider.h>
    ```

## Updating Complication Data

When the request occurs to update the complication data, the complication provider application can receive the request by adding `watchface_complication_provider_update_requested_cb()`. The watch face application can send the update request, and this request also occurs after the complication provider application notifies that the complication data is changed.

```cpp
void _watchface_complication_provider_update_requested_cb(const char *provider_id,
        const char *req_appid, watchface_complication_type_e type, const bundle *context,
        bundle *share_data, void *user_data)
{
    if (type == WATCHFACE_COMPLICATION_TYPE_SHORT_TEXT) {
        watchface_complication_provider_data_set_short_text(shared_data, "updated short text");
    } else if (type == WATCHFACE_COMPLICATION_TYPE_TIME) {
        complication_time_info_h info;
        watchface_complication_provider_timeinfo_create(&info);
        watchface_complication_provider_timeinfo_set_timezone_id(info, "Asia/Seoul");
        watchface_complication_provider_data_set_timeinfo(shared_data, info);
        watchface_complication_provider_timeinfo_destroy(info);
    }
}

bool app_create(void *data)
{
    watchface_complication_provider_add_update_requested_cb("PROVIDER_ID",
            _watchface_complication_provider_update_requested_cb, NULL);
}
```

The complication provider application must set the updated complication data to `shared_data` in the update requested callback.
And it is possible to verify whether the data is valid or not using `watchface_complication_provider_data_is_valid()`.
If the data is invalid, `watchface_complication_updated_cb()` of the complication will not be called.

The complication data can be set using the following APIs. These APIs can be used only in `watchface_complication_provider_update_requested_cb()`:

| API | Description |
|--------|-----------------|
| `watchface_complication_provider_data_set_title()` | Sets the complication title. |
| `watchface_complication_provider_data_set_short_text()` | Sets the short text type data. |
| `watchface_complication_provider_data_set_long_text()` | Sets the long text type data. |
| `watchface_complication_provider_data_set_image_path()` | Sets the image path type data. |
| `watchface_complication_provider_data_set_ranged_value()` | Sets the ranged value type data. |
| `watchface_complication_provider_data_set_icon_path()` | Sets the icon path type data. |
| `watchface_complication_provider_data_set_timestamp()` | Sets the timestamp type data. |
| `watchface_complication_provider_data_set_extra_data()` | Sets the extra data. |
| `watchface_complication_provider_timeinfo_create()` | Creates the time information handle. |
| `watchface_complication_provider_timeinfo_set_timezone()` | Sets the timezone. For example, UTC+8 |
| `watchface_complication_provider_timeinfo_set_timezone_id()` | Sets the timezone ID. For example, Asia/Seoul |
| `watchface_complication_provider_timeinfo_set_timezone_country()` | Sets the timezone country. For example, Korea |
| `watchface_complication_provider_timeinfo_set_timezone_city()` | Sets the timezone city. For example, Seoul |
| `watchface_complication_provider_timeinfo_destroy()` | Destroys the time information handle. |
| `watchface_complication_provider_data_set_timeinfo()` | Sets the time information data. |

> **Note**
>
> `watchface_complication_provider_data_set_timestamp()` is deprecated since Tizen 5.5.
> Instead, use `watchface_complication_provider_timeinfo_create()` and `watchface_complication_provider_timeinfo_set_timezone_id()`.


```cpp
void _watchface_complication_provider_update_requested_cb(const char *provider_id,
        const char *req_appid, watchface_complication_type_e type, const bundle *context,
        bundle *share_data, void *user_data)
{
    bool is_valid;

    if (type == WATCHFACE_COMPLICATION_TYPE_SHORT_TEXT) {
        watchface_complication_provider_data_set_short_text(shared_data, "updated short text");
    } else if (type == WATCHFACE_COMPLICATION_TYPE_TIME) {
        complication_time_info_h info;
        watchface_complication_provider_timeinfo_create(&info);
        watchface_complication_provider_timeinfo_set_timezone_id(info, "Asia/Seoul");
        watchface_complication_provider_data_set_timeinfo(shared_data, info);
        watchface_complication_provider_timeinfo_destroy(info);
    }

    watchface_complication_provider_data_is_valid(shared_data, &is_valid);
}
```

If the callback is not necessary, it can be removed by using `watchface_complication_provider_remove_update_requested_cb()`:

```cpp
{
    watchface_complication_provider_remove_update_requested_cb("PROVIDER_ID",
            _watchface_complication_provider_update_requested_cb);
}
```

## Notifying the Complication Data Update

When the complication data is changed, the complication provider application can notify that the complication data is updated.
If the notification successfully transfers to the complication, the complication data update request will occur:


```cpp
{
    watchface_complication_provider_notify_update("PROVIDER_ID");
}
```

## Transferring Event Action

The complication provider can provide additional action that is touching. In this case, complication provider is launched with touch event and information of provider that has touched.

The following are event types:

| Event type | Description |
|-------------|-------------|
| `WATCHFACE_COMPLICATION_EVENT_NONE` | The complication is not tapped. |
| `WATCHFACE_COMPLICATION_EVENT_TAP` | The complication is tapped. |
| `WATCHFACE_COMPLICATION_EVENT_DOUBLE_TAP` | The complication is double tapped. |

The complication provider provides followings:

1. The complication provider can set the support events in `tizen-manifest.xml` using `<support-event>`.

2. The complication provider can get the transferred event from `app_control_h` that is the parameter of the `app_control` life cycle callback
by using `watchface_complication_provider_get_event()`.
And if the touch event is transferred from watchface, the information of the complication is also transferred.

    To get the information, the following functions are used to get the information:

    | API | Information |
    |-----|-----------|
    | `watchface_complication_provider_event_get_provider_id()` | Gets the provider id of touched complication. |
    | `watchface_complication_provider_event_launch_get_complication_type()` | Gets the complication type of touched complication. |
    | `watchface_complication_provider_event_launch_get_context()` | Gets the context information of touched complication. |


    Then complication provider can define the action according to the event and the information of complication that is touched.


    ```cpp
    void app_control(app_control_h app_control, void *data)
    {
        watchface_complication_event_type_e event_type;
        char *provider_id;
        watchface_complication_type_e type;
        bundle *context;

        watchface_complication_provider_get_event(app_control, &event_type);

        if (event_type == WATCHFACE_COMPLICATION_EVENT_TAP) {
            watchface_complication_provider_event_get_provider_id(app_control,
                    &provider_id);
            watchface_complication_provider_event_launch_get_complication_type(
                    app_control, &type);
            watchface_complication_provider_event_launch_get_context(app_control,
                    &context);

            /* Do something */
        }
    }
    ```


## Providing XML Schema to Create Complication Provider Application

To create the complication provider application, complication provider tags are provided in `tizen-manifest.xml` file.
It is possible to provide multiple complication provider in a complication provider application:

```xml
<complication provider-id="mycomplicationid" setup-appid="org.tizen.watch_setting">
</complication>
```

It is mandatory to use attribute **provider-id** that is the id of the complication.
If it is necessary to set the options to provide the specific data (such as, world clock), it can provide the complication setting application.
In this case, **setup-appid** is the appid of the complication setting application.

If the **trusted** attribute value is `true`, the complication provider do not send data to the complications which have different certificate.

At least one `<support-type>` is necessary to create the complication provider application. Also, it is possible to support multiple types.
These support type means data type and the complication provider provides data types that are defined in xml. It is not possible to declare duplicated data type for
one complication provider id.

```xml
<support-type>
</support-type>
```

And, the specific default value is mandatory depending on each support types:

| Support types | Mandatory default values | Optional default values |
|---------------|--------------------------|---------------------------|
| `<short-text-type>` | `<default-short-text>` | `<default-title>` |
|                     |                        | `<default-icon>` |
|                     |                        | `<default-extra-data>` |
| `<long-text-type>` | `<default-long-text>` | `<default-title>` |
|                    |                       | `<default-icon>` |
|                    |                       | `<default-extra-data>` |
| `<ranged-value-type>` | `<default-value>` | `<default-title>` |
|                       | `<default-min>` | `<default-short-text>` |
|                       | `<default-max>` | `<default-icon>` |
|                       |                   | `<default-extra-data>` |
| `<icon-type>` | `<default-icon>` | `<default-extra-data>` |
| `<image-type>` | `<default-image>` | `<default-extra-data>` |
| `<time-type>` | `<default-hour>` | `<default-short-text>` |
|               | `<default-minute>` | `<default-extra-data>` |
|               | `<default-second>` |         |
|               | `<default-timezone-id>` |         |


> **Note**
>
> `<default-hour>`, `<default-minute>`, and `<default-second>` are deprecated since Tizen 5.5.
> Instead, use `<default-timezone-id>`.
> `<default-timezone-id>` is the value declared in the IANA(Internet Assigned Numbers Authority) TZ database. For example, Asia/Seoul.
> If the xml contains `<default-timezone-id>`, then `<default-hour>`, `<default-minute>`, and `<default-second>` are not necessary.


`<label>` is the name of the complication provider.
If it is necessary to support the multiple language, **multiple language** tag must be provided:

```xml
<label>MyComplication</label>
<label xml:lang="en-us">EngComplication</label>
```

`<period>` is used to update complication provider data automatically, and in unit seconds:

```xml
<period>60</period>
```

In this case, the complication will send data update request to the complication provider every 60 seconds.

`<support-event>` is the type of event that can be supported. It is possible to set **tap**, **double-tap**
events or both.

And it is possible to add `<privileges>` to restrict getting the complication data.
In this case, watchface must add the specific privileges to get the complication data in `tizen-manifext.xml`:


```xml
<complication provider-id="mycomplicationid" setup-appid ="org.tizen.watch_setting" trusted="true">
    <support-type>
        <short-text-type>
            <default-short-text>70</default-short-text>
        </short-text-type>
        <ranged-value-type>
            <default-current>70</default-current>
            <default-min>0</default-min>
            <default-max>100</default-max>
        </ranged-value-type>
        <time-type>
            <default-timezone-id>Asia/Seoul</default-timezone-id>
        <time-type>
    </support-type>
    <period>60</period>
    <label>MyComp</label>
    <label xml:lang="en-us">EngLabel</label>
    <support-event>
        <event>tap</event>
        <event>double-tap</event>
    </support-event>
    <privileges>
        <privilege>http://tizen.org/privilege/alarm.get</privilege>
        <privilege>http://tizen.org/privilege/alarm.set</privilege>
    </privileges>
</complication>
```

## Related Information
- Dependencies
  - Tizen 5.0 and Higher for Wearable
