# Machine Learning Service

The Machine Learning Service API provides utility interfaces for both AI developers and application developers. AI developers can provide their pipelines, models, and resources as ML services, and application developers can use these services via this API.

The main features of the Machine Learning Service API include the following:

- Provide AI pipelines, models, and resources as ML services via machine learning agent.

  AI developers can manage their AI pipeline description with a unique name. Then they can launch the pipeline as an ML service. They also provide their model files or resources (images, audio samples, etc.) with a unique name. Application developers can access and use these models or resources.

- APIs for [pipeline](#machine-learning-service-api-for-pipeline), [model](#machine-learning-service-api-for-model), and [resource](#machine-learning-service-api-for-resource).

  There are three types of Machine Learning Service API - for pipeline, for model, and for resource.

  1. With Machine Learning Service API for pipeline, application developers can request their data to be processed by the launched ML service. The communication is powered by [NNStreamer's tensor_query](https://nnstreamer.github.io/gst/nnstreamer/tensor_query/README.html){:target="_blank"}, which implements [Edge-AI](https://nnstreamer.github.io/edge-ai.html){:target="_blank"} functionality.

  2. With Machine Learning Service API for model, application developers can get a registered model with a paired unique name. Then they may use it in their inference or train scenario. When AI developers upgrade the model, the application still behaves correctly in its scenario without any change to the application's code, unless the layout of the model is changed.

  3. With Machine Learning Service API for resource, developers can share a set of resource files with a unique name. The resource files can be images, audio samples, binary, or any other data files. Developers can get the set of resources with the unique name and may use them in their AI inference or training scenario.

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

## Machine Learning Service API for pipeline

Let's say some AI developers want to provide an object detection service. The ML service takes an image data from other applications, and give back the image with bounding boxes drawn on it. An example pipeline can be described as this:

```text
tensor_query_serversrc port=#reserved_appointed_port_number host=localhost connect-type=TCP !
other/tensors,num_tensors=1,types=uint8,format=static,dimensions=3:320:320:1,framerate=0/1 !
tensor_transform mode=arithmetic option=typecast:float32,add:0.0,div:255.0 !
queue ! tensor_filter framework=tensorflow2-lite model=/path/to/yolov5s/model/file.tflite !
other/tensors,num_tensors=1,types=float32,format=static,dimensions=85:6300:1,framerate=0/1 !
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
    other/tensors,num_tensors=1,types=float32,format=static,dimensions=85:6300:1,framerate=0/1 ! \
    tensor_decoder mode=bounding_boxes option1=yolov5 option2=/path/to/coco/label.txt option4=320:320 option5=320:320 ! \
    video/x-raw,format=RGBA,width=320,height=320 ! tensor_converter ! \
    other/tensors,format=static,num_tensors=1,dimensions=4:320:320:1,types=uint8 ! \
    tensor_query_serversink async=false sync=false";

    // Set the pipeline with service name.
    ml_service_pipeline_set ("object_detection_service", object_detection_pipeline);
    ```

2. Get or delete the pipeline description of the service name:

    ```c
    // Get the pipeline description of given service name.
    gchar *pipeline;
    ml_service_pipeline_get ("object_detection_service", &pipeline);

    // Delete the pipeline description of given service.
    ml_service_pipeline_delete ("object_detection_service");
    ```

AI developers can manage the ML service doing the following:.

1. Launch and start the service:

    ```c
    // Launch the given service. Proper pipeline description is should be set beforehand.
    ml_service_h object_detection_service_h;
    ml_service_pipeline_launch ("object_detection_service", object_detection_service_h);

    // Start the given service. Clients can use this service when the pipeline is in playing state.
    ml_service_start (object_detection_service_h);
    ```

2. Stop, destroy or get the pipeline state:

    ```c
    // Get the state of given service.
    ml_pipeline_state_e state;
    ml_service_pipeline_get_state (object_detection_service_h, &state);

    // Stop the given service.
    ml_service_stop (object_detection_service_h);

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

## Machine Learning Service API for model

AI developers and application developers work together to manage an ML-powered application. AI developers focus on improving the performance or accuracy of model file. On the other hand, application developers do not care about details of the model file itself as long as the layout of model is preserved. Decoupling those two groups can improve development efficiency in terms of DevOps.

Let's say an application utilizes the famous MobileNet based model for its image classification task. While maintaining it, AI developers keep improving the accuracy or performance of the model. Instead of changing the application code to handle this model update, the application may use the latest registered MobileNet model. Machine Learning Service API supports this application development scenario.

> [!NOTE]
> Machine Learning Service API for model is supported since Tizen 8.0.

### AI developers registering their model

AI developers can release a model providing application. The application has a model file, and it is registered using this API when the application launches:

```c
// Unique name shared with application developers
const gchar *key = "imgcls-mobilenet";

// Provide the absolute file path
gchar *improved_model_path = g_strdup_printf ("%s/%s", app_get_shared_resource_path (), "mobilenet_v2.tflite");

// Parameter deciding whether to activate this model or not
const bool is_active = true;

// Model description parameter
const gchar *description = "This is description of the mobilenet_v2 model ...";

// Out parameter
unsigned int version;

// Register the model via ML Service API
ml_service_model_register (key, improved_model_path, is_active, description, &version);

// Update the model description
ml_service_model_update_description (key, version, "Updated description for mobilenet_v2");

...

// Register a sample model as NOT active
ml_service_model_register (key, "/some/path/to/model.file", false, "not yet active", &version);

// Get model info with its name and version
ml_information_h model_info;
ml_service_model_get (key, version, &model_info);

// Check values of retrieved model info
gchar *_path;
ml_information_get (model_info, "path", (void **) &_path); // Value of _path: "/some/path/to/model.file"
gchar *_description;
ml_information_get (model_info, "description", (void **) &_description); // Value of _description: "not yet active"

// Activate the not yet active model, setting all other models as NOT active
ml_service_model_activate (key, version);

// Destroy the model info
ml_information_destroy (model_info);

// Get all model info with same name
ml_information_list_h all_info_list;
ml_service_model_get_all (key, &all_info_list);

// Get the number of model info
unsigned int info_length;
ml_information_list_length (all_info_list, &info_length);

for (int i = 0; i < info_length; i++) {
  // Do something for each model info
  ml_information_h info;
  ml_information_list_get_info (all_info_list, i, &info);
  ...
}

// Delete the model from the ml service
ml_service_model_delete (key, version);

// Delete the model info list
ml_information_list_destroy (all_info_list);
```

### Application code using the registered model

Application developers can use the registered model:

```c
// The name shared with AI developers
const gchar *key = "imgcls-mobilenet";
gchar *model_path;

ml_information_h activated_model_info;

// Get registered and activated model via ML Service API
int status = ml_service_model_get_activated (key, &activated_model_info);
if (status == ML_ERROR_NONE) {
  // If there is a model registered by AI developers, use it
  gchar *activated_model_path;

  // Get path of the model
  status = ml_information_get (activated_model_info, "path", (void **) &activated_model_path);

  model_path = g_strdup (activated_model_path);
} else {
  // If there is no registered model, use the default model in the app
  model_path = g_strdup_printf ("%s/%s", app_get_resource_path (), "mobilenet_v1.tflite");
}

// Destroy the model info
ml_information_destroy (activated_model_info);

// Do inference with the variable `model_path`
...

```

## Machine Learning Service API for resource

These APIs allow developers to manage and share any resource files such as images, audio samples, binary, or any other data files. Those resources can be added, retrieved, and deleted using the provided APIs.

Let's say an application trains a model on-device. While training, the application may want to use some validation image files to validate its model. AI developers can add validation image files as ML resources, and application developers can use them to validate the on-device trained model:
> [!NOTE]
> Machine Learning Service API for resource is supported since Tizen 8.0.
```c
// AI developers provide the validation image files as resources

// Unique name shared with developers
const gchar *key_add = "mobilenet-validation-img";

// Add 5 validation image files as resources
for (int i = 0; i < 5; i++) {
  // Provide the absolute file path and description
  gchar *res_path = g_strdup_printf ("%s/%s", app_get_shared_resource_path (), "val_img%d.jpg", i);
  gchar *res_description = g_strdup_printf ("This is description of the validation image %d...", i);

  // Add the resource file path and description
  ml_service_resource_add (key_add, res_path, res_description);

  // Destroy the resource file path and description
  g_free (res_path);
  g_free (res_description);
}

...

// Application developers use the validation image files as resources

// Unique name shared with developers
const gchar *key_get = "mobilenet-validation-img";

// Get all resource info with same name
ml_information_list_h res_info_list;
ml_service_resource_get (key_get, &res_info_list);

// Get the number of resource info
unsigned int info_length;
ml_information_list_length (res_info_list, &info_length);

for (int i = 0; i < info_length; i++) {
  ml_information_h info;
  ml_information_list_get (res_info_list, i, &info);

  gchar *path;
  ml_information_get (info, "path", (void **) &path);

  gchar *description;
  ml_information_get (info, "description", (void **) &description);

  // The validation image files may be used for validate on-device trained mobilenet model
  ...
}

// Delete the resource info
ml_information_list_destroy (res_info_list);

...

// Remove the resource from the ml service
ml_service_resource_delete (key);
```

## Machine learning service with configuration file
It provides an API that manages machine learning services based on the configuration file. Application users can easily use the machine learning service by writing necessary options in the configuration file. The API is designed to be simple and flexible, allowing developers to create, manage, and use machine learning models in their applications. A key feature of this API is that it allows users to manage these capabilities using a configuration file, simplifying the process of setting up and managing machine learning models without updating the application.

### Configuration file template
The configuration file is used to set up the machine learning model and to provide information about the model/pipeline. The configuration file is a JSON file that contains a list of key-value pairs.
- Single-based v.s. Pipeline-based
1. **Single-based** : a simple approach that uses a single model. The single-based approach is suitable for simple tasks.
    ```
    "single" :
    {
      "model" : [mandatory, string] the file path of the model file.
      "framework" : [optional, string] the neural network framework.
      "custom" : [optional, string] the custom options for the neural network framework.
      "input_info" : [optional, array] the array of tensor information of input data.
      "output_info" : [optional, array] the array of tensor information of output data.
    },
    "information" :
    {
      "key" : "value" // Any key-value pair can be added.
    }
    ```

2. **Pipeline-based** : a more complex approach that utilizes GStreamer/NNStreamer pipeline with neural network model(s). The pipeline-based approach is suitable for complex tasks such as requiring many models or GStreamer's performant data processing functionalities. You may check [NNStreamer](https://github.com/nnstreamer/nnstreamer) or [NNStreamer's example](https://github.com/nnstreamer/nnstreamer-example) for more details about pipeline usage.
    ```
    "pipeline" :
    {
      "description" : [mandatory, string] the pipeline description. It should be valid GStreamer pipeline.
      "input_node" : [mandatory, array] the array of input node (appsrc) and tensor information of input data.
      "output_node" : [mandatory, array] the array of output node (appsink or tensor_sink) and tensor information of output data.
    },
    "information" :
    {
      "key" : "value" // Any key-value pair can be added.
    }
    ```

### Configuration file example (image classification)
These are two configuration files of image classification task using mobilenet tflite model.

1. Single-based configuration file

    ```json
    {
      "single" :
      {
        "model" : "/path/to/model/mobilenet_v2_1.0_224_quant.tflite",
        "framework" : "tensorflow-lite",
        "input_info" : [
          {
            "type" : "uint8",
            "dimension" : "3:224:224:1"
          }
        ],
        "output_info" : [
          {
            "type" : "uint8",
            "dimension" : "1001:1"
          }
        ]
      },
      "information" :
      {
        "threshold" : "0.65",
        "label_path" : "/path/to/label/label.txt"
      }
    }
    ```

  This is a simple configuration for a model that takes a single input tensor and produces a single output tensor.

  - Input tensor is of type `uint8` and has dimension `3:224:224:1`. The model would take an image of 224x224 with 3 color channels (RGB) and a batch size of 1.
  - Output tensor is of type `uint8` and has dimension `1001:1`. It would represent a vector of 1001 class probabilities for some classification task.
  - Application can get `threshold` and `label_path` values with `ml_service_get_information` API.

  Note that **`"input_info"` and `"output_info"` can be omitted for tflite model**, because NNStreamer can infer the input and output tensor information when open the tflite model file. However, a few frameworks require explicit input/output information. So you should check your model and its framework.

2. Pipeline-based configuration file

    ```json
    {
      "pipeline" :
      {
        "description" : "appsrc name=input_img caps=other/tensors,num_tensors=1,format=static,types=uint8,dimensions=3:224:224:1,framerate=0/1 ! tensor_filter framework=tensorflow-lite model=/path/to/model/mobilenet_v2_1.0_224_quant.tflite ! tensor_sink name=result_clf",
        "input_node" : [
          {
            "name" : "input_img",
            "info" : [
              {
                "type" : "uint8",
                "dimension" : "3:224:224:1"
              }
            ]
          }
        ],
        "output_node" : [
          {
            "name" : "result_clf",
            "info" : [
              {
                "type" : "uint8",
                "dimension" : "1001:1"
              }
            ]
          }
        ]
      },
      "information" :
      {
        "threshold" : "0.65",
        "label_path" : "/path/to/label/label.txt"
      }
    }
    ```

  This is a pipeline-based configuration for an image classification task. The description should be valid GStreamer pipeline.

  - `appsrc` element named `input_img` is the source of the input data, which is a tensor of type `uint8` and dimension `3:224:224:1`. `caps` is required here, and it is equivalent to corresponding `input_node`.
  - `tensor_filter` element uses the TensorFlow-Lite framework and the `mobilenet_v2_1.0_224_quant.tflite` model to process the input data.
  - `tensor_sink` element named `result_clf` is the sink for the output data, which produces a single tensor of type `uint8` and dimension of `1001:1` as written in `output_node`.
  - Application can get `threshold` and `label_path` values with `ml_service_get_information` API.

### Example of use
This section shows how to use the ml-service.
```c
  // Callback function for the event from machine learning service.
  // Note that the handle of event data will be deallocated after the return and this is synchronously called.
  // Thus, if you need the event data, copy the data and return fast.
  // Do not spend too much time in the callback.
  static void
  _ml_service_event_cb (ml_service_event_e event, ml_information_h event_data, void *user_data)
  {
    ml_tensors_data_h data;
    void *_data;
    size_t _size;
 
    switch (event) {
      case ML_SERVICE_EVENT_NEW_DATA:
        // For the case of new data event, handle output data.
        ml_information_get (event_data, "data", &data);
        ml_tensors_data_get_tensor_data (data, 0, &_data, &_size);
        break;
      default:
        break;
    }
  }
 
  // The path to the configuration file.
  const char config_path[] = "/path/to/application/configuration/my_application_config.conf";
 
  // Create ml-service for model inference from configuration.
  ml_service_h handle;
 
  ml_service_new (config_path, &handle);
  ml_service_set_event_cb (handle, _ml_service_event_cb, NULL);
 
  // Get input information and allocate input buffer.
  ml_tensors_info_h input_info;
  void *input_buffer;
  size_t input_size;
 
  ml_service_get_input_information (handle, NULL, &input_info);
 
  ml_tensors_info_get_tensor_size (input_info, 0, &input_size);
  input_buffer = malloc (input_size);
 
  // Create input data handle.
  ml_tensors_data_h input;
 
  ml_tensors_data_create (input_info, &input);
  ml_tensors_data_set_tensor_data (input, 0, input_buffer, input_size);
 
  // Push input data into ml-service and process the output in the callback.
  ml_service_request (handle, NULL, input);
 
  // Finally, release all handles and allocated memories.
  ml_tensors_info_destroy (input_info);
  ml_tensors_data_destroy (input);
  ml_service_destroy (handle);
  free (input_buffer);
```

### Extended usage case for AI service
By modifying the configuration file, you can construct various AI service, such as 1) model registration to the remote (edge) device. 2) AI pipeline registration to the remote device. 3) Requesting AI model training on the remote device.

### ML-SERVICE-API usage for Large Language Model (LLM)
This example demonstrates how to implement a Large Language Model (LLM) service using `ml-service-api`. To help you understand, we'll wrap ml-service-api as shown below to create an `ml-lxm-service`(unreleased) and explain how to make LLM work.

#### Here is a link to the full source code: https://github.com/nnstreamer/nnstreamer-example/tree/main/Tizen.platform/lxm_service

#### Prerequisites
- `ml-api-service` and `flare` development packages installed on your target device

#### API Reference
#### LXM service availability status.
```cpp
typedef enum
{
  ML_LXM_AVAILABILITY_AVAILABLE = 0,
  ML_LXM_AVAILABILITY_DEVICE_NOT_ELIGIBLE,
  ML_LXM_AVAILABILITY_SERVICE_DISABLED,
  ML_LXM_AVAILABILITY_MODEL_NOT_READY,
  ML_LXM_AVAILABILITY_UNKNOWN
} ml_lxm_availability_e;
```
#### Availability Check
```cpp
/**
 * @brief Checks LXM service availability.
 * @param[out] status Current availability status.
 * @return ML_ERROR_NONE on success, error code otherwise.
 */
int ml_lxm_check_availability (ml_lxm_availability_e * status);
```

### Data Type
```cpp
/**
 * @brief Token streaming callback type.
 * @param token Generated token string.
 * @param user_data User-defined context.
 */
typedef void (*ml_lxm_token_cb)(ml_service_event_e event, ml_information_h event_data, void *user_data);

/**
 * @brief Generation options for LXM responses.
 */
typedef struct {
  double temperature;
  size_t max_tokens;
} ml_lxm_generation_options_s;
```
#### Session Management
```cpp
/**
 * @brief Creates an LXM session.
 * @param[out] session Session handle.
 * @param[in] config_path Path to configuration file.
 * @param[in] instructions Initial instructions (optional).
 * @return ML_ERROR_NONE on success.
 */
int ml_lxm_session_create(ml_lxm_session_h *session, const char *config_path, const char *instructions);

/**
 * @brief Destroys an LXM session.
 * @param[in] session Session handle.
 * @return ML_ERROR_NONE on success.
 */
int ml_lxm_session_destroy(ml_lxm_session_h session);

/**
 * @brief Sets runtime instructions for a session.
 * @param[in] session Session handle.
 * @param[in] instructions New instructions.
 * @return ML_ERROR_NONE on success.
 */
int ml_lxm_session_set_instructions(ml_lxm_session_h session, const char *instructions);
```

#### Prompt Handling
```cpp
/**
 * @brief Creates a prompt object.
 * @param[out] prompt Prompt handle.
 * @return ML_ERROR_NONE on success.
 */
int ml_lxm_prompt_create(ml_lxm_prompt_h *prompt);

/**
 * @brief Destroys a prompt object.
 * @param[in] prompt Prompt handle.
 * @return ML_ERROR_NONE on success.
 */
int ml_lxm_prompt_destroy(ml_lxm_prompt_h prompt);

/**
 * @brief Appends text to a prompt.
 * @param[in] prompt Prompt handle.
 * @param[in] text Text to append.
 * @return ML_ERROR_NONE on success.
 */
int ml_lxm_prompt_append_text(ml_lxm_prompt_h prompt, const char *text);

/**
 * @brief Appends an instruction to a prompt.
 * @param[in] prompt Prompt handle.
 * @param[in] instruction Instruction to append.
 * @return ML_ERROR_NONE on success.
 */
int ml_lxm_prompt_append_instruction(ml_lxm_prompt_h prompt, const char *instruction);
```

#### Response Generation
```cpp
/**
 * @brief Generates an token-streamed response.
 * @param[in] session Session handle.
 * @param[in] prompt Prompt handle.
 * @param[in] options Generation parameters.
 * @param[in] token_callback Callback for each generated token.
 * @param[in] user_data User context passed to callback.
 * @return ML_ERROR_NONE on success.
 */
int ml_lxm_session_respond(
  ml_lxm_session_h session,
  ml_lxm_prompt_h prompt,
  const ml_lxm_generation_options_s *options,
  ml_lxm_token_cb token_cb,
  void *user_data
);
```
#### Error Codes
- ML_ERROR_NONE: Operation successful
- ML_ERROR_INVALID_PARAMETER: Invalid parameters detected
- ML_ERROR_OUT_OF_MEMORY: Memory allocation failure
- ML_ERROR_IO_ERROR: File/DB operation failure


#### Sample Code Explanation

### Configuration file
```
{
    "single" :
    {
        "framework" : "flare",
        "model" : ["sflare_if_4bit_3b.bin"],
        "adapter" : ["history_lora.bin"],
        "custom" : "tokenizer_path:tokenizer.json,backend:CPU,output_size:1024,model_type:3B,data_type:W4A32",
        "invoke_dynamic" : "true",
    }
}
```

#### Key Components
```cpp
#include <ml-api-service.h>
#include "ml-lxm-service.h"

// Global handles
ml_lxm_session_h g_session = NULL;
ml_lxm_prompt_h g_prompt = NULL;

```
#### Main Workflow
1. Session Creation
```cpp
ret = ml_lxm_session_create(&g_session, config_path, "Default instructions");
```
2. Prompt Handling
```cpp
ml_lxm_prompt_create(&g_prompt);
ml_lxm_prompt_append_text(g_prompt, "Explain quantum computing");
```
3. Response Generation
```cpp
ml_lxm_generation_options_s options = {
  .temperature = 1.2,
  .max_tokens = 128
};

ml_lxm_session_respond(
  g_session,
  g_prompt,
  &options,
  token_handler,
  NULL
);
```
4. Token Callback
```cpp
static void token_handler(
  ml_service_event_e event,
  ml_information_h event_data,
  void *user_data
) {
  /* Process tokens here */
}
```
5. Cleanup
```cpp
ml_lxm_prompt_destroy(g_prompt);
ml_lxm_session_destroy(g_session);
```
#### Full Example Snippet
```cpp
#include <ml-api-service.h>
#include "ml-lxm-service.h"

static void token_handler(ml_service_event_e event,
                          ml_information_h event_data,
                          void *user_data);
int main() {
  ml_lxm_session_h session;
  ml_lxm_prompt_h prompt;

  // 1. Create session
  ml_lxm_session_create(&session, "/path/to/config", NULL);

  // 2. Create prompt
  ml_lxm_prompt_create(&prompt);
  ml_lxm_prompt_append_text(prompt, "Hello AI");

  // 3. Generate response
  ml_lxm_generation_options_s options = {1.0, 50};
  ml_lxm_session_respond(session, prompt, &options, token_handler, NULL);

  // 4. Cleanup
  ml_lxm_prompt_destroy(prompt);
  ml_lxm_session_destroy(session);

  return 0;
}

static void token_handler(ml_service_event_e event,
                          ml_information_h event_data,
                          void *user_data) {
  ml_tensors_data_h data = NULL;
  void *_raw = NULL;
  size_t _size = 0;
  int ret;

  switch (event) {
  case ML_SERVICE_EVENT_NEW_DATA:
    if (event_data != NULL) {

      ret = ml_information_get(event_data, "data", &data);
      if (ret != ML_ERROR_NONE) {
        g_print("Failed to get data from event_data\n");
        return;
      }

      ret = ml_tensors_data_get_tensor_data(data, 0U, &_raw, &_size);
      if (ret != ML_ERROR_NONE) {
        g_print("Failed to get tensor data\n");
        return;
      }

      std::cout.write(static_cast<const char *>(_raw), _size);
      std::cout.flush();
    }
  default:
    break;
  }
}
```

## Related information

- Dependencies
  - Since Tizen 7.0
- API References
  - [ML-Service API](../../api/common/latest/group__CAPI__ML__NNSTREAMER__SERVICE__MODULE.html)
