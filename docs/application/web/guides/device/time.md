# Time and Date Management

You can use locale-specific calendar features by retrieving date and time information. You can also change the date, time, and time zone, and make some date- and time-related calculations. The Time API overcomes several limitations of the JavaScript `Date` object.

The Time API is mandatory for Tizen mobile, wearable, and TV profiles, which means that it is supported on all mobile, wearable, and TV devices. All mandatory APIs are supported on the Tizen Emulators.

Locale refers to the set of information that is specific to a language and a country. It affects the numeric formats (decimal and list separators), date formats, and the character sorting order. It determines how a locale-specific functionality behaves; for example, how numbers are displayed or strings converted to dates.

The main features of the Time API include:

- Managing the current date, time, and time zone   

  You can [retrieve the current date and time](#retrieving-date-and-time) or all available time zones, and check whether a specific year is a leap year.

- Getting the locale-specific date and time formats   

  If locale-specific settings have been made on the device, the date must be displayed in the corresponding locale-specific format. Tizen supports several different date and time formats, and you can [retrieve the currently used formats](#retrieving-the-local-date-and-time-format).

- Performing date- and time-related calculations   

  You can [perform different calculations and comparisons on date and time data](#calculating-date-and-time-information) regardless of the time units used in the compared events.

- Monitoring time and time zone changes   

  You can [retrieve notifications on time changes](#retrieving-time-change-notifications) performed by the user.

## Retrieving Date and Time

With the `TimeUtil` interface (in [mobile](../../api/latest/device_api/mobile/tizen/time.html#TimeUtil), [wearable](../../api/latest/device_api/wearable/tizen/time.html#TimeUtil), and [TV](../../api/latest/device_api/tv/tizen/time.html#TimeUtil) applications), you can retrieve the current date, time, and time zone, and the number of available time zones, and determine whether a year is a leap year.

You can also perform other date-and time-related tasks, such as getting the date of the next and previous daylight saving time transition, converting current time to UTC standard time, and getting the time zone abbreviation.

> **Note**  
> UTC is the primary time standard used by the world to track time. Time zones are created for the world as a positive or negative offset of UTC. For example, the time zone for Iceland is UTC+00:00, and the time zone for India is UTC+05:30.
>
> DST (or summer time) is the practice of clocks being advanced temporarily by a fixed time during the summer to take advantage of more daylight. Typically, this temporary adjustment is one hour. For example, one hour shift ahead in time will cause the last moment of 20:59 to jump to 22:00 instead of 21:00. In this case, the day will have 23 hours. In another scenario, one hour shift back in time will cause the day to have 25 hours.

To handle date and time in your application:

1. To get the current date and time, use the `getCurrentDateTime()` method, which returns a `TZDate` object:

   ```
   var current_dt = tizen.time.getCurrentDateTime();
   console.log('Current time / date is ' + current_dt.toLocaleString());
   ```

2. To handle time zone information:    

   1. To retrieve the current time zone, use the `getLocalTimezone()` method:

      ```
      console.log('The current time zone is ' + tizen.time.getLocalTimezone());
      ```

      The general format of the time zones is "general descriptor/specific descriptor 1/specific descriptor 2/specific descriptor n". For example, "America/Argentina/Buenos_Aires".

   2. To get the number of available time zones, use the `getAvailableTimezones()` method:

      ```
      var tzids = tizen.time.getAvailableTimezones();
      console.log('The device supports ' + tzids.length + ' time zones.');
      ```

3. If you are creating a calendar-based application or accepting a date on an application form, you must validate user input for leap year date value. For example, 29/02/2011 is an invalid user input.

   To determine if the year is a leap year, use the `isLeapYear()` method:

   ```
   var current_dt = tizen.time.getCurrentDateTime();
   var is_leap = tizen.time.isLeapYear(current_dt.getFullYear());
   if (is_leap)
      console.log('This year is a leap year.');
   ```

    The `getFullYear()` method returns the year (4 digits) of the `TZDate` object.

## Retrieving the Local Date and Time Format

The date and time can be expressed, for example, in a numerical format YYYY-MM-DD hh:mm:ss (for example, "1996-10-23 16:08:27") or in hybrid format (for example, "Wednesday, October 23, 1996, 04:08:27 PM").

To handle date and time formats in your application:

1. To check the date format, use the `getDateFormat()` method:

   ```
   var dateFormat = tizen.time.getDateFormat();
   console.log('Date format is ' + dateFormat);
   ```

2. To check the time format, use the `getTimeFormat()` method:

   ```
   var timeFormat = tizen.time.getTimeFormat();
   console.log('Time format is ' + timeFormat);
   ```

## Calculating Date and Time Information

Calculate and compare time and date information using the applicable methods of the `TimeDuration` interface (in [mobile](../../api/latest/device_api/mobile/tizen/time.html#TimeDuration), [wearable](../../api/latest/device_api/wearable/tizen/time.html#TimeDuration), and [TV](../../api/latest/device_api/tv/tizen/time.html#TimeDuration) applications):

1. To calculate the duration difference between 2 date or time events, use the `difference()` method of the `TimeDuration` object:

   ```
   var event1, event2; /* Assume that those are correct tizen.CalendarEvent objects */
   /* Calculate event1.duration - event2.duration */
   var diff = event1.duration.difference(event2.duration);
   if (diff.length < 0)
       console.log('Event1 is longer than Event2.');
   else if (diff.length == 0)
       console.log('Event1 is as long as Event2.');
   else
       console.log('Event1 is shorter than Event2.');
   ```

   > **Note**  
   > The unit of the returned `TimeDuration` object is equivalent to the largest possible unit amongst the source parameter units while making sure that precision is not lost in the result. This implies that if, for example, a comparison is done between "1 hour" and "20 minutes", the result is displayed as 40 minutes, not 0.67 hour. Although the hour is a bigger unit than the minute, the result is more precise if presented in minutes.

2.  To compare 2 `TimeDuration` objects for equality, use the `equalsTo()` method:

      ```
      var d1 = new tizen.TimeDuration(60, 'MINS');
      var d2 = new tizen.TimeDuration(1, 'HOURS');
      var ret = d1.equalsTo(d2); /* Returns true */
      ```

3.  To check whether 1 `TimeDuration` object is shorter than another, use the `lessThan()` method:

      ```
      /* Check whether d1 is shorter than d2 */
      var d1 = new tizen.TimeDuration(1, 'HOURS');
      var d2 = new tizen.TimeDuration(120, 'MINS');
      var ret = d1.lessThan(d2); /* Returns true */
      ```

4.  To check whether 1 `TimeDuration` object is longer than another, use the `greaterThan()` method:

      ```
      /* Check whether d1 is longer than d2 */
      var d1 = new tizen.TimeDuration(2, 'HOURS');
      var d2 = new tizen.TimeDuration(60, 'MINS');
      var ret = d1.greaterThan(d2); /* Returns true */
      ```

5. To add a predefined time to the current date, use the `addDuration()` method:

   ```
   /* Convert the current date to the date of the next day, at the same time */
   var now = tizen.time.getCurrentDateTime();
   var tomorrow = now.addDuration(new tizen.TimeDuration(1, 'DAYS');
   ```

    If the number of added time is negative, date or time is set to an earlier moment of time.

## Retrieving Time Change Notifications

Getting notifications when the user changes the time or time zone allows you to react to those changes in your application.

1. To monitor time or time zone changes, define the event handlers:

   - The time change event handler is called when the user adjusts the clock:

     ```
     function timeChangedCallback() {
         try {
             var current_dt = tizen.time.getCurrentDateTime();
             console.log('Clock has been set. Current date/time is ' + current_dt.toLocaleString());
         }
     }
     ```

   - The time zone change event handler is called when the user switches the time zone:

     ```
     function timezoneChangedCallback() {
         try {
             /*
                New time zone can be retrieved
                through tizen.time.getLocalTimezone()
             */
             var zone = tizen.time.getLocalTimezone();
             console.log('Time zone has been set to ' + zone);
         }
     }
     ```

2. When the event handlers are defined, register them as listeners:

   - Register the time change listener using the `setDateTimeChangeListener()` method of the `TimeUtil` interface (in [mobile](../../api/latest/device_api/mobile/tizen/time.html#TimeUtil), [wearable](../../api/latest/device_api/wearable/tizen/time.html#TimeUtil), and [TV](../../api/latest/device_api/tv/tizen/time.html#TimeUtil) applications):

     ```
     tizen.time.setDateTimeChangeListener(timeChangedCallback);
     ```

   - Register the time zone change listener using the `setTimezoneChangeListener()` method of the `TimeUtil` interface:

     ```
     tizen.time.setTimezoneChangeListener(timezoneChangedCallback);
     ```

3. To stop receiving the notifications, deregister the listeners:

   - To deregister the time change listener, use the `unsetDateTimeChangeListener()` method of the `TimeUtil` interface:

     ```
     tizen.time.unsetDateTimeChangeListener();
     ```

   - To deregister the time zone change listener, use the `unsetTimezoneChangeListener()` method of the `TimeUtil` interface:

     ```
     tizen.time.unsetTimezoneChangeListener();
     ```

## Related Information
* Dependencies     
     - Tizen 2.4 and Higher for Mobile
     - Tizen 2.3.1 and Higher for Wearable
     - Tizen 3.0 and Higher for TV
