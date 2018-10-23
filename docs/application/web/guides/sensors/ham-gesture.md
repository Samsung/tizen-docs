# Gesture Recognition

You can set your application to recognize specific user gestures and react when the user performs them. The various recognizable gestures include, for example, when the user taps, shakes up, or picks up the device, or moves it along an axis.

This feature is supported in mobile and wearable applications only.

The main gesture recognition features of the Human Activity Monitor API include:

- Checking the gesture support

  You can [check whether a specific gesture type is supported](#checking-the-gesture-support) on a device.

- Receiving notifications

  You can monitor when a defined gesture type is recognized, and [receive a notification about the gesture](#receiving-notifications-on-recognized-gestures).

## Checking the Gesture Support

Some gestures are not supported on all devices because the devices lack the necessary sensors.

To check whether a specific gesture type is supported on the current device, use the `isGestureSupported()` method of the `HumanActivityMonitorManager` interface (in [mobile](../../api/latest/device_api/mobile/tizen/humanactivitymonitor.html#HumanActivityMonitorManager) and [wearable](../../api/latest/device_api/wearable/tizen/humanactivitymonitor.html#HumanActivityMonitorManager) applications):

```
try {
    var isSupported = tizen.humanactivitymonitor.isGestureSupported('GESTURE_PICK_UP');
    console.log('GESTURE_PICK_UP is ' + (isSupported ? 'supported' : 'not supported'));
} catch (error) {
    console.log('Error ' + error.name + ': ' + error.message);
}
```

## Receiving Notifications on Recognized Gestures

Learning how to register a listener for gesture recognition allows you to receive notifications about different gestures the user performs with a device:

1. To register a listener, use the `addGestureRecognitionListener()`  method of the `HumanActivityMonitorManager` interface (in [mobile](../../api/latest/device_api/mobile/tizen/humanactivitymonitor.html#HumanActivityMonitorManager) and [wearable](../../api/latest/device_api/wearable/tizen/humanactivitymonitor.html#HumanActivityMonitorManager) applications):

   ```
   var listenerId;

   function listener(data) {
       console.log('Received ' + data.event + ' event on ' + new Date(data.timestamp * 1000) + ' for '+ data.type + ' type');
   }

   function errorCallback(error) {
       console.log(error.name + ': ' + error.message);
   }

   try {
       listenerId = tizen.humanactivitymonitor.addGestureRecognitionListener('GESTURE_SHAKE', listener, errorCallback);
   } catch (error) {
       console.log('Error ' + error.name + ': ' + error.message);
   }
   ```

2. To stop receiving the notifications, remove the listener using the `removeGestureRecognitionListener()` method of the `HumanActivityMonitorManager` interface with the listener ID:

   ```
   try {
       tizen.humanactivitymonitor.removeGestureRecognitionListener(listenerId);
   } catch (err) {
       console.log('Exception: ' + err.name);
   }
   ```

## Related Information
* Dependencies   
  - Tizen 4.0 and Higher for Mobile
  - Tizen 4.0 and Higher for Wearable
