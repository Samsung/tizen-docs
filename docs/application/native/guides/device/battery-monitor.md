# Battery Monitor

You can access the information related to the power consumption by applications or by hardware resources available on a battery-powered device for a specific duration of time. The value of the battery power usage is returned in the milliampere hour(mAh).

The power consumption of an application is calculated by accumulating the usage of various individual resources used by the application.

This feature is supported in wearable applications only.

The Battery Monitor APIs provide the following provisions to fetch the battery usage:

- Getting battery usage information of an application.

    You can [retrieve the battery usage information of an application](#appusage_get) by specifying its application ID, [resource IDs](#resource_key), and timestamps such as **from** and **to** as per the Unix Epoch time format.

- Getting battery usage information of a resource.

    You can [retrieve the battery usage information of single or multiple resources](#resourceusage_get) by specifying its [resource IDs](#resource_key), and timestamps such as **from** and **to** as per the Unix Epoch time format.

    You can retrieve the data that is recorded within the last seven days.

## Prerequisites

To enable your application to use the Battery Monitor functionality:

1. To use the [Battery Monitor](../../api/wearable/latest/group__CAPI__SYSTEM__BATTERY__BATTERY__MONITOR__MODULE.html) API, the application has to request permission by adding the following privileges to the `tizen-manifest.xml` file:

    ```xml
    <privileges>
       <privilege>http://tizen.org/privilege/systemmonitor</privilege>
    </privileges>
    ```

2. To use the functions and data types of the Battery Monitor API, include the `<battery_monitor.h>` header file in your application:

    ```
    #include <battery_monitor.h>
    ```

<a name="appusage_get"></a>
## Get Battery Usage Information of Application

To get the battery usage information related to the application ID:

- Get the battery usage information of an application for a particular resource over a specific interval of time.
  To get the resource ID, use the `battery_monitor_resource_id_e` enum. The timestamps **from** and **to** must be set as per the Unix Epoch time format:

    ```
    #include <battery_monitor.h>
    #include <time.h>

    void
    func(void)
    {
       int error_code = BATTERY_MONITOR_ERROR_NONE;

       char* app_id = "org.tizen.samsung";
       double battery_usage = -1;
       battery_monitor_resource_id_e resource_id = BATTERY_MONITOR_RESOURCE_ID_CPU;
       time_t now, from = -1, to = -1; time(&now);

       /* To get the usage for past thousand seconds from current epoch time */
       int period_t = 1000;
       to = now; from = to - period_t;

       error_code = battery_monitor_get_power_usage_by_app_per_resource(app_id, resource_id, from, to, &battery_usage);

       if (error_code == BATTERY_MONITOR_ERROR_NONE)
           printf("The Battery Usage for appid [%s], for resource cpu is [%lf] mAh", app_id, battery_usage);
       else if (error_code == BATTERY_MONITOR_ERROR_RECORD_NOT_FOUND)
           printf("The Battery Usage for appid [%s], for resource cpu is not recorded", app_id);
       else
           printf("Error Occurred [%d]", error_code);

       free(app_id);

       return;
    }
    ```

- Get the total battery usage of an application ID over a specific interval of time. The timestamps **from** and **to** must be set as per the Unix Epoch time format:

    ```
    /* To get the usage for past 24 hours from the current epoch time */
    int period_t = 24*60*60; //24 hours in seconds
    to = now; from = to - period_t;

    error_code = battery_monitor_get_power_usage_by_app(app_id, from, to, &battery_usage);
    if (error_code == BATTERY_MONITOR_ERROR_NONE)
        printf("The Total Battery Usage for appid [%s] over last 24 hrs is [%lf]", app_id, battery_usage);
    else if (error_code == BATTERY_MONITOR_ERROR_RECORD_NOT_FOUND)
        printf("The Battery Usage for appid [%s] is not recorded", app_id);
    else
        printf("Error Occurred [%d]", error_code);

    /* To get usage for a period of thousand seconds starting two hours before the current epoch time */
    int period_t = 2*60*60; //2 hours in seconds
    from = now - period_t; to = from + 1000;

    error_code = battery_monitor_get_power_usage_by_app(app_id, from, to, &battery_usage);
    if (error_code == BATTERY_MONITOR_ERROR_NONE)
        printf("The Total Battery Usage for appid [%s] over 1000s interval is [%lf] mAh", app_id, battery_usage);
    else if (error_code == BATTERY_MONITOR_ERROR_RECORD_NOT_FOUND)
        printf("The Battery Usage for appid [%s] is not recorded", app_id);
    else
        printf("Error Occurred [%d]", error_code);

    ```

- Get the battery usage information of an application ID for each resource over a specific interval of time.
  To get the resource ID, use the `battery_monitor_resource_id_e` enum. The timestamps **from** and **to** must be set as per the Unix Epoch time format:

    ```
    battery_usage_data_h data_handle = NULL;
    /* To get the usage for past thousand seconds from the current epoch time */
    int period_t = 1000;
    to = now; from = to - period_t;

    /*Use this API to fetch the usage of all the available resources in the data handle*/
    error_code = battery_monitor_get_power_usage_by_app_for_all_resources(app_id, from, to, &data_handle);
    if (error_code == BATTERY_MONITOR_ERROR_NONE)
        printf("Data Handle information received");
    else if (error_code == BATTERY_MONITOR_ERROR_RECORD_NOT_FOUND)
        printf("The Battery Usage for appid [%s] is not recorded", app_id);
    else
        printf("Error Occurred [%d]", error_code);

    /*Retrieving the information one by one from the data_handle*/
    battery_monitor_resource_id_e resource_id = BATTERY_MONITOR_RESOURCE_ID_CPU;

    error_code = battery_monitor_usage_data_get_power_usage_per_resource(data_handle, resource_id, &battery_usage);
    if (error_code == BATTERY_MONITOR_ERROR_NONE)
        printf("The Battery Usage by CPU is [%lf]", battery_usage);

    resource_id = BATTERY_MONITOR_RESOURCE_ID_WIFI;

    error_code = battery_monitor_usage_data_get_power_usage_per_resource(data_handle, resource_id, &battery_usage);
    if (error_code == BATTERY_MONITOR_ERROR_NONE)
        printf("The Battery Usage by the Wi-Fi is [%lf]", battery_usage);
    else if (error_code == BATTERY_MONITOR_ERROR_RECORD_NOT_FOUND)
        printf("The Battery Usage for the resource is not recorded");

    /* Similarly for other resources.
    .
    . You can also iterate over the resource enums using 'BATTERY_MONITOR_RESOURCE_ID_MAX'
    .
    .
    */

    /*To avoid memory leak, free the handle*/
    error_code = battery_monitor_battery_usage_data_destroy(data_handle);
    if (error_code != BATTERY_MONITOR_ERROR_NONE)
        printf("Error Occurred [%d]", error_code);
    ```

<a name="resourceusage_get"></a>
## Get Battery Usage Information of Resource

To get the battery usage information related to the resource ID:

- Get the battery usage information of a particular resource over a specific interval of time.
  To get the resource ID, use the `battery_monitor_resource_id_e` enum. The timestamps **from** and **to** must be set as per the Unix Epoch time format:

    ```
    resource_id = BATTERY_MONITOR_RESOURCE_ID_DISPLAY;
    error_code = battery_monitor_get_power_usage_by_resource(resource_id, from, to, &battery_usage);
    if (error_code == BATTERY_MONITOR_ERROR_NONE)
        printf("The Battery Usage by Display in the last 1000 seconds is [%lf]", battery_usage);
    else if (error_code == BATTERY_MONITOR_ERROR_RECORD_NOT_FOUND)
        printf("The Battery Usage by Display is not recorded");

    resource_id = BATTERY_MONITOR_RESOURCE_ID_WIFI;
    error_code = battery_monitor_get_power_usage_by_resource(resource_id, from, to, &battery_usage);
    if (error_code == BATTERY_MONITOR_ERROR_NONE)
        printf("The Battery Usage by Wi-Fi in the last 1000 seconds is [%lf]", battery_usage);
    else if (error_code == BATTERY_MONITOR_ERROR_RECORD_NOT_FOUND)
        printf("The Battery Usage by Wi-Fi is not recorded");

    /* Similarly for other resources. */

    ```
<a name="resource_key"></a>
## Resource Keys

The following table lists the available resource keys, which are part of the `battery_monitor_resource_id_e` enumeration:

**Table: Resource Keys**

 | Key                                            | Description                              |
 |------------------------------------------------|------------------------------------------|
 | `BATTERY_MONITOR_RESOURCE_ID_BLE`              | Resource key for Bluetooth.              |
 | `BATTERY_MONITOR_RESOURCE_ID_WIFI`             | Resource key for Wi-Fi.                  |
 | `BATTERY_MONITOR_RESOURCE_ID_CPU`              | Resource key for CPU.                    |
 | `BATTERY_MONITOR_RESOURCE_ID_DISPLAY`          | Resource key for Display.                |
 | `BATTERY_MONITOR_RESOURCE_ID_DEVICE_NETWORK`   | Resource key for Device Network.         |
 | `BATTERY_MONITOR_RESOURCE_ID_GPS_SENSOR`       | Resource key for GPS Sensor.             |
 | `BATTERY_MONITOR_RESOURCE_ID_MAX`              | Key for iterating over enums only.       |

## Related Information
- Dependencies
  - Tizen 5.5 and Higher for Wearable
