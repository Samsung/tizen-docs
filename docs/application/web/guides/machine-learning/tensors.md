# Tensors management

Machine Learning Web API in Tizen requires `TensorsInfo` and `TensorsData` objects. These objects are used to perform calculation with neural network models.

The main features of the Machine Learning API include:

- Checking support of a specific neural network framework

  You can [check NNFW availability](#check-nnfw-availability) using `checkNNFWAvailability`.

- Creating tensor's structure.

  You can use `TensorsInfo` object to [manage tensor information](#manage-tensor-information).

- Reading and writing raw data.

  You can [read and write tensor data](#manage-tensor-data) using `TensorsData` object.

## Check NNFW availability

To check whether specific Neural Network Framework (NNFW) is supported you can use `checkNNFWAvailability`:

    ```javascript
    var fw = "TENSORFLOW_LITE";
    var hw = "CPU";
    var available = tizen.ml.checkNNFWAvailability(fw, hw);
    console.log(available); // true
    ```

## Manage tensor information

1. To configure the tensor information, you need to create a new instance of the `TensorsInfo` class:

    ```javascript
    var tensorsInfo = new tizen.ml.TensorsInfo();
    ```

2. `TensorsInfo` object can store information such as name, data type, and dimensions:

    ```javascript
    tensorsInfo.addTensorInfo("tensor", "UINT8", [2, 2]);
    ```

 > [!NOTE]
 >
 > One `TensorsInfo` object can store information on up to 16 tensors.

3. You can modify tensor's parameters with help of `setTensorName`, `setTensorType`, and `setDimensions`:

    ```javascript
    tensorsInfo.setTensorName(0, "tensorName");
    tensorsInfo.setTensorType(0, "UINT16");
    tensorsInfo.setTensorDimensions(0, [2, 2]);
    ```

4. To clone and compare `TensorsInfo` object:

    ```javascript
    var clone = tensorsInfo.clone();
    var isEqual = tensorsInfo.equals(clone);
    ```

 > [!NOTE]
 > Use `equals()` to compare `TensorInfo` objects. Comparisons must not be done with built-in `==`, `===`, `!=`, `!==` operators which may return false results for this data type.

5. To calculate the byte size of tensor data use `getTensorSize`:

    ```javascript
    var byteSize = tensorsInfo.getTensorSize(0);
    ```

6. After you create tensor definition, you can use `getTensorsData` to get `TensorsData` object:

    ```javascript
    var tensorsData = tensorsInfo.getTensorsData();
    ```

7. Ensure to dispose off the `TensorsInfo` object when you do not need it anymore:

    ```javascript
    tensorsInfo.dispose();
    ```

## Manage tensor data

The `TensorsData` object keeps data value of the tensors.

1. To get specific data object from `TensorsData`, use `getTensorRawData`.

    ```javascript
    var rawData = tensorsData.getTensorRawData(0);
    ```

- You can also specify location and size of data you want to get.

    ```javascript
    // fetch one element
    var rawDataOne = tensorsData.getTensorRawData(0, [0, 0], [1, 1]);
    // fetch first row
    var rawDataRow = tensorsData.getTensorRawData(0, [0, 0], [-1, 1]);
    ```

 > [!NOTE]
 > To gather more information about specifying location and size of the raw data, see `TensorsData.getTensorRawData` (in [mobile](../../api/latest/device_api/mobile/tizen/ml.html#TensorsData::getTensorRawData), [wearable](../../api/latest/device_api/wearable/tizen/ml.html#TensorsData::getTensorRawData), and [TV](../../api/latest/device_api/tv/tizen/ml.html#TensorsData::getTensorRawData) applications) to gather more information about specifying location and size of raw data.

2. To set data to `TensorsData` object, use `setTensorRawData`:

    ```javascript
    tensorsData.setTensorRawData(0, [1, 2, 3, 4]);
    ```

- You can also specify location and size of data you want to set.

    ```javascript
    // set only one element
    tensorsData.setTensorRawData(0, [7], [0, 0], [1, 1]);
    // set first row
    tensorsData.setTensorRawData(0, [4, 5], [0, 0], [-1, 1]);
    ```

 >  [!NOTE]
 > To gather more information about specifying location and size of the raw data, see `TensorsData.setTensorRawData` (in [mobile](../../api/latest/device_api/mobile/tizen/ml.html#TensorsData::setTensorRawData), [wearable](../../api/latest/device_api/wearable/tizen/ml.html#TensorsData::setTensorRawData), and [TV](../../api/latest/device_api/tv/tizen/ml.html#TensorsData::setTensorRawData) applications) to gather more information about specifying location and size of raw data.

3. Ensure to dispose off the `TensorsData` objects when you do not need them anymore:

    ```javascript
    tensorsData.dispose();
    ```

## Related information

- Dependencies
  - Tizen 6.5 and Higher for Mobile
  - Tizen 6.5 and Higher for Wearable
  - Tizen 6.5 and Higher for TV
  - Tizen 6.5 and Higher for Mobile
  - Tizen 6.5 and Higher for Wearable
  - Tizen 6.5 and Higher for TV
