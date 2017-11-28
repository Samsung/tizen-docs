Attached Devices
================

## Dependencies

- Tizen 4.0 and Higher

You can control attached devices and monitor device changes in your
application.

The main features of the device control include:

-   Battery information

    You can [get battery details](#battery), such as the current
    percentage, the charging state, and the current level state.

- Device control

    You can manage various components and elements on the device:

    -   Display

        You can [get and set display details](#display), such as the
        number of displays, the maximum brightness of the display, the
        current brightness, and the display state.

    - Haptic

        You can [manage haptic devices](#haptic) by, for example,
        getting the number of haptic devices, opening or closing the
        haptic handle, and requesting vibration effect playback.

    - IR

        You can [manage IR devices](#ir) by, for example, determining
        whether an IR device is available and transmitting an
        IR pattern.

    - LED

        You can [manage the camera flash LED](#led) by, for example,
        getting the maximum and current brightness of the LED. You can
        also change the current brightness of the camera flash LED, and
        request the service LED to play effects.

    - Power

        You can [request the power state](#power) to be locked
        or unlocked.

- Change monitoring

    You can [register an event handler to monitor device
    changes](#changes).



Prerequisites
-------------

To enable your application to use the device control functionality:

1.  To use the [Tizen.System.Display](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1System_1_1Display.html), [Tizen.System.Led](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1System_1_1Led.html), and [Tizen.System.Vibrator](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1System_1_1Vibrator.html)
    classes, the application has to request permission by adding the
    following privileges to the `tizen-manifest.xml` file:

    ``` {.prettyprint}
    <privileges>
       <!--To use the Display class -->
       <privilege>http://tizen.org/privilege/display</privilege>
       <!--To use the Vibrator class -->
       <privilege>http://tizen.org/privilege/haptic</privilege>
       <!--To use the Led class -->
       <privilege>http://tizen.org/privilege/led</privilege>
    </privileges>
    ```

2. To use the methods and properties of the [Tizen.System](https://developer.tizen.org/dev-guide/csapi/namespaceTizen_1_1System.html) namespace classes, include the namespace in your application:

    ``` {.prettyprint}
    using Tizen.System;
    ```



Retrieving Battery Information <a id="battery"></a>
------------------------------

To retrieve battery information:

-   Get the battery charge percentage with the `Percent` property of the
    [Tizen.System.Battery](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1System_1_1Battery.html) class.

    The property contains the current battery charge percentage as an
    integer value from 0 to 100 that indicates the remaining battery
    charge as a percentage of the maximum level.

    ``` {.prettyprint}
    int s_Percent;
    s_Percent = Battery.Percent;
    ```

- Get the current battery charging state with the
    `IsCharging` property.

    The property contains the device battery charging state as `TRUE` or
    `FALSE`.

    ``` {.prettyprint}
    bool charging;
    charging = Battery.IsCharging;
    ```

- Get the current battery level with the `Level` property.

    The property contains the device battery level as a value of the
    [Tizen.System.BatteryLevelStatus](https://developer.tizen.org/dev-guide/csapi/namespaceTizen_1_1System.html#ae27f4a8d7a61d29a49a265c337116df8) enumeration.

    ``` {.prettyprint}
    BatteryLevelStatus status;
    status = Battery.Level;
    ```



Controlling the Display <a id="display"></a>
-----------------------

To retrieve and set display properties:

-   Get the number of display devices with the `NumberOfDisplays`
    property of the
    [Tizen.System.Display](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1System_1_1Display.html)
    class:

    ``` {.prettyprint}
    int num;
    num = Display.NumberOfDisplays;
    ```

- Get the maximum possible brightness with the `MaxBrightness`
    property:

    ``` {.prettyprint}
    Display dis = Display.Displays[0];

    int maxBrightness = dis.MaxBrightness;
    ```

- Get and set the display brightness with the `Brightness` property:

    ``` {.prettyprint}
    Display dis = Display.Displays[0];

    int curBrightness = 0;
    curBrightness = dis.Brightness;
    dis.Brightness = 30;
    ```

- Get the display state with the `State` property.

    The property contains the display state as a value of the
    [Tizen.System.DisplayState](https://developer.tizen.org/dev-guide/csapi/namespaceTizen_1_1System.html#a04b41846384e5a4eec93b3439af7f289) enumeration.

    ``` {.prettyprint}
    DisplayState state;
    state = Display.State;
    ```



Controlling Haptic Devices <a id="haptic"></a>
--------------------------

To control haptic devices:

-   Get the number of haptic devices with the `NumberOfVibrators`
    property of the
    [Tizen.System.Vibrator](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1System_1_1Vibrator.html)
    class:

    ``` {.prettyprint}
    int num;
    num = Vibrator.NumberOfVibrators;
    ```

- Play and stop an effect on a given haptic device with the
    `Vibrate()` and `Stop()` methods.

    The device vibrates for a specified time with a constant intensity.
    The effect handle can be 0.

    ``` {.prettyprint}
    Vibrator vib = Vibrator.Vibrators[0];
    vib.Vibrate(3000, 50);

    vib.Stop();
    ```



Controlling IR Devices <a id="ir"></a>
----------------------

To control an IR device:

1.  Determine whether IR is available on the device using the
    `IsAvailable` property of the
    [Tizen.System.IR](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1System_1_1IR.html)
    class:

    ``` {.prettyprint}
    bool test;
    test = IR.IsAvailable;
    ```

2. Transmit an IR pattern with a specific carrier frequency using the
    `Transmit()` method:

    ``` {.prettyprint}
    List<int> pattern = new List<int>();
    pattern.Add(10);
    pattern.Add(50);
    IR.Transmit(10, pattern);
    ```



Controlling LED Devices <a id="led"></a>
-----------------------

To control LEDs on the device:

-   Get the maximum brightness value of a camera flash LED with the
    `MaxBrightness` property of the
    [Tizen.System.Led](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1System_1_1Led.html)
    class:

    ``` {.prettyprint}
    int test;
    test = Led.MaxBrightness;
    ```

- Get and set the current brightness value of a camera flash LED with
    the `Brightness` property:

    ``` {.prettyprint}
    int test;
    test = Led.Brightness;

    Led.Brightness = 45;
    ```

- Play and stop a custom effect on the service LED that is located on
    the front of the device with the `Play()` and `Stop()` methods:

    ``` {.prettyprint}
    var t = Task.Run(async delegate
    {
        await Task.Delay(1000);

        return 0;
    });

    Led.Play(500, 200, Color.FromRgba(255, 255, 255, 1));
    t.Wait();

    Led.Stop();
    ```



Controlling the Power State  <a id="power"></a>
---------------------------

To lock and unlock the CPU state:

-   Lock the power state with the `RequestCpuLock()` method of the
    [Tizen.System.Power](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1System_1_1Power.html) class.

    The method locks the CPU for a specified time. After the given time
    (in milliseconds), the lock is unlocked. If the process is
    destroyed, every lock is removed.

    ``` {.prettyprint}
    Power.RequestCpuLock(2000);
    ```

- Unlock the power state with the `ReleaseCpuLock()` method:

    ``` {.prettyprint}
    Power.ReleaseCpuLock();
    ```



Monitoring Device Changes <a id="changes"></a>
-------------------------

To monitor device changes, use event handlers registered to the
following events:

-   `LevelChanged` and `PercentChanged` events in the
    [Tizen.System.Battery](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1System_1_1Battery.html)
    class are called when the battery level and charge
    percentage change.
-   `ChargingStateChanged` event in the
    [Tizen.System.Battery](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1System_1_1Battery.html)
    class is called when the charger is connected or disconnected.
-   `StateChanged` event in the
    [Tizen.System.Display](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1System_1_1Display.html)
    class is called when the device display state changes.
-   `BrightnessChanged` event in the
    [Tizen.System.Led](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1System_1_1Led.html)
    class is called when LED brightness changes.

To manage device display status change events:

1.  Define an event handler:

    ``` {.prettyprint}
    public static void DisplayEventHandler()
    {
        EventHandler<DisplayStateChangedEventArgs> handler = null;
        handler = (object sender, DisplayStateChangedEventArgs args);
        Log.Debug(LogTag, string.Format("Display State:: {0}", value));
    }
    ```

2. Register the event handler for the `StateChanged` event of the
    `Tizen.System.Display` class:

    ``` {.prettyprint}
    Display.StateChanged += handler;
    ```

3. When no longer needed, deregister the event handler:

    ``` {.prettyprint}
    Display.StateChanged -= handler;
    ```


