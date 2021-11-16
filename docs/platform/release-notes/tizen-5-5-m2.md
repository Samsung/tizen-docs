# Tizen 5.5 Public M2

Release date: Oct. 30, 2019

The Tizen 5.5 Public M2 release provides developers with the Tizen kernel, device drivers, middleware subsystems, and Web and Native API set.


## Release Details

- [Getting source code](http://review.tizen.org/git/) (Tizen 5.5 M2 source codes are under **tizen_5.5** branch.)

- Getting binaries and images
  - Base: [http://download.tizen.org/releases/milestone/tizen/base/tizen-base_20191011.2/](http://download.tizen.org/releases/milestone/tizen/base/tizen-base_20191011.2/)
  - Profile(Unified): [http://download.tizen.org/releases/milestone/tizen/unified/tizen-unified_20191024.2/](http://download.tizen.org/releases/milestone/tizen/unified/tizen-unified_20191024.2/)

- [How to flash to a device](../developing/flashing.md)


## Release Notes

### System (Kernel and System framework)

#### New and changed features

- New API set and features
  - Fast boot
    - Unified barrier for system and session boot sequence has been developed.
    - On-demand activation has been applied to more services.
    - udev initialization in the user session has been optimized.
  - Activation and service control
    - Access control for system services has been developed.
    - Signal unicast-based activation has been developed.
  - D-Bus
    - Shared data structures using FlatBuffers have been developed.
    - Boot-time verifier for serialized policy rules has been developed.
    - D-Bus policy checker has been improved.
    - KDBus has been ported to 4.14 kernel.
  - Device and storage
    - Battery temperature monitoring has been improved.
    - Basic power saving mode has been added.
    - High and low brightness modes have been added.
    - Display control latency has been reduced.
    - Bezel control has been developed.
    - Power state configuration has been added.
    - Storage cleanup operations have been developed.
    - New features for display and external storage have been added.
  - edge-orchestration
    - Service offloading has been extended to execute service via multiple platforms such as Tizen, Android, and container.


### System (OS Upgrade and Reliability)

#### New and changed features

- OS upgrade
  - OS upgrade from Tizen 4.0 to Tizen 5.5 has been supported.
- System reliability
  - Web-based Callstack Analyzer Tool has been added for convenient coredump analysis.
  - Ability to create coredump from the live process has been added to examine the status of the live process. In addition, an interface to create crash-manager reports with live coredump has been added.
  - Stability monitor has been added to monitor and control resource utilization of CPU, IO, memory, number of open fds, and so on. 
    - According to the pre-determined maximum and average limits configuration, actions for system stability can be executed. The actions for system stability are live-coredump, notification, process termination, and so on.
    - Flexible configuration allows applying limits based on various process characteristics.

#### Known Issues

- OS upgrade
  - OS upgrade from Tizen 5.0 to Tizen 5.5 is not yet supported.


### System (Base)

#### New and changed features

- Open source
  - expat 
    - Version 2.2.6 has been upgraded to version 2.2.7.
  - perl-TimeDate 
    - Version 1.20 has been upgraded to version 2.30.
  - sqlite 
    - Version 3.26.0 has been upgraded to version 3.29.0.
  - pcre
    - Version 8.41 has been upgraded to version 8.43.
  - meson
    - Version 0.49.0 has been upgraded to version 0.51.2.
  - icu 
    - Version 63.1 has been upgraded to version 63.2.
  - tzdata 
    - Version 2018i has been upgraded to version 2019a.
  - augeas 
    - Version 1.10.1 has been upgraded to version 1.12.0.
  - boost 
    - Version 1.58.0 has been upgraded to version 1.65.1.
  - gtk-doc 
    - Version 1.29 has been upgraded to version 1.32.
  - libzip
    - Version 1.5.1 has been upgraded to version 1.5.2.
  - ninja
    - Version 1.7.0 has been upgraded to version 1.8.2.
  - re2
    - Version 20190101 has been upgraded to version 20190901.
  - golang (1.12.6) has been added.
  - libsigc++ (2.2.11) has been added.
  - mm-common (0.9.5) has been added.
  - python-ply (3.11) has been added.
  - python3-ply (3.11) has been added.
  - python3-lxml (4.3.0) has been added.
  - python3-six (1.10.0) has been added.
  - libglibmm (2.32.0) has been added.
  - libxml++ (2.34.2) has been added.
  - python3-MarkupSafe (1.0) has been added.
  - python3-argparse (1.4.0) has been added.
  - python3-funcsigs (1.0.2) has been added.
  - python3-linecache2 (1.0.0) has been added.
  - python3-mako (1.0.6) has been added.
  - python3-mock (2.0.0) has been added.
  - python3-nose (1.2.1) has been added.
  - python3-pbr (2.0.0) has been added.
  - python3-traceback2 (1.4.0) has been added.
  - python3-unittest2 (1.1.0) has been added.
  - Tinyxml2 (3.0.0) has been added.
- The capi-system-settings API set has been expanded:
  - system-settings key value has been added.
    - SYSTEM_SETTINGS_KEY_ROTARY_EVENT_ENABLED

#### Fixes

- CVE patches
  - glib
    - CVE-2019-12450
  - python
    - CVE-2019-9936
  - sqlite
    - CVE-2019-16168
  - libxslt
    - CVE-2019-13117
    - CVE-2019-13118


### Application framework

#### New and changed features

- New component-based application API set
  - Application model for UI components and service components to operate in one application process has been provided.
- New component manager API set
  - API set to query information of component-based applications has been provided.
- Improved API set for watchface complication
  - API to set timezone has been added.


### Window System

#### New and changed features

- Wayland
  - The open source wayland-protocols has been upgraded to version 1.17.
  - The libwayland-egl package has been provided by Wayland.
- Wayland extension
  - The tizen_input_device_manager protocol has been extended to support a request generation for the pointer and touch axis event.
  - The tizen_remote_surface_manager protocol has been extended to support a new request creation for the tizen_remote_surface interface. This new request allows the display server to bind wl_surface to tizen_remote_surface correctly.
  - The tizen_dpms protocol has been added. Display server can get the dpms request to control the dpms status of the display output.
- Enlightenment Wayland display server
  - Support for softkey has been added. It provides the same functionality as the H/W back key and home key in the S/W manner.
  - Support for the multi-outputs configuration has been added. The display server can manage multi-outputs to display an image on each output.
  - Support for the dpms protocol. Display server can support the wayland protocol for dpms.
  - Support for the custom launching window transition effect has been added. It allows the launcher application to perform various custom launching animation effect instead of the enlightenment display server through tizen-ws-shell.
  - Support for the seamless widget transition effect has been added. It supports seamless widget animation between one window to another window. Seamless animation is an animation that seamlessly transits from one window (occupying the current screen) to the other window (will occupy the next screen) and looks like a transition effect is running only on one window.
  - The `focus_policy_ext` configurable property has been added to support the window focus policy selection.
    - E_FOCUS_EXT_HISTORY: Default value. The queue-based window focus policy has been applied.
    - E_FOCUS_EXT_TOP_STACK: The topmost window focus policy has been applied.
  - The remote surface submodule has been refactored to improve reusability.
  - The debugging tool has been improved to show the transformed geometry data of windows and state of the GPU acceleration.
- Tizen Display Manager (TDM)
  - The API set for the output mirroring has been added.
    - tdm_output_set_mirror
    - tdm_output_unset_mirror
  - The libtdm-virtual backend support for TDM HWC has been added.
  - The tdm-monitor support for the fps option at the TDM HWC has been added.
- TPL-EGL
  - The libtpl-egl does not provide the libwayland-egl package. Wayland provides the libwayland-egl package.
- Tizen WS Shell
  - New API set and enums for softkey have been added as follows:
    - API set
      - tzsh_softkey_create
      - tzsh_softkey_destroy
      - tzsh_softkey_global_show
      - tzsh_softkey_global_hide
      - tzsh_softkey_global_visible_state_get
      - tzsh_softkey_global_expand_state_set
      - tzsh_softkey_global_expand_state_get
      - tzsh_softkey_global_opacity_state_set
      - tzsh_softkey_global_opacity_state_get
    - Enums
      - TZSH_SOFTKEY_STATE_VISIBLE_UNKNOWN
      - TZSH_SOFTKEY_STATE_VISIBLE_SHOW
      - TZSH_SOFTKEY_STATE_VISIBLE_HIDE
      - TZSH_SOFTKEY_STATE_EXPAND_UNKNOWN
      - TZSH_SOFTKEY_STATE_EXPAND_ON
      - TZSH_SOFTKEY_STATE_EXPAND_OFF
      - TZSH_SOFTKEY_STATE_OPACITY_UNKNOWN
      - TZSH_SOFTKEY_STATE_OPACITY_OPAQUE
      - TZSH_SOFTKEY_STATE_OPACITY_TRANSPARENT
  - The Tizen launcher service has been added to support the custom window transition effect and seamless widget transition effect.
  - tizen_shell_util has been added to support the generation of the input events.
- efl-util
  - New API set and enums for the generation of input axis event have been added as follows:
    - API set
      - efl_util_input_generate_wheel
      - efl_util_input_generate_touch_axis
    - Enums
      - EFL_UTIL_INPUT_POINTER_WHEEL_VERT
      - EFL_UTIL_INPUT_POINTER_WHEEL_HORZ

#### Fixes

- TBM
  - Code defects detected by the static analysis tool have been fixed.
- TDM
  - Defects detected by the static analysis tool have been fixed.
  - Test cases for the HAL have been fixed.
- libxkbcommon
  - Security vulnerabilities such as CVE-2018-15856, CVE-2018-15855, and CVE-2018-15853 have been fixed.
- Enlightenment Wayland display server
  - Code defects detected by the static analysis tool have been fixed.
  - Issue in which an infinite loop occurs when changing the window layer of the client window has been fixed.
  - Issue in which the pointer leave event occurs during touch down has been fixed.


### Graphics Engine

#### New and changed features

- DALi (3D UI Toolkit)
  - Actor, Window, and Renderer
    - Support for the off-screen buffer rendering has been added in additional windows.
    - An environment variable to set DPI has been added.
    - Support for setting a focus to each window has been added.
  - Performance
    - Support for uploading resources only without rendering has been added.
  - Backend
    - Support for Android backend has been added.
  - Text
    - Support for adjusting the text point size to match the size of the TextLabel has been added.
- NUI
  - NUI.Components has been added. 
    - Button
    - Loading
    - Popup
    - Progress
    - ScrollBar
    - Slider
    - Switch
    - Tab
    - Toast
  - API set for window rotations has been added.
  - API set for layouts has been added.
  - Dispose class has been refactored to reduce code duplication.

#### Fixes

- DALi
  - Actor, Window, and Renderer
    - Bugs for multiple windows have been fixed.
    - A SizeScalePolicy bug has been fixed.
    - A RenderTask bug has been fixed.
  - Text
    - A text ellipsis bug has been fixed.
- NUI
  - A crash of View.HasFocus has been fixed.
  - A bug of WatchApplication has been fixed.
  - A crash of LayoutController has been fixed.
  - Some memory leaks have been fixed.
  - Many bugs for views have been fixed.


### UI framework

#### New and changed features

- EFL
  - Version 1.22 has been upgraded to version 1.23.
  - Support for autotools has been removed.
  - Android 9-patch image support has been added.
  - Unicode variation selector support has been added.
- Accessibility
  - Universal switch AT-client has been tested.
- rlottie
  - Following vector properties have been added:
    - Shape trim path (individual)
    - Auto orient
    - Spatial Bezier interpolation
    - Reve across time
    - Mask path
    - Mask opacity
    - Mask add
    - Mask subtract
    - Mask intersect
    - Alpha matte
    - Alpha inverted matte
- Multi assistant framework
  - A reference default wakeup engine has been added.
  - New reference assistant such as google assistant has been added.
- Voice framework
  - New API set for voice control manager C# application has been added.
  - New API set for voice control engine has been added. The API set requests the voice control engine to synthesize text to speech using its own voice.
  - New API set to set audio type on the STT engine side has been added.
  - New API set to receive the utterance status has been added. The API set receives utterance status while you speak using STT.
- Autofill framework
  - API to cancel the fill request has been added.
- Sticker framework
  - A sticker framework that provides sticker information to the application and retrieves sticker information from the application has been added.

#### Fixes

- Memory consumption of rlottie has been improved.

#### Known Issues

- Universal switch application AT-client has been tested only in the Mobile profile.


### Multimedia framework

#### New and changed features

- Sound Manager
  - Audio ducking API set has been added.
  - API set for preferred built-in devices has been added.
  - API to support network devices has been added.
- Audio IO
  - Channel enum has been extended to support multi-channel recording.
  - Format enum has been extended to support S32LE playback and recording.
  - Deprecated symbols related to Unity have been added for compatibility.
- GStreamer-sharp
  - C# binding code for GStreamer on Tizen has been regenerated.
  - API to handle H/W resources and display has been added.
  - Xamarin sample applications that explain how to make custom pipeline with Tizen GStreamer plugins have been added.
  - Simple guideline for Tizen Xamarin application has been added.
- Media Player
  - API set for audio offloading has been added.
  - API to query about the supported format for push media stream has been added.
  - Support for audio pcm extraction has been added.
  - Support for setting audio codec type has been added.
- Vision
  - Deep Neural Network (DNN) based high-level vision inference API sets, such as image classification, object detection, face, and its landmark detection, have been added.
    - Support for TensorFlow Lite model data has been added.
    - Support for Caffe and TensorFlow model data with OpenCV has been added.
- Media Controller
  - API set to support subtitles, 360 mode, display mode, and display rotation has been added.
  - API set for ability has been added.
  - New error message has been added for ability not supported.
- Image Utility
  - API set for decoding and encoding an image has been updated.
- C# API
  - AudioIO
    - API set to support multi-channel and signed 32-bit audio sample has been added.
  - AudioManager
    - Audio ducking API set has been added.
    - API to support network devices has been added.
    - API to get preferred input, output devices has been added.
  - ImageUtil
    - API set to extract thumbnail synchronously has been added.
    - The condition of resizing thumbnail output size has been changed.
  - MediaCodec
    - The feature and exception tag of EventArgs class has been removed.
  - MediaContent
    - API to add face information has been added.
  - MediaController
    - API set to create an instance without a bundle has been added.
    - API set to support subtitles, 360 mode, display mode, and display rotation has been added.
  - MediaTool
    - API set to support PCM audio channel mapping has been added.
  - MediaPlayer
    - API set to export decoded audio and video data has been added.
    - The cancelable version of PrepareAsync API has been added.
    - API set to get supported audio and video types has been changed. The API can get all supported codec types defined by each target.
    - API to use audio offload has been added.
  - MediaVision
    - API set to support inference face detection, facial landmark detection, object detection, and image classification has been added.
- Multimedia Daemon
  - Resource-manager
    - New resource for audio offload has been added.

#### Fixes

- C# API
  - AudioIO
    - Crash issue caused by using the GC collected delegate has been fixed.
    - Block and crash issue caused by thread deadlock has been fixed.
  - AudioManager
    - Crash issue caused by marshaling safe handle has been fixed.
  - Camera
    - Missed exception of constructor has been fixed.
  - ImageUtil
    - Crash issue caused by marshaling buffer has been fixed.
  - MediaPlayer
- Crash issue caused by accessing null handle when enabling audio decided data has been fixed.
- Multimedia Daemon
  - Muse-server
    - Security vulnerability has been fixed.
    - Thread issues such as scheduling and ASAN when connecting an instance has been fixed.
    - Busy looping related to performance has been fixed.
  - Resource-manager
    - Forking failure of the PID file has been fixed.
    - Memory leak in the heap consistency check has been fixed.
    - Daemonizing issue related to GDBus has been fixed.
- Wav Player
  - WavPlayer
    - Unexpected complete callback invocation in case of stopping playback has been fixed.
- CVE patches
  - libsndfile
    - CVE-2019-3832
    - CVE-2018-19758
    - CVE-2018-19661 
    - CVE-2018-19662
    - CVE-2017-17456 
    - CVE-2017-17457
    - CVE-2017-14245
    - CVE-2017-14246
    - CVE-2017-8361
    - CVE-2017-8363
    - CVE-2017-8365

#### Known Issues

- Media Vision
  - Model data for the inference API set has not been provided. You can use model data in the open model zoo repository.


### Network and Connectivity

#### New and changed features

- User awareness framework
  - Combined condition of user detection for each service category has been introduced.
    - Applications can define their interests of sensors as combined conditions of supported sensors.
- Device provisioning protocol
  - Wi-Fi easy connect (DPP) specification has been developed.
- Connman
  - Connman has been upgraded to version 1.37.
  - WPA3 specification has been developed.
  - New configurations have been added.
    - If it uses gateway timeserver or not.
    - If it enables auto-ip configuration or not.
    - If it uses global nameserver configuration or not.
- wpa_supplicant
  - wpa_supplicant has been upgraded to version 2.8.
- Intelligent network monitoring
  - New platform API set for checking the reason for network error has been added.
- API changes
  - Wi-Fi manager
    - API to get the maximum number of SSIDs for the specific scan has been added.
    - API to get hidden property of access point has been added.
    - Security types for SAE, OWE, and DPP have been added.
  - Bluetooth
    - API to get a remote client's MTU value has been added.
    - API documents have been fixed for wrong list of possible return values.
  - Connection
    - API to get an internet connection state has been added.

#### Fixes

- Bluetooth
  - Many issues of BT/BLE features for RPI3 have been resolved.
  - The pairing logic of the headless profile was modified to support BR/EDR and LE pairing.


### Security

#### New and changed features

- Cynara
  - The cynara policy recovery mechanism has been added.
    - You can save the default policy at image creation time.
    - If a problem is detected when loading the Cynara policy, the policy is recovered with saved one and the flag file is created.
    - When the flag file is discovered, you can additionally re-installing all downloaded applications to generate the Cynara policy.
    - This feature has been added but hasn't been enabled. You must make the default policy and re-install downloaded applications when the flag file is created.
- Privilege
  - The application privilege policy has been changed.
    - The application can declare any privilege regardless of its profile or version.
    - The application always acquires the authorities of the declared privileges.
  - The following privileges have been added:
    - Voicecontrol.tts (partner level)
    - securesysteminfo (partner level)
    - The securesysteminfo privilege will be treated as a privacy privilege.
- Secure system information
  - The access permission to system information such as IMEI has been changed.
    - No third party application can access the secure system information.
- Openssl
  - Version 1.0.2s has been upgraded to version 1.1.1d.


### Service framework

#### New and changed features

- Battery-Monitor framework
  - Battery-Monitor framework has been developed to monitor per resource per application battery consumption.
  - CPU, Screen, Bluetooth, Wi-Fi, and Device Network power consumption have been monitored by the Battery-Monitor framework.
  - Support for fetching battery usage of the last day and last one week has been added.
  - Support for different modes of operation for getting the battery usage information has been added. Following are the supported modes:
    - Support for fetching information for an application for a particular resource over a certain duration of time has been added.
    - Support for fetching total battery usage information of an application, combining all the resources over certain duration of time has been added.
    - Support for fetching battery usage values for all the resources separately used by an application id for a certain duration has been added.
    - Support for fetching battery usage values for a particular resource over certain duration of time has been added.
- Account framework
  -  New API set has been added to fetch information of the deleted account.
- Message Service
  - Support for Commercial Mobile Alert System (CMAS) has been added.
    - Support for alerts from 4396 ~ 4399 has been added to the message API set.
      - 4396 : CMAS public safety alerts
      - 4397 : Public safety alerts for additional language
      - 4398 : State/local WEA tests
      - 4399 : State/Local WEA test for a additional languages.
    - Public safety alerts for additional languages have been added to message service.

#### Fixes

- Maps
    - Dependency on deprecated packages has been removed.


### Web framework

#### New and changed features

- Tizen Web Engine
  - Chromium open source version has been changed.
    - Chromium-efl based open source version has been changed from version M63 to version M69. 
    - A distributed web engine feature has been added. This feature allows distributed web content processing on multiple devices using IP network connectivity.
- Web Runtime
  - Web Runtime new feature has been applied.
    - WRT Service application feature has been added. This feature allows you to create a service app using JavaScript.
    - Support WRT Add-on has been added. This feature allows a third party developer to extend the WRT feature or to customize the WRT policy /w extension module, which is written with JavaScript.
- Web UI framework
  - Following TAU UI component has been added:
    - Multi shape graph component
    - contents carousel
    - 3D container
  - WYSIWYG UI build has been added for easy Web application development.


### Lightweight Web Solution

#### New and changed features

- Rendering Engine
  - Canvas elements and their properties have been added.
  - SVG elements and their properties have been extended.
  - CSS animation feature has been added.
  - WebSocket feature has been added.
  - Animated GIF has been supported.
- JS Engine (ES6 Features)
  - Class type has been added.
  - Pattern feature has been added.
  - Proxy feature has been added.
  - Iterator operations have been added.
  - Extended parameter has been added.
  - Generator has been added.
- Support for headless profile has been added.
- Performance and Memory Optimization
  - Rendering Engine
    - Direct mode has been enabled on EvasGL backend.
    - CompositorGL has been fixed to enhance performance.
    - Multithreaded image decoding feature has been added.
    - OpenGL Texture is re-used to reduce loading time.
  - JS Engine
    - Lexer objects have been allocated on stack memory rather than heap memory.
    - The initialization process of an interpreter has been simplified.

#### Fixes

- Bug fixes
  - Layout bugs have been fixed.
  - Memory leaks have been fixed.
  - Crashes have been fixed.


### Tizen .NET

#### New and changed features

- .NET Core (Runtime)
  - .NETCore has been upgraded from 3.0.0-preview2 to 3.0.0.
- Xamarin.Forms
  - Xamarin.Forms 4.2.0, which is latest stable version has been supported.
- Tizen.CircularUI
  - Wearable UI extension (Tizen.Wearable.CircularUI) 1.3.0 has been supported.
- TizenFX (C# Device API) API Level 6
  - New Application API set for component ID has been added.
  - New ComponentBased API set has been added.
  - New AudioManager API set for audio ducking has been added.
  - New PackageManager API set to get dependency information has been added.
  - New MachineLearning Inference API set has been added.
  - New MediaContent API set to add face information into the database manually has been added.
  - Not used filter keywords of MediaContent has been deprecated.
  - New AudioChannel and SampleType of AudioIO have been added.
  - New ImageUtil API set to extract thumbnail has been added.
  - New MediaPlayer API set to export video frames and audio PCM data has been added.
  - New MediaPlayer API set to cancel preparing has been added.
  - New MediaPlayer API set for audio codec and offload has been added.
  - New Multimedia Remote API set for subtitles and 360 mode has been added.
  - New Vision API set for detection and classification using the inference engine has been added.
  - New UI component set of NUI has been added.
  - Tizen.NUI.UIComponents module has been deprecated.
  - New NUI API set for window creation and rotation has been added.
  - New SystemSettings API set to get rotary event enabled has been added.
  - New VoiceControlManager API set has been added.

#### Known Issues

- Xamarin.Forms
  - For more information on the list of limitations, see [here](../../application/dotnet/api/xamarin-forms-limitations.md).


### Toolchain

#### New and changed features

- Toolchain watermarking (annobin) function has been added.
- AddressSanitizer shadow scaling option has been applied to reduce runtime overhead on RAM.
- libasansi library has been introduced to support dotnet ASan runtime.
- gcov-force-options package has been added. This package has scripts to enable automatic package coverage instrumentation.

#### Fixes

- GCC
  - Bugfix on Internal Compiler Error (ICE) has been back-ported from upstream - bug #83623 #85496.
  - LeakSanitizer allocator bug on 64-bit target (aarch64, x86_64) has been fixed.
  - IntegerSanitizer option's bug with "-fsanitize=shift,unsigned-integer-overflow" has been fixed.
  - AddressSanitizer runtime option has been modified (allocator_may_return_null=1) to provide better report.
- GLIBC
  - fclose SIGABORT issue on multi-thread environment with race condition has been fixed by applying bug fix of [#15142](https://sourceware.org/bugzilla/show_bug.cgi?id=15142).
  - New localedata(tl_PH) has been added (bug [#15260](https://sourceware.org/bugzilla/show_bug.cgi?id=15260)).


### Machine Learning

#### New and changed features

- Inference API set
  - Neural network pipeline API set has been added. This API set allows you to construct and execute data stream pipelines with neural networks, tensor operators, input nodes, and multimedia filters.
  - Neural network single API set has been added. This API set allows invoking neural network models with simple API calls.
- NNStreamer
  - [NNStreamer 1.0](https://github.com/nnsuite/nnstreamer) has been added as a set of GStreamer plugins to enable the Inference API set.
  - NNStreamer in Tizen 5.5 M2 supports TensorFlow Lite (1.13) models, custom C/C++ models (.so files), and python codes. Such models may be supplied by applications as resource files.
- nnfw: Neural Network Runtime
  - nn package has been introduced to support the direct loading of TensorFlow Lite models.
  - In order to use nn package independently, a new Runtime API set has been introduced. (Experimental)
  - Custom operator has been supported. For operations that are not provided by runtime as built-in, you can define and implement them and use them through nn package and the Runtime API set.
  - [Performance optimizations] In supporting complex acceleration that inferences one model by using a combination of CPU and GPU, new parallel scheduler provides 30% better performance than single acceleration.
- TensorFlow Lite has been updated from version 1.09 to version 1.13.

#### Known Issues

- Neural network single API set
  - With a given handle, the dimensions of input tensors should be identical. If the dimensions are changed, a handle should be closed and re-opened.
- Inference API set
  - It supports TensorFlow Lite (.tflite) and custom C (.so) models. In Tizen 5.5, TensorFlow (.pb) and nnfw-runtime models are not supported.
