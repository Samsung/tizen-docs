# Alarms

You can schedule an application to be run at a specific time. When an alarm is triggered, the application is launched (unless it is already running).

The Alarm API is mandatory for Tizen mobile, wearable, and TV profiles, which means that it is supported on all mobile, wearable, and TV devices. All mandatory APIs are supported on the Tizen Emulators.

The main features of the Alarm API include:

- Alarm management   

  You can [manage alarms](#managing-alarms) by creating and deleting them. You can also obtain a list of all existing alarms on the device.

- Application launches with alarms   

  You can set an alarm to [launch an application when triggered](#launching-applications-with-alarms).

- Alarm events   

  You can [retrieve information about the next alarm event](#checking-for-alarm-events).

- Alarm notification management **in mobile and wearable applications only**   

  You can create alarm notifications, which [post a notification](#managing-alarm-notifications-in-mobile-and-wearable-applications) when the alarm is triggered. You can also obtain the details of the created notifications.

## Prerequisites

To use the Alarm API (in [mobile](../../api/latest/device_api/mobile/tizen/alarm.html), [wearable](../../api/latest/device_api/wearable/tizen/alarm.html), and [TV](../../api/latest/device_api/tv/tizen/alarm.html) applications), the application has to request permission by adding the following privilege to the `config.xml` file:

```
<tizen:privilege name="http://tizen.org/privilege/alarm"/>
```

## Managing Alarms

Both relative and absolute alarms are available: a relative alarm is triggered after a specified delay from the moment it is created, while an absolute alarm is triggered at a specified time and date. You can also create a recurring alarm that is repeated after a specified period of time, or on the given days of the week at a defined time.

To obtain a list of alarms, and create and delete alarms:

1. To obtain a list of all the alarms that have been set on a device but not yet triggered, use the `getAll()` method:

   ```
   var alarms = tizen.alarm.getAll();
   console.log(alarms.length + ' alarms present in the storage.');
   ```

2. To create an alarm:

   - To create an absolute alarm, create an instance of the `AlarmAbsolute` interface (in [mobile](../../api/latest/device_api/mobile/tizen/alarm.html#AlarmAbsolute), [wearable](../../api/latest/device_api/wearable/tizen/alarm.html#AlarmAbsolute), and [TV](../../api/latest/device_api/tv/tizen/alarm.html#AlarmAbsolute) applications).

     You must define the time and date when the alarm is triggered as a `Date` object.

     ```
     /* Alarm is triggered at 8:00 on April 4, 2012 */
     var date = new Date(2012, 3, 4, 8, 0);
     var alarm1 = new tizen.AlarmAbsolute(date);
     ```

   - To create a relative alarm, create an instance of the `AlarmRelative` interface (in [mobile](../../api/latest/device_api/mobile/tizen/alarm.html#AlarmRelative), [wearable](../../api/latest/device_api/wearable/tizen/alarm.html#AlarmRelative), and [TV](../../api/latest/device_api/tv/tizen/alarm.html#AlarmRelative) applications).

     You must define the delay after which the alarm is triggered. Use the predefined constants from the `AlarmManager` interface (in [mobile](../../api/latest/device_api/mobile/tizen/alarm.html#AlarmManager), [wearable](../../api/latest/device_api/wearable/tizen/alarm.html#AlarmManager), and [TV](../../api/latest/device_api/tv/tizen/alarm.html#AlarmManager) applications).

     ```
     /* Alarm is triggered in 3 hours */
     var alarm2 = new tizen.AlarmRelative(3 * tizen.alarm.PERIOD_HOUR);
     ```

   - To create a recurring absolute alarm, create an instance of the `AlarmAbsolute` interface.

     You must define the time and date when the alarm is triggered as a `Date` object. In addition, you can define the weekdays or a time period when the alarm is repeated. Define the time period using the predefined constants from the `AlarmManager` interface.

     ```
     /* Alarm is triggered for the first time at 8:00 on April 4, 2012 */
     var date = new Date(2012, 3, 4, 8, 0);

     /* Alarm repeats every 2 days, at 08:00, starting after April 4, 2012 */
     var alarm3 = new tizen.AlarmAbsolute(date, 2 * tizen.alarm.PERIOD_DAY);

     /*
        Alarm repeats every Saturday and Sunday,
        at 08:00, starting after April 4, 2012
     */
     var alarm4 = new tizen.AlarmAbsolute(date, ['SA', 'SU']);
     ```

        > **Note**  
        > You cannot define both a time period and a weekday recurrence for the same alarm.

   - To create a recurring relative alarm, create an instance of the `AlarmRelative` interface.

     You must define the delay after which the alarm is triggered, and the period after which it is repeated.

     ```
     /*
        Alarm is triggered for the first time in 1 hour,
        and then repeated every 2 minutes
     */
     var alarm5 = new tizen.AlarmRelative(tizen.alarm.PERIOD_HOUR, 2 * tizen.alarm.PERIOD_MINUTE);
     ```
<a name="removeAlarm"></a>

3. To delete an alarm, use the `remove()` method with the alarm ID:

   ```
   /* First add created alarm to the device */
   /* Tizen alias ID is deprecated since Tizen 2.3.1 */
   tizen.alarm.add(alarm1, 'tizen.internet');
   /* Then remove it */
   tizen.alarm.remove(alarm1.id);
   ```

   To delete all alarms at once, use the `removeAll()` method.

## Launching Applications with Alarms

Learning how to launch applications with alarms is a basic alarm management skill:

1. To launch an application when an alarm is triggered, you must define the application as a parameter in the `add()` method used to add the created alarm to the system:

   ```
   /* Run the browser */
   var alarm = new tizen.AlarmAbsolute(new Date(2012, 10, 4, 8, 0));
   /* Tizen alias ID is deprecated since Tizen 2.3.1 */
   tizen.alarm.add(alarm, 'tizen.internet');
   ```

2. To launch an application with additional information when an alarm is triggered, you must use the application control and define the required arguments as a parameter in the `add()` method used to add the created alarm to the system:

   ```
   /*
      Run the browser and open the defined browser page
      with the operation/view application control
   */

   var alarm = new tizen.AlarmAbsolute(new Date(2012, 10, 4, 8, 0));
   var appControl = new tizen.application.ApplicationControl('http://tizen.org/appcontrol/operation/view',
                                                             'http://www.tizen.org');

   tizen.alarm.add(alarm, 'org.tizen.browser', appControl);
   ```

## Checking for Alarm Events

You can retrieve information about the next alarm event using the `AlarmAbsolute` (in [mobile](../../api/latest/device_api/mobile/tizen/alarm.html#AlarmAbsolute), [wearable](../../api/latest/device_api/wearable/tizen/alarm.html#AlarmAbsolute), and [TV](../../api/latest/device_api/tv/tizen/alarm.html#AlarmAbsolute) applications) and `AlarmRelative` (in [mobile](../../api/latest/device_api/mobile/tizen/alarm.html#AlarmRelative), [wearable](../../api/latest/device_api/wearable/tizen/alarm.html#AlarmRelative), and [TV](../../api/latest/device_api/tv/tizen/alarm.html#AlarmRelative) applications) interfaces. They provide the time and date of the next scheduled absolute alarm, or the time remaining before the next relative alarm.

1. Create an absolute alarm:

   ```
   /* Alarm is triggered at 8:00 on April 4, 2012 */
   var alarm = new tizen.AlarmAbsolute(new Date(2012, 3, 4, 8, 0));
   tizen.alarm.add(alarm, 'org.tizen.browser');
   ```

2. Use the `getNextScheduledDate()` method to retrieve the time and date of the next absolute alarm to be triggered:

   ```
   console.log('The alarm will trigger at ' + alarm.getNextScheduledDate());
   ```

3. Create a relative alarm:

   ```
   /* Alarm is triggered in 3 hours */
   var alarm = new tizen.AlarmRelative(3 * tizen.alarm.PERIOD_HOUR);
   tizen.alarm.add(alarm, 'org.tizen.browser');
   ```

4. Use the `getRemainingSeconds()` method to retrieve the number of seconds till the next relative alarm is triggered:

   ```
   console.log('The alarm triggers ' + alarm.getRemainingSeconds() + ' seconds later');
   ```

## Managing Alarm Notifications in Mobile and Wearable Applications

Alarm notification is an alarm which, when triggered, automatically posts a [notification](../../api/latest/device_api/mobile/tizen/notification.html#Notification). You can create alarm notifications with both `AlarmAbsolute` (in [mobile](../../api/latest/device_api/mobile/tizen/alarm.html#AlarmAbsolute) and [wearable](../../api/latest/device_api/wearable/tizen/alarm.html#AlarmAbsolute) applications) and `AlarmRelative` (in [mobile](../../api/latest/device_api/mobile/tizen/alarm.html#AlarmRelative) and [wearable](../../api/latest/device_api/wearable/tizen/alarm.html#AlarmRelative) applications) alarm types. The notification is shown in the status bar on the device.

To create an alarm notification with the `AlarmRelative` alarm type and `UserNotification` notification type, where the alarm is periodic and the notification is posted after the alarm is triggered:

1. Create an `AlarmRelative` object:

   ```
   /* Alarm triggers after 3 seconds and repeats every 3 hours */
   var alarm = new tizen.AlarmRelative(3, 3 * tizen.alarm.PERIOD_HOUR);
   ```

2. Create the `ApplicationControl` and `UserNotificationInit` instances needed for the `UserNotification` notification type:

   ```
   /* Create ApplicationControl object */
   var appControl = new tizen.ApplicationControl('http://tizen.org/appcontrol/operation/default',
                                                 null, 'image/jpg', null);
   /* You can add additional attributes to the notification dictionary */
   var notificationDict = {
       content: 'This is a simple notification\'s content.',
       actions: {
           vibration: true,
           appId: tizen.application.getCurrentApplication().appInfo.id,
           appControl: appControl
       },
   };
   /* Create UserNotification object */
   var notification = new tizen.UserNotification('SIMPLE', 'Simple notification\'s title',
                                                 notificationDict);
   ```

3. Add the alarm notification:

   ```
   /* Add the created alarm to the storage */
   tizen.alarm.addAlarmNotification(alarm, notification);
   ```

4. You can retrieve the details of the added notification before the alarm goes off:

   ```
   /* Obtain notification object */
   var noti = tizen.alarm.getAlarmNotification(alarm.id);
   console.log('Notification title: ' + noti.title + ', content: ' + noti.content);
   ```

   You can [remove the alarm notification](#removeAlarm) with the `tizen.alarm.remove()` method.


## Related Information
* Dependencies   
   - Tizen 2.4 and Higher for Mobile
   - Tizen 2.3.1 and Higher for Wearable
   - Tizen 3.0 and Higher for TV
