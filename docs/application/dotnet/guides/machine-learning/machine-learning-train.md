# Machine Learning Train

You can use the `Tizen.MachineLearning.Train` class to construct, control, and train a machine learning model in Tizen devices.

The main features of machine learning train include the following:

- Constructing a deep neural network (DNN)
  
  You can construct a DNN model using a model description file or by writing code through `Tizen.MachineLearning.Train` class.

- Training with your own data
  
  `Tizen.MachineLearning.Train` class also allows you to train the model with your own data as a file I/O or by defining a data generator.

- Evaluating the model during training
  
  You can validate and test your model during the training process easily by defining the dataset.

> [!NOTE]
> Every example code does not handle all error use cases.
> The error must be handled more extensively compared to the example code written on this page.

## Prerequisites

To enable your application to use `Tizen.MachineLearning.Train` class, follow the steps below:

1. To use the method and properties of the `Tizen.MachineLearning.Train.Model`, `Tizen.MachineLearning.Train.Dataset`, `Tizen.MachineLearning.Train.Layer` and `Tizen.MachineLearning.Train.Optimizer`, include the `Tizen.MachineLearning.Train` namespace in your application:

    ```csharp
    using Tizen.MachineLearning.Train;
    ```

2. To use `Tizen.MachineLearning.Train` class, include the following features in your `tizen-manifest.xml` file:

    ```XML
    <feature name="http://tizen.org/feature/machine_learning">true</feature>
    <feature name="http://tizen.org/feature/machine_learning.training">true</feature>
    ```

   In case of saving or loading model files from outside of the application's own resources, the application has to request permission by adding the following privileges to the `tizen-manifest.xml` file:

    ```XML
    <privileges>
      <!-- For accessing media storage -->
      <privilege>http://tizen.org/privilege/mediastorage</privilege>

      <!-- For accessing external storage -->
      <privilege>http://tizen.org/privilege/externalstorage</privilege>
    </privileges>
    ```

## Building blocks

Following are the four major class of `Tizen.MachineLearning.Train`:

 - [Tizen.MachineLearning.Train.Model](#model-class)
 - [Tizen.MachineLearning.Train.Layer](#layer-class)
 - [Tizen.MachineLearning.Train.Optimizer](#optimizer-class)
 - [Tizen.MachineLearning.Train.Dataset](#dataset-class)

### Model class

`Tizen.MachineLearning.Train.Model` class is a wrapper component that has the topology of `Tizen.MachineLearning.Train.Layer`, `Tizen.MachineLearning.Train.Optimizer`, and `Tizen.MachineLearning.Train.Dataset` class.
`Tizen.MachineLearning.Train.Model` class performs training and saves the updated parameters that can later be used for inference.
In the following figure, `data` represents input data or feature and `label` is the actual value to be tested over prediction:

![model](./media/model.png)

```csharp
// Create model
string filePath = Tizen.Applications.Application.Current.DirectoryInfo.Data;
string binPath = filePath + "model_weights.bin";
string iniPath = filePath + "model.ini";
string iniWithBinPath = filePath + "model_and_weights.ini";

var model = new Model();

/* Configure model(omitted for brevity) */

// Compile model - This freezes the model. Afterwards the model cannot be modified.
model.Compile("loss=cross", "batch_size=16");
// Run model
model.Run("epochs=2");

// Save and load below format.
model.Save(binPath, NNTrainerModelFormat.Bin);
model.Save(iniPath, NNTrainerModelFormat.Ini);
model.Save(iniWithBinPath, NNTrainerModelFormat.iniWithBin);
// Model will be disposed by GC but you can use Dispose() as below.
model.Dispose();
```

A number of properties can be set at `Model.Compile` and `Model.Run` phase:

| Method                       | Key       | Value         | Description                            |
| ---------------------------- | --------- | ------------- | -------------------------------------- |
| `Model.Compile`, `Model.Run` | epochs    | (integer)     | Determines epochs for the model.        |
|                              | save_path | (string)      | Model path to save parameters after a single epoch. |

### Layer class

`Tizen.MachineLearning.Train.Layer` class is a component that does actual computation while managing internal trainable parameters.
The following example shows how to create, add and get the layer to the model:

```csharp
// Create model
var model = new Model();
// Create layer
var fcLayer = new Layer(NNTrainerLayerType.FC);

// Configure layer
fcLayer.SetProperty("unit=10", "activation=softmax", "bias_initializer=zeros", "name=fc100");

// After adding the layer to model, you do not need to destroy layer since ownership is transferred to the model.
model.AddLayer(fcLayer);

// Get layer from the model with the given name.
// The returned layer must not be deleted as it is owned by the model.
string layerName = "fc100";
Layer getLayer = model.GetLayer(layername);
```

There are two types of layers. One type includes commonly trainable weights and the other type does not include them.
The following are the available properties for each layer type which include commonly trainable weights.

Type | Key | Value | Default value | Description
---------- | --- | ----- | ----------- | -----------
(Universal properties)                                       |                             |                             |                         | Universal properties that apply to every layer
&#xfeff;                                                     | name                        | (string)                    |                         | An identifier for each layer
&#xfeff;                                                     | trainable                   | (boolean)                   | true                    | Allow weights to be trained if true
&#xfeff;                                                     | input_layers                | (string)                    |                         | Comma-separated names of layers to be inputs of the current layer
&#xfeff;                                                     | input_shape                 | (string)                    |                         | Comma-separated formatted string as "channel:height:width". If there is no channel then it must be 1. The first layer of the model must have input_shape. Other can be omitted as it is calculated at compile phase.
&#xfeff;                                                     | flatten                     | (boolean)                   |                         | Flatten shape from `c:h:w` to `1:1:c*h*w`
&#xfeff;                                                     | activation                  | (categorical)               |                         | Activation type
&#xfeff;                                                     |                             | tanh                        |                         | Hyperbolic tangent
&#xfeff;                                                     |                             | sigmoid                     |                         | Sigmoid function
&#xfeff;                                                     |                             | relu                        |                         | Relu function
&#xfeff;                                                     |                             | softmax                     |                         | Softmax function
&#xfeff;                                                     | loss                        | (float)                     | 0                       | Loss
&#xfeff;                                                     | weight_initializer          | (categorical)               | xavier_uniform          | Weight initializer
&#xfeff;                                                     |                             | zeros                       |                         | Zero initialization
&#xfeff;                                                     |                             | lecun_normal                |                         | LeCun normal initialization
&#xfeff;                                                     |                             | lecun_uniform               |                         | LeCun uniform initialization
&#xfeff;                                                     |                             | xavier_normal               |                         | Xavier normal initialization
&#xfeff;                                                     |                             | xavier_uniform              |                         | Xavier uniform initialization
&#xfeff;                                                     |                             | he_normal                   |                         | He normal initialization
&#xfeff;                                                     |                             | he_uniform                  |                         | He uniform initialization
&#xfeff;                                                     | bias_initializer            | (categorical)               | zeros                   | Bias initializer
&#xfeff;                                                     |                             | zeros                       |                         | Zero initialization
&#xfeff;                                                     |                             | lecun_normal                |                         | LeCun normal initialization
&#xfeff;                                                     |                             | lecun_uniform               |                         | LeCun uniform initialization
&#xfeff;                                                     |                             | xavier_normal               |                         | Xavier normal initialization
&#xfeff;                                                     |                             | xavier_uniform              |                         | Xavier uniform initialization
&#xfeff;                                                     |                             | he_normal                   |                         | He normal initialization
&#xfeff;                                                     |                             | he_uniform                  |                         | He uniform initialization
&#xfeff;                                                     | weight_regularizer          | (categorical)               |                         | Weight regularizer. Currently, only l2norm is supported
&#xfeff;                                                     |                             | l2norm                      |                         | L2 weight regularizer
&#xfeff;                                                     | weight_regularizer_constant | (float)                     | 1                       | Weight regularizer constant
`NNTrainerLayerType.FC`                                      |                             |                             |                         | Fully connected layer
&#xfeff;                                                     | unit                        | (unsigned integer)          |                         | Number of outputs
`NNTrainerLayerType.Conv1D`                                  |                             |                             |                         | 1D convolution layer
&#xfeff;                                                     | filters                     | (unsigned integer)          |                         | Number of filters
&#xfeff;                                                     | kernel_size                 | (unsigned integer)          |                         | Kernel size
&#xfeff;                                                     | stride                      | (unsigned integer)          | 1                       | Strides
&#xfeff;                                                     | padding                     | (categorical)               | valid                   | Padding type
&#xfeff;                                                     |                             | valid                       |                         | No padding
&#xfeff;                                                     |                             | same                        |                         | Preserve dimension
&#xfeff;                                                     |                             | (unsigned integer)          |                         | Size of padding applied uniformly to all side
&#xfeff;                                                     |                             | (array of unsigned integer of size 2) |                         | Padding for left, right
`NNTrainerLayerType.Conv2D`                                  |                             |                             |                         | 2D convolution layer
&#xfeff;                                                     | filters                     | (unsigned integer)          |                         | Number of filters
&#xfeff;                                                     | kernel_size                 | (array of unsigned integer) |                         | Comma-separated unsigned integers for kernel size, `height, width` respectively
&#xfeff;                                                     | stride                      | (array of unsigned integer) | 1, 1                    | Comma-separated unsigned integers for strides, `height, width` respectively
&#xfeff;                                                     | padding                     | (categorical)               | valid                   | Padding type
&#xfeff;                                                     |                             | valid                       |                         | No padding
&#xfeff;                                                     |                             | same                        |                         | Preserve height/width dimension
&#xfeff;                                                     |                             | (unsigned integer)          |                         | Size of padding applied uniformly to all side
&#xfeff;                                                     |                             | (array of unsigned integer of size 2) |                         | Padding for height, width
&#xfeff;                                                     |                             | (array of unsigned integer of size 4) |                         | Padding for top, bottom, left, right
`NNTrainerLayerType.Embedding`                               |                             |                             |                         | Embedding layer
&#xfeff;                                                     | in_dim                      | (unsigned integer)          |                         | Vocabulary size
&#xfeff;                                                     | out_dim                     | (unsigned integer)          |                         | Word embedding size
`NNTrainerLayerType.RNN`                                     |                             |                             |                         | RNN layer
&#xfeff;                                                     | unit                        | (unsigned integer)          |                         | Number of output neurons
&#xfeff;                                                     | hidden_state_activation     | (categorical)               | tanh                    | Activation type
&#xfeff;                                                     |                             | tanh                        |                         | Hyperbolic tangent
&#xfeff;                                                     |                             | sigmoid                     |                         | Sigmoid function
&#xfeff;                                                     |                             | relu                        |                         | Relu function
&#xfeff;                                                     |                             | softmax                     |                         | Softmax function
&#xfeff;                                                     | return_sequences            | (boolean)                   | false                   | Return only the last output if true, else return full output
&#xfeff;                                                     | dropout                     | (float)                     | 0                       | Dropout rate
&#xfeff;                                                     | integrate_bias              | (boolean)                   | false                   | Integrate bias_ih, bias_hh to bias_h
`NNTrainerLayerType.RNNCell`                                 |                             |                             |                         | RNN cell layer
&#xfeff;                                                     | unit                        | (unsigned integer)          |                         | Number of output neurons
&#xfeff;                                                     | hidden_state_activation     | (categorical)               | tanh                    | Activation type
&#xfeff;                                                     |                             | tanh                        |                         | Hyperbolic tangent
&#xfeff;                                                     |                             | sigmoid                     |                         | Sigmoid function
&#xfeff;                                                     |                             | relu                        |                         | Relu function
&#xfeff;                                                     |                             | softmax                     |                         | Softmax function
&#xfeff;                                                     | dropout                     | (float)                     | 0                       | Dropout rate
&#xfeff;                                                     | integrate_bias              | (boolean)                   | false                   | Integrate bias_ih, bias_hh to bias_h
`NNTrainerLayerType.LSTM`                                    |                             |                             |                         | LSTM layer
&#xfeff;                                                     | unit                        | (unsigned integer)          |                         | Number of output neurons
&#xfeff;                                                     | hidden_state_activation     | (categorical)               | tanh                    | Activation type
&#xfeff;                                                     |                             | tanh                        |                         | Hyperbolic tangent
&#xfeff;                                                     |                             | sigmoid                     |                         | Sigmoid function
&#xfeff;                                                     |                             | relu                        |                         | Relu function
&#xfeff;                                                     |                             | softmax                     |                         | Softmax function
&#xfeff;                                                     | recurrent_activation        | (categorical)               | sigmoid                 | Activation type for recurrent step
&#xfeff;                                                     |                             | tanh                        |                         | Hyperbolic tangent
&#xfeff;                                                     |                             | sigmoid                     |                         | Sigmoid function
&#xfeff;                                                     |                             | relu                        |                         | Relu function
&#xfeff;                                                     |                             | softmax                     |                         | Softmax function
&#xfeff;                                                     | return_sequences            | (boolean)                   | false                   | Return only the last output if true, else return full output
&#xfeff;                                                     | dropout                     | (float)                     | 0                       | Dropout rate
&#xfeff;                                                     | integrate_bias              | (boolean)                   | false                   | Integrate bias_ih, bias_hh to bias_h
&#xfeff;                                                     | max_timestep                | (unsigned integer)          |                         | Maximum timestep
`NNTrainerLayerType.LSTMCell`                                |                             |                             |                         | LSTM cell layer
&#xfeff;                                                     | unit                        | (unsigned integer)          |                         | Number of output neurons
&#xfeff;                                                     | hidden_state_activation     | (categorical)               | tanh                    | Activation type
&#xfeff;                                                     |                             | tanh                        |                         | Hyperbolic tangent
&#xfeff;                                                     |                             | sigmoid                     |                         | Sigmoid function
&#xfeff;                                                     |                             | relu                        |                         | Relu function
&#xfeff;                                                     |                             | softmax                     |                         | Softmax function
&#xfeff;                                                     | recurrent_activation        | (categorical)               | sigmoid                 | Activation type for recurrent step
&#xfeff;                                                     |                             | tanh                        |                         | Hyperbolic tangent
&#xfeff;                                                     |                             | sigmoid                     |                         | Sigmoid function
&#xfeff;                                                     |                             | relu                        |                         | Relu function
&#xfeff;                                                     |                             | softmax                     |                         | Softmax function
&#xfeff;                                                     | dropout                     | (float)                     | 0                       | Dropout rate
&#xfeff;                                                     | integrate_bias              | (boolean)                   | false                   | Integrate bias_ih, bias_hh to bias_h
`NNTrainerLayerType.GRU`                                     |                             |                             |                         | GRU layer
&#xfeff;                                                     | unit                        | (unsigned integer)          |                         | Number of output neurons
&#xfeff;                                                     | hidden_state_activation     | (categorical)               | tanh                    | Activation type
&#xfeff;                                                     |                             | tanh                        |                         | Hyperbolic tangent
&#xfeff;                                                     |                             | sigmoid                     |                         | Sigmoid function
&#xfeff;                                                     |                             | relu                        |                         | Relu function
&#xfeff;                                                     |                             | softmax                     |                         | Softmax function
&#xfeff;                                                     | recurrent_activation        | (categorical)               | sigmoid                 | Activation type for recurrent step
&#xfeff;                                                     |                             | tanh                        |                         | Hyperbolic tangent
&#xfeff;                                                     |                             | sigmoid                     |                         | Sigmoid function
&#xfeff;                                                     |                             | relu                        |                         | Relu function
&#xfeff;                                                     |                             | softmax                     |                         | Softmax function
&#xfeff;                                                     | return_sequences            | (boolean)                   | false                   | Return only the last output if true, else return full output
&#xfeff;                                                     | dropout                     | (float)                     | 0                       | Dropout rate
&#xfeff;                                                     | integrate_bias              | (boolean)                   | false                   | Integrate bias_ih, bias_hh to bias_h
&#xfeff;                                                     | reset_after                 | (boolean)                   | true                    | Apply reset gate before/after the matrix
`NNTrainerLayerType.GRUCell`                                 |                             |                             |                         | GRU cell layer
&#xfeff;                                                     | unit                        | (unsigned integer)          |                         | Number of output neurons
&#xfeff;                                                     | reset_after                 | (boolean)                   | true                    | Apply reset gate before/after the matrix multiplication
&#xfeff;                                                     | hidden_state_activation     | (categorical)               | tanh                    | Activation type
&#xfeff;                                                     |                             | tanh                        |                         | Hyperbolic tangent
&#xfeff;                                                     |                             | sigmoid                     |                         | Sigmoid function
&#xfeff;                                                     |                             | relu                        |                         | Relu function
&#xfeff;                                                     |                             | softmax                     |                         | Softmax function
&#xfeff;                                                     | recurrent_activation        | (categorical)               | sigmoid                 | Activation type for recurrent step
&#xfeff;                                                     |                             | tanh                        |                         | Hyperbolic tangent
&#xfeff;                                                     |                             | sigmoid                     |                         | Sigmoid function
&#xfeff;                                                     |                             | relu                        |                         | Relu function
&#xfeff;                                                     |                             | softmax                     |                         | Softmax function
&#xfeff;                                                     | dropout                     | (float)                     | 0                       | Dropout rate
&#xfeff;                                                     | integrate_bias              | (boolean)                   | false                   | Integrate bias_ih, bias_hh to bias_h
`NNTrainerLayerType.ZoneoutLSTMCell`                         |                             |                             |                         | Zoneout LSTM cell layer
&#xfeff;                                                     | unit                        | (unsigned integer)          |                         | Number of output neurons
&#xfeff;                                                     | hidden_state_activation     | (categorical)               | tanh                    | Activation type
&#xfeff;                                                     |                             | tanh                        |                         | Hyperbolic tangent
&#xfeff;                                                     |                             | sigmoid                     |                         | Sigmoid function
&#xfeff;                                                     |                             | relu                        |                         | Relu function
&#xfeff;                                                     |                             | softmax                     |                         | Softmax function
&#xfeff;                                                     | recurrent_activation        | (categorical)               | sigmoid                 | Activation type for recurrent step
&#xfeff;                                                     |                             | tanh                        |                         | Hyperbolic tangent
&#xfeff;                                                     |                             | sigmoid                     |                         | Sigmoid function
&#xfeff;                                                     |                             | relu                        |                         | Relu function
&#xfeff;                                                     |                             | softmax                     |                         | Softmax function
&#xfeff;                                                     | cell_state_zoneout_rate     | (float)                     | 0                       | Zoneout rate for cell state
&#xfeff;                                                     | hidden_state_zoneout_rate   | (float)                     | 0                       | Zoneout rate for hidden state
&#xfeff;                                                     | integrate_bias              | (boolean)                   | false                   | Integrate bias_ih, bias_hh to bias_h
&#xfeff;

The following are the available properties for each layer type which do not include (`weight_initializer`, `bias_initializer`, `weight_regularizer`, `weight_regularizer_constant`) properties.

Type | Key | Value | Default value | Description
---------- | --- | ----- | ----------- | -----------
(Universal properties)                                       |                             |                             |                         | Universal properties that apply to every layer
&#xfeff;                                                     | name                        | (string)                    |                         | An identifier for each layer
&#xfeff;                                                     | trainable                   | (boolean)                   | true                    | Allow weights to be trained if true
&#xfeff;                                                     | input_layers                | (string)                    |                         | Comma-separated names of layers to be inputs of the current layer
&#xfeff;                                                     | input_shape                 | (string)                    |                         | Comma-separated formatted string as "channel:height:width". If there is no channel then it must be 1. First layer of the model must have input_shape. Other can be omitted as it is calculated at compile phase.
&#xfeff;                                                     | flatten                     | (boolean)                   |                         | Flatten shape from `c:h:w` to `1:1:c*h*w`
&#xfeff;                                                     | activation                  | (categorical)               |                         | Activation type
&#xfeff;                                                     |                             | tanh                        |                         | Hyperbolic tangent
&#xfeff;                                                     |                             | sigmoid                     |                         | Sigmoid function
&#xfeff;                                                     |                             | relu                        |                         | Relu function
&#xfeff;                                                     |                             | softmax                     |                         | Softmax function
&#xfeff;                                                     | loss                        | (float)                     | 0                       | Loss
`NNTrainerLayerType.Input`                                   |                             |                             |                         | Input layer
&#xfeff;                                                     | normalization               | (boolean)                   | false                   | Normalize input if true
&#xfeff;                                                     | standardization             | (boolean)                   | false                   | Standardize input if true
`NNTrainerLayerType.BN`                                      |                             |                             |                         | Batch normalization layer
&#xfeff;                                                     | epsilon                     | (float)                     | 0.001                   | Small value to avoid dividing by zero
&#xfeff;                                                     | moving_mean_initializer     | (categorical)               | zeros                   | Moving mean initializer
&#xfeff;                                                     |                             | zeros                       |                         | Zero initialization
&#xfeff;                                                     |                             | lecun_normal                |                         | LeCun normal initialization
&#xfeff;                                                     |                             | lecun_uniform               |                         | LeCun uniform initialization
&#xfeff;                                                     |                             | xavier_normal               |                         | Xavier normal initialization
&#xfeff;                                                     |                             | xavier_uniform              |                         | Xavier uniform initialization
&#xfeff;                                                     |                             | he_normal                   |                         | He normal initialization
&#xfeff;                                                     |                             | he_uniform                  |                         | He uniform initialization
&#xfeff;                                                     | moving_variance_initializer | (categorical)               | ones                    | Moving variance initializer
&#xfeff;                                                     |                             | zeros                       |                         | Zero initialization
&#xfeff;                                                     |                             | lecun_normal                |                         | LeCun normal initialization
&#xfeff;                                                     |                             | lecun_uniform               |                         | LeCun uniform initialization
&#xfeff;                                                     |                             | xavier_normal               |                         | Xavier normal initialization
&#xfeff;                                                     |                             | xavier_uniform              |                         | Xavier uniform initialization
&#xfeff;                                                     |                             | he_normal                   |                         | He normal initialization
&#xfeff;                                                     |                             | he_uniform                  |                         | He uniform initialization
&#xfeff;                                                     | gamma_initializer           | (categorical)               | ones                    | Gamma initializer
&#xfeff;                                                     |                             | zeros                       |                         | Zero initialization
&#xfeff;                                                     |                             | lecun_normal                |                         | LeCun normal initialization
&#xfeff;                                                     |                             | lecun_uniform               |                         | LeCun uniform initialization
&#xfeff;                                                     |                             | xavier_normal               |                         | Xavier normal initialization
&#xfeff;                                                     |                             | xavier_uniform              |                         | Xavier uniform initialization
&#xfeff;                                                     |                             | he_normal                   |                         | He normal initialization
&#xfeff;                                                     |                             | he_uniform                  |                         | He uniform initialization
&#xfeff;                                                     | beta_initializer            | (categorical)               | zeros                   | Beta initializer
&#xfeff;                                                     |                             | zeros                       |                         | Zero initialization
&#xfeff;                                                     |                             | lecun_normal                |                         | LeCun normal initialization
&#xfeff;                                                     |                             | lecun_uniform               |                         | LeCun uniform initialization
&#xfeff;                                                     |                             | xavier_normal               |                         | Xavier normal initialization
&#xfeff;                                                     |                             | xavier_uniform              |                         | Xavier uniform initialization
&#xfeff;                                                     |                             | he_normal                   |                         | He normal initialization
&#xfeff;                                                     |                             | he_uniform                  |                         | He uniform initialization
&#xfeff;                                                     | momentum                    | (float)                     | 0.99                    | Momentum for moving average in batch normalization
`NNTrainerLayerType.Pooling2D`                               |                             |                             |                         | Pooling layer
&#xfeff;                                                     | pooling                     | (categorical)               |                         | Pooling type
&#xfeff;                                                     |                             | max                         |                         | Max pooling
&#xfeff;                                                     |                             | average                     |                         | Average pooling
&#xfeff;                                                     |                             | global_max                  |                         | Global max pooling
&#xfeff;                                                     |                             | global_average              |                         | Global average pooling
&#xfeff;                                                     | pool_size                   | (array of unsigned integer) |                         | Comma-separated unsigned integers for pooling size, `height, width`  respectively
&#xfeff;                                                     | stride                      | (array of unsigned integer) | 1, 1                    | Comma-separated unsigned integers for stride, `height, width`  respectively
&#xfeff;                                                     | padding                     | (categorical)               | valid                   | Padding type
&#xfeff;                                                     |                             | valid                       |                         | No padding
&#xfeff;                                                     |                             | same                        |                         | Preserve height/width dimension
&#xfeff;                                                     |                             | (unsigned integer)          |                         | Size of padding applied uniformly to all side
&#xfeff;                                                     |                             | (array of unsigned integer of size 2) |                         | Padding for height, width
&#xfeff;                                                     |                             | (array of unsigned integer of size 4) |                         | Padding for top, bottom, left, right
`NNTrainerLayerType.Flatten`                                 |                             |                             |                         | Flatten layer
`NNTrainerLayerType.Activation`                              |                             |                             |                         | Activation layer
&#xfeff;                                                     | activation                  | (categorical)               |                         | Activation type
&#xfeff;                                                     |                             | tanh                        |                         | Hyperbolic tangent
&#xfeff;                                                     |                             | sigmoid                     |                         | Sigmoid function
&#xfeff;                                                     |                             | relu                        |                         | Relu function
&#xfeff;                                                     |                             | softmax                     |                         | Softmax function
`NNTrainerLayerType.Addition`                                |                             |                             |                         | Addition layer
`NNTrainerLayerType.Concat`                                  |                             |                             |                         | Concat layer
`NNTrainerLayerType.MultiOut`                                |                             |                             |                         | Multiout layer
`NNTrainerLayerType.Split`                                   |                             |                             |                         | Split layer
&#xfeff;                                                     | split_dimension             | (unsigned integer)          |                         | Which dimension to split. Split batch dimension is not allowed
`NNTrainerLayerType.Permute`                                 |                             |                             |                         | Permute layer
`NNTrainerLayerType.Dropout`                                 |                             |                             |                         | Dropout layer
&#xfeff;                                                     | dropout                     | (float)                     | 0                       | Dropout rate
`NNTrainerLayerType.BackboneNNStreamer`                      |                             |                             |                         | NNStreamer layer
&#xfeff;                                                     | model_path                  | (string)                    |                         | NNStreamer model path
`NNTrainerLayerType.CentroidKNN`                             |                             |                             |                         | Centroid KNN layer
&#xfeff;                                                     | num_class                   | (unsigned integer)          |                         | Number of class
`NNTrainerLayerType.PreprocessFlip`                          |                             |                             |                         | Preprocess flip layer
&#xfeff;                                                     | flip_direction              | (categorical)               |                         | Flip direction
&#xfeff;                                                     |                             | horizontal                  |                         | Horizontal direction
&#xfeff;                                                     |                             | vertical                    |                         | Vertical direction
&#xfeff;                                                     |                             | horizontal_and_vertical     | horizontal_and_vertical | Horizontal and vertical direction
`NNTrainerLayerType.PreprocessTranslate`                     |                             |                             |                         | Preprocess translate layer
&#xfeff;                                                     | random_translate            | (float)                     |                         | Translate factor value
`NNTrainerLayerType.PreprocessL2Norm`                        |                             |                             |                         | Preprocess l2norm layer
`NNTrainerLayerType.LoseMSE`                                 |                             |                             |                         | MSE loss layer
`NNTrainerLayerType.LossCrossEntropySigmoid`                 |                             |                             |                         | Cross entropy with sigmoid loss layer
`NNTrainerLayerType.LossCrossEntropySoftmax`                 |                             |                             |                         | Cross entropy with softmax loss layer

### Optimizer class

`Tizen.MachineLearning.Train.Optimizer` class determines how to update model parameters according to loss from prediction.
Currently, Stochastic Gradient Descent optimizer and Adam optimizer are supported:

```csharp
// Create model
var model = new Model();

// Create optimizer
var optimizer = new Oprimizer(NNTrainerOptimizerType.SGD);

// Configure an optimizer
optimizer.SetProperty("beta1=0.002", "beta2=0.001");

// Set optimizer to the model
// No need to destroy optimizer after setting optimizer since the ownership is transferred to the model.
model.SetOptimizer(optimizer);
```

Following are the available properties for each optimizer type:

| Type                           | Key           | value   | Description                                    |
| ------------------------------ | ------------- | ------- | ---------------------------------------------- |
| (Universal properties)         |               |         | Universal properties that apply to every layer |
| &#xfeff;                       | learning_rate | (float) | Initial learning rate for the optimizer        |
| `NNTrainerOptimizerType.SGD`   |               |         | Stochastic Gradient Descent optimizer          |
| &#xfeff;                       | decay_steps   | (float) | Decay steps                                    |
| &#xfeff;                       | decay_rate    | (float) | Decay rate                                     |
| `NNTrainerOptimizerType.Adam`  |               |         | Adam optimizer                                 |
| &#xfeff;                       | decay_steps   | (float) | Decay steps                                    |
| &#xfeff;                       | decay_rate    | (float) | Decay rate                                     |
| &#xfeff;                       | beta1         | (float) | Beta1 coefficient for Adam                     |
| &#xfeff;                       | beta2         | (float) | Beta2 coefficient for Adam                     |
| &#xfeff;                       | epsilon       | (float) | Epsilon coefficient for Adam                   |

### Dataset class

`Tizen.MachineLearning.Train.Dataset` class is in charge of feeding data into the model.
The dataset can be created from a file.
For more information, see [configure the model](#configure-the-model) section.

The following code is an example of handling `Tizen.MachineLearning.Train.Dataset` class:

```csharp
string datasetFilePath = Tizen.Applications.Application.Current.DirectoryInfo.Data + "trainingSet.dat";

NNTrainerDatasetMode[] datasetMode = new NNTrainerDatasetMode[] {
  NNTrainerDatasetMode.Test,
  NNTrainerDatasetMode.Train,
  NNTrainerDatasetMode.Valid
};

// Create dataset
var dataset = new Dataset();

for (int i = 0; i < 3; i++)
{
    dataset.AddFile(datasetMode[i], datasetFilePath);
    // configure dataset
    dataset.SetProperty(datasetMode[i], "buffer_size=1");
}

// after setting a dataset to model,
// you do not need to destroy dataset since ownership is transferred to the model.
model.SetDataset(dataset);
```

## Construct a model

A model can be constructed with the given configuration file.
If you have a model configuration file that describes the model, the file can be used to construct initially with `Tizen.MachineLearning.Train.Model(string modelConf)`.
Even if the model is constructed from a file, switching, modifying, or setting a component is possible until you compile with `Tizen.MachineLearning.Train.Model.Compile()`.

### Construct a model from a description file

As of now, only INI formatted files `*.ini` are supported to construct a model from a file.

#### Create a model from INI formatted file

Special sections `[Model]`, `[Optimizers]`, `[train_set]`, `[valid_set]`, `[test_set]` are respectively referring to `model`, `optimizer` and data provider objects.
Rest of INI sections map to a `layer`. Keys and values from each section set properties of the layer.
All keys and values are treated as case-insensitive.

Following is an example of the `*.ini` file:

```ini
[Model] # Special section that describes model itself
Type = NeuralNetwork  # Model type : only NeuralNetwork is supported as of now
batch_size = 9

####  Model run related properties
Epochs = 20     # Epochs

[Optimizer]
Type = adam  # Optimizer : Adaptive Moment Estimation(adam)
Learning_rate = 0.0001  # Learning rate for the optimizer
Decay_rate = 0.96 # The decay rate for decaying the learning rate
Decay_steps = 1000       # decay step for the exponentially decayed learning rate
beta1 = 0.9     # beta 1 for adam
beta2 = 0.9999  # beta 2 for adam
epsilon = 1e-7  # epsilon for adam

[train_set]
Type = file
BufferSize = 9
path = "trainingSet.dat"

[valid_set]
Type = file
path = "valSet.dat"

# Add [test_set] section if applicable

# Layer Sections, each section name refers to name of the layer
[inputlayer]
Type = input
Input_Shape = 1:1:62720 # Input dimension in channel:height:width
Normalization = true

[outputlayer]
Type = fully_connected
Unit = 2    # Width of output dimension
bias_initializer = zeros
weight_initializer = xavier_uniform
Activation = sigmoid  # activation : sigmoid, softmax
weight_regularizer = l2norm
weight_regularizer_constant = 0.005
input_layers = inputlayer

[loss]
Type = cross # Define loss as a layer
```

The following restrictions must be adhered to:

 - Model file must have a `[Model]` section.
 - Model file must have at least one layer.
 - Valid keys must have valid properties. The invalid keys in each section result in an error.

> [!NOTE]
> All paths inside the INI file are relative to the INI file path unless the absolute path is stated.
> Consider setting `save_path`, `train_set`, `valid_set`, and `test_set` from the code rather than describing inside the model file to avoid this behavior.

The following example constructs model from INI file:

```csharp
string configurePath = Tizen.Applications.Application.Current.DirectoryInfo.Resource + "model.ini";

try
{
  var model = new Model(configurePath);
}
catch (Exception e)
{
  // handle error
}
```

### Construct a model on code

An empty model can be constructed with `Tizen.MachineLearning.Train.Model()`.

## Configure the model

After constructing a model, the model can be configured by following the steps as described below:

> [!NOTE]
> The example code written here reproduces the model description from [create a model from INI formatted file](#create-a-model-from-ini-formatted-file) except the following is different:
> - Relative path is changed to dynamic app resource and data path.
> - Model related properties that can only be set at compile or run phase.

First, an empty model needs to be created:

```csharp
try
{
  var model = new Model();
}
catch (Exception e)
{
  //handle error
}
```

### Add a layer

`Tizen.MachineLearning.Train.Model.AddLayer` appends a layer to the end of the graph in the model:

```csharp
try
{
  var inputLayer = new Layer(NNTrainerLayerType.Input);
  inputLayer.SetProperty("name=inputlayer", "input_shape=1:1:62720", "normalization=true");
  model.AddLayer(inputLayer);

  var fcLayer = new Layer(NNTrainerLayerType.FC);
  fcLayer.SetProperty("name=outputlayer", "unit=2", "bias_initializer=zeros", "weight_initializer=xavier_uniform", "activation=sigmoid");
  model.AddLayer(fcLayer);
}
catch (Exception e)
{
  //handle error
}
```

### Get a layer

`Tizen.MachineLearning.Train.Model.GetLayer` gets a layer from the model with the given name:

```csharp
try
{
  // Constructs the neural network model
  var model = new Model();
  // Creates and add a neural network layer
  var inputLayer = new Layer(NNTrainerLayerType.Input);
  // Set a name for the layer
  inputLayer.SetProperty("name=inputlayer");
  // Adds layer in neural network model
  model.AddLayer(inputLayer);
  // Get layer from the model with the given name.
  // The returned layer must not be deleted as it is owned by the model.
  string layerName = "inputlayer";
  Layer getLayer = model.GetLayer(layername);
}
catch (Exception e)
{
  //handle error
}
```

### Set an optimizer
Create an optimizer using `Tizen.MachineLearning.Train.Optimizer` class and set it to the model. The manner is the same as for `Tizen.MachineLearning.Train.Layer` class:

```csharp
try
{
  var model = new Model();
  // Create an optimizer
  var optimizer = new Optimizer(NNTrainerOptimizerType.Adam);
  // Configure a optimizer
  optimizer.SetProperty("learning_rate=0.0001", "decay_rate=0.96", "decay_steps=1000", "beta1=0.002", "beta2=0.001", "epsilon=1e-7");
  // Set optimizer to the model
  model.SetOptimizer(optimizer);
}
catch (Exception e)
{
  //handle error
}
```

### Set a dataset
The dataset can be created from a file. Here, you need to provide streams of tensor data and arrays of values representing the label, usually one-hot encoded.

#### Sample, batch, and epoch

This section explains the following three concepts: sample, batch, and epoch.

Let's assume a given model requires three inputs and two labels. This has been reflected in the examples below:

1. Sample

    A sample denotes a single pair of inputs/labels. The example can be as follows:

    ```
    [input_1][input_2][input_3][label_1][label_2]
    ```

2. Batch

    A batch is a bundle of samples which is fed to a single iteration. If a batch is of size 5, the batch layout, where `/*` denotes nth sample will be as follows:

    ```
    [[input_1/1][input_1/2][input_1/3][input_1/4][input_1/5]],
    [[input_2/1][input_2/2][input_2/3][input_2/4][input_2/5]],
    [[input_3/1][input_3/2][input_3/3][input_3/4][input_3/5]],
    [[label_1/1][label_1/2][label_1/3][label_1/4][label_1/5]],
    [[label_2/1][label_2/2][label_2/3][label_2/4][label_2/5]],
    ```

3. Epoch

    An epoch refers to a full, exhaustive visit to a dataset.

    So, if you consider [Cifar-100](https://www.cs.toronto.edu/~kriz/cifar.html#The%20CIFAR-100%20dataset){:target="_blank"} dataset when using the full training set, a single training epoch will contain 50,000 samples. If the batch size is 100, it will be of 500 batches (or iterations).

#### Construct a dataset on code

An empty dataset can be constructed with `Tizen.MachineLearning.Train.Dataset` class.
A data provider added with `NNTrainerDatasetMode.Train`, `NNTrainerDatasetMode.Valid`, `NNTrainerDatasetMode.Test` will be used when training, validating, and testing respectively.

Consider setting property with `Tizen.MachineLearning.Train.Dataset.SetProperty` when the data provider needs certain properties.

#### Set a dataset from file

To create a dataset from files, each file must contain an array of samples.
A single sample consists of an array of raw float array for input and another array or raw float array for labels that contains the same size as model output:

```
# If a model requires two inputs and a single label for a sample, a single sample would contain...
[[float array for input1][input 2][float array for label1]],
...,
[[float array for input1][input 2][float array for label1]]
```

As an example, again, consider the [Cifar-100](https://www.cs.toronto.edu/~kriz/cifar.html#The%20CIFAR-100%20dataset){:target="_blank"} dataset.
In Cifar-100 data, it contains an image of size 3 * 32 * 32 and a coarse label of 20 classes, and a fine label of 100 classes.

If your model requires an image and two labels (coarse, fine) both one-hot encoded for a sample, the file layout would be:
```
[[3072 pixels][20 floats for coarse label][100 floats for fine label]],
...
...
[[3072 pixels][20 floats for coarse label][100 floats for fine label]]
```

After preparing the file, create dataset as follows:

```csharp

string datasetFilePath = Tizen.Applications.Application.Current.DirectoryInfo.Data + "trainingSet.dat";

try
{
  var model = new Model();
  var dataset = new Dataset();
  // a file data provider to be used for training
  dataset.AddFile(NNTrainerDatasetMode.Train, datasetFilePath);
  dataset.SetProperty(NNTrainerDatasetMode.Train, "buffer_size=9");

  model.SetDataset(dataset);
}
catch (Exception e)
{
  // handle error
}
```
The property `buffer_size` defines the maximum amount of batches to be queued while training. When it is not given, it is set to 1.

## Compile the model

Compiling a model finalizes the model with loss.
Once compiled, any modification to the properties of the model is restricted.
Adding layers or changing the optimizer or dataset of the model is not permitted either:

```csharp
try
{
  model.Compile("loss=cross");
}
catch (Exception e)
{
  // handle error
}
```

## Train the model

Now, the model is ready to train. Train model as follows:

```csharp
try
{
  model.Run("batch_size=9", "epochs=20");
}
catch (Exception e)
{
  // handle error
}
```
## Destroy the model

Model will be disposed by GC, but you can use `Dispose()` method.
`Tizen.MachineLearning.Train.Model.AddLayer`, `Tizen.MachineLearning.Train.Model.SetOptimizer`, and `Tizen.MachineLearning.Train.Model.SetDataset` transfers ownership to the model.
`Tizen.MachineLearning.Train.Layer`, `Tizen.MachineLearning.Train.Optimizer` and `Tizen.MachineLearning.Train.Dataset` that belongs to the `model` are also deleted.

## Use the trained model for inference

The trained model can be used for inference with Machine Learning Inference APIs.
Ensure that the INI file contains the correct weight file in `save_path` in `[Model]` section.
The valid INI file can be made with`Tizen.MachineLearning.Train.Model.Save` if you have constructed the model with the provided method.
For example, you can use the trained model with a single API as follows:

```csharp
using Tizen.MachineLearning.Inference;

TensorInfo inInfo;
TensorInfo outInfo;
string modelFilePath = Tizen.Applications.Application.Current.DirectoryInfo.Data + "modelFile.ini";
...

var single = new SingleShot(modelFilePath, inInfo, outInfo);
```

You can use the trained model with Pipeline API as follows:

```csharp
using Tizen.MachineLearning.Inference;

/* framework is 'nntrainer'*/
const string description = "appsrc ! other/tensor,dimension=(string)2:1:1:1,type=(string)  int8,framerate=(fraction)0/1 ! tensor_filter framework=nntrainer model=model.ini ! tensor_sink";

var pipeline = new Pipeline(description);
```
## Related information

- Dependencies
  - Tizen 7.0 and Higher