# Contextual Device Usage History Data
## Dependencies
- Tizen 2.4 and Higher for Mobile
- Tizen 4.0 and Higher for Wearable

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

To use the functions and data types of the Contextual History API (in [mobile](../../../../org.tizen.native.mobile.apireference/group__CAPI__CONTEXT__HISTORY__MODULE.html) and [wearable](../../../../org.tizen.native.wearable.apireference/group__CAPI__CONTEXT__HISTORY__MODULE.html) applications), include the `<context_history.h>` header file in your application:

```
#include <context_history.h>
```

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

## History Data Types

Through contextual history, you can mainly retrieve statistics for 3 categories of usage logs, including application usage, media playback, and communications. The following table summarizes the available history data types and required privileges.

**Table: History data types and required privileges**

| History type                             | Description and privilege                |
| ---------------------------------------- | ---------------------------------------- |
| Application usage history:<br> `CONTEXT_HISTORY_RECENTLY_USED_APP`<br>`CONTEXT_HISTORY_FREQUENTLY_USED_APP`<br>`CONTEXT_HISTORY_RARELY_USED_APP`<br>`CONTEXT_HISTORY_PEAK_TIME_FOR_APP`<br>`CONTEXT_HISTORY_COMMON_SETTING_FOR_APP`<br>`CONTEXT_HISTORY_BATTERY_USAGE`<br>`CONTEXT_HISTORY_RECENT_BATTERY_USAGE` | The contextual history contains data on which applications are used on the foreground. From this data, the following statistics are provided:<br><br> - Most recently or frequently used applications, in a descending order of the application use counts.<br> - Most rarely used applications in removable applications, in an ascending order of the application use counts.<br> - Peak time for applications, or the time period when the user most frequently uses an application during the day.The result is a sorted list of hours of the day, in a descending order of the application use count in each one-hour time slot.<br> - Common settings for applications, or the most common setting values regarding an application or any applications.<br>- Most battery consuming applications, in a descending order of the battery consumption.<br><br> The required privilege is `http://tizen.org/privilege/apphistory.read`. |
| Media playback history:<br> `CONTEXT_HISTORY_PEAK_TIME_FOR_MUSIC`<br>`CONTEXT_HISTORY_PEAK_TIME_FOR_VIDEO`<br>`CONTEXT_HISTORY_COMMON_SETTING_FOR_MUSIC`<br>`CONTEXT_HISTORY_COMMON_SETTING_FOR_VIDEO` | Media playback events, including music and video playback, can be logged. From this data, the following statistics are provided:<br><br>- Peak time for music or video playback, or the time period when the user most frequently listens to music or watches videos during the day.The result is a sorted list of hours of the day, in a descending order of the playback count in each one-hour time slot.<br>- Common settings for music or video playback, or the most common setting values when listening to music or watching videos.<br><br>The required privilege is `http://tizen.org/privilege/mediahistory.read`.For more information on other media content metadata, such as when or how many times media content is played, see the [Media Content and Metadata](../media/media-content-n.md) guide. |
| Communication history:`CONTEXT_HISTORY_FREQUENTLY_COMMUNICATED_ADDRESS` | Applications can retrieve the contacts the user has called or messaged most frequently.The required privilege is `http://tizen.org/privilege/callhistory.read`.<br>For more information on the communication history, see the [Contacts](contacts-n.md) guide. |

> **Note**  
> To compute the above usage history statistics, it is necessary to store and aggregate contextual events. In many cases, immediately reflecting the contextual events to the statistics costs more than applying the events in a batch later. For this reason, the above history statistics may not show up-to-date results all the time.

## Filters and Attributes

Regarding each history data type, 1 or more filters can be set to specify the necessary statistics. For example, applications can get information about the 3 most frequently used applications from the last 30 days by setting the filters of the result size and time span. The supported filters for the history data types are summarized in the following table.

**Table: Supported filters for history data**

| History  type                            | Supported  filter                        | Type    | Description                              |
| ---------------------------------------- | ---------------------------------------- | ------- | ---------------------------------------- |
| All  types, except:<br>    CONTEXT_HISTORY_RECENT_BATTERY_USAGE | CONTEXT_HISTORY_FILTER_TIME_SPAN         | Integer | This filter  specifies in days the time span of the data to be aggregated. For example, if  the value is set to 10, the application gets the statistics from the data  logged in the last 10 days.<br>    Only positive filter values are allowed. Because of the system resources  available, the maximum time span can be limited implicitly. If the value is  not set, the default value of 30 days is used. |
| All  types, except:<br>    CONTEXT_HISTORY_RECENT_BATTERY_USAGE | CONTEXT_HISTORY_FILTER_START_TIME<br>    CONTEXT_HISTORY_FILTER_END_TIME | Integer | If an  application requires more fine-grained controls than the time span filter,  the start and end time of the period can be set as Unix epoch time in seconds  using these filters. It is also possible to set the start time or the end  time only. |
| All  types, except:<br>    CONTEXT_HISTORY_COMMON_SETTING_FOR_APP<br>        CONTEXT_HISTORY_COMMON_SETTING_FOR_MUSIC<br>        CONTEXT_HISTORY_COMMON_SETTING_FOR_VIDEO<br> | CONTEXT_HISTORY_FILTER_RESULT_SIZE       | Integer | This filter  limits the number of data records to be retrieved. It accepts positive  integers as the filter values, but if not set, it is set to 10 by default. It  is possible that the aggregated result contains a smaller number of records  than the filter value.    <br><br>    Note that this value may have no effect for some history types. For  example, the common setting history types return one record for one request,  thus the result size is ignored while aggregating the logs. |
| CONTEXT_HISTORY_RECENTLY_USED_APP<br>    CONTEXT_HISTORY_FREQUENTLY_USED_APP | CONTEXT_HISTORY_FILTER_WIFI_BSSID        | String  | Applications  can get the statistics of the data logged while a specific Wi-Fi is  connected, by setting the BSSID string of the target Wi-Fi  AP.<br><br>        The currently connected Wi-Fi AP's BSSID can be retrieved through the Wi-Fi  Manager APIs. For more information, see the [Wi-Fi](../connectivity/wifi-n.md)  guide. |
| CONTEXT_HISTORY_RECENTLY_USED_APP<br>    CONTEXT_HISTORY_FREQUENTLY_USED_APP | CONTEXT_HISTORY_FILTER_AUDIO_JACK        | Integer | Applications  can get the statistics of the data logged while the headphone is connected or  disconnected. The audio jack status can be either <br> CONTEXT_HISTORY_FILTER_AUDIO_JACK_NOT_CONNECTED or<br> CONTEXT_HISTORY_FILTER_AUDIO_JACK_CONNECTED. |
| CONTEXT_HISTORY_PEAK_TIME_FOR_APP  <br>    CONTEXT_HISTORY_COMMON_SETTING_FOR_APP | CONTEXT_HISTORY_FILTER_APP_ID            | String  | Use  this filter to compute the peak time (or the common settings) for a specific  application. Without this filter, the peak time (or the common setting) is  computed from the usage history of all applications.<br>    For more information on the application IDs, see [Package ID and Application ID](../../../../org.tizen.training/html/native/app_model/application_model_n.htm#packageID) |
| CONTEXT_HISTORY_PEAK_TIME_FOR_APP<br>    CONTEXT_HISTORY_PEAK_TIME_FOR_MUSIC<br>    CONTEXT_HISTORY_PEAK_TIME_FOR_VIDEO | CONTEXT_HISTORY_FILTER_DAY_OF_WEEK       | Integer | Use this filter  to get usage patterns on weekdays or weekends. The filter value can be either  <br> CONTEXT_HISTORY_FILTER_DAY_OF_WEEK_WEEKDAYS, <br> CONTEXT_HISTORY_FILTER_DAY_OF_WEEK_WEEKENDS, or <br> CONTEXT_HISTORY_FILTER_DAY_OF_WEEK_ALL.<br> Without this filter, data from both weekdays and  weekends are used. |
| CONTEXT_HISTORY_FREQUENTLY_COMMUNICATED_ADDRESS | CONTEXT_HISTORY_FILTER_COMMUNICATION_TYPE | Integer | By default,  communication frequency is computed from the call and message logs.  Applications can narrow down the target data to one type of communication,  call or messaging, using this filter.<br><br>    The filter value can be either<br>  CONTEXT_HISTORY_FILTER_COMMUNICATION_TYPE_CALL, <br>  CONTEXT_HISTORY_FILTER_COMMUNICATION_TYPE_MESSAGE, or <br>  CONTEXT_HISTORY_FILTER_COMMUNICATION_TYPE_ALL. |

The history data records retrieved through the contextual history API contain the following data attributes.

**Table: Attributes provided by history data**

| History type                             | Provided attribute            | Type                                     | Description                              |
| ---------------------------------------- | ----------------------------- | ---------------------------------------- | ---------------------------------------- |
| `CONTEXT_HISTORY_RECENTLY_USED_APP`<br> `CONTEXT_HISTORY_FREQUENTLY_USED_APP`<br> `CONTEXT_HISTORY_RARELY_USED_APP` | `CONTEXT_HISTORY_APP_ID`      | String                                   | This attribute denotes the application ID.For more information on the application IDs, see [Package ID and Application ID](../../../../org.tizen.training/html/native/app_model/application_model_n.htm#packageID). |
|`CONTEXT_HISTORY_RECENTLY_USED_APP`<br> `CONTEXT_HISTORY_FREQUENTLY_USED_APP`<br> `CONTEXT_HISTORY_RARELY_USED_APP` | `CONTEXT_HISTORY_TOTAL_COUNT`            | Integer                       | This attribute denotes how many times the application is used on the foreground. |                    
| `CONTEXT_HISTORY_RECENTLY_USED_APP`<br> `CONTEXT_HISTORY_FREQUENTLY_USED_APP`<br> `CONTEXT_HISTORY_RARELY_USED_APP` |`CONTEXT_HISTORY_TOTAL_DURATION`         | Integer                       | This attribute denotes the time the application is being displayed on the foreground in seconds. If the application is used multiple times, it denotes the accumulated time of use. |                                          
| `CONTEXT_HISTORY_RECENTLY_USED_APP`<br> `CONTEXT_HISTORY_FREQUENTLY_USED_APP`<br> `CONTEXT_HISTORY_RARELY_USED_APP` |`CONTEXT_HISTORY_LAST_TIME`              | Integer                       | This attribute denotes when the application has been used (moved to the foreground) the last time, in Unix epoch in seconds. |                                          
| `CONTEXT_HISTORY_PEAK_TIME_FOR_APP`<br> `CONTEXT_HISTORY_PEAK_TIME_FOR_MUSIC`<br> `CONTEXT_HISTORY_PEAK_TIME_FOR_VIDEO` | `CONTEXT_HISTORY_HOUR_OF_DAY` | Integer                                  | This attribute denotes the hour of the day. Its value is an integer from 0 to 23. |
| `CONTEXT_HISTORY_PEAK_TIME_FOR_APP`<br> `CONTEXT_HISTORY_PEAK_TIME_FOR_MUSIC`<br> `CONTEXT_HISTORY_PEAK_TIME_FOR_VIDEO`| `CONTEXT_HISTORY_TOTAL_COUNT`            | Integer                       | This attribute denotes the aggregated count of the application uses or media playbacks within the hour of the day defined with `CONTEXT_HISTORY_HOUR_OF_DAY`. |                    
| `CONTEXT_HISTORY_COMMON_SETTING_FOR_APP`<br> `CONTEXT_HISTORY_COMMON_SETTING_FOR_MUSIC`<br> `CONTEXT_HISTORY_COMMON_SETTING_FOR_VIDEO` | `CONTEXT_HISTORY_AUDIO_JACK`  | Integer                                  | This attribute denotes the most common audio jack status. The value is either `CONTEXT_HISTORY_FILTER_AUDIO_JACK_NOT_CONNECTED` or `CONTEXT_HISTORY_FILTER_AUDIO_JACK_CONNECTED`. |
| `CONTEXT_HISTORY_COMMON_SETTING_FOR_APP`<br> `CONTEXT_HISTORY_COMMON_SETTING_FOR_MUSIC`<br> `CONTEXT_HISTORY_COMMON_SETTING_FOR_VIDEO` |`CONTEXT_HISTORY_SYSTEM_VOLUME`          | Integer                       | This attribute denotes the most common system volume level. |                                          
| `CONTEXT_HISTORY_COMMON_SETTING_FOR_APP`<br> `CONTEXT_HISTORY_COMMON_SETTING_FOR_MUSIC`<br> `CONTEXT_HISTORY_COMMON_SETTING_FOR_VIDEO` |`CONTEXT_HISTORY_MEDIA_VOLUME`           | Integer                       | This attribute denotes the most common media volume level.For more information on the system and media volume settings, see the [Sound Manager](../media/sound-n.md) guide. |                                          
| `CONTEXT_HISTORY_FREQUENTLY_COMMUNICATED_ADDRESS` | `CONTEXT_HISTORY_ADDRESS`     | String                                   | This attribute denotes the contact address or a phone number. |
|  `CONTEXT_HISTORY_FREQUENTLY_COMMUNICATED_ADDRESS` |`CONTEXT_HISTORY_TOTAL_COUNT`            | Integer                       | This attribute denotes the total number of communications with the address defined with `CONTEXT_HISTORY_ADDRESS`. |                                        
|  `CONTEXT_HISTORY_FREQUENTLY_COMMUNICATED_ADDRESS` |`CONTEXT_HISTORY_TOTAL_DURATION`         | Integer                       | This attribute denotes the accumulated duration of calls in seconds with the address defined with `CONTEXT_HISTORY_ADDRESS`. |                                        
|  `CONTEXT_HISTORY_FREQUENTLY_COMMUNICATED_ADDRESS` |`CONTEXT_HISTORY_LAST_TIME`              | Integer                       | This attribute denotes when a call is connected or a message is received or sent last in Unix epoch in seconds, to or from the address defined with `CONTEXT_HISTORY_ADDRESS`. |                                       
| `CONTEXT_HISTORY_BATTERY_USAGE`<br> `CONTEXT_HISTORY_RECENT_BATTERY_USAGE` | `CONTEXT_HISTORY_APP_ID`      | String                                   | This attribute denotes the application ID.For more information on the application IDs, see [Package ID and Application ID](../../../../org.tizen.training/html/native/app_model/application_model_n.htm#packageID). |
| `CONTEXT_HISTORY_BATTERY_USAGE`<br> `CONTEXT_HISTORY_RECENT_BATTERY_USAGE` |`CONTEXT_HISTORY_TOTAL_AMOUNT`           | Double                        | This attribute denotes the accumulated battery consumption of the application. |                                          