# Tizen 2.3

Release Date: 09 Feb, 2015

The Tizen 2.3 release provides developers with the Tizen kernel, device drivers, middleware subsystems, and Web/Native APIs, necessary to develop future Tizen compliant solutions.


## Release Details

- [Getting source code](http://review.tizen.org/git/) (Tizen 2.3 source codes are under **tizen_2.3** branch.)

- [Getting binaries and images](http://download.tizen.org/releases/2.3)

- [How to flash to a device](https://wiki.tizen.org/wiki/Flash_Tizen_2.3_Image_to_Reference_Device)


## SDK Release Notes

### Tizen 2.3 Rev3 (Jul. 6, 2015)

#### IDE and Tools

##### Fixed Bugs

- Native IDE
  - The compression library issue making the tpk size too big due to the defective compression has been fixed.
  - Invalid file permission issue when unzip the tpk has been fixed. This issue can cause the application is rejected due to signing failure from Tizen seller site.



### Tizen 2.3 Rev2 (Feb. 13, 2015)

#### IDE and Tools

##### New Features

- Native UI Builder
  - The Native UI Builder is a WYSIWYG Editing tool for Tizen Native App developer. It can help the developer to develop Tizen UI Application easily.
  - The Native UI Builder has the following features:
    - Project Template
      - 2 Native UI Builder Application Templates are added.
    - WYSIWYG Editor
      - 2 Native UI Builder Application Templates are added.
      - Widget Palette.
      - Drag-and-drop widget placement, moving, deleting, and visual layout editing.
      - ­Copy/cut/paste, and undo/redo, align, match size.
      - ­Guidelines
      - ­Preview mode
    - Properties View
      - Attributes editing through effective graphical UX.
      - Creating a visual UI event binding with you event handler code and moving to the event handler code.
    - Navigation View
      - Showing the view thumbnail.
      - You can switch editing view by clicking the view thumbnail.
    - Outline View
      - Hierarchical structure of the view.
    - Resources View
      - Resource management – import/copy/paste/delete resources.
      - You can edit the resource property of the widgets using drag and drop.
- Emulator, Web simulator, Native UI Builder, Web UI Builder
  - The qHD(540X960) resolution is additionally supported.

##### Changed Features

- Native IDE
  - Building and packaging
    - Multi-project packaging. You can develop a UI project and service or shared library projects as a package.



### Tizen 2.3 Rev1 (Dec. 2, 2014)

#### Tizen Platform Mobile Profile

##### Web framework

**Changed Features**

- Webkit
  - The unit of Media Query has been changed from phisical pixel to CSS pixel.
  - Now window.screen object returns the values in which the devicePixelRatio is reflected.

##### Native Framework

**Changed Features**

- Network API Module
  - The connection_reset_profile(…) has been changed from synchronous API to asynchronous API.
  - The behavior of NFC set activiaton via app control has been changed to return the result and end automatically after the operation.
  - The package_manager_clear_cache_dir(), package_manager_clear_all_cache_dir(), package_manager_get_package_size_info() and package_manager_get_total_package_size_info() have been removed for the security reason.
  - Bluetooth system popup has been added for phone book request and message request operations.

**Fixed Bugs**

- Network API Module
  - The issue of the bluetooth pairing did not working properly on occasion has been fixed.
  - Connection API privilege issues have been fixed.

#### IDE and Tools

##### New Features

- Web UI Builder
  - Migration
    - Added Migration wizard for project(tizen 2.2.1).
  - N-Screen
    - Added Configuration Editor (UI Builder project configuration editor).

##### Changed Features

- Web UI Builder
  - Page Designer
    - Added page combo in toolbar.
    - Added “Set positon” in context menu.
  - Pages View
    - Changed page template wizard. (create, import, export template wizard).
    - Changed context menu(“Add Basic Page” From “Add Empty Page”).
    - The position of page name was changed to the top of the page in pages view.
  - DataBinding view
    - Added “Set Target” in toolbar of Data Model panel.
  - N-Screen
    - Changed devices list.
  - Animation
    - Added custom animation..
  - Changed timeline icon.


- Tools
  - Added “—strip” option to native “package” command.
  - Removed Default Author Certificate.
  - Added web privilege "[http://tizen.org/privilege/internet](https://tizen.org/privilege/internet)".

##### Fixed Bugs

- Fixed less compiler’s bug that cannot compile less resources.
- Removed xwalk’s launch command and option page.
- Fixed to show logs normally for the service applications.


- Emulator
  - In Ubuntu, added warning message if host’s graphic driver is invalid for emulator.(Gallium driver). Pop-up dialog is showed when.
    - Emulator is installed.
    - Launch emulator with emulator-manager.
  - IntelHaxm
    - Skip IntelHaxm installation if the same version of the driver has already been installed.
- Tools
  - Added to generate .exportMap file when native project is created.
  - Fixed rootstrap bug that causes some compile error.
- Web UI builder
  - Fixed UI Builder’s bug that occurred tool exception sometimes.

##### Known Issues

- IDE
  - o In the MacOS 10.9 version, the File dialog button may not respond from the second time onwards:
    - [https://bugs.eclipse.org/bugs/show_bug.cgi?id=433486](https://bugs.eclipse.org/bugs/show_bug.cgi?id=433486)





### Tizen 2.3.0 (Nov. 8, 2014)

#### Tizen Platform Mobile Profile

##### Web framework

**New Features**

The following Mobile Web Device APIs have been added in this release to allow a richer variety of features to be implemented in mobile Web applications:

- Web Device API
- The  following Mobile Web Device APIs have been added in this release to allow a richer variety of features to be implemented in mobile Web applications:
  - Account API (tizen.account)
    - Manages accounts within the device. For example, applications can use this API to create an account or change account information.
  - Archive API (tizen.archive)
    - Creates an archive file and operates on it. For example, applications can use this API to extract files from an archive or add a file to an archive.
  - Badge API (tizen.badge)
    - Overlays an image with the number of unread notifications for an application on the application’s Home screen icon. The image is known as a badge.
  - Bluetooth API
    - Manages Bluetooth connections. An application must now request permission from the user to use Bluetooth. Previously, you were able to enable Bluetooth without user consent, but that API is to be deprecated soon. To request permission, you must now launch the Bluetooth settings option from within your application so that the user can choose to enable Bluetooth. Similarly, applications must no longer change a device’s Bluetooth visibility, as this API is also to be deprecated.
  - Exif API (tizen.exif)
    - Manipulates exchangeable image file format (Exif) metadata.
  - FM Radio API (tizen.fmradio)
    - Manages FM radio operations, such as switching the FM radio on or off, scanning frequencies, and tuning up or down.
  - Human Activity Monitor API (tizen.humanactivitymonitor)
    - Provides support for pedometers, heart rate monitors (HRMs), and GPS tracking features to determine the device’s geographical location and changes, such as velocity changes. It also supports the detection of “wrist-up” motions. For example, if a smartwatch user rotates their wrist to look at their watch screen, the application can detect this and present content on the screen.
    - Only HRMs are supported on the Tizen 2.3 mobile and wearable Emulator.
  - MediaKey API (tizen.mediakey)
    - Provides methods to handle multimedia keys, such as the volume control or pause buttons on a Bluetooth headset connected to the Tizen device.
  - Sensor API (tizen.sensorservice)
    - Supports light, magnetic, pressure, proximity, and ultraviolet sensors.
    - All sensor types are supported on the Tizen 2.3 mobile and wearable Emulator through the Event Injectors.
  - Sound API (tizen.sound)
    - Controls the sound volume level for various sound types, such as system sounds, media playback audio, notifications, and alarms. It also gets information about the sound mode of the device, such as whether it is set to the mute or vibrate mode.
- The following features have been added to the existing Mobile Web Device APIs in this release:
  - Calendar API
    - The feature to use calendars from multiple accounts has been added. This is useful because you can create, add, or remove calendars from different accounts by using their account ID.
  - CallHistory API
    - The device’s local phone number (calling party) attribute can now be added to the call history information. This is particularly useful in dual SIM devices.
  - Contact API
    - The feature to use contacts from multiple accounts has been added. This is useful because you can create, add, or remove contacts from different accounts by using their account ID.
    - The following attributes (among others) have been added for individual contacts: relationship, messenger address, contact message alert setting, and contact vibration pattern URL.
  - Content API
    - The 'isFavorite' attribute has been added to the Content interface to mark favorite content.
    - The playlist feature has been added so that you can add, remove, and update your favorite media content.
  - Data Synchronization API
    - From Tizen 2.3, this API is optional for Tizen mobile devices.
  - Filesystem API
    - The 'camera' virtual path has been added to make it easier to access the pictures and videos taken by a device.
  - Messaging API
    - The feature to select which SIM card to use when sending an SMS had been added to support devices that can use multiple SIM cards.
  - NFC API
    - The NFC card emulation feature has been added.
    - The feature to turn NFC on and off has been deprecated. Instead, you must launch the NFC settings option from within your application to allow the user to choose to enable NFC.
  - Push API
    - The feature to retrieve unread push notifications when your application is connected to a push service has been added.
  - Secure Element API
    - The feature to get received data from the application select command (getSelectResponse()) has been added.
  - System Information API
    - The new profile name enum values (MOBILE, WEARABLE) have been added to be used in the application manifest (config.xml) to indicate which device types your application can support. Note that the previous enum values (MOBILE_FULL and MOBILE_WEB in SystemInfoProfile) have been deprecated.
    - The getCapabilities() method has been replaced with getCapability() and must be used to retrieve the device capabilities.
    - The feature to get information about multiple system properties, such as dual SIM card capabilities, has been provided. For example, in the previous API, you were able to retrieve the information for a single SIM card only; however, now you can get an array of available SIM cards on the device.
    - The feature to get memory state information, total memory size, and available memory size has been added. You can query the total memory on the device as well as the currently available memory in bytes.
    - The DUID has been replaced with tizen ID, which is a randomly-generated value based on the model name.
    - The feature to obtain the Wi-Fi MAC address information has been added.
  - TBM Surface API
    - The feature to get low-level graphic buffer which is provided by system has been added.
  - Time API
    - The feature to register and unregister callbacks to receive notifications of device time, date, or time zone changes has been added.


- Web Runtime
  - The Dynamic Box has been enabled.
    - Note that the Dynamic Box Viewer is only supported on the reference target device, not on the Emulator.
- Web UI Framework (TAU)
  - The navigation bar winset has been added.
    - The navigation bar with a history can be used through the <nav data-role=”navigation”> element.
  - The select menu winset has been added.
    - The select menu with the tizen theme can be used through the <select name="select-custom-1" data-native-menu="false"> element.

**Changed Features**

- Web UI Framework (TAU)
  - The base library has been changed to TAU from jQM. TAU API use is recommended.
  - The library JS path has been changed from tizen-web-ui-fw/{version}/js/tizen-web-ui-fw.js to lib/tau/mobile/js/tau.js.
  - The default theme file path has been changed from tizen-web-ui-fw/{version}/theme/default/theme.css to lib/tau/mobile/theme/default/tau.css.
  - The date-time picker and multimedia view widgets have been deprecated. Use the HTML standard instead (input, video, and audio elements).
  - The gallery3D, split view, and virtual grid widgets have been deprecated.

**Fixed Bugs**

- Web UI Framework (TAU)
  - The issue of the ‘refresh’ method of the listview winset not working properly has been fixed.
  - The broken button style has been fixed.

##### Native Framework

The Tizen platform provides a new API for native applications in Tizen 2.3, replacing the previous Tizen 2.2.1 Native API. The primary development language for native applications has changed from C++ to C. However, the C++ standard library has been provided as an open source library, so C++ can still be used to create the application logic that does not use any Tizen platform features. This big change has been made for the following reasons:

- The Tizen native framework currently only supports the mobile profile. However, in the near future, multiple other device profiles, such as wearable and TV will be supported. A new Native API is required to ensure that the native framework is lightweight and fast to run well on both low- and high-end profiles and devices.
- With the new native framework, minimal porting effort is required to run native applications on multiple Tizen device profiles.
- Improved scalability, and fast, themeable, and easily customizable graphics are now possible by using the Enlightenment Foundation Libraries (EFL).
- More than 10 open source libraries are now available to 3rd party applications through the native framework. This is particularly advantageous for developers who are already familiar with some of these libraries, because they can quickly add features and use previous written code in certain cases.

Note that you cannot use the new Tizen 2.3 SDK to develop native applications that have been written with the older Tizen SDKs. If you want to develop a native application written with an older Tizen SDK, rewrite your application with the new Tizen 2.3 SDK. The signature changes of Native APIs from Tizen 2.3 Beta to Tizen 2.3 release can be found from [here](http://download.tizen.org/misc/change-log/Native%20API%20Changes.pdf).

The new Tizen Native API includes the following API modules and features:

- Application Framework API Module
  - Application model
    - The UI application model.
    - The service application model. Service applications run in the background without a graphical user interface.
  - Application controls
    - The framework to share application functionalities with other applications.
    - Explicit and implicit application control resolution. This enables you to specify a specific application or give the user a choice of applications when launching another application from your application for a specific task.
  - Data controls
    - The framework to exchange data between applications by allowing an application to query the public database of another application that has opted to be a data provider.
  - Package management
    - Retrieving information about installed packages.
    - Application-specific metadata in the application manifest.
    - Package filtering and package application filtering to get an installed package list more effectively.
    - Retrieving package information from a specific Tizen package file.
  - Message port
    - Sending messages to the message ports of another application.
    - Receiving messages from other applications.
    - Trusted communication between applications. This is allowed only if both applications are signed with the same certificate.
  - Notification
    - Text notifications on the status bar.
    - Ongoing notifications, such as when a download is in progress.
    - Additional notification functionality to customize each notification message. For example, the notification title, icon, and sound can be customized. Furthermore, thumbnail and multiline-type notifications are supported.
    - Removing individual notifications.
  - Badge
    - Overlaying an image with the number of unread notifications for that application on the application’s icon.
    - Setting and getting the value and visibility of the badge.
  - Bundle
    - The small string-based dictionary abstract data type.
    - Creating and managing a small dictionary for passing information among modules or processes through inter-process communication methods, such as message port.
- Context API Module
  - Activity recognition
    - Recognizing user activities, such as walking, running, or being in a vehicle with a device.
    - Reacting to recognized user activities.
  - Gesture recognition
    - Recognizing gestures, such as tap, shake, snap, and tilt.
    - Reacting to recognized user gestures.
- Content API Module
  - Media content
    - Managing, inserting, updating, or removing content information, such as file attribute metadata, playlists, and custom data.
    - Retrieving all content associated with a media directory when searching for content information.
    - Extracting metadata, such as EXIF and ID3 tags, from images, audio, and video files.
    - Scanning for a file or directory to synchronize content information with the local content database.
    - Enabling and disabling content database change notifications.
  - Download manager
    - Downloading content using HTTP.
    - Enabling and disabling download notifications.
    - Setting the allowed network type.
    - Managing the HTTP header fields.
- Messaging API Module
  - Message management
    - Creating, sending, and receiving SMS messages.
    - Searching for SMS and MMS messages in the inbox, sentbox, and outbox individually or in all message boxes together.
    - Sending and receiving WAP push messages.
  - Email
    - Creating, sending, and receiving email messages.
    - Setting email attributes, such as the email subject or recipients.
  - Push
    - Connecting to a push service.
    - Receiving push notification data.
- Base API Module
  - Calendar data (utils-i18n)
    - Converting the date, time, and calendar fields using the Gregorian calendar (used by most of the world), depending on the device locale.
    - Managing time zone information with daylight saving time (DST).
  - Formatting data (utils-i18n)
    - Formatting numbers, currencies, dates, and time depending on the device locale.
  - Data types and collections
    - Supporting data types and collections provided by the Eglibc, Glib, and C++ Standard Library open source libraries.
  - Utility functions
    - Supporting utility functions provided by the Glib, C++ Standard Library, and Minizip open source libraries.
  - Threads and synchronization mechanisms
    - Supporting thread and synchronization mechanisms provided by the Glib open source library.
- I/O API Module
  - I/O support by open source libraries, such as Eglibc, Glib, Sqlite, and C++ Standard Library
    - Supporting file and directory functions provided by the Eglibc and Glib open source libraries.
    - Supporting database features provided by Sqlite3.
- Multimedia API Module
  - Camera
    - Displaying a live preview and capturing a still image.
  - Image util
    - Decoding and encoding JPEG images. Tools, such as crop, resize, and rotate, are also provided to transform images.
  - Metadata extractor
    - Extracting metadata information from a media file.
  - Player and recorder
    - Playing audio and video from media files that are stored on a device or streamed over a network.
    - Providing audio and video pre-processing filter APIs. Attributes, such as recording filename and file format, can be configured.
    - Playing DTMF tones (with the tone player).
    - Playing Waveform Audio File (WAV) format files using the WAV player.
    - Providing low-level audio playback and capture.
    - Recording audio and video.
  - Sound manager
    - Checking and controlling output volumes.
    - Enabling and disabling volume change notifications.
    - Determining sound session policies, such as how to handle sound session interruptions.
  - Video util
    - Transcoding or converting media files from one encoding to another.
  - Media codec
    - Encoding and decoding audio and video data by having direct access to the media codec on the device.
  - Media tool
    - Handling audio and video packet buffers. These buffers are utilized by the Multimedia API modules.
  - Radio
    - Starting and stopping radio.
    - Seeking radio frequencies.
    - Scanning radio signals.
    - Getting the radio state.
- Network API Module
  - Bluetooth
    - Support for the following:
      - GAP (Generic Access Profile)
      - Audio Profiles (HFP, HSP, and A2DP)
      - GATT(Generic Attribute Profile)
      - OPP (Object Push Profile)
      - HID (Human Interface Device Profile)
      - HDP (Health Device Profile)
      - SPP (Serial Port Profile)
    - Note that Bluetooth features are only supported on reference target devices, not on the SDK Emulator.
  - Connection management
    - Providing the custom connection management service API.
    - Selecting a preferred connection.
    - Providing an internet protocol (IP) address that represents a network resource or service.
  - Wi-Fi
    - Managing the local Wi-Fi device.
    - Note that Wi-Fi features are only supported on reference target devices, not on the SDK Emulator.
  - Socket and HTTP
    - Supporting socket and HTTP features provided by the openSSL and Curl open source libraries.
- Security API Module
  - Supporting a wide range of cryptographic algorithms, certificate handling mechanisms, hash functions, and key management algorithms covered by the openSSL open source library
  - Key manager
    - The secure repository (protected by a user’s password) for keys, certificates, and sensitive data of the users and their applications.
  - Privilege info
    - Reading information of a given privilege name.
  - Smack
    - A significant number of rules have been revised to allow required access only.
    - Supporting better access control in the kernel space with Map Smack rules with native or Web privileges.
- Social API Module
  - Account manager
    - Managing the account information from multiple accounts.
    - Accessing account and account provider information.
  - Contacts
    - Managing and searching contacts in the device storage.
    - Importing and exporting vCard files.
    - Aggregating contacts.
    - Managing user profiles.
    - Providing bulk operations for adding, updating, and removing contacts.
    - Storing application launch data in contacts.
    - Providing extra categories for data.
  - Calendar
    - Managing and searching personal schedules and task information in the device storage.
    - Importing and exporting vCalendar files.
    - Updating an event instance.
    - Providing absolute time for reminders.
- System API Module
  - Device
    - Listening and handling events for various devices, such as battery, display, haptic, led, and power services.
  - Dlog
    - Sending and filtering log output from the Dlog service.
  - Storage
    - Providing information, such as total available space of internal and external storages.
    - Getting a path for the media directory.
  - Runtime info
    - Providing runtime information, such as hardware availability. For example, obtaining information about whether a USB device is connected.
  - System settings
    - Accessing various system settings, such as the current language.
  - Sensor
    - Starting and stopping receiving acceleration, gravity, gyroscope, humidity, light, magnetic, orientation, pressure, proximity, and temperature sensor data.
    - Getting and setting sensor options.
  - System info
    - Providing system information, such as API and platform versions, supported device features, and screen dimensions.
- Telephony API Module
  - Telephony information
    - Getting information on the current call type, status, and event.
    - Getting information on the current network, such as the cell ID, LAC, and PLMN.
    - Getting information on the current network status, such as the availability of the call and data services and roaming.
    - Getting information on the inserted SIM card.
- UI API Module
  - EFL (UI core)
    - UI controls
      - Providing containers, such as forms, panels, split panels, and windows, which can be used to hold different UI components.
      - Providing windows, such as frames, pop-ups, and message boxes, which can be used to support layered display surfaces for UI components.
      - Providing UI components for user interaction, such as buttons, lists, grids, panes, labels, sliders, tab bars, and various date, time, and color pickers.
    - Scalable UI
      - Developing and migrating multi-resolution applications with utilities, such as the layout manager, logical coordinates, and automatic resource selection.
    - Themes
      - Providing a set of themes. Each application can select a theme to use.
    - Effects
      - Providing 3D effect animations, such as page flipping and various rotations.
    - Multi-point touch and gestures
      - Providing multi-point touch events and touch gestures.
    - Scene management
      - Managing form life-cycles, and making transitions between forms or panels easier and smoother.
    - Animation
      - Providing key frame-based animation of UI controls, such as view or panel transitions.
    - SW accessibility
      - Providing a container for the customization of the screen reader functionality for the visually handicapped users.
    - Focused UI
      - Displaying and moving the UI control focus by touch gestures and the HW keyboard.
    - 2D graphics
      - Providing platform-independent 2D graphics.
      - Providing graphics rendering methods and data structures.
      - Providing floating point matrix and vector manipulation functions.
    - 3D graphics
      - Supporting OpenGL ES 1.1 and 2.0, which are subsets of the OpenGL 3D graphics API that has been designed for mobile devices.
      - Supporting OpenGL rendering on drawing canvasses.
  - Tizen buffer management
    - Providing a low-level graphics buffer.
    - Getting the format list supported by the system.
    - Accessing the surface with the access type.
    - Supporting multiple plane graphic buffers.
    - Getting information about surface and planes.
- UIX
  - Speech-To-Text (STT) service to recognize text from voice
  - Text-To-Speech (TTS) service to synthesize voice from text and play synthesized sound data
- Web API Module
  - The Tizen Native API provides EFL WebKit APIs for:
    - Web browsing
      - Loading and rendering a page from a network or local storage.
    - Page navigation list
      - Listing the visited pages.
    - Page control
      - Getting the size of a Web page.
      - Scrolling a Web page.
      - Clearing the navigation history.
    - Webview configuration settings
      - Managing features, such as enable JavaScript, user agent, load image, encoding, and font size.
      - Providing private browsing control.
    - Cookie and cache control
      - Clearing the cache and cookies.
- Open Source Libraries
  - The following open source libraries are additionally supported in the 2.3 release:
    - libEXIF (0.6.21): Accessing EXIF meta information in image files.
    - Json-glib (0.10.4): Manipulating JSON documents.
    - Glib (2.32.3): Basic programming facilities.
    - Curl (7.28.1_24): Client side URL data transfer library.
    - libXML2 (2.7.8): Parsing XML documents.
    - Fontconfig (2.9.0) and Freetype (2.4.9): Rendering text and fonts.
    - Minizip (1.2.5): Processing files in the ZIP format.
    - Sqlite (3.7.13): Lightweight SQL database.
    - Cairo (1.12.14): 2D graphics library.
    - openssl (1.0.1g_1): Library for basic cryptographic functions.
    - libOAuth (0.9.4): Open standard for authorization.

The new Tizen Native API does not support the following features in the 2.3 release (but they are expected in a future release):

- Image recognition and QR code recognition (Tizen::Ui in the 2.2.1 Native API)
- Quick Panel Frame and Dynamic Box (Tizen::Shell in the 2.2.1 Native API)
- Serial port (Tizen::System in the 2.2.1 Native API)
- IME and downloadable IME (Tizen::UI in the 2.2.1 Native API)

#### Tizen Platform Wearable Profile

The wearable profile provides a complete implementation of the Web API optimized for wearable devices. It includes the WebKit, a layout engine designed to enable Web browsers to render Web pages. It also provides a runtime for Web applications.

##### Web Framework

**New Features**

- Web Device API


- The following Wearable Web Device APIs have been added in this release to allow a richer variety of features to be implemented in wearable Web applications: 

  - Badge API (tizen.badge)

    - Overlays an image with the number of unread notifications for an application on the application’s Home screen icon. The image is known as a badge.

  - Human Activity Monitor API (tizen.humanactivitymonitor)

    - #### Provides support for pedometers, heart rate monitors (HRMs), and GPS tracking features to determine the device’s geographical location and changes, such as velocity changes. It also supports the detection of “wrist-up” motions. For example, if a smartwatch user rotates their wrist to look at their watch screen, the application can detect this and present content on the screen.

    - Only HRMs are supported on the Tizen 2.3 mobile and wearable Emulator.

  - MediaKey API (tizen.mediakey)

    - Provides methods to handle multimedia keys, such as the volume control or pause buttons on a Bluetooth headset connected to the Tizen device.

  - Sensor API (tizen.sensorservice)

    - Supports light, magnetic, pressure, proximity, and ultraviolet sensors.
    - All sensor types are supported on the Tizen 2.3 mobile and wearable Emulator through the Event Injectors.

  - Sound API (tizen.sound)

    - Controls the sound volume level for various sound types, such as system sounds, media playback audio, notifications, and alarms. It also gets information about the sound mode of the device, such as whether it is set to the mute or vibrate mode.

- The following features have been added to the existing Wearable Web Device APIs in this release, in addition to new features in the Alarm, Application, Package, Download, Message port, Power, and System setting API modules:

  - Content API
    - The 'isFavorite' attribute has been added to the Content interface to mark favorite content.
    - The playlist feature has been added so that you can add, remove, and update your favorite media content.
  - Filesystem API
    - The 'camera' virtual path has been added to make it easier to access the pictures and videos taken by a device.
  - System Information API
    - The new profile name enum values (MOBILE, WEARABLE) have been added to be used in the application manifest (config.xml) to indicate which device types your application can support. Note that the previous enum values (MOBILE_FULL and MOBILE_WEB in SystemInfoProfile) have been deprecated.
    - The getCapabilities() method has been replaced with getCapability() and must be used to retrieve the device capabilities.
    - The feature to get information about multiple system properties, such as dual SIM card capabilities, has been provided. For example, in the previous API, you were able to retrieve the information for a single SIM card only; however, now you can get an array of available SIM cards on the device.
    - The feature to get memory state information, total memory size, and available memory size has been added. You can query the total memory on the device as well as the currently available memory in bytes.
    - The DUID has been replaced with tizen ID, which is a randomly-generated value based on the model name.
    - The feature to obtain the Wi-Fi MAC address information has been added.
  - Time API
    - The feature to register and unregister callbacks to receive notifications of device time, date, or time zone changes has been added.

- Web Runtime

  - 3 new application types have been added to the 2.3 wearable profile (WebIME, ClockWidget, and Web Service Application):
    - The following configuration elements have been added to support the Web IME application:
      - <tizen:ime>, <tizen:uuid>, <tizen:languages>, and <tizen:language>
    - Web service application type is provided to support background running without the UI. The following configuration element has been added to support the Web service application:
      - <tizen:service>
    - The ClockWidget application type is provided to customize the Home screen. The following configuration element has been added to support the ClockWidget application:
      - <tizen:category name="[http://tizen.org/category/wearable_clock](http://tizen.org/category/wearable_clock)" />
  - The Web Dynamic Box has been added to provide content on the Home screen:
    - The following configuration elements have been added to support Web Dynamic Box:
      - <tizen:app-widget>
  - The <tizen:category> element has been added to define the categories to which an application belongs.
  - The application ID constraint has been added to the Web application packages (widgets):
    - Once the application has been published, the ID cannot be changed.

- Web UI Framework (TAU)

  - A new Web UI framework, called TAU, has been added to the 2.3 wearable profile. This JS framework is written to optimize the application launching time based on pure JavaScript replacing JQueryMobile.
    - Page navigation and basic event handling support as pure JavaScript library have been added.
    - CSS themes and resources for reference Web UI widgets are supported:
      - 2 resolutions are supported: 320x320 and 360x480
    - Advanced widgets, including virtual list, indexed scroll, and swipelist, have been added.
    - Reflection of the system font change is supported.
    - Widget test application for the wearable UI has been added.

- Webkit

  - The layout engine of the 2.3 wearable profile is based on WebKit2 and its APIs are selected to support typical uses for a wearable device.
    - W3C/HTML5 specifications support:
      - DOM/Media/Graphics: HTML5 audio/video element, HTML5 Forms (Partial), Session History API, DOM/JS-related HTML5 enhancements, iframe sandbox attribute, HTML5 2D Canvas, Web Speech (TTS only), and Scalable Vector Graphics.
      - CSS3: CSS3 2D Transforms (H/W accelerated), CSS3 3D Transforms (H/W accelerated), CSS3 Animations (H/W accelerated), CSS3 Transitions (H/W accelerated), CSS3 Colors, CSS3 Backgrounds and Borders (Partial), CSS3 Flexible Box Layout (Partial), and CSS3 User Interface (Partial).
      - Device: Touch Events, CSS3 Media Queries (Partial), Vibration API, getUserMedia API, Battery Status, Device Orientation Events, and Geolocation.
      - Communication: Network access including XHR, and Web Socket.
      - Security: iframe sandbox and CSP1.0 (Partial).
      - Storage: Web Storage, File Reader API, and Indexed DB API.
      - Performance: Web Worker (Partial) and Page visibility API.
    - Changes in W3C APIs:
      - Page visibility API: the “webkit” prefix has been removed: webkitvisibilitychange -> visibilitychange
      - File Reader API: BlobBuilder has been deprecated and replaced by the Blob object
      - The indexed DB flag change: multientry -> multiEntry
    - Khronos specifications support:
      - WebGL and Typed Arrays.
    - W3C Widget specifications support
      - Packaging and Configuration, Digital Signing, and Widget Interface.
    - Camera API support
      - Providing, for example, camera preview, camera setting changes (such as picture size and format), image capture, and video recording.
      - Recording audio.
      - Supporting audio recording formats: AMR and 3GP.
    - HTML5 security policy
      - The behavior on privileges of the HTML5 APIs has been changed.

 

#### IDE and Tools

##### New Features

- Common
  - Provides the multi-profile development environment with a new wearable profile.
  - Upgrades the Eclipse version to Kepler(4.3) SR2.
  - Provides the Eclipse theme for Tizen optionally (configured in Preferences > General > Appearance in the Tizen IDE).
- Web IDE and tools
  - Adds a new wearable profile for wearable application development.
    - Project Wizard provides wearable template and samples.
  - Adds a new Command Bar tool which provides convenient command and is integrated with the IDE.
  - Adds the Javascript unit testing tool based on QUnit.
  - Provides Android keystore certificate support when generating a certificate request.
  - Connection Explorer
    - Adds a new Remote Device Manager tool in the Connection Explorer, providing management features for remotely connected devices.
  - HTML Editor
    - Adds the breadcrumb, advanced content assist, and hover in the HTML Editor.
    - Adds a quick-fix when a file name included in HTML is changed (like .js or .png).
  - Supports compiling LESS (dynamic stylesheet language) and Coffeescript (language that compiles into Javascript).
  - Javascript Editor
    - Supports content assist for some string literal parameters.
    - Supports hyperlink for some string literal parameters.
    - Supports a quick-fix when the file name included in Javascript is changed (like .html, .png, or .css).
  - Configuration Editor
    - Adds the background-support setting in the Tizen tab.
- Web UI Builder
  - Supports the new Tizen Web UI framework (TAU).
  - Adds a new Animator tool providing CSS animation to widgets.
  - Adds a new Data Binding tool providing 2-way binding between the data and view. Currently 6 types of data source and 16 bindable widgets are supported for TAU.
  - Adds a new Resources View tool providing easy editing for setting the image property.
  - Adds a new Widget Snippet function which makes a widget contain some widgets.
  - Supports Page Template in the Page View making a template.
  - Adds a new N-Screen tool providing easy editing for a UI of a predefined resolution.
  - Adds a new CSS Selector tool supporting the CSS Selector to add to the widget from the live DOM.
- Native IDE
  - Adds the native IDE for the Tizen version 2.3, supporting native application development.
  - Building and packaging
    - Supports TPK (Tizen Package File) packaging.
    - Supports author and distributor signing.
    - Supports multi-process application packaging. Multi-process applications enable a hybrid architecture combining UI and service applications.
    - Supports the LLVM 3.4 and GCC tool chains.
  - Adds the PO file editor for i18n.
  - Adds EFL Enventor only in Ubuntu. It supports editing and previewing edc source files.
  - Adds the Potential Bug Detector static analysis tool to help to find bugs in applications.
- Dynamic Analyzer
  - Changes the data collecting mechanism.
  - Adds Network Analysis.
  - Adds OpenGL Analysis.
  - Adds Energy Usage in the Time line view.
- Emulator
  - Adds a new Emulator Control Panel (ECP) tool to replace the Event Injector in the previous version.
    - Supports the device manager, such as Device Tree and Network.
    - Supports virtual inputs, such as Gesture.
    - Supports uninstalling applications.
    - Supports message synchronization between the ECP (UI and CLI tools) and Emulator.
    - Adds the feature to enable/disable host directory sharing in runtime.
    - Adds sensors: pressure, ultraviolet, and heart rate monitor.
    - Adds the “altitude” and “horizontal accuracy” location input values on the manual event injection settings.
  - Adds the EventCast tool enabling you to inject sensor and touch events more intuitively by means of a real target.
- Tools
  - Adds new Command Line Tools.

##### Changed Features

- Install Manager
  - Supports multi-profile installation.
  - Provides UI renewal and improved UX.
  - Offers improved performance.
- Web IDE and tools
  - Certificate
    - Disables the generating author certificate button at Security Profile of preferences, since the process generating the author certificate has changed.
    - Provides a toolbar for generating a certificate request and registering a certificate.
  - Connection Explorer
    - Provides UI renewal and improved UX.
  - Project Explorer
    - Shows the platform profile information with the project name.
    - Shows the content of the wgt file directly.
  - Build and packaging
    - Separates the packaging process from the build process.
    - Provides the context menu of ‘Build Package’.
    - Provides the ‘package’ property and removes the ‘Build’ property.
    - Optimizes Web resources (html, js, css, png) when the ‘Build Package’ command is executed.
  - Web UI Builder
    - Changes the programming model for the new UI FW TAU.
    - Enhances the Properties View.
- Emulator
  - Menu
    - Deletes the host keyboard menu from the pop-up menu and the Emulator Control Panel. From now on, the Tizen platform automatically recognizes a host keyboard when a key event is injected.
  - Emulator Manager
    - Changes the HD (720x1280) resolution density to 306.
  - Emulator Control Panel
    - Enables the sensor, location, and telephony events in the wearable Emulator.
    - Changes the marking map injection from a mouse-double-click to a mouse-left-click on Location.
    - Changes the moving map from a mouse drag to mouse-left-click on Location.
- Dynamic Analyzer
  - Changes the settings dialog UX to select one of the feature templates.

##### Fixed Bugs

- IDE
  - Packaging
    - The OutOfMemoryError at the signing process on a project having large resources has been fixed.
    - The bug at the signing process in case of a Unicode resource name on the project has been fixed.

##### Known Issues

- IDE and Tools
  - Because the old workspace metadata is incompatible due to the major upgrading effect, an IDE crash can occur. Create new workspace to avoid the problem.
  - The Connection Explorer view sometime does not show all running Emulator information.
- Web UI Builder
  - The text functions (ellipsis and line-break) are sometimes displayed differently with an actual operation.
  - Some TAU widgets are not included in the widget palette nor work properly.
  - The selected resolution in the N-Screen View is not applied on the application.
  - In some cases, the designer does not work properly if you modify the HTML code directly.
  - The scroll bar is displayed in the middle of the content area in the Simulator, if the animation applies to the content.
  - The animation does not work properly with N-Screen.
  - The IDE creates a console window when an internal browser has been created in Windows 8.
- Emulator
  - On Windows, depending on your OS theme (such as non-Aero themes and Windows XP themes), a display surface can be erased for a while if the Emulator window is obscured by another window. If you click the Emulator window, the display surface works correctly again.
  - The Emulator skin cannot be drawn properly on Ubuntu, if the graphics driver is not installed or an old version is installed. To fix this issue, upgrade the graphics driver.
  - When the disk storage is full, various incorrect operations can occur.
  - To use the Tizen Emulator, you need, for example, an Intel VTx supported by the CPU, and the latest vendor-provided version of the graphic card driver. Check the prerequisites for the Tizen Emulator from:
    - [https://developer.tizen.org](https://developer.tizen.org)
    - On Ubuntu, if the host machine is using Nvidia Optimus technology, you can set the Tizen Emulator to run with your Nvidia graphics card through the bumblebee project: [https://wiki.ubuntu.com/Bumblebee](https://wiki.ubuntu.com/Bumblebee)
  - The browser for the map of the location tab does not support HTTPS/SSL certificate on Ubuntu.
  - Sound control does not work properly in wearable settings application.
- IDE
  - In the Mac OS 10.9 version, the File dialog button may not respond from the second time onwards:
    - [https://bugs.eclipse.org/bugs/show_bug.cgi?id=433486](https://bugs.eclipse.org/bugs/show_bug.cgi?id=433486)
