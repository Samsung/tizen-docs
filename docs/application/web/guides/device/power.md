# Power States

You can access a device's power resources. Currently, the screen and CPU power resources are supported, allowing you to request a specific power state and control the brightness of the screen.

This feature is optional.

The main features of the Power API include the following:

- Managing power resources

  You can [request and release a specific power state](#managing-power-resources).

- Managing the screen brightness

  You can [get and set the screen brightness](#managing-the-screen-brightness).

- Managing the screen state

  You can [switch the screen on and off](#managing-the-screen-state), and check whether the screen is on.

## Prerequisites

To use the Power API, the application has to request permission by adding the following privilege to the `config.xml` file:

```
<tizen:privilege name="http://tizen.org/privilege/power"/>
```

## Manage power resources

You can request and release a minimum power state for the screen and CPU. The request locks the screen to a minimum state and keeps the device bright and awake. For example, if you set the minimum power state to `SCREEN_NORMAL`, the device display always remains in the `SCREEN_NORMAL` level and never goes down to the `SCREEN_DIM` level.

The following table lists the levels you can request.

**Table: Power state levels**

| Level           | Description                              |
| --------------- | ---------------------------------------- |
| `SCREEN_OFF`    | In this state, the screen is off. You cannot request this state, but it can be used in event handlers. |
| `SCREEN_DIM`    | In this state, the screen is dimmed. When this state is requested, the device does not go to the `SCREEN_OFF` state automatically. |
| `SCREEN_NORMAL` | In this state, the screen uses the default brightness the user has configured for the device. When this state is requested, the device does not go to the `SCREEN_DIM` state automatically. |
| `CPU_AWAKE`     | In this state, the CPU is awake. When this state is requested, the device does not go to `SLEEP` state automatically. |

> [!NOTE]
> If you request a new power state without releasing the previous state, the Tizen platform follows the highest minimum state requested.

To request and release the power state:

1. To set the power state, call the `request()` method of the `PowerManager` interface with the intended power resource and its state. In this example, the `SCREEN_NORMAL` state is requested for the screen resource:

   ```
   tizen.power.request('SCREEN', 'SCREEN_NORMAL');
   ```

2. To release a power state, call the `release()` method with the intended resource:

   ```
   tizen.power.release('SCREEN');
   ```

3. To listen for the screen state changes, use the `setScreenStateChangeListener()` method:

   ```
   function onScreenStateChanged(previousState, changedState) {
       console.log('Screen state changed from' + previousState + 'to' + changedState);
   }
   tizen.power.setScreenStateChangeListener(onScreenStateChanged);
   ```

4. To unset the screen state change callback and stop monitoring it, use the `unsetScreenStateChangeListener()` method:

   ```
   tizen.power.unsetScreenStateChangeListener();
   ```

## Manage the screen brightness

To get, set, and restore the screen brightness, follow these steps:

- To get the screen brightness, call the `getScreenBrightness()` method of the `PowerManager` interface:

  ```
  var screenBrightness = tizen.power.getScreenBrightness();
  ```

- To set the screen brightness, call the ` setScreenBrightness()` method of   the `PowerManager` interface with the value from 0 to 1.

  In this example, the screen brightness is set to `1` (the brightest setting):

  ```
  tizen.power.setScreenBrightness(1);
  ```

- To restore the default screen brightness, use the `restoreScreenBrightness()` method of the `PowerManager` interface:

  ```
  tizen.power.restoreScreenBrightness();
  ```

## Manage the screen state

To check whether the screen is on, call the `isScreenOn()` method of the `PowerManager` interface:

```
var isScreenOn = tizen.power.isScreenOn();
```

## Related information
* Dependencies
  - Tizen 2.4 and Higher
