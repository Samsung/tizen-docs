# Tizen 8.0 Public M1

Release date: May 31, 2023

## Release details

- [Getting source code](http://review.tizen.org/git/) (Tizen 8.0M1 source codes are under **tizen** branch.)

- Getting binaries and images
  - Base: [http://download.tizen.org/releases/milestone/TIZEN/Tizen/Tizen-Base/tizen-base_20230515.082838/](http://download.tizen.org/releases/milestone/TIZEN/Tizen/Tizen-Base/tizen-base_20230515.082838/)
  - Profile(Unified): [http://download.tizen.org/releases/milestone/TIZEN/Tizen/Tizen-Unified/tizen-unified_20230524.002652/](http://download.tizen.org/releases/milestone/TIZEN/Tizen/Tizen-Unified/tizen-unified_20230524.002652/)

- [How to flash to a device](../developing/flashing.md)


## Release notes

### System (kernel and system framework)

#### New and changed features

- System and resource management
  - Multi-user user-add function has been improved by fixing smack/permission exception case.
  - Multi-user user-get-list latency issue has been fixed by getting the list from directory.
  - Ready-state callback of multi-user service has been supported to reduce booting-time.
  - Process OOM_FIXED_APPS feature has been restored.
  - Process CPU affinity feature has been restored.
- Device and sensor management
  - Input event on/off function for input device has been supported.
  - Display white balance function has been supported.
  - Display rotation function has been supported.
  - Power suspending and resuming callback function have been supported.
  - Power suspending cancellation function has been supported.
  - Power lock status callback has been supported.
  - Power wakeup reason function has been supported.
  - UART flush and drain functions have been supported.
  - Sensor listener attribute getter function has been supported.
  - Sensor attribute setter/getter functions have been supported.
  - Sensitivity attribute of Proximity sensor has been supported.
  - Sensord signal handling has been improved by removing race conditions.
- OS upgrade
  - Delta binary verifier of FOTA has been added to verify the valid of delta binary.
- libdrm 
  - Version 2.4.109 has been upgraded to version 2.4.114.
  - libkms.so has been removed.
- libusb 
  - Version 1.0.21 has been upgraded to version 1.0.25.
- cryptsetup 
  - Version 2.3.3 has been upgraded to version 2.3.7.

#### Fixes

- systemd
  - CVE-2020-1712 patch has been applied.
- dbus
  - CVE-2022-42012 patch has been applied.
  - CVE-2022-42011 patch has been applied.
  - CVE-2022-42010 patch has been applied.


### System (base)

#### New and changed features

- Open source
  - autoconf-archive
    - Version 2022.02.11 has been upgraded to version 2022.09.03.
  - automake
    - Version 1.16.4 has been upgraded to version 1.16.5.
  - ccache
    - Version 4.4 has been upgraded to version 4.7.4.
  - cmake
    - Version 3.21.3 has been upgraded to version 3.25.2.
  - cmocka
    - Version 1.1.1 has been upgraded to version 1.1.5.
  - diffutils
    - Version 3.3 has been upgraded to version 3.8.
  - dos2unix
    - Version 7.4.2 has been upgraded to version 7.4.3.
  - dosfstools
    - Version 3.0.16 has been upgraded to version 4.2.
  - doxygen
    - Version 1.9.2 has been upgraded to version 1.9.5.
  - ed
    - Version 1.17 has been upgraded to version 1.19.
  - fdupes
    - Version 2.1.2 has been upgraded to version 2.2.1.
  - file
    - Version 5.41 has been upgraded to version 5.44.
  - gettext
    - Version 0.19.8.1 has been upgraded to version 0.21.1.
  - golang
    - Version 1.17.4 has been upgraded to version 1.19.5.
  - groff
    - Version 1.22.2 has been upgraded to version 1.22.4.
  - gpg2
    - Version 2.3.7 has been upgraded to version 2.4.0.
  - gpgme
    - Version 1.3.2 has been upgraded to version 1.18.0.
  - help2man
    - Version 1.48.5 has been upgraded to version 1.49.3.
  - icu
    - Version 70.1 has been upgraded to version 70.1.
  - less
    - Version 466 has been upgraded to version 608.
  - libksba
    - Version 1.6.0 has been upgraded to version 1.6.3.
  - libtool
    - Version 2.4.6 has been upgraded to version 2.4.7.
  - libunistring
    - Version 0.9.10 has been upgraded to version 1.1.
  - meson
    - Version 0.60.3 has been upgraded to version 1.0.0.
  - mtools
    - Version 4.0.36 has been upgraded to version 4.0.42.
  - multipath-tools
    - Version 0.8.8 has been upgraded to version 0.9.4.
  - ninja
    - Version 1.10.2 has been upgraded to version 1.11.1.
  - parted
    - Version 3.4 has been upgraded to version 3.5.
  - python3-sqlite
    - Version 0.4.7 has been upgraded to version 0.5.0.
  - sqlite
    - Version 3.39.0 has been upgraded to version 3.40.1.
  - sudo
    - Version 1.9.4 has been upgraded to version 1.9.12p1.
  - tcl
    - Version 8.6.10 has been upgraded to version 8.6.13.
  - texinfo
    - Version 6 has been upgraded to version 7.
  - tzdata
    - Version 2021e has been upgraded to version 2022g.
  - update-alternatives
    - Version 1.20.5 has been upgraded to version 1.21.18.
  - uthash
    - Version 1.9.7 has been upgraded to version 2.3.0.
  - vim
    - Version 8.2.2173 has been upgraded to version 8.2.5172.
  - xmlto
    - Version 0.0.25 has been upgraded to version 0.0.28.
  - xz
    - Version 5.2.5 has been upgraded to version 5.4.0.
  - yasm
    - Version 1.2.0 has been upgraded to version 1.3.0.
  - zlib
    - Version 1.2.11 has been upgraded to version 1.2.13.
  - zstd
    - Version 1.4.5 has been upgraded to version 1.5.2.


### Application framework

#### New and changed features

- Application Manager
  -  C# API that terminates without restarting application has been added.
- Package Manager
  - New feature has been ready to remove user data from other applications.
- App-control 
  - Launch-bounds APIs have been provided.
  - Extended appid for multi-instance has been introduced.
- TIDL
  - The TIDL compiler has been updated to generate code that use Cion API for Dart language
- Tizen Database Connectivity (TDBC)
  - New feature has been ready to access  a database.
    - Provides an C# API which defines how a client may access a database.
    - The default SQLite driver is provided by platform. 
- Launchpad
  - New  feature has been ready to execute applications or loaders.
- NUIGadget
  -  New feature has been added that is a component model distributed in DLL library form.
  -  Packaged and distributed as resource package. 

#### Fixes

- AMD
  - Potential defects have been fixed.
- App Installer
  - Potential defects have been fixed.


### Window and interaction

#### New and changed features

- Wayland
  - The version of Wayland has been upgraded to 1.21.0.
  - The wtz-screen protocol has been added.
    - wtz-screen interface provides the logical screen information and functionalities.
  - The wtz-shell protocol has been added.
    - wtz-shell and wtz-surface provide Tizen-style surface requests and events.
  - The set_auto_placement request has been added to tizen_launch_appinfo interface.
  - The set_pin_mode and unset_pin_mode requests have been added to tizen_policy interface.
  - The init_generator_with_sync request has been added to tizen_input_device_manager interface.
- Enlightenment
  - The name of e_desk_group has been changed to e_desk_area.
  - The server protocol implementation of wtz_screen and wtz_splitscreen interfaces has been included.
  - The server protocol implementation of wtz_shell interface has been included.
  - The policies for Multi-Windows management have been added.
    - Those are Smart Launch, Snap Window, All Minimize and Smart Rotation.
  - The wheel event in touchpad has been supported.
- TBM
  - Parallelization function to improve the authentication speed from TBM has been added.
- TPL-EGL
  - The API to set the front buffer rendering for each surface has been provided.
  - The API to check if a surface has a fence sync has been provided.
- Mesa
  - The version of Mesa has been upgraded to 22.3.5.
- Vulkan
  - The version of SPIRV-Cross, SPIRV-Headers and SPIRV-Tools has been upgraded to 1.3.239.
  - The version of Vulkan-Headers, Vulkan-Hpp, Vukan-Loader and Vulkan-ValidationLayers has been upgraded to 1.3.240.
  - The version of glslang has been upgraded to 1.3.239.
- Libinput
  - The version of Libinput has been upgraded to 1.22.0.
- Libxkbcommon
  - The version of Libxkbcommon has been upgraded to 1.5.1.
- TTS Framework
  - Supports root daemon as TTS client.
  - Supports on-demand reconnection of clients when TTS service abnormally terminated. This is useful for low-end devices when its cpu consumption is very high.
- STT Framework
  - Support USB plug-in microphone for TV binary.
- Voice Control Framework
  - The IPC interface between the voice control engine and voice control clients has been changed from D-Bus to TIDL, which is a proper IPC method between applications.
  - The C API to reduce background volume when the voice manager client wants has been added.
- Text Input
  - The performance to get surrounding text has been improved.
- NLP
  - NLP APIs have been deprecated.

#### Fixes

- TTS Framework
  - Fix threads safety issue, which TIDL IPC connection is established and closed.
- Voice Control Framework
  -  Remove the unnecessary circular dependencies on the client side.


### Graphics and UI

#### New and changed features

- Rendering
  - Support for multisampling level of FBO rendering has been added.
- Scene3D
  - A new default camera for 3D scene has been added.
  - Support for asynchronous loading of Model and SceneView has been added.
  - Support for KHR_materials_specular and KHR_materials_ior extension of glTF has been added.
  - Support for embedded texture data of glTF has been added.
  - Cache manager for 3D models has been added.
  - Support for glb format has been added.
  - Support for equirectangular projection has been added.
  - Support for NavigationMesh and PathFinding has been added.
- View and Window
  - Some properties have been added to the Camera.
  - An overlay layer has added to the Scene.
  - A new window type DESKTOP has been added.
  - Support for window layout has been added.
  - A BorderWindow has been added to the window.
- Images
  - Support for CMYK jpeg image loading has been added.
-  Text
  - Some text geometry APIs have been added.
  - Some text span APIs have been added.
-  Drag and Drop
  - Support for multiple windows on a single process has been added.
-  Performance / Memory Improvement
  - The object sizes of some internal classes have been reduced.
  - Message processing logic has been optimized.
  - Some matrix operations have been optimized.
  - Unnecessary ClipBoard creation has been removed.
- Aurum
  - Support for UI context changed event has been added.
  - Support for UI scrolling finished event has been added. 
- Vector Animation
  - Tizenvg has been updated to the latest thorvg.

#### Fixes

- Various partial update defects have been fixed.
- A transform matrix calculation defect has been fixed.
- A screen rotation defect has been fixed.
- Various BMP decoder defects have been fixed.
- Various text defects have been fixed.
- Various Aurum defects have been fixed.
- Various touch and gesture defects have been fixed.


### Multimedia framework

#### New and changed features

- Open source
  - OpenCV version 4.5.3 has been upgraded to version 4.7.0.
  - GStreamer version 1.20.0 has been upgraded to version 1.22.0.
  - Ffmpeg version 4.4.1 has been upgraded to version 5.1.2.
  - Taglib version 1.12 has been upgraded to version 1.13.
  - Tiff version 4.3.0 has been upgraded to version 4.4.0.
  - GraphicsMagicK version 1.3.36 has been upgraded to version 1.3.38.
  - libwebp version 1.2.1 has been upgraded to version 1.2.4.
  - libjpeg-turbo version 2.1.1 has been upgraded to version 2.1.4.
  - libpng version 1.6.37 has been upgraded to version 1.6.38.
  - libjxl version 0.6.1 has been upgraded to version 0.7.0.
  - libvpx version 1.10.0 has been upgraded to version 1.12.0.
- MediaVision
  - Support for DesignQR has been added.
- Media Camera
  - New APIs for camera settings have been added.
- Native WebRTC
  - New stats types have been added to get information for candidate pair, local candidate, and remote candidate.
  - New error type of network resource failure has been added.
  - Some macro definitions of stats have been deprecated.
- Media Content
  - Deprecated some storage related APIs and unused media metadata have been removed.
  - Deprecated thumbnail util APIs have been removed.


### Network and connectivity

#### New and changed features

- Network
  - Support PSK_SHA256 for ieee80211w has been added.
  - Timers to handle timeout for asynchronous APIs in wifi-manager have been added.
- Download cache support
  - Capi-web-url-download and download-provider have been extended to support cache service.
    - Stores a copy of a given resource and serves it back when requested.
    - The freshness lifetime is calculated based on several headers.
    - Uses If-None-Match request to check if the resource is in fact still fresh.
  - New APIs for handling cache option have been added.
  - New API for removing the files cached by each application has been added.
- Bluetooth
  - New APIs for GATT client connecting and disconnecting have been added.
  - New APIs for GATT server connection state changed callback have been added.
  - New API for setting advertising flags has been added.
  - New APIs for setting advertising custom name have been added.
- Open source
  - Curl version has been upgraded to 7.86.0.
  - Wpa_supplicant version has been upgraded to 2.10.

#### Fixes

- Network
  - The logic to store profile extension information has been fixed.
  - The logic for Netlink scan has been fixed.
  - The logic to calculate scores for AP connections has been fixed.
  - The logic for background scan has been fixed.
  - The logic to monitor the status of the Wi-Fi module has been fixed.
- Bluetooth
  - The RSSI parsing issue from discovery has been fixed.
  - Discovery busy state handling logic has been fixed.
  - Adapter state check logic has been fixed.
  - EIR manufacturer data handling logic has been fixed.
  - Bonded devices response not coming issue has been fixed.
  - Infinite callback issue in EOF case has been fixed.


### Security

#### New and changed features

- Privacy privilege manager
  - Privacy privilege manager (PPM) feature has been deprecated.


### Service framework

#### Fixes

- Account Framework
  - Potential defects have been fixed.
- Sync-Manager
  - Potential defects have been fixed.


### Web framework

#### New and changed features

- Web Engine
  - Open source chromium 108 version base has been applied.
  - OzonePlatform for EFL has been added.
  - Ozone EFL based Onscreen/Offscreen rendering mode has been supported.
  - Offscreen rendering mode based NUI feature has been supported.
  - ESPP based media renderer has been added.
- Web Runtime
  - Open source electron 22.0.0 version has been applied.

#### Fixes

- Stability issue in multi windows scenario has been fixed.
- Media permission issue on WRT has been fixed.


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
- Url parsing defects have been fixed.
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


### Toolchain

#### New and changed features

- GCC
  - ARM target changes have been back-ported from releases/gcc-9.
  - Libsanitizer: AddressSanitizer overhead reduction option has been added.
- Glibc
  - Timezone: updated from tzcode 2020a.
- Binutils
  - Packaging: keep shared libraries for libbfd & libopcodes.

#### Fixes

- GCC
  - Bugfix PR c++/61414 patchset has been applied.
  - Bugfix PR middle-end/98189, 95886 patchset has been applied.
- Glibc
  - Static TLS (Thread Local Storage) block memory allocation bugfix patchset has been applied.
  - CVE bugs are fixed
    - CVE-2022-23219
    - CVE-2022-23218
    - CVE-2021-38604
    - CVE-2021-35942
    - CVE-2021-3326
    - CVE-2021-27645
    - CVE-2020-27618
    - CVE-2021-3999
  - AddressSanitizer build error for aarch64 architecture has been fixed.


### Machine learning

#### New and changed features

- Machine Learning (ML) API updates
  - ML.Service API Updates
    - Add new APIs to separately manage ML model files. These APIs allow ML applications to exploit the latest ML model deployed without code-level modifications that require re-packaging and re-distribution of the whole application.
    - AI Inference offloading between Tizen and TizenRT has been improved. The binary size of TizenRT is optimized (< 100kB). 
  - ML.Inference API Updates
    - Add new API to use extended rank limit. To maintain the backward compatibility, the default rank limit is 4. The extended rank is only used when new API is called.
    - Support TensorFlow Lite v2.11.0 by default.
  - ML.Training API Updates
    - Add Identify Layer as a utility layer which flows everthing as it is.
     - Add learning rate scheduling features.
- Step learning rate scheduling
- Exponent learning rate scheduling
    - Add API to get the weight data
- NNStreamer updates
  - NNStreamer has been upgraded to version 2.3.0.
  - Support for large-size model of the NNStreamer pipeline has been added.
    - The number of rank limit has been increased up to 8.
    - The number of tensor limit has been increased up to 100.
  - Support for the model storage of Device MLOps has been added.
    - Model management feature such as register, fetch active model, update, and delete has been added. Using this feature, ML applications can share their model with other applications.
  - Pipeline based data repository and training feature has been added.
    - New NNStreamer elements such as datareposrc, datareposink, and tensor_trainer have been added.
    - Support for the training in AI pipeline has been added.
- NNTrainer updates
  - Support proactive swap which utilizes secondary storage for less memory consumption.
    - Add Cache Pool/Cache Loader/Cache Element classes.
    - Update Memory pool and planner for better utilization.
  - Added Execution order and memory usage tarcing for debugging.
  - Added TFLite exporter which generates inference model for tflite (unstable).
- Open source updates
  - TensorFlow-Lite2 has been upgraded to version 2.11.0.
  - Flatbuffers has been upgraded to version 2.0.6.

#### Fixes

- Reported bugs in NNStreamer and ML API have been fixed.

#### Known issues
- XNNPACK delegate of TensorFlow-Lite2 is temporarily disabled due to the toolchain version issue.
