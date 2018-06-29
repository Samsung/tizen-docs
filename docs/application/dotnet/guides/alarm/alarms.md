# Alarms



You can use alarms to launch applications or send user notifications at specific times. The mechanism involved in launching the application is the [Tizen.Applications.AppControl](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Applications.AppControl.html) class.

The `Tizen.Applications.AppControl` class allows launching an application explicitly, giving its package name, or providing certain criteria that the application must meet. For example, the criteria can include the type of data on which the application must be able to operate. The structure containing the criteria is called an application control.

The main features of the `Tizen.Applications.Alarm` and `Tizen.Applications.AlarmManager` classes include:

-   Setting alarms with a specific delay

    You can [set an alarm to trigger after a specific amount of time](#scenario_1).

- Setting alarms for specific dates

    You can [set an alarm for a specific date](#scenario_2).

- Setting recurring alarms

    You can [set a recurring alarm](#scenario_3) to trigger on a specific day or days of the week.

- Managing existing alarms

    You can [list all scheduled alarms and cancel them](#scenario_4).


## Prerequisites

To enable your application to use the alarm functionality:

1.  To use the [Tizen.Applications.Alarm](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Applications.Alarm.html) and [Tizen.Applications.AlarmManager](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Applications.AlarmManager.html) classes, the application has to request permission by adding the following privileges to the `tizen-manifest.xml` file:

    ```
    <privileges>
       <privilege>http://tizen.org/privilege/alarm.get</privilege>
       <privilege>http://tizen.org/privilege/alarm.set</privilege>
       <!--If an alarm is used to send a notification-->
       <privilege>http://tizen.org/privilege/notification</privilege>
    </privileges>
    ```

2. To use the methods and properties of the `Tizen.Applications.Alarm` and `Tizen.Applications.AlarmManager` classes, include the [Tizen.Applications](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Applications.html) namespace in your application:

    ```
    using Tizen.Applications;
    ```

3. To use the methods and properties of the [Tizen.Applications.Notifications](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Applications.Notifications.html) namespace to make an alarm send a notification, include the namespace in your application:

    ```
    using Tizen.Applications.Notifications;
    ```


<a name="scenario_1"></a>
## Setting an Alarm with a Specific Delay

You can set an alarm which, when it expires, either launches an application or sends a notification to the user:

-   To set an alarm to launch an application:

    You need 2 applications: the "AlarmRegister" application that sets the alarm, and the "AlarmTarget" application that is launched when the alarm expires.

    1.  In the AlarmRegister application:
        1.  To identify which application to start when the alarm expires, the [Tizen.Applications.AlarmManager](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Applications.AlarmManager.html) class needs an application control instance.

            Create a new instance of the [Tizen.Applications.AppControl](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Applications.AppControl.html) class, and set the `Operation` and `ApplicationID` properties for it. The `Operation` property identifies the operation to be performed, and the `ApplicationID` property identifies the `appid` of the target application to be launched. You can get the `appid` of the target application from its `tizen-manifest.xml` file.
            ```
            int DELAY = 2;
            int PERIOD = 1;

            AppControl appControl = new AppControl();

            appControl.Operation = AppControlOperations.Default;
            appControl.ApplicationId = "org.tizen.alarmslave";
            ```

        2.  To schedule an alarm after a delay, use the `CreateAlarm()` method of the `Tizen.Applications.AlarmManager` class, with the initial delay, interval for subsequent alarms, and instance of the `Tizen.Applications.AppControl` class as parameters.

            The method creates the alarm as a new instance of the [Tizen.Applications.Alarm](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Applications.Alarm.html) class.

            ​```
            Alarm myAlarm = AlarmManager.CreateAlarm(DELAY, PERIOD, appControl);
            ​```

    2. When the alarm expires, it triggers the `OnAppControlReceived()` event handler of the [Tizen.Applications.CoreApplication](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Applications.CoreApplication.html) class in the AlarmTarget application:

        ```
        protected override void OnAppControlReceived(AppControlReceivedEventArgs e)
        {
            base.OnAppControlReceived(e);
        }
        ```

- To set an alarm to send a notification to the user:
    1.  Create a notification to be sent to the user as an instance of the [Tizen.Applications.Notifications.Notification](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Applications.Notifications.Notification.html) class:

        ```
        int DELAY = 2;
        int PERIOD = 1;
        Notification myNoti;

        myNoti = new Notification
        {
            Title = "Notification",
            Content = "Hello Tizen"
        };
        ```

    2. To schedule an alarm after a delay, use the `CreateAlarm()` method of the `Tizen.Applications.AlarmManager` class, with the initial delay, interval for subsequent alarms, and instance of the `Tizen.Applications.Notifications.Notification` class as parameters.

        The method creates the alarm as a new instance of the `Tizen.Applications.Alarm` class.

        ```
        Alarm myAlarm = AlarmManager.CreateAlarm(DELAY, PERIOD, myNoti);
        ```


<a name="scenario_2"></a>
## Setting an Alarm for a Specific Date

To schedule an alarm for a specific date, use the `CreateAlarm()` method of the [Tizen.Applications.AlarmManager](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Applications.AlarmManager.html) class with an instance of the `DateTime` structure as its first parameter.

The following example schedules an application control to trigger 20 seconds after the current time (using the `AddSecond()` method of the `DateTime` structure):

```
DateTime dt = AlarmManager.GetCurrentTime();

myAlarm = AlarmManager.CreateAlarm(dt.AddSeconds(20), appControl);
```


<a name="scenario_3"></a>
## Setting a Recurring Alarm

You can set a recurring alarm that goes off at a specific moment, and thereafter at regular intervals.

To schedule a recurring alarm to go off on specific days of the week, use the `CreateAlarm()` method of the [Tizen.Applications.AlarmManager](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Applications.AlarmManager.html) class, with values of the [Tizen.Applications.AlarmWeekFlag](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Applications.AlarmWeekFlag.html) enumeration as the second parameter. You can join multiple values together to set the alarm to trigger on multiple days of the week.

The following example schedules an application control to be invoked at a set time every Tuesday and Friday:

```
Tizen.Applications.AppControl appControl = new Tizen.Applications.AppControl();
appControl.Operation = AppControlOperations.Default;
appControl.ApplicationId = "org.tizen.alarmslave"

Alarm myAlarm = AlarmManager.CreateAlarm(DateTime.New.AddSecond(10),
                                         AlarmWeekFlag.Tuesday | AlarmWeekFlag.Friday, appControl);
```

<a name="scenario_4"></a>
## Listing All Scheduled Alarms and Canceling an Alarm

You can list all scheduled alarms, and cancel alarms either one by one or all at once:

-   To list all scheduled alarms, use the `GetAllScheduledAlarms()` method of the [Tizen.Applications.AlarmManager](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Applications.AlarmManager.html) class:

    ```
    List<Alarm> alarms;

    alarms = (List<Alarm>)AlarmManager.GetAllScheduledAlarms();
    ```

- To cancel a single scheduled alarm, use the `Cancel()` method of the [Tizen.Applications.Alarm](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Applications.Alarm.html) class:

    ```
    Tizen.Applications.AppControl appControl = new Tizen.Applications.AppControl();
    Alarm myAlarm;

    appControl.Operation = AppControlOperations.Default;
    appControl.ApplicationId = "org.tizen.alarmslave";
    myAlarm = AlarmManager.CreateAlarm(100, appControl);

    try
    {
        myAlarm.Cancel();
    }
    catch (Exception e)
    {
        Log.Error("ALARM", "Exception occurs");
    }
    ```

- To cancel all alarms registered by the application, use the `CancelAll()` method of the `Tizen.Applications.AlarmManager` class:

    ```
    AlarmManager.CancelAll();
    ```

## Related Information
  * Dependencies
    -   Tizen 4.0 and Higher
