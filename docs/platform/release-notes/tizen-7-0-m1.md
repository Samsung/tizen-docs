# Tizen 7.0 Public M1

Release date: May 31, 2022


## Release Notes

### System (Kernel and System framework)

#### New and changed features

- Kernel and U-Boot upgrade
  - Kernel for Raspberry Pi 4 has been upgraded to version 5.10.95.
  - U-boot has been upgraded to v2021.10.
- PREEMPT_RT Support
  - PREEMPT_RT applied kernel for Raspberry Pi 4 has been supported.
- System and resource management
  - Cgroup hierarchy and configurations have been improved.
  - Partition detection mechanism in initrd has been optimized.
- Device and sensor management
  - Sensor attribute set API set for lidar sensor has been developed.
  - USB gadget mode management based on bitmap has been developed.
  - API set for boot mode and reason has been developed.
  - Udev-based detection and recovery for dm-verity corruption have been developed.
- Resource management
  - CPU and memory resource isolation based on cgroup hierarchy has been developed.
  - CPU boosting and throttling configurations for PREEMT_RT have been developed.
- Container support
  - Internal storage detection has been improved for container environment.
  - Dlog log separation for container environment has been developed.
- Open source
  - GDBus (Glib) has been upgraded to version 2.70.0.
  - Bcc has been upgraded to version 0.24.0 for supporting llvm 10.0.0.


### System (Base)

#### New and changed features

- Open source
  - abseil-cpp
    - Version 20200923.2 has been upgraded to version 20210324.2.
  - attr
    - Version 2.4.48 has been upgraded to version 2.5.1.
  - autoconf
    - Version 2.69 has been upgraded to version 2.71.
  - autoconf-archive
    - Version 2019.01.06 has been upgraded to version 2021.02.19.
  - automake
    - Version 1.15.1 has been upgraded to version 1.16.4.
  - boost
    - Version 1.71.0 has been upgraded to version 1.77.0.
  - byacc
    - Version 20100216 has been upgraded to version 20210808.
  - chrpath
    - Version 0.13 has been upgraded to version 0.16.
  - cmake
    - Version 3.16.4 has been upgraded to version 3.21.
  - dash
    - Version 0.5.9.1 has been upgraded to version 0.5.11.5.
  - docbook-xsl-stylesheets
    - Version 1.78.1 has been upgraded to version 1.79.2.
  - dos2unix
    - Version 7.4.1 has been upgraded to version 7.4.2.
  - doxygen
    - Version 1.8.2 has been upgraded to version 1.9.2.
  - ecryptfs-utils
    - Version 104 has been upgraded to version 111.
  - ed
    - Version 1.6 has been upgraded to version 1.17.
  - expat
    - Version 2.2.9 has been upgraded to version 2.4.1.
  - expect
    - Version 5.45 has been upgraded to version 5.45.4.
  - fdupes
    - Version 1.4 has been upgraded to version 2.1.2.
  - file
    - Version 5.39 has been upgraded to version 5.41.
  - glib
    - Version 2.62.3 has been upgraded to version 2.70.0.
  - gobject-introspection
    - Version 1.66.0 has been upgraded to version 1.70.0.
  - golang
    - Version 1.15.2 has been upgraded to version 1.17.4.
  - grpc
    - Version 1.35.0 has been upgraded to version 1.42.0.
  - gtest
    - Version 1.10.0 has been upgraded to version 1.11.0.
  - gtk-doc
    - Version 1.32 has been upgraded to version 1.33.2.
  - help2man
    - Version 1.40.10 has been upgraded to version 1.48.5.
  - Icu
    - Version 67.1 has been upgraded to version 70.1.
  - Intltool
    - Version 0.50.2 has been upgraded to version 0.51.0.
  - iso-codes
    - Version 3.13 has been upgraded to version 4.7.0.
  - Itstool
    - Version 2.0.5 has been upgraded to version 2.0.7.
  - jsoncpp
    - Version 1.9.2 has been upgraded to version 1.9.4.
  - json-glib
    - Version 1.6.0 has been upgraded to version 1.6.6.
  - kbd
    - Version 2.0.4 has been upgraded to version 2.2.0.
  - lcov
    - Version 1.14 has been upgraded to version 1.15.
  - libaio
    - Version 0.3.110 has been upgraded to version 0.3.112.
  - libarchive
    - Version 3.5.1 has been upgraded to version 3.5.2.
  - libdatrie
    - Version 0.2.10 has been upgraded to version 0.2.13.
  - libevent
    - Version 2.1.11 has been upgraded to version 2.1.12.
  - libksba
    - Version 1.3.0 has been upgraded to version 1.6.0.
  - libpipeline
    - Version 1.2.2 has been upgraded to version 1.5.0.
  - libsigc++
    - Version 2.9.3 has been upgraded to version 2.10.7.
  - libsolv
    - Version 0.7.16 has been upgraded to version 0.7.19.
  - libtool
    - Version 2.4.2 has been upgraded to version 2.4.6.
  - libunistring
    - Version 0.9.4 has been upgraded to version 0.9.10.
  - libwbxml2
    - Version 0.11.2 has been upgraded to version 0.11.7.
  - libxml++
    - Version 2.42.0 has been upgraded to version 3.2.3.
  - libzip
    - Version 1.7.3 has been upgraded to version 1.8.0.
  - lsof
    - Version 4.87 has been upgraded to version 4.91.
  - m4
    - Version 1.4.17 has been upgraded to version 1.4.19.
  - make
    - Version 4.0 has been upgraded to version 4.3.
  - man-db
    - Version 2.6.3 has been upgraded to version 2.9.4.
  - meson
    - Version 0.55.3 has been upgraded to version 0.60.3.
  - mm-common
    - Version 1.0.1 has been upgraded to version 1.0.3.
  - mtools
    - Version 4.0.18 has been upgraded to version 4.0.36.
  - multipath-tools
    - Version 0.4.9 has been upgraded to version 0.8.8.
  - openfst
    - Version 1.6.5 has been upgraded to version 1.8.1.
  - paho-mqtt-c
    - Version 1.3.7 has been upgraded to version 1.3.9.
  - parted
    - Version 3.1 has been upgraded to version 3.4.
  - patch
    - Version 2.7 has been upgraded to version 2.7.6.
  - pcre
    - Version 8.44 has been upgraded to version 8.45.
  - perl
    - Version 5.32.0 has been upgraded to version 5.34.0.
  - pkg-config
    - Version 0.28 has been upgraded to version 0.29.2.
  - procps-ng
    - Version 3.3.16 has been upgraded to version 3.3.17.
  - psmisc
    - Version 23.3 has been upgraded to version 23.4.
  - python3
    - Version 3.9.1 has been upgraded to version 3.9.10.
  - re2
    - Version 20201101 has been upgraded to version 20220201.
  - re2c
    - Version 1.1.1 has been upgraded to version 3.0.
  - rpmlint
    - Version 1.4 has been upgraded to version 1.11.
  - rsync
    - Version 3.1.1 has been upgraded to version 3.2.3.
  - sgml-skel
    - Version 0.6 has been upgraded to version 0.7.1.
  - sqlite
    - Version 3.33.0 has been upgraded to version 3.36.0.
  - sudo
    - Version 1.9.4 has been upgraded to version 1_9_7p2.
  - tzdata
    - Version 2020a has been upgraded to version 2021e.
  - util-linux
    - Version 2.36 has been upgraded to version 2.37.


### Application framework

#### New and changed features

- Tizen boot sequence
  - A new feature has been ready to control app launch on system boot.
  - A tool to check the status of the app after booting has been provided.
- TIDL
  - The TIDL compiler can generate new API set using the Cion-group API set.

#### Fixes

- App-core
  - The implementation has been refactored into the C++ language.
- Pkgmgr-info
  - A cache for pkginfo-server has been applied to improve the online mode performance of getting package information.
  - Offline mode performance of getting package information has been improved.
- App-installer
  - The preload package installation order in MIC builds has been changed for devices with low storage capacity.


### Window and Interaction

#### New and changed features

- Open source
  - wayland has been upgraded to version 1.20.0.
  - The libxkb-common has been upgraded to version 1.3.1.
  - The libinput has been upgraded to version 1.17.0.
  - The libevdev has been upgraded to version 1.11.0.
  - The mesa has been upgraded to version 21.2.3.
- Enlightenment
  - The Drag and Drop has been added. It provides wl_data_device_manager interface of wayland protocol to the wayland-clients.
- Vulkan
  - The vulkan-wsi-layer has been added. It implements Vulkan window system integration extensions.
- OpenCL
  - The Common OpenCL Packages have been added.
    - The OpenCL-Headers has been added. It contains C language headers for the OpenCL API.
    - The OpenCL-ICD-Loader has been added. It allows developers to build application against an Installable Client Driver loader.
- TTS Framework
  - In order to reduce memory usage, the TTS engine, which used to execute in multiple processes, has been improved to execute as one process.
  - The client structure and TTS player to support thread safety has been improved.
  - The TTS engine API to terminate the process has been added.
  - The API to connect TTS engine synchronously has been added.
  - The API to repeat TTS text has been added.
- Sticker Framework
  - C# sticker API has been added.
- Text Input Framework
  - Vietnamese and Thai language has been supported in the Tizen reference IME.
  - The inputmethod C# API set to set preedit cursor position and set the callback to get input hint has been added.
  - wayland inputmethod interface has been updated as the latest open source.

#### Fixes

- Text Input Framework
  - C# inputmethod API set returns the appropriate error exception.


### Graphics and UI

#### New and changed features

- Rendering
  - An interface to support direct rendering has been added.
- Input and Gesture
  - Support for CustomWheel Event has been added to the View.
  - Some properties and signals regarding input and gesture have been added.
- Window
  - A method to receive an auxiliary message has been added.
  - Methods to maximize and minimize a window have been added.
  - Support for Drag and Drop has been added.
- View
  - Various methods have been added to the WebView.
  - Various properties and methods have been added to the TextLabel, TextField and TextEditor.
- ATSPI
  - Multi window activate/deactivate has been added.
  - TextField password information protection has been added.
  - Hyperlink ATSPI Interface has been added.
  - Performance to enable AT-SPI has been improved.
  - MBR (Minimum Bounding Rectangle) has been added.
  - Multiple AT-SPI interfaces for View have been added.
  - Default label Feature has been added.
  - NUI Component default accessibility has been added.
  - Singleton Accessibility Delegate to enhance memory usage has been added.
  - Text Control Accessible has been added.
  - ATSPI/Screen-Reader Enabled/Disabled Signal has been added.
  - ATSPI suppressed events have been added.
- XAML
  - The separated Tizen.NUI.XamlBuild package has been integrated and migrated into Tizen.NET meta package.
- Aurum
  - Toolkit Event Listener has been added.
  - Searching object with partial string feature has been added.
  - Generating XPath for UI Object feature has been added.
  - Setting focus object has been added.
  - Using role name for no type object case has been added.
- UI Analyzer
  - Click, Input Text, Disconnect functions have been added.
  - The selected rectangle in screenshot with object item has been added.
  - XPath information feature has been added.
- Performance Improvement
  - Property registration time has been decreased.
  - Unnecessary memory reallocation and copy have been reduced in the various classes.
  - The type registration has been optimized.
  - The VisualRenderer has been added to reduce property registration for each visual.
  - Loading time for various image format has been decreased.
  - An operation of the font description has been optimized.
  - An unused signal of the StyleManager has been disconnected with Controls.
- Open source
  - Harfbuzz version 2.6.7 has been upgraded to version 3.4.0.
  - SDL version 2.0.8 has been upgraded to version 2.0.14.
  - AT-SPI2-Core version 2.39.90 has been upgraded to version 2.42.0.

#### Fixes

- The SceneHolder's RenderTarget initialization defect has been fixed.
- Various partial update defects have been fixed.
- Various ATSPI defects have been fixed.
- Various text related defects have been fixed.


### Multimedia framework

#### New and changed features

- Open source
  - GStreamer
    - Version 1.16.2 has been upgraded to version 1.20.0.
    - mms plugin has been removed.
  - libnice
    - Version 0.1.17 has been upgraded to version 0.1.18.
  - OpenCV
    - Version 4.5.0 has been upgraded to version 4.5.3.
  - Pulseaudio
    - Version 13.0 has been upgraded to version 15.0.
  - libsndfile
    - Version 1.0.28 has been upgraded to version 1.0.31.
  - ffmpeg
    - Version 4.3.1 has been upgraded to version 4.4.
  - libtiff
    - Version 4.1.0 has been upgraded to version 4.3.0.
  - GraphicsMagick
    - Version 1.3.35 has been upgraded to version 1.3.36.
  - libwebp
    - Version 1.1.0 has been upgraded to version 1.2.1.
  - taglib
    - Version 1.11.1 has been upgraded to version 1.12.
  - libjpeg-turbo
    - Version 2.0.6 has been upgraded to version 2.1.1.
  - lcms2
    - Version 2.4 has been upgraded to version 2.12.
- Native WebRTC
  - Statistics API set has been added.
  - Data channel buffered amount API set has been added.
  - Frame rate set/get functions for video source have been added.
  - Bundle policy API has been added.
  - Support for in-band FEC has been added.
- Image Util
  - Support for Jpeg-XL has been added.
    - Open source libjxl 0.6.1 version has been applied.
    - Support for decoding Jpeg-XL image format has been added.
    - Support for encoding Jpeg-XL image format has been added.
  - The image_util_encode_set_webp_lossless API has been deprecated.
- Media Editing Framework
  - Support for the most frequently used editing functionalities has been added.
    - Place audio/video/image contents freely on timeline.
    - Cut and paste clip and add video transition for overlapped video.
    - Add background music and adjust volume level by each audio track.
    - Add effects using various GStreamer effect plugins.
  - Pause & resume, share editing artifacts

#### Fixes

- Native WebRTC
  - Various types of memory leak defects have been fixed.
  - A crash when making packet lost custom event has been fixed.
  - ‘ice-gathering-state’ signal defect regarding data channel has been fixed.


### Network and Connectivity

#### New and changed features

- Matter
  - Matter which aims for unifying and IP-based connectivity protocol has been added.
- Thread
  - Network device protocol for thread has been added.
- Wi-Fi
  - New feature for BSS transition has been added.
- Bluetooth API
  - The API set for LE CoC has been added.
  - New feature for LE CoC has been added.
    - `http://tizen.org/feature/network.bluetooth.le.coc`
- Open source
  - Connman has been upgraded to version 1.40.
  - Curl has been upgraded to version 7.81.0.
  - Libwebsockets has been upgraded to version 4.2.
  - Mdnsresponder has been upgraded to version 1310.80.1.

#### Fixes

- Bluetooth
  - Some bugs related with BLE Advertisement have been fixed.
  - The specific logic for mobile profile has been removed.
  - Some logics for IoT profile have been added.
- Network
  - Logical deadlock issue has been fixed.
  - Some bugs related with INS have been fixed.
  - Some memory leak issues have been fixed.


### Service framework

#### Fixes

- Account Framework
  - Potential defects have been fixed.
- Sync-Manager
  - Potential defects have been fixed.
- Location Framework
  - Potential defects have been fixed.
- Message Framework
  - Potential defects have been fixed.


### Web framework

#### New and changed features

- Web Engine
  - Open source chromium 94 version base has been applied. Below features and API set have been provided by the new web engine.
    - WebRTC Insertable Streams feature has been added.
    - Pan/Tilt support for camera using media constraints in getUserMedia() has been added.
    - WebCodecs feature for efficient, low-level access to built-in (software and hardware) media encoders and decoders has been added.
    - File System Access API to read or save changes directly to files and folders on the user's device has been added.
    - Application Cache feature has been deprecated.
- Web Runtime
  - Open source electron 15.3.3 version has been applied.

#### Fixes

- Image drag & drop between NUI app and web app has been supported.


### Lightweight Web Solution

#### New and changed features

- Lightweight Web Engine
  - Web Engine
    - Dropdown menu feature has been added.
    - CSS Custom property has been added.
    - CSS mask-image property has been added.
    - Rendering performance for css custom property has been optimized.
    - Painting performance for gradient has been improved.
  - Javascript Engine
    - WeakRef and finalizationRegistry specification have been added.
    - JS debugger has been added.
- JS based lightweight backend service FW
  - Lightweight node.js
    - Customizable exception handling has been added.
    - Serializer and deserializer have been added.
    - IndexedPropertyHandlers have been added.

#### Fixes

- Lightweight Web Engine
  - WebSocket memory leak defects have been fixed.
  - Grid layout defects have been fixed.
- Lightweight node.js
  - Promise defects have been fixed.
  - Template defects have been fixed.
  - Multithread defects have been fixed.
  - StackTrace defects have been fixed.
  - V8 modules have been hidden by default.


### Tizen .NET

#### New and changed features

- .NET
  - TizenFx
    - Some Slider events have been removed from Tizen.NUI.
    - Sticker class has been added to Tizen.Uix.
    - RepeatedText class has been added to Tizen.Uix.Tts.
    - New module errors have been added to Tizen.Uix.Tts.
    - MediaFileSource class has been added to Tizen.Multimedia.Remoting.
    - BufferedAmountLow event has added to Tizen.Multimedia.Remoting.
    - GLView has been added to NUI.
    - PrimaryCursorPosition has been added to TextField and TextEditor of NUI.
    - InputHint has been added to Tizen.Uix.InputMethod.
  - .NET runtime and tools
    - .NET Runtime has been upgraded from NETCore 3.1.3 to .NET 6.


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


### Machine Learning

#### New and changed features

- Machine Learning (ML) Inference API updates
  - capi-machine-learning-inference-single package have been added so that devices may have SingleShot API without installing Pipeline API, GStreamer, and NNStreamer's core packages.
  - Version 2.7.0 of TensorFlow Lite has been supported as default.
- Machine Learning (ML) Service API (new)
  - API set to set / get / delete pipeline descriptions has been added. Applications may register (set) pipeline descriptions and other applications may refer to (get) such shared pipeline descriptions.
- Machine Learning (ML) Training API updates
  - ml_train_model_get_layer() API has been added to get neural network layer from the model with the given name.
- NNTrainer updates
  - New layers to support advanced training methods have been added.
    - CNN: Convolution 1D layer.
    - Recurrent Net: LSTM Cell, GRU Cell, RNN Cell and Zoneout LSTM Cell layer
- NNStreamer updates
  - NNStreamer has been upgraded to version 2.1.
  - Extra configuration for product support has been added.
  - TF-Lite filter has been updated to support XNNPACK Delegate of Tensorflow Lite.
  - TRIx-Engine filter for TRIV2 NPU has been added.
  - [Experimental] new interfaces for Edge-AI service are introduced. This will provide various among-device AI experience:
    - provides inference or AI-based service from low-powered node to high-end device.
    - publishes or subscribes raw data stream (e.g., camera frame, sensor data) via MQTT.
    - This may support both pipelined or non-pipelined applications and edge devices.
- Trix-Engine
  - Support TRIx NPU equipped product, DTV
  - Available for DTV web application development
- TensorFlow Lite updates
  - TensorFlow Lite has been upgraded to version 2.7.0.
  - XNNPack Delegate has been enabled.
- Neural Network Runtime
  - Introduced configuration files in nnpackage to allow users to set configuration variables via conf files.
  - Runtime uses Arm Compute Library v21.02.
  - A new backend (gpu_cl) has been added. This backend supports Add, Convolution, Depthwise Convolution, Pooling, Reshape, Relu, Softmax operations.
  - A new backend (TRIX) has been added.
    - TRIX backend supports trix binary with NHWC layout.
    - TRIX backend supports trix binary with input/output of Q8 and Q16 type.
