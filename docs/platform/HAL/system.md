# System

## Sensor Resource Management

The Tizen supports various sensors such as accelerometers, gyroscopes, and magnetometers. These sensors are used by applications to provide a variety of services, such as motion detection, gesture recognition, and location tracking. To manage these sensors efficiently, the Tizen platform uses a sensor resource management framework.
The Tizen uses HAL architecture to abstract the hardware-specific details of sensor devices. Below figure shows the sensor HAL architecture in Tizen.

**Figure: Sensor HAL architecture**

![hal-api-sensor](media/hal-api-sensor.png)


## Sensor descriptions and combinations
Sensor|Description|Sensor combinations
---|---|---
SENSOR_ACCELEROMETER|Accelerometer|Physical Sensor
SENSOR_GRAVITY|Gravitational Accelerometer|SENSOR_ACCELEROMETER + SENSOR_GYROSCOPE<br>SENSOR_ACCELEROMETER + lowpass filter
SENSOR_LINEAR_ACCELERATION|Accelerometer without Gravity|SENSOR_ACCELEROMETER - SENSOR_GRAVITY
SENSOR_MAGNETIC|Geomagnetic field|Physical Sensor
SENSOR_ROTATION_VECTOR|Rotation of device|SENSOR_ACCELEROMETER + SENSOR_GYROSCOPE + SENSOR_MAGNETIC
SENSOR_ORIENTATION|Orientation of device(Azimuth, Pitch, Roll|SENSOR_ROTATION_VECTOR(Convert (x,y,x) to (Azimuth, Pitch, Roll))
SENSOR_GYROSCOPE|Gyroscope|Physical Sensor
SENSOR_LIGHT|Light intensity|Physical Sensor
SENSOR_PROXIMITY|Proximity detection|Physical Sensor
SENSOR_PRESSURE|Atmospheric pressure|Physical Sensor
SENSOR_ULTRAVIOLET|Ultraviolet ray|Physical Sensor
SENSOR_HRM|Heart rate monitor(per minute)|Physical Sensor
SENSOR_HRM_LED_GREEN|Green LED light for HRM|Physical Sensor
SENSOR_GYROSCOPE_ROTATION_VECTOR|Rotation of device(x, y, z)|SENSOR_ACCELEROMETER + SENSOR_GYROSCOPE
SENSOR_GEOMAGNETIC_ROTATION_VECTOR|Rotation of device(x, y, z)|SENSOR_ACCELEROMETER + SENSOR_MAGNETIC
SENSOR_GYROSCOPE_ORIENTATION|Rotation of device(Azimuth, Pitch, Roll)|SENSOR_GYROSCOPE_ROTATION_VECTOR(Convert (x,y,x) to (Azimuth, Pitch, Roll))
SENSOR_GEOMAGNETIC_ORIENTATION|Rotation of device(Azimuth, Pitch, Roll)|SENSOR_GEOMAGNETIC_ROTATION_VECTOR(Convert (x,y,x) to (Azimuth, Pitch, Roll))
SENSOR_HRM_BATCH|Batch data of Heart rate monitor<br>(provide datas saved in buffer)|Physical Sensor
SENSOR_HRM_LED_GREEN_BATCH|Batch data of Green LED light for HRM<br>(provide datas saved in buffer)|Physical Sensor
SENSOR_HUMAN_PEDOMETER|Pedometer(steps)|SENSOR_ACCELEROMETER