# Tizen 9.0 M1 Release

Release date: May 31, 2024

## Release details

- [Getting source code](http://review.tizen.org/git/) (Tizen 9.0 M1 source codes are under **tizen** branch.)

- Getting binaries and images
  - Base: https://download.tizen.org/releases/milestone/TIZEN/Tizen/Tizen-Base/tizen-base_20240516.070242/
  - Profile(Unified): https://download.tizen.org/releases/milestone/TIZEN/Tizen/Tizen-Unified/tizen-unified_20240523.040324/

- [How to flash to a device](../developing/flashing.md)


## Release notes

### System (kernel and system framework)

#### New and changed features

- Kernel
  - Kernel for Raspberry Pi 4 has been upgraded to version 6.6.17.
  - Raspberry Pi 5 has been supported with the ARM64 Raspberry Pi 4 BOOT image
    - Known issue: Raspberry Pi 5 board should have EEPROM version 2013-12-06.

- System and resource management
  - The ISU of resourced package has been added.

- Device and sensor management
  - The priority-based sound feedback playback has been added and the getter of supported theme ID list.
  - The key mapping between linux kernel input key code and button has been supported when adding new hardware button.
  - The getter of power lock count and callback for change of power lock count have been added.

- OS upgrade
  - The RPK format of ISU package has been added. It is possible to install/uninstall ISU packages via pkgcmd tool.
  - The update-control plugin has been supported in order to separate the vendor/product dependent code.

- kmod
  - Version 30 has been upgaded to version 31.
- f2fs-tools
  - Version 1.14.0 has been upgaded to version 1.16.0.
- libdrm
  - Version 2.4.114 has been upgaded to version 2.4.118.
- device-mapper
  - Version 2.02.98 has been upgraded to version 2.03.22.
- KDBus
  - KDBus has been supported on the upgraded glib 2.78.4.


#### Fixes
- sessiond
 - The dependency with libsessiond has been removed to reduce the memory usage when it is not used.
- storaged
 - Tizen.System.Feedback issue that does not detect 'unmountable event' has been fixed.
- sensord
 - The exception handling code when listener connection is failed has beed added.


### System (base)

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
    - Version 2.70.0 has been upgraded to version 2.78.1.
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

- Tizen Core
  - A new main loop model has been added.
- NUIGadget
  - Support for using external libraries has been added.
- Package Manager
  - Package manager server has been improved by using the Rust language and TIDL.
- Resource Package
  -  Runtime Library Sharing has been added to the Resource Package (RPK).

#### Fixes

- RPC-Port
  - The parcel data capacity has been changed. (8 bytes -> 1024 bytes)
- Service-Application
  - Dependencies have been modified. (Approximately 134kb reduction)


### Window and interaction

#### New and changed features

- Wayland
  - The version of Wayland has been upgraded to 1.22.0.
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
  - The API to check if a keyboard key is present on a given input device has been added.
  - The API to check if a device is physically connected or virtual has been added.
  - Gesture recognition has been improved so that only the surrounding touch coordinates are recognized as gestures using the 'within_distance' configuration.
- libds
  - The implementation of linux-dmabuf-unstable-v1 interface has been added.
  - The implementation of wtz-blur-server interface has been added.
  - The implementation of wtz-blender-server interface has been added.
- Vulkan
  - Vulkan-Utility-Libraries of which version is 1.3.268 has been added.
- TTS Framework
  - The API to generate silent PCM data has been added, which can be used when voice is not required in certain situation.
  - The function to save PCM data for debugging has been supported.
  - The script for operating system upgrade to keep users config has been supported.
- MMI Framework
  - The user-defined workflows and nodes have been supported, which can support specific user scenario. 
  - The CLI scripts to test has been added. This is useful to creating automated test environments during development.
  - The function to feed data from client has been added. 

#### Fixes

- TTS Framework
  - Fix race condition when player thread is terminated. 
- Voice Control Framework
  - Fix the restore logic when the db file is damaged.


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
- Text
  - A Cutout Property in TextLabel has been added.
  - RemoveFrontInset and RemoveBackInset Properties in TextField and TextEditor have been added.
  - An AnchorColor Property in TextLabel has been added.
  - A TextFitArray in TextLabel has been added.
- WindowSystem
  - New GetSourceMimetypes of KVMService in NUI.WindowSystem has been added.
  - A Window constructor using WindowData and FrontBufferRendering have been added.
  - A SetSecondarySelection in NUI.WindowSystem has been added.
- NUI Gadget
  - Support Unload API to release assembly has been added.
  - Support NUI Gadget Resource Manager to get Culture Information.
- Rendering
  - Support for multisampling level of FBO rendering has been added.
  - Support InheritedVisibilityChanged Event for each View.
  - Support for controlling of RenderTask order.
- Scene3D
  - Support to turn on/off Shadow of Directional Light for each Model.
  - Support Geometry based hit test for 3D.
  - Support to control rendering order of each Rendering Item.
- Drag and Drop
  - Support for multiple windows on a single process has been added.
- Performance/Memory Improvement
  - Optimize render thread bottleneck.
  - Optimize Property update logic in render thread.
  - Optimize to control Vector capacity release for memory usage.
  - Support shader pre-compile option.
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
- HandDrawingEngine
  - Support for drawing engine based on vector graphics has been added.

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
- Media Streamer
  - Media Streamer APIs has been removed.

### Network and connectivity

#### New and changed features

- Network
  - New property to provide frequency information in Wi-Fi config APIs has been added.
  - New error type to handle no carrier exception has been added.
  - Supports automatic connection when AP changes from WPA2 to WPA3.
- Bluetooth
  - The API to get the maximum buffer size of L2CAP socket has been added.
- Open source
  - Curl has been upgraded to version 8.5.0.

#### Fixes

- Network
  - The logic to parse device information in multiple device environments has been fixed.
  - D-Bus signal handling code for Wi-Fi has been fixed.
  - The issues in the code for storing and loading wifi configuration have been fixed.
  - The issue where not being able to support SSID other than utf-8 format in netlink scan has been fixed.
  - The issue where unnecessary background scan attempts has been fixed.
- Bluetooth
  - The crash issue in LE scanning has been fixed.
  - The LE scan duty value for low energy has been modified.
    New interval value for low energy is 1400 ms.
    New window value for low energy is 140 ms.
  - Some GATT operation fail issues have been fixed.
  - The PBAP operation fail issue has been fixed.
  - The issue where the previous trigger_bond_info was deleted when requesting bond has been fixed.
  - The issue where event did not occur when CoC connection failed has been fixed.
  - The issue where CoC pending info was not cleared forever has been fixed.
  - The issue where more than 255 GATT attributes could not be supported has been fixed.
  - The issue where server MTU changed callback was not called has been fixed.


### Security

#### New and changed features

- Openssl
  - Openssl has been upgraded to 3.0.13.


### Service framework

#### Fixes

- Push Client
  - Potential defects have been fixed.

### Web framework

#### New and changed features

- WebGPU has been supported.
- Sharescreen API has been supported.
- Picture in Picture(Document, Media Session API) has been supported.
- Third party cookies are not allowed in a page for Security.
- clang has been upgraded to version 18

#### Fixes

- Fix the autofill related crash/freeze issues
- Fix the memory leak issue of SkiaOutPutDeivceOffscreen
- Fix the Fullscreen API crash in webapps
- Replace the deprecated CHROMIUM_image with CHROMIUM_shared_image


### Lightweight web solution

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
  - Tizen.Applications.PackageManager
    - ClearUserData method has been added.
  - Tizen.Applications.RPCPort
    - New constructor has been added to Parcel class.
  - Tizen.Nlp has been deprecated.
  - Tizen.Security.PrivacyPrivilegeManager has been deprecated.
  - Tizen.Security.DevicePolicyManager has been deprecated.
  - Tizen.Multimedia.Camera
    - New setting APIs have been added.
  - Tizen.Data.Tdbc has been added.
  - Tizen.Applications.Common
    - New resource control APIs have been added.
  - Tizen.Multimedia.Remoting
    - WebRTCStatisticsProperty enum have been updated.
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
  - Tizen.Multimedia.Vision
    - InferenceTargetType and InferenceBackendType have been removed.
  - Tizen.Uix.Tts
    - New TTS synthesized PCM APIs have been added.
  - Tizen.Account.FidoClient has been deprecated.
  - Tizen.NUI.Scene3D
    - MotionData class has been added.


### Machine learning

## New and changed features

### Machine Learning (ML) API updates
  - ML.Service API Updates
    - Add new API to provide machine learning service with a configuration file. Application users can easily use the machine learning service by writing necessary options in the configuration file. The API is designed to be simple and flexible, allowing developers to create, manage, and use machine learning service in their applications. A key feature of this API is that it allows users to manage these capabilities using the configuration file, simplifying the process of setting up and managing machine learning service without updating the application. This API can be used not only within on-device but also on the remote (edge) device using the same API.
    - By modifying the configuration file, the application developer can construct various AI services, such as 1) request inference to single model on the device or remote device 2) request inference for more complex tasks such as requiring many models or GStreamer's performant data processing functionalities on the device or remote device 3) model and AI pipeline registration to the remote device.
  - ML.Inference API Updates
    - Add API for cloning tensor data and managing tensor information.

### NNStreamer updates
  - NNStreamer has been upgraded to version 2.4.1.
  - Add mlops-agent daemon to support on-device MLOps and model-agnostic applications.
    - Based on the configuration file, the application can support various ML frameworks, H/W Accelerators, and Input/Output formats without rebuilding the application.
    - ML Application can update the model package, store the data for On-Device training, and manage the model version.

### Open source updates
  - TensorFlow-Lite2 has been upgraded to version 2.15.0.
  - Flatbuffers has been upgraded to version v23.5.26.
  - TensorFlow-Lite1 has been deprecated.

## Fixes
  - Reported bugs in NNStreamer and ML API have been fixed.

## Known issues
  - XNNPACK delegate of TensorFlow-Lite2 is temporarily disabled due to the toolchain version issue.
