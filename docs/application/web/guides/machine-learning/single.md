# Single

You can use the Single API to load the existing neural network model from the storage. After loading the model, you can invoke it with a single instance of input data. Then, you can get the inference output result.

The main features of the Single API include:

- Loading a neural network model

  You can [open the neural network model](#open-the-model) from storage and configure a runtime environment.

- Invoking the neural network model

  After creating the `SingleShot` instance, you can invoke the model [synchronously](#invoke) or [asynchronously](#invoke-asynchronously) with the input data and get the inference output result.

- Fetching the inference result

  You can [fetch the inference result](#fetch-the-result) after invoking the respective model.

## Prerequisites

To access files using the Single API (in [mobile](../../api/latest/device_api/mobile/tizen/ml_single.html), [wearable](../../api/latest/device_api/wearable/tizen/ml_single.html), and [TV](../../api/latest/device_api/tv/tizen/ml_single.html) applications), the application has to request storage privileges by adding the following privileges to the `config.xml` file:

  ```xml
  <!-- for accessing internal storage only -->
  <tizen:privilege name="http://tizen.org/privilege/mediastorage"/>
  <!-- for accessing external storage only -->
  <tizen:privilege name="http://tizen.org/privilege/externalstorage"/>
  ```

Additionally, to access files using the Single API (in [mobile](../../api/latest/device_api/mobile/tizen/ml_single.html) and [wearable](../../api/latest/device_api/wearable/tizen/ml_single.html) applications), the application has to request [proper storage permissions](../security/privacy-related-permissions.md) using the PPM API (in [mobile](../../api/latest/device_api/mobile/tizen/ppm.html) and [wearable](../../api/latest/device_api/wearable/tizen/ppm.html) applications).

## Open the model

1. To load the model from storage, use `openModel`:
    ```javascript
    var model = tizen.ml.single.openModel("documents/mobilenet_v1_1.0_224_quant.tflite");
    ```

2. If the model supports dynamic tensors, you can:

    - provide custom input and output tensors:
        ```javascript
        var input = new tizen.ml.TensorsInfo()
        input.addTensorInfo("input", "FLOAT32", [3])
        var output = new tizen.ml.TensorsInfo()
        output.addTensorInfo("output", "FLOAT32", [3])
        var model = tizen.ml.single.openModel("documents/dynamic.tflite", input, output);
        input.dispose();
        output.dispose();
        ```

    - set the model's `input` tensor:
        ```javascript
        var input = new tizen.ml.TensorsInfo()
        input.addTensorInfo("input", "FLOAT32", [3])
        model.input = input;
        input.dispose();
        ```

    - open model in dynamic mode to change input data format, if the model supports changing it:

        ```javascript
        var model = tizen.ml.single.openModel("documents/mobilenet_v1_1.0_224_quant.tflite", null, null, "ANY", "ANY", true);
        ```

3. You can also provide parameters that define the framework and hardware for your model:

    ```javascript
    var model = tizen.ml.single.openModel("documents/mobilenet_v1_1.0_224_quant.tflite", null, null, "TENSORFLOW_LITE", "ANY");
    ```

4. Ensure to close `SingleShot` objects when you do not need them anymore:

    ```javascript
    model.close()
    ```

5. You can also open the model asynchronously with `openModelAsync`. Doing so avoids blocking UI when opening the big model file:

    ```javascript
    function errorCallback(error)
    {
      console.log("Error while opening model: " + error.message);
    }

    function successCallback(model)
    {
      console.log("Model opened successfully");

      // Do inference here

      model.close();
    }
    tizen.ml.single.openModelAsync("documents/mobilenet_v1_1.0_224_quant.tflite", successCallback, errorCallback);
    ```

## Invoke

To invoke the neural network model, you need to create the `TensorsData` instance to pass the input data to the model. You can find the details about using `TensorsData` interface in [Tensors Management](./tensors.md) guide:

1. Create the `TensorsData` object based on the information from the model:

    ```javascript
    var inputTensorsInfo = model.input;
    var inputTensorsData = inputTensorsInfo.getTensorsData();
    ```

2. Set the raw data to the `TensorsData` object:

    ```javascript
    // create or fetch data
    var inputData = new Uint8Array(224 * 224 * 3);
    inputTensorsData.setTensorRawData(0, inputData);
    ```

3. Invoke the model:

    ```javascript
    var result = model.invoke(inputTensorsData);
    ```

## Invoke asynchronously

For inferences taking more time, it is recommended to use `invokeAsync()` method. It preserves responsive application UI during the inference:

1. Create callbacks:

    ```javascript
    function errorCallback(error)
    {
      console.log("Error during invokeAsync: " + error.message);
    }

    function successCallback(result)
    {
      console.log("Inference finished successfully");

      /* process result here */
      console.log(result.getTensorRawData(0));

      /* always call dispose() on no longer needed objects */
      result.dispose();
    }
    ```

2. Invoke the model asynchronously:

    ```javascript
    model.invokeAsync(inputTensorsData, successCallback, errorCallback);
    ```

    > [!NOTE]
    > Ensure to dispose the `TensorsData` object provided by `successCallback`, when no longer needed.

The computation in more complex models may take long time, to limit this time, you can use `setTimeout` to set desired limit in milliseconds:

  ```javascript
  model.setTimeout(100);
  ```

If the invoke time is longer than 100 ms, you encounter `TimeoutError`.

## Fetch the result

1. After successful `SingleShot` invoke, you can get raw data from the result:

    ```javascript
    var rawData = result.getTensorRawData(0);
    ```

2. Ensure to dispose off the objects when you do not need them anymore:

    ```javascript
    result.dispose();
    inputTensorsData.dispose();
    inputTensorsInfo.dispose();
    model.close();
    ```

## Related information

- Dependencies
  - Tizen 6.5 and Higher for Mobile
  - Tizen 6.5 and Higher for Wearable
  - Tizen 6.5 and Higher for TV
