# Tizen 6.0 Public M2 Release Notes

Release date: Oct. 15, 2020


## Release Notes

### System (Kernel and System framework)

#### New and changed features

- Kernel upgrade
  - Kernel for Raspberry Pi 4 has been upgraded to version 5.4y.
- 64Bit Kernel and Boot Support
  - 64Bit supported Kernel and Boot for Raspberry Pi 4
- Lightweight KSM
  - Reference implementation of lightweight version of Kernel Samepage Merging (LKSM) in Raspberry PI 4 Kernel and resourced extension with LKSM
- System management
  - Runtime storage verification with dm-verity has been developed.
  - Systemd has been optimized for better boot performance.
- D-Bus
  - Algorithms for D-Bus policy check have been improved for reducing dbus call latency.
  - D-Bus implementation on public API set has been optimized.
- Logger
  - QoS feature has been developed for fairly limiting and fully utilizing log usage.
  - Deduplication feature has been developed for preventing repeated logs.
  - CPU usage on dlog_logger has been optimized with added configurations.
- Device and resource management
  - Doze mode has been developed for power saving during lcd-off period.
  - Always-on-display feature has been improved for better user experience.
  - Configurable CPU pinning for heterogeneous cores has been developed.
  - Monitoring for CPU lock timeout has been improved to prevent battery drain.
  - C API set for obtaining battery information has been added.
  - C# API set for power management QoS has been added.

#### Fixes

- System and device management
  - Emergency mode has been fixed to remove wrong service dependencies.


### System (System Reliability & OS Upgrade)

#### New and changed features

- Update package signing/verification has been enhanced.
- Recovery package signer/verifier has been added.
- Removable storage-based update/recovery has been supported. 
- Update result API has been enhanced.
- Diagnostics API, which can be used to retrieve diagnostic information from the system like system crash, has been added.
- Ability to resolve callstack from updatable applications has been added.
- Size-reduced coredumps for C# programs have been added.


### System (Base)

#### New and changed features

- The capi-base-utils API set has been expanded.
  - New
    - ures: Resource management module.

#### Fixes

- The capi-system-system-settings API has been refactored.


### Application framework

#### New and changed features

- TIDL Extension
  - API set
    - The API set for synchronous connection has been added.
    - New keywords for sharing files have been added.
  - Tools
    - Tools for analyzing latency and throughput have been provided.
    - The enhanced TIDL compiler using receive threads to improve concurrency has been provided.
- Multi-package installer
  - API set
    - The API set has been provided to install multiple packages at once.
  - Tools
    - Tools have been provided to install multiple packages at once.
- Tizen Theme Manager
  - Getting resources
    - The API set for obtaining related resources path using a specific resource key has been provided.
  - Theme changed event
    - The API set for receiving the changed event from the app when changing the settings has been provided.
  - Theme overlay
    - Overlay function between default theme and selected theme has been provided.


### Window and Interaction

#### New and changed features

- Interaction
  - Gesture FW & engine
    - The API set to receive the event for hand gesture has been supported.
    - Gesture Framework for managing multi gesture clients and engines has been supported.
    - The service app for default gesture engine has been supported.
    - Support for on-demand daemon launch has been added.
- Enlightenment Wayland display server
  - Display Compatibility for the Legacy Widget Application has been added. Legacy Widget applications can display on the screen of which size is different from the one of application without the modification.
- Ecore Buffer
  - The ecore-buffer and ecore-buffer-queue API set has been deprecated.
- Tizen-ws-shell
  - A new enumeration has been added to support a new type of quickpanel service.
- Quickpanel C# Support
  - C# API set for quickpanel client and service has been added. (Tizen.NUI.WindowSystem.Shell)
- The libds API set that can be used to create and configure wayland-based display server has been newly added.


### Graphics Engine

#### New and changed features

- DALi (3D UI Toolkit)
  - All API set of DALi has been deprecated. NUI (DALi C# layer) replaces DALi API set.
- NUI
  - Common
    - Throwing an exception has been added when some methods are used in worker threads.
    - Support for ComponentApplications has been added.
  - Image
    - Support for WebP image has been added.
    - Support for asynchronous loading of gif images has been added.
  - Input
    - The keyboard repeat setting changed event has been added.
  - Utility
    - Some Capture API set has been added.

#### Fixes

- NUI
  - View
    - The size bug of the View has been fixed when setting the size and animating the size are used at the same time.
    - A PropertyNotification bug has been fixed.
    - Some bugs of GaussianBlurVies have been fixed.
    - Some bugs of TextLabels have been fixed.
  - Common
    - Some memory leak bugs have been fixed.


### UI framework

#### New and changed features

- EFL
  - Version 1.24 has been upgraded to version 1.25.
  - Support for gengrid has been added for wearable profile.
  - Support for evas vector graphic has been added.
  - Support for relative container has been added.


### Multimedia framework

#### New and changed features

- Camera
  - Support for platform privilege has been added.
- MediaStreamer
  - Native WebRTC API set has been added.
    - MEDIA_STREAMER_PARAM_WEBRTC_PEER_TYPE
    - MEDIA_STREAMER_PARAM_WEBRTC_STUN_SERVER
    - MEDIA_STREAMER_PARAM_WEBRTC_REMOTE_SESSION_DESCRIPTION
    - MEDIA_STREAMER_PARAM_WEBRTC_ADD_ICE_CANDIDATE
    - MEDIA_STREAMER_PARAM_WEBRTC_RTP_TRANSCEIVER_DIRECTION_FOR_AUDIO
    - MEDIA_STREAMER_PARAM_WEBRTC_RTP_TRANSCEIVER_DIRECTION_FOR_VIDEO
    - MEDIA_STREAMER_PARAM_MAX_LATENESS
    - MEDIA_STREAMER_PARAM_RTP_LATENCY
    - media_streamer_node_decoded_ready_cb
    - media_streamer_node_set_decoded_ready_cb
    - media_streamer_node_unset_decoded_ready_cb
    - media_streamer_webrtc_node_set_message_cb
    - media_streamer_webrtc_node_unset_message_cb
- Image Util
  - Support for WebP has been added.
  - Support for encoding for GIF and WebP animation has been added.
  - Support for ARGB and GBRA for PNG encoding has been added.
- Metadata Editor
  - Support for WAV, FLAC, and OGG has been added.
- Media Controller
  - Result codes for command have been added.
  - Three Playback states have been added. (Connection, Buffering, and Error)
- Media Vision
  - New enumerations for human pose landmark and body part have been added.
  - API set to detect pose landmark, i.e., human body pose, has been added.
- Recorder
  - API set to decide video frame encoding has been added.
  - Support for video scaling has been added.
    - It is only for single video stream supported device.


### Network and Connectivity

#### New and changed features

- Connection API
  - Following API set to require new partner level privilege has been changed.
    - New privilege: http://tizen.org/privilege/network.route
    - Privilege level: partner
    - Affected API set
      - connection_add_route
      - connection_remove_route
      - connection_add_route_ipv6
      - connection_remove_route_ipv6
      - connection_add_route_entry
      - connection_remove_route_entry
- Bluetooth mesh network
  - Bluetooth framework has been extended to support Bluetooth mesh network standard.
    - Platform API for Bluetooth mesh network features has been added.
    - Open source bluez module has been upgraded to support Bluetooth mesh network.
    - Tizen Bluetooth framework has been extended to control bluez’s mesh daemon.
  - Tizen devices will be able to do Bluetooth mesh network provisioning and control devices like smart blubs, which support Bluetooth mesh network standard.
- Wi-Fi multiple interface support
  - Network modules have been extended to support devices with multiple Wi-Fi network interfaces.
    - connman and net-config have been extended to identify a specific Wi-Fi network interface for its operations like scan and connect.
    - Platform API for specifying Wi-Fi network interface for each operation has been added for connection and wifi-manager API.
  - Public connection and wifi-manager API are backward compatible by introducing a concept of default Wi-Fi network interface.
- UWB (Ultra wideband) ranging
  - Platform API for UWB has been added.
  - UWB manager daemon has been added.
  - It has been tested with Decawave’s dwm1001 module on RPI4.
  - Devices with UWB modules will be able to measure distance between them.


### Security

#### New and changed features

- Security monitor
  - Query-based security API has been added.
  - Type-safe query builder has been added.
  - Support for Device Policy Management has been added.
- Privileges
  - New privilege has been added.
    - network.route


### Service framework

#### New and changed features

- Location Framework
  - Support for getting velocity accuracy has been added.
  - Support for getting location bounds to check on edge with tolerance has been added.
    - Support for checking on edge with tolerance for polygon has been added.
    - Support for checking on edge with tolerance for circle has been added.
    - Support for checking on edge with tolerance for rectangle has been added.
- Battery-Monitor Framework
  - Support for resetting battery dump data has been added.
  - Support for dumping application id with event of battery dump has been added.
- Context Framework
  - Motion API has been deprecated.

#### Fixes

- Context Framework
  - Fix for potential security vulnerability has been added.
- Location Framework
  - Precision improvement in getting distance between two locations has been added.


### Web framework

#### New and changed features

- Web engine
  - Feature support
    - Support for OffscreenCanvas has been added: OffscreenCanvas enables canvas rendering apart from the main thread.
  - Feature change/fix
    - Strict MIME type for module scripts: Loading module script from the local file feature has been removed.
    - App control URL bug fix: appcontrol:// scheme now able to launch application from encoded URL.
- Web runtime
  - Device API has been added for wrt-service.
  - Web server and web server has been added as a wrt-service built-in module.
  - WRT.js API management policy has been added.
    - API has been changed from generic js to type script.
    - API compatibility checker has been added.

#### Fixes

- Compatibility enhancement
  - The problem of autofill operation in major web site has been improved.
- Stability enhancement
  - Unexpected random crash while clean up sequence has been fixed.


### Lightweight Web Solution

#### New and changed features

- Rendering engine
  - Data Element's DOM API has been added.
  - Performance Web API set has been added.
  - Range Web API set has been added.
- JS Engine	
  - ES10 features have been added.
    - Array.prototype.flat
    - Array.prototype.flatMap
    - Object.fromEntries
    - String.prototype.trimStart
    - String.prototype.trimEnd
  - Following features' syntax has been updated.
    - Optional catch binding parameters
    - Allowing U+2028 (LINE SEPARATOR) and U+2029 (PARAGRAPH SEPARATOR) in string literals
  - Array.prototype.sort has been updated due to the specification change.
  - Function.prototype.toString has been updated due to the specification change.
- Performance and Memory Optimization
  - JS Engine
    - Debugger core features have been updated.
    - Lazy AtomicString initialization for memory/performance has been optimized.
    - Vector extension logic has been improved.

#### Fixes

- Bug fixes
  - Layout bugs have been fixed.
  - Scroll bugs have been fixed.
  - Font Rendering bugs have been fixed.
  - Memory overflow bugs have been fixed.
  - Crash issues have been fixed.


### Tizen .NET

#### New and changed features

- NET runtime and tools
  - .NETCore has been upgraded from 3.1.0 to 3.1.3.
- TizenFx
  - Tizen.NUI
    - VertexBuffer class has been added.
    - Pagination class has been added.
    - Screen connection methods have been added to CustomView class.
    - SlidingStarted event has been added to Slider class.
    - ThumbColor property has been added to Slider class.
    - FlexLayout and GridLayout have been added.
    - ScrollPosition and ScrollCurrentPosition have been added to ScrollableBase class.
    - Notification class has been added.
    - FlexContainer class has been deprecated.
    - IndicatorColor and SelectedIndicatorColor have been added to Pagination class.
    - Quickpanel has been added to WindowSystem.
  - Tizen.Network.Connection
    - Required privilege level has been changed.
  - Tizen.MachineLearning
    - Custom filter class has been added.
  - Tizen.Multimedia
    - Setter/Getter for volume recording has been added to AudioIO.
    - Result code and playback state have been added to MediaController.
    - New RequestCommand for async has been added to MediaController.
    - New barcode types have been added to Vision.
  - Tizen.Applications
    - Synchronous connection request and private file sharing have been added to RPCPort.
  - Tizen.Network
    - New Avrcp Control has been added to Bluetooth.


### Toolchain

#### New and changed features

- Toolchain configure dumper support has been developed.
  - "{package}-configure-dump.rpm" in binutils, glibc, and gcc have been provided with “dump_configure“ macro.
- Build with armv8-a machine option has been added.
- ASan has been enabled.
  - Automated build, test with JIRA reporting process have been established.
  - Libasansi feature for .NET ASan has been back-ported from Tizen 5.5.

#### Fixes

- Patches for CVE-2020-10029 have been back-ported in glibc from upstream.


### Machine Learning

#### New and changed features

- ML/Training API (new)
  - The ability to update and train deep neural networks on Tizen devices has been added.
  - The ML/Training API allows application developers to describe their own neural network models and train the models or to re-train pre-trained models in run-time.
- ML/Inference API update
  - The ability to use various hardware accelerators with Single API has been added.
  - The ability to fine-tune each element of a pipeline in run-time has been added.
  - The latency overheads of Single API have been reduced.
- NNStreamer update
  - NNStreamer has been upgraded from 1.5.2 to 1.6.0.
  - AI acceleration hardware support has been added.
    - ML API may utilize Verisicon-Vivante and Qualcomm-SNPE in addition to previously supported hardware.
      - You may need to download and install additional adaptors from tizen.org for these additional hardware supports.
  - The ability to import stream data from or export stream data to Flatbuffers and Protobuffers has been added for distributed or remote pipelines.
  - The ability to implement and insert tensor-converters for custom data types in run-time has been added.
- NNTrainer (new)
  - NNTrainer has been added to allow on-device neural network training, which mainly targets transfer learning mechanisms with a few simple layers.
  - NNTrainer provides various weight initializers, optimizers, activation functions, and loss functions.
  - Neural network models may be constructed by applications in run-time or may be loaded from a model file along with pre-trained weight values. The trained weight values can be saved and loaded later.
  - Data set for training may be generated by application in run-time or may be fetched from a filesystem.
- NNFW Runtime (ONE Runtime) update
  - NNFW Runtime has been upgraded from 1.4.0 to 1.9.0.
  - The ability to install extensions to provide customized performance optimization has been added.

#### Fixes

- ML/Inference API
  - Incorrect error codes have been fixed.
  - The edge-TPU and Movidius-X run-time issues have been fixed.

