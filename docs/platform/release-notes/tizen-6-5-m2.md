# Tizen 6.5 Public M2

Release date: Oct. 31, 2021

## Release details

- [Getting source code](http://review.tizen.org/git/) (Tizen 6.5 M2 source codes are under **tizen_6.5** branch.)

- Getting binaries and images
  - Base: [http://download.tizen.org/releases/milestone/tizen/base/tizen-base_20211001.1/](http://download.tizen.org/releases/milestone/tizen/base/tizen-base_20211001.1/)
  - Profile(Unified): [http://download.tizen.org/releases/milestone/tizen/unified/tizen-unified_20211014.1/](http://download.tizen.org/releases/milestone/tizen/unified/tizen-unified_20211014.1/)

## Release notes

### System (kernel and system framework)

#### New and changed features

- New API and features
  - Kernel
    - A fine-grained version of THP (Transparent HugePage) in Linux kernel for embedded systems has been implemented in Raspberry Pi 4.
  - HAL
    - HAL API Layer is implemented for unifying the HAL backend style and splitting out the hardware dependency.
    - New image structure is adapted for HAL, new partition is added for a set of HAL backend packages.
  - System and resource management
    - VIP process monitor has been improved by removing race conditions.
    - Percentage-based memory threshold has been developed.
    - Coredump generation for .NET 6 runtime has been supported.
    - Tizen feature database tools have been improved.
    - Container adaptation for file system mount units has been developed.
  - Device and sensor management
    - Orientation and rotation vector sensor algorithms have been upgraded for improving correctness.
    - HAL backend for Inertial Measurement Unit (IMU) sensors has been implemented for Raspberry Pi 4 devices.
    - Separate backend libraries for sensor devices have been supported.
    - Daemon-less direct API set for peripheral-io and runtime memory usage has been developed.
    - Sleep mode for IoT headless devices has been supported.
    - Display control for HDMI-based external display devices has been supported.
    - Display option for USB connection change has been added.
    - API for board serial number has been added.
  - OS upgrade
    - FOTA update for Raspberry Pi 4 IoT headless devices has been supported.
    - Crash recovery schemes have been developed for reliable OS upgrade.
    - Metadata for FOTA server management has been included in delta files.
    - Testsuites for OS upgrade have been developed.
    - Delta file generators have been improved.
  - Open source
    - CVE-2021-33910 patch has been applied to systemd.


### System (base)

#### New and changed features

- Open source
  - ccache
    - Version 3.1.6 has been upgraded to version 4.4.
  - libxml2
    - Version 2.9.10 has been upgraded to version 2.9.12.
  - gtest
    - Version 1.8.0 has been upgraded to version 1.10.0.
- System-settings
  - Image validation checker for two keys has been removed.
    - SYSTEM_SETTINGS_KEY_WALLPAPER_HOME_SCREEN
    - SYSTEM_SETTINGS_KEY_WALLPAPER_LOCK_SCREEN

#### Fixes

- CVE patches
  - libxml2
    - CVE-2019-20388
    - CVE-2020-24977
    - CVE-2020-7595


### Application framework

#### New and changed features

- Resource package
  - A new installer for resource packages has been added.
  - API set for retrieving information of a resource package has been added.
- Cross device communication using TIDL
  - API set for device-to-device communication has been added.
  - An option to compile for device-to-device communication has been added to TIDLC.
- rpc-port extension
  - The library has been modified to use stub API in daemon process.

#### Fixes

- rpc-port
  - The dependency on D-Bus has been removed.
- pkgmgr-tool
  - Minor bugs have been fixed.


### Window and interaction

#### New and changed features

- Text Input Framework
  - The sticker input in reference IME in case of installing sticker package has been added.
  - The keyboard hot key (Shift & Space) for switching H/W keyboard language has been added.
  - The API to support NUI IME has been added.
- Multi-assistant Framework
  - Support for N:N relationship between multiple wake-up engines and voice assistants has been added.
- Multi-modal Interaction Framework
  - The API to support multi-modal interaction has been added.
  - The multi-modal interaction manager has been added.
- Enlightenment Wayland display server
  - Foreign Shell has been added. This provides sharing wayland resources between wayland clients through exporting and importing foreign shells.
  - Support for always on parent functionality has been added.
  - Support for pending_show functionality has been added.
  - Support for showing the softkey service by swipe up has been added.
- TBM
  - TBM HAL Backend for amlogic chipset has been added.
  - TBM HAL Backend for msm chipset has been added.
- TDM
  - TDM HAL Backend for amlogic chipset has been added.
  - TDM HAL Backend for msm chipset has been added.


### Graphics and UI

#### New and changed features

- NUI
  - Common
    - HorizontalAlignment and VerticalAlignment have been added in LinearLayout.
    - Argument type of TimePeriod has been changed.
    - AdjustViewSize to ImageView has been added.
    - Page Transition API set has been added.
    - Text Selection API set in TextField, TextEditor has been added.
    - SpaceEvenly to FlexJustification has been added.
    - Copy, Cut and Paste for Text on TextEditor and TextField have been added.
    - FindDescendantByID, Raise, Lower, GetOriginalImageSize have been added.
    - BorderlineWidth, Color and Offset in View have been added.
    - SelectionCleared, SelectionChanged and CursorPositionChanged events to TextField and TextEditor have been added.
    - EllipsisPosition properties to TextLabel, TextField and TextEditor have been added.
    - SafeNativeWindowHandle has been replaced into Window.NativeHandle.
    - VideoView.NativeHandle has been added.
    - Hyphenation and Mixed modes to LinewrapeMode enum have been added.
    - InputFilter API set in TextField, TextEditor has been added.
    - NUI IME window support has been added.
    - Capture API set has been added.
    - GetHeightForWidth() and GetWidthForHeight() have been added.
    - AnchorClicked events to TextLabel, TextField and TextEditor have been added.
    - Transition API set has been added.
    - EXaml (Enhanced XAML) feature which separates XAML resources has been added.
    - Gesture propagation has been added.
    - Support for ETC2_EAC compressed format texture has been added.
    - Support for focus finder has been added.
    - Support for background and span markup tags has been added to TextLabel.
  - Components
    - RiveAnimationView has been added.
    - Grouping, Clipping, Masking, Gradient (Linear, Radial), Path and Picture functions has been added in CanvasView.
    - Accessibility (AT-SPI2) functionalities for all Components have been added.
    - Navigator Popped event has been added.
    - Page Appear/Disappear events have been added.
    - MakeToast function has been added in Notification.
    - ItemAlignment and ItemSpacing properties have been added in Button.
    - Slider and Progress properties related to showing value have been added.
    - Page Navigation API set has been added.
    - DialogPage has been added.
    - Menu and MenuItem classes have been added.
- ThorVG
  - SVG Loader has been enhanced by supporting more extensible SVG spec including embedding images.
  - PNG, JPG formats have been supported.
  - Binary Vector Graphics Data Format (TVG) has been supported.
  - SVG - TVG file converter has been added in the ThorVG Viewer (`www.thorvg.org/viewer`).

#### Fixes

- NUI
  - Layout related bugs have been fixed.
  - A clipping bug of a transparent renderer has been fixed.
  - A bug that a triple tap doesn’t work has been fixed.
  - Invalid text selection behavior has been fixed.


### Multimedia framework

#### New and changed features

- MediaPlayer
  - New display type for video and UI synchronization has been added.
- capi-media-vision
  - Inference
    - New pre-/post-process based on models meta files has been applied.
- media-content
  - New media type for ebook (epub3, pdf) has been added.
  - API set for searching ebooks has been added.


### Network and connectivity

#### New and changed features

- Wireguard VPN
  - Wireguard protocol which aims for better performance than IPsec and OpenVPN has been added.
- Advanced on-line checking
  - New BPF-based low overhead mechanism for checking internet connection status has been added.
- Wi-Fi
  - New feature for supporting MAC address randomization has been added.
    - `http://tizen.org/feature/network.wifi.mac_randomization`
- User Awareness API
  - The API set for monitoring user location has been added.
  - New feature for the user location has been added.
    - `http://tizen.org/feature/network.user_awareness.location`
- Smartcard API
  - New feature for supporting USB type secure element has been added.
    - `http://tizen.org/feature/network.secure_element.usb`
- Vine
  - BLE datapath support has been added.
  - Wifi-Aware (NAN) datapath support has been added.
- Bluetooth API
  - New GATT C# API set for MTU size has been added.

#### Fixes

- Bluetooth
  - GATT write request issue with the zero length has been fixed.
  - Some bugs related with Mesh Node role have been fixed.
  - Device name converting issue in C# has been fixed.
- User Awareness
  - Some memory leak issues have been fixed.
- Network
  - MAC address randomization issue with multiple Wi-Fi interfaces has been fixed.
  - Some bugs related with WPA3-SAE transition mode have been fixed.
  - Some memory leak issues have been fixed.


### Service framework

#### Fixes

- Account Framework
  - Potential defects have been fixed.
- Sync-Manager
  - Potential defects have been fixed.
- Location Framework
  - Potential defects have been fixed.
  - HAL layer decoupling has been applied.
- Messaging
  - Potential defects have been fixed.
- Push
  - Glib timer support has been added.


### Web framework

#### New and changed features

- Web Runtime
  - Addon features have been added.
    - Translation feature
    - Categorization feature

#### Fixes

- Web Engine
  - NUI WebView support
    - Resizing issue has been fixed.
    - Surface orientation issue has been fixed.
  - Known Security vulnerabilities have been fixed.
    - CWE-676


### Lightweight web solution

#### New and changed features

- Lightweight Web Engine
  - Web Engine
    - Flutter port has been added.
    - An Image map feature has been added.
    - Support for HTTP/2 Protocol has been added.
  - JS API set
    - TextEncoder/TextDecoder Web API set has been added.
  - Javascript Engine
    - ECMAScript 2020 features have been added.
    - WebAssembly MVP features have been added.
    - JS CodeCache has been optimized.
- JS based lightweight backend service FW
  - Lightweight node.js has been added.

#### Fixes

- Lightweight Web  Engine
  - (Grid/Flex) Layout defects have been fixed.
  - File defects have been fixed.


### Tizen .NET

#### New and changed features

- TizenFx
  - Tizen.NUI
    - LinearLayout.LinearAlignment has been deprecated.
    - Navigator Popped event has been added.
    - Page Appear/Disappear event has been added.
    - Argument of TimePeriod has been changed.
    - LinearLayout.Horizontal/VerticalAlignment has been added.
    - AdjustViewSize has been added to ImageView.
    - Page Transition has been added.
    - The name of ImageView Property has been changed.
    - Text Selection has been added to TextField, TextEditor.
    - Input Filter has been added to TextField, TextEditor.
    - Copy, Cut, and Paste have been added to TextField, TextEditor.
    - BorderlineWidth/Color/Offset has been added to NUI.BaseComponents.View.
    - RiveAnimationView has been added.
    - Support for IME Window has been added.
    - WebView has been added.
    - CameraView has been added.
    - Picker has been added.
    - ResizePolicy has been deprecated.
  - Tizen.Multimedia
    - New Inference configuration has been added.
    - Legacy Inference configuration has been deprecated.
    - Support for Video & UI Sync has been added.
    - Support for HEIF image has been added.
    - ConnectAsync has been added.
    - Support for EBook Format has been added.
    - Additional GATT API set has been added.
    - WebRTC has been added.
    - Support for CameraPixelFormat (VP8, VP9) has been added.
    - Additional VideoMimeTypes have been added.
  - Tizen.Applications
    - Cion has been added.
    - New constructor and method has been added to RPCPort.
    - Parcel.Header has been added to RPCPort.
    - Support for Resource Control has been added.
  - Tizen.Uix.Tts
    - Errors and API set for Screen Reader Option have been added.
  - Tizen.Uix.InputMethod
    - IME Resizing has been added.
  - Tizen.MachineLearning
    - Support for Neural Network Framework and HW Type has been added.
  - Tizen.Security
    - OCSP has been deprecated.


### Toolchain

#### New and changed features

- Hardware-assisted AddressSanitizer (HWASan)
  - GCC/ Libsanitizer : HWASan feature has been backported and tuned for Tizen.
  - HWASan compiler options have been applied.
  - HWASan runtime options have been applied to build and runtime environment.
  - Support for HWASan has been added to glibc and packages.
- Large File Support (LFS)
  - LFS support has been added to AArch64.
- New architecture(ARMv7hl) support
  - Build support has been added for 32-bit hard float ABI.

#### Fixes

- Binutils/ LTO bug #25355
  - LTO plugin bugfix has been backported into binutils, ld, and bfd.
- Glibc/ dynamic linker bug #24259
  - Dynamic linker crash after a previously failed call to dlopen has been fixed.
- Toolchain testsuites bugs have been fixed on GCC, Glibc and Binutils.


### Machine learning

#### New and changed features

- Machine Learning (ML) Inference API
  - New neural network framework identifiers including VD_AIFW (Samsung Tizen TV) and TRIX_ENGINE (SR NPU) have been added.
  - New HW accelerator designators including NPU_SLSI (Samsung S.LSI) and NPU_SR (SR NPU) have been added.
  - ml_pipeline_src_input_callback() API has been added to support callbacks for the app-src element.
  - ml_check_nnfw_availability_full() API has been added to check HW availability with custom option strings.
- Machine Learning (ML) Training API and NNTrainer updates
  - Model save and load API set have been added.
  - Model input and output tensor information query API has been added.
  - API set to create and to set dataset properties has been added.
  - New layers to support advanced training methods have been added.
    - CNN : Embedding layer, Split layer, Permute layer, and Dropout layer
    - Recurrent Net : RNN layer, LSTM layer, and GRU layer
  - New layers to augment data have been added.
    - Flip layer, and Translate layer.
  - New layers to support meta-learning algorithms have been added.
    - Centroid KNN layer and L2norm layer
- NNStreamer updates
  - NNStreamer has been upgraded to version 2.0.
  - Integrated SR-NPU development environment has been added: HAL, driver package, emulator, sample code, and so on.
  - Script mode for Python and Lua has been added to run scripts directly in the pipeline description.
  - New subplugins including Apache TVM, SNPE (Snapdragon Neural Processing Engine) have been added.
  - New event for tensor-filter subplugin has been added to support an optional event, custom HW availability checks.
- Edge-AI features
  - Data serialization mechanisms have been added: Protocol buffer, FlatBuffer, and FlexBuffer.
  - Remote query (client/server) capability has been added. This allows offloading AI inference workload.
  - New tensor stream types, sparse tensors and flexible tensors, have been added to support various AI data streaming format.
  - MQTTSink and MQTTSrc elements have been added to support Pub/Sub streams via MQTT brokers.
- AI Inference Offloading Framework
  - A new framework for offloading ML model inference to the high-end devices in LAN has been added.
  - An app can discover high-end devices (peers) in LAN and request to one of them to inference the app’s ML model on behalf.
  - All the devices are authenticated and the communication channels for transferring inputs and outputs are encrypted.
  - NNStreamer is used for construction remote inference pipeline.

#### Fixes

- ML Inference API / NNStreamer
  - The hidden memory issues including memory leakage, double free, and segmentation faults have been fixed.
  - Mutex issues including unnecessary locks and dead locks have been fixed.
