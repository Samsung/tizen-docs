# Tizen RT

Tizen has been commercialized in smart TV, smartphone, wearable devices (Gear S, Gear Fit), and smart home appliances. However, low-end and low-cost IoT devices, such as home appliances without display and wearable bands with a small LCD, have received less attention. The goal of TizenRT is to extend the Tizen platform device coverage to these kind of low-end devices.

Tizen RT is an RTOS-based lightweight platform.

* Hardware targets
Cortex-M/R processors with MPU, less than 2 MB RAM, and less than 16 MB Flash.

* Development environment
	- Tizen RT Studio for SmartThings
	Tizen RT Studio 2.0 (or later) is used as an IDE for developing IoT applications with the Tizen IoT Platform and ARTIK 053(s).

	- IoT Setup Wizard
	The TizenRT Setup Wizard is a computer application for easily setting up Tizen IoT on hardware targets. In 4. Flash the project, flashing a platform image into ARTIK 053(s) is only supported with the IoT Setup Wizard in a Linux computer environment.

To get started with developing your own Tizen IoT applications:
1. [Install the Tizen Studio for RT](rt-install.md)
2. [Manage the project](rt-create-project.md)
3. [Managing SmartThings&trade; Certificates](rt-ide/smartthings-ext/manage-certificate.md)
4. [Flash the project](rt-flash.md)
5. [Use the serial terminal](rt-terminal.md)
6. [Debug the project](rt-debug.md)