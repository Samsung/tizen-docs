# Tizen 4.0 Public M2

Release Date: 01 Nov, 2017

The Tizen 4.0 Public M2 release provides developers with the Tizen kernel, device drivers, middleware subsystems, and Web/Native APIs.

## Release Details

- [Getting source code](http://review.tizen.org/git/) (Tizen 4.0 M2 source codes are under **tizen_4.0** branch.)

- [Getting binaries and images](http://download.tizen.org/releases/milestone/tizen/4.0-unified/)
  - Base: [http://download.tizen.org/releases/milestone/tizen/4.0-base/tizen-4.0-base_20170929.1/](http://download.tizen.org/releases/milestone/tizen/4.0-base/tizen-4.0-base_20170929.1/)
  - Mobile: [http://download.tizen.org/releases/milestone/tizen/4.0-unified/tizen-4.0-unified_20171027.1/images/standard/mobile-wayland-armv7l-tm1/](http://download.tizen.org/releases/milestone/tizen/4.0-unified/tizen-4.0-unified_20171027.1/images/standard/mobile-wayland-armv7l-tm1/)
  - Wearable: [http://download.tizen.org/releases/milestone/tizen/4.0-unified/tizen-4.0-unified_20171027.1/images/standard/wearable-wayland-armv7l-tw2/](http://download.tizen.org/releases/milestone/tizen/4.0-unified/tizen-4.0-unified_20171027.1/images/standard/wearable-wayland-armv7l-tw2/)
  - TV: [http://download.tizen.org/releases/milestone/tizen/4.0-unified/tizen-4.0-unified_20171027.1/images/standard/tv-wayland-armv7l-odroidu3/](http://download.tizen.org/releases/milestone/tizen/4.0-unified/tizen-4.0-unified_20171027.1/images/standard/tv-wayland-armv7l-odroidu3/)

- [How to flash to a device](../developing/flashing.md)


## Release Notes

### System (Kernel and System Framework)

#### New and Changed Features

- System Framework
  - Extended internal storage support, without on-demand device encryption, has been added:
    - Extended internal storage is an SD card-based storage extension feature.
  - Dbus debugging and profiling tools (eBPF-based monitoring) have been added.
  - Supplementary group support for libdbuspolicy with Kdbus backend has been added.
  - C# Public APIs (device, feedback, storage, dlog, tizen-platform-config (internal)) has been added.
  - New Public enumerators have been added to libsvi, such as FEEDBACK_PATTERN_SYSTEM_SHORT.
  - A media directory that can be shared between users (/opt/usr/home/owner/media/Shared) has been added.

#### Fixes

- System Framework
  - The libsvi enumerator has been reorganized for each profile.
  - The tlm crash bug has been fixed.
  - The libdbuspolicy bug has been fixed.

#### Known Issues

- ODE (on-demand device encryption) for extended internal storage has not been fully implemented.

### System (IoT System)

#### New and Changed Features

- System Upgrade
  - A RO update/upgrade solution based on enhanced bsdiff/bspatch/7zip has been added.
  - A RW update/upgrade solution based on systemd offline update has been added. A RW script file verification solution has also been added.
  - An update/upgrade default UX has been added.
- System Recovery
  - A recovery ramdisk solution has been added.
  - Flexible recovery menu functionality on the basis of a configuration file has been added.
  - A TDM/TBM-based recovery UI engine has been added.
- System Information
  - A per-runtime system information engine has been added.
  - Additional APIs for smart management (per-application system resource usage information) have been added.
- Crash Manager
  - A ptrace-based callstack generator has been added.
- Resource Management
  - A light-weight resource management daemon for light-weight devices has been added. The resource management daemon supports shared library-based modules, and the low-memory management module is supported by default.
  - User-space memory limitation and memory compaction functionalities have been added.
- Open-source Libraries
  - The 7zip and divsufsort libraries have been added to support system upgrading.

#### Known Issues

- Generic fault monitoring and a recovery solution for improved platform reliability are planned for Tizen 5.0. Only a system recovery solution has been implemented for Tizen 4.0.

### System (Base)

#### New and Changed Features

- The following open-source libraries have been upgraded:
  - augeas (1.7.0)
  - file (5.31)
  - icu (58.2)
  - iniparser (3.2)
  - libarchive (3.3.1)
  - libevent (2.1.8)
  - libfdisk (2.30, renamed from libfdisk1 package)
  - libgio (2.52.2)
  - libglib (2.52.2)
  - libgthread (2.52.2)
  - libicu (58.2)
  - libmagic (5.31)
  - libmagic-data (5.31)
  - libmount (2.30)
  - libsmartcols (2.30)
  - libuuid (2.30)
  - libzip (1.04)
  - libzip (1.1.3)
  - lzo (2.10)
  - minizip (1.2.11)
  - tzdata (2017b)
  - util-linux (2.30)
  - uuid (2.30)
  - zlib (1.2.11)
- The capi-base-utils API set has been expanded:
  - uchariterator
  - Plural Rules
- The capi-system-settings API set has been expanded:
  - SYSTEM_SETTINGS_KEY_ACCESSIBILITY
  - SYSTEM_SETTINGS_KEY_VIBRATION
- The capi-system-settings API now returns ‘not supported’ error codes depending on the current feature type (mobile, tv, or wearable).

#### Fixes

- upstream/libarchive
  - CVE-2016-6250, CVE-2016-7166, CVE-2016-5844, CVE-2016-4302, CVE-2017-5601, CVE-2016-5418, CVE-2016-8688, CVE-2016-7166, CVE-2013-0211, CVE-2016-8687, CVE-2016-4809, and CVE-2015-2304
- upstream/libevent
  - CVE-2016-10195 and CVE-2015-6525
- upstream/ncurses
  - The terminfo-base package name has been changed to terminfo-base-full.
- upstream/util-linux
  - The libfdisk1 package name has been changed to libfdisk.
  - CVE-2014-3683, CVE-2015-5224, CVE-2016-2779, and CVE-2016-5011

### Application Framework

#### New and Changed Features

- Job Scheduler API
  - The API is used to optimize background job scheduling:
    - Service applications can schedule background jobs based on event conditions or period.
- Package Manager
  - Applications can be installed on an encrypted extended SD card.
  - Applications can store their private runtime data on an extended SD card.
- Application IPC
  - Access control with privileges for app-control and data-control APIs has been added.
- Application Launchers
  - The amd daemon has been refactored to support low-power IoT devices:
    - A modular structure has been introduced. Each functionality can be enabled or disabled by installing or removing amd-mod-* packages.

#### Fixes

- Bugs in the widget framework, related to supporting complicated widget and watch scenarios on wearable devices, have been resolved.

### Window System

#### New and Changed Features

- Wayland
  - The open-source Wayland library has been upgraded to 1.13.0.
- Extended Wayland Protocols
  - To avoid server-side memory leaks, a destructor has been added to protocols that do not have a corresponding request.
  - Various gesture types, such as tap, palm cover, and edge drag, have been added to the tizen_gesture protocol.
  - tizen_remote_surface has been extended to enable the client to accept or reject specific changed_buffer events, using a given filter value.
- Enlightenment Wayland Display Server
  - Support for the accessibility zoom function, using pp converting, has been added.
  - Support for the e_output capture function has been added.
  - Support for sharing the HW layer between video and UI has been added.
  - A scale factor option for the dump buffer has been added.
  - Window rotation information has been added to `wl_surface.set_buffer_transform()`.
  - DPMS, eom, screenshooter, and video functionalities have been moved from Enlightenment modules to the Enlightenment core.
  - The ecore-drm dependency has been removed by using libtdm.
  - A dbus signal can be broadcast when the screen is rotated.
  - The video window alpha handling rule has been changed.
  - Support for screen dumps has been added for debugging.
  - A new layer has been added to support the cursor.
  - The transient_below feature has been added to support a client window which needs to be placed under the parent window.
  - The `sd_notify()` function call has been added to the main function for sending systemd start-up notifications, since the `ecore_main_loop_begin()` function in EFL no longer calls it.
  - Creating the keymap cache file is now processed before initializing the DRM.
  - A remote surface client check has been added to permit access only to processes with a privileged UID.
  - A dbus policy check has been added to permit access only to processes with a privileged UID.
  - Auxiliary hints have been added for:
    - wm.policy.win.deiconify.update: to support clients which need to defer deiconify rendering.
    - wm.policy.win.iconify.buffer.flush: to support clients which need to change the buffer flush feature use when iconified.
  - Configuration values have been added for:
    - deiconify_approve: wait for render commit when deiconifying the client
    - rsm_buffer_release_mode: change the buffer flush mode for remote_surface
    - hold_prev_win_img: keep saved window image files
  - The debugging tool has been extended with support for:
    - shutdown: exit the Enlightenment display server
    - module: load/unload Enlightenment submodules
    - accepts_focus information
- wayland-tbm
  - Support has been added for the wl_tbm_queue reserved memory detach protocol.
  - Support has been added for the buffer transform protocol and API.
  - A scale factor option for the dump buffer has been added to wayland-tbm-monitor.
- Tizen ws Shell
  - The `tzsh_quickpanel_show()` and `tzsh_quickpanel_hide()` APIs have been changed to work in a synchronous manner.
- efl-util
  - efl-util gesture APIs have been added to handle global gestures, such as edge swipe, tap, and palm cover.
- pepper
  - The doctor server has been added as a reference implementation of a headless server. It is designed to have minimal library dependencies.
- Tizen HAL
  - Tizen display HAL
    - Support for asynchronous DPMS operations has been added.
    - Support for the "dummy" backend, which is installed with the libtdm frontend library, has been added.
  - Tizen buffer HAL
    - Support for the tbm_surface_queue GUARANTEE_CYCLE mode has been added.
    - Support for the tbm_surface_queue flush free buffer has been added.
    - Support for capturing a TBM surface in XRGB8888 format to a file has been added.
    - Support for adjusting the dump buffer scale has been added.
  - Tizen EGL porting layer
    - A new backend TPL_BACKEND_WL_EGL_THREAD has been added.
    - Handling Wayland event processing in a separate thread has been implemented.
    - A new `tpl_surface_cancel_dequeued_buffer()` API has been added, to use tbm_surface_queue in the GUARANTEE_CYCLE mode.
    - A new `tpl_display_get_backend_type()` API has been added, to retrieve the exact backend type before using `tpl_display_create()`.

#### Fixes

- Enlightenment Wayland Display Server
  - The EOM ec's subsurface showing error has been fixed.
  - The EOM different resolution buffer showing error has been fixed.
  - The screen flickering bug when hardware compositing mode and remote surface is changed has been fixed.
  - The remote surface screen-rotation bugs have been fixed.
  - The keyboard effect screen-rotation bug has been fixed.
  - Many code defects detected by the static analysis tool have been fixed.
- wayland-tbm
  - The bug related to the massive wayland-tbm-monitor debug message has been fixed.
- Tizen HAL
  - Tizen display HAL
    - The bug related to the massive tdm-monitor debug message has been fixed.
    - The multithread deadlock bugs have been fixed.
    - Some memory leak bugs have been fixed.
    - The setenv crash bug during multithreading has been fixed.
    - The tdm vblank bugs related to DPMS and output connection have been fixed.
    - The memory crash bugs that occur when user handlers are called have been fixed.
  - Tizen buffer HAL
    - The setenv crash bug during multithreading has been fixed.
    - The sequence queue enqueue and release bugs have been fixed.
  - Tizen EGL porting layer
    - Autotools have been applied to the build system.

### Graphics Engine

#### New and Changed Features

- DALi (3D UI Toolkit)
  - Common
    - Dual ABI support has been added.
    - C++11 build has been enabled.
    - EFL Elementary dependency has been removed.
  - Actor and Stage
    - Actor depth traversal algorithms have been simplified.
    - Layout direction properties have been added for RTL/LTR support.
    - A signal for layout direction change has been added.
  - Property
    - The `GetCurrentProperty()` function has been added.
  - Image
    - All Image classes have been deprecated.
    - CPU-based image masking has been added.
    - Floating-point formats have been added to PixelData.
    - Support for the KTX_UNCOMPRESSED_ALPHA8 format has been added.
  - Window
    - Support for window rotation has been added.
    - Support for screen rotation has been added.
    - Support for window resizing has been added.
  - Key event and input
    - Device information has been added to touch and key events.
    - Direction key handling has been added to move the key cursor.
    - The KeyExtension plugin has been added to support extension keys.
    - The GrabKeyList API has been added.
  - Text
    - Ge'ez (Ethiopic), Ol_chiki, Baybayin, and Meitei scripts have been added.
  - Control, Visual, and Style
    - Text scroll modes have been added to TextLabel.
    - The scroll mode properties have been added to ScrollView to simplify Rulers.
    - Line count and line wrap mode properties have been added to TextLabel and TextEditor.
    - Placeholder properties have been added to TextField and TextEditor.
    - ScrollStateChangedSignal has been added to TextEditor.
    - The ENABLE_SELECTION property has been added to TextField and TextEditor to enable or disable text selection and clipboard.
    - Support for text padding has been added to text controls.
    - Support for text color animation has been added.
    - TextLabel has been changed to use TextVisual.
    - Support for custom vertex shaders has been added to NPatchVisual.
    - Support for multiple images has been added to AnimatedImageVisual.
    - Support for outline text has been added to TextVisual.
    - Support for multiple resource loading threads has been added to TextureManager.
    - A config section has been added to stylesheet.
  - 3D rendering and animation
    - The `Animation::PlayAfter()` API has been added.
    - The `Animation::SetLoopMode()` and `Animation::GetLoopMode()` APIs have been added.
    - An environment variable to set the multi-sampling level has been added.
  - Performance
    - Unnecessary glClear calls have been reduced.
    - Unnecessary SwapBuffer calls have been reduced.
    - Fast bounding-box clipping has been added.
  - Video
    - Support for position and size has been added to underlay video.
  - NUI (C# interface)
    - The dispose pattern has been applied.
    - Hidden input properties have been added.
    - Support for TTS player has been added.
    - The dependency for Tizen.Applications.dll has been removed.
    - Support for group animation has been added to VisualView.
    - 3D rendering APIs, such as Renderer, Geometry, Shader, and Texture, have been added.
    - ImfManager APIs have been added.
    - The ResourceLoaded signal has been added to View.
    - Background color animation has been added to View.
    - Support for the 'as' keyword has been added.
    - The Viewport property has been added to Layer.
    - Support for PropertyMap and PropertyArray has been added.
    - The container base for Layer and View has been added.
    - Support for property notification has been added.
    - WatchApplication and WatchTime have been added.
    - The scene graph has been added to the C# layer.
    - Support for disposing children when the parent is disposed has been added.
- Evas Render Engine
  - Support for EvasGL thread separation on direct rendering mode has been added.
  - The pre-compiled shader list has been optimized for boot time enhancement.
  - Support for the Evas GL capability test has been added.
- SDL
  - Support for OpenGL ES has been added.
  - The support indicator widget has been added.
  - The enhancement window rotation feature has been added.

#### Fixes

- DALi (3D UI Toolkit)
  - The bug where the USE_ASSIGNED_SIZE resize policy overwrites the actor's original policy has been fixed.
  - When animating the same property using multiple animators, the final value was set based on whichever animator came last rather than the end time of the animator. This bug has been fixed.
  - The NativeImage rendering bug has been fixed.
  - The rendering order bug when clipping is enabled has been fixed.
  - The position error when INHERIT_POSITION is false has been fixed.
  - The crash caused by some PNG files has been fixed.
  - The bug when a font does not support all the glyphs of a script has been fixed.
  - The scalable/color fonts selection bug has been fixed.
  - The bug where TiltSensor is not started after being stopped has been fixed.
  - The bug where the **Delete All** key does not work has been fixed.
  - The ImageView crash caused by invalid images has been fixed.
  - The text scroll alignment bug has been fixed.
  - The text scroll animation bugs have been fixed.
  - The text position error in some glyphs has been fixed.
  - The crash caused by the same image being set repeatedly has been fixed.
  - The image flickering issue when images are replaced has been fixed.
  - The crash caused by disconnecting from native signals when a managed object is being disposed has been fixed.
- Evas Render Engine Enhancement
  - The Evas object image rotated image bug has been fixed.
  - The Evas GL PreRotation bug has been fixed.
  - When MSAA is used in EvasGL, the depth/stencil buffer can be created.

### UI Framework

#### New and Changed Features

- EFL
  - Edbus has been deprecated for security reasons.
  - Some source repositories have been changed:
    - From profile/PROFILE/platform/core/efl-config to platform/core/uifw/efl-config
    - From profile/PROFILE/platform/core/efl-misc to platform/core/uifw/efl-misc
    - From profile/PROFILE/platform/core/efl-modules to platform/core/uifw/efl-modules
- Text Input
  - New features and APIs:
    - In the TV profile, support for voice recognition on IME has been added.
    - Support for smart reply in inputdelegator and IME has been added.
    - In mobile and TV profiles, support for inputdelegator has been added.
    - Support for the floating keyboard type has been added.
    - An Ecore_IMF API for getting the keyboard mode has been added.
    - An Ecore_IMF API for setting a prediction hint has been added.
    - An Inputmethod API for sending media input has been added.
    - An Inputmethod API for sending private commands has been added.
    - An Inputmethod API for getting prediction hints has been added.
- Voice Framework
  - New features and APIs:
    - C# APIs for the STT and TTS engines have been added.
    - Support for a voice control hybrid engine has been added.

#### Fixes

- Many bugs have been fixed:
  - Exception-handling code has been added.
  - Memory leaks have been fixed.
  - A broken link in documentation has been fixed.

#### Known Issues

- Accessibility
  - The ScreenReader functionality has not been fully tested.
- Clipboard
  - The CBHM (ClipBoard History Manager) has not been fully tested.
- View Manager
  - The View Manager has not been fully tested.
- Customization API
  - In the wearable profile, the theme is not ready for customization.
- Focused UI has not been fully tested.
- UI mirroring has not been fully tested.
- The Tizen 4.0 UX is not yet finalized (the UI control and theme can change later).

### Multimedia Framework

#### New and Changed Features

- Camera
  - The "[http://tizen.org/privilege/camera](http://tizen.org/privilege/camera)" privilege requirement has been removed from some APIs.
  - New APIs for interrupting a started callback have been added.
  - The preview callback can now be set and unset while previewing.
- Recorder
  - The "[http://tizen.org/privilege/recorder](http://tizen.org/privilege/recorder)" privilege requirement has been removed from some APIs.
  - New APIs for interrupting a started callback have been added.
  - A new thread for a muxed stream callback has been added.
- Media Content
  - A new API for bookmark and face searching has been added.
  - APIs for updating file metadata (such as description, display name, added_time, rating, and content name) have been deprecated.
  - The API for getting/setting folder metadata (such as order, name, parent folder ID, and modified time) has been deprecated.
- Audio
  - A new Sound-Pool API set has been added.
  - New APIs for acquiring/releasing all focuses at once have been added.
  - A new API for delivering focus to another stream info handle has been added.
  - A new API for removing all devices from the stream information handle has been added.
  - Device state APIs have been deprecated.
- Player
  - A new API for getting/setting the maximum limit of the streaming variant has been added.
  - A new API for getting/setting the audio-only mode has been added.
  - A new API for getting/setting the streaming buffering time has been added.
- Common
  - A new OPUS enumeration for MediaTool has been added.
- Codec
  - Kernel dependency was removed by changing the physical address to bo in tm1.
  - A new API for configuration by media format has been added to MediaCodec.
  - Logic for sequences that have top/bottom crop has been added.
- MediaMuxer
  - A new API for registering/unregistering an EOS (end of stream) callback function that is invoked when an EOS occurs has been added.
- MediaStreamer
  - A new type for adaptive sink to generate fragmented files has been added.
  - HTTP streaming service using HTTP server has been added.
- Muse
  - The library has been split based on server, core, and client.
  - Support for security vulnerability (invalid memory access) analysis has been added.
  - A new thread has been added to the diagnostic tool:
    - Memory leak check when executing create/destroy events

#### Fixes

- Codec
  - The issue where ports were blocked during buffer flushing has been fixed.

### Network and Connectivity

#### New and Changed Features

- Data Network
  - New features and APIs in mobile, wearable, and TV profiles:
    - A wifi-manager API for getting the Wi-Fi module state has been added.
    - A wifi-manager API to get the Wi-Fi scan results for WPS (Wi-Fi Positioning System) has been added.
    - A wifi-manager API for getting the raw SSID has been added.
    - A wifi-manager and connection API for getting the DHCP lease duration has been added.
    - A wifi-manager API for getting the RSSI level has been added.
    - A wifi-manager API to scan using specific multiple SSID and channel has been added.
    - Support for EAP-AKA and EAP-SIM has been added.
    - A connection API to check whether the connection is metered has been added.
    - A wifi-manager API to get the connection error state has been added.
  - Major open-source package upgrades:
    - glib-networking has been upgraded from 2.38 to 2.50.
    - mdnsresponder has been upgraded from 576.30.4 to 765.50.9.
    - iptables has been upgraded from 1.4.21 to 1.6.1.
    - openvpn has been upgraded from 2.3.2 to 2.4.2.
- Bluetooth
  - New features and APIs:
    - The C# Public OPP Client API has been added.
    - The C# Public OPP Server API has been added.
- Telephony
  - New features and APIs:
    - In mobile, wearable and TV profiles, the is_metered field is now provided through profile data.
    - In mobile and wearable profiles, support for the call blocking feature in the call manager has been added.
    - In mobile and wearable profiles, support for unknown call blocking in the call manager has been added.
    - In mobile and wearable profiles, support for the cool-down feature in the call manager has been added.
    - In mobile and wearable profiles, support for call parameters update to stream-manager in the call manager has been added.

#### Fixes

- Data Network
  - A memory leak in the connman and net-config has been fixed.
  - A memory leak in the libnet-client and wifi-manager has been fixed.
- Telephony
  - A memory leak in the telephony manager plugin and telephony dbus handling plugin has been fixed.
  - The bugs in tapitest have been fixed.
- MTP
  - A memory leak in the MTP daemon has been fixed.
- NFC
  - The bug that caused a crash during UTC testing has been fixed.
  - The bug that caused a crash when launched by dbus activation has been fixed.
  - A memory leak in the NFC daemon has been fixed.
- Bluetooth
  - Memory corruption in a GATT operation has been fixed.
  - The crash issue in an OTP operation has been fixed.
  - The crash issue in discover services has been fixed.

### Security

#### New and Changed Features

- Trusted Execution Environment
  - A new native and Web TEE Client API has been added:
    - This API only works on devices supporting TEE.
  - tef-simulator, a package to simulate TEE on emulators, has been added.
- License Manager
  - When using app-defined privileges, a way to check consumer validity has been added.
- Privacy Privilege Manager API
  - New third-party APIs for privacy privilege usage have been added for native and C#.
- Privilege List
  - In the wearable profile, the following privileges have been added:
    - Native
      - apphistory.read
    - Web
      - account.read
      - account.write
      - calendar.read
      - calendar.write
      - contact.read
      - contact.write
  - In mobile, wearable and TV profiles, the following privileges have been added:
    - Web
      - appmanager.launch
      - datasharing
      - wifidirect
  - In mobile and wearable profiles, the following privileges have been added:
    - Native
      - blocknumber.read
      - blocknumber.write
      - gestureactivation
      - gesturegrab
      - peripheralio
  - In the TV profile, the following privilege has been removed:
    - Web
      - bluetooth
  - In mobile, wearable and TV profiles, the following privilege has been removed:
    - Native and Web:
      - d2d.datasharing
- Data Loss Prevention (DLP)
  - In the mobile profile, a new feature detecting data loss through HTTP and HTTPS has been added.

### Service Framework

#### New and Changed Features

- PIMS
  - Phonenumber Utils
    - In mobile and wearable profiles, new APIs for number blocking have been added.
- Location
  - Fused Location
    - New APIs for fused location have been added.
- Sensor
  - A new API for the significant motion sensor has been added.
- Context
  - Contextual History
    - In the mobile profile, several history data type enumerations have been deprecated.
    - In the wearable profile, Contextual History APIs have been added.
    - In mobile and wearable profiles, an API for checking history data type support has been added.
  - Contextual Trigger
    - In the mobile profile, several trigger event and condition type enumerations have been deprecated.
- Push
  - Support for the Chinese infrastructure has been added.
  - Support for multi-user application install/uninstall has been added.
- Sync Manager
  - In mobile and wearable profiles, multi-user support has been implemented.
  - In mobile and wearable profiles, the sync-service logic for use by other services has been added.
  - In mobile and wearable profiles, a Bluetooth connected callback has been added.
  - In mobile and wearable profiles, a new sync-manager feature and error enumeration have been added.

#### Fixes

- Account Manager
  - Account feature exception has been added for offline APIs.
  - Unused D-bus policy rules have been removed.
  - The D-bus policy rule has been fixed from system_fw to service_fw.
- Push
  - The bug related to waking up a service application has been fixed.
  - The bug related to push_request_unread_notification for root/system daemon has been fixed.
  - The bug with updating the reg db when the re-request is the same has been fixed.
  - Memory leaks have been fixed.
- service-adaptor
  - The bug related to using the deprecated `readdir_r()` API has been fixed.
  - Memory leaks have been fixed.
- FIDO
  - On-demand timeout for the fido-service daemon has been added.
  - fido-service has been changed to be used in the system daemon.
  - fido-asm.service has been changed to use on-demand dbus activation.
  - Coding rules and memory leaks have been fixed.
- Sync Manager
  - In mobile and wearable profiles, sync data storage has changed from XML to DB.
  - In the wearable profile, the calendar capability has been added.

### Web Framework

#### New and Changed Features

- New APIs have been added:
  - ewk_view_original_url_get
  - ewk_context_background_music_(get|set)
  - ewk_context_block_multimedia_on_call_(get|set)
  - ewk_context_rotation_lock_(get|set)
  - ewk_context_sound_overlap_(get|set)
- Circular video player support has been added.
- Notification icon and badge support have been added.
- Gesture support for brightness and volume control in fullscreen video has been added.
- Support for controlling media playback actions using an external controller has been added.
- The media stream recording feature has been added.
- Power consumption has been improved:
  - Limit the max frame rate for current consumption.
- WASM version 0x1
  - To switch on WASM, specify the runtime switch.
- Direct Canvas
  - Support for accelerated WebGL on fullscreen 3D canvas has been added:
    - The directcanvas attribute is needed on the canvas element.

### Tizen .NET

#### New and Changed Features

- C# Runtime
  - .NET Core 2.0.0 support
    - Major performance improvements in the runtime and framework.
    - Implements .NET Standard 2.0.
  - .NET Standard 2.0.0 support
    - .NET Standard is a set of APIs that all .NET implementations must provide to conform to the standard. This unifies the .NET implementations and prevents future fragmentation.
    - There more than 32,000 APIs in .NET Standard 2.0. These additions make it much easier to port existing code to .NET Standard.
    - .NET Standard 2.0 is supported on the following platforms as well as Tizen:
      - .NET Framework 4.6.1
      - .NET Core 2.0
      - Mono 5.4
      - Xamarin.iOS 10.14
      - Xamarin.Mac 3.8
      - Xamarin.Android 7.5
      - Upcoming version of UWP (expected to ship later this year)
- Xamarin.Forms
  - Xamarin.Forms version 2.4.0 Service Release 1 is supported.
  - Uses Tizen40 (tizen40) as a TargetFramework.
  - Now supports Tizen wearable profile (Preview).
- TizenFX
  - Included in the official release of Tizen API Version 4.
  - New APIs based on native APIs have been added:
    - capi-media-image-util
    - contacts-service2
    - phonenumber-utils
    - calendar-service2
    - sync-manager
    - tts-engine
    - stt-engine
    - libnsd-dns-sd (capi-network-nsd)
    - libnsd-ssdp (capi-network-nsd)
    - appcore-watch
    - libshortcut
    - attach-panel
    - capi-context

### SCM

#### New and Changed Features

- gcc
  - The Address Sanitizer, UndefinedBehavior Sanitizer, and Leak Sanitizer are now supported.
- glibc
  - ASLR (fPIC and pie) has been applied.
- binutils
  - The DT_RUNPATH tag is now used by default instead of the DT_RPATH tag.

#### Fixes

- gcc
  - A bug introduced in GCC 5 that affects conformance to the procedure call standard (AAPCS) has been fixed:
    - [https://gcc.gnu.org/bugzilla/show_bug.cgi?id=77728](https://gcc.gnu.org/bugzilla/show_bug.cgi?id=77728)
- glibc
  - CVE-2015-5180, CVE-2016-6323, and CVE-2017-1000366 have been applied.
