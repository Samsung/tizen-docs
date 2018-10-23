# Contextual Device Usage History Data


The Tizen platform collects data on the device usage. Based on this data, the applications can take advantage of the user's application usage patterns through statistical analysis.

The Contextual History API provides history data about application usage, media playback, communications, and device settings. Among context history data types, `CONTEXT_HISTORY_RECENTLY_USED_APP`, `CONTEXT_HISTORY_FREQUENTLY_USED_APP`, `CONTEXT_HISTORY_BATTERY_USAGE`, and `CONTEXT_HISTORY_RECENT_BATTERY_USAGE` are available for both mobile and wearable devices. The other history data types are supported in mobile applications only.

The main features of the Contextual History API include:

- Getting a profile data list

  You can get the device usage history profiles as a list of data records.

  When an application reads each [type of history data](#datatypes), the application can [set filters to specify the necessary statistics](#filters). The following example shows how to [get information about the 5 most frequently used applications](#get_list) from the last 30 days.

  ```
  /* Setting filter key and values */
  context_history_filter_set_int(filter, CONTEXT_HISTORY_FILTER_RESULT_SIZE, 5);
  context_history_filter_set_int(filter, CONTEXT_HISTORY_FILTER_TIME_SPAN, 30);

  /* Requesting the statistics */
  context_history_list_h list;
  context_history_get_list(handle, CONTEXT_HISTORY_FREQUENTLY_USED_APP, filter, &list);
  ```

- Enumerating profile data lists

  You can enumerate the records contained in the retrieved profile data list.

  Once the `context_history_list_h` data handle is retrieved through the `context_history_get_list()` function, you can [retrieve the attributes of each data record of the handle](#enumerate_list). You can use the `context_history_list_get_current()` function to get the current record and the `context_history_record_get_string()`, `context_history_record_get_int()`, and `context_history_record_get_double()` functions to access its values.

## Prerequisites

To use the functions and data types of the Contextual History API (in [mobile](../../api/mobile/latest/group__CAPI__CONTEXT__HISTORY__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__CONTEXT__HISTORY__MODULE.html) applications), include the `<context_history.h>` header file in your application:

```
#include <context_history.h>
```

<a name="get_list"></a>
## Getting a Profile Data List

To retrieve a contextual history profile:

1. Create 2 handles: 1 for using the Contextual History API and 1 for the filter:

   ```
   /* Contextual History API handle */
   context_history_h handle;
   context_history_create(&handle);

   /* Filter handle */
   context_history_filter_h filter;
   context_history_filter_create(&filter);
   ```

2. Get information about the 5 applications used most frequently during the last 2 weeks (14 days):

   ```
   /* Requesting the top 5 applications */
   context_history_filter_set_int(filter, CONTEXT_HISTORY_FILTER_RESULT_SIZE, 5);

   /* Limiting the time span of usage logs to 14 days */
   context_history_filter_set_int(filter, CONTEXT_HISTORY_FILTER_TIME_SPAN, 14);
   ```

3. Retrieve profile data based on the defined filter:

   ```
   context_history_list_h list;

   /* Getting the list of records */
   context_history_get_list(handle, CONTEXT_HISTORY_FREQUENTLY_USED_APP, filter, &list);

   /* Release the filter after use */
   context_history_filter_destroy(filter);
   ```

<a name="enumerate_list"></a>
## Enumerating Profile Data Lists

The list retrieved using the `context_history_get_list()` function contains a sorted list of records, each of which consists of a key and value pair.

To enumerate the list:

1. Check the number of records in the list.

   In some cases, the retrieved list can contain less records than the result size set in the filter.

   ```
   int size;
   context_history_list_get_count(list, &size);
   ```

2. Enumerate the list using a loop:

   ```
   int i;
   int count;
   char* app_id;
   context_history_record_h record;

   for (i = 0; i < size; ++i) {
       /* Getting the current record */
       context_history_list_get_current(list, &record);

       /* Retrieving the application ID and the total use count from the record */
       context_history_record_get_string(record, CONTEXT_HISTORY_APP_ID, &app_id);
       context_history_record_get_int(record, CONTEXT_HISTORY_TOTAL_COUNT, &count);

       /* Freeing the application ID string */
       free(app_id);

       /* Releasing the memory occupied by the record */
       context_history_record_destroy(record);

       /* Iterating to the next record */
       context_history_list_move_next(list);
   }
   ```

3. Release the list to prevent any resource leaks:

   ```
   context_history_list_destroy(list);
   ```

4. When no longer needed, release and destroy the handle:

   ```
   context_history_destroy(handle);
   ```

<a name="datatypes"></a>
## History Data Types

Through contextual history, you can mainly retrieve statistics for 3 categories of usage logs, including application usage, media playback, and communications. The following table summarizes the available history data types and required privileges.

**Table: History data types and required privileges**
<table>
	<thead>
		<tr>
			<th>History type</th>
			<th>Description and privilege</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Application usage history:
			<p><code>CONTEXT_HISTORY_RECENTLY_USED_APP</code></p>
			<p><code>CONTEXT_HISTORY_FREQUENTLY_USED_APP</code></p>
			<p><code>CONTEXT_HISTORY_RARELY_USED_APP</code></p>
			<p><code>CONTEXT_HISTORY_PEAK_TIME_FOR_APP</code></p>
			<p><code>CONTEXT_HISTORY_COMMON_SETTING_FOR_APP</code></p>
			<p><code>CONTEXT_HISTORY_BATTERY_USAGE</code></p>
			<p><code>CONTEXT_HISTORY_RECENT_BATTERY_USAGE</code></p>
			</td>
			<td>The contextual history contains data on which applications are used on the foreground. From this data, the following statistics are provided:
			<ul>
				<li>Most recently or frequently used applications, in a descending order of the application use counts.</li>
				<li>Most rarely used applications in removable applications, in an ascending order of the application use counts.</li>
				<li>Peak time for applications, or the time period when the user most frequently uses an application during the day.
				<p>The result is a sorted list of hours of the day, in a descending order of the application use count in each one-hour time slot.</p>
				</li>
				<li>Common settings for applications, or the most common setting values regarding an application or any applications.</li>
				<li>Most battery consuming applications, in a descending order of the battery consumption.</li>
			</ul>
			The required privilege is <code>http://tizen.org/privilege/apphistory.read</code>.</td>
		</tr>
		<tr>
			<td>Media playback history:
			<p><code>CONTEXT_HISTORY_PEAK_TIME_FOR_MUSIC</code></p>
			<p><code>CONTEXT_HISTORY_PEAK_TIME_FOR_VIDEO</code></p>
			<p><code>CONTEXT_HISTORY_COMMON_SETTING_FOR_MUSIC</code></p>
			<p><code>CONTEXT_HISTORY_COMMON_SETTING_FOR_VIDEO</code></p>
			</td>
			<td>Media playback events, including music and video playback, can be logged. From this data, the following statistics are provided:
			<ul>
				<li>Peak time for music or video playback, or the time period when the user most frequently listens to music or watches videos during the day.
				<p>The result is a sorted list of hours of the day, in a descending order of the playback count in each one-hour time slot.</p>
				</li>
				<li>Common settings for music or video playback, or the most common setting values when listening to music or watching videos.</li>
			</ul>
			<p>The required privilege is <code>http://tizen.org/privilege/mediahistory.read</code>.</p>
			<p>For more information on other media content metadata, such as when or how many times media content is played, see the <a href="https://developer.tizen.org/development/guides/native-application/media-and-camera/media-content-and-metadata/media-content">Media Content and Metadata</a> guide.</p>
			</td>
		</tr>
		<tr>
			<td>Communication history:
			<p><code>CONTEXT_HISTORY_FREQUENTLY_COMMUNICATED_ADDRESS</code></p>
			</td>
			<td>Applications can retrieve the contacts the user has called or messaged most frequently.
			<p>The required privilege is <code>http://tizen.org/privilege/callhistory.read</code>.</p>
			<p>For more information on the communication history, see the <a href="https://developer.tizen.org/development/guides/native-application/personal-data/contacts">Contacts</a> guide.</p>
			</td>
		</tr>
	</tbody>
</table>

> **Note**
>
> To compute the above usage history statistics, it is necessary to store and aggregate contextual events. In many cases, immediately reflecting the contextual events to the statistics costs more than applying the events in a batch later. For this reason, the above history statistics may not show up-to-date results all the time.

<a name="filters"></a>
## Filters and Attributes

Regarding each history data type, 1 or more filters can be set to specify the necessary statistics. For example, applications can get information about the 3 most frequently used applications from the last 30 days by setting the filters of the result size and time span. The supported filters for the history data types are summarized in the following table.

**Table: Supported filters for history data**
<table>
	<thead>
		<tr>
			<th>History type</th>
			<th>Supported filter</th>
			<th>Type</th>
			<th>Description</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td rowspan="2">All types, <strong>except</strong>:
			<p><code>CONTEXT_HISTORY_RECENT_BATTERY_USAGE</code></p>
			</td>
			<td><code>CONTEXT_HISTORY_FILTER_TIME_SPAN</code></td>
			<td>Integer</td>
			<td>This filter specifies in days the time span of the data to be aggregated. For example, if the value is set to 10, the application gets the statistics from the data logged in the last 10 days.
			<p>Only positive filter values are allowed. Because of the system resources available, the maximum time span can be limited implicitly. If the value is not set, the default value of 30 days is used.</p>
			</td>
		</tr>
		<tr>
			<td><code>CONTEXT_HISTORY_FILTER_START_TIME</code>
			<p><code>CONTEXT_HISTORY_FILTER_END_TIME</code></p>
			</td>
			<td>Integer</td>
			<td>If an application requires more fine-grained controls than the time span filter, the start and end time of the period can be set as Unix epoch time in seconds using these filters. It is also possible to set the start time or the end time only.</td>
		</tr>
		<tr>
			<td>All types, <strong>except</strong>:
			<p><code>CONTEXT_HISTORY_COMMON_SETTING_FOR_APP</code></p>
			<p><code>CONTEXT_HISTORY_COMMON_SETTING_FOR_MUSIC</code></p>
			<p><code>CONTEXT_HISTORY_COMMON_SETTING_FOR_VIDEO</code></p>
			</td>
			<td><code>CONTEXT_HISTORY_FILTER_RESULT_SIZE</code></td>
			<td>Integer</td>
			<td>This filter limits the number of data records to be retrieved. It accepts positive integers as the filter values, but if not set, it is set to 10 by default. It is possible that the aggregated result contains a smaller number of records than the filter value.
			<p>Note that this value may have no effect for some history types. For example, the common setting history types return one record for one request, thus the result size is ignored while aggregating the logs.</p>
			</td>
		</tr>
		<tr>
			<td rowspan="2"><code>CONTEXT_HISTORY_RECENTLY_USED_APP</code>
			<p><code>CONTEXT_HISTORY_FREQUENTLY_USED_APP</code></p>
			</td>
			<td><code>CONTEXT_HISTORY_FILTER_WIFI_BSSID</code></td>
			<td>String</td>
			<td>Applications can get the statistics of the data logged while a specific Wi-Fi is connected, by setting the BSSID string of the target Wi-Fi AP.
			<p>The currently connected Wi-Fi AP's BSSID can be retrieved through the Wi-Fi Manager APIs. For more information, see the <a href="https://developer.tizen.org/development/guides/native-application/connectivity-and-wireless/wi-fi">Wi-Fi</a> guide.</p>
			</td>
		</tr>
		<tr>
			<td><code>CONTEXT_HISTORY_FILTER_AUDIO_JACK</code></td>
			<td>Integer</td>
			<td>Applications can get the statistics of the data logged while the headphone is connected or disconnected. The audio jack status can be either <code>CONTEXT_HISTORY_FILTER_AUDIO_JACK_NOT_CONNECTED</code> or <code>CONTEXT_HISTORY_FILTER_AUDIO_JACK_CONNECTED</code>.</td>
		</tr>
		<tr>
			<td><code>CONTEXT_HISTORY_PEAK_TIME_FOR_APP</code>
			<p><code>CONTEXT_HISTORY_COMMON_SETTING_FOR_APP</code></p>
			</td>
			<td><code>CONTEXT_HISTORY_FILTER_APP_ID</code></td>
			<td>String</td>
			<td>Use this filter to compute the peak time (or the common settings) for a specific application. Without this filter, the peak time (or the common setting) is computed from the usage history of all applications.
			<p>For more information on the application IDs, see <a href="https://developer.tizen.org/development/training/native-application/tizen-application-model#packageID">Package ID and Application ID</a>.</p>
			</td>
		</tr>
		<tr>
			<td><code>CONTEXT_HISTORY_PEAK_TIME_FOR_APP</code>
			<p><code>CONTEXT_HISTORY_PEAK_TIME_FOR_MUSIC</code></p>
			<p><code>CONTEXT_HISTORY_PEAK_TIME_FOR_VIDEO</code></p>
			</td>
			<td><code>CONTEXT_HISTORY_FILTER_DAY_OF_WEEK</code></td>
			<td>Integer</td>
			<td>Use this filter to get usage patterns on weekdays or weekends. The filter value can be either <code>CONTEXT_HISTORY_FILTER_DAY_OF_WEEK_WEEKDAYS</code>, <code>CONTEXT_HISTORY_FILTER_DAY_OF_WEEK_WEEKENDS</code>, or <code>CONTEXT_HISTORY_FILTER_DAY_OF_WEEK_ALL</code>. Without this filter, data from both weekdays and weekends are used.</td>
		</tr>
		<tr>
			<td><code>CONTEXT_HISTORY_FREQUENTLY_COMMUNICATED_ADDRESS </code></td>
			<td><code>CONTEXT_HISTORY_FILTER_COMMUNICATION_TYPE</code></td>
			<td>Integer</td>
			<td>By default, communication frequency is computed from the call and message logs. Applications can narrow down the target data to one type of communication, call or messaging, using this filter.
			<p>The filter value can be either <code>CONTEXT_HISTORY_FILTER_COMMUNICATION_TYPE_CALL</code>, <code>CONTEXT_HISTORY_FILTER_COMMUNICATION_TYPE_MESSAGE</code>, or <code>CONTEXT_HISTORY_FILTER_COMMUNICATION_TYPE_ALL</code>.</p>
			</td>
		</tr>
	</tbody>
</table>

The history data records retrieved through the contextual history API contain the following data attributes.

**Table: Attributes provided by history data**
<table>
	<thead>
		<tr>
			<th>History type</th>
			<th>Provided attribute</th>
			<th>Type</th>
			<th>Description</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td rowspan="4"><code>CONTEXT_HISTORY_RECENTLY_USED_APP</code>
			<p><code>CONTEXT_HISTORY_FREQUENTLY_USED_APP</code></p>
			<p><code>CONTEXT_HISTORY_RARELY_USED_APP</code></p>
			</td>
			<td><code>CONTEXT_HISTORY_APP_ID</code></td>
			<td>String</td>
			<td>This attribute denotes the application ID.
			<p>For more information on the application IDs, see <a href="https://developer.tizen.org/development/training/native-application/tizen-application-model#packageID">Package ID and Application ID</a>.</p>
			</td>
		</tr>
		<tr>
			<td><code>CONTEXT_HISTORY_TOTAL_COUNT</code></td>
			<td>Integer</td>
			<td>This attribute denotes how many times the application is used on the foreground.</td>
		</tr>
		<tr>
			<td><code>CONTEXT_HISTORY_TOTAL_DURATION</code></td>
			<td>Integer</td>
			<td>This attribute denotes the time the application is being displayed on the foreground in seconds. If the application is used multiple times, it denotes the accumulated time of use.</td>
		</tr>
		<tr>
			<td><code>CONTEXT_HISTORY_LAST_TIME</code></td>
			<td>Integer</td>
			<td>This attribute denotes when the application has been used (moved to the foreground) the last time, in Unix epoch in seconds.</td>
		</tr>
		<tr>
			<td rowspan="2"><code>CONTEXT_HISTORY_PEAK_TIME_FOR_APP</code>
			<p><code>CONTEXT_HISTORY_PEAK_TIME_FOR_MUSIC</code></p>
			<p><code>CONTEXT_HISTORY_PEAK_TIME_FOR_VIDEO</code></p>
			</td>
			<td><code>CONTEXT_HISTORY_HOUR_OF_DAY</code></td>
			<td>Integer</td>
			<td>This attribute denotes the hour of the day. Its value is an integer from 0 to 23.</td>
		</tr>
		<tr>
			<td><code>CONTEXT_HISTORY_TOTAL_COUNT</code></td>
			<td>Integer</td>
			<td>This attribute denotes the aggregated count of the application uses or media playbacks within the hour of the day defined with <code>CONTEXT_HISTORY_HOUR_OF_DAY</code>.</td>
		</tr>
		<tr>
			<td rowspan="3"><code>CONTEXT_HISTORY_COMMON_SETTING_FOR_APP</code>
			<p><code>CONTEXT_HISTORY_COMMON_SETTING_FOR_MUSIC</code></p>
			<p><code>CONTEXT_HISTORY_COMMON_SETTING_FOR_VIDEO</code></p>
			</td>
			<td><code>CONTEXT_HISTORY_AUDIO_JACK</code></td>
			<td>Integer</td>
			<td>This attribute denotes the most common audio jack status. The value is either <code>CONTEXT_HISTORY_FILTER_AUDIO_JACK_NOT_CONNECTED</code> or <code>CONTEXT_HISTORY_FILTER_AUDIO_JACK_CONNECTED</code>.</td>
		</tr>
		<tr>
			<td><code>CONTEXT_HISTORY_SYSTEM_VOLUME</code></td>
			<td>Integer</td>
			<td>This attribute denotes the most common system volume level.</td>
		</tr>
		<tr>
			<td><code>CONTEXT_HISTORY_MEDIA_VOLUME</code></td>
			<td>Integer</td>
			<td>This attribute denotes the most common media volume level.
			<p>For more information on the system and media volume settings, see the <a href="https://developer.tizen.org/development/guides/native-application/media-and-camera/audio-management/sound-manager">Sound Manager</a> guide.</p>
			</td>
		</tr>
		<tr>
			<td rowspan="4"><code>CONTEXT_HISTORY_FREQUENTLY_COMMUNICATED_ADDRESS</code></td>
			<td><code>CONTEXT_HISTORY_ADDRESS</code></td>
			<td>String</td>
			<td>This attribute denotes the contact address or a phone number.</td>
		</tr>
		<tr>
			<td><code>CONTEXT_HISTORY_TOTAL_COUNT</code></td>
			<td>Integer</td>
			<td>This attribute denotes the total number of communications with the address defined with <code>CONTEXT_HISTORY_ADDRESS</code>.</td>
		</tr>
		<tr>
			<td><code>CONTEXT_HISTORY_TOTAL_DURATION</code></td>
			<td>Integer</td>
			<td>This attribute denotes the accumulated duration of calls in seconds with the address defined with <code>CONTEXT_HISTORY_ADDRESS</code>.</td>
		</tr>
		<tr>
			<td><code>CONTEXT_HISTORY_LAST_TIME</code></td>
			<td>Integer</td>
			<td>This attribute denotes when a call is connected or a message is received or sent last in Unix epoch in seconds, to or from the address defined with <code>CONTEXT_HISTORY_ADDRESS</code>.</td>
		</tr>
		<tr>
			<td rowspan="2"><code>CONTEXT_HISTORY_BATTERY_USAGE</code>
			<p><code>CONTEXT_HISTORY_RECENT_BATTERY_USAGE</code></p>
			</td>
			<td><code>CONTEXT_HISTORY_APP_ID</code></td>
			<td>String</td>
			<td>This attribute denotes the application ID.
			<p>For more information on the application IDs, see <a href="https://developer.tizen.org/development/training/native-application/tizen-application-model#packageID">Package ID and Application ID</a>.</p>
			</td>
		</tr>
		<tr>
			<td><code>CONTEXT_HISTORY_TOTAL_AMOUNT</code></td>
			<td>Double</td>
			<td>This attribute denotes the accumulated battery consumption of the application.</td>
		</tr>
	</tbody>
</table>

## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 4.0 and Higher for Wearable
