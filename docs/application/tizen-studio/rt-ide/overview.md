# TizenRT

Tizen platform is commercialized on smart TVs, smartphones, wearable devices (Gear S, Gear Fit), and smart home appliances. However, low-end and low-cost IoT devices, such as home appliances without display and wearable bands with a small LCD, have received less attention. The objective of TizenRT, where RT stands for real time is to extend the Tizen platform device coverage to these kind of low-end IoT devices.

TizenRT is an RTOS-based lightweight platform that can be installed into these low-end IoT devices. TizenRT follows Linux-style development that helps you to easily build your business logic on top of TizenRT. Therefore, TizenRT is only for Ubuntu. 

TizenRT consists of lightweight RTOS called TinyAra, IoT protocols, such as IoTivity and LWM2M, and JerryScript/IoT.js.

![TizenRT](media\rt_content.png)

For more information, click [![TizenRT](media\rt_podcast.png)](media\podcast_tizenrt_architecture.mp3).

The low-end IoT devices in which the TizenRT platform is installed have the following hardware and environmental requirements:

- Hardware targets: 

  Cortex-M/R processors with MPU, less than 2 MB RAM, and less than 16 MB Flash.

- Development environment:
	- Tizen Studio for RT for SmartThings:
	  Tizen Studio for RT  version 2.0 or higher is used as an IDE for developing IoT applications with st_things framework and ARTIK 053.
	  
## TizenRT Architecture

![TizenRT Architecture](media\rt_architecture.png)

TizenRT has evolved with intelligent things platform like security IoT data handling, smart things, and voice service enabling. It is open source under Apache License 2.0.

TizenRT is commercialized and installed in various Samsung products such as  air conditioners, ovens, refrigerators, air purifiers, and so on.

For more information on TizenRT, see [TizenRT GitHub](https://github.com/Samsung/TizenRT).
