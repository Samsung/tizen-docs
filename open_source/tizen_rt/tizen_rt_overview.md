# Tizen RT

Tizen has been commercialized in smart TV, smartphone, wearable devices (Gear S, Gear Fit), and smart home appliances. However, the low-end and low-cost IoT devices, such as home appliances without LCD and wearable bands with a small LCD, have received less attention. The goal of Tizen RT is to extend the Tizen platform device coverage to these kind of low-end devices. Tizen RT is an RTOS-based lightweight platform that it can fit into these devices, which are typically equipped with Cortex-M/R processors with MPU, less than 2 MB RAM, and less than 16 MB Flash.

Typical RTOS-based development environment has several limitations. Firstly, it cannot load additional modules at runtime, and secondly, it can be inferior to a Linux environment. To tackle these limitations, Tizen RT adopts Linux-style development environments, including POSIX API, BSD Socket API, Shell, and Kconfig build configuration. This helps Linux developers build their business logics easily on top of Tizen RT. In addition, Tizen RT will adopt the lightweight JavaScript environment, consisting of JerryScript and IoT.js, during 2017.

## Overview

Tizen RT consists of lightweight RTOS called TinyAra, IoT protocols, such as IoTivity and LWM2M, and JerryScript/IoT.js, as shown in the following figure.

**Figure: Tizen RT content**

[![img](https://source.tizen.org/sites/default/files/resize/images/tizen_rt_introduction-800x350.png)](https://source.tizen.org/sites/default/files/images/tizen_rt_introduction.png)

The TinyAra project was started in 2015 based on NuttX, which is a real-time operating system (RTOS) with an emphasis on standard compliance and a small footprint. While maintaining the kernel architecture, TinyAra has grown by building up the IPv4/IPv6 network stack, file system, lightweight database called AraStorage, device monitor, and IoT protocols, such as IoTivity (OCF) and LWM2M. The combination of AraStorage and IoTivity allows TinyAra to collect, store, and deliver IoT sensor data easily. The mixture of the device monitor, which observes the status of connectivity, power, and errors, and the lightweight M2M promotes TinyAra as a large-scale device management solution. TinyAra has evolved into Tizen RT in 2016 by stacking multiple frameworks required for IoT scenarios. In 2017, it will adopt the lightweight JavaScript environment, called JerryScript and IoT.js.

The following figure illustrates the Tizen RT development, with green-colored boxes and gray-colored boxes released in 2016 and 2017, respectively. Tizen RT is first commercialized in the low-end home appliances in the first or second quarter of 2017.

**Figure: Tizen RT development**

[![img](https://source.tizen.org/sites/default/files/resize/images/tizen_rt_architecture-800x466.png)](https://source.tizen.org/sites/default/files/images/tizen_rt_architecture.png)