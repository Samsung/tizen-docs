# Device Sensors

You can access and manage sensor data from [various sensors on the device](#supported-sensors). The main purpose of a sensor is to provide a value for the relevant environment parameter.

This feature is optional.

The main features of the Sensor API include the following:

- Managing sensors

  You can [enable the sensor, read sensor data, and disable the sensor](#managing-sensors).

- Receiving notifications

  You can [receive notifications on sensor data changes](#receiving-notifications-on-sensor-data-changes).

- Obtaining sensor hardware information

  You can [retrieve information about the technical limits of the sensor](#obtaining-sensor-hardware-information).

## Manage sensors

Learning how to start, read and stop a sensor is a basic sensor management skill, follow these steps to manage sensors:

<a name="support"></a>
1. Check that the sensor is supported by the device using the `getCapability()` method of the `SystemInfo` interface for the proper [capability](#capability) related to the sensor:

   ```
   var proximityCapability = tizen.systeminfo.getCapability('http://tizen.org/feature/sensor.proximity');

   if (proximityCapability === true) {
       /* Device supports the proximity sensor */
       var proximitySensor = tizen.sensorservice.getDefaultSensor('PROXIMITY');
   }
   ```

2. To get all available sensor types, use the `getAvailableSensors()` method:

   ```
   var sensors = tizen.sensorservice.getAvailableSensors();
   console.log('Available sensor: ' + sensors.toString());
   ```

3. Obtain the `Sensor` object using the `getDefaultSensor()` method of the `SensorService` interface. Enable the sensor using the `start()` method:

   ```
   var proximitySensor = tizen.sensorservice.getDefaultSensor('PROXIMITY');

   function onsuccessCB() {
       console.log('The proximity sensor started successfully.');
   }

   proximitySensor.start(onsuccessCB);
   ```

4. To get data from the sensor, use the appropriate method of the sensor object. For example, for the `LightSensor`, use the `getLightSensorData()` method:

   ```
   var lightSensor = tizen.sensorservice.getDefaultSensor('LIGHT');

   function onGetSuccessCB(sensorData) {
       console.log('light level: ' + sensorData.lightLevel);
   }

   function onsuccessCB() {
       console.log('sensor started');
       lightSensor.getLightSensorData(onGetSuccessCB);
       lightSensor.stop();
   }

   lightSensor.start(onsuccessCB);
   ```

5. To disable the sensor when it is no longer needed, use the `stop()` method of the `Sensor` interface:

   ```
   proximitySensor.stop();
   ```

## Receive notifications on sensor data changes

Learning how to register a change event handler for sensor data enables your application to react to changes without the need to check current values constantly:

1. Define an event handler for sensor data changes by implementing the `SensorDataSuccessCallback` interface:

   ```
   function onchangedCB(sensorData) {
       console.log('Light sensor data: ' + sensorData.lightLevel);
   }
   ```

2. Register a change listener to be called when the sensor data changes.

   To register a  change listener, use the `setChangeListener()` method of the `Sensor` interface:

   This command requires the following 3 parameters:

   - The first one is a handle to the callback method, which is invoked for every incoming event.
   - The second determines the amount of time (in milliseconds) passing between 2 consecutive events. Valid values are integers from 10 to 1000, inclusively. For example, the value 100 results in approximately 10 events being send every second.
   - The third determines the batch latency time (in milliseconds) at which sensor events are stored or delivered when the processor stays on the sleep or suspend status. You can calculate the maximum batch latency value using the `maxBatchCount` (for example, interval x `maxBatchCount`). If `maxBatchCount` is zero, the device does not support the batch latency time.

   ```
   var lightSensor = tizen.sensorservice.getDefaultSensor('LIGHT');

   function onsuccessCB() {
       console.log('Light sensor service has started successfully.');
   }

   function onchangedCB(sensorData) {
       console.log('Light sensor data: ' + sensorData.lightLevel);
   }

   lightSensor.setChangeListener(onchangedCB, 500, 2000);
   lightSensor.start(onsuccessCB);
   ```

   The default value of the second parameter is 100 and for the third parameter 0. If you do not pass a value, the default is used:

   ```
   var lightSensor = tizen.sensorservice.getDefaultSensor('LIGHT');

   function onsuccessCB() {
       console.log('Light sensor service has started successfully.');
   }

   function onchangedCB(sensorData) {
       console.log('Light sensor data: ' + sensorData.lightLevel);
   }

   /* Use the default interval value (100 ms) */
   lightSensor.setChangeListener(onchangedCB);
   lightSensor.start(onsuccessCB);
   ```

3. To stop receiving notifications on sensor data changes, use the `unsetChangeListener()` method of the Sensor interface:

   ```
   lightSensor.unsetChangeListener();
   ```

## Obtain sensor hardware information

Learning how to retrieve information about the sensor hardware enables your application to know the sensor's technical limits:

1. Define a success callback for handling a `SensorHardwareInfo` object. You can also define an optional error callback:

   ```
   function onsuccessCB(hwInfo) {
       console.log('name: ' + hwInfo.name);
       console.log('type: ' + hwInfo.type);
       console.log('vendor: ' + hwInfo.vendor);
       console.log('minValue: ' + hwInfo.minValue);
       console.log('maxValue: ' + hwInfo.maxValue);
       console.log('resolution: ' + hwInfo.resolution);
       console.log('minInterval: ' + hwInfo.minInterval);
       console.log('maxBatchCount: ' + hwInfo.maxBatchCount);
   }

   function onerrorCB(error) {
       console.log('An error occurred: ' + error.message);
   }
   ```

2. Call the `getSensorHardwareInfo()` method of an existing `Sensor` object to obtain its hardware information as the `SensorHardwareInfo` object:

   ```
   var proximitySensor = tizen.sensorservice.getDefaultSensor('PROXIMITY');

   proximitySensor.getSensorHardwareInfo(onsuccessCB, onerrorCB);
   ```

<a name="capability"></a>
## Supported sensors

The following table lists the sensor capabilities you can use to [determine whether a specific sensor is supported](#support) on a device.

**Table: Sensors and capabilities**

| Sensor                                   | Capability                               |
| ---------------------------------------- | ---------------------------------------- |
| Acceleration sensor                      | `http://tizen.org/feature/sensor.accelerometer` |
| Gravity sensor                           | `http://tizen.org/feature/sensor.gravity` |
| Gyroscope rotation vector sensor         | `http://tizen.org/feature/sensor.gyroscope_rotation_vector` |
| Gyroscope sensor                         | `http://tizen.org/feature/sensor.gyroscope` |
| Gyroscope sensor, uncalibrated           | `http://tizen.org/feature/sensor.gyroscope.uncalibrated` |
| Heart rate monitor sensor                | `http://tizen.org/feature/sensor.heart_rate_monitor` |
| Heart rate monitor sensor (green LED)    | `http://tizen.org/feature/sensor.heart_rate_monitor.led_green` |
| Heart rate monitor sensor (infrared LED) | `http://tizen.org/feature/sensor.heart_rate_monitor.led_ir` |
| Heart rate monitor sensor (red LED)      | `http://tizen.org/feature/sensor.heart_rate_monitor.led_red` |
| Light sensor                             | `http://tizen.org/feature/sensor.photometer` |
| Linear acceleration sensor               | `http://tizen.org/feature/sensor.linear_acceleration` |
| Magnetic sensor                          | `http://tizen.org/feature/sensor.magnetometer` |
| Magnetic sensor, uncalibrated            | `http://tizen.org/feature/sensor.magnetometer.uncalibrated` |
| Pressure sensor                          | `http://tizen.org/feature/sensor.barometer` |
| Proximity sensor                         | `http://tizen.org/feature/sensor.proximity` |
| Ultraviolet sensor                       | `http://tizen.org/feature/sensor.ultraviolet` |

## Related information
* Dependencies
  - Tizen 2.4 and Higher
