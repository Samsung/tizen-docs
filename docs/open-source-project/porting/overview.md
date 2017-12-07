# Overview

Tizen is an open-source software stack created for a wide array of devices with different form factors. The primary purposes of Tizen are to create an open software platform available for carriers, OEMs, and developers to make their innovative ideas a reality and to introduce a successful, real-world product that improves the mobile experience for users.

It is also important that is no central point of failure, where 1 industry player can restrict or control the innovations of any other. The result is a full, production-quality consumer product with source code open for customization and porting.

The intent of the porting guides is to provide information and instructions to boot Tizen on new hardware and create products based on the Tizen OS. The Tizen porting guides take you through the porting process by elaborating the Tizen architecture, the necessary tools, and the development environment setup, as well as creating a Tizen image and demonstrating the modifications needed across various functional areas.

## Tizen Architecture

The following figure illustrates the Tizen architecture for smart phone and tablet devices.

**Figure: Tizen architecture**

![Tizen architecture](media/what-is-tizen-architecture.png)

For more information on the Tizen framework layer, see the [Tizen Application Types](https://developer.tizen.org/development/getting-started/overview#type).

## Core Layer

The core layer consists of various subsystems:

- **Application framework**  
The Application framework provides application management, including launching other applications using the package name, URI, or MIME type. It also launches predefined services, such as the system dialer application. The Application framework also notifies applications of common events, such as low memory events, low battery, changes in screen orientation, and push notifications.
- **Base**  
Base contains GNU/[Linux](https://wiki.tizen.org/Linux)-based essential system libraries that provide key features, such as database support, internationalization, and XML parsing.
- **Connectivity**  
Connectivity consists of all network and connectivity related functionalities, such as 3G, Wi-Fi, Bluetooth, HTTP, and NFC (Near Field Communication). Data network is based on ConnMan (Connection manager), which provides 3G and Wi-Fi based network connection management.
- **Graphics and UI**  
Graphics and UI consist of the system graphic and UI stacks, which include EFL (Enlightenment Foundation Libraries), window management system (x11 for Tizen 2.x / Wayland for Tizen 3.0), input methods, and OpenGL&reg; ES APIs.

  EFL, the heart of the graphics component, is a suite of libraries. EFL is used to create rich graphics with ease, for all UI resolutions. The libraries build UIs in layers, allowing for 3D transformations and more. EFL includes the Evas canvas API library and the elementary widget library.

  WebKit-based graphics are provided as well, capable of running within a full browser UI or a dedicated Web runtime environment (without a browser window), all based on Tizen's own HTML5 canvas WebKitEFL implementation. Additionally, WebGL&trade; is supported and Web-based frameworks for UI, such as jQuery Mobile, are also offered, which help with porting existing jQuery code.
- **Location**  
Location provides location-based services (LBS), including position information, geocoding, satellite information, and GPS status. It delivers location information from various positioning sources, such as GPS, WPS (Wi-Fi Positioning System), Cell ID, and sensors.
- **Messaging**  
Messaging consists of Message and Email. The Message supports SMS, MMS, and cell broadcast messages. Email supports protocols, such as SMTP, IMAP, and POP3.
- **Multimedia**  
Multimedia is based on GStreamer. It provides support for media, including video, audio, imaging, and VoIP. It also provides media content management for managing media file metadata information.
- **PIM (Personal Information Management)**  
PIM enables managing user data on the device, including managing calendar, contacts, tasks, and retrieving data about the device context (such as device position and cable status).
- **Security**  
Security is responsible for security deployment across the system. It consists of the platform security enablers, such as access control, certificate management, and secure application distribution.

  For more information, see [Security/Tizen 3.0 security porting guide](https://wiki.tizen.org/wiki/Security/Tizen_3.0_security_porting_guide) and [All 3.X security pages](https://wiki.tizen.org/wiki/Security#All_3.X_security_pages).
- **System**  
System consists of service (process), device, and resource management features, including:
  - Interfaces for accessing devices, such as sensors, display, or vibrator
  - Power management, such as LCD display backlight dimming/off and application processor sleep
  - Monitoring devices and handling events, such as USB, MMC, charger, and earjack events
  - Resource management, such as CPU quota control and low memory management
  - Service management, such as watchdog management and capability control
- **Telephony**  
Telephony consists of cellular functionalities communicating with the modem:
  - Provides call services (single call and multiparty call).
  - Provides call-related and non-call-related supplementary services (call waiting, barring, and forwarding and USSD).
  - Supports GSM, UMTS, LTE, and CDMA network services.
  - Provides packet services and network status information.
  - Provides SMS-related services.
  - Provides SIM card functionalities (SIM phonebook, SIM EF files, SIM Application Toolkit support)
- **Web**  
Web provides a complete implementation of the Tizen Web API optimized for low-power devices. It includes WebKit, which is a layout engine designed to allow Web browsers to render Web pages. It also provides Web runtime for Web applications.
