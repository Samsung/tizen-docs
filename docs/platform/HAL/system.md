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