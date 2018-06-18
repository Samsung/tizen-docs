# Calendar

You can manage your schedule and tasks in calendars. A calendar is a collection of events or tasks, depending on the calendar type. Each event or task has a series of attributes, such as purpose, starting time, and duration.

This feature is supported in mobile and wearable applications only.

The main features of the Calendar API include:

- Calendar management   

  You can [create a new calendar](#creating-a-calendar) using the `addCalendar()` method of the `CalendarManager` interface (in [mobile](../../api/latest/device_api/mobile/tizen/calendar.html#CalendarManager) and [wearable](../../api/latest/device_api/wearable/tizen/calendar.html#CalendarManager) applications) (you also need the Account API (in [mobile](../../api/latest/device_api/mobile/tizen/account.html) and [wearable](../../api/latest/device_api/wearable/tizen/account.html) applications)).

- Calendar item management   

  You can manage calendar items (add a new [event](#adding-events-to-a-calendar) or [task](#adding-tasks-to-a-calendar) to a calendar, or manage a single calendar [event](#managing-a-single-event) or [task](#managing-a-single-task)) by using the applicable methods of the `Calendar` interface (in [mobile](../../api/latest/device_api/mobile/tizen/calendar.html#Calendar) and [wearable](../../api/latest/device_api/wearable/tizen/calendar.html#Calendar) applications). You can also delete or [update a single instance of a recurring event](#updating-recurring-events).

  When creating an important event or task, such as a monthly meeting or a task of paying a utility bill, you can set an alarm for it by using the `CalendarAlarm` interface (in [mobile](../../api/latest/device_api/mobile/tizen/calendar.html#CalendarAlarm) and [wearable](../../api/latest/device_api/wearable/tizen/calendar.html#CalendarAlarm) applications). The alarm is triggered at a defined time to remind the user of the event or task.

  You can create multiple [events](#adding-events-to-a-calendar-in-the-batch-mode) or [tasks](#adding-tasks-to-a-calendar-in-the-batch-mode), and manage multiple calendar [events](#managing-multiple-events-in-the-batch-mode) or [tasks](#managing-multiple-tasks-in-the-batch-mode) simultaneously by using the applicable batch methods. The batch mode provides faster, optimized processing of multiple calendar items.

  > **Note**  
  > The batch mode does not provide progress information about operations. To ensure that you can view the progress, break the batch operation down into multiple smaller batch operations. For example, break down a batch of 100 update requests into 10 batch operations that update 10 records at a time. Breaking down a batch operation also helps you avoid blocking other database operations, such as add or remove.

- iCalendar 2.0 format conversions

  You can convert a calendar [event](#converting-event-formats) or [task](#converting-task-formats) to the iCalendar format and back.

- Calendar change notifications   

  You can keep the calendar in your application synchronized with user-specific calendars, such as a calendar on a social networking Web site, by [receiving notifications](#receiving-notifications-on-calendar-changes) in your application when calendar items change.

The Calendar API uses the `TZDate` object (in [mobile](../../api/latest/device_api/mobile/tizen/time.html#TZDate) and [wearable](../../api/latest/device_api/wearable/tizen/time.html#TZDate) applications) of the Time API (in [mobile](../../api/latest/device_api/mobile/tizen/time.html) and [wearable](../../api/latest/device_api/wearable/tizen/time.html) applications) and not the standard JavaScript `Date` object to handle difficult issues related to the time zone, because the `TZDate` object handles exact time and provides various utility methods.

## Prerequisites

To enable your application to use the calendar functionality:

1. To make your application visible in the Tizen Store only for devices that support the calendar feature, the application must specify the following feature in the `config.xml` file:

   ```
   <widget>
      <tizen:feature name="http://tizen.org/feature/calendar"/>
   </widget>
   ```

   Additionally, to double-check the Calendar API support (in [mobile](../../api/latest/device_api/mobile/tizen/calendar.html) and [wearable](../../api/latest/device_api/wearable/tizen/calendar.html) applications) while the application is running, use the `tizen.systeminfo.getCapability()` method and enable or disable the code that needs the API, as needed.

2. To use the Calendar API, the application has to request permission by adding the following privileges to the `config.xml` file:

   ```
   <tizen:privilege name="http://tizen.org/privilege/calendar.read"/>
   <tizen:privilege name="http://tizen.org/privilege/calendar.write"/>
   ```

## Creating a Calendar

> **Note**  
> The created calendar is associated with a specified account. Therefore, you must retrieve the account before creating a new calendar.

To create a new calendar:

1. Declare a variable to store the created calendar:

   ```
   var myCalendar = null;
   ```

2. Define a success callback for the `getAccounts()` method. The callback receives a list of `Account` objects (in [mobile](../../api/latest/device_api/mobile/tizen/account.html#Account) and [wearable](../../api/latest/device_api/wearable/tizen/account.html#Account) applications). Use the first account ID to construct a new `Calendar` object (in [mobile](../../api/latest/device_api/mobile/tizen/calendar.html#Calendar) and [wearable](../../api/latest/device_api/wearable/tizen/calendar.html#Calendar) applications).  
   Add the new calendar to the system using the `addCalendar()` method of the `CalendarManager` interface (in [mobile](../../api/latest/device_api/mobile/tizen/calendar.html#CalendarManager) and [wearable](../../api/latest/device_api/wearable/tizen/calendar.html#CalendarManager) applications):

   ```
   function getAccountsSuccess(accounts) {
       var account = accounts[0];
       if (account) {
           /* New calendar can be created and added */
           myCalendar = new tizen.Calendar(account.id, 'remote calendar', 'TASK');
           tizen.calendar.addCalendar(myCalendar);
           console.log('New calendar created with ID=' + myCalendar.id);
       }
   }
   ```

3. To retrieve available accounts, use the `getAccounts()` method. The following method call invokes the `getAccountsSuccess` event handler defined above:

   ```
   tizen.account.getAccounts(getAccountsSuccess, function(err));
   ```

## Retrieving a Calendar

You must retrieve the calendar object of the applicable type from the applicable calendar to access an existing calendar item.

To access the device calendars and retrieve calendar objects:

- To retrieve the default calendar, use the `getDefaultCalendar()` method of the `CalendarManager` interface (in [mobile](../../api/latest/device_api/mobile/tizen/calendar.html#CalendarManager) and [wearable](../../api/latest/device_api/wearable/tizen/calendar.html#CalendarManager) applications).  
  The following example retrieves the event-type default calendar:

  ```
  tizen.calendar.getDefaultCalendar('EVENT');
  ```

- To retrieve all the available calendars as an array, use the `getCalendars()` method.  
  The following example retrieves all event-type calendars:

  ```
  tizen.calendar.getCalendars('EVENT', calendarListCallback, errorCallback);
  ```

- To retrieve a special calendar, which combines events (or tasks) from all calendars of the same type, use the `getUnifiedCalendar()` method of the `CalendarManager` interface.  
   The following example retrieves a unified event-type calendar:

  ```
  tizen.calendar.getUnifiedCalendar('EVENT');
  ```

## Events

The events are identified using the `CalendarEventId`, which is a `CalendarItemId` typedef (in [mobile](../../api/latest/device_api/mobile/tizen/calendar.html#CalendarItemId) and [wearable](../../api/latest/device_api/wearable/tizen/calendar.html#CalendarItemId) applications). In recurring events, the `CalendarEventId` contains a recurrence ID (`rid`) in addition to the actual event ID, to separately identify each occurrence of the recurring event.

> **Note**  
> Depending on the time zone and daylight saving time, an event for "today" can actually occur in the past or in the future.

Using the `CalendarEvent` object (in [mobile](../../api/latest/device_api/mobile/tizen/calendar.html#CalendarEvent) and [wearable](../../api/latest/device_api/wearable/tizen/calendar.html#CalendarEvent) applications), you can:

- Add events to a calendar one by one or in a batch mode.
- Update or delete events one by one or in a batch mode.
- Update recurring events.
- Convert events to the iCalendar format and back.

### Adding Events to a Calendar

To add events to a calendar:

1. Retrieve the default system calendar using the `getDefaultCalendar()` method of the `CalendarManager` interface (in [mobile](../../api/latest/device_api/mobile/tizen/calendar.html#CalendarManager) and [wearable](../../api/latest/device_api/wearable/tizen/calendar.html#CalendarManager) applications).

   With the parameter, specify the calendar type as an event.

   ```
   var calendar = tizen.calendar.getDefaultCalendar('EVENT');
   ```

2. Create a `CalendarEvent` object (in [mobile](../../api/latest/device_api/mobile/tizen/calendar.html#CalendarEvent) and [wearable](../../api/latest/device_api/wearable/tizen/calendar.html#CalendarEvent) applications) and define the event properties:

   ```
   var ev = new tizen.CalendarEvent({
       description:'HTML5 Introduction',
       summary:'HTML5 Webinar',
       startDate: new tizen.TZDate(2011, 3, 30, 10, 0),
       duration: new tizen.TimeDuration(1, 'HOURS'),
       location:'Huesca',
   ```

3. To make a recurring event, define a recurrence rule.

   In this example, the event repeats once a day for 3 days.

   ```
       recurrenceRule: new tizen.CalendarRecurrenceRule('DAILY', {occurrenceCount: 3})
   });
   ```

4. To set up an alarm to remind the user about the event, create an alarm with the `CalendarAlarm` interface (in [mobile](../../api/latest/device_api/mobile/tizen/calendar.html#CalendarAlarm) and [wearable](../../api/latest/device_api/wearable/tizen/calendar.html#CalendarAlarm) applications), and add the alarm to the event:

   ```
   /* Alarm is triggered with sound 30 minutes before the event start time */
   var alarm = new tizen.CalendarAlarm(new tizen.TimeDuration(30, 'MINS'), 'SOUND');

   ev.alarms = [alarm];
   ```

5. Add the `CalendarEvent` object to the default calendar with the `add()` method of the `Calendar` object (in [mobile](../../api/latest/device_api/mobile/tizen/calendar.html#Calendar) and [wearable](../../api/latest/device_api/wearable/tizen/calendar.html#Calendar) applications).

   ```
   calendar.add(ev); /* ev.id attribute is generated */
   ```

### Adding Events to a Calendar in the Batch Mode

You can create multiple events simultaneously by using the `addBatch()` method.

To add events to a calendar in the batch mode:

1. Retrieve the default system calendar using the `getDefaultCalendar()` method of the `CalendarManager` interface (in [mobile](../../api/latest/device_api/mobile/tizen/calendar.html#CalendarManager) and [wearable](../../api/latest/device_api/wearable/tizen/calendar.html#CalendarManager) applications):

   ```
   var calendar = tizen.calendar.getDefaultCalendar('EVENT');
   ```

2. Define the items to be added as an array:

   ```
   var ev = new tizen.CalendarEvent({
       description:'HTML5 Introduction',
       summary:'HTML5 Webinar',
       startDate: new tizen.TZDate(2011, 3, 30, 10, 0),
       duration: new tizen.TimeDuration(1, 'HOURS'),
       location:'Huesca'
   });
   ```

   > **Note**  
   > To keep the example as simple as possible, the array above includes only 1 event.

3. Use the `addBatch()` method of the `Calendar` object (in [mobile](../../api/latest/device_api/mobile/tizen/calendar.html#Calendar) and [wearable](../../api/latest/device_api/wearable/tizen/calendar.html#Calendar) applications) to add the events in the array to the calendar:

   ```
   calendar.addBatch([ev]);
   ```

   > **Note**  
   > The `addBatch()` method is asynchronous, and its callbacks must be used to react to the success or failure of the operation.

### Managing a Single Event

To manage a single event:

1. Retrieve the default system calendar using the `getDefaultCalendar()` method of the `CalendarManager` interface (in [mobile](../../api/latest/device_api/mobile/tizen/calendar.html#CalendarManager) and [wearable](../../api/latest/device_api/wearable/tizen/calendar.html#CalendarManager) applications).

   With the parameter, specify the calendar type as event.

   ```
   var myCalendar = tizen.calendar.getDefaultCalendar('EVENT');
   ```

2. Retrieve all events stored in the calendar by using the `find()` method of the `Calendar` object (in [mobile](../../api/latest/device_api/mobile/tizen/calendar.html#Calendar) and [wearable](../../api/latest/device_api/wearable/tizen/calendar.html#Calendar) applications):

   ```
   myCalendar.find(eventSearchSuccessCallback);
   ```

   When searching for calendar items, you can create [attribute filters](../data/data-filter.md#creating-attribute-filters), [attribute range filters](../data/data-filter.md#creating-attribute-range-filters), and [composite filters](../data/data-filter.md#creating-composite-filters) based on [specific filter attributes](../data/data-filter.md#calendar-filter-attributes). You can also [sort the search results](../data/data-filter.md#using-sorting-modes). In this example, all the events are retrieved because no filter is used.

3. Update or delete the found item inside the `eventSearchSuccessCallback()` event handler.

   In this example, the description parameter of the first event is changed and the event is updated in the calendar using the `update()` method. The second event is deleted using the `remove()` method.

   ```
   /* Define the event success callback */
   function eventSearchSuccessCallback(events) {
       /* Update the first existing event */
       events[0].description = 'New Description';
       myCalendar.update(events[0]);

       /* Delete the second existing event */
       myCalendar.remove(events[1].id);
   }
   ```

### Updating Recurring Events

If you need to delete or update a single instance of a recurring event, get the list of event instances first with the `expandRecurrence()` method of the `CalendarEvent` object (in [mobile](../../api/latest/device_api/mobile/tizen/calendar.html#CalendarEvent) and [wearable](../../api/latest/device_api/mobile/tizen/calendar.html#CalendarEvent) applications). Then, delete the applicable event instance, or update it by calling the `update()` method with the `updateAllInstances` parameter set to `false`.

To update recurring events:

1. Retrieve the default system calendar using the `getDefaultCalendar()` method of the `CalendarManager` interface (in [mobile](../../api/latest/device_api/mobile/tizen/calendar.html#CalendarManager) and [wearable](../../api/latest/device_api/wearable/tizen/calendar.html#CalendarManager) applications).

   Retrieve the event using the `get()` method by specifying the event ID.

   ```
   var calendar = tizen.calendar.getDefaultCalendar('EVENT');
   var event = calendar.get(evId);
   ```

2. Expand the recurring event to get its instances by using the `expandRecurrence()` method of the `CalendarEvent` object:

   ```
   event.expandRecurrence(new tizen.TZDate(2012, 2, 1), new tizen.TZDate(2012, 2, 15),
                          eventExpandSuccessCB);
   ```

   The expanded event instances have their own `id.uid` and `id.rid` attributes, where the `id.uid` attribute is the same for all instances.

3. Update a single instance of the expanded recurring event.

   For recurring events, you can use the second parameter of the `update()` method to determine whether a single instance or all occurrences of the event are updated. If the parameter is set to `true`, all instances are updated, while if it is set to `false`, only the indicated instance of the recurring event is updated (based on the `id.rid` attribute).

   In this example, the second instance of the event is updated.

   ```
   /* Success event handler */
   function eventExpandSuccessCB(events) {
       events[1].summary = 'updated summary';
       calendar.update(events[1], false);
   }
   ```

### Managing Multiple Events in the Batch Mode

You can manage multiple events simultaneously by using the applicable batch methods: `updateBatch()` and `removeBatch()`.

To manage multiple events in the batch mode:

1. Retrieve the default system calendar using the `getDefaultCalendar()` method of the `CalendarManager` interface (in [mobile](../../api/latest/device_api/mobile/tizen/calendar.html#CalendarManager) and [wearable](../../api/latest/device_api/wearable/tizen/calendar.html#CalendarManager) applications).

   With the parameter, specify the calendar type as event.

   ```
   var myCalendar = tizen.calendar.getDefaultCalendar('EVENT');
   ```

2. Retrieve all events stored in the calendar by using the `find()` method of the `Calendar` object (in [mobile](../../api/latest/device_api/mobile/tizen/calendar.html#Calendar) and [wearable](../../api/latest/device_api/wearable/tizen/calendar.html#Calendar) applications):

   ```
   myCalendar.find(eventSearchSuccessCallback, errorCallback);
   ```

   When searching for calendar items, you can create [attribute filters](../data/data-filter.md#creating-attribute-filters), [attribute range filters](../data/data-filter.md#creating-attribute-range-filters), and [composite filters](../data/data-filter.md#creating-composite-filters) based on [specific filter attributes](../data/data-filter.md#calendar-filter-attributes). You can also [sort the search results](../data/data-filter.md#using-sorting-modes). In this example, all the events are retrieved because no filter is used.

3. To update events:      

   1. Define the items to be updated in the success event handler of the `find()` method:

      ```
      function eventSearchSuccessCallback(events) {
          events[0].description = 'New Description 1';
          events[1].description = 'New Description 2';
      ```

   2. Use the `updateBatch()` method to update multiple calendar items asynchronously:

      ```
          /* Update the first 2 existing events */
          myCalendar.updateBatch(events.slice(0, 2));
      }
      ```

4. To delete events, use the `removeBatch()` method in the success event handler of the `find()` method to delete multiple calendar items asynchronously:

   ```
   function eventSearchSuccessCallback(events) {
       /* Delete the first 2 existing events */
       myCalendar.removeBatch([events[0].id, events[1].id]);
   }
   ```

### Converting Event Formats

You can make event exchange more efficient in your application by converting an event to the iCalendar format (or back) using the `CalendarEvent` object (in [mobile](../../api/latest/device_api/mobile/tizen/calendar.html#CalendarEvent) and [wearable](../../api/latest/device_api/wearable/tizen/calendar.html#CalendarEvent) applications) constructor and the `convertToString()` method of the `CalendarItem` interface (in [mobile](../../api/latest/device_api/mobile/tizen/calendar.html#CalendarItem) and [wearable](../../api/latest/device_api/wearable/tizen/calendar.html#CalendarItem) applications).

The conversion allows you to exchange calendar data between applications by sharing files with the `.ics` extension. The iCalendar format is independent of the underlying transport protocol, meaning that calendar items can be exchanged using a variety of transports, including HTTP, SMTP, and infrared. The iCalendar format can be used to store calendar item information and exchange calendar data over the Internet.

The following example shows a sample event in iCalendar format:

```
BEGIN:VCALENDAR
BEGIN:VEVENT
DTSTART:20110714T150000Z
DTEND:20110715T173000Z
SUMMARY:Prepare team meeting
END:VEVENT
END:VCALENDAR
```

To convert the events to iCalendar format and back:

- To convert an iCalendar string to an event:    

  1. Retrieve the default system calendar using the `getDefaultCalendar()` method of the `CalendarManager` interface (in [mobile](../../api/latest/device_api/mobile/tizen/calendar.html#CalendarManager) and [wearable](../../api/latest/device_api/wearable/tizen/calendar.html#CalendarManager) applications).

     With the parameter, specify the calendar type as event.

     ```
     var calendar = tizen.calendar.getDefaultCalendar('EVENT');
     ```

  2. Create a new `CalendarEvent` object from the iCalendar string and add it to the default calendar:

     ```
     try {
         var ev = new tizen.CalendarEvent('BEGIN:VCALENDAR\r\n' +
                                          'BEGIN:VEVENT\r\n' +
                                          'DTSTAMP:19970901T1300Z\r\n' +
                                          'DTSTART:19970903T163000Z\r\n' +
                                          'DTEND:19970903T190000Z\r\n' +
                                          'SUMMARY:Tizen, Annual Employee Review\r\n' +
                                          'CATEGORIES:BUSINESS,HUMAN RESOURCES\r\n' +
                                          'END:VEVENT\r\n' +
                                          'END:VCALENDAR', 'ICALENDAR_20');

         calendar.add(ev);
         console.log('Event added with UID ' + ev.id.uid);
     }
     ```

  To convert multiple strings and import them to a calendar, convert the strings one by one and then use the `addBatch()` method to [add all the events at once in a batch mode](#adding-events-to-a-calendar-in-the-batch-mode).

- To convert an event to the iCalendar format:    

  1. Get the default calendar and find all events which include the "Tizen" string in the `Summary` attribute:

     ```
     var myCalendar;

     myCalendar = tizen.calendar.getDefaultCalendar('EVENT');

     /* Define a filter */
     var filter = new tizen.AttributeFilter('summary', 'CONTAINS', 'Tizen');

     /* Search for the events */
     myCalendar.find(eventSearchSuccessCallback, errorCallback, filter);
     ```

  2. Convert an event to an iCalendar string in the success event handler of the `find()` method using the `convertToString()` method:

     ```
     function eventSearchSuccessCallback(events) {
         /* Convert the first event */
         var vevent = events[0].convertToString('ICALENDAR_20');
     }
     ```

  To export and convert multiple events from a calendar, find the required events using the `find()` method with an applicable filter, and then convert the found events one by one.

## Tasks

The tasks are identified using the `CalendarTaskId`, which is a `CalendarItemId` typedef (in [mobile](../../api/latest/device_api/mobile/tizen/calendar.html#CalendarItemId) and [wearable](../../api/latest/device_api/wearable/tizen/calendar.html#CalendarItemId) applications).

Using the `CalendarTask` object (in [mobile](../../api/latest/device_api/mobile/tizen/calendar.html#CalendarTask) and [wearable](../../api/latest/device_api/wearable/tizen/calendar.html#CalendarTask) applications), you can:

- Add tasks to a calendar one by one or in a batch mode.
- Update or delete tasks one by one or in a batch mode.
- Convert tasks to the iCalendar format and back.

### Adding Tasks to a Calendar

To add tasks to a calendar:

1. Retrieve the default system calendar using the `getDefaultCalendar()` method of the `CalendarManager` interface (in [mobile](../../api/latest/device_api/mobile/tizen/calendar.html#CalendarManager) and [wearable](../../api/latest/device_api/wearable/tizen/calendar.html#CalendarManager) applications).

   With the parameter, specify the calendar type as task.

   ```
   var calendar = tizen.calendar.getDefaultCalendar('TASK');
   ```

2. Create a `CalendarTask` object (in [mobile](../../api/latest/device_api/mobile/tizen/calendar.html#CalendarTask) and [wearable](../../api/latest/device_api/wearable/tizen/calendar.html#CalendarTask) applications) and define the task properties:

   ```
   var task = new tizen.CalendarTask({
       description:'HTML5 Introduction',
       summary:'HTML5 Webinar',
       startDate: new tizen.TZDate(2011, 3, 10, 10, 0),
       dueDate: new tizen.TZDate(2011, 3, 30, 10, 0),
       completedDate: new tizen.TZDate(2011, 3, 20, 10, 0),
       location:'Huesca'
   });
   ```

3. To set up an alarm to remind the user about the task, create an alarm with the `CalendarAlarm` interface (in [mobile](../../api/latest/device_api/mobile/tizen/calendar.html#CalendarAlarm) and [wearable](../../api/latest/device_api/wearable/tizen/calendar.html#CalendarAlarm) applications), and add the alarm to the task:

   ```
   /* Alarm is triggered with sound 30 minutes before the task start time */
   var alarm = new tizen.CalendarAlarm(new tizen.TimeDuration(30, 'MINS'), 'SOUND');

   task.alarms = [alarm];
   ```

4. Add the `CalendarTask` object to the default calendar with the `add()` method of the `Calendar` object (in [mobile](../../api/latest/device_api/mobile/tizen/calendar.html#Calendar) and [wearable](../../api/latest/device_api/wearable/tizen/calendar.html#Calendar) applications):

   ```
   calendar.add(task); /* task.id attribute is generated */
   ```

### Adding Tasks to a Calendar in the Batch Mode

You can create multiple tasks simultaneously by using the `addBatch()` method.

To add tasks to a calendar in the batch mode:

1. Retrieve the default system calendar using the `getDefaultCalendar()` method of the `CalendarManager` interface (in [mobile](../../api/latest/device_api/mobile/tizen/calendar.html#CalendarManager) and [wearable](../../api/latest/device_api/wearable/tizen/calendar.html#CalendarManager) applications):

   ```
   var calendar = tizen.calendar.getDefaultCalendar('TASK');
   ```

2. Define the items to be added as an array:

   ```
   var task = new tizen.CalendarTask({
       description:'HTML5 Introduction',
       summary:'HTML5 Webinar',
       startDate: new tizen.TZDate(2011, 3, 30, 10, 0),
       dueDate: new tizen.TZDate(2011, 5, 30, 10, 0),
       completedDate: new tizen.TZDate(2011, 4, 30, 10, 0),
       location:'Huesca'
   });
   ```

   > **Note**  
   > To keep the example as simple as possible, the array above includes only 1 task.

3. Use the `addBatch()` method of the `Calendar` object (in [mobile](../../api/latest/device_api/mobile/tizen/calendar.html#Calendar) and [wearable](../../api/latest/device_api/wearable/tizen/calendar.html#Calendar) applications) to add the tasks in the array to the calendar:

   ```
   calendar.addBatch([task]);
   ```

   > **Note**  
   > The `addBatch()` method is asynchronous, and its callbacks must be used if you want to react to the success or failure of the operation.

### Managing a Single Task

To manage a single task:

1. Retrieve the default system calendar using the `getDefaultCalendar()` method of the `CalendarManager` interface (in [mobile](../../api/latest/device_api/mobile/tizen/calendar.html#CalendarManager) and [wearable](../../api/latest/device_api/wearable/tizen/calendar.html#CalendarManager) applications).

   With the parameter, specify the calendar type as task.

   ```
   var myCalendar = tizen.calendar.getDefaultCalendar('TASK');
   ```

2. Retrieve all tasks stored in the calendar by using the `find()` method of the `Calendar` object (in [mobile](../../api/latest/device_api/mobile/tizen/calendar.html#Calendar) and [wearable](../../api/latest/device_api/wearable/tizen/calendar.html#Calendar) applications):

   ```
   myCalendar.find(taskSearchSuccessCallback);
   ```

   When searching for calendar items, you can create [attribute filters](../data/data-filter.md#creating-attribute-filters), [attribute range filters](../data/data-filter.md#creating-attribute-range-filters), and [composite filters](../data/data-filter.md#creating-composite-filters) based on [specific filter attributes](../data/data-filter.md#calendar-filter-attributes). You can also [sort the search results](../data/data-filter.md#using-sorting-modes). In this example, all the events are retrieved because no filter is used.

3. Update or delete the found item inside the `taskSearchSuccessCallback()` event handler.

   In this example, the description parameter of the first task is changed and the task is updated in the calendar using the `update()` method. The second task is deleted using the `remove()` method.

   ```
   /* Define the event success callback */
   function taskSearchSuccessCallback(tasks) {
       /* Update the first existing task */
       tasks[0].description = 'New Description';
       myCalendar.update(tasks[0]);

       /* Delete the second existing task */
       myCalendar.remove(tasks[1].id);
   }
   ```

### Managing Multiple Tasks in the Batch Mode

You can manage multiple tasks simultaneously by using the applicable batch methods: `updateBatch()` and `removeBatch()`.

To manage multiple tasks in the batch mode:

1. Retrieve the default system calendar using the `getDefaultCalendar()` method of the `CalendarManager` interface (in [mobile](../../api/latest/device_api/mobile/tizen/calendar.html#CalendarManager) and [wearable](../../api/latest/device_api/wearable/tizen/calendar.html#CalendarManager) applications).

   With the parameter, specify the calendar type as task.

   ```
   var myCalendar = tizen.calendar.getDefaultCalendar('TASK');
   ```

2. Retrieve all tasks stored in the calendar by using the `find()` method of the `Calendar` object (in [mobile](../../api/latest/device_api/mobile/tizen/calendar.html#Calendar) and [wearable](../../api/latest/device_api/wearable/tizen/calendar.html#Calendar) applications):

   ```
   myCalendar.find(taskSearchSuccessCallback);
   ```

   When searching for calendar items, you can create [attribute filters](../data/data-filter.md#creating-attribute-filters), [attribute range filters](../data/data-filter.md#creating-attribute-range-filters), and [composite filters](../data/data-filter.md#creating-composite-filters) based on [specific filter attributes](../data/data-filter.md#calendar-filter-attributes). You can also [sort the search results](../data/data-filter.md#using-sorting-modes). In this example, all the events are retrieved because no filter is used.

3. To update tasks:      

   1. Define the items to be updated in the success event handler of the `find()` method:

      ```
      function taskSearchSuccessCallback(tasks) {
          tasks[0].description = 'New Description 1';
          tasks[1].description = 'New Description 2';
      ```

   2. Use the `updateBatch()` method to update multiple calendar items asynchronously:

      ```
          /* Update the first 2 existing tasks */
          myCalendar.updateBatch(tasks.slice(0, 2));
      }
      ```

4. To delete tasks, use the `removeBatch()` method in the success event handler of the `find()` method to delete multiple calendar items asynchronously:

   ```
   function taskSearchSuccessCallback(tasks) {
       /* Delete the first 2 existing tasks */
       myCalendar.removeBatch([tasks[0].id, tasks[1].id]);
   }
   ```

### Converting Task Formats

You can make task exchange more efficient in your application by converting a task to the iCalendar format (or back) using the `CalendarTask` object constructor (in [mobile](../../api/latest/device_api/mobile/tizen/calendar.html#CalendarTask) and [wearable](../../api/latest/device_api/wearable/tizen/calendar.html#CalendarTask) applications) and the `convertToString()` method of the `CalendarItem` interface (in [mobile](../../api/latest/device_api/mobile/tizen/calendar.html#CalendarItem) and [wearable](../../api/latest/device_api/wearable/tizen/calendar.html#CalendarItem) applications).

The conversion allows you to exchange calendar data between applications by sharing files with the `.ics` extension. The iCalendar format is independent of the underlying transport protocol, meaning that calendar items can be exchanged using a variety of transports, including HTTP, SMTP, and Infrared. The iCalendar format can be used to store calendar item information and exchange calendar data over the Internet.

The following example shows a sample task in iCalendar format:

```
BEGIN:VCALENDAR
BEGIN:VTODO
DTSTAMP:TZID=CET:20110902T110000Z
DTSTART:TZID=CET:20110906T140000Z
DUE:TZID=CET:20110906T150000Z
SUMMARY:Prepare team meeting
END:VTODO
END:VCALENDAR
```

To convert the task to iCalendar format and back:

- To convert an iCalendar string to a task:    

  1. Retrieve the default system calendar using the `getDefaultCalendar()` method of the `CalendarManager` interface (in [mobile](../../api/latest/device_api/mobile/tizen/calendar.html#CalendarManager) and [wearable](../../api/latest/device_api/wearable/tizen/calendar.html#CalendarManager) applications).

     With the parameter, specify the calendar type as task.

     ```
     var calendar = tizen.calendar.getDefaultCalendar('TASK');
     ```

  2. Create a new `CalendarTask` object from the iCalendar string and add it to the default calendar:

     ```
     var task = new tizen.CalendarTask('BEGIN:VCALENDAR\r\n' +
                                       'VERSION:2.0\r\n' +
                                       'BEGIN:VTODO\r\n' +
                                       'DTSTAMP:TZID=CET:20110902T110000Z\r\n' +
                                       'DTSTART:TZID=CET:20110906T140000Z\r\n' +
                                       'DUE:TZID=CET:20110906T150000Z\r\n' +
                                       'SUMMARY:Tizen, discuss the schedule\r\n' +
                                       'DESCRIPTION:Find the feasible schedule\r\n' +
                                       'CATEGORIES:HUMAN RESOURCES\r\n' +
                                       'END:VTODO\r\n' +
                                       'END:VCALENDAR', 'ICALENDAR_20');

     calendar.add(task);
     console.log('Task added with id ' + task.id);
     ```

  To convert multiple strings and import them to a calendar, convert the strings one by one and then use the `addBatch()` method to [add all the tasks at once in a batch mode](#adding-tasks-to-a-calendar-in-the-batch-mode).

- To convert a task to the iCalendar format:    

  1. Get the default calendar and find all calendar items which include the "Tizen" string in the `Summary` attribute:

     ```
     var myCalendar;

     myCalendar = tizen.calendar.getDefaultCalendar('TASK');

     /* Define a filter */
     var filter = new tizen.AttributeFilter('summary', 'CONTAINS', 'Tizen');

     /* Search for the tasks */
     myCalendar.find(taskSearchSuccessCallback, null, filter);
     ```

  2. Convert a calendar item to an iCalendar string in the success event handler of the `find()` method using the `convertToString()` method:

     ```
     function taskSearchSuccessCallback(tasks) {
         /* Convert the first task */
         var vtodo = tasks[0].convertToString('ICALENDAR_20');
     }
     ```

  To export and convert multiple tasks from a calendar, find the required tasks using the `find()` method with an applicable filter, and then convert the found tasks one by one.

## Receiving Notifications on Calendar Changes

You can keep the calendar in your application synchronized with user-specific calendars by receiving notifications in your application when calendar items are added, updated, or deleted. Every change made to the calendar database triggers an event for which you can define a notification. For batch mode operations, each operation generates only a single event. A recurring event is treated as one event.

The `addChangeListener()` method of the `Calendar` interface registers an event listener, which starts asynchronously once the `addChangeListener()` method returns the subscription identifier for the listener. You can use the `CalendarChangeCallback` interface (in [mobile](../../api/latest/device_api/mobile/tizen/calendar.html#CalendarChangeCallback) and [wearable](../../api/latest/device_api/wearable/tizen/calendar.html#CalendarChangeCallback) applications) to define listener event handlers for receiving the notifications.

To receive notifications when calendar items are added, updated, or removed:

1. Define the needed variables:

   ```
   /* Watcher identifier */
   var watcherId = 0;

   /* This example assumes that the calendar is initialized */
   var calendar;
   ```

2. Define the event handlers for different notifications using the `CalendarChangeCallback` listener interface (in [mobile](../../api/latest/device_api/mobile/tizen/calendar.html#CalendarChangeCallback) and [wearable](../../api/latest/device_api/wearable/tizen/calendar.html#CalendarChangeCallback) applications):

   ```
   var watcher = {
       /* When new items are added */
       onitemsadded: function(items) {
           console.log(items.length + ' items were added');
       },

       /* When items are updated */
       onitemsupdated: function(items) {
           console.log(items.length + ' items were updated');
       },

       /* When items are deleted */
       onitemsremoved: function(ids) {
           console.log(ids.length + ' items were removed');
       }
   };
   ```

3. Register the listener to use the defined event handlers:

   ```
   watcherId = calendar.addChangeListener(watcher);
   ```

4. To stop the notifications, use the `removeChangeListener()` method:

   ```
   function cancelWatch() {
       calendar.removeChangeListener(watcherId);
   }
   ```

## Related Information
* Dependencies   
  - Tizen 2.4 and Higher for Mobile
  - Tizen 4.0 and Higher for Wearable
