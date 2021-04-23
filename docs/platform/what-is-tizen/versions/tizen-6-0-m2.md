# Tizen 6.0

The second milestone (M2) release of Tizen 6.0 was announced in October 2020.
Tizen is an open-source operating system (OS) maintained by Samsung and is developed and optimized for smart devices since 2012.

The key features of Tizen 6.0 are the enhancement of development environment, core and AI component.

## Enhancement of Development Environment and Core Component

### Tizen.NET

Tizen builds a C# application development environment based on .NET Core, an open source .NET platform, for app development productivity.
To provide and further refine. Offers the latest .NETCore 3.1 and the latest version of cross-platform Xamarin,

In particular, the application start-up time and memory retention are minimal compared to the previous one by utilizing the biography-based dictionary function, etc.
Reduction by more than 15%. In addition, when developing an app, so that you can check UI changes without additional build modification,
XAML Hot Reload beta service is supported.

- **.NET Core** :
Latest .NET Core 3.1(LTS)
Optimized performance
Diagnostics tools

- **TizenFX** :
Tizen platform-specific API set
API level 8 Released

- **Xamarin** :
Latest Xamarin.Forms (4.8.0) & Xamarin.Essentials (1.5.3) are available.
TV UI Controls & CircularUI : New UI controls for Smart TVs and Smart Watches.
XAML Hot Reload : Boosting Developer productivity



### Web framework

Tizen 6.0 provides a new user experience through device-to-device connectivity and interworking.

- Web-based device various offloading services

Tizen 6.0 provides a variety of multi-device offloading services using web technology.
As web technology advances and the complexity of applications such as A.I and AR/VR increases, maximization of computational performance within web contents,
There is a need to utilize various terminal resources (hardware) such as sensors.


### Lightweight Web Solution

Escargot provides Web contents in products with HW Resource restrictions such as home appliances.
Compared to Chrome's V8 JavaScript engine, it is about 14%, and memory is only used about 35% based on the benchmark app.
It supports ES6 full spec and supports up to a large part of ES 10.

- **Lightweight JavaScript engine (ESCARGOT)** in https://github.com/Samsung/excargot

  - Memory size  (vs chrome v8) octane benchmark in Ubuntu 18.04
    - Binary size : 13.7 %
    - Average RSS : 35.1 %

  - Features
    - Support ES6 Full feature and partial support of ES10

## AI Integrated Intelligent Platform

Tizen is trying to evolve into an AI integratred platform.

NNSteamer is an on-device AI FW that makes it easy to configure complex artificial neural networks in apps by making artificial neural network configurations with Gstreamer's stream filter plugin.

In this 6.0, NN Runtime support such as Control-flow and Dynamic Tensor has been added to support voice model acceleration. In addition, by providing the NN Compiler front-end for NN Runtime, it converts well-known ML framework-based models such as Tensorflow and tensorflow-lite so that they can be used on CE devices with insufficient resources (on NNRuntime).

- NNStreamer
  - Neural Network Pipeline
    - .NET and C APIs supported.
    - Various NPU hardware supported.
    - Basic EDGE-AI functions.
  - Implement AI app more easily
  - Execute AI app more efficiently

- NNTrainer
  - On-Device Training
    - Transfer learning, meta learning, reinforcement learning
    - APIs to construct and update (learn!) neural network layers

- NN Runtime
  - Tizen’s default Neural Network inference framework (since v5.0)
  - CPU+GPU mixed acceleration with profiling based optimal scheduling (since v5.5)
  - Useful features for speech model support (in v6.0)
    - Control-flow, Dynamic Tensor, Shape Inference, etc.

- NN Compiler in Tizen SDK
  - Support well known ML frameworks, and model formats
    - Tensorflow, Tensorflow-lite (preferential), Caffe, ONNX (experimental)
  - Easy scalability through Common IR and NN Package    


### Core and Kernel
 - TIDL Extension, Multi-package installeration supported in Application framework
 - Gesture FW and engine supported in Window and Interaction frameworks
 - DALi (3D UI Toolkit) API set of DALi has been deprecated. DALi API set has been replaced with NUI (DALi C# layer) in Graphics frameworks
 - Ultra wideband (UWB) ranging, Wi-Fi multiple interface supported in Network and Connectivity framework.
 - Kernel for Raspberry Pi 4 has been upgraded to version 5.4.50.
 - 64Bit Kernel and Boot for Raspberry Pi 4 has been supported.
 - etc.

For more information, see [release note](../../release-notes/tizen-6-0-m2.md).
