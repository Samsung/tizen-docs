# Face Detection, Recognition, and Tracking


You can perceive and understand a face, or track a face in your application.

The main features of Media Vision Face API include:

- Detecting faces

  You can decode an image file and [detect faces](#detect) on it.

- Recognizing faces

  You can [recognize faces](#recognize) in an image with a set of example faces.

- Tracking faces

  You can [track faces](#track) using the camera preview images, starting from a specific location in the image.

## Prerequisites

To enable your application to use the media vision face functionality:

1. To use the functions and data types of the Media Vision Face API (in [mobile](../../api/mobile/latest/group__CAPI__MEDIA__VISION__FACE__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__MEDIA__VISION__FACE__MODULE.html) applications), include the `<mv_face.h>` header file in your application.

   In addition, you must include the `<image_util.h>` header file to handle the image decoding tasks, or the `<camera.h>` header file to provide preview images.

   ```
   #include <mv_face.h>

   /* Image decoding for face detection and recognition */
   #include <image_util.h>
   /* Preview images for face tracking */
   #include <camera.h>
   ```

2. Create a structure to store the global data:

   - For face detection, use the following `facedata_s` structure:

     ```
     struct _facedata_s {
         mv_source_h g_source;
         mv_engine_config_h g_engine_config;
     };
     typedef struct _facedata_s facedata_s;
     static facedata_s facedata;
     ```

   - For face recognition, use the following `facedata_s` structure:

     ```
     struct _facedata_s {
         mv_source_h g_source;
         mv_engine_config_h g_engine_config;
         mv_face_recognition_model g_face_recog_model;
     };
     typedef struct _facedata_s facedata_s;
     static facedata_s facedata;
     ```

   - For face tracking, use the following `facedata_s` structure:

     ```
     struct _facedata_s {
         /* Variable for camera display */
         Evas_Object *win;
         Evas_Object *rect;
         Evas *evas;

         int preview_width;
         int preview_height;

         camera_h g_camera;

         mv_source_h g_source;
         mv_engine_config_h g_engine_config;

         mv_quadrangle_s face_roi;
         mv_face_tracking_model_h g_face_track_model;
     };
     typedef struct _facedata_s facedata_s;
     static facedata_s facedata;
     ```

<a name="detect"></a>
## Detecting Faces

To detect faces:

1. Create a source handle using the `mv_create_source()` function with the `mv_source_h` member of the detection data structure as the out parameter:

    ```
    int error_code = 0;

    error_code = mv_create_source(&facedata.g_source);
    if (error_code != MEDIA_VISION_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);
    ```

	The source stores the face to be detected and all related data. You manage the source through the source handle.

2. Decode the image file from which the face is to be detected, and fill the `g_source` handle with the decoded raw data.

   In the following example, the face of the NASA astronaut is to be detected (the image file can be downloaded from [NASA-AstronautGroup18](https://commons.wikimedia.org/wiki/File%3ANASA_Astronaut_Group_18.jpg) and it is saved to `<OwnDataPath>/NasaAstronaut.jpg` where `<OwnDataPath>` refers to your own data path).

    ```
    /* For details, see the Image Util API Reference */
    unsigned char *dataBuffer = NULL;
    unsigned int bufferSize = 0;
    int width = 0;
    int height = 0;

    error_code = image_util_decode_jpeg("/mydir/NasaAstronaut.jpg", IMAGE_UTIL_COLORSPACE_RGB888,
                                        &dataBuffer, &height, &bufferSize);
    if (error_code != IMAGE_UTIL_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);

    /* Fill the dataBuffer to g_source */
    error_code = mv_source_fill_by_buffer(facedata.g_source, dataBuffer, bufferSize,
                                          width, height, MEDIA_VISION_COLORSPACE_RGB888);
    if (error_code != MEDIA_VISION_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);

    free(dataBuffer);
    dataBuffer = NULL;
    ```

3. Create the media vision engine using the `mv_create_engine_config()` function. The function creates the `g_engine_config` engine configuration handle and configures it with default attributes.

    ```
    error_code = mv_create_engine_config(&facedata.g_engine_config);
    if (error_code != MEDIA_VISION_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "error code= %d", error_code);
    ```

	Face detection details can be configured by setting attributes to the engine configuration handle. In this use case, the `MV_FACE_DETECTION_MODEL_FILE_PATH` attribute is configured. For more information on the attributes, see the Media Vision API reference (in [mobile](../../api/mobile/latest/group__CAPI__MEDIA__VISION__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__MEDIA__VISION__MODULE.html) applications).

    ```
    error_code = mv_engine_config_set_string_attribute(facedata.g_engine_config,
                                                       MV_FACE_DETECTION_MODEL_FILE_PATH,
                                                       "/usr/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml");
    if (error_code != MEDIA_VISION_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "error code= %d", error_code);
    ```

4. When the source and engine configuration handles are ready, use the `mv_face_detect()` function to detect faces:

    ```
    error_code = mv_face_detect(facedata.g_source, facedata.g_engine_config,
                                _on_face_detected_cb, NULL);
    if (error_code != MEDIA_VISION_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "error code= %d", error_code);
    ```

5. The `mv_face_detect()` function invokes the `_on_face_detected_cb()` callback.

   The following callback example prints the number of detected faces with their location.

    ```
    static void
    _on_face_detected_cb(mv_source_h source, mv_engine_config_h engine_config,
                         mv_rectangle_s *face_locations, int number_of_faces, void *user_data)
    {
        if (number_of_faces > 0) {
            int index = 0;
            for (index = 0; index < number_of_faces; ++index) {
                dlog_print(DLOG_INFO, LOG_TAG, "face [%d]: x-[%d], y-[%d], width-[%d], height-[%d]\n",
                           index, face_locations[index].x, face_locations[index].y,
                           face_locations[index].width, face_locations[index].height);
            }
        }
    }
    ```

6. After the face detection is complete, destroy the source and engine configuration handles using the `mv_destroy_source()` and `mv_destroy_engine_config()` functions:

    ```
    error_code = mv_destroy_source(facedata.g_source);
    if (error_code != MEDIA_VISION_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);

    error_code = mv_destroy_engine_config(facedata.g_engine_config);
    if (error_code != MEDIA_VISION_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);
    ```
<a name="recognize"></a>
## Recognizing Faces

To recognize faces:

1. Create the source and engine configuration handles:

   ```
   int error_code = 0;

   error_code = mv_create_source(&facedata.g_source);
   if (error_code != MEDIA_VISION_ERROR_NONE)
       dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);

   error_code = mv_create_engine_config(&facedata.g_engine_config);
   if (error_code != MEDIA_VISION_ERROR_NONE)
       dlog_print(DLOG_ERROR, LOG_TAG, "error code= %d", error_code);
   ```

2. Create a `g_face_recog_model` media vision face recognition model handle using the `mv_face_recognition_model_create()` function. The handle must be created before any recognition is attempted.

    ```
    error_code = mv_face_recognition_model_create(&facedata.g_face_recog_model);
    if (error_code != MEDIA_VISION_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);
    ```

3. Add face examples to the face recognition model handle.

   Make sure that the face examples are of the same person but captured at different angles. The following example assumes that 10 face samples (`face_sample_1.jpg` - `face_sample_10.jpg` in the `<OwnDataPath>` folder) are used and that the face area in each example covers approximately 95~100% of the image. The label of the face is set to '1'.

   ```
   int example_index = 0;
   int face_label =1;

   char filePath[1024];
   unsigned char *dataBuffer = NULL;
   unsigned int bufferSize = 0;
   int width = 0;
   int height = 0;

   for (example_index = 1; example_index <= 10; ++example_index) {
       /* Decode image and fill the image data to g_source handle */
       snprintf(filePath, 1024, "%s/face_sample_%d.jpg", mydir, example_index);
       error_code = image_util_decode_jpeg(filePath, IMAGE_UTIL_COLORSPACE_RGB888,
                                           &dataBuffer, &width, &height, &bufferSize);
       if (error_code != MEDIA_VISION_ERROR_NONE)
           dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);

       roi.x = roi.y = 0;
       roi.width = width;
       roi.height = height;
       error_code = mv_source_clear(facedata.g_source);
       if (error_code != MEDIA_VISION_ERROR_NONE)
           dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);

       error_code = mv_source_fill_by_buffer(facedata.g_source, &dataBuffer,
                                             &bufferSize, &width, &height, MEDIA_VISION_COLORSPACE_RGB888);
       if (error_code != MEDIA_VISION_ERROR_NONE)
           dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);

       free(dataBuffer);
       dataBuffer = NULL;

       error_code = mv_face_recognition_model_add(facedata.g_source,
                                                  facedata.g_face_recog_model, &roi, face_label);
       if (error_code != MEDIA_VISION_ERROR_NONE)
           dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);
   }
   ```

4. Use the `mv_face_recognition_model_learn()` function to train the face recognition model with the added examples:

    ```
    error_code = mv_face_recognition_model_learn(facedata.g_engine_config, facedata.g_face_recog_model);

    if (error_code != MEDIA_VISION_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "error code= %d", error_code);
    ```

5. When the face recognition model handle is ready, use the `mv_face_recognize()` function to recognize the face.

   The following example assumes that there is a `whos_face.jpg` face image in the `OwnDataPath` folder, and this image is different from the samples. In addition, the `whos_face.jpg` image includes a face which fits to the image resolution. Thus, in this example, a `NULL` parameter is given as the `face_location` parameter of the `mv_face_recognize()` function. Normally, define the parameter with the correct input image face location.

    ```
    /* Decode the image and fill the image data to g_source handle */
    snprintf(filePath, 1024, "%s/whos_face.jpg", mydir);
    error_code = image_util_decode_jpeg(filePath, IMAGE_UTIL_COLORSPACE_RGB888,
                                        &dataBuffer, &width, &height, &bufferSize);
    if (error_code != MEDIA_VISION_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "error code= %d", error_code);

    error_code = mv_source_clear(facedata.g_source);
    if (error_code != MEDIA_VISION_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "error code= %d", error_code);

    error_code = mv_source_fill_by_buffer(facedata.g_source, &dataBuffer, &bufferSize,
                                          &width, &height, MEDIA_VISION_COLORSPACE_RGB888);
    if (error_code != MEDIA_VISION_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "error code= %d", error_code);

    free(dataBuffer);
    dataBuffer = NULL;

    error_code = mv_face_recognize(facedata.g_source, facedata.g_face_recog_model, facedata.g_engine_config,
                                   NULL, _on_face_recognized_cb, NULL);
    if (error_code != MEDIA_VISION_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "error code= %d", error_code);
    ```

6. The `mv_face_recognize()` function invokes the `_on_face_recognized_cb()` callback.

   The following callback example prints the recognized face label with a confidence value.

    ```
    static void
    _on_face_recognized_cb(mv_source_h source, mv_face_recognition_model_h recognition_model,
                           mv_engine_config_h engine_config, mv_rectangle_s *face_location,
                           const int *face_label, double confidence, void *user_data)
    {
        if (face_label) {
            dlog_print(DLOG_INFO, LOG_TAG,
                       "face label [%d] with confidence [%.2f]\n",
                       *face_label, confidence);
        }
    }
    ```

7. After the face recognition is complete, destroy the source, engine configuration, and face recognition model handles using the `mv_destroy_source()`, `mv_destroy_engine_config()`, and `mv_face_recognition_model_destroy()` functions:

    ```
    error_code = mv_destroy_source(facedata.g_source);
    if (error_code != MEDIA_VISION_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);

    error_code = mv_destroy_engine_config(facedata.g_engine_config);
    if (error_code != MEDIA_VISION_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);

    error_code = mv_face_recognition_model_destroy(facedata.g_face_recog_model);
    if (error_code != MEDIA_VISION_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);
    ```
<a name="track"></a>
## Tracking Faces

To track faces:

1. Initialize the camera, required handles, and the initial tracking location:

   1. Initialize the camera, set the preview callback, and start the preview.

      The preview callback is used to get the preview image in which the face is tracked. For more information on starting the camera, see [Configuring the Camera and its Callbacks](camera.md#configuring_callback) in the Camera guide.

      ```
      /* Create the camera handle */
      int error_code = 0;
      error_code = camera_create(CAMERA_DEVICE_CAMERA0, &facedata.g_camera);
      if (error_code != CAMERA_ERROR_NONE)
          dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);

      /* Set the camera display */
      error_code = camera_set_display(facedata.g_camera, CAMERA_DISPLAY_TYPE_OVERLAY, GET_DISPLAY(facedata.win);
      if (error_code != CAMERA_ERROR_NONE)
          dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);

      /* Get the camera preview resolution */
      error_code = camera_get_preview_resolution(facedata.g_camera, &facedata.preview_width,
                                                 &facedata.preview_height);
      if (error_code != CAMERA_ERROR_NONE)
          dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);

      /* Set the camera preview callback */
      error_code = camera_set_media_packet_preview_cb(facedata.g_camera, _camera_media_packet_preview_cb, NULL);
      if (error_code != CAMERA_ERROR_NONE)
          dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);

      /* Start the camera preview */
      error_code = camera_start_preview(facedata.g_camera);
      if (error_code != CAMERA_ERROR_NONE)
          dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);
      ```

   2. Create the source and engine configuration handles:

      ```
      error_code = mv_create_source(&facedata.g_source);
      if (error_code != MEDIA_VISION_ERROR_NONE)
          dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);

      error_code = mv_create_engine_config(&facedata.g_engine_config);
      if (error_code != MEDIA_VISION_ERROR_NONE)
          dlog_print(DLOG_ERROR, LOG_TAG, "error code= %d", error_code);
      ```

   3. Define the camera preview callback.

      The callback allows you to receive preview images as media packet handles. In the callback, first fill the `g_source` handle with the media packet using the `mv_source_fill_by_media_packet()` function.

      ```
      static void
      _camera_media_packet_preview_cb(media_packet_h pkt, void *user_data)
      {
          if (pkt == NULL)
              return;

          error_code = mv_source_fill_by_media_packet(facedata.g_source, pkt);
          if (error_code != MEDIA_VISION_ERROR_NONE)
              dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error code);

          if (pkt) {
              error_code = media_packet_destroy(pkt);
              pkt = NULL;
          }
      }
      ```

   4. Set the initial tracking location.

      In the following example, the `mv_face_detect()` function is used to detect the face and provide its initial location.

      Save the detected face location in the `_on_face_detected_cb()` callback function. Note that the `g_source` handle must be kept while detecting, and updated with new preview images while tracking.

      ```
      error_code = mv_face_detect(facedata.g_source, facedata.g_engine_config,
                                  _on_face_detected_cb, NULL);

      if (error_code != MEDIA_VISION_ERROR_NONE)
          dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);

      static void
      _on_face_detected_cb(mv_source_h source, mv_engine_config_h engine_config,
                           mv_rectangle_s *face_locations, int number_of_faces, void *user_data)
      {
          if (number_of_faces > 0) {
              /*
                 Track the face of index '0'.
                 Convert mv_rectangle_s to mv_quadrangle_s
              */
              facedata.face_roi.points[0].x = face_location[0].x;
              facedata.face_roi.points[0].y = face_location[0].y;
              facedata.face_roi.points[1].x = face_location[0].x + face_location[0].width;
              facedata.face_roi.points[1].y = face_location[0].y;
              facedata.face_roi.points[2].x = face_location[0].x;
              facedata.face_roi.points[2].y = face_location[0].y + face_location[0].height;
              facedata.face_roi.points[3].x = face_location[0].x + face_location[0].width;
              facedata.face_roi.points[3].y = face_location[0].y + face_location[0].height;
          }
      }
      ```

2. Manage face tracking:

   1. Create the `g_face_track_model` media vision face tracking model handle:

      ```
      error_code = mv_face_tracking_model_create(&facedata.g_face_track_model);
      if (error_code != MEDIA_VISION_ERROR_NONE)
          dlog_print(DLOG_ERROR, LOG_TAG, "error code= %d", error_code);
      ```

   2. Prepare the face tracking model handle with the initial location (detected earlier):

      ```
      error_code = mv_face_tracking_model_prepare(facedata.g_face_track_model, facedata.g_engine_config,
                                                  facedata.g_source, &facedata.face_roi);
      if (error_code != MEDIA_VISION_ERROR_NONE)
          dlog_print(DLOG_ERROR, LOG_TAG, "error code= %d", error_code);
      ```

   3. Use the `mv_face_track()` function to track the face.

  	  > **Note**
      >
      > Control the `g_source` handle carefully. Do not update it to the next preview image while the `mv_face_track()` function processes the `g_source` handle with the current preview image.

      ```
      error_code = mv_face_track(facedata.g_source, facedata.g_face_track_model,
                                 facedata.g_engine_config, _on_face_tracked_cb, false, NULL);
      if (error_code != MEDIA_VISION_ERROR_NONE)
          dlog_print(DLOG_ERROR, LOG_TAG, "error code= %d", error_code);
      ```

   4. The `mv_face_track()` function invokes the `_on_face_tracked_cb()` callback.

      The following callback example prints the current location of the tracked face.

      ```
      static void
      _on_face_tracked_cb(mv_source_h source, mv_face_tracking_model_h tracking_model,
                          mv_engine_config_h engine_config, mv_quadrangle_s *location,
                          double confidence, void *user_data)
      {
          dlog_print(DLOG_INFO, LOG_TAG, "Location: (%d,%d) -> (%d,%d) -> (%d,%d) -> (%d,%d)\n",
                     location->points[0].x, location->point[0].y,
                     location->points[1].x, location->point[1].y,
                     location->points[2].x, location->point[2].y,
                     location->points[3].x, location->point[3].y)
      }
      ```

3. After the face tracking is complete, stop the camera preview, unset the preview callback, and destroy the camera handle:

   ```
   error_code = camera_stop_preview(facedata.g_camera);
   if (error_code != CAMERA_ERROR_NONE)
       dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);

   error_code = camera_unset_media_packet_preview_cb(facedata.g_camera);
   if (error_code != CAMERA_ERROR_NONE)
       dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);

   error_code = camera_destroy(facedata.g_camera);
   if (error_code != CAMERA_ERROR_NONE)
       dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);
   ```

   For more information, see [Releasing Resources](camera.md#release) in the Camera guide.

4. Destroy the source, engine configuration, and face tracking model handles using the `mv_destroy_source()`, `mv_destroy_engine_config()`, and `mv_face_tracking_model_destroy()` functions:

    ```
    error_code = mv_destroy_source(facedata.g_source);
    if (error_code != MEDIA_VISION_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);

    error_code = mv_destroy_engine_config(facedata.g_engine_config);
    if (error_code != MEDIA_VISION_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);

    error_code = mv_face_tracking_model_destroy(facedata.g_face_track_model);
    if (error_code != MEDIA_VISION_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);
    ```

## Related Information
- Dependencies
  - Tizen 3.0 and Higher for Mobile
  - Tizen 3.0 and Higher for Wearable
