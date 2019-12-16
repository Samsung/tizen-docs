# Battery Monitor

You can access the information related to the power consumption by applications or by hardware resources on a battery-powered device for a specific duration of time. The value is returned as the percentage of the total battery capacity.

The power consumption of an application is calculated by accumulating the usage of various individual resources used by the application.

This feature is supported in wearable applications only.

The Battery Monitor APIs provide following provisions to fetch the battery usage:

- Getting battery usage information of an application.

    You can [retrieve battery usage information of an application](#appusage_get) by specifying its application ID, [resource IDs](#resource_key), and the [time duration](#duration_key).

- Getting battery usage information of a resource.

    You can [retrieve battery usage information of single or multiple resources](#resourceusage_get) by specifying its [resource IDs](#resource_key), and the [time duration](#duration_key).

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
## Getting Battery Usage Information of Application

To get the battery usage information related to the application ID:

- Get battery usage information of an application for a particular resource over a specific duration of time.
  To get the resource ID, use the `battery_monitor_resource_id_e` enum and to get the time duration type information, use the `battery_monitor_duration_type_e` enum:

    ```
    #include <battery_monitor.h>

    void
    func(void)
    {
       char* app_id = "org.tizen.samsung";

       int error_code = BATTERY_MONITOR_ERROR_NONE;
       int battery_usage = -1;
       battery_monitor_resource_id_e resource_id = BATTERY_MONITOR_RESOURCE_ID_DISPLAY;
       battery_monitor_duration_type_e duration_val = BATTERY_MONITOR_DURATION_TYPE_1DAY;

       error_code = battery_monitor_get_usage_by_app_id_for_resource_id(app_id, resource_id, duration_val, &battery_usage);

       if (error_code == BATTERY_MONITOR_ERROR_NONE)
           printf("The Battery Usage for appid [%s], for resource display is [%d]", app_id, battery_usage);
       else
           printf("Error Occurred [%d]", error_code);

       resource_id = BATTERY_MONITOR_RESOURCE_ID_WIFI;
       duration_val = BATTERY_MONITOR_DURATION_TYPE_1WEEK;

       error_code = battery_monitor_get_usage_by_app_id_for_resource_id(app_id, resource_id, duration_val, &battery_usage);

       if (error_code == BATTERY_MONITOR_ERROR_NONE)
           printf("The Battery Usage for appid [%s], for resource wifi is [%d]", app_id, battery_usage);

       else
           printf("Error Occurred [%d]", error_code);

       free(app_id);

       return;
    }
    ```

- Get total battery usage of an application ID over a specific duration of time.
  To get a particular time duration type, use the `battery_monitor_duration_type_e` enum:

    ```
    duration_val = BATTERY_MONITOR_DURATION_TYPE_1DAY;
    error_code = battery_monitor_get_total_usage_by_app_id(app_id, duration_val, &battery_usage);
    if (error_code == BATTERY_MONITOR_ERROR_NONE)
        printf("The total battery usage for appid [%s] over last 24 hrs is [%d]", app_id, battery_usage);
    else
        printf("Error Occurred [%d]", error_code);

    duration_val = BATTERY_MONITOR_DURATION_TYPE_1WEEK;
    error_code = battery_monitor_get_total_usage_by_app_id(app_id, duration_val, &battery_usage);
    if (error_code == BATTERY_MONITOR_ERROR_NONE)
        printf("The total battery usage for appid [%s] over last 7 days is [%d]", app_id, battery_usage);
    else
        printf("Error Occurred [%d]", error_code);

    ```

- Get the battery usage information of an application ID for each resource over a specific duration of time.
  To get the resource ID, use the `battery_monitor_resource_id_e` enum and to get the time duration type information, use the `battery_monitor_duration_type_e` enum:

    ```
    battery_monitor_h data_handle = NULL;


    /*First use this API to fetch the usage for all the available resources in the data handle*/
    error_code = battery_monitor_get_usage_by_app_id_for_all_resource_id(app_id, duration_val, &data_handle);

    if (error_code == BATTERY_MONITOR_ERROR_NONE)
        printf("Data Handle information received");
    else
        printf("Error Occurred [%d]", error_code);

    /*Now retrieving the information one by one from the data_handle*/
    battery_monitor_resource_id_e resource_id = BATTERY_MONITOR_RESOURCE_ID_DISPLAY;

    error_code = battery_monitor_get_usage_for_resource_id(data_handle, resource_id, &battery_usage);
    if (error_code == BATTERY_MONITOR_ERROR_NONE)
        printf("Battery Usage by display is [%d]", battery_usage);

    resource_id = BATTERY_MONITOR_RESOURCE_ID_WIFI;

    error_code = battery_monitor_get_usage_for_resource_id(data_handle, resource_id, &battery_usage)
    if (error_code == BATTERY_MONITOR_ERROR_NONE)
        printf("Battery Usage by display is [%d]", battery_usage);

    /* Similarly for other resources...
    .
    .
    .
    */

    /*To avoid memory leak free the handle*/
    error_code = battery_monitor_destroy(data_handle);
    if (error_code != BATTERY_MONITOR_ERROR_NONE)
        printf("Error Occurred [%d]", error_code);
    ```

<a name="resourceusage_get"></a>
## Getting Battery Usage Information of Resource

To get battery usage information related to the resource ID:

- Get the battery usage information of a particular resource over a specific duration of time.
  To get the resource ID, use the `battery_monitor_resource_id_e` enum and to get time duration type information, use the `battery_monitor_duration_type_e` enum:

    ```
    resource_id = BATTERY_MONITOR_RESOURCE_ID_DISPLAY;
    error_code = battery_monitor_get_total_usage_by_resource_id(resource_id, duration_val, &battery_usage);
    if (error_code == BATTERY_MONITOR_ERROR_NONE)
        printf("Battery Usage Display in last 24 hrs is [%d]", battery_usage);

    resource_id = BATTERY_MONITOR_RESOURCE_ID_WIFI;
    error_code = battery_monitor_get_total_usage_by_resource_id(resource_id, duration_val, &battery_usage);
    if (error_code == BATTERY_MONITOR_ERROR_NONE)
        printf("Battery Usage Wifi in last 24 hrs is [%d]", battery_usage);

    /* Similarly for other resources...
    .
    .
    .
    */

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
 | `BATTERY_MONITOR_RESOURCE_ID_HRM_SENSOR`       | Resource key for HRM Sensor.             |

<a name="duration_key"></a>
## Duration Types

The following table lists the available duration type keys, which are part of the `battery_monitor_duration_type_e` enumeration:

**Table: Duration Type Keys**

 | Key                                            | Description                              |
 |------------------------------------------------|------------------------------------------|
 | `BATTERY_MONITOR_DURATION_TYPE_1DAY`           | Duration of last one day (24 hrs)        |
 | `BATTERY_MONITOR_DURATION_TYPE_1WEEK`          | Duration of last one week (7 days)       |

## Related Information
- Dependencies
  - Tizen 5.5 and Higher for Wearable
