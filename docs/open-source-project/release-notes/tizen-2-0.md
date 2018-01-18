# Tizen 2.0

Release Date: 18 Feb, 2013



The Tizen 2.0 release provides developers with the Tizen kernel, device drivers, middleware subsystems, and Web/Native APIs, necessary to develop future Tizen compliant solutions.

## Release Details

- [Getting binaries and images](http://download.tizen.org/releases/2.0/tizen-2.0_20130219.4/)
- [Detailed application information](https://wiki.tizen.org/wiki/Porting_Guide#Application)

## Release Notes

Tizen is an open source, standards-based software platform supported by leading mobile operators, device manufacturers, and chip suppliers for multiple device categories, including smartphones, tablets, netbooks, in-vehicle infotainment devices, and smart TVs.

The Tizen Platform consists of the web framework (APIs), native framework (APIs), and core system.

The Tizen Software Development Kit (SDK) is a comprehensive set of tools for developing Web applications, native applications, and the platform component for Tizen. The SDK contains an install manager, IDE, tools, documents, samples, and a platform image.

# Tizen Platform

## Web Framework

### New Features

- HTML5 / W3C
  - Device
    - The Network Information API
      - This API provides an interface for Web applications to access the underlying connection information of the device.
  - Media
    - Web Audio API (Partial)
      - This high-level JavaScript API is used to process and synthesize audio in Web applications.
    - HTML Media Capture
      - This HTML form extension enables users to access a device's media capture mechanism, such as a camera or microphone, from a file upload control.
  - UI
    - Clipboard API and events
      - This API is used in clipboard operations such as copy, cut, and paste in Web applications.
    - HTML Drag and drop
      - This event-based drag-and-drop mechanism is defined in the HTML5 specification.
- Web Runtime
  - External storage installation capability for Web applications
  - New configuration extension:
    - <tizen:privilege>: This tag is used to specify API permissions. (The <feature> tag is now be used to specify the required platform or hardware features.)
  - NPRuntime plug-in support in Web applications:
    - In the 2.0 release, only the 3rd party libraries supported as public APIs, such as eglibc, can be used in NPRuntime plug-ins.

### Changed Features

- For Tizen Web API change details, see [Tizen API Change Notes](http://developer.tizen.org/downloads/sdk/2.0-api-change-notes).

- HTML5/W3C

  - Reference documentation divided into separate documents in accordance with specification documents:

    - HTML5 2D Canvas to HTML5 2D Canvas element and HTML Canvas 2D Context

  - Specification returned in this release:

    - Vibration API
      - This API provides access to the vibration mechanism of the hosting device.

  - Specification version update:

    *Note*: If you have developed Web applications based on the Tizen 2.0 alpha version of the following specifications, you MUST check whether the corresponding features are available in the updated version of the specifications referred to in this release.

    - Dom, forms, and styles
      - Selectors API Level 1
      - CSS3 Backgrounds and Borders Module Level 3
      - CSS3 Flexible Box Layout Module
      - CSS Text Module Level 3 (Partial)
      - CSS3 Basic User Interface Module Level 3 (CSS3 UI)
      - CSS Fonts Module Level 3 (Partial)
      - WOFF File Format 1.0
      - CSS3 Media Queries (Partial)
    - Device
      - DeviceOrientation Event Specification (Partial)
      - Battery Status API
      - HTML5 Browser State
      - The Screen Orientation API
    - Graphics
      - HTML5 Canvas Element
      - HTML Canvas 2D Context
    - Communication
      - The WebSocket API
      - HTML5 Web Messaging
    - Security
      - Cross-Origin Resource Sharing
    - Performance and optimization
      - Web Workers (partial)
      - Page Visibility
    - Location
      - Geolocation API Specification

- Web Runtime

  - The partially supported W3C Widget URI scheme (to be replaced by a new URI scheme in the 2.1 release) has been depracated.

- Web UI Framework

  - jQuery and jQuery Mobile (jQM) versions are upgraded to jQuery 1.8.2 and jQM 1.2.0.
  - Theme
    - The "tizen-black" theme has been removed.
    - The "tizen-white" theme has been changed to a new UX style.
  - Widget
    - The automatic footer generation feature has been removed. (<div data-role="footer"/;> needs to be specified.)
    - The optionheader, nocontents, controlgroup, pagecontrol, colorselector, dayselector widgets are removed.
    - The image slider widget has been renamed as "gallery".
    - The shortcut scroll widget has been renamed as "fast scroll".
    - The swipe list widget has been refactored to a new style.
    - The control bar widget has been refactored to "tab bar".
    - The multi-button entry widget has been refactored to "token text area".
    - The context popup has been replaced with "popup" as in jQM 1.2.0.
    - The toggle switch has been replaced with "flip toggle switch" as in jQM 1.2.0.
    - The popup has been replaced with "popup with data-position-to='window' attribute" as in jQM 1.2.0.
    - The expandable list has been replaced with "collapsible list" as in jQM 1.2.0.
    - The auto divider has been replaced with "auto-divider" as in jQM 1.2.0.
    - The search bar supports additional data-* attributes.
  - Viewport meta tag
    - The "data-framework-viewport-scale" attribute of the web-ui-fw script tag has been changed to "data-frame-viewport-width = 'device-width' | 'screen-width' | '[number]'".

- Tizen Web APIs

  - Privilege
    - The feature for API access has been replaced with "privilege". The changed names are included in the API specification.
  - WebAPIException
    - The WebAPIException interface is used by APIs to throw errors synchronously. The WebAPIError interface is only used for asynchronous error handling.
  - ApplicationControl
    - The ApplicationService interface has been renamed as ApplicationControl. Therefore, any APIs using ApplicationControl, such as Alarm, Application, and Notification, also have been changed.
  - Account
    - Placeholders have been deleted.
  - Location-based services
    - LBS and Geocoder APIs have been deleted.
  - Application
    - This API has been recategorized according to usage.
    - The kill() method is no longer public.
  - Call history
    - The call history functionality is separated from the Call API.
    - The Call API has been deleted.
  - Download
    - A number of helper APIs has been added.
  - Power
    - This API has been refactored for better usability.
  - Contact
    - The "person" concept that is used to group a number of contacts has been added.
  - Content
    - The Media Content API has been refactored to Content to cover non-media content.
  - System information
    - A functionality to retrieve device capabilities has been added.
    - The SystemInfoPower property has been renamed as SystemInfoBattery.
    - The SystemInfoBuild property has been added.
    - The SystemInfoDevice property has been deleted.
    - The SystemInfoEthernetNetwork property has been deleted.
  - System setting
    - Setting system-wide values has been enabled.
  - Unsupported APIs, attributes, and parameters have been deleted.

- ### Known Issues

- - W3C / HTML5
    - Touch events
      - If you touch and hold on the screen, an abnormal touch cancel event occurs.
  - Web UI Framework
    - The screen blinks if either transit pages or a pop-up window uses Web UI framework.

## Native Framework

The Tizen native framework is newly supported in this version.

### New Features

- Tizen::App
  - Application model
    - This feature provides:
      - UI application model
      - Background execution model without a graphical user interface
  - AppControl and DataControl
    - These features provide:
      - Implicit application control resolution
      - Certificate manager application control
      - Framework to access specific data exported by other applications and to share application data
  - Application management
    - This feature provides:
      - Multitasking in the application
      - Service type applications
      - Active application changing event
  - AppSetting
    - This feature allows you to design your own setting menu with the IDE, and display and modify it in the system setting menu.
  - Package management
    - This feature provides installation and uninstallation management, and information of the installed packages.
- Tizen::Base
  - Basic types
    - This feature provides basic data types such as Object, Boolean, Buffer, BufferBase, ByteBuffer, Character, Short, Int8, Integer, Long, LongLong, Number, Double, Float, DoubleMatrix, FloatMatrix, String, TimeSpan, DateTime, and UuId.
  - Collections
    - This feature provides data collections such as ArrayList, HashMap, Collection, LinkedList, MultiHashMap, Queue, Stack, Comparers, and Enumerators.
  - Utility
    - This feature provides common utilities such as Inflator, Deflator, FileZipper, FileUnzipper, LinkInfo, Math, RegularExpression, StringTokenizer, StringUtil, Uri, and ZipEntry.
  - Runtime
    - This feature provides:
      - Worker threads and event-driven threads
      - Synchronization mechanisms: Mutex, Semaphore, and Monitor
      - RAII-style classes: MutexGuard, SemaphoreGuard, and MonitorGuard
  - Smart pointers
    - This feature provides:
      - Sole ownership management smart pointers: auto_ptr and unique_ptr
      - Reference-counted shared ownership management smart pointers: shared_ptr and weak_ptr
      - Custom deleter: unique_ptr and shared_ptr
      - Move semantic: unique_ptr (explicit move), auto_ptr (implicit move), and the std::move() method template
- Tizen::Content
  - Content manager
    - This feature provides:
      - Content information management, such as file attributes, metadata, and custom data
      - Searching content in a device
      - Playlists
      - Retrieving all content associated with a content directory
  - Download manager
    - This feature provides launching the download manager using HTTP.
- Tizen::Graphics
  - Graphics
    - This feature provides:
      - Platform-independent 2D graphics
      - Graphics rendering methods and data structures
      - Floating point matrix and vector classes
  - 3D graphics
    - This feature provides:
      - OpenGL ES 1.1 and 2.0, which are subsets of the OpenGL 3D graphics API designed for mobile devices.
      - GL utilities:
        - GLPlayer and IGlRenderer provide templates to increase OpenGL ES usability.
        - CanvasTexture provides a fast and convenient way to draw 2D primitives onto OpenGL ES Texture.
        - VideoTexture provides a fast and convenient way to play a video stream as OpenGL ES Texture.
      - Performance:
        - Provides a hardware acceleration mode, which accelerates applications using graphics hardware. When the HwAcceleration mode is enabled in the manifest.xml file, the GL surface rendering performance is also enhanced.
- Tizen::Io
  - File
    - This feature provides:
      - Basic file I/O operations
      - Retrieving the attributes of a file or directory
  - Directory
    - This feature provides:
      - Basic directory operations
      - Accessing the collection of a specific directory entry list
      - Retrieving information about each directory entry
  - Database
    - This feature provides:
      - Basic database management
      - Navigating the database result set
      - Manipulating SQL-compatible statements
  - File event manager
    - This feature provides monitoring individual files or directories.
  - Message port
    - This feature provides:
      - Sending messages to the message ports of another application
      - Receiving messages from other applications
      - Trusted communication (allowed only if both applications are signed with the same certificate)
  - Memory mapped file
    - This feature provides using a memory mapped file, which maps the data of a file to the virtual address space of an application.
  - Registry
    - This feature provides methods to access and manipulate registry files including key-value structured data set.
  - Serial port
    - This feature provides methods for communication between external device and Tizen device.
  - Secure I/O
    - This feature provides methods to encrypt or decrypt the file, database, and registry file.
- Tizen::Locales
  - Locale information
    - This feature provides management of the locale information specified by the combination of language and country codes (defined by ISO) if available in the system registry format.
  - Calendar data
    - This feature provides:
      - Converting the date, time, and calendar fields using the Gregorian calendar, which is used by most of the world
      - Managing time zone information with DST (Daylight Saving Time)
  - Formatting data
    - This feature provides formatting numbers, currencies, date, and time.
- Tizen::Media
  - Encoding and decoding
    - This feature provide the encoding and decoding of images, videos, and audio data.
  - Player and recorder
    - This feature provides:
      - Playing audio and video from media files stored on a device or streaming over the network
      - Playback of DTMF tones
      - Low-level audio playback and capturing
      - Audio and video recording
  - Camera
    - This feature provides a camera to display a live preview and capture a still image.
  - VideoFrameExtractor
    - This API provides video frame extraction in a media file.
- Tizen::Messaging
  - Message management
    - This feature provides:
      - Creating, sending, and receiving SMS messages
      - Searching SMS messages in the inbox, sentbox, outbox, or all message boxes
      - Creating, sending, and receiving MMS messages and email messages with attachments
      - Sending and receiving IP push messages
- Tizen::Net
  - Account management
    - This feature provides network account management.
  - Connection management
    - This feature provides:
      - Custom connection management service API
      - Selecting the preferred connection
  - Utility
    - This feature provides:
      - Internet protocol (IP) address that represents a network resource or service (only IPv4 is supported)
      - DNS utility retrieving information about a specific host from the Internet Domain Name System (DNS)
  - Socket
    - This feature provides:
      - BSD-type socket functionality
      - Secure sockets
  - HTTP
    - This feature provides:
      - HTTP 1.0/1.1 client features, including pipelining, chunking, and connection management
      - HTTPS (TLS1.0 and SSL3.0)
      - HTTP authentication (basic, digest, NTLM, and negotiate)
      - HTTP entity API (multi-part, string, Xml, and url encoded)
  - Wi-Fi and Wi-Fi Direct
    - This feature provides:
      - Functionality for managing the local Wi-Fi device
      - Functionality for using Wi-Fi Direct networks
      - *Note*: Wi-Fi features are only supported on the reference target device, not on the Emulator.
  - Bluetooth
    - This feature provides:
      - Functionality for configuring the local Bluetooth device
      - Bluetooth OPP (Object Push Profile), SPP (Serial Port Profile), and HDP (Health Device Profile) services
      - Device and service discovery
      - *Note*: Bluetooth features are only supported on the reference target device, not on the Emulator.
  - NFC
    - This feature provides functionality for the Read/Write and P2P mode.
- Tizen::Security
  - Crypto
    - This feature provides:
      - Implementing cryptography algorithms that facilitate adding security features to applications
      - Crypto algorithms, such as Hash, HMAC, symmetric cipher (AES, DES, 3DES, RC2, RC4, SkipJack, and Cast), and asymmetric cipher (RSA)
      - *Note*: The RC5 algorithm is not supported.
      - Key exchange algorithms (DH and KEA)
  - Certificate management
    - This feature provides:
      - X.509 certificates
      - X.509 certificate chain validation from an "entity" certificate to a trusted CA certificate
      - DER and PEM formats
  - Key management
    - This feature provides:
      - Secret keys to encrypt and decrypt messages
      - Public keys and private keys to offer authentication and public key infrastructure
      - Pseudo random number generation
      - X9.31 PRNG
- Tizen::Shell
  - Notification
    - This feature provides:
      - Ongoing notifications
      - Additional notification functionality to customize each notification message
      - Changing notification title, icon, and sound
      - Progress bar for ongoing notifications
  - QuickPanelFrame
  - This feature provides a custom UI plugin for the notification tray.


- Addressbook
  - This feature provides:
    - Managing and searching contacts on the device storage
    - Importing and exporting vCard files
    - Contact aggregation
- Calendarbook
  - This feature provides:
    - Managing and searching the personal schedule and task information on the device storage
    - Importing and exporting vCalendar files


- Alarm
  - This feature provides one-time or repeating alarms.
- DeviceManager
  - This feature provides listening and handling events for various external devices.
- Environment
  - This feature provides system environment variables.
- PowerManager
  - This feature provides managing the device power state.
- RuntimeInfo
  - This feature provides runtime information, such as the allocated memory, storage, and CPU utilization.
- SettingInfo
  - This feature provides managing various user settings.
- SystemInfo
  - This feature provides system information, such as the API and platform versions, supported device features, and screen dimensions.
- SystemTime
  - This feature provides retrieving current system time, ticks, and uptime.
- Vibrator
  - This feature provides handling the vibration functionality of a device.


- Telephony information
  - This feature provides:
    - Getting information of the current call type, status, and event
    - Getting information of the current network, such as the cell ID, LAC, and PLMN
    - Getting information of the current network status, such as the availability of call and data services and roaming
    - Getting information of the inserted SIM card


- Text Encoding and Decoding
  - This feature provides:
    - Encoding Unicode characters to various other characters
    - Decoding characters in character sets to Unicode characters


- UI core
  - This feature provides:
    - Containers, such as forms, panels, split panels, and windows, which can be used to hold different UI components
    - Windows, such as frames, pop-ups, and message boxes, which can be used to support layered display surfaces for UI components
    - Accessibility container for customization of screen reader functionality for the visually impaired
- UI controls
  - This feature provides:
    - UI components for user interaction, including button, edit field, footer, gallery, header, label, slider, tab bar, and various date, time, and color pickers
    - Various lists using the ListView, GroupedListView, IconListView, and TableView classes
- Multi-point touch and gestures
  - This feature provides multi-point touch events and touch gestures.
- Scalable UI
  - This feature provides developing and migrating multi-resolution applications with utilities, such as the layout manager, logical coordinates, and automatic resource selection.
- Animation
  - This feature provides:
    - Key frame-based, asynchronous animation of UI controls (such as form or panel transitions)
    - Advanced 3D effects and animations using VisualElement and its related classes
- Effects
  - This feature provides 3D effect animations, such as page flipping and various rotations, created with the UI Effect Builder.
- Scene management
  - This feature provides form life-cycle management and makes the transitions between forms or panels easier.
- Downloadable IME
  - This feature provides a custom input creation method.
- Themes
  - This feature provides 2 different themes (dark and light). Each application can select a theme to use.


- Sensor management
  - This feature provides:
    - Gyro, light, tilt, magnetic, acceleration, and proximity sensors
    - Motion detection (snap, double tap, and shake)
    - Waking up from the sleep mode (available on acceleration)


- Web browsing
  - This feature provides:
    - Loading a page from the network or local storage
    - Text selection
    - Sending a page loading request with a customized HTTP header and HTTP body
- Hybrid application programming
  - This feature provides:
    - JavaScript code evaluation for C++ to JavaScript binding
    - Event handler bridge for JavaScript to C++ binding
- Page navigation list
  - This feature provides a list of visited pages from a Web control instance.
- Settings
  - This feature provides:
    - Configuring Web controls, such as setting the user agent, input style, and font size
    - Configuring Web control behavior, such as enabling JavaScript, Javascript popup, and HTML5 Geolocation features
- Cookie and cache control
  - This feature provides:
    - Private browsing control
    - Separate cache and cookie storage for each application
    - Clearing the cache and cookies
- Web history
  - This feature provides a list of visited pages from the browser.
- JSON
  - This feature provides a JSON parser and JSON writer.


- The reference applications use Tizen native APIs.
- Home
  - This application contains user-selected items and executes them.
- Lock
  - This application locks and unlocks the device screen.
- Calculator
  - This application performs arithmetic operations.
- Calendar
  - This application manages planned events.
- Camera
  - This application records images and videos.
- Clock
  - This application includes an alarm, timer, stopwatch, and word clock.
- Contacts
  - This application manages contacts.
- Email
  - This application sends and receives emails.
- Gallery
  - This application shows images and videos.
- Image viewer
  - This application views images.
- Internet
  - This application browses the Internet.
- Memo
  - This application reads and writes memos.
- Messages
  - This application sends and receives messages.
- Music player
  - This application plays music and manages playlists.
- My files
  - This application browses the files in the device.
- Phone
  - This application sends and receives calls and manages call logs.
- Settings
  - This application sets system settings.
- Video player
  - This application plays videos.

### Known Issues

- Tizen::Graphics
  - Graphics
    - The Tizen SDK adopts font resources with open source license, therefore, some rarely used glyphs are missing.
    - When the HwAcceleration flag is turned on in the Emulator, the OpenGL ES 1.1 functions do not behave properly.
  - 3D graphics
    - The OpenGL ES pbuffer surface is not supported in the Emulator.
- Tizen::Media
  - Various effects of the Camera feature are not supported in the Emulator in Mac OS X.
  - The front camera is not working in specific reference targets.
    - The front camera is not working in the specific target device. (Ref.Device-PQ)
    - The camera flash is not working in the specific target device. (Ref.Device-210)
    - The camera's NV12 capture format is not working in the specific target device. (Ref.Device-PQ)
    - The GPU enabled Emulator has performance degradation in Camera previewing and Player rendering.
  - There are performance issues when decoding large scale images in the Emulator.
- Tizen::Messaging
  - The IP Push feature is not supported in the reference target.
  - The SMS/MMS feature is not supported in the reference target.
- Tizen::Net
  - The account management feature is not supported in the reference target.
  - PS network connection is not supported in the reference target.
- Tizen::Telephony
  - The telephony feature is not supported in the reference target.
- Tizen::Ui
  - In this release, only the light colored theme is supported.
  - When a container is deleted, the parent (container) is deleted first, followed by the child controls. The order is to be fixed so that the child controls are deleted first.
  - The Tizen::Ui::Controls::Frame::OnTerminating() event handler is currently not called properly.
  - It is possible for a control to receive the Tizen::Ui::IFocusEventListener::OnFocusLost() event handler before receiving the OnFocusGained() event handler.
  - Tizen::Ui::Animations::IVisualElementEventListener listeners are sometimes called needlessly.
  - Termination event handlers for animation and animation group are sometimes called in the reverse order.

## Core System

### New Features

- Reference Kernel
  - The following features have been added:
    - Support for TRATS2 board (Exynos4412)
    - Support for FB (Frame Buffer)-based graphics (updated to use DRM (Direct Rendering Manager) for DRI (Direct Rendering Infrastructure))
    - Support for CMA (Contiguous Memory Allocator)
    - Support for IOMMU for some DMA devices
    - Support for Extcon
    - *Note*: Some of the new features are back-ported and cannot be aligned with the stable version.
- Core applications
  - The following features have been added:
    - Camera, Gallery, and Music apps
    - Contact link
- Sync
  - Sync agent
    - The following features have been added:
      - Common elements for sync client (this feature has been revised)
      - Plugin mechanism to easily add new features
  - OMA DS
    - The following features have been added:
      - Support for OMA DS v1.2
      - 3 plugins including plain-text, vCard, and xcallog
  - OMA DM
    - The following features have been added:
      - Support for OMA DM v1.2

### Changed Features

- System
  - libusb has been upgraded from 1.0.9 to 0.1.12.
- Reference kernel
  - The Linux kernel has been upgraded from 2.6.36 to 3.0.

### Known Issues

- Reference Kernel
  - The rear-camera is not supported. (Ref.Device-PQ)
  - The front-camera's flash is not supported. (Ref.Device-210)
- Core applications
  - Internet is not supported in this version.

## Supported Devices

### Features

- Emulator
  - The Emulator is an x86-based Qemu image which can be run on computers.
  - Preloaded applications:
    - Core applications
      - Home and Lock
    - Reference applications
      - Calculator, Calendar, CalendarService, Camera, Clock, Contacts, Email, Gallery, ImageViewer, Internet, Memo, Messages, MusicPlayer, MyFiles, Phone, Settings, and VideoPlayer
    - Home and Lock applications can be changed from core applications to reference applications with the build configuration.
    - All reference applications can be changed from reference applications to core applications with the build configuration.
- Reference target devices
  - The reference target devices are designed based on commercial target devices:
  - Ref.Device-210
    - Ref.Device-210 is a reference target based on Samsung Galaxy S2 HD.
  - Ref.Device-PQ
    - Ref.Device-PQ is a reference target based on Samsung Galaxy S3.
  - Preloaded applications:
    - Core applications
      - Home, Calculator, Calendar, CalendarService, Camera, Clock, Contacts, Email, Gallery, ImageViewer, Memo, Messages, MusicPlayer, MyFiles, Phone, Settings and VideoPlayer
    - Reference applications
      - Internet
    - All applications can be changed to reference applications with the build configuration.

### Known Issues

- Emulator
  - The core applications that are not preloaded have not been fully tested in the Emulator.

# IDE and Tools

### New Features

- General
  - Multiple OS support
    - The IDE is available for 32-bit and 64-bit Linux (Ubuntu), Windows, and Mac OS X.
  - Native (C++) development support
    - The native (C++) SDK provides convenient development tools, such as the IDE, dynamic analyzer, unit test, code coverage, UI builder, effective UI builder, and API checker.
  - Eclipse version upgrade
    - Upgrades the Eclipse for IDE from Helios SR1 to Indigo SR2.
  - Design renewal
    - The Tizen pinwheel BI (Brand Identity) has been applied.
    - A new delightful color scheme for icons, textures, and shapes has been applied.
- Common Tools
  - Install Manager
    - The following features have been added:
      - Support for setting the network environment:
        - Support for proxy and proxy authentication
        - Three options are provided:
          - Direct connection
          - Automatic proxy configuration
          - Manual proxy configuration
      - Support for package information cache:
        - If a system does not support a network, the Install Manager can show components trees.
      - Support for advanced extra package control:
        - You can find extra package information at 'tizen-sdk-data/extra'.
        - An extra repository can be added even if there are no packages which can be updated.
        - Extra repository and packages can be removed.
      - Support for retrying a download when an installation failure occurs
      - A refined message text
  - Emulator
    - The following features have been added:
      - Support for HW VT acceleration on 32/64-bit Linux (Ubuntu), Windows, and Mac OS X
      - OpenGL ES enhancement:
        - Support for HW acceleration on 32/64-bit Linux (Ubuntu), Windows, and Mac OS X
        - Support for HW acceleration with NVIDIA, ATI, and Intel graphic cards
        - *Note*: This feature requires the driver for OpenGL ES >= 2.0 and GLSL >= 1.20 for the Intel graphic card on Windows.
        - *Note*: This feature requires Ubuntu version 12.04 or higher for the Intel graphic card.
        - Support for SW mesa in Tizen guest, in case OpenGL ES is not available in the host
        - Support for the pixmap surface and eglImageKHR/glEGLImageTargetTexture2DOES extensions
      - QEMU version upgrade to 1.2.0.
      - Multimedia codec enhancement:
        - GStreamer FFmpeg plugin for the Emulator has been updated from 0.10.11 to 0.10.13.
        - Support for more codecs, including VC-1
        - Faster responsiveness
      - Support for host proxy protocols, such as FTP, socket, and HTTPS
      - Memory capability enhancement of Tizen guest by adding a swap partition
      - Support for RAM dump function as an advanced debugging feature (Ubuntu only)
      - Emulator UX enhancement
        - This feature provides:
          - Flexible and portable general purpose skin that consists of display and key windows
          - HW keys now located in the key window
          - Key window enabled by the context menu or a toggle button in the display window
          - Platform booting progress displayed in the bottom of the screen
          - Support for mouse wheel inputs from the host (visible only if the guest applications can handle scroll actions)
          - Support for easy browsing of Emulator-related paths by double-clicking in the Detail Info dialog, such as, Log Path, SD Card Path, File Sharing Path, and Image Path
  - Emulator Manager
    - The following features have been added:
      - General purpose skin is applicable to various Tizen profile devices
      - Support for display density in DPI (Dots Per Inch)
      - Support for counting the maximum multi-touch points
  - Support for CLI (Command Line Interface)
- Event Injector
  - The following features have been added:
    - File injection of sensor data
    - Support for the orientation sensor
    - Support for NFC
    - Support for a pluggable sdcard with the size of 4, 8, 16, or 32 GB
    - Support for CLI (Command Line Interface)
- CLI (Command Line Interface) tools
  - The following features have been added:
    - Developing Tizen applications without an Eclipse-based IDE
      - Compact and suitable for a minimal SDK
      - Support for device connection and project packaging, signing, and installation
    - Support for the native-gen, native-make, native-packaging, native-run, and native-debug commands for native application development.
    - Support for Web application development.
- SDB (Smart Development Bridge)
  - The following features have been added:
    - Support for commands for installing and uninstalling application packages
    - Support for commands for connecting and disconnecting to a device via TCP/IP
    - Support for creating a remote file with a utf-8 character encoding (--with-utf-8)
    - Support for the target name given by the Emulator Manager
    - Console supporting ANSI color (ansicon.exe) in Windows


- Web IDE

  - The following features have been added:
    - Editor
      - JavaScript Development Tools (JSDT)
        - Validator policies changed to remove unnecessary warnings
      - Support for JavaScript and CSS source code beautifier (Ctrl + 6)
      - *Note*: The Preview tab in the HTML editor has been deleted. The Google Chrome-based HTML preview is supported through the preview button in the action bar.
    - Views
      - HTML and CSS previews
        - Container changed from the in-place view to the Google Chrome browser
        - Instantly displaying changes made to HTML or CSS code (live-reload)
      - Advanced Declaration view for JavaScript
        - Instantly displaying the declaration of the selected code on a separate view
      - JavaScript Log view
        - Support for colors based on the level
      - Support for IDE-related views through help context pop-ups
    - Building, running, and debugging
      - RDS (Rapid Development Support) added to enable faster building, running, and debugging of applications
      - Widget package file created using the Full or Clean Build
      - The remote inspector container changed from the in-place view to the Google Chrome browser
      - Support for incremental build
      - Support for hybrid application packaging
    - Tools
      - Support for CLI (Command Line Interface) tools
    - Other changes
      - Widget signing menu in the project context menu removed
      - Support for the Tizen Web UI framework library version 0.2.4 and related templates

- Web UI Builder

  - Programming model

  - - Support for 4 types of templates
    - Support for application life-cycle event handlers, such as on-load and on-unload
    - Support for automatically generating application termination code for the back button of the application main screen
    - Complementing project configuration

- WYSIWYG page design editor (Page Designer)

  - Support for a widget palette including 29 Tizen UI widgets and 12 HTML widgets
  - Support for drag-and-drop creation, moving, and deletion of widgets
  - Support for multiple selection, copy, cut, and paste actions
  - Support for viewport scaling mode that is similar to the Emulator's

- Outline view

  - Support for deleting and renaming widgets

- Properties view

  - Support for CSS styling for HTML block widgets
  - Support for custom event handlers
  - Complementing preset event handlers

- Pages view

  - Improvement of the page display information
  - Improvement of the page operation UX


- API implementation
  - Bluetooth, Notification, and Download APIs
  - Existing modules updated according to Tizen API specification changes
- UI enhancement
  - The device panel redesigned: geo-location, network, communication, sensor, and battery added
  - Consolidation of the device settings into the configuration window
  - Enhancement of the application launch bar (the project history is kept)
  - Support for the device panel on/off configuration window


- Native IDE
  - Native IDE is new for Tizen version 2.0. It is a smart and powerful development environment to create native applications for Tizen platforms.
- Project Wizard
  - This feature provides:
    - Various templates and samples to create native applications
    - Express mode for faster project generation
- Editor
  - This feature provides:
    - Code assist for Tizen native APIs
    - Multi-form editor for the manifest file. You can configure the ID, version, icon, and privileges of the application.
- Building and packaging
  - This feature provides:
    - TPK (Tizen Package File) packaging
    - Author and distributor signing
    - Multi-process application packaging. Multi-process applications enable hybrid architecture combining UI and service applications.
    - LLVM 3.1 and GCC toolchain
    - GCD (Grand Central Dispatch), with LLVM toolchain only
    - OpenMP 3.0., with GCC toolchain only
    - PCH (Pre-compiled Header) compilation
    - 3rd party rootstrap extensions
- Running and debugging
  - This feature provides:
    - Various debugging methods: normal, attach, and coredump
    - RDS (Rapid Development Support) for uploading only the changed files when re-launching, skipping the packaging process
    - Launch control for various application types, such as an IME application
    - Crash report service and crash file viewer
    - Sbuilding the project automatically if there is no executable file when launching the application
- Preference pages for customization
- Tools
  - This feature provides:
    - CLI (Command Line Interface)
    - Unit testing using the Google C++ testing framework
    - Support for code according to gcov chart
    - C++ UI builder, C++ UI Effect Builder, and API checker tools
    - OProfile profiling tool, which detects the method and module execution time
    - Valgrind profiling tool, which detects the abnormal use of heap and stack memory
- Dynamic analyzer
  - This feature provides:
    - Effective analysis of the application behavior at runtime
    - Integration with the IDE menu
    - System information in the Timeline view
    - Overall application analysis in the Summary view
    - Detailed file, thread, and UI analysis
    - Saving and loading the trace result
    - Recording and replaying application user interaction
    - Showing related source code as a tooltip and in the IDE
    - Combining chart and table selections
    - Range-based analysis


- This component uses a GBS (> 0.12)-based build system.
- The Platform IDE enables configuring various GBS build options, such as offline build and incremental build.


- This feature provides:
  - The same UX as the native and Web IDEs
  - Basic categorized project templates
  - Creating a project using directly downloaded sources from GIT


- This feature provides:
  - Creating new rootstraps (sysroots) using a specified package repository (snapshot)
  - Showing available rootstraps on the Rootstrap View
  - Changing the rootstrap to make platform project building easy
  - Exporting and importing rootstrap.


- This feature provides:
  - Building a platform project without manually installing dependent packages
  - Running and debug a platform module without manual installation
  - Configuring the launch using a launch configuration wizard


- This feature provides:
  - Showing and changing repository information of the selected target (rootstrap or device)
  - Installing or removing local or remote packages
  - Upgrading whole packages of the selected target


- This feature provides:
  - Changing the sudo password
  - Managing site options:
    - GIT base address
    - GIT project list
    - Proxy setting to connect package repository


- DIBS (Distributed Intelligent Build System)
  - This feature provides:
    - New development system for Tizen SDK
      - Building a Tizen SDK package from a local source
      - Installing or replacing the package in Tizen SDK installation
      - Requesting the builder to upload the package on the remote DIBS build or package server
      - Install manager for installing the Tizen SDK from the DIBS package server
    - DIBS package server
      - Multi-distributions and multi-target-OS and their management
      - Creating a snapshot for distribution, and supports snapshot management
      - Exposing the SDK packages in the Internet
      - Command line tool for the package server and client
    - DIBS build server
      - Building remote-request Tizen SDK packages
      - Checking the reverse-build-dependency and provides its resolve process
      - Multi-distributions and multi-target-OS
      - ubuntu-32/64, windows-32/64, and macos-64 for the build server
      - Distributed child servers
      - Automatic package synchronization between package servers
      - Command line tools for the build server and client
    - DIBS Web
      - Ruby-On-Rails-based Web UI for DIBS
      - Project page showing all involved DIBS projects
      - Requesting to build or upload the Tizen SDK package on the project page
      - Job page showing the status of all requested jobs
      - Administrator managing the DIBS system on the admin page


- IDE Help contents
  - Getting started with Tizen
    - This section provides an overview of Tizen, the developer environment, and other general guides.
  - Tizen Web App Programming
    - This section provides API references, information about the Web application development process and tools, the programming guide, tutorials for Tizen Web application development, and descriptions of Web sample applications.
  - Tizen Native App Programming
    - This section provides the API reference, information about the native application development process and tools, the programming guide, tutorials for Tizen native application development, and descriptions of native sample applications.
  - Tizen Platform Development
    - This section provides the API reference and information about the Tizen platform development environment and process.
  - Tizen SDK Development
    - This section provides information about the Tizen SDK development environment and process.

### Known Issues

- Web IDE

  - In the Web-signing CLI, the password input problem still exists. To work around this, insert passwords in the profile.xml file before signing.
  - The advanced Declaration view for JavaScript has several known issues due to JSDT-related bugs.
  - Assignment tracing for JavaScript has several known issues:
    - If local variables are used as a method name in a method call expression, assignment tracing does not function.
    - Incorrect activation occurs if the inner and outer methods are both anonymous.
  - The template namespaces have been changed to *www.tizen.org*. If you cannot see the project templates or samples in the Project Wizard, modify the namespaces in the tizen-app-template.xml file of the template directory accordingly.

- Native IDE

  - Debugging
    - Attach debugging does not work because the executable is built with the -fPIE option.
  - RDS (Rapid Development Support)
    - RDS is not supported in multi-process application projects.
    - RDS is not supported in CLI tools.
    - RDS does not support signing.
  - CLI (Command Line Interface)
    - The project path and Tizen SDK path are fixed when the project is generated. If you change the path, the project cannot be built.
    - .bat files are not provided for Windows.
  - Unit test
    - The Test Explorer does not work if the project files have not been changed. In this case, edit the code manually, build the project, and run it.
  - Code coverage
    - Code coverage is not supported for the LLVM toolchain. To use code coverage, use the GCC toolchain.
  - Valgrind
    - Valgrind profiling is only supported in the Emulator.

- Emulator

  - OpenGL ES acceleration can have problems in certain environments:

    - Windows XP/7 with Intel motherboard integrated card
    - Ubuntu 11.10 with Intel CPU/motherboard integrated card

    If this occurs, turn off the HW GL acceleration in the Emulator Manager. The HW GL acceleration can be disabled due to host capability, even though you select 'HW GL Acceleration supported' in the Emulator Manager.

  - When you launch the Emulator on Windows, you can get a "failed to allocate memory" error. In that case, try the following:

    - Increase the user area of the virtual memory in the system to 3 GB by running the "bcdedit /set increaseuserva 3072" command on the console with administrator rights (Windows 7 only).
    - Close some other programs and try to launch the Emulator again.
    - If you have set the RAM size as 768 or 1024 MB for the VM in the Emulator Manager, change the RAM size to 512 MB.

  - Using the Emulator with SOCKS (SOCKet Secure) proxy on Mac OS X can cause unexpected problems.

  - You cannot play some video files linked in YouTube, or other Web pages, using the browser on the Emulator.

  - The Emulator log file (emulator.log) can become too large if you run the Emulator for a long time.

  - The Emulator screenshot is drawn with a framebuffer of a virtual device. Sometimes the screenshot may not appear correctly.

  - When you use the camera on Mac OS X, the brightness and contrast settings would not work.

  - Some menu items of the top menu bars of the Emulator and the Emulator Manager do not work on Mac OS X.

- Dynamic analyzer

  - A screenshot is sometimes not taken if the screen or scene change is implemented using an animation technique.

- Install Manager

  - A shortcut is not provided in Mac OS X.
  - If a dialog displays that the Install Manager is damaged on Mac OS, please see [http://support.apple.com/kb/HT5290](http://support.apple.com/kb/HT5290).

- # Next Release

- The next version, Tizen 2.1, will be released in the 2nd quarter of 2013. As a minor release, it will only contain several new features and performance enhancement without API modifications or removal. The main features of Tizen 2.1 include account management, application installing service, livebox support, performance optimization, and a security enhancement.
