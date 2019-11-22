# Tizen 5.5

The second milestone (M2) of Tizen 5.5 was released (https://docs.tizen.org/platform/release-notes/tizen-5-5-m2) in October 2019.
Tizen is open-source OS maintained by Samsung and developed & optimized for smart devices since 2012.
Currently, more than 130+ million Tizen-based devices are commercialized such as TVs, watches, Family-hubs, IoT based home appliances etc.
(Samsung TVs (2015~), Galaxy Wearables (2014~), Family-Hub Refrigerators (2016~), Smart Signage (2019~), Air Conditioners (2019~), Flip board (2019~) etc.)
The key features of Tizen 5.5 are the enhancement of development environment/core, supporting AI component and the expansion of IoT profile.



![img](media/3.0_introduction_3.png)

## The enhancement of development environment and core component for a Strengthened Application Ecosystem

- **Tizen.NET** is the development environment for developing high quality and high performance application in C#. There is the enhancement in Tizen Development environment in Tizen 5.5.
In Tizen 5.5, the latest Xamarin.Forms 4.0 and the lasted .NET Core 3.0 is supported. Xamarin.Forms on Tizen .NET is the complete cross-platform UI toolkit that allows you to create native UI. The latest .NET Core support unloading DLL and AOT, pre-loading & pre-initialization,Tiered complication, MPGO for enhancing application launching time. There is memory optimization by reducing relocation of DLL file, pre-loading for resource sharing etc.NET Core 3.0 Runtime is faster, lighter than previous version. There was 28% reduction in application launching time and 20% reduction in memory usage.
 New Tizen extension for official visual studio for Mac also is released in Tizen 5.5. The key features of Tizen extension is providing Tizen.NET  Application development environment, Tizen IDE tools  and application debugging using netcore debugger. Log in Mac.

- **Tizen 5.5’s Watchface Complication APIs** provide easier way to create custom complication in watchface. APIs provide various kinds of complication types. Developers can provide various kinds of complication services such as health, battery, air pollution etc. by using APIs.

- **Tizen 5.5 supports Lottie animation**
 Lottie which was named by AirBnB, is library that renders After Effects animations in real time. The lottie file is composed by using JSON format, it contains visual shape information such as rectangle, circle, path and fill methods like the traditional vector graphics elements.
- **Multi-assistant Framework**
Aims to support various AI assistants on the same time for giving a better usability. The framework defines a common interface for making an assistant of multi-assistant framework. And it provides an expandable wake-up engine that recognizes invocation keyword for each assistant and supports to add a new keyword.

- **The multi-device distributed web engine** is designed for both memory resource requirements mitigation and JavaScript execution speed enhancement to overcome the resource constraints of the low-end devices. With the prior multi-process design of the web engine, the memory usage of the renderers becomes significant as multiple tabs are created. CPU resource consumption of the renderer processes is also substantial as web applications get complicated. To manage hardware resources and to make resource usage predictable in low-end devices, the multi-device distributed web engine introduces features for offloading renderer processes over the network to resource-free devices while the browser process runs on the local low-end device.

- **User Awareness Framework**
Smart devices could provide useful services based on the user presence context. Tizen 5.5 supports User Awareness Framework based on multiple sensors. Currently, Wi-Fi, BLE, motion, and light sensors are supported and it could be extended to support other types of sensors based plug-in architecture.


## Intelligent/AI/On Device AI

- **A new Tizen domain, Machine Learning (ML)**, is introduced along with its ML Inference API sets: “Pipeline ML API” and “Single ML API”. ML Inference API sets allows application developers to apply their machine learning mechanisms or neural network models easily and efficiently. Especially if the intelligence application has multiple sensors, multiple neural network models, and complex topology of data paths, Pipeline ML API can help implement the system efficiently with less time and effort. If developers need to use neural network models preloaded with the platform, APIs in Media Vision are appropriate because ML Inference APIs require developers to supply neural network models. In other words, for predefined special functions, Media Vision is appropriate and for general or custom functions, ML Inference is appropriate.
ML API sets are based on NNStreamer (https://github.com/nnsuite/nnstreamer), which allow to construct GStreamer pipelines consisting of conventional GStreamer media plugins and neural network plugins. Although we plan to expand its functionality to on-device training in later releases, ML API sets of the current version of Tizen support machine learning inferences only. In ML API sets, there are two API subsets: Pipeline ML API set and Single ML API set.
Pipeline ML API set allows developers to construct and execute GStreamer pipelines with the conventional GStreamer plugins and neural network plugins provided by NNStreamer. With this API set, developers may construct pipelines with multiple instances of neural network models, input streams, and various stream path manipulators. Note that a few of GStreamer plugins that are white-listed are allowed with Tizen Application APIs; on the other hand, all of NNStreamer plugins are allowed. For input streams, you may use camera, mic, files, or arbitrary inputs from applications. However, your applications need to acquire appropriate privileges for the given inputs. For output streams, you may use files or callback functions of the application.
Single ML API set allows developers to invoke a given neural network model (e.g., .tflite TensorFlow-lite model file) with a single instance of input buffer easily.
In Tizen 5.5, ML API sets allow TensorFlow-lite 1.13 and custom C libraries for model files although NNStreamer itself supports a lot more neural network frameworks (TensorFlow, Caffe2, PyTorch, custom Python codes, Movidius NCSDK, and so on). However, device developers may install such frameworks and enable ML API sets to utilize such frameworks.
- **Media Vision**
Starting with BarCode recognition and generation in Tizen 2.4, detection, recognition and tracking of Face and images have been added to MediaVision. They are based on traditional Computer Vision technology and have been able to guarantee some execution speed on low-end hardware. Recently, the rapid development of AI technology has increased the demand for DNN-based vision technologies, and MediaVision has applied the AI Framework to some of the existing and new functions of MediaVision in response to this trend.
In Tizen 5.5, Application developer can recognize Face and Facial Landmark via Calling MediaVision API which based on AI Framework such as Caffe and TF-Lite. In addition, an interface for image classification and object detection is also provided, and it is supported to use a reference model provided by Tizen or a model trained by developer.

## Building an IoT Device Ecosystem

To build Tizen IoT device ecosystem, Tizen open source project worked closely with partners. Tizen IoT profile supports open hardware platforms such as RPI3 and SDTA7X2. Several IoT Cloud solutions are also integrated in Tizen 5.5. Tizen 5.5 provides IoT headless and IoT Headed profiles based on the building blocks for supporting various purpose devices.
Tizen 5.5 provides IoT total solution of the open hardware platform, platform OS and IoT cloud.


For detail information, see [IoT Partners](https://docs.tizen.org/iot/iot-partners/).
