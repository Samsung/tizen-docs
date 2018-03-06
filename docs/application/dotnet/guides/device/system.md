# System Information


You can access various information about your device system and its runtime status.

The main system information features include:

-   Retrieving system information

    You can [access system information](#information), such as platform features or device capabilities, using the [Tizen.System.Information](https://developer.tizen.org/dev-guide/csapi/api/Tizen.System.Information.html) class.

- Retrieving resource usage details

    You can [retrieve the resource usage details](#usage) of the device or a particular process by using the [Tizen.System.ProcessCpuUsage](https://developer.tizen.org/dev-guide/csapi/api/Tizen.System.ProcessCpuUsage.html), [Tizen.System.ProcessMemoryUsage](https://developer.tizen.org/dev-guide/csapi/api/Tizen.System.ProcessMemoryUsage.html), [Tizen.System.SystemCpuUsage](https://developer.tizen.org/dev-guide/csapi/api/Tizen.System.SystemCpuUsage.html), and [Tizen.System.SystemMemoryUsage](https://developer.tizen.org/dev-guide/csapi/api/Tizen.System.SystemMemoryUsage.html) classes.

- Monitoring runtime changes

    You can register a callback with the `Tizen.System.Information` class to [receive notifications](#callback) when a specific feature changes at runtime.

System information features are classified as either static features, which are device features whose value does not change, or runtime features, whose value can change according to, for example, what peripherals are currently connected to the device. The features are identified using [feature keys](#runtimefeaturekey).


## Prerequisites

To enable your application to use the system information functionality:

1.  To access per-process resource information (to use the [Tizen.System.ProcessCpuUsage](https://developer.tizen.org/dev-guide/csapi/api/Tizen.System.ProcessCpuUsage.html) and [Tizen.System.ProcessMemoryUsage](https://developer.tizen.org/dev-guide/csapi/api/Tizen.System.ProcessMemoryUsage.html) classes), the application has to request permission by adding the following privilege to the `tizen-manifest.xml` file:

    ```
    <privileges>
       <privilege>http://tizen.org/privilege/systemmonitor</privilege>
    </privileges>
    ```

2. To use the methods and properties of the [Tizen.System.Information](https://developer.tizen.org/dev-guide/csapi/api/Tizen.System.Information.html), `Tizen.System.ProcessCpuUsage`, `Tizen.System.ProcessMemoryUsage`, [Tizen.System.SystemCpuUsage](https://developer.tizen.org/dev-guide/csapi/api/Tizen.System.SystemCpuUsage.html), and [Tizen.System.SystemMemoryUsage](https://developer.tizen.org/dev-guide/csapi/api/Tizen.System.SystemMemoryUsage.html) classes, include the [Tizen.System](https://developer.tizen.org/dev-guide/csapi/api/Tizen.System.html) namespace in your application:

    ```
    using Tizen.System;
    ```

<a name="information"></a>
## Retrieving System Information

To retrieve system information, use the `TryGetValue()` method of the [Tizen.System.Information](https://developer.tizen.org/dev-guide/csapi/api/Tizen.System.Information.html) class:

-   To retrieve a static feature:

    ```
    /// Check whether the device has a battery
    public static bool is_battery_powered_device()
    {
        bool ret;

        if (Tizen.System.Information.TryGetValue<bool>("http://tizen.org/feature/battery", out ret) == false)
        {
            /// Error handling
        }

        return ret;
    }
    ```

- To retrieve the current value of a runtime feature:

    ```
    /// Check whether the battery is charging
    public static bool is_charging()
    {
        bool ret;

        if (Tizen.System.Information.TryGetValue<bool>("http://tizen.org/runtimefeature/battery.charging", out ret) == false)
        {
            /// Error handling
        }

        return ret;
    }
    ```

<a name="usage"></a>
## Retrieving Resource Usage Details

To get resource usage details, use the [Tizen.System.ProcessCpuUsage](https://developer.tizen.org/dev-guide/csapi/api/Tizen.System.ProcessCpuUsage.html), [Tizen.System.ProcessMemoryUsage](https://developer.tizen.org/dev-guide/csapi/api/Tizen.System.ProcessMemoryUsage.html), [Tizen.System.SystemCpuUsage](https://developer.tizen.org/dev-guide/csapi/api/Tizen.System.SystemCpuUsage.html), and [Tizen.System.SystemMemoryUsage](https://developer.tizen.org/dev-guide/csapi/api/Tizen.System.SystemMemoryUsage.html) classes. Since these classes collect information during their construction, you can simply make a new instance to access the resource usage details.

-   To retrieve system memory usage details:

    ```
    public static int get_total_memory_size(void)
    {
        Tizen.System.SystemMemoryUsage usage = new Tizen.System.SystemMemoryUsage();

        return usage.Total;
    }
    ```

- To retrieve CPU usage details of a process:

    ```
    public static void print_family_cpu_usage(Familyinfo family)
    {
        IList<int> processList;
        Tizen.System.ProcessCpuUsage usage;

        processList = new List<int>();
        processList.Add(family.me.pid);
        processList.Add(family.father.pid);

        usage = new Tizen.System.ProcessCpuUsage(processList);

        Tizen.Log.Info("MY_HOUSE", "My CPU UTime = " + usage.GetUTime(family.me.pid));
        Tizen.Log.Info("MY_HOUSE", "Father's CPU STime = " + usage.GetSTime(family.father.pid));
    }
    ```

<a name="callback"></a>
## Monitoring Runtime Changes

You can monitor the changes in the runtime feature key values by registering event handlers for the corresponding events.

For example, to monitor whether an audio jack is connected, and to turn the device volume to safe levels when it is:

```
private const string RuntimeFeatureAudiojackConnected = "http://tizen.org/runtimefeature/audiojack.connected";

/// Event handler for the audio jack connection event
public static void TurnDownTheVolumeCallback(object sender, RuntimeFeatureStatusChangedEventArgs args)
{
    if (MySpeaker.GetVolume() > 10)
    {
        MySpeaker.SetVolume(10);
    }
}

/// To begin monitoring, register the event handler for the audiojack.connected event
public static void init()
{
    Tizen.System.Information.SetCallback(RuntimeFeatureAudiojackConnected, TurnDownTheVolumeCallback);
}

/// When monitoring is no longer needed, deregister the event handler
public static void deinit()
{
    Tizen.System.Information.UnsetCallback(RuntimeFeatureAudiojackConnected, TurnDownTheVolumeCallback);
}
```

<a name="runtimefeaturekey"></a>
## Feature Keys

The static feature keys are identical to the ones used in Tizen native applications. For more information, see the native [System Information](../../../native/guides/device/system.md#feature) guide.

The runtime feature keys have the `runtimefeature` prefix. The available runtime feature keys are listed in the following table.

**Table: Runtime feature keys**

| Key                                      | Type   | Description                              |
|----------------------------------------|------|----------------------------------------|
| `http://tizen.org/runtimefeature/audiojack.connected` | `bool` | Indicates whether an audio jack is connected. |
| `http://tizen.org/runtimefeature/audiojack.type` | `int`  | Indicates the audio jack connector type. For available values, see the [Tizen.System.AudioJackConnectionType](https://developer.tizen.org/dev-guide/csapi/api/Tizen.System.AudioJackConnectionType.html) enumeration. |
| `http://tizen.org/runtimefeature/autorotation` | `bool` | Indicates whether auto-rotation is enabled. |
| `http://tizen.org/runtimefeature/battery.charging` | `bool` | Indicates whether the battery is currently charging. |
| `http://tizen.org/runtimefeature/bluetooth` | `bool` | Indicates whether Bluetooth is enabled.  |
| `http://tizen.org/runtimefeature/charger` | `bool` | Indicates whether a charger is connected. |
| `http://tizen.org/runtimefeature/dataroaming` | `bool` | Indicates whether data roaming is enabled. |
| `http://tizen.org/runtimefeature/gps`    | `int`  | Indicates the current GPS status. For available values, see the [Tizen.System.GpsStatus](https://developer.tizen.org/dev-guide/csapi/api/Tizen.System.GpsStatus.html) enumeration. |
| `http://tizen.org/runtimefeature/packetdata` | `bool` | Indicates whether packet data is enabled through the 3G network. |
| `http://tizen.org/runtimefeature/tethering.bluetooth` | `bool` | Indicates whether Bluetooth tethering is enabled. |
| `http://tizen.org/runtimefeature/tethering.usb` | `bool` | Indicates whether USB tethering is enabled. |
| `http://tizen.org/runtimefeature/tethering.wifi` | `bool` | Indicates whether a Wi-Fi hotspot is enabled. |
| `http://tizen.org/runtimefeature/tvout`  | `bool` | Indicates whether the TV out is connected. |
| `http://tizen.org/runtimefeature/vibration` | `bool` | Indicates whether vibration is enabled.  |


## Related Information
* Dependencies
  -   Tizen 4.0 and Higher
