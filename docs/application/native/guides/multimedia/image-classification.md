# Image Classification

You can classify an image, which belongs to corresponding labels.

The main features of the Media Vision Inference API include:

- Classifying an image

  You can [classify](#classify) an image

## Prerequisites

To enable your application to use the media vision inference functionality:

1. To use the functions and data types of the Media Vision Inference API (in [mobile](../../api/mobile/latest/group__CAPI__MEDIA__VISION__INFERENCE__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__MEDIA__VISION__INFERENCE__MODULE.html) applications), include the `<mv_inference.h>` header file in your application.

   In addition, you must include the `<image_util.h>` header file to handle the image decoding tasks, or the `<camera.h>` header file to provide preview images.

   ```
   #include <mv_inference.h>

   /* Image decoding for image recognition */
   #include <image_util.h>
   /* Preview images for image tracking */
   #include <camera.h>
   ```

2. Create a structure to store the global data:

   - For image classification, use the following `imagedata_s` structure:

     ```
     struct _imagedata_s {
         mv_source_h g_source;
         mv_engine_config_h g_engine_config;
         mv_inference_h g_inferece;
     };
     typedef struct _imagedata_s imagedata_s;
     static imagedata_s imagedata;
     ```

<a name="classify"></a>
## Classify an image

To classify an image:

1. Create the source and engine configuration handles:

    ```
    int error_code = 0;

    error_code = mv_create_source(&imagedata.g_source);
    if (error_code != MEDIA_VISION_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);

    error_code = mv_create_engine_config(&imagedata.g_engine_config);
    if (error_code != MEDIA_VISION_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "error code= %d", error_code);
    ```

2. Decode the image file and fill the `g_source` handle with the decoded raw data.

   In the following example, the `sample.jpg` is the image to be classifed and it is in the `<OwnDataPath>` folder, where `<OwnDataPath>` refers to your own data path.

    ```
    /* For details, see the Image Util API Reference */
    unsigned char *dataBuffer = NULL;
    unsigned long long bufferSize = 0;
    unsigned long width = 0;
    unsigned long height = 0;
    image_util_decode_h imageDecoder = NULL;

    error_code = image_util_decode_create(&imageDecoder);
    if (error_code != IMAGE_UTIL_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);

    error_code = image_util_decode_set_input_path(imageDecoder, "/mydir/sample.jpg");
    if (error_code != IMAGE_UTIL_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);

    error_code = image_util_decode_set_colorspace(imageDecoder, IMAGE_UTIL_COLORSPACE_RGB888);
    if (error_code != IMAGE_UTIL_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);

    error_code = image_util_decode_set_output_buffer(imageDecoder, &dataBuffer);
    if (error_code != IMAGE_UTIL_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);

    error_code = image_util_decode_run(imageDecoder, &width, &height, &bufferSize);
    if (error_code != IMAGE_UTIL_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);

    error_code = image_util_decode_destroy(imageDecoder);
    if (error_code != IMAGE_UTIL_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);

    /* Fill the dataBuffer to g_source */
    error_code = mv_source_fill_by_buffer(imagedata.g_source, dataBuffer, (unsigned int)bufferSize,
                                          (unsigned int)width, (unsigned int)height, MEDIA_VISION_COLORSPACE_RGB888);
    if (error_code != MEDIA_VISION_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);

    free(dataBuffer);
    dataBuffer = NULL;
    ```

3. To classify the `sample.jpg` image, create a `g_inference` media vision inference handle.

    ```
    error_code = mv_inference_create(&imagedata.g_inference);
    if (error_code != MEDIA_VISION_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);
    ```

4. Configure `g_engine_config` with classification model data to classify image. In the following example, TensorFlow-Lite model is used and `data.tflite` and `label.txt` are in `<OwnDataPath>`. Model data is available in open model zoo such as [hosted model zoo](https://www.tensorflow.org/lite/guide/hosted_models#floating_point_models).

    ```
    #define MODEL_DATA "OwnDataPath/data.tflite"
    #define MODEL_LABEL "OwnDataPath/label.txt"

    error_code = mv_engine_config_set_string_attribute(handle,
                      MV_INFERENCE_MODEL_WEIGHT_FILE_PATH,
                      MODEL_DATA);

    error_code = mv_engine_config_set_string_attribute(handle,
                      MV_INFERENCE_MODEL_USER_FILE_PATH,
                      MODEL_LABEL);

    error_code = mv_engine_config_set_double_attribute(handle,
                      MV_INFERENCE_MODEL_MEAN_VALUE,
                      127.5);

    error_code = mv_engine_config_set_double_attribute(handle,
                      MV_INFERENCE_MODEL_STD_VALUE,
                      127.5);

    error_code = mv_engine_config_set_double_attribute(handle,
                      MV_INFERENCE_CONFIDENCE_THRESHOLD,
                      0.0);

    error_code = mv_engine_config_set_int_attribute(handle,
                      MV_INFERENCE_BACKEND_TYPE,
                      MV_INFERENCE_BACKEND_TFLITE);

    error_code = mv_engine_config_set_int_attribute(handle,
                      MV_INFERENCE_INPUT_TENSOR_WIDTH,
                      224);

    error_code = mv_engine_config_set_int_attribute(handle,
                      MV_INFERENCE_INPUT_TENSOR_HEIGHT,
                      224);

    error_code = mv_engine_config_set_int_attribute(handle,
                      MV_INFERENCE_INPUT_TENSOR_CHANNELS,
                      3);
    ```
The datails of configuration attributes such as `MV_INFERENCE_MODEL_WEIGHT_FILE_PATH` can be found in [Inference API](../../api/mobile/latest/group__CAPI__MEDIA__VISION__INFERENCE__MODULE.html).

5. Use the `mv_inference_configure()` function to configure `g_inference` inference handle with `g_engine_config`.
    ```
    error_code = mv_inference_configure(imagedata.g_inference, imagedata.g_engine_config);
    if (error_code != MEDIA_VISION_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);
    ```

6. Use the `mv_inference_prepare()` function to prepare inference.
    ```
    error_code = mv_inference_prepare(imagedata.g_inference);
    if (error_code != MEDIA_VISION_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);
    ```

7. Use the `mv_inference_image_classify()` function to classify the image.

    ```
    error_code = mv_inference_image_classify(imagedata.g_source, &imagedata.g_inference, NULL, _on_image_classified_cb, NULL);
    if (error_code != MEDIA_VISION_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);
    ```

6. The `mv_inference_image_classify()` function invokes the `_on_image_classified_cb()` callback.

   The following callback example prints the classified image labels with thier scores.

    ```
    static void
    _on_image_classified_cb(mv_source_h source, const int number_of_classes,
                  const int *indices, const char **names,
                  const float *confidences, void *user_data)
    {
      dlog_print(DLOG_INFO, LOG_TAG, classifed %d labels\n", number_of_classes);

      for (int n = 0; n < number_of_classes; ++n)
        dlog_print(DLOG_INFO, LOG_TAG, %s with %.3f score\n", names[n], confidences[n]);
    }
    ```

7. After the image classification is complete, destroy the source, engine configuration, and inference handles using the `mv_destroy_source()`, `mv_destroy_engine_config()`, and `mv_inference_destroy()` functions:

    ```
    error_code = mv_destroy_source(imagedata.g_source);
    if (error_code != MEDIA_VISION_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);

    error_code = mv_destroy_engine_config(imagedata.g_engine_config);
    if (error_code != MEDIA_VISION_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);

    error_code = mv_inference_destroy(imagedata.g_inference);
    if (error_code != MEDIA_VISION_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);
    ```

## Related Information
- Dependencies
  - Tizen 5.5 and Higher for Mobile
  - Tizen 5.5 and Higher for Wearable
