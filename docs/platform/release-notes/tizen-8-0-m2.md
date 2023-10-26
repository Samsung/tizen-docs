# Tizen 8.0 M2 Release

Release date: Oct 31, 2023

## Release details

- [Getting source code](http://review.tizen.org/git/) (Tizen 8.0 M2 source codes are under **tizen_8.0** branch.)

- Getting binaries and images
  - Base: [http://download.tizen.org/releases/milestone/TIZEN/Tizen-8.0/Tizen-8.0-Base/tizen-8.0-base_20231016.131614/](http://download.tizen.org/releases/milestone/TIZEN/Tizen-8.0/Tizen-8.0-Base/tizen-8.0-base_20231016.131614/)
  - Profile(Unified): [http://download.tizen.org/releases/milestone/TIZEN/Tizen-8.0/Tizen-8.0-Unified/tizen-8.0-unified_20231019.221723/](http://download.tizen.org/releases/milestone/TIZEN/Tizen-8.0/Tizen-8.0-Unified/tizen-8.0-unified_20231019.221723/)

- [How to flash to a device](../developing/flashing.md)


## Release notes

### System (kernel and system framework)

#### New and changed features

- Kernel
  - Kernel for Raspberry Pi 4 has been upgraded to version 5.15.92.
  - CONFIG_PSI feature of Kernel is used to monitor resources.
- System and resource management
  - Provide the resource-manager/system-plugin-API interface to separate deviced-plugin from device management service.
    - The system-plugin-backend-deviced-headed/headless git/package have been added to support the vendor specific code without any changes of device management core.
  - Separate resourced-plugin including LMK(Low Memory Killer) & CPU boosting stall governors from resource management service.
    - The system-plugin-backend-resourced-generic git/package has been added to include the vendor specific policy according to hardware specification.
  - The light-weighted multi-user csharp-API has been supported.

- Device and sensor management
  - Multi-theme function of sound feedback has been supported to change the feedkback theme on runtime in order to provide the advanced user-experience.
  - Pre suspend-wakeup notifier has been added to reduce the turn on latency of display.

- OS upgrade
  - ISU (Individual Service Upgrade) has been supported instead of fully FOTA update to upgrade per-service quickly and reduce the FOTA cost.

- cryptsetup
  - Version 2.3.7 has been upgraded to version 2.6.1.

#### Fixes

- dbus
  - CVE-2023-34969 patch has been applied.
- btrfs
  - CVE-2023-1611 patch has been applied.
- systemd / cryptsetup / crash-worker / initrd / libdbuspolicy / upgrade
  - Change dependency from openssl1.1 to openssl3.


### System (base)

#### New and changed features

- Open source
  - python3-protobuf
    - Version 3.9.2 has been upgraded to version 4.24.1.
  - ncruses
    - Version 6.2 has been upgraded to version 6.4

#### Fixes

- Open source
  - boost
    - CVE-2018-25032 patch has been applied.
  - libarchive
    - CVE-2023-30571 patch has been applied.
  - python3-numpy
    - CVE-2023-41040 patch has been applied.
    - Add G_SLICE env to install section
	- recompile in the install section
  - grpc
    - Change dependency from openssl1.1 to openssl3
  - libzip
    - Change dependency from openssl1.1 to openssl3
  - libzypp
    - Change dependency from openssl1.1 to openssl3
  - npth
    - Change make_build macro
  - paho-mqtt-c
    - Change dependency from openssl1.1 to openssl3
  - python3
    - Change dependency from openssl1.1 to openssl3
  - python-pycurl
    - Change dependency from openssl1.1 to openssl3
  - python-pyOpenSSL
    - Change dependency from openssl1.1 to openssl3
  - rsync
    - Change dependency from openssl1.1 to openssl3
  - ncruses
	- 20231001 patch has been applied.


### Application framework

#### New and changed features

- Tizen Database Access Object (TDAO)
  - New feature has been ready to access a database.
    - Provide classes for DAO and Entity
    - Provides Compile-time Verification of SQL queries
- TIDL
  - Support for import keyword has been added.
  - Support for method privilege has been added.
  - Support for container types has been added.
  - Support for struct inheritance has been added.
- Launchpad
  - Loader process management has been modified.
  - Process pool feature has been added.
- Application
  - Timezone changed event API has been added.

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
  - The single-pixel-buffer-v1 protocol has been added.
    - This protocol extension allows clients to create single-pixel buffers.
  - The wtz-blender protocol has been added.
    - This protocol allows clients to have more control over alpha compositing and blending of surface contents.
  - The keyboard_grab and keyboard_ungrab requests have been added to tizen_input_device_manager interface.
- Enlightenment
  - The name of e_desk_group has been changed to e_desk_area.
  - The server protocol implementation of wtz_screen and wtz_splitscreen interfaces has been included.
  - The server protocol implementation of wtz_shell interface has been included.
  - The policies for Multi-Windows management have been added.
    - Those are Smart Launch, Snap Window, All Minimize and Smart Rotation.
  - The wheel event in touchpad has been supported.
  - The server protocol implementation of single-pixel-buffer-v1 interface has been included.
  - The server protocol implementation of wtz-blender interface has been included.
  - The server protocol implementation of tws_service_kvm interface has been included.
  - The relative pointer has been supported.
  - The pointer lock has been supported.
  - The input thread for processing key event has been separated for removing key event delivery delay element (Input Device check, Compositing, Capture, and so on).
- Tizen WS Shell
  - The KVM service has been added.
    - KVM service provides Copy&Paste and Drag&Drop among multi-devices
    - The tws_service_kvm interface has beed added to tzsh protocol.
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
- EOM
  - EOM APIs have been deprecated.
- Libinput
  - The version of Libinput has been upgraded to 1.22.0.
- Libxkbcommon
  - The version of Libxkbcommon has been upgraded to 1.5.1.
- TTS Framework
  - Supports root daemon as TTS client.
  - Supports on-demand reconnection of clients when TTS service abnormally terminated. This is useful for low-end devices when its cpu consumption is very high.
  - Supports a client-side callback function to receive synthesized pcm data.
  - Supports a new C API to set playing mode.
- STT Framework
  - Supports USB plug-in microphone for TV binary.
  - Supports new C APIs for audio streaming at client side.
- Voice Control Framework
  - The IPC interface between the voice control engine and voice control clients has been changed from D-Bus to TIDL, which is a proper IPC method between applications.
  - The C API to reduce background volume when the voice manager client wants has been added.
- MMI Framework
  - New MMI architecture has been applied.
  - Supports workflows of voice touch, wakeupless command, and user recognition.
- Gesture Framework
  - Gesture framework has been deprecated.
- Text Input
  - The performance to get surrounding text has been improved.
  - Autofill and Inputmethod setting application has been reimplemented based on NUI gadget.
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
  - Support to modify Physically Based Rendering(PBR) material in runtime.
  - Support for compressed texture formats.
  - Support for directional light and shadow.
  - Support for particle system.
  - Support for integrated open source physics engine (Chipmunk for 2D, Bullet for 3D)
- AI Avatar
  - A new NUI based avatar framework for AI feature.
  - Support for new API to control body/face motion.
  - Support for AI LipSync on device.
- View and Window
  - Some properties have been added to the Camera.
  - An overlay layer has added to the Scene.
  - A new window type DESKTOP has been added.
  - Support for window layout has been added.
  - A BorderWindow has been added to the window.
- Images
  - Support for CMYK jpeg image loading has been added.
  - Support for texture uploading without passing main event.
  - Support for PlaceHolder.
  - Support for image transition.
  - Masking for runtime generated image.
- Text
  - Some text geometry APIs have been added.
  - Some text span APIs have been added.
  - Support for cache of font list
- Drag and Drop
  - Support for multiple windows on a single process has been added.
- Performance / Memory Improvement
  - The object sizes of some internal classes have been reduced.
  - Message processing logic has been optimized.
  - Some matrix operations have been optimized.
  - Unnecessary ClipBoard creation has been removed.
  - Performance optimization of layouting.
  - Graphics backend optimization
- Aurum
  - Support for UI context changed event has been added.
  - Support for UI scrolling finished event has been added.
  - Supports for enabling xPath command
  - Supports for getting the window rotation angle
  - Supports for getting information whether application idle or not
  - Improves the performance of finding element
  - Supports for window rotation function
  - Improves the performance of creating xPath
- UI Analyzer(internal Tool)
  - Supports for the information of rotated window
  - Supports for enhanced test recording
  - Supports for testing validataions
  - Supports for playing the recorded tests and showing the result
  - Supports for saving the recorded tests and loading the saved file
  - Supports for playing the smoke tests automatically
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
- Fixs the crash issue for web application
- Fix the crash issue when click function works
- Fix the memory leak


### Multimedia framework

#### New and changed features

- Open source
  - GStreamer version 1.20.0 has been upgraded to version 1.22.0.
  - Ffmpeg version 4.4.1 has been upgraded to version 5.1.2.
  - Taglib version 1.12 has been upgraded to version 1.13.
  - Tiff version 4.3.0 has been upgraded to version 4.4.0.
  - GraphicsMagicK version 1.3.36 has been upgraded to version 1.3.38.
  - libwebp version 1.2.1 has been upgraded to version 1.2.4.
  - libjpeg-turbo version 2.1.1 has been upgraded to version 2.1.4.
  - libpng version 1.6.37 has been upgraded to version 1.6.38.
  - libjxl version 0.6.1 has been upgraded to version 0.7.0.
- Media Camera
  - New APIs for camera device manager have been added.
  - New APIs for focus level been added.
- Native WebRTC
  - New APIs for audio mute have been added.
  - Some display functions have been changed to return not-supported error on a headless binary.
- Media Content
  - Deprecated some storage related APIs and unused media metadata have been removed.
  - Deprecated thumbnail util APIs have been removed.
- Audio Framework
  - New APIs for sound effects have been added.
    - Support Acoustic Echo Cancellation functionality.
    - Support Noise Suppression based on neural network.
    - Support Automatic Gain Control.
    - Support to be able to get a reference playback stream when recording sound.
- Media Player
  - New APIs for video codec type settings have been added.
- MediaController
  - Add new Capability APIs
    - New C# APIs for PlaybackPosition, PlaylistCapability, CustomCommandCapability, SearchCapability has been added.

### Network and connectivity

#### New and changed features

- Network
  - Support 6GHz band for Wi-Fi 6E has been added.
  - New API for getting 6Ghz band support has been added.
  - New APIs to provide DHCP state and its event have been added.
  - New enumeration for no carrier error has been added.
- Bluetooth
  - New API for setting advertising flags has been added.
  - New APIs for extended advertising have been added.
  - New APIs for scanning extended advertisement have been added.
- Open source
  - ConnMan version has been upgraded to 1.41.

#### Fixes

- Network
  - The logic for passphrase decryption has been fixed.
  - Some logics for BSS transition have been added.
- Bluetooth
  - Failed issue when you fill advertising data with maximum bytes has been fixed.
  - Invalid handle issue when gatt connected with the bonded device has been fixed.
  - Registering gatt client failed issue has been fixed.
  - EIR manufacturer data parsing issue has been fixed.


### Security

#### New and changed features

- Privacy privilege manager
  - Privacy privilege manager (PPM) feature has been deprecated.
- Key manager
  - supports multi-staged encryption.
  - supports importing and exporting wrapped key.
  - supports key derivation with ECDH and KBKDF.


### Service framework

#### New and changed features

- Account Framework
  - FIDO Client has been deprecated.
- Sync-Manager
  - Potential defects have been fixed.
- Location Manager
  - Native APIs of Maps Service has been deprecated.
  - Native APIs Geofence Manager has been deprecated.
  - C# APIs of Maps Service has been deprecated.
  - C# APIs of Geofence Manager has been deprecated.
- Messaging
  - Native APIs of Email service has been deprecated.
  - C# APIs of Email Service has been deprecated.
  - Native APIs of Messaging service has been deprecated.
  - C# APIs of Messaging service has been deprecated.

### Web framework

#### New and changed features

- Web Engine
  - SoundFocusManager for web media has been supported.
  - Accessibility has been supported.
  - H.264 codec for public profile has been supported.
  - ewk_view_ime_window_set to support IME for NUIhas been added.
- Web Runtime
  - Views-based splash screen has been applied.

#### Fixes

- Rotation defect in offscreen mode has been fixed.
- Media suspend/resume defect between apps has been fixed.
- Text Drag and Drop defect has been fixed.
- Crash in ScrollFocusedNode has been fixed.


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

#### New and changed features

- Machine Learning (ML) API updates
  - ML.Service API Updates
    - Add new APIs to separately manage ML model files. These APIs allow ML applications to exploit the latest ML model deployed without code-level modifications that require re-packaging and re-distribution of the whole application.
    - AI Inference offloading between Tizen and TizenRT has been improved. The binary size of `NNStreamer-Edge` is optimized.
    - Add new APIs for machine learning resource which contains images, audio, video and binary files. These APIs provides a method to share the data files those can be used for training or inferencing the AI models.
    - Add new utility functions to handle the key-value style information. This informantion object can be used to update the configuration and check the internal status.
  - ML.Inference API Updates
    - Add new API to use extended rank limit. To maintain the backward compatibility, the default rank limit is 4. The extended rank is only used when new API is called.
    - Support TensorFlow Lite v2.11.0 by default.
  - ML.Training API Updates
    - Add Identify Layer as a utility layer which flows everthing as it is.
    - Add learning rate scheduling features.
    - Step learning rate scheduling.
    - Exponent learning rate scheduling.
    - Add API to get the weight data.
- NNStreamer updates
  - NNStreamer has been upgraded to version 2.4.0.
  - Support for large-size model of the NNStreamer pipeline has been added.
    - The number of rank limit has been increased up to 16.
    - The number of tensor limit has been increased up to 256.
  - Support for the model storage of Device MLOps has been added.
    - Model management feature such as register, fetch active model, update, and delete has been added. Using this feature, ML applications can share their model with other applications.
  - Pipeline based data repository and training feature has been added.
    - New NNStreamer elements such as `datareposrc`, `datareposink`, and `tensor_trainer` have been added.
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
