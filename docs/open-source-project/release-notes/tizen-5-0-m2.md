# Tizen 5.0 Public M2 Release Notes

Release date: Oct. 31, 2018


## System (Kernel and System framework)

### New and changed features

- New APIs and features
  - D-Bus
    - A policy rule checker has been developed and deployed for improving security.
  - Dlog
    - A new feature of front-end filters has been developed for efficient logging and facilitating runtime log analysis.
  - Deviced
    - C# APIs for display control have been added.
    - Native APIs for multi-LED control have been added.
  - Storaged
    - Native and C# APIs for storage device types have been added.
    - A new storage cleanup policy has been developed.
  - Compressed fs
    - Btrfs, Squashfs, and Overlayfs have been supported for rootfs.
- Refactoring and Maintenance
  - Systemd/Multi-user
    - Lazy mount units and APIs have been added for improving developer experience.
    - Passwd files have been divided into read-only and read-write files for better reliability and security.
    - Hashing for the root password has been reinforced from MD5 to SHA-512.
  - Opensource Upgrade
    - Squashfs has been upgraded to the version of 4.3.
    - Btrfs-progs has been upgraded to the version of 4.16.1.
- Testsuite
  - Deviced HAL TC
    - A new testsuite for Deviced HAL APIs has been developed.
  - D-Bus
    - A new testsuite for D-Bus policy modules has been developed.
  - Dlog
    - A new testsuite including unit and stress tests has been developed.

### Fixes

- Systemd 
  - CVE-2018-1049 has been patched. 
- D-Bus
  - Duplicated and unnecessary D-Bus policy rules have been cleaned up.
  - dbus-glib (deprecated library) has been removed.
- USB-Host
  - Race condition problems in TCT and libraries have been fixed.


## System (IoT System)

### New and changed features

- Debugging tools have been enhanced to obtain stability and reliability quickly during development, the tools help to reduce product development period for bringing up new devices.
  - Mini Coredump has been provided by reducing unnecessary sections from default coredump for transmitting via network and for reducing truncated coredumps by sudden process cleanup.
  - Linux-based callstack symbol resolution tools have been provided to integrate into CI/CD infrastructure.
  - Thread-based self watchdog system (except of systemd based watchdog) has been added.
- The SW upgrade has been enhanced to apply more devices like headless device.
  - For small company that does not have SW upgrade infra, SW upgrade infra has been provided on basis of Samsung Smartthings DeviceManager (https://console.smartthingsdm.com). Now, it is on Beta services.
  - Remote update control for updating headless device has been provided. The OCF based update protocol and reference agents have been provided. In addition, remote update control framework has been provided to support several devices. The framework provides update control APIs and update control plugins. The default plugin is available at the Tizen IoT homepage.
  - For secure update, generic template for binary signing/verification has been provided. Default binary signer and verifier are available at the Tizen IoT homepage.
- Low Memory Management for headless devices has been enhanced. 
  - Applications can be excluded from low memory killer by defining OOM exception in manifest file.
  - OOM Score control interface has been provided for controlling active application like sound-focused application.
- Swap system has been enhanced to support multiple swap types and devices.
  - File-based swap and Zswap-based swap has been added.
  - Early memory reclaiming (to swap) feature has been added.

### Fixes

- The bug that does not deliver low memory notification via event system has been fixed for headless devices.


## System (Base)

### New and changed features

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


## Application framework

### New and changed features

- TIDL (Tizen Interface Definition Language), rpc-port
  - rpc-port is now available in the wearable profile.
  - TIDL has been improved in terms of performance and stability.
- Watchface complication framework
  - API has been refined to support more complex UX.
- App control API
  - A new API for sending launch request asynchronously has been added.
- Minicontrol API
  - Minicontrol API is now available in the wearable profile.


## Window System

### New and changed features

- Wayland
  - The opensource wayland has been upgraded to the 1.15.0 version.
- Extended Wayland Protocols
  - tizen_move_resize protocol has been added to support move and resize for wl_surface at the same time by passing x,y,w,h geometry parameters.
- libinput
  - The ABS_MT_PRESSURE event type has been handled to support pressure-based input devices.
  - The following libinput APIs have been added to set udev monitor's event source and buffer size.
    - libinput_udev_set_udev_monitor_event_source
    - libinput_udev_set_udev_monitor_buffer_size
- Enlightenment (Display Server)
  - e_dbus has been added to optimize booting time. It is parallelizing D-Bus connection to remove waiting time during initialization of the enlightenment.
  - Input device management in the Enlightenment devicemgr module has been moved to the Enlightenment core.
  - Support for tizen_move_resize protocol has been added to make move and resize for client's window at the same time.
  - Added the Vendor Driven HWC feature.
    - Split HWC features into HWC Planes and HWC Windows.
    - HWC Planes
      - Deciding the hwc policy at Enlightenment.
      - legacy the hwc feature which uses the e_planes
    - HWC Windows
      - Deciding the hwc policy at libtdm backend.
      - Vendor driven hwc feature which uses the e_hwc_windows
  - Enhanced the TCT for window system.
    - The following test cases have been added to verify software regressions of the enlightenment display server after new feature adding.
      - D-Bus message system for server, window stacking, various cases for normal and alpha windows, multi windows stacking, size and stacking for floating window, transient for window, notification type window, screen saver function, window rotation, various cases for window focus, input events for keygrab
  - The debugging tool has been extended with support for:
    - kill -pid [pid] -f: the pid of the client is going to be killed immediately.
- efl-util
  - New efl_util_input_initialize_generator_with_sync API has been added to support input device initialization in a synchronous manner.
  - The following efl-util APIs and enums have been removed:
    - APIs
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
  - Added the TDM HAL testing cases.
  - Added the tdm_hwc and tdm_hwc API for Vendor Driven HWC.
- Tizen Buffer HAL (TBM)
  - Added the TBM HAL testing cases.
- Tizen Porting Layer for EGL (TPL-EGL)
  - libwayland-egl-tizen
    - Added wl_egl_window_tizen_set_window_serial function.
  - libtpl-egl
    - Added tpl_surface_create_with_num_buffers function.
    - Added tpl_display_get_with_backend_type function.
- Vulkan
  - Added the support for VK_KHR_incremental_present.
  - Added the support for using OldSwapchain.

### Fixes

- Enlightenment (Display Server)
  - Many code defects detected by the static analysis tool have been fixed.
  - Fixed wrong input region of the window after the screen is rotated to the 90 degrees or 270 degrees.
  - Fixed a problem that is unwanted focus set to a window for a while that has been specified 'focus_skip_set' during it is mapping.


## Graphics Engine

### New and changed features

- DALi (3D UI Toolkit)
  - Actor and Renderer
    - Support for notification to inform Actor’s children order change has been added.
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
    - APIs to pause and resume the timer have been added.
  - Control and Visual
    - WebView control has been added.
    - Support for FlexLayout, AbsoluteLayout and GridLayout has been added.
  - 3D Model
    - Support for glTF (GL Transmission Format) has been added.
  - Performance
    - Changed not to render transparent texts.
  - NUI (C# Interface)
    - Added support for WebView.
- SDL (Simple DirectMedia Layer)
  - Upgrade to 2.0.8.
  - Added SDL sub-module as SDL-ttf.
  - Added new features.
    - Auxiliary Hint.
    - Focus Skip.

### Fixes

- DALi (3D UI Toolkit)
  - Actor and Renderer
    - RenderTask bug to waiting forever has been fixed.
    - Depth buffer clear bug has been fixed.
    - BlendFunc has been fixed in case of a non-premultiplied format.
  - Window
    - Flickering issue has been fixed when a window is resized.
  - Control
    - Some bugs about layout have been fixed.
  - NUI (C# Interface)
    - Minor bugs (ex: wrong position, not shown) of Layout have been fixed.
    - RaiseToTop in View class bug has been fixed.
    - XamlResource memory leak error has been fixed.
    - VisualFittingMode bug in VisualMaps has been fixed.
- Evas Rendering Engine.
  - Bug of rotation is fixed in Evas GL Engine.
  - Added thread safety patch to Evas TBM Engine.
  - Bug of image downscaling is fixed in Evas GL Engine.
  - Added the patch is TBM Queue is used per TBM surface in Evas TBM Engine.
-  SDL (Simple DirectMedia Layer)
  - Bug of pause/resume in multi-windows is fixed.


## UI framework

### New and changed features

- EFL
  - Version 1.20 is upgraded to 1.21.
- Harfbuzz
  - Version 0.4.6 is upgraded to 1.8.1.
- Freetype2
  - Version 2.9 is upgraded to 2.9.1.
- Text Input
  - NLP (Natural Language Processing) API has been added.
- Voice interaction
  - Added new APIs to supporting multiple assistant.
  - Added APIs which has platform privilege to supporting voice panel app. 
  - Added APIs to supporting to send and to receive specific engine result.

### Fixes

- Fixed bugs.
- CBHM (Clip Board History Manager) is now working properly.


## Multimedia framework

### New and changed features

- Common
  - Tizen Allocator & Bufferpool has been added.
- Media Player
  - Playback time related APIs in nanoseconds has been added.
  - Setting zoom level with fov about spherical video API has been added.
  - Video ROI (region of interest) API has been added.
  - Support for resuming HTTP playback during buffering has been added.
  - Support for cancellation of asynchronous preparing has been allowed.
  - Support for some tags of HLS v20 has been added.
  - The tizen allocator is applied to mediacodec.
  - The tizen allocator & buffer pool have been applied to the following modules:
    - Player, MediaCodec, Video360, VideoConverter
    - TM1, TM2, TW2, ARTIK Codec Plugins
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
  - New APIs for USB audio output device are added.
- Pulseaudio
  - Added infrastructure of support for airplay(raop) device playback functionality.
- OpenCV
  - Version 2.4.9 has been upgraded to 3.4.1.
  - Deep Neural Network (DNN) module has been enabled. 


## Network and Connectivity

### New and changed features

- Network Monitoring
  - Added intelligent-network-monitoring APIs.
    - Added support for monitoring default connection capability.
    - Added support for getting wireless link properties.
    - Added support for watching network interface availability.
    - Added support for providing various network status information for diagnosis.
-  Wi-Fi Native CAPI
  - Added a wifi-manager API for forgetting an AP asynchronously.
  - Added a new wifi security type (WPA_FT_PSK).
  - Added new config APIs for EAP private key and password.
  - Added new config APIs for Hidden AP connection with static IP setting.
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
  - Added Wi-Fi SON (Self-organizing Networks) APIs.
    - Added support for managing Wi-Fi Mesh network.
    - Added support for getting Wi-Fi Mesh network parameters.
    - Added support for SoftAP to extend existing network coverage.
      - Added 802.11w PMF (Protected Management Frame) feature.
      - Added 802.11k RRM (Radio Resource Management) feature.
- Multi Device Group
  - Added Multi Device Group APIs based on IoTivity.
    - Added group management support for devices.
    - Added D2D communication support in a group.
- Bluetooth
  - Added BT 5.0 APIs for getting 2M Phy support.
    - Added feature for BLE 5.0.
      - http://tizen.org/feature/network.bluetooth.le.5_0
  - Added support for fd GATT based data transfer.
- Multi-path TCP (MPTCP)
  - Added Multi-path TCP, which implemented in Kernel and API.
    - Added support for Multi-path TCP functions.


## Security

### New and changed features

- Security-manager
  - DB recovery logic has been added.
- Privilege
  - The following privileges have been added.
    - permission.check, updatecontrol.admin
  - The default web privilege policy has been changed.
    - From 5.0, web applications should declare media/externalstorage privilege if needed.
- Default-ac-domains
  - The System::Tools label has been added.
    - This label will be used for system tools.
- Askuser
  - New APIs have been added.
    - Getting multiple privileges as parameter.
    - Checking permission of other application.
- Security-analyzer
  - The security module guide documents have been added.
    - Security-manager, Cynara, Privilege


## Service framework

### Fixes

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
  - Removed wifi dependency and added wifi-manager dependency.
- Maps-plugin-here 
  - Updated.
  - Fixed memory leak and potential defects.
  - Updated user consent.
- Sensor 
  - Fixed memory leak and potential defects.
- Email 
  - Fixed memory leak and potential defects.
- Contact
  - Disable unsupported charset.
  - Fixed potential defect.


## Web framework

### New and changed features

- Add feature of [App control with URI scheme]
  - Support feature which is similar with android chrome intent.
  - Tizen native app implicit/explicit launching by using [app-control:// ]
  - Supporting Fallback url.
- Implement alternative TBM back-end for web page rendering.
  - By setting chromium-efl’s layout result can be rendered to memory surface.
  - Using this path chromium=efl webview can be merged with given UI framework (NUI,..).


## Lightweight Web Solution

### New and changed features

- WebView support for Bixby Capsule Viewer on TV has been added.
- WebView support for DALi (NUI) has been added.


## Tizen .NET

### New and changed features

- .NET Core (Runtime)
  - Coreclr version 2.1.1 is upgraded to 2.1.4.
  - Corefx version 2.1.1 is upgraded to 2.1.4.
- Xamarin.Forms
  - Xamarin.Forms 3.2.0 which is latest stable version is supported.
- Tizen.CircularUI
  - Wearable UI extension (Tizen.Wearable.CircularUI) version 1.0.0-pre2 is supported.
- Tizen.TV.UIControls
  - TV UI extension (Tizen.TV.UIControls) version 1.0.0-beta is now available.
- TizenFX
  - Added new MediaController APIs for playlist, event and capabilities.
  - Added new MediaController APIs for sending command and its callback and deprecate old one.
  - Added new AudioManager APIs for USB Audio output device.
  - Deprecated the device state enums of AudioManager.
  - Added new AudioManager APIs for device running changed event and deprecate old one.
  - Added new AudioIO APIs and enum for sample type and change maximum sample rate.
  - Added new MediaPlayer APIs to set/get the video ROI area.
  - Added new Camera APIs for new preview format (RGB).
  - Added new Multimedia APIs for the rotation of MediaTool.
  - Added new Multimedia APIs to set/get playback position in nanoseconds.
  - Added new Multimedia APIs to set zoom level with the field of view.
  - Added new Multimedia APIs to set/get replaygain.
  - Added new Multimedia APIs to set/get adaptive variants and property for buffering time.
  - Added new Nlp APIs of new Namespace and Class.
  - Added new InputMethod APIs for floating keyboard and to hide/launch IME.
  - Added new WiFi APIs for forgetting AP and, BssidScan, RawSsid, CountryCode, WPS connection cancellation.
  - Added new Applications APIs for rpc-port to support RPC (Remote Procedure Call).
  - Added new NUI APIs for KeyboardRepeatInfo and TextPredition.
  - Added the change of NUI APIs for ChildAdded, ChildRemoved, PropertySet events & properties of TableView.CellPosition.

### Known Issues

- Xamarin.Forms
  - For more information on the list of limitations, see [here](https://developer.tizen.org/development/api-reference/.net-application/current-xamarin.forms-limitations).


## Experimental

### New and changed features

- nnfw: Neural Network Runtime (Experimental Release)
  - Android NN API compatible (currently supports 25/37 operators).
  - TensorFlow Lite compatible (currently supports 25/68 operators).
  - Run MobileNet model.

