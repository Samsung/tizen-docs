# Trainer

ML Trainer API allows you to construct, control, and train a machine learning model on Tizen devices.

The main features of the ML Trainer API include the following:

- Constructing deep neural network (DNN)
   - You can construct a model directly in the code or with a description file.

- Training with your own data
   - ML Trainer API allows you to train a model using data loaded from a file.

- Evaluating the model during training
   - You can easily validate and test your model during the training process by defining the dataset.

> [!NOTE]
> For clarity, errors in the examples are not handled correctly. In production code, take care of all of them to prevent your application from terminating. All errors can be found in [API reference](../../api/latest/device_api/mobile/tizen/ml_trainer.html).

## Prerequisites

To use ML Trainer API, include the following features in your `config.xml` file:

```xml
<feature name="http://tizen.org/feature/machine_learning"/>
<feature name="http://tizen.org/feature/machine_learning.training"/>
```

In case of saving or loading model files from the outside of the application's own resources, the application has to request permission by adding the following privileges to the `config.xml` file:

```xml
<!-- For accessing media storage -->
<tizen:privilege name="http://tizen.org/privilege/mediastorage"/>
<!-- For accessing external storage -->
<tizen:privilege name="http://tizen.org/privilege/externalstorage"/>
<!-- For reading and writing -->
<tizen:privilege name="http://tizen.org/privilege/filesystem.read"/>
<tizen:privilege name="http://tizen.org/privilege/filesystem.write"/>
```

## Build blocks

There are four major components of ML Trainer API, all of which are listed below:
- Model
- Layer
- Optimizer
- Dataset

Let's explore all of them with a simple example.

## Create dataset

Dataset is in charge of feeding data into the model. ML Trainer API supports loading datasets from a file. The file format is described in [the guide for Tizen Native API](../../../native/guides/machine-learning/machine-learning-training#set-a-dataset-from-file):

```javascript
var trainFile = "documents/train.dat";
var validateFile = null;
var testFile = "documents/test.dat";
var dataset = tizen.ml.trainer.createFileDataset(trainFile, validateFile, testFile);
```

Optionally you can [set properties](../../api/7.0/device_api/mobile/tizen/ml_trainer.html#Dataset::setProperty) of the dataset with `setProperty` method:

```javascript
dataset.setProperty("buffer_size", "100", "MODE_TRAIN");
```

## Create model

Model is a wrapper component that has the topology of layers, optimizers, and datasets. The model performs training and saves the updated parameters that can later be used for inference. You can create your model either in the code or from a configuration file.

### Create model in code

Create model object:

```javascript
var model = tizen.ml.trainer.createModel();
```

Add an input layer and set its properties. The shape has the following format: `channels:height:width`. Therefore, if the input is grayscale images of size 28x28, the value for `input_shape` is `1:28:28`:

```javascript
var layer0 = tizen.ml.trainer.createLayer("LAYER_INPUT");
layer0.setProperty("input_shape", "1:28:28");
model.addLayer(layer0);
```

Let's add a few more layers. `input_shape` properties can be omitted as the shapes will be calculated at compile phase. There are many types of layers. All of them and their properties can be found in [the guide for Tizen Native API](../../../native/guides/machine-learning/machine-learning-training#layer):

```javascript
var layer1 = tizen.ml.trainer.createLayer("LAYER_CONV2D");
layer1.setProperty("filters", "32");
layer1.setProperty("kernel_size", "3, 3");
layer1.setProperty("activation", "relu");
model.addLayer(layer1);

var layer2 = tizen.ml.trainer.createLayer("LAYER_POOLING2D");
layer2.setProperty("pooling", "max");
layer2.setProperty("pool_size", "2, 2");
model.addLayer(layer2);

var layer3 = tizen.ml.trainer.createLayer("LAYER_FLATTEN");
model.addLayer(layer3);

var layer4 = tizen.ml.trainer.createLayer("LAYER_FC");
layer4.setProperty("unit", "100");
layer4.setProperty("activation", "relu");
model.addLayer(layer4);

var layer5 = tizen.ml.trainer.createLayer("LAYER_FC");
layer5.setProperty("unit", "10");
layer5.setProperty("activation", "softmax");
model.addLayer(layer5);
```

Add an optimizer to the model. It is used to update the model's weights according to the loss value. All optimizers and their properties can be found in [the guide for Tizen Native API](../../../native/guides/machine-learning/machine-learning-training#optimizer):

```javascript
var optimizer = tizen.ml.trainer.createOptimizer("OPTIMIZER_SGD");
optimizer.setProperty("learning_rate", "0.01");
model.setOptimizer(optimizer);
```

Now compile the model:

```javascript
model.compile({
    loss: "cross",
});
```

You can print the model's structure using `summarize` method:

```javascript
var summary = model.summarize();
console.log(summary);
```

Output:

```
================================================================================
          Layer name          Layer type     Input dimension         Input layer
================================================================================
        layer_input0               input           1:1:28:28
--------------------------------------------------------------------------------
       layer_conv2d1              conv2d           1:1:28:28        layer_input0
--------------------------------------------------------------------------------
 layer_conv2d1/activ          activation          1:32:26:26       layer_conv2d1
--------------------------------------------------------------------------------
    layer_pooling2d2           pooling2d          1:32:26:26 layer_conv2d1/activ
--------------------------------------------------------------------------------
      layer_flatten3             flatten          1:32:25:25    layer_pooling2d2
--------------------------------------------------------------------------------
           layer_fc4     fully_connected         1:1:1:20000      layer_flatten3
--------------------------------------------------------------------------------
 layer_fc4/activatio          activation           1:1:1:100           layer_fc4
--------------------------------------------------------------------------------
           layer_fc5     fully_connected           1:1:1:100 layer_fc4/activatio
--------------------------------------------------------------------------------
      cross_softmax0       cross_softmax            1:1:1:10           layer_fc5
================================================================================
```

### Create model from a configuration file

Configuration file structure is described in [the guide for Tizen Native API](../../../native/guides/machine-learning/machine-learning-training#create-a-model-from-ini-formatted-file). This is a simplified configuration for the model created in the previous section:

```ini
[model]
type = NeuralNetwork
batch_size = 32
epochs = 2

[optimizer]
type = sgd
learning_rate = 0.01

[layer_input0]
type = input
input_shape = 1:28:28

[layer_conv2d1]
type = conv2d
filters = 32
kernel_size = "3, 3"
activation = relu

[layer_pooling2d2]
type = pooling2d
pooling = max
pool_size = "2, 2"

[layer_flatten3]
type = flatten

[layer_fc4]
type = fully_connected
unit = 100
activation = relu

[layer_fc5]
type = fully_connected
unit = 10
activation = softmax
```

To load the configuration use `createModel` function:

```javascript
var configFile = "documents/model.ini";
var model = tizen.ml.trainer.createModel(configFile);
```

Compile the model:

```javascript
model.compile({
    loss: "cross",
});
```

## Training

Connect the dataset to the model:

```javascript
model.setDataset(dataset);
```

Now the model is ready to train. To do that use `run` method:

```javascript
var options = {
    epochs: 2,
    batch_size: 32,
};

function successCallback() {
    console.log("done");
}

function errorCallback(error) {
    console.log(error);
}

model.run(options, successCallback, errorCallback);
```

## Save trained model to a file

The trained model can be saved to a file for future use. Let's use the `FORMAT_INI_WITH_BIN` format, which will produce two files: an `ini` file with the network structure and a binary file with the weights. There are more formats which can be found in [API reference](../../api/7.0/device_api/mobile/tizen/ml_trainer.html#Model::saveToFile). Remember to add proper privileges to the `config.xml` as described in [the prerequisites](#prerequisites):

```javascript
var modelFile = "documents/trained_model.ini";
model.saveToFile(modelFile, "FORMAT_INI_WITH_BIN");
```

## Load trained model from a file

A trained model can be loaded from a file, both its structure and weights. If the model was saved using `FORMAT_INI_WITH_BIN` format, which produces two files, provide a path to the `ini` file. It contains a reference to the binary file with weights. It will be loaded during the compilation phase. Remember to add proper privileges to the `config.xml` as described in [the prerequisites](#prerequisites):

```javascript
var model = tizen.ml.trainer.createModel();
var modelFile = "documents/trained_model.ini";
model.load(modelFile, "FORMAT_INI_WITH_BIN");
model.compile();
```

## Destroy the model

If the model or its elements are not used anymore, they should be destroyed to avoid memory leaks. Disposing a model also destroys all objects associated with it (such as layers):

```javascript
model.dispose();
```

## Use the trained model for inference

The trained model can be loaded using either [ML Single API](./single.md) or [ML Pipeline API](./pipeline.md). This is an example of the first one:

```javascript
var single = tizen.ml.single.openModel("documents/trained_model.ini", null, null, "NNTR_INF", "AUTO");

// ...

single.close();
```

## Related information

- Dependencies
  - Tizen 7.0 and Higher for Mobile
  - Tizen 7.0 and Higher for Wearable
  - Tizen 7.0 and Higher for TV
