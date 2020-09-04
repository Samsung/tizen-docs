# Tizen 5.0 Public M2

Release date: Oct. 30, 2018

The Tizen 5.0 Public M2 release provides developers with the Tizen kernel, device drivers, middleware subsystems, and Native/Web/TizenFX APIs.


## Release Details

- [Getting source code](http://review.tizen.org/git/) (Tizen 5.0 M2 source codes are under **tizen_5.0** branch.)

- Getting binaries and images
  - Base: [http://download.tizen.org/releases/milestone/tizen/base/tizen-base_20180928.1/](http://download.tizen.org/releases/milestone/tizen/base/tizen-base_20180928.1/)
  - Mobile(Fridge) / Wearable / TV /  IOT : [http://download.tizen.org/releases/milestone/tizen/unified/tizen-unified_20181024.1/images/](http://download.tizen.org/releases/milestone/tizen/unified/tizen-unified_20181024.1/images/)

- [How to flash to a device](../developing/flashing.md)


## Release Notes

### System (Kernel and System framework)

#### New and changed features

- New API set and features
  - D-Bus
    - A policy rule checker has been developed and deployed for improving security.
  - Dlog
    - A new feature of front-end filter has been developed for efficient logging and facilitating runtime log analysis.
  - Deviced
    - C# API set for display control has been added.
    - Native API set for multi-LED control has been added.
  - Storaged
    - Native and C# API set for storage device types has been added.
    - A new storage cleanup policy has been developed.
  - Compressed fs
    - Btrfs, Squashfs, and Overlayfs support has been added for rootfs.
- Refactoring and Maintenance
  - Systemd/Multi-user
    - Lazy mount units and API set has been added for improving developer experience.
    - Passwd files have been divided into read-only and read-write files for better reliability and security.
    - Hashing for the root password has been reinforced from MD5 to SHA-512.
  - Open source Upgrade
    - Squashfs has been upgraded to version 4.3.
    - Btrfs-progs has been upgraded to version 4.16.1.
- Testsuite
  - Deviced HAL TC
    - A new testsuite for Deviced HAL API set has been developed.
  - D-Bus
    - A new testsuite for D-Bus policy modules has been developed.
  - Dlog
    - A new testsuite including unit and stress tests has been developed.

#### Fixes

- Systemd 
  - CVE-2018-1049 has been patched. 
- D-Bus
  - Duplicated and unnecessary D-Bus policy rules have been removed.
  - dbus-glib (deprecated library) has been removed.
- USB-Host
  - Race condition problems in TCT and libraries have been fixed.


### System (IoT System)

#### New and changed features

- Debugging tools have been enhanced to obtain stability and reliability quickly during development, the tools help to reduce product development period for bringing up new devices:
  - Mini Coredump has been provided by reducing unnecessary sections from default coredump for transmitting through network and for reducing truncated coredumps by sudden process cleanup.
  - Linux based callstack symbol resolution tools have been provided to integrate into CI/CD infrastructure.
  - Thread based self watchdog system (except of systemd based watchdog) has been added.
- The SW upgrade has been enhanced to apply on more devices such as headless device:
  - For small company that does not have SW upgrade infra, SW upgrade infra has been provided on basis of Samsung Smartthings DeviceManager. Now, it is available on Beta services.
  - Remote update control for updating headless device has been provided. The OCF based update protocol and reference agents have been provided. In addition, remote update control framework has been provided to support several devices. The framework provides update control API set and update control plugins. The default plugin is available on the Tizen IoT homepage.
  - For secure update, generic template for binary signing/verification has been provided. Default binary signer and verifier are available on the Tizen IoT homepage.
- Low Memory Management for headless devices has been enhanced:
  - Applications can be excluded from low memory killer by defining Out of Memory (OOM) exception in manifest file.
  - OOM Score control interface has been provided for controlling active application like sound-focused application.
- Swap system has been enhanced to support multiple swap types and devices:
  - File-based swap and Zswap-based swap has been added.
  - Early memory reclaiming (to swap) feature has been added.

#### Fixes

- The bug that does not deliver low memory notification through event system has been fixed for headless devices.


### System (Base)

#### New and changed features

- Upgraded the following open source libraries:
  - icu (60.2)
  - ncurses (6.1)
    - CVE-2018-10754, CVE-2017-16879, CVE-2017-13734, CVE-2017-13733, CVE-2017-13732, CVE-2017-13731, CVE-2017-13730, CVE-2017-13729, CVE-2017-13728
  - sqlite (3.24.0)
    - CVE-2018-8740
  - procps-ng (3.3.15)
    - CVE-2018-1122, CVE-2018-1123, CVE-2018-1124, CVE-2018-1125, CVE-2018-1126
  - unzip (6.10c23)
    - CVE-2018-1000031, CVE-2018-1000032, CVE-2018-1000033, CVE-2018-1000035
  - json-glib (1.4.2)
- Expanded the capi-base-utils API set: 
  - Simple Date Format
  - Locale Display Names


### Application framework

#### New and changed features

- Tizen Interface Definition Language (TIDL), rpc-port
  - rpc-port is now available in the wearable profile.
  - TIDL has been improved in terms of performance and stability.
- Watchface complication framework
  - API has been refined to support more complex UX.
- App control API
  - A new API for sending launch request asynchronously has been added.
- Minicontrol API
  - Minicontrol API is now available in the wearable profile.


### Window System

#### New and changed features

- Wayland
  - The open source wayland has been upgraded to the 1.15.0 version.
- Extended Wayland Protocols
  - tizen_move_resize protocol has been added to support moving and resizing wl_surface at the same time by passing x,y,w,h geometry parameters.
- libinput
  - The ABS_MT_PRESSURE event type has been handled to support pressure-based input devices.
  - The following libinput API set has been added to set udev monitor's event source and buffer size:
    - libinput_udev_set_udev_monitor_event_source
    - libinput_udev_set_udev_monitor_buffer_size
- Enlightenment (Display Server)
  - e_dbus has been added to optimize booting time. It is parallelizing D-Bus connection to remove waiting time during initialization of the enlightenment.
  - Input device management in the Enlightenment devicemgr module has been moved to the Enlightenment core.
  - Support for tizen_move_resize protocol has been added to make move and resize for client's window at the same time.
  - Added the Vendor Driven HWC feature.
    - The two HWC features are:
    - HWC Planes
      - Enlightenment decides the HWC policy with e_planes.
      - Legacy HWC feature, which uses e_planes.
    - HWC Windows
      - The libtdm backend decides the HWC policy.
      - Vendor Driven HWC feature, which uses e_hwc_windows.
  - Enhanced the TCT for window system.
    - The following test cases have been added to verify the software regressions of the enlightenment display server:
      - D-Bus message system for server
      - Window stacking
      - Various cases for normal and alpha windows
      - Multi windows stacking
      - Size and stacking for floating window
      - Transient for window, notification type window
      - Screen saver function, window rotation
      - Various cases for window focus
      - Input events for keygrab feature
  - The debugging tool has been extended with support for:
    - kill -pid [pid] -f: Immediately kills the pid of the client.
- efl-util
  - New efl_util_input_initialize_generator_with_sync API has been added to support input device initialization in a synchronous manner.
  - The following efl-util API set and enums have been removed:
    - API set
      - efl_util_notification_window_level_error_cb
      - efl_util_set_notification_window_level_error_cb
      - efl_util_unset_notification_window_level_error_cb
      - efl_util_window_screen_mode_error_cb
      - efl_util_set_window_screen_mode_error_cb
      - efl_util_unset_window_screen_mode_error_cb
    - Enums
      - EFL_UTIL_NOTIFICATION_LEVEL_1
      - EFL_UTIL_NOTIFICATION_LEVEL_2
      - EFL_UTIL_NOTIFICATION_LEVEL_3
- libpepper-efl
  - The wayland shell implementation has been replaced to use zxdg_shell_v6 interface.
- Wayland TBM
  - Added the set_buffer_serial request at the wl_tbm protocol.
- Tizen Display HAL (TDM)
  - Added the TDM HAL test cases.
  - Added the tdm_hwc and tdm_hwc API for Vendor Driven HWC.
- Tizen Buffer HAL (TBM)
  - Added the TBM HAL test cases.
- Tizen Porting Layer for EGL (TPL-EGL)
  - libwayland-egl-tizen
    - Added wl_egl_window_tizen_set_window_serial function.
  - libtpl-egl
    - Added tpl_surface_create_with_num_buffers function.
    - Added tpl_display_get_with_backend_type function.
- Vulkan
  - Added support for VK_KHR_incremental_present.
  - Added support for using OldSwapchain.

#### Fixes

- Enlightenment (Display Server)
  - Many code defects detected by the static analysis tool have been fixed.
  - Fixed wrong input region of the window after the screen is rotated to the 90 degrees or 270 degrees.
  - Fixed unwanted focus set to a window that is specified as 'focus_skip_set' when it is mapped.


### Graphics Engine

#### New and changed features

- DALi (3D UI Toolkit)
  - Actor and Renderer
    - Support for notification to inform Actor's children order change has been added.
    - Support for changing rendering behavior has been added.
    - A mechanism to specify a callback on every frame has been added.
    - A CULLED property has been added to Actor.
  - Application
    - IdleEnterer callback has been added.
  - Input
    - An API has been added to identify right and left mouse button click.
    - Support for enabling the text prediction has been added.
    - Support for keyboard repeat information has been added.
  - Text
    - Support for software styling has been added.
  - Timer
    - API set to pause and resume the timer has been added.
  - Control and Visual
    - WebView control has been added.
    - Support for FlexLayout, AbsoluteLayout, and GridLayout has been added.
  - 3D Model
    - Support for GL Transmission Format (glTF) has been added for 3D watchface.
  - Performance
    - Changed not to render transparent texts.
  - NUI (C# Interface)
    - Added support for WebView.
- Simple DirectMedia Layer (SDL)
  - Upgraded to 2.0.8.
  - Added SDL sub-module as SDL-ttf.
  - Added new features.
    - Auxiliary Hint.
    - Focus Skip.

#### Fixes

- DALi (3D UI Toolkit)
  - Actor and Renderer
    - RenderTask bug (to waiting forever) has been fixed.
    - Depth buffer clear bug has been fixed.
    - BlendFunc has been fixed in case of a non-premultiplied format.
  - Window
    - Flickering issue has been fixed when a window is resized.
  - Control
    - Some bugs about layout have been fixed.
  - NUI (C# Interface)
    - Minor bugs (For example, wrong position, not shown) of Layout have been fixed.
    - RaiseToTop in View class bug has been fixed.
    - XamlResource memory leak error has been fixed.
    - VisualFittingMode bug in VisualMaps has been fixed.
- Evas Rendering Engine.
  - Bug of rotation is fixed in Evas GL Engine.
  - Added thread safety patch to Evas TBM Engine.
  - Bug of image downscaling is fixed in Evas GL Engine.
  - Bug of deadlock for multiple TBM Surfaces is fixed in Evas TBM Engine.
-  Simple DirectMedia Layer (SDL)
  - Bug in pause or resume in multi-windows is fixed.


### UI framework

#### New and changed features

- EFL
  - Version 1.20 is upgraded to 1.21.
- Harfbuzz
  - Version 0.4.6 is upgraded to 1.8.1.
- Freetype2
  - Version 2.9 is upgraded to 2.9.1.
- Text Input
  - Natural Language Processing (NLP) API has been added.
- Voice interaction
  - Added new API set to support multiple assistant.
  - Added API set, which has platform privileges to support voice panel app. 
  - Added Service Framework API set, which sends and receives data for supporting specific engine (For example, Bixby 2.0).

#### Fixes

- Fixed bugs.
- Clip Board History Manager (CBHM) is now working properly.


### Multimedia framework

#### New and changed features

- Common
  - Tizen Allocator and Bufferpool has been added.
- Media Player
  - Playback time related API set in nanoseconds has been added.
  - Setting zoom level with Field of View (FOV) for spherical video API has been added.
  - Video region of interest (ROI) API has been added.
  - Support for resuming HTTP playback during buffering has been added.
  - Support for cancellation of asynchronous preparing has been allowed.
  - Support for some tags of HLS v20 has been added.
  - The tizen allocator is applied to mediacodec.
  - The tizen allocator and buffer pool have been applied to the following modules:
    - Player, MediaCodec, Video360, and VideoConverter
    - TM1, TM2, TW2, and ARTIK Codec Plugins
    - Tizenwlsink
- Camera
  - Removed deprecated enums related with sound policy.
  - Added new preview format for depth camera.
  - Updated preview data structure for RGB format.
- Media Controller 
  - Added support for content type and age rating for the playing contents.
  - Added support for icon setting for controller servers.
  - Added support for capabilities of controller servers.
  - Added support for search command.
- Recorder
  - Removed deprecated enums related with sound policy.
- Sound Manager
  - New API set for USB audio output device is added.
- Pulseaudio
  - Added infrastructure of support for airplay (raop) device playback functionality.
- OpenCV
  - Version 2.4.9 has been upgraded to 3.4.1.
  - Deep Neural Network (DNN) module has been enabled. 


### Network and Connectivity

#### New and changed features

- Network Monitoring
  - Added intelligent-network-monitoring API set.
    - Added support for monitoring default connection capability.
    - Added support for getting wireless link properties.
    - Added support for watching network interface availability.
    - Added support for providing various network status information for diagnosis.
-  Wi-Fi Native CAPI
  - Added a wifi-manager API for forgetting an access point (AP) asynchronously.
  - Added a new Wi-Fi security type (WPA_FT_PSK).
  - Added new config API set for EAP private key and password.
  - Added new config API set for Hidden AP connection with static IP setting.
- Network Firewall
  - Added support for netfilter logging functions.
  - Added support for rule inserting function to top.
  - Added a STC API for setting firewall log rule.
  - Added a STC API for setting firewall netfilter log rule.
- STC
  - Added support for tethering data usage monitoring per client.
  - Added support for tethering data usage limitation per client.
- Telephony
  - Optimized D-Bus rules for reducing D-Bus policy scanning time.
- Wi-Fi SON
  - Added Wi-Fi SON (Self-organizing Networks) API set.
    - Added support for managing Wi-Fi Mesh network.
    - Added support for getting Wi-Fi Mesh network parameters.
    - Added support for SoftAP to extend existing network coverage.
      - Added 802.11w Protected Management Frame (PMF) feature.
      - Added 802.11k Radio Resource Management (RRM) feature.
- Multi Device Group
  - Added Multi Device Group API set based on IoTivity.
    - Added group management support for devices.
    - Added D2D communication support in a group.
- Bluetooth
  - Added BT 5.0 API set for getting 2M Phy support.
    - Added feature for BLE 5.0.
      - `http://tizen.org/feature/network.bluetooth.le.5_0`
  - Added support for fd GATT based data transfer.
- Multi-path TCP (MPTCP)
  - Added Multi-path TCP, which is implemented in Kernel and API.
    - Added support for Multi-path TCP functions.


### Security

#### New and changed features

- Security-manager
  - DB recovery logic has been added.
- Privilege
  - The following privileges have been added:
    - permission.check
    - updatecontrol.admin
  - The default web privilege policy has been changed.
    - From 5.0, web applications must declare media/externalstorage privilege if needed.
- Default-ac-domains
  - The System::Tools label has been added.
    - This label will be used for system tools.
- Askuser
  - New API set has been added.
    - Gets multiple privileges as parameter.
    - Checks permission of other application.
- Security-analyzer
  - The security module guide documents have been added.
    - Security-manager, Cynara, and Privilege


### Service framework

#### Fixes

- Account-Manager 
  - Fixed D-Bus policies.
  - Fixed memory leak and potential defects.
  - Refactored code to increase code maintainability. 
- Sync-manager 
  - Fixed D-Bus policies.
- Geofence-server 
  - Fixed D-Bus policies.
  - Fixed memory leak and potential defects.
- LBS Server 
  - Removed Wi-Fi dependency and added wifi-manager dependency.
- Maps-plugin-here 
  - Updated Maps-plugin-here and user consent.
  - Fixed memory leak and potential defects.
- Sensor 
  - Fixed memory leak and potential defects.
- Email 
  - Fixed memory leak and potential defects.
- Contact
  - Disabled unsupported charset.
  - Fixed potential defect.


### Web framework

#### New and changed features

- Added feature of App control with URI scheme.
  - Similar to android chrome intent.
  - Launches Tizen Native app implicitly or explicitly using [app-control:// ].
  - Supports fallback URL.
- Implemented alternative TBM back-end for web page rendering.
  - By setting chromium-efl's layout, the result can be rendered to memory surface.
  - Using the path, WebView can be merged with given UI framework.


### Lightweight Web Solution

#### New and changed features

- Added lightweight WebView support for Bixby Capsule Viewer on TV.
- Added lightweight WebView support for DALi (NUI).


### Tizen .NET

#### New and changed features

- .NET Core (Runtime)
  - Coreclr version 2.1.1 is upgraded to 2.1.4.
  - Corefx version 2.1.1 is upgraded to 2.1.4.
- Xamarin.Forms
  - Xamarin.Forms 3.2.0, which is the latest stable version, is now supported.
- Tizen.CircularUI
  - Wearable UI extension (Tizen.Wearable.CircularUI) version 1.0.0-pre2 is supported.
- Tizen.TV.UIControls
  - TV UI extension (Tizen.TV.UIControls) version 1.0.0-beta is now available.
- TizenFX
  - Added new MediaController API set for playlist, event, and capabilities.
  - Added new MediaController API set for sending command and its callback. The old API is deprecated.
  - Added new AudioManager API set for USB Audio output device.
  - Deprecated the device state enums of AudioManager.
  - Added new AudioManager API set for device running changed event. The old API is deprecated.
  - Added new AudioIO API set and enum for sample type and changed maximum sample rate.
  - Added new MediaPlayer API set to set or get the video ROI area.
  - Added new Camera API set for new preview format (RGB).
  - Added new Multimedia API set for the rotation of MediaTool.
  - Added new Multimedia API set to set or get playback position in nanoseconds.
  - Added new Multimedia API set to set zoom level with the field of view.
  - Added new Multimedia API set to set or get replaygain.
  - Added new Multimedia API set to set or get adaptive variants and property for buffering time.
  - Added new Nlp API set for new Namespace and Class.
  - Added new InputMethod API set for floating keyboard and to hide or launch IME.
  - Added new Wi-Fi API set for forgetting access point (AP), BssidScan, RawSsid, CountryCode, and WPS connection cancellation.
  - Added new Applications API set for rpc-port to support Remote Procedure Call (RPC).
  - Added new NUI API set for KeyboardRepeatInfo and TextPredition.
  - Added the change of NUI API set for ChildAdded, ChildRemoved, PropertySet events and properties of TableView.CellPosition.

#### Known Issues

- Xamarin.Forms
  - For more information on the list of limitations, see [here](../../application/dotnet/api/xamarin-forms-limitations.md).


### Experimental

#### New and changed features

- nnfw: Neural Network Runtime (Experimental Release)
  - Android NN API compatible (currently supports 25/37 operators).
  - TensorFlow Lite compatible (currently supports 25/68 operators).
  - Run MobileNet model.

