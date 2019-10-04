# Battery Monitor

You can access the information related to the power consumption by applications or by hardware resources on a battery-powered device for a certain duration of time. The value is returned as the percentage of the total batttery capacity.

The power consumption of an application is calculated by accumulating the usage of various individual resources used by the application.

The Battery Monitor APIs provide following provisions to fetch the battery usage:

- Getting battery usage information of a particular application.

  You can [retrieve information of an application](#appusage_get) by specifying its application ID, [resource](#resource_key) IDs and the time [duration](#duration_key).

- Getting battery usage information of a particular resource.

  You can [retrieve information of a single or muiltiple resources](#resourceusage_get) by specifying its [resource](#resource_key) IDs, and the time [duration](#duration_key).

## Prerequisites

To enable your application to use the Battery Monitor functionality:

1. To use the functions and data types of the Battery Monitor API (in [wearable](../../api/wearable/latest/group__CAPI__SYSTEM__BATTERY__MONITOR__MODULE.html) applications), include the `<battery_monitor.h>` header file in your application:

   ```
   #include <battery_monitor.h>
   ```

2. The application has to request permission by adding the following privileges to the `tizen-manifest.xml` file:

   ```xml
   <privileges>
      <privilege>http://tizen.org/privilege/systemmonitor</privilege>
   </privileges>
   ```

<a name="appusage_get"></a>
## Getting Battery Usage Information of Particular Application

The battery usage information contains a combination of application ID, resource ID and time duration.

1. Fetching information of an application for a particular resource over a certain duration of time.
   The `battery_monitor_resource_id_e`, `battery_monitor_duration_type_e` enums can be used to provide information related to specific resource and particular duration type respectively, as shown in the following code:

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

2. Fetching total battery usage information of an application ID by combining all the resources over certain a certain duration of time.
   The `battery_monitor_duration_type_e` enum can be used to choose a particular duration type, see the following code:

   ```
   #include <battery_monitor.h>

   void
   func(void)
   {
	char* app_id = "org.tizen.samsung";

	int error_code = BATTERY_MONITOR_ERROR_NONE;
	int battery_usage = -1;
	battery_monitor_duration_type_e duration_val = BATTERY_MONITOR_DURATION_TYPE_1DAY;

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

	return;
   }
   ```
3. Fetching battery usage values for all the resources used by an application ID for a certain duration of time.
   The `battery_monitor_resource_id_e`, `battery_monitor_duration_type_e` enums can be used to provide information related to specific resource and particular duration type respectively, as shown in the following code:

   ```
   #include <battery_monitor.h>

   void
   func(void)
   {
	battery_monitor_h data_handle = NULL;

	char* app_id = "org.tizen.samsung";
	int error_code = BATTERY_MONITOR_ERROR_NONE;
	int battery_usage = -1;
	battery_monitor_duration_type_e duration_val = BATTERY_MONITOR_DURATION_TYPE_1DAY;

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

	error_code = battery_monitor_destroy(data_handle);
	if (error_code != BATTERY_MONITOR_ERROR_NONE)
		printf("Error Occurred [%d]", error_code);

	free(app_id);

	return;
   }
   ```

<a name="resourceusage_get"></a>
## Getting Battery Usage Information of Particular Resource

The battery usage information contains combination of the resource ID and the time duration.

1. Fetching the battery usage information of a particular resource over a certain duration of time.
   The `battery_monitor_resource_id_e`, `battery_monitor_duration_type_e` enums can be used to provide information related to specific resource and particular duration type respectively, as shown in the following code:

   ```
   #include <battery_monitor.h>

   void
   func(void)
   {
	int error_code = BATTERY_MONITOR_ERROR_NONE;
	int battery_usage = -1;
	battery_monitor_resource_id_e resource_id = BATTERY_MONITOR_RESOURCE_ID_DISPLAY;
	battery_monitor_duration_type_e duration_val = BATTERY_MONITOR_DURATION_TYPE_1DAY;

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

	return;
   }
   ```
<a name="resource_key"></a>
## Resource Keys

The following table lists the available resource keys, which are part of `battery_monitor_resource_id_e` enumeration:

**Table: Resource Keys**
 | Key                                            | Description                                   |
 |------------------------------------------------|-----------------------------------------------|
 | `BATTERY_MONITOR_RESOURCE_ID_BLE`              | Indicates resource key for Bluetooth.         |
 | `BATTERY_MONITOR_RESOURCE_ID_WIFI`             | Indicates resource key for Wifi.              |
 | `BATTERY_MONITOR_RESOURCE_ID_CPU`              | Indicates resource key for CPU.               |
 | `BATTERY_MONITOR_RESOURCE_ID_DISPLAY`          | Indicates resource key for Display.           |
 | `BATTERY_MONITOR_RESOURCE_ID_DEVICE_NETWORK`   | Indicates resource key for Device Network.    |
 | `BATTERY_MONITOR_RESOURCE_ID_GPS_SENSOR`       | Indicates resource key for GPS Sensor.        |
 | `BATTERY_MONITOR_RESOURCE_ID_HRM_SENSOR`       | Indicates resource key for HRM Sensor.        |

<a name="duration_key"></a>
## Duration Types

The following table lists the available duration type keys, which are part of `battery_monitor_duration_type_e` enumeration:

**Table: Duration Type Keys**
 | Key                                            | Description                                          |
 |------------------------------------------------|------------------------------------------------------|
 | `BATTERY_MONITOR_DURATION_TYPE_1DAY`           | Indicates the Duration of last one day i.e. 24 hrs   |
 | `BATTERY_MONITOR_DURATION_TYPE_1WEEK`          | Indicates the Duration of last one week i.e. 7 days  |

## Related Information
- Dependencies
  - Tizen 5.5 and Higher for Wearable
