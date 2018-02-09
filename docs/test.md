This is template for API Guide document.

- Title

This section shows the title of the contents with #

```markdown
# Alarm
```

- Content

This section shows contents of the document.

```markdown
Content

- [Prerequisites](#prerequisites)
- [Setting an Alarm after Specific Time](#scenario_1)
- [Setting an Alarm on a Specific Date](#scenario_2)
- [...](#scenario_3)
```

- Overview

This section shows what the API is.

```markdown
You can use alarms to launch applications or send user notifications at specific times. The mechanism involved in launching the application is the [Tizen.Applications.AppControl](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1Applications_1_1AppControl.html) class.

The `Tizen.Applications.AppControl` class allows launching an application explicitly, giving its package name, or providing certain criteria that the application must meet. For example, the criteria can include the type of data on which the application must be able to operate. The structure containing the criteria is called an application control.

The following figure illustrates the rule components and their relations.
```

- Image

A image has a caption if it is needed.

```markdown
**Figure: Rule components**

![Rule components](media/image.png)
```

- Main feature

Main features MUST be described in the form of a gerund.

```markdown
The main features of the `Tizen.Applications.Alarm` and `Tizen.Applications.AlarmManager` classes include:

- Setting alarms with a specific delay  
  You can [set an alarm to trigger after a specific amount of time](https://developer.tizen.org/development/tizen-.net-preview/api/guides/alarms#scenario_1).
- Setting alarms for specific dates  
  You can [set an alarm for a specific date](https://developer.tizen.org/development/tizen-.net-preview/api/guides/alarms#scenario_2).
- ...
```

- Feature

This section shows the detailed features.

```markdown
## Trigering events

This feature is ......
```

- Prerequisites

This section shows the required features, privileges, or conditions.

```markdown
## Prerequisites

To enable your application to use the alarm functionality:

1. To use the Alarm API applications), the application has to request permission by adding the following privileges to the `tizen-manifest.xml` file:

   <privileges>
      <privilege>http://tizen.org/privilege/alarm.get</privilege>
      <privilege>http://tizen.org/privilege/alarm.set</privilege>
      <!--If an alarm is used to send a notification-->
      <privilege>http://tizen.org/privilege/notification</privilege>
   </privileges>

2. To use the methods and properties of the `Tizen.Applications.Alarm` and `Tizen.Applications.AlarmManager`classes, include the [Tizen.Applications](https://developer.tizen.org/dev-guide/csapi/namespaceTizen_1_1Applications.html) namespace in your application:

   using Tizen.Applications;

3. ...
```


- Procedure

This section shows steps to explain how to do.

```markdown
## Setting an Alarm with a Specific Delay

You can set an alarm which, when it expires, either launches an application or sends a notification to the user:

- To set an alarm to launch an application:

  You need 2 applications: the "AlarmRegister" application that sets the alarm, and the "AlarmTarget" application that is launched when the alarm expires.

  1. In the AlarmRegister application:
     1. To identify which application to start when the alarm expires, the [Tizen.Applications.AlarmManager](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1Applications_1_1AlarmManager.html) class needs an application control instance.Create a new instance of the [Tizen.Applications.AppControl](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1Applications_1_1AppControl.html) class, and set the `Operation` and `ApplicationID` properties for it. The `Operation` property identifies the operation to be performed, and the `ApplicationID` property identifies the `appid` of the target application to be launched. You can get the `appid` of the target application from its `tizen-manifest.xml` file.  
         ```
         int DELAY = 2;
         int PERIOD = 1;

         AppControl appControl = new AppControl();

         appControl.Operation = AppControlOperations.Default;
         appControl.ApplicationId = "org.tizen.alarmslave";
         ```
     2. To schedule an alarm after a delay, use the `CreateAlarm()` method of the `Tizen.Applications.AlarmManager` class, with the initial delay, interval for subsequent alarms, and instance of the `Tizen.Applications.AppControl` class as parameters.The method creates the alarm as a new instance of the [Tizen.Applications.Alarm](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1Applications_1_1Alarm.html) class.  
         ```
         Alarm myAlarm = AlarmManager.CreateAlarm(DELAY, PERIOD, appControl);
         ```
  2. Implement the AlarmTarget application:
     A scheduled alarm calls AlarmTarget's `app_control_cb()` callback when the alarm expires:

- To set an alarm to send a notification to the user:
    Create a notification to be sent to the user as an instance of the Tizen.Applications.Notifications.Notification class:

 ...
```

- Note

  MUST add "Note" with strong.

```markdown
> **Note**
>
> The system can adjust when the alarm expires.
> ...
```

- Table

This section shows table element.

```markdown
**Table: tm fields**

| Member   | Type | Meaning                  | Range |
| -------- | ---- | ------------------------ | ----- |
| `tm_sec` | int  | Seconds after the minute | 0-61* |
```
