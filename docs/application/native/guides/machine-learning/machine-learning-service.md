# Machine Learning Service

The Machine Learning Service API provides utility interfaces for both AI developers and application developers. AI developers can provide their pipelines as ML services, and application developers can use these services via the network.

The main features of the Machine Learning Service API include the following:

- Providing AI pipelines as ML services via machine-learning-agent (daemon).

  AI developers can manage their AI pipeline description with a unique name. Then they can launch the pipeline as an ML service.

- Using launched ML services via the network.

  Application developers can request their data to be processed by the launched ML service. The communication is powered by [NNStreamer's tensor_query](https://nnstreamer.github.io/gst/nnstreamer/tensor_query/README.html), which implements [Edge-AI](https://nnstreamer.github.io/edge-ai.html) functionality.

## Prerequisites

Follow the steps below to enable your application to use Machine Learning Service API:

1. To use the functions and data types of the Machine Learning Service API, include the `<ml-api-service.h>` header file in your application:

   ```c
   #include <ml-api-service.h>
   ```

2. To use the Machine Learning Service API, include the following features in your `tizen-manifest.xml` file:

   ```xml
   <feature name="http://tizen.org/feature/machine_learning">true</feature>
   <feature name="http://tizen.org/feature/machine_learning.service">true</feature>
   ```

## An example of object detection with Machine Learning Service API

Let's say some AI developers want to provide an object detection service. The ML service takes an image data from other applications, and give back the image with bounding boxes drawn on it. An example pipeline can be described as this:

```text
tensor_query_serversrc port=#reserved_appointed_port_number host=localhost connect-type=TCP !
other/tensors,num_tensors=1,types=uint8,format=static,dimensions=3:320:320:1,framerate=0/1 !
tensor_transform mode=arithmetic option=typecast:float32,add:0.0,div:255.0 !
queue ! tensor_filter framework=tensorflow2-lite model=/path/to/yolov5s/model/file.tflite !
other/tensors,num_tensors=1,types=float32,format=static,dimensions=85:6300:1:1,framerate=0/1 !
tensor_decoder mode=bounding_boxes option1=yolov5 option2=/path/to/coco/label.txt option4=320:320 option5=320:320 !
video/x-raw,format=RGBA,width=320,height=320 ! tensor_converter !
other/tensors,format=static,num_tensors=1,dimensions=4:320:320:1,types=uint8 !
tensor_query_serversink async=false sync=false
```

The pipeline expects a 320x320 RGB raw image as input, and pre-process it to invoke the yolov5s tflite model. The inference result is decoded to bounding box image with tensor_decoder. The service provider can upgrade their internal neural network without changing the code of the client if input and output layout is preserved.

Clients who want to use this service may use their own pipeline communicating with the service, or can use the Machine Learning Service API, which is more easy to use.

The following code snippet shows an example of how the Machine Learning Service API can be used in this scenario. Note that checking return value and error handling is omitted for brevity.

### AI developers launching the object detection ML service

AI developers can manage the pipeline description by doing the following:

1. Set the pipeline description with a service name "object_detection_service":

    ```c
    const gchar object_detection_pipeline[] = "\
    tensor_query_serversrc port=#reserved_port_number host=localhost ! \
    other/tensors,num_tensors=1,types=uint8,format=static,dimensions=3:320:320:1,framerate=0/1 ! \
    tensor_transform mode=arithmetic option=typecast:float32,add:0.0,div:255.0 ! \
    queue ! tensor_filter framework=tensorflow2-lite model=/path/to/yolov5s/model/file.tflite ! \
    other/tensors,num_tensors=1,types=float32,format=static,dimensions=85:6300:1:1,framerate=0/1 ! \
    tensor_decoder mode=bounding_boxes option1=yolov5 option2=/path/to/coco/label.txt option4=320:320 option5=320:320 ! \
    video/x-raw,format=RGBA,width=320,height=320 ! tensor_converter ! \
    other/tensors,format=static,num_tensors=1,dimensions=4:320:320:1,types=uint8 ! \
    tensor_query_serversink async=false sync=false";

    // Set the pipeline with service name.
    ml_service_set_pipeline ("object_detection_service", object_detection_pipeline);
    ```

2. Get or delete the pipeline description of the service name:

    ```c
    // Get the pipeline description of given service name.
    gchar *pipeline;
    ml_service_get_pipeline ("object_detection_service", &pipeline);

    // Delete the pipeline description of given service.
    ml_service_delete_pipeline ("object_detection_service");
    ```

AI developers can manage the ML service doing the following:.

1. Launch and start the service:

    ```c
    // Launch the given service. Proper pipeline description is should be set beforehand.
    ml_service_h object_detection_service_h;
    ml_service_launch_pipeline ("object_detection_service", object_detection_service_h);

    // Start the given service. Clients can use this service when the pipeline is in playing state.
    ml_service_start_pipeline (object_detection_service_h);
    ```

2. Stop, destroy or get the pipeline state:

    ```c
    // Get the state of given service.
    ml_pipeline_state_e state;
    ml_service_get_pipeline_state (object_detection_service_h, &state);

    // Stop the given service.
    ml_service_stop_pipeline (object_detection_service_h);

    // Destroy the given service.
    ml_service_destroy (object_detection_service_h);
    ```

### Application developers using the service

Clients (application developers) can use services with the Machine Learning Service API exploiting NNStreamer's tensor_query feature They can do this by using the following steps:.

1. Create the query client with ml_option:

    Set the configuration of tensor_query_client with ml_option. Refer [tensor_query_client](https://nnstreamer.github.io/gst/nnstreamer/tensor_query/README.html#tensor_query_client) for details.

    ```c
    // Create ml_option.
    ml_service_h client;
    ml_option_create (&query_client_option);

    // Set the "port" value to be some available port.
    guint client_port = #available_port;
    ml_option_set (query_client_option, "port", &client_port, NULL);

    gchar *dest_host = g_strdup ("localhost");
    ml_option_set (query_client_option, "dest-host", dest_host, g_free);

    // Set the "dest-port" value to be the port of object detection service.
    guint dest_port = #reserved_service_port_number;
    ml_option_set (query_client_option, "dest-port", &dest_port, NULL);

    // Set the "connect-type" value to be "TCP".
    gchar *connect_type = g_strdup ("TCP");
    ml_option_set (query_client_option, "connect-type", connect_type, g_free);

    // Set the "timeout" value to be 30 sec.
    guint timeout = 30 * 1000U; /* 30 sec */
    ml_option_set (query_client_option, "timeout", &timeout, NULL);

    // Set the "caps" value to be the string that object detection service requires.
    gchar *caps_str = g_strdup ("other/tensors,num_tensors=1,format=static,types=uint8,dimensions=3:320:320:1,framerate=0/1");
    ml_option_set (query_client_option, "caps", caps_str, g_free);

    // Create the query client with given ml_option.
    ml_option_h query_client_option = NULL;
    ml_service_query_create (query_client_option, &client);
    ```

2. Request data to be processed by the launched ML service:

    ```c
    // Set input tensors info.
    ml_tensors_info_h in_info;
    ml_tensor_dimension in_dim;
    ml_tensors_data_h input;

    ml_tensors_info_create (&in_info);
    in_dim[0] = 3;
    in_dim[1] = 320;
    in_dim[2] = 320;
    in_dim[3] = 1;

    ml_tensors_info_set_count (in_info, 1);
    ml_tensors_info_set_tensor_type (in_info, 0, ML_TENSOR_TYPE_UINT8);
    ml_tensors_info_set_tensor_dimension (in_info, 0, in_dim);
    ml_tensors_data_create (in_info, &input);

    // Set input data.
    uint8_t *input_data;
    size_t input_data_size;

    // Fill the input data with application data.

    ml_tensors_data_set_tensor_data (input, 0, &input_data, input_data_size);

    // Request the input data and get output from the service.
    ml_tensors_data_h output;
    ml_service_query_request (client, input, &output);

    // Use the received data in the application.
    uint8_t *received;
    size_t output_data_size;
    ml_tensors_data_get_tensor_data (output, 0, (void **) &received, &output_data_size);

    // Destroy the used data
    ml_tensors_data_destroy (output);
    ```

## Related information

- Dependencies
  - Tizen 7.0 and Higher for Mobile
  - Tizen 7.0 and Higher for Wearable
  - Tizen 7.0 and Higher for TV
  - Tizen 7.0 and Higher for IoT
