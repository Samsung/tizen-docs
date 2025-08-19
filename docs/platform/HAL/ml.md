# Machine Learning

HAL (Hardware Abstraction Layer) modules for the Machine Learning framework provide an interface for hardware-accelerated neural network inference.

## ML Hardware Acceleration

At the Hardware Abstraction Layer, the ML acceleration feature handles inference requests from Tizen's [Machine Learning API](../../application/native/guides/machine-learning/overview.md) and delegates them to various hardware acceleration devices.
This HAL is not used directly by application developers; instead, it serves as a backend for NNStreamer.

The process is as follows:
 * An application uses the Tizen ML API.
 * The underlying framework (NNStreamer's tizen-hal tensor_filter subplugin) calls the ML HAL API.
 * The ML HAL API routes the request to a specific HAL ML Accelerator Backend.
 * The backend executes the task on the target device and returns the result.

<img src="media/tizen-hal-ml.png" width=600/>

You may check the HAL usage in the `tensor_filter` implementation [here](https://github.com/nnstreamer/nnstreamer/blob/main/ext/nnstreamer/tensor_filter/tensor_filter_tizen_hal.cc).
