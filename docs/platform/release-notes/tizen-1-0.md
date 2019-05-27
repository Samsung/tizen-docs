# Tizen 1.0 Release Notes

Release Date: Apr. 30, 2012

Version: **1.0 Larkspur**



This document details the new features in the Tizen 1.0 Larkspur release and provides a summary of the main components of the platform.

This release provides a solid baseline for device vendors and developers to start creating software for mobile devices. The Tizen 1.0 Larkspur Core OS provides a complete set of enabling technologies for mobile computing. It is specifically designed for productizing smart phones and tablet devices.

**UPDATE: Tizen OS development with RPM/OBS (Aug. 6, 2012) **

This first release since the initial Larkspur release comes with major changes in many areas, notably the completed migration from Debian to rpm based packaging and a new way of how packages and sources are maintained. For Tizen developers GIT becomes the focal point and the only reference for sources and packaging data. Developers now are provided with new tools to interact with both the source management system (git) and the build system (OBS) in an efficient way and easy way.

The complete development process leverages state of the art open–source source management, review and continuous integration tools to accelerate development and high quality releases.

## Changes since the beta release

This release focused on stability and performance improvements. In addition, the following new features have been added:

### Web

- W3C/HTML5 specifications support
- WebRTC getUserMedia() API to access local camera

### Location

- POI (Points of Interest) support
- Structured queries for location with category, name, and location
- Unstructured queries for location
- Route search feature support
- Multiple transportation mode (car, pedestrian)
- Route customization (shortest, fastest, areas to avoid)

### Connectivity

- Wi-Fi Direct key features enhancement
- Activation/deactivation
- Device discovery
- Peer to Peer connection with Wi-Fi Direct device
- Group owner election

## Features

Below is a summary of the features provided by the components of the Tizen platform.

### Application framework

Provides the functionality for launching a Tizen application and managing its lifecycle and information. Main features include:

- Application lifecycle management using Appcore
- Quick launching mode using pre-loading and pre-initialization
- Application information management
- Application integrity verification with hash value comparison
- Package management
- i18n/l10n based on GNU gettext and libICU
- Two types of IPC mechanism support:
- DBUS
- Simple publish/subscribe notification

### Graphics & UI

Consists of the following major components:

- Window System
- Graphics
- Enlightenment Foundation Library (EFL)
- Input Service Framework (ISF)

Features include:

- Window system based on the X11 open source project
- Direct Rendering Infrastructure (DRI) support: DRI2 protocol 2.6 and libdrm 2.4.29
- XGestureExtension support
- Composite window manager based on EFL open source project
- 3D graphics
- Supports OpenGL ES 1.1 and 2.0
- Supports EGL 1.4
- 2D graphics
- 2D vector graphics based on the Cairo open source project
- Widget toolkit
- Supports both desktop PCs and multi-touch-screens, using the same widgets
- Scalable widgets based on scale factors
- Change scale factor based on screen size and resolution
- Animation support based on the EFL open source project
- Dynamic backend support
- Software backend (X11) and H/W acceleration backend (OpenGL ES)
- Video/image composition support
- Input Service Framework based on scim 1.4.7 (open source)
- Automatically shows or hides the virtual keyboard when entry gets or loses focus
- Switches virtual keyboard mode
- Supports Keyboard Engine for soft-keyboard
- Supports a variety of interfaces between applications and the engine
- Supports loading 3rd party IMEs
- Keyboard engine for supporting hardware-based keyboards, such as a Bluetooth Keyboard

### Multimedia

Provides features for playing and manipulating of video, audio, images, and VoIP. It also provides content management for media file metadata. Its features include:

- Multimedia framework based on the GStreamer open source project
- Player
- Local playback: Various file formats/DRM (PlayReady, OMA, DivX DRM)/A2DP/Subtitle(SRT,SMI,SUB)
- Streaming playback: HTTP Streaming, HLS (HTTP Live Streaming), RTP/RTSP Streaming, progressive download (File/URI)
- Camera preview/Capture/Camera Setting, Recording
- Capture (multi, timer, frame, mosaic, panorama)
- Video/Audio recording support
- Audio recording support
- Sound path control, audio I/O, WAV player, tone player support
- Audio playback using simple API (supports only uncompressed WAV files)
- Playback or capture PCM with a given memory buffer
- OpenAL playback function support
- Extracting media property information and metadata from media content (ID3Tag, Thumbnail, Exif etc)
- Radio operation support
- Software mixing of multiple audio streams based on PulseAudio open source project
- Various codec support
- Audio decoder: AAC, MP3, WMA 7/8, WAV, Vorbis, AMR-NB / AMR-WB
- Audio encoder: Vorbis, AMR-NB
- Video decoder: MPEG-1, MPEG-4, H.263, H.264, On2 VP3, Theora
- Video encoder: MPEG-4 part 2, H.263
- Various container format support
- MP4, 3GP, AVI, WM 7/8, ASF, MKV, MPG, MP3, AAC, AMR, AC3, WMA, OGG, WAV, IMY, RMF, MMF, XMF, MID
- OpenMAX IL Support

### Web

Provides a complete implementation of the Tizen Web API optimized for mobile devices. It includes WebKit, a layout engine designed to enable web browsers to render web pages. It also provides a runtime for web applications. Its features include:

- W3C/HTML5 specifications support
- Content: HTML5 audio/video element, HTML5 Forms (Partial), Session History API, DOM/JS related HTML5 Enhancements, iframe sandbox attribute, HTML5 2D Canvas, Inline SVG
- CSS3: CSS3 2D Transforms (H/W Accelerated), CSS3 3D Transforms (H/W Accelerated), CSS3 Animations (H/W Accelerated), CSS3 Transitions (H/W Accelerated), CSS3 Colors, CSS3 Backgrounds and Borders (Partial), CSS3 Flexible Box Layout (Partial), CSS3 Multicolumn Layout (Partial), CSS3 Text Effects (Partial), CSS3 User Interface (Partial), Downloadable Fonts, WOFF 1.0
- Device / OS Integration: Touch Events, CSS3 Media Queries (Partial), Geolocation API, Orientation and Acceleration (Partial), Browser online state, Vibration API, HTML Media Capture (using the input tag), getUserMedia API, Battery Status, Network Info API, Web Notifications, Sensors.
- Network and Communication: WebSocket API, Web Messaging, XMLHttpRequest Level 2, Cross-Origin Resource Sharing (CORS), Server-Sent Events
- Storage: Web Storage, File Reader API, File Writer API, File System API, HTML5 Application Cache, Web SQL Database, Indexed DB API
- Performance: Web Worker (Partial), Page visibility API
- Non-W3C Specifications
- Khronos specifications support : WebGL, Typed Arrays
- Fullscreen API (Mozilla Spec)(Partial), Viewport Metatag (Apple Spec), JSON parsing/stringfy (JSON.org Spec), URI scheme (tel:, sms:, mmsto:, mailto:)(OMA Spec)
- Legacy Web Standards support
- HTTP 1.1 Protocol, DOM Level 2 Views, HTML 4.01 Strict, DOM Level 2 Traversal, DOM Level 2 Range, MIME Part 1 and Part 2, object tag handling and HTTP status codes, DOM Level 2 Core, DOM Level 2 Events, CSS2.1 Selectors, DOM Level 2 Style, DOM Level 2 HTML, Unicode 5.0 UTF-16/UTF-8, HTML 4.0 Transitional, SVG 1.1, SMIL 2.1, SVG 1.1 Fonts, Data URI scheme, ECMAScript (3rd edition) Conformance, XHTML 1.0 Strict
- W3C Widget specifications support
- Packaging and Configuration, Widget Access Request Policy, Digital Signing, Widget Interface, URI scheme
- Tizen Device APIs to access to a device’s platform capabilities support
- Tizen, Alarm, Application, Bluetooth, Calendar, Call, Contact, Filesystem, Geocoder, Media Content, Messaging, NFC, System Information, Time
- Web UI service support based on JQuery Mobile 1.0
- Rich and optimized Tizen widgets
- Tizen UI theme support
- Localization support
- Web application templates

### Messaging

Provides the functionality to send & receive SMS, MMS, and email messages.

- Support SMS, WAP push message and cell broadcast messages.
- Support OMA MMS 1.2.
- Support Email protocols
- SMTP (Simple Mail Transfer Protocol, RFC2821)
- IMAP4 (Internet Message Access Protocol, RFC2060)
- POP3 (Post Office Protocol, RFC2449)

### Location

Provides Location Based Services (LBS), including position information, geocoding, satellite information, and GPS status. It is based on GeoClue, which delivers location information from various positioning sources such as GPS, WPS (Wi-Fi Positioning System), Cell ID, and sensors.
Features include:

- Locating current position, velocity, and distance support
- Last known position, velocity, satellite support
- Satellite information of GPS and GLONASS support
- Notification when a user enters or exits a predefined set of boundaries, like school attendance zone or neighborhood boundary

Map service delivers advanced maps features and functionalities:

- Geocoding and reverse geocoding support
- POI (Point of Interest) support
- Route search feature support

### Security

Responsible for security deployment across the system. It consists of platform security enablers, such as access control, certificate management, and secure application distribution. Its features include:

- Certificate management and cert/signature verification
- Secure storage for confidential data
- User space access control management
- Cryptography and SSL support, based on OpenSSL open source project

### System

Consists of the following system and device management features:

- Monitoring the system status and communicating it to applications
- OOM (Out Of Memory) status, Process status, Battery Status
- Controlling the LCD power state
- LCD on / dimming / off
- Monitoring the devices status and communicating it to applications
- JACK / POWERSUPPLY / BACKLIGHT / LCD / LED / TOUCHKEY
- Providing APIs that handle the various sensor devices
- Accelerometer / Geomagnetic / Gyroscope / Light / Proximity / Motion

### Base

Contains Linux based essential system libraries that provide key features, such as database support, internationalization, and XML parsing. Base consists of pure open source projects, such as SQLite, Glibc, Glib, LibXML, LibICU, and so on.

### Connectivity

Consists of all network and connectivity related functionalities, such as 3G, Wi-Fi, Bluetooth, HTTP, and NFC (Near Field Communication). Data network is based on the ConnMan open source project, which provides 3G and Wi-Fi based network connection management. The connectivity features include:

- Always-on connectivity which tries to keep connecting cellular or Wi-Fi network, preferring Wi-Fi network connection
- Auto-connecting Wi-Fi access point which has been already remembered
- Exponentially increasing and back-off Wi-Fi scan interval which minimizes Wi-Fi power consumption
- Wi-Fi Direct support
- DNS proxy scheme support
- Extension on WiFi API Information
- bssid, max data rate, channel frequency, encryption mode
- bluez 4.98 version upgrade release, and obexd 0.44 initial release included
- Bluetooth OOB pairing

### Telephony

Provides cellular and VoIP call functionality. It supports the following:

- UMTS/CDMA call, ALS, MPTY, AoC
- UMTS Supplementary Service such as USSD, CLI, CF, CW, CH, Call Barring
- UMTS PDP for IPv4 and IPv6, CDMA PPP
- UMTS/CDMA SMS, Cell Broadcast
- UMTS/GSM SIM manipulation, SIM security, Personalization
- UMTS/GSM SAT command management
- NITZ support, RSSI display
- SIM authentication extension on IMS, GSM, and UMTS

### PIM (Personal Information Management)

Enables the management of user data on the device, including calendar, contacts, and tasks. It also supports retrieving data about the device context, such as device position or cable status.
It supports the following:

- CRUD (Create, Read, Update, Delete) operations for PIMS data – contacts, calendar, task.
- vCard 3.0
- vCalendar 1.0

### Kernel

The Tizen reference kernel is based on the Linux kernel.