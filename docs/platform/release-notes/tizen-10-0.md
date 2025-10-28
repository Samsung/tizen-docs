# Tizen 10.0 Release

Release date: Oct 31, 2025

## Release details

- [Getting source code](http://review.tizen.org/gerrit/) (Tizen 10.0 source codes are under **tizen** branch.)

- Getting binaries and images:
  - Base: https://download.tizen.org/releases/milestone/TIZEN/Tizen/Tizen-Base/tizen-base_20250923.230953/
  - Profile (Unified): https://download.tizen.org/releases/milestone/TIZEN/Tizen/Tizen-Unified/tizen-unified_20251024.151443/

- [How to flash an image to device](../developing/flashing-rpi.md)


## Release notes

### System kernel and system framework

#### New and changed features

- Kernel
  - U-boot for Raspberry Pi 4, 5 and VIM3 has been upgraded to version 2024.10.
  - Kernel for Raspberry Pi 4 and 5 has been upgraded to version 6.12.42.
    - The kernel now supports erofs read-only filesystem.
    - The kernel now supports kernel btf and dwarf4 debug option.
  - Kernel for Raspberry Pi 5 has been changed to print kernel log to gpio uart by default.

- System Framework
  - IPC(dbus) optimization
    - Optimize format convert step from GVariant to GVariantVector on kdbus.
    - Reduce the count of KDBUS_CMD_CONN_INFO ioctl count from 3 to 1 by using caching method.
    - Improve gdbus performance of 33.9% on 1024 byte data transfer.
    - Improve libdbus performance of 7.8% on 1024 byte data transfer

  - System and resource management
    - The CPU_BOOSTING_FORCE_RESET_ON_CLEAR flag has been added to reset boosting forcely during cpu_boosting clear.
    - The no-smack environment has been supported on dbus and systemd for Automotive Tizen Platform.
    - The /etc/resourced/limiter.conf.d of resourced has been supported to configure memory/cpu limitation for each profile.
    - It supports the configuration that can exclude the CMA size from MemAvailable during LMK (Low Memory Killer).
    - The CPU_BOOSTING_LEVEL_COLDBOOT has been added to support a level stronger than CPU_BOOSTING_LEVEL_STRONG.
    - The VIP watchdog reboot function has supported the action configuration o prevent infinite reboot due to repetitive VIP process kill.

  - Device and resource management
    - Add Tizen.System.Battery.PowerSource C# API to get the connected power source.

  - Multi-User management
    - The per-subsession maximums storage limitation has been added when adding new subsession.
    - The sessiond plugin structure has been supported to help GBM dependent service.
    - The new user ADD speed optimization from 12 sec to 1 sec.
    - The session on-demand deactivation has been supported to reduce 500KB memory usage.

  - OS Upgrade and Individual Service Upgrade
    - The timeout functionality of data migration script has been added to prevent never-finished data migration.
    - The crash-worker for ISU package has been supported.

  - HAL management
    - The HAL IPC transport feature has been added to support the fully separated platform from product.
    - The part of hal-api-device package has supported for HAL IPC transport like battery/display/led/bezel/extcon.
    - The HAL backend manifest has been added to specify the used HAL transport type on product.
    - The DLConf (Dynamic Loader Configuration) feature has been addded to install/use the same name and different version library.
    - The hal-rootstrap-data-da package has been supported to manage DA owned packages.
    - The systemd service execution under /hal has been supported by adding /hal/lib/systemd/system.
    - The kernel module loading under /hal has been supported by adding /hal/lib/modules and modules-load.d/modprobe.d under /hal.
    - The udev rules loading under /hal has been supported by adding /hal/etc/udev/rules.d/ path.

  - Diagnostics management
    - The "so_info" file, which includes the RPM information installed under /hal, has been supported when a crash occurs by crash-worker.
    - The stability-monitor has supported the coredump option to enable the coredump according to the configuration value.

- Open Source
  - libbpf
    - Version 1.0.1 has been upgraded to version 1.5.0.
  - kmod
    - Version 31 has been upgraded to version 34.
  - libdrm
    - Version 2.4.118 has been upgraded to version 2.4.124.

#### Fixes
- deviced
  - The power module has been modified to be supported on headless profile.
  - The display dimming timeout has been fixed to initialize the default value on constructor.
  - The display on/off operation has been fixed when deviced plugin is not used.
  - If the application registered for power state change callback is killed, complete the power transition without waiting.
  - The display ON bug after silent reboot has been fixed.
  - The display lock state change callback bug has been fixed.
- resourced
  - The CPU_BOOSTING_RESET_ON_FORK on fail issue has been fixed on a resource_set_cpu_boosting().
- gdbus
  - The gdbus has been modified to receive unicast-type broadcast signals without subscription.
- libdbuspolicy
  - The dependency of libdbuspolicy has been removed from glib to move glib build into base build.
- OS Upgrade and HAL
  - The smack issue of hal-backend-compatibility on hal-api-common has been fixed
  - The build issue of hal-rootstrap has been fixed on DA/VD build environment.
- stability-monitor
  - The UID getter has been updated according to AUL update on Tizen 10.0.

### Toolchain

#### New and changed features

- Open Source
  - gcc version 9.2.0 has been upgraded to version 14.2.0.
  - glibc version 2.30 has been upgraded to version 2.40.
  - binutils version 2.33.1 has been upgraded to version 2.43.
  - llvm version 17.0.6 has been upgraded to version 19.1.4.
  - libffi version 3.4.2 has been upgraded to version 3.4.7.
  - gdb version 13.2 has been upgraded to version 15.1.
  - strace version 5.9 has been upgraded to version 6.6.
  - valgrind version 3.16.1 has been upgraded to version 3.25.0.


### System (Base)

#### New and changed features

- Open Source
  - abseil-cpp
    - Version 20230802.1 has been upgraded to version 20240722.
  - cmake
    - Version 3.25.2 has been upgraded to version 3.31.2.
  - grpc
    - Version 1.42.0 has been upgraded to version 1.68.2.
  - gtest
    - Version 1.14.0 has been upgraded to version 1.15.2.
  - gtk-doc
    - Version 1.33.2 has been upgraded to version 1.34.0.
  - icu
    - Version 74.1 has been upgraded to version 76.1.
  - iniparser
    - Version 4.1 has been upgraded to version 4.2.4.
  - jq
    - Version 1.6 has been upgraded to version 1.7.1.
  - json-c
    - Version 0.17 has been upgraded to version 0.18-20240915.
  - jsoncpp
    - Version 1.9.5 has been upgraded to version 1.9.6.
  - less
    - Version 643 has been upgraded to version 668.
  - libarchive
    - Version 3.7.2 has been upgraded to version 3.7.7.
  - libwbxml2
    - Version 0.11.8 has been upgraded to version 0.11.10.
  - libxml2
    - Version 2.12.5 has been upgraded to version 2.13.5.
  - libxslt
    - Version 1.1.39 has been upgraded to version 1.1.42.
  - libzio
    - Version 1.08 has been upgraded to version 1.09.
  - libzip
    - Version 1.10.1 has been upgraded to version 1.11.3.
  - make
    - Version 4.3 has been upgraded to version 4.4.1.
  - meson
    - Version 1.3.0 has been upgraded to version 1.6.1.
  - ninja
    - Version 1.11.1 has been upgraded to version 1.12.1.
  - npth
    - Version 1.6 has been upgraded to version 1.8.
  - pcre2
    - Version 10.4 has been upgraded to version 10.45.
  - perl-Alien-Build
    - Version 2.8 has been upgraded to version 2.84.
  - perl-B-Hooks-EndOfScope
    - Version 0.26 has been upgraded to version 0.28.
  - perl-Class-Data-Inheritable
    - Version 0.09 has been upgraded to version 0.1.
  - perl-DateTime-Locale
    - Version 1.4 has been upgraded to version 1.44.
  - perl-DateTime-TimeZone
    - Version 2.61 has been upgraded to version 2.63.
  - perl-HTML-Tagset
    - Version 3.2 has been upgraded to version 3.24.
  - perl-libwww-perl
    - Version 6.72 has been upgraded to version 6.77.
  - perl-namespace-autoclean
    - Version 0.29 has been upgraded to version 0.31.
  - perl-Net-DBus
    - Version 1.0.0 has been upgraded to version 1.2.0.
  - perl-Path-Tiny
    - Version 0.144 has been upgraded to version 0.146.
  - perl-Term-Table
    - Version 0.018 has been upgraded to version 0.023.
  - perl-Test2-Suite
    - Version 0.000159 has been upgraded to version 0.000163.
  - perl-Try-Tiny
    - Version 0.31 has been upgraded to version 0.32.
  - perl-URI
    - Version 5.21 has been upgraded to version 5.31.
  - perl-Variable-Magic
    - Version 0.63 has been upgraded to version 0.64.
  - perl-XML-LibXML
    - Version 2.0209 has been upgraded to version 2.021.
  - perl-XML-Parser
    - Version 2.46 has been upgraded to version 2.47.
  - perl-YAML
    - Version 1.3 has been upgraded to version 1.31.
  - python3
    - Version 3.12.0 has been upgraded to version 3.13.1.
  - python3-libxml2
    - Version 2.12.5 has been upgraded to version 2.13.5.
  - python3-lxml
    - Version 4.9.3 has been upgraded to version 5.3.1.
  - python3-sqlite
    - Version 0.4.7 has been upgraded to version 0.5.4.
  - python3-grpcio
    - Version 1.65.0rc1 has been upgraded to version 1.70.0.
  - python-libxml2
    - Version 2.12.5 has been upgraded to version 2.13.5.
  - re2
    - Version 20231101 has been upgraded to version 20240702.
  - re2c
    - Version 3.1 has been upgraded to version 4.0.2.
  - sqlite
    - Version 3.44.0 has been upgraded to version 3.48.0.
  - tinyxml2
    - Version 9.0.0 has been upgraded to version 10.0.0.
  - tzdata
    - Version 2023c has been upgraded to version 2024b.
  - xz
    - Version 5.4.5 has been upgraded to version 5.6.3.
  - zlib
    - Version 1.3 has been upgraded to version 1.3.1.
  - zstd
    - Version 1.5.5 has been upgraded to version 1.5.6.

- system-settings
  - SYSTEM_SETTINGS_KEY_OOBE enum has been added.
    - tizen.org/feature/systemsetting.oobe feature has been implemented to support

### Application framework

#### New and changed features

- Application Core
  - Component-based Native API has been deprecated.
  - The Tizen.Applications.UIGadget has been added.
  - The LocaleManager has been added
- Application Utility
  - Minicontrol APIs have been deprecated.
- Application Installer
  - New APIs related to first installed time and update have been added.
- Configuration
  - The multi user feature has been added to buxton2.
- Theme manager
  - The RPK(Resource Package) has been supported.
- Tizen Action Framework
  - A new Tizen Action Framework enabling AI integration within the platform has been added.
- TIDL Protocol2
  - It has improved RPC performance through optimization of the Unit type.
  - It has added new types: u8, u16, u32, u64, file_desc.
- United Service
  - United service for daemon framework has been added.
    - Some Appfw service daemons have been integrated. (alarm-server, data-provider-master, esd)
- Widget
  - Widget viewer evas APIs have been deprecated.

#### Fixes

- Application Installer
  - Fix bug where some privilege disappears if it fails during package update


### Window and interaction

#### New and changed features

- Wayland
  - The version of Wayland has been upgraded to 1.23.1.
  - wtz-screen wayland protocol has been added for supporting multi-display.
- vulkan-wsi-layer
  - Version 2023.12.01 has been upgraded to version 2024.12.02.
- Vulkan-ValidationLayer
  - Version 1.3.268 has been upgraded to version 1.3.296.
- Vulkan-Loader
  - Version 1.3.268 has been upgraded to version 1.3.296.
- Vulkan-Headers
  - Version 1.3.268 has been upgraded to version 1.3.296.
- Vulkan-Tools
  - Version 1.3.268 has been upgraded to version 1.3.296.
- Vulkan-Utility-Libraries
  - Version 1.3.268 has been upgraded to version 1.3.296.
- SPIRV-Tools
  - Version 2023.5.1 has been upgraded to version 2024.4.1.
- glslang
  - Version 13.1.1 has been upgraded to version 15.0.0.
- Libinput
  - The version of Libinput has been upgraded to 1.27.1.
- Libevdev
  - The version of Libevdev has been upgraded to 1.13.3.
- Libxkbcommon
  - The version of Libxkbcommon has been upgraded to 1.7.0.
- Enlightenment
  - Multi-display which provide multi-seat (input) and multi-screen (window management) has been supported.
    - Multi-Zones and Multi-DeskArea have been supported
    - Input for multi seat and display has been supported.
  - Enlightenment has been redesigned
    - The Enlightenment has encapsulated the APIs provided to the Enlightenment module.
    - Enlightenment offers an E_View API that can replace the Evas_Object.
    - A bunch of legacy codes that weren't being used in Enlightenment got deleted.
  - The virtual touch API to control the application that does not handle touch event has been provided.
  - The ecore event processing mode has been added to remove evas dependency.
  - The documentation for gesture API has been added.
  - In order to save memory, the cursor surface has been created when it is actually needed.
  - The memory usage of enlightenment has been reduced.
  - Unit and Integration testcases are added and improved.
- libds
  - The implementation of wtz-screen interface has been added.
- Angle
  - Angle of which version is chromium/6410 has been added.
  - Support the translation of OpenGL ES /EGL to Vulkan.
- Display VX
  - Support Relumino for accessibility.
  - Enhance UX through blur effect with customizable radius and region settings.
- Text Input
  - Fullscreen IME mode has been provided.
  - The memory usage of ISF has been reduced.
  - The memory usage of NUI IME has been reduced.
  - NLP APIs has been removed
  - The remote input API to connect asynchronously has been added.


### Graphics and UI

#### New and changed features

- Image and Animation
  - Support apply once option for Constraint.
- Inputs and Utilities
  - New Hit test algorithm to support Multiple FBO rendering.
  - A DeviceName in hover and touch has been added.
  - SetPanGestureMinimumTouchesRequired and SetPanGestureMaximumTouchesRequired in GestureOptions has been added.
  - VirtualRemocon and VirtualMouse in sub device types has been added.
  - Support geometry-based touch and gestures.
- Text
  - Support Full Screen IME
  - A new ellipsis mode (Auto Scroll)
  - Support Variable Font
  - Text cache face size pool for memory optimization
  - Better Asynchronous Text with separated FontConfig handle.
- Rendering
  - More Blur option- Content Blur, Blur Strength animation, blur Once.
  - Improve Gradient Quality and Feature (Supporting Conic Gradient and Gradient Animation)
  - Support Alpha masking between 2 View.
  - Support Squircle Corner
  - Upgraded Shadow - Inner Shadow Supported, Multiple Shadow Supported
  - Support easy OffScreenRendering for a sub Scene tree.
  - Better Partial Update, Optimize sorting of damaged rect.
  - Using Separated Uniform Index Map for Shared UBO.
- Performance/memory improvement
  - Actor Ignored option to remove overhead of not rendered objects.
  - Optimize Rendering Pipeline - Pipeline Caching, Reduce GPU command size, and avoid unnecessary pipeline binding.
  - Initialize DALi adaptor on candidate thread.
  - Unified Event FD
  - Create Accessibility and Visual data on demand.
  - Shader Pipeline File Caching to improve App launching time.
  - Support Partial Rendering when the FBO is used.
- UI Test Automation
  - Enhance stability for long-term test execution
  - Support Java language interface
  - Support Image Resource Path information acquisition
  - Support popup removal functionality for test stability
  - Support interface to view hidden UI Objects
  - Support highlighted functionality
  - Improve DumpTree functionality performance
  - Support binder for Aurum C# support
  - Support automation ID for WebApp
  - Support OneUI Component test automation
  - Support resource ID acquisition functionality
- Vector Graphics
  - Optimize for complex shapes in lottie-player.
  - Support for clip-path tag.
- Markdown Renderer with NUI
- Accessibility
  - Add screen-reader multi window navigation support
  - Add screen-reader support for 3D Scene
  - Improve screen-reader support for webview

#### Fixes

  - Fix bug when find element with showing condition.
  - Fix memory leaks
  - Fix memory corruption
  - Fix strict weak ordering.
  - Fix the bug of reloading setting
  - Fix the bug of cancel button on Popup
  - Fix the bug of invalid behavior in step menu
  - Fix parameter for catch
  - Fix the bug of ordering object.
  - Fix Dialog and AlertDialog behaviours for Accessibility.
  - Fix View to use control-accessible State::SENSITIVE for Accessibility.
  - Fix Navigator to support Page with Transitions.
  - Fix Various Accessibility defects.
  - Fix Various LottieAnimation defects.
  - Fix Various WidgetView defects.
  - Fix the bug during touch event hittest.
  - Fix SVG image loading defects.
  - Fix Various Text defects.
  - Fix Aurum crash issue.
  - Optimize screen-reader memory usage


### Multimedia framework

#### New and changed features

- Open source
  - ffmpeg version 6.1 has been upgraded to version 7.1.
  - tiff version 4.6.0 has been upgraded to version 4.7.0.
  - GraphicsMagick version 1.3.42 has been upgraded to version 1.3.45.
  - libwebp version 1.3.2 has been upgraded to version 1.4.0.
  - libjpeg-turbo version 3.0.1 has been upgraded to version 3.0.4.
  - libpng version 1.6.40 has been upgraded to version 1.6.44.
  - giflib version 5.2.1 has been upgraded to version 5.2.2.
  - libjxl version 0.7.0 has been upgraded to version 0.11.1.
  - gstreamer version 1.22.8 has been upgraded to version 1.24.11.
  - orc version 0.4.34 has been upgraded to version 0.4.40.
  - libnice version 0.1.21 has been upgraded to version 0.1.22.
- Media Common
  - New media format for RGB has been added.
- Media Codec
  - Support new media format for RGB.
  - Tizen codec HAL(Hardware Abtraction Layer) interface has beed added.
    - The GStreamer plugin for Tizen codec HAL has been added.
    - The reference backend using V4L2 interface for Tizen codec HAL has been added.
    - It supports HAL backend service via TIDL.
- Media Content
  - Deprecated APIs from Tizen 8.0 have been removed.
  - Exception handling for ".scan_ignore" has been removed.
  - New enum for collate type to support natural sort have been added.
- Native WebRTC
  - Empty ICE candidate as the end-of-candidates marker has been added.
  - PCMU/PCMA formats have been supported to the encoded audio frame callback.
  - FPS and key frame information have been supported to the encoded video frame callback.
  - libsmack dependency has been replaced with cynara-creds-self.
- Audio IO
  - Add float32 audio sample type enumeration.
- Sound Pool
  - All APIs have been deprecated.
- Media Demuxer
  - All APIs have been deprecated.
- Media Muxer
  - All APIs have been deprecated.
- Screen Mirroring
  - New display control APIs have been added for screen mirroring sink.

#### Fixes

- Audio Frameworks
  - Fixed ducking to wait finish of another ducking operation of same target stream.
  - Fixed ducking state changed callback is not invoked if the first duration of the ramp is 0 and non-zero thereafter.
  - Fixed built-in device couldn't be selected as a preemptive device.
  - Fixed unexpected pulseaudio self-kill due to insufficient threshold of real-time scheduling.
  - Fixed focus nodes being disappeared at certain timings.
  - Fixed focus nodes could not be removed on exit due to insufficient permissions.
- Media Common
  - Fixed invalid return value for AAC type via media format APIs.
- Media Codec
  - Fixed MJPEG encoding and decoding failure.
  - Fixed invalid return value when feature is not supported.
  - Fixed invalid bitrate setting via media format handle.

### Network and connectivity

#### New and changed features

- Open Source
  - Bluez
    - Version 5.70 has been upgraded to version 5.79.
  - Connman
    - Version 1.41 has been upgraded to version 1.42.
  - curl
    - Version 8.5.0 has been upgraded to version 8.11.0.
  - mdnsresponder
    - Version has been updated from 1310.140.1 to 1556.80.2.
- Bluetooth
  - GATT service app slot expansion.
    - The maximum number of apps that can be registered has been set to 50.
  - The API call time has been optimized.
- Download
  - Rate limiting have been added.
    - The maxinum rate for download.
- Iotcon
  - All APIs have been deprecated.
- Network
  - New APIs for handling the frequency value of stored Wi-Fi configuration have been added.
  - The URLs used during the online status check has been changed.
  - New options for Wi-Fi roaming have been added.
    - An option to use signal-based network selection has been added.
    - An option to change the roaming scan interval is added.
    - An option to do a full scan every time when try to auto-connect is added.
  - PNS(Preference-based Network Selection) feature has been added.
- Smartcard
  - All APIs have been deprecated.
- Stc
  - All APIs have been deprecated.
- Telephony
  - All APIs have been deprecated.

#### Fixes

- Bluetooth
  - The crash issue when create bond fails has been fixed.
  - The crash issue when GATT notification register fails has been fixed.
  - The issue where pb get size fail event does not occur has been fixed.
  - The LE bond timeout issue has been fixed.
  - The crash issue when socket fd is -1 has been fixed.
  - The blocking issue when calling recvmsg has been fixed.
  - The issue where auto-pair-blocklist file size continuing to grow when bond fails has been fixed.
- Network
  - The logic to retry Wi-Fi roaming has been fixed.
  - The logic to create Wi-Fi interface has been fixed.
  - Stack OOB Write Vulnerability issue has been fixed.
  - The logic to load Wi-Fi configuration has been fixed.
  - The logic to convert prefix to netmask has been fixed.
  - The issue where NTP is not restarted when timeserver is changed has been fixed.
  - The logic to parse IEs has been fixed.
  - The logic to scan multiple SSIDs and frequencies has been fixed.

### Security

#### New and changed features

- HAL Introduction to Tizen Security Modules
  - The HAL concept has been introduced to key-manager, device-certificate-manager, and auth-fw.
  - The HAL API for security modules are defined in hal_api_security(platform/hal/api/security).
- New Padding support in Key-manager
  - Key-manager supports no padding and ISO9797_M2 Support in AES/CBC.
- Multiple security-config support
  - The security-config-ext allows each product owner to extends security-config for their own services and configurations.


### Service framework

#### Fixes

- Location
  - Potential defects have been fixed.
- Email
  - Potential defects have been fixed.

### Web framework

#### New and changed features

- Open Source Upgrade
  - Chromium
    - Version 120.0.6099.5 has been upgraded to version 130.0.6723.116.
  - Electron
    - Version 28.1 has been upgraded to version 33.3.0.
  - Node
    - Version 18.18 has been upgraded to version 20.18.
  - Clang
    - Version 18 has been upgraded to 20.
- Tizen Web Engine
  - Improved app launching time using lazy loading of libraries
  - Replaced direct access to /proc/xxx/attr/current path with cynara and security api.
  - Copy&Paste has been replaced with evas/eina functionalities.
  - Enabled shared library component for v8 and node.
  - [MM] Update Video co-ordinates on media thread.
  - [MM] Support XRGB format.
  - [MM] Support BGRX and BGRA formats from TBM.

#### Fixes

- Fixed Screencast feature not working on RWI.
- Fixed Webapp only having background-color not showing.
- Fixed crash issue in SelectionMagnifier related to improper parent elm object.
- Fixed crash issue related to the IME when navigating to a new page with link.
- Applied triple buffer only for NUI.


### Lightweight Web Solution

#### New and changed features

- Lightweight Web Engine
  - Web Engine
    - More SVG-related features have been additionally implemented
  - JavaScript Engine
    - ECMAscript feature (from ECMAScript 2024) has been added.
      - JSON.parse and source text access
      - Float16Array
      - Iterator Helpers

#### Fixes

- Lightweight Web Engine
  - Web Engine
    - Incorrect padding area calculation issue has been fixed
    - SVG mask related bugs have been fixed
    - Custom property bugs have been fixed


### Tizen .NET

#### New and changed features

- TizenFx
  - Tizen.Maps has been removed.
  - Tizen.Messaging.Email has been removed.
  - Tizen.Account.FidoClient has been removed.
  - Tizen.Location.Geofence has been removed.
  - Tizen.Messaging.Messages has been removed.
  - Tizen.Applications.PackageManager
    - New property for first installed time has been added.
  - Tizen.Network.Smartcard has been deprecated.
  - Tizen.Network.WiFi
    - New method to remove configuration has been added.
  - Tizen.Network.IoTConnectivity has been deprecated.
  - Tizen.Context has been deprecated.
  - Tizen.NUI
    - Classes for Xaml have been deprecated.
    - Methods for adding AlphaFunction have been deprecated.
  - Tizen.Network.Nsd has been deprecated.
  - Tizen.Network.Stc has been deprecated.
  - Tizen.Telephony has been deprecated.
  - Tizen.Multimedia
    - New mime types for audio, video have been added.
  - Tizen.System.SystemSettings
    - OOBE(Out Of Box Experience) has been added.
  - Tizen.Applications.PackageManager
    - New package type: RPK has been added.
  - Tizen.Multimedia.Remoting
    - New display mode and device type have been added.
  - Tizen.Multimedia.Remoting
    - Folder scanning functionality by specific file has been removed.
  - Tizen.Network.WifiDirect
    - New enumerations and methods for VSIE have been added.
  - Tizen.Nlp has been removed.
  - Tizen.Content.MediaContent
    - Deprecated CreateThumbnailAsync() methods have been removed.

### Machine learning

#### New and changed features

  - Machine Learning (ML) API updates
    - ML API has been upgraded to version 1.8.8.
      - Add NNFW enum type to support llama.cpp and features of Tizen ML HAL.
      - Add new functionality to apply asynchronous inference and flexible tensor data.

  - NNStreamer and related modules update
    - NNStreamer has been upgraded to version 2.4.4.
      - Add new inference filter to support various H/W accelerators of Tizen ML HAL.
      - Add new inference filter to support the llama.cpp.
      - Add new inference filter to support the llama2.c (Experimental).
      - Update NNStreamer plugins and callbacks to support asynchronous inference and flexible tensor stream.
      - Add ORC functions for 64bit integers (SIMD).

  - Open source updates
    - TensorFlow-Lite2 has been upgraded to version 2.18.0, which enables XNNPack and ARM Kleidi.
    - Flatbuffers has been upgraded to version 24.3.25.

#### Fixes
  - Reported bugs in NNStreamer and ML API have been fixed.

#### Known issues
  - Clang has been required to build the TensorFlow-Lite2 with enabling XNNPack and ARM Kleidi.
