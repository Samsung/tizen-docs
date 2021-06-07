# Pipeline

You can use the `Tizen.MachineLearning.Inference.Pipeline` class to manage the topology of data and the interconnection between processors and models.

Pipeline allows you to construct and execute a pipeline with multiple neural network models, multiple inputs and output nodes, multiple data processors, pre-and-post processors, and various data path manipulators.
If the input is streamed data, Pipeline can simplify your application and improve its performance.

The main features of Pipeline include:

- Pipeline construction

  You can [compose the data stream pipeline](#construct) using Machine Learning Inference with various elements of [GStreamer](https://gstreamer.freedesktop.org) and [NNStreamer](https://github.com/nnstreamer/nnstreamer).

- Pushing the input data

  You can [push the input data](#inputdata) into the streamed pipeline.

- Subscribing to the output data

  Pipeline supports multiple output nodes. You can [subscribe to the output data](#outputdata) from the constructed pipeline.

- Data flow control

  Using the various nodes and functionalities in Pipeline, you can easily [handle and control the data flow](#dataflow).

## Prerequisites

To enable your application to use the Machine Learning Inference API functionality:

1. To use the methods and properties of the `Tizen.MachineLearning.Inference.Pipeline` class or its related classes such as `Tizen.MachineLearning.Inference.TensorsData` and `Tizen.MachineLearning.Inference.TensorsInfo`, include the `Tizen.MachineLearning.Inference` namespace in your application:

    ```csharp
    using Tizen.MachineLearning.Inference;
    ```

2. If the model file you want to use is located in the **media storage** or the **external storage**, the application has to request permission by adding the following privileges to the `tizen-manifest.xml` file:

    ```XML
    <privileges>
      <!--To access media storage-->
      <privilege>http://tizen.org/privilege/mediastorage</privilege>

      <!--To access, read, and write to the external storage-->
      <privilege>http://tizen.org/privilege/externalstorage</privilege>
    </privileges>
    ```

<a name="construct"></a>
## Pipeline construction

To construct a pipeline, you must have a pipeline description with the [GStreamer](https://gstreamer.freedesktop.org) and [NNStreamer](https://github.com/nnstreamer/nnstreamer) elements.

1. If the model file is located in the resource directory of your own application, you need to get its absolute path:

    ```csharp
    string ResourcePath = Tizen.Applications.Application.Current.DirectoryInfo.Resource;
    string model_path = ResourcePath + "models/mobilenet_v1_1.0_224_quant.tflite";
    ```

2. You can construct a pipeline with the description string, including the neural network framework and a model file:

    ```csharp
    /* Create Pipeline instance with the pipeline description. */
    string description = "appsrc name=srcx ! " +
                         "other/tensor,dimension=(string)3:224:224:1,type=(string)uint8,framerate=(fraction)0/1 ! " +
                         "tensor_filter framework=tensorflow-lite model=" + model_path + " ! " +
                         "tensor_sink name=sinkx";
    Pipeline pipe = new Pipeline(description);
    ```

<a name="inputdata"></a>
## Push input data

`SourceNode` provides a method to push input data into the pipeline:

```csharp
/* Get the source node with the name 'srcx'. */
var src_node = pipe.GetSource("srcx");

/* Start the pipeline. */
pipe.Start();

/* Prepare input tensor data, with data type UInt8 and dimension 3:224:224:1. */
var in_info = new TensorsInfo();
in_info.AddTensorInfo(TensorType.UInt8, new int[4] { 3, 224, 224, 1 });

var in_data = in_info.GetTensorsData();

/* Push input tensor data into the pipeline. */
src_node.Input(in_data);
```

<a name="outputdata"></a>
## Subscribe to output data

You can use `SinkNode` to get the output tensor data from the pipeline:

```csharp
/* Firstly, declare the event handler for the data received event. */
void DataReceivedEvent(object sender, DataReceivedEventArgs args)
{
    /* Add your task with received data. */
    TensorsData dataReceived = args.Data;
}
```

```csharp
/* Get the sink node with the name 'sinkx'. */
var sink_node = pipe.GetSink("sinkx");

/* Subscribe the event to get the data from the sink node. */
sink_node.DataReceived += DataReceivedEvent;

/* Start the pipeline. */
pipe.Start();
```

<a name="dataflow"></a>
## Data flow control

If you need to stop the data stream or select the data flow with multiple stream paths for neural network models, Pipeline provides methods to handle the flow.

1. Start or stop the data flow.

    `Start()` and `Stop()` control the overall data flow of the pipeline asynchronously.
    You can also get the pipeline state from the `State` property:

    ```csharp
    string description = "input-selector name=ins ! tensor_converter ! valve name=valvex ! tensor_sink name=sinkx " +
                         "videotestsrc is-live=true ! videoconvert ! ins.sink_0 " +
                         "videotestsrc is-live=true ! videoconvert ! ins.sink_1";
    var pipe = new Pipeline(description);

    /* After constructing the pipeline, the pipeline state is not 'Playing'. */
    var pipeline_state = pipe.State;

    /* Start the pipeline (The pipeline state will be 'Playing'). */
    pipe.Start();

    /* Stop the pipeline (The pipeline state will be 'Paused'). */
    pipe.Stop();
    ```

2. Open or close the stream.

    The `valve` element controls the stream of a pipeline.
    If you include a `valve` element in the pipeline description, you can get the instance of `ValveNode` with its name.
    It provides a method to let the flow pass to a downstream element, or stop the flow:

    ```csharp
    /* Get the valve node with the name 'valvex'. */
    var valve_node = pipe.GetValve("valvex");

    /* Close valve and stop the flow. */
    valve_node.Control(false);

    /* Start the pipeline (The pipeline state will be 'Playing'). The sink node with the name 'sinkx' cannot receive the data. */
    pipe.Start();
    ```

3. Select the stream path.

    `input-selector` and `output-selector` are the elements to select the data flow with multiple stream paths.
    After getting `SwitchNode` in the pipeline, you can set the input or the output pad for which one gets the data flow:

    ```csharp
    /* Get the switch node with the name 'ins'. */
    var switch_node = pipe.GetSwitch("ins");

    /* Select the pad 'sink_1'. */
    switch_node.Select("sink_1");

    /* Start the pipeline (The pipeline state will be 'Playing'). The input stream from the second video source will be passed to downstream elements. */
    pipe.Start();
    ```

## Custom Filter

For your convenience, NNStreamer provides an interface for processing the tensor data with the `custom-easy` framework. After registering the user-defined callback method with the input and the output tensor information, NNStreamer can manipulate tensor data in the pipeline without an independent shared object. Since the callback method works as **filter** in the pipeline, it is named as `Custom Filter`.

Note that the Custom Filter on the dotnet layer shows relatively lower performance than those of the native layer because of marshaling and unmarshalling between the dotnet and native layer. If your application is mission-critical, then use the native Custom Filter.

1. Define Custom Filter and register it.

    Before you use the Custom Filter in the pipeline, you have to register the Custom Filter with input and output tensor information, and its name:

    ```csharp
    /* Define the Custom Filter method */
    private TensorsData InvokePassThrough(TensorsData inData)
    {
        /* Just Pass through without modification */
        return inData;
    }

    ...

    /* Define input and output tensor information */
    TensorsInfo in_info = new TensorsInfo();
    in_info.AddTensorInfo(TensorType.UInt8, new int[4] { 4, 1, 1, 1 });

    TensorsInfo out_info = new TensorsInfo();
    out_info.AddTensorInfo(TensorType.UInt8, new int[4] { 4, 1, 1, 1 });

    /* Register the Custom Filter with the name 'custom-passthrough' */
    CustomFilter customFilter = CustomFilter.Create("custom-passthrough", in_info, out_info, InvokePassThrough);
    ```

2. Construct a pipeline with Custom Filter.

    After registering the Custom Filter, you can use it when constructing the pipeline:

    ```csharp
    /* framework is 'custom-easy' and registered name is used */
    string desc = "appsrc name=srcx ! other/tensor,dimension=(string)4:1:1:1,type=(string)uint8,framerate=(fraction)0/1 ! " +
                    "tensor_filter framework=custom-easy model=" + customFilter.Name + " ! tensor_sink name=sinkx";

    /* Construct a pipeline and get the source node */
    var pipeline = new Pipeline(desc);
    var src_node = pipeline.GetSource("srcx");

    /* Make an input data */
    var buffer_in = new byte[] { 1, 2, 3, 4 };
    var in_data = in_info.GetTensorsData();
    in_data.SetTensorData(0, buffer_in);

    /* Start the pipeline and feed an input data */
    pipeline.Start();
    src_node.Input(in_data);
    ```

## Get and Set the property of a node

All elements in the pipeline have specific properties and can be manipulated to control the operation of a pipeline. To get and set the property value, you have to get the element node in the pipeline by calling `GetNormal()` method:

```csharp
string desc = "videotestsrc name=vsrc is-live=true ! videoconvert ! videoscale name=vscale ! " +
              "video/x-raw,format=RGBx,width=224,height=224,framerate=60/1 ! tensor_converter ! " +
              "valve name=valvex ! input-selector name=is01 ! tensor_sink name=sinkx";

/* Construct the pipeline */
var pipeline = new Pipeline(desc);

/* Get the videoscale node */
var vscale_node = pipeline.GetNormal("vscale");
```

After getting the node, you can set and get the value of the specific property:

```csharp
/* Set the value of the property 'sharpness' */
vscale_node.SetValue("sharpness", 0.72);

/* Get the value of the property 'sharpness' */
double retSharpness;
vscale_node.GetValue("sharpness", out retSharpness);

/* Get the value of the property 'sharpness' with generic method */
retSharpness = vscale_node.GetValue<double>("sharpness");
```

To figure out the property information of the target element, you can run `gst-inspect-1.0` command on your device as follows:
```Console
$ gst-inspect-1.0 videoscale
...
Element Properties:
  name                : The name of the object
                        flags: readable, writable
                        String. Default: "videoscale0"
  parent              : The parent of the object
                        flags: readable, writable
                        Object of type "GstObject"
  qos                 : Handle Quality-of-Service events
                        flags: readable, writable
                        Boolean. Default: true
  method              : method
                        flags: readable, writable
                        Enum "GstVideoScaleMethod" Default: 1, "bilinear"
                           (0): nearest-neighbour - Nearest Neighbour
                           (1): bilinear         - Bilinear (2-tap)
                           (2): 4-tap            - 4-tap Sinc
                           (3): lanczos          - Lanczos
                           (4): bilinear2        - Bilinear (multi-tap)
                           (5): sinc             - Sinc (multi-tap)
                           (6): hermite          - Hermite (multi-tap)
                           (7): spline           - Spline (multi-tap)
                           (8): catrom           - Catmull-Rom (multi-tap)
                           (9): mitchell         - Mitchell (multi-tap)
  add-borders         : Add black borders if necessary to keep the display aspect ratio
                        flags: readable, writable
                        Boolean. Default: true
  sharpness           : Sharpness of filter
                        flags: readable, writable
                        Double. Range:             0.5 -             1.5 Default:               1
  ...
```


## Related information
- Dependencies
  - Tizen 6.0 and Higher
