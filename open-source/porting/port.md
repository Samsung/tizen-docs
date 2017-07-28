# Tizen 3.0 Porting Guide

## Contents

 [[hide]()] 

- [1Introduction](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Introduction)[1.1About Tizen](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#About_Tizen)[1.2Purpose of This Document](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Purpose_of_This_Document)
- [2Tizen Architecture](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Tizen_Architecture)[2.1The Core Layer](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#The_Core_Layer)[2.1.1Tizen Core Services](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Tizen_Core_Services)[2.1.1.1Application Framework](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Application_Framework)[2.1.1.2Base](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Base)[2.1.1.3Connectivity](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Connectivity)[2.1.1.4Graphics and UI](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Graphics_and_UI)[2.1.1.5Location](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Location)[2.1.1.6Messaging](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Messaging)[2.1.1.7Multimedia](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Multimedia)[2.1.1.8PIM (Personal Information Management)](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#PIM_.28Personal_Information_Management.29)[2.1.1.9Security](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Security)[2.1.1.10System](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#System)[2.1.1.11Telephony](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Telephony)[2.1.1.12Web](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Web)
- [3Development Environment Setup](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Development_Environment_Setup)
- [4Getting the Source Code and Build](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Getting_the_Source_Code_and_Build)[4.1Platform Build](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Platform_Build)[4.2Kernel Build](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Kernel_Build)[4.3Image Build](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Image_Build)
- [5Tizen Bootup Overview](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Tizen_Bootup_Overview)[5.1Kernel Bootup](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Kernel_Bootup)[5.2Platform Bootup](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Platform_Bootup)
- [6BSP Customization](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#BSP_Customization)[6.1Boot Loader Fundamentals](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Boot_Loader_Fundamentals)[6.2Boot Loader Setup and Build](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Boot_Loader_Setup_and_Build)[6.3Boot Loader Kernel Parameters](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Boot_Loader_Kernel_Parameters)
- [7Kernel Fundamentals](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Kernel_Fundamentals)
- [8System](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#System_2)[8.1Partition and Filesystem](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Partition_and_Filesystem)[8.1.1Tizen Partition Layout](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Tizen_Partition_Layout)[8.1.2Supported Filesystems in Tizen](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Supported_Filesystems_in_Tizen)[8.1.3File-system Hierarchy Standard in Tizen](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#File-system_Hierarchy_Standard_in_Tizen)[8.2System Framework](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#System_Framework)[8.2.1systemd](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#systemd)[8.2.2resourced](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#resourced)[8.2.3deviced](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#deviced)[8.2.4dlog](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#dlog)[8.2.5Porting Smart Development Bridge (SDB)](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Porting_Smart_Development_Bridge_.28SDB.29)[8.2.6Porting Device HAL Interface](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Porting_Device_HAL_Interface)[8.2.6.1Battery HAL](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Battery_HAL)[8.2.6.2Display HAL](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Display_HAL)[8.2.6.3External Connector HAL](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#External_Connector_HAL)[8.2.6.4LED HAL](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#LED_HAL)[8.2.6.5IR HAL](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#IR_HAL)[8.2.6.6Touchscreen HAL](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Touchscreen_HAL)[8.3Sensor Framework](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Sensor_Framework)[8.3.1Types of Sensors](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Types_of_Sensors)[8.3.2Architectural Overview](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Architectural_Overview)[8.3.3Components of the Sensor Framework](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Components_of_the_Sensor_Framework)[8.3.4Porting HAL Interface](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Porting_HAL_Interface)[8.3.4.1Sensor](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Sensor)[8.3.4.2Sensorhub](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Sensorhub)[8.3.5References](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#References)[8.3.6Project Git Repository](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Project_Git_Repository)[8.3.7Test and Verify Sensors](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Test_and_Verify_Sensors)
- [9Graphics and UI](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Graphics_and_UI_2)[9.1Buffer Management](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Buffer_Management)[9.1.1Porting OAL Interface](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Porting_OAL_Interface)[9.1.2TBM Backends](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#TBM_Backends)[9.1.3Reference](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Reference)[9.2Display Management](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Display_Management)[9.2.1Porting OAL Interface](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Porting_OAL_Interface_2)[9.2.2TDM backends](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#TDM_backends)[9.2.3References](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#References_2)[9.3Input Management](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Input_Management)[9.3.1libinput](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#libinput)[9.3.2libevdev](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#libevdev)[9.3.3mtdev](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#mtdev)[9.3.4libinput backends](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#libinput_backends)[9.4OpenGL](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#OpenGL)[9.4.1Tizen OpenGL ES and EGL Architecture](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Tizen_OpenGL_ES_and_EGL_Architecture)[9.4.2Tizen Porting Layer (TPL) for EGL](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Tizen_Porting_Layer_.28TPL.29_for_EGL)[9.4.3Tizen Porting Layer for EGL Object Model](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Tizen_Porting_Layer_for_EGL_Object_Model)[9.4.3.1TPL-EGL Core Object](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#TPL-EGL_Core_Object)[9.4.3.2TPL-EGL Objects and Corresponding EGL Objects](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#TPL-EGL_Objects_and_Corresponding_EGL_Objects)[9.4.3.3TPL-EGL Frontend API](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#TPL-EGL_Frontend_API)[9.4.3.3.1TPL-EGL Object](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#TPL-EGL_Object)[9.4.3.3.2TPL-EGL Display](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#TPL-EGL_Display)[9.4.3.3.3TPL-EGL Surface](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#TPL-EGL_Surface)[9.4.3.4TPL-EGL and Wayland Server and Client](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#TPL-EGL_and_Wayland_Server_and_Client)[9.4.3.5Buffer Flow Between the Wayland Server and GLES/EGL Driver](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Buffer_Flow_Between_the_Wayland_Server_and_GLES.2FEGL_Driver)[9.4.4Project Git Repository](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Project_Git_Repository_2)[9.4.5libtpl-egl Reference Driver](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#libtpl-egl_Reference_Driver)[9.4.6Test and Verify the OpenGL ES Driver](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Test_and_Verify_the_OpenGL_ES_Driver)
- [10Multimedia](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Multimedia_2)[10.1Camera](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Camera)[10.1.1Porting OAL Interface](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Porting_OAL_Interface_3)[10.1.1.1GStreamer Camera Plugin](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#GStreamer_Camera_Plugin)[10.1.1.2Camera HAL](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Camera_HAL)[10.1.1.2.1Major Functions](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Major_Functions)[10.1.2Configuration](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Configuration)[10.1.3References](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#References_3)[10.2Radio](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Radio)[10.2.1Porting OAL Interface](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Porting_OAL_Interface_4)[10.2.1.1Radio HAL](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Radio_HAL)[10.2.1.2Major Functions](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Major_Functions_2)[10.2.2References](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#References_4)[10.3Audio](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Audio)[10.3.1Porting OAL Interface](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Porting_OAL_Interface_5)[10.3.2Configuration](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Configuration_2)[10.3.3References](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#References_5)[10.4Player](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Player)[10.4.1Porting OAL Interface](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Porting_OAL_Interface_6)[10.4.2Configuration](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Configuration_3)[10.4.3References](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#References_6)[10.5Codec](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Codec)[10.5.1Porting OAL Interface](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Porting_OAL_Interface_7)[10.5.2Configuration](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Configuration_4)[10.5.3References](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#References_7)
- [11Connectivity](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Connectivity_2)[11.1Bluetooth](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Bluetooth)[11.1.1Porting OAL Interface](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Porting_OAL_Interface_8)[11.1.2Configuration](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Configuration_5)[11.1.3References](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#References_8)[11.2WLAN](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#WLAN)[11.2.1Porting OAL Interface](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Porting_OAL_Interface_9)[11.2.2References](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#References_9)[11.3NFC](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#NFC)[11.3.1Porting OAL Interface](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Porting_OAL_Interface_10)[11.3.2Configuration](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Configuration_6)[11.3.3References](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#References_10)[11.4MTP](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#MTP)[11.4.1Porting OAL Interface](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Porting_OAL_Interface_11)[11.4.2Configuration](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Configuration_7)[11.4.3References](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#References_11)
- [12Location](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Location_2)[12.1Location Framework](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Location_Framework)[12.1.1Porting OAL Interface](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Porting_OAL_Interface_12)[12.2Geofence](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Geofence)[12.3Map Service](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Map_Service)[12.3.1Porting OAL Interface](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Porting_OAL_Interface_13)[12.3.1.1HERE Maps plugin](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#HERE_Maps_plugin)
- [13Telephony](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Telephony_2)[13.1Tizen Telephony Architecture](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Tizen_Telephony_Architecture)[13.2Telephony Libraries](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Telephony_Libraries)[13.3Telephony Plugins](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Telephony_Plugins)[13.4Telephony Server](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Telephony_Server)[13.5Porting OAL Interface](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Porting_OAL_Interface_14)[13.5.1Plugin Descriptors](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Plugin_Descriptors)[13.5.2Call Service Operations](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Call_Service_Operations)[13.5.3SMS Service Operations](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#SMS_Service_Operations)[13.5.4Network Service Operations](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Network_Service_Operations)[13.5.5HAL operations](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#HAL_operations)[13.6Configuration](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Configuration_8)[13.7References](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#References_12)[13.8Appendix](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Appendix)[13.8.1Sample Implementation for the Modem Interface Plugin](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Sample_Implementation_for_the_Modem_Interface_Plugin)[13.8.2Sample Implementation for the Modem Plugin](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Sample_Implementation_for_the_Modem_Plugin)[13.8.3Workflow](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Workflow)
- [14Application](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Application)[14.1Configuration](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Configuration_9)
- [15Appendix](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Appendix_2)[15.1NFC OAL API](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#NFC_OAL_API)

# Introduction[[edit](https://wiki.tizen.org/index.php?title=Tizen_3.0_Porting_Guide&action=edit&section=1)]

## About Tizen[[edit](https://wiki.tizen.org/index.php?title=Porting_Guide/Introduction&action=edit&section=T-1)]

Tizen is a standards-based platform that provides Web and native APIs for developing [applications](https://wiki.tizen.org/Applications) for multiple [device](https://wiki.tizen.org/index.php?title=Device&action=edit&redlink=1) categories. Tizen is currently targeted for smartphones and tablet devices, though more device types will be available in the future.

## Purpose of This Document[[edit](https://wiki.tizen.org/index.php?title=Porting_Guide/Introduction&action=edit&section=T-2)]

The intent of this document is to provide information and instruction to boot Tizen on new hardware and create products based on the Tizen OS. The Tizen porting guide takes you through the porting process by elaborating the Tizen architecture, the necessary tools, and the development environment setup, as well as creating a Tizen Image and demonstrating the modifications needed across various functional areas.

# Tizen Architecture[[edit](https://wiki.tizen.org/index.php?title=Tizen_3.0_Porting_Guide&action=edit&section=2)]

The following figure illustrates the Tizen architecture for smartphone and tablet devices.

![what_is_tizen_architecture.png](https://developer.tizen.org/sites/default/files/images/what_is_tizen_architecture.png)

You can get detailed information of the Tizen framework layer from Dev Guide[[1\]](https://developer.tizen.org/development/getting-started/overview#type)

## The Core Layer[[edit](https://wiki.tizen.org/index.php?title=Porting_Guide/Tizen_Architecture&action=edit&section=T-1)]

### Tizen Core Services[[edit](https://wiki.tizen.org/index.php?title=Porting_Guide/Tizen_Architecture&action=edit&section=T-2)]

#### Application Framework[[edit](https://wiki.tizen.org/index.php?title=Porting_Guide/Tizen_Architecture&action=edit&section=T-3)]

The Application Framework provides application management, including launching other applications using the package name, URI, or MIME type. It also launches predefined services, such as the system dialer application. The Application Framework also notifies applications of common events, such as low memory events, low battery, changes in screen orientation, and push notifications.

#### Base[[edit](https://wiki.tizen.org/index.php?title=Porting_Guide/Tizen_Architecture&action=edit&section=T-4)]

Base contains [GNU](https://wiki.tizen.org/index.php?title=GNU&action=edit&redlink=1)/[Linux](https://wiki.tizen.org/Linux) * base essential system libraries that provide key features, such as database support, internationalization, and XML parsing.

#### Connectivity[[edit](https://wiki.tizen.org/index.php?title=Porting_Guide/Tizen_Architecture&action=edit&section=T-5)]

Connectivity consists of all network and connectivity related functionalities, such as 3G, Wi-Fi, Bluetooth, HTTP, and NFC (Near Field Communication). Data network is based on ConnMan (Connection manager), which provides 3G and Wi-Fi based network connection management.

#### Graphics and UI[[edit](https://wiki.tizen.org/index.php?title=Porting_Guide/Tizen_Architecture&action=edit&section=T-6)]

Graphics and UI consist of the system graphic and UI stacks, which includes EFL (Enlightenment Foundation Libraries), window management system (x11 for Tizen 2.x / wayland for Tizen 3.0), input methods, and OpenGL® ES APIs.

EFL, the heart of the graphics component, is a suite of libraries. EFL is used to create rich graphics with ease, for all UI resolutions. The libraries build UIs in layers, allowing for 3D transformations and more. EFL includes the Evas canvas API library and the elementary widget library.

WebKit-based graphics is provided as well capable of running within a full browser UI or dedicated Web Runtime (without browser window), all based on Tizen's own HTML5 canvas WebKitEFL implementation. WebGL is supported too and Web-based frameworks for UI such as jQuery Mobile are also offered, what may help with porting existing jQuery code.

#### Location[[edit](https://wiki.tizen.org/index.php?title=Porting_Guide/Tizen_Architecture&action=edit&section=T-7)]

Location provides location based services (LBS), including position information, geocoding, satellite information, and GPS status. It delivers location information from various positioning sources, such as GPS, WPS (Wi-Fi Positioning System), Cell ID, and sensors.

#### Messaging[[edit](https://wiki.tizen.org/index.php?title=Porting_Guide/Tizen_Architecture&action=edit&section=T-8)]

Messaging consists of Message and Email. The Message supports SMS, MMS, and cell broadcast messages. Email supports protocols such as SMTP, IMAP, and POP3.

#### Multimedia[[edit](https://wiki.tizen.org/index.php?title=Porting_Guide/Tizen_Architecture&action=edit&section=T-9)]

Multimedia is based on GStreamer. It provides support for media, including video, audio, imaging, and VoIP. It also provides media content management for managing media file metadata information.

#### PIM (Personal Information Management)[[edit](https://wiki.tizen.org/index.php?title=Porting_Guide/Tizen_Architecture&action=edit&section=T-10)]

PIM enables managing user data on the device, including managing calendar, contacts, tasks, and retrieving data about the device context (such as device position and cable status).

#### Security[[edit](https://wiki.tizen.org/index.php?title=Porting_Guide/Tizen_Architecture&action=edit&section=T-11)]

Security is responsible for security deployment across the system. It consists of the platform security enablers, such as access control, certificate management, and secure application distribution.

For more information, see [Security/Tizen 3.0 security porting guide](https://wiki.tizen.org/wiki/Security/Tizen_3.0_security_porting_guide) and [All 3.X security pages](https://wiki.tizen.org/wiki/Security#All_3.X_security_pages).

#### System[[edit](https://wiki.tizen.org/index.php?title=Porting_Guide/Tizen_Architecture&action=edit&section=T-12)]

System consists of service (process), device, and resource management features, including:

- Interfaces for accessing devices, such as sensors, display, or vibrator
- Power management, such as LCD display backlight dimming/off and application processor sleep
- Monitoring devices and handling events, such as USB, MMC, charger, and ear jack events
- Resource management, such as CPU quota control and low memory management
- Service management, such as watchdog management and capability control

#### Telephony[[edit](https://wiki.tizen.org/index.php?title=Porting_Guide/Tizen_Architecture&action=edit&section=T-13)]

Telephony consists of cellular functionalities communicating with the modem:

- Provides call services (single call and multiparty call).
- Provides call-related and non-call-related supplementary services (call waiting, barring, and forwarding and USSD).
- Supports GSM, UMTS, LTE and CDMA network services.
- Provides packet services and network status information.
- Provides SMS-related services.
- Provides SIM card functionalities (SIM phonebook, SIM EF files, SIM Application Toolkit support)

#### Web[[edit](https://wiki.tizen.org/index.php?title=Porting_Guide/Tizen_Architecture&action=edit&section=T-14)]

Web provides a complete implementation of the Tizen Web API optimized for low power devices. It includes WebKit, which is a layout engine designed to allow Web browsers to render Web pages. It also provides Web runtime for Web applications.

# Development Environment Setup[[edit](https://wiki.tizen.org/index.php?title=Tizen_3.0_Porting_Guide&action=edit&section=3)]

To set up the Tizen OS Development environment and to obtain information regarding development, see the following links:

- [Setup your environment](https://source.tizen.org/documentation/developer-guide/environment-setup)
- [Installing development tools](https://source.tizen.org/documentation/developer-guide/installing-development-tools)

# Getting the Source Code and Build[[edit](https://wiki.tizen.org/index.php?title=Tizen_3.0_Porting_Guide&action=edit&section=4)]

Follow this guide to download the full source code for your Tizen platform and kernel.

- **git clone**

1. Download the `xml` file and extract each `<git_path>`.
2. Clone each git project using the `git clone ssh://<Username>@review.tizen.org:29418/<git_path>` command.


```
$ wget https://download.tizen.org/releases/weekly/tizen/mobile/tizen-mobile_20160727.5/builddata/manifest/tizen-mobile_20160727.5_arm-wayland.xml
$ for i in `cat tizen-mobile_20160727.5_arm-wayland.xml | grep "path" |  awk -F "\"" '{print $4}'`; do mkdir -p $i; cd $i/..; git clone ssh://<Username>@review.tizen.org:29418/$i; cd -; done

```

- **repo init' and 'repo sync**

1. Initialize the repository using the `repo init -u ssh://<Username>@review.tizen.org:29418/scm/manifest -b <branch_name> -m <profile>.xml` command.
2. Replace the project's `.xml` file inside the `$workspace/.repo/` directory with the manifest file in the `$srcrpm_snapshot`.
3. Use the `repo sync` to sync the repository.


```
$ repo init -u ssh://<Username>@review.tizen.org:29418/scm/manifest -b tizen -m mobile.xml 
$ wget --directory-prefix=$workspace/.repo/manifests/mobile/ https://download.tizen.org/releases/weekly/tizen/mobile/tizen-mobile_20160727.5/builddata/manifest/tizen-mobile_20160727.5_arm-wayland.xml
$ mv $workspace/.repo/manifests/mobile/tizen-mobile_20160727.5_arm-wayland.xml projects.xml
$ repo sync

```

When there is en error in the `repo sync` command, first of all check whether the git project name inside the `projects.xml` file exists in `review.tizen.org`. 

For more information, see [Cloning the Tizen source](https://source.tizen.org/documentation/developer-guide/getting-started-guide/cloning-tizen-source).

See the following links for more information:

- Source code Management on Tizen releases:




- Tizen Build setup




- Tizen Bug Tracking system




- Download URL: [http://download.tizen.org/](http://download.tizen.org/)

## Platform Build[[edit](https://wiki.tizen.org/index.php?title=Porting_Guide/Getting_Source_Code%26Build&action=edit&section=T-1)]

- To learn how to add something to Tizen, see [Developer Guide](https://source.tizen.org/documentation/developer-guide).


- To build the source code by using git build system, see [Git Build System](https://source.tizen.org/documentation/reference/git-build-system).

## Kernel Build[[edit](https://wiki.tizen.org/index.php?title=Porting_Guide/Getting_Source_Code%26Build&action=edit&section=T-2)]

To build the Tizen kernel for the TM1 board:

1. Install and setup cross compile tools on your system if the target and host are different (such as x86).

   ​

2. Prepare the kernel source code for TM1 from `profile/mobile/platform/kernel/linux-3.10-sc7730`.`git: https://review.tizen.org/git/?p=profile/mobile/platform/kernel/linux-3.10-sc7730.git``branch: accepted/tizen_mobile`

3. If your kernel source has been used to create binaries for other architecture, start by cleaning them up.

4. Setup the `.config` file for TM1.`$ make ARCH=arm tizen_tm1_defconfig`

5. After reconfiguring your needs (such as `make ARCH=arm menuconfig`) or using the stock configuration (no modifications), build it.`$ make ARCH=arm zImage``$ make ARCH=arm dtbs`

6. Create `devicetree` and `zImage` merged image with image tools.`$ scripts/sprd_dtbtool.sh -o arch/arm/boot/merged-dtb -p scripts/dtc/ -v arch/arm/boot/dts/``$ scripts/sprd_mkdzimage.sh -o arch/arm/boot/dzImage -k arch/arm/boot/zImage -d arch/arm/boot/merged-dtb`

7. Build and make kernel module image as well. Note that you may need to do sudo first to let `sudo -n` work in the script.`$ sudo ls``$ scripts/mkmodimg.sh`

8. Make a `.tar` archive from `dzImage` and `modules.img`.You can make your own `.tar` file from the 2 files.`$ tar cf FILENAME_YOU_WANT.tar -C arch/arm/boot dzImage -C ../../../usr/tmp-mod modules.img`

9. Send the `.tar` image to the target using `lthor`.`$ lthor FILENAME_YOU_WANT.tar`

## Image Build[[edit](https://wiki.tizen.org/index.php?title=Porting_Guide/Getting_Source_Code%26Build&action=edit&section=T-3)]

- To create the image by using MIC, see [MIC Image Creator](https://source.tizen.org/documentation/reference/mic-image-creator).

# Tizen Bootup Overview[[edit](https://wiki.tizen.org/index.php?title=Tizen_3.0_Porting_Guide&action=edit&section=5)]

This section provides a brief overview of the typical booting sequence, starting from the boot loader to the kernel and the platform.

[![Boot-1.png](https://wiki.tizen.org/images/thumb/b/b6/Boot-1.png/500px-Boot-1.png)](https://wiki.tizen.org/File:Boot-1.png)

## Kernel Bootup[[edit](https://wiki.tizen.org/index.php?title=3.0_Porting_Guide/Tizen_Bootup_Overview&action=edit&section=T-1)]

The Tizen bootup process is the same as any other [Linux](https://wiki.tizen.org/Linux) kernel. You just need to make sure that the correct device tree binary or machine ID and the boot arguments are passed from the boot loader.

## Platform Bootup[[edit](https://wiki.tizen.org/index.php?title=3.0_Porting_Guide/Tizen_Bootup_Overview&action=edit&section=T-2)]

- If `initramfs` existsAfter the initial RAM disk image has been mounted, `initramfs` hands over the control to `systemd` as the system manager daemon in Tizen platform.
- If there is no `initramfs`Kernel hands over the control to `systemd` as system manager daemon in Tizen platform.

From this point, `systemd` is responsible for probing all remaining hardware, mounting all necessary file systems and spawning all configured services. Basically, the system boot-up process is split up in various discrete steps. To synchronize point during start-up, target units (files whose name ends in `.target`) are used for grouping units. The boot-up process is highly parallelized in each target so that the order in which specific target units are reached is not deterministic. The system-plugin is an target-specific plugin for configuration setting such as mount point (`/etc/fstab`) and specific target boot scripts.

The following figure shows the early boot sequence after starting the kernel.

[![Tizen 3.0 boot2.png](https://wiki.tizen.org/images/thumb/1/15/Tizen_3.0_boot2.png/500px-Tizen_3.0_boot2.png)](https://wiki.tizen.org/File:Tizen_3.0_boot2.png)

- `sysinit.target`Special target unit for early boot-up scriptsIt has dependencies on necessary services and targets such as `local-fs.target`.At this point, most of file systems like `/opt` and `/tmp` are mounted and `systemd` related daemons, such as `systemd-journald`, are launched.
- `basic.target`Special target unit for basic boot-up.At this point, all necessary initialization for general purpose daemons such as mount points, sockets, timers, and path units are completed.Tizen specific services (such as `tizen-system-env`) also are executed.

For more information, see [systemd bootup process](https://www.freedesktop.org/software/systemd/man/bootup.html) and [systemd special target](https://www.freedesktop.org/software/systemd/man/systemd.special.html).

The following figure shows the overview of normal booting sequence in Tizen platform.

[![Tizen 3.0 normal noot.png](https://wiki.tizen.org/images/thumb/f/f0/Tizen_3.0_normal_noot.png/900px-Tizen_3.0_normal_noot.png)](https://wiki.tizen.org/File:Tizen_3.0_normal_noot.png)

- `multi-user.target`Special target unit for setting up a multi-user system which is non-graphical support.In Tizen platform, this target is used for launching platform infrastructure daemons such as dbus (system session), device manager, resource manager, gps manager, telephony daemon, WRT (Web Runtime) security daemon, media server, tlm, and daemons related to connectivity.Some `systemd`-related daemons (such as `systemd-logind`) are also started in this phase.
- `graphical.target`Special target unit for setting up a graphical environment.
- `systemd` user session`systemd` user session is executed by tlm and `systemd-logind` to execute `user@.service`.Tizen platform uses the `systemd` user session for the user privilege daemons.Some daemons related with graphic system such as Enlightenment (Windows manager) are launched as user privilege in this phase.`ac.service` and `launchpad-process-pool` are launched as user privilege.Tizen applications are running as user privilege.

# BSP Customization[[edit](https://wiki.tizen.org/index.php?title=Tizen_3.0_Porting_Guide&action=edit&section=6)]

This section covers the basic configuration, setup, and build procedure required for building the boot loader and the kernel image for [ARM](https://wiki.tizen.org/ARM).

## Boot Loader Fundamentals[[edit](https://wiki.tizen.org/index.php?title=Porting_Guide/BSP_Customization&action=edit&section=T-1)]

Boot loader is a small piece of software that is required to perform the basic hardware and peripheral initialization and load the kernel and proper device tree binary for the device to RAM. For the Tizen platform, the boot loader comes in 2 parts. The first part is the primary boot loader and the second part is the secondary boot loader. The primary boot loader is the proprietary boot loader. The secondary boot loader is the open source boot loader u-boot, which is customized further for the Tizen platform.

If your platform is already loaded with the compatible boot loader software, you can skip this section and move directly to the kernel section.

## Boot Loader Setup and Build[[edit](https://wiki.tizen.org/index.php?title=Porting_Guide/BSP_Customization&action=edit&section=T-2)]

To build the Tizen TM1 boot loader:

1. Install and setup cross compile tools on your system if the target and your host are different (such as x86).
2. Start with cleaning up the `u-boot-tm1` source. (Download the source from the [u-boot-tm1](https://review.tizen.org/git/?p=profile/mobile/platform/kernel/u-boot-tm1.git;a=summary) repository.)`$ make distclean`
3. Set up the configration for TM1.
4. Build `u-boot`.`$ make ARCH=arm`
5. Once the build is successful, the `u-boot.bin` file is created. (This step is for preventing from flashing the other `u-boot.bin` file.)`$ tools/mkimage_signed.sh u-boot.bin "tizen_tm1"`
6. After the scrip is run, the `u-boot-mmc.bin` file is created.
7. Create a boot loader tarball to download the `u-boot` binary onto the target.`$ tar cvf bootloader.tar u-boot-mmc.bin`

Be careful when you modify the boot loader, as there is a risk of breaking the device for good.

## Boot Loader Kernel Parameters[[edit](https://wiki.tizen.org/index.php?title=Porting_Guide/BSP_Customization&action=edit&section=T-3)]

The command line parameters can be passed from boot loader to [Linux](https://wiki.tizen.org/Linux) kernel. Here are some example command line parameters:

```
   Example:
   console=ttyS1,115200n8
   mem=1024M
   loglevel=1

```

# Kernel Fundamentals[[edit](https://wiki.tizen.org/index.php?title=Tizen_3.0_Porting_Guide&action=edit&section=7)]

The kernel is the operating system that drives the platform. Here the kernel refers to the open source [Linux](https://wiki.tizen.org/Linux) kernel that is customized for the Tizen platform. The following section gives a brief overview about the Tizen kernel setup, configuration, and the build procedure for building a Linux kernel for your Tizen platform. The output of the kernel binary is a `zImage` merged with `devicetree` or the `zImage` and `devicetree` binary that is suitable for boot loader of the specific board. If you have chosen for a secure booting configuration in your boot loader, this kernel image must be compatible with your boot loader.

To download the Tizen kernel source package, see [Getting Source Code and Build](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Getting_Source_Code.26Build). Set up or modify your kernel configuration, use the appropriate `defconfig` file from `arch/arm/configs/` ([ARM](https://wiki.tizen.org/ARM) CPU).

For more detailed information about Tizen kernel configuration and kernel building, see [Kernel Build](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Kernel_Build).

| Note                                     |
| ---------------------------------------- |
| Tizen uses `INOTIFY` instead of `DNOTIFY`. You must disable `DNOTIFY` from your kernel configuration. |

If you want to use `initramfs`, you can use these configurations:

- `CONFIG_INITRAMFS_SOURCE`
- `CONFIG_INITRAMFS_ROOT_UID`
- `CONFIG_INITRAMFS_ROOT_GID`
- `CONFIG_INITRAMFS_COMPRESSION_NONE/GZIP/BZIP2/LZNA/LZO`

# System[[edit](https://wiki.tizen.org/index.php?title=Tizen_3.0_Porting_Guide&action=edit&section=8)]

## Partition and Filesystem[[edit](https://wiki.tizen.org/index.php?title=3.0_Porting_Guide/System&action=edit&section=T-1)]

### Tizen Partition Layout[[edit](https://wiki.tizen.org/index.php?title=3.0_Porting_Guide/System&action=edit&section=T-2)]

The following description is an example of the Tizen partition layout. The product vendor can modify the sequence or partition layout for their devices as needed.

1. The `boot` partition includes the kernel image, boot-loader image, and modem image. Additionally, it can contain device driver modules.
2. The `rootfs` partition is mounted on the root directory. It contains fundamental frameworks for Tizen and some general utilities for Linux.
3. The `system-data` partition is mounted on the `/opt` directory and it includes the platform database and platform configurations.
4. The `user` partition can be mounted on the `/opt/usr` directory separately. The partition includes applications and data installed by user.
5. External storage are mounted on `/opt/media`.
6. The image files (`rootfs.img`, `system-data.img`, and `user.img`) can be zipped for downloading, such as `<IMAGE_NAME>.tar.gz`.

According to the partition layout, the `/etc/fstab` directory must be modified or the `systemd` mount units must be added properly. For the purpose, the `fstab` file or specific system mount unit files for the device must be added in the `system-plugin` git. The following example shows the `fstab` file.

```
/dev/root         /               ext4    defaults,noatime 0      1
LABEL=system-data /opt            ext4    defaults,noatime 0      2
LABEL=user        /opt/usr        ext4    defaults,noatime 0      3

```

### Supported Filesystems in Tizen[[edit](https://wiki.tizen.org/index.php?title=3.0_Porting_Guide/System&action=edit&section=T-3)]

Filesystems that Tizen supports Extended 4 (Ext 4) file-system, which is configured as the default file-system. The Tizen kernel has to be compiled to enable support for the other file systems like JFS, XFS, BTRFS, and Reiserfs. The following configuration option must be enabled in the kernel configuration file. 

- `CONFIG_EXT4_FS=y`
- `CONFIG_EXT4_FS_XATTR=y`
- `CONFIG_EXT4_USE_FOR_EXT23=y`
- `CONFIG_EXT4_FS_SECURITY=y`

### File-system Hierarchy Standard in Tizen[[edit](https://wiki.tizen.org/index.php?title=3.0_Porting_Guide/System&action=edit&section=T-4)]

The Tizen directory hierarchy intends to follow the FHS as possible for compatibility as a member of Linux world. However, Tizen uses the `/opt` directory for Tizen specific purposes Tizen recommends that whole RW data places to the `/opt` directory.

[![FSH.png](https://wiki.tizen.org/images/thumb/5/56/FSH.png/300px-FSH.png)](https://wiki.tizen.org/File:FSH.png)

Directory macros are provided for accessing Tizen specific directory by Tizen Platform Configuration Metafile. The following table lists the example macros.

| Directory macros | Real path    |
| ---------------- | ------------ |
| `TZ_SYS_DATA`    | `/opt/data`  |
| `TZ_SYS_SHARE`   | `/opt/share` |
| `TZ_SYS_VAR`     | `/opt/var`   |

## System Framework[[edit](https://wiki.tizen.org/index.php?title=3.0_Porting_Guide/System&action=edit&section=T-5)]

The System framework module abstracts low level system functions and manages the Tizen system.

- `systemd` requirements for system and service managementLinux Kernel >= 3.4 , Linux Kernel >= 3.8 for Smack support`CONFIG_CGROUPS`, `CONFIG_TIMERFD`, `CONFIG_SIGNALFD`, `CONFIG_EPOLL`, ...
- Basic resource requirements (such as cpu, memory) usage management
  - Linux Kernel >= 3.10 for `VMPRESSURE`, Linux Kernel >= 3.8 for `MEMCG SWAP`
  - `CONFIG_CGROUPS`, `CONFIG_CGROUP_SCHED`, `CONFIG_MEMCG`, `CONFIG_MEMCG_SWAP`, ...
- `deviced` requirements for device and power managementDevice HAL layer porting
- dlog requirements
  - Selecting a proper backend for target environment and enable appropriate kernel feature
    1. Additional KMSG Patch for Multiple Kmsg Backend
    2. Android Logger Driver for Android Log Backend
    3. User Space Logger Dameon

It is recommended to use Linux Kernel 3.10 or above.

[![SystemFW.png](https://wiki.tizen.org/images/thumb/f/fb/SystemFW.png/600px-SystemFW.png)](https://wiki.tizen.org/File:SystemFW.png)

#### systemd[[edit](https://wiki.tizen.org/index.php?title=3.0_Porting_Guide/System&action=edit&section=T-6)]

[systemd](https://wiki.tizen.org/index.php?title=Systemd&action=edit&redlink=1) (ver.219), is system and service manager for Tizen system. Basically, `systemd` provides a lot of functionality such as parallesized service execution, socket and D-Bus activation for starting services and daemon, on-demand starting of deamons, managing the service processes as a group using Linux cgroup, supporting automount points, snapshotting and restoring of services.

The core of `systemd` manages all units, such as service, socket, and mount. It stores all log data. When developers add a new service daemon, they need to provide proper system units and unit dependency.

`systemd` requires to enable the `cgroup` and `autofs` options in the [Linux](https://wiki.tizen.org/Linux) Kernel configuration. It also depends on dbus and some libraries.

#### resourced[[edit](https://wiki.tizen.org/index.php?title=3.0_Porting_Guide/System&action=edit&section=T-7)]

`resourced` is a daemon managing system resources such as memory and cpu.

- To use most of the resourced functionality, you have to enable kernel feature about cgroup
  - `CONFIG_CGROUPS`: Base feature
  - `CONFIG_CGROUP_SCHED`: Controls the CPU share of applications
  - `CONFIG_MEMCG`: Selects the victim in the low memory situation
  - `CONFIG_FREEZER`: Freezes background (and idle) applications
  - `CONFIG_MEMCG_SWAP`, `CONFIG_MEMCG_SWAP_ENABLED`, `CONFIG_ZRAM`, `CONFIG_ZSMALLOC`: Saves memory by compressing

| Note                                     |
| ---------------------------------------- |
| For using resourced freezer feature, you need to install the freezer plugin by enabling `CONFIG_FREEZER`. |

#### deviced[[edit](https://wiki.tizen.org/index.php?title=3.0_Porting_Guide/System&action=edit&section=T-8)]

The `deviced` is a daemon which handles the device events, such as the battery level and plug and play device status and provides the interfaces to manage devices such as power, display, and external storages. Each functionality may require HAL layer if your BSP does not provide the Linux kernel standard interface.

- Managing the LCD backlight state (on/off/dim)
- Managing the CPU sleep state and handling the requests lock CPU not to sleep
- Monitoring the external devices, such as USB cable, earjack, and charger
- Monitoring the battery level
- Managing the external storages, such as SD card and USB storages
- Playing and handling the vibrator
- Setting USB configurations to connect to the host PC
- Powering off the LED, IR, and other features
- Using the device HAL to handle devices and get events

#### dlog[[edit](https://wiki.tizen.org/index.php?title=3.0_Porting_Guide/System&action=edit&section=T-9)]

Tizen provides 3 backends for logging system:

- Multiple `kmsg` backend




- Android-logger backend




- User logger backend



### Porting Smart Development Bridge (SDB)[[edit](https://wiki.tizen.org/index.php?title=3.0_Porting_Guide/System&action=edit&section=T-10)]

SDB is a device management tool used for remote shell command, file transfer, controlling device log out, and USB debugging.

- Kernel driver is necessary to use sdb. The following are examples of the kernel drivers:




- The USB interface descriptor of SDB interface on the target device must have the following information to recognize the target as a kind of Tizen device.

```
Class: 0xff
SubClass: 0x20
Protocol: 0x02

```

- If multi-configuration is used, the SDB client of the host PC (Linux PC) selects the first configuration. SDB must be located on the first configuration on the target with multi-configuration system.


- External Connector Class (`extcon`) needs to be ported to the kernel to recognize the USB cable connection. If `extcon` cannot be ported, the following shell command can be used to enable SDB.

```
/usr/bin/direct_set_debug.sh --sdb-set
```

### Porting Device HAL Interface[[edit](https://wiki.tizen.org/index.php?title=3.0_Porting_Guide/System&action=edit&section=T-11)]

The device HAL is applied for the hardware independent platform. The device HAL consists of libraries corresponding to hardware, such as display, external connector, battery, LED, and IR. The HAL is used by `deviced` to control hardware and manages the events of device state changes. `deviced` (device daemon) opens the implemented libraries and uses the APIs to control the devices.

OEM developers must implement the API defined in the header files of the `libdevice-node` package and compile their libraries (`.so` file) for their devices.

The following code snippet shows the device HAL structure.

```
#define MAKE_TAG_CONSTANT(A,B,C,D) (((A) << 24) | ((B) << 16) | ((C) << 8) | (D))
#define HARDWARE_INFO_TAG MAKE_TAG_CONSTANT('T','H','I','T')

struct hw_common;
struct hw_info {
    /* magic must be initialized to HARDWARE_INFO_TAG */
    uint32_t magic;
    /* HAL version */
    uint16_t hal_version;
    /* Device version */
    uint16_t device_version;
    /* Device ID */
    const char *id;
    /* Device name */
    const char *name;
    /* Author name */
    const char *author;
    /* Module's dynamic shared object */
    void *dso;
    /* Reserved for future use */
    uint32_t reserved[8];
    /* Open device */
    int (*open)(struct hw_info *info, const char *id, struct hw_common **common);
    /* Close device */
    int (*close)(struct hw_common *common);
};

struct hw_common {
    /* Indicate to this device information structure */
    struct hw_info *info;
};

```

#### Battery HAL[[edit](https://wiki.tizen.org/index.php?title=3.0_Porting_Guide/System&action=edit&section=T-12)]

The battery HAL provides functions to get the battery status. The HAL interface is defined in the `hw/battery.h` header file of the `libdevice-node` library, and the `pkg-config` `device-node` must be used to use the HAL interface.

The following code snippet shows the battery HAL interface.

```
/*
   Device ID
*/
#define BATTERY_HARDWARE_DEVICE_ID "battery"

#define POWER_SOURCE_NONE "none"
#define POWER_SOURCE_AC "ac"
#define POWER_SOURCE_USB "usb"
#define POWER_SOURCE_WIRELESS "wireless"
 
/*
   Device version 
*/
#define BATTERY_HARDWARE_DEVICE_VERSION MAKE_VERSION(0,1)

struct battery_info {
    char *name; /* "display" */
    char *status; /* "Charging", "Discharging", "Full", "Not charging" */
    char *health; /* "Good", "Cold", "Dead", "Overheat", "Over voltage" */
    char *power_source; /* "ac", "usb", "wireless" */
    int online; /* 0 ~ */
    int present; /* 0 or 1 */
    int capacity; /* 0 ~ 100 */
    int current_now; /* Current (uA). Positive value if power source is connected, negative value if power source is not connected */
    int current_average; /* Average curretn (uA). Positive value if power source is connected, negative value if power source is not connected */
};

typedef void (*BatteryUpdated)(struct battery_info *info, void *data);

struct battery_device {
    struct hw_common common;

    /* Register battery event */
    int (*register_changed_event)(BatteryUpdated updated_cb, void *data);
    void (*unregister_changed_event)(BatteryUpdated updated_cb);

    /* Get current states */
    int (*get_current_state)(BatteryUpdated updated_cb, void *data);
};

```

The following table lists the battery HAL functions.

| Function prototype                       | Description                              |           |
| ---------------------------------------- | ---------------------------------------- | --------- |
| `int (*register_changed_event)(BatteryUpdated updated_cb, void *data);` | The function adds callback function which is called when battery status is changed. | Mandatory |
| `void (*unregister_changed_event)(BatteryUpdated updated_cb);` | The function removes the callback function added for the battery status event. | Mandatory |
| `int (*get_current_state)(BatteryUpdated updated_cb, void *data);` | The function calls the function provided as the first parameter. The battery information is delivered to the function parameter. | Mandatory |

The following code snippet shows an example of the battery HAL.

```
#define BATTERY_ROOT_PATH "/sys/class/power_supply"

static int 
get_power_source(char **src)
{
    int ret, val;
    ret = sys_get_int(BATTERY_ROOT_PATH"/"POWER_SOURCE_AC"/online", &val);
    if (ret >= 0 && val > 0) {
        *src = POWER_SOURCE_AC;

        return 0;
    }

    ret = sys_get_int(BATTERY_ROOT_PATH"/"POWER_SOURCE_USB"/online", &val);
    if (ret >= 0 && val > 0) {
        *src = POWER_SOURCE_USB;

        return 0;
    }

    ret = sys_get_int(BATTERY_ROOT_PATH"/"POWER_SOURCE_WIRELESS"/online", &val);
    if (ret >= 0 && val > 0) {
        *src = POWER_SOURCE_WIRELESS;

        return 0;
    }

    *src = POWER_SOURCE_NONE;

    return 0;
}

static int 
battery_get_current_state(BatteryUpdated updated_cb, void *data)
{
    int fd;
    struct battery_info info;
    char status[32];
    char health[32];
    char *power_source;

    if (!updated_cb)
        return -EINVAL;

    info.name = BATTERY_HARDWARE_DEVICE_ID;


    fd = open(BATTERY_ROOT_PATH"/battery/status", O_RDONLY);
    read(fd, status, sizeof(status));
    close(fd);
    info.status = status;

    fd = open(BATTERY_ROOT_PATH"/battery/health", O_RDONLY);
    read(fd, health, sizeof(health));
    close(fd);
    info.health = health;

    ....

    get_power_source(&power_source);
    info.power_source = power_source;

    updated_cb(&info, data);

    return 0;
}

static int 
battery_open(struct hw_info *info, const char *id, struct hw_common **common)
{
    struct battery_device *battery_dev;
    battery_dev = calloc(1, sizeof(struct battery_device));

    battery_dev->common.info = info;
    battery_dev->register_changed_event = battery_register_changed_event;
    battery_dev->unregister_changed_event = battery_unregister_changed_event;
    battery_dev->get_current_state = battery_get_current_state;

    *common = (struct hw_common *)battery_dev;

    return 0;
}

static int 
battery_close(struct hw_common *common)
{
    free(common);

    return 0;
}

HARDWARE_MODULE_STRUCTURE = { 
    .magic = HARDWARE_INFO_TAG,
    .hal_version = HARDWARE_INFO_VERSION,
    .device_version = BATTERY_HARDWARE_DEVICE_VERSION,
    .id = BATTERY_HARDWARE_DEVICE_ID,
    .name = "battery",
    .open = battery_open,
    .close = battery_close,
};

```

#### Display HAL[[edit](https://wiki.tizen.org/index.php?title=3.0_Porting_Guide/System&action=edit&section=T-13)]

The display HAL provides functions to control the display brightness. The HAL interface is defined in the `hw/display.h` header file of the `libdevice-node` library, and the `pkg-config` `device-node` must be used to use the HAL interface.

The following code snippet shows the display HAL interface.

```
/*
   Device ID
*/
#define DISPLAY_HARDWARE_DEVICE_ID "display"

/*
   Device version
*/
#define DISPLAY_HARDWARE_DEVICE_VERSION MAKE_VERSION(0,2)

struct display_device {
    struct hw_common common;

    /* Control display brightness */
    int (*get_max_brightness)(int *brightness);
    int (*get_brightness)(int *brightness);
    int (*set_brightness)(int brightness);
};

```

The following table lists the display HAL functions.

| Function prototype                       | Description                              |           |
| ---------------------------------------- | ---------------------------------------- | --------- |
| `int (*get_max_brightness)(int *brightness)` | The function returns the maximum brightness value the display driver supports. | Mandatory |
| `int (*get_brightness)(int *brightness)` | The function returns the current brightness value. | Mandatory |
| `int (*set_brightness)(int brightness)`  | The function sets the brightness value.  | Mandatory |

The following code snippet shows an example of the display HAL.

```
#ifndef BACKLIGHT_PATH
#define BACKLIGHT_PATH "/sys/class/backlight/panel"
#endif

static int 
display_get_max_brightness(int *val)
{
    static int max = -1; 
    char buf[BUF_MAX];
    int fd;
    if (max < 0) {
        fd = open(BACKLIGHT_PATH"/max_brightness", O_RDONLY);
        read(fd, buf, sizeof(buf));
        close(fd);
        max = atoi(buf);
    }
    *val = max;

    return 0;
}

static int 
display_get_brightness(int *brightness)
{
    int fd;
    char buf[BUF_MAX];
    fd = open(BACKLIGHT_PATH"/brightness", O_RDONLY);
    read(fd, buf, sizeof(buf));
    close(fd);
    *brightness = atoi(buf);

    return 0;
}

static int 
display_set_brightness(int brightness)
{
    int max;
    char buf[BUF_MAX];
    display_get_max_brightness(&max);    
    if (brightness > max)
        brightness = max;
    snprintf(buf, sizeof(buf), "%d", brightness);
    fd = open(BACKLIGHT_PATH"/brightness", O_WRONLY);
    write(fd, buf, strlen(buf));
    close(fd);

    return 0;
}

static int 
display_open(struct hw_info *info,
        const char *id, struct hw_common **common)
{
    struct display_device *display_dev;

    if (!info || !common)
        return -EINVAL;

    display_dev = calloc(1, sizeof(struct display_device));
    if (!display_dev)
        return -ENOMEM;

    display_dev->common.info = info;
    display_dev->get_max_brightness = display_get_max_brightness;
    display_dev->get_brightness = display_get_brightness;
    display_dev->set_brightness = display_set_brightness;

    *common = (struct hw_common *)display_dev;

    return 0;
}

static int 
display_close(struct hw_common *common)
{
    if (!common)
        return -EINVAL;

    free(common);

    return 0;
}

HARDWARE_MODULE_STRUCTURE = {
    .magic = HARDWARE_INFO_TAG,
    .hal_version = HARDWARE_INFO_VERSION,
    .device_version = DISPLAY_HARDWARE_DEVICE_VERSION,
    .id = DISPLAY_HARDWARE_DEVICE_ID,
    .name = "Display",
    .open = display_open,
    .close = display_close,
};

```

#### External Connector HAL[[edit](https://wiki.tizen.org/index.php?title=3.0_Porting_Guide/System&action=edit&section=T-14)]

The external connector HAL provides functions to get the external connector device status. The HAL interface is defined in the `hw/external_connection.h` header file of the `libdevice-node` library, and the `pkg-config` `device-node` needs to be used to use the HAL interface.

The following code snippet shows the interface of the external connector HAL.

```
/*
   Device ID
*/
#define EXTERNAL_CONNECTION_HARDWARE_DEVICE_ID "external_connection"

#define EXTERNAL_CONNECTION_USB "USB"
#define EXTERNAL_CONNECTION_USB_HOST "USB-HOST"
#define EXTERNAL_CONNECTION_TA "TA"
#define EXTERNAL_CONNECTION_HDMI "HDMI"
#define EXTERNAL_CONNECTION_DOCK "Dock"
#define EXTERNAL_CONNECTION_MIC "Microphone"
#define EXTERNAL_CONNECTION_HEADPHONE "Headphone"

/*
   Device version
*/
#define EXTERNAL_CONNECTION_HARDWARE_DEVICE_VERSION MAKE_VERSION(0,1)

struct connection_info {
    char *name;
    char *state;
    int flags;
};

typedef void (*ConnectionUpdated)(struct connection_info *info, void *data);

struct external_connection_device {
    struct hw_common common;

    /* Register external_connection event */
    int (*register_changed_event)(ConnectionUpdated updated_cb, void *data);
    void (*unregister_changed_event)(ConnectionUpdated updated_cb);

    /* Get current states */
    int (*get_current_state)(ConnectionUpdated updated_cb, void *data);
};

```

The following table lists the external connector HAL functions.

| Function prototype                       | Description                              |           |
| ---------------------------------------- | ---------------------------------------- | --------- |
| `int (*register_changed_event)(ConnectionUpdated updated_cb, void *data);` | The function adds callback function which is called when the external connector status is changed. | Mandatory |
| `void (*unregister_changed_event)(ConnectionUpdated updated_cb);` | The function removes the callback function added for the external connector status event. | Mandatory |
| `int (*get_current_state)(ConnectionUpdated updated_cb, void *data);` | The function calls the function provided as the first parameter. The external connector information is delivered to the function parameter. | Mandatory |

The following code snippet shows an example of the external connector HAL.

```
#define SWITCH_ROOT_PATH "/sys/devices/virtual/switch"

static struct switch_device {
    char *type;
    char *name;
    int state;
} switch_devices[] = {
    {EXTERNAL_CONNECTION_USB, "usb_cable", 0},
    {EXTERNAL_CONNECTION_DOCK, "dock", 0},
    {EXTERNAL_CONNECTION_HEADPHONE, "earjack", 0},
};

static int
read_switch_state(char *path)
{
    char node[128], val[8];
    FILE *fp;

    snprintf(node, sizeof(node), "%s/%s/state", SWITCH_ROOT_PATH, path);
    fp = fopen(node, "r");
    fgets(val, sizeof(val), fp));
    fclose(fp);

    return atoi(val);
}

static int 
external_connection_get_current_state(ConnectionUpdated updated_cb, void *data)
{
    int ret, i;
    struct connection_info info;
    char buf[8];

    for (i = 0 ; i < ARRAY_SIZE(switch_devices) ; i++) {
        ret = read_switch_state(switch_devices[i].name);
        info.name = switch_devices[i].type;
        snprintf(buf, sizeof(buf), "%d", ret);
        info.state = buf;
        updated_cb(&info, data);
    }

    return 0;
}

static int
read_switch_state(char *path)
{
    char node[128], val[8];
    FILE *fp;

    snprintf(node, sizeof(node), "%s/%s/state", SWITCH_ROOT_PATH, path);
    fp = fopen(node, "r");
    fgets(val, sizeof(val), fp));
    fclose(fp);

    return atoi(val);
}

static int
external_connection_close(struct hw_common *common)
{
    free(common);

    return 0;
}

HARDWARE_MODULE_STRUCTURE = {
    .magic = HARDWARE_INFO_TAG,
    .hal_version = HARDWARE_INFO_VERSION,
    .device_version = EXTERNAL_CONNECTION_HARDWARE_DEVICE_VERSION,
    .id = EXTERNAL_CONNECTION_HARDWARE_DEVICE_ID,
    .name = "external_connection",
    .open = external_connection_open,
    .close = external_connection_close,
};

```

#### LED HAL[[edit](https://wiki.tizen.org/index.php?title=3.0_Porting_Guide/System&action=edit&section=T-15)]

The LED HAL provides functions to control LED lights. The HAL interface is defined in the `hw/led.h` header file of the `libdevice-node` library, and the `pkg-config` `device-node` must be used to use the HAL interface.

The following example shows the interface of the LED HAL.

```
/*
   Device ID
*/
#define LED_HARDWARE_DEVICE_ID  "led"

/*
   Device version
*/
#define LED_HARDWARE_DEVICE_VERSION MAKE_VERSION(1,0)

/*
   LED device ID
*/
#define LED_ID_CAMERA_BACK "camera_back"
#define LED_ID_CAMERA_FRONT "camera_front"
#define LED_ID_NOTIFICATION "notification"
#define LED_ID_TOUCH_KEY "touch_key"

enum led_type {
    LED_TYPE_MANUAL,
    LED_TYPE_BLINK,
};

struct led_state {
    /* LED type */
    enum led_type type;
    /*
       The first byte means opaque and the other 3 bytes are RGB values.
       You can use opaque byte as a led brightness value.
       If the first byte is 0x00, led is switched off.
       Anything else is worked as on. The max value is 0xFF.
    */
    unsigned int color;
    /* Turn on time in milliseconds */
    int duty_on;
    /* Turn off time in milliseconds */
    int duty_off;
};

struct led_device {
    struct hw_common common;

    int (*set_state)(struct led_state *state);
};

```

The following table lists the LED HAL functions.

| Function prototype                       | Description                              |           |
| ---------------------------------------- | ---------------------------------------- | --------- |
| `int (*set_state)(struct led_state *state);` | The function sets LED play style and plays LED lights. | Mandatory |

The following code snippet shows an example of the LED HAL.

```
#ifndef CAMERA_BACK_PATH
#define CAMERA_BACK_PATH "/sys/class/leds/torch-sec1"
#endif

static int
camera_back_set_state(struct led_state *state)
{
    static int max = -1;
    int brt;
    char buf[BUF_MAX];
    int fd;

    if (state->type == LED_TYPE_BLINK) {
        printf("camera back led does not support LED_TYPE_BLINK mode");

        return -ENOTSUP;
    }

    if (max < 0) {
        fd = open(CAMERA_BACK_PATH"/max_brightness", O_RDONLY);
        read(fd, buf, sizeof(buf));
        close(fd);
        max = atoi(buf);
    }

    brt = (state->color >> 24) & 0xFF;
    brt = brt / 255.f * max;

    snprintf(buf, sizeof(buf), "%d", brt);
    fd = open(CAMERA_BACK_PATH"/brightness", O_WRONLY);
    write(fd, buf, strlen(buf));
    close(fd);

    return 0;
}

struct led_device camera_back_dev = {
    .set_state = camera_back_set_state,
};

struct led_device_list {
    const char *id;
    struct led_device *operations;
    struct led_device *dev;
} led_list[] = {
    {LED_ID_CAMERA_BACK, &camera_back_dev, NULL},
    {LED_ID_CAMERA_FRONT, NULL, NULL},
    {LED_ID_NOTIFICATION, NULL, NULL},
    {LED_ID_TOUCH_KEY, NULL, NULL},
};

static int
led_open(struct hw_info *info, const char *id, struct hw_common **common)
{
    int i, list_len, id_len;

    list_len = ARRAY_SIZE(led_list);
    id_len = strlen(id) + 1;
    for (i = 0 ; i < list_len ; i++) {
        if (strncmp(id, led_list[i].id, id_len))
            continue;
        if (!led_list[i].operations)
            return -ENOTSUP;
        if (led_list[i].dev)
            goto out;
        break;
    }

    if (i >= list_len)
        return -EINVAL;
    led_list[i].dev = calloc(1, sizeof(struct led_device));

    led_list[i].dev->common.info = info;
    led_list[i].dev->set_state
        = led_list[i].operations->set_state;

out:
    *common = (struct hw_common *)led_list[i].dev;

    return 0;
}

static int
led_close(struct hw_common *common)
{
    free(common);

    return 0;
}

HARDWARE_MODULE_STRUCTURE = {
    .magic = HARDWARE_INFO_TAG,
    .hal_version = HARDWARE_INFO_VERSION,
    .device_version = LED_HARDWARE_DEVICE_VERSION,
    .id = LED_HARDWARE_DEVICE_ID,
    .name = "Default LED",
    .open = led_open,
    .close = led_close,
};

```

#### IR HAL[[edit](https://wiki.tizen.org/index.php?title=3.0_Porting_Guide/System&action=edit&section=T-16)]

The IR HAL provides functions to control IR transmission. The HAL interface is defined in the `hw/ir.h` header file of the `libdevice-node` library, and the `pkg-config` `device-node` must be used to use the HAL interface.

The following example shows the interface of the IR HAL.

```
/*
   Device ID
*/
#define IR_HARDWARE_DEVICE_ID "ir"

/*
   Device version
*/
#define IR_HARDWARE_DEVICE_VERSION MAKE_VERSION(0,1)

struct ir_device {
    struct hw_common common;

    /* Control the IR state */
    int (*is_available)(bool *available);
    int (*transmit)(int *frequency_pattern, int size);
};

```

The following table lists the IR HAL functions.

| Function prototype                       | Description                              |           |
| ---------------------------------------- | ---------------------------------------- | --------- |
| `int (*is_available)(bool *available);`  | The function returns whether the target device supports IR transmission. | Mandatory |
| `int (*transmit)(int *frequency_pattern, int size);` | The function transmits IR with frequency pattern and its size. | Mandatory |

The following code snippet shows an example of the IR HAL.

```
#define IRLED_CONTROL_PATH "/sys/class/ir/ir_send"

static int
ir_is_available(bool *available)
{
    *available = true;

    return 0;
}

static int
ir_transmit(int *frequency_pattern, int size)
{
    int i, ret;

    for (i = 0; i < size; i++) {
        snprintf(buf, sizeof(buf), "%d", frequency_pattern[i]);
        fd = open(IRLED_CONTROL_PATH, O_WRONLY);
        write(fd, buf, strlen(buf));
        close(fd);
    }   

    return 0;
}

static int
ir_open(struct hw_info *info, const char *id, struct hw_common **common)
{
    struct ir_device *ir_dev;

    ir_dev = calloc(1, sizeof(struct ir_device));

    ir_dev->common.info = info;
    ir_dev->is_available = ir_is_available;
    ir_dev->transmit = ir_transmit;

    *common = (struct hw_common *)ir_dev;

    return 0;
}

static int
ir_close(struct hw_common *common)
{
    free(common);

    return 0;
}

HARDWARE_MODULE_STRUCTURE = {
    .magic = HARDWARE_INFO_TAG,
    .hal_version = HARDWARE_INFO_VERSION,
    .device_version = IR_HARDWARE_DEVICE_VERSION,
    .id = IR_HARDWARE_DEVICE_ID,
    .name = "ir",
    .open = ir_open,
    .close = ir_close,
};

```

#### Touchscreen HAL[[edit](https://wiki.tizen.org/index.php?title=3.0_Porting_Guide/System&action=edit&section=T-17)]

The touchscreen HAL provides functions to on/off touchscreen. The HAL interface is defined in the `hw/touchscreenf.h` header file of the `libdevice-node` library, and the `pkg-config` `device-node` must be used to use the HAL interface.

The following example shows the interface of the touchscreen HAL.

```
/*
   Device ID
*/
#define TOUCHSCREEN_HARDWARE_DEVICE_ID "touchscreen"

/*
   Device version
*/
#define TOUCHSCREEN_HARDWARE_DEVICE_VERSION MAKE_VERSION(0,1)

enum touchscreen_state {
    TOUCHSCREEN_OFF, /* Disable touchscreen */
    TOUCHSCREEN_ON, /* Enable touchscreen */
};

struct touchscreen_device {
    struct hw_common common;

    /* Control touchscreen state */
    int (*get_state)(enum touchscreen_state *state);
    int (*set_state)(enum touchscreen_state state);
};

```

The following table lists the touchscreen HAL functions.

| Function prototype                       | Description                              |           |
| ---------------------------------------- | ---------------------------------------- | --------- |
| `int (*get_state)(enum touchscreen_state *state);` | The function returns whether the touchscreen is enabled. | Mandatory |
| `int (*set_state)(enum touchscreen_state state);` | The function enables and disables the touchscreen. | Mandatory |

The following code snippet shows an example of the touchscreen HAL.

```
#define TURNON_TOUCHSCREEN 1
#define TURNOFF_TOUCHSCREEN 0
#define TOUCHSCREEN_PATH "/sys/class/input/touchscreen/enable"

static int
touchscreen_get_state(enum touchscreen_state *state)
{
    int val;
    int fd;
    char buf[BUF_MAX];

    fd = open(TOUCHSCREEN_PATH, O_RDONLY);
    read(fd, buf, sizeof(buf));
    close(fd);
    val = atoi(buf);

    switch (val) {
    case TURNOFF_TOUCHSCREEN:
        *state = TOUCHSCREEN_OFF;
        break;
    case TURNON_TOUCHSCREEN:
        *state = TOUCHSCREEN_ON;
        break;
    default:
        return -EINVAL;
    }

    return 0;
}

static int
touchscreen_set_state(enum touchscreen_state state)
{
    int val;
    char buf[BUF_MAX];

    switch (state) {
    case TOUCHSCREEN_OFF:
        val = TURNOFF_TOUCHSCREEN;
        break;
    case TOUCHSCREEN_ON:
        val = TURNON_TOUCHSCREEN;
        break;
    default:
        return -EINVAL;
    }

    snprintf(buf, sizeof(buf), "%d", val);
    fd = open(TOUCHSCREEN_PATH, O_WRONLY);
    write(fd, buf, strlen(buf));
    close(fd);

    return ret;
}

static int
touchscreen_open(struct hw_info *info, const char *id, struct hw_common **common)
{
    struct touchscreen_device *touchscreen_dev;

    touchscreen_dev = calloc(1, sizeof(struct touchscreen_device));

    touchscreen_dev->common.info = info;
    touchscreen_dev->get_state = touchscreen_get_state;
    touchscreen_dev->set_state = touchscreen_set_state;

    *common = (struct hw_common *)touchscreen_dev;

    return 0;
}

static int
touchscreen_close(struct hw_common *common)
{
    free(common);

    return 0;
}

HARDWARE_MODULE_STRUCTURE = {
    .magic = HARDWARE_INFO_TAG,
    .hal_version = HARDWARE_INFO_VERSION,
    .device_version = TOUCHSCREEN_HARDWARE_DEVICE_VERSION,
    .id = TOUCHSCREEN_HARDWARE_DEVICE_ID,
    .name = "touchscreen",
    .open = touchscreen_open,
    .close = touchscreen_close,
};

```

## Sensor Framework[[edit](https://wiki.tizen.org/index.php?title=3.0_Porting_Guide/Sensor&action=edit&section=T-1)]

Sensor devices are used widely in mobile devices to enhance user experience. Most modern mobile OSs have a framework which manages hardware and virtual sensors on the platform and provides convenient API to the application.

#### Types of Sensors[[edit](https://wiki.tizen.org/index.php?title=3.0_Porting_Guide/Sensor&action=edit&section=T-2)]

Sensors are classified as hardware and virtual sensors. Tizen supports individual HAL for the following sensors:

- Hardware sensors
  - Accelerometer
  - Geomagnetic sensor
  - Gyroscope
  - Light sensor
  - Proximity sensor
  - Pressure sensor
  - Ultraviolet sensor
  - Temperature sensor
  - Humidity sensor
  - HRM (Heart Rate Monitor)
  - HRM LED green sensor
  - HRM LED IR sensor
  - HRM LED red sensor
  - Uncalibrated geomagnetic sensor
  - Uncalibrated gyroscope sensor
  - Human pedometer
  - Human sleep monitor
  - Human sleep detector
  - Human stress monitor
- Virtual sensors
  - Orientation sensor
  - Gravity sensor
  - Linear acceleration sensor
  - Rotation vector sensor
  - Gyroscope rotation vector sensor
  - Geomagnetic rotation vector sensor

#### Architectural Overview[[edit](https://wiki.tizen.org/index.php?title=3.0_Porting_Guide/Sensor&action=edit&section=T-3)]

The sensor framework provides a sensor server for managing sensor HALs and a medium through which the client applications are connected to the sensor handler to exchange data.

[![Sensor Framework Architecture](https://wiki.tizen.org/images/thumb/2/2f/Tizen_3_sensorfw.png/684px-Tizen_3_sensorfw.png)](https://wiki.tizen.org/File:Tizen_3_sensorfw.png)

The sensor HALs retrieve data from sensor hardware and enable the client applications to use the data form specific requirements.

#### Components of the Sensor Framework[[edit](https://wiki.tizen.org/index.php?title=3.0_Porting_Guide/Sensor&action=edit&section=T-4)]

- Sensor Client Library

Any application that wants to access the sensor server and communicate with it must use the sensor API library. Using the Sensor API, the application can control sensors and receive sensor events from the sensor server. 
As shown in the above diagram, any application or middleware framework, by using the sensor API, can have the sensor client library executing within its own process context.

- Sensor Server

The sensor server is a daemon which communicates uniquely to multiple sensors (through drivers) in the system and dispatches sensor data or events back to the application. 
The sensor server takes care of initializing the sensors during boot, driver configuration, sensor data fetching and delivery, and managing all sensors and client on the platform.

- Sensor HAL (Hardware Abstraction Layer)

The sensor HAL, which is interfaced to the sensor server, takes care of interacting with the sensor drivers. HAL processes the data from the sensor drivers and communicates it to the server. Hardware sensors have to support HAL.
The sensor HAL is implemented as a shared library and the sensor_loader finds hal so library and loads it from the `/usr/lib/sensor/` directory at booting time.

### Porting HAL Interface[[edit](https://wiki.tizen.org/index.php?title=3.0_Porting_Guide/Sensor&action=edit&section=T-5)]

#### Sensor[[edit](https://wiki.tizen.org/index.php?title=3.0_Porting_Guide/Sensor&action=edit&section=T-6)]

[![Tizen 3 sensor fw hal.png](https://wiki.tizen.org/images/thumb/8/88/Tizen_3_sensor_fw_hal.png/591px-Tizen_3_sensor_fw_hal.png)](https://wiki.tizen.org/File:Tizen_3_sensor_fw_hal.png)

- Adding New Hardware Sensors

For porting new hardware sensors, the HAL library inherited `sensor_device` interface has to be implemented. You can find the HAL header files in `git:sensord/src/hal`.

The Tizen HAL sensor types are also defined in the `sensor_hal_types.h` header file under the names `SENSOR_DEVICE_...`.

The following code snippet shows the interface of the sensor HAL in the `sensor_hal.h` header file.

```
/*
   Create devices
*/
typedef void *sensor_device_t;
typedef int (*create_t)(sensor_device_t **devices);

/*
   Sensor device interface
   1 device must be abstracted from 1 device event node
*/
class sensor_device {
public:
    virtual ~sensor_device() {}

    uint32_t get_hal_version(void)
    {
        return SENSOR_HAL_VERSION(1, 0);
    }

    virtual int get_poll_fd(void) = 0;
    virtual int get_sensors(const sensor_info_t **sensors) = 0;

    virtual bool enable(uint32_t id) = 0;
    virtual bool disable(uint32_t id) = 0;

    virtual int read_fd(uint32_t **ids) = 0;
    virtual int get_data(uint32_t id, sensor_data_t **data, int *length) = 0;

    virtual bool set_interval(uint32_t id, unsigned long val)
    {
        return true;
    }
    virtual bool set_batch_latency(uint32_t id, unsigned long val)
    {
        return true;
    }
    virtual bool set_attribute_int(uint32_t id, int32_t attribute, int32_t value)
    {
        return true;
    }
    virtual bool set_attribute_str(uint32_t id, int32_t attribute, char *value, int value_len)
    {
        return true;
    }
    virtual bool flush(uint32_t id)
    {
        return true;
    }
};

```

The following table shows the description of the `sensor_device` interface.

| Prototype                                | Description                              | Return value      |
| ---------------------------------------- | ---------------------------------------- | ----------------- |
| `uint32_t get_hal_version(void)`         | Returns the HAL version.                 | Version           |
| `int get_poll_fd(void)`                  | Returns the file description to poll events. | `fd`              |
| `int get_sensors(const sensor_info_t **sensors)` | Returns the list of supported sensors.See the `sensor_info_t` in the `sensor_hal_types.h` header file. | Size              |
| `bool enable(uint32_t id)`               | Enables the sensor.                      | `true` on success |
| `bool disable(uint32_t id)`              | Disables the sensor.                     | `true` on success |
| `int read_fd(uint32_t **ids)`            | Returns the sensor device IDs.The sensor framework calls this function when an event is detected from the `poll-fd` | Size              |
| `int get_data(uint32_t id, sensor_data_t **data, int *length)` | Updates the `sensor_data_t` object (data) with the details about the sensor, such as accuracy, timestamp, and values.Note that the `sensor_data_t` object has to be created using the `malloc()` function. | 0 on success      |
| `bool set_interval(uint32_t id, unsigned long val)` | Sets the interval.                       | `true` on success |
| `bool set_batch_latency(uint32_t id, unsigned long val)` | Sets the batch latecy.                   | `true` on success |
| `bool set_attribute_int(uint32_t id, int32_t attribute, int32_t value)` | Sets the `int` value to the attribute.   | `true` on success |
| `bool set_attribute_str(uint32_t id, int32_t attribute, char *value, int value_len)` | Sets the string value to attribute.      | `true` on success |
| `bool flush(uint32_t id)`                | Flushes the sensor events.               | `true` on success |
| `int (create_t *)(sensor_device_t **devices)` | Returns the list of `sensor_device`.You must implement this interface for creating the sensor module in `sensord`. | Size              |

The following code snippet shows the interface of the sensor HAL types in the `sensor_hal_type.h` header file.

```
/*
   Sensor Types
   These types are used to control the sensors
  
   - base unit
     acceleration values : meter per second^2 (m/s^2)
     magnetic values     : micro-Tesla (uT)
     orientation values  : degrees
     gyroscope values    : degree/s
     temperature values  : degrees centigrade
     proximity valeus    : distance
     light values        : lux
     pressure values     : hectopascal (hPa)
     humidity            : relative humidity (%)
*/
typedef enum {
    SENSOR_DEVICE_UNKNOWN = -2,
    SENSOR_DEVICE_ALL = -1,
    SENSOR_DEVICE_ACCELEROMETER,
    SENSOR_DEVICE_GRAVITY,
    SENSOR_DEVICE_LINEAR_
    SENSOR_DEVICE_GEOMAGNETIC,
    SENSOR_DEVICE_ROTATION_VECTOR,
    SENSOR_DEVICE_ORIENTATION,
    SENSOR_DEVICE_GYROSCOPE,
    SENSOR_DEVICE_LIGHT,
    SENSOR_DEVICE_PROXIMITY,
    SENSOR_DEVICE_PRESSURE,
    SENSOR_DEVICE_ULTRAVIOLET,
    SENSOR_DEVICE_TEMPERATURE,
    SENSOR_DEVICE_HUMIDITY,
    SENSOR_DEVICE_HRM,
    SENSOR_DEVICE_HRM_LED_GREEN,
    SENSOR_DEVICE_HRM_LED_IR,
    SENSOR_DEVICE_HRM_LED_RED,
    SENSOR_DEVICE_GYROSCOPE_UNCAL,
    SENSOR_DEVICE_GEOMAGNETIC_UNCAL,
    SENSOR_DEVICE_GYROSCOPE_RV,
    SENSOR_DEVICE_GEOMAGNETIC_RV,

    SENSOR_DEVICE_HUMAN_PEDOMETER = 0x300,
    SENSOR_DEVICE_HUMAN_SLEEP_MONITOR,
    SENSOR_DEVICE_HUMAN_SLEEP_DETECTOR,
    SENSOR_DEVICE_HUMAN_STRESS_MONITOR,

    SENSOR_DEVICE_EXERCISE_WALKING = 0x400,
    SENSOR_DEVICE_EXERCISE_RUNNING,
    SENSOR_DEVICE_EXERCISE_HIKING,
    SENSOR_DEVICE_EXERCISE_CYCLING,
    SENSOR_DEVICE_EXERCISE_ELLIPTICAL,
    SENSOR_DEVICE_EXERCISE_INDOOR_CYCLING,
    SENSOR_DEVICE_EXERCISE_ROWING,
    SENSOR_DEVICE_EXERCISE_STEPPER,

    SENSOR_DEVICE_FUSION = 0x900,
    SENSOR_DEVICE_AUTO_ROTATION,
    SENSOR_DEVICE_AUTO_BRIGHTNESS,

    SENSOR_DEVICE_GESTURE_MOVEMENT = 0x1200,
    SENSOR_DEVICE_GESTURE_WRIST_UP,
    SENSOR_DEVICE_GESTURE_WRIST_
    SENSOR_DEVICE_GESTURE_MOVEMENT_STATE,

    SENSOR_DEVICE_ACTIVITY_TRACKER = 0x1A00,
    SENSOR_DEVICE_ACTIVITY_LEVEL_MONITOR,
} sensor_device_type;

```

The following code snippet shows the interface of the sensor HAL infomation in the `sensor_hal_type.h` header file.

```
/*
   A platform sensor handler is generated based on this handle
   This ID can be assigned from HAL developer, so it has to be unique in 1 sensor_device.
*/
typedef struct sensor_info_t {
    uint32_t
    const char *name;
    sensor_device_type type;
    unsigned int event_type; /* for Internal API */
    const char *model_name;
    const char *vendor;
    float min_range;
    float max_range;
    float resolution;
    int min_interval;
    int max_batch_count;
    bool wakeup_supported;
} sensor_info_t;

enum sensor_accuracy_t {
    SENSOR_ACCURACY_UNDEFINED = -1,
    SENSOR_ACCURACY_BAD = 0,
    SENSOR_ACCURACY_NORMAL = 1,
    SENSOR_ACCURACY_GOOD = 2,
    SENSOR_ACCURACY_VERYGOOD = 3
};

#define SENSOR_DATA_VALUE_SIZE 16

/* sensor_data_t */
typedef struct sensor_data_t {
    int accuracy;
    unsigned long long timestamp;
    int value_count;
    float values[SENSOR_DATA_VALUE_SIZE];
} sensor_data_t;

#define SENSOR_PEDOMETER_DATA_DIFFS_SIZE	20

typedef struct {
    int accuracy;
    unsigned long long timestamp;
    int value_count; /* value_count == 8 */
    float values[SENSOR_DATA_VALUE_SIZE];
    /* values = {step count, walk step count, run step count,
	         moving distance, calorie burned, last speed,
	         last stepping frequency (steps per sec),
	         last step status (walking, running, ...)} */
    /* Additional data attributes (not in sensor_data_t)*/
    int diffs_count;
    struct differences {
        int timestamp;
        int steps;
        int walk_steps;
        int run_steps;
        int walk_up_steps;
        int walk_down_steps;
        int run_up_steps;
        int run_down_steps;
        float distance;
        float calories;
        float speed;
    } diffs[SENSOR_PEDOMETER_DATA_DIFFS_SIZE];
} sensor_pedometer_data_t;

#define CONVERT_TYPE_ATTR(type, index) ((type) << 8 | 0x80 | (index))

enum sensor_attribute {
    SENSOR_ATTR_ACTIVITY = CONVERT_TYPE_ATTR(SENSOR_DEVICE_ACTIVITY_TRACKER, 0x1),
};

enum sensor_activity {
    SENSOR_ACTIVITY_UNKNOWN = 1,
    SENSOR_ACTIVITY_STILL = 2,
    SENSOR_ACTIVITY_WALKING = 4,
    SENSOR_ACTIVITY_RUNNING = 8,
    SENSOR_ACTIVITY_IN_VEHICLE = 16,
    SENSOR_ACTIVITY_ON_BICYCLE = 32,
};

```

The following code snippet shows an example of the `sensor_device` implementation for the accelerometer (`sensor-hal-tm1/src/`).

```
/* In create.cpp */
#include <sensor/sensor_hal.h>
#include <sensor_log.h>
#include <vector>

#include "accel/accel_device.h"

static std::vector<sensor_device_t> devs;

template<typename _sensor>
void
create_sensor(const char *name)
{
    sensor_device *instance = NULL;
    try {
        instance = new _sensor;
    } catch (std::exception &e) {
        ERR("Failed to create %s sensor device, exception: %s", name, e.what());

        return;
    } catch (int err) {
        _ERRNO(err, _E, "Failed to create %s sensor device", name);

        return;
    }

    devs.push_back(instance);
}

extern "C" int create(sensor_device_t **devices)
{
#ifdef ENABLE_ACCEL
    create_sensor<accel_device>("Accelerometer");
#endif

    *devices = &devs[0];
    
    return devs.size();
}

```

```
/* In accel_device.h */
#ifndef _ACCEL_DEVICE_H_
#define _ACCEL_DEVICE_H_

#include <sensor/sensor_hal.h>
#include <string>
#include <vector>
#include <functional>

class accel_device : public sensor_device {
public:
    accel_device();
    virtual ~accel_device();

    int get_poll_fd(void);
    int get_sensors(const sensor_info_t **sensors);

    bool enable(uint32_t id);
    bool disable(uint32_t id);

    bool set_interval(uint32_t id, unsigned long val);

    int read_fd(uint32_t **ids);
    int get_data(uint32_t id, sensor_data_t **data, int *length);

private:
    int m_node_handle;
    int m_x;
    int m_y;
    int m_z;
    unsigned long m_polling_interval;
    unsigned long long m_fired_time;
    bool m_sensorhub_controlled;

    int m_method;
    std::string m_data_node;
    std::string m_enable_node;
    std::string m_interval_node;

    std::function<bool (void)> update_value;

    std::vector<uint32_t> event_ids;

    bool update_value_input_event(void);
    bool update_value_iio(void);

    void raw_to_base(sensor_data_t *data);
};
#endif /* _ACCEL_DEVICE_H_ */

```

```
/* In accel_device.cpp */
#include <fcntl.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>

#include <linux/input.h>
#include <sys/ioctl.h>
#include <poll.h>

#include <util.h>
#include <sensor_common.h>
#include <sensor_log.h>

#include "accel_device.h"

#define MODEL_NAME "K2HH"
#define VENDOR "ST Microelectronics"
#define RESOLUTION 16
#define RAW_DATA_UNIT 0.122
#define MIN_INTERVAL 1
#define MAX_BATCH_COUNT 0

#define SENSOR_NAME "SENSOR_ACCELEROMETER"
#define SENSOR_TYPE_ACCEL		"ACCEL"

#define INPUT_NAME	"accelerometer_sensor"
#define ACCEL_SENSORHUB_POLL_NODE_NAME "accel_poll_delay"

#define GRAVITY 9.80665
#define G_TO_MG 1000
#define RAW_DATA_TO_G_UNIT(X) (((float)(X))/((float)G_TO_MG))
#define RAW_DATA_TO_METRE_PER_SECOND_SQUARED_UNIT(X) (GRAVITY * (RAW_DATA_TO_G_UNIT(X)))

#define MIN_RANGE(RES) (-((1 << (RES))/2))
#define MAX_RANGE(RES) (((1 << (RES))/2)-1)

static sensor_info_t sensor_info = {
    id: 0x1,
    name: SENSOR_NAME,
    type: SENSOR_DEVICE_ACCELEROMETER,
    event_type: (SENSOR_DEVICE_ACCELEROMETER << SENSOR_EVENT_SHIFT) | RAW_DATA_EVENT,
    model_name: MODEL_NAME,
    vendor: VENDOR,
    min_range: MIN_RANGE(RESOLUTION) * RAW_DATA_TO_METRE_PER_SECOND_SQUARED_UNIT(RAW_DATA_UNIT),
    max_range: MAX_RANGE(RESOLUTION) * RAW_DATA_TO_METRE_PER_SECOND_SQUARED_UNIT(RAW_DATA_UNIT),
    resolution: RAW_DATA_TO_METRE_PER_SECOND_SQUARED_UNIT(RAW_DATA_UNIT),
    min_interval: MIN_INTERVAL,
    max_batch_count: MAX_BATCH_COUNT,
    wakeup_supported: false
};

accel_device::accel_device()
: m_node_handle(-1)
, m_x(-1)
, m_y(-1)
, m_z(-1)
, m_polling_interval(1000)
, m_fired_time(0)
, m_sensorhub_controlled(false)
{
    const std::string sensorhub_interval_node_name = ACCEL_SENSORHUB_POLL_NODE_NAME;

    node_info_query query;
    node_info info;

    query.sensorhub_controlled = m_sensorhub_controlled = util::is_sensorhub_controlled(sensorhub_interval_node_name);
    query.sensor_type = SENSOR_TYPE_ACCEL;
    query.key = INPUT_NAME;
    query.iio_enable_node_name = "accel_enable";
    query.sensorhub_interval_node_name = sensorhub_interval_node_name;

    if (!util::get_node_info(query, info)) {
        _E("Failed to get node info");
        throw ENXIO;
    }

    util::show_node_info(info);

    m_method = info.method;
    m_data_node = info.data_node_path;
    m_enable_node = info.enable_node_path;
    m_interval_node = info.interval_node_path;

    m_node_handle = open(m_data_node.c_str(), O_RDONLY);

    if (m_node_handle < 0) {
        _ERRNO(errno, _E, "accel handle open fail for accel processor");
        throw ENXIO;
    }

    if (m_method == INPUT_EVENT_METHOD) {
        if (!util::set_monotonic_clock(m_node_handle))
            throw ENXIO;

        update_value = [=]() {
            return this->update_value_input_event();
        };
    } else {
        if (!info.buffer_length_node_path.empty())
            util::set_node_value(info.buffer_length_node_path, 480);

        if (!info.buffer_enable_node_path.empty())
            util::set_node_value(info.buffer_enable_node_path, 1);

        update_value = [=]() {
            return this->update_value_iio();
        };
    }

    _I("accel_device is created!");
}

accel_device::~accel_device()
{
    close(m_node_handle);
    m_node_handle = -1;

    _I("accel_device is destroyed!");
}

int
accel_device::get_poll_fd(void)
{
    return m_node_handle;
}

int
accel_device::get_sensors(const sensor_info_t **sensors)
{
    *sensors = &sensor_info;

    return 1;
}

bool
accel_device::enable(uint32_t id)
{
    util::set_enable_node(m_enable_node, m_sensorhub_controlled, true, SENSORHUB_ACCELEROMETER_ENABLE_BIT);
    set_interval(id, m_polling_interval);

    m_fired_time = 0;
    _I("Enable accelerometer sensor");
    
    return true;
}

bool
accel_device::disable(uint32_t id)
{
    util::set_enable_node(m_enable_node, m_sensorhub_controlled, false, SENSORHUB_ACCELEROMETER_ENABLE_BIT);

    _I("Disable accelerometer sensor");
	
    return true;
}

bool
accel_device::set_interval(uint32_t id, unsigned long val)
{
    unsigned long long polling_interval_ns;

    polling_interval_ns = ((unsigned long long)(val) * 1000llu * 1000llu);

    if (!util::set_node_value(m_interval_node, polling_interval_ns)) {
        _E("Failed to set polling resource: %s", m_interval_node.c_str());

        return false;
    }

    _I("Interval is changed from %dms to %dms", m_polling_interval, val);
    m_polling_interval = val;
    
    return true;
}

bool
accel_device::update_value_input_event(void)
{
    int accel_raw[3] = {0,};
    bool x,y,z;
    int read_input_cnt = 0;
    const int INPUT_MAX_BEFORE_SYN = 10;
    unsigned long long fired_time = 0;
    bool syn = false;

    x = y = z = false;

    struct input_event accel_input;
    _D("accel event detection!");

    while ((syn == false) && (read_input_cnt < INPUT_MAX_BEFORE_SYN)) {
        int len = read(m_node_handle, &accel_input, sizeof(accel_input));
        if (len != sizeof(accel_input)) {
            _E("accel_file read fail, read_len = %d",len);
			
            return false;
        }

        ++read_input_cnt;

        if (accel_input.type == EV_REL) {
            switch (accel_input.code) {
            case REL_X:
                accel_raw[0] = (int)accel_input.value;
                x = true;
                break;
            case REL_Y:
                accel_raw[1] = (int)accel_input.value;
                y = true;
                break;
            case REL_Z:
                accel_raw[2] = (int)accel_input.value;
                z = true;
                break;
            default:
                _E("accel_input event[type = %d, code = %d] is unknown.", accel_input.type, accel_input.code);

                return false;
                break;
            }
        } else if (accel_input.type == EV_SYN) {
            syn = true;
            fired_time = util::get_timestamp(&accel_input.time);
        } else {
            _E("accel_input event[type = %d, code = %d] is unknown.", accel_input.type, accel_input.code);

            return false;
        }
    }

    if (syn == false) {
        _E("EV_SYN didn't come until %d inputs had come", read_input_cnt);
		
        return false;
    }

    if (x)
        m_x =  accel_raw[0];
    if (y)
        m_y =  accel_raw[1];
    if (z)
        m_z =  accel_raw[2];

    m_fired_time = fired_time;

    _D("m_x = %d, m_y = %d, m_z = %d, time = %lluus", m_x, m_y, m_z, m_fired_time);

    return true;
}

bool
accel_device::update_value_iio(void)
{
    struct {
        int16_t x;
        int16_t y;
        int16_t z;
        int64_t timestamp;
    } __attribute__((packed)) data;

    struct pollfd pfd;

    pfd.fd = m_node_handle;
    pfd.events = POLLIN | POLLERR;
    pfd.revents = 0;

    int ret = poll(&pfd, 1, -1);

    if (ret == -1) {
        _ERRNO(errno, _E, "Failed to poll from m_node_handle:%d", m_node_handle);

        return false;
    } else if (!ret) {
        _E("poll timeout m_node_handle:%d", m_node_handle);
	
        return false;
    }

    if (pfd.revents & POLLERR) {
        _E("poll exception occurred! m_node_handle:%d", m_node_handle);

        return false;
    }

    if (!(pfd.revents & POLLIN)) {
        _E("poll nothing to read! m_node_handle:%d, pfd.revents = %d", m_node_handle, pfd.revents);

        return false;
    }

    int len = read(m_node_handle, &data, sizeof(data));

    if (len != sizeof(data)) {
        _E("Failed to read data, m_node_handle:%d read_len:%d", m_node_handle, len);
	
        return false;
    }

    m_x = data.x;
    m_y = data.y;
    m_z = data.z;
    m_fired_time = data.timestamp;

    _D("m_x = %d, m_y = %d, m_z = %d, time = %lluus", m_x, m_y, m_z, m_fired_time);

    return true;
}

int
accel_device::read_fd(uint32_t **ids)
{
    if (!update_value()) {
        _D("Failed to update value");

        return false;
    }

    event_ids.clear();
    event_ids.push_back(sensor_info.id);

    *ids = &event_ids[0];

    return event_ids.size();
}

int
accel_device::get_data(uint32_t id, sensor_data_t **data, int *length)
{
    sensor_data_t *sensor_data;

    /* [Important] In HAL, you MUST allocate memory for data. 
     * HAL doesn't need to care of releasing this memory because this memory must be released after sending this data to clients.
    */
    sensor_data = (sensor_data_t *)malloc(sizeof(sensor_data_t));
    retvm_if(!sensor_data, -ENOMEM, "Memory allocation failed");

    sensor_data->accuracy = SENSOR_ACCURACY_GOOD;
    sensor_data->timestamp = m_fired_time;
    sensor_data->value_count = 3;
    sensor_data->values[0] = m_x;
    sensor_data->values[1] = m_y;
    sensor_data->values[2] = m_z;

    raw_to_base(sensor_data);

    *data = sensor_data;
    *length = sizeof(sensor_data_t);

    return 0;
}

void
accel_device::raw_to_base(sensor_data_t *data)
{
    data->values[0] = RAW_DATA_TO_METRE_PER_SECOND_SQUARED_UNIT(data->values[0] * RAW_DATA_UNIT);
    data->values[1] = RAW_DATA_TO_METRE_PER_SECOND_SQUARED_UNIT(data->values[1] * RAW_DATA_UNIT);
    data->values[2] = RAW_DATA_TO_METRE_PER_SECOND_SQUARED_UNIT(data->values[2] * RAW_DATA_UNIT);
}

```

#### Sensorhub[[edit](https://wiki.tizen.org/index.php?title=3.0_Porting_Guide/Sensor&action=edit&section=T-7)]

The sensorhub HAL supports multiple sensors logically from 1 physical device file. In case many sensors are simultaneously supported by the single device file, the sensorhub HAL can be comprised so that it can operate each sensor as a logically separate device.

- Providing the sensor HAL interface to manufacturers/vendors through the `sensor_hal.h` and `sensor_hal_types.h` header files.
- Using just 1 thread for polling sensor events from multiple device files

[![Tizen_3_Sensorhub_Architecture](https://wiki.tizen.org/images/thumb/6/6e/Tizen_3_sensorhub2.png/597px-Tizen_3_sensorhub2.png)](https://wiki.tizen.org/File:Tizen_3_sensorhub2.png)

The sensorhub HAL can be developed by using the `sensor_device` interface. An example of sensorhub HAL can be found in the `sensor-hal-tm1/src/sensorhub` git.

IDs can be assigned by the vendor or manufacturer for the sensorhub sensors by using the following `sensor_info_t` interface.

```
typedef struct sensor_info_t {                  
    uint32_t id;
    const char *name;                           
    sensor_device_type type;                    
    unsigned int event_type; /* For Internal API */
    const char *model_name;                     
    const char *vendor;                         
    float min_range;                            
    float max_range;                            
    float resolution;                           
    int min_interval;                           
    int max_batch_count;                        
    bool wakeup_supported;                      
} sensor_info_t; 

```

The following code snippet shows an example of the sensorhub HAL implementation.

```
#include <algorithm>
#include <sensor_log.h>

#include "sensorhub.h"
#include "sensorhub_controller.h"
#include "sensorhub_manager.h"
#include "system_state.h"

sensorhub_device::sensorhub_device()
{
    controller = &sensorhub_controller::get_instance();
    if (!controller) {
        ERR("Failed to allocated memory");
        throw;
    }

    manager = &sensorhub_manager::get_instance();
    if (!manager) {
        ERR("Failed to allocated memory");
        throw;
    }
    manager->set_controller(controller);
    system_state_handler::get_instance().set_controller(controller);

    INFO("sensorhub_device is created!");
}

sensorhub_device::~sensorhub_device()
{
    INFO("sensorhub_device is destroyed!");
}

int
sensorhub_device::get_poll_fd(void)
{
    return controller->get_poll_fd();
}

int
sensorhub_device::get_sensors(const sensor_info_t **sensors)
{
    int size;
    size = manager->get_sensors(sensors);
    
    return size;
}

bool
sensorhub_device::enable(uint32_t id)
{
    system_state_handler::get_instance().initialize();

    controller->enable();
    sensorhub_sensor *sensor = manager->get_sensor(id);

    if (!sensor) {
        ERR("Failed to enable sensor(0x%x)", id);

        return false;
    }

    return sensor->enable();
}

bool
sensorhub_device::disable(uint32_t id)
{
    system_state_handler::get_instance().finalize();

    controller->disable();
    sensorhub_sensor *sensor = manager->get_sensor(id);

    if (!sensor) {
        ERR("Failed to disable sensor(0x%x)", id);

        return false;
    }

    return sensor->disable();
}

bool
sensorhub_device::set_interval(uint32_t id, unsigned long val)
{
    sensorhub_sensor *sensor = manager->get_sensor(id);

    if (!sensor) {
        ERR("Failed to set interval to sensor(0x%x)", id);

        return false;
    }

    return sensor->set_interval(val);
}

bool
sensorhub_device::set_batch_latency(uint32_t id, unsigned long val)
{
    sensorhub_sensor *sensor = manager->get_sensor(id);

    if (!sensor) {
        ERR("Failed to set batch latency to sensor(0x%x)", id);

        return false;
    }

    return sensor->set_batch_latency(val);
}

bool
sensorhub_device::set_attribute_int(uint32_t id, int32_t attribute, int32_t value)
{
    int ret;

    sensorhub_sensor *sensor = manager->get_sensor(id);

    if (!sensor) {
        ERR("Failed to set attribute to sensor(0x%x)", id);
		
        return false;
    }

    ret = sensor->set_attribute_int(attribute, value);

    if ((ret < 0) && (ret != -EBUSY)) {
        ERR("Failed to send sensorhub data");

        return false;
    }

    if (ret == -EBUSY) {
        WARN("Command is sent during sensorhub firmware update");
        
        return false;
    }

    return true;
}

bool
sensorhub_device::set_attribute_str(uint32_t id, int32_t attribute, char *value, int value_len)
{
    int ret;

    sensorhub_sensor *sensor = manager->get_sensor(id);

    if (!sensor) {
        ERR("Failed to set attribute to sensor(0x%x)", id);
        
        return false;
    }

    ret = sensor->set_attribute_str(attribute, value, value_len);

    if ((ret < 0) && (ret != -EBUSY)) {
        ERR("Failed to send sensorhub data");

        return false;
    }

    if (ret == -EBUSY) {
        WARN("Command is sent during sensorhub firmware update");
	
        return false;
    }

    return true;
}

int
sensorhub_device::read_fd(uint32_t **ids)
{
    sensorhub_data_t data;

    /* Step 1 */
    if (!controller->read_fd(data))
        return 0;

    /* Step 2 */
    const char *hub_data = data.values;
    int data_len = data.value_count;

    /* Step 3 */
    event_ids.clear();

    while (data_len > 0) {
        DBG("Remaining data length: %d", data_len);
        int parsed = parse(hub_data, data_len);
        if (parsed < 0) {
            ERR("Parsing failed");
            break;
        }

        data_len -= parsed;
        hub_data += parsed;
    }

    /* Step 4 */
    int size = event_ids.size();

    if (event_ids.empty())
        return 0;

    *ids = &event_ids[0];

    return size;
}

int
sensorhub_device::get_data(uint32_t id, sensor_data_t **data, int *length)
{
    int remains = 1;

    sensorhub_sensor *sensor = manager->get_sensor(id);
    if (!sensor) {
        ERR("Failed to get data from sensor(0x%x)", id);

        return -1;
    }

    remains = sensor->get_data(data, length);

    return remains;
}

bool
sensorhub_device::flush(uint32_t id)
{
    return false;
}

int
sensorhub_device::parse(const char *hub_data, int data_len)
{
    return parse_data(hub_data, data_len);
}

int
sensorhub_device::parse_data(const char *hub_data, int data_len)
{
    const char *cursor = hub_data;
    int32_t libtype = 0;

    sensorhub_sensor *sensor = manager->get_sensor(libtype);
    if (!sensor) {
        ERR("Unknown Sensorhub lib type: %d", libtype);
        
        return -1;
    }

    event_ids.push_back(sensor->get_id());

    return sensor->parse(cursor, data_len);
}

int
sensorhub_device::parse_debug(const char *hub_data, int data_len)
{
    return 0;
}

```

```
#include <unistd.h>
#include <string.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <dirent.h>
#include <linux/input.h>
#include <sys/ioctl.h>
#include <fstream>

#include <sensor_log.h>
#include <util.h>
#include "sensorhub_controller.h"

sensorhub_controller::sensorhub_controller()
: m_enabled(false)
, m_poll_node(-1)
, m_data_node(-1)
{
}

sensorhub_controller::~sensorhub_controller()
{
}

sensorhub_controller& sensorhub_controller::get_instance(void)
{
    static sensorhub_controller instance;
	
    return instance;
}

int
sensorhub_controller::get_poll_fd(void)
{
    /* Returns the sensorhub fd */

    return -1;
}

bool
sensorhub_controller::enable(void)
{
    m_enabled = true;
    INFO("Enable Sensorhub");
	
    return true;
}

bool
sensorhub_controller::disable(void)
{
    m_enabled = false;
    INFO("Disable Sensorhub");
	
    return true;
}

int
sensorhub_controller::open_input_node(const char* input_node)
{
    /* Implements the specific sensorhub logic */
	
    return -1;
}

bool
sensorhub_controller::read_fd(sensorhub_data_t &data)
{
    /* Implements the specific sensorhub logic */
	
    return false;
}

int
sensorhub_controller::read_sensorhub_data(void)
{
    /* Implements the specific sensorhub logic */

    return -1;
}

int
sensorhub_controller::read_large_sensorhub_data(void)
{
    /* Implements the specific sensorhub logic */
	
    return -1;
}

int
sensorhub_controller::send_sensorhub_data(const char *data, int data_len)
{
    /* Implements the specific sensorhub logic */

    return -1;
}

int
sensorhub_controller::print_sensorhub_data(const char* name, const char *data, int length)
{
    /* Implements the specific sensorhub logic */
    
    return 0;
}

```

### References[[edit](https://wiki.tizen.org/index.php?title=3.0_Porting_Guide/Sensor&action=edit&section=T-8)]

The reference kernel configuration for sensors varies with different vendor types.
However, there is a standard kernel subsystem for sensors, that is IIO(The Industrial I/O subsystem) subsystem. IIO is intended to provide support for devices that in some sense are analog to digital or digital to analog.
For more information, see [https://wiki.analog.com/software/linux/docs/iio/iio](https://wiki.analog.com/software/linux/docs/iio/iio).

Examples)

| Sensor components  | Kernel configuration    | Device nodes                             |
| ------------------ | ----------------------- | ---------------------------------------- |
| Accelerometer      | `CONFIG_INPUT_KR3DH`    | `/dev/input/event0/``/dev/input/event1/``/dev/input/event2/``/dev/input/event3/``/dev/input/event4/``/dev/input/event5/` |
| Proximity          | `CONFIG_INPUT_GP2A`     |                                          |
| Light sensor       | `CONFIG_INPUT_GP2A`     |                                          |
| Electronic compass | `CONFIG_SENSORS_AK8975` |                                          |

### Project Git Repository[[edit](https://wiki.tizen.org/index.php?title=3.0_Porting_Guide/Sensor&action=edit&section=T-9)]

| Project               | Repository                               | Description                              |
| --------------------- | ---------------------------------------- | ---------------------------------------- |
| `capi-system-sensor`  | `platform/core/api/sensor`               | Tizen sensor C-API                       |
| `sensord`             | `platform/core/system/sensord`           | The sensor daemon and libraries for managing sensors and clients |
| `sensor-hal-tm1`      | `platform/adaptation/tm1/sensor-hal-tm1` | Sensor HAL for TM1 device                |
| `sensor-hal-tm2`      | `platform/adaptation/tm2/sensor-hal-tm2` | Sensor HAL for TM2 device                |
| `sensor-hal-tw1`      | `platform/adaptation/tw1/sensor-hal-tw1` | Sensor HAL for TW1 device                |
| `sensor-hal-emulator` | `platform/adaptation/emulator/sensor-hal-emulator` | Sensor HAL for emulator                  |

### Test and Verify Sensors[[edit](https://wiki.tizen.org/index.php?title=3.0_Porting_Guide/Sensor&action=edit&section=T-10)]

`sensor-test package`, which is in sensord git, provides a command line tool for testing sensors, that is `sensorctl`. after installing sensor-test package, you can test sensors by using following commands

- $ sensorctl test accelerometer
- $ sensorctl test gyroscope
- $ sensorctl test accelerometer 100 /* enable accelerometer with interval 100 ms */
- $ sensorctl test accelerometer 100 1000 /* enable accelerometer with interval 100 ms and 1s batch latency */
- $ sensorctl test accelerometer 100 1000 0 /* enable accelerometer with interval 100 ms, 1s batch latency and always on option */
- $ sensorctl info accelerometer /* retrieve accelerometer sensor information */

# Graphics and UI[[edit](https://wiki.tizen.org/index.php?title=Tizen_3.0_Porting_Guide&action=edit&section=9)]

The application composes the graphic user interface by creating a window with toolkit. The display server composites application's windows and show the result on screen. For this procedure, the graphics and UI middleware offers the next 3 modules for client and server.

- [Tizen Buffer Manager (TBM)](https://wiki.tizen.org/TBM)
- [Tizen Display Manager (TDM)](https://wiki.tizen.org/TDM)
- [TPL-EGL](https://wiki.tizen.org/3.0_Porting_Guide/Graphics_and_UI/OpenGL)

[![Graphics-ui-diagram.png](https://wiki.tizen.org/images/9/9d/Graphics-ui-diagram.png)](https://wiki.tizen.org/File:Graphics-ui-diagram.png)

These modules allow the client and server to render with the GPU, share buffers with other processes, and organize hardware output devices for various chipset devices. They are HAL for graphics and UI. Their backend module needs to be implemented for the new hardware device.

- [Tizen Buffer Manager (TBM)](https://wiki.tizen.org/TBM) provides the abstraction interface for the graphic buffer manager in Tizen.
- [Tizen Display Manager (TDM)](https://wiki.tizen.org/TDM) provides the abstraction interface for the display server, such like a X server and a wayland server, to allow the direct access to graphics hardware in a safe and efficient manner as a display HAL.
- [TPL-EGL](https://wiki.tizen.org/3.0_Porting_Guide/Graphics_and_UI/OpenGL) is an abstraction layer for surface and buffer management on Tizen platform aimed to implement the EGL porting layer of OpenGLES driver over various display protocols.

For an application to handle input device's events, the [Input Manager](https://wiki.tizen.org/3.0_Porting_Guide/Graphics_and_UI/Input) is mainly comprised of `libinput` and a thin wrapper around it. It handles input events in wayland compositors and communicates with wayland clients.

## Buffer Management[[edit](https://wiki.tizen.org/index.php?title=3.0_Porting_Guide/Graphics_and_UI&action=edit&section=T-1)]

The TBM has a frontend libary and a backend module. The TBM frontend library is hardware-independent and provides the generic buffer interface for users. On the other hand, the TBM backend module is hardware-dependent and provides the buffer interface depended on the target system. The chipset vendors have to provide their own backend modules in order for the TBM to work well in Tizen platform. This is because the vendors' way to manage the graphic buffers can be different among various chipset devices. TBM already has several backends for reference, such as `libtbm-dumb`, and `libtbm-shm`.

[![Tbm-backend.png](https://wiki.tizen.org/images/thumb/2/22/Tbm-backend.png/642px-Tbm-backend.png)](https://wiki.tizen.org/File:Tbm-backend.png)

With TBM, the client and server can allocate buffers and share it between them. For example, a client allocates a graphic buffer, draws something on it with GL and sends it to the display server for displaying it on the screen without buffer copying. The TBM backend module is implemented as a shared library and the TBM frontend finds the `libtbm-default.so` file and loads it from the `/usr/lib/bufmgr` directory at runtime.

```
sh-3.2# ls -al
lrwxrwxrwx  1 root root    14 Jul 28  2016 libtbm_default.so -> libtbm_sprd.so
lrwxrwxrwx  1 root root    20 Jul 28  2016 libtbm_sprd.so -> libtbm_sprd.so.0.0.0
lrwxrwxrwx  1 root root    20 Jul 28  2016 libtbm_sprd.so.0 -> libtbm_sprd.so.0.0.0
-rwxr-xr-x  1 root root 26728 Jun 29  2016 libtbm_sprd.so.0.0.0

```

- Initialing the TBM backend module

The `TBMModuleData` is for the entry point symbol to initialize the TBM backend module. The TBM backend module must have to define the global data symbol with the name of `tbmModuleData`. The TBM frontend loads the `tbmModuleData` global data symbol and calls the `init()` function at the initial time.

| Note                                     |
| ---------------------------------------- |
| Do not change the name of the symbol in the TBM backend module. |

```
/*
   @brief tbm module data
   Data type for the entry point of the backend module
*/
typedef struct {
    TBMModuleVersionInfo *vers;	/* TBM module information */
    ModuleInitProc init; /* init function of a backend module */
} TBMModuleData;

typedef int (*ModuleInitProc) (tbm_bufmgr, int);

```

At the initialization of the backend module, the backend module allocates the `tbm_bufmgr_backend` instance (`tbm_backend_alloc`), fills the information, and initializes the backend module to the TBM (`tbm_backend_init`).

```
tbm_bufmgr_backend tbm_backend_alloc(void);
void tbm_backend_free(tbm_bufmgr_backend backend);
int tbm_backend_init(tbm_bufmgr bufmgr, tbm_bufmgr_backend backend);

```

```
MODULEINITPPROTO (init_tbm_bufmgr_priv);

static TBMModuleVersionInfo DumbVersRec =
{
    "shm",
    "Samsung",
    TBM_ABI_VERSION,
};

TBMModuleData tbmModuleData = {&DumbVersRec, init_tbm_bufmgr_priv};

int
init_tbm_bufmgr_priv(tbm_bufmgr bufmgr, int fd)
{
    tbm_bufmgr_backend bufmgr_backend;

    bufmgr_shm = calloc(1, sizeof(struct _tbm_bufmgr_shm));

    bufmgr_backend = tbm_backend_alloc();

    bufmgr_backend->priv = (void *)bufmgr_shm;
    bufmgr_backend->bufmgr_deinit = tbm_shm_bufmgr_deinit,
    bufmgr_backend->bo_size = tbm_shm_bo_size,
    bufmgr_backend->bo_alloc = tbm_shm_bo_alloc,
    bufmgr_backend->bo_free = tbm_shm_bo_free,
    bufmgr_backend->bo_import = tbm_shm_bo_import,
    bufmgr_backend->bo_import_fd = NULL,
    bufmgr_backend->bo_export = tbm_shm_bo_export,
    bufmgr_backend->bo_export_fd = NULL,
    bufmgr_backend->bo_get_handle = tbm_shm_bo_get_handle,
    bufmgr_backend->bo_map = tbm_shm_bo_map,
    bufmgr_backend->bo_unmap = tbm_shm_bo_unmap,
    bufmgr_backend->bo_lock = NULL;
    bufmgr_backend->bo_unlock = NULL;
    bufmgr_backend->surface_get_plane_data = tbm_shm_surface_get_plane_data;
    bufmgr_backend->surface_supported_format = tbm_shm_surface_supported_format;


    if (!tbm_backend_init(bufmgr, bufmgr_backend))
    {
        tbm_backend_free(bufmgr_backend);
        free(bufmgr_shm);

        return 0;
    }

    return 1;
}

```

### Porting OAL Interface[[edit](https://wiki.tizen.org/index.php?title=3.0_Porting_Guide/Graphics_and_UI/TBM&action=edit&section=T-1)]

TBM provides the header files to implement the TBM backend module.

| Header file                              | Description                              |
| ---------------------------------------- | ---------------------------------------- |
| [tbm_bufmgr_backend.h](https://review.tizen.org/gerrit/gitweb?p=platform/core/uifw/libtbm.git;a=blob;f=src/tbm_bufmgr_backend.h;h=839ec996de16493e40b90c72066448d770575bca;hb=refs/heads/tizen) | This file includes the information to implement the TBM backend module. |
| [tbm_drm_helper.h](https://review.tizen.org/gerrit/gitweb?p=platform/core/uifw/libtbm.git;a=blob;f=src/tbm_drm_helper.h;h=0c93a378d2ddf64f2bcb9ebf6a1d0b85563670a2;hb=refs/heads/tizen) | This file includes the helper function for the drm interface backend module. |
| [tbm_bufmgr.h](https://review.tizen.org/gerrit/gitweb?p=platform/core/uifw/libtbm.git;a=blob;f=src/tbm_bufmgr.h;h=50fcf08101c2cb0a4b8750f3eda30d375c981ea7;hb=refs/heads/tizen) | This is the user header file including the general information to use the TBM. |
| [tbm_surface.h](https://review.tizen.org/gerrit/gitweb?p=platform/core/uifw/libtbm.git;a=blob;f=src/tbm_surface.h;h=0686a4ed2d0e26c0386e9f1232f0aa2a6e7f5eb6;hb=refs/heads/tizen) | This is the user header file including the general information to use the `tbm_surface`. |

- TBM Backend interface

The following table lists the TBM Backend interface for initializing and deinitializing.

| Function                       | Description                              |           |
| ------------------------------ | ---------------------------------------- | --------- |
| `ModuleInitProc()`             | The `init` function of a backend module. | Mandatory |
| `bufmgr_deinit()`              | Deinitializes the buffer manager private. | Mandatory |
| `bufmgr_bind_native_display()` | If the backend needs to get the native display, use this backend function. | Optional  |

The following table lists the TBM backend interface functions for `tbm_bo`.

| Function          | Description                              |                                          |
| ----------------- | ---------------------------------------- | ---------------------------------------- |
| `bo_alloc()`      | Allocates the buffer object.If backend wants to reuse the `bo` private at frontend, return the same pointer of the `bo` private. | Mandatory                                |
| `bo_free()`       | Frees the buffer object.The frontend calls this function when it does not use the `bo` private. | Mandatory                                |
| `bo_import()`     | Imports the buffer object associated with the key.If the backend does not support a buffer sharing by the TBM key, the function pointer must be set to `NULL`. | Optional                                 |
| `bo_export()`     | Exports the buffer object.If the backend does not support a buffer sharing by TBM key, the function pointer must be set to `NULL`. | Optional                                 |
| `bo_import_fd()`  | Imports the buffer object associated with the prime `fd.`The `tbm_fd` must be frees by the user. If the backend does not support a buffer sharing by TBM `fd`, the function pointer must be set to `NULL`. | Mandatory(Must support buffer sharing by TBM `fd`.) |
| `bo_export_fd()`  | Imports the buffer object associated with the prime `fd.`The `tbm_fd` must be freed by the user. If the backend does not support a buffer sharing by TBM `fd`, the function pointer must be set to `NULL`. | Mandatory(Must support buffer sharing by TBM `fd`.) |
| `bo_get_flags()`  | Gets the TBM flags of memory type        | Mandatory                                |
| `bo_size()`       | Gets the size of a buffer object.        | Mandatory                                |
| `bo_get_handle()` | Gets the `tbm_bo_handle` according to the device type. | Mandatory                                |
| `bo_map()`        | Maps the buffer object according to the device type and the option. | Mandatory                                |
| `bo_unmap()`      | Unmaps the buffer object.                | Mandatory                                |
| `bo_lock()`       | Locks the buffer object with a device and an opt. | Optional                                 |
| `bo_unlock()`     | Unlocks the buffer object.               | Optional                                 |

The following table lists the TBM backend interface for `tbm_surface`.

| Function                     | Description                              |           |
| ---------------------------- | ---------------------------------------- | --------- |
| `surface_supported_format()` | Queries the formats list and the number to be supported by backend. | Mandatory |
| `surface_get_plane_data()`   | Gets the plane data, such as the size, ofeset, pitch, and buffer object index of the surface. | Mandatory |
| `surface_bo_alloc()`         | Allocates the buffer object for TBM surface with width, height, format, and buffer object index.If the backend does not want to allocate the buffer of the TBM surface with width, format and height, the function pointer must be set to `NULL`. The TBM frontend allocation buffer of the TBM surface with data is gained from the `surface_get_plane_data()`. | Optional  |

The following table lists the TBM buffer memory types.

| Buffer memory type   | Description                              |
| -------------------- | ---------------------------------------- |
| `TBM_BO_DEFAULT`     | Default memory: it depends on the backend |
| `TBM_BO_SCANOUT`     | Scanout memory                           |
| `TBM_BO_NONCACHABLE` | Non-cachable memory                      |
| `TBM_BO_WC`          | Write-combine memory                     |
| `TBM_BO_VENDOR`      | Vendor specific memory (depends on the backend) |

The following table lists the TBM buffer device types.

| Device type          | Description                              |
| -------------------- | ---------------------------------------- |
| `TBM_DEVICE_DEFAULT` | The device type to get the default handle |
| `TBM_DEVICE_CPU`     | The device type to get the virtual memory |
| `TBM_DEVICE_2D`      | The device type to get the 2D memory handle |
| `TBM_DEVICE_3D`      | The device type to get the 3D memory handle |
| `TBM_DEVICE_MM`      | The device type to get the multimedia handle |

The following table lists the TBM buffer access options.

| Access option       | Description                              |
| ------------------- | ---------------------------------------- |
| `TBM_OPTION_READ`   | The access option to read                |
| `TBM_OPTION_WRITE`  | The access option to write               |
| `TBM_OPTION_VENDOR` | The vendor specific option that depends on the backend |

- TBM DRM helper function

If target uses the `drm` interface, the client needs to get the authenticated `fd` from the display server and the display server must share the `drm` master `fd` with the TDM backend module. The TBM frontend provides the helper functions for `drm`authentication with the wayland protocol and sharing the master `fd` with TDM backend module.

| Function                                 | Description                              |
| ---------------------------------------- | ---------------------------------------- |
| `tbm_drm_helper_wl_auth_server_init()`   | If the TBM backend module need to use the authentication server, the backend module must call this function in the display server. |
| `tbm_drm_helper_wl_auth_server_deinit()` | Deinitailizes the `drm` authentication in display server. |
| `tbm_drm_helper_get_master_fd()`         | If the TDM backend module already has a `drm` master `fd`, the TBM backend module can get the master `fd` from this function. |
| `tbm_drm_helper_set_tbm_master_fd()`     | If the TBM backend module opens the `drm` master `fd`, this function has to be called for sharing the `drm` master `fd` with TDM. |
| `tbm_drm_helper_unset_tbm_master_fd()`   | If the TBM backend module is opened and does not use the `drm` master `fd`, this function has to be called. |
| `tbm_drm_helper_get_auth_info()`         | Client gets the authenticated `fd` and device info from the display server. |

### TBM Backends[[edit](https://wiki.tizen.org/index.php?title=3.0_Porting_Guide/Graphics_and_UI/TBM&action=edit&section=T-2)]

| Backend         | Project ([http://review.tizen.org](http://review.tizen.org/)) | Description                              |
| --------------- | ---------------------------------------- | ---------------------------------------- |
| `libtbm-shm`    | [platform/adaptation/libtbm-shm](https://review.tizen.org/gerrit/gitweb?p=platform/adaptation/libtbm-shm.git;a=summary) | The backend for the target device whitch supports the SHM memory interface.The SHM backend module uses the XSI shared memory segment and does not have hardware dependencies. |
| `libtbm-dumb`   | [platform/adaptation/libtbm-dumb](https://review.tizen.org/gerrit/gitweb?p=platform/adaptation/libtbm-dumb.git;a=summary) | The backend for the target device which supports the DUMB memory interface.If the target kernel supports the `drm` interface, the target can use the `dumb` backend because the DUMB memory interface is the default `drm` memory interface. |
| `libtbm-sprd`   | [platform/adaptation/spreadtrum/libtbm-sprd](https://review.tizen.org/gerrit/gitweb?p=platform/adaptation/spreadtrum/libtbm-sprd.git;a=summary) | The backend for the target device which uses the Spreadtrum chipset only.The `sprd` backend module uses the `drm` gem memory interface but some `ioctl` only provided by the `sprd drm` kernel. |
| `libtbm-exynos` | [platform/adaptation/samsung_exynos/libtbm-exynos](https://review.tizen.org/gerrit/gitweb?p=platform/adaptation/samsung_exynos/libtbm-exynos.git;a=summary) | The backend for the target device which uses the exynos chipset only.The `exynos` backend module uses the `drm` gem memory interface but some `ioctl` only provided by `exynos drm` kernel. |
| `libtbm-vigs`   | [platform/adaptation/emulator/libtbm-vigs](https://review.tizen.org/gerrit/gitweb?p=platform/adaptation/emulator/libtbm-vigs.git;a=summary) | The backend for the target device which supports the VIGS interface.The `vigs` backend is used by the emulator target. |

### Reference[[edit](https://wiki.tizen.org/index.php?title=3.0_Porting_Guide/Graphics_and_UI/TBM&action=edit&section=T-3)]

For more detailed information about the TBM and TBM backend, see [Tizen Buffer Manager (TBM)](https://wiki.tizen.org/TBM).

## Display Management[[edit](https://wiki.tizen.org/index.php?title=3.0_Porting_Guide/Graphics_and_UI&action=edit&section=T-2)]

The display server composites and shows the client's buffers on screen. The display server sometimes needs to convert or scale an image to a different size or format. To make it possible for various chipset devices, the display server needs the display hardware resource information and control them. [Tizen Display Manager (TDM)](https://wiki.tizen.org/TDM) offers these functionalities for the display server with the unified interface for various chipset devices.

[![Tdm-backend.png](https://wiki.tizen.org/images/5/59/Tdm-backend.png)](https://wiki.tizen.org/File:Tdm-backend.png)

With TDM, the display server can do the mode setting, the DPMS control and showing a buffer (framebuffer or video buffer) on the screen in the most efficient way. If the hardware supports the m2m converting and capture device, the display server can also convert an image and dump a screen including all hardware overlays with no compositing.

The vendor has to implement the TDM backend module. The TDM backend module has the responsibility to let the TDM frontend know the display hardware resource information. The display server gets this information and control hardware devices via the TDM frontend APIs. TDM already has several backends for reference, such as `libtdm-drm` and `libtdm-fbdev`.

The TDM backend is implemented as a shared library and the TDM frontend finds the `libtdm-default.so` file and loads it in the `/usr/lib/tdm` directory at runtime.

```
sh-3.2# ls -l /usr/lib/tdm
total 40
lrwxrwxrwx 1 root root    14 Jul 28  2016 libtdm-default.so -> libtdm-drm.so
-rwxr-xr-x 1 root root 37152 Jul 12  2016 libtdm-drm.so

```

The TDM backend module must define the global data symbol with the name `tdm_backend_module_data`. The TDM frontend reads this symbol at the initialization time. TDM calls the `init()` function of the `tdm_backend_module_data`. For more information, see [tdm_backend.h](https://review.tizen.org/gerrit/gitweb?p=platform/core/uifw/libtdm.git;a=tree;h=refs/heads/tizen;hb=refs/heads/tizen).

```
typedef struct _tdm_backend_module {
    const char *name; /* The module name of the backend module */
    const char *vendor; /* The vendor name of the backend module */
    unsigned long abi_version; /* The ABI version of the backend module */
    tdm_backend_data *(*init)(tdm_display *dpy, tdm_error *error);
    void (*deinit)(tdm_backend_data *bdata);
} tdm_backend_module;

```

```
#include <tdm_backend.h>

static tdm_drm_data *drm_data;

tdm_backend_data*
tdm_drm_init(tdm_display *dpy, tdm_error *error)
{
    drm_data = calloc(1, sizeof(tdm_drm_data));

    return (tdm_backend_data*)drm_data;
}

void
tdm_drm_deinit(tdm_backend_data *bdata)
{
    free(bdata);
}

tdm_backend_module tdm_backend_module_data =
{
    "drm",  
    "Samsung",
    TDM_BACKEND_SET_ABI_VERSION(1,1),
    tdm_drm_init,
    tdm_drm_deinit
};

```

The TDM backend must register the `tdm_func_display()`, `tdm_func_output()`, and `tdm_func_layer()` functions with the `tdm_backend_register_func_display()`, `tdm_backend_register_func_output()`, and `tdm_backend_register_func_layer()` functions in the `tdm_backend_module_data` `init()` function.

```
#include <tdm_backend.h>

tdm_backend_data*
tdm_drm_init(tdm_display *dpy, tdm_error *error)
{
    memset(&drm_func_display, 0, sizeof(drm_func_display));
    drm_func_display.display_get_capability = drm_display_get_capability;
    drm_func_display.display_get_pp_capability = drm_display_get_pp_capability;
    drm_func_display.display_get_outputs = drm_display_get_outputs;
    drm_func_display.display_get_fd = drm_display_get_fd;
    drm_func_display.display_handle_events = drm_display_handle_events;
    drm_func_display.display_create_pp = drm_display_create_pp;
    ret = tdm_backend_register_func_display(dpy, &drm_func_display);
    if (ret != TDM_ERROR_NONE)
        goto failed;

    memset(&drm_func_output, 0, sizeof(drm_func_output));
    drm_func_output.output_get_capability = drm_output_get_capability;
    
    ret = tdm_backend_register_func_output(dpy, &drm_func_output);
    if (ret != TDM_ERROR_NONE)
        goto failed;

    memset(&drm_func_layer, 0, sizeof(drm_func_layer));
    drm_func_layer.layer_get_capability = drm_layer_get_capability;

    ret = tdm_backend_register_func_layer(dpy, &drm_func_layer);
    if (ret != TDM_ERROR_NONE)
        goto failed;

    return (tdm_backend_data*)drm_data;
}

```

After loading the TDM backend module, the TDM frontend calls the `display_get_capability()`, `display_get_outputs()`, `output_get_capability()`, `output_get_layers()`, and `layer_get_capability()` functions to get the hardware specific information. That is, the TDM backend module must implement these 5 functions.

In addition, if a target has a memory-to-memory converting hardware device and the capture hardware device, the TDM backend module can register the `tdm_func_pp()` and `tdm_func_capture()` functions with the `tdm_backend_register_func_pp()` and `tdm_backend_register_func_capture()` functions.

### Porting OAL Interface[[edit](https://wiki.tizen.org/index.php?title=3.0_Porting_Guide/Graphics_and_UI/TDM&action=edit&section=T-1)]

TDM provides the header files to implement the TDM backend module.

| Header file                              | Description                              |
| ---------------------------------------- | ---------------------------------------- |
| [tdm_backend.h](https://review.tizen.org/gerrit/gitweb?p=platform/core/uifw/libtdm.git;a=tree;h=refs/heads/tizen;hb=refs/heads/tizen) | This file defines the TDM backend interface. |
| [tdm_log.h](https://review.tizen.org/gerrit/gitweb?p=platform/core/uifw/libtdm.git;a=tree;h=refs/heads/tizen;hb=refs/heads/tizen) | This file to print logs in frontend and backend modules. |
| [tdm_helper.h](https://review.tizen.org/gerrit/gitweb?p=platform/core/uifw/libtdm.git;a=tree;h=refs/heads/tizen;hb=refs/heads/tizen) | This file to help TDM backend/frontend user to implement. |

The display backend interface is mandatory. For more information, see [tdm_backend.h](https://review.tizen.org/gerrit/gitweb?p=platform/core/uifw/libtdm.git;a=tree;h=refs/heads/tizen;hb=refs/heads/tizen).

| Function                           | Description                              |           |
| ---------------------------------- | ---------------------------------------- | --------- |
| `display_get_capability()`         | Gets the display capabilities of the backend module.TDM calls this function not only at the initialization, but also at the update time when new output is connected. If the hardware has the restriction of the number of max usable layer count, the backend module can set the max count to `max_layer_count` of the `tdm_caps_display` structure. Otherwise, set -1. | Mandatory |
| `display_get_pp_capability()`      | Gets the `pp` capabilities of the backend module.TDM calls this function not only at the initialization, but also at the update time when new output is connected. The backend module does not need to implement this function if the hardware does not have the memory-to-memory converting device. Otherwise, the backend module must fill the `tdm_caps_pp` data. The `tdm_caps_pp` contains the hardware restriction information which a converting device can handle, such as format and size. | Optional  |
| `display_get_capture_capability()` | Gets the capture capabilities of the backend module.TDM calls this function not only at the initialization, but also at the update time when new output is connected. The backend module does not need to implement this function if the hardware does not have the capture device. Otherwise, the backend module must fill the `tdm_caps_capture` data. The `tdm_caps_capture` contains the hardware restriction information which a capture device can handle, such as format and size. | Optional  |
| `display_get_outputs()`            | Gets an output array of the backend module.TDM calls this function not only at the initialization, but also at the update time when new output is connected. The backend module must return the newly-allocated array which contains `tdm_output*` data. It is freed in the frontend. | Mandatory |
| `display_get_fd()`                 | Gets the file descriptor of the backend module.The backend module can return the epoll's `fd`. | Optional  |
| `display_handle_events()`          | Handles the events which happens on the `fd` of the backend module. | Optional  |
| `display_create_pp()`              | Creates a `pp` object of the backend module.The backend module does not need to implement this function if the hardware does not have the memory-to-memory converting device | Optional  |

The output backend interface is mandatory. For more information, see [tdm_backend.h](https://review.tizen.org/gerrit/gitweb?p=platform/core/uifw/libtdm.git;a=tree;h=refs/heads/tizen;hb=refs/heads/tizen).

| Function                      | Description                              |           |
| ----------------------------- | ---------------------------------------- | --------- |
| `output_get_capability()`     | Gets the capabilities of a output object.TDM calls this function not only at the initialization, but also at the update time when new output is connected. The `tdm_caps_output` contains connection status, modes, available properties, and size restriction information. | Mandatory |
| `output_get_layers()`         | Gets a layer array of a output object.TDM calls this function not only at the initialization, but also at the update time when new output is connected. The backend module must return the newly-allocated array which contains `tdm_layer*` data. It is freed in the frontend. | Mandatory |
| `output_set_property()`       | Sets the property with a given ID.       | Optional  |
| `output_get_property()`       | Gets the property with a given ID.       | Optional  |
| `output_wait_vblank()`        | Waits for `VBLANK`.If this function returns `TDM_ERROR_NONE`, the backend module must call a user `vblank` handler with the user data of this function after interval `vblanks`. | Mandatory |
| `output_set_vblank_handler()` | Sets the user `vblank` handler.          | Mandatory |
| `output_commit()`             | Commits the changes for an output object.When this function is called, the backend module must apply all changes of the given output object to screen as well as the layer changes of this output. If this function returns `TDM_ERROR_NONE`, the backend module must call a user commit handler with the user data of this function after all changes of the given output object are applied. | Mandatory |
| `output_set_commit_handler()` | Sets a user commit handler.              | Mandatory |
| `output_set_dpms()`           | Sets the DPMS of an output object.       | Optional  |
| `output_get_dpms()`           | Gets the DPMS of an output objectn       | Optional  |
| `output_set_mode()`           | Sets one of the available modes of an output object. | Mandatory |
| `output_create_capture()`     | Creates a capture object of an output objectThe backend module does not need to implement this function if the hardware does not have a capture device. | Optional  |
| `output_set_status_handler()` | Sets an output connection status handler.The backend module must call the output status handler when the output connection status has been changed to let the TDM frontend know the change. | Optional  |
| `output_set_dpms_handler()`   | Sets an output DPMS handler.The backend module must call the output DPMS handler when the output DPMS has been changed to let the TDM frontend know the change. | Optional  |

The layer backend interface is mandatory. For more information, see [tdm_backend.h](https://review.tizen.org/gerrit/gitweb?p=platform/core/uifw/libtdm.git;a=tree;h=refs/heads/tizen;hb=refs/heads/tizen).

| Function                   | Description                              |           |
| -------------------------- | ---------------------------------------- | --------- |
| `layer_get_capability()`   | Get the capabilities of a layer object.The backend module must implement this function. TDM calls this function not only at the initialization, but also at the update time when new output is connected. The `tdm_caps_layer` contains available formats/properties, and zpos information. | Mandatory |
| `layer_set_property()`     | Sets the property with a given ID.       | Optional  |
| `layer_get_property()`     | Gets the property with a given ID.       | Optional  |
| `layer_set_info()`         | Sets the geometry information to a layer object.The backend module applies the geometry information when the output object of a layer object is committed. | Mandatory |
| `layer_get_info()`         | Gets the geometry information to a layer object. | Mandatory |
| `layer_set_buffer()`       | Sets a TDM buffer to a layer object.The backend module shows a TDM buffer on the screen when the output object of a layer object is committed. | Mandatory |
| `layer_unset_buffer()`     | Unset a TDM buffer from a layer object.The backend module must remove the current showing buffer from screen. | Mandatory |
| `layer_set_video_pos()`    | Sets the `zpos` for a video layer object.The backend module does not need to implement this function if the backend module does not have video layers. The `zpos` of the video layer is changeable. | Optional  |
| `layer_create_capture()`   | Creates a capture object of a layer object.The backend module does not need to implement this function if the hardware does not have a capture device. | Optional  |
| `layer_get_buffer_flags()` | Gets the buffer flags which the layer can support. | Optional  |

The `pp` backend interface is optional. For more information, see [tdm_backend.h](https://review.tizen.org/gerrit/gitweb?p=platform/core/uifw/libtdm.git;a=tree;h=refs/heads/tizen;hb=refs/heads/tizen).

| Function                | Description                              |
| ----------------------- | ---------------------------------------- |
| `pp_destroy()`          | Destroys a `pp` object.                  |
| `pp_set_info()`         | Sets the geometry information to a `pp` object.The backend module applies the geometry information when committed. |
| `pp_attach()`           | Attaches a source buffer and a destination buffer to a `pp` object.The backend module converts the image of a source buffer to a destination buffer when committed. The size/crop/transform information is set using the `pp_set_info()` function of `tdm_func_pp`. When done, the backend module must return the source/destination buffer using the `tdm_pp_done_handler()` function. |
| `pp_commit()`           | Commits changes for a `pp` object.       |
| `pp_set_done_handler()` | Sets a user done handler to a `pp` object.The backend module must call the `tdm_pp_done_handler()` function when image conversion is done. |

The capture backend interface is optional. For more information, see [tdm_backend.h](https://review.tizen.org/gerrit/gitweb?p=platform/core/uifw/libtdm.git;a=tree;h=refs/heads/tizen;hb=refs/heads/tizen).

| Function                     | Description                              |
| ---------------------------- | ---------------------------------------- |
| `capture_destroy()`          | Destroys a capture object.               |
| `capture_set_info()`         | Sets the geometry information to a capture object.The backend module applies the geometry information when committed. |
| `capture_attach()`           | Attaches a TDM buffer to a capture object.When the `capture_commit()` function is called, the backend module starts to dump a output or a layer to a TDM buffer. The backend module starts to dump an output or a layer to a TDM buffer when committed. The size/crop/transform information is set using the `capture_set_info()` function of the `tdm_func_capture`. When done, the backend module must return the TDM buffer using the `tdm_capture_done_handler()` function. |
| `capture_commit()`           | Commits changes for a capture object.    |
| `capture_set_done_handler()` | Sets a user done handler to a capture object.The backend module must call the `tdm_capture_done_handler()` function when capture operation is done. |

### TDM backends[[edit](https://wiki.tizen.org/index.php?title=3.0_Porting_Guide/Graphics_and_UI/TDM&action=edit&section=T-2)]

There are several backends which can be referred to implement the TDM backend.

| Backend         | Project ([http://review.tizen.org](http://review.tizen.org/)) | Description                              |
| --------------- | ---------------------------------------- | ---------------------------------------- |
| `libtdm-drm`    | [platform/adaptation/libtdm-drm](https://review.tizen.org/gerrit/gitweb?p=platform/adaptation/libtdm-drm.git;a=summary) | The backend for the target device which supports the DRM interface, such as the Tizen SDK emulatorNo PP & Capture capability |
| `libtdm-fbdev`  | [platform/adaptation/libtdm-fbdev](https://review.tizen.org/gerrit/gitweb?p=platform%2Fadaptation%2Flibtdm-fbdev.git;a=summary) | The backend for the target device which supports the FBDEV interfaceNo PP & Capture capability |
| `libtdm-exynos` | [platform/adaptation/samsung_exynos/libtdm-exynos](https://review.tizen.org/gerrit/gitweb?p=platform%2Fadaptation%2Fsamsung_exynos%2Flibtdm-exynos.git;a=summary) | The backend for the target device which uses the `exynos` chipsetUsing the DRM interfaceHas PP & Capture capabilityUsing the exynos-specific DRM interface to support PP |
| `libtdm-sprd`   | [platform/adaptation/spreadtrum/libtdm-sprd](https://review.tizen.org/gerrit/gitweb?p=platform%2Fadaptation%2Fspreadtrum%2Flibtdm-sprd.git;a=summary) | The backend for the target device which uses the Spreadtrum chipsetUsing the sptreadtrum-specific `ioctl`Using the DRM interface to support `vblank`Has PP capability, but no capture capability |

### References[[edit](https://wiki.tizen.org/index.php?title=3.0_Porting_Guide/Graphics_and_UI/TDM&action=edit&section=T-3)]

For detailed information about the TDM and TDM backend, see [Tizen Display Manager (TDM)](https://wiki.tizen.org/TDM).

## Input Management[[edit](https://wiki.tizen.org/index.php?title=3.0_Porting_Guide/Graphics_and_UI&action=edit&section=T-3)]

The input manager supports for a `libinput` based input device back-end. `libinput` is a common input library for wayland compositor. With `libinput`, the input stack is simpler without the Xorg input drivers. Input is not a HAL component from Tizen 3.0.

[![Tizen 3.0 Input.png](https://wiki.tizen.org/images/1/11/Tizen_3.0_Input.png)](https://wiki.tizen.org/File:Tizen_3.0_Input.png)

### libinput[[edit](https://wiki.tizen.org/index.php?title=3.0_Porting_Guide/Graphics_and_UI/Input&action=edit&section=T-1)]

The `libinput` library handles input devices for display servers and other applications that need to directly deal with input devices.

- Device detection
- Device handling
- Input device event processing
- Scaling touch coordinates
- Generating pointer events from touchpads
- Pointer acceleration

For more information, see the [libinput wiki](https://freedesktop.org/wiki/Software/libinput/).

### libevdev[[edit](https://wiki.tizen.org/index.php?title=3.0_Porting_Guide/Graphics_and_UI/Input&action=edit&section=T-2)]

The `libevdev` library handles evdev kernel devices. It abstracts the evdev ioctls through type-safe interfaces and provides functions to change the appearance of the device. For more information, see [https://en.wikipedia.org/wiki/Evdev](https://en.wikipedia.org/wiki/Evdev).

### mtdev[[edit](https://wiki.tizen.org/index.php?title=3.0_Porting_Guide/Graphics_and_UI/Input&action=edit&section=T-3)]

The `mtdev` stand-alone library transforms all variants of kernel MT events to the slotted type B protocol. For more information, see [http://www.linuxfromscratch.org/blfs/view/svn/general/mtdev.html](http://www.linuxfromscratch.org/blfs/view/svn/general/mtdev.html).

### libinput backends[[edit](https://wiki.tizen.org/index.php?title=3.0_Porting_Guide/Graphics_and_UI/Input&action=edit&section=T-4)]

`libinput: platform/upstream/libinput`

## OpenGL[[edit](https://wiki.tizen.org/index.php?title=3.0_Porting_Guide/Graphics_and_UI&action=edit&section=T-4)]

This document describes the essential elements of Tizen's platform-level graphics architecture related to OpenGL ES and EGL, and how it is used by the application framework and the display server. The focus is on how graphical data buffers move through the system.

Tizen platform requires the OpenGL ES driver for the acceleration of the Wayland display server and `wayland-egl` client. This platform demands OpenGL ES and EGL driver which is implemented by the Tizen EGL Porting Layer.

### Tizen OpenGL ES and EGL Architecture[[edit](https://wiki.tizen.org/index.php?title=3.0_Porting_Guide/Graphics_and_UI/OpenGL&action=edit&section=T-1)]

The following figure illustrates the Tizen OpenGL ES and EGL architecture.

[![OPENGLES STACK.png](https://wiki.tizen.org/images/thumb/d/d6/OPENGLES_STACK.png/700px-OPENGLES_STACK.png)](https://wiki.tizen.org/File:OPENGLES_STACK.png)

- CoreGL

An injection layer of OpenGL ES that provides the following capabilities:

- Support for driver-independent optimization (FastPath)
- EGL/OpenGL ES debugging
- Performance logging
- Supported versions
  - EGL 1.4
  - OpenGL ES 1.1, 2.0, 3.0, 3.1

CoreGL loads the manufacturer's OpenGL ES driver from the `/usr/lib/driver` directory. CoreGL provides the `libEGL.so`, `libGLESv1_CM.so`, and `libGLESvs.so` driver files in the `/usr/lib` directory.

- GPU Vendor GL / EGL driver

The Tizen platform demands that the GPU vendor implements the GL and EGL driver using `libtpl-egl`. The GPU vendor GL / EGL driver must be installed in the following path:

| Library path      | File                                     |
| ----------------- | ---------------------------------------- |
| `/usr/lib/driver` | `libEGL.so``libGLESv1_CM.so``libGLESv2.so` |

### Tizen Porting Layer (TPL) for EGL[[edit](https://wiki.tizen.org/index.php?title=3.0_Porting_Guide/Graphics_and_UI/OpenGL&action=edit&section=T-2)]

TPL-EGL is an abstraction layer for surface and buffer management on Tizen platform. It is used for implementation of the EGL platform functions.

[![Tpl architecture.png](https://wiki.tizen.org/images/thumb/0/0e/Tpl_architecture.png/700px-Tpl_architecture.png)](https://wiki.tizen.org/File:Tpl_architecture.png)

The background for the Tizen EGL Porting Layer for EGL is in various window system protocols in Tizen. There was a need for separating common layer and backend.

Tizen uses the Tizen Porting Layer for EGL, as the TPL-EGL APIs prevents burdens of the EGL porting on various window system protocols. The GPU GL Driver’s Window System Porting Layer can be implemented by TPL-EGL APIs which are the corresponding window system APIs. The TBM, Wayland, and GBM backends are supported.

### Tizen Porting Layer for EGL Object Model[[edit](https://wiki.tizen.org/index.php?title=3.0_Porting_Guide/Graphics_and_UI/OpenGL&action=edit&section=T-3)]

TPL-EGL provides interfaces based of object driven model. Every TPL-EGL object can be represented as a generic `tpl_object_t`, which is reference-counted and provides common functions. Currently, display and surface types of TPL-EGL objects are provided. Display, like normal display, represents a display system which is usually used for connection to the server. Surface corresponds to a native surface like `wl_surface`. A surface might be configured to use N-buffers, but is usually double-buffered or triple-buffered. Buffer is actually something to render on, usually a set of pixels or a block of memory. For these 2 objects, the Wayland, GBM, TBM backend are defined, and they are corresponding to their own window systems. This means that you do not need to care about the window systems.

#### TPL-EGL Core Object[[edit](https://wiki.tizen.org/index.php?title=3.0_Porting_Guide/Graphics_and_UI/OpenGL&action=edit&section=T-4)]

- TPL-EGL Object

Base class for all TPL-EGL objects

- TPL-EGL Display

Encapsulates the native display object (`Display *, wl_display`) Like a normal display, represents a display system which is usually used for connection to the server, scope for other objects.

- TPL-EGL Surface

Encapsulates the native drawable object (`Window, Pixmap, wl_surface`) The surface corresponds to a native surface, such as `tbm_surface_queue` or `wl_surface`. A surface can be configured to use N-buffers, but they are usually double-buffered or triple-buffered.

#### TPL-EGL Objects and Corresponding EGL Objects[[edit](https://wiki.tizen.org/index.php?title=3.0_Porting_Guide/Graphics_and_UI/OpenGL&action=edit&section=T-5)]

Both TPL-EGL and vendor GLES/EGL driver handles the `tbm_surface` as TPL surface's corresponding buffer. It is represented by the `TBM_Surface` part in the following figure.

[![Relationship TPL EGL Gray.png](https://wiki.tizen.org/images/thumb/e/e6/Relationship_TPL_EGL_Gray.png/700px-Relationship_TPL_EGL_Gray.png)](https://wiki.tizen.org/File:Relationship_TPL_EGL_Gray.png)

The following figure illustrates the GLES drawing API flow.

[![GLES API FLOW GRAY.png](https://wiki.tizen.org/images/thumb/4/41/GLES_API_FLOW_GRAY.png/800px-GLES_API_FLOW_GRAY.png)](https://wiki.tizen.org/File:GLES_API_FLOW_GRAY.png)

#### TPL-EGL Frontend API[[edit](https://wiki.tizen.org/index.php?title=3.0_Porting_Guide/Graphics_and_UI/OpenGL&action=edit&section=T-6)]

##### TPL-EGL Object[[edit](https://wiki.tizen.org/index.php?title=3.0_Porting_Guide/Graphics_and_UI/OpenGL&action=edit&section=T-7)]

This is the base class for all TPL-EGL objects. It provides common functionalities to all TPL-EGL objects.

| Function                     | Description                              |
| ---------------------------- | ---------------------------------------- |
| `tpl_object_reference()`     | Increases the reference count of a TPL-EGL object. All TPL-EGL objects are reference-counted. They have reference count 1 on creatation. When the reference count drops to 0, the object is freed. |
| `tpl_object_unreference()`   | Decreases the reference count and destroys the object if it becomes 0. |
| `tpl_object_get_reference()` | Gets the reference count of the given TPL-EGL object. |
| `tpl_object_get_type()`      | Gets the type of the object (display, surface, or buffer). |
| `tpl_object_set_user_data()` | Sets the user data to a TPL-EGL object. Users want to relate some data with a TPL-EGL object. This function provides registering a pointer to such data which can be retrieved later using the `tpl_object_get_user_data()`function. The key is the pointer value itself as a key. |
| `tpl_object_get_user_data()` | Gets the registered user data of a TPL-EGL object. |

##### TPL-EGL Display[[edit](https://wiki.tizen.org/index.php?title=3.0_Porting_Guide/Graphics_and_UI/OpenGL&action=edit&section=T-8)]

Encapsulates the native display object (`Display *, wl_display`). Any other objects created from TPL-EGL Display inherit its backend type.

| Function                                 | Description                              |
| ---------------------------------------- | ---------------------------------------- |
| `tpl_display_create()`                   | Creates the TPL-EGL display object for the given native display. Creates a TPL-EGL display if there is no existing TPL-EGL display for the given native display. If given `NULL` for `native_dpy`, this function returns the default display. |
| `tpl_display_get()`                      | Gets the TPL-EGL display object for the given native display. If thereis an existing TPL-EGL display for the given native display, it returns the TPL-EGL display. |
| `tpl_display_get_native_handle()`        | Gets the native display handle which the given TPL-EGL display is created for. |
| `tpl_display_query_config()`             | Queries the supported pixel formats for the given TPL-EGL display. You might want to know what pixel formats are available on the given display. This function is used to query such available pixel formats. Give `TPL_DONT_CARE` to parameters for size values if any values are acceptable. |
| `tpl_display_filter_config()`            | Filters the configuration according to a given TPL-EGL display. This function modifies current config specific to the current given TPL-EGL display. |
| `tpl_display_get_native_window_info()`   | Queries information on the given native window. |
| `tpl_display_get_native_pixmap_info()`   | Queries information on the given native pixmap. |
| `tpl_display_get_buffer_from_native_pixmap()` | Gets the native buffer from the given native pixmap. |

##### TPL-EGL Surface[[edit](https://wiki.tizen.org/index.php?title=3.0_Porting_Guide/Graphics_and_UI/OpenGL&action=edit&section=T-9)]

Encapsulates the native drawable object (`Window, Pixmap, wl_surface`). Its main features are retrieving the buffer for a frame and posting the surface to a screen.

| Function                                 | Description                              |
| ---------------------------------------- | ---------------------------------------- |
| `tpl_surface_create()`                   | Creates a TPL-EGL surface for the given native surface. |
| `tpl_surface_get_display()`              | Gets the TPL-EGL display where the given TPL-EGL surface was created from. |
| `tpl_surface_get_native_handle()`        | Gets the native surface handle of the given TPL-EGL surface. |
| `tpl_surface_get_type()`                 | Gets the type of the given TPL surface.  |
| `tpl_surface_get_size()`                 | Gets the current size of the given TPL-EGL surface. Size of a surface can change when a user resizes window or the server resizes it. TPL-EGL updates the size information every time when a buffer is queried using the `tpl_surface_dequeue_buffer()` function. Consider that there can still be mismatch between actual surface size and the cached one. |
| `tpl_surface_validate()`                 | Validates the current frame of the given TPL-EGL surface. Call this function before getting the actual final render target buffer. Calling the `tpl_surface_dequeue_buffer()` function after calling this function can give different output with previous one. Buffer returned after calling this function is guaranteed to be not changing. |
| `tpl_surface_dequeue_buffer()`           | Gets the buffer of the current frame for the given TPL-EGL surface. This function returns buffer of the current frame. Depending on backend, communication with the server can be required. Returned buffers are used for rendering the target to draw the current frame. Returned buffers are valid until the next `tpl_surface_dequeue_buffer()` function call. If the `tpl_surface_validate()` function returns `TPL_FALSE`, the previously returned buffers must no longer be used. This function is called again before drawing, and it returns a valid buffer. |
| `tpl_surface_enqueue_buffer()`           | Posts a given `tbm_surface`. This function request display server to post a frame. This is the function which can enqueue a buffer to the `tbm_surface_queue`. Make sure this function is called exactly once for a frame. Scheduling post calls on a separate thread is recommended. |
| `tpl_surface_enqueue_buffer_with_damage()` | Posts a given `tbm_surface` with region of damage. Damage information is used for reducing number of pixels composited in the compositor. Setting the `num_rects` to 0 or `rects` to `NULL` means entire area is damaged. This function request displays server to post a frame. This function is identical with the `tpl_surface_enqueue_buffer()` function except for delivering the damage information for updating. Make sure this function is called exactly once for a frame. Scheduling post calls on a separate thread is recommended. |
| `tpl_surface_set_post_interval()`        | The frame interval ensures that only a single frame is posted within the specified vsync intervals. When a frame ends, the frame interval is set to the surface's current interval. |
| `tpl_surface_get_post_interval()`        | Get frame interval of the given TPL-EGL surface. |

The following code snippet shows a simple example of the Tizen Porting Layer.

```
dpy = tpl_display_create(...);
sfc = tpl_surface_create(dpy, ...);

while (1)
{
    buf = tpl_surface_dequeue_buffer(sfc);

    /* Draw something */

    tpl_surface_enqueue_buffer(sfc, buf);
}

```

In the GPU vendor driver, the "Draw something" part is what the GPU frame builder does. TPL-EGL exposes the native platform buffer identifiers and managers so that the buffer can be used in other modules. Currently, `dma_buf/DRM` is supported for these of purposes. EGL porting layer calls TPL-EGL functions to do what it is requested, and gives the result to the GPU vendor driver. TPL-EGL does all the protocol dependent actions. Such protocol dependent part can be well-separated into TPL-EGL backends. Also, TPL-EGL backend can be configured at runtime. You can specify which type of backend to use when initializing a display object.

#### TPL-EGL and Wayland Server and Client[[edit](https://wiki.tizen.org/index.php?title=3.0_Porting_Guide/Graphics_and_UI/OpenGL&action=edit&section=T-10)]

[![Libtpl-egl-module diagram.png](https://wiki.tizen.org/images/thumb/c/c2/Libtpl-egl-module_diagram.png/700px-Libtpl-egl-module_diagram.png)](https://wiki.tizen.org/File:Libtpl-egl-module_diagram.png)

Tizen uses the `wl_tbm` protocol instead of `wl_drm`. The `wl_tbm` protocol is born for sharing the buffer(`tbm_surface`) between the `wayland_client` and `wayland_server`. Although the `wayland_tbm_server_init` and `wayland_tbm_client_init` pair is a role for the `eglBindWaylandDisplayWL`, the EGL driver is required to implement the entrypoints for the `eglBindWaylandDisplayWL` and `eglUnbindWaylandDisplayWL` as dummy. For more information, see [https://cgit.freedesktop.org/mesa/mesa/tree/docs/specs/WL_bind_wayland_display.spec](https://cgit.freedesktop.org/mesa/mesa/tree/docs/specs/WL_bind_wayland_display.spec).

#### Buffer Flow Between the Wayland Server and GLES/EGL Driver[[edit](https://wiki.tizen.org/index.php?title=3.0_Porting_Guide/Graphics_and_UI/OpenGL&action=edit&section=T-11)]

The following figure shows the buffer flow between wayland server and GLES/EGL Driver. And passed buffer's type is `tbm_surface`.

[![Libtpl-egl buffer flow.png](https://wiki.tizen.org/images/thumb/c/c9/Libtpl-egl_buffer_flow.png/800px-Libtpl-egl_buffer_flow.png)](https://wiki.tizen.org/File:Libtpl-egl_buffer_flow.png)

### Project Git Repository[[edit](https://wiki.tizen.org/index.php?title=3.0_Porting_Guide/Graphics_and_UI/OpenGL&action=edit&section=T-12)]

| Project         | Repository                               | Description                              |
| --------------- | ---------------------------------------- | ---------------------------------------- |
| `libtpl-egl`    | `platform/core/uifw/libtpl-egl`          | Tizen Porting Layer for EGL              |
| `libtbm`        | `platform/core/uifw/libtbm`              | The library for the Tizen Buffer Manager |
| `coregl`        | `platform/core/uifw/coregl`              | An injection layer of OpenGL ES / EGL    |
| `wayland-tbm`   | `platform/core/uifw/wayland-tbm`         | Wayland tbm is a protocol for graphics memory management for Tizen |
| `emulator-yagl` | `platform/adaptation/emulator/emulator-yagl` | OpenGL ES / EGL driver for the emulator  |
| `tpl-novice`    | `platform/core/uifw/ws-testcase`         | Novice test framework for TPL            |

### libtpl-egl Reference Driver[[edit](https://wiki.tizen.org/index.php?title=3.0_Porting_Guide/Graphics_and_UI/OpenGL&action=edit&section=T-13)]

The Emulator YAGL (OpenGLES / EGL driver for the emulator) is implemented by `libtpl-egl`.

The following commit explains how to port the driver with `libtpl-egl` from the traditional drm-based driver.

- Porting YAGL to the Tizen platform [https://review.tizen.org/gerrit/#/c/67921/](https://review.tizen.org/gerrit/#/c/67921/)

### Test and Verify the OpenGL ES Driver[[edit](https://wiki.tizen.org/index.php?title=3.0_Porting_Guide/Graphics_and_UI/OpenGL&action=edit&section=T-14)]

The Khronos OpenGL ES CTS supports the `wayland-egl`. `libtpl-egl` has a test case for the `libtpl-egl`. The `ws-testcase`'s `tpl-novice` has sample code for the `libtpl-egl`.

# Multimedia[[edit](https://wiki.tizen.org/index.php?title=Tizen_3.0_Porting_Guide&action=edit&section=10)]

## Camera[[edit](https://wiki.tizen.org/index.php?title=Porting_Guide/Multimedia&action=edit&section=T-1)]

The Multimedia camcorder framework controls the GStreamer camera plugin to capture camera data from the device. The kernel interfaces to control the camera device can be different for different chipsets, so the camera HAL (Hardware Abstraction Layer) used by camera plugin is provided and it must be implemented specifically for each chipset. Each configuration file contains its own specific hardware dependent information. The Multimedia Camcorder framework reads and parses the information in these configuration files.

[![Tizen3.0 MMFWCamcorder.png](https://wiki.tizen.org/images/thumb/1/1f/Tizen3.0_MMFWCamcorder.png/600px-Tizen3.0_MMFWCamcorder.png)](https://wiki.tizen.org/File:Tizen3.0_MMFWCamcorder.png)

- Camera Source Plugin for GStreamer

Gets camera data (preview or captured image) and sets various camera commands through camera HAL interface

- Camera HAL

Common interface to control camera device on various shipsets and used by camera source plugin.

- Configuration Files

There are 3 config files for the Multimedia Camcorder framework. They are provided by `mmfw- sysconf-xxx`.

- `mmfw_camcorder.ini`




- `mmfw_camcorder_dev_video_pri.ini`




- `mmfw_camcorder_dev_video_sec.ini`



### Porting OAL Interface[[edit](https://wiki.tizen.org/index.php?title=Porting_Guide/Multimedia&action=edit&section=T-2)]

#### GStreamer Camera Plugin[[edit](https://wiki.tizen.org/index.php?title=Porting_Guide/Multimedia&action=edit&section=T-3)]

The default reference camera source plugin which uses the camera HAL interface is provided.

#### Camera HAL[[edit](https://wiki.tizen.org/index.php?title=Porting_Guide/Multimedia&action=edit&section=T-4)]

The `mm-hal-interface` package provides the header file of the camera HAL.

- Repository path: `platform/core/multimedia/mm-hal-interface`
- File name: `tizen-camera.h`

##### Major Functions[[edit](https://wiki.tizen.org/index.php?title=Porting_Guide/Multimedia&action=edit&section=T-5)]

The following table lists the functions related to initialization and deinitialization.

| Prototype                                | Description                          |
| ---------------------------------------- | ------------------------------------ |
| `int camera_init(void **camera_handle)`  | Initializes new camera HAL handle.   |
| `int camera_deinit(void *camera_handle)` | Deinitializes the camera HAL handle. |

The following table lists the functions related to open and close camera device.

| Prototype                                | Description               |
| ---------------------------------------- | ------------------------- |
| `int camera_open_device(void *camera_handle, int device_index)` | Opens the camera device.  |
| `int camera_close_device(void *camera_handle)` | Closes the camera device. |

The following table lists the functions related to getting device information.

| Prototype                                | Description                              |
| ---------------------------------------- | ---------------------------------------- |
| `int camera_get_device_list(void *camera_handle, camera_device_list_t *device_list)` | Gets the camera device list.             |
| `int camera_add_message_callback(void *camera_handle, camera_message_cb callback, void *user_data, uint32_t *cb_id)` | Registers a callback function to be called to send a message by the camera HAL. |
| `int camera_remove_message_callback(void *camera_handle, uint32_t cb_id)` | Unregisters a callback function.         |

The following table lists the functions related to preview and capture.

| Prototype                                | Description                              |
| ---------------------------------------- | ---------------------------------------- |
| `int camera_set_preview_stream_format(void *camera_handle, camera_format_t *format)` | Sets the format of the preview stream.`typedef struct camera_format {    camera_pixel_format_t stream_format;    camera_resolution_t stream_resolution;    uint32_t stream_fps;    camera_rotation_t stream_rotation;    camera_pixel_format_t capture_format;    camera_resolution_t capture_resolution;    uint32_t capture_quality;} camera_format_t;` |
| `int camera_get_preview_stream_format(void *camera_handle, camera_format_t *format)` | Gets the format of the preview stream.   |
| `int camera_start_preview(void *camera_handle, camera_preview_frame_cb callback, void *user_data)` | Starts the preview frames on the screen.`typedef int (*camera_preview_frame_cb)(camera_buffer_t *buffer, camera_metadata_t *meta, void *user_data);` |
| `int camera_stop_preview(void *camera_handle)` | Stops the preview frames.                |
| `int camera_release_preview_buffer(void *camera_handle, int buffer_index)` | Releases the preview buffer. The preview buffer must be released with this function after using it. |
| `int camera_start_auto_focus(void *camera_handle)` | Starts the camera auto focusing operation. |
| `int camera_stop_auto_focus(void *camera_handle)` | Stops the camera auto focusing operation. |
| `int camera_start_capture(void *camera_handle, camera_capture_cb callback, void *user_data)` | Starts capturing still images.`typedef int (*camera_capture_cb)(camera_buffer_t *main, camera_buffer_t *postview, camera_buffer_t *thumbnail, void *user_data);` |
| `int camera_stop_capture(void *camera_handle)` | Stops capturing still images.            |

The following table lists the functions related to video recording.

| Prototype                                | Description                              |
| ---------------------------------------- | ---------------------------------------- |
| `int camera_set_video_stream_format(void *camera_handle, camera_format_t *format)` | Sets the format of the video stream for recording. |
| `int camera_get_video_stream_format(void *camera_handle, camera_format_t *format)` | Gets the format of the video stream for recording. |
| `int camera_start_record(void *camera_handle, camera_video_frame_cb callback, void *user_data)` | Starts the video frame for recording.`typedef int (*camera_video_frame_cb)(camera_buffer_t *buffer, camera_metadata_t *meta, void *user_data);` |
| `int camera_stop_record(void *camera_handle)` | Stops the video frame.                   |
| `int camera_release_video_buffer(void *camera_handle, int buffer_index)` | Releases the video buffer. The video buffer must be released with this function after using it. |

The following table list the functions related to controlling the camera device.

| Prototype                                | Description                              |
| ---------------------------------------- | ---------------------------------------- |
| `int camera_set_command(void *camera_handle, int64_t command, void *value)` | Sets various commands and values to control the camera device.`#define CAMERA_COMMAND_BASE                     ((int64_t)1)#define CAMERA_COMMAND_WHITE_BALANCE            ((int64_t)(CAMERA_COMMAND_BASE << 1))#define CAMERA_COMMAND_ISO                      ((int64_t)(CAMERA_COMMAND_BASE << 2))#define CAMERA_COMMAND_CONTRAST                 ((int64_t)(CAMERA_COMMAND_BASE << 3))#define CAMERA_COMMAND_SATURATION               ((int64_t)(CAMERA_COMMAND_BASE << 4))#define CAMERA_COMMAND_HUE                      ((int64_t)(CAMERA_COMMAND_BASE << 5))#define CAMERA_COMMAND_SHARPNESS                ((int64_t)(CAMERA_COMMAND_BASE << 6))#define CAMERA_COMMAND_EFFECT                   ((int64_t)(CAMERA_COMMAND_BASE << 7))#define CAMERA_COMMAND_SCENE_MODE               ((int64_t)(CAMERA_COMMAND_BASE << 8))#define CAMERA_COMMAND_EXPOSURE_MODE            ((int64_t)(CAMERA_COMMAND_BASE << 9))#define CAMERA_COMMAND_EXPOSURE                 ((int64_t)(CAMERA_COMMAND_BASE << 10))#define CAMERA_COMMAND_ROTATION                 ((int64_t)(CAMERA_COMMAND_BASE << 11))#define CAMERA_COMMAND_FLIP                     ((int64_t)(CAMERA_COMMAND_BASE << 12))#define CAMERA_COMMAND_FOCUS_MODE               ((int64_t)(CAMERA_COMMAND_BASE << 13))#define CAMERA_COMMAND_FOCUS_RANGE              ((int64_t)(CAMERA_COMMAND_BASE << 14))#define CAMERA_COMMAND_SHOT_MODE                ((int64_t)(CAMERA_COMMAND_BASE << 15))#define CAMERA_COMMAND_ANTI_SHAKE               ((int64_t)(CAMERA_COMMAND_BASE << 16))#define CAMERA_COMMAND_FOCUS_AREA               ((int64_t)(CAMERA_COMMAND_BASE << 17))#define CAMERA_COMMAND_DIGITAL_ZOOM             ((int64_t)(CAMERA_COMMAND_BASE << 18))#define CAMERA_COMMAND_OPTICAL_ZOOM             ((int64_t)(CAMERA_COMMAND_BASE << 19))#define CAMERA_COMMAND_RECORDING_HINT           ((int64_t)(CAMERA_COMMAND_BASE << 20))#define CAMERA_COMMAND_WDR                      ((int64_t)(CAMERA_COMMAND_BASE << 21))#define CAMERA_COMMAND_SHUTTER_SPEED            ((int64_t)(CAMERA_COMMAND_BASE << 22))#define CAMERA_COMMAND_FLASH_MODE               ((int64_t)(CAMERA_COMMAND_BASE << 23))#define CAMERA_COMMAND_FACE_DETECTION           ((int64_t)(CAMERA_COMMAND_BASE << 24))` |
| `int camera_get_command(void *camera_handle, int64_t command, void *value)` | Gets the current value of the command.   |
| `int camera_set_batch_command(void *camera_handle, camera_batch_command_control_t *batch_command, int64_t *error_command)` | Sets a set of commands.`typedef struct camera_batch_command_control {    /* Flag for modified command */    int64_t command_set_flag;    /* Value list */    camera_white_balance_t white_balance;    int iso;    int contrast;    int saturation;    int hue;    int sharpness;    camera_effect_t effect;    camera_scene_mode_t scene_mode;    camera_exposure_mode_t exposure_mode;    int exposure;    camera_rotation_t rotation;    camera_flip_t flip;    camera_focus_mode_t focus_mode;    camera_focus_range_t focus_range;    camera_exposure_mode_t shot_mode;    int anti_shake;    camera_rectangle_t focus_area;    int digital_zoom;    int optical_zoom;    int recording_hint;    int wdr;    camera_flash_mode_t flash_mode;    camera_face_detection_t face_detection;} camera_batch_command_control_t;` |

### Configuration[[edit](https://wiki.tizen.org/index.php?title=Porting_Guide/Multimedia&action=edit&section=T-6)]

Read the keyword and its value from the file. Recognize the categories by using the keyword list of the MSL camcorder, and save the member structure of MSL camcorder. Later, these values are used as attribute values or some other operation. The permission of this file is read-only to make sure the configuration files are read once before creating camcorder. Use a semicolon (“;”) to add comments in the config file.

The following table shows the description of the `mmfw_camcorder.ini` file.

| Category                                 | Entry                                    | Description                              |
| ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| GeneralGeneral setting or information    | `SyncStateChange`                        | The API running type. It must be 1 (`TRUE`). |
| `ModelName`                              | Model name of target                     |                                          |
| Video inputSetting list related to video input | `UseConfCtrl`                            | Sets whether to use the configuration file. It must be 1 (`TRUE`). |
| `ConfCtrlFile0` or `1`                   | The name of the setting file to control the camera device. |                                          |
| `VideosrcElement`                        | The source plugin which obtains the camera input buffer from the device |                                          |
| `UseZeroCopyFormat`                      | Sets whether to use the zero copy format. |                                          |
| `DeviceCount`                            | The number of camera device              |                                          |
| `SupportMediaPacketPreviewCb`            | Sets whether the camera API supports media packet preview callback on the target. |                                          |
| Audio inputSetting list related to audio input | `AudiosrcElement`                        | Audio source plugin, which obtains audio for the camcorder or voice recorder |
| `AudiomodemsrcElement`                   | Audio source plugin which obtains audio for call recording |                                          |
| Video inputSetting list related to video output | `DisplayDevice`                          | Supported output device list and the default value |
| `Videosink`                              | Supported output surface list and the default value |                                          |
| `VideosinkElementOverlay`                | Plugin name for the Overlay output surface and the property setting list |                                          |
| `VideosinkElementEvas`                   | Plugin name for the Evas output surface and the property setting list |                                          |
| `VideosinkElementGL`                     | Plugin name for the GL output surface and the property setting list. |                                          |
| `VideosinkElementNULL`                   | Plugin name for the `NULL` surface and the property setting list. |                                          |
| Video encoder                            | Defines the video encoder list for video recording |                                          |
| Audio encoder                            | Defines the audio encoder list for AV recording or voice recording |                                          |
| CaptureSetting list related to image capture | `UseEncodebin`                           | Sets whether to use the `encodebin` to capture the image. It is recommended to keep this value as 0 (`FALSE`). |
| Record                                   | Setting value list for each recording mode. It is recommend to keep the values of the example config file. |                                          |
| Mux                                      | The mux plugin list related with the file container. |                                          |

The following table shows the description of the `mmfw_camcorder_dev_video_pri.ini` file for the primary camera (usually the rear main camera) and the `mmfw_camcorder_dev_video_sec.ini` file for the secondary camera (usually the front camera).

| Category                           | Entry                                    | Description                              |
| ---------------------------------- | ---------------------------------------- | ---------------------------------------- |
| CameraInformation about the camera | `InputIndex`                             | Camera number to select (primary or secondary) |
| `DeviceName`                       | Name of the camera module                |                                          |
| `PreviewResolution`                | A list of all supported preview resolutions the user can set, as well as the default values for this camera device. |                                          |
| `CaptureResolution`                | A list of all supported capture resolutions the user can set, as well as the default values for this camera device. |                                          |
| `VideoResolution`                  | A list of all supported video resolutions the user can set, as well as the default value for this camera device. |                                          |
| `FPS0 ~ 9`                         | A list of all supported FPS (Frame Per Second) by preview resolution settings the user can use, as well as the default values for this camera device. |                                          |
| `PictureFormat`                    | A list of all supported preview formats a user can set, as well as the default values for this camera device. |                                          |
| `RecommendDisplayRotation`         | Default display rotation value for displaying camera input. |                                          |
| `RecommendPreviewFormatCapture`    | Recommended preview format for capturing images. |                                          |
| `RecommendPreviewFormatRecord`     | Recommended preview format for recording. |                                          |
| `RecommendPreviewResolution`       | Recommended preview resolution by ratio of preview resolution. |                                          |
| `FacingDirection`                  | The facing direction of camera device.   |                                          |
| StrobeCamera flash settings        | `StrobeMode`                             | Supported strobe mode and default values. This is converted to a real value and used in the kernel internally. |
| EffectEffect settings              | Brightness                               | Supported range of brightness and default values. |
| Contrast                           | Supported range of contrast and default values. |                                          |
| Saturation                         | Supported range of saturation and default values. |                                          |
| Sharpness                          | Supported range of sharpness and default values. |                                          |
| Whitebalance                       | Supported white balance list and default values. This is converted to real value used in kernel internally. |                                          |
| ColorTone                          | Supported color tone list and default values. This is converted to a real value and used in the kernel internally. |                                          |
| WDR                                | Supported Wide Dynamic Range mode list and default values. This is converted to a real value and used in the kernel internally. |                                          |
| PhotographCamera shooting settings | `DigitalZoom`                            | Supported range of digital zoom level and default values. |
| `OpticalZoom`                      | Supported range of optical zoom level and default values. |                                          |
| `FocusMode`                        | Supported focus mode list and default value. This is converted to a real value and used in the kernel internally. |                                          |
| `AFType`                           | Supported AUTO focus mode list and default values. This is converted to a real value and used in the kernel internally. |                                          |
| `AEType`                           | Supported AUTO Exposure mode list and default value. This is converted to a real value and used in the kernel internally. |                                          |
| `ExposureValue`                    | Supported range of exposure value and default values. |                                          |
| ISO                                | Supported ISO list and default value. This is converted to a real value and used in the kernel internally. |                                          |
| `ProgramMode`                      | Supported program mode (scene mode) list and default value. This is converted to a real value and used in the kernel internally. |                                          |
| `AntiHandshake`                    | Supported anti-hand shake mode list and default value. This is converted to a real value and used in the kernel internally. |                                          |
| CaptureImage capture settings      | `OutputMode`                             | Supported capture format list and default values. |
| `JpegQuality`                      | Supported range of JPEG quality and default values. |                                          |
| `MultishotNumber`                  | Supported range of multi shot count and default values. |                                          |
| `SensorEncodedCapture`             | Whether the camera device supports encoded capture format(EX:JPEG) or not. |                                          |
| `SupportHDR`                       | Supported HDR mode list and default value. |                                          |
| `SupportZSL`                       | Whether the camera device supports zero shutter lag capture or not. |                                          |
| DetectDetect function settings     | `DetectMode`                             | Supported detect mode list and default values. |

### References[[edit](https://wiki.tizen.org/index.php?title=Porting_Guide/Multimedia&action=edit&section=T-7)]

- Driver Configuration

Set the kernel `.config` values for the camera:

```
CONFIG_VIDEO_DEV = y
CONFIG_VIDEO_SAMSUNG = y
CONFIG_VIDEO_SAMSUNG_V4L2 = y
CONFIG_VIDEO_FIMC = y
CONFIG_VIDEO_FIMC_MMAP_OUTPUT_CACHE = y
CONFIG_VIDEO_FIMC_MIPI = y
CONFIG_VIDEO_FIMG2D = y
CONFIG_VIDEO_JPEG = y
CONFIG_VIDEO_MFC5X = y

```

- Kernel Node

```
For Camera: /dev/video1       
Other CAMIF interfaces: /dev/video(0-3)

```

- GStreamer

For more information about GStreamer, see [http://gstreamer.freedesktop.org/documentation/](http://gstreamer.freedesktop.org/documentation/) and [http://gstreamer.freedesktop.org/data/doc/gstreamer/head/pwg/html/index.html](http://gstreamer.freedesktop.org/data/doc/gstreamer/head/pwg/html/index.html).

- V4L2

For more information about V4L2, see [http://v4l2spec.bytesex.org/spec-single/v4l2.html](http://v4l2spec.bytesex.org/spec-single/v4l2.html).

## Radio[[edit](https://wiki.tizen.org/index.php?title=Porting_Guide/Multimedia&action=edit&section=T-8)]

The radio interface part of the multimedia framework supports APIs to implement the following FM radio features.

- Tune a frequency
- Get and set a frequency
- Scan all available frequencies
- Seek up and down
- Get the frequency signal

[![Radio.png](https://wiki.tizen.org/images/thumb/3/31/Radio.png/600px-Radio.png)](https://wiki.tizen.org/File:Radio.png)

The interfaces to control the radio device are different to each other. Therefore, Tizen provides the Radio Hardware Abstraction Layer (HAL) to control various radio devices with a common interface. With the common interface, you can control the radio device on various chipsets used by the `libmm-radio`.

### Porting OAL Interface[[edit](https://wiki.tizen.org/index.php?title=Porting_Guide/Multimedia&action=edit&section=T-9)]

The OAL interface for FM radio is the radio HAL interfaces.

#### Radio HAL[[edit](https://wiki.tizen.org/index.php?title=Porting_Guide/Multimedia&action=edit&section=T-10)]

The `mm-hal-interface` package provides the radio HAL header file.

- Repository path: `platform/core/multimedia/mm-hal-interface`
- File name: `tizen-radio.h`

The OAL interface for FM radio is the [Linux](https://wiki.tizen.org/Linux) kernel V4L2 interface. The radio module directly uses the V4L2 `ioctls` to perform various radio hardware configurations.

The reference section explains the V4L2 interfaces used by the FM radio interface.

#### Major Functions[[edit](https://wiki.tizen.org/index.php?title=Porting_Guide/Multimedia&action=edit&section=T-11)]

The following table lists the functions related to initialization and deinitialization.

| Prototype                                | Description                         |
| ---------------------------------------- | ----------------------------------- |
| `radio_error_t radio_init(void **radio_handle)` | Initializes new radio HAL handle.   |
| `radio_error_t radio_deinit(void *radio_handle)` | Deinitializes the radio HAL handle. |

The following table lists the functions related to preparing and unpreparing the radio device.

| Prototype                                | Description                 |
| ---------------------------------------- | --------------------------- |
| `radio_error_t radio_prepare_device(void *radio_handle)` | Prepare the radio device.   |
| `radio_error_t radio_unprepare_device(void *radio_handle)` | Unprepare the radio device. |

The following table lists the functions related to opening and closing the radio device.

| Prototype                                | Description              |
| ---------------------------------------- | ------------------------ |
| `radio_error_t radio_open_device(void *radio_handle)` | Opens the radio device.  |
| `radio_error_t radio_close_device(void *radio_handle)` | Closes the radio device. |

The following table lists the functions related to starting and stopping the radio device.

| Prototype                                | Description              |
| ---------------------------------------- | ------------------------ |
| `radio_error_t radio_start (void *radio_handle)` | Starts the radio device. |
| `radio_error_t radio_stop (void *radio_handle)` | Stops the radio device.  |

The following table lists the functions related to setting and getting the frequency.

| Prototype                                | Description               |
| ---------------------------------------- | ------------------------- |
| `radio_error_t radio_get_frequency(void *radio_handle, uint32_t *frequency)` | Gets the radio frequency. |
| `radio_error_t radio_set_frequency(void *radio_handle, uint32_t frequency)` | Sets the radio frequency. |

The following table lists the functions related to seeking for channels.

| Prototype                                | Description                              |
| ---------------------------------------- | ---------------------------------------- |
| `radio_error_t radio_seek(void *radio_handle, radio_seek_direction_type_t direction)` | Seeks (up or down) the effective frequency of the radio, asynchronously`typedef enum radio_seek_direction_type    RADIO_SEEK_DIRECTION_UP, /* Seek upward */    RADIO_SEEK_DIRECTION_DOWN /* Seek downward */} radio_seek_direction_type_t;` |

The following table lists the functions related to muting and unmuting the radio device.

| Prototype                                | Description        |
| ---------------------------------------- | ------------------ |
| `radio_error_t radio_mute(void *radio_handle)` | Mutes the radio.   |
| `radio_error_t radio_unmute(void *radio_handle)` | Unmutes the radio. |

The following table lists the functions related to setting and getting the volume.

| Prototype                                | Description                              |
| ---------------------------------------- | ---------------------------------------- |
| `radio_error_t radio_get_volume(void *radio_handle, float *volume)` | Gets the radio's current volume.         |
| `radio_error_t radio_set_volume(void *radio_handle, float volume)` | Sets the current radio's volume.         |
| `radio_error_t radio_set_media_volume(void *radio_handle, uint32_t level)` | Sets the current media volume level(system media volume). |

The following table lists the functions related to getting the signal strength.

| Prototype                                | Description                              |
| ---------------------------------------- | ---------------------------------------- |
| `radio_error_t radio_set_media_volume(void *radio_handle, uint32_t level);` | Gets the current signal strength of the radio. |

### References[[edit](https://wiki.tizen.org/index.php?title=Porting_Guide/Multimedia&action=edit&section=T-12)]

- Kernel Node

```
For Radio: /dev/radio0       

```

## Audio[[edit](https://wiki.tizen.org/index.php?title=Porting_Guide/Multimedia&action=edit&section=T-13)]

The following figure illustrates the different audio layers.

[![Audio.png](https://wiki.tizen.org/images/thumb/7/72/Audio.png/600px-Audio.png)](https://wiki.tizen.org/File:Audio.png)

- PulseAudio
  - PulseAudio is a sound server accepting sound input from 1 or more sources and redirecting it to 1 or more sinks. PulseAudio has the following features:
    - Software mixing of multiple audio streams
    - Support for multiple audio sources and sinks
    - An extensible plugin architecture with support for loadable modules
    - Low-latency operation
    - Support external devices such as Bluetooth audio and USB audio devices.
  - Pulseaudio interacts with AudioHAL interfaces to support various type of devices.
- Audio HAL
  - Predefined interfaces for Audio Hardware Abstraction Layer (HAL)
  - Interface includes the following categories: volume, route, stream, pcm
- Configuration Files
  - Configurations for running Pulseaudio and Audio Systems which can be modified without code changes.
    - pulseaudio configurations (daemon.conf, client.conf, system.pa, etc.)
    - stream / device configuration (stream-map.json, device-map.json)

### Porting OAL Interface[[edit](https://wiki.tizen.org/index.php?title=Porting_Guide/Multimedia&action=edit&section=T-14)]

The following table lists the audio HAL interfaces.

| Interface                                | Description                              |
| ---------------------------------------- | ---------------------------------------- |
| `audio_return_t audio_init(void **audio_handle)` | Initializes the audio HAL handle.        |
| `audio_return_t audio_deinit(void *audio_handle)` | De-initializes the audio HAL handle.     |
| `audio_return_t audio_get_volume_level_max(void *audio_handle, audio_volume_info_t *info, uint32_t *level)` | Gets the maximum volume level supported for a particular volume information. |
| `audio_return_t audio_get_volume_level(void *audio_handle, audio_volume_info_t *info, uint32_t *level)` | Gets the volume level specified for a particular volume information. |
| `audio_return_t audio_set_volume_level(void *audio_handle, audio_volume_info_t *info, uint32_t level)` | Sets the volume level specified for a particular volume information. |
| `audio_return_t audio_get_volume_value(void *audio_handle, audio_volume_info_t *info, uint32_t level, double *value)` | Gets the volume value specified for a particular volume information and level. |
| `audio_return_t audio_get_volume_mute(void *audio_handle, audio_volume_info_t *info, uint32_t *mute)` | Gets the volume mute specified for a particular volume information. |
| `audio_return_t audio_set_volume_mute(void *audio_handle, audio_volume_info_t *info, uint32_t mute)` | Sets the volume mute specified for a particular volume information. |
| `audio_return_t audio_update_route(void *audio_handle, audio_route_info_t *info)` | Updates the audio routing according to audio route information. |
| `audio_return_t audio_update_route_option(void *audio_handle, audio_route_option_t *option)` | Updates audio routing option according to audio route option. |
| `audio_return_t audio_notify_stream_connection_changed(void *audio_handle, audio_stream_info_t *info, uint32_t is_connected)` | Notifies when a stream is connected and disconnected. |
| `audio_return_t audio_pcm_open(void *audio_handle, void **pcm_handle, uint32_t direction, void *sample_spec, uint32_t period_size, uint32_t periods)` | Opens a PCM device.                      |
| `audio_return_t audio_pcm_start(void *audio_handle, void *pcm_handle)` | Starts a PCM device.                     |
| `audio_return_t audio_pcm_stop(void *audio_handle, void *pcm_handle)` | Stops a PCM device.                      |
| `audio_return_t audio_pcm_close(void *audio_handle, void *pcm_handle)` | Closes a PCM device.                     |
| `audio_return_t audio_pcm_avail(void *audio_handle, void *pcm_handle, uint32_t *avail)` | Gets available number of frames.         |
| `audio_return_t audio_pcm_write(void *audio_handle, void *pcm_handle, const void *buffer, uint32_t frames)` | Writes frames to a PCM device.           |
| `audio_return_t audio_pcm_read(void *audio_handle, void *pcm_handle, void *buffer, uint32_t frames)` | Reads frames from a PCM device.          |
| `audio_return_t audio_pcm_get_fd(void *audio_handle, void *pcm_handle, int *fd)` | Gets poll descriptor for a PCM handle.   |
| `audio_return_t audio_pcm_recover(void *audio_handle, void *pcm_handle, int revents)` | Recovers the PCM state.                  |
| `audio_return_t audio_pcm_get_params(void *audio_handle, void *pcm_handle, uint32_t direction, void **sample_spec, uint32_t *period_size, uint32_t *periods)` | Gets parameters of a PCM device.         |
| `audio_return_t audio_pcm_set_params(void *audio_handle, void *pcm_handle, uint32_t direction, void *sample_spec, uint32_t period_size, uint32_t periods)` | Sets hardware and software parameters of a PCM device. |

### Configuration[[edit](https://wiki.tizen.org/index.php?title=Porting_Guide/Multimedia&action=edit&section=T-15)]

To support a variety of devices, PulseAudio and device configuration have to be modified by the vendor. The following table shows the PulseAudio configuration.

| Configurations           | Description                              |
| ------------------------ | ---------------------------------------- |
| `/etc/pulse/daemon.conf` | Configuration file for the PulseAudio daemon.In this file, the PulseAudio daemon properties such as priority, log-level, resampling method, and default sample rate can be modified.In Tizen, PulseAudio daemon must be running as only system mode not user mode. |
| `/etc/pulse/client.conf` | Configuration file for the PulseAudio clients.Not much needed for modification in general use case. |
| `/etc/pulse/system.pa`   | PulseAudio Sound Server startup script.This startup script is used only if PulseAudio is started in system mode.Initial module loading is triggered by this file, so if there are some vendor specific modules to be loaded, they must be added here. |
| `/etc/pulse/default.pa`  | PulseAudio Sound Server Startup Script.This startup script is used only if PulseAudio is started per user.Currently Tizen does not support this mode. |

- Stream/device configuration
  - Stream map: Latency, volume and streams can be configured in this file.
  - Device map: Device types and device files can be configured in this file.

The following table shows examples of the the device configuration.

| Configurations               | Example                                  |
| ---------------------------- | ---------------------------------------- |
| `/etc/pulse/stream-map.json` | `{    "latencies":[        {            "type":"low",            "fragsize-ms":25,            "minreq-ms":-1,            "tlength-ms":100,            "prebuf-ms":0,            "maxlength":-1,        },            {            "type":"high",            "fragsize-ms":75,            "minreq-ms":-1,            "tlength-ms":400,            "prebuf-ms":0,            "maxlength":-1,        },    ],    "volumes":[        {            "type":"media",            "is-hal-volume":1,        },        {            "type":"system",            "is-hal-volume":0,        },        {            "type":"notification",            "is-hal-volume":0,        },        {            "type":"ringtone",            "is-hal-volume":0,        },        {            "type":"call",            "is-hal-volume":1,        },        ],    "streams":[        {            "role":"media",            "priority":3,            "route-type":"auto",            "volume-types":{"in":"none","out":"media"},            "avail-in-devices":["audio-jack","builtin-mic"],            "avail-out-devices":["forwarding","audio-jack","bt","builtin-speaker"],            "avail-frameworks":["player","wav-player","tone-player","audio-io","recorder"],        },        {            "role":"system",            "priority":2,            "route-type":"auto",            "volume-types":{"in":"none","out":"system"},            "avail-in-devices":["none"],            "avail-out-devices":["forwarding","audio-jack","bt","builtin-speaker"],            "avail-frameworks":["player","wav-player","tone-player","audio-io"],        },        {            "role":"notification",            "priority":4,            "route-type":"auto-all",            "volume-types":{"in":"none","out":"notification"},            "avail-in-devices":["none"],            "avail-out-devices":["audio-jack","bt","builtin-speaker"],            "avail-frameworks":["player","wav-player","tone-player","audio-io"],        },        {            "role":"ringtone-call",            "priority":6,            "route-type":"auto-all",            "volume-types":{"in":"none","out":"ringtone"},            "avail-in-devices":["none"],            "avail-out-devices":["audio-jack","bt","builtin-speaker"],            "avail-frameworks":["player","wav-player","tone-player","audio-io"],        },        {            "role":"call-voice",            "priority":6,            "route-type":"manual",            "volume-types":{"in":"none","out":"call"},            "avail-in-devices":["builtin-mic","audio-jack","bt"],            "avail-out-devices":["builtin-receiver","builtin-speaker","audio-jack","bt"],            "avail-frameworks":["sound-manager"],        },	    ]}` |
| `/etc/pulse/device-map.json` | `{    "device-types":[        {            "device-type":"builtin-speaker",            "builtin":true,            "direction":["out"],            "avail-condition":["pulse"],            "playback-devices":{"normal":"alsa:sprdphone,0", "call-voice":"alsa:VIRTUALAUDIOW,0"}        },        {            "device-type":"builtin-mic",            "builtin":true,            "direction":["in"],            "avail-condition":["pulse"],            "capture-devices":{"normal":"alsa:sprdphone,0"}        },        {            "device-type":"audio-jack",            "builtin":false,            "direction":["both","out"],            "avail-condition":["pulse","dbus"],            "playback-devices":{"normal":"alsa:sprdphone,0", "call-voice":"alsa:VIRTUALAUDIOW,0"},            "capture-devices":{"normal":"alsa:sprdphone,0"}        },        {            "device-type":"bt",            "profile":"a2dp",            "builtin":false,            "direction":["out"],            "avail-condition":["pulse"]        },        {            "device-type":"bt",            "profile":"sco",            "builtin":false,            "direction":["both"],            "avail-condition":["pulse","dbus"],            "playback-devices":{"normal":"alsa:sprdphone,0", "call-voice":"alsa:VIRTUALAUDIOW,0"},            "capture-devices":{"normal":"alsa:sprdphone,0"}        },        {            "device-type":"usb-audio",            "builtin":false,            "direction":["both", "in", "out"],            "avail-condition":["pulse"]        }    ],        "device-files":        {            "playback-devices":[                {                    "device-string":"alsa:sprdphone,0",                    "role":                    {                        "normal":"rate=44100",                    }                },                {                    "device-string":"alsa:VIRTUALAUDIOW,0",                    "role":                    {                        "call-voice":"rate=16000 channels=1 tsched=0 alternate_rate=16000",                    }                }            ],            "capture-devices":[            {                "device-string":"alsa:sprdphone,0",                "role":{"normal":"rate=44100"}            }        ]    }}` |

### References[[edit](https://wiki.tizen.org/index.php?title=Porting_Guide/Multimedia&action=edit&section=T-16)]

- Driver configuration for Samsung chipset



  The following list is an example of the kernel `.config` values to be set for audio in the Samsung chipset.

```
CONFIG_SOUND=y
CONFIG_SND=y
CONFIG_SND_TIMER=y
CONFIG_SND_HWDEP=y
CONFIG_SND_JACK=y
CONFIG_SND_SOC = y
CONFIG_SND_SOC_SAMSUNG = y
CONFIG_SND_SAMSUNG_I2S = y
CONFIG_SND_SOC_SLP_TRATS_MC1N2 = y
CONFIG_SND_SOC_I2C_AND_SPI = y
CONFIG_SND_SOC_MC1N2=y

```

- PulseAudio

  Version: 5.0

  Website: [http://www.freedesktop.org/wiki/Software/PulseAudio](http://www.freedesktop.org/wiki/Software/PulseAudio)


- ALSA

  Website: [http://www.alsa-project.org](http://www.alsa-project.org/)

## Player[[edit](https://wiki.tizen.org/index.php?title=Porting_Guide/Multimedia&action=edit&section=T-17)]

The multimedia player framework controls the player plugins (demuxer, codecs, and renderer plugins) of the GStreamer to play media content. The kernel interfaces to control codecs can be different for different chipsets, so the corresponding codec plugins must be implemented specifically for each chipset.

[![Player.png](https://wiki.tizen.org/images/thumb/0/0c/Player.png/600px-Player.png)](https://wiki.tizen.org/File:Player.png)

### Porting OAL Interface[[edit](https://wiki.tizen.org/index.php?title=Porting_Guide/Multimedia&action=edit&section=T-18)]

[![Playerplugin.png](https://wiki.tizen.org/images/2/28/Playerplugin.png)](https://wiki.tizen.org/File:Playerplugin.png)

There is no specific OAL for the multimedia player framework. As part OAL interface, the player plugins consists of the `gst-omx` codec plugins and video/audio renderer plugins. For details of the `gst-omx` plugin details, see [Porting OAL Interface (Codecs)](https://wiki.tizen.org/Porting_Guide#Porting_OAL_Interface_9). For more information about Avsystem for audio, see [Audio](https://wiki.tizen.org/Porting_Guide/Multimedia#Audio)), and Wayland (UI-framework) for display, see [Video](https://wiki.tizen.org/Porting_Guide/Multimedia#Video).

### Configuration[[edit](https://wiki.tizen.org/index.php?title=Porting_Guide/Multimedia&action=edit&section=T-19)]

- Configuration file
  - The multimedia player framework uses the `mmfw_player.ini` configuration file to set various parameters for selecting different codecs and display plugins.
  - The `mmfw_player.ini` configuration file is provided by the `mmfw-sysconf-xxx` package.
  - In the final stage of development, the permission for this file needs to be changed to read-only.
- Configuring the player
  - File name: `mmfw_player.ini`
  - 1 `player.ini` file is needed in each board (or model).
  - Codec plugins for this board are located in the `/usr/lib/gstreamer-1.0` directory. Changing the codec plugin does not mean modifying this `.ini` file because the player supports the auto plugin feature.
- As needed, the following setting values can be used:
  - Exclude keyword element
  - Audio filter

### References[[edit](https://wiki.tizen.org/index.php?title=Porting_Guide/Multimedia&action=edit&section=T-20)]

- Display Driver Configuration for Samsung chipset


The following list is an example of the kernel `.config` values to be set for display in the Samsung chipset.

```
CONFIG_DRM =  y
CONFIG_FB = y
CONFIG_FB_S3C = y
CONFIG_FB_S3C_LCD_INIT = y
CONFIG_FIMD_EXT_SUPPORT = y
CONFIG_FIMD_LITE_SUPPORT = y

```

- Kernel Node


- Frame buffers: `/dev/fb(0-4)`
- `gst-omx` version : 1.2.0[http://gstreamer.freedesktop.org/src/gst-omx/](http://gstreamer.freedesktop.org/src/gst-omx/)[http://www.freedesktop.org/wiki/GstOpenMAX](http://www.freedesktop.org/wiki/GstOpenMAX)
- For all GStreamer documentation, see [http://gstreamer.freedesktop.org/documentation/](http://gstreamer.freedesktop.org/documentation/).
- For developing GStreamer plugins, see [http://gstreamer.freedesktop.org/data/doc/gstreamer/head/pwg/html/index.html](http://gstreamer.freedesktop.org/data/doc/gstreamer/head/pwg/html/index.html).
- For more information about OpenMAX IL components, see [http://www.khronos.org/openmax/il/](http://www.khronos.org/openmax/il/).

## Codec[[edit](https://wiki.tizen.org/index.php?title=Porting_Guide/Multimedia&action=edit&section=T-21)]

The following figure illustrates the codecs and their relations. It shows 2 types of codec plugins, the Gstreamer and OpenMAX.

[![Codec.png](https://wiki.tizen.org/images/thumb/9/9e/Codec.png/600px-Codec.png)](https://wiki.tizen.org/File:Codec.png)

- Gstreamer codec plugin
  - The Gstreamer codec plugin can be linked and used easily to the Gstreamer pipeline, which is used in the multimedia framework.
- OpenMAX codec plugin
  - Some of the codec vendors provide OpenMAX IL components and not Gstreamer plugins. Tizen provides the `gst-omx` plugins to use the OpenMAX IL components. The Gstreamer pipeline used in the multimedia framework can control and transfer data to OpenMAX IL component using the `gst-omx` plugin.


- Description of each codec component


- Gstreamer codec plugin



  - In addition, to link a Gstreamer pipeline, the capability of the codec plugin can be negotiated with the linked element in the pipeline.
  - To get detailed information, such as the capability of an element, use the `#gst-inspect-1.0 (element name)` command.[![Gst-inspect.png](https://wiki.tizen.org/images/0/07/Gst-inspect.png)](https://wiki.tizen.org/File:Gst-inspect.png)

- OpenMAX component codec plugin



  - To use the OpenMAX component in Gstreamer, the `gst-omx` (open source) package is provided. By using this package, Gstreamer can recognize and use an OpenMAX component as a Gstreamer element. `gst-omx` is a Gstreamer plugin that allows communication with OpenMAX IL components. The usage of the `gst-omx` plugin is the same as other Gstreamer plugins.
  - For more detailed information about this plugin, see [http://www.freedesktop.org/wiki/GstOpenMAX](http://www.freedesktop.org/wiki/GstOpenMAX). For more information about OpenMAX IL, see [http://www.khronos.org/openmax/](http://www.khronos.org/openmax/).
  - The `gst-omx` plugin refers to a `gstomx.conf` configuration file. This file is included in the `gst-omx` package, and installed to the `/etc/xdg/gst-omx.conf` directory in the target device.

### Porting OAL Interface[[edit](https://wiki.tizen.org/index.php?title=Porting_Guide/Multimedia&action=edit&section=T-22)]

**OpenMAX component codec plugin**

An industry standard that provides an abstraction layer for computer graphics, video, and sound routines. The interface abstracts the hardware and software architecture in the system. The OpenMAX IL API allows the user to load, control, connect, and unload the individual components. This flexible core architecture allows the Integration Layer to easily implement almost any media use case and mesh with existing graph-based media frameworks. The key focus of the OpenMAX IL API is portability of media components OpenMAX IL interfaces between media framework, such as GStreamer and a set of multimedia components (such as an audio or video codecs). `gst-omx` is a GStreamer plug-in package that allows communication with OpenMAX IL components. The `gst-omx` structuring is classified into different object classes based on the functionality. The following is the object structuring of a video decoder plugin in `gst-omx`.

[![Gst-omx.png](https://wiki.tizen.org/images/f/fc/Gst-omx.png)](https://wiki.tizen.org/File:Gst-omx.png)

The `GstVideoDecoder` base class is for video decoders provide encoded data to derived `GstOMXVideoDec` and each input frame is provided in turn to the subclass's `handle_frame` callback. The `GstVideoDecoder` base class and derived subclass cooperate in the following way:

1. Configuration
   - `GstVideoDecoder` calls the `start()` function when the decoder element is activated.
   - `GstVideoDecoder` calls the `set_format()` function to inform the subclass of caps describing input video data
2. Data processing
   - Each input frame is provided in turn to the subclass's `handle_frames()` function.
   - The subclass calls the `gst_video_decoder_finish_frame()` or `gst_video_decoder_drop_frame()` function.
3. Shutdown phase
   - The `GstVideoDecoer` class calls the `stop()` function.

### Configuration[[edit](https://wiki.tizen.org/index.php?title=Porting_Guide/Multimedia&action=edit&section=T-23)]

**OpenMAX component codec plugin**

The `gst-omx` plugin refers to a configuration file, such as `gstomx.conf`. This file is included in the `gst-omx` package, and installed in the `/etc/xdg/gstomx.conf` directory on the target device. The `gstomx.conf` file needs to change appropriately, according to vendors which provide OpenMAX component. The following figures lists the values of each item in the lists separated by commas. Each Gstreamer element is separated by a semicolon.

[![Gst-openmax.conf.png](https://wiki.tizen.org/images/4/40/Gst-openmax.conf.png)](https://wiki.tizen.org/File:Gst-openmax.conf.png)

The following figure shows an example.

[![Omx mpeg4dec.png](https://wiki.tizen.org/images/0/06/Omx_mpeg4dec.png)](https://wiki.tizen.org/File:Omx_mpeg4dec.png)

Each value needs to be changed appropriately, according to vendors who provide the OpenMAX component. When you are finished with these settings, the result is a Gstreamer type codec plugin, and you can test the codec the same way.

- Using the codec plugin in the player
  - Because the player uses auto plugging, it does not need an additional setting.
    - If the decoder plugin has an acceptable capability, this plugin can be linked with a player pipeline in order of rank.
    - If the codec name is included in the excluded keyword in the `/usr/etc/mmfw_player.ini` file (`mmfw-sysconf` package), it is excluded in the player pipeline.
- Using the codec plugin in the camcorder
  - Because the camcorder clarified its audio, video, and image encoder in the `/usr/etc/mmfw_camcorder.ini` file (`mmfw-sysconf` package), you need to change this category value to set your own codec name.

[![Videoencoder.png](https://wiki.tizen.org/images/7/7a/Videoencoder.png)](https://wiki.tizen.org/File:Videoencoder.png)

### References[[edit](https://wiki.tizen.org/index.php?title=Porting_Guide/Multimedia&action=edit&section=T-24)]

- `gst-omx` version: 1.2[http://gstreamer.freedesktop.org/src/gst-omx/](http://gstreamer.freedesktop.org/src/gst-omx/)[http://www.freedesktop.org/wiki/GstOpenMAX](http://www.freedesktop.org/wiki/GstOpenMAX)
- For all GStreamer documentation, see [http://gstreamer.freedesktop.org/documentation/](http://gstreamer.freedesktop.org/documentation/).
- For developing GStreamer plug-ins, see [http://gstreamer.freedesktop.org/data/doc/gstreamer/head/pwg/html/index.html](http://gstreamer.freedesktop.org/data/doc/gstreamer/head/pwg/html/index.html).
- For more information about OpenMAX IL components, see [http://www.khronos.org/openmax/il/](http://www.khronos.org/openmax/il/).

# Connectivity[[edit](https://wiki.tizen.org/index.php?title=Tizen_3.0_Porting_Guide&action=edit&section=11)]

## Bluetooth[[edit](https://wiki.tizen.org/index.php?title=Porting_Guide/Connectivity&action=edit&section=T-1)]

Bluetooth is the short range communication used to communicate between 2 devices. In Tizen, open source Bluetooth components like BlueZ and ObexD are used. Bluez and Obexd run as the daemon and there is an interface library Bluetooth Framework, used for applications to access BlueZ or ObexD over the D-Bus interface.

This section explains the Bluetooth architecture on the Tizen platform and how Tizen can be ported, along with the configuration parameters and its values.

Bluetooth Low Energy function was implemented in BlueZ and `bluetooth-frwk`.

The following figure explains the Bluetooth architecture on Tizen.

[![Bluetooth.png](https://wiki.tizen.org/images/thumb/a/a9/Bluetooth.png/600px-Bluetooth.png)](https://wiki.tizen.org/File:Bluetooth.png)

The Bluetooth framework provides dialogue for the user. It controls the BlueZ, ObexD, and PulseAudio daemons. Bluetooth provides a standard interface between the Bluetooth chip and AP, called the HCI (Host Controller Interface). HCI can be implemented on USB, UART, SDIO, but for the mobile environment, UART is used most. Depending on the chip vendor, HCI Interface Activation can be different. The vendor provides the HCI configuration and the initial scripts. For example, Broadcom and Spreadtrum provide firmware and a loading tool. Tizen supports Bluetooth version 4.2. The supported profiles are GATT, FTP, OPP, MAP, PBAP, A2DP, AVRCP, HSP/HFP, RFCOMM, HID, HDP, and PAN. Bluetooth framework Tizen Bluetooth is based on the open source BlueZ project. BlueZ provides the DBUS API and based on it, Tizen BT framework provides the C Language API. It is recommended to use the Tizen Bluetooth framework.

The following components are necessary for Bluetooth:

- Application
  - The user dialogue that controls the BlueZ, ObexD, and PulseAudio daemons
- ObexD
  - The open source component
  - Object exchange daemon
  - Supports OPP, FTP, PBAP, SYNC, and MAP profile stack
- BluetoothD
  - BluetoothD is the open souce component, Bluez 5.37 is supported
  - Bluetooth central daemon
  - Supports GAP, SDP, A2DP, AVRCP, HFP, HSP, and GATT profile stack
- Bluetooth Subsystem
  - Provides the BT unix socket. Each protocol can be accessed by its socket.
  - Supports the L2CAP, RFCOMM, SCO, and HCI protocols
- Bluetooth Driver
  - BT Chip Driver
  - In case of UART, [Linux](https://wiki.tizen.org/Linux) kernel provides the interface.
  - GPIO configuration, `rfkill` (Radio Frequency Management) and power management can be handled by both the vendor and the porting engineer.
- BT Firmware Loading Module
  - Depending on the environment, it loads the Bluetooth firmware to the Bluetooth chip.
  - Tizen and the chipset vendor need to implement this together.
  - Package: `bluetooth-tools`

### Porting OAL Interface[[edit](https://wiki.tizen.org/index.php?title=Porting_Guide/Connectivity&action=edit&section=T-2)]

The following OAL scripts are run during the Bluetooth stack start and end sequences. These scripts invoke the Bluetooth chip specific (such as Broadcom and Spreadtrum) scripts, provided by the chipset vendor to perform chip specific configuration. These scripts are available in the `bluetooth-dev-tools.under` package. When this package is installed, it copies the scripts in the `/usr/etc/Bluetooth/` directory.

- `bt-stack-up.sh`




- `bt-stack-down.sh`




- `bt-reset-env.sh`




- Tizen BT Obex profiles

In Tizen, for the `obex` based profiles, the open source ObexD is used.

- BT Obex profiles server (`obexd`)




- BT Obex profiles client (`obex-client`)



### Configuration[[edit](https://wiki.tizen.org/index.php?title=Porting_Guide/Connectivity&action=edit&section=T-3)]

There are a few configuration changes that need to be made to enable the specific chipset and the scripts and other configuration information, such as UART speed and UART terminal (`tty`), to be opened specific to the chipset. These changes must be provided by the chipset vendors.

- Configuration for the BCM4358 Bluetooth chipset by Broadcomm


- `hciattach`




- The Bluetooth UART used is `/dev/ttySAC3`
- The Broadcom firmware used is `BCM4358A1_001.002.005.0032.0066.hcd`
- The UART speed configuration is 3000000 for BCM4358A1
- The `bcmtool` used is `bcmtool_4358a1`
- The `.bd_addr` contains the unique Bluetooth address, which is generated during the first Bluetooth activation
- Register the Bluetooth device:

```
bcmtool_4358a1 /dev/ttySAC0 –FILE=BCM4358A1_001.002.005.0032.0066.hcd –BAUD=3000000 –ADDR=/csa/bluetooth/.bd_addr –SETSCO=0,0,0,0,0,0,0,3,3,0 –LP
```

- Attach a serial device using UART HCI to the Bluetooth stack for a broadcom device:

```
hciattach /dev/ttySAC3 –S 3000000 bcm2035 3000000 flow
```

- Run the Bluetooth daemon version 5.37:

```
bluetoothd
```

- Bring the device up, set up the device name, and enable the SSP mode:

```
hciconfig hci0 up
hciconfig hci0 name “Tizen-Mobile”
hciconfig hci0 sspmode 1
```

- Switch on the Bluetooth radio:

```
rfkill unblock bluetooth
```

- Switch off the Bluetooth radio:

```
rfkill block bluetooth
```

- Configuration for the sc2331 Bluetooth chipset by Spreadtrum


- `hciattach`




- Registering the Bluetooth device:




- Install the following files in the target's `/usr/lib/firmware` directory:

```
sc2331_fdl.bin
sc2331_fw.bin
scx35_pikeavivaltove_3M_MARLIN_connectivity_calibration.ini
scx35_pikeavivaltove_3M_MARLIN_connectivity_configure.ini
```

- The Bluetooth UART used is `/dev/ttyS0`.
- The UART speed configuration is 3000000 for sc2331.
- Attach a serial device using UART HCI to the Bluetooth stack:

```
hciattach -s 3000000 /dev/ttyS0 sprd 3000000 flow
```

- Run the bluetooth daemon version 5.37:

```
bluetoothd
```

- Bring the device up, set up the device name, and enable the SSP mode:

```
hciconfig hci0 up
hciconfig hci0 name “Tizen-Mobile”
hciconfig hci0 sspmode 1

```

### References[[edit](https://wiki.tizen.org/index.php?title=Porting_Guide/Connectivity&action=edit&section=T-4)]

Open source component version: BlueZ 5.37

For more information, see [http://www.bluez.org/](http://www.bluez.org/).

- Reference kernel configuration for Bluetooth

The following kernel `.config` are enabled for Broadcom Bluetooth support:

```
CONFIG_BT=y
CONFIG_BT_L2CAP=y
CONFIG_BT_RFCOMM=y
CONFIG_BT_RFCOMM_TTY=y
CONFIG_BT_BNEP=y
CONFIG_BT_HIDP=y
CONFIG_BT_HCIUART=y
CONFIG_BT_HCIUART_H4=y
CONFIG_BCM4330=y
CONFIG_RFKILL=y
CONFIG_RFKILL_INPUT=y
CONFIG_RXTRA_FIRMWARE_BCM4330=”BCM4330.hcd”
```

The following kernel `.config` are enabled for Bluetooth AVRCP support:

```
CONFIG_INPUT_MISC=y
CONFIG_INPUT_UINPUT=y

```

The following kernel `.config` are enabled for Bluetooth HID support:

```
CONFIG_INPUT_GP2A=y
CONFIG_INPUT_KR3DH=y
```

The following kernel `.config` are enabled for Bluetooth Audio (SCO-over-PCM) support:

```
CONFIG_BT_SCO=y
CONFIG_INPUT_GP2A=y
CONFIG_INPUT_KR3DH=y
```

The following kernel `.config` are enabled for Bluetooth Audio (SCO-over-PCM) support:

```
CONFIG_BT_SCO=y
```

## WLAN[[edit](https://wiki.tizen.org/index.php?title=Porting_Guide/Connectivity&action=edit&section=T-5)]

This section provides a step-by-step explanation of what's involved in adding a new Wi-Fi driver and making Wi-Fi work. [![Wlan.png](https://wiki.tizen.org/images/thumb/1/16/Wlan.png/800px-Wlan.png)](https://wiki.tizen.org/File:Wlan.png)

Feature Overview:

- WLAN (802.11 b/g/n)
- WPS PBC
- EAP (PEAP, TTLS)

Tizen uses `wpa_supplicant` as the platform interface to the Wi-Fi device. Your Wi-Fi driver must be compatible with the standard `wpa_supplicant`.

The Tizen WLAN architecture is centered on the Linux wireless (IEEE-802.11) subsystem. The Linux wireless SW stack defines the WLAN hardware adaptation software interfaces that need to be used in Tizen. In practice, the required interfaces are defined by cfg80211 for FullMAC WLAN devices and by mac80211 for SoftMAC WLAN devices. In addition, a Linux network interface needs to be supported towards the Linux TCP/IP stack.

The Connection Manager (ConnMan) is a daemon for managing internet connections within embedded devices running the Linux operating system.

The `wpa_supplicant` is a WPA Supplicant with support for WPA and WPA2 (IEEE 802.11i / RSN). Supplicant is the IEEE 802.1X/WPA component that is used in the client stations. It implements key negotiation with a WPA Authenticator and it controls the roaming and IEEE 802.11 authentication/association of the WLAN driver.

### Porting OAL Interface[[edit](https://wiki.tizen.org/index.php?title=Porting_Guide/Connectivity&action=edit&section=T-6)]

The WLAN driver plugin is specific to a Wi-Fi chipset. This includes firmware and tools specific to Wi-Fi chipsets. Wi-Fi chipset firmware and tools files must be copied to the WLAN driver plugin directory, built, and installed before testing the Wi-Fi functionality. Because of Tizen platform requirement, the Wi-Fi driver must create the `/opt/etc/.mac.info` file, which has the MAC address of device.

The WLAN driver plugin contains the `wlan.sh` file (located in `/usr/bin/wlan.sh`), which is used to load or unload the Wi-Fi driver firmware.

When the `wifi_activate()` function is called, the load driver request is sent to the NET-CONFIG daemon. The NET-CONFIG daemon loads the Wi-Fi driver using the `wlan.sh` script file. Similarly, the `wifi_deactivate()` function requests unloading of the Wi-Fi driver. In case of Wi-Fi Direct, the `wifi_direct_activate()` and `wifi_direct_deactivate()` functions make the Wi-Fi Direct manager load or unload the Wi-Fi driver using the `wlan.sh` script.

Using the `/usr/bin/wlan.sh` script:

- `wlan.sh start`: Power up the Wi-Fi driver in station mode by loading the driver and running the firmware file.
- `wlan.sh p2p`: Power up the Wi-Fi driver in Wi-Fi Direct mode by loading the driver and running the firmware file.
- `wlan.sh softap`: Power up the Wi-Fi driver in Soft AP mode by loading the driver and running the firmware file.
- `wlan.sh stop`: Power down the Wi-Fi driver.

All other Wi-Fi related functionality is handled by the ConnMan daemon

### References[[edit](https://wiki.tizen.org/index.php?title=Porting_Guide/Connectivity&action=edit&section=T-7)]

- Connection Manager (ConnMan) project website: [https://01.org/connman](https://01.org/connman)
- Linux wireless (IEEE-802.11) subsystem: [http://linuxwireless.org/](http://linuxwireless.org/)
- Information on Linux WPA/WPA2/IEEE 802.1X Supplicant: [http://hostap.epitest.fi/wpa_supplicant/](http://hostap.epitest.fi/wpa_supplicant/)
- Latest ConnMan release: [http://git.kernel.org/?p=network/connman/connman.git;a=summary](http://git.kernel.org/?p=network/connman/connman.git;a=summary)
- WLAN driver plugin git path: `/adaptation/devices/wlandrv-plugin-tizen-bcm43xx`


- Reference kernel configurations


- These options need to be enabled if the driver supports the cfg802.11 configuration API, instead of the wireless extension API. For more information, see [http://linuxwireless.org](http://linuxwireless.org/).

```
CONFIG_CFG80211
CONFIG_LIB80211
CONFIG_MAC80211 (Enable this flag, if the driver supports the softMAC feature)

```

- The following configuration options must be enabled in the kernel if the driver supports wireless extension APIs.

```
CONFIG_WIRELESS_EXT=y
CONFIG_WEXT_CORE=y
CONFIG_WEXT_PROC=y
CONFIG_WEXT_PRIV=y
CONFIG_WEXT_SPY=y
CONFIG_WIRELESS_EXT_SYSFS=y
```

## NFC[[edit](https://wiki.tizen.org/index.php?title=Porting_Guide/Connectivity&action=edit&section=T-8)]

The NFC application enables the user to read and/or import the content written on an NFC tag, edit the content written on an NFC tag, write and save data in an NFC tag, and load and save the NFC data from or in a file.

[![Nfc.png](https://wiki.tizen.org/images/thumb/4/43/Nfc.png/600px-Nfc.png)](https://wiki.tizen.org/File:Nfc.png)

The NFC client acts as an interface between the NFC app and the NFC manager, while writing or editing tag information in any physical tag. The NFC manager is the main interface, which actually deals with NFC physical tags, creates a connection with tags, and detects it. It is a daemon process to control the NFC chipset (such as NXP pn544). It provides the read and write service and basic P2P communication service, as well as the basic API for the client application. The NFC stack contains the required plugin, based on the NFC chipset. Currently, the `nfc-plugin-nxp` is used for the NXP chipset. The NFC plugin acts as an interface between the NFC chipset with the NFC framework (`nfc-manager`). It must be implemented according to the interface provided by the `nfc-manager`.

### Porting OAL Interface[[edit](https://wiki.tizen.org/index.php?title=Porting_Guide/Connectivity&action=edit&section=T-9)]

The NFC plugin is implemented as a shared library and it interfaces the Tizen `nfc-manager` and the vendor NFC chip. The NFC manager loads the `libnfc-plugin.so` library at runtime from the `/usr/lib/libnfc-plugin.so` directory. Any vendor-specific plugin is installed within the same path. The plugin must be written with predefined OAL API interfaces.

During initialization, the `nfc-manager` loads the `nfc-plugin.so` library, searches for the `onload()` function, and calls the function with an interface structure instance as an argument for mapping of all the OAL interfaces. These OAL/OEM interfaces are implemented according to the underlying NFC chipset. Once the mapping is done, the NFC manager interact with `nfc-plugin`, which implements the vendor specific OAL interfaces.

The following example shows the `onload()` function for reference:

```
Bool
onload(net_nfc_oem_interface_s *oem_interfaces)
{
    oem_interfaces->init = xxx;  /* xxx refers to plugin APIs */
    oem_interfaces->deinit = xxx;
    oem_interfaces->register_listener = xxx;
    oem_interfaces->unregister_listener = xxx;
    oem_interfaces->check_firmware_version = xxx;

    return true;
}

```

The NFC OAL interfaces are defined in the following structure. Use the `net_nfc_oem_controller.h` header file.

```
typedef struct _net_nfc_oem_interface_s
{
    net_nfc_oem_controller_init init;
    net_nfc_oem_controller_deinit deinit;
    net_nfc_oem_controller_register_listener register_listener;
    net_nfc_oem_controller_unregister_listener unregister_listener;
    net_nfc_oem_controller_check_firmware_version check_firmware_version;
    net_nfc_oem_controller_update_firmware update_firmeware;
    net_nfc_oem_controller_get_stack_information get_stack_information;
    net_nfc_oem_controller_configure_discovery configure_discovery;
    net_nfc_oem_controller_get_secure_element_list get_secure_element_list;
    net_nfc_oem_controller_set_secure_element_mode set_secure_element_mode;
    net_nfc_oem_controller_connect connect;
    net_nfc_oem_controller_connect disconnect;
    net_nfc_oem_controller_check_ndef check_ndef;
    net_nfc_oem_controller_check_target_presence check_presence;
    net_nfc_oem_controller_read_ndef read_ndef;
    net_nfc_oem_controller_write_ndef write_ndef;
    net_nfc_oem_controller_make_read_only_ndef make_read_only_ndef;
    net_nfc_oem_controller_transceive transceive;
    net_nfc_oem_controller_format_ndef format_ndef;
    net_nfc_oem_controller_exception_handler exception_handler;
    net_nfc_oem_controller_is_ready is_ready;
    net_nfc_oem_controller_llcp_config config_llcp;
    net_nfc_oem_controller_llcp_check_llcp check_llcp_status;
    net_nfc_oem_controller_llcp_activate_llcp activate_llcp;
    net_nfc_oem_controller_llcp_create_socket create_llcp_socket;
    net_nfc_oem_controller_llcp_bind bind_llcp_socket;
    net_nfc_oem_controller_llcp_listen listen_llcp_socket;
    net_nfc_oem_controller_llcp_accept accept_llcp_socket;
    net_nfc_oem_controller_llcp_connect_by_url connect_llcp_by_url;
    net_nfc_oem_controller_llcp_connect connect_llcp;
    net_nfc_oem_controller_llcp_disconnect disconnect_llcp;
    net_nfc_oem_controller_llcp_socket_close close_llcp_socket;
    net_nfc_oem_controller_llcp_recv recv_llcp;
    net_nfc_oem_controller_llcp_send send_llcp;
    net_nfc_oem_controller_llcp_recv_from recv_from_llcp;
    net_nfc_oem_controller_llcp_send_to send_to_llcp;
    net_nfc_oem_controller_llcp_reject reject_llcp;
    net_nfc_oem_controller_llcp_get_remote_config get_remote_config;
    net_nfc_oem_controller_llcp_get_remote_socket_info get_remote_socket_info;
    net_nfc_oem_controller_sim_test sim_test;
    net_nfc_oem_controller_test_mode_on test_mode_on;
    net_nfc_oem_controller_test_mode_off test_mode_off;
net_nfc_oem_controller_support_nfc support_nfc;
} net_nfc_oem_interface_s;

```

The `nfc_oem_interface_s` is exported in the `nfc-plugin`. Using this interface structure, the `nfc-manager` communicates with the OAL interfaces at runtime. The NFC plugin loads when the `nfc-manager` is started and the plugin `init()` function is called to initialize the NFC chip.

```
int (*init) (net_nfc_oem_controller_init*);
```

The `deinit()` function the `nfc-manager` issues to deinitialize the NFC chip:

```
int (*deinit) (net_nfc_oem_controller_deinit *);
```

- Sending the notification to the upper layer (NFC Service)

Refer to the `phdal4nfc_message_glib.c` file. The `g_idle_add_full` is used for handling the message in the NFC Service. You can use the callback client asynchronously in the client context. Post a message in queue, and the message is processed by a client thread.

- Reference implementation of the NFC plugin

Sample code snippets cannot be reproduced. Code is proriatory. For reference, see the `nfc-plugin-emul` and `nfc-plugin-nxp` files.

### Configuration[[edit](https://wiki.tizen.org/index.php?title=Porting_Guide/Connectivity&action=edit&section=T-10)]

The `nfc-plugin` package must be saved to the `/usr/lib/libnfc-plugin.so` directory when installed. When the `nfc-manager` starts, it looks for the plugin library and loads it dynamically from this path.

### References[[edit](https://wiki.tizen.org/index.php?title=Porting_Guide/Connectivity&action=edit&section=T-11)]

Enable the following configuration options in the kernel `.config`.

```
Using Pn544: CONFIG_PN544_NFC
Using Pn65n: CONFIG_PN65N_NFC

```

API references available are under the [Tizen_3.0_Porting_Guide#Appendix_2](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Appendix_2).

For more information, see [http://nfc-forum.org/](http://nfc-forum.org/).

## MTP[[edit](https://wiki.tizen.org/index.php?title=Porting_Guide/Connectivity&action=edit&section=T-12)]

- MTP exchanges can only occur between 2 products at a time, and in each communication, 1 product acts as the initiator and the other as the responder.
- The initiator is the product that initiates actions with the responder by sending operations to the responder.

[![Mtp-initiator.png](https://wiki.tizen.org/images/thumb/2/2f/Mtp-initiator.png/600px-Mtp-initiator.png)](https://wiki.tizen.org/File:Mtp-initiator.png)

- The responder can not initiate any actions, and can only send responses to operations sent by the initiator or send events.

[![Mtp-responder.png](https://wiki.tizen.org/images/thumb/6/6d/Mtp-responder.png/600px-Mtp-responder.png)](https://wiki.tizen.org/File:Mtp-responder.png)

- In the Tizen system, the USB host is the initiator, and the USB device is the responder.

### Porting OAL Interface[[edit](https://wiki.tizen.org/index.php?title=Porting_Guide/Connectivity&action=edit&section=T-13)]

- Tizen MTP initiator and responder do not have an OAL Interface.
- There are extension possibilities of the MTP Transport layer.

### Configuration[[edit](https://wiki.tizen.org/index.php?title=Porting_Guide/Connectivity&action=edit&section=T-14)]

- MTP Initiator


- The MTP Initiator consist of 3 packages.

```
mtp-initiator daemon
mtp-initiator api
libmtp opensource
```

- The MTP initiator does not operate independently. It requires the help of another module, such as USB.
- When the USB device is connected to the host, the module must run the MTP initiator daemon.


- MTP Responder


- The MTP responder consist of 1 package.

```
mtp-responder daemon
```

- The MTP responder does not operate independently. It requires the help of another module, such as USB.
- When the USB device is connected to the host, the module must run the MTP responder daemon.

### References[[edit](https://wiki.tizen.org/index.php?title=Porting_Guide/Connectivity&action=edit&section=T-15)]

- Media Transfer Protocol v.1.1 Spec: [http://www.usb.org/developers/docs/devclass_docs/](http://www.usb.org/developers/docs/devclass_docs/)

# Location[[edit](https://wiki.tizen.org/index.php?title=Tizen_3.0_Porting_Guide&action=edit&section=12)]

## Location Framework[[edit](https://wiki.tizen.org/index.php?title=3.0_Porting_Guide/Location&action=edit&section=T-1)]

Location provides location based services (LBS) including the position information, satellite information and GPS status.

[![Location.png](https://wiki.tizen.org/images/3/30/Location.png)](https://wiki.tizen.org/File:Location.png)

You can use the following location features´:

- GPS (Global positioning system)
- Getting the current position, last known position, accuracy, distance and velocity
- Getting the satellite information of GPS and GLONASS
- Notifying a user when they enter or exit a predefined set of boundaries, known as geofence, like school attendance zones or neighborhood boundaries


- Location framework


- location-manager




- Location Library
  - Contains the location providers that can be used by the location-manager to get the services.
  - GPS
    - GPS provides position information, velocity and satellite information. It is used to get the current position of a device.
- dbus
  - This is the IPC used to communicate between location module and the Location daemon.
- lbs-server
  - lbs-server provides position, velocity, NMEA, and satellite information by communicating with a GPS chip.
  - lbs-server has the following functionalities:
    - Initializes and deinitializes the GPS, opens and closes GPS applications.
    - Provides the position result for location library.
    - Location session management-determination for session termination based on session status.
    - Serial interface with the GPS receiver
    - Enables the GPS chipset to support standalone GPS positioning methods.
    - Supports the standalone operation mode.



### Porting OAL Interface[[edit](https://wiki.tizen.org/index.php?title=3.0_Porting_Guide/Location&action=edit&section=T-2)]

The GPS plugin is implemented based on the Tizen `lbs-server` for vendor specific GPS devices.

The GPS plugin is implemented as a shared library and the `lbs-server` loads a specific GPS plugin at runtime. A GPS plugin must be written with predefined interfaces.

The `lbs-server-plugin-dev` source package is installed on OBS by adding the following command in the package spec file.

```
BuildRequires: pkgconfig(lbs-server-plugin)

```

The `lbs-server-plugin-dev` package source files can be found in the following directories:

```
/usr/include/lbs-server-plugin/*.h 
/usr/lib/pkgconfig/lbs-server-plugin.pc

```

The `gps_plugin_intf.h` header file includes the API interfaces for the communication between the `lbs-server` and its GPS plugin.

```
typedef struct { 
    /* Initialize the plugin module and register callback function for event delivery */ 
    int (*init) (gps_event_cb gps_event_cb, void *user_data); 
    /* Deinitialize the plugin module */ 
    int (*deinit) (gps_failure_reason_t *reason_code); 
    /* Request specific action to plugin module */ 
    int (*request) (gps_action_t gps_action, void *gps_action_data, gps_failure_reason_t *reason_code); 
} gps_plugin_interface; 

```

```
const gps_plugin_interface *get_gps_plugin_interface();

```

The `get_gps_plugin_interface()` function must be exported in the GPS plugin. It gives the `gps_plugin_interface` structure to the `lbs-server`, and the `lbs-server` communicates by these interfaces. When the `lbs-server` is started, the GPS plugin is loaded and the `init()` function is called. At this moment, a GPS device must be initialized.

```
int (*init) (gps_event_cb gps_event_cb, void *user_data);

```

When `init()` function is called, the `gps_event_cb` is set. GPS events and data from a GPS device is delivered by the `gps_event_cb` registered call back function.

```
typedef int (*gps_event_cb) (gps_event_info_t *gps_event_info, void *user_data);

```

The following example describes the GPS events.

```
typedef enum { 
    GPS_EVENT_START_SESSION = 0x0000, /* The session is started */ 
    GPS_EVENT_STOP_SESSION, /* The session is stopped */ 
    GPS_EVENT_CHANGE_INTERVAL, /* Change updating interval */
    GPS_EVENT_REPORT_POSITION = 0x0100, /* Bring up GPS position data */ 
    GPS_EVENT_REPORT_SATELLITE, /* Bring up GPS SV data */ 
    GPS_EVENT_REPORT_NMEA, /* Bring up GPS NMEA data */ 
    GPS_EVENT_SET_OPTION = 0x0200, /* The option is set */ 
    GPS_EVENT_GET_REF_LOCATION = 0x0300, /* Get the reference location for AGPS */ 
    GPS_EVENT_GET_IMSI, /* Get IMSI for identification */ 
    GPS_EVENT_OPEN_DATA_CONNECTION = 0x0400, /* Request opening data network connection */ 
    GPS_EVENT_CLOSE_DATA_CONNECTION, /* Request closing data network connection */ 
    GPS_EVENT_DNS_LOOKUP_IND, /* Request resolving host name */ 
    GPS_EVENT_AGPS_VERIFICATION_INDI, /* Verification indicator for AGPS is required */
    GPS_EVENT_FACTORY_TEST = 0x0500,/* Factory test is done */ 
    GPS_EVENT_ERR_CAUSE = 0xFFFF /* Some error is occurred */ 
} gps_event_id_t;

```

The GPS events contains specific GPS event data which is part of `gps_event_data_t` is delivered, see the `gps_plugin_intf.h`. When the `lbs-server` want to make a request to GPS device, the `request()` function is called.

```
int (*request) (gps_action_t gps_action, void *gps_action_data, gps_failure_reason_t *reason_code); 

```

Each request is classified by `gps_action_t`.

```
typedef enum { 
    GPS_ACTION_SEND_PARAMS = 0x00, 
    GPS_ACTION_START_SESSION, 
    GPS_ACTION_STOP_SESSION, 
    GPS_ACTION_CHANGE_INTERVAL,
    GPS_INDI_SUPL_VERIFICATION, 
    GPS_INDI_SUPL_DNSQUERY, 
    GPS_ACTION_START_FACTTEST, 
    GPS_ACTION_STOP_FACTTEST, 
    GPS_ACTION_REQUEST_SUPL_NI,
    GPS_ACTION_DELETE_GPS_DATA, 
} gps_action_t;

```

With the standalone GPS (unassisted GPS), the `GPS_ACTION_START_SESSION` and `GPS_ACTION_STOP_SESSION` are mandatory actions. If the `GPS_ACTION_START_SESSION` is delivered, the GPS plugin starts the acquisition of satellites and reports the `GPS_EVENT_START_SESSION` event to the `lbs-server` by the `gps_event_cb` callback function. Once the acquisition is completed and position is fixed, its position should be delivered by the `gps_event_cb` with the `GPS_EVENT_REPORT_POSITION` event ID and the position data.

To shut down the `lbs-server`, deinitialize the GPS device with the `deinit()` function.

```
int (*deinit) (gps_failure_reason_t *reason_code);

```

- Addign a new GPS plugin



```
#define PLATFORM_PATH "/sys/devices/platform"
#define PLUGIN_PATH PLATFORM_PATH"/xxxxx_gps"

```

The `check_plugin_module(char* module_name)` function checks the access to available plugin in the `/sys/devices/platform` directory and the `load_plugin_module` loads the plugin during the boot up time.

## Geofence[[edit](https://wiki.tizen.org/index.php?title=3.0_Porting_Guide/Location&action=edit&section=T-3)]

The Geofence Manager API provides service related to geofence. A geofence is a virtual perimeter for a real-world geographic area.

[![Geofence.png](https://wiki.tizen.org/images/5/58/Geofence.png)](https://wiki.tizen.org/File:Geofence.png)

You can to set a geofence with geopoint, Wi-Fi MAC address, and Bluetooth address. Notifications on events, such as changes in the service status are provided.

There are 2 kinds of places and fences:

- Public places and fences that are created by the MyPlace application can be used by all applications.
- Private places and fences that are created by a specified application can only be used by the same application.

Notifications can be received about the following events:

- Zone in when a device enters a specific area
- Zone out when a device exits a specific area
- Results and errors for each event requested by the geofence module

## Map Service[[edit](https://wiki.tizen.org/index.php?title=3.0_Porting_Guide/Location&action=edit&section=T-4)]

The Location Maps API (Maps API) allows you to create map-aware applications.

[![Mapservice.png](https://wiki.tizen.org/images/3/35/Mapservice.png)](https://wiki.tizen.org/File:Mapservice.png)

The Maps API has the following features:

- Geocoder (geocoding and reverse geocoding)
- Places (search places)
- Routes (search directions)
- Map Widget (rendering map images)

The Maps API allows you to choose a map service provider to be included in the plugins.

### Porting OAL Interface[[edit](https://wiki.tizen.org/index.php?title=3.0_Porting_Guide/Location&action=edit&section=T-5)]

The Maps plugin is implemented as a shared library and the Maps framework loads a specific Maps plugin at runtime. A Maps plugin must be written with predefined interfaces. The `capi-maps-service-plugin-devel` source package is installed on OBS by adding the following command in the package specification file:

```
BuildRequires: pkgconfig(capi-maps-service-plugin-devel)

```

The `capi-maps-service-plugin-devel` package source files can be found in the following directories:

```
/usr/include/maps/maps_plugin*.h
/usr/include/maps/maps_*_plugin.h
/usr/include/maps/maps_extra_types.h

```

The `module.h` header file includes the API interfaces for the communication between the Maps and its plugin.

```
typedef struct _interface_s {
    /* Plugin dedicated functions */
    maps_plugin_init_f maps_plugin_init;
    maps_plugin_shutdown_f maps_plugin_shutdown;
    maps_plugin_get_info_f maps_plugin_get_info;
    maps_plugin_init_module_f maps_plugin_init_module;

    /* Maps Provider access key, preference, and capabilities */
    maps_plugin_set_provider_key_f maps_plugin_set_provider_key;
    maps_plugin_get_provider_key_f maps_plugin_get_provider_key;
    maps_plugin_set_preference_f maps_plugin_set_preference;
    maps_plugin_get_preference_f maps_plugin_get_preference;
    maps_plugin_is_service_supported_f maps_plugin_is_service_supported;
    maps_plugin_is_data_supported_f maps_plugin_is_data_supported;

    /* Geocode */
    maps_plugin_geocode_f maps_plugin_geocode;
    maps_plugin_geocode_inside_area_f maps_plugin_geocode_inside_area;
    maps_plugin_geocode_by_structured_address_f maps_plugin_geocode_by_structured_address;
    maps_plugin_reverse_geocode_f maps_plugin_reverse_geocode;
    maps_plugin_multi_reverse_geocode_f maps_plugin_multi_reverse_geocode;

    /* Place */
    maps_plugin_search_place_f maps_plugin_search_place;
    maps_plugin_search_place_by_area_f maps_plugin_search_place_by_area;
    maps_plugin_search_place_by_address_f maps_plugin_search_place_by_address;
    maps_plugin_search_place_list_f maps_plugin_search_place_list;
    maps_plugin_get_place_details_f maps_plugin_get_place_details;

    /* Route */
    maps_plugin_search_route_f maps_plugin_search_route;
    maps_plugin_search_route_waypoints_f maps_plugin_search_route_waypoints;

    /* Cancel request */
    maps_plugin_cancel_request_f maps_plugin_cancel_request;

    /* Mapping */
    maps_plugin_create_map_view_f maps_plugin_create_map_view;
    maps_plugin_destroy_map_view_f maps_plugin_destroy_map_view;
    maps_plugin_render_map_f maps_plugin_render_map;
    maps_plugin_move_center_f maps_plugin_move_center;
    maps_plugin_set_scalebar_f maps_plugin_set_scalebar;
    maps_plugin_get_scalebar_f maps_plugin_get_scalebar;
    maps_plugin_on_object_f maps_plugin_on_object;
    maps_plugin_screen_to_geography_f maps_plugin_screen_to_geography;
    maps_plugin_geography_to_screen_f maps_plugin_geography_to_screen;
    maps_plugin_get_min_zoom_level_f maps_plugin_get_min_zoom_level;
    maps_plugin_get_max_zoom_level_f maps_plugin_get_max_zoom_level;
    maps_plugin_get_center_f maps_plugin_get_center;
    maps_plugin_capture_snapshot_f maps_plugin_capture_snapshot;
} interface_s;

```

These functions must be implemented and exported in the Maps plugin. To create a Maps handle classified by provider name string, the `maps_plugin_get_info()` function must provide the name. The name is recommended to be capitalized.

The Maps plugins are located in the `/usr/lib/maps/plugins` directory.

#### HERE Maps plugin[[edit](https://wiki.tizen.org/index.php?title=3.0_Porting_Guide/Location&action=edit&section=T-6)]

For now, the HERE Maps plugin is embedded on the platform basically, and the provider name is 'HERE'. To use this plugin, you must get the credential keys in the HERE developers site, "[https://developer.here.com](https://developer.here.com/)". You may need to pay a fee according to the threshold.

For user consent demanded by HERE, the user consent application included in the HERE Maps plugin is launched at first time of use if not agreed before.

# Telephony[[edit](https://wiki.tizen.org/index.php?title=Tizen_3.0_Porting_Guide&action=edit&section=13)]

This document covers detailed Telephony architecture including the various components of Telephony and workflow through Telephony framework. The document also provides porting guidelines for vendors to ease the OAL interface development for their hardware.

- Tizen Telephony features


- Telecommunication functionalities, such as call, SS, SMS, SIM, network, and packet service
- Plug-in Architecture


- Definitions


- Core object
  - Bundle of functions and supportive database information designated to specific module, such as call, SS, SIM, network, which processes requests, responses, and notifications.
  - Core objects form the executable component of a Telephony module (call, SS, SIM, network)
- HAL
  - HAL, Hardware Abstraction Layer, abstracts the actual hardware used and ensures that similar functionality is provided by various hardware (modems) of the same modem vendor.
  - All hardware specific changes are controlled and processed by HALs.
  - The modem driver can be required depending on the modem chipset.
- Hooks
  - Hooks provide a mechanism to tap requests, responses, and notifications of other Telephony modules.
  - Hooking is a transparent mechanism and does not affect the normal processing of requests, responses, and notifications.

## Tizen Telephony Architecture[[edit](https://wiki.tizen.org/index.php?title=Tizen_3.0_Porting_Guide&action=edit&section=14)]

Tizen Telephony supports the plugin architecture, which provides flexibility to include various types of predefined plugins into the system with little change.

[![Telephony-arch.png](https://wiki.tizen.org/images/thumb/5/5f/Telephony-arch.png/700px-Telephony-arch.png)](https://wiki.tizen.org/File:Telephony-arch.png)

The 3 major components of Tizen Telephony are the libraries, plugins, and server.

## Telephony Libraries[[edit](https://wiki.tizen.org/index.php?title=Tizen_3.0_Porting_Guide&action=edit&section=15)]

- Telephony API (TAPI) library

The TAPI library (or simply TAPI) is a standardized interface provided to applications to interact with Tizen Telephony. It is provided as a `libtapi` package. The TAPI executes in the application’s context, and it provides sync and async APIs. The following figure shows the `libtapi` internal composition.

[![Libtapi.PNG](https://wiki.tizen.org/images/thumb/5/5c/Libtapi.PNG/500px-Libtapi.PNG)](https://wiki.tizen.org/File:Libtapi.PNG)

Applications can interface to Telephony features, such as call, SMS, and network, through the respective module APIs exposed in the `libtapi` library. Telephony also provides an additional library, `capi-telephony` for third party applications.

- Core Telephony library

The Core Telephony library (or `libtcore`) provides an API framework for Tizen Telephony to inter-work. It is provided as `libtcore` package. The following figure shows the internal composition overview of the `libtcore`.

[![Telephony03.png](https://wiki.tizen.org/images/thumb/f/f3/Telephony03.png/500px-Telephony03.png)](https://wiki.tizen.org/File:Telephony03.png)

With `libtcore`, you can:

- Create, destroy, and maintain various server components, such as server, communicator, HAL, plugin, and core object.
- Maintain storage, queue mechanism, and general utilities.
- Support CMUX (creation/destruction/processing).
- Parse AT.

## Telephony Plugins[[edit](https://wiki.tizen.org/index.php?title=Tizen_3.0_Porting_Guide&action=edit&section=16)]

There are 4 kinds of plugins:

- Communicator plugins
  - Interfaces TAPI and Telephony Server.
  - For example, DBUS communicator (`DBUS_TAPI`) is provided by default.




- Modem plugins
  - Core functional units providing the Telephony functionality.
  - Maintain and manage the Telephony states.
  - Maintain and manage the databases related to Telephony.




- Modem interface plugins
  - Interfaces the telephony server to the communication processor.
  - Hardware specific plugins which define hardware capabilities and usage
  - Modem interface plugin is also called HAL.




- Free Style plugins
  - Provide completely independent functionality irrespective of hardware (communication processor).
  - For example plugins, such as packetservice, storage, and indicator.



The following figure provides an overview of all the Telephony plugins together.

[![Telephony08.png](https://wiki.tizen.org/images/thumb/1/15/Telephony08.png/500px-Telephony08.png)](https://wiki.tizen.org/File:Telephony08.png)

## Telephony Server[[edit](https://wiki.tizen.org/index.php?title=Tizen_3.0_Porting_Guide&action=edit&section=17)]

Tizen Telephony runs as a Telephony server daemon called `telephony-daemon`.

The Telephony server executes as a `g-main` loop from the `glib` library.

[![Telephony09.png](https://wiki.tizen.org/images/thumb/7/75/Telephony09.png/800px-Telephony09.png)](https://wiki.tizen.org/File:Telephony09.png)

## Porting OAL Interface[[edit](https://wiki.tizen.org/index.php?title=Tizen_3.0_Porting_Guide&action=edit&section=18)]

OEM vendors can port available plugins within Telephony as needed. It is not mandatory that all the plugins to be ported to support a specific hardware.

This section provides guidance to OEM vendors to develop various Telephony plugins.

### Plugin Descriptors[[edit](https://wiki.tizen.org/index.php?title=Tizen_3.0_Porting_Guide&action=edit&section=19)]

Any telephony plugin is required to provide a descriptor structure described in the following example.

| Structure                                | Description                              |
| ---------------------------------------- | ---------------------------------------- |
| `struct tcore_plugin_define_desc {    gchar *name;    enum tcore_plugin_priority priority;    int version;    gboolean(*load)();    gboolean(*init)(TcorePlugin *);    void (*unload)(TcorePlugin *);};` | Structure referred by Telephony server to load, initialize, and unload the plugin.This structure defines:Name of the pluginInitializing priority of the pluginPlugin versionPlugin 'load' function referencePlugin 'init' function referencePlugin 'unload' function reference |

The descriptor structure of each plugin must be named as `plugin_define_desc`. The server obtains the address of this symbol in order to provide control to the plugin to execute its defined functionality.

The order of initialization among various Telephony plugins is defined based on the plugin’s priority.

OEMs need to specifically implement the modem and modem interface plugins to support their hardware.

### Call Service Operations[[edit](https://wiki.tizen.org/index.php?title=Tizen_3.0_Porting_Guide&action=edit&section=20)]

The implementation of the functions described in the following example is required to provide call services.

| Structure                                | Description                              |
| ---------------------------------------- | ---------------------------------------- |
| `struct tcore_call_operations {    TReturn (*dial)(CoreObject *o, UserRequest *ur);    TReturn (*answer)(CoreObject *o, UserRequest *ur);    TReturn (*end)(CoreObject *o, UserRequest *ur);    TReturn (*hold)(CoreObject *o, UserRequest *ur);    TReturn (*active)(CoreObject *o, UserRequest *ur);    TReturn (*swap)(CoreObject *o, UserRequest *ur);    TReturn (*join)(CoreObject *o, UserRequest *ur);    TReturn (*split)(CoreObject *o, UserRequest *ur);};` | The structure referred by the Telephony server to provide call services.This structure defines:Call 'dial' function referenceCall 'answer' function referenceCall 'end' function referenceCall 'hold' function referenceCall 'active' function referenceCall 'swap' function referenceCall 'join' function referenceCall 'split' function reference |

### SMS Service Operations[[edit](https://wiki.tizen.org/index.php?title=Tizen_3.0_Porting_Guide&action=edit&section=21)]

The implementation of the functions described in the following example is required to provide SMS services.

| Structure                                | Description                              |
| ---------------------------------------- | ---------------------------------------- |
| `struct tcore_sms_operations {    TReturn (*send_umts_msg)(CoreObject *o, UserRequest *ur);    TReturn (*send_cdma_msg)(CoreObject *o, UserRequest *ur);    TReturn (*read_msg)(CoreObject *o, UserRequest *ur);    TReturn (*save_msg)(CoreObject *o, UserRequest *ur);    TReturn (*delete_msg)(CoreObject *o, UserRequest *ur);    TReturn (*get_sca)(CoreObject *o, UserRequest *ur);    TReturn (*set_sca)(CoreObject *o, UserRequest *ur);    TReturn (*get_sms_params)(CoreObject *o, UserRequest *ur);    TReturn (*set_sms_params)(CoreObject *o, UserRequest *ur);};` | Structure referred by the Telephony server to provide SMS-related services.This structure defines:SMS 'send' function referenceSMS 'read' function referenceSMS 'save' function referenceSMS 'delete' function referenceSMS 'get sca' function referenceSMS 'set sca' function referenceSMS 'get sms params' function referenceSMS 'set sms params' function reference |

### Network Service Operations[[edit](https://wiki.tizen.org/index.php?title=Tizen_3.0_Porting_Guide&action=edit&section=22)]

The implemenation of the functions described in the following example is required to provide network services.

| Structure                                | Description                              |
| ---------------------------------------- | ---------------------------------------- |
| `struct tcore_network_operations {    TReturn (*search)(CoreObject *o, UserRequest *ur);    TReturn (*set_plmn_selection_mode)(CoreObject *o, UserRequest *ur);    TReturn (*get_plmn_selection_mode)(CoreObject *o, UserRequest *ur);    TReturn (*set_service_domain)(CoreObject *o, UserRequest *ur);    TReturn (*get_service_domain)(CoreObject *o, UserRequest *ur);    TReturn (*set_band)(CoreObject *o, UserRequest *ur);    TReturn (*get_band)(CoreObject *o, UserRequest *ur);};` | Structure referred by the Telephony server to provide network services.This structure defines:Network 'search' function referenceNetwork 'set plmn selection mode' function referenceNetwork 'get plmn selection mode' function referenceNetwork 'set service domain' function referenceNetwork 'get service domain' function referenceNetwork 'set band' function referenceNetwork 'get band' function reference |

### HAL operations[[edit](https://wiki.tizen.org/index.php?title=Tizen_3.0_Porting_Guide&action=edit&section=23)]

The implementation of the functions described in the following example is required to provide HAL operations.

| Structure                                | Description                              |
| ---------------------------------------- | ---------------------------------------- |
| `struct tcore_hal_operations {    TReturn (*power)(TcoreHal *hal, gboolean flag);    TReturn (*send)(TcoreHal *hal, unsigned int data_len, void *data);    TReturn (*setup_netif)(CoreObject *co,                           TcoreHalSetupNetifCallback func, void *user_data,                           unsigned int cid, gboolean enable);};` | Structure referred by Telephony server to provide HAL operations.This structure defines:HAL 'power' function referenceHAL 'send' function referenceHAL 'setup network interface' function reference |

Sample implementations of the modem and modem interface plugins is available in the [Appendix](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Appendix) section.

## Configuration[[edit](https://wiki.tizen.org/index.php?title=Tizen_3.0_Porting_Guide&action=edit&section=24)]

There are no specific configurations required for Telephony except for conforming to the installation paths of various Telephony plugins.

All Telephony plugins need to be installed in the following folders:

- Modem Plugins: `%{_libdir}/telephony/plugins/modems/`
- Other Plugins: `%{_libdir}/telephony/plugins/`

## References[[edit](https://wiki.tizen.org/index.php?title=Tizen_3.0_Porting_Guide&action=edit&section=25)]

Tizen source website [http://review.tizen.org/git/](http://review.tizen.org/git/)

Telephony packages

- Telephony daemon




- Telephony core library




- TAPI




- Telephony API for a third party application




- Communicator (`DBUS_TAPI`)




- Free Style plugin (indicator)




- Free Style plugin (packetservice)




- Free Style plugin (nitz)




- Free Style plugin (Database)




- Free Style plugin (VCONF)




- Modem plugin (device)




- Modem Interface plugin (device)




- Modem plugin (emulator)




- Modem Interface plugin (emulator)



## Appendix[[edit](https://wiki.tizen.org/index.php?title=Tizen_3.0_Porting_Guide&action=edit&section=26)]

#### Sample Implementation for the Modem Interface Plugin[[edit](https://wiki.tizen.org/index.php?title=Tizen_3.0_Porting_Guide&action=edit&section=27)]

```
/* HAL Operations */
static struct tcore_hal_operations hal_ops = {
    .power = hal_power,
    .send = hal_send,
    .setup_netif = hal_setup_netif,
};

static
gboolean on_load()
{
    dbg(" Load!!!");

    return TRUE;
}

static 
gboolean on_init(TcorePlugin *plugin)
{
    TcoreHal *hal;
    PluginData *user_data;
    struct custom_data *data;

    dbg(" Init!!!");

    if (plugin == NULL) {
        err(" PLug-in is NULL");

        return FALSE;
    }

    /* User data for Modem Interface plugin */
    user_data = g_try_new0(PluginData, 1);
    if (user_data == NULL) {
        err(" Failed to allocate memory for Plugin data");

        return FALSE;
    }

    /* Register to eerver */
    user_data->modem = tcore_server_register_modem(tcore_plugin_ref_server(plugin), plugin);
    if (user_data->modem == NULL) {
        err(" Registration Failed");
        g_free(user_data);
	
        return FALSE;
    }
    dbg(" Registered from Server");


    data = g_try_new0(struct custom_data, 1);
    if (data == NULL) {
        err(" Failed to allocate memory for Custom data");

        /* Unregister from server */
        tcore_server_unregister_modem(tcore_plugin_ref_server(plugin), user_data->modem);

        /* Free plugin data */
        g_free(user_data);

        return FALSE;
    }

    /* Open DPRAM device */
    data->vdpram_fd = vdpram_open();
    if (data->vdpram_fd < 0) {
        /* Free custom data */
        g_free(data);

        /* Unregister from server */
        tcore_server_unregister_modem(tcore_plugin_ref_server(plugin), user_data->modem);

        /* Free plugin data */
        g_free(user_data);

        return FALSE;
    }
    /* Create and initialize HAL */
    hal = tcore_hal_new(plugin, "vmodem", &hal_ops, TCORE_HAL_MODE_AT);
    if (hal == NULL) {
        /* Close VDPRAM device */
        vdpram_close(data->vdpram_fd);

        /* Free custom data */
        g_free(data);

        /* Unregister from server */
        tcore_server_unregister_modem(tcore_plugin_ref_server(plugin), user_data->modem);

        /* Free Plugin data */
        g_free(user_data);

        return FALSE;
    }
    user_data->hal = hal;

    /* Link custom data to HAL user data */
    tcore_hal_link_user_data(hal, data);

    /* Set HAL as Modem Interface plugin's user data */
    tcore_plugin_link_user_data(plugin, user_data);

    /* Register to Watch list */
    data->watch_id_vdpram = __register_gio_watch(hal, data->vdpram_fd, on_recv_vdpram_message);
    dbg(" fd: [%d] Watch ID: [%d]", data->vdpram_fd, data->watch_id_vdpram);

    /* Power ON VDPRAM device */
    if (_modem_power(hal, TRUE) == TCORE_RETURN_SUCCESS) {
        dbg(" Power ON - [SUCCESS]");
    } else {
        err(" Power ON - [FAIL]");
        goto EXIT;
    }

    /* Check CP Power ON */
    g_timeout_add_full(G_PRIORITY_HIGH, SERVER_INIT_WAIT_TIMEOUT, __load_modem_plugin, hal, 0);

    dbg("[VMMODEM] Exit");

    return TRUE;

EXIT:
    /* Deregister from Watch list */
    __deregister_gio_watch(data->watch_id_vdpram);

    /* Free HAL */
    tcore_hal_free(hal);

    /* Close VDPRAM device */
    vdpram_close(data->vdpram_fd);

    /* Free custom data */
    g_free(data);

    /* Unregister from Server */
    tcore_server_unregister_modem(tcore_plugin_ref_server(plugin), user_data->modem);

    /* Free plugin data */
    g_free(user_data);

    return FALSE;
}

static void
on_unload(TcorePlugin *plugin)
{
    TcoreHal *hal;
    struct custom_data *data;
    PluginData *user_data;

    dbg(" Unload!!!");

    if (plugin == NULL)
        return;

    user_data = tcore_plugin_ref_user_data(plugin);
    if (user_data == NULL)
        return;

    hal = user_data->hal;

    data = tcore_hal_ref_user_data(hal);
    if (data == NULL)
        return;

    /* Deregister from Watch list */
    __deregister_gio_watch(data->watch_id_vdpram);
    dbg(" Deregistered Watch ID");

    /* Free HAL */
    tcore_hal_free(hal);
    dbg(" Freed HAL");

    /* Close VDPRAM device */
    vdpram_close(data->vdpram_fd);
    dbg(" Closed VDPRAM device");

    /* Free custom data */
    g_free(data);

    tcore_server_unregister_modem(tcore_plugin_ref_server(plugin), user_data->modem);
    dbg(" Unregistered from Server");

    dbg(" Unloaded MODEM");
    g_free(user_data);
}

/* VMODEM Descriptor Structure */
EXPORT_API struct tcore_plugin_define_desc plugin_define_desc = {
    .name = "VMODEM",
    .priority = TCORE_PLUGIN_PRIORITY_HIGH,
    .version = 1,
    .load = on_load,
    .init = on_init,
    .unload = on_unload
};

```

#### Sample Implementation for the Modem Plugin[[edit](https://wiki.tizen.org/index.php?title=Tizen_3.0_Porting_Guide&action=edit&section=28)]

```
static
gboolean on_load()
{
    dbg("LOAD!!!");

    return TRUE;
}

static
gboolean on_init(TcorePlugin *p)
{
    TcoreHal *h;

    dbg("INIT!!!");

    if (!p) {
        err("Plug-in is NULL");

        return FALSE;
    }

    h = tcore_server_find_hal(tcore_plugin_ref_server(p), "vmodem");
    if (!h) {
        err("HAL is NULL");

        return FALSE;
    }

    tcore_hal_add_send_hook(h, on_hal_send, p);
    tcore_hal_add_recv_callback(h, on_hal_recv, p);

    /* Initialize Modules */
    s_modem_init(p, h);
    s_network_init(p, h);
    s_sim_init(p, h);
    s_ps_init(p, h);
    s_call_init(p, h);
    s_ss_init(p, h);
    s_sms_init(p, h);
    tcore_hal_set_power(h, TRUE);

    /* Send "CPAS" command to invoke POWER UP NOTI */
    s_modem_send_poweron(p);

    dbg("Init - Successful");

    return TRUE;
}

static void
on_unload(TcorePlugin *p)
{
    TcoreHal *h;

    dbg("UNLOAD!!!");

    if (!p) {
        err("Plug-in is NULL");
	
        return;
    }

    h = tcore_server_find_hal(tcore_plugin_ref_server(p), "vmodem");
    if (h) {
        tcore_hal_remove_send_hook(h, on_hal_send);
        tcore_hal_remove_recv_callback(h, on_hal_recv);
    }

    /* Deinitialize the modules */
    s_modem_exit(p);
    s_network_exit(p);
    s_sim_exit(p);
    s_ps_exit(p);
    s_call_exit(p);
    s_ss_exit(p);
    s_sms_exit(p);
}

/* ATMODEM plug-in descriptor */
struct tcore_plugin_define_desc plugin_define_desc = {
    .name = "ATMODEM",
    .priority = TCORE_PLUGIN_PRIORITY_MID,
    .version = 1,
    .load = on_load,
    .init = on_init,
    .unload = on_unload
};

```

#### Workflow[[edit](https://wiki.tizen.org/index.php?title=Tizen_3.0_Porting_Guide&action=edit&section=29)]

1. Initialization sequence

   1. The server loads the modem interface plugin.
   2. The modem interface plugin registers to the server.
   3. The server enumerates the modem interface plugin.
   4. Create the physical HAL.
   5. The modem interface plugin queries the modem state.
   6. If the modem is online, the CMUX (internal) channels are established.
   7. The logical HAL is created for each CMUX channel and assigned for a core object type. These are updated to the mapping table.
   8. Change the physical HAL mode to `TRANSPARENT` (disables the queue).
   9. The modem interface plugin requests server to load the modem plugin (corresponding to its architecture).
   10. The server loads modem plugin.
   11. The modem plugin initializes the sub-modules and creates the core objects (based on the core object types defined in the mapping table by the modem interface plugin).
   12. The modem plugin notifies the server of the `PLUGIN_ADDED` event.
   13. The modem notifies the communicator of the `PLUGIN_ADDED` event.
   14. The communicator creates interfaces for the sub-modules present (based on the core objects created).

2. Request processing sequence

   1. The application request is sent to the communicator through TAPI.
   2. The communicator creates a user request based on the incoming request.
   3. The user request is dispatch to communicator.
   4. The communicator dispatches user request to server.
   5. The server finds the plugin based on the modem name.
   6. The server extracts the core object type based on the request command from plugin’s core objects list.
   7. The server dispatches the user request to the core object.
   8. The core object dispatches the user request to dispatch a function based on the request command.
   9. Pending request is formed, added to the queue, and sent to the logical HAL assigned for the core object.
   10. The logical HAL dispatches the request data to a CMUX channel dedicated to it.
   11. CMUX encodes the request data and dispatches it to the physical HAL.
   12. The physical HAL sends the request data to the modem.

3. Response processing sequence

   1. Response data sent by the modem is received by the physical HAL.
   2. The physical HAL dispatches the response data to CMUX.
   3. CMUX decodes the received response data and dispatches the corresponding logical HAL based on the CMUX channel.
   4. The logical HAL dispatches the decoded response data to the corresponding core object.
   5. The core object processes the received response data and extracts the user request from the pending queue and sends the response data corresponding to the user request.
   6. The user request extracts the communicator.
   7. The received response data is sent to the corresponding communicator.
   8. The communicator sends the response data to TAPI which communicates the response to application.

4. Indication processing sequence

   1. Notification data sent by the modem is received by the physical HAL.
   2. The physical HAL dispatches the notification data to CMUX.
   3. CMUX decodes the received notification data and dispatches the corresponding logical HAL based on the CMUX channel registered for the notification.
   4. The logical HAL dispatches the decoded notification data to the corresponding core object that registered for the notification.
   5. The core object processes the received notification data and dispatches to the server.
   6. The server dispatches the notification data to corresponding communicator.
   7. The communicator sends the notification data to TAPI, which communicates the same to the application.


# Application[[edit](https://wiki.tizen.org/index.php?title=Tizen_3.0_Porting_Guide&action=edit&section=30)]

Tizen supports both core and reference [applications](https://wiki.tizen.org/Applications). The core applications are developed with platform internal interfaces, such as Enlightenment Foundation Libraries ([EFL](https://wiki.tizen.org/EFL)) and other 3rd party libraries. The reference applications are developed with Tizen native APIs.

The following table shows whether the core and reference versions of the preloaded sample applications are supported by default on the [Emulator](https://wiki.tizen.org/Emulator) and target device.

| Application name | Emulator              | Target           |                       |      |
| ---------------- | --------------------- | ---------------- | --------------------- | ---- |
| Core application | Reference application | Core application | Reference application |      |
| Calculator       | No                    | Yes              | Yes                   | No   |
| Calendar         | No                    | Yes              | Yes                   | No   |
| CalendarService  | No                    | Yes              | Yes                   | No   |
| Camera           | No                    | Yes              | Yes                   | No   |
| Clock            | No                    | Yes              | Yes                   | No   |
| Contacts         | No                    | Yes              | Yes                   | No   |
| Email            | No                    | Yes              | Yes                   | No   |
| Gallery          | No                    | Yes              | Yes                   | No   |
| Home             | Yes                   | No               | Yes                   | No   |
| ImageViewer      | No                    | Yes              | Yes                   | No   |
| Internet         | No                    | Yes              | No                    | Yes  |
| Lock             | Yes                   | No               | Yes                   | No   |
| Memo             | No                    | Yes              | Yes                   | No   |
| Messages         | No                    | Yes              | Yes                   | No   |
| MusicPlayer      | No                    | Yes              | Yes                   | No   |
| MyFiles          | No                    | Yes              | Yes                   | No   |
| Phone            | No                    | Yes              | Yes                   | No   |
| Settings         | No                    | Yes              | Yes                   | No   |
| VideoPlayer      | No                    | Yes              | Yes                   | No   |

## Configuration[[edit](https://wiki.tizen.org/index.php?title=Porting_Guide/Application&action=edit&section=T-1)]

You can switch a preloaded sample application between core and reference applications using the [MIC image creator](https://source.tizen.org/documentation/reference/mic-image-creator). To switch the application, remove the preloaded application package and add the new package image with the correct name. The following table shows the core and reference application image names of the preloaded sample applications.

| Application name | Core application            | Reference application  |
| ---------------- | --------------------------- | ---------------------- |
| Calculator       | `org.tizen.calculator`      | `apps.Calculator`      |
| Calendar         | `org.tizen.calendar`        | `apps.Calendar`        |
| CalendarService  | `org.tizencalendar-service` | `apps.CalendarService` |
| Camera           | `org.tizen.camera-app`      | `apps.Camera`          |
| Clock            | `org.tizen.clock`           | `apps.Clock`           |
| Contacts         | `org.tizen.contacts`        | `apps.Contacts`        |
| Email            | `org.tizen.email`           | `apps.Email`           |
| Gallery          | `org.tizen.gallery`         | `apps.Gallery`         |
| Home             | `org.tizen.menu-screen`     | `apps.Home`            |
| ImageViewer      | `org.tizen.image-viewer`    | `apps.ImageViewer`     |
| Internet         | `org.tizen.browser`         | `apps.Internet`        |
| Lock             | `org.tizen.lockscreen`      | `apps.Lock`            |
| Memo             | `org.tizen.memo`            | `apps.Memo`            |
| Messages         | `org.tizen.message`         | `apps.Messages`        |
| MusicPlayer      | `org.tizen.music-player`    | `apps.MusicPlayer`     |
| MyFiles          | `org.tizen.myfile`          | `apps.MyFiles`         |
| Phone            | `org.tizen.call`            | `apps.Phone`           |
| Settings         | `org.tizen.setting`         | `apps.Settings`        |
| VideoPlayer      | `org.tizen.video-player`    | `apps.VideoPlayer`     |

# Appendix[[edit](https://wiki.tizen.org/index.php?title=Tizen_3.0_Porting_Guide&action=edit&section=31)]

## NFC OAL API[[edit](https://wiki.tizen.org/index.php?title=Porting_Guide/Appendix&action=edit&section=T-1)]

| Function                                 | Description                              | Parameter                                |
| ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| `net_nfc_oem_controller_init init;`      | Initializes the NFC chip.                | `net_nfc_error_e`: Returns an error code on failure. |
| `net_nfc_oem_controller_deinit deinit;`  | Deinitializes the NFC chip.              | None                                     |
| `net_nfc_oem_controller_register_listener register_listener;` | Registers a callback function for a tag event, SE event, and llcp event. | `target_detection_listener_cb target_detection_listener`: The tag event callback function`se_transaction_listener_cb se_transaction_listener`: The SE event callback function`llcp_event_listener_cb llcp_event_listener`: The llcp event callback function`net_nfc_error_e`: Returns an error code on failure. |
| `net_nfc_oem_controller_unregister_listener unregister_listener;` | Releases a callback function for a tag event, SE event, and llcp event. | None                                     |
| `net_nfc_oem_controller_check_firmware_version check_firmware_version;` | Checks the firmware version of the NFC chip. | `net_nfc_error_e`: Returns an error code on failure. |
| `net_nfc_oem_controller_update_firmware update_firmware;` | Updates the NFC chip firmware.           | `net_nfc_error_e`: Returns an error code on failure. |
| `net_nfc_oem_controller_get_stack_information get_stack_information;` | Gets the list of supported tags and the current firmware version. | `net_nfc_stack_information_s`: Pointer value to get the information of support tags and the current firmware version`net_nfc_error_e`: Returns an error code on failure. |
| `net_nfc_oem_controller_configure_discovery configure_discovery;` | Delivers the config information on discovery. | `net_nfc_discovery_mode_e`: The start/stop mode`net_nfc_event_filter_e config`: The information for tag filtering`net_nfc_error_e`: Returns an error code on failure. |
| `net_nfc_oem_controller_get_secure_element_list get_secure_element_list;` | Gets the information of the current secure element. | `net_nfc_secure_element_info_s`: The pointer value to get secure element information`int`: The pointer value to get the count of the secure element`net_nfc_error_e`: Returns an error code on failure. |
| `net_nfc_oem_controller_set_secure_element_mode set_secure_element_mode;` | Sets the secure element to use.          | `net_nfc_secure_element_type_e`: Secure element information`net_nfc_secure_element_mode_e`: The mode information to set`net_nfc_error_e`: Returns an error code on failure. |
| `net_nfc_oem_controller_connect connect;` | Connects to the detected tag/target.     | `net_nfc_target_handle_s`: The tag/target handle for connecting`net_nfc_error_e`: Returns an error code on failure. |
| `net_nfc_oem_controller_connect disconnect;` | Disconnects the connected tag/target.    | `net_nfc_target_handle_s`: The tag/target handle for disconnecting`net_nfc_error_e`: Returns an error code on failure. |
| `net_nfc_oem_controller_check_ndef check_ndef;` | Checks the tag to for ndef support.      | `net_nfc_target_handle_s`: The tag handle to check ndef`int`: The max size supported in the tag`int`: The real data size saved in the tag`net_nfc_error_e`: Returns an error code on failure. |
| `net_nfc_oem_controller_check_target_presence check_presence;` | Checks if a tag exist in the RF range.   | `net_nfc_target_handle_s`: The tag handle to check presence`net_nfc_error_e`: Returns an error code on failure. |
| `net_nfc_oem_controller_read_ndef read_ndef;` | Reads ndef data in a tag.                | `net_nfc_target_handle_s`: The tag handle to read`data_s`: The pointer value to save the ndef data`net_nfc_error_e`: Returns an error code on failure. |
| `net_nfc_oem_controller_write_ndef write_ndef;` | Writes the data to the tag.              | `net_nfc_target_handle_s`: The handle to write`data_s`: The data to write`net_nfc_error_e`: Returns an error code on failure. |
| `net_nfc_oem_controller_make_read_only_ndef make_read_only_ndef;` | Makes the tag to a read only tag.        | `net_nfc_target_handle_s`: The target tag handle`net_nfc_error_e`: Returns an error code on failure. |
| `net_nfc_oem_controller_transceive transceive;` | Sends and receives the low command to the tag or target. | `net_nfc_target_handle_s`: The tag or target handle to transceive`net_nfc_transceive_info_s`: The pointer value included command or data to send and data to receive`data_s`: The pointer value to send the information of context`net_nfc_error_e`: Returns an error code on failure. |
| `net_nfc_oem_controller_format_ndef format_ndef;` | Formats the tag.                         | `net_nfc_target_handle_s`: The tag handle to format`data_s`: The key value to send the tag for formatting`net_nfc_error_e`: Returns an error code on failure. |
| `net_nfc_oem_controller_exception_handler exception_handler;` | When the `nfc-manager` faces an unwanted exception, it tries to deinitialize and initialize the stack before unregistering and registering the callback function. | None                                     |
| `net_nfc_oem_controller_is_ready is_ready;` | Checks the status of the NFC stack.      | `net_nfc_error_e`: Returns an error code on failure. |
| `net_nfc_oem_controller_llcp_config config_llcp;` | Sets the llcp configuration (miu, lto, wks, option). | `net_nfc_target_handle_s`: The target handle to set llcp`net_nfc_error_e`: Returns an error code on failure. |
| `net_nfc_oem_controller_llcp_check_llcp check_llcp_status;` | Checks the llcp configuration (miu, lto, wks, option). | `net_nfc_target_handle_s`: The target handle to check llcp`net_nfc_error_e`: Returns an error code on failure. |
| `net_nfc_oem_controller_llcp_activate_llcp activate_llcp;` | Activates the llcp functionality.        | `net_nfc_target_handle_s`: The target handle to activate`net_nfc_error_e`: Returns an error code on failure. |
| `net_nfc_oem_controller_llcp_create_socket create_llcp_socket;` | Creates the llcp socket                  | `net_nfc_llcp_socket_t`: The pointer value to receive the socket information`net_nfc_socket_type_e socketType`: The type of socket to create`uint16_t miu`: The miu value`uint8_t rw`: The rw value`net_nfc_error_e`: Returns an error code on failure.`void`: The value to control the context (can be set to `NULL`) |
| `net_nfc_oem_controller_llcp_bind bind_llcp_socket;` | Binds the socket.                        | `net_nfc_llcp_socket_t socket`: The information about the socket to bind`uint8_t service_access_point`: The information of access point to bind`net_nfc_error_e`: Returns an error code on failure. |
| `net_nfc_oem_controller_llcp_listen listen_llcp_socket;` | Sets the socket to listen.               | `net_nfc_target_handle_s`: The target handle`uint8_t`: The service name to listen`net_nfc_llcp_socket_t socket`: Socket information`net_nfc_error_e`: Returns an error code on failure.`void`: The value to control the context (can be set to `NULL`) |
| `net_nfc_oem_controller_llcp_accept accept_llcp_socket;` | Accepts the connect request in listening status. | `net_nfc_llcp_socket_t socket`: Socket information to accept`net_nfc_error_e`: Returns an error code on failure. |
| `net_nfc_oem_controller_llcp_connect_by_url connect_llcp_by_url;` | Connects the server with the service name. | `net_nfc_target_handle_s`: The handle of the target to connect`net_nfc_llcp_socket_t socket`: Socket information`uint8_t`: Service name to connect`net_nfc_error_e`: Returns an error code on failure.`void`: The value to control the context (can be set to `NULL`) |
| `net_nfc_oem_controller_llcp_connect connect_llcp;` | Connects to the server with access point (port number). | `net_nfc_target_handle_s`: The target handle`net_nfc_llcp_socket_t socket`: Socket information`uint8_t service_access_point`: Access point number`net_nfc_error_e`: Returns an error code on failure.`void`: The value to control the context (can be set to `NULL`) |
| `net_nfc_oem_controller_llcp_disconnect disconnect_llcp;` | Disconnects the llcp link.               | `net_nfc_target_handle_s`: Socket information to disconnect`net_nfc_llcp_socket_t socket`: The information of the socket to disconnect`net_nfc_error_e`: Returns an error code on failure.`void`: The value to control the context (can be set to `NULL`) |
| `net_nfc_oem_controller_llcp_socket_close close_llcp_socket;` | Closes the llcp socket.                  | `net_nfc_llcp_socket_t socket`: Socket information to close`net_nfc_error_e`: Returns an error code on failure. |
| `net_nfc_oem_controller_llcp_recv recv_llcp;` | Receives the data using the llcp link.   | `net_nfc_target_handle_s`: The target handle to receive`net_nfc_llcp_socket_t socket`: Socket information to receive`data_s`: The pointer value to receive the data`net_nfc_error_e`: Returns an error code on failure.`void`: The value to control the context (can be set to `NULL`) |
| `net_nfc_oem_controller_llcp_send send_llcp;` | Sends the data using llcp link.          | `net_nfc_target_handle_s`: The target handle to send`net_nfc_llcp_socket_t socket`: Socket information to send`data_s`: The data to send`net_nfc_error_e`: Returns an error code on failure.`void`: The value to control the context (can be set to `NULL`) |
| `net_nfc_oem_controller_llcp_recv_from recv_from_llcp;` | Rejects the connect request from the client socket. | `net_nfc_target_handle_s`: The target handle to reject`net_nfc_llcp_socket_t socket`: The socket information to reject`net_nfc_error_e`: Returns an error code on failure. |
| `net_nfc_oem_controller_llcp_send_to send_to_llcp;` | Sends the data using the service access point. | `net_nfc_target_handle_s`: The peer target handle`net_nfc_llcp_socket_t socket`: The socket information`data_s`: The data to send`uint8_t service_access_point`: The service access point to send`net_nfc_error_e`: Returns an error code on failure.`void`: The value to control the context (can be set to `NULL`) |
| `net_nfc_oem_controller_llcp_reject reject_llcp;` | Rejects the connect request from the client socket. | `net_nfc_target_handle_s`: The target handle to reject`net_nfc_llcp_socket_t socket`: The socket information to reject`net_nfc_error_e`: Returns an error code on failure. |
| `net_nfc_oem_controller_llcp_get_remote_config get_remote_config;` | Gets te llcp socket config information of the peer device. | `net_nfc_target_handle_s`: The peer target handle`net_nfc_llcp_config_info_s`: The pointer value to get config information of peer device's llcp socket`net_nfc_error_e`: Returns an error code on failure. |
| `net_nfc_oem_controller_llcp_get_remote_socket_info get_remote_socket_info;` | Gets the llcp socket information of the peer device. | `net_nfc_target_handle_s`: The peer target handle`net_nfc_llcp_socket_t socket`: The llcp socket information`net_nfc_llcp_socket_option_s`: The pointer value to save the information of remote socket`net_nfc_error_e`: Returns an error code on failure. |
| `net_nfc_oem_controller_sim_test sim_test;` | Tests the SWP link with SIM and NFC chipset. | `net_nfc_error_e`: Returns an error code on failure. |
| `net_nfc_oem_controller_test_mode_on test_mode_on;` | Changes the NFC chip to test mode. (Test mode exists only in the NXP case. If there are none, it does not need to implemented.) | `net_nfc_error_e`: Returns an error code on failure. |
| `net_nfc_oem_controller_test_mode_off test_mode_off;` | Changes the status of the NFC chip from test mode to normal mode. (Test mode exists only in the NXP case. If there are none, it does not need to implemented.) | `net_nfc_error_e`: Returns an error code on failure. |
| `net_nfc_oem_controller_support_nfc support_nfc` | Checks each the device file of each chip. | If the device file is not found, the function returns `NET_NFC_NOT_SUPPORTED`. |