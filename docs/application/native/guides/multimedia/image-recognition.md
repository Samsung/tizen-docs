# Image Recognition and Tracking


You can extract features of an image object and recognize it from specific images. You can also track the image object in your application.

The main features of the Media Vision Image API include:

- Recognizing images

  You can [recognize image objects](#recognize) in specific images, and extract image object features.

- Tracking images

  You can [track image objects](#track) using the camera preview images and a specific image tracking model.

## Prerequisites

To enable your application to use the media vision image functionality:

1. To use the functions and data types of the Media Vision Image API (in [mobile](../../api/mobile/latest/group__CAPI__MEDIA__VISION__IMAGE__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__MEDIA__VISION__IMAGE__MODULE.html) applications), include the `<mv_image.h>` header file in your application.

   In addition, you must include the `<image_util.h>` header file to handle the image decoding tasks, or the `<camera.h>` header file to provide preview images.

   ```
   #include <mv_image.h>

   /* Image decoding for image recognition */
   #include <image_util.h>
   /* Preview images for image tracking */
   #include <camera.h>
   ```

2. Create a structure to store the global data:

   - For image recognition, use the following `imagedata_s` structure:

     ```
     struct _imagedata_s {
         mv_source_h g_source;
         mv_engine_config_h g_engine_config;
         mv_image_object h g_image_object;
     };
     typedef struct _imagedata_s imagedata_s;
     static imagedata_s imagedata;
     ```

   - For image tracking, use the following `imagedata_s` structure:

     ```
     struct _imagedata_s {
         /* Variable for camera display */
         Evas_Object *win;
         Evas_Object *rect;
         Evas *evas;

         int preview_width;
         int preview_height;

         camera_h g_camera;

         mv_source_h g_source;
         mv_engine_config_h g_engine_config;

         mv_image_object_h g_image_object
         mv_image_tracking_model_h g_image_track_model;
     };
     typedef struct _imagedata_s imagedata_s;
     static imagedata_s imagedata;
     ```

<a name="recognize"></a>
## Recognizing Images

To recognize images:

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

   In the following example, the `sample.jpg` is the target image to be recognized and it is in the `<OwnDataPath>` folder, where `<OwnDataPath>` refers to your own data path.

    ```
    /* For details, see the Image Util API Reference */
    unsigned char *dataBuffer = NULL;
    unsigned int bufferSize = 0;
    int width = 0;
    int height = 0;

    error_code = image_util_decode_jpeg("/mydir/sample.jpg", IMAGE_UTIL_COLORSPACE_RGB888,
                                        &dataBuffer, &width, &height, &bufferSize);
    if (error_code != IMAGE_UTIL_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);

    /* Fill the dataBuffer to g_source */
    error_code = mv_source_fill_by_buffer(imagedata.g_source, dataBuffer, bufferSize,
                                          width, height, MEDIA_VISION_COLORSPACE_RGB888);
    if (error_code != MEDIA_VISION_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);

    free(dataBuffer);
    dataBuffer = NULL;
    ```

3. To recognize the `sample.jpg` image from others, create a `g_image_object` media vision image object handle and set a label.

   In the following example, the image object label is set to '1'.

    ```
    error_code = mv_image_object_create(&imagedata.g_image_object);
    if (error_code != MEDIA_VISION_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);

    error_code = mv_image_object_set_label(&imagedata.g_image_object, 1);
    if (error_code != MEDIA_VISION_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);
    ```

4. Use the `mv_image_object_fill()` function to extract the `sample.jpg` features and keep them in the `g_image_object` image object handle.

   In the following example, the `NULL` parameter is given since the object to be recognized is the whole of the input image file. Give a correct ROI value, if the image object to be recognized is only a part of the input image file.

    ```
    error_code = mv_image_object_fill(imagedata.g_image_object, imagedata.g_engine_config,
                                      imagedata.g_source, NULL);
    if (error_code != MEDIA_VISION_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);
    ```

5. Use the `mv_image_recognize()` function to recognize the image object.

   The following example assumes that there is a `what_isThis.jpg` image file in the `<OwnDataPath>` folder, including the image object.

    ```
    error_code = image_util_decode_jpeg("/mydir/what_isThis.jpg", IMAGE_UTIL_COLORSPACE_RGB888,
                                        &dataBuffer, &width, &height, &bufferSize);
    if (error_code != IMAGE_UTIL_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);

    error_code = mv_source_clear(imagedata.g_source);
    if (error_code != MEDIA_VISION_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);

    /* Fill the dataBuffer to g_source */
    error_code = mv_source_fill_by_buffer(imagedata.g_source, dataBuffer, bufferSize,
                                          width, height, MEDIA_VISION_COLORSPACE_RGB888);
    if (error_code != MEDIA_VISION_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);

    free(dataBuffer);
    dataBuffer = NULL;

    error_code = mv_image_recognize(imagedata.g_source, &imagedata.g_image_object, 1,
                                    imagedata.g_engine_config, _on_image_recognized_cb, NULL);
    if (error_code != MEDIA_VISION_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);
    ```

6. The `mv_image_recognize()` function invokes the `_on_image_recognized_cb()` callback.

   The following callback example prints the recognized image object label with its location.

    ```
    static void
    _on_image_recognized_cb(mv_source_h source, mv_engine_config_h engine_config,
                            const mv_image_object_h *image_objects, mv_quadrangle_s **locations,
                            unsigned int number_of_objects, void *user_data)
    {
        int object_num = 0;
        for (object_num = 0; object_num < number_of_object; ++object_num) {
            if (locations[object_num]) {
                int recognized_label = 0;
                mv_image_object_get_label(image_objects[object_num], &recognized_label);
                dlog_print(DLOG_INFO, LOG_TAG, "image label [%d] on location: (%d,%d) -> (%d,%d) -> (%d,%d) -> (%d,%d)\n",
                           recognized_label, locations[object_num]->points[0].x, locations[object_num]->points[0].y,
                           locations[object_num]->points[1].x, locations[object_num]->points[1].y,
                           locations[object_num]->points[2].x, locations[object_num]->points[2].y,
                           locations[object_num]->points[3].x, locations[object_num]->points[3].y);
            }
        }
    }
    ```

7. After the image recognition is complete, destroy the source, engine configuration, and image object handles using the `mv_destroy_source()`, `mv_destroy_engine_config()`, and `mv_image_object_destroy()` functions:

    ```
    error_code = mv_destroy_source(imagedata.g_source);
    if (error_code != MEDIA_VISION_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);

    error_code = mv_destroy_engine_config(imagedata.g_engine_config);
    if (error_code != MEDIA_VISION_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);

    error_code = mv_image_object_destroy(imagedata.g_image_object);
    if (error_code != MEDIA_VISION_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);
    ```

<a name="track"></a>
## Tracking Images

To track images:

1. Initialize the camera and required handles:

   1. Initialize the camera, set the preview callback, and start the preview.

      The preview callback is used to get the preview image in which the image object is tracked. For more information on starting the camera, see [Configuring the Camera and its Callbacks](camera.md#configuring_callback) in the Camera guide.

      ```
      /* Create the camera handle */
      int error_code = 0;
      error_code = camera_create(CAMERA_DEVICE_CAMERA0, &imagedata.g_camera);
      if (error_code != CAMERA_ERROR_NONE)
          dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);

      /* Set the camera display */
      error_code = camera_set_display(imagedata.g_camera, CAMERA_DISPLAY_TYPE_OVERLAY, GET_DISPLAY(imagedata.win);
      if (error_code != CAMERA_ERROR_NONE)
          dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);

      /* Get the camera preview resolution */
      error_code = camera_get_preview_resolution(imagedata.g_camera, &imagedata.preview_width,
                                                 &imagedata.preview_height);
      if (error_code != CAMERA_ERROR_NONE)
          dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);

      /* Set the camera preview callback */
      error_code = camera_set_media_packet_preview_cb(imagedata.g_camera, _camera_media_packet_preview_cb, NULL);
      if (error_code != CAMERA_ERROR_NONE)
          dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);

      /* Start the camera preview */
      error_code = camera_start_preview(imagedata.g_camera);
      if (error_code != CAMERA_ERROR_NONE)
          dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);
      ```

   2. Create the source and engine configuration handles:

      ```
      error_code = mv_create_source(&imagedata.g_source);
      if (error_code != MEDIA_VISION_ERROR_NONE)
          dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);

      error_code = mv_create_engine_config(&imagedata.g_engine_config);
      if (error_code != MEDIA_VISION_ERROR_NONE)
          dlog_print(DLOG_ERROR, LOG_TAG, "error code= %d", error_code);
      ```

   3. To track an image, create a `g_image_object` media vision image object handle and set a label.

      In the following example, the image to be tracked is `sample.jpg` and the image object label is set to '1'.

      ```
      error_code = mv_image_object_create(&imagedata.g_image_object);
      if (error_code != MEDIA_VISION_ERROR_NONE)
          dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);

      error_code = mv_image_object_set_label(&imagedata.g_image_object, 1);
      if (error_code != MEDIA_VISION_ERROR_NONE)
          dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);
      ```

   4. Use the `mv_image_object_fill()` function to extract the `sample.jpg` features and keep them in the `g_image_object` image object handle.

      In the following example, the `NULL` parameter is given since the object to be tracked is the whole of the input image file. Give a correct ROI value, if the image object to be tracked is only a part of the input image file.

      ```
      error_code = mv_image_object_fill(imagedata.g_image_object, imagedata.g_engine_config,
                                        imagedata.g_source, NULL);
      if (error_code != MEDIA_VISION_ERROR_NONE)
          dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);
      ```

   5. Create a `g_image_track_model` media vision image tracking model handle and set the target image object to be tracked:

      ```
      error_code = mv_image_tracking_model_create(&imagedata.g_image_track_model);
      if (error_code != MEDIA_VISION_ERROR_NONE)
          dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);

      error_code = mv_image_tracking_model_set_target(imagedata.g_image_object,
                                                      imagedata.g_image_track_model);
      if (error_code != MEDIA_VISION_ERROR_NONE)
          dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);
      ```

   6. Define the camera preview callback.

      The callback allows you to receive preview images as media packet handles. In the callback, to track the image object, first fill the `g_source` handle with the media packet using the `mv_source_fill_by_media_packet()` function.

      ```
      static void
      _camera_media_packet_preview_cb(media_packet_h pkt, void *user_data)
      {
          if (pkt == NULL)
              return;

          error_code = mv_source_fill_by_media_packet(imagedata.g_source, pkt);
          if (error_code != MEDIA_VISION_ERROR_NONE)
              dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error code);

          if (pkt) {
              error_code = media_packet_destroy(pkt);
              pkt = NULL;
          }
      }
      ```

2. Manage image tracking:

   1. Use the `mv_image_track()` function to track the target image object in the preview images:

      ```
      error_code = mv_image_track(imagedata.g_source, imagedata.g_image_track_model,
                                  imagedata.g_engine_config, _on_image_tracked_cb, NULL);
      if (error_code != MEDIA_VISION_ERROR_NONE)
          dlog_print(DLOG_ERROR, LOG_TAG, "error code= %d", error_code);
      ```

   2. The `mv_image_track()` function invokes the `_on_image_tracked_cb()` callback.

      The following callback example prints the location of the target image object.

      ```
      static void
      _on_image_tracked_cb(mv_source_h source, mv_image_object_h image_object,
                           mv_engine_config_h engine_config, mv_quadrangle_s *location,
                           void *user_data)
      {
          if (location) {
              dlog_print(DLOG_INFO, LOG_TAG, "location: (%d,%d) -> (%d,%d) -> (%d,%d) -> (%d,%d)\n",
                         location->points[0].x, location->points[0].y,
                         location->points[1].x, location->points[1].y,
                         location->points[2].x, location->points[2].y,
                         location->points[3].x, location->points[3].y);
          }
      }
      ```

3. After the image tracking is complete, stop the camera preview, unset the preview callback, and destroy the camera handle:

   ```
   error_code = camera_stop_preview(imagedata.g_camera);
   if (error_code != CAMERA_ERROR_NONE)
       dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);

   error_code = camera_unset_media_packet_preview_cb(imagedata.g_camera);
   if (error_code != CAMERA_ERROR_NONE)
       dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);

   error_code = camera_destroy(imagedata.g_camera);
   if (error_code != CAMERA_ERROR_NONE)
       dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);
   ```

   For more information, see [Releasing Resources](camera.md#release) in the Camera guide.

4. Destroy the source, engine configuration, image object, and image tracking model handles using the `mv_destroy_source()`, `mv_destroy_engine_config()`, `mv_image_object_destroy()`, and `mv_image_tracking_model_destroy()` functions:

    ```
    error_code = mv_destroy_source(imagedata.g_source);
    if (error_code != MEDIA_VISION_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);

    error_code = mv_destroy_engine_config(imagedata.g_engine_config);
    if (error_code != MEDIA_VISION_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);

    error_code = mv_image_object_destroy(imagedata.g_image_object);
    if (error_code != MEDIA_VISION_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);

    error_code = mv_image_tracking_model_destroy(imagedata.g_image_track_model);
    if (error_code != MEDIA_VISION_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);
    ```

## Related Information
- Dependencies
  - Tizen 3.0 and Higher for Mobile
  - Tizen 3.0 and Higher for Wearable
