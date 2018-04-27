# Device Motions

You can access the [acceleration values](#acceleration-values) from the device accelerometer.

The Device Motion API is mandatory for Tizen mobile, wearable, and TV profiles, which means that it is supported on all mobile, wearable, and TV devices. All mandatory APIs are supported on the Tizen Emulators.

The main features of the Device Motion API include:

- Getting the current acceleration        

  You can [get the current acceleration](#getting-the-current-acceleration) along the X, Y, and Z axes.

- Monitoring the acceleration values        

  You can [get the acceleration along the X, Y, and Z axes at regular intervals](#monitoring-the-acceleration-values).

## Acceleration Values

The acceleration data is captured into the `Acceleration` interface (in [mobile](../../api/latest/device_api/mobile/tizen/cordova/device-motion.html#Acceleration), [wearable](../../api/latest/device_api/wearable/tizen/cordova/device-motion.html#Acceleration), and [TV](../../api/latest/device_api/tv/tizen/cordova/device-motion.html#Acceleration) applications). The acceleration values include the effect of gravity (9.81 m/s2), so that when a device lies flat and facing up, the x, y, and z values returned must be 0, 0, and 9.81.

**Table: Acceleration values**

| Property  | Value                                    |
| --------- | ---------------------------------------- |
| x         | Amount of acceleration on the X axis (in m/s2) |
| y         | Amount of acceleration on the Y axis (in m/s2) |
| z         | Amount of acceleration on the Z axis (in m/s2) |
| timestamp | Creation timestamp in milliseconds       |

This guide demonstrates how you can get access to the device accelerometer through the `navigator.accelerometer` object.

## Prerequisites

To perform any Cordova-related operations, you must wait until Cordova is fully set up (the `deviceready` event occurs):

```
document.addEventListener('deviceready', onDeviceReady, false);

function onDeviceReady() {
    console.log('Cordova features now available');
}
```

## Getting the Current Acceleration

To get the current acceleration along the X, Y, and Z axes:

1. Define a callback method to be invoked with the current acceleration values:

   ```
   function onSuccess(acceleration) {
       console.log('Acceleration X: ' + acceleration.x + '\n' +
                   'Acceleration Y: ' + acceleration.y + '\n' +
                   'Acceleration Z: ' + acceleration.z + '\n' +
                   'Timestamp: ' + acceleration.timestamp);
   }
   ```

2. Define a callback method to be invoked when errors occur:

   ```
   function onError() {
       console.log('onError!');
   }
   ```

3. Call the `getCurrentAcceleration()` method and pass the callbacks:

   ```
   navigator.accelerometer.getCurrentAcceleration(onSuccess, onError);
   ```

## Monitoring the Acceleration Values

To retrieve the acceleration along the X, Y, and Z axes at regular intervals:

1. Define a callback method to be invoked with the current acceleration values:

   ```
   function onSuccess(acceleration) {
       console.log('Acceleration X: ' + acceleration.x + '\n' +
                   'Acceleration Y: ' + acceleration.y + '\n' +
                   'Acceleration Z: ' + acceleration.z + '\n' +
                   'Timestamp: ' + acceleration.timestamp);
       console.log('Please wait 3 seconds for the next measurement...');
   }
   ```

2. Define a callback method to be invoked when errors occur:

   ```
   function onError() {
       console.log('onError!');
   }
   ```

3. Specify the interval of calling the `onSuccess()` callback in milliseconds:

   ```
   var options = {frequency: 3000}; /* Update every 3 seconds */
   ```

4. Call the `watchAcceleration()` method with options:

   ```
   var watchID = navigator.accelerometer.watchAcceleration(onSuccess, onError, options);
   ```

   Acceleration is now measured regularly, and each time a callback is called.

5. When finished, stop monitoring the acceleration value by calling the `clearWatch()` method with the `watchID` as a parameter:

   ```
   navigator.accelerometer.clearWatch(watchID);
   ```


## Related Information
* Dependencies   
   - Tizen 3.0 and Higher for Mobile
   - Tizen 3.0 and Higher for Wearable
   - Tizen 3.0 and Higher for TV
