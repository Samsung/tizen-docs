# Image Classification

Image classification is one of the main features of the Media Vision Inference API. You can [classify](#classify) an image, which belongs to the corresponding labels. For example, to classify an image consisting of a food item, you can apply a food classification model while doing inference of the decoded image data.

## Prerequisites

To enable your application to use the media vision inference functionality:

1. To use the functions and data types of the Media Vision Inference API (in [mobile](../../api/mobile/latest/group__CAPI__MEDIA__VISION__INFERENCE__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__MEDIA__VISION__INFERENCE__MODULE.html) applications), include the `<mv_inference.h>` header file in your application.

   In addition, you must include the `<image_util.h>` header file to handle the image decoding tasks, or the `<camera.h>` header file to provide the preview images:

   ```c
   #include <mv_inference.h>

   /* Image decoding for image recognition */
   #include <image_util.h>
   /* Preview images for image tracking */
   #include <camera.h>
   ```

2. Create a structure to store the global data.

     For image classification, use the following `imagedata_s` structure:

     ```c
     struct _imagedata_s {
         mv_source_h g_source;
         mv_engine_config_h g_engine_config;
         mv_inference_h g_inferece;
     };
     typedef struct _imagedata_s imagedata_s;
     static imagedata_s imagedata;
     ```

<a name="classify"></a>
## Classify image

To classify an image:

1. Create the source and engine configuration handles:

    ```c
    int error_code = 0;

    error_code = mv_create_source(&imagedata.g_source);
    if (error_code != MEDIA_VISION_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);

    error_code = mv_create_engine_config(&imagedata.g_engine_config);
    if (error_code != MEDIA_VISION_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "error code= %d", error_code);
    ```

2. Decode the image file and fill the `g_source` handle with the decoded raw data.

   In the following example, `sample.jpg` is the image to be classified and it is in the `<OwnDataPath>` folder.
   The `<OwnDataPath>` refers to your own data path:

    ```c
    /* For details, see the Image Util API Reference */
    unsigned char *dataBuffer = NULL;
    unsigned long long bufferSize = 0;
    unsigned long width = 0;
    unsigned long height = 0;
    image_util_decode_h imageDecoder = NULL;

    error_code = image_util_decode_create(&imageDecoder);
    if (error_code != IMAGE_UTIL_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);

    error_code = image_util_decode_set_input_path(imageDecoder, "/<OwnDataPath>/sample.jpg");
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

3. To classify the `sample.jpg` image, create a `g_inference` media vision inference handle:

    ```c
    error_code = mv_inference_create(&imagedata.g_inference);
    if (error_code != MEDIA_VISION_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);
    ```

4. Configure `g_engine_config` with classification model data to classify image. In the following example, TensorFlow Lite model is used and `data.tflite` and `label.txt` are in `<OwnDataPath>`. Model data is available in open model zoo such as [hosted model zoo](https://www.tensorflow.org/lite/guide/hosted_models#floating_point_models):

    ```c
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
    For more information on the configuration attributes such as `MV_INFERENCE_MODEL_WEIGHT_FILE_PATH`, see Media Vision Inference API (in [mobile](../../api/mobile/latest/group__CAPI__MEDIA__VISION__INFERENCE__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__MEDIA__VISION__INFERENCE__MODULE.html) applications).

5. Use `mv_inference_configure()` to configure `g_inference` inference handle with `g_engine_config`:
    ```c
    error_code = mv_inference_configure(imagedata.g_inference, imagedata.g_engine_config);
    if (error_code != MEDIA_VISION_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);
    ```

6. Use `mv_inference_prepare()` to prepare inference:
    ```c
    error_code = mv_inference_prepare(imagedata.g_inference);
    if (error_code != MEDIA_VISION_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);
    ```

7. Use `mv_inference_image_classify()` to classify the image:

    ```c
    error_code = mv_inference_image_classify(imagedata.g_source, &imagedata.g_inference, NULL, _on_image_classified_cb, NULL);
    if (error_code != MEDIA_VISION_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);
    ```

   `mv_inference_image_classify()` invokes `_on_image_classified_cb()` callback.
    The following callback example prints the classified image labels with their scores:

    ```c
    static void
    _on_image_classified_cb(mv_source_h source, const int number_of_classes,
                  const int *indices, const char **names,
                  const float *confidences, void *user_data)
    {
      dlog_print(DLOG_INFO, LOG_TAG, "classified %d labels\n", number_of_classes);

      for (int n = 0; n < number_of_classes; ++n)
        dlog_print(DLOG_INFO, LOG_TAG, "%s with %.3f score\n", names[n], confidences[n]);
    }
    ```

8. After the image classification is complete, destroy the source, engine configuration, and the inference handles using `mv_destroy_source()`, `mv_destroy_engine_config()`, and `mv_inference_destroy()`:

    ```c
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
