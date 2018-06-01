# Calendar


A calendar is a system of organizing days for social purposes. It is composed of [records](#record2), such as events and todos. The records consist of subrecords, such as alarms, attendees, or extensions. For example, if an event is recurring, separate instances are generated for each time the event occurs.

The calendar information is stored in a calendar database. To manage the information in the database, you must [connect to the calendar service](#prerequisites). The calendar service module works in a way similar to a client-service architecture. In this architecture, the Tizen application is the client side and has to connect to the service before using calendar service APIs.

The following figure illustrates the calendar model.

**Figure: Calendar model**

![Calendar model](./media/calendar_model.png)

The main features of the Calendar API include:

- Calendar books

  - Determine where the events and todos belong.
  - Create [calendar books](#book) using the local device (with no account), service providers, such as Google or Yahoo (with an account), or applications, such as Joyn or Facebook.
  - Search and organize events using [filters and queries](#filter2).
  - Monitor [database changes](#change).

  Each account can have multiple calendar books. The calendar book name does not need to be unique on the device because it is handled with an ID. Since the local device address book has no account, its related account ID is zero.

- Events and todos

  - Manage [event instances](#event).
  - Create [events](#create_event) and [todos](#create), set properties for them, such as summary, start time, and description, and store them in the database.
  - Update [event](#update_event) and [todo](#update) details in the database.
  - Delete [events](#delete_event) and [todos](#delete) from the database.
  - Set [reminders](#remind).

The calendar service supports [vCalendars](#vcal).

The following figure illustrates the different Calendar entities and their relationships.

**Figure: Calendar entities**

![Calendar entities](./media/calendar_entity.png)

<a name="record2"></a>
## Records

A record represents an actual record in the internal database, but you can consider it as a structure describing a single but complex entity, such as a calendar event or a time zone.

A record has many properties, for example, a todo record has the todo description, priority, progress, creation time, last modified and completed time, and many other properties. A record can also contain an identifier field, which holds an ID of another record. Setting this field's value establishes a relation between the records, for example, a calendar event contains the ID of a calendar book to which it belongs.

To use a record, you must obtain its handle. You can use many methods to obtain the handle, for example, you can create a new record or use an existing record ID:

- Obtaining the handle when creating a record:

  ```
  /* Create an event and get a handle */
  calendar_record_h event = NULL;
  calendar_record_create(_calendar_event._uri, &event);
  ```

- Obtaining the handle using the ID:

  ```
  /* Get the record handle with ID */
  calendar_record_h event2 = NULL;
  calendar_db_get_record(_calendar_event._uri, event_id, &event2);
  ```

To manage the record using the handle, you can use the URI, views, or basic types:

- URI

  A record type is identified by a structure called the view. For example, the `_calendar_event` view describes the properties of the calendar event record. Every view has a special field - `_uri` - that uniquely identifies the view. In many cases, you must provide the `_uri` value to indicate what type of record you want to create or operate on.

  ```
  /* Create an event with the _calendar_event view */
  calendar_record_h record = NULL;
  calendar_record_create(_calendar_event._uri, &record);
  ```

- Views and properties

  Generic access functions can be used (according to data-view declarations) to access calendar views. A data-view is almost the same as a database "VIEW", which limits access and guarantees performance. A "record" represents a single row of the data-views.

  **Table: Calendar views**

  | Editable view                            | Read-only view                           |
  |------------------------------------------|------------------------------------------|
  | `_calendar_book`<br>`_calendar_event`<br>`_calendar_todo`<br>`_calendar_timezone`<br>`_calendar_attendee`<br>`_calendar_alarm`<br>`_calendar_extended_property` | `_calendar_updated_info`<br>`_calendar_event_calendar_book`<br>`_calendar_todo_calendar_book`<br>`_calendar_event_calendar_book_attendee`<br>`_calendar_instance_utime_calendar_book`<br>`_calendar_instance_localtime_calendar_book`<br>`_calendar_instance_utime_calendar_book_extended`<br>`_calendar_instance_localtime_calendar_book_extended` |

  The `_calendar_updated_info` view is used when identifying record changes depending on the version. The other read-only views are a combination of editable views for UI convenience:

  - `_calendar_event` + `_calendar_book` = `_calendar_event_calendar_book`
  - `_calendar_instance_utime` + `_calendar_book` = `_calendar_instance_utime_calendar_book`
  - `_calendar_event` + `_calendar_book` + `_calendar_attendee` = `_calendar_event_calendar_book_attendee`

  > **Note**  
  > The `_calendar_instance_utime` and `_calendar_instance_localtime` views are not available as editable views, but can be used in combination with other views in read-only views.

  The record types that have `*_id` as their property hold identifiers of other records. For example, the attendee and alarm views hold the ID of their corresponding events or todos in the `event_id` or `todo_id` property (as children of the corresponding event or todo records).

  The `record` type properties are other records. For example, an event record has `attendee` and `alarm` record properties, which means that records of those types can be children of the event type records. The following figure illustrates macros in a `calendar_view.h` header file.

  **Figure: Properties**

  ![Properties](./media/calendar_property.png)

  The calendar service uses a version system in the following APIs:

  ```
  calendar_db_get_current_version(int *calendar_db_version)
  calendar_db_get_changes_by_version(..., int *current_calendar_db_version)
  calendar_db_get_last_change_version(int *last_change_version)
  calendar_db_get_changes_exception_by_version(..., int calendar_db_version, ...)
  ```

  Whenever modifications are made in the database, the version number is increased. If sync applications, such as Google or Facebook, sync at version 13 and try to sync again every 1 minute, they want to get the changes from version 14 to the current version.

  To get the current version, the `calendar_db_get_current_version()` function is used. The `calendar_db_get_changes_by_version()` function retrieves the modified record list. The `calendar_db_get_changes_exception_by_version()` function is used to get [modified instances in a recurring event](#exception_rule).

- Basic types

  Records contain properties of basic types: `integer`, `lli` (long integer, long long int), `double`, `string`, `bool`, and `time`. The `time` type holds either a long long int, or 3 integers (year, month, day).

  The following table lists the setter and getter functions for each type.

  **Table: Setter and getter functions**

  | Property            | Setter                          | Getter                          |
  |---------------------|---------------------------------|---------------------------------|
  | `integer`           | `calendar_record_set_int()`     | `calendar_record_get_int()`     |
  | `long long integer` | `calendar_record_set_lli()`     | `calendar_record_get_lli()`     |
  | `double`            | `calendar_record_set_double()`  | `calendar_record_get_double()`  |
  | `string`            | `calendar_record_set_str()`     | `calendar_record_get_str()`     |
  | `calendar_time_s`   | `calendar_record_set_caltime()` | `calendar_record_get_caltime()` |

  These functions also require specifying which property to get and set, and for this, every getter and setter function needs a record and property ID. Create a property ID by combining the data-view and property name. For example, the property ID of an event `summary` property is `_calendar_event.summary`.

  The following example sets the `summary` property of an event record:

  ```
  /* Create an event with the _calendar_event view */
  calendar_record_h event = NULL;
  calendar_record_create(_calendar_event._uri, &event);

  /* Set event summary to the _calendar_event view */
  calendar_record_set_str(event, _calendar_event.summary, "Meeting");
  ```

  <a name="time"></a>
  The calendar time structure property, `calendar_caltime_s`, is defined as follows:

  ```
  struct _calendar_time_s {
      calendar_time_type_e type;
      union {
          long long int utime;
          struct {
              int year;
              int month;
              int mday;
          } date;
      } time;
  };
  typedef struct _calendar_time_s calendar_time_s;
  ```

  Use this structure when setting the calendar time (`_CALENDAR_PROPERTY_CALTIME`) properties of the records.

  The time structure can hold 2 types of data, as defined in the following table. These types are identified by the values of the `calendar_time_type_e` variable (in [mobile](../../api/mobile/latest/group__CAPI__SOCIAL__CALENDAR__SVC__RECORD__MODULE.html#ga809c1bb1db41169c65939b929520e9b6) and [wearable](../../api/wearable/latest/group__CAPI__SOCIAL__CALENDAR__SVC__RECORD__MODULE.html#ga809c1bb1db41169c65939b929520e9b6) applications), and they determine the usage of the structure.

  **Table: Data types**

  | Identifier                | Type            | Name  | Purpose                                  |
  |---------------------------|-----------------|-------|------------------------------------------|
  | `CALENDAR_TIME_UTIME`     | `long long int` | utime | UTC time is used to describe non-all-day events.<br> For non-all-day events, you must convert local time to UTC time. The local time zone identifier must be stored in the record, in the corresponding property.<br> For example, when setting the start time of an event, the local time zone must be stored in the `start_tzid` property. |
  | `CALENDAR_TIME_LOCALTIME` | `struct`        | date  | Date only (year, month, and day of the month) is used to describe all day events.<br> For all day events, the structure type field must be set to `CALENDAR_TIME_LOCALTIME`. Only the date (no time) is stored.<br> Both the start and end time of the event must be set, and they do not have to be equal. If they are not, the event lasts more than 1 day. Note that in such cases there are no instances created, as this is still a non-recurring event. |

  When converting local time to UTC time, use the function shown in the following example. It converts the given date and time to the corresponding UTC time, considering the given time zone (first parameter). The function uses the i18n API (in [mobile](../../api/mobile/latest/group__CAPI__BASE__UTILS__I18N__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__BASE__UTILS__I18N__MODULE.html) applications).

  ```
  #define ms2sec(ms) (long long int)(ms / 1000.0)

  long long int
  _time_convert_itol(char *tzid, int y, int mon, int d, int h, int min, int s)
  {
      int ret = 0;
      i18n_uchar utf16_timezone[64] = {0};
      i18n_ustring_copy_ua_n(utf16_timezone, tzid, sizeof(utf16_timezone)/sizeof(i18n_uchar));

      i18n_ucalendar_h ucal = NULL;
      char *loc_default = NULL;

      i18n_ulocale_get_default((const char **)&loc_default);
      ret = i18n_ucalendar_create(utf16_timezone, -1, loc_default, I18N_UCALENDAR_GREGORIAN, &ucal);
      if (I18N_ERROR_NONE != ret) {
          dlog_print(DLOG_DEBUG, LOG_TAG, "i18n_ucalendar_create() failed (%d)\n", ret);

          return -1;
      }

      i18n_ucalendar_set_date_time(ucal, y, mon - 1, d, h, min, s);

      i18n_udate date;
      ret = i18n_ucalendar_get_milliseconds(ucal, &date);
      if (I18N_ERROR_NONE != ret) {
          dlog_print(DLOG_DEBUG, LOG_TAG, "i18n_ucalendar_create() failed (%d)\n", ret);
          i18n_ucalendar_destroy(ucal);

          return -1;
      }
      i18n_ucalendar_destroy(ucal);

      return ms2sec(date);
  }
  ```

  ```
  /* Fill calendar time structures (start and end time) */
  calendar_time_s st = {0};
  calendar_time_s et = {0};

  st.type = CALENDAR_TIME_UTIME;
  st.time.utime = _time_convert_itol("Asia/Seoul", 2012, 9, 15, 11, 0, 0);

  et.type = CALENDAR_TIME_UTIME;
  et.time.utime = _time_convert_itol("Asia/Seoul", 2012, 9, 15, 12, 0, 0);

  /* Create an event record */

  /* Set local time zone of start time */
  calendar_record_set_str(event, _calendar_event.start_tzid, "Asia/Seoul");

  /* Set start time */
  calendar_record_set_caltime(event, _calendar_event.start_time, st);

  /* Set local time zone of end time */
  calendar_record_set_str(event, _calendar_event.end_tzid, "Asia/Seoul");

  /* Set end time */
  calendar_record_set_caltime(event, _calendar_event.end_time, et);
  ```

### Child Records

A certain record type can be a parent of other records. For example, the attendee records can hold an event identifier in their `event_id` property. The event is the parent record of the attendee child records.

The following code example creates an event and inserts an attendee record into it as a child record:

```
calendar_record_h event = NULL;
calendar_record_h attendee = NULL;

int event_id = 0;

calendar_record_create(_calendar_event._uri, &event);

/* Attendee record can be a child record of the event record */
calendar_record_create(_calendar_attendee._uri, &attendee);
calendar_record_set_str(attendee, _calendar_attendee.name, "John");
calendar_record_add_child_record(event, _calendar_event.calendar_attendee, attendee);

/* Insert event into the database */
calendar_db_insert_record(event, &event_id);
calendar_record_destroy(event, true);
```

<a name="book"></a>
## Calendar Books

A calendar book is a placeholder for other calendar records. Every event and todo must belong to a calendar book. There are 3 built-in calendar books, as shown in the following table.

**Table: Calendar books**

| Book                                | Description   |
|-------------------------------------|---------------|
| `DEFAULT_EVENT_CALENDAR_BOOK_ID`    | Event book    |
| `DEFAULT_TODO_CALENDAR_BOOK_ID`     | Todo book     |
| `DEFAULT_BIRTHDAY_CALENDAR_BOOK_ID` | Birthday book |

The following code example sets a calendar book ID for an event:

```
calendar_record_h event = NULL;

calendar_record_create(_calendar_event._uri, &event);

/* Set default calendar book ID */
calendar_record_set_int(event, _calendar_event.calendar_id, DEFAULT_EVENT_CALENDAR_BOOK_ID);

/* Set other fields */

int event_id = 0;
calendar_db_insert_record(event, &event_id);

/* Destroy */
calendar_record_destroy(event, true);
```

To receive a list of existing calendar books, use the following code:

```
calendar_list_h calendar_book_list = NULL;
calendar_db_get_all_records(_calendar_calendar_book._uri, 0, 0, &calendar_book_list);
```

In the `calendar_db_get_all_records()` function, you need as parameters the URI of the view to get records from, the index from which results are received, the maximum number of results, and the record list.

<a name="event"></a>
## Event Instances and Reminders

An event record describes various properties, such as description, categories, and priority. It also contains information on when the event takes place. In a recurring event, there are more than 1 instances of the event. Each instance has its corresponding instance record.

If an event is inserted with rrule (recurrence rule), alarm, and attendee, its data is saved to each relevant database. Generated instances based on the rrule are also stored in the instance database.

**Figure: Views and databases for event instances**

![Views and databases for event instances](./media/calendar_db.png)

The following table illustrates an example of a recurring event and its instances.

**Table: Event and instance example**

| Event                                    | Instances                                |
|------------------------------------------|------------------------------------------|
| Recurrence rules:<br> - Start date on 2012-10-09 (Tuesday)<br> - Frequency set to WEEKLY<br> - Interval set to 1<br> - Count set to 3 | 2012-10-09 Tuesday<br> 2012-10-16 Tuesday<br> 2012-10-22 Tuesday |

The recurrence model in the Calendar API is compliant with the [iCalendar specification](http://www.ietf.org/rfc/rfc2445.txt). The following event properties have the same functionality as their corresponding values in iCalendar:

**Table: Recurrence rules**

| Recurrence rule property | Description                              |
|--------------------------|------------------------------------------|
| `freq`                   | Yearly, monthly, weekly, or daily        |
| `count`                  | Until count. If the count is 3, 3 instances are generated. |
| `interval`               | Interval is a positive integer representing how often the recurrence rule repeats |
| `byday`                  | MO, TU, WE, TH, FR, SA, or SU            |
| `bymonthday`             | Days of the month                        |
| `byyearday`              | Days of the year                         |
| `byweekno`               | Ordinals specifying weeks of the year    |
| `bymonth`                | Months of the year                       |
| `bysetpos`               | Values which correspond to the nth occurrence within the set of events |
| `wkst`                   | Day on which the workweek starts         |

When you have a recurring event, you can [remove a specific recurrence instance](#exception_add) from it, or [add exceptions to the recurrence](#exception_modify).

<a name="exception_rule"></a>
### Exceptions

If 1 of the instances of a recurring event is modified (such as its summary or date) or deleted, it is called an exception. For example, if the second instance date is modified from 16th to 17th, 17th is the exception.

**Table: Exception example**

| Event                                    | Instances                                | Exceptions         |
|------------------------------------------|------------------------------------------|--------------------|
| Recurrence rules:<br> - Start date on 2012-10-09 (Tuesday)<br> - Frequency set to WEEKLY<br> - Interval set to 1<br> - Count set to 3 | 2012-10-09 Tuesday<br> 2012-10-16 Tuesday > modified<br> 2012-10-22 Tuesday | 2012-10-17 Tuesday |

To get the changes in an exception, use the `calendar_db_get_changes_exception_by_version()` function. The instances and exceptions are deleted together when the original event is deleted.

<a name="remind"></a>
### Reminders

The following figure illustrates how the alarm process works.

**Figure: Alarm process**

![Alarm process](./media/calendar_alarm.png)

To get a reminder when an alarm is triggered, the application must set the reminder MIME name. After the reminder MIME name is set, insert an alarm as a child of an event record:

```
/* Set alarm */
calendar_record_h alarm = NULL;
calendar_record_create(_calendar_alarm._uri, &alarm);
calendar_record_set_int(alarm, _calendar_alarm.tick_unit, CALENDAR_ALARM_TIME_UNIT_SPECIFIC);
calendar_time_s at = {0};
at.type = CALENDAR_TIME_UTIME;
at.time.utime = (1404036000 - 60); /* 60 secs before 1404036000 (Sun, 29 Jun 2014 10:00:00 GMT) */
calendar_record_set_caltime(alarm, _calendar_alarm.alarm_time, at);

/* Add alarm as child */
calendar_record_add_child_record(event, _calendar_event.calendar_alarm, alarm);
```

When the registered alarm is triggered and the alarm manager notices it, the calendar service calls those packages that have the reminder MIME name.

<a name="filter2"></a>
## Filters and Queries

Queries are used to retrieve [event](#get_event) and [todo](#get) data which satisfies a given criteria, like an integer property being greater than a given value, or a string property containing a given substring. The criteria are defined by creating filters and adding conditions to them, joining them with logical operators. Also, instead of a condition, another filter can be added to create more complex filters.

When a filter is ready, it can be set as a property of a query. Other query properties allow configuring how the returned results are grouped and sorted.

To filter calendar data:

- Filtering

  The operator precedence in filters is determined by the order in which the conditions and filters are added. The following table shows an example of how the operator precedence works.

  **Table: Filter conditions**

  | Condition                                | Result                                   |
  |------------------------------------------|------------------------------------------|
  | Condition C1<br>OR<br>Condition C2<br>AND<br>Condition C3 | (C1 OR C2) AND C3                        |
  | **Filter F1**:<br>Condition C1<br>OR<br>Condition C2<br><br>**Filter F2**:<br>Condition C3<br>OR<br>Condition C4<br><br>**Filter F3**:<br>Condition C5<br>AND<br>F1<br>AND<br>F2 | (C5 AND F1) AND F2<br>Meaning (C5 AND (C1 OR C2)) AND (C3 OR C4) |

  The following code creates a filter, accepting events with high priority or those that include the word "meeting" in their description.

  ```
  calendar_filter_h filter = NULL;

  /* Create a filter returning event type records */
  calendar_filter_create(_calendar_event._uri, &filter);

  /* Add a 'priority equals high' condition */
  calendar_filter_add_int(filter, _calendar_event.priority, CALENDAR_MATCH_EQUAL, CALENDAR_EVENT_PRIORITY_HIGH);

  /* Add OR operator */
  calendar_filter_add_operator(filter, CALENDAR_FILTER_OPERATOR_OR);

  /* Add a 'description contains "meeting"' condition */
  calendar_filter_add_str(filter, _calendar_event.description, CALENDAR_MATCH_CONTAINS, "meeting");
  ```

  Insert the filter into the query and execute the query:

  ```
  calendar_query_h query = NULL;
  calendar_list_h list = NULL;

  /* Create a query returning event type records */
  calendar_query_create(_calendar_event._uri, &query);

  /* Add the filter */
  calendar_query_set_filter(query, filter);

  /* Execute the query, results are returned in a list */
  calendar_db_get_records_with_query(query, 0, 0, &list);

  calendar_filter_destroy(filter);
  calendar_query_destroy(query);

  /* Use the list */

  calendar_list_destroy(list, true);
  ```

- Projection querying

  A projection allows you to query the data for only those specific properties of a record that you actually need, at lower latency and cost than retrieving the entire set of properties.

  The following example code creates a filter that gets only the event ID, summary, and start time from the records with the "test" (string filter) in their summary. Create a query, and add a filter to it; the results are received in a list.

  ```
  calendar_query_h query = NULL;
  calendar_filter_h filter = NULL;

  /* Set query with filter */
  calendar_query_create(_calendar_event_calendar_book_attendee._uri, &query);
  calendar_filter_create(_calendar_event_calendar_book_attendee._uri, &filter);
  calendar_filter_add_str(filter, _calendar_event.summary, CALENDAR_MATCH_CONTAINS, "test");
  calendar_query_set_filter(query, filter);

  /* Set projection */
  unsigned int projection[3];
  projection[0] = _calendar_event_calendar_book_attendee.event_id;
  projection[1] = _calendar_event_calendar_book_attendee.summary;
  projection[2] = _calendar_event_calendar_book_attendee.start_time;

  /* Get list */
  calendar_query_set_projection(query, projection, 3);
  calendar_db_get_records_with_query(query, 0, 0, &list);

  /* Destroy handle */
  calendar_filter_destroy(filter);
  calendar_query_destroy(query);
  calendar_list_destroy(list, true);
  ```

<a name="change"></a>
## Database Change Notifications

To detect the [event](#monitor_event) and [todo](#monitor) changes in the calendar database, register a callback with the `calendar_db_add_changed_cb()` function. To deregister the callback and ignore database changes, use the `calendar_db_remove_changed_cb()` function.

Clients wait for calendar change notifications on the client side. If the calendar is changed by another module, the server publishes an inotify event. The Inotify module broadcasts to the subscribed modules, and an internal inotify handler is called at the client side. A user callback function is called with the user data.

```
/* Add callback function */
void __event_changed_ cb(const char *view_uri, void *user_data) {}
/* Add change notification callback */
calendar_db_add_changed_cb(_calendar_event._uri, __event_changed_cb, NULL);
```

<a name="vcal"></a>
## vCalendar

Use the vCalendar to exchange personal calendar and schedule information.

vCalendar supports versions 1.0 (vcs) and 2.0 (ics). vCalendar version 2.0 is known as iCalendar. For more information on vCalendar, see [rfc2445](http://www.ietf.org/rfc/rfc2445.txt).

The following snippet shows an example of the vCalendar:

```
BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//hacksw/handcal//NONSGML v1.0//EN
BEGIN:VEVENT
DTSTART:19970714T170000Z
DTEND:19970715T035959Z
SUMMARY:Bastille Day Party
END:VEVENT
END:VCALENDAR
```

To use the vCalendar:

- You can use the calendar service to [compose a vCalendar stream](#make). With the stream, it is possible to transmit data in JSON format.

  ```
  calendar_list_h list = NULL;
  /* Create or get list to make a vcalendar stream */

  char *stream = NULL;
  calendar_vcalendar_make_from_records(list, &stream);

  /* Jobs for stream */

  /* Free */
  free(stream);
  ```

- You can [parse the vCalendar](#parse):

  ```
  /* Read stream from file */

  calendar_list_h list = NULL;
  calendar_vcalendar_parse_to_calendar(stream, &list);

  /* Jobs for list */
  calendar_list_destroy(list, true);
  ```

<a name="prerequisites"></a>
## Prerequisites

To enable your application to use the calendar functionality:

1. To use the Calendar API (in [mobile](../../api/mobile/latest/group__CAPI__SOCIAL__CALENDAR__SVC__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__SOCIAL__CALENDAR__SVC__MODULE.html) applications), the application has to request permission by adding the following privileges to the `tizen-manifest.xml` file:

   ```
   <privileges>
      <privilege>http://tizen.org/privilege/calendar.read</privilege>
      <privilege>http://tizen.org/privilege/calendar.write</privilege>
   </privileges>
   ```

2. To use the functions and data types of the Calendar API, include the `<calendar.h>` header file in your application:

   ```
   #include <calendar.h>
   ```

   To ensure that a Calendar function has been executed properly, make sure that the return value is equal to `CALENDAR_ERROR_NONE`. If the function returns an error, handle it accordingly.

3. To access the calendar database, connect to the calendar service using the `calendar_connect()` function:

   ```
   int error_code;
   error_code = calendar_connect();
   if (error_code != CALENDAR_ERROR_NONE)
       dlog_print(DLOG_ERROR, LOG_TAG, "calendar_connect failed: %x\n", error_code);
   ```

   When the calendar service is no longer needed, disconnect from the service using the `calendar_disconnect()` function:

   ```
   error_code = calendar_disconnect();
   if (error_code != CALENDAR_ERROR_NONE)
       dlog_print(DLOG_ERROR, LOG_TAG, "calendar_disconnect failed: %x\n", error_code);
   ```

<a name="create_event"></a>
## Creating an Event

Creating a new event involves creating an event handle, setting the event properties, and inserting the event into the calendar database.

Some event properties are defined as child records that are associated with the parent record. For a detailed list of the event properties, see the `_calendar_event` view description in the Calendar API (in [mobile](../../api/mobile/latest/group__CAPI__SOCIAL__CALENDAR__SVC__VIEW__MODULE.html#CAPI_SOCIAL_CALENDAR_SVC_VIEW_MODULE_calendar_event) and [wearable](../../api/wearable/latest/group__CAPI__SOCIAL__CALENDAR__SVC__VIEW__MODULE.html#CAPI_SOCIAL_CALENDAR_SVC_VIEW_MODULE_calendar_event) applications). If the property type is `child list`, the property is defined as a child record.

To create a new event:

1. Create an event handle using the `calendar_record_create()` function with the `_calendar_event._uri` property as the first parameter and the event handle variable as the second parameter:

   ```
   calendar_record_h event = NULL;
   error_code = calendar_record_create(_calendar_event._uri, &event);
   if (error_code != CALENDAR_ERROR_NONE)
       dlog_print(DLOG_ERROR, LOG_TAG, "calendar_record_create failed: %x\n", error_code);
   ```

   > **Note**  
   > Records created with the `calendar_record_create()` function are memory objects, with `calendar_record_h` type variables as their handles. If you changes these objects, the changes are not reflected in the calendar database until you explicitly insert or update the objects to the database using the `calendar_db_insert_record()` or `calendar_db_update_record()` function.

2. Set the event properties:

   - Set the subject.

     To set the subject for the event, use the `calendar_record_set_str()` function with the `_calendar_event.summary` property as the second parameter:

     ```
     error_code = calendar_record_set_str(event, _calendar_event.summary, "summary");
     if (error_code != CALENDAR_ERROR_NONE)
         dlog_print(DLOG_ERROR, LOG_TAG, "set summary failed: %x\n", error_code);
     ```

   - Set the description.

     To set the description for the event, use the `calendar_record_set_str()` function with the `_calendar_event.description` property as the second parameter:

     ```
     error_code = calendar_record_set_str(event, _calendar_event.description, "description");
     if (error_code != CALENDAR_ERROR_NONE)
         dlog_print(DLOG_ERROR, LOG_TAG, "set description failed: %x\n", error_code);
     ```

   - Set the time zone for the start and end times.

     To set the time zone for the event start and end times, use the `calendar_record_set_str()` function with the `_calendar_event.start_tzid` and `_calendar_event.end_tzid` properties as the second parameter. If you do not set the time zone, the system uses UTC.

     ```
     error_code = calendar_record_set_str(event, _calendar_event.start_tzid, "Asia/Seoul");
     if (error_code != CALENDAR_ERROR_NONE)
         dlog_print(DLOG_ERROR, LOG_TAG, "set start_tzid failed: %x\n", error_code);

     error_code = calendar_record_set_str(event, _calendar_event.end_tzid, "Asia/Seoul");
     if (error_code != CALENDAR_ERROR_NONE)
         dlog_print(DLOG_ERROR, LOG_TAG, "set end_tzid failed: %x\n", error_code);
     ```

   - Set the start and end times.

     To set the start and end times for the event, use the `calendar_record_set_caltime()` function with the `_calendar_event.start_time` and `_calendar_event.end_time` properties as the second parameter:

     ```
     calendar_time_s starttime = {0};
     starttime.type = CALENDAR_TIME_UTIME;
     starttime.time.utime = 1404036000; /* 2014/06/29 10:00:00 UTC */
     error_code = calendar_record_set_caltime(event, _calendar_event.start_time, starttime);
     if (error_code != CALENDAR_ERROR_NONE)
         dlog_print(DLOG_ERROR, LOG_TAG, "set start_time failed: %x\n", error_code);

     calendar_time_s endtime = {0};
     endtime.type = CALENDAR_TIME_UTIME;
     endtime.time.utime = 1404036000 + 3600; /* 2014/06/29 11:00:00 UTC */
     error_code = calendar_record_set_caltime(event, _calendar_event.end_time, endtime);
     if (error_code != CALENDAR_ERROR_NONE)
         dlog_print(DLOG_ERROR, LOG_TAG, "set end_time failed: %x\n", error_code);
     ```

     The `calendar_time_s` structure (in [mobile](../../api/mobile/latest/structcalendar__time__s.html) and [wearable](../../api/wearable/latest/structcalendar__time__s.html) applications) has [2 types](#time).

   - To create a recurring event:

     1. Set the frequency (in [mobile](../../api/mobile/latest/group__CAPI__SOCIAL__CALENDAR__SVC__MODULE.html#CAPI_SOCIAL_CALENDAR_SVC_MODULE_Creating_a_recurring_event) and [wearable](../../api/wearable/latest/group__CAPI__SOCIAL__CALENDAR__SVC__MODULE.html#CAPI_SOCIAL_CALENDAR_SVC_MODULE_Creating_a_recurring_event) applications).

        In the following example, the event is set to occur every month on the 3rd, 4th, and 5th day:

        ```
        error_code = calendar_record_set_int(event, _calendar_event.freq,
                                             CALENDAR_RECURRENCE_MONTHLY);
        if (error_code != CALENDAR_ERROR_NONE)
            dlog_print(DLOG_ERROR, LOG_TAG, "set freq failed: %x\n", error_code);

        error_code = calendar_record_set_int(event, _calendar_event.interval, 1);
        if (error_code != CALENDAR_ERROR_NONE)
            dlog_print(DLOG_ERROR, LOG_TAG, "set interval failed: %x\n", error_code);

        error_code = calendar_record_set_str(event, _calendar_event.bymonthday, "3,4,5");
        if (error_code != CALENDAR_ERROR_NONE)
            dlog_print(DLOG_ERROR, LOG_TAG, "set bymonthday failed: %x\n", error_code);
        ```

     2. Set the range of recurrence (in [mobile](../../api/mobile/latest/group__CAPI__SOCIAL__CALENDAR__SVC__MODULE.html#CAPI_SOCIAL_CALENDAR_SVC_MODULE_Creating_a_recurring_event) and [wearable](../../api/wearable/latest/group__CAPI__SOCIAL__CALENDAR__SVC__MODULE.html#CAPI_SOCIAL_CALENDAR_SVC_MODULE_Creating_a_recurring_event) applications).

        In the following example, the event is set to occur a total of 8 times:

        ```
        error_code = calendar_record_set_int(event, _calendar_event.range_type,
                                             CALENDAR_RANGE_COUNT);
        if (error_code != CALENDAR_ERROR_NONE)
            dlog_print(DLOG_ERROR, LOG_TAG, "set range_type failed: %x\n", error_code);

        error_code = calendar_record_set_int(event, _calendar_event.count, 8);
        if (error_code != CALENDAR_ERROR_NONE)
            dlog_print(DLOG_ERROR, LOG_TAG, "set count failed: %x\n", error_code);
        ```

     Based on the recurrence settings above and the start time (set in the previous step) of June 29, this event occurs 8 times: on Jul 3, 4, and 5, on Aug 3, 4, and 5, and on Sep 3 and 4.

   - Add an alarm.

     To add an alarm, create a handle to an alarm record, set the alarm properties, and insert the alarm as a child record to the event.

     In the following example, the alarm is defined to activate 60 seconds before the event start time:

     ```
     calendar_record_h alarm = NULL;
     calendar_time_s ct;
     error_code = CALENDAR_ERROR_NONE;

     /* Create the alarm record */
     error_code += calendar_record_create(_calendar_alarm._uri, &alarm);

     /* Set the properties */
     error_code += calendar_record_set_int(alarm, _calendar_alarm.tick_unit,
                                           CALENDAR_ALARM_TIME_UNIT_SPECIFIC);
     ct.type = CALENDAR_TIME_UTIME;
     ct.time.utime = 1404036000 - 60; /* 60 sec before starttime (1404036000) */
     error_code += calendar_record_set_caltime(alarm, _calendar_alarm.alarm_time, ct);

     /* Add to the event as a child record */
     error_code += calendar_record_add_child_record(event,
                                                    _calendar_event.calendar_alarm,
                                                    alarm);

     if (error_code != CALENDAR_ERROR_NONE)
         dlog_print(DLOG_ERROR, LOG_TAG, "adding the alarm failed \n");
     ```

     The `calendar_alarm_time_unit_type_e` enumeration (in [mobile](../../api/mobile/latest/group__CAPI__SOCIAL__CALENDAR__SVC__RECORD__MODULE.html#ga631b1b606158479e3a14a921b006b4fe) and [wearable](../../api/wearable/latest/group__CAPI__SOCIAL__CALENDAR__SVC__RECORD__MODULE.html#ga631b1b606158479e3a14a921b006b4fe) applications) defines the available alarm tick units.

     > **Note**  
     > If you use `CALENDAR_ALARM_TIME_UNIT_SPECIFIC` as a tick unit, specify the alarm time in Unix time.

   - Add an attendee.

     To add an attendee, create a handle to an attendee record, set the attendee properties, and insert the attendee as a child record to the event.

     In the following example, 1 attendee named John is added:

     ```
     calendar_record_h attendee = NULL;
     error_code = CALENDAR_ERROR_NONE;

     /* Create the attendee record */
     error_code += calendar_record_create(_calendar_attendee._uri, &attendee);

     /* Set the attendee properties */
     error_code += calendar_record_set_str(attendee, _calendar_attendee.name, "John");

     /* Add to the event as a child record */
     error_code += calendar_record_add_child_record(event,
                                                    _calendar_event.calendar_attendee,
                                                    attendee);

     if (error_code != CALENDAR_ERROR_NONE)
         dlog_print(DLOG_ERROR, LOG_TAG, "adding the attendee failed \n");
     ```

   Set other event properties similarly, as needed.

3. Insert the event into the calendar database using the `calendar_db_insert_record()` function. All child records added to the event using the `calendar_record_add_child_record()` function are inserted automatically along with the parent.

   The system assigns a unique ID to the event, and the function returns it as its second parameter.

   ```
   int id = -1;
   error_code = calendar_db_insert_record(event, &id);
   if (error_code != CALENDAR_ERROR_NONE)
       dlog_print(DLOG_ERROR, LOG_TAG, "calendar_db_insert_record failed: %x\n", error_code);

   dlog_print(DLOG_ERROR, LOG_TAG, "id: %d\n", id);
   ```

4. When no longer needed, destroy the event handle and release all its resources using the `calendar_record_destroy()` function:

   ```
   calendar_record_destroy(event, true);
   ```

   If you set the second parameter to `true`, all child records of the given record are also destroyed, irrespective of how the child records were added (individually or along with their parent record).

<a name="get_event"></a>
## Retrieving Events

To retrieve a single event:

1. Retrieve an event record using the `calendar_db_get_record()` function with the event ID as the second parameter:

   ```
   calendar_record_h record;
   const int event_id = ...; /* Get the event ID */
   error_code = calendar_db_get_record(_calendar_event._uri, event_id, &record);
   if (error_code != CALENDAR_ERROR_NONE)
       dlog_print(DLOG_ERROR, LOG_TAG, "calendar_db_get_record failed: %x\n", error_code);
   ```

2. When no longer needed, destroy the event handle and release all its resources using the `calendar_record_destroy()` function:

   ```
   calendar_record_destroy(record, true);
   ```

To retrieve multiple events:

1. Retrieve a list of all events, or retrieve a filtered list of events:

   - To retrieve a list of all events, use the `calendar_db_get_all_records()` function:

     ```
     calendar_list_h list = NULL;
     error_code = calendar_db_get_all_records(_calendar_event._uri, 0, 0, &list);
     if (error_code != CALENDAR_ERROR_NONE)
         dlog_print(DLOG_ERROR, LOG_TAG, "calendar_db_get_all_records failed: %x\n", error_code);
     ```

   - To retrieve a filtered list of events:

     1. Define a list handle variable, and create a query handle using the `calendar_query_create()` function:

        ```
        calendar_list_h list = NULL;
        calendar_query_h query = NULL;

        error_code = calendar_query_create(_calendar_event._uri, &query);
        if (error_code != CALENDAR_ERROR_NONE)
            dlog_print(DLOG_ERROR, LOG_TAG, "calendar_query_create failed: %x\n", error_code);
        ```

     2. Create a filter handle using the `calendar_filter_create()` function:

        ```
        calendar_filter_h filter = NULL;

        error_code = calendar_filter_create(_calendar_event._uri, &filter);
        if (error_code != CALENDAR_ERROR_NONE)
            dlog_print(DLOG_ERROR, LOG_TAG, "calendar_filter_create failed: %x\n", error_code);
        ```

     3. Add a filtering condition using the `calendar_filter_add_XXX()` function.

        The following example adds a string-based filtering condition that retrieves the events whose summary field contains the string "summary to find":

        ```
        error_code = calendar_filter_add_str(filter, _calendar_event.summary,
                                             CALENDAR_MATCH_CONTAINS, "summary to find");
        if (error_code != CALENDAR_ERROR_NONE)
            dlog_print(DLOG_ERROR, LOG_TAG, "filter add condition failed: %x\n", error_code);
        ```

     4. To add more conditions, define an operator between the conditions.

        The following example first adds an AND operator and then a string-based filtering condition that retrieves the events whose description field contains the string "description to find".

        The combination of the AND operator and the 2 conditions means that the filter only retrieves the events that contain "summary to find" in their summary and "description to find" in their description.

        ```
        error_code = calendar_filter_add_operator(filter, CALENDAR_FILTER_OPERATOR_AND);
        if (error_code != CALENDAR_ERROR_NONE)
            dlog_print(DLOG_ERROR, LOG_TAG, "calendar_filter_add_operator failed: %x\n", error_code);

        error_code = calendar_filter_add_str(filter, _calendar_event.description,
                                             CALENDAR_MATCH_CONTAINS, "description to find");
        if (error_code != CALENDAR_ERROR_NONE)
            dlog_print(DLOG_ERROR, LOG_TAG, "filter add condition failed: %x\n", error_code);
        ```

        You can also create a filter with integer and time conditions. For example, to filter all-day events that start after January 1st, 2016:

        ```
        calendar_time_s time_to_compare = {0};
        time_to_compare.type = CALENDAR_TIME_LOCALTIME;
        time_to_compare.time.date.mday = 1;
        time_to_compare.time.date.month = 1;
        time_to_compare.time.date.year = 2016;
        error_code = calendar_filter_add_caltime(filter, _calendar_event.start_time,
                                                 CALENDAR_MATCH_GREATER_THAN, time_to_compare);
        if (error_code != CALENDAR_ERROR_NONE)
            dlog_print(DLOG_ERROR, LOG_TAG, "filter add condition failed: %x\n", error_code);
        ```

        The `type` parameter of the `calendar_time_s` structure (in [mobile](../../api/mobile/latest/structcalendar__time__s.html) and [wearable](../../api/wearable/latest/structcalendar__time__s.html) applications) determines whether the event is an all-day event (`CALENDAR_TIME_LOCALTIME`) or a non-all-day event (`CALENDAR_TIME_UTIME`).

        To retrieve the specified time period, use 2 conditions using `CALENDAR_MATCH_GREATER_THAN` and `CALENDAR_MATCH_LESS_THAN` with the operator `CALENDAR_FILTER_OPERATOR_AND`. You can also use `CALENDAR_MATCH_EQUAL` to set an equality condition.

     5. Set the filter to the query using the `calendar_query_set_filter()` function:

        ```
        error_code = calendar_query_set_filter(query, filter);
        if (error_code != CALENDAR_ERROR_NONE)
            dlog_print(DLOG_ERROR, LOG_TAG, "calendar_query_set_filter failed: %x\n", error_code);
        ```

     6. Retrieve the filtered list of events using the `calendar_db_get_records_with_query()` function:

        ```
        error_code = calendar_db_get_records_with_query(query, 0, 0, &list);
        if (error_code != CALENDAR_ERROR_NONE)
            dlog_print(DLOG_ERROR, LOG_TAG, "calendar_db_get_records_with_query failed: %x\n", error_code);
        ```

        The third parameter defines a limit for the number of results. If you set it to 0, the list returns all events matching the query.

     7. When no longer needed, destroy the filter and query handles and release all their resources using the `calendar_filter_destroy()` and `calendar_query_destroy()` functions:

        ```
        calendar_filter_destroy(filter);
        calendar_query_destroy(query);
        ```

2. Iterate through the list of found events, and retrieve event details:

   1. Use a loop to iterate through the list and retrieve the event details.

      Move forward and backward within the event list using the `calendar_list_next()` and `calendar_list_prev()` functions, and retrieve the current event using the `calendar_list_get_current_record_p()` function.

      > **Note**  
      > Some functions have the `_p` postfix. The postfix means that the returned value must not be freed by the application, as it is a pointer to the data in an existing record.

      The following example iterates through the list and retrieves the summary of each event:

      ```
      calendar_record_h record;
      while (calendar_list_get_current_record_p(list, &record) == CALENDAR_ERROR_NONE) {
          char* summary;
          calendar_record_get_str_p(record, _calendar_event.summary, &summary);
          dlog_print(DLOG_ERROR, LOG_TAG, "summary: %s\n", summary);

          error_code = calendar_list_next(list);
          if (error_code != CALENDAR_ERROR_NONE)
              break;
      }
      ```

   2. Optionally, retrieve more details of each event using the `calendar_gl_event_data_t` structure:

      ```
      calendar_gl_event_data_t *gl_event_data = NULL;
      calendar_record_h record = NULL;
      while (calendar_list_get_current_record_p(list, &record) == CALENDAR_ERROR_NONE) {
          gl_event_data = _create_gl_event_data(record);
          /* You can get, for example, summary: */
          /* gl_event_data->summary */

          _free_gl_event_data(gl_event_data);

          error_code = calendar_list_next(list);
          if (error_code != CALENDAR_ERROR_NONE)
              break;
      }
      ```

      Define the `calendar_gl_event_data_t` structure and the functions for using the structure:

      ```
      struct _calendar_gl_event_data {
          int id;
          char *summary;
          char *description;
          calendar_time_s start_time;
      };
      typedef struct _calendar_gl_event_data calendar_gl_event_data_t;

      /* Release the resources allocated to the structure */
      static void
      _free_gl_event_data(calendar_gl_event_data_t *gl_event_data)
      {
          if (NULL == gl_event_data)
              return;

          free(gl_event_data->summary);
          free(gl_event_data->description);
          free(gl_event_data);
      }

      /* Create the structure for an event */
      static calendar_gl_event_data_t*
      _create_gl_event_data(calendar_record_h record)
      {
          calendar_gl_event_data_t *gl_event_data;
          int error_code;

          gl_event_data = malloc(sizeof(calendar_gl_event_data_t));
          memset(gl_event_data, 0x0, sizeof(calendar_gl_event_data_t));

          error_code = calendar_record_get_str(record, _calendar_event.summary,
                                               &gl_event_data->summary);
          if (error_code != CALENDAR_ERROR_NONE) {
              dlog_print(DLOG_ERROR, LOG_TAG, "get summary failed: %i\n", error_code);
              _free_gl_event_data(gl_event_data);

              return NULL;
          }

          error_code = calendar_record_get_str(record, _calendar_event.description,
                                               &gl_event_data->description);
          if (error_code != CALENDAR_ERROR_NONE) {
              dlog_print(DLOG_ERROR, LOG_TAG, "get description failed: %i\n", error_code);
              _free_gl_event_data(gl_event_data);

              return NULL;
          }

          error_code = calendar_record_get_int(record, _calendar_event.id, &gl_event_data->id);
          if (error_code != CALENDAR_ERROR_NONE) {
              dlog_print(DLOG_ERROR, LOG_TAG, "get id failed: %i\n", error_code);
              _free_gl_event_data(gl_event_data);

              return NULL;
          }

          error_code = calendar_record_get_caltime(record, _calendar_event.start_time,
                                                   &gl_event_data->start_time);
          if (error_code != CALENDAR_ERROR_NONE) {
              dlog_print(DLOG_ERROR, LOG_TAG, "get start_time failed: %i\n", error_code);
              _free_gl_event_data(gl_event_data);

              return NULL;
          }

          return gl_event_data;
      }
      ```

      To access a specific event detail in a child record, retrieve the child record.

3. When no longer needed, destroy the list handle and release all its resources using the `calendar_list_destroy()` function:

   ```
   calendar_list_destroy(list, true);
   ```

<a name="update_event"></a>
## Updating an Event

To update event details:

1. Retrieve the event you want to update using the `calendar_db_get_record()` function with the event ID as the second parameter:

   ```
   calendar_record_h record;
   const int event_id = ...; /* Get the event ID */
   error_code = calendar_db_get_record(_calendar_event._uri, event_id, &record);
   if (error_code != CALENDAR_ERROR_NONE)
       dlog_print(DLOG_ERROR, LOG_TAG, "calendar_db_get_record failed: %x\n", error_code);
   ```

   You can also retrieve the event using a search function, such as `calendar_db_get_records_with_query()`.

2. Set the properties you want to update.

   The following example sets a new subject and description for the event:

   ```
   error_code = calendar_record_set_str(record, _calendar_event.summary, "summary updated");
   if (error_code != CALENDAR_ERROR_NONE)
       dlog_print(DLOG_ERROR, LOG_TAG, "set summary failed: %x\n", error_code);

   error_code = calendar_record_set_str(record, _calendar_event.description, "description updated");
   if (error_code != CALENDAR_ERROR_NONE)
       dlog_print(DLOG_ERROR, LOG_TAG, "set description failed: %x\n", error_code);
   ```

3. Update the event using the `calendar_db_update_record()` function:

   ```
   error_code = calendar_db_update_record(record);
   if (error_code != CALENDAR_ERROR_NONE)
       dlog_print(DLOG_ERROR, LOG_TAG, "calendar_db_update_record failed: %x\n", error_code);
   ```

4. When no longer needed, destroy the event handle and release all its resources using the `calendar_record_destroy()` function:

   ```
   calendar_record_destroy(record, true);
   ```

<a name="delete_event"></a>
## Deleting an Event

To delete an event, use the `calendar_db_delete_record()` function with the event ID as the second parameter:

```
int event_id = ...; /* Get the event ID */
error_code = calendar_db_delete_record(_calendar_event._uri, event_id);
if (error_code != CALENDAR_ERROR_NONE)
    dlog_print(DLOG_ERROR, LOG_TAG, "calendar_db_delete_record failed: %x\n", error_code);
```

<a name="exception_add"></a>
## Removing an Instance from a Recurring Event

To remove an event instance from a recurring event:

1. Create a recurring event.

   The following example creates an event with the following properties:

   - Frequency: `CALENDAR_RECURRENCE_MONTHLY`
   - Interval: 1
   - Days of the month: "3, 4, 5"
   - Range type: `CALENDAR_RANGE_COUNT`
   - Count: 8

   ```
   int error_code = CALENDAR_ERROR_NONE;

   calendar_record_h event = NULL;
   error_code += calendar_record_create(_calendar_event._uri, &event);
   error_code += calendar_record_set_str(event, _calendar_event.summary, "test");
   error_code += calendar_record_set_str(event, _calendar_event.start_tzid, "Asia/Seoul");
   error_code += calendar_record_set_str(event, _calendar_event.end_tzid, "Asia/Seoul");

   calendar_time_s st = {0};
   st.type = CALENDAR_TIME_UTIME;
   st.time.utime = 1349226000;
   error_code += calendar_record_set_caltime(event, _calendar_event.start_time, st);

   calendar_time_s et = {0};
   et.type = CALENDAR_TIME_UTIME;
   et.time.utime = 1354582800;
   error_code += calendar_record_set_caltime(event, _calendar_event.end_time, et);

   error_code += calendar_record_set_int(event, _calendar_event.freq, CALENDAR_RECURRENCE_MONTHLY);
   error_code += calendar_record_set_int(event, _calendar_event.interval, 1);
   error_code += calendar_record_set_str(event, _calendar_event.bymonthday, "3,4,5");

   error_code += calendar_record_set_int(event, _calendar_event.range_type, CALENDAR_RANGE_COUNT);
   error_code += calendar_record_set_int(event, _calendar_event.count, 8);

   if (error_code != CALENDAR_ERROR_NONE)
       dlog_print(DLOG_ERROR, LOG_TAG, "creating the event failed: \n");
   ```

   The event has 8 instances:

   **Table: Event instances**

   | unixtime                                 | Date time                                |
   |------------------------------------------|------------------------------------------|
   | 1349226000<br> 1349312400<br> 1349398800<br> 1351904400<br> 1351990800<br> 1352077200<br> 1354496400<br> 1354582800 | 2012-10-03 01:00:00<br> 2012-10-04 01:00:00<br> 2012-10-05 01:00:00<br> 2012-11-03 01:00:00<br> 2012-11-04 01:00:00<br> 2012-11-05 01:00:00<br> 2012-12-03 01:00:00<br> 2012-12-04 01:00:00 |

2. Create the exception by setting the `exdate` property.

   In vCalendar 2.0 (RFC 2445), the `exdate` property is used to identify a deleted instance. If multiple instances are deleted, datetimes are added with a comma (for example, `20121104T010000Z, 20121105T010000Z, 20121203T010000Z`).

   ```
   error_code = calendar_record_set_str(event, _calendar_event.exdate, "20121104T010000Z");
   if (error_code != CALENDAR_ERROR_NONE)
       dlog_print(DLOG_ERROR, LOG_TAG, "set exdate failed: %x\n", error_code);
   ```

3. Insert the event into the calendar database using the `calendar_db_insert_record()` function:

   ```
   int event_id;
   error_code = calendar_db_insert_record(event, &event_id);
   if (error_code != CALENDAR_ERROR_NONE)
       dlog_print(DLOG_ERROR, LOG_TAG, "calendar_db_insert_record failed: %x\n", error_code);

   calendar_record_destroy(event, true);
   ```

<a name="exception_modify"></a>
## Adding an Exception to a Recurring Event

To add an exception to a recurring event:

1. Make sure you have an existing recurring event.

2. Clone the existing event.

   Cloning means that the new event initially has the same properties as the original event. In vCalendar 2.0 (RFC 2445), the recurrence ID is used to identify the modified instance (exception).

   ```
   calendar_record_h clone = NULL;
   error_code = CALENDAR_ERROR_NONE;

   error_code += calendar_record_clone(event, &clone);
   error_code += calendar_record_set_int(clone, _calendar_event.original_event_id, event_id);
   error_code += calendar_record_set_str(clone, _calendar_event.recurrence_id, "20121005T010000Z");

   if (error_code != CALENDAR_ERROR_NONE)
       dlog_print(DLOG_ERROR, LOG_TAG, "cloning the event failed: %x\n", error_code);
   ```

3. Modify or add event properties to create the exception.

4. Insert the exception into the calendar database using the `calendar_db_insert_record()` function:

   ```
   int exdate_event_id = 0;
   error_code = calendar_db_insert_record(clone, &exdate_event_id);
   if (error_code != CALENDAR_ERROR_NONE)
       dlog_print(DLOG_ERROR, LOG_TAG, "calendar_db_insert_record failed: %x\n", error_code);

   calendar_record_destroy(clone, true);
   calendar_record_destroy(event, true);
   ```

<a name="monitor_event"></a>
## Monitoring Event Changes

To receive a notification whenever an event changes:

1. Register a callback using the `calendar_db_add_changed_cb()` function:

   ```
   error_code = calendar_db_add_changed_cb(_calendar_event._uri, _event_changed_callback, NULL);
   if (error_code != CALENDAR_ERROR_NONE)
       dlog_print(DLOG_ERROR, LOG_TAG, "calendar_db_add_changed_cb failed: %x\n", error_code);
   ```

2. Define the event change callback.

   The following example shows how to retrieve the new event details in the callback:

   ```
   static calendar_gl_event_data_t *_gl_event_data = ...;

   static void
   _event_changed_callback(const char *view_uri, void *user_data)
   {
       if (0 != strcmp(view_uri, _calendar_event._uri))
           return;

       if (NULL == _gl_event_data)
           return;

       int event_id = _gl_event_data->id;
       _free_gl_event_data(_gl_event_data);
       _gl_event_data = NULL;

       calendar_record_h record = NULL;
       int error_code;
       error_code = calendar_db_get_record(_calendar_event._uri, event_id, &record);
       if (error_code != CALENDAR_ERROR_NONE)
           return;

       _gl_event_data = _create_gl_event_data(record);
       /* Use _gl_event_data */

       calendar_record_destroy(record, true);
   }
   ```

<a name="create"></a>
## Creating a Todo

Creating a new todo involves creating a todo handle, setting the todo properties, and inserting the todo into the calendar database.

Some todo properties are defined as child records that are associated with the parent record. For a detailed list of the todo properties, see the `_calendar_todo` view description in the Calendar API (in [mobile](../../api/mobile/latest/group__CAPI__SOCIAL__CALENDAR__SVC__VIEW__MODULE.html#CAPI_SOCIAL_CALENDAR_SVC_VIEW_MODULE_calendar_todo) and [wearable](../../api/wearable/latest/group__CAPI__SOCIAL__CALENDAR__SVC__VIEW__MODULE.html#CAPI_SOCIAL_CALENDAR_SVC_VIEW_MODULE_calendar_todo) applications). If the property type is `child list`, the property is defined as a child record.

To create a new todo:

1. Create a todo handle using the `calendar_record_create()` function with the `_calendar_todo._uri` property as the first parameter and the todo handle variable as the second parameter:

   ```
   calendar_record_h todo = NULL;
   error_code = calendar_record_create(_calendar_todo._uri, &todo);
   if (error_code != CALENDAR_ERROR_NONE)
       dlog_print(DLOG_ERROR, LOG_TAG, "calendar_record_create failed: %x\n", error_code);
   ```

   > **Note**  
   > Records created with the `calendar_record_create()` function are memory objects, with `calendar_record_h` type variables as their handles. If you changes these objects, the changes are not reflected in the calendar database until you explicitly insert or update the objects to the database using the `calendar_db_insert_record()` or `calendar_db_update_record()` function.

2. Set the todo properties:

   - Set the subject.

     To set the subject for the todo, use the `calendar_record_set_str()` function with the `_calendar_todo.summary` property as the second parameter:

     ```
     error_code = calendar_record_set_str(todo, _calendar_todo.summary, "summary");
     if (error_code != CALENDAR_ERROR_NONE)
         dlog_print(DLOG_ERROR, LOG_TAG, "set summary failed: %x\n", error_code);
     ```

   - Set the description.

     To set the description for the todo, use the `calendar_record_set_str()` function with the `_calendar_todo.description` property as the second parameter:

     ```
     error_code = calendar_record_set_str(todo, _calendar_todo.description, "description");
     if (error_code != CALENDAR_ERROR_NONE)
         dlog_print(DLOG_ERROR, LOG_TAG, "set description failed: %x\n", error_code);
     ```

   - Set the due time.

     To set the due time for the todo, use the `calendar_record_set_caltime()` function with the `_calendar_todo.due_time` property as the second parameter:

     ```
     calendar_time_s duetime = {0};
     duetime.type = CALENDAR_TIME_UTIME;
     duetime.time.utime = 1404036000; /* 2014/06/29 11:00:00 UTC */

     error_code = calendar_record_set_caltime(todo, _calendar_todo.due_time, duetime);
     if (error_code != CALENDAR_ERROR_NONE)
         dlog_print(DLOG_ERROR, LOG_TAG, "set due_time failed: %x\n", error_code);
     ```

   - Set the status.

     To set the status for the todo, use the `calendar_record_set_int()` function with the `_calendar_todo.todo_status` property as the second parameter. The `calendar_todo_status_e` enumeration (in [mobile](../../api/mobile/latest/group__CAPI__SOCIAL__CALENDAR__SVC__RECORD__MODULE.html#ga3e1b9cae05705d471a4746d8ab6d3622) and [wearable](../../api/wearable/latest/group__CAPI__SOCIAL__CALENDAR__SVC__RECORD__MODULE.html#ga3e1b9cae05705d471a4746d8ab6d3622) applications) defines the possible status values.

     ```
     error_code = calendar_record_set_int(todo, _calendar_todo.todo_status,
                                          CALENDAR_TODO_STATUS_COMPLETED);
     if (error_code != CALENDAR_ERROR_NONE)
         dlog_print(DLOG_ERROR, LOG_TAG, "set todo_status failed: %x\n", error_code);
     ```

   Set other todo properties similarly, as needed.

3. Insert the todo into the calendar database using the `calendar_db_insert_record()` function. All child records added to the todo using the `calendar_record_add_child_record()` function are inserted automatically along with the parent.

   The system assigns a unique ID to the todo, and the function returns it as its second parameter.

   ```
   int id;
   error_code = calendar_db_insert_record(todo, &id);
   if (error_code != CALENDAR_ERROR_NONE)
       dlog_print(DLOG_ERROR, LOG_TAG, "calendar_db_insert_record failed: %x\n", error_code);
   ```

4. When no longer needed, destroy the todo handle and release all its resources using the `calendar_record_destroy()` function:

   ```
   calendar_record_destroy(todo, true);
   ```

   If you set the second parameter to `true`, all child records of the given record are also destroyed, irrespective of how the child records were added (individually or along with their parent record).

<a name="get"></a>
## Retrieving Todos

To retrieve a single todo:

1. Retrieve an todo record using the `calendar_db_get_record()` function with the todo ID as the second parameter:

   ```
   calendar_record_h record;
   const int todo_id = ...; /* Get the todo ID */
   error_code = calendar_db_get_record(_calendar_todo._uri, todo_id, &record);
   if (error_code != CALENDAR_ERROR_NONE)
       dlog_print(DLOG_ERROR, LOG_TAG, "calendar_db_get_record failed: %x\n", error_code);
   ```

2. When no longer needed, destroy the todo handle and release all its resources using the `calendar_record_destroy()` function:

   ```
   calendar_record_destroy(record, true);
   ```

To retrieve multiple todos:

1. Retrieve a list of all todos, or retrieve a filtered list of todos:

   - To retrieve a list of all todos, use the `calendar_db_get_all_records()` function:

     ```
     calendar_list_h list = NULL;
     error_code = calendar_db_get_all_records(_calendar_todo._uri, 0, 0, &list);
     if (error_code != CALENDAR_ERROR_NONE)
         dlog_print(DLOG_ERROR, LOG_TAG, "calendar_db_get_all_records failed: %x\n", error_code);
     ```

   - To retrieve a filtered list of todos:

     1. Define a list handle variable, and create a query handle using the `calendar_query_create()` function:

        ```
        calendar_list_h list = NULL;
        calendar_query_h query = NULL;

        error_code = calendar_query_create(_calendar_todo._uri, &query);
        if (error_code != CALENDAR_ERROR_NONE)
            dlog_print(DLOG_ERROR, LOG_TAG, "calendar_query_create failed: %x\n", error_code);
        ```

     2. Create a filter handle using the `calendar_filter_create()` function:

        ```
        calendar_filter_h filter = NULL;

        error_code = calendar_filter_create(_calendar_todo._uri, &filter);
        if (error_code != CALENDAR_ERROR_NONE)
            dlog_print(DLOG_ERROR, LOG_TAG, "calendar_filter_create failed: %x\n", error_code);
        ```

     3. Add a filtering condition using the `calendar_filter_add_XXX()` function.

        The following example adds a string-based filtering condition that retrieves the todos whose summary field contains the string "summary to find":

        ```
        error_code = calendar_filter_add_str(filter, _calendar_todo.summary,
                                             CALENDAR_MATCH_CONTAINS, "summary to find");
        if (error_code != CALENDAR_ERROR_NONE)
            dlog_print(DLOG_ERROR, LOG_TAG, "filter add condition failed: %x\n", error_code);
        ```

     4. To add more conditions, define an operator between the conditions.

        The following example first adds an AND operator and then a string-based filtering condition that retrieves the todos whose description field contains the string "description to find".

        The combination of the AND operator and the 2 conditions means that the filter only retrieves the todos that contain "summary to find" in their summary and "description to find" in their description.

        ```
        error_code = calendar_filter_add_operator(filter, CALENDAR_FILTER_OPERATOR_AND);
        if (error_code != CALENDAR_ERROR_NONE)
            dlog_print(DLOG_ERROR, LOG_TAG, "calendar_filter_add_operator failed: %x\n", error_code);

        error_code = calendar_filter_add_str(filter, _calendar_todo.description,
                                             CALENDAR_MATCH_CONTAINS, "description to find");
        if (error_code != CALENDAR_ERROR_NONE)
            dlog_print(DLOG_ERROR, LOG_TAG, "filter add condition failed: %x\n", error_code);
        ```

        You can also create a filter with integer and time conditions. For example, to filter all completed todos:

        ```
        error_code = calendar_filter_add_int(filter, _calendar_todo.todo_status,
                                             CALENDAR_MATCH_EQUAL, CALENDAR_TODO_STATUS_COMPLETED);
        if (error_code != CALENDAR_ERROR_NONE)
            dlog_print(DLOG_ERROR, LOG_TAG, "filter add condition failed: %x\n", error_code);
        ```

     5. Set the filter to the query using the `calendar_query_set_filter()` function:

        ```
        error_code = calendar_query_set_filter(query, filter);
        if (error_code != CALENDAR_ERROR_NONE)
            dlog_print(DLOG_ERROR, LOG_TAG, "calendar_query_set_filter failed: %x\n", error_code);
        ```

     6. Retrieve the filtered list of todos using the `calendar_db_get_records_with_query()` function:

        ```
        error_code = calendar_db_get_records_with_query(query, 0, 0, &list);
        if (error_code != CALENDAR_ERROR_NONE)
            dlog_print(DLOG_ERROR, LOG_TAG, "calendar_db_get_records_with_query failed: %x\n", error_code);
        ```

        The third parameter defines a limit for the number of results. If you set it to 0, the list returns all todos matching the query.

     7. When no longer needed, destroy the filter and query handles and release all their resources using the `calendar_filter_destroy()` and `calendar_query_destroy()` functions:

        ```
        calendar_filter_destroy(filter);
        calendar_query_destroy(query);
        ```

2. Iterate through the list of found todos, and retrieve todo details:

   1. Use a loop to iterate through the list and retrieve the todo details.

      Move forward and backward within the todo list using the `calendar_list_next()` and `calendar_list_prev()` functions, and retrieve the current todo using the `calendar_list_get_current_record_p()` function.

      > **Note**  
	  > Some functions have the `_p` postfix. The postfix means that the returned value must not be freed by the application, as it is a pointer to the data in an existing record.

      The following example iterates through the list and retrieves the summary of each todo:

      ```
      calendar_record_h record;
      while (calendar_list_get_current_record_p(list, &record) == CALENDAR_ERROR_NONE) {
          char* summary;
          calendar_record_get_str_p(record, _calendar_todo.summary, &summary);
          dlog_print(DLOG_ERROR, LOG_TAG, "summary: %s\n", summary);

          error_code = calendar_list_next(list);
          if (error_code != CALENDAR_ERROR_NONE)
              break;
      }
      ```

   2. Optionally, retrieve more details of each todo using the `calendar_gl_todo_data_t` structure:

      ```
      calendar_gl_todo_data_t *gl_todo_data = NULL;
      calendar_record_h record = NULL;
      while (calendar_list_get_current_record_p(list, &record) == CALENDAR_ERROR_NONE) {
          gl_todo_data = _create_gl_todo_data(record);
          /* You can get, for example, summary: */
          /* gl_todo_data->summary */

          _free_gl_todo_data(gl_todo_data);

          error_code = calendar_list_next(list);
          if (error_code != CALENDAR_ERROR_NONE)
              break;
      }
      ```

      Define the `calendar_gl_todo_data_t` structure and the functions for using the structure:

      ```
      struct _calendar_gl_todo_data {
          int id;
          char *summary;
          char *description;
          calendar_time_s due_time;
      };
      typedef struct _calendar_gl_todo_data calendar_gl_todo_data_t;

      /* Release the resources allocated to the structure */
      static void
      _free_gl_todo_data(calendar_gl_todo_data_t *gl_todo_data)
      {
          if (NULL == gl_todo_data)
              return;

          free(gl_todo_data->summary);
          free(gl_todo_data->description);
          free(gl_todo_data);
      }

      /* Create the structure for a todo */
      static calendar_gl_todo_data_t*
      _create_gl_todo_data(calendar_record_h record)
      {
          calendar_gl_todo_data_t *gl_todo_data;
          int error_code;

          gl_todo_data = malloc(sizeof(calendar_gl_todo_data_t));
          memset(gl_todo_data, 0x0, sizeof(calendar_gl_todo_data_t));

          error_code = calendar_record_get_str(record, _calendar_todo.summary,
                                               &gl_todo_data->summary);
          if (error_code != CALENDAR_ERROR_NONE) {
              dlog_print(DLOG_ERROR, LOG_TAG, "get summary failed: %x\n", error_code);
              _free_gl_todo_data(gl_todo_data);

              return NULL;
          }

          error_code = calendar_record_get_str(record, _calendar_todo.description,
                                               &gl_todo_data->description);
          if (error_code != CALENDAR_ERROR_NONE) {
              dlog_print(DLOG_ERROR, LOG_TAG, "get description failed: %x\n", error_code);
              _free_gl_todo_data(gl_todo_data);

              return NULL;
          }

          error_code = calendar_record_get_int(record, _calendar_todo.id, &gl_todo_data->id);
          if (error_code != CALENDAR_ERROR_NONE) {
              dlog_print(DLOG_ERROR, LOG_TAG, "get id failed: %x\n", error_code);
              _free_gl_todo_data(gl_todo_data);

              return NULL;
          }

          error_code = calendar_record_get_caltime(record, _calendar_todo.due_time,
                                                   &gl_todo_data->due_time);
          if (error_code != CALENDAR_ERROR_NONE) {
              dlog_print(DLOG_ERROR, LOG_TAG, "get due_time failed: %x\n", error_code);
              _free_gl_todo_data(gl_todo_data);

              return NULL;
          }

          return gl_todo_data;
      }
      ```

      To access a specific todo detail in a child record, retrieve the child record.

3. When no longer needed, destroy the list handle and release all its resources using the `calendar_list_destroy()` function:

   ```
   calendar_list_destroy(list, true);
   ```

<a name="update"></a>
## Updating a Todo

To update todo details:

1. Retrieve the todo you want to update using the `calendar_db_get_record()` function with the todo ID as the second parameter:

   ```
   calendar_record_h record;
   const int todo_id = ...; /* Get the todo ID */
   error_code = calendar_db_get_record(_calendar_todo._uri, todo_id, &record);
   if (error_code != CALENDAR_ERROR_NONE)
       dlog_print(DLOG_ERROR, LOG_TAG, "calendar_db_get_record failed: %x\n", error_code);
   ```

   You can also retrieve the todo using a search function, such as `calendar_db_get_records_with_query()`.

2. Set the properties you want to update.

   The following example sets a new subject and description for the todo:

   ```
   error_code = calendar_record_set_str(record, _calendar_todo.summary, "summary updated");
   if (error_code != CALENDAR_ERROR_NONE)
       dlog_print(DLOG_ERROR, LOG_TAG, "set summary failed: %x\n", error_code);

   error_code = calendar_record_set_str(record, _calendar_todo.description, "description updated");
   if (error_code != CALENDAR_ERROR_NONE)
       dlog_print(DLOG_ERROR, LOG_TAG, "set description failed: %x\n", error_code);
   ```

3. Update the todo using the `calendar_db_update_record()` function:

   ```
   error_code = calendar_db_update_record(record);
   if (error_code != CALENDAR_ERROR_NONE)
       dlog_print(DLOG_ERROR, LOG_TAG, "calendar_db_update_record failed: %x\n", error_code);
   ```

4. When no longer needed, destroy the todo handle and release all its resources using the `calendar_record_destroy()` function:

   ```
   calendar_record_destroy(record, true);
   ```

<a name="delete"></a>
## Deleting a Todo

To delete a todo, use the `calendar_db_delete_record()` function with the todo ID as the second parameter:

```
int todo_id = ...; /* Get the todo ID */
error_code = calendar_db_delete_record(_calendar_todo._uri, todo_id);
if (error_code != CALENDAR_ERROR_NONE)
    dlog_print(DLOG_ERROR, LOG_TAG, "calendar_db_delete_record failed: %x\n", error_code);
```

<a name="monitor"></a>
## Monitoring Todo Changes

To receive a notification whenever a todo changes:

1. Register a callback using the `calendar_db_add_changed_cb()` function:

   ```
   error_code = calendar_db_add_changed_cb(_calendar_todo._uri, _todo_changed_callback, NULL);
   if (error_code != CALENDAR_ERROR_NONE)
       dlog_print(DLOG_ERROR, LOG_TAG, "calendar_db_add_changed_cb failed: %x\n", error_code);
   ```

2. Define the todo change callback.

   The following example shows how to retrieve the new todo details in the callback:

   ```
   static calendar_gl_todo_data_t *_gl_todo_data = ...;

   static void
   _todo_changed_callback(const char *view_uri, void *user_data)
   {
       if (0 != strcmp(view_uri, _calendar_todo._uri))
           return;

       if (NULL == _gl_todo_data)
           return;

       int todo_id = _gl_todo_data->id;
       _free_gl_todo_data(_gl_todo_data);
       _gl_todo_data = NULL;

       calendar_record_h record = NULL;
       calendar_error_e error_code;
       error_code = calendar_db_get_record(_calendar_todo._uri, todo_id, &record);
       if (error_code != CALENDAR_ERROR_NONE)
           return;

       _gl_todo_data = _create_gl_todo_data(record);
       /* Use _gl_todo_data */

       calendar_record_destroy(record, true);
   }
   ```

<a name="make"></a>
## Creating a vCalendar

To create a vCalendar stream from an event:

1. Retrieve the event:

   ```
   int event_id = ...; /* Get the event ID */
   calendar_record_h record = NULL;
   error_code = calendar_db_get_record(_calendar_event._uri, event_id, &record);
   if (error_code != CALENDAR_ERROR_NONE)
       dlog_print(DLOG_ERROR, LOG_TAG, "calendar_db_get_record failed: %x\n", error_code);
   ```

2. Create a vCalendar stream from the event:

   ```
   char *vcalendar_stream = NULL;
   calendar_list_h list = NULL;

   error_code = calendar_list_create(&list);
   if (error_code != CALENDAR_ERROR_NONE)
       dlog_print(DLOG_ERROR, LOG_TAG, "calendar_list_create failed: %x\n", error_code);

   error_code = calendar_list_add(list, record);
   if (error_code != CALENDAR_ERROR_NONE)
       dlog_print(DLOG_ERROR, LOG_TAG, "calendar_list_add failed: %x\n", error_code);

   error_code = calendar_vcalendar_make_from_records(list, &vcalendar_stream);
   if (error_code != CALENDAR_ERROR_NONE)
       dlog_print(DLOG_ERROR, LOG_TAG, "calendar_vcalendar_make_from_records failed: %x\n", error_code);
   ```

3. When no longer needed, free the vCalendar stream, destroy the list handle, and release all its resources:

   ```
   free(vcalendar_stream);
   calendar_list_destroy(list, true);
   ```

<a name="parse"></a>
## Parsing a vCalendar

To parse a vCalendar from a file and insert its content into the calendar database:

1. Parse the vCalendar stream using the `calendar_vcalendar_parse_to_calendar_foreach()` function:

   ```
   char vcalendar_file_path[512] = {0};
   char *resource_path = app_get_resource_path();
   snprintf(vcalendar_file_path, sizeof(vcalendar_file_path), "%s/%s", resource_path, "vcalendar.ics");
   free(resource_path);

   error_code = calendar_vcalendar_parse_to_calendar_foreach(/* vCalendar file path */
                                                             vcalendar_file_path,
                                                             /* Callback to invoke */
                                                             _vcalendar_parse_cb,
                                                             /* User data for callback */
                                                             NULL);
   ```

2. Define a callback that inserts the parsed event or todo into the calendar database.

   The vCalendar stream can contain multiple events or todos. The `calendar_vcalendar_parse_to_calendar_foreach()` function invokes a separate callback for each parsed item. As long as the callback returns `true`, the foreach function continues to parse new events and todos.

   ```
   static bool
   _vcalendar_parse_cb(calendar_record_h record, void *user_data)
   {
       if (NULL == record)
           return false;

       int id = -1;
       error_code = calendar_db_insert_record(record, &id);
       if (error_code != CALENDAR_ERROR_NONE) {
           dlog_print(DLOG_ERROR, LOG_TAG, "calendar_db_insert_record failed: %x\n", error_code);

           return false;
       }
       dlog_print(DLOG_ERROR, LOG_TAG, "inserted id: %d\n", id);
       /* Use record */

       return true;
   }
   ```

## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 3.0 and Higher for Wearable
