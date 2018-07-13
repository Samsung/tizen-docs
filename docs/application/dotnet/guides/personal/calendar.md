# Calendar


A calendar is a system of organizing days for social purposes. It is composed of [records](#record2), such as events and todos. The records consist of subrecords, such as alarms, attendees, or extensions. For example, if an event is recurring, separate instances are generated for each time the event occurs.

The calendar information is stored in a calendar database. To manage the information in the database, you must [create a calendar manager instance](#prerequisites).

The following figure illustrates the calendar model.

**Figure: Calendar model**

![Calendar model](./media/calendar_model.png)

The main features of the Tizen.Pims.Calendar namespace include:

-   Calendar books

    -   Determine where the events and todos belong.
    -   Create [calendar books](#book) using the local device (with no account), service providers, such as Google or Yahoo (with an account), or applications, such as Joyn or Facebook.
    -   Search and organize events using [filters and queries](#filter2).
    -   Monitor [database changes](#change).

    Each account can have multiple calendar books. The calendar book name does not need to be unique on the device because it is handled with an ID. Since the local device address book has no account, its related account ID is zero.

- Events and todos
    -   Manage [event instances](#event).
    -   Create [events](#create_event) and [todos](#create), set properties for them, such as summary, start time, and description, and store them in the database.
    -   Update [event](#update_event) and [todo](#update) details in the database.
    -   Delete [events](#delete_event) and [todos](#delete) from the database.
    -   Set [reminders](#remind).

The calendar service supports [vCalendars](#vcal).

The following figure illustrates the different Calendar entities and their relationships.

**Figure: Calendar entities**

![Calendar entities](./media/calendar_entity.png)

<a name="record2"></a>
## Records

A record represents an actual record in the internal database, but you can consider it as a structure describing a single but complex entity, such as a calendar event or a time zone.

A record has many properties, for example, a todo record has the todo description, priority, progress, creation time, last modified and completed time, and many other properties. A record can also contain an identifier field, which holds an ID of another record. Setting this field's value establishes a relation between the records, for example, a calendar event contains the ID of a calendar book to which it belongs.

Records are stored as instances of the [Tizen.Pims.Calendar.CalendarRecord](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Pims.Calendar.CalendarRecord.html) class. The following examples illustrate creating a new record and retrieving an existing record by using its ID:

-   Creating a new record:

    ```
    var record = new CalendarRecord(CalendarViews.Event.Uri);
    ```

- Retrieving an existing record:

    ```
    var manager = new CalendarManager();
    var record = manager.Get(CalendarViews.Event.Uri, eventId);
    ```

To manage the record, you can use the classes of the [Tizen.Pims.Calendar.CalendarViews](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Pims.Calendar.CalendarViews.html) namespace and the [Tizen.Pims.Calendar.CalendarTypes](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Pims.Calendar.CalendarTypes.html) class:

-   URI

    A record type is identified by a structure called the view. For example, the [Tizen.Pims.Calendar.CalendarViews.Event](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Pims.Calendar.CalendarViews.Event.html) class describes the properties of the calendar event record. Every class in the Tizen.Pims.Calendar.CalendarViews namespace has a `Uri` field that uniquely identifies the view. In many cases, you must provide the `Uri` value to indicate what type of record you want to create or operate on.

    ```
    var record = new CalendarRecord(CalendarViews.Event.Uri);
    ```

- Views and properties

    Generic access methods can be used (according to data-view declarations) to access calendar views. A data-view is almost the same as a database "VIEW", which limits access and guarantees performance. A "record" represents a single row of the data-views.

    **Table: Calendar views**

    | Views                                    | Description                              |
    |----------------------------------------|----------------------------------------|
    | `Tizen.Pims.Calendar.CalendarViews.Book` | This view holds calendar book properties, such as name, color, and visibility.<br>There are 3 [default calendar books](#book) for the local event, todo, and birthday event types.<br>Calendar books can be created by service providers, such as Google or Yahoo (with an account), or by applications, such as Joyn or Facebook. |
    | `Tizen.Pims.Calendar.CalendarViews.Event` | This view holds event properties, such as a summary, description, and location.<br>Alarms, attendees, and extended views can be inserted as child records for an event.<br>Recurrence properties can be set to make a repeating event, such as a birthday.<br>The recurrence rules follow the [vCalendar2.0 specification](https://www.ietf.org/rfc/rfc2445.txt). |
    | `Tizen.Pims.Calendar.CalendarViews.Todo` | This view holds todo properties, such as a due time. |
    | `Tizen.Pims.Calendar.CalendarViews.Alarm` | This view holds notification properties. Multiple alarms can be inserted into an event or todo. |
    | `Tizen.Pims.Calendar.CalendarViews.Attendee` | This view holds attendee properties. Multiple attendees can be inserted into an event or todo. |
    | `Tizen.Pims.Calendar.CalendarViews.Timezone` | This view holds time zone properties.    |
    | `Tizen.Pims.Calendar.CalendarViews.InstanceUtimeBook` | This view has the combined properties of instance and book.<br>Instances are generated depending on time type (`UtcTime` or `LocalTime`). |
    | `Tizen.Pims.Calendar.CalendarViews.InstanceLocaltimeBook` | This view has the combined properties of instance and book. The instance view is used to get repeat instances.<br>Instances are generated depending on the time type (`UtcTime` or `LocalTime`). |
    | `Tizen.Pims.Calendar.CalendarViews.InstanceUtimeBookExtended` | This view has the combined properties of instance, book, and extended. The instance view is used to get repeat instances.<br>Instances are generated depending on the time type (`UtcTime` or `LocalTime`). |
    | `Tizen.Pims.Calendar.CalendarViews.InstanceLocaltimeBookExtended` | This view has the combined properties of instance, book, and extended. The instance view is used to get repeat instances.<br>Instances are generated depending on the time type (`UtcTime` or `LocalTime`). |
    | `Tizen.Pims.Calendar.CalendarViews.UpdatedInfo` | This view has properties to use when identifying record changes depending on the version. |
    | `Tizen.Pims.Calendar.CalendarViews.Extended` | This view has the key/value properties to add extended data. |

- The calendar service uses a version system. Whenever modifications are made in the database, the version number is increased. If sync applications, such as Google or Facebook, sync at version 13 and try to sync again every 1 minute, they want to get the changes from version 14 to the current version. To get the current version, use the `Version` property of the [Tizen.Pims.Calendar.CalendarDatabase](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Pims.Calendar.CalendarDatabase.html) class. You can retrieve the modified record list with the `GetChangesByVersion()` method.

    ```
    var manager = new CalendarManager();

    int version;
    version = manager.Database.Version;

    int currentVersion;
    var changeslist = manager.Database.GetChangesByVersion(..., currentVersion);

    int lastVersion;
    manager.Database.GetLastChangeVersion(lastVersion);
    ```

- Basic types

    Records contain properties of basic types: `integer`, `long`, `double`, `string`, and `CalendarTime`.

    The `CalendarTime` type holds a time stamp in the `DateTime` format.

    The following table lists the setter and getter methods for each type.

    **Table: Setter and getter methods**

    | Type           | Property                                 | Setter                                   | Getter                                   |
    |--------------|----------------------------------------|----------------------------------------|----------------------------------------|
    | `integer`      | `Tizen.Pims.Calendar.CalendarViews.Event.BookId` | `record.Set<int>(CalendarViews.Event.BookId, 3)` | `record.Get<int>(CalendarViews.Event.BookId)` |
    | `long`         | `Tizen.Pims.Calendar.CalendarViews.Todo.CompletedTime` | `record.Set<long>(CalendarViews.Todo.CompletedTime, 349866000)` | `record.Get<long>(CalendarViews.Todo.CompletedTime)` |
    | `double`       | `Tizen.Pims.Calendar.CalendarViews.Event.Latitude` | `record.Set<double>(CalendarViews.Event.Latitude, 37.566)` | `record.Get<double>(CalendarViews.Event.Latitude)` |
    | `string`       | `Tizen.Pims.Calendar.CalendarViews.Event.Summary` | `record.Set<string>(CalendarViews.Event.Summary, "Birthday")` | `record.Get<string>(CalendarViews.Event.Summary)` |
    | `CalendarTime` | `Tizen.Pims.Calendar.CalendarViews.Event.Start` | `record.Set<CalendarTime>(CalendarViews.Event.Start, new CalendarTime(349866000))` | `record.Get<CalendarTime>(CalendarViews.Event.Start)` |

    These methods also require specifying which property to get and set, and for this, every getter and setter method needs a record and property ID.

    For example, the property ID of a `Summary` property of an event is `CalendarViews.Event.Summary`.

    The following example sets the `Summary` property of an event record:

    ```
    var record = new CalendarRecord(CalendarViews.Event.Uri);
    record.Set<string>(CalendarViews.Event.Summary, "Meeting");
    ```

    The `CalendarTime` type can hold 2 types of data. To make UTC time, epoch time needs to be inserted as a parameter.

    Birthday is not changed based on the timezone. In this case, the local time type needs to be used to fix the date.

    For example, setting a time with `new CalendarTime(1981, 2, 1, 0, 0, 0);` means that the date, 1981/02/01, is constant in all countries.

    **Table: CalendarTime data types**

    | Identifier                | Description                              |
    |-------------------------|----------------------------------------|
    | `CalendarTime.Type.Utc`   | UTC time is used to describe non-all-day events.<br>For non-all-day events, you must convert local time to UTC time. The local time zone identifier must be stored in the record, in the corresponding property.<br>For example, when setting the start time of an event, the local time zone must be stored in the `CalendarViews.Event.StartTzid` property. |
    | `CalendarTime.Type.Local` | Date only (year, month, and day of the month) is used to describe all-day events.<br>For all day events, use `CalendarTime` with parameters (year, month, day, hour, minute, second).<br>Both the start and end time of the event must be set, and they do not have to be equal. If they are not, the event lasts more than 1 day. |

    For example, adding an event with the current time:

    ```
    CalendarTime input = new CalendarTime(DateTime.Now.Ticks);
    CalendarRecord record;

    record = new CalendarRecord(CalendarViews.Event.Uri);
    record.Set<CalendarTime>(CalendarViews.Event.Start, input);
    record.Set<string>(CalendarViews.Event.StartTzid, "Asia/Seoul");
    ```

    For example, adding a birthday on 1st of February, 1981:

    ```
    CalendarTime input = new CalendarTime(1981, 2, 1, 0, 0, 0);
    CalendarRecord record;

    record = new CalendarRecord(CalendarViews.Event.Uri);
    record.Set<CalendarTime>(CalendarViews.Event.Start, input);
    ```

    <a name="children"></a>
### Child Records

A certain record type can be a parent of other records. For example, the attendee records can hold an event identifier in their `ParentId` property. The event is the parent record of the attendee child records.

The following code example creates an event and inserts an attendee record into it as a child record:

```
var record = new CalendarRecord(CalendarViews.Event.Uri);
var attendee = new CalendarRecord(CalendarViews.Attendee.Uri);
attendee.Set<string>(CalendarViews.Attendee.Name, "John");
record.AddChild(CalendarViews.Event.Attendee, attendee);
```

<a name="book"></a>
## Calendar Books

A calendar book is a container for other calendar records. Every event and todo must belong to a calendar book. There are 3 built-in calendar books, as shown in the following table.

**Table: Calendar books**

| Book                                 | Description         |
|------------------------------------|-------------------|
| `CalendarTypes.DefaultBook.Event`    | Local Event book    |
| `CalendarTypes.DefaultBook.Todo`     | Local Todo book     |
| `CalendarTypes.DefaultBook.Birthday` | Local Birthday book |

To set a calendar book ID for an event:
```
var record = new CalendarRecord(CalendarViews.Event.Uri);
record.Set<int>(CalendarViews.Event.BookId, CalendarTypes.DefaultBook.Event);
```

To receive a list of existing calendar books:

```
var manager = new CalendarManager();
var list = manager.Database.GetAll(CalendarViews.Book.Uri, 0, 0);
```

The `GetAll()` method requires as its parameters the URI of the class to get records from, the index from which results are received, and the maximum number of results.

<a name="event"></a>
## Event Instances and Reminders

An event record describes various properties, such as description, categories, and priority. It also contains information on when the event takes place. In a recurring event, there is more than 1 instance of the event. Each instance has its corresponding instance record.

If an event is inserted with recurrence rule, alarm, and attendee, its data is saved to each relevant database. Generated instances based on the recurrence rule are also stored in the instance database.

**Figure: Views and databases for event instances**

![Views and databases for event instances](./media/calendar_db.png)

The following table illustrates an example of a recurring event and its instances.

**Table: Event and instance example**

| Event with recurrence rule               | Generated instances |
|----------------------------------------|-------------------|
| Recurrence rules: <br>Start date on 2012-10-09 (Tuesday)<br>Frequency set to WEEKLY<br>Interval set to 1<br>Count set to 3 | 2012-10-09 Tuesday  |
| Recurrence rules: <br>Start date on 2012-10-09 (Tuesday)<br>Frequency set to WEEKLY<br>Interval set to 1<br>Count set to 3 | 2012-10-16 Tuesday  |
| Recurrence rules: <br>Start date on 2012-10-09 (Tuesday)<br>Frequency set to WEEKLY<br>Interval set to 1<br>Count set to 3 | 2012-10-22 Tuesday  |

The calendar recurrence model is compliant with the [iCalendar specification](http://www.ietf.org/rfc/rfc2445.txt). The following event properties have the same functionality as their corresponding values in iCalendar:

**Table: Recurrence rules**

| Recurrence rule property | Description                              |
|------------------------|----------------------------------------|
| `Freq`                   | Yearly, monthly, weekly, or daily        |
| `Count`                  | Until count. If the count is 3, 3 instances are generated. |
| `Interval`               | Interval is a positive integer representing how often the recurrence rule repeats |
| `Byday`                  | MO, TU, WE, TH, FR, SA, or SU            |
| `Bymonthday`             | Days of the month                        |
| `Byyearday`              | Days of the year                         |
| `Byweekno`               | Ordinals specifying weeks of the year    |
| `Bymonth`                | Months of the year                       |
| `Bysetpos`               | Values which correspond to the nth occurrence within the set of events |
| `Wkst`                   | Day on which the workweek starts         |

When you have a recurring event, you can [remove a specific recurrence instance](#exception_add) from it, or [add exceptions to the recurrence](#exception_modify).

<a name="exception_rule"></a>
### Exceptions

If 1 instance of a recurring event is modified (such as its summary or date) or deleted, it is called an exception. For example, if the second instance date is modified from 16th to 17th, 17th is the exception.

**Table: Exception example**

| Event                                    | Instances          | Exceptions         |
|----------------------------------------|------------------|------------------|
| Recurrence rules:<br>Start date on 2012-10-09 (Tuesday)<br>Frequency set to WEEKLY<br>Interval set to 1<br>Count set to 3 | 2012-10-09 Tuesday |                    |
| Recurrence rules:<br>Start date on 2012-10-09 (Tuesday)<br>Frequency set to WEEKLY<br>Interval set to 1<br>Count set to 3 |                    | 2012-10-17 Tuesday |
| Recurrence rules:<br>Start date on 2012-10-09 (Tuesday)<br>Frequency set to WEEKLY<br>Interval set to 1<br>Count set to 3 | 2012-10-22 Tuesday |                    |

<a name="remind"></a>
### Reminders

The following figure illustrates how the alarm process works.

**Figure: Alarm process**

![Alarm process](./media/calendar_alarm.png)

To get a reminder when an alarm is triggered, the application must set the reminder MIME name. After the reminder MIME name is set, insert an alarm as a child of an event record:

```
/// Set alarm
var alarm = new CalendarRecord(CalendarViews.Alarm.Uri);
alarm.Set<int>(CalendarViews.Alarm.TickUnit, CalendarTypes.TickUnit.Specific);
/// 60 secs before 1404036000 (Sun, 29 Jun 2014 10:00:00 GMT)
alarm.Set<CalendarTime>(CalendarViews.Alarm.AlarmTime, new CalendarTime(1404036000 - 60));

/// Add alarm as child
var record = new CalendarRecord(CalendarViews.Event.Uri);
record.AddChild(CalendarViews.Event.Alarm, alarm);
```

When the registered alarm is triggered and the alarm manager notices it, the calendar service calls those packages that have the reminder MIME name.

<a name="filter2"></a>
## Filters and Queries

Queries are used to retrieve [event](#get_event) and [todo](#get) data which satisfies a given criteria, like an integer property being greater than a given value, or a string property containing a given substring. The criteria are defined by creating filters and adding conditions to them, joining them with logical operators. Also, instead of a condition, another filter can be added to create more complex filters.

When a filter is ready, it can be set as a property of a query. Other query properties allow configuring how the returned results are grouped and sorted.

To filter calendar data:

-   Filtering

    The operator precedence in filters is determined by the order in which the conditions and filters are added. The following table shows an example of how the operator precedence works.

    **Table: Filter conditions**

    | Condition                                | Result                                   |
    |----------------------------------------|----------------------------------------|
    | Condition C1<br>OR<br>Condition C2<br>AND<br>Condition C3 | (C1 OR C2) AND C3                        |
    | **Filter F1**:<br>Condition C1<br>OR<br>Condition C2<br><br>**Filter F2**:<br>Condition C3<br>OR<br>Condition C4<br><br>**Filter F3**:<br>Condition C5<br>AND<br>F1<br>AND<br>F2 | (C5 AND F1) AND F2<br>Meaning (C5 AND (C1 OR C2)) AND (C3 OR C4) |

    The following code creates a filter, accepting events with high priority:

    ```
    var query = new CalendarQuery(CalendarViews.Event.Uri);
    var filter = new CalendarFilter(CalendarViews.Event.Uri, CalendarViews.Event.Priority, CalendarFilter.IntegerMatchType.Equal, CalendarTypes.Priority.High);
    query.SetFilter(filter);

    var manager = new CalendarManager();
    var list = manager.Database.GetRecordsWithQuery(query, 0, 0);
    ```

- Projection querying

    A projection allows you to query the data for only those specific properties of a record that you actually need, at lower latency and cost than retrieving the entire set of properties.

    The following example code creates a filter that gets only the event ID and summary from the records with the "test" (string filter) in their summary. Create a query, and add a filter to it; the results are received in a list.

    ```
    var query = new CalendarQuery(CalendarViews.Event.Uri);
    var filter = new CalendarFilter(CalendarViews.Event.Uri, CalendarViews.Event.Summary, CalendarFilter.StringMatchType.Contains, "test");
    query.SetFilter(filter);

    uint[] projection = new uint[] {CalendarViews.Event.Summary, CalendarViews.Event.Id};
    query.SetProjection(projection);

    var manager = new CalendarManager();
    var list = manager.Database.GetRecordsWithQuery(query, 0, 0);
    filter.Dispose();
    query.Dispose();
    ```

    <a name="change"></a>
## Database Change Notifications

To detect the [event](#monitor_event) and [todo](#monitor) changes in the calendar database, register an event handler with the `AddDBChangedDelegate()` method. To deregister the event handler and ignore database changes, use the `RemoveDBChangedDelegate()` method.

Clients wait for calendar change notifications on the client side. If the calendar is changed by another module, the server publishes an inotify event. The Inotify module broadcasts to the subscribed modules, and an internal inotify handler is called at the client side. A user event handler is called with the user data.

```
static void DBChangedHandler(object sender, DBChangedEventArgs args)
{
    /* Do something */
}

var manager = new CalendarManager();
manager.Database.AddDBChangedDelegate(CalendarViews.Event.Uri, DBChangedHandler);
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

-   You can use the calendar service to [compose a vCalendar stream](#make). With the stream, it is possible to transmit data in JSON format.

    ```
    var list = CalendarList(CalendarViews.Event.Uri);
    var record = CalendarRecord(CalendarViews.Event.Uri);
    list.AddRecord(record);
    string stream = CalendarVcalendar.Compose(list);
    ```

- You can [parse the vCalendar](#parse):

    ```
    string stream = "BEGIN:VCALENDAR\r\n"
                    + "VERSION:1.0\r\n"
                    + "BEGIN:VEVENT\r\n"
                    + "SUMMARY:test1\r\n"
                    + "DTSTART:20140721T000000Z\r\n"
                    + "DTEND:20140721T010000Z\r\n"
                    + "AALARM;TYPE=WAVE;VALUE=CONTENT-ID:19960903T060000;PT15M;4;\r\n"
                    + "DALARM:19960415T235000;PT5M;2;Your Taxes Are Due !!!\r\n"
                    + "MALARM:;TYPE=WAVE;VALUE=URL:19960415T235959; ; ; file:///mmedia/taps.wav\r\n"
                    + "END:VEVENT\r\n"
                    + "END:VCALENDAR\r\n";
    var list = CalendarVcalendar.Parse(stream);
    ```

## Prerequisites

To enable your application to use the calendar functionality:

1.  To use the calendar, the application has to request permission by adding the following privileges to the `tizen-manifest.xml` file:

    ```
    <privileges>
       <privilege>http://tizen.org/privilege/calendar.read</privilege>
       <privilege>http://tizen.org/privilege/calendar.write</privilege>
    </privileges>
    ```

2. To use the methods and properties of the [Tizen.Pims.Calendar](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Pims.Calendar.html) namespace, include it in your application:

    ```
    using Tizen.Pims.Calendar;
    ```

3. To access the calendar database, create a new instance of the [Tizen.Pims.Calendar.CalendarManager](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Pims.Calendar.CalendarManager.html) class:

    ```
    var manager = new CalendarManager();
    ```

    <a name="create_event"></a>
## Creating an Event

Creating a new event involves creating an event instance, setting its properties, and inserting it into the calendar database.

Some event properties are defined as child records that are associated with the parent record.

To create a new event:

1.  Create the event as an instance of the [Tizen.Pims.Calendar.CalendarRecord](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Pims.Calendar.CalendarRecord.html) class, with the `CalendarViews.Event.Uri` property as a parameter:

    ```
    var record = new CalendarRecord(CalendarViews.Event.Uri);
    ```

2. Set the event properties:

    -   Set the subject:

        ```
        record.Set<string>(CalendarViews.Event.Summary, "summary");
        ```

    - Set the description:

        ```
        record.Set<string>(CalendarViews.Event.Description, "description");
        ```

    - Set the time zone for the start and end times:

        ```
        record.Set<string>(CalendarViews.Event.StartTzid, "Asia/Seoul");
        ```

    - Set the start and end times:

        ```
        CalendarTime start = new CalendarTime(1404036000); /// 2014/06/29 10:00:00 UTC
        CalendarTime end = new CalendarTime(start.UtcTime + 3600); /// 1 hour later

        record.Set<CalendarTime>(CalendarViews.Event.Start, start);
        record.Set<CalendarTime>(CalendarViews.Event.End, end);
        ```

    - To create a recurring event:

        1.  Set the frequency.

            In the following example, the event is set to occur every month on the 3rd, 4th, and 5th day:

            ```
            var record = new CalendarRecord(CalendarViews.Event.Uri);
            record.Set<int>(CalendarViews.Event.Freq, CalendarTypes.Recurrence.Monthly);
            record.Set<int>(CalendarViews.Event.Interval, 1);
            record.Set<int>(CalendarViews.Event.Bymonthday, "3,4,5");
            ```

        2. Set the range of recurrence.

            In the following example, the event is set to occur a total of 8 times:

            ```
            record.Set<int>(CalendarViews.Event.RangeType, CalendarTypes.RangeType.Count);
            record.Set<int>(CalendarViews.Event.Count, 8);
            ```

        Based on the recurrence settings above and the start time (set in the previous step) of June 29, this event occurs 8 times: on Jul 3, 4, and 5, on Aug 3, 4, and 5, and on Sep 3 and 4.

    - Add an alarm.

        To add an alarm, create an alarm record as an instance of the `Tizen.Pims.Calendar.CalendarRecord` class, set the alarm properties, and insert the alarm as a child record to the event.

        In the following example, the alarm is defined to activate 60 seconds before the event start time:

        ```
        var alarm = new CalendarRecord(CalendarViews.Alarm.Uri);
        alarm.Set<int>(CalendarViews.Alarm.TickUnit, CalendarTypes.TickUnit.Specific);
        alarm.Set<CalendarTime>(CalendarViews.Alarm.AlarmTime, new CalendarTime(1404036000 - 60)); /// 60 sec before starttime (1404036000)

        record.AddChild(CalendarViews.Event.Alarm, alarm);
        ```

        The [Tizen.Pims.Calendar.CalendarTypes.TickUnit](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Pims.Calendar.CalendarTypes.TickUnit.html) enumeration defines the available alarm tick units.

        > **Note**   
		> If you use `Tizen.Pims.Calendar.CalendarTypes.TickUnit.Specific` as a tick unit, specify the alarm time in Unix time.

    - Add an attendee.

        To add an attendee, create an attendee record as an instance of the `Tizen.Pims.Calendar.CalendarRecord` class, set the attendee properties, and insert the attendee as a child record to the event.

        In the following example, 1 attendee named John is added:

        ```
        var attendee = new CalendarRecord(CalendarViews.Attendee.Uri);
        attendee.Set<string>(CalendarViews.Attendee.Name, "John");

        record.AddChild(CalendarViews.Event.Attendee, attendee);
        ```

    Set other event properties similarly, as needed.

3. Insert the event into the calendar database using the `Insert()` method of the [Tizen.Pims.Calendar.CalendarDatabase](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Pims.Calendar.CalendarDatabase.html) class. All child records added to the event are inserted automatically along with the parent.

    The system assigns a unique ID to the event, and the method returns it.

    ```
    var manager = new CalendarManager();
    int recordId = manager.Database.Insert(record);
    ```

    <a name="get_event"></a>
## Retrieving Events

To retrieve a single event:

1.  Retrieve an event record using the `Get()` method of the [Tizen.Pims.Calendar.CalendarDatabase](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Pims.Calendar.CalendarDatabase.html) class, with the event ID as the second parameter:

    ```
    var manager = new CalendarManager();
    var record = manager.Database.Get(CalendarViews.Event.Uri, eventId);
    ```

2. When no longer needed, destroy the event instance and release all its resources using the `Dispose()` method of the [Tizen.Pims.Calendar.CalendarRecord](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Pims.Calendar.CalendarRecord.html) class:

    ```
    record.Dispose();
    ```

To retrieve multiple events:

1.  Retrieve a list of all events, or retrieve a filtered list of events:
    -   To retrieve a list of all events, use the `GetAll()` method of the `Tizen.Pims.Calendar.CalendarDatabase` class:

        ```
        var manager = new CalendarManager();
        var list = manager.Database.GetAll(CalendarViews.Event.Uri, 0, 0);
        ```

    - To retrieve a filtered list of events:
        1.  Create a query as an instance of the [Tizen.Pims.Calendar.CalendarQuery](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Pims.Calendar.CalendarQuery.html) class:

            ```
            var query = new CalendarQuery(CalendarViews.Event.Uri)
            ```

        2. Create a filter using the [Tizen.Pims.Calendar.CalendarFilter](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Pims.Calendar.CalendarFilter.html) class and adding conditions.

            The following example adds a string-based filtering condition that retrieves the events whose summary field contains the string "summary to find":

            ```
            var filter = new CalendarFilter(CalendarViews.Event.Uri, CalendarViews.Event.Summary, CalendarFilter.StringMatchType.Contains, "summary to find");
            ```

        3. To add more conditions, define an operator between the conditions.

            The following example adds an AND operator along with a second condition, which is a string-based filtering condition that retrieves the events whose description field contains the string "description to find".

            The combination of the AND operator and the 2 conditions means that the filter only retrieves the events that contain "summary to find" in their summary and "description to find" in their description.

            ```
            filter.AddCondition(CalendarFilter.LogicalOperator.And, CalendarViews.Event.Description, CalendarFilter.StringMatchType.Contains, "description to find");
            ```

            You can also create a filter with integer and time conditions. For example, to filter all-day events that start after January 1st, 2016:

            ```
            CalendarTime start = new CalendarTime(2016, 1, 1, 0, 0, 0);
            filter.AddCondition(CalendarFilter.LogicalOperator.And, CalendarViews.Event.Start, CalendarFilter.IntegerMatchType.GreaterThanOrEqual, start);
            ```

        4. Set the filter to the query using the `SetFilter()` method of the `Tizen.Pims.Calendar.CalendarQuery` class:

            ```
            query.SetFilter(filter);
            ```

        5. Retrieve the filtered list of events using the `GetRecordsWithQuery()` method of the `Tizen.Pims.Calendar.CalendarDatabase` class:

            ```
            var list = manager.Database.GetRecordsWithQuery(query, 0, 0);
            ```

            The third parameter defines a limit for the number of results. If you set it to 0, the list returns all events matching the query.

        6. When no longer needed, destroy the filter and query instances and release all their resources using the `Dispose()` methods of the `Tizen.Pims.Calendar.CalendarFilter` and `Tizen.Pims.Calendar.CalendarQuery` classes, respectively:

            ```
            filter.Dispose();
            query.Dispose();
            ```

2. Use a loop to iterate through the list and retrieve the event details.

    Move forward and backward within the event list using the `MovePrevious()` and `MoveNext()` methods of the [Tizen.Pims.Calendar.CalendarList](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Pims.Calendar.CalendarList.html) class, and retrieve the current event with the `GetCurrentRecord()` method.

    The following example iterates through the list and retrieves the summary of each event:

    ```
    var manager = new CalendarManager();
    var list = manager.Database.GetAll(CalendarViews.Event.Uri, 0, 0);
    list.MoveFirst();
    var record;
    while (record = list.GetCurrentRecord())
    {
        string summary = record.Get<string>(CalendarViews.Event.Summary);
        list.MoveNext();
    }
    ```

3. When no longer needed, destroy the list instance and release all its resources using the `Dispose()` method:

    ```
    list.Dispose();
    ```

    <a name="update_event"></a>
## Updating an Event

To update event details:

1.  Retrieve the event you want to update using the `Get()` method of the [Tizen.Pims.Calendar.CalendarDatabase](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Pims.Calendar.CalendarDatabase.html) class, with the event ID as the second parameter:

    ```
    var manager = new CalendarManager();
    var record = manager.Database.Get(CalendarViews.Event.Uri, eventId);
    ```

    You can also retrieve the event using the `GetRecordsWithQuery()` method.

2. Set the properties you want to update.

    The following example sets a new subject and description for the event.

    ```
    record.Set<string>(CalendarViews.Event.Summary, "Updated Summary");
    record.Set<string>(CalendarViews.Event.Description, "Updated Description");
    ```

3. Update the event using the `Update()` method:

    ```
    manager.Database.Update(record);
    ```

4. When no longer needed, destroy the event and database manager instances and release all their resources using the `Dispose()` methods of the [Tizen.Pims.Calendar.CalendarRecord](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Pims.Calendar.CalendarRecord.html) and [Tizen.Pims.Calendar.CalendarManager](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Pims.Calendar.CalendarManager.html) classes, respectively:

    ```
    record.Dispose();
    manager.Dispose();
    ```

    <a name="delete_event"></a>
## Deleting an Event

To delete an event, use the `Delete()` method of the [Tizen.Pims.Calendar.CalendarDatabase](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Pims.Calendar.CalendarDatabase.html) class, with the event ID as the second parameter:

```
var manager = new CalendarManager();
manager.Database.Delete(CalendarViews.Event.Uri, eventId);
```

<a name="exception_add"></a>
## Removing an Instance from a Recurring Event

To remove an event instance from a recurring event:

1.  Create a recurring event.

    The following example creates an event with the following properties:

    -   Frequency: monthly
    -   Interval: 1
    -   Days of the month: "3, 4, 5"
    -   Range type: count
    -   Count: 8

    ```
    var manager = new CalendarManager();

    var record = new CalendarRecord(CalendarViews.Event.Uri);
    record.Set<string>(CalendarViews.Event.Summary, "test");
    record.Set<string>(CalendarViews.Event.StartTzid, "Asia/Seoul");
    CalendarTime start = new CalendarTime(1349226000);
    record.Set<CalendarTime>(CalendarViews.Event.Start, start)
    record.Set<string>(CalendarViews.Event.EndTzid, "Asia/Seoul");
    CalendarTime end = new CalendarTime(1354582800);
    record.Set<CalendarTime>(CalendarViews.Event.End, end);

    record.Set<int>(CalendarViews.Event.Freq, CalendarTypes.Recurrence.Monthly);
    record.Set<int>(CalendarViews.Event.Interval, 1);
    record.Set<string>(CalendarViews.Event.Bymonthday, "3,4,5");
    record.Set<int>(CalendarViews.Event.RangeType, CalendarTypes.RangeType.Count);
    record.Set<int>(CalendarViews.Event.Count, 8);
    ```

    The event has 8 instances:

    **Table: Event instances**

    | unixtime                                 | Date time                                |
    |----------------------------------------|----------------------------------------|
    | 1349226000 <br>1349312400 <br> 1349398800 <br>1351904400 <br>1351990800<br> 1352077200 <br>1354496400<br> 1354582800 | 2012-10-03 01:00:00 <br>2012-10-04 01:00:00 <br>2012-10-05 01:00:00 <br>2012-11-03 01:00:00 <br>2012-11-04 01:00:00 <br>2012-11-05 01:00:00 <br>2012-12-03 01:00:00 <br>2012-12-04 01:00:00 |

2. Create the exception by setting the `Exdate` property.

    In vCalendar 2.0 (RFC 2445), the `Exdate` property is used to identify a deleted instance. If multiple instances are deleted, datetimes are added with a comma (for example, `20121104T010000Z, 20121105T010000Z, 20121203T010000Z`).

    ```
    record.Set<string>(CalendarViews.Event.Exdate, "20121104T010000Z");
    ```

3. Insert the event into the calendar database using the `Insert()` method of the `Tizen.Pims.Calendar.CalendarDatabase` class:

    ```
    int eventId = manager.Database.Insert(record);

    record.Dispose();
    ```

    <a name="exception_modify"></a>
## Adding an Exception to a Recurring Event

To add an exception to a recurring event:

1.  Make sure you have an existing recurring event.
2. Clone the existing event with the `Clone()` method of the [Tizen.Pims.Calendar.CalendarRecord](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Pims.Calendar.CalendarRecord.html) class.

    Cloning means that the new event initially has the same properties as the original event. In vCalendar 2.0 (RFC 2445), the recurrence ID is used to identify the modified instance (exception).

    ```
    var clone = record.Clone();
    clone.Set<int>(CalendarViews.Event.OriginalEventId, eventId);
    clone.Set<string>(CalendarViews.Event.RecurrenceId, "20121005T010000Z");
    ```

3. Modify or add event properties to create the exception.
4. Insert the exception into the calendar database using the `Insert()` method of the [Tizen.Pims.Calendar.CalendarDatabase](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Pims.Calendar.CalendarDatabase.html) class:

    ```
    var manager = new CalendarManager();
    int cloneId = manager.Database.Insert(clone);

    clone.Dispose();
    record.Dispose();
    ```

    <a name="monitor_event"></a>
## Monitoring Event Changes

To receive a notification whenever an event changes:

1.  Register an event handler using the `AddDBChangedDelegate()` method of the [Tizen.Pims.Calendar.CalendarDatabase](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Pims.Calendar.CalendarDatabase.html) class:

    ```
    var manager = new CalendarManager();
    manager.Database.AddDBChangedDelegate(CalendarViews.Event.Uri, DBChangedHandler);
    ```

2. Define the event handler:

    ```
    static void DBChangedHandler(object sender, DBChangedEventArgs args)
    {
        /// Do something
    }
    ```

    <a name="create"></a>
## Creating a Todo

Creating a new todo involves creating a todo instance, setting its properties, and inserting it into the calendar database.

Some todo properties are defined as child records that are associated with the parent record. For a detailed list of the todo properties, see the [Tizen.Pims.Calendar.CalendarViews.Todo](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Pims.Calendar.CalendarViews.Todo.html) view description. If the property type is `child list`, the property is defined as a child record.

To create a new todo:

1.  Create the todo as an instance of the [Tizen.Pims.Calendar.CalendarRecord](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Pims.Calendar.CalendarRecord.html) class, with the `Uri` property of the `Tizen.Pims.Calendar.CalendarDatabase` class as a parameter:

    ```
    var record = new CalendarRecord(CalendarViews.Todo.Uri);
    ```

    > **Note**   
	> Records created as instances of the `Tizen.Pims.Calendar.CalendarRecord` class are memory objects. If you change these objects, the changes are not reflected in the calendar database until you explicitly insert or update the objects to the database using the `Insert()` or `Update()` methods of the [Tizen.Pims.Calendar.CalendarDatabase](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Pims.Calendar.CalendarDatabase.html) class.

2. Set the todo properties:

    -   Set the subject.

        To set the subject for the todo, use the `Set<string>()` method with the `Summary` property of the `Tizen.Pims.Calendar.CalendarDatabase` class as the first parameter:

        ```
        record.Set<string>(CalendarViews.Todo.Summary, "Summary");
        ```

    - Set the description.

        To set the description for the todo, use the `Set<string>()` method with the `Description` property of the `Tizen.Pims.Calendar.CalendarDatabase` class as the first parameter:

        ```
        record.Set<string>(CalendarViews.Todo.Description, "Description");
        ```

    - Set the due time.

        To set the due time for the todo, use the `Set<CalendarTime>()` method with the `Due` property of the `Tizen.Pims.Calendar.CalendarDatabase` class as the first parameter:

        ```
        CalendarTime due = new CalendarTime(1404036000); /// 2014/06/29 11:00:00 UTC
        record.Set<CalendarTime>(CalendarViews.Todo.Due, due);
        ```

    - Set the status.

        To set the status for the todo, use the `Set<int>()` with the `Status` property of the `Tizen.Pims.Calendar.CalendarDatabase` class as the first parameter. The [Tizen.Pims.Calendar.Calendar​Types.​Todo​Status](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Pims.Calendar.CalendarTypes.TodoStatus.html) enumeration defines the possible status values.

        ```
        record.Set<int>(CalendarViews.Todo.Status, CalendarTypes.TodoStatus.NeedAction);
        ```

    Set other todo properties similarly, as needed.

3. Insert the todo into the calendar database using the `Insert()` method of the `Tizen.Pims.Calendar.CalendarDatabase` class. All child records added to the todo are inserted automatically along with the parent.

    ```
    var manager = new CalendarManager();
    int todoId = manager.Database.Insert(record);
    ```

4. When no longer needed, destroy the todo and database manager instances and release all their resources using the `Dispose()` methods of the `Tizen.Pims.Calendar.CalendarRecord` and [Tizen.Pims.Calendar.CalendarManager](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Pims.Calendar.CalendarManager.html) classes, respectively:

    ```
    record.Dispose();
    manager.Dispose();
    ```

    <a name="get"></a>
## Retrieving Todos

To retrieve a single todo:

1.  Retrieve a todo record using the `Get()` method of the [Tizen.Pims.Calendar.CalendarRecord](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Pims.Calendar.CalendarRecord.html) class with the todo ID as the second parameter:

    ```
    var manager = new CalendarManager();
    var record = manager.Database.Get(CalendarViews.Todo.Uri, todoId);
    ```

2. When no longer needed, destroy the todo instance and release all its resources using the `Dispose()` method:

    ```
    record.Dispose();
    ```

To retrieve multiple todos:

1.  Retrieve a list of all todos, or retrieve a filtered list of todos:
    -   To retrieve a list of all todos, use the `GetAll()` method of the [Tizen.Pims.Calendar.CalendarDatabase](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Pims.Calendar.CalendarDatabase.html) class:

        ```
        var manager = new CalendarManager();
        var list = manager.Database.GetAll(CalendarViews.Todo.Uri, 0, 0);
        ```

    - To retrieve a filtered list of todos:
        1.  Create a query as an instance of the [Tizen.Pims.Calendar.CalendarQuery](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Pims.Calendar.CalendarQuery.html) class:

            ```
            var query = new CalendarQuery(CalendarViews.Todo.Uri)
            ```

        2. Create a filter using the [Tizen.Pims.Calendar.CalendarFilter](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Pims.Calendar.CalendarFilter.html) class and adding conditions.

            The following example adds a string-based filtering condition that retrieves the todos whose summary field contains the string "summary to find":

            ```
            var filter = new CalendarFilter(CalendarViews.Todo.Uri, CalendarViews.Todo.Summary, CalendarFilter.StringMatchType.Contains, "summary to find");
            ```

        3. To add more conditions, define an operator between the conditions.

            The following example adds an AND operator along with a second condition, which is a string-based filtering condition that retrieves the todos whose description field contains the string "description to find".

            The combination of the AND operator and the 2 conditions means that the filter only retrieves the todos that contain "summary to find" in their summary and "description to find" in their description.

            ```
            filter.AddCondition(CalendarFilter.LogicalOperator.And, CalendarViews.Todo.Description, CalendarFilter.StringMatchType.Contains, "description to find");
            ```

            You can also create a filter with integer and time conditions. For example, to filter all completed todos:

            ```
            filter.AddCondition(CalendarFilter.LogicalOperator.And, CalendarViews.Todo.Status, CalendarFilter.IntegerMatchType.Equal, CalendarTypes.TodoStatus.Completed);
            ```

        4. Set the filter to the query using the `SetFilter()` method of the `Tizen.Pims.Calendar.CalendarQuery` class:

            ```
            query.SetFilter(filter);
            ```

        5. Retrieve the filtered list of todos using the `GetRecordsWithQuery()` method of the `Tizen.Pims.Calendar.CalendarDatabase` class:

            ```
            var list = manager.Database.GetRecordsWithQuery(query, 0, 0);
            ```

            The third parameter defines a limit for the number of results. If you set it to 0, the list returns all todos matching the query.

        6. When no longer needed, destroy the filter and query instances and release all their resources using the `Dispose()` methods of the `Tizen.Pims.Calendar.CalendarFilter` and `Tizen.Pims.Calendar.CalendarQuery` classes, respectively:

            ```
            filter.Dispose();
            query.Dispose();
            ```

2. Use a loop to iterate through the list and retrieve the todo details.

    Move forward and backward within the event list using the `MovePrevious()` and `MoveNext()` methods of the [Tizen.Pims.Calendar.CalendarList](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Pims.Calendar.CalendarList.html) class, and retrieve the current event using the `GetCurrentRecord()` method.

    The following example iterates through the list and retrieves the summary of each todo:

    ```
    var manager = new CalendarManager();
    var list = manager.Database.GetAll(CalendarViews.Todo.Uri, 0, 0);
    list.MoveFirst();
    var record;
    while (record = list.GetCurrentRecord())
    {
        string summary = record.Get<string>(CalendarViews.Todo.Summary);
        list.MoveNext();
    }
    ```

3. When no longer needed, destroy the list instance and release all its resources using the `Dispose()` method of the [Tizen.Pims.Calendar.CalendarList](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Pims.Calendar.CalendarList.html) class:

    ```
    list.Dispose();
    ```

    <a name="update"></a>
## Updating a Todo

To update todo details:

1.  Retrieve the todo you want to update using the `Get()` method of the [Tizen.Pims.Calendar.CalendarManager](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Pims.Calendar.CalendarManager.html) class with the todo ID as the second parameter:

    ```
    var manager = new CalendarManager();
    var record = manager.Database.Get(CalendarViews.Todo.Uri, todoId);
    ```

    You can also retrieve the todo using the `GetRecordsWithQuery()` method.

2. Set the properties you want to update.

    The following example sets a new subject and description for the todo:

    ```
    record.Set<string>(CalendarViews.Todo.Summary, "Updated Summary");
    record.Set<string>(CalendarViews.Todo.Description, "Updated Description");
    ```

3. Update the todo using the `Update()` method:

    ```
    manager.Database.Update(record);
    ```

4. When no longer needed, destroy the todo and database manager instances and release all their resources using the `Dispose()` methods of the [Tizen.Pims.Calendar.CalendarRecord](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Pims.Calendar.CalendarRecord.html) and `Tizen.Pims.Calendar.CalendarManager` classes, respectively:

    ```
    record.Dispose();
    manager.Dispose();
    ```

    <a name="delete"></a>
## Deleting a Todo

To delete a todo, use the `Delete()` method of the [Tizen.Pims.Calendar.CalendarManager](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Pims.Calendar.CalendarManager.html) class, with the todo ID as the second parameter:

```
var manager = new CalendarManager();
manager.Database.Delete(CalendarViews.Todo.Uir, todoId);
```

<a name="monitor"></a>
## Monitoring Todo Changes

To receive a notification whenever a todo changes:

1.  Register an event handler using the `AddDBChangedDelegate()` method of the [Tizen.Pims.Calendar.CalendarDatabase](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Pims.Calendar.CalendarDatabase.html) class:

    ```
    var manager = new CalendarManager();
    manager.Database.AddDBChangedDelegate(CalendarViews.Todo.Uri, DBChangedHandler);
    ```

2. Define the event handler:

    ```
    static void DBChangedHandler(object sender, DBChangedEventArgs args)
    {
        /// Do something
    }
    ```

    <a name="make"></a>
## Creating a vCalendar

To create a vCalendar stream from an event:

1.  Retrieve the event:

    ```
    var manager = new CalendarManager();
    var record = manager.Get(CalendarViews.Event.Uri, eventId);
    ```

2. Create a vCalendar stream from the event:

    ```
    var list = new CalendarList();
    list.AddRecord(record);

    string stream = CalendarVcalendar.Compose(list);
    ```

3. When no longer needed, destroy the list instance and release all its resources:

    ```
    list.Dispose();
    ```

    <a name="parse"></a>
## Parsing a vCalendar

To parse a vCalendar from a file and insert its content into the calendar database:

1.  Parse the vCalendar stream using the `Parse()` method of the [Tizen.Pims.Calendar.CalendarVcalendar](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Pims.Calendar.CalendarVcalendar.html) class:

    ```
    string stream = "BEGIN:VCALENDAR\r\n"
                    + "VERSION:1.0\r\n"
                    + "BEGIN:VEVENT\r\n"
                    + "SUMMARY:test1\r\n"
                    + "DTSTART:20140721T000000Z\r\n"
                    + "DTEND:20140721T010000Z\r\n"
                    + "AALARM;TYPE=WAVE;VALUE=CONTENT-ID:19960903T060000;PT15M;4;\r\n"
                    + "DALARM:19960415T235000;PT5M;2;Your Taxes Are Due !!!\r\n"
                    + "MALARM:;TYPE=WAVE;VALUE=URL:19960415T235959; ; ; file:///mmedia/taps.wav\r\n"
                    + "END:VEVENT\r\n"
                    + "END:VCALENDAR\r\n";

    var list = CalendarVcalendar.Parse(stream);
    ```

2. Iterate through the list of found records, and retrieve record details.

    The vCalendar stream can contain multiple events or todos.

    ```
    list.MoveFirst();
    var record;
    while (record = list.GetCurrentRecord())
    {
        string summary = record.Get<string>(CalendarViews.Todo.Summary);
        list.MoveNext();
    }
    ```


## Related Information
* Dependencies
  -   Tizen 4.0 and Higher
