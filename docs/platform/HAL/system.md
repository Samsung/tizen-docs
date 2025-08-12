# System

HAL modules related to the System framework support below features.
- Device Resource Management
- Sensor Resource Management
- Power Resource Management

## Device Resource Management

At the Hardware Abstraction Layer, device resource management handles device control requests
from tize core framework to hal-backend and kernel.
Device Resource Management is supported by process below

1. User requests device control through the capi-device call.
2. deviced handles that requests by calling HAL API functions.
3. Through HAL API call, deviced can get results from HAL Backend processed.

**Figure: Device Resource Management HAL hierarchy**
![File system hierarchy](media/device-resource-management-hierarchy.png)

These are supported HAL API Device modules
- Battery
- Bezel
- Board
- Display
- External connection
- Haptic
- Input
- IR
- LED
- Memory
- Power
- Thermal
- Touchscreen


### Battery
The Battery HAL module provides the way to get the current battery capacity value, battery state and charging state. And it provides the power source information like name, type. It also supports the API for an application to receive the battery events from the system. To receive the battery event it should be described by the callback function.

### Bezel
The Bezel HAL module provides the way to control bezel state like hardware, software, vibration. There are bezel states like turn on/off, vibration intensity.

### Board
The Board HAL module provides the way to get device board information.

### Display
The Display HAL module provides getter/setter properties related to display. It also supports the API for an application to receive the display event by callback function from the system.

### External Connection
The External Connection HAL module provides the way to get properties related to External_connection. It also supports the API for an application to receive the external_connection event by callback function from the system.

### Haptic
The Haptic HAL module provides the way to control haptic device like open/close, vibration and stop.

### Input
The Input HAL module provides the way to enable/disable input events from kernel.

### IR
The IR HAL module provides the way to get the information whether IR is available and transmit IR command.

### LED
The LED HAL module provides the way to control the attached LED device such as the camera flash and service LED.
It supports to turn on the camera flash and set the pattern to the service LED which is located to the front of a device.

### Memory
The Memory HAL module provides the way to get memory information.

### Power
The Power HAL module provides the way to get power wakeup reason.

### Thermal
The Thermal HAL module provides the way to get the current thermal value such as Application Processor, Communication Processor and Battery.

### Touchscreen
The Touchscreen HAL module provides the way to get or set touchscreen properties.


## Power Resource Management
It includes PASS (system daemon), hal-api-power, and hal-backend-power.

PASS (Power-Aware System Service) is a daemon that handles devices such as CPU, memory bus, GPU, memory, and battery.
Hal-api-power is an interface to connect pass and hal-backend-power.
Hal-backend-power requests the control of the device to Linux kernel.

**Figure: Power Resource Management HAL hierarchy**

![File system hierarchy](media/power-resource-management-hierarchy.png)


These are supported HAL API Device modules
- CPU
- Memory Bus
- GPU
- Memory
- Battery

### CPU
The CPU HAL module provides management of CPU frequency, thermal, and CPU hotplug. 

### Memroy Bus
The memory bus module provides management of Device Frequency Scaling (devfreq) and thermal of memory bus.  

### GPU
The GPU module provides management of GPU frequency and thermal.

### Memroy
The Memory module provides management of physical memory size during a page fault.

### Battery
The battery module provides management of battery such as thermal, charging status, and charging current.

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
