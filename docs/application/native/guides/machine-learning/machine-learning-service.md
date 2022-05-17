# Machine Learning Service

The Machine Learning Service API provides utility interfaces for AI application developers.

These functions allow the following operations with NNStreamer:
- Set and get the pipeline description with a name, which is a unique key string of applicable service.
- Delete the pipeline description.

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

## An example of usage

The following code snippet shows a simple example of the Machine Learning Service API.

An ML developer adds a pipeline description which includes preprocessing and invoking a neural network model, and an application developer can get the registered pipeline.

1. Set the pipeline description:
    ```c
    const gchar my_pipeline[] = "videotestsrc is-live=true ! videoconvert ! tensor_converter ! tensor_sink async=false";
    int status;

    status = ml_service_set_pipeline ("my_pipeline", my_pipeline);
    if (status != ML_ERROR_NONE) {
      // handle error case
      goto error;
    }
    ```

2. Get the pipeline description and construct this for various data-streamed services:
    ```c
    gchar *pipeline;
    int status;
    ml_pipeline_h handle;

    status = ml_service_get_pipeline ("my_pipeline", &pipeline);
    if (status != ML_ERROR_NONE) {
      // handle error case
      goto error;
    }

    status = ml_pipeline_construct (pipeline, NULL, NULL, &handle);
    if (status != ML_ERROR_NONE) {
      // handle error case
      goto error;
    }

    // run the service.

    error:
    ml_pipeline_destroy (handle);
    g_free (pipeline);
    ```

## Related information

- Dependencies
  - Tizen 7.0 and Higher for Mobile
  - Tizen 7.0 and Higher for Wearable
  - Tizen 7.0 and Higher for TV
  - Tizen 7.0 and Higher for IoT
