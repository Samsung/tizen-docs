# Attached Devices


You can control attached devices and monitor device changes in your application.

The main features of the device control include:

-   Battery information

    You can [get battery details](#battery), such as the current percentage, the charging state, and the current level state.

-   Device control

    You can manage various components and elements on the device:

    -   Display

        You can [get and set display details](#display), such as the number of displays, the maximum brightness of the display, the current brightness, and the display state.

    -   Haptic

        You can [manage haptic devices](#haptic) by, for example, getting the number of haptic devices, opening or closing the haptic handle, and requesting vibration effect playback.

    -   IR

        You can [manage IR devices](#ir) by, for example, determining whether an IR device is available and transmitting an IR pattern.

    -   LED

        You can [manage the camera flash LED](#led) by, for example, getting the maximum and current brightness of the LED. You can also change the current brightness of the camera flash LED, and request the service LED to play effects.

    -   Power

        You can [request the power state](#power) to be locked or unlocked.

-   Change monitoring

    You can [register an event handler to monitor device changes](#changes).

## Prerequisites

To enable your application to use the attached device control functionality:

1.  To use the [Tizen.System.Display](https://developer.tizen.org/dev-guide/csapi/api/Tizen.System.Display.html), [Tizen.System.Led](https://developer.tizen.org/dev-guide/csapi/api/Tizen.System.Led.html), and [Tizen.System.Vibrator](https://developer.tizen.org/dev-guide/csapi/api/Tizen.System.Vibrator.html) classes, the application has to request permission by adding the following privileges to the `tizen-manifest.xml` file:

    ```
    <privileges>
       <!--To use the Display class -->
       <privilege>http://tizen.org/privilege/display</privilege>
       <!--To use the Vibrator class -->
       <privilege>http://tizen.org/privilege/haptic</privilege>
       <!--To use the Led class -->
       <privilege>http://tizen.org/privilege/led</privilege>
    </privileges>
    ```

2.  To use the methods and properties of the [Tizen.System](https://developer.tizen.org/dev-guide/csapi/api/Tizen.System.html) namespace classes, include the namespace in your application:

    ```
    using Tizen.System;
    ```

## Retrieving Battery Information

To retrieve battery information:

-   Get the battery charge percentage with the `Percent` property of the [Tizen.System.Battery](https://developer.tizen.org/dev-guide/csapi/api/Tizen.System.Battery.html) class.

    The property contains the current battery charge percentage as an integer value from 0 to 100 that indicates the remaining battery charge as a percentage of the maximum level.

    ```
    int s_Percent;
    s_Percent = Battery.Percent;
    ```

-   Get the current battery charging state with the `IsCharging` property.

    The property contains the device battery charging state as `TRUE` or `FALSE`.

    ```
    bool charging;
    charging = Battery.IsCharging;
    ```

-   Get the current battery level with the `Level` property.

    The property contains the device battery level as a value of the [Tizen.System.BatteryLevelStatus](https://developer.tizen.org/dev-guide/csapi/api/Tizen.System.BatteryLevelStatus.html) enumeration.

    ```
    BatteryLevelStatus status;
    status = Battery.Level;
    ```

<a name="display"></a>
## Controlling the Display

To retrieve and set display properties:

-   Get the number of display devices with the `NumberOfDisplays` property of the [Tizen.System.Display](https://developer.tizen.org/dev-guide/csapi/api/Tizen.System.Display.html) class:

    ```
    int num;
    num = Display.NumberOfDisplays;
    ```

-   Get the maximum possible brightness with the `MaxBrightness` property:

    ```
    Display dis = Display.Displays[0];

    int maxBrightness = dis.MaxBrightness;
    ```

-   Get and set the display brightness with the `Brightness` property:

    ```
    Display dis = Display.Displays[0];

    int curBrightness = 0;
    curBrightness = dis.Brightness;
    dis.Brightness = 30;
    ```

-   Get the display state with the `State` property.

    The property contains the display state as a value of the [Tizen.System.DisplayState](https://developer.tizen.org/dev-guide/csapi/api/Tizen.System.DisplayState.html) enumeration.

    ```
    DisplayState state;
    state = Display.State;
    ```

<a name="haptic"></a>
## Controlling Haptic Devices

To control haptic devices:

-   Get the number of haptic devices with the `NumberOfVibrators` property of the [Tizen.System.Vibrator](https://developer.tizen.org/dev-guide/csapi/api/Tizen.System.Vibrator.html) class:

    ```
    int num;
    num = Vibrator.NumberOfVibrators;
    ```

-   Play and stop an effect on a given haptic device with the `Vibrate()` and `Stop()` methods.

    The device vibrates for a specified time with a constant intensity. The effect handle can be 0.

    ```
    Vibrator vib = Vibrator.Vibrators[0];
    vib.Vibrate(3000, 50);

    vib.Stop();
    ```

<a name="ir"></a>
## Controlling IR Devices

To control an IR device:

1.  Determine whether IR is available on the device using the `IsAvailable` property of the [Tizen.System.IR](https://developer.tizen.org/dev-guide/csapi/api/Tizen.System.IR.html) class:

    ```
    bool test;
    test = IR.IsAvailable;
    ```

2.  Transmit an IR pattern with a specific carrier frequency using the `Transmit()` method:

    ```
    List<int> pattern = new List<int>();
    pattern.Add(10);
    pattern.Add(50);
    IR.Transmit(10, pattern);
    ```

<a name="led"></a>
## Controlling LED Devices
To control LEDs on the device:

-   Get the maximum brightness value of a camera flash LED with the `MaxBrightness` property of the [Tizen.System.Led](https://developer.tizen.org/dev-guide/csapi/api/Tizen.System.Led.html) class:

    ```
    int test;
    test = Led.MaxBrightness;
    ```

-   Get and set the current brightness value of a camera flash LED with the `Brightness` property:

    ```
    int test;
    test = Led.Brightness;

    Led.Brightness = 45;
    ```

-   Play and stop a custom effect on the service LED that is located on the front of the device with the `Play()` and `Stop()` methods:

    ```
    var t = Task.Run(async delegate
    {
        await Task.Delay(1000);

        return 0;
    });

    Led.Play(500, 200, Color.FromRgba(255, 255, 255, 1));
    t.Wait();

    Led.Stop();
    ```

<a name="power"></a>
## Controlling the Power State

To lock and unlock the CPU state:

-   Lock the power state with the `RequestCpuLock()` method of the [Tizen.System.Power](https://developer.tizen.org/dev-guide/csapi/api/Tizen.System.Power.html) class.

    The method locks the CPU for a specified time. After the given time (in milliseconds), the lock is unlocked. If the process is destroyed, every lock is removed.

    ```
    Power.RequestCpuLock(2000);
    ```

-   Unlock the power state with the `ReleaseCpuLock()` method:

    ```
    Power.ReleaseCpuLock();
    ```

<a name="changes"></a>
## Monitoring Device Changes

To monitor device changes, use event handlers registered to the following events:

-   `LevelChanged` and `PercentChanged` events in the [Tizen.System.Battery](https://developer.tizen.org/dev-guide/csapi/api/Tizen.System.Battery.html) class are called when the battery level and charge percentage change.
-   `ChargingStateChanged` event in the [Tizen.System.Battery](https://developer.tizen.org/dev-guide/csapi/api/Tizen.System.Battery.html) class is called when the charger is connected or disconnected.
-   `StateChanged` event in the [Tizen.System.Display](https://developer.tizen.org/dev-guide/csapi/api/Tizen.System.Display.html) class is called when the device display state changes.
-   `BrightnessChanged` event in the [Tizen.System.Led](https://developer.tizen.org/dev-guide/csapi/api/Tizen.System.Led.html) class is called when LED brightness changes.

To manage device display status change events:

1.  Define an event handler:

    ```
    public static void DisplayEventHandler()
    {
        EventHandler<DisplayStateChangedEventArgs> handler = null;
        handler = (object sender, DisplayStateChangedEventArgs args);
        Log.Debug(LogTag, string.Format("Display State:: {0}", value));
    }
    ```

2.  Register the event handler for the `StateChanged` event of the `Tizen.System.Display` class:

    ```
    Display.StateChanged += handler;
    ```

3.  When no longer needed, deregister the event handler:

    ```
    Display.StateChanged -= handler;
    ```


## Related Information
* Dependencies
  -   Tizen 4.0 and Higher
