# System

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
