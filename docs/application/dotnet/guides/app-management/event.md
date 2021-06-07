# Event Broadcast and Subscription


The application can broadcast its own events to all listeners who want to listen. The events can either be predefined [system events from the platform](#platform) or user-defined events. Platform modules can broadcast system events whereas UI and service applications broadcast user-defined events.

The main features of the Event API are:

- Event publication

  You can [publish an event](#broadcast) using the [Tizen.Applications.EventManager.ApplicationEventManager](/application/dotnet/api/TizenFX/latest/api/Tizen.Applications.EventManager.ApplicationEventManager.html) class.

- Event subscription

  You can [subscribe to an event](#manage) using the [Tizen.Applications.EventManager.EventReceiver](/application/dotnet/api/TizenFX/latest/api/Tizen.Applications.EventManager.EventReceiver.html) class.

- Launch-On-Events

  You can [launch](#launch) the service applications when the desired target event occurs.

The application can be suspended while in the background, causing a pause in event handling. Since the application cannot receive events in the suspended state, they are all delivered in series after the application exits the suspended state. Following are the two methods to manage this situation and prevent the application from being flooded with events:

- To handle events in the background without going to a suspended state, [declare a background category](../applications/uiapplication/ui-app.md#allow_bg).
- To avoid receiving any events that are triggered while the application is suspended, remove the event handler before entering the suspended state and add it back after exiting the suspended state. You can [manage the event handler](../applications/uiapplication/ui-app.md#callback) addition and removal in the `APP_EVENT_SUSPENDED_STATE_CHANGED` event callback, which is triggered each time the application enters and exist the suspended state.

## Prerequisites

To enable your application to use the event functionality:

1. To use the methods and properties of the [Tizen.Applications.EventManager.ApplcationManager](/application/dotnet/api/TizenFX/latest/api/Tizen.Applications.EventManager.ApplicationEventManager.html) and [Tizen.Applications.EventManager.EventReceiver](/application/dotnet/api/TizenFX/latest/api/Tizen.Applications.EventManager.EventReceiver.html) classes, include the [Tizen.Applications.EventManager](/application/dotnet/api/TizenFX/latest/api/Tizen.Applications.EventManager.html) namespace in your application:

   ```csharp
   using Tizen.Applications.EventManager
   ```

2. To use Launch-On-Events in your application, define the `http://tizen.org/appcontrol/operation/launch_on_event` operation in the `tizen-manifest.xml` file.

   The URI name for the operation represents the event name in the Launch-On-Event format (`event://{Event_Name}`):

   ```XML
   <app-control>
      <operation name="http://tizen.org/appcontrol/operation/launch_on_event"/>
      <uri name="event://tizen.system.event.battery_charger_status"/>
   </app-control>
   ```

<a name="broadcast"></a>
## Publishing an Event

To publish an event to all receivers:

1. Create the bundle for publishing the event data:

   ```csharp
   Bundle bundle = new Bundle();
   bundle.AddItem("key", "value");
   ```

2. Use the `Publish()` method to publish the event:

   ```csharp
   ApplicationEventManager.Publish("event.org.tizen.example.AppEventTestApp.AppEvent", bundle);
   ```

<a name="manage"></a>
## Subscribing to an Event

To subscribe to a predefined system event or user-defined event:

1. Add an event handler.

   One event can have multiple event handlers, and one handler can be registered multiple times.

   - Add an event handler for a system event:

     ```csharp
     void OnReceived(object sender, EventManagerEventArgs e)
     {
         LogUtils.Write(LogUtils.DEBUG, LOG_TAG, "On Received : " + e.Name);
     }

     /* Register the event handler */
     EventReceiver receiver = new EventReceiver(SystemEvents.BatteryChargerStatus.EventName);
     receiver.Received += OnReceived;
     ```

   - Add an event handler for a user-defined event:

     When defining an event name for a user event such as `event.org.tizen.senderapp.user_event`, the name format is `event.{sender appid}.{user-defined name}`. The `{user-defined name}` must:

     - Contain only the ASCII characters "[A-Z][a-z][0-9]_" and not begin with a digit.
     - Not contain a '.' (period) character.
     - Not exceed the maximum name length (127 bytes).
     - Be at least 1 byte in length.

     ```csharp
     EventReceiver receiver = new EventReceiver("event.org.tizen.example.AppEventTestApp.AppEvent");
     receiver.Received += OnReceived;
     ```

2. Remove the event handler when no longer needed.

   A registered handler can be removed when the application is running. All the registered handlers can be removed when the application is terminated:

   ```csharp
   receiver.Received -= OnReceived;
   ```

<a name="launch"></a>
## Managing Launch-On-Events

To register an interest in a Launch-On-Event, define the `http://tizen.org/appcontrol/operation/launch_on_event` operation in the `tizen-manifest.xml` file.

> **Note**
>
> Only service applications can register and receive Launch-On-Events.
>
> The Launch-On-Event operation cannot be requested using the `AppControl.SendLaunchRequest()` method, unlike other application control operations.

The following table shows the system events that support Launch-On-Event:

**Table: System events supporting Launch-On-Event**

| Name                                     | Condition                                |
|------------------------------------------|------------------------------------------|
| `SystemEvents.BatteryChargerStatus.EventName` | When the charger state is `SystemEvents.BatteryChargerStatus.StatusValueConnected`. |
| `SystemEvents.UsbStatus.EventName`         | When the USB state is `SystemEvents.UsbStatus.StatusValueConnected`.     |
| `SystemEvents.EarjackStatus.EventName`     | When the earjack state is `SystemEvents.EarjackStatus.StatusValueConnected`. |
| `SystemEvents.IncomingMsg.EventName`       | When the `SystemEvents.IncomingMsg.TypeKey` and `SystemEvents.IncomingMsg.IdKey` exist.  |
| `SystemEvents.WifiState.EventName`         | When the Wi-Fi state is `SystemEvents.WifiState.StateValueConnected`.   |

To receive the Launch-On-Event:

```csharp
void AppControlReplyReceivedCallback(Tizen.Applications.AppControl launchRequest, Tizen.Applications.AppControl replyRequest, AppControlReplyResult result)
{
    string eventUri = "event://" + SystemEvents.BatteryChargerStatus.EventName;
        if (launchRequest.Operation.Equals(SystemEvents.BatteryChargerStatus.EventName))
        {
            if (launchRequest.Uri.Equals(eventUri))
            {
                string batteryValue = launchRequest.ExtraData.Get(SystemEvents.BatteryChargerStatus.StatusKey);
                LogUtils.Write(LogUtils.DEBUG, LOG_TAG, "Status value : " + batteryValue);
            }
        }
}
```

The application can get the event name and data in the first `AppControlReplyCallback()` callback, which is called after the application state changes to `created`.

<a name="platform"></a>
## Platform Event Types

The following list shows the events of modules:

- capi-system-device

  - battery

    | Event name | Event data Key | Event data Value | Condition | Notes |
    |-------|-------|--------|--------|--------|
    | `SystemEvents.BatteryChargerStatus.EventName` | `SystemEvents.BatteryChargerStatus.StatusKey`  | - `SystemEvents.BatteryChargerStatus.StatusValueDisconnected` : Charger is not connected<br>- `SystemEvents.BatteryChargerStatus.StatusValueConnected`: Charger is connected<br>- `SystemEvents.BatteryChargerStatus.StatusValueCharging`: Charging is enabled<br>- `SystemEvents.BatteryChargerStatus.StatusValueDischarging`: Charging is disabled (for example, 100% full  state) | When the charger has been connected or disconnected, or when the charging state has changed (charging or not charging). | If there is an earlier occurrence regarding this event, you receive the event as soon as you  register an event handler for this event. You can use this earlier event data as the initial value. |
    | `SystemEvents.BatteryLevelStatus.EventName`   | `SystemEvents.BatteryLevelStatus.StatusKey`    | - `SystemEvents.BatteryLevelStatus.StatusValueEmpty` <br>- `SystemEvents.BatteryLevelStatus.StatusValueCritical` <br>- `SystemEvents.BatteryLevelStatus.StatusValueLow` <br>- `SystemEvents.BatteryLevelStatus.StatusValueHigh` <br>- `SystemEvents.BatteryLevelStatus.StatusValueFull` | When the  battery level has changed.     | You can get the  current value with the `Tizen.System.Battery.Level` property. |

- deviced

  - usb

    | Event name | Event data Key | Event data Value | Condition | Notes |
    |-------|-------|--------|--------|--------|
    | `SystemEvents.UsbStatus.EventName`            | `SystemEvents.UsbStatus.StatusKey`  | - `SystemEvents.UsbStatus.StatusValueDisconnected`:  USB cable is not connected<br>- `SystemEvents.UsbStatus.StatusValueConnected`: USB cable is connected, but the service is not  available<br>-  `SystemEvents.UsbStatus.StatusValueAvailable`: USB service is available (for example, mtp or SDB) | When the USB  cable has been connected or disconnected, or when the USB service state has  changed. | N/A |

  - earjack

    | Event name | Event data Key | Event data Value | Condition | Notes |
    |-------|-------|--------|--------|--------|
    | `SystemEvents.EarjackStatus.EventName`       | `SystemEvents.EarjackStatus.StatusKey`  | - `SystemEvents.EarjackStatus.StatusValueDisconnected`:  Earjack is not connected <br>- `SystemEvents.EarjackStatus.StatusValueConnected`: Earjack is connected | When the  earjack connection state has changed. | You can get the current value using `System.Information.SetCallback` with the `http://tizen.org/runtimefeature/audiojack.connected` key. |

  - display

    | Event name | Event data Key | Event data Value | Condition | Notes |
    |-------|-------|--------|--------|--------|
    | `SystemEvents.DisplayState.EventName`        | `SystemEvents.DisplayState.StateKey`    | - `SystemEvents.DisplayState.StateValueNormal`:  Display on, normal brightness<br>- `SystemEvents.DisplayState.StateValueDim`: Display on, dimmed brightness<br>- `SystemEvents.DisplayState.StateValueOff`: Display off | When the  display state has changed.     | You can get the  current value with the `System.Display.State` property. |

- systemd

  - system

    | Event name | Event data Key | Event data Value | Condition | Notes |
    |-------|-------|--------|--------|--------|
    | `SystemEvents.BootCompleted.EventName`        | N/A                     | N/A                                      | When the  platform has completed booting. | You can treat  the initial value as `false`  before you receive this event. If the application is already in a  boot-completed state before you register an event handler, you receive the  event as soon as you register the event handler. |
    | `SystemEvents.SystemShutdown.EventName`       | N/A                     | N/A                                      | When  the system power-off has been started. | You  can treat the initial value as `false` before you receive this event. If the application is already  in a shutting-down state before you register an event handler, you receive  the event as soon as you register the event handler. |

- resourced

  - ram memory

    | Event name | Event data Key | Event data Value | Condition | Notes |
    |-------|-------|--------|--------|--------|
    | `SystemEvents.LowMemory.EventName`            | `SystemEvents.LowMemory.Key`              | - `SystemEvents.LowMemory.ValueNormal`:  Available > 200MB <br> - `SystemEvents.LowMemory.ValueSoftWarning`: 100MB < available <= 200MB <br>- `SystemEvents.LowMemory.ValueHardWarning`: Available <= 100MB    <br> **Note**<br> The above numbers can vary depending on the total RAM size of the  target device. | When  the size of available memory has changed. | If  there is an earlier occurrence regarding this event, you receive the event as  soon as you register an event handler for this event. You can use this  earlier event data as the initial value. |

- network

  - connectivity

    | Event name | Event data Key | Event data Value | Condition | Notes |
    |-------|-------|--------|--------|--------|
    | `SystemEvents.WifiState.EventName`            | `SystemEvents.WifiState.StateKey`             | - `SystemEvents.WifiState.StateValueOn`:  Wi-Fi on <br>-  `SystemEvents.WifiState.StateValueOff`: Wi-Fi off <br>- `SystemEvents.WifiState.StateValueConnected`: Wi-Fi connection established | When the Wi-Fi  state has changed.       | You can get the  current value with the `Network.Connection.ConnectionManager.WiFiState` property. |
    | `SystemEvents.Btstate.EventName`              | `SystemEvents.Btstate.StateKey`               | - `SystemEvents.Btstate.StateValueOff`:  Legacy Bluetooth off <br>-  `SystemEvents.Btstate.StateValueOn`: Legacy Bluetooth on | When the  Bluetooth state has changed.   | You can get the  current value with the `Network.Bluetooth.BluetoothAdapter.IsBluetoothEnabled` property. |
    | `SystemEvents.Btstate.EventName`              | `SystemEvents.Btstate.LeStateKey`             | - `SystemEvents.Btstate.LeStateValueOff`:  LE function off <br>- `SystemEvents.Btstate.LeStateValueOn`: LE function on | When Bluetooth  LE state has changed.    |   -                                       |
    | `SystemEvents.Btstate.EventName`              | `SystemEvents.Btstate.TransferStateKey`       | - `SystemEvents.Btstate.TransferStateValueNontransfering`:  Idle state  <br>-  `SystemEvents.Btstate.TransferStateValueTransfering`: File is transferring | When the file  transfer state has changed. | -                                         |    

- libslp-location

  - location

    | Event name | Event data Key | Event data Value | Condition | Notes |
    |-------|-------|--------|--------|--------|
    | `SystemEvents.LocatingEnableState.EventName` | `SystemEvents.LocatingEnableState.StateKey`   | - `SystemEvents.LocatingEnableState.StateValueDisabled`:  Location disabled <br>-  `SystemEvents.LocatingEnableState.StateValueEnabled`: Location enabled | When the `location_enable_state` has  changed, for example, by the user toggling the location setting in the  settings menu or quick panel. | You can get the  current value with the `Location.LocatorHelper.IsEnabledType` property. |
    | `SystemEvents.GpsEnableState.EventName`      | `SystemEvents.GpsEnableState.StateKey`        | - `SystemEvents.GpsEnableState.StateValueDisabled`:  GPS disabled  <br>- `SystemEvents.GpsEnableState.StateValueEnabled`: GPS enabled | When the `gps_enable_state` has changed.   | You can get the  current value with the `Location.LocatorHelper.IsEnabledType` property. |
    | `SystemEvents.NpsEnableState.EventName`      | `SystemEvents.NpsEnableState.StateKey`        | - `SystemEvents.NpsEnableState.StateValueDisabled`:  NPS disabled <br>-  `SystemEvents.NpsEnableState.StateValueEnabled`: NPS enabled | When the NPS  setting has changed, for example, by the user toggling the location  settings. | You can get the  current value with the `Location.LocatorHelper.IsEnabledType` property. |

- msg-service

  - message

    | Event name | Event data Key | Event data Value | Condition | Notes |
    |-------|-------|--------|--------|--------|
    | `SystemEvents.IncomingMsg.EventName`          | `SystemEvents.IncomingMsg.TypeKey`                | - `SystemEvents.IncomingMsg.TypeValueSms`:  SMS-type message <br>-  `SystemEvents.IncomingMsg.TypeValueMms`: MMS-type message <br>-  `SystemEvents.IncomingMsg.TypeValuePush`: Push-type message <br>-  `SystemEvents.IncomingMsg.TypeValueCb`: Cb-type message | When an SMS, MMS, push, or CB message has been received. |       -                                   |
    | `SystemEvents.IncomingMsg.EventName`          | `SystemEvents.IncomingMsg.IdKey`                  | `msg_id`: Message ID of the received message (string of the unsigned `int` type value) | -                                         |           -                               |
    | `SystemEvents.OutgoingMsg.EventName`          | `SystemEvents.OutgoingMsg.TypeKey`                | - `SystemEvents.OutgoingMsg.TypeValueSms`:  SMS-type message <br>-  `SystemEvents.OutgoingMsg.TypeValueMms`: MMS-type message | When an SMS or MMS message has been sent. |       -                                   |
    | `SystemEvents.OutgoingMsg.EventName`          | `SystemEvents.OutgoingMsg.IdKey`                  | `msg_id`: Message ID of the sent message (string of the unsigned `int` type value) | -                                         |           -                               |
    
- alarm-manager

  - time

    | Event name | Event data Key | Event data Value | Condition | Notes |
    |-------|-------|--------|--------|--------|
    | `SystemEvents.TimeChanged.EventName`          | N/A                     | N/A                                      | When  the system time setting has changed. | You  can get the current value with the `Applications.AlarmManager.GetCurrentTime` method. |

- setting

  - time

    | Event name | Event data Key | Event data Value | Condition | Notes |
    |-------|-------|--------|--------|--------|
    | `SystemEvents.TimeZone.EventName`             | `SystemEvents.TimeZone.Key`               | The  value of this key is the time zone value of the time zone database, for  example, "Asia/Seoul", "America/New_York". For more  information, see the IANA Time Zone Database. | When  the time zone has changed.         | You  can get the current value with the `System.SystemSettings.LocaleTimeZone` property. |

  - locale

    | Event name | Event data Key | Event data Value | Condition | Notes |
    |-------|-------|--------|--------|--------|
    | `SystemEvents.HourFormat.EventName`           | `SystemEvents.HourFormat.Key`             | - `SystemEvents.HourFormat.Value12` <br>- `SystemEvents.HourFormat.Value24`                             | When  the `hour_format` has changed,  for example, by the user toggling the date and time settings for the 24-hour  clock (where **OFF** stands  for the 12-hour clock). | You  can get the current value with the `System.SystemSettings.LocaleTimeFormat24HourEnabled` property. |
    | `SystemEvents.LanguageSet.EventName`          | `SystemEvents.LanguageSet.Key`           | The value of  this key is the full name of the locale, for example, `ko_KR.UTF8` for Korean and `en_US.UTF8` for American English. For more information, see the Linux  locale information. | When the `language_set` has changed.       | You can get the  current value with the `System.SystemSettings.LocaleLanguage` property. |
    | `SystemEvents.RegionFormat.EventName`         | `SystemEvents.RegionFormat.Key`           | The  value of this key is the full name of the locale, for example, `ko_KR.UTF8` for the Korean region  format and `en_US.UTF8`  for the USA region format. For more information, see the Linux locale  information. | When  the `region_format` has changed.     | You  can get the current value with the `System.SystemSettings.LocaleCountry` property. |

  - sound

    | Event name | Event data Key | Event data Value | Condition | Notes |
    |-------|-------|--------|--------|--------|
    | `SystemEvents.SilentMode.EventName`           | `SystemEvents.SilentMode.Key`             | - `SystemEvents.SilentMode.ValueOn` <br> - `SystemEvents.SilentMode.ValueOff`                            | When  the ringtone has changed to 0 or another mode. For example, if the call  slider has been changed to 0, `silent_mode` is `"on"`. Otherwise, `silent_mode` is `"off"`. | You  can get the current value with the `System.SystemSettings.SoundSilentModeEnabled` property. |

  - vibration

    | Event name | Event data Key | Event data Value | Condition | Notes |
    |-------|-------|--------|--------|--------|
    | `SystemEvents.VibrationState.EventName`       | `SystemEvents.VibrationState.StateKey`          | - `SystemEvents.VibrationState.StateValueOn` <br> - `SystemEvents.VibrationState.StateValueOff`                           | When the  vibration state has changed.   | You can get the current value using `System.Information.SetCallback` with the `http://tizen.org/runtimefeature/vibration` property. |

  - screen

    | Event name | Event data Key | Event data Value | Condition | Notes |
    |-------|-------|--------|--------|--------|
    | `SystemEvents.AutoRotateState.EventName` | `SystemEvents.AutoRotateState.StateKey` | - `SystemEvents.AutoRotateState.StateOn` <br> - `SystemEvents.AutoRotateState.StateOff`                      | When the screen autorotate state  has  changed, for example, by the user toggling the display settings. | You can get the  current value with the `System.SystemSettings.DisplayScreenRotationAutoEnabled` property. |

  - mobile

    | Event name | Event data Key | Event data Value | Condition | Notes |
    |-------|-------|--------|--------|--------|
    | `SystemEvents.MobileDataState.EventName`     | `SystemEvents.MobileDataState.StateKey`       | - `SystemEvents.MobileDataState.StateValueOn` <br> - `SystemEvents.MobileDataState.StateValueOff`            | When the mobile data state has changed,  for example, by the user toggling the network settings. | You can get the  current value with the `System.SystemSettings.Data3GNetworkEnabled` property. |
    | `SystemEvents.DataRoamingState.EventName`    | `SystemEvents.DataRoamingState.StateKey`      | - `SystemEvents.DataRoamingState.StateValueOn` <br> - `SystemEvents.DataRoamingState.StateValueOff`                   | When the data roaming state  has changed,  for example, by the user toggling the network settings. | You can get the current value using `System.Information.SetCallback` with the `http://tizen.org/runtimefeature/dataroaming` key. |

  - font

    | Event name | Event data Key | Event data Value | Condition | Notes |
    |-------|-------|--------|--------|--------|
    | `SystemEvents.FontSet.EventName`              | `SystemEvents.FontSet.Key`                | The value of  this key is the font name of the string type by font-config. | When the font  has changed.              | You can get the  current value with the `System.SystemSettings.FontType` property. |


## Related Information
* Dependencies
  - Tizen 5.5 and Higher
