# Tizen 9.0 M2 Release

Release date: Oct 31, 2024

## Release details

- [Getting source code](http://review.tizen.org/git/) (Tizen 9.0 M2 source codes are under **tizen_9.0** branch.)

- Getting binaries and images:
  - Base: https://download.tizen.org/releases/milestone/TIZEN/Tizen/Tizen-Base/tizen-base_20240929.112120/
  - Profile(Unified): https://download.tizen.org/releases/milestone/TIZEN/Tizen/Tizen-Unified/tizen-unified_20241025.103727/

- [How to flash an image to device](../developing/flashing.md)


## Release notes

### System kernel and system framework

#### New and changed features

- Kernel
  - Raspberry Pi 5 booting issue with specific EEPROM version has been resolved.
    - Booting is possible from Raspberry Pi 5 EEPROM version 2024-04-20 onwards.

  - The format of ramdisk and ramdisk-recovery images has changed to an initramfs based on cpio.gz.

- System and resource management
  - KDBus has been supported on the upgraded glib 2.80.5.

- Device and sensor management
  - The display dimming brightness adjustment has been supported.
  - The user configuration of display module has been supported (example. /etc/deviced/conf.d/display.conf).
  - API document have been updated for Device/Sensor/Resource management.

- Resource management
  - The robot and component-based app type has been supported.
  - The user configuration of limiter module has been supported (example. /etc/resourced/limiter.conf.d/limiter.conf).

- OS Upgrade
  - HAL ABI Compatibility
    - The ABI compatibility between Platform and HAL has been guaranteed. It supports the Platform-Only OS Upgrade and HAL-Reuse.
    - HAL-rootstrap has been added to support ABI compatibility between platform and HAL. It contains the ABI-guaranteed packages used by HAL-backend.
    - HAL-rootstrap-checker has been added to check whether HAL-backenend has been built using only HAL-rootstrap. It prevents the ABI break of HAL-backend as system-side.
    - Multi-HAL interface architecture of HAL module has been added to support the various hardware by single platform.
    - HAL Compatibility Checker has been added to check whether HAL backend version between the supported HAL interface version. If there are mismatch, fail to load HAL backend.
    - HAL ACR (API Change Request) procedure has been added.

  - Data Migration
    - Online OS Upgrade has been added to perform the quick upgrade through one reboot without a separate data migation mode.
    - The automated test of OS Upgrade and delta image automation generator have been added to verify OS Upgrade between different Tizen version.

- ISU (Individual Service Upgrade)
  - The ISU has supported '/etc/isu/[package name]/isu.cfg.d/' to create ISU package which contains the multiple package files.
  - The ISU version getter has been added.
  - The ISU data migration script has been added.

- device-mapper
  - Version 2.02.98 has been upgraded to version 2.03.22.

#### Fixes
- KDBus
  - KDBus deadlock has been fixed on generated code by gdbus-codgen.
- ISU
  - The duplicate install issue has been fixed.
- resourced
  - The reboot fail issue when VIP process is dead has been fixed.


### Toolchain

#### New and changed features

- Open Source
  - llvm version 10.0.0 has been upgraded to version 17.0.6.
  - linux-glibc-devel version 3.10 has been upgraded to version 5.4.
  - libgc version 8.0.4 has been upgraded to version 8.2.6.


### System (Base)

#### New and changed features

- Open Source
  - abseil-cpp
    - Version 20210324.2 has been upgraded to version 20230802.1.
  - augeas
    - Version 1.12.0 has been upgraded to version 1.14.1.
  - boost
    - Version 1.77.0 has been upgraded to version 1.83.0.
  - brotli
    - Version 1.0.9 has been upgraded to version 1.1.0.
  - byacc
    - Version 20221229 has been upgraded to version 20230521.
  - ccache
    - Version 4.7.4 has been upgraded to version 4.8.3.
  - desktop-file-utils
    - Version 0.26 has been upgraded to version 0.27.
  - diffutils
    - Version 3.8 has been upgraded to version 3.10.
  - dos2unix
    - Version 7.4.3 has been upgraded to version 7.5.1.
  - doxygen
    - Version 1.9.5 has been upgraded to version 1.9.8.
  - expat
    - Version 2.4.1 has been upgraded to version 2.5.0.
  - file
    - Version 5.44 has been upgraded to version 5.45.
  - glib
    - Version 2.70.0 has been upgraded to version 2.80.5.
  - golang
    - Version 1.19.5 has been upgraded to version 1.21.3.
  - gpg2
    - Version 2.4.0 has been upgraded to version 2.4.3.
  - gpgme
    - Version 1.18.0 has been upgraded to version 1.23.1.
  - groff
    - Version 1.22.4 has been upgraded to version 1.23.0.
  - grpc
    - Version 1.42.0 has been upgraded to version 1.60.0.
  - gtest
    - Version 1.12.1 has been upgraded to version 1.14.0.
  - icu
    - Version 70.1 has been upgraded to version 74.1.
  - iso-codes
    - Version 4.12.0 has been upgraded to version 4.15.0.
  - json-c
    - Version 0.15 has been upgraded to version 0.17.
  - json-glib
    - Version 1.6.6 has been upgraded to version 1.8.0.
  - leveldb
    - Version 1.22 has been upgraded to version 1.23.
  - libarchive
    - Version 3.6.2 has been upgraded to version 3.7.2.
  - libksba
    - Version 1.6.3 has been upgraded to version 1.6.5.
  - libpipeline
    - Version 1.5.4 has been upgraded to version 1.5.7.
  - libsolv
    - Version 0.7.20 has been upgraded to version 0.7.27.
  - libwbxml2
    - Version 0.11.7 has been upgraded to version 0.11.8.
  - libxml2
    - Version 2.10.2 has been upgraded to version 2.12.5.
  - libxslt
    - Version 1.1.37 has been upgraded to version 1.1.39.
  - libzio
    - Version 1.06 has been upgraded to version 1.08.
  - libzip
    - Version 1.9.2 has been upgraded to version 1.10.1.
  - libzypp
    - Version 17.23.7 has been upgraded to version 17.31.23.
  - meson
    - Version 1.0.0 has been upgraded to version 1.3.0.
  - mm-common
    - Version 1.0.3 has been upgraded to version 1.0.5.
  - mtools
    - Version 4.0.42 has been upgraded to version 4.0.43.
  - multipath-tools
    - Version 0.9.4 has been upgraded to version 0.9.7.
  - openfst
    - Version 1.8.1 has been upgraded to version 1.8.2.
  - paho-mqtt-c
    - Version 1.3.9 has been upgraded to version 1.3.13.
  - parted
    - Version 3.5 has been upgraded to version 3.6.
  - perl
    - Version 5.34.0 has been upgraded to version 5.38.0.
  - procps-ng
    - Version 3.3.17 has been upgraded to version 4.0.4.
  - psmisc
    - Version 23.4 has been upgraded to version 23.6.
  - pygobject2
    - Version 2.28.6 has been upgraded to version 3.46.0.
  - python3
    - Version 3.11.2 has been upgraded to version 3.12.0.
  - re2
    - Version 20220201 has been upgraded to version 20231101.
  - re2c
    - Version 3.0 has been upgraded to version 3.1.
  - rsync
    - Version 3.2.3 has been upgraded to version 3.2.7.
  - sgml-skel
    - Version 0.7.1 has been upgraded to version 0.7.2.
  - sqlite
    - Version 3.40.1 has been upgraded to version 3.44.0.
  - swig
    - Version 4.0.2 has been upgraded to version 4.1.1.
  - texinfo
    - Version 7 has been upgraded to version 7.1.
  - tinyxml2
    - Version 4.0.1 has been upgraded to version 9.0.0.
  - update-alternatives
    - Version 1.21.18 has been upgraded to version 1.22.2.
  - util-linux
    - Version 2.37.4 has been upgraded to version 2.39.
  - xz
    - Version 5.4.0 has been upgraded to version 5.4.5.
  - yaml-cpp
    - Version 0.6.3 has been upgraded to version 0.8.0.
  - zlib
    - Version 1.2.13 has been upgraded to version 1.3.
  - zstd
    - Version 1.5.2 has been upgraded to version 1.5.5.



### Application framework

#### New and changed features

- App-event
  - The app-event has been changed to use TIDL instead of DBUS.
- Launchpad
  - The launchpad has been refactored. A sub module (lux) written in rust language has been added.
- TIDL
  - The TIDL compiler has been updated to generate code that uses the Rust programming language.
- Tizen Core
  - The C# API has been added.

#### Fixes

- RPC-Port
  - The receiving timeout has been changed. (10 seconds -> 25 seconds)
  - It has been changed to a structure that can receive events through the event loop of the connected(or listened) thread.


### Window and interaction

#### New and changed features

- Wayland
  - The version of Wayland has been upgraded to 1.22.0.
  - The grab_relative_motion and ungrab_relative_motion requests have been added to tizen_input_device_manager interface.
- vulkan-wsi-layer
  - Version 2022.11.24 has been upgraded to version 2023.12.01.
- Vulkan-ValidationLayer
  - Version 1.3.240 has been upgraded to version 1.3.268.
- Vulkan-Loader
  - Version 1.3.240 has been upgraded to version 1.3.268.
- Vulkan-Headers
  - Version 1.3.240 has been upgraded to version 1.3.268.
- Vulkan-Tools
  - Version 1.3.240 has been upgraded to version 1.3.268.
- SPIRV-Tools
  - Version 2023.1.1 has been upgraded to version 2023.5.1.
- glslang
  - Version 2023.1.1 has been upgraded to version 13.1.1.
- Libinput
  - The version of Libinput has been upgraded to 1.24.0.
- Libevdev
  - The version of Libevdev has been upgraded to 1.13.0.
- Libxkbcommon
  - The version of Libxkbcommon has been upgraded to 1.6.0.
- Enlightenment
  - The input thread is now responsible for processing mouse/touch event to remove potential delays in their delivery (thus preventing cursor freezing and enabling support for high frequency input devices, etc.).
  - The delivery of multi-touch events is improved by optimizing the event flushing process.
  - Unit and Integration testcases are added and improved.
  - The APIs to access the internal data of the Enlightenment core have been added.
  - The Video Shell feature has been added for synchronization between UI and Video.
  - Support multiple mime types for the Clipboard History Manager.
  - Support blur functionality.
  - The E_View for encapsulation of Evas has been added.
- Tizen WS Shell
  - The API to request to perform drop to given target in the tws_service_kvm has been added
- libds
  - The implementation of linux-dmabuf-unstable-v1 interface has been added.
  - The implementation of wtz-blur-server interface has been added.
  - The implementation of wtz-blender-server interface has been added.
  - The implementation of wtz-blur-rectangle interface has been added.
  - The implementation of wtz-blur-behind interface has been added.
- Vulkan
  - Vulkan-Utility-Libraries of which version is 1.3.268 has been added.
- TTS Framework
  - The APIs for creating synthesis parameter handles that allow configuring TTS settings like pitch, speed, volume, and background volume per client have been added.
  - The APIs for retrieving personal TTS models and selecting among them have been added. 
- MMI Framework
  - The APIs for creating nodes and workflows have been added.
  - The APIs for utilizing workflows and receiving results have been added.
- Text Input
  - The API to set align of IME has been added.
  - The API to move and resize the floating IME has been added.
  - The InputMethod APIs related to ElmSharp is removed.
  - The InputMethod's RotationChanged event is deprecated.


#### Fixes

- TTS Framework
  - Fix a potential issue with a dangling pointer.
  - Fix a race condition during destruction of an RPC handle.
- Voice Control Framework
  - Fix a threading safety concern by employing mutex locks.
  - Fix the background volume ducking problem where it would not deactivate once the state was fully transitioned to "ducked".


### Graphics and UI

#### New and changed features

- Image and Animation
  - An ID of Animation and more API for RenderTask have been added.
  - A SetTransitionEffectOption for ImageView's transition effect has been added.
  - A NotifyAfterRasterization in LottieAnimationView has been added.
  - A EnableFrameCache in LottieAnimationView has been added.
  - Support NativeImageQueue creation with queue count.
  - Support LottieAnimationView file load asynchronously.
  - Support to get Marker list information in LottieAnimationView.
  - Resize webp buffer by using decoder in loading time.
  - Support auto resizing of image buffer according to the View's Size.
  - Support caching for SVG resources.
- Inputs and Utilities
  - A VelocityTracker for touch event has been added.
  - A SetTime in Touch has been added.
  - A SetTapMaximumMotionAllowedDistance in Gesture has been added.
  - A State property of NUIApplication has been added.
  - A backendMode to the DirectRenderingGLView has been added.
  - DispatchWheelEvents and DispatchPrentWheelEvents in View have been added.
  - An AliveCount property to get currently alived View number has been added.
  - Support ProcessController without Initialize.
  - Support DisposeRecursively() full search in Container.
  - A GetLastPanGestureState in Gesture has been added.
  - Optimize the frequency of event occurrence during multi-touch.
- Text
  - A Cutout Property in TextLabel has been added.
  - RemoveFrontInset and RemoveBackInset Properties in TextField and TextEditor have been added.
  - An AnchorColor Property in TextLabel has been added.
  - A TextFitArray in TextLabel has been added.
  - Support for async text rendering.
  - A SetInputPanelPositionAlign in InputMethonContext has been added.
  - A Offset property in text outline has been added.
  - A Blur Radious property in text outline has been added.
- Window System
  - New GetSourceMimetypes of KVMService in NUI.WindowSystem has been added.
  - A Window constructor using WindowData and FrontBufferRendering have been added.
  - A SetSecondarySelection in NUI.WindowSystem has been added.
  - A RelativeMotionGrab and RelativeMotionUnGrab in Window have been added.
  - Support for window background/behind blur.
- NUI Gadget
  - Support Unload API to release assembly has been added.
  - Support NUI Gadget Resource Manager to get Culture Information.
- Rendering
  - Support for multisampling level of FBO rendering has been added.
  - Support InheritedVisibilityChanged Event for each View.
  - Support for controlling of RenderTask order.
  - Support customization of View's rendering items using VisualObject.
  - Support Blur effect for View background.
- Scene3D
  - Support to turn on/off Shadow of Directional Light for each Model.
  - Support Geometry based hit test for 3D.
  - Support to control rendering order of each Rendering Item.
  - Support 2D Panel to draw 2D UI Content inside 3D Scene.
  - Support Capture for SceneView.
- Drag and Drop
  - Support for multiple windows on a single process has been added.
- Performance/Memory Improvement
  - Optimize render thread bottleneck.
  - Optimize Property update logic in render thread.
  - Optimize to control Vector capacity release for memory usage.
  - Support custom shader pre-compile option.
  - Support to synchronize rendering fps with lottie's fps.
- Aurum
  - Improve the performance of finding element and dump objects by adding new methods.
  - Support for sorting child objects by coordinates.
  - Support for creating xpath when processes name are same.
  - Support for updating function of application information.
  - Support for updating function of XPath information.
  - Support for changing the port number(50051-50060)
  - Support for separating event registration.
  - Improve the performance by refactoring processing event.
  - Support for navigation functions.
  - Support for getting the parent.
  - Support for aurum-python to improve user convienent.
- UI Analyzer (internal Tool)
  - Support new workspace for saving screenshot
  - Support for changing slider feature
  - Support for description information
  - Support for the count of objects in object tree.
  - Support for vertical scrollbar in screen shot
  - Support for aurum-python
  - Support for the distiction between several root layers
  - Improve the performance when window is resized.
  - Support for player cancel function.
  - Support for upgrade the vulnerable.
  - Support for waiting the grpc server ready.
  - Support for role, highlightable attributes.
  - Support for change the sdb port.
- HandDrawingEngine
  - Support for drawing engine based on vector graphics has been added.
- Vector Graphics
  - Improve the offscreen rendering performance of multiple shapes in lottie-player.
  - A trim path dynamic property in lottie-player has been added.
- Clipboard
  - Support for multi-type copy and paste.
  - A HasType in Clipboard has been added.

#### Fixes

  - Fix bug when find element with showing condition.
  - Fix Memory leaks
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
  - Fix svg image loading defects.
  - Fix Various Text defects.
  - Fix Aurum crash issue.
  - Fix the text space issue for UI-Analyzer


### Multimedia framework

#### New and changed features

- Open source
  - ffmpeg version 5.1.2 has been upgraded to version 6.1.
  - tiff version 4.4.0 has been upgraded to version 4.6.0.
  - GraphicsMagick version 1.3.38 has been upgraded to version 1.3.42.
  - libwebp version 1.2.4 has been upgraded to version 1.3.2.
  - libjpeg-turbo version 2.1.4 has been upgraded to version 3.0.1.
  - libpng version 1.6.38 has been upgraded to version 1.6.40.
  - taglib version 1.13 has been upgraded to version 1.13.1.
  - lcms2 version 2.12 has been upgraded to version 2.16.
- Media Camera
  - New error value has been added for preview callback APIs.
- Media Player
  - New APIs for video codec type settings have been added.
- Media Content
  - Pinyin related defines have been removed.
  - Some APIs with low usability have been deprecated.
  - Bookmark, playlist, tag APIs have been deprecated.
- Metadata Editor
  - All APIs have been deprecated.
- Image Util
   - Remove deprecated APIs from Tizen 5.0 and 5.5.
- MediaController
  - Remove deprecated APIs from Tizen 5.0 and 5.5.
- MediaVision
  - Deprecated legacy face, image, surveillance APIs.
  - Deprecated inference APIs.
  - New machine learning task APIs have been added.
- Single Oriented AI Service framework (Internal)
  - Support AutoZoom Service API
  - Provide adaptation interfaces to support various backends such as various inputs and machine learning frameworks
    - Support MediaVision framework as a machine learning based vision backend
    - Support Camera API, OpenCV and vision source as Camera input backends
- Media Streamer
  - Media Streamer APIs has been removed.
- Native WebRTC
  - Renegotiation has been supported.
  - Domain name as connection address of ICE candidate has been supported.
  - Consent-freshness of RFC7675 has been supported.
  - New enum for 'max-compat' bundle policy has been added.
  - New API for specifying payload type has been added.
  - New APIs for getting local/remote description have been added.
- Audio Frameworks
  - Acoustic Echo Cancellation has been added via audio-io.
  - Automatic Gain Control has been integrated through audio-io.
  - Neural network-based Noise Suppression has been implemented, supporting audio-io APIs.
- Resource Manager
  - Light weight resource manager have been applied.

### Network and connectivity

#### New and changed features

- Network
  - New APIs for monitoring and retrieving the state of default gateway and DNS have been added.
  - New API for initiating a one-time online HTTP check has been added.
- Wi-Fi Aware
  - New set of APIs to manage Wi-Fi Aware functionalities has been added.
    - Allows applications to create, configure, and manage Wi-Fi Aware sessions.
    - Supports various session types such as Publish and Subscribe.
    - Provides mechanisms for sending and receiving messages between peers.
  - Includes features for enabling and disabling Wi-Fi Aware, handling session termination, and discovering nearby services.
  - Enhanced capabilities for establishing secure data paths and managing peer connections.
- Bluetooth
  - New disconnection error type to handle MIC failure has been added.

#### Fixes

- Network
  - Path traversal issue has been fixed.
  - The issue with unintended auto-connect attempts has been fixed.
  - The logic to monitor ethernet cable connection state has been fixed.
- Bluetooth
  - The issue where wrong MTU changed cb was unset has been fixed.
  - The issue of not receiving dbus signal has been fixed.
  - The issue where WriteValue/AcquireNotify method comes before gatt connected has been fixed.


### Security

#### New and changed features

- PQC Algorithm Support
  - The ligoqs has been added for PQC algorithms.
  - The key manager supports ML-KEM.
- Passkey Support
  - New native and C# WebAuthn APIs are provided.
  - Hybrid transport is supported.


### Service framework

#### Fixes

- Location
  - Potential defects have been fixed.
- Email
  - Potential defects have been fixed.

### Web framework

#### New and changed features

- WebAuthn has been supported based on Tizen Native WebAuthn.
- CSS nesting has been supported.
- LLVM Toolchain has been upgraded to version 18.

#### Fixes

- Fix the autofill related crash/freeze issues
- Fix the memory leak issue of SkiaOutPutDeivceOffscreen
- Fix the Fullscreen API crash in webapps
- Replace the deprecated CHROMIUM_image with CHROMIUM_shared_image
- Fix the RWI websocket disconnect issue
- Fix to support WebM container


### Lightweight Web Solution

#### New and changed features

- Lightweight Web Engine
- Web Engine
- Service Worker lifecycle has been supported.
- Caching responses on network requests in the Service Worker has been supported.
- Maplike declaration has been added.
- JavaScript Engine
- ECMAscript feature (from ES2022) has been added.

#### Fixes

- Lightweight Web Engine
- Network loader defects have been fixed.
- Memory leak defects have been fixed.
- URL parsing defects have been fixed.
- History management defects have been fixed.


### Tizen .NET

#### New and changed features

- TizenFx
  - Tizen.Content.MediaContent
    - Deprecated properties have been removed from MediaInfoColumns class.
    - Deprecated classes (StorageType/Storage/StorageCommand) have been removed.
    - All Bookmark and Playlist APIs have been removed.
  - Tizen.Applications.PackageManager
    - ClearUserData method has been added.
  - Tizen.Applications.RPCPort
    - New constructor has been added to Parcel class.
  - Tizen.Applications.Shortcut has been deprecated.
  - Tizen.Applications.Badge has been deprecated.
  - Tizen.Nlp has been deprecated.
  - Tizen.Security.PrivacyPrivilegeManager has been deprecated.
  - Tizen.Security.DevicePolicyManager has been deprecated.
  - Tizen.Security.Webauthn has beed added.
  - Tizen.Multimedia.Camera
    - New setting APIs have been added.
  - Tizen.Multimedia.Vision
    - New inference APIs have been added.
    - All legacy APIs have been deprecated.
  - Tizen.Multimedia.Metadata
    - StitchedContent360 method has been added.
  - Tizen.Multimedia.AudioManager
    - SoundEffect method has been added.
  - Tizen.Data.Tdbc has been added.
  - Tizen.Applications.Common
    - New resource control APIs have been added.
  - Tizen.Multimedia.Remoting
    - WebRTCStatisticsProperty enum have been updated.
    - Deprecated APIs of MediaController server has been removed.
  - Tizen.Multimedia.Vision
    - New QR APIs have been added.
  - Tizen.Content.Download
    - New caching APIs have been added.
  - Tizen.Location.Geofence has been deprecated.
  - Tizen.Messaging.Email has been deprecated.
  - Tizen.Messaging.Messages has been deprecated.
  - Tizen.Applications.ComponentBased
    - TimeZoneChanged event handler has been added.
  - Tizen.Applications.Common
    - TimeZoneEvent has been added.
  - Tizen.Applications.AttachPanel has been deprecated.
  - Tizen.Multimedia.Vision
    - InferenceTargetType and InferenceBackendType have been removed.
  - Tizen.Multimedia.Util
    - Deprecated APIs has been removed.
  - Tizen.Multimedia.StreamRecorder has been removed.
  - Tizen.Uix.Tts
    - New TTS synthesized PCM APIs have been added.
  - Tizen.Uix.InputMethod
    - RotationChanged event has been deprecated.
    - Some APIs depending on ElmSharp has been removed.
  - Tizen.Account.FidoClient has been deprecated.
  - Tizen.NUI.Scene3D
    - MotionData class has been added.
  - Tizen.NUI
    - Scrollable and ScrollViewEffect has been deprecated.
    - WeakEvent has been added.
  - Tizen.Core has been added.
    - New main loop model to provide improved functionality has been added.
  - Tizen.Network.Connection
    - WPA3 security type has been added.
  - TizenWebView has been removed.
  - Tizen.NUI.Wearable has been deprecated.


### Machine learning

## New and changed features

### Machine Learning (ML) API updates
  -  ML.Service API Updates
    - ML Service API supports application developers to use AI offloading service using various protocols such as TCP, MQTT, and other custom connection via NNStreamer-Edge.
  - Add NNFW enum type to support TensorRT and QNN.

### NNStreamer and Related modules update
  - NNStreamer has been upgraded to version 2.4.2.
    - Add new inference filter to support the ONNX Runtime.
    - Add new inference filter to support the SNPE version 2 (Qualcomm Neural Processing SDK).
    - Add new inference filter to support the QNN (Qualcomm AI Engine Direct).
    - Add new inference filter to support the TensorRT version 10.
    - Add new inference filter to support the ncnn engine (Tencent).
    - Add new inference filter to support the ExecuTorch (Experimental).

  - NNStreamer-Edge has been upgraded to version 0.2.6.
    - Support custom connection (user defined protocol).
    - Support Multi-Connectivity Framework (MCF) using custom connection.

  - MLOps-Agent has been upgraded to version 1.8.6.
    - Parse the path for AI model or recource files from installed RPK.

  - Support ML computation offloading to an Android device (Experimental).

## Fixes
  - Reported bugs in NNStreamer and ML API have been fixed.

## Known issues
  - XNNPACK delegate of TensorFlow-Lite2 is temporarily disabled due to the Toolchain version issue.
