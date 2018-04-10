# Alarms


You can launch an application at a specific time using alarms. The mechanism involved in launching the application is the App Control API (in [mobile](../../api/mobile/latest/group__CAPI__APP__CONTROL__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__APP__CONTROL__MODULE.html) applications).

The AppControl API allows [launching an application](../app-management/app-controls.md) explicitly, giving its package name, or providing certain criteria that the application must meet. For example, the criteria can include the type of data on which the application must be able to operate. The structure containing the criteria is called an application control.

The main features of the Alarm API include:

- Setting alarms after a specific time

  You can [set an alarm to trigger after a specific amount of time](#scenario_1).

- Setting alarms on specific dates

  You can [set an alarm on a specific date](#scenario_2).

- Setting recurring alarms

  You can [set a recurring alarm](#scenario_3) to trigger at a specific time of the day.

- Managing existing alarms

  You can [list all scheduled alarms and cancel them](#scenario_4).

## Prerequisites

To enable your application to use the alarm functionality:

1. To use the Alarm API (in [mobile](../../api/mobile/latest/group__CAPI__ALARM__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__ALARM__MODULE.html) applications), the application has to request permission by adding the following privileges to the `tizen-manifest.xml` file:
```
<privileges>  
	<privilege>http://tizen.org/privilege/alarm.get</privilege>   
    <privilege>http://tizen.org/privilege/alarm.set</privilege>
</privileges>
```
2. To use the functions and data types of the Alarm API, include the `<app_alarm.h>` header file in your application:
```
#include <app_alarm.h>
```
<a name="scenario_1"></a>
## Setting an Alarm after Specific Time

> **Note**  
> Since 2.4, the `alarm_schedule_after_delay()` function does not support an exact period and delay to minimize device wake-ups. The system can adjust when the alarm expires.

To set an alarm after a specific time:

1. Implement the AlarmRegister application:

   1. To identify which application to start when the alarm expires, the Alarm API needs the `app_control_h` handle.

      Obtain the `app_control_h` handle of a specific app by calling the `app_control_set_app_id()` function. You can get the AlarmTarget `app_id` from the `tizen-manifest.xml` file.

      ```
      bool
      init_alarm()
      {
          int ret;
          int DELAY = 2;
          int REMIND = 1;
          int alarm_id;

          app_control_h app_control = NULL;
          ret = app_control_create(&app_control);
          ret = app_control_set_operation(app_control, APP_CONTROL_OPERATION_DEFAULT);
          ret = app_control_set_app_id(app_control, "org.tizen.alarmslave");
      ```

   2. To schedule an alarm after a delay, use the `alarm_schedule_after_delay()` function:

      ```
          ret = alarm_schedule_after_delay(app_control, DELAY, REMIND, &alarm_id);

          return true;
      }
      ```

2. Implement the AlarmTarget application:

   A scheduled alarm calls AlarmTarget's `app_control_cb()` callback when the alarm expires:

   ```
   void
   service_app_control(app_control_h app_control, void *data)
   {
       dlog_print(DLOG_INFO, LOG_TAG, "app_control called by Alarm API.");
   }
   ```

<a name="scenario_2"></a>
## Setting an Alarm on a Specific Date

To schedule an alarm on a specific date, use the `alarm_schedule_at_date()` function.

The second parameter defines the time of the first active alarm. It can be defined using the `tm` struct included in the `<time.h>` header file. The following table lists the selected `tm` fields.

**Table: tm fields**

| Member    | Type                   | Meaning                  | Range |
|-----------|------------------------|--------------------------|-------|
| `tm_sec`  | int                    | Seconds after the minute | 0-61* |
| `tm_min`  | int| Minutes after the hour | 0-59                     |
| `tm_hour` | int| Hours since midnight   | 0-23                     |
| `tm_mday` | int| Day of the month       | 1-31                     |
| `tm_mon`  | int| Months since January   | 0-11                     |
| `tm_year` | int| Years since 1900       | -                        |

The following code schedules an application control to invoke after 4 seconds (using the `date.tm_sec` member). Using, for example, `date.tm_mday`, can set the alarm to another day of the month. Since the third parameter is set to 0, the alarm is executed only once.

```
struct tm date;
ret = alarm_get_current_time(&date);

date.tm_sec += 4;
ret = alarm_schedule_at_date(app, &date, 0, &alarm_id);
```

> **Note**  
> The `alarm_schedule_at_date()` function has been deprecated since Tizen 2.4. Use the `alarm_schedule_once_at_date()` function instead.

<a name="scenario_3"></a>
## Setting a Recurring Alarm at a Specific Time of the Day

To schedule an alarm on a specific time of the day with a recurrence, use the `alarm_schedule_with_recurrence_week_flag()` function.

The third parameter defines the day of the week on which the alarm recurs. The value is defined with the `enum alarm_week_flag_e` enumerator (in [mobile](../../api/mobile/latest/group__CAPI__ALARM__MODULE.html#gaa2b3960fe55c63cb3f6739758bd172ee) and [wearable](../../api/wearable/latest/group__CAPI__ALARM__MODULE.html#gaa2b3960fe55c63cb3f6739758bd172ee) applications), and can be a combination of days, for example `ALARM_WEEK_FLAG_TUESDAY | ALARM_WEEK_FLAG_FRIDAY`. The value can also be a binary, such as `1<<3 | 1<<6`.

The following code schedules an application control to invoke on TUESDAY and FRIDAY:

```
struct tm date;
ret = alarm_get_current_time(&date);

time_t time_current = mktime(&date);
dlog_print(DLOG_INFO, TAG, "Schedule on date: %s ", ctime(&time_current));
ret = alarm_schedule_with_recurrence_week_flag(app_control, &date,
                                               ALARM_WEEK_FLAG_TUESDAY | ALARM_WEEK_FLAG_FRIDAY, &alarm_id);
```

<a name="scenario_4"></a>
## Listing All Scheduled Alarms and Canceling an Alarm

To list all scheduled alarms, use the `alarm_foreach_registered_alarm()` function.

To cancel a specific scheduled alarm, use the `alarm_cancel()` function with the alarm ID. To cancel all alarms registered by the application, use the `alarm_cancel_all()` function.

The following code implements the callback for the `alarm_foreach_registered_alarm()` function. It lists all registered alarms and alarm recurrence days. At the end of the function, the `alarm_cancel()` function is called to cancel every scheduled alarm.

```
static bool
on_foreach_registered_alarm(int alarm_id, void *user_data)
{
    int flag;
    int ret = 0;
    struct tm date;
    time_t time_current;

    ret = alarm_get_scheduled_date(alarm_id, &date);
    if (ret != ALARM_ERROR_NONE)
        dlog_print(DLOG_ERROR, TAG, "Get time Error: %d ", ret);

    /* Logging scheduled alarm info */
    time_current = mktime(&date);
    dlog_print(DLOG_INFO, TAG, "Registered alarm: %d on date: %s ", alarm_id, ctime(&time_current));

    ret = alarm_get_scheduled_recurrence_week_flag(alarm_id, &flag);
    if (ret == 0) {
        if (flag & ALARM_WEEK_FLAG_SUNDAY)
            dlog_print(DLOG_INFO, TAG, "Alarm Recurrence on SUNDAY \n");
        if (flag & ALARM_WEEK_FLAG_MONDAY)
            dlog_print(DLOG_INFO, TAG, "Alarm Recurrence on MONDAY \n");
        if (flag & ALARM_WEEK_FLAG_TUESDAY)
            dlog_print(DLOG_INFO, TAG, "Alarm Recurrence on TUESDAY \n");
        if (flag & ALARM_WEEK_FLAG_WEDNESDAY)
            dlog_print(DLOG_INFO, TAG, "Alarm Recurrence on WEDNESDAY \n");
        if (flag & ALARM_WEEK_FLAG_THURSDAY)
            dlog_print(DLOG_INFO, TAG, "Alarm Recurrence on THURSDAY \n");
        if (flag & ALARM_WEEK_FLAG_FRIDAY)
            dlog_print(DLOG_INFO, TAG, "Alarm Recurrence on FRIDAY \n");
        if (flag & ALARM_WEEK_FLAG_SATURDAY)
            dlog_print(DLOG_INFO, TAG, "Alarm Recurrence on SATURDAY \n");
    }

    /* Cancel scheduled alarms */
    ret = alarm_cancel(alarm_id);
    if (ret != ALARM_ERROR_NONE)
        dlog_print(DLOG_ERROR, TAG, "Cancel Error: %d ", ret);

    return true;
}

ret = alarm_foreach_registered_alarm(on_foreach_registered_alarm, NULL);
if (ret != ALARM_ERROR_NONE)
    dlog_print(DLOG_ERROR, TAG, "Listing Error: %d ", ret);
```

## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
