# Tizen 6.5 Public M1

Release date: May 31, 2021


## Release Notes

### System (Kernel and System framework)

#### New and changed features

- Kernel upgrade
  - Kernel for Raspberry Pi 4 has been upgraded to version 5.10.25.
- System management
  - Filesystem compression (SquashFS) has been applied to the ramdisk partition.
  - F2FS filesystem has been adopted for writable partitions.
  - D-Bus message marshalling operations have been optimized.
- Device and sensor management
  - Hardware abstraction layer (HAL) for device and sensor modules has been refactored.
  - HAL test cases have been developed.
  - Display state caching has been developed.
  - Daemon-less direct API for battery framework has been developed.
- Resource management
  - C# API set for process memory usage on GPU and SWAP has been added.
  - Memory limitation for UI applications has been improved.
- Diagnostics and logging
  - Transparent redirection of stdout and stderr to dlog has been developed.
  - Efficient sharing of diagnostics data between services and applications has been developed.
  - API set for publishing and requesting diagnostics data has been added.
- Open Source
  - SquashFS has been upgraded to version 4.4 for up-to-date compression algorithms.
  - E2fsprogs has been upgraded to version 1.46.0 for CVE patches.
  - Cryptsetup has been upgraded to version 2.3.3 for CVE patches.


### System (Base)

#### New and changed features

- Open Source
  - attr
    - Version 2.4.47 has been upgraded to version 2.4.48.
  - file
    - Version 5.37 has been upgraded to version 5.39.
  - gobject-introspection
    - Version 1.52.1 has been upgraded to version 1.66.0.
  - grpc
    - Version 1.20.1 has been upgraded to version 1.35.0.
  - icu
    - Version 65.1 has been upgraded to version 67.1.
  - json-c
    - Version 0.13.1 has been upgraded to version 0.15.
  - json-glib
    - Version 1.4.4 has been upgraded to version 1.6.0.
  - libarchive
    - Version 3.4.0 has been upgraded to version 3.5.1.
  - libsigc++
    - Version 2.2.11 has been upgraded to version 2.9.3.
  - libxml++
    - Version 2.34.2 has been upgraded to version 2.42.0.
  - libzip
    - Version 1.5.2 has been upgraded to version 1.7.3.
  - ncureses
    - Version 6.1 has been upgraded to version 6.2.
  - pcre
    - Version 8.43 has been upgraded to version 8.44.
  - procps-ng
    - Version 3.3.15 has been upgraded to version 3.3.16.
  - psmisc
    - Version 23.2 has been upgraded to version 23.3.
  - python
    - Version 2.7.17 has been upgraded to version 2.7.18.
  - python-six
    - Version 1.10.0 has been upgraded to version 1.15.0.
  - sqlite
    - Version 3.31.1 has been upgraded to version 3.33.0.
  - tzdata
    - Version 2019c has been upgraded to version 2020a.
  - update-alternatives
    - Version 1.18.15 has been upgraded to version 1.20.5.
  - util-linux
    - Version 2.34 has been upgraded to version 2.36.
  - xz
    - Version 5.2.4 has been upgraded to version 5.2.5.

#### Fixes

- CVE patches
  - file
    - CVE-2019-18218
  - json-c
    - CVE-2020-12762
  - libsigc++
    - CVE-2019-19221
    - CVE-2020-9308


### Application framework

#### New and changed features

- Improvement to get package information logic
  - The architecture has been changed from shared-repo to client-server.
  - Database access concurrency has been improved.
- Widget Component
  - Widget Component has been added to component-based application model.

#### Fixes

- preference
  - Preference API has been refactored.
- rpc-port
  - Memory leak has been fixed.
  - The library has been modified to use proxy API in daemon process.
- pkgmgr-tool
  - The tool has been modified to check backend execution in MIC process.


### Window and Interaction

#### New and changed features

- Open Source upgrade
  - Wayland
    - Version 1.18.0 has been upgraded to version 1.18.92.
  - Libevdev
    - Version 1.8.0 has been upgraded to version 1.10.0.
  - Libinput
    - Version 1.15.0 has been upgraded to version 1.16.
    - Input-haltests has been added for testing input driver(s).
  - Libxkbcommon
    - Libxkbcommon has been upgraded to version 1.0.0.
  - Mtdev
    - Version 1.1.5 has been upgraded to version 1.1.6.
  - NLTK
    - Version 3.2.5 has been upgraded to version 3.4.
  - Mesa
    - Version 19.3 has been upgraded to version 21.0.
- Enlightenment Wayland display server
  - UI and Video Rotation Synchronization has been added. UI surface and Video surface can be updated on a screen at the same time.
  - Hardware Composition based on Atomic Pageflip has been added. This provides the exact time when the pageflip operation has been executed. This feature is available on RPI4 target because it depends on hardware functionality.
  - Display Server with GPU Explicit synchronization has been added. Display Server can control the file descriptors (FD) for the GPU rendering synchronization in order to manage the efficient rendering process. This feature is available on the RPI4 target because it depends on hardware functionality.
- TBM
  - HAL-API-TBM has been added. The libtbm uses HAL-API-TBM instead of loading TBM backend module.
- TDM
  - HAL-API-TDM has been added. The libtdm uses HAL-API-TDM instead of loading TDM backend module.
- TTS Framework
  - New client architecture has been applied.
  - New tolerance architecture has been applied.
  - Partial thread safety in client side has been applied.
  - Support for both TIDL and D-Bus has been added.
- Voice Control Framework
  - New audio streaming architecture has been applied. Shortcut for audio streaming has been added.
- Text Input Framework
  - The API to set the pre-edit cursor position in pre-edit has been added.
  - The API to get input hint such as multiline or singleline has been added.
- Sticker Framework
  - The API to set or get the group image has been added.
  - The API to get the list of group image in a sticker package has been added.

#### Fixes

- TTS Framework
  - Playing TTS bugs have been fixed.
  - Potential deadlock bug has been fixed.
  - TC failure that occurs sometimes has been fixed.
- Voice Control Framework
  - Memory leak has been fixed.


### Graphics and UI

#### New and changed features

- NUI
  - Components
    - CameraView has been added.
    - CanvasView for custom drawing has been added.
    - Navigator, Page, and AppBar have been added.
    - TabView and its related classes, TabBar, TabContent, TabButton, and TabButtonGroup have been added.
    - Dialog and AlertDialog have been added.
    - Picker has been added.
    - CollectionView has been added.
    - ScrollOutOfBound event has been added in ScrollableBase.
  - Common
    - ThemeManager has been added.
    - FrameUpdateCallback has been added.
    - Palette API set has been added.
    - CornerRadiusPolicy has been added in View.
    - TouchArea property has been added in View.
    - ExcludeLayouting has been added in View.
    - Sound Feedback has been added in Control.
    - FontSizeScale property has been added in TextLabel, TextField, and TextEditor.
    - Parse color from Strings (hexCode, RGB, RGBA) has been added.
    - DisallowInterceptTouchEvent which disables the parent view’s touch intercepting has been added.
- DALi
  - Renderer and Animation
    - Support for advanced blending equations has been added.
    - Some View's properties that couldn't be animated can be animated now.
    - Support for RIV format has been added, Rive animation runtime engine has been integrated.
  - Image and Video
    - SVG Raster Engine (NanoSVG) has been replaced with TizenVG (ThorVG).
    - Support for SVG masking and path clipping has been added.
    - Support for synchronization of video players z-order has been added.
  - Components
    - Some WebView API set has been added.
    - Some properties have been added to TextLabel, TextField, and TextEditor.
  - Common
    - Support for MacOS has been added.
    - Memory management has been optimized.
- ThorVG
  -  A New vector graphics engine has been introduced.
- EFL
  - Renderer and Animation
    - Vector Primitive Engine (Ector) has been replaced with TizenVG (ThorVG).
    - Support for WebP Animation has been added.
  - Image and Video
    - Video and UI Sync has been added.
    - Support for APNG Image format has been added.
- Open Source
  - AT-SPI2-ATK
    - Version 2.34.1 has been upgraded to version 2.38.0.
  - AT-SPI2-CORE
    - Version 2.34 has been upgraded to version 2.39.90.
  - Freetype2
    - Version 2.10.1 has been upgraded to version 2.10.4.
  - Fribidi
    - Version 1.0.8 has been upgraded to version 1.0.10.
  - Harfbuzz
    - Version 2.6.4 has been upgraded to version 2.6.7.

#### Fixes

- DALi
  - Some clipping bugs have been fixed.
  - A window resizing bug has been fixed.
  - An image loading state bug has been fixed.
  - Some TextField and TextEditor bugs have been fixed.


### Multimedia framework

#### New and changed features

- Open Source
  - libvorbis
    - Version 1.3.4 has been upgraded to version 1.3.7.
  - libexif
    - Version 0.6.21 has been upgraded to version 0.6.22.
  - alsa-lib
    - Version 1.0.28 has been upgraded to version 1.0.29.
  - libjpeg
    - Version 2.0.4 has been upgraded to version 2.0.6.
  - giflib
    - Version 5.1.9 has been upgraded to version 5.2.1.
  - GraphicsMagick
    - Version 1.3.34 has been upgraded to version 1.3.35.
  - libav
    - The libav has been removed and replaced to FFmpeg.
  - FFmpeg
    - Version 4.3.1 has been added.
- Camera FW
  - New HAL architecture has been applied.
- Media tool
  - New API set for referencing media packet has been added.
- capi-media-vision
  - Barcode Detection
    - Three attributes for images rotation have been added.
      - MV_BARCODE_DETECT_ATTR_ROTATION_DEGREES
      - MV_BARCODE_DETECT_ATTR_ROTATION_COUNT
      - MV_BARCODE_DETECT_ATTR_ROTATION_DIRECTION
    - Enumeration for the direction
      - MV_BARCODE_DETECT_ATTR_ROTATION_CLOCKWISE
      - MV_BARCODE_DETECT_ATTR_ROTATION_COUNTER_CLOCKWISE
      - MV_BARCODE_DETECT_ATTR_ROTATION_ALL
    - One attribute for image enhancement has been added.
      - MV_BARCODE_DETECT_ATTR_USE_ENHANCEMENT
- Media Content
  - New API for getting media handle by path has been added.
- Image Util
  - Support for decoding HEIF (High Efficiency Image Format) has been added.
    - Decode HEIC brand of HEIF

#### Fixes

- Muse server
  - Deadlock problem of signal handler has been fixed by calling malloc of async-signal-safe internally.
- Resource Manager
  - A conflict issue caused by not released resource of the abnormal terminated client has been fixed.
- Media Streamer
  - Custom sink node freeze bug has been fixed.
  - An unexpected error problem with stop() API has been fixed.


### Network and Connectivity

#### New and changed features

- User Awareness API
  - The API set for device has been added.
  - The API set for user has been added.
  - The API set for service has been added.
  - The API set for monitor has been added.
  - Following API set requires the Bluetooth or network privilege as the device type which is monitored by the API:
    - Privilege: `http://tizen.org/privilege/bluetooth` or `http://tizen.org/privilege/network.get`
    - Affected API set
      - ua_monitor_add_sensor
      - ua_monitor_remove_sensor
      - ua_user_add_device
      - ua_user_remove_device
      - ua_device_update
      - ua_monitor_start_scan
      - ua_monitor_stop_scan
      - ua_monitor_start_presence_detection
      - ua_monitor_stop_presence_detection
      - ua_monitor_start_absence_detection
      - ua_monitor_stop_absence_detection
  - Following API set requires the location privilege:
    - Privilege: `http://tizen.org/privilege/location`
    - Affected API set
      - ua_monitor_start_scan
      - ua_monitor_stop_scan
      - ua_monitor_start_presence_detection
      - ua_monitor_stop_presence_detection
      - ua_monitor_start_absence_detection
      - ua_monitor_stop_absence_detection
- Wi-Fi Manager API
  - Wi-Fi connection logic has been optimized for better performance.
- Wi-Fi
  - MAC address randomization has been added.
- Bluetooth Transport Discovery Service (TDS)
  - An application scenario of enabling Wi-Fi Aware using Bluetooth Transport Discovery Service specification has been introduced.
  - Devices which can communicate using Wi-Fi Aware technology, do not need to keep their Wi-Fi Aware interfaces to be activated always. Bluetooth TDS provides a feature of the discovery of available communication technologies between devices.
- Vine
  - Secure simple service discovery and communication framework, a.k.a. Vine has been added.
  - Applications in the same LAN can discover others in a simple way.
  - Applications are able to communicate in secure channel, which is encrypted via TLS.
- Open Source
  - connman has been upgraded to version 1.38.
  - wpa_supplicant has been upgraded to version 2.9.
  - curl has been upgraded to version 7.73.0.
  - c-ares has been upgraded to version 1.17.1.

#### Fixes

- Bluetooth
  - GATT handler bugs have been fixed.
  - The bug of sending response twice has been fixed.
- Network
  - Bugs in wifi-manager API have been fixed.
  - Bugs in ConnMan have been fixed.


### Security

#### New and changed features

- Privileges
  - New privileges have been added.
    - `http://tizen.org/privilege/bugreport.admin`
    - `http://tizen.org/privilege/usb.host`
    - `http://tizen.org/privilege/log`


### Service framework

#### Fixes

- Context Framework
  - Potential issues and memory leaks have been fixed.
- Account Framework
  - Potential issues have been fixed.
- Location Framework
  - Memory leaks have been fixed.
- Sync Manager
  - Potential defects have been fixed.


### Web framework

#### New and changed features

- Web Engine
  - Open Source Chromium 85 version base has been applied. The following features and API set have been provided by the new web engine:
    - Web Animations
      - Support for animation.ready and animation.finished has been added.
      - Smoother animation support with composite mode
    - SameSite Cookies
      - For cookies without specifying a SameSite attribute will be treated as SameSite=Lax by default.
    - WebRTC
      - Support for latest WebRTC features for group calls has been added.
  - Layout engine(LayoutNG) bug fixes and performance enhancement.
  - TLS 1.0 and TLS 1.1 have been deprecated.
- Web Runtime
  - Open Source Electron 10.1.4 version has been applied.
  - Device Home feature has been added. (Experimental)
    - Remote device UI template has been provided.
    - pin-code verification between devices has been provided.
  - Remote Camera feature has been added. (Experimental)
    - Support for getUserMedia() with remote camera of mobile device has been added.

#### Fixes

- Web Engine
  - Known Security vulnerabilities have been fixed.
    - CVE-2020-24977
    - CVE-2020-7754
    - CVE-2016-9909
    - CVE-2020-1971
    - CVE-2020-13790


### Lightweight Web Solution

#### New and changed features

- Rendering engine
  - Some DOM API and Web API set have been added.
    - SVG Element, Image Element, HTMLCollection, Event, File, and Window
- Performance and Memory Optimization
  - Animation Performance has been optimized.
    - Threaded image decoder has been applied for animation optimization.
    - PoolAllocator feature has been added to enhance layout performance.

#### Fixes

- Memory leak bugs have been fixed.
- Crash issues have been fixed.


### Tizen .NET

#### New and changed features

- .NET runtime and tools
  - N/A
- TizenFX
  - Tizen.Applications
    - ComponentPort class has been added.
    - ComponentTask class has been added.
    - RequestEventArg class has been added.
    - IWindowProxy interface has been added.
    - WidgetComponent class has been added.
  - Tizen.Multimedia
    - Landmark struct has been added.
    - PoseLandmarkDetector has been added.
  - Tizen.NUI
    - FontSizeScale struct has been added.
    - RelativeLayout class has been added.
    - RelativeLayout.Alignment enum has been added.
    - ToogleButton class has been removed.
    - Slider class has been removed.
    - ScrollView class has been removed.
    - ScrollBar class has been removed.
    - RadioButton class has been removed.
    - PushButton class has been removed.
    - ProgressBar class has been removed.
    - Popup class has been removed.
    - CheckBoxButton class has been removed.
    - Button class has been removed.
    - WidgetViewSignal class has been removed.
    - KeyBoardTypeSignalType class has been removed.
    - SWIGTYPE_p_bundle class has been removed.
    - PropertyNotifySignal class has been removed.
    - Property class of ItemView, Scorallable, Renderer, and Shader has been removed.
    - LayerBehavior.Layer2D enum has been removed.
    - Shadow class has been added.
    - Theme class has been added.
    - TimePeriod class has been added.
    - Transition class has been added.
    - ControlState class has been added.
    - ViewStyle class has been added.
    - AppBar class has been added.
    - ContentPage class has been added.
    - Navigator class has been added.
    - Page class has been added.
  - Tizen.Security
    - TEEC has been deprecated.
- Xamarin.Forms
  - Xamarin.Forms 5.0.0, which is the latest stable version has been supported.

#### Fixes

- Tizen.Network.Bluetooth
  - Marshaler coverting bugs have been fixed.
  - Null reference bugs have been fixed.


### Toolchain

#### New and changed features

- New architecture(Armv7hl) support
  - GCC: Armv7hl configuration has been newly added for hard float ABI.

#### Fixes

- Gcc/ Libsanitizer
  - SIGSEGV in fopen64 interceptor has been fixed.
- Glibc/ iconvdata (CVE-2019-25013)
  - Buffer overrun in EUC-KR conversion module has been fixed.


### Machine Learning

#### New and changed features

- ML / Web Inference API
  - New API set, Pipeline and Single have been added.
- Machine Learning Inference API update
  - The package name has been changed from capi-nnstreamer to capi-machine-learning-inference. However, this is a platform internal change, and does not affect application developers.
  - The ability to register a tensor_if custom callback function in case the condition of tensor_if becomes complex has been added.
  - The ability to open the model with various custom options such as flexible or fixed input dimensions has been added; for example, ml_single_open_full().
  - The ability to check whether the given element is registered or not has been added.
  - The ability to invoke the model with pre-allocated output buffers, which is generally faster than normal invocation, has been added; for example, ml_single_invoke_fast().
- NNStreamer update
  - NNStreamer has been upgraded from 1.6.0 to 1.7.1.
  - The ability to create conditional branches (tensor_if) based on tensor values has been added. For example, developers may skip frames if there is no object detected with high confidence.
  - The ability to support TensorFlow Lite 2 with GPU and NNAPI delegations along with gRPC/flatbuffer with sync and async mode has been added.
  - The ability to designate priorities between multiple frameworks in case multiple frameworks support the same model file format (for example, TensorFlow-lite’s .tflite format) has been added.
  - The ORC acceleration for tensor manipulation and subplugin auto detection based on the extension of the model file has been added.
  - An ml_nnfw_type_e enumeration has been added to support PyTorch and NNtrainer.
- Machine Learning Training API update
  - Number of ml_train_layer_type_e has been added.
    - ML_TRAIN_LAYER_TYPE_BN
    - ML_TRAIN_LAYER_TYPE_CONV2D
    - ML_TRAIN_LAYER_TYPE_FLATTEN
    - ML_TRAIN_LAYER_TYPE_ACTIVATION
    - ML_TRAIN_LAYER_TYPE_ADDITION
    - ML_TRAIN_LAYER_TYPE_CONCAT
    - ML_TRAIN_LAYER_TYPE_MULTIOUT
- ONE runtime update
  - ONE runtime has been upgraded from 1.9.0 to 1.15.0.
  - ONERT uses ARM Compute Library v21.02.
  - Expanded CPU backend support
    - 16x1 block sparsity support in Float32 FullyConnected operation.
    - Add, AvgPool2d, Concat, Conv2D, DepthToSpace, DepthwiseConv2D, Dequantize, Div, Elu, ExpandDims, LeakRelu, LogicalAnd, Maximum, MaxPool2D, Minimum, Mul, Pad, PadV2, Quantize, Rank, Reshape, Resizebiliear, Shape, Softmax, Squeeze, and Sub support for INT8 quantized model
    - Dequantize, Rank support for UINT8 quantized model
  - Expanded ACL(ARM Compute Library) backend support
    - ArgMin support of both CL and NEON backends for Float32, UINT8, INT8 models
    - ArgMax support of NEON backend for INT8 models
- TensorFlow Lite 2 with GPU Delegate
  - TensorFlow Lite 2 (2.3.0) has been added. The GPU Delegate option has been enabled.
  - To support the backward compatibility of the previous TensorFlow Lite Model, both TensorFlow Lite (1.13) and TensorFlow Lite 2 (2.3.0) have been supported.

#### Fixes

- Machine Learning Inference API
  - The hidden memory issues such as double free, memory leakage, and so on have been fixed.

#### Known Issues

- TensorFlow Lite 2 with GPU Delegation
  - To enable GPU Delegation, installation of the OpenCL library has been required.
