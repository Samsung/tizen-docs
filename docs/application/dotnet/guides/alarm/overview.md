# Alarms

You can use alarms to launch applications or send user notifications at specific times. The mechanism involved in launching the application is the [Tizen.Applications.AppControl](/application/dotnet/api/TizenFX/latest/api/Tizen.Applications.AppControl.html) class.

The `Tizen.Applications.AppControl` class allows launching an application explicitly, giving its package name, or providing certain criteria that the application must meet. For example, the criteria can include the type of data on which the application must be able to operate. The structure containing the criteria is called an application control.

You can use the following alarm features in your .NET applications:

-   [Alarm](alarms.md)

    You can use the `Tizen.Applications.Alarm` class, to set an "alarm clock" for the delivery of a notification at some point in the future.

## Related information
- Dependencies
  - Tizen 4.0 and Higher
- API References
  - [Tizen.Applications.AppControl](/application/dotnet/api/TizenFX/latest/api/Tizen.Applications.AppControl) class
  - [Tizen.Applications.AlarmManager](/application/dotnet/api/TizenFX/latest/api/Tizen.Applications.AlarmManager) class
  - [Tizen.Applications.Alarm](/application/dotnet/api/TizenFX/latest/api/Tizen.Applications.Alarm) class
  
