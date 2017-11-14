System Settings
===============

## Dependencies

- Tizen 4.0 and Higher

You can access the system configuration related to user preferences,
such as ringtone, wallpaper, and font.

The main features of the `Tizen.System.SystemSettings` class include:

-   Managing system settings

    You can [retrieve the current system settings](#settings).

- Monitoring system setting changes

    You can set event handlers to [monitor changes in the system
    settings](#events).


Prerequisites
-------------

To enable your application to use the system setting functionality:

1.  To use the
    [Tizen.System.SystemSettings](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1System_1_1SystemSettings.html)
    class, the application has to request permission by adding the
    following privilege to the `tizen-manifest.xml` file:

    ``` {.prettyprint}
    <privileges>
       <privilege>http://tizen.org/privilege/systemsettings.admin</privilege>
    </privileges>
    ```

2. To make your application visible in the Tizen Store only for devices
    that support the system setting features used in your application,
    add the corresponding feature keys to the `tizen-manifest.xml` file:

    ``` {.prettyprint}
    <!--To use the WallpaperHomeScreen property and WallpaperHomeScreenChanged event-->
    <feature name="http://tizen.org/feature/systemsetting.home_screen"/>
    ```

    The following table lists the feature keys required by the specific
    properties and events of the `Tizen.System.SystemSettings` class.

    **Table: Feature keys related to system settings**

    | Feature key                              | Property                                 | Event                                    |
    | ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
    | `http://tizen.org/feature/network.wifi`  | `NetworkWifiNotificationEnabled`         | `NetworkWifiNotificationSettingChanged`  |
    | `http://tizen.org/feature/network.telephony` | `UltraDataSave`                          | `UltraDataSaveChanged`, `UltraDataSavePackageListChanged` |
    | `http://tizen.org/feature/systemsetting.font` | `DefaultFontType`, `FontType`, `FontSize` | `FontSizeChanged`, `FontTypeChanged`     |
    | `http://tizen.org/feature/systemsetting.home_screen` | `WallpaperHomeScreen`                    | `WallpaperHomeScreenChanged`             |
    | `http://tizen.org/feature/systemsetting.incoming_call` | `IncomingCallRingtone`, `SoundNotification` | `IncomingCallRingtoneChanged`, `SoundNotificationChanged` |
    | `http://tizen.org/feature/systemsetting.lock_screen` | `LockscreenApp`, `WallpaperLockScreen`   | `LockScreenAppChanged`, `WallpaperLockScreenChanged` |
    | `http://tizen.org/feature/systemsetting.notification_email` | `EmailAlertRingtone`                     | `EmailAlertRingtoneChanged`              |

    You can also check whether a device supports a given feature by
    using the `TryGetValue()` method of the
    [Tizen.System.SystemInfo](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1System_1_1SystemInfo.html)
    class and, accordingly, enabling or disabling the code requiring the
    feature:

    ``` {.prettyprint}
    const string HOME_SCREEN_FEATURE_KEY = "http://tizen.org/feature/systemsetting.home_screen";
    bool ret;

    if (SystemInfo.TryGetValue<bool>(HOME_SCREEN_FEATURE_KEY, out ret) == false)
    {
        /// Error handling
    }
    ```

    **Note** In TV applications, you can test the system settings
    functionality on an emulator only. Most target devices do not
    currently support this feature.

    ​

3. To use the methods and properties of the
    `Tizen.System.SystemSettings` class, include the
    [Tizen.System](https://developer.tizen.org/dev-guide/csapi/namespaceTizen_1_1System.html)
    namespace in your application:

    ``` {.prettyprint}
    using Tizen.System;
    ```


Retrieving System Settings {#settings}
--------------------------

You can retrieve system settings with the properties of the
[Tizen.System.SystemSettings](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1System_1_1SystemSettings.html)
class.

To retrieve, for example, the ringtone for incoming calls, use the
`Tizen.System.SystemSettings.IncomingCallRingtone` property:

``` {.prettyprint}
var getValue = Tizen.System.SystemSettings.IncomingCallRingtone;
```


Monitoring System Setting Changes {#events}
---------------------------------

You can set up notifications about system setting changes by defining
event handlers and registering them for the
[Tizen.System.SystemSettings](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1System_1_1SystemSettings.html)
class events.

To monitor, for example, when the ringtone for incoming calls changes:

1.  Define the event handler and register it for the
    `IncomingCallRingtoneChanged` event:

    ``` {.prettyprint}
    private static void OnIncomingCallRingtoneChanged(object sender, Tizen.System.IncomingCallRingtoneChangedEventArgs e)
    {
        Assert.IsInstanceOf<string>(e.Value, "OnIncomingCallRingtoneChanged: IncomingCallRingtone not an instance of string");
    }

    Tizen.System.SystemSettings.IncomingCallRingtoneChanged += OnIncomingCallRingtoneChanged;
    ```

2. When you no longer need the event handler, deregister it:

    ``` {.prettyprint}
    Tizen.System.SystemSettings.IncomingCallRingtoneChanged -= OnIncomingCallRingtoneChanged;
    ```
