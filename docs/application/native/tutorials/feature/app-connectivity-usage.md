
# Network Usage

The following sections describe how to create applications that have
cost-efficient control over their usage of network resources. If your
application performs a lot of network operations, you must provide user
settings that allow the user to control your application's data
behavior, such as how often the application syncs data, whether to
perform uploads or downloads only when Wi-Fi is switched on, and whether
to use data while roaming. With these controls available to them, users
are much less likely to disable your application's access to background
data when they approach their limits, because they can instead precisely
control how much data your application uses.

<a name="privilege"></a>
## Required Privileges and Features

Applications that access network information and statistics must declare
the required privileges in the `tizen-manifest.xml` file. For more
information on the Tizen privileges, see [Security and API
Privileges](../details/sec-privileges.md).

To perform the network operations, the application manifest must include
the following privileges:

```xml
<privileges>
   <privilege>http://tizen.org/privilege/network.get</privilege>
</privileges>
```

To perform the network operations, the device must support the following
[features](../details/app-filtering.md):

-   To use Wi-Fi:
    -   `http://tizen.org/feature/network.wifi`
    -   `http://tizen.org/feature/network.wifi.direct`
    -   `http://tizen.org/feature/network.wifi.direct.display`
    -   `http://tizen.org/feature/network.wifi.direct.service_discovery`
-   To use the mobile network:
    -   `http://tizen.org/feature/network.telephony`


<a name="type"></a>
## Monitoring Connection Type Changes


When the network connection is changed, the application must receive a
notification. For instance, if the Wi-FI network is changed to a visited
mobile network (roaming), the user can pay for the mobile data without
user recognition.

The Connection API (in
[mobile](../../api/mobile/latest/group__CAPI__NETWORK__CONNECTION__MODULE.html)
and
[wearable](../../api/wearable/latest/group__CAPI__NETWORK__CONNECTION__MODULE.html)
applications) provides a function that provides a notification about the
connection status. The application can download or upload files only
when Wi-Fi is connected by checking the network type in the triggered
callback.

The Connection API supports the following network types:

-   `CONNECTION_TYPE_DISCONNECTED`
-   `CONNECTION_TYPE_WIFI`
-   `CONNECTION_TYPE_CELLULAR` (indicates the mobile network)
-   `CONNECTION_TYPE_ETHERNET`
-   `CONNECTION_TYPE_BT`

The following example demonstrates how to monitor network connection
changes:

```c++
#include <net_connection.h>

static void
connection_changed_cb(connection_type_e type, void* user_data)
{
    dlog_print(DLOG_INFO, LOG_TAG, "Type changed callback, connection type: %d", type);
}

int
get_network_connection()
{
    int error_code;
    static connection_h connection;
    void *user_data;

    error_code = connection_create(&connection);
    if (error_code != CONNECTION_ERROR_NONE)
        return;

    error_code = connection_set_type_changed_cb(connection, connection_changed_cb, user_data);
    if (error_code != CONNECTION_ERROR_NONE)
        return;

    error_code = connection_destroy(connection);
    if (error_code != CONNECTION_ERROR_NONE)
        return;
}
```

<a name="mobile_change"></a>
## Monitoring Mobile (Cellular) Network Service Changes


Sometimes, the application must check the state of the mobile network
service to make the user experience better by protecting against running
tasks in the background when the device is, for example, roaming.
Downloading or uploading content without user awareness in that
situation can incur charges, and result in unreasonable use of the
mobile network resources. The application must use the data transport
network efficiently, providing a better user experience for the mobile
data network.

### Getting the State of Mobile Network Service

The Telephony Information API (in
[mobile](../../api/mobile/latest/group__CAPI__TELEPHONY__INFORMATION.html)
and
[wearable](../../api/wearable/latest/group__CAPI__TELEPHONY__INFORMATION.html)
applications) is composed of Call (in
[mobile](../../api/mobile/latest/group__CAPI__TELEPHONY__INFORMATION__CALL.html)
and
[wearable](../../api/wearable/latest/group__CAPI__TELEPHONY__INFORMATION__CALL.html)
applications), SIM (in
[mobile](../../api/mobile/latest/group__CAPI__TELEPHONY__INFORMATION__SIM.html)
and
[wearable](../../api/wearable/latest/group__CAPI__TELEPHONY__INFORMATION__SIM.html)
applications), Network (in
[mobile](../../api/mobile/latest/group__CAPI__TELEPHONY__INFORMATION__NETWORK.html)
and
[wearable](../../api/wearable/latest/group__CAPI__TELEPHONY__INFORMATION__NETWORK.html)
applications), and Modem (in
[mobile](../../api/mobile/latest/group__CAPI__TELEPHONY__INFORMATION__MODEM.html)
and
[wearable](../../api/wearable/latest/group__CAPI__TELEPHONY__INFORMATION__MODEM.html)
applications) APIs for the mobile network service.

The Telephony Network API provides the detailed mobile network
information: LAC, Cell ID, RSSI, roaming state, MCC, MNC, network
provider name, PS type, and network type. The
`telephony_network_get_service_state()` function gets the current
network state of the telephony service. It returns one of the
`telephony_network_service_state_e` enumerator values (in
[mobile](../../api/mobile/latest/group__CAPI__TELEPHONY__INFORMATION__NETWORK.html#gae9f3b6e54a1086b8734f4acc71fd001b)
and
[wearable](../../api/wearable/latest/group__CAPI__TELEPHONY__INFORMATION__NETWORK.html#gae9f3b6e54a1086b8734f4acc71fd001b)
applications).

The following table indicates the `telephony_network_service_state_e`
enumeration that has the mobile network service state.

**Table: Mobile network service states**

| Enumeration                              | Description                    |
| ---------------------------------------- | ------------------------------ |
| `TELEPHONY_NETWORK_SERVICE_STATE_IN_SERVICE` | In service                     |
| `TELEPHONY_NETWORK_SERVICE_STATE_OUT_OF_SERVICE` | Out of service                 |
| `TELEPHONY_NETWORK_SERVICE_STATE_EMERGENCY_ONLY` | Only emergency call is allowed |

The following example demonstrates how to get the mobile network service
state:

```c++
/* Convert network telephony_network_service_state_e to string */
char*
_telephony_network_state_to_string(telephony_network_service_state_e network_state)
{
    switch (network_state) {
    case TELEPHONY_NETWORK_SERVICE_STATE_IN_SERVICE:
        return "TELEPHONY_NETWORK_SERVICE_STATE_IN_SERVICE";
    case TELEPHONY_NETWORK_SERVICE_STATE_OUT_OF_SERVICE:
        return "TELEPHONY_NETWORK_SERVICE_STATE_OUT_OF_SERVICE";
    case TELEPHONY_NETWORK_SERVICE_STATE_EMERGENCY_ONLY:
        return "TELEPHONY_NETWORK_SERVICE_STATE_EMERGENCY_ONLY";
    default:
        return "Unknown";
    }
}

void
get_telephony_information(appdata_s *ad, Evas_Object *obj, void *event_info)
{
    /* Create a telephony handle */
    telephony_handle_list_s handle_list;
    /* In the case of a single SIM, you get only one handle */
    ret = telephony_init(&handle_list);

    /* Print */
    for (i = 0; i < app_data->handle_list.count; i++) {
        dlog_print(DLOG_INFO, "TEST", "telephony handle[%p] for subscription[%d]",
                   app_data->handle_list.handle[i], i);
    }

    /* Get the network service state */
    telephony_network_service_state_e network_service_state;
    char *state = NULL;
    ret = telephony_network_get_service_state(handle_list.handle[0], &network_service_state);
    state = _telephony_network_state_to_string(network_service_state);
    if (ret != TELEPHONY_ERROR_NONE)
        dlog_print(DLOG_DEBUG, LOG_TAG, "[telephony_network_get_service_state] failed");
    else
        dlog_print(DLOG_DEBUG, LOG_TAG, "Network Service State [%s]", state);
}

static void
app_terminate(void *data)
{
    /* Release and free the created telephony handle */
    telephony_deinit(&handle_list);
}

/* Auto-generated functions (from the Tizen Studio) are not included */

int
main(int argc, char* argv[])
{
    AppData app_data;  /* Store telephony handle here */
    service_app_lifecycle_callback_s event_callback;
    app_event_handler_h handlers[5] = {NULL,};

    event_callback.create = service_app_create;
    event_callback.terminate = service_app_terminate;
    event_callback.app_control = service_app_control;

    service_app_add_event_handler(&handlers[APP_EVENT_LOW_BATTERY], APP_EVENT_LOW_BATTERY,
                                  service_app_low_battery, &app_data);
    service_app_add_event_handler(&handlers[APP_EVENT_LOW_MEMORY], APP_EVENT_LOW_MEMORY,
                                  service_app_low_memory, &app_data);
    service_app_add_event_handler(&handlers[APP_EVENT_LANGUAGE_CHANGED], APP_EVENT_LANGUAGE_CHANGED,
                                  service_app_lang_changed, &app_data);
    service_app_add_event_handler(&handlers[APP_EVENT_REGION_FORMAT_CHANGED], APP_EVENT_REGION_FORMAT_CHANGED,
                                  service_app_region_changed, &app_data);

    /* Set AppData as a user_data */
    return service_app_main(argc, argv, &event_callback, &app_data);
}
```

### Monitoring Mobile Network Changes

Another way to get the mobile network state and protect the user against
unreasonable use of the mobile network resources is to register a
notification callback.

The `telephony_set_noti_cb()` function allows the application to listen
for the changes in the mobile network state, and also provides mobile
network information by specifying the notification ID when the mobile
network state changes.

The following table indicates the available notification IDs.

**Table: Notification IDs**

| Changed state             | Notification ID                          |
|-------------------------|----------------------------------------|
| Network service state     | `TELEPHONY_NOTI_NETWORK_SERVICE_STATE`   |
| Cell ID                   | `TELEPHONY_NOTI_NETWORK_CELLID`          |
| Roaming status            | `TELEPHONY_NOTI_NETWORK_ROAMING_STATUS`  |
| Signal strength           | `TELEPHONY_NOTI_NETWORK_SIGNALSTRENGTH_LEVEL` |
| Network name              | `TELEPHONY_NOTI_NETWORK_NETWORK_NAME`    |
| Packet-switched type      | `TELEPHONY_NOTI_NETWORK_PS_TYPE`         |
| Default data subscription | `TELEPHONY_NOTI_NETWORK_DEFAULT_DATA_SUBSCRIPTION` |
| Default subscription      | `TELEPHONY_NOTI_NETWORK_DEFAULT_SUBSCRIPTION` |

The `telephony_noti_e` enumerator (in
[mobile](../../api/mobile/latest/group__CAPI__TELEPHONY__INFORMATION.html#ga3f9d407deee8c7c7f1f7ed946bc60b4d)
and
[wearable](../../api/wearable/latest/group__CAPI__TELEPHONY__INFORMATION.html#ga3f9d407deee8c7c7f1f7ed946bc60b4d)
applications) defines the available notification IDs. The callback
function registered by the `telephony_set_noti_cb()` function
(`network_service_state_noti_cb()` in the following example) delivers
change notifications for a network asynchronously.

The following example demonstrates how to register a notification for
the mobile network state change:

```c++
/* Convert network telephony_network_service_state_e to string */
char*
_telephony_network_state_to_string(telephony_network_service_state_e network_state)
{
    switch (network_state) {
    case TELEPHONY_NETWORK_SERVICE_STATE_IN_SERVICE:
        return "TELEPHONY_NETWORK_SERVICE_STATE_IN_SERVICE";
    case TELEPHONY_NETWORK_SERVICE_STATE_OUT_OF_SERVICE:
        return "TELEPHONY_NETWORK_SERVICE_STATE_OUT_OF_SERVICE";
    case TELEPHONY_NETWORK_SERVICE_STATE_EMERGENCY_ONLY:
        return "TELEPHONY_NETWORK_SERVICE_STATE_EMERGENCY_ONLY";
    default:
        return "Unknown";
    }
}

/* This function is triggered, if the mobile network status is changed */
void
network_service_state_noti_cb(telephony_h handle, telephony_noti_e noti_id, void *data, void *user_data)
{
    telephony_network_service_state_e network_state = *(int *)data;
    char *network_state_string = _telephony_network_state_to_string(network_state);
    dlog_print(DLOG_DEBUG, LOG_TAG, "Network service state: [%s]", network_state_string);
}

void
monitor_telephony_information(appdata_s *ad, Evas_Object *obj, void *event_info)
{
    /*  Create a telephony handle */
    telephony_handle_list_s handle_list;
    /* In the case of a single SIM, you get only one handle */
    ret = telephony_init(&handle_list);

    /*
       Register the network_service_state_noti_cb() callback function
       to be notified if the Network Service state is changed
    */
    ret = telephony_set_noti_cb(handle_list.handle[0], TELEPHONY_NOTI_NETWORK_SERVICE_STATE, network_service_state_noti_cb, NULL);
    if (ret != TELEPHONY_ERROR_NONE)
        dlog_print(DLOG_DEBUG, LOG_TAG, "[telephony_set_noti_cb] failed");
}

static void
app_terminate(void *data)
{
    /* Release and free the created telephony handle */
    telephony_deinit(&handle_list);
}
```

<a name="info"></a>
## Getting Connection Information

The connection state can be changed depending on various mobile
environments, such as the settings of the mobile phone or the signal
strength received by the mobile phone from the cellular network or Wi-Fi
AP (access point). The Connection API (in
[mobile](../../api/mobile/latest/group__CAPI__NETWORK__CONNECTION__MODULE.html)
and
[wearable](../../api/wearable/latest/group__CAPI__NETWORK__CONNECTION__MODULE.html)
applications) provides a function that gets the current state of the
mobile network service and Wi-Fi network.

### Getting the Mobile (Cellular) Network Connection State

The application can use the `connection_get_cellular_state()` function
to get the mobile connection state.

The network connection can be in one of the following states:

-   `CONNECTION_CELLULAR_STATE_OUT_OF_SERVICE`
-   `CONNECTION_CELLULAR_STATE_FLIGHT_MODE`
-   `CONNECTION_CELLULAR_STATE_ROAMING_OFF`
-   `CONNECTION_CELLULAR_STATE_CALL_ONLY_AVAILABLE`
-   `CONNECTION_CELLULAR_STATE_AVAILABLE`
-   `CONNECTION_CELLULAR_STATE_CONNECTED`

The following example demonstrates how to get the mobile network state:

```c++
connection_cellular_state_e cellular_state;
connection_get_cellular_state(connection, &cellular_state);
switch (cellular_state) {
case CONNECTION_CELLULAR_STATE_OUT_OF_SERVICE:
    dlog_print(DLOG_INFO, LOG_TAG, "Out of service");
    break;
case CONNECTION_CELLULAR_STATE_FLIGHT_MODE:
    dlog_print(DLOG_INFO, LOG_TAG, "Flight mode");
    break;
case CONNECTION_CELLULAR_STATE_ROAMING_OFF:
    dlog_print(DLOG_INFO, LOG_TAG, "Roaming is switched off");
    break;
case CONNECTION_CELLULAR_STATE_CALL_ONLY_AVAILABLE:
    dlog_print(DLOG_INFO, LOG_TAG, "Call only");
    break;
case CONNECTION_CELLULAR_STATE_AVAILABLE:
    dlog_print(DLOG_INFO, LOG_TAG, "Available");
    break;
case CONNECTION_CELLULAR_STATE_CONNECTED:
    dlog_print(DLOG_INFO, LOG_TAG, "Connected");
    break;
default:
    dlog_print(DLOG_INFO, LOG_TAG, "error");
    break;
}
```

### Getting Wi-Fi Connection State

The application can use the `connection_get_wifi_state()` function to
get the Wi-Fi connection state.

The Wi-Fi connection can be in one of the following states:

-   `CONNECTION_WIFI_STATE_DEACTIVATED`
-   `CONNECTION_WIFI_STATE_DISCONNECTED`
-   `CONNECTION_WIFI_STATE_CONNECTED`

The following example demonstrates how to get the Wi-Fi network state:

```c++
connection_wifi_state_e wifi_state;
connection_get_wifi_state(connection, &wifi_state);
switch (wifi_state) {
case CONNECTION_WIFI_STATE_DEACTIVATED:
    dlog_print(DLOG_INFO, LOG_TAG, "Deactivated state");
    break;
case CONNECTION_WIFI_STATE_DISCONNECTED:
    dlog_print(DLOG_INFO, LOG_TAG, "Disconnected state");
    break;
case CONNECTION_WIFI_STATE_CONNECTED:
    dlog_print(DLOG_INFO, LOG_TAG, "Connected state");
    break;
default:
    dlog_print(DLOG_INFO, LOG_TAG, "error");
    break;
}
```

<a name="statistics"></a>
## Collecting Connection Statistics

The Connection Statistics API (in
[mobile](../../api/mobile/latest/group__CAPI__NETWORK__CONNECTION__STATISTICS__MODULE.html)
and
[wearable](../../api/wearable/latest/group__CAPI__NETWORK__CONNECTION__STATISTICS__MODULE.html)
applications) provides functions for getting statistical information,
such as the amount of sent or received data. The API also provides
functions for getting the cumulative size of packets sent or received
since the last reset based on the operation mode, such as packet
switching (PS).

Connection statistics include the amount of total sent and received data
and the last sent and received data. The parameters of the
`connection_get_statistics()` function determine which connection type
and which statistics are gathered:

-   The `connection_type_e` enumerator (in
    [mobile](../../api/mobile/latest/group__CAPI__NETWORK__CONNECTION__MANAGER__MODULE.html#ga85c33901b8ac24f2e5f66440ec4519ee)
    and
    [wearable](../../api/wearable/latest/group__CAPI__NETWORK__CONNECTION__MANAGER__MODULE.html#ga85c33901b8ac24f2e5f66440ec4519ee) applications)
    defines the connection types: `CONNECTION_TYPE_WIFI` is Wi-Fi and
    `CONNECTION_TYPE_CELLULAR` is the mobile network. Only Wi-Fi and
    mobile network connections are supported in the statistics.
-   The `connection_statistics_type_e` enumerator (in
    [mobile](../../api/mobile/latest/group__CAPI__NETWORK__CONNECTION__STATISTICS__MODULE.html#ga24b29d70490e8cd9ee34f45615ea1c63)
    and
    [wearable](../../api/wearable/latest/group__CAPI__NETWORK__CONNECTION__STATISTICS__MODULE.html#ga24b29d70490e8cd9ee34f45615ea1c63) applications)
    defines the statistics type.

The following example demonstrates how to get received data and sent
data for mobile connections:

```c++
long long total_received_size;

/* Gets statistics of total received data through the mobile network connection */
error_code = connection_get_statistics(connection, CONNECTION_TYPE_CELLULAR,
                                       CONNECTION_STATISTICS_TYPE_TOTAL_RECEIVED_DATA,
                                       &total_received_size);

long long total_sent_size;

/* Gets statistics of total sent data through the mobile network connection */
error_code = connection_get_statistics(connection, CONNECTION_TYPE_CELLULAR,
                                       CONNECTION_STATISTICS_TYPE_TOTAL_SENT_DATA,
                                       &total_sent_size);
```
