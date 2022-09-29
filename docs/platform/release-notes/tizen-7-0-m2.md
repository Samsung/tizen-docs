# Tizen 7.0 Public M2

Release date: Oct. 31, 2022


## Release notes

### System (kernel and system framework)

#### New and changed features

- Kernel feature
  - kfence, a sampling-based memory errobluer detector, support with CONFIG_KFENCE on Raspberry Pi 4
- Resource Monitor
  - Unified resource monitor framework and capi-system-resource-monitor have been added to monitor the various resource status.
  - Web-based resource viewer has been added to monitor the whole resource status of Tizen device.
- Dlog
  - Zero-copy buffer technique has been developed in order to reduce the printing overhead of log.
- Lightweight Multi-user session support
  - Lightweight multi-user session based on sub-session has been developed.
  - Directory and file protection of users has been developed.
  - Memory usage and user switching latency have been optimized.
- Device and sensor management
  - Power state transition callbacks have been developed such as sleep, reboot, poweroff and so on.
  - Delay function of power transition according to user requirement has been developed.
- Resource management
  - CPU boosting and inheritance C API have been developed and optimized.
  - CPU boosting C# API has been developed for dotnet app boosting.
  - Socket activation for on-demand CPU boosting has been supported.

#### Fixes

- Sensor management
  - Gyroscope rotation vector sensor and gyroscope orientation sensor have been initialized to prevent the wrong operation.


### System (system reliability and OS upgrade)

#### New and changed features

- OS Upgrade and System Recovery
  - OS upgrade with A/B Partition has been developed to prevent unexpected FOTA failure.
  - OS Upgrade fatal error detection and recovery have been developed.


### System (base)

#### New and changed features

- Open source
  - gpg2
    - Version 2.0.26 has been upgraded to version 2.3.7.
    - CVE-2019-13050, CVE-2019-14855, CVE-2022-34903
  - libzip
    - Version 1.8.0 has been upgraded to version 1.9.2.
  - libxml2
    - Version 2.9.12 has been upgraded to version 2.10.2.
  - libxml2
    - Version 2.9.12 has been upgraded to version 2.10.2.
    - CVE-2022-23308, CVE-2022-29824
  - libxslt
    - Version 1.1.34 has been upgraded to version 1.1.37.
  - npth
    - Version 1.6 has been added.
  - python-libxml2
    - Version 2.9.12 has been upgraded to version 2.10.2.
  - python3-appdirs
    - Version 1.4.0 has been upgraded to version 1.4.4.
  - python3-cairo
    - Version 1.17.1 has been upgraded to version 1.19.1.
  - python3-Cheetah
    - Version 3.2.4 has been upgraded to version 3.2.7b1.
  - python3-cython
    - Version 0.29.21 has been upgraded to version 0.29.30.
  - python3-gobject
    - Version 3.38.0 has been upgraded to version 3.40.1.
  - python3-lxml
    - Version 4.6.2 has been upgraded to version 4.9.1.
  - python3-mako
    - Version 1.0.6 has been upgraded to version 1.2.1.
  - python3-MarkupSafe
    - Version 1.1.1 has been upgraded to version 2.1.1.
  - python3-numpy
    - Version 1.19.4 has been upgraded to version 1.23.1.
  - python3-packaging
    - Version 20.8 has been upgraded to version 21.3.
  - python3-pbr
    - Version 5.5.1 has been upgraded to version 5.9.0.
  - python3-pygments
    - Version 2.7.3 has been upgraded to version 2.12.0.
  - python3-pyparsing
    - Version 2.2.0 has been upgraded to version 3.0.7.
  - python3-setuptools
    - Version 50.3.1 has been upgraded to version 63.2.0.
  - python3-six
    - Version 1.15.0 has been upgraded to version 1.16.0.
  - python3-sqlite
    - Version 0.4.2 has been upgraded to version 0.4.7.
  - python3-libxml2
    - Version 2.9.12 has been upgraded to version 2.10.2.
  - Perl-Error
    - Version 0.17017 has been upgraded to version 0.17029.
  - Perl-gettext
    - Version 1.05 has been upgraded to version 1.07.
  - Perl-HTML-Parser
    - Version 3.69 has been upgraded to version 3.78.
  - Perl-json
    - Version 4.02 has been upgraded to version 4.03.
  - Perl-libwww-perl
    - Version 5.836 has been upgraded to version 6.56.
  - Perl-Net-DBus
    - Version 1.0.0 has been upgraded to version 1.2.0.
  - Perl-Pod-Coverage
    - Version 0.22 has been upgraded to version 0.23.
  - Perl-Switch
    - Version 2.16 has been upgraded to version 2.17.
  - Perl-Test-Pod
    - Version 1.45 has been upgraded to version 1.52.
  - Perl-Test-Pod-Coverage
    - Version 1.08 has been upgraded to version 1.10.
  - Perl-URI
    - Version 1.6 has been upgraded to version 5.12.
  - Perl-XML-Parser
    - Version 2.41 has been upgraded to version 2.46.
  - Perl-XML-Simple
    - Version 2.18 has been upgraded to version 2.25.
  - Perl-XML-Twig
    - Version 3.39 has been upgraded to version 3.52.
  - Perl-YAML
    - Version 0.84 has been upgraded to version 1.3.
  - sqlite2
    - Version 3.37.2 has been upgraded to version 3.39.0.
  - wdiff
    - Version 1.1.2 has been upgraded to version 1.2.2.
  - Yaml-cpp
    - Version 0.7.0 has been added.


### Application framework

#### New and changed features

- TIDL
  - TIDL compiler extension for MQTT plugin
    - The TIDL compiler has been updated to generate code that uses the MQTT protocol.
  - Dart programming language support
    - The TIDL compiler has been updated to generate code that uses the Dart programming language.
- Light multi-user system
  - Cross-user sandboxing has been added.

#### Fixes

- Parcel
  - Insert performance has been improved.


### Window and interaction

#### New and changed features

- Text Input Framework
  - The class and APIs related to ElmSharp have been deprecated.
  - The feature of NUI IME has been improved.
    - The UI performance of NUI Reference IME has been improved.
    - Emoticon layout has been supported.
  - Separates the Setting application from NUI IME to launch it directly by system keyboard setting application.
  - Keyboard setting application has been implemented as NUI.
  - Key code has been provided when pressing or releasing IME key.
- Autofill
  - Autofill setting application has been implemented as NUI.
- Multi Assistant
  - The new API for sending wakeup word has been added.
  - The new API for getting whether the voice assistant is enabled.
  - The memory usage of multi assistant has been reduced by not loading unnecessary wakeup engine.
- TTS Framework
  - The C API to provide the activated mode among default, screen reader, notification and etc. to the TTS engine has been added.
  - The C/C# API to provide TTS service states such as ready, synthesizing, and playing to TTS clients has been added.
- Voice Control Framework
  - The IPC interface between the voice-control engine and voice-control clients has been changed from D-Bus to TIDL, which is a proper IPC method between applications.
  - The C API to reduce background volume when the voice manager client wants has been added.
- Multi-Modal Framework
  - The new voice-touch feature has been added.
    - The screen analyzer as one of the input modalities has been added.
    - The voice recognition input modality has been added.
    - IU (Intent Understanding) Module for the voice touch has been enhanced.
    - Always listening mode has been supported.
- Enlightenment
  - The ratio-fit resize has been added. It provides that a window can be resized with a ratio-fit value.
  - The done event for interactive move and resize has been added. A wayland client can know when the interactive move and resize has been done.

#### Fixes

- Enlightenment
  - Several issues on Drag and Drop have been fixed.
    - An issue of hiding a dragged window intermediately has been fixed.
    - An issue of misusing a hash function has been fixed.
    - An issue of sending a drop event when the drop is cancelled has been fixed.


### Graphics and UI

#### New and changed features

- Rendering
  - Support for a dedicated UI thread has been added.
  - Support for EGL_EXT_image_dma_buf_import has been added.
- Scene3D
  - Tizen.NUI.Scene3D namespace has been added.
  - SceneView and Model have been added.
  - Support for facial animation has been added.
  - Support for cubemap images has been added.
  - BVH loader has been added.
- View
  - Various properties about touch and key event have been added.
- Input and Gesture
  - Pan gesture behavior has been optimized.
- Images
  - Support for Lottie dynamic properties has been added.
  - Support for asynchronous svg file loading has been added.
  - Support for asynchronous Lottie file loading has been added.
  - Support for GPU alpha masking has been added.
- Performance Improvement
  - Some image operations have been optimized.
  - Texture cache logic has been optimized.
  - Building time of a uniform map has been decreased.
  - Signal connection time has been decreased.
  - Vector operation time has been decreased.
  - Text rendering time has been decreased.
- Rive-Tizen
  - rive-cpp code base to support rive 2.0 API has been updated.
  - Skia based animation renderer has been introduced.
- EFL
  - Webp animation memory usage has been optimized.
  - Stability has been improved.
- Aurum
  - Support for intelligent UI Automation has been added.
  - Support for the repeated key event has been added.
  - Support for the interface to get Text minimum rectangle has been added.
  - Support to get window information from display server has been added.
  - The performance key event response time has been improved.
  - Support for the interface to get object information with specific area has been added..
  - Support to get Process ID from AT-SPI has been added.
- UI Analyzer
  - Support for query function of the focusable object has been added.
- Accessibility
  - ATSPI support for embedded UIs in NUI/DALi (widget applications, web content).
  - New reading UX in screen-reader
  - New property in NUI/DALI to support automation: DevelControl::Property::AUTOMATION_ID
  - New NUI API for accessibility attributes: View.AccessibilityAttributes
  - Registration of full EFL setting application package name in the AT-SPI registry.
- Figma
  - Support for converting Figma to xaml has been added.
  - Figma plugin : `https://github.com/nui-dali/FigmaToNUIXaml`
- Components
  - Support for drag and drop between applications has been added.

#### Fixes

- Various partial update defects have been fixed.
- Visual defect of scrolling text has been fixed.
- Various text defects have been fixed.
- Various ATSPI defects have been fixed.
- Various Aurum and UI analyzer defects have been fixed.


### Multimedia framework

#### New and changed features

- MediaVision
  - On-Device learning based Face Recognition API.
    - Support for face registration in runtime has been added.
    - Support for face unregistration in runtime has been added.
    - Support for face recognition in runtime has been added.
  - 3D API set has been added.
    - Support for Depth process based on Stereo has been added.
    - Support for PointCloud process has been added.
  - Region-of-Interest Tracker set has been added.
- Native WebRTC
  - Encoder bitrate APIs for video source have been added.
  - Transceiver codec APIs have been added.
  - NULL source type for recvonly direction has been added.
  - File path and looping APIs for media file source have been added.
  - Device id APIs for camera source have been added.
  - Support for AEC of microphone source has been added.
  - Support for YV12 format to render video frame has been added.
  - MediaScreenSource APIs have been changed to platform privilege.
  - DataChannel BufferedAmount C# APIs have been added.
  - Statistics C# APIs have been added.
- Sound Manager
  - Deprecated APIs since Tizen 4.0 have been removed.
- Media Streamer
  - All APIs have been deprecated.
- Media Content
  - Pinyin filter keywords have been deprecated.
  - CreateThumbnail C# API has been added and CreateThumbnailAsync C# API has been deprecated.
- Media Camera
  - APIs for network camera and extra stream preview have been added.
- Media Common
  - Memory leak detector feature has been added.
  - The new MediaPacket constructor based on ref count has been added.
  - The Display APIs for ElmSharp have been deprecated.
- Media Util
  - ThumbnailExtractor ExtractAsync has been deprecated.

#### Fixes

- Native WebRTC
  - Validation of STUN/TURN server URL has been improved.
  - Data type of 'packets-lost' issue has been fixed.
  - OPUS channel information has been added to rtpmap attribute of SDP description to comply with Web API.
  - Default resolution for screen source has been fixed to use the display resolution of a target device.
  - An invalid mute operation of camera source not using Tizen memory has been fixed.
- Media Common
  - Daemon launching failure issue related with display service has been resolved.
  - Deadlock issue by non thread safe cynara API has been resolved.
  - Player data thread memory issue (heap-use-after-free) has been resolved.
- Media Camera
  - The C# crash issue in RPI 64bit system has been fixed.
    - Changed bool to byte in EncodedPlane internally for 64bit union struct marshaling


### Network and connectivity

#### New and changed features

- Wi-Fi
  - New features for Wi-Fi roaming have been added.
    - IEEE 802.11 k feature has been added for scanning nearby Aps quickly.
    - IEEE 802.11 r feature has been added for authenticating quickly while roaming.
    - IEEE 802.11 v feature has been added for triggering roaming from the infrastructure AP based on the network status.
- Network
  - New APIs for browsing and resolving remote services have been added.
  - New APIs for getting extra AP information have been added.
  - New API for BSS entries from the cache has been added.
  - New enum for association failure has been added.
  - H2E (Hash-To-Element) feature for WPA (Wi-Fi Protected Access) has been added.

#### Fixes

- Bluetooth
  - The UUID generating logic for mesh profile has been added.
  - The data sending issue on LE CoC has been fixed.
  - The wrong operation about same GATT services and descriptors has been fixed.
- Network
  - The time issue about network information change has been fixed.
  - The issue about BSS (Basic Service Set) transition has been fixed.


### Service framework

#### Fixes

- Account Framework
  - Potential defects have been fixed.
- Sync-Manager
  - Potential defects have been fixed.
- Location Framework
  - Potential defects have been fixed.
- Messaging Framework
  - Potential defects have been fixed.


### Web framework

#### New and changed features

- Web Engine
  - Tizen.WebView C# API has been deprecated.
  - Resource size (content_shell.pak) has been optimized.
  - Launching performance and memory have been improved.
- Web Runtime
  - Open source Node.js 14.15.4 version has been applied.

#### Fixes

- Web Engine
  - Accessibility defects have been fixed.
  - NUI WebView related defects have been fixed.
  - ewk_view_scroll_by defect has been fixed.


### Lightweight web solution

#### New and changed features

- Lightweight Web Engine
  - Web Engine
    - CSS SVGRadialGradientElement has been added.
  - Javascript Engine
    - Private instance fields/methods of class have been added.
    - Top-level await feature has been added.
    - RegExp match indeces has been added.
- JS based lightweight backend service FW
  - Lightweight Node.js
    - Tizen device API module has been added.
    - Binding Glib message queue has been added.
    - Memory tracing APIs have been added.
    - App templates for RPMs and TPKs have been added.
    - Preliminary Javascript debugging via VS code has been added.

#### Fixes

- Lightweight Web Engine
  - SVG defects have been fixed.
  - Flex layout defects have been fixed.
  - Animated gif defects have been fixed.
- Lightweight Node.js
  - Visualizing stack traces has been fixed.
  - Thread-safety defects have been fixed.
  - App Template defects have been fixed.


### Tizen .NET

#### New and changed features

- .NET
  - .NET Multi-platform App UI (MAUI)
    - .NET MAUI General Availability (GA) has been supported.
  - TizenFx
    - Non-intuitive key focus events of Tizen.NUI have been deprecated.
    - IsLooping method has been added to MediaFileSource class.
    - New construct has been added to MediaPacket class.
    - Encoder/Decoder for Jpeg XL image have been added to Tizen.Multimedia.Util.
    - VideoFrameRate and BundlePolicy have been added to Tizen.Multimedia.Remoting.
    - Route table method has been added to Tizen.Network.Connection.
    - Tizen.MachineLearning.Train has been added.
    - An exception has been added to ImageTrackingModel class.
    - Tizen.Multimedia.StreamRecorder has been deprecated.
    - Model class has been added to Tizen.NUI.Scene3D.
    - Service state information method has been added to Tizen.Uix.Tts.
    - Some utility methods have been added to CameraDeviceManager class.
    - WebRTC statistics method has been added to Tizen.Multimedia.Remoting.
    - TransceiverCodec has been added to Tizen.Multimedia.Remoting.
    - Unused Camera class and CameraType of NUI have been deprecated.
    - Deep learning face recognition has been added to Tizen.Multimedia.Vision.
    - ROI tracker has been added to Tizen.Multimedia.vision.
    - CameraDeviceId and EncoderBitrate have been added to Tizen.Multimedia.Remoting.
    - CreateThumbnail has been added to Tizen.Content.MediaContent.
    - ElmSharp and related constructors have been deprecated.
    - ExtractAsync of ThumbnailExtractor class has been deprecated.
    - Deprecated method of AudioManager has been removed.
    - Tizen.WebView has been deprecated.
    - EncodedPlane has been added to Tizen.Multimedia Camera.
    - Camera and SceneView class has been added to Tizen.NUI.Scene3D.
    - Privilege level of MediaScreenSource class has been changed from public to platform.


### Toolchain

#### New and changed features

- GCC
  - Timezone data has been updated to tzcode 2020a.

#### Fixes

- GCC
  - C++ bugfix patches have been applied (PR c++/61414).
  - Memcmp bugfix patches have been applied (PR middle-end/95189, 95886).
- Glibc
  - TLS(Thread Local Storage) bugfix patches have been applied (BZ #25051).


### Machine learning

#### New and changed features

- Machine Learning (ML) API updates
  - ML.Service API Updates
    - Home Edge-AI and Among-Device AI support: applications may register and deploy AI service modules, which can be accessed by other applications in the device or connected devices. Such edge-AI or among-device AI capability is provided by the API set to launch / start / stop / destroy the AI pipeline descriptions, which has been newly added. Developers may provide the specific inference operations as ML service and other applications may use this service via the network. Note that this capability is compatible with SmartThings and Matter via AITT module and devices without nnstreamer (e.g., TizenRT) can be potentially connected by adopting nnstreamer-edge library.
    - API set to create / request the query service to the ML service instance has been newly added. Applications may create the query for inference offloading and request it to the ML service instance with its data.
  - ML.Inference API Updates
    - API set to set / destroy the ML options has been newly added. Developers may use this API to set the various option of the deep neural network framework.
    - Version 2.8.1 of TensorFlow Lite has been supported as default.
  - ML.Training API Updates
    - Added New Enumerations for layers
      - ML_TRAIN_LAYER_TYPE_ATTENTION
      - ML_TRAIN_LAYER_TYPE_MOL_ATTENTION
      - ML_TRAIN_LAYER_TYPE_LAYER_NORMALIZATION
      - ML_TRAIN_LAYER_TYPE_POSITIONAL_ENCODING
    - .NET API has been added. Now, It is possible to construct, control, and train a machine learning model in Tizen device with Tizen.ManchineLearning.Trainng .NET Class.
      - It provides :
        - Tizen.MachineLeanring.Train.Model
        - Tizen.MachineLearning.Train.Layer
        - Tizen.MachineLearning.Train.Optimizer
        - Tizen.MachineLearning.Train.Dataset
        - And more.
    - Training API in WebAPIs has been added for creation and training new models for machine learning on Tizen.
      - It contains:
        - Layer creattionLayer(LayterType type);
        - Dataset createFileDataset()
        - Layer createOptimizer()
        - Model createModelWithConfiguration()
        - Model createMode()
        - And more.
- NNStreamer updates
  - NNStreamer has been upgraded to version 2.2.
  - New tensor stream type, Float16, has been added.
  - Edge AI functionality has been added.
    - nnstreamer-edge package has been newly added. It provides interfaces to support data connection and AI offloading feature between edge devices.
    - NNStreamer and related plugins now support distributed AI inference by using the interfaces for edge AI.
  - User customized tensorflow2-lite of tensor filter has been supported. Developers may designate user-supplied tf2-lite instead of the default one.
  - Apache MXNet filter has been newly added.
  - NXP DeepViewRT filter has been newly added.
  - PyTorch has been upgraded to version 1.10.2.
  - Error messages, exception handling, and documentation have been improved for application / pipeline writers.
  - The Rank limit of tensor stream has been increased from 4 to 8. (Experimental)
  - edgesrc / edgesink element newly added to support publish-subscribe communication. (Experimental)
- NNTrainer updates
  - New layers to support advanced training methods have been added.
    - Attention, MoL Attention, Multi-Head Attention Layer
    - Positional Encoding Layer
    - Layer Normalization Layer
  - Support for Transformer with Multi-Head Attention Layer has been added.
  - Memory Optimization Scheme has been improved.
    - Refactoring Memory Scheduler, Memory Pool, Tensor Pool for better Performance
    - Consume only 1/3.9 Peak Memory of TFLite v2.9 for VGG Model with better Latency (1/1.49)
  - Experimental Features (Turned off by Default)
    - Support for Batch-wise Parallelization has been added.
    - Support for Learning Rate Scheduling has been added.
    - Support for Leaky Relu Layer has been added.
    - Tensorflow-lite Exporter
    - Support for Gradient Clipping by Global Norm has been added.
    - Scheduled memory swapping to further minimize peak memory consumption, which reduces the peak down to 1/4 of the conventional nntrainer.
- Neural Network Runtime
  - Runtime has been supported to run nnpackage with multiple models.
  - Conv2D and Depthwise Conv2D support per-channel quantization of uint8 type.
  - TRIX backend supports batch execution which run in parallel with multicore.

#### Fixes

- NNStreamer
  - Several workarounds have been added for glitches in Qualcomm-SNPE's libraries.

#### Known Issues

- NNStreamer
  - Python2 filter has been removed. Only Python3 is supported.
  - Converter and decoder with Python3 codes do not support multi-thread methods. However, multithreading in Python3 filters are now supported.
- NNTrainer
  - Further memory saving with swapping is experimental and it does not support multi-threaded training.
