# Tizen 2.3.1

The Tizen 2.3.1 release provides developers with the Tizen kernel, device drivers, middleware subsystems, and Web/native APIs, necessary to develop future Tizen-compliant solutions.

## Release Details

- [Getting source code](http://review.tizen.org/git/) (Tizen 2.3.1 source code is in the **tizen_2.3.1** branch.)
- [Getting binaries and images](http://download.tizen.org/releases/2.3.1/)
- [How to flash to a device](https://wiki.tizen.org/wiki/Flash_Tizen_2.3_Image_to_Reference_Device)



## SDK Release Notes

### Tizen 2.3.1 Rev1  (Nov. 13, 2015)

>  **Note**
>
>  The Tizen 2.3.1 rev1 SDK only supports the Tizen 2.3.1 Platform. The upcoming Tizen 2.4 rev1 SDK will support both the Tizen 2.3.1 and 2.4 Platforms. The Tizen 2.3.1 rev1 SDK will be available until the Tizen 2.4 rev1 SDK is released.

#### IDE and Tools

**New Features**

- Native UIB (only for Ubuntu)
  - Supports Wearable Profile
    - 320 * 320, 360 * 360, 360 * 480 square resolutions for wearable devices have been added.
    - 360 * 360 circle resolution for wearable devices has been added.
  - Supports the making of a snippet (such as custom widget) by combining ready-made UI components. Snippets work the same as other ready-made UI components.
- CLI
  - Supports the packaging, installing, running, and uninstalling of features for 2.3.0 projects.

**Changed Features**

- TAU (Tizen Advanced UI Framework)
  - TAU for web UI controls and some web sample applications have been updated to support the latest Design guide.
    - The sizes of the following components got smaller.
      - List item, Checkbox, Radio button, Toggle switch
    - The size of header text is changed
    - Visual interaction of button is changed
    - Circular edge shadow is added to popup component
    - The colors of the following are changed
      - Selector, Circular index scrollbar
- Common
  - To improve security for connected Tizen devices, the execute permission of some features, such as Dynamic Analyzer, SDBD, etc., which control the devices, has been changed from the root/administrator to the developer.

**Fixed Bugs**

- Native IDE
  - The bug, which IDE stops responding when an Android device is connected, has been fixed.
- Emulator
  - The bug, which IDE fails to install the Tizen HAX driver on a PC if the Android HAX driver is already installed, has been fixed.

**Known Issues**

- Common
  - Tizen IDE for MAC OS X has dependencies on Apple JDK. To support legacy java software on MAC OS X, download and install the Java for Mac OS X 2015-001 from [https://support.apple.com/kb/DL1572](https://support.apple.com/kb/DL1572)
- Emulator
  - To use the Tizen Emulator, you should install an Intel VTx supported by the CPU, and the latest version of the graphic card driver provided by the vendor. Check the prerequisites for the Tizen Emulator from: 
    - [https://developer.tizen.org/downloads/sdk/installing-sdk/prerequisites-tizen-sdk](https://developer.tizen.org/downloads/sdk/installing-sdk/prerequisites-tizen-sdk).
    - If the host machine is using the Nvidia Optimus technology on either Ubuntu or Windows, you must set the Tizen Emulator to run with your Nvidia graphics card. If you use Ubuntu, check the bumblebee project ([https://wiki.ubuntu.com/Bumblebee](https://wiki.ubuntu.com/Bumblebee)). If you use Windows, you should select "High Speed NVIDIA Processor" as "Preferred Graphics processor" in the Nvidia control panel.
    - On Ubuntu, if the graphics driver is outdated, your Ubuntu desktop session may be occasionally logged out when launching the Emulator Manager. Or the Emulator skin may be drawn improperly. Please check the prerequisites and upgrade the latest graphics driver.
  - On Ubuntu 14.04, the shortcut menu can appear sometimes transparently.
  - On Windows, depending on your OS theme (such as Non-Aero themes and Windows XP themes), a display surface can be erased for a while if the Emulator window is covered by another window. If you click the Emulator window, the display surface runs correctly again
  - On Windows, if a memory allocation error occurs while executing the Emulator, try the following: 
    - Close some other programs and try to launch the Emulator again
    - If the RAM size is set as 768 or 1024 MB for the VM in the Emulator Manager, change the RAM size to 512 MB.
    - Increase the user area of the virtual memory in the system to 3 GB by typing **bcdedit /set increaseuserva 3072** on the console with administrator rights (Windows 7 only) andreboot.
  - If you use a MacBook Pro which has both Intel HD and NVidia GPUs, when you execute the Emulator with the **OpenGL ES ver. v1.1 & v2.0** option, the Emulator may be unexpectedly terminated. Please use the **OpenGL ES ver. v2.0 & v3.0 **option.
  - The Dynamic Analyzer may not recognize the Emulator the first time but it will recognize it next time.



### Tizen 2.3.1 (Sep. 3, 2015)

#### Tizen Platform Wearable Profile

The wearable profile provides a complete implementation of the Web APIs optimized for wearable devices. It includes WebKit, a layout engine designed to enable Web browsers to render Web pages. It also provides a runtime for Web applications. From Tizen 2.3.1, it provides native APIs for wearable native applications.

The wearable profile’s features include:

##### Web Framework

###### Web Device API

The following wearable Web Device APIs have been added in this release to allow a richer variety of features to be implemented in wearable Web applications:

- ##### Archive API (tizen.archive)

  - Creates an archive file and operates on it. For example, applications can use this API to extract files from an archive or add a file to an archive.
- Exif  API (tizen.exif)
  - Manipulates exchangeable image file format (Exif) metadata.
- NFC API (tizen.nfc)
  - Provides Near Field Communication (NFC) service to enable information exchange between NFC-enabled devices.
  - Provides a new NFC host-based card emulation feature.
- Secure Element API (tizen.seService)
  - Enables the application to communicate with several Secure Elements (SE).
- Push API (tizen.push)
  - Provides functionality to receive push notifications.
- Bluetooth API (tizen.bluetooth)
  - Provides functionality to control Bluetooth.
  - Provides a new advertising feature for remote devices (including Bluetooth LE devices).
  - Provides a new feature to allow the application to act as a GATT client (Generic Attribute Profile  client).

The following features have been added to the existing wearable Web Device APIs in this release:

-  Sensor APIEnables the application to get raw HRM sensor data.
-  Sound APIEnables the application to check whether a specific sound device type is connected.

######  Web Runtime

The following custom event has been added in this release to give notifications on detected rotary detents:

- Custom event: rotarydetent

The following custom events and configuration have been added to support the ambient mode for watch applications:

- Configuration: ambient_support
- Custom event: ambientmodechanged, timetick

The Web Dynamic Box feature has been removed from this release.

######  Web UI Framework (TAU)

The Tizen platform also provides new components for wearable Web applications in this release.

**New Features**

- Support for wearable devices with a circular screen has been added.
  - UI components for wearable devices have been enhanced to support a circular screen. You can make an application that runs on both rectangular and circular screens with a single source code.
  - Drawer, Marquee, PageIndicator, and Selector have been added as wearable common UI components.
  - Circular Progressbar and SnapListview (specialized for a circular screen) have been added.
- Documents and samples have been updated.
  - The “Support for Circular UI” section has been added. It includes descriptions for the new UI components and migration guides for users who want to make their TAU-using applications work on a circular screen.
  - Samples for the new UI components and information on how to use rotary events have been added.

**Changed Features**

- In SectionChanger, the fillContent option has been added to allow sections to be partially displayed.
- In Popup, maximizing pop-ups to the screen dimensions is supported through its option.
- In Page/Popup, you can enable the scrolls using the tau.defaults.enablePageScroll and tau.defaults.enablePopupScroll variables.
- In Page, the ui-scroller element has been added as a child of the page element.
- TAU license has been changed to the Flora license from the MIT license.
- Expandable Header Concept has been removed.
- MoreOption can be implemented with the Popup and Selector components.

**Fixed Bugs**

- Gesturing bugs, which occurred when dragging on a nested SectionChanger, have been fixed.
- Differences between codes in the documents and their corresponding samples have been fixed.
- AnchorHighlight bugs, which occurred when removing the activeClass, have been fixed.
- According to the memory usage, composited layers for components have been reduced.

###### Webkit

The layout engine of the 2.3.1 wearable profile now supports circular/rotaUX for circle-shaped wearable devices:

- Support for the circular-type Web UI framework and a new media type to detect circle-shaped wearable devices has been added.
- Integration with platform UI components (such as pickers and popups) to support the circular/rotary UX has been added.
- Support for a touchcancel event (in some abnormal occurrences, such as touchstart event being canceled upon a palm gesture) has been added. 

##### Native Framework

The Tizen platform provides native APIs for wearable native applications in this release:  

- Application Framework API module
  - Application model
    - Widget application model has been added.
    - Watch application model has been added.
- Base API module
  - i18n
    - APIs for generating and parsing number or date format patterns for any locale have been added.
- UI API module
  - EFL (UI core)
    - Same EFL APIs are available as in the mobile profile
      (except for some profile-specific Elementary APIs).
    - Rectangular and circular UI components and Theme (Styles) have been added.
- WebView API module
  - Tizen Native API provides EFL WebKit APIs to:
    - Create a webview context and instance.
    - Set the URL and load a Web page.
    - Navigate the loaded Web page back and forward.
    - Reload, pause, and resume the Web page.
    - Retrieve the page navigation details.
    - Define basic settings, such as default font size, and cookie and cache management.
- Location API module
  - Location Manager
    - Support for wearable devices has been added.
- Network API module
  - Bluetooth
    - Support for the following:
      - GAP (Generic Access Profile)
      - Audio Profiles (HFP, HSP, and A2DP)
      - GATT(Generic Attribute Profile)
      - OPP (Object Push Profile)
      - HID (Human Interface Device Profile)
      - HDP (Health Device Profile)
      - SPP (Serial Port Profile)
    - New LE (Low Energy) APIs have been added, such as adding the advertising manufacturer data. The previous LE APIs have been deprecated in Tizen 2.3.1 and are to be removed in Tizen 3.0.
    - **Note:** Bluetooth features are only supported on reference target devices, not on the SDK emulator.
  - Connection management
    - Support for:
      - IPv6 (Internet Protocol version 6)
      - New API for IPv6 routing
  - Wi-Fi
    - **Note**: Wi-Fi features are only supported on reference target devices, not on the SDK emulator.
  - NFC
    - New NFC host-based card emulation APIs have been added.
  - Smartcard
    - New Smartcard API has been added.
- Socket and HTTP features supported by the OpenSSL and Curl open source libraries are provided.
- Graphics
  - 2D Graphics
    - Cairo evas-gl backend feature has been added to provide GPU-accelerated Cairo rendering.
- Sensor API module
  - Support to enable the application to get HRM and raw HRM sensor data has been added.

#### Tizen Platform Mobile Profile

##### Web Framework

The following features have been added to the existing mobile web device APIs in this release:

- NFC APIThe NFC host-based card emulation feature has been added.
- Sensor APIRaw HRM sensor data retrieval feature has been added.
- Sound APICheck whether a specific sound device type is connected has been added.
- Bluetooth  APIAdvertising for remote devices (including Bluetooth LE devices) has been added.Feature to act as a GATT client (Generic Attribute Profile client) has been added.

##### Native Framework

The following features have been added to the existing mobile native APIs in this release:

- Application Framework API module
  - ##### Application model

    - Widget application model has been added.
- Base API module
  - i18n
    - APIs for finding the location of boundaries in text and Unicode set have been added.
- Messaging API module
  - Message management
    - Several enums have been modified for unused or product code.
  - E-mail
    - API has been added to convert strings:
      int email_convert_mutf7_to_utf8(const char *mutf7_str, char **utf8_str)
- Network API module
  - Bluetooth
    - Support for the following:
      - GAP (Generic Access Profile)
      - Audio Profiles (HFP, HSP, and A2DP)
      - GATT(Generic Attribute Profile)
      - OPP (Object Push Profile)
      - HID (Human Interface Device Profile)
      - HDP (Health Device Profile)
      - SPP (Serial Port Profile)
    - New LE API was added for adding advertising manufacturer data. The previous LE APIs have been deprecated in Tizen 2.3.1 and are to be removed in Tizen 3.0.
    - **Note:** Bluetooth features are only supported on reference target devices, not on the SDK emulator.
  - Connection management
    - Support for the following:
      - IPv6 (Internet Protocol version 6)
      - New API for IPv6 routing
  - Wi-Fi
    - **Note**: Wi-Fi features are only supported on reference target devices, not on the SDK emulator.
  - NFC
    - New NFC host-based card emulation API has been added.
  - Smartcard
    - New Smartcard APsI have been added.
  - Socket and HTTP features supported by the OpenSSL and Curl open source libraries are provided.
- Social API module
  - Contacts
    - Connection recovery from abnormal disconnection has been added.
    - SIM access disability verification feature in a non-telephony device has been added.
  - Calendar
    - Connection recovery from abnormal disconnection has been added.
- UI API module
  - EFL (UI core)
  - Tizen Buffer Management
- Graphics
  - 2D Graphics
    - Cairo evas-gl backend feature has been added to provide GPU-accelerated Cairo rendering.
- Sensor API moduleFeatures to get HRM and raw HRM sensor data have been added.

**Fixed Bugs**

- Evas GL extension list bugs:
  - Get the extension list of GLES 1.1 and the exceptional case has been fixed.
  - Abnormal extension name had been fixed.
- Memory leak in case of the GLES 1.1 surface has been fixed.
- Reconfiguration of the window surface when Evas GL runs with Direct Rendering has been fixed.
- Null-checking code has been added.
- Pixmap surface fallback has been added for the case of the GLES 1.1 indirect rendering .
- Black rectangle underneath the image has been added for the native surface video.
- glGetString wrapper function has been added for Evas GL.

##### Security

###### Privilege

- Privilege verification process during the installation is changed to check the API version of the application. It checks whether the given privilege is valid in a given API version. If a deprecated or unknown privilege is declared in the tizen-manifest.xml (or config.xml) file and the API version (or required version) is equal or greater than 2.3.1, the installation fails. There is an exception for a Web application with a required version lower than 2.3.1. Deprecated or unknown privilege declared in those applications does not cause a problem during the installation.
- Native privileges for the mobile profile:
  - New privileges:
    - [http://tizen.org/privilege/reboot](http://tizen.org/privilege/reboot)
    - [http://tizen.org/privilege/secureelement](http://tizen.org/privilege/secureelement)
    - [http://tizen.org/privilege/widget.viewer](http://tizen.org/privilege/widget.viewer)
  - Deprecated privilege:
    - [http://tizen.org/privilege/systemsettings](http://tizen.org/privilege/systemsettings) (APIs using this privilege are changed to N/P)
- Native privileges for the wearable profile:
  - Native privileges available in the wearable profile:
    -  ​
    -  [http://tizen.org/privilege/alarm.get](http://tizen.org/privilege/alarm.get)
    -  [http://tizen.org/privilege/alarm.set](http://tizen.org/privilege/alarm.set)
    -  [http://tizen.org/privilege/appmanager.kill](http://tizen.org/privilege/appmanager.kill)
    -  [http://tizen.org/privilege/appmanager.launch](http://tizen.org/privilege/appmanager.launch)
    -  [http://tizen.org/privilege/bluetooth](http://tizen.org/privilege/bluetooth)
    -  [http://tizen.org/privilege/bluetooth.admin](http://tizen.org/privilege/bluetooth.admin)
    -  [http://tizen.org/privilege/call](http://tizen.org/privilege/call)
    -  [http://tizen.org/privilege/callhistory.read](http://tizen.org/privilege/callhistory.read)
    -  [http://tizen.org/privilege/callhistory.write](http://tizen.org/privilege/callhistory.write)
    -  [http://tizen.org/privilege/camera](http://tizen.org/privilege/camera)
    -  [http://tizen.org/privilege/content.write](http://tizen.org/privilege/content.write)
    -  [http://tizen.org/privilege/datasharing](http://tizen.org/privilege/datasharing)
    -  [http://tizen.org/privilege/display](http://tizen.org/privilege/display)
    -  [http://tizen.org/privilege/download](http://tizen.org/privilege/download)
    -  [http://tizen.org/privilege/externalstorage](http://tizen.org/privilege/externalstorage)
    -  [http://tizen.org/privilege/externalstorage.appdata](http://tizen.org/privilege/externalstorage.appdata)
    -  [http://tizen.org/privilege/haptic](http://tizen.org/privilege/haptic)
    -  [http://tizen.org/privilege/healthinfo](http://tizen.org/privilege/healthinfo)
    -  [http://tizen.org/privilege/internet](http://tizen.org/privilege/internet)
    -  [http://tizen.org/privilege/keymanager](http://tizen.org/privilege/keymanager)
    -  [http://tizen.org/privilege/keymanager.admin](http://tizen.org/privilege/keymanager.admin)
    -  [http://tizen.org/privilege/led](http://tizen.org/privilege/led)
    -  [http://tizen.org/privilege/location](http://tizen.org/privilege/location)
    -  [http://tizen.org/privilege/location.enable](http://tizen.org/privilege/location.enable)
    -  [http://tizen.org/privilege/mediastorage](http://tizen.org/privilege/mediastorage)
    -  [http://tizen.org/privilege/message.read](http://tizen.org/privilege/message.read)
    -  [http://tizen.org/privilege/message.write](http://tizen.org/privilege/message.write)
    -  [http://tizen.org/privilege/network.get](http://tizen.org/privilege/network.get)
    -  [http://tizen.org/privilege/network.profile](http://tizen.org/privilege/network.profile)
    -  [http://tizen.org/privilege/network.set](http://tizen.org/privilege/network.set)
    -  [http://tizen.org/privilege/nfc](http://tizen.org/privilege/nfc)
    -  [http://tizen.org/privilege/nfc.admin](http://tizen.org/privilege/nfc.admin)
    -  [http://tizen.org/privilege/nfc.cardemulation](http://tizen.org/privilege/nfc.cardemulation)
    -  [http://tizen.org/privilege/notification](http://tizen.org/privilege/notification)
    -  [http://tizen.org/privilege/packagemanager.admin](http://tizen.org/privilege/packagemanager.admin)
    -  [http://tizen.org/privilege/packagemanager.info](http://tizen.org/privilege/packagemanager.info)
    -  [http://tizen.org/privilege/power](http://tizen.org/privilege/power)
    -  [http://tizen.org/privilege/push](http://tizen.org/privilege/push)
    -  [http://tizen.org/privilege/reboot](http://tizen.org/privilege/reboot)
    -  [http://tizen.org/privilege/recorder](http://tizen.org/privilege/recorder)
    -  [http://tizen.org/privilege/screenshot](http://tizen.org/privilege/screenshot)
    -  [http://tizen.org/privilege/secureelement](http://tizen.org/privilege/secureelement)
    -  [http://tizen.org/privilege/systemsettings.admin](http://tizen.org/privilege/systemsettings.admin)
    -  [http://tizen.org/privilege/telephony](http://tizen.org/privilege/telephony)
    -  [http://tizen.org/privilege/telephony.admin](http://tizen.org/privilege/telephony.admin)
    -  [http://tizen.org/privilege/volume.set](http://tizen.org/privilege/volume.set)
    -  [http://tizen.org/privilege/widget.viewer](http://tizen.org/privilege/widget.viewer)
    -  [http://tizen.org/privilege/window.priority.set](http://tizen.org/privilege/window.priority.set)
- Web privileges for the mobile profile:
  - New privilege:
    - [http://tizen.org/privilege/telephony](http://tizen.org/privilege/telephony)
  - Deprecated privilege:
    - [http://tizen.org/privilege/systemmanager](http://tizen.org/privilege/systemmanager) (Use [http://tizen.org/privilege/telephony](http://tizen.org/privilege/telephony) instead.)
- Web privilege for the wearable profile:
  - New privileges:
    - [http://tizen.org/privilege/bluetooth.admin](http://tizen.org/privilege/bluetooth.admin)
    - [http://tizen.org/privilege/bluetooth.gap](http://tizen.org/privilege/bluetooth.gap)
    - [http://tizen.org/privilege/bluetooth.health](http://tizen.org/privilege/bluetooth.health)
    - [http://tizen.org/privilege/bluetooth.spp](http://tizen.org/privilege/bluetooth.spp)
    - [http://tizen.org/privilege/bluetoothmanager](http://tizen.org/privilege/bluetoothmanager)
    - [http://tizen.org/privilege/nfc.admin](http://tizen.org/privilege/nfc.admin)
    - [http://tizen.org/privilege/nfc.cardemulation](http://tizen.org/privilege/nfc.cardemulation)
    - [http://tizen.org/privilege/nfc.common](http://tizen.org/privilege/nfc.common)
    - [http://tizen.org/privilege/nfc.p2p](http://tizen.org/privilege/nfc.p2p)
    - [http://tizen.org/privilege/nfc.tag](http://tizen.org/privilege/nfc.tag)
    - [http://tizen.org/privilege/push](http://tizen.org/privilege/push)
    - [http://tizen.org/privilege/secureelement](http://tizen.org/privilege/secureelement)
    - [http://tizen.org/privilege/telephony](http://tizen.org/privilege/telephony)
  - Deprecated privilege:
    - [http://tizen.org/privilege/systemmanager](http://tizen.org/privilege/systemmanager) (Use [http://tizen.org/privilege/telephony](http://tizen.org/privilege/telephony) instead.)

#### IDE and Tools

##### New Features

- Native IDE
  - Support for developing a native application based on the Tizen wearable SDK has been added.
  - Support  for using the ninja build system has been added:
    - Generating ninja build script files
    - Using the ninja build instead of make
  - “Archive Generator” has been added:
    - Merging static objects from one library into another static library
  - Watch project types have been added:
    - Watch app can be installed only when launching the application.
- Tools
  - CLI (Common Line Interface) supports ‘post-certification’ of packaged binaries from native (.tpk), Web (.wgt), and hybrid (.tpk + .wgt) applications.
- Emulator
  - 360 * 360 and circular wearable emulators have been added.
  - Extra packages are automatically installed when launching the emulator. You do not need to manually install them on the emulator.
  - Rotary events for a circular screen are supported.
  - Virtual hardware key which functions like a back button, has been added to the circular wearable emulator.
- Sample applications for the wearable profile
  - The following Web sample applications have been added in this release:
    - Altimeter, App Callee, App Caller, Compass, Digital Watch, Hello Tizen, Mini Gallery, NewsFeed, Spinning Arrow, Sunburn Monitor, World Clock
  - The following native sample applications have been added in this release:
    - Analog Watch, Bluetooth-Chat, Digital-Watch, Notification Manager, Rotary Timer, Watch Application
    - (Circle/Rectangle) Email, (Circle/Rectangle) Setting UI, (Circle) Time Setting UI, (Rectangle) Dialer UI, (Circle/Rectangle) UI Controls
    - Cairo Basic, Cairo EvasGL, EvasGLCube, GLView11Cube, GLViewCube, GLViewShader

**Changed Features**

- Web IDE and tools
  - ‘app-widget’ element has been removed from the config.xml editor.
  - ‘tau’ keyword has been added to the CSS validation.
  - Web UI Builder has been deprecated.
  - Some ‘widget’ terms have been changed to ‘Web application’.
  - Default-installed user templates are no longer provided. However, the user template feature is still supported (only for Web applications).
  - Tizen Import Wizards, such as "Web Projects and Widget file", have been replaced with an integrated Import Wizard named "Tizen Project or Package". This is intended for multi-platform changeable support.


- Native IDE
  - shared/res folder has been added to the source location by default to build the EDC and PO files in the shared/res folder path.

**Fixed Bugs**

- Web IDE and tools
  - False error message when using ‘flex’ in the CSS file has been fixed.
- Emulator
  - Bug, which caused the “Always on Top” feature to sometimes not work correctly on Ubuntu, has been fixed.
  - Bug, which caused the emulator to sometimes not display the screen on Ubuntu and Radeon graphics cards, has been fixed.
- Native IDELinked resources are now added to the TPK file when packaging a project.Problem about a project build configuration occasionally changing from x86 to arm has been fixed.Linking error caused by an empty space in a project name when a project is building has been fixed.

**Known Issues**

- Web IDE and tools
  - Web SimulatorWeb Simulator does not support a circular UI.
- Emulator
  - In Mac OS, some files  transferred  to the emulator using an SDB push command cannot be accessed due to a file permission problem. To solve this problem, the file permission for other users must be changed at the host side.
  - If you already installed an Android HAX driver, the Tizen HAX driver is not installed. This causes you to encounter the "No accelerator found" error while launching the emulator. Uninstall the Android HAX driver and install the Tizen HAX driver manually as follows:
    - MS WindowsUninstall the Android HAX driver by going to the Windows control panel > "Programs and Features" > "Intel(R) Hardware Accelerated Execution Manager".Install the Tizen HAX driver by executing the driver installer, whose path is "<TIZEN_SDK_HOME>\tools\emulator\etc\IntelHaxmTizen.exe" and proceeding with the installation process.
    - Mac OS X 10.10Uninstall the Android HAX driver by opening a terminal, changing the directory to "/System/Library/Extensions/intelhaxm.kext/Contents/Resources", and entering the "sudo ./uninstall.sh" command.Install the Tizen HAX driver by executing the driver installer, whose path is "<TIZEN_SDK_HOME>/tools/emulator/etc/IntelHaxmTizen_for_10.10.dmg" and proceeding with the installation process.
    - Mac OS X 10.9 and underUninstall the Android HAX driver by opening a terminal, changing the directory to "/System/Library/Extensions/intelhaxm.kext/Contents/Resources", and entering the "sudo ./uninstall.sh" command.Install the Tizen HAX driver by executing the driver installer, whose path is "<TIZEN_SDK_HOME>/tools/emulator/etc/IntelHaxmTizen.dmg" and proceeding with the installation process. 
  - Emulator Manager can be closed  temporarily.
    - Condition
      - Run Emulator Manager
      - Change the werable-2.3.1 profile into x86-standard from x86-circle
      - Close the Emulator Manager and re-run
      - Select all tab on Emulator Manager
    - Solution
      - Roll back the werable-2.3.1 profile into x86-circle
- Dynamic Analyzer failed to recognize emulator for 1st time only & later running fine.
