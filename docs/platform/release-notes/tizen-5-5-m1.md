# Tizen 5.5 Public M1

Release date: May 31, 2019

The Tizen 5.5 Public M1 release provides developers with the Tizen kernel, device drivers, middleware subsystems, and Web and Native API set.


## Release Details

- [Getting source code](http://review.tizen.org/git/) (Tizen 5.5 M1 source codes are under **tizen_5.5** branch.)

- Getting binaries and images
  - Base: [http://download.tizen.org/releases/milestone/tizen/base/tizen-base_20190503.1/](http://download.tizen.org/releases/milestone/tizen/base/tizen-base_20190503.1/)
  - profile(unified): [http://download.tizen.org/releases/milestone/tizen/unified/tizen-unified_20190523.1/](http://download.tizen.org/releases/milestone/tizen/unified/tizen-unified_20190523.1/)

- [How to flash to a device](../developing/flashing.md)


## Release Notes

### System (Kernel and System framework)

#### New and changed features

- Kernel upgrade
  - Kernel for Raspberry Pi 3 and ODROID-XU3 has been upgraded to version 4.14.
- New API set and features
  - Activationd
    - Event-based activation has been developed.
  - D-Bus
    - A prototype of shared data structures using FlatBuffers has been developed.
    - New policy rules for security enhancement have been developed.
  - Deviced
    - API set for thermal management has been added.
    - Display image effect has been developed.
    - Touchscreen sensitivity control has been developed.
    - Plugin interfaces for submodules have been added.
    - Logdump utility has been developed.
  - Feedbackd
    - Standard and unlimited patterns have been developed.
  - edge-orchestration
    - Discover edge-orchestration device and registered service has been added.
    - Scoring device resource for registered service has been added.
    - Offloading service to other edge device has been added.
  - Network flashing
    - Flashing platform image through network has been developed.

#### Fixes

- System core modules
  - Deviced
    - Reliability during poweroff has been improved.
  - Systemd
    - Race conditions during boot sequence have been fixed.
    - CVE issues (CVE-2018-16864, CVE-2018-16865, and CVE-2018-16866) have been patched.
  - D-Bus
    - Upstream patches regarding memory leak have been added.
    - Race condition on libdbuspolicy has been fixed.


### System (IoT System)

#### New and changed features

- Memory management for long-lived process like background-locked application has been enhanced.
  - Separated memory cgroup for long-lived process has been added. When system goes to idle state, it proactively reclaims the long-lived memory of the process to provide better memory usage environment for devices with limited memory.
- Memory reclaim at boot can be configured (enabled and disabled).
- Watchdog functionalities for headless-device have been enhanced like headed-device.
- System-dump supports extension mechanism to dump vendor-specific information. In addition, system-dump dumps installed-package list for checking installed-app version as default behaviors.


### System (Base)

#### New and changed features

- Open source upgrade
  - icu (63.1)
  - Python (2.7.15)
  - sqlite (3.26.0)
  - tzdata (2018f)
  - gobject-introspection (1.52.1)
  - python-gobject (3.30.1)
  - python-cairo (1.17.0)
  - expat (2.2.6)
  - openfst (1.6.5) has been added.
  - file (5.35)
  - jsoncpp (1.8.4)
  - jsontool (9.0.6)
  - psmisc (23.2)
  - re2 (20181001)
  - gtk-doc (1.29)
  - xz (5.2.4)
  - itstool (2.0.5) has been added.
  - meson (0.49)
  - python-setuptools (40.6.3)
  - dos2unix (7.4.0)
  - libarchive (3.3.3)
  - libsolv (0.6.35)
  - perl-TimeDate (2.30)
  - re2c (1.1.1)
- Expanded the capi-system-settings API set:
  - Added system-settings key value
    - SYSTEM_SETTINGS_KEY_ACCESSIBILITY_GRAYSCALE
    - SYSTEM_SETTINGS_KEY_ACCESSIBILITY_NEGATIVE_COLOR
  - Added features for accessibility
    - http://tizen.org/feature/accessibility.grayscale
    - http://tizen.org/feature/accessibility.negative

#### Fixes

- CVE patches
  - libxslt : CVE-2019-11068
  - sqlite3: CVE-2019-9936
  - Python: CVE-2019-9740 and CVE-2019-9636
  - file : CVE-2019-8906


### Application framework

#### New and changed features

- New notification API set
  - Various types of notifications have been provided to represent various information.
- Improved app-control API set
  - API set for Uniform Resource Identifier (URI) has been provided.
  - A synchronous launch request API has been provided.
  - It allows applications to use API set that can be used separately for each request of app-control.
- Improved API set for package manager
  - A way to describe dependencies between packages has been provided.
  - API to get dependencies between packages has been provided.
- New C# API set
  - C# API set for watch-complication has been provided.
  - C# API set for application events has been provided.


### Window System

#### New and changed features

- Wayland
  - The open source wayland-protocols has been upgraded to version 1.16.
- Wayland extension
  - The tizen_launch_appinfo interface has been added. Display server can get the application information such as pids and appids from the clients.
- Enlightenment Wayland display server
  - Support for the accessibility screen zoom has been added. The system service can utilize this feature by using the Tizen shell magnifier functions of the tizen-ws-shell.
  - Support for the High (4K) resolution has been added. Display server can display the multi-resolution windows with the fullscreen size on a screen.
  - Support for various types of quickpanel has been added. In addition to the system default type quickpanel, a new context menu type quickpanel is also supported.
  - The focus history feature has been added to support queue-based management of window focus. It provides consistent focus policy to GUI applications for Tizen.
  - Taking a window capture has been updated to create an image file, which includes soft keyboard UI when a user is typing.
  - The window capture submodule has been refactored to improve reusability.
  - Reference implementation of ping-pong policy has been added to the e-mod-tizen-wm-policy module, which can be used to detect unresponsive GUI applications.
  - The e_dbus has been changed to support more reliable D-Bus connection in the multi-threaded environment.
  - The logging utility function ELOG has been changed to not use the parameter of e_pixmap.
  - The e_msg has been updated to provide better functionality when communicating between enlightenment modules.
  - The HWC Windows is enabled on the reference targets.
  - The debugging tool has been extended with support for:
    - -trace serial: print Tizen Buffer Manager (TBM) serial updates
- Tizen ws shell
  - New API set and enums for various types of quickpanel have been added as follows:
    - API set
      - tzsh_quickpanel_create_with_type
      - tzsh_quickpanel_type_get
    - Enums
      - TZSH_QUICKPANEL_TYPE_UNKNOWN
      - TZSH_QUICKPANEL_TYPE_SYSTEM_DEFAULT
      - TZSH_QUICKPANEL_TYPE_CONTEXT_MENU
  - The tzsh_quickpanel_create API has been deprecated since Tizen 5.5. It has been replaced by the new tzsh_quickpanel_create_with_type API.
  - Support for Tizen shell magnifier service has been added to make it easier to develop accessibility screen zoom module.
- Tizen Display Manager (TDM)
  - TDM provides the API set for managing the virtual outputs.
    - The wayland clients can create and destroy the virtual output.
    - The wayland clients can get the buffer, which is displayed on the virtual outputs.
  - The API set for TDM HWC has been added.
    - tdm_hwc_set_name
    - tdm_hwc_set_cursor_image
    - tdm_hwc_get_property
    - tdm_hwc_set_property
  - TDM backends of the reference targets enable the TDM HWC feature.
- Tizen Buffer Manager (TBM)
  - TBM_BO_TILED flag has been added. TBM backends use the tiled memory with this flag.
  - The API set for waiting the dequeue buffer has been added.
    - Tbm_surface_queue_can_dequeue_wait_timeout
- Mesa
  - Mesa has been upgraded from version 17.1.0 to version 19.0.0.
- Vulkan
  - Vulkan has been upgraded from version 1.1.74 to version 1.1.92.
  - New Vulkan packages have been added:
    - Vulkan-Headers
    - Vulkan-Loader
    - Vulkan-Tools
    - Vulkan-ValidationLayers

#### Fixes

- libxkbcommon
  - Security vulnerabilities (CVE-2018-15858, CVE-2018-15859, CVE-2018-15861, CVE-2018-15863, CVE-2018-15862, and CVE-2018-15864) have been fixed.
- Enlightenment Wayland display server
  - Many code defects detected by the static analysis tool have been fixed.
  - Compilation warnings while building on the 64-bit architecture have been fixed.
  - Duplicated internal event generation for creation of window has been fixed.
  - Gesture recognition problem for the edge swipe using multi-fingers has been fixed.
  - Missed up event from the input generator has been fixed to pair up with the down event correctly.
- TBM
  - The defects related to the mutex lock have been fixed.
- TDM
  - Many defects related to tdm_hwc have been fixed.
  - The tdm_hwc implementation of the tdm backends has been fixed.
    - libtdm-exynos
    - libtdm-exynos-deconfb
    - libtdm-sprd
    - libtdm-vc4
- TPL-EGL
  - Many deadlock defects on the tpl-egl thread have been fixed.
  - The timeout function to wait for the dequeue buffer has been added in order to fix the dequeue deadlock.


### Graphics Engine

#### New and changed features

- DALi (3D UI Toolkit)
  - Actor and Renderer
    - RENDERING_BEHAVIOR property has been added to Renderer.
    - Support for multiple window rendering has been added.
    - Move semantics have been added to Property::Array, Property::Map, and Property::Value.
  - API
    - Deprecated API set in Tizen 3.0 has been removed.
  - Performance
    - Some classes have been refactored to reduce binary size.
  - Image
    - An API to get an original image size has been added.
  - Text
    - Support for circular text has been added.
    - Feature to support layout text and icons has been added.
    - Support for bitmap fonts has been added.
    - Some text render utils have been added.
  - Control and Visual
    - AnimatedVectorImageVisual has been added.
    - VisualEventSignal has been added to Control.
  - Input
    - DragAndDropDetector has been added.
  - NUI
    - JavaScript Interface API set has been added to WebView.
    - PluginParser has been added to support OpenGL or Vulkan backend switching.
    - ViewAdded event has been added to window.
    - LogicalKey and KeyPressed properties have been added to Key.
    - VectorAnimationView (DALi Lottie) has been added to NUI.
    - Interop classes are added to NUI.
    - Layout implementation has been moved from DALi to NUI.

#### Fixes

- DALi (3D UI Toolkit)
  - Image
    - JPEG encoder bug has been fixed.
  - Text
    - Software italic and bold issues have been fixed.
    - Right-To-Left (RTL) behavior bug in Markup language has been fixed.
    - An incorrect ellipsis bug has been fixed.
  - Control and Visual
    - Resource leaks in layoutting have been fixed.
    - A ResourceReady signal bug has been fixed.
    - A RELOAD action bug of ImageVisual has been fixed.
    - A PRE_MULTIPLIED_ALPHA property bug of ImageView has been fixed.
  - NUI
    - SynchronouseLoading and OrientationCorrection bugs have been fixed when the Image property is set.
    - A crash has been fixed when reLayout is done by adding or removing child.
    - Null handle of Renderer return error has been fixed.
    - Crash of WatchApplication has been fixed.
    - Transition, DynamicResource, and Style related issues of NUI XAML have been fixed.


### UI framework

#### New and changed features

- EFL
  - Version 1.21 is upgraded to version 1.22.
  - Meson build system support has been added (beta).
  - Lottie animation viewer has been added.
  - Evas map quality has been improved.
- Atk
  - Version 2.28.1 is upgraded to version 2.30.0.
- At-spi2-core
  - Version 2.26.1 is upgraded to version 2.31.1.
- At-spi2-atk
  - Version 2.26.1 is upgraded to version 2.30.0.
- Fontconfig
  - Version 2.13.0 is upgraded to version 2.13.1.
- Fribidi
  - Version 1.0.2 is upgraded to version 2.0.5.
- Harfbuzz
  - Version 1.8.1 is upgraded to version 2.4.0.
- rlottie
  - Lottie file support has been added.

#### Known Issues

- Accessibility toolkit packages support meson build system only:
  - Atk, At-spi2-core, and At-spi2-atk
- Elementary uses legacy focus policy rather than the recent focus manager for compatibility issue.


### Interaction Framework

#### New and changed features

- Multi-assistant framework
  - Tizen now supports multi-assistant framework that supports multiple assistants at the same time.
- Speech recognition engine
  - Embedded speech recognition engine has been added as a Speech To Text (STT) engine. For supporting an environment without internet, you can now optionally use an embedded based speech recognition engine in your application.
- Autofill framework
  - Autofill API set that allows you to automatically fill out commonly entered information has been added.
  - IME API set that gets the key code and the visibility state of a candidate has been added.


### Multimedia framework

#### New and changed features

- MediaTool
  - API set to support audio channel mask has been added.
- Media Player
  - Audio offloading support has been added.
  - Some display type has been removed.
  - API set for progressive download has been removed.
  - The player_get_streaming_download_progress precondition has been extended.
  - The range of parameter values of buffering related function has been changed and the value of -1 has been allowed.
  - Support for controlling the audio pitch has been added.
- Media Controller
  - Management of content season, episode, and resolution metadata has been added.
  - Support for getting and counting playlists has been updated.
  - Support for counting search conditions has been added.
- Image Util
  - image_util_calculate_buffer_size() has been deprecated.
  - Sync transform API set (convert, crop, resize, and rotate) has been added.
- Thumbnail Util
  - Support to extract thumbnails even if requested size exceeds the source size has been added.
- Camera
  - Buffer sharing mechanism to improve buffer protection has been changed.
  - Support for user allocated buffer for zero copy preview has been added.
- Recorder
  - Buffer sharing mechanism to improve buffer protection has been changed.
- Audio IO
  - Support for applying VoIP latency in case of VoIP audio type has been added.
- PulseAudio
  - Support for triggering audio ducking effect by recording stream has been added.
  - Support for applying volume type to loopback stream has been added.
  - Support for getting the pid of the latest stream has been added.
  - Support for individual volume has been added.
- Audio HAL
  - API to set volume ratio to control H/W volume according to each stream type has been added.
- C# API
  - Common
    - Deprecated (platform invoke) P/Invoke functions have been changed to recommended functions.
  - AudioManager
    - API to check whether any stream from the current AudioStreamPolicy is actually using the device has been added.
  - ImageUtil
    - API set to calculate buffer size has been deprecated.
  - MediaContent
    - API set to control storage information has been deprecated.
    - The possibility of MediaContent DB inconsistency has been removed.
  - MediaTool
    - API set to set max bps and duration of MediaTool has been added.
  - MediaPlayer
    - API set to control AudioPitch has been added.
    - The precondition of GetDownloadProgress API has been changed.
    - Description of Preparing state restriction has been added.
    - The range and default value related BufferingTime have been changed.
  - Metadata
    - API to set composer has been added.

#### Fixes

- Media Content
  - media_info_insert_to_db() returns the updated media information. Earlier, this API returned the media information without verifying whether it was up-to-date.
  - media_face_create() support only for the images has been added.
- Sound Manager
  - Timeout issue of acquiring or releasing focus in focus watch callback when the previous request is in progress has been fixed.
- PulseAudio
  - Invalid device of virtual stream issue in case of device connection change has been fixed.
- C# API
  - Camera
    - Block issue caused by calculating preview buffer size has been fixed.
  - MediaController
    -  The playlist missing in P/Invoke issue has been fixed.
  - MediaPlayer
    - SetPlayPosition() block issue with MediaStreamSource has been fixed.
- Multimedia Daemon
  - Murphy
    - The launching failure issue with the pid file has been fixed.
  - Mm-resource-manager
    - The issue of the GDBus method related with the USB detachable has been fixed.
  - Muse-server
    - The busy loop issue caused for high CPU usage has been fixed.


### Network and Connectivity

#### New and changed features

- User awareness framework
  - A framework for user detection based on multiple sensors has been added.
- Bluetooth A2DP multipoint connection support
  - Advanced Audio Distribution Profile (A2DP) sink target can support up to two different source devices.
- Wi-Fi band steering
  - Band steering mechanism between 2.4GHz and 5GHz of the same AP has been added.
- API changes
  - Intelligent network monitoring
    - API to get network interface link information has been added.
    - API to test network connection status (availability of gateway and DNS server) has been added.
    - API to test reachability of HTTP server has been added.
  - Wi-Fi manager
    - API to get whether 5GHz band is supported has been added.
    - API set to get Extensible Authentication Protocol (EAP) anonymous identity has been added.
  - Bluetooth
    - Privilege level of out of band (OOB) data getter API has been changed.
  - Smart traffic control
    - API to clone and destroy statistics info handle has been added.
    - Legacy API to get statistics info asynchronously has been deprecated.
    - API to get all statistics info has been added.
    - Legacy API to get total statistics info has been deprecated.
  - curl version up (7.62.0)
  - C# API
    - BluetoothLeDevice API set getting the remote device information has been added.
    - Legacy C# Gatt API has been deprecated.
    - New BluetoothGattClient C# API has been added.
    - BluetoothLeDevice API set getting the remote device information has been deprecated.
    - Bluetooth - Wrong AcceptStateChangedEventArgs class property and DestroyServerSocket API has been deprecated.
    - Bluetooth - New SocketConnection class property has been added.
    - Bluetooth - API to destroy Gatt server has been added.
    - STC C# API has been added.
    - API to check Wi-Fi scan state has been added.
    - API to check cellular roaming state has been added.
    - Wi-Fi - Exceptions to provide accurate error information has been added.


### Security

#### New and changed features

- Security-manager
  - Smack rules will be loaded directly from security-manager DB. All rule files have been removed.
- Privilege
  - The following privileges have been added:
    - autofillmanager, internal/buxton/systemsetting, filesystem.read, filesystem.write, windowsystem.admin, d2d.datasharing, d2d.remotelaunch
- Privilege-info
  - New API has been added.
    - Getting several privilege information as list.


### Service framework

#### Fixes

- Account-Manager
  - Unwanted D-Bus API calls have been removed.
  - Memory leaks have been fixed.
  - Fix to remove provider information from global account db has been added.
- Sync-Manager
  - Additional D-Bus error handling has been enabled.
  - Potential defects have been fixed.
- Calendar-service
  - Support for calendar DB purge when a device is reset has been added.
  - Potential defects have been fixed.
- Email-service
  - Potential defects have been fixed.
- Message Service
  - Potential defects have been fixed.
- Location Service
  - Potential defects have been fixed.
  - Deprecated capi-network-wifi dependency has been replaced.
- Sensord
  - Potential defects have been fixed.
  - Timestamp data type issue has been fixed.
- Phonenumber-Utils
  - Potential defects have been fixed.


### Web framework

#### New and changed features

- Web Engine
  - Web Engine Upgrade Framework has been added.
    - chromium-efl package can be upgraded with TPK, not whole image upgrade.
    - chromium-efl-squashfs package has been added to provide the preload web engine as a squashfs image file, not regular file.
    - chromium-efl squashfs image file has been compressed by about 60%.
    - chromium-efl, chromium-efl-update systemd services have been added for squashfs image mount.
    - chromium-efl-install systemd service has been added for tpk installation.
  - C# API
    - WebView
      - API set to resume or suspend has been added.
      - API set to handle scale, scroll, zoom, and orientation has been added.
      - API to load URL with given request date has been added.
      - API to find text in page has been added.
      - Events to handle policy decision have been added.
      - Event and delegate to handle context menu have been added.
    - BackForwardList
      - API set to handle back or forward list has been added.
    - Context
      - API to clear resource cache has been added.
    - ContextMenu
      - API set to handle context menu has been added.
    - PolicyDecision
      - API set to handle navigation policy decision has been added.
      - API set to handle response policy decision has been added.
      - API set to handle new window policy decision has been added.
    - Settings
      - API to set whether window can be opened by script has been added.
  - Autofill
    - Autofill feature that works with autofill framework has been added.
    - This feature automatically fills out a login form with appropriate data from autofill framework.
    - Supports default popups for authentication and accounts.
  - CSS Scroll Snap feature has been added.
  - IME support for NUI has been added.
- Web Runtime
  - WRTjs (the new type of JavaScript-based WRT Framework) has been added.
  - WRTjs is based on the open source Electron project.
  - Compatibility with the legacy Tizen WRT Apps has been provided.
  - Compatibility with the existing Tizen API set has been provided.
  - Legacy WRT (xwalk-based runtime) has been deprecated.
- Web application development environment for Tizen Platform has improved.
  - The new components of TAU like Dimmer, Graph, Coverflow, and i3d have been added for multi-devices or rich application authoring.
  - Two-way data binding of components feature has been added for multi-devices.
  - The key-navigation and TV landscape layout feature has been added.
  - Web SDK based on VSCode extension is provided.
  - The IntelliSense function for Tizen WebApp SDK has been enhanced.


### Lightweight Web Solution

#### New and changed features

- Security modules
  - Content Security Policy (CSP) has been added.
  - Same Origin Policy (SOP) has been added.
- New backends
  - Support for Ecore_Wayland2 backend has been added.
  - Support for Evas_gl backend has been added.
- JS ES6 Features
  - Arrow function has been added.
  - Proxy has been added.
  - Reflect has been added.
  - Built-in functions have been added.
- Performance
  - Animation performance (transition) has been improved.
  - Type conversion performance in JS has been improved.

#### Fixes

- Bug fixes
  - Many layout bugs, including flex layout have been fixed.
  - Memory leaks have been fixed.
  - Crashes have been fixed.


### Tizen .NET

#### New and changed features

- .NET Core (Runtime)
  - .NETCore has been upgraded from 2.1.4 to 3.0.0 preview 2.
- Xamarin.Forms
  - Xamarin.Forms 3.6.0, which is latest stable version is supported.
- Tizen.CircularUI
  - Wearable UI extension (Tizen.Wearable.CircularUI) 1.2.0 is supported.
    - MediaPlayer and GoogleMapView are newly added.
- Tizen.Appium
  - Tizen.Appium, which is a service library for supporting UI automation test, 1.0.0 preview version is supported.
  - New project template (UI Test App) has been added.
- TizenFX
  - API set of storage ID and storage type has been deprecated.
  - Precondition of streaming API set to support more precise control has been changed.
  - Buffer size calculating API of ImageUtil has been deprecated.
  - New MediaPlayer API set to control an audio pitch has been added.
  - The behavior of MediaContent API to avoid inconsistency between DB and file system has been changed.
  - BluetoothLeDevice API set to get the remote device information has been deprecated.
  - New BluetoothLeDevice API set to get the remote device information has been added.
  - New Multimedia API set to support new content metadata has been added.
  - Gatt API set has been deprecated.
  - The range of parameter for buffering API of MediaPlayer and descriptions has been modified.
  - New PackageManager API set to get additional package information has been added.
  - New PackageManager API set to get additional archive information has been added.
  - New EventManager API set for application events has been added.
  - New Applications API set to get application's component type and category information has been added.
  - New feature key for external storage has been added.
  - New Bluetooth API set for handling Gatt client has been added.
  - New AudioManager API set for the stream information has been added.
  - New WebView API set to support more features has been added.
  - New Sensor API set to cover all the sensors has been added.
  - New Network API set to support Smart Traffic Control (STC) has been added.
  - New Bluetooth API set to destroy Gatt server has been added.
  - New SystemSettings API set for AccessibilityGrayscale and AccessibilityNegativeColor has been added.
  - NUI API set for text related properties has been deprecated.
  - New VoiceControlManager to support Voice Control Manager has been added.
  - New InputMethod API set to handle input has been added.
  - New DevicePolicyManager to support managing device policies has been added.
  - New MediaContent API set for composer property has been added.
  - New Bluetooth API set to add new Client property has been added.
  - New Alarm API set for WeekFlag, Period, and ScheduledDate has been added.
  - New Wi-Fi API set to provide accurate error information has been added.
  - New WidgetControl API set for MainAppId, PackageId properties has been added.
  - New DataControl API set for client appid and provider id has been added.
  - New MediaTool API set for the VideoMediaFormat has been added.
  - New AppControl API set to support sending the launch request asynchronously has been added.
  - New InputMethod API set to update the input panel event has been added.
  - New Application API set to add CurrentDeviceOrientation property for CoreUIApplication has been added.

#### Known Issues

- Xamarin.Forms
  - For more information on the list of limitations, see [here](../../application/dotnet/api/xamarin-forms-limitations.md).


### Toolchain

#### New and changed features

- ASan heap profile flags have been added to libsanitizer.
- ASan __libc_siglongjmp/__libc_longjmp interceptors have been added.
- Sanitizer feature has been improved.
  - asan-runtime-env package has been added to pre-installation list of mic.
  - ASan report description on stack traces has been improved.

#### Fixes

- CVE patchset (CVE-2017-16997, CVE-2018-6485, CVE-2018-19591, CVE-2019-9169, CVE-2019-6488, and CVE-2019-7309) for glibc have been applied.
- Bugfix patchset (#21081 and #22442) on glibc have been back-ported.


### Experimental

#### New and changed features

- nnfw: Neural Network Runtime (Experimental Release)
  - Support for new architecture design named 'neurun' for CPU/GPU mixed inference has been added.
  - Support for mixed acceleration for InceptionV3 and MobileNet model by manual planning has been added.
  - Android NN API compatible (Supports major operations selected carefully.)

- nnstreamer: Neural Network Streamer
   - An efficient and flexible stream pipeline to neural networks has been added.
   - Support for a neural network model as a media filter and converter has been added.
   - Support for multiple neural network models in a single stream pipeline instance has been added.
   - Support for multiple sources and stream paths for neural network models has been added.
   - Support for RNN and CNN model architectures with Tensorflow, Tensorflow-lite has been added.
   - Neural network API based on NNStreamer to manage pipelines has been added.
   - A plugin to support Linux IIO based on sensors has been added.
