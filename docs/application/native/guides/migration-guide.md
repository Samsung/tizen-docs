# Migration Guide from 2.3 to 2.4

Tizen 2.4 introduces new APIs for applications and modifies the behavior of some APIs to improve the quality of the platform. The following sections define the issues you must consider to make your application conform to Tizen 2.4 Application Framework APIs.

## New Background Application Policy

Since Tizen 2.4, an application in the background goes into a suspended state.

In the suspended state, the application process is executed with limited CPU resources. In other words, the platform does not allow the running of the background applications, except for some exceptional applications (such as Media and Download) that necessarily work in the background. In this case, the application can designate their background category as an allowed category to avoid going into the suspended state.

For more information, and a list of background categories that allow the application to run in the background, see [Background Categories](app-management/efl-ui-app.md#allow_bg).

You can receive an event when the background application goes to the suspended state. Pass `APP_EVENT_SUSPENDED_STATE_CHANGED` as `event_type` to the `ui_app_add_event_handler()` or `service_app_add_event_handler()` function to handle the suspended event. You must release the resources properly when your application goes to the suspended state.

## Changes in the Alarm API for Reducing Power Consumption

Since Tizen 2.4, the Alarm API is changed to reduce the power consumption of the device:

- Alarm APIs that support exact alarms are changed to be able to launch UI applications only. While launching UI applications when the alarm expires, the framework turns the LCD display on. Because of this you must not use those Alarm APIs for background processing. You can use the `alarm_schedule_after_delay()` function that supports an inexact alarm for background processing.
- The `alarm_schedule_after_delay()` function is changed to support an inexact alarm. You can pass a period for alarm expiration, but the platform decides when the alarm expires according to the status of the device.

  The `alarm_schedule_after_delay()` function can launch service applications when it is expired. However, the target service application must specify a background category to be registered as the target application of the function.
- Regarding the `app_control` parameter of the Alarm APIs, only explicit launch is allowed. You cannot pass `app_control` for an implicit launch because the implicit launch cannot specify the target application when it is registered.

When you migrate your application from Tizen 2.3 to Tizen 2.4, check the changes and modify your application to conform with the Tizen 2.4 Alarm APIs.

## Tizen Application Event System in Mobile Applications

Tizen 2.4 introduces new Tizen Application Event APIs for subscribing system events and publishing and subscribing application events to other applications.

Using the Tizen Application Event APIs, you can register your service application to be launched when a specified event is published. You can specify the event name through the `<app-control>` element in the application manifest file. This launch-on-event allows your service application to only run after receiving an event from the platform or other application. Note that UI applications cannot be launched using the launch-on-event mechanism. For more information, see the [Event](../../api/mobile/latest/group__CAPI__EVENT__MODULE.html) API.

## Application Group Launching Management

When you launch an application using the `app_control_send_launch_request()` function, you can treat the launched application as a sub-view of your application. For example, when your application launches the message composer application to send a message, you can treat the message composer as a member of your application group. Tizen 2.4 introduces the application group feature to supports this requirement.

The application can specify a launch mode when it launches a new application with the `app_control_set_launch_mode()` function. The following modes are available:

- `APP_CONTROL_LAUNCH_MODE_SINGLE`: the launched application is launched in a separate group.
- `APP_CONTROL_LAUNCH_MODE_GROUP`: the launched application is included in the group of the caller application.

You can also specify whether your application supports the group mode launching. You can specify the supported launch mode of your application in the application manifest file. The available `launch_mode` options are:

- `single`: the application is always launched in a separate group, even if the caller application requests the `APP_CONTROL_LAUNCH_MODE_GROUP` mode.
- `caller`: the application is launched according to the caller application request.
- `group`: the application is included in the group of the caller application.

For more information, see [Managing Application Groups](app-management/app-controls.md#group).

## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
