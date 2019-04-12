# Tizen 2.1

Release Date: 18 May, 2013



The Tizen 2.1 Nectarine release provides developers with the Tizen kernel, device drivers, middleware subsystems, and Web/Native APIs, necessary to develop future Tizen compliant solutions.

## Release Details

- [Getting source code](http://review.tizen.org/git/) (Tizen 2.1 Nectarine source codes are under **tizen_2.1** branch.)
- [Getting binaries and images](http://download.tizen.org/releases/2.1/tizen-2.1)
- [How to flash to a device](https://wiki.tizen.org/wiki/Flash_Tizen_2.1_Image_to_Reference_Device)

## Release Notes

Tizen is an open source, standards-based software platform supported by leading mobile operators, device manufacturers, and chip suppliers for multiple device categories, including smartphones, tablets, netbooks, in-vehicle infotainment devices, and smart TVs.

The Tizen Platform consists of the Web framework (APIs), native framework (APIs), and core system.

The Tizen Software Development Kit (SDK) is a comprehensive set of tools for developing Web applications, native applications, and the platform component for Tizen. The SDK contains an install manager, IDE, tools, documents, samples, and a platform image.

### Tizen Platform

#### Web Framework

##### New Features

- HTML5 / W3C
  - Security
    - Content Security Policy 1.0
      - This policy language provides the declaration of a set of content restrictions for Web resources, and a mechanism for transmitting the policy from a server to a client when the policy is enforced
  - Performance and Optimization
    - Navigation Timing
      - This API provides an interface for Web applications to access timing information related to navigation and elements
- Web Runtime
  - Web Dynamic Box runtime framework to enable embedding of Web Dynamic Boxes in viewer applications (for example, the Home screen). The supported features include:
    - Web Dynamic Box installation and uninstallation
    - Web Dynamic Box configuration extensions
    - Web Dynamic Box execution and life-cycle management
  - Configuration extension updates
    - The "package" attribute in the <tizen:application> element to specify the package ID

##### Changed Features

- For Tizen Web API change details, see [Tizen API Change Notes](http://developer.tizen.org/downloads/sdk/2.1-api-change-notes).

- HTML5/W3C

  - Reference documentation unified as a single document in accordance with the specification changes:

    - CSS 2D Transforms and CSS 3D Transforms Module Level 3 to CSS Transforms

  - Specification version update

    *Note*: If you have developed Web applications based on the previous Tizen versions (including 2.0) of the following specifications, you MUST check whether the corresponding features are available in the updated version of the specifications referred to in this release.

    - DOM, Forms, and Styles
      - HTML5 Forms (Partial) - The formnovalidate content attribute of the form element is not supported
      - CSS Transforms
      - CSS Animations Module Level 3
      - CSS Transitions Module Level 3 (Partial)
      - CSS Multi-column Layout Module (Partial) - The column, avoid-page, and avoid-column values of the break-before and break-after properties, and the avoid-page and avoid-column values of the break-inside property are not supported
    - Device
      - Touch Events version 1 (Partial)
      - The Screen Orientation API
      - The Network Information API
    - Graphics
      - HTML5 The canvas element (Partial) - The toBlob method of the HTMLCanvasElement interface is not supported
      - HTML Canvas 2D context (Partial) - The scrollPathIntoView method of the CanvasRenderingContext2D interface is not supported
    - Media
      - HTML5 The video element (Partial) - The videoTracks attribute of HTMLMediaElement and the abort event are not supported
      - HTML5 The audio element (Partial) - The audioTracks attribute of HTMLMediaElement and the abort event are not supported
      - Web Audio API (Partial)
        - The computedValue attribute of the AudioParam interface is not supported
        - The SOUNDFIELD enum string constant value of the PanningModelType enum for the panningModel attribute is not supported

  - Update to method, attribute, and constructor support

    - DOM, Forms and Styles
      - Selectors API Level 2 (Partial) - The matchesSelector method (Element interface) is not supported
      - Media Queries (Partial) – The color-index, min-color-index, max-color-index, resolution, scan, print, 3d-glasses, and grid queries are not supported
    - Storage
      - File API: Writer (Partial) - The FileSaver interface and saveAs method (Window interface) are not supported
    - UI
      - Clipboard API and Events - The ClipboardEvent interface constructor is not supported

- Web UI Framework

  - The following widgets are newly introduced:
    - Gallery 3D
    - Split View
  - The APIs of the following widgets are updated:
    - Fast Scroll
    - Token Text Area
    - Progress
    - Multimedia View
    - Virtual Grid

- Tizen Web APIs

  The following APIs are newly introduced or updated:

  - Bookmark
  - DataControl
  - DataSync
  - MessagePort
  - Notification
  - Package
  - Push
  - SecureElement
  - SystemInfo

#### Native Framework

##### New Features

- Tizen::App
  - Application controls
    - Bluetooth, Gallery, and Todo application controls added
    - Platform application control supports implicit resolution
    - Supports signature-based access control
  - Data controls
    - Supports flow-control operation on multiple requests
    - Supports signature-based access control
- Tizen::App::Package
  - Package management
    - Supports application-specific metadata in the manifest
    - Supports package filtering and package app filtering for more effective ways to get installed package list
    - Supports getting package information from the specific Tizen package file
- Tizen::Base
  - Basic types
    - Supports tick resolution in the Tizen::Base::DateTime class
    - Supports the Tizen::Base::String hash code provider and comparer which can be used with the template Collection classes
  - Collection
    - Supports conversion between Tizen collections and C++ standard library containers
    - Supports non-owning collection and owning collection through the DeleterFunctionType argument
  - Utility
    - Supports tokenizing string scanner and converter (Tizen::Base::Utility::Scanner class)
  - Runtime
    - Supports non-recursive mutex
- Tizen::Content
  - Content management
    - Supports metadata extraction (such as EXIF and ID3 tags from images, audio, and video)
    - Supports scanning for a file or directory to synchronize content information with the local content database
    - Supports database change notifications
  - Download manager
    - Download information is available for at least the next 24 hours
    - Supports enabling and disabling the download notifications
    - Supports setting the allowed network type
    - Supports managing the HTTP header fields
- Tizen::Graphics
  - Graphics
    - Supports floating point precision
      - API set which draws 2D primitives in floating point coordinates is added
    - New properties for canvas
      - Line cap style, which controls the shapes of the end of line
      - Line join style, which determines how to draw the intersection of two joining lines
      - Composite mode, which determines how to merge a 2D primitive with another primitive
      - Anti-alias mode for 2D drawing in canvas
    - TextElement of EnrichedText are vertically aligned along the baseline with TEXT_ALIGNMENT_BASELINE
  - 3D Graphics
    - OpenGL ES
      - pbuffer surface is available in the Emulator
      - FBO for OpenGL-ES 1.1 is supported in the Emulator
    - GL utilities
      - Sample application and programming guide for CanvasTexture
      - Sample application and programming guide for VideoTexture
      - Programming guide for GlPlayer and GlRenderer


- Tizen::Io


- FileLock
  - Supports an advisory lock mechanism on file or registry file
- Dataset
  - Supports handling an in-memory table-structured dataset for DataControl result set


- Tizen::Locales


- New country codes added:
  - COUNTRY_BL (Saint Barthelemy)
  - COUNTRY_MF (Saint Martin (French part))
  - COUNTRY_AREA_419 (Latin America and the Caribbean)


- Tizen::Media


- Camera
  - Scene mode is added
- Audio and video recorder
  - Audio and video pre-processing filter APIs and classes
- Image
  - Floating point-based resized image decoding API
  - EXIF orientation getter
- VideoFrameExtractor
  - Recording rotation getter


- Tizen::Net


- NFC
  - Reserved Push feature
- HTTP
  - Server certificate is verified manually


- Tizen::Security


- Key
  - Supports "X509" and "PKCS#1" format for public keys and "PKCS#8" and "PKCS#1" format for private keys
  - Supports changing the format of the RSA key and encoding
- PKCS
  - Supports "PKCS#5" (Password-based Encryption Standard) and "PKCS#8" (Private-key Information Syntax Standard)
- Cert
  - Supports .p12 and .pfx certificate installation


- Tizen::Shell


- Notification
  - Supports badge change event listener
  - Supports notifications by application control - implicit AppControl resolution is attempted when the user selects the message
  - Supports text message notifications on the status bar
  - Supports removing individual notifications
  - Supports thumbnail and multiline-type notifications
- Dynamic Box
  - Supports showing the widget and its Drop View on the Home screen
- Shortcut manager
  - Supports adding application shortcuts on the Home screen


- Lock manager


- Supports getting the lock state and dismissing swipe unlocking


- Tizen::Social


- Account
  - Supports methods to manage the account information
  - Supports methods to access accounts and account providers
- Calendarbook
  - Supports methods to update an event instance
  - Supports absolute time for reminders
- Addressbook
  - Supports user profile
  - Supports bulk operations for adding, updating, and removing contacts


- Tizen::System


- Environment
  - System ringtone path is added in the PredefinedDirectoryType enum
- IScreenEventListener
  - The OnScreenBrightnessChanged event handlers added
- PowerManager
  - Supports subscribing to boot events
- RuntimeInfo
  - The following keys are added:
  - [http://tizen.org/runtime/system.status](http://tizen.org/runtime/system.status)
  - [http://tizen.org/runtime/memory.allocated.self](http://tizen.org/runtime/memory.allocated.self)
- SettingInfo
  - The SetValueAsync method is added for asynchronous elements
  - The following keys are added:
    - [http://tizen.org/setting/application.home](http://tizen.org/setting/application.home)
    - [http://tizen.org/setting/application.lock](http://tizen.org/setting/application.lock)
    - [http://tizen.org/setting/developer.usb_debugging](http://tizen.org/setting/developer.usb_debugging)
    - [http://tizen.org/setting/graphics.gpu.rendering](http://tizen.org/setting/graphics.gpu.rendering)
    - [http://tizen.org/setting/network.bluetooth](http://tizen.org/setting/network.bluetooth)
    - [http://tizen.org/setting/network.bluetooth.tethering](http://tizen.org/setting/network.bluetooth.tethering)
    - [http://tizen.org/setting/network.wifi](http://tizen.org/setting/network.wifi)
    - [http://tizen.org/setting/network.wifi.direct](http://tizen.org/setting/network.wifi.direct)
    - [http://tizen.org/setting/network.wifi.notification](http://tizen.org/setting/network.wifi.notification)
    - [http://tizen.org/setting/network.wifi.tethering](http://tizen.org/setting/network.wifi.tethering)
    - [http://tizen.org/setting/network.wifi.tethering.hide](http://tizen.org/setting/network.wifi.tethering.hide)
    - [http://tizen.org/setting/network.wifi.tethering.security](http://tizen.org/setting/network.wifi.tethering.security)
    - [http://tizen.org/setting/network.wifi.tethering.security.password](http://tizen.org/setting/network.wifi.tethering.security.password)
    - [http://tizen.org/setting/screen.mode](http://tizen.org/setting/screen.mode)
    - [http://tizen.org/setting/sound.notification](http://tizen.org/setting/sound.notification)
    - [http://tizen.org/setting/speech.tts.screen](http://tizen.org/setting/speech.tts.screen)
    - [http://tizen.org/setting/storage.directory.bluetooth.download](http://tizen.org/setting/storage.directory.bluetooth.download)
    - [http://tizen.org/setting/storage.directory.camera.record](http://tizen.org/setting/storage.directory.camera.record)
    - [http://tizen.org/setting/storage.directory.radio.broadcast](http://tizen.org/setting/storage.directory.radio.broadcast)
    - [http://tizen.org/setting/storage.directory.video.broadcast](http://tizen.org/setting/storage.directory.video.broadcast)
    - [http://tizen.org/setting/storage.directory.voice.record](http://tizen.org/setting/storage.directory.voice.record)
    - [http://tizen.org/setting/storage.directory.wap.download](http://tizen.org/setting/storage.directory.wap.download)
    - [http://tizen.org/setting/usb.tethering](http://tizen.org/setting/usb.tethering)
    - [http://tizen.org/setting/vibrator.level.notification](http://tizen.org/setting/vibrator.level.notification)
- SystemInfo
  - The GetBuildInfo method is added
  - The following keys are added:
    - [http://tizen.org/feature/graphics.acceleration](http://tizen.org/feature/graphics.acceleration)
    - [http://tizen.org/feature/network.nfc.reserved_push](http://tizen.org/feature/network.nfc.reserved_push)
    - [http://tizen.org/feature/network.push](http://tizen.org/feature/network.push)
    - [http://tizen.org/feature/opengles](http://tizen.org/feature/opengles)
    - [http://tizen.org/feature/screen.auto_rotation](http://tizen.org/feature/screen.auto_rotation)
    - [http://tizen.org/feature/screen.size.normal.480.800](http://tizen.org/feature/screen.size.normal.480.800)
    - [http://tizen.org/feature/screen.size.normal.720.1280](http://tizen.org/feature/screen.size.normal.720.1280)
    - [http://tizen.org/feature/shell.appwidget](http://tizen.org/feature/shell.appwidget)
    - [http://tizen.org/feature/sip.voip](http://tizen.org/feature/sip.voip)
    - [http://tizen.org/feature/speech.recognition](http://tizen.org/feature/speech.recognition)
    - [http://tizen.org/feature/speech.synthesis](http://tizen.org/feature/speech.synthesis)
    - [http://tizen.org/feature/network.telephony.mms](http://tizen.org/feature/network.telephony.mms)
    - [http://tizen.org/feature/network.telephony.sms.cbs](http://tizen.org/feature/network.telephony.sms.cbs)
    - [http://tizen.org/feature/vision.face_recognition](http://tizen.org/feature/vision.face_recognition)
    - [http://tizen.org/feature/vision.image_recognition](http://tizen.org/feature/vision.image_recognition)
    - [http://tizen.org/feature/vision.qrcode_generation](http://tizen.org/feature/vision.qrcode_generation)
    - [http://tizen.org/feature/vision.qrcode_recognition](http://tizen.org/feature/vision.qrcode_recognition)
- Vibrator
  - Supports array-based pattern vibration


- Tizen::Telephony


- SIM Manager
  - Supports getting SIM state and type


- Tizen::Ui


- APIs related to floating point are added throughout the UI namespace to reduce loss of precision issues when handling different resolutions
- UI controls
  - GroupContainer for grouping controls together with a grouped look is added
  - Supports verifying paste texts by implements Tizen::Ui::Controls::ITextFilter interface that processes a text event
- IME
  - Supports input methods in the Tizen::Ui::Ime::InputMethod classes which can be used to input characters to text input UI controls, and interact with the associated UI controls
  - Supports managing input methods through the Tizen::Ui::Ime::InputMethodManager classes


- Tizen::Uix


- Vision
  - Image recognition
    - Supports natural image recognition and tracking functionalities
    - New API for reference image feature set creation used in the image recognition is supported
  - QR code recognition
    - Supports standard QR code recognition and generation functionalities
- Sensor management
  - Supports device orientation, user acceleration, and gravity sensors


- Tizen::Web


- HTML5/W3C programming
  - Supports Geolocation, GetUserMedia, Custom Handlers, Web Notification, Web Socket, Web GL, Web Worker, App Cache, Indexed DB, Web SQL Database, Web Storage, File System, Vibration, Prevent Default, and many more
- Bookmark
  - Supports bookmark information management for a preloaded browser
- Storage
  - Supports managing quota for Application Cache, Indexed DB, Web SQL Database, Web Storage, and File System
- Page control
  - Supports:
    - Getting the size of a Web page
    - Scrolling a Web page
    - Clearing navigation history, auto-cumulated data, or auto-fill data
- Setting
  - Supports configuring the auto-complete or auto-fill features
- Floating point
  - Supports precision for floating-point coordinates
- JSON
  - Supports the compose API for unescape Unicode


- Reference native applications


- Messages
  - Multimedia Messaging System (MMS) is added

##### Changed Features

- For Tizen native API change details, see [Tizen API Change Notes](http://developer.tizen.org/downloads/sdk/2.1-api-change-notes).
- Tizen::App
  - AppControl
    - Phone AppControl is split into Phone and Call
    - The AppControl argument is changed, but the previous argument is still supported
  - GetInstanceByAppId() privilege level is changed from Partner to Platform
- Tizen::Ui
  - The client size of the Tizen::Ui::Controls::Popup control has changed to remove unnecessary left and right margins of 20 pixels
  - The height of the Tizen::Ui::Controls::MessageBox and Tizen::Ui::Controls::ProgressPopup controls is no longer variable according to the length of the body text
  - Indicator height is reduced in the landscape mode to provide more content area. Therefore, client bounds of the Tizen::Ui::Controls::Form control changes in the landscape mode. When the indicator is made translucent while in the landscape mode, it becomes completely transparent. The indicator and Form behavior for the portrait orientation has not changed.
  - The UI control deleting order has changed. UI controls were being deleted from parent to child, but in Tizen version 2.1, they are deleted from child to parent.
  - It is recommended to use ".#.png" for extension of a nine patch image. If the extension is not ".#.png", a bitmap which is loaded by the GetBitmapN() method and the UI Builder tool is not represented as a nine patch.
  - Scene management
    - User input is disabled on scene transition animations
    - The RegisterScene() method returns the exception to prevent duplicated form IDs on different form scenes

##### Known Issues

- Tizen::App
  - AppControl
    - The PICK operation of the MusicPlayer application control is supported only on the target device
    - Video call is not supported for the Call application control
- Tizen::Graphics
  - Graphics
    - The Tizen SDK adopts font resources with open source license, therefore, some rarely used glyphs are missing
  - 3D graphics
    - OpenGL ES
      - To create an egl window surface for Tizen::Ui::Controls, the width of the control has to be an even number
      - When a GL application runs with HW Acceleration enabled in the Emulator, the rendering results are flipped along y-axis
- Tizen::Io
  - MessagePort
    - Sending ByteBuffer values to a Web application through the RemoteMessagePort::SendMessage() method is not supported for native applications
- Tizen::Locales
  - Number formatting has known issues when saved number strings with a decimal point or thousands separator are handled after the locale setting has changed
- Tizen::Locations
  - If the current locale, time zone, or time is changed after region monitoring is enabled, the location provider does not always notify of the region change
- Tizen::Media
  - The camera preview or video is not shown if the height is longer than width when the H/W acceleration is off
  - The video frame that is rendered on the screen at the end of a stream or when the Player::Stop() method is called can differ depending on the device model and the H/W acceleration mode
- Tizen::Web
  - Web
    - The UI for the auto-complete feature does not work
    - To use a site supporting geolocation feature, enable the "Remember Preference" check box when a confirm popup appears
  - JSON
    - The JSON parser is currently locale-dependent. It will be changed in a later revision to be locale-independent.

#### Core System

##### New Features

- Reference Kernel
  - MFC (Multi Function Codec) firmware is added
  - Bluetooth
    - Supports encoding of 32/128 bit UUIDs is added
  - Camera
    - Supports 3264x2488 and 3264x1836 preview resolutions for RD-PQ
- System
  - Systemd
    - As a system and service manager, systemd (v.43) is newly applied to the platform, replacing the System V init daemon
    - Parallelized service activation, on-demand socket and D-Bus activation for starting services and daemons, managing the service processes as a group using Linux cgroup, supporting automount points, snapshotting, and restoring of services are newly added
    - systemd coredump handler is disabled as the Tizen platform has its own crash debugging module
    - Supports SMACK labeling of FIFO and UNIX domain sockets used by systemd at runtime
    - In order to support backward compatibility of System V init, necessary features, such as "reboot parameter passing" are added into systemd
  - Device-node
    - New module to control hardware devices. A tunnel between system framework and OAL (OEM Adaptation Layer), which accesses real device nodes. In addition, this module decides the permission of device nodes with which user can access.
- Security
  - Smack
    - Full Smack support in kernel space including long label support, recursive transmute
    - Smack labels for platform core modules and sample Smack rule sets enabling apps to run properly

##### Changed Features

- System
  - System V init daemon is removed and systemd is used as the service manager
  - Power manager
    - When a user or an application changes the brightness of display, the power manager daemon broadcasts the information to other applications
  - Device manager
    - Even in a low battery condition, changing the display brightness can be done
  - Feedback
    - All vibration files are combined to an XML file to reduce the size of binary. The XML file is implemented by base64 encoding schemes.
  - Vibrator
    - When a vibration effect is created, its magnitude can be set
  - Sys-Assert
    - Debug mode is enabled
- dlog
  - In the logging mode, the platform log turns on or off conditionally

#### Supported Devices

##### Features

- Emulator
  - The Emulator is an x86-based Qemu image which can be run on computers
  - Preloaded applications:
    - Reference Core applications
      - Home and Lock
    - Reference native applications
      - Calculator, Calendar, CalendarService, Camera, Clock, Contacts, Email, Gallery, ImageViewer, Internet, Memo, Messages, MusicPlayer, MyFiles, Phone, Settings, and VideoPlayer
    - Home and Lock applications can be changed from reference core applications to reference native applications with the build configuration
    - All reference native applications can be changed from reference native applications to reference core applications with the build configuration
- Reference target devices
  - The reference target devices are designed based on commercial target devices:
  - Ref.Device-210
    - Ref.Device-210 is a reference target based on Samsung Galaxy S2 HD
  - Ref.Device-PQ
    - Ref.Device-PQ is a reference target based on Samsung Galaxy S3
  - Preloaded applications:
    - Reference Core applications
      - Home, Calculator, Calendar, CalendarService, Camera, Clock, Contacts, Email, Gallery, ImageViewer, Memo, Messages, MusicPlayer, MyFiles, Phone, Settings and VideoPlayer
    - Reference native applications
      - Calculator, Calendar, CalendarService, Camera, Clock, Contacts, Email, Gallery, ImageViewer, Internet, Memo, Messages, MusicPlayer, MyFiles, Phone, Settings, and VideoPlayer

#### Supported Languages

- The following languages are supported:
  - Arabic
  - Armenian
  - Azerbaijani
  - Basque
  - Bulgarian
  - Catalan
  - Chinese
  - Chinese(Singapore)
  - Chinese(HongKong)
  - Chinese(Taiwan)
  - Croatian
  - Czech
  - Danish
  - Dutch
  - English (US)
  - English (UK)
  - English (Philippines)
  - Estonian
  - Finnish
  - French
  - French (Canada)
  - Galician
  - Georgian
  - German
  - Greek
  - Hindi
  - Hungarian
  - Icelandic
  - Irish
  - Italian
  - Japanese
  - Kazakh
  - Korean
  - Latvian
  - Lithuanian
  - Macedonian
  - Norwegian
  - Polish
  - Portuguese
  - Portuguese(Brazil)
  - Romanian
  - Russian
  - Serbian
  - Slovak
  - Slovenian
  - Spanish
  - Spanish (Mexico)
  - Swedish
  - Turkish
  - Ukrainian
  - Uzbek

#### Licenses

- The following changes have been made in the licenses:
  - The term "Compatibility Definition Document" in the Flora license and Tizen SDK License has been changed to "Tizen Compliance Specification"
  - The term "Compatibility Test Suites" in the Flora license and Tizen SDK License has been changed to "Tizen Compliance Tests"
  - The Flora License 4.4 condition has been clarified regarding the licensee's own copyright to derivative works or modifications

### IDE and Tools

#### New Features

- General
  - Design renewal
    - The Tizen pinwheel BI (Brand Identity) has been applied
    - A new delightful color scheme for icons, textures, and shapes has been applied
    - The application icon size has been increased from 108 to 117
  - "Keyboard Shortcuts" menu added: a user can download Tizen IDE shortcuts in PDF format
    - Menu with a link to Tizen Web site added
- Common Tools
  - Emulator
    - The following changes have been made in OpenGL ES:
      - Support for the FBO extension for GLES1.1
      - Removal of SW mesa from the Tizen platform
    - systemd has been adopted for the Tizen platform booting
    - Sleep mode performance on Ubuntu and Mac OS X has been enhanced by removing redundant CPU usage
    - The orientation of the general purpose skin can be done with the skin indicator, which is by default located on the upper left corner and rotated along the skin
  - Emulator Manager
    - Checking the OpenGL capability of host has been added to enable and disable GPU acceleration automatically
  - Event Injector
    - The following changes have been made:
      - Support for the user acceleration sensor
      - Support for the gravity sensor
      - Support for the orientation sensor
      - Support for the MMS sent status
      - UI enhancement for telephony messaging
      - Removal of toggle buttons (check boxes) from the 3-axis sensor
  - Install Manager
    - Supports command line interface (CLI) for installing or removing the SDK
    - Separates the "Minimal" installation type into "Web Minimal" and "Native Minimal"
    - Shows the installed size of the SDK packages
    - Supports styling scripting tags for component description
- Web IDE and Tools
  - Configuration editor
    - Supports app-control operations on the Tizen tab
    - Supports app-widget settings on the Tizen tab
    - Supports account settings on the Tizen tab
    - Supports mouse events and touch effects on the Dynamic Box on the Tizen tab
    - Supports tools for icon production in the configuration editor
    - Changes the default required version from 1.0 to 2.1
  - Editors (HTML, JavaScript, and CSS)
    - Supports the code assist and privilege list for the add-on SDK
    - Changes the default mode of the HTML editor to the source mode
  - Building, running, and debugging
    - Supports NPPlugin packaging
    - Checks application ID validation during launch
    - Checks the architecture for a hybrid app before launch
    - Launching the application is canceled in case of existing errors in the "config.xml" file
  - Application signing
    - Application signing is mandatory for launching
    - Checks validation of the certificate password in the Secure Profile before launching
  - Project Wizard
    - Updated template libraries to jQuery 1.8.2 and jQM 1.2.0
    - Updated Tizen Web UI Framework to 0.2.26
  - Preferences
    - Removed the API assist option
- Web UI Builder
  - Programming model
    - Supports application life-cycle event handlers, such as on-show and on-hide
  - Properties view
    - Supports widget CSS style properties
  - WYSIWYG page design editor (Page Designer)
    - Supports absolute layout
    - Supports HTML block and common container widgets absolute layout
  - Advanced Declaration view
    - Support has been added
- Web Simulator
  - API implementation
    - SystemSetting, Push, NetworkBearerSelection, and Package modules added
    - Various old modules updated according to a specification change, including Messaging, SystemInfo, Content, and Power
    - Supports system service of dialer and messaging added and manual callbacks from other applications and services enabled
    - config.xml parser updated (as per new schema)
  - UI enhancement
    - UI refinement


- Native IDE and Tools


- Building
  - New build configuration: Debug, Release, and Profile
  - New architecture: LLVM-Bitcode/X86 (experimental), LLVM-Bitcode/ARM (experimental)
- Application signing
  - Application signing mandatory for launching
- Running and debugging
  - Supports attach debugging
  - Supports Smart Launch
  - Supports "Enable update" mode to test the Tizen Store update
  - Detailed error messages shown when the package is installed
- Tools
  - Code coverage
    - Code coverage is supported for the LLVM toolchain
  - Unit Test
    - Changed to use the static gtest library
  - Native CLI supports multi-project application packaging
  - sdb
    - sdbd has the "developer" privilege, so a user requiring root permission must use the "sdb root on" command
    - The "sdb install" command supports the Web package (*.wgt)
  - Rootstrap Manager removed (use the Platform SDK)
- Dynamic analyzer
  - Feature configuration view is added
  - File chart information on the File analysis page is updated (see the manual)


- Platform IDE


- Supports local package repository


- SDK Development Tools


- The "build-cli changelog" command for querying the change log is added
- Supports the project lock preventing building
- Shows the progress when registering packages
- Supports the remote build option ("--save") of the "build-cli" command to save build results in a local storage
- Shows detailed log of remote jobs on DIBS WEB

#### Bugs Fixed

- Web IDE
  - JSDT
    - Alerting the keyword error for "continue" and "delete" used as a property name of an object is fixed
    - Malfunction of the open declaration feature (for the position of creating an object with a constructor which has a declaration with parameters) is fixed
  - NPE at re-launching application after the first launch succeeded is fixed
  - Bugs for incremental signing are fixed
  - UI Builder project exception created by the user template is fixed
  - JSON Validator error is fixed
  - Hybrid app CLI is fixed
  - Various bugs related to templates are fixed
  - Template attribute (data-inline) is fixed
  - Movable header in the jQuery Mobile templates is fixed
  - The issue of not opening the configuration editor when there are errors in the file is fixed
  - Web-hybrid app CLI bug is fixed
  - Including generated signature files into deltaInfoList is fixed
  - Duplicated project location is checked when creating a new project
  - The "Google Chrome settings in preferences" problem is fixed

#### Known Issues

- Common IDE

  - RDS (Rapid Development Support)
    - RDS is not supported in multi-process application projects
    - RDS is not supported in CLI tools
  - CLI (Command Line Interface)
    - The project path and Tizen SDK path are fixed when the project is generated. If you change the path, the project cannot be built.

- Web IDE

  - The advanced Declaration view for JavaScript has several known issues due to JSDT-related bugs
  - The Lock function of the advanced Declaration view has been disabled because of a NullPointerException issue
  - Assignment tracing for JavaScript has several known issues:
    - If local variables are used as a method name in a method call expression, assignment tracing does not function
    - Incorrect activation occurs if the inner and outer methods are both anonymous
  - Web Simulator
    - Only a single application can run at a time
    - Modules not supported: DataControl, MessagePort, SecureElement, Bookmark, and DataSynchronization
    - Daylight saving time-related methods are not supported in the Time module
  - The "could not delete resources" problem while building is fixed
  - An error can occur in the Web UI Builder template when you try to perform the clean and build action. This is a bug in the JavaScript Validator in Eclipse, and can be resolved as follows:
    1. Uncheck JavaScript Validator in the Builders section of the application properties.
    2. Delete errors in the Problems view.
    3. Clean and build the project again.

- Native IDE

  - Unit test
    - Currently, the unit test is designed to support only functional testing
    - Unit Test application is not an OSP-based application. Therefore, some methods related with OSP application framework, such as methods of the Tizen::Base::String class, can behave incorrectly.
    - The Test Explorer does not work if the project files have not been changed. In this case, edit the code manually, build the project, and run it.
  - Valgrind
    - Valgrind profiling is only supported in the Emulator

- Emulator

  - If you run the Emulator with Oracle Java 1.7 or higher on Mac OS, it may result in your host machine getting slower. If you run two or more Emulator VMs, Occasionally booting the Emulator does no work.

  - Your Ubuntu desktop session can be occasionally logged out when launching the Emulator Manager, if you use NVIDIA graphic card. In that case, install the latest driver directly from the NVIDIA website.

  - OpenGL ES acceleration can have problems in certain environments:

    - Windows XP/7 with Intel motherboard integrated card
    - Ubuntu 11.10 with Intel CPU/motherboard integrated card

    If this occurs, you can launch the Emulator by switching off the HW GL acceleration in the Emulator Manager. However, you cannot use any GL-related applications, such as a Web browser.

  - When you launch the Emulator on Windows, you can get a "failed to allocate memory" error. In that case, try the following:

    - Increase the user area of the virtual memory in the system to 3 GB by running the "bcdedit /set increaseuserva 3072" command on the console with administrator rights (Windows 7 only)
    - Close some other programs and try to launch the Emulator again
    - If you have set the RAM size as 768 or 1024 MB for the VM in the Emulator Manager, change the RAM size to 512 MB

  - Using the Emulator with SOCKS (SOCKet Secure) proxy on Mac OS X can cause unexpected problems

  - You cannot play all video files that are linked in YouTube or other Web pages and require the browsers registered to them

  - The Emulator log file (emulator.log) can become too large if you run the Emulator for a long time

- Dynamic analyzer

  - A screenshot is sometimes not taken if the screen or scene change is implemented using an animation technique
  - The analysis of the IME and Service Applications is not supported

- Install Manager

  - A shortcut is not provided in Mac OS X

