# Machine Learning Inference


You can easily create and efficiently execute data stream pipelines that consist of neural networks as filters in pipelines.

The main features of the Machine Learning Inference API include:

- Construction of data pipeline

  You can compose the data stream pipeline through Machine Learning Inference with various elements of [GStreamer](https://gstreamer.freedesktop.org) and [NNStreamer](https://github.com/nnstreamer/nnstreamer).

- [Single](#single-api) API and [Pipeline](#pipeline-api) API

  There are two types of Machine Learning Inference API - Single API and Pipeline API.

  Single API is useful for a simple usage scenario of neural network models. It allows invoking a neural network model with a single instance of input data for the model directly. It is useful if you have the input data pre-processed with the application itself and there are no complex interactions between neural network models, data processors, or data stream paths.

  Pipeline API allows developers to construct and execute pipelines with multiple neural network models, multiple inputs and output nodes, multiple data processors, pre-and-post processors, and various data path manipulators. Besides, if the input is online data or streamed data, Pipeline API simplifies your application and improves its performance.


- Support various neural network frameworks (NNFW)

  TensorFlow, TensorFlow-Lite, Caffe2, and PyTorch are the supported neural network frameworks. Neural network model files trained by such frameworks can be imported as filters of pipelines directly.
  Custom filters, which are neural network models implemented directly with programming languages including C/C++ and Python, maybe imported as filters of pipelines directly as well.

  > [!NOTE]
  > The devices powered by Tizen OS can contain TensorFlow-Lite only. Ensure that the neural network frameworks that you want to use are installed.

## Prerequisites

To enable your application to use the machine learning functionality:

1. To use the functions and data types of the Machine Learning Inference API, include the `<nnstreamer.h>` header file in your application:

   ```c
   #include <nnstreamer.h>
   ```

2. To use the Machine Learning Inference API, include the following features in your `tizen-manifest.xml` file:

   ```xml
   <feature name="http://tizen.org/feature/machine_learning">true</feature>
   <feature name="http://tizen.org/feature/machine_learning.inference">true</feature>
   ```

## Single API

This section shows how to load a model without the construction of pipelines.

1. Open a model file:

    ```c
    #include <nnstreamer-single.h>

    ml_single_h single;
    ml_tensors_info_h in_info, out_info;

    ...

    ml_single_open (&single, "model_file_path", in_info, out_info, ML_NNFW_TYPE_TENSORFLOW_LITE, ML_NNFW_HW_ANY);
    ```

    To load a model file, two `ml_tensors_info_h` are required. `in_info` contains the information of the input tensors, and `out_info` contains the information of the output tensors. For more information, see [Tensors Information](#tensors-information).

2. Get the [Tensors Information](#tensors-information).

    After opening the model, use the following functions to bring the information of the input and output tensors:

    ```c
    ml_single_get_input_info (single, &in_info);
    ml_single_get_output_info (single, &out_info);
    ```

3. Invoke the model with input and output [Tensors Data](#tensors-data).

    The model can be invoked with input and output tensors data. The result is included in the output tensors data:

    ```c
    ml_tensors_data_create (in_info, &input);
    ml_single_invoke (single, input, &output);
    ```

4. Close the opened handle:

    ```c
    ml_single_close (single);
    ```

## Pipeline API

This section shows how to create a pipeline.

### Basic Usage

1. Construct a pipeline with the GStreamer elements.

    Different pipelines can be constructed using various GStreamer elements:

    ```c
    char pipeline[] = "videotestsrc num_buffers=2 ! videoconvert ! videoscale ! video/x-raw,format=RGBx,width=224,height=224 ! tensor_converter ! fakesink";
    ml_pipeline_h handle;

    ml_pipeline_construct (pipeline, NULL, NULL, &handle);
    ```

2. Start the pipeline and get state:

    ```c
    /* The pipeline could be started when the state is paused */
    ml_pipeline_start (handle);
    ml_pipeline_get_state (handle, &state);
    ```

3. Stop the pipeline and get state:

    ```c
    ml_pipeline_stop (handle);
    ml_pipeline_get_state (handle, &state);
    ```

4. Destroy the pipeline.

    When no longer needed, destroy the pipeline:

    ```c
    ml_pipeline_destroy (handle);
    ```

### Element API

You need to manipulate the input and the output data to run neural network models with Machine Learning Inference API. In addition, you can construct pipelines that can be controlled.

Followings are the available elements:

- **Source**

    The configuration of the data source element is required to set the input tensor data:

    ```c
    char pipeline[] = "appsrc name=srcx ! other/tensor,dimension=(string)4:1:1:1,type=(string)uint8,framerate=(fraction)0/1 ! tensor_sink";
    ```

    `ml_pipeline_src_get_handle()` controls the `appsrc` element with the name `srcx`:

    ```c
    ml_pipeline_h handle;
    ml_pipeline_src_h srchandle;

    ml_pipeline_construct (pipeline, NULL, NULL, &handle);
    ml_pipeline_start (handle);

    ml_pipeline_src_get_handle (handle, "srcx", &srchandle);
    ```

    You can check the information of input tensors using `srchandle`:

    ```c
    ml_tensors_info_h info;

    ml_pipeline_src_get_tensors_info (srchandle, &info);
    ```

    The input tensor data can be filled according to the `info`:

    ```c
    ml_tensors_data_h data;

    ml_tensors_data_create (info, &data);

    for (i = 0; i < 10; i++) {
      uintarray1[i] = (uint8_t *) malloc (4);
      uintarray1[i][0] = i + 4;
      uintarray1[i][1] = i + 1;
      uintarray1[i][2] = i + 3;
      uintarray1[i][3] = i + 2;
    }

    ml_tensors_data_set_tensor_data (data, 0, uintarray1[0], 4);

    /* Setting the policy of raw data pointer */
    ml_pipeline_src_input_data (srchandle, data, ML_PIPELINE_BUF_POLICY_DO_NOT_FREE);
    ```

    After using the data source element, release the handle:

    ```c
    ml_pipeline_src_release_handle (srchandle);
    ```

- **Sink**

    The configuration of the data sink element is required to get the output tensor data:

    ```c
    char pipeline[] = "videotestsrc num-buffers=3 ! videoconvert ! tensor_converter ! appsink name=sinkx";
    ```

    `appsink` element with the name `sinkx` becomes reachable through `ml_pipeline_sink_register()`:

    ```c
    ml_pipeline_h handle;
    ml_pipeline_sink_h sinkhandle;

    ml_pipeline_construct (pipeline, NULL, NULL, &handle);

    ml_pipeline_sink_register (handle, "sinkx", sink_callback, user_data, &sinkhandle);
    ```

    You can get the data from `sink_callback()`, whenever `appsink` named `sinkx` receives data:

    ```c
    typedef void (*ml_pipeline_sink_cb) (const ml_tensors_data_h data, const ml_tensors_info_h info, void *user_data);
    ```

    Release the `sinkhandle` through `ml_pipeline_sink_unregister()`:

    ```c
    ml_pipeline_sink_unregister (sinkhandle);
    ```

- **Valve**

    This element is used to control the stream of a pipeline:

    ```c
    char pipeline[] = "videotestsrc is-live=true ! videoconvert ! videoscale ! video/x-raw,format=RGBx,width=16,height=16,framerate=10/1 ! tensor_converter ! valve name=valve1 ! fakesink";
    ml_pipeline_h handle;

    ml_pipeline_construct (pipeline, NULL, NULL, &handle);
    ```

    By default, valve named `valve1` of the pipeline is opened. You can control the valve using `ml_pipeline_valve_h`:

    ```c
    ml_pipeline_valve_h valve1;

    ml_pipeline_valve_get_handle (handle, "valve1", &valve1);
    ```

    After you start a pipeline, you can control the stream of the pipeline with a valve:

    ```c
    ml_pipeline_start (handle);

    ml_pipeline_valve_set_open (valve1, false); /* Close */
    ```

    You can also open the pipeline by controlling the stream of a pipeline with a valve:

    ```c
    ml_pipeline_valve_set_open (valve1, true); /* Open */
    ```

    Before you destroy the pipeline, release `ml_pipeline_valve_h`:

    ```c
    ml_pipeline_valve_release_handle (valve1); /* Release valve handle */
    ```

- **Switch**

    The switch element is used when you need only one working branch from a pipeline that has multiple branches:

    ![input-selector](./media/input-selector.png)

    ```c
    char pipeline[] = "input-selector name=ins ! tensor_converter ! tensor_sink name=sinkx videotestsrc is-live=true ! videoconvert ! ins.sink_0 videotestsrc num-buffers=3 is-live=true ! videoconvert ! ins.sink_1";
    ```

    Get `ml_pipeline_switch_h`. The name of the switch in this pipeline is `ins`:

    ```c
    ml_pipeline_h handle;
    ml_pipeline_switch_h switchhandle;
    ml_pipeline_switch_e type;

    ml_pipeline_construct (pipeline, NULL, NULL, &handle);
    ml_pipeline_switch_get_handle (handle, "ins", &type, &switchhandle);
    ```

    You can control the switch using the handle `ml_pipeline_switch_h`:

    ```c
    ml_pipeline_switch_select (switchhandle, "sink_1");
    ```

    Before you destroy the pipeline, release `ml_pipeline_switch_h`:

    ```c
    ml_pipeline_switch_release_handle (switchhandle);
    ```

    The following image shows the switch at the end of the pipeline:

    ![output-selector](./media/output-selector.png)

    ```c
    char pipeline[] = "videotestsrc is-live=true ! videoconvert ! tensor_converter ! output-selector name=outs outs.src_0 ! tensor_sink name=sink0 async=false outs.src_1 ! tensor_sink name=sink1 async=false"
    ```

- **If**

    The if (tensor_if) element allows creating conditional branches based on tensor values. For example, you may skip frames if there is no object detected with high confidence. The input and output stream data type is either `other/tensor` or `other/tensors`.

    - **Properties**
      - `compared-value`: Specifies the compared value and is represented as operand 1 from input tensors.
        - A_VALUE: Decided based on a single scalar value.
        - TENSOR_AVERAGE_VALUE: Decided based on an average value of a specific tensor.
        - CUSTOM: Decided based on a user-defined callback.
      - `compared-value-option`: Specifies an element of the nth tensor or you can pick one from the tensors.
        - [C][W][H][B],n: Used for A_VALUE of the compared-value, for example 0:1:2:3,0 means [0][1][2][3] value of first tensor.
        - nth tensor: Used for TENSOR_AVERAGE_VALUE of the compared-value, and specifies which tensor is used.
      - `supplied-value`: Specifies the supplied value (SV) from the user.
        - SV
        - SV1, SV2: Used for range operators.
      - `operator`: Specifies a comparison operator which is used for comparing the compared-value (CV) and the supplied-value (SV).
        - EQ: Check if CV == SV
        - NEQ: Check if CV != SV
        - GT: Check if CV > SV
        - GE: Check if CV >= SV
        - LT: Check if CV < SV
        - LE: Check if CV <= SV
        - RANGE_INCLUSIVE: Check if SV1 <= CV and CV <= SV2
        - RANGE_EXCLUSIVE: Check if SV1 < CV and CV < SV2
        - NOT_IN_RANGE_INCLUSIVE: Check if CV < SV1 or SV2 < CV
        - NOT_IN_RANGE_EXCLUSIVE: Check if CV <= SV1 or SV2 <= CV
      - `then`: Specifies the action, if the result is TRUE.
        - PASSTHROUGH: Does not let you make changes to the buffers. Buffers are pushed straight through.
        - SKIP: Does not let you generate the output frame (frame skip).
        - TENSORPICK: Lets you choose the nth tensor among the input tensors.
          ```
          [ tensor 0 ]
          [ tensor 1 ]  ->   tensor if    ->    [ tensor 0 ]
          [ tensor 2 ]    (tensorpick 0,2)      [ tensor 2 ]
          input tensors                         output tensors
          ```
      - `then-option`: Specifies the option for TRUE action.
        - nth tensor: Used for TENSORPICK option, for example, `then-option`=`0,2` means tensor `0` and tensor `2` are selected as output tensors among the input tensors.
      - `else`: Specifies the action, if the result is FALSE.
        - PASSTHROUGH: Does not let you make changes to the buffers. Buffers are pushed straight through.
        - SKIP: Does not let you generate an output frame (frame skip).
        - TENSORPICK: Lets you choose the nth tensor among the input tensors.
      - `else-option`: Specifies the option for FALSE action.
        - nth tensor: Used for TENSORPICK option, for example, `else-option`=`0,2` means tensor `0` and tensor `2` are selected as output tensors among the input tensors.

    - **Example launch line with simple if-condition**

      If a specific value, for example, [3][4][2][5] value of the first tensor is between a given range of [10,100], input buffers are pushed straight through. If the value is not in the given range, tensor `0` and tensor `2` are selected as output tensors. It can be expressed as:

      ```
      gst-launch ... (tensors 0,1,2 stream) !
          tensor_if name=tif \
                      compared-value=A_VALUE compared-value-option=3:4:2:5,0 \
                      supplied-value=10,100 \
                      operator=RANGE_INCLUSIVE \
                      then=PASSTHROUGH \
                      else=TENSORPICK \
                      else-option=0,2 \
          ! tif.src_0 ! (tensors 0,1,2 for TRUE action) ...
          ! tif.src_1 ! (tensors 0,2 for FALSE action) ...
      ```

    - **Custom if-condition**

      If the if-condition is complex and cannot be expressed with tensor_if expressions, you can define a custom if-condition, and create a pipeline as follows:

      - **Define and register custom if-custom**

        Before you use the custom if-condition in the pipeline, you have to register the custom if-condition with input tensors information and data:

        ```c
        /* Define custom if-condition */
        static int tensor_if_custom_cb (const ml_tensors_data_h data, const ml_tensors_info_h info, int *result, void *user_data)
        {
        /* Describe the conditions and pass the result. Result 0 refers to FALSE and a non-zero value refers to TRUE. */
        *result = 1;
        /* Return 0 if there is no error. */
        return 0;
        }

        ...
        /* Register tensor_if custom with name 'tif_custom_cb_name' */
        status = ml_pipeline_tensor_if_custom_register ("tif_custom_cb_name", tensor_if_custom_cb, NULL, &custom);
        ```

      - **Construct a pipeline with custom if-condition**

        After registering the custom if-condition, you can use custom if-condition when constructing the pipeline:

        ```c
        /* The pipeline description (input data with dimension 2:1:1:1 and type int8 will be passed to tensor_if custom condition. Depending on the result, proceed to true or false paths.) */
        const char pipeline[] = "appsrc ! other/tensor,dimension=(string)2:1:1:1,type=(string)int8,framerate=(fraction)0/1 ! tensor_if name=tif compared-value=CUSTOM compared-value-option=tif_custom_cb_name then=PASSTHROUGH else=PASSTHROUGH tif.src_0 ! tensor_sink name=true_condition async=false tif.src_1 ! tensor_sink name=false_condition async=false"
        int status;
        ml_pipeline_h pipe;
        ml_pipeline_if_h custom;

        /* Construct the pipeline. */
        status = ml_pipeline_construct (pipeline, NULL, NULL, &pipe);
        if (status != ML_ERROR_NONE) {
        /* Handle error case. */
        goto error;
        }

        /* Start the pipeline and execute the tensor. */
        ml_pipeline_start (pipe);

        error:
        /* Destroy the pipeline and unregister tensor_if custom. */
        ml_pipeline_stop (pipe);
        ml_pipeline_destroy (pipe);
        ml_pipeline_tensor_if_custom_unregister (custom);

        ```

- **Normal element**

    All elements in the pipeline have specific properties and can be manipulated to control the operation of a pipeline. To get and set the property value, you have to get the element handle in the pipeline by calling `ml_pipeline_element_get_handle()` with its name as follows:
    ```c
    ml_pipeline_h handle = nullptr;
    ml_pipeline_element_h demux_h = nullptr;

    pipeline = g_strdup("videotestsrc ! video/x-raw,format=RGB,width=640,height=480 ! videorate max-rate=1 ! " \
	    "tensor_converter ! tensor_mux ! tensor_demux name=demux ! tensor_sink");

    // Construct a pipeline
    status = ml_pipeline_construct (pipeline, NULL, NULL, &handle);

    // Get the handle of the target element
    status = ml_pipeline_element_get_handle (handle, "demux", &demux_h);
    ```

    After fetching the handle of the target element, you can set and get the value of the specific property:
    ```c
    gchar *ret_tensorpick;

    // Set the string value of the given element's property
    status = ml_pipeline_element_set_property_string (demux_h, "tensorpick", "1,2");

    // Get the string value of the given element's property
    status = ml_pipeline_element_get_property_string (demux_h, "tensorpick", &ret_tensorpick);
    ```

    Before you destroy the pipeline, release `demux_h` by calling `ml_pipeline_element_release_handle()`:
    ```c
    ml_pipeline_element_release_handle (demux_h);
    ```

    To figure out the property information of the target element, you can run `gst-inspect-1.0` command on your device as follows:
    ```text
    # gst-inspect-1.0 tensor_demux
    ...
    Element Properties:
    name                : The name of the object
                            flags: readable, writable
                            String. Default: "tensordemux0"
    parent              : The parent of the object
                            flags: readable, writable
                            Object of type "GstObject"
    silent              : Produce verbose output
                            flags: readable, writable
                            Boolean. Default: true
    tensorpick          : Choose nth tensor among tensors
                            flags: readable, writable
                            String. Default: ""
    ...
    ```

### Pipeline States

For more information about the pipeline states, see [GStreamer guide](https://gstreamer.freedesktop.org/documentation/plugin-development/basics/states.html).

## Tensors Information

`ml_tensors_info_h` contains the information of tensors. The tensor info can be managed using the following functions:

- **Create and destroy**

    ```c
    ml_tensors_info_h info;

    ml_tensors_info_create (&info);
    ml_tensors_info_destroy (info);
    ```

- **Set functions**

    ```c
    /* Set how many tensors exist */
    ml_tensors_info_set_count (info, 1);

    /* Set the type of the tensor_0 as UINT8 */
    ml_tensors_info_set_tensor_type (info, 0, ML_TENSOR_TYPE_UINT8);

    /* Set the dimension of the tensor_0 as in_dim */
    ml_tensors_info_set_tensor_dimension (info, 0, in_dim);

    /* Set the name of the tensor_0 as "tensor-name-test" */
    ml_tensors_info_set_tensor_name (info, 0, "tensor-name-test");
    ```

- **Get functions**

    ```c
    /* Get how many tensors exist */
    ml_tensors_info_get_count (info, &num);

    /* Get the type of the tensor_0 */
    ml_tensors_info_get_tensor_type (info, 0, &out_type);

    /* Get the dimension of the tensor_0 */
    ml_tensors_info_get_tensor_dimension (info, 0, in_dim);

    /* Get the name of the tensor_0 */
    ml_tensors_info_get_tensor_name (info, 0, &out_name);

    /* Get the size of the tensor_0 */
    ml_tensors_info_get_tensor_size (info, 0, &data_size);
    ```

## Tensors Data

`ml_tensors_data_h` contains the raw data of tensors. The tensor data can be managed using the following functions:

- **Create and destroy**

    ```c
    ml_tensors_data_h data;
    ml_tensors_info_h info;

    ml_tensors_data_create (info, &data);
    ml_tensors_data_destroy (data);
    ```

- **Get and set tensor data**

    ```c
    /* Get tensor data */
    void *data_ptr;
    size_t data_size;

    ml_tensors_data_get_tensor_data (data, 0, &data_ptr, &data_size);

    /* Set tensor data */
    uint8_t dummy[4] = {1, 1, 1, 1};
    ml_tensors_data_set_tensor_data (data, 0, dummy, 1);
    ```

## Custom Filter

For your convenience, NNStreamer provides an interface for processing the tensor data with the `custom-easy` framework. After registering the user-defined callback function with the input and the output tensor information, NNStreamer can manipulate tensor data in the pipeline without an independent shared object. Since the callback function works as **filter** in the pipeline, it is named as `Custom Filter`.

- **Define and register Custom Filter**

    Before you use the Custom Filter in the pipeline, you have to register the Custom Filter with input and output tensor information and its name:

    ```c
    /* Define Custom Filter function */
    static int custom_filter_invoke_cb (const ml_tensors_data_h in, ml_tensors_data_h out, void *user_data)
    {
        /* Get input tensors using data handle 'in',
           and fill output tensors using data handle 'out'. */
        if (user_data) {
            void *raw_data = NULL;
            size_t *data_size = (size_t *) user_data;

            ml_tensors_data_get_tensor_data (out, 0, &raw_data, data_size);
        }

        return 0;
    }
    ...

    ml_tensors_info_h in_info, out_info;
    ml_custom_easy_filter_h custom;
    ml_tensor_dimension dim = { 2, 1, 1, 1 };
    size_t data_size;
    int status;

    /* Define input and output tensor information. */
    ml_tensors_info_create (&in_info);
    ml_tensors_info_set_count (in_info, 1);
    ml_tensors_info_set_tensor_type (in_info, 0, ML_TENSOR_TYPE_INT8);
    ml_tensors_info_set_tensor_dimension (in_info, 0, dim);

    ml_tensors_info_create (&out_info);
    ml_tensors_info_set_count (out_info, 1);
    ml_tensors_info_set_tensor_type (out_info, 0, ML_TENSOR_TYPE_FLOAT32);
    ml_tensors_info_set_tensor_dimension (out_info, 0, dim);

    /* Register custom filter with name 'my-custom-filter' */
    status = ml_pipeline_custom_easy_filter_register ("my-custom-filter", in_info, out_info, custom_filter_invoke_cb, &data_size, &custom);
    ```

- **Construct a pipeline with Custom Filter**

    After registering the Custom Filter, you can use it when constructing the pipeline:

    ```c
    ml_pipeline_h pipe;

    /* framework is 'custom-easy' and registered model `my-custom-filter` is used */
    const char pipeline[] = "appsrc ! other/tensor,dimension=(string)2:1:1:1,type=(string)  int8,framerate=(fraction)0/1 ! tensor_filter framework=custom-easy model=my-custom-filter ! tensor_sink";

    status = ml_pipeline_construct (pipeline, NULL, NULL, &pipe);
    ```

    After using the Custom Filter handle, it should be unregistered by calling `ml_pipeline_custom_easy_filter_unregister()`:
    ```c
    ml_pipeline_destroy (handle);
    ml_pipeline_custom_easy_filter_unregister (custom);
    ```


## Related Information

- Dependencies
  - Tizen 5.5 and Higher for Mobile
  - Tizen 5.5 and Higher for Wearable
