# Barcode Detection and Generation


You can perceive and understand an image or extract information from images in your application.

The main features of Media Vision BarCode API include:

- Handling images

  You can handle images by creating a source handle and filling it from an image buffer or media packet. [Create the source handle](#prepare) with the `mv_create_source()` function, and fill it with the `mv_source_fill_by_buffer()` or `mv_source_fill_by_media_packet()` function.

- Detecting barcodes

  You can [detect barcodes](#detect) in an image or from camera preview streams, and then decrypt them to display messages to the user.

  Before detecting a barcode, you must define the barcode detection target attribute value:

  - Detect both 1D and 2D barcodes
  - Detect 1D barcodes only
  - Detect 2D barcodes only

- Generating barcodes

  You can encrypt a given message, [generate a barcode](#generate) from it, and save it in a memory or as a file.

  Before generating a barcode, you must define the barcode text generation attribute value:

  - Generate barcode without an input message
  - Generate barcode with an input message (supports only 1D barcodes)

  You must also define the following [barcode specifications](#spec):

  - [Barcode type](#barcode)
  - [QR code specification](#qrcode) (if the QA code barcode type is used)
  - Image format (if the barcode is saved as a file)
    - JPEG
    - BMP
    - PNG

## Prerequisites

To enable your application to use the media vision barcode functionality:

1. To use the functions and data types of the Media Vision BarCode API (in [mobile](../../api/mobile/latest/group__CAPI__MEDIA__VISION__BARCODE__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__MEDIA__VISION__BARCODE__MODULE.html) applications), include the `<mv_barcode.h>` header file in your application:

   ```
   #include <mv_barcode.h>
   ```

2. To handle camera preview images in barcode detection, include the `<camera.h>` header file in your application:

   ```
   #include <camera.h>
   ```

<a name="prepare"></a>
## Preparing the Barcode Engines

To initialize the barcode detection and generation engines for use:

1. For barcode detection:

   1. Create a structure for storing the data required for barcode detection engine configuration:

      ```
      struct _bardetdata_s {
          /* Camera display variables */
          Evas_Object *win;
          Evas_Object *rect;
          Evas *evas;

          int preview_width;
          int preview_height;

          /* Media source handle */
          mv_source_h g_source;
          /* Barcode detection engine handle */
          mv_engine_config_h g_engine_cfg;

          /* Camera handle */
          camera_h g_camera;
      };
      typedef struct _bardetdata_s bargendata_s;

      static bardetdata_s bardetdata;
      ```

   2. Create a source handle using the `mv_create_source()` function with the `mv_source_h` member of the detection data structure as the out parameter:

      ```
      int error_code = 0;

      error_code = mv_create_source(&bardetdata.g_source);
      if (error_code != MEDIA_VISION_ERROR_NONE)
          dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);
      ```

      The source stores the barcode to be detected and all related data. You manage the source through the source handle.

   3. Create the barcode detection engine using the `mv_create_engine_config()` function. The function creates the `g_engine_cfg` engine configuration handle and configures it with default attributes.

      ```
      int error_code = 0;

      error_code = mv_create_engine_config(&bardetdata.g_engine_cfg);
      if (error_code != MEDIA_VISION_ERROR_NONE)
          dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);
      ```

      For example, to define the detection target, use the `mv_engine_config_set_int_attribute()` function with the `MV_BARCODE_DETECT_ATTR_TARGET` attribute. The possible values are defined in the `mv_barcode_detect_attr_target_e` enumeration (in [mobile](../../api/mobile/latest/group__CAPI__MEDIA__VISION__BARCODE__MODULE.html#ga47aaef5d40653352c5bee73b227062a6) and [wearable](../../api/wearable/latest/group__CAPI__MEDIA__VISION__BARCODE__MODULE.html#ga47aaef5d40653352c5bee73b227062a6) applications). The default value is `MV_BARCODE_DETECT_ATTR_TARGET_ALL`.

   4. To provide camera preview images, create the camera handle, set the camera display and the camera preview callback, and start the camera preview:

      ```
      /* Create the camera handle */
      error_code = camera_create(CAMERA_DEVICE_CAMERA0, &bardetdata.g_camera);
      if (error_code != CAMERA_ERROR_NONE)
          dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);

      /* Set the camera display */
      error_code = camera_set_display(bardetdata.g_camera, CAMERA_DISPLAY_TYPE_OVERLAY,
                                      GET_DISPLAY(bardetdata.win));
      if (error_code != CAMERA_ERROR_NONE)
          dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);

      /* Get the camera preview resolution */
      error_code = camera_get_preview_resolution(bardetdata.g_camera, &bardetdata.width,
                                                 &bardetdata.height);
      if (error_code != CAMERA_ERROR_NONE)
          dlog_print(DLOG_ERROR, LOG_TAG, "error code %d", error_code);

      /* Set the camera preview callback */
      error_code = camera_set_media_packet_preview_cb(bardetdata.g_camera,
                                                      _camera_media_packet_preview_cb,
                                                      NULL);
      if (error_code != CAMERA_ERROR_NONE)
          dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);

      /* Start the camera preview */
      error_code = camera_start_preview(barcodeAppData.g_camera);
      if (error_code != CAMERA_ERROR_NONE)
          dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);
      ```

      For more information on the `camera_set_display()` function, see [Configuring the Camera and its Callbacks](camera.md#configuring_callback) in the Camera guide.

2. For barcode generation:

   1. Create a structure for storing the data required for barcode generation engine configuration:

      ```
      struct _bargendata_s {
          /* Barcode information variables */
          mv_barcode_type_e type;
          mv_barcode_qr_ecc_e ecc;
          mv_barcode_qr_mode_e mode;
          int version;

          size_t width;
          size_t height;

          mv_barcode_image_format_e image_format;

          /* Media source handle */
          mv_source_h g_source;
          /* Barcode generation engine handle */
          mv_engine_config_h g_engine_cfg;
      };
      typedef struct _bargendata_s bargendata_s;

      static bargendata_s bargendata;
      ```

   2. Create the barcode generation engine using the `mv_create_engine_config()` function. The function creates the `g_engine_cfg` engine configuration handle and configures it with default attributes.

      ```
      int error_code = 0;

      error_code = mv_create_engine_config(&bargendata.g_engine_cfg);
      if (error_code != MEDIA_VISION_ERROR_NONE)
          dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);
      ```

      For example, to define whether the barcode is generated with text, use the `mv_engine_config_set_int_attribute()` function with the `MV_BARCODE_GENERATE_ATTR_TEXT` attribute. The possible values for the attribute are defined in the `mv_barcode_generate_attr_text_e` enumeration (in [mobile](../../api/mobile/latest/group__CAPI__MEDIA__VISION__BARCODE__MODULE.html#gaff049431f2259d00cfd0fdc7ee721858) and [wearable](../../api/wearable/latest/group__CAPI__MEDIA__VISION__BARCODE__MODULE.html#gaff049431f2259d00cfd0fdc7ee721858) applications). The default value is `MV_BARCODE_GENERATE_ATTR_TEXT_INVISIBLE`.

<a name="detect"></a>
## Detecting Barcodes

To detect barcodes:

1. To access the camera preview images in which to detect barcodes:

   1. Implement the `_camera_media_packet_preview_cb()` callback. This callback is invoked by the `camera_start_preview()` function after each captured preview image and returns a handle for the media packet containing the image.

   2. In the callback, fill the source with the media packet using the `mv_source_fill_by_media_packet()` function. This function takes as parameters the source handle and the media packet handle.

      The image is now stored in the source, and you can access the image through the source handle.

      ```
      static void
      _camera_media_packet_preview_cb(media_packet_h pkt, void *user_data)
      {
          mv_point_s mv_point = {0, 0};
          mv_rectangle_s mv_roi = {mv_point, bardetdata.width, bardetdata.height};

          if (pkt == NULL)
              return;

          error_code = mv_source_fill_by_media_packet(bardetdata.g_source, pkt);
          if (error_code != MEDIA_VISION_ERROR_NONE)
              dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error code);

          if (pkt) {
              error_code = media_packet_destroy(pkt);
              pkt = NULL;
          }
      }
      ```

2. In the `_camera_media_packet_preview_cb()` callback, detect barcodes in the image using the `mv_barcode_detect()` function:

   ```
   static void
   _camera_media_packet_preview_cb(media_packet_h pkt, void *user_data)
   {
       error_code = mv_barcode_detect(bardetdata.g_source, bardetdata.g_engine_cfg,
                                      mv_roi, _barcode_detected_cb, NULL);
       if (error_code != MEDIA_VISION_ERROR_NONE)
           dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);
   }
   ```

   The ROI (region of interest) feature allows you to define a rectangular region of the image in which to detect barcodes. In the above example code, the whole image is set as the ROI.

3. Implement a callback that is invoked by the `mv_barcode_detect()` function after it has finished processing the image for barcodes.

   Use the callback to handle the detection results, and to clear the source for the next image. To clear the source, use the `mv_source_clear()` function.

   The following example code implements a callback that prints the number of detected barcodes and their messages, if the number is greater than zero. The code also clears the source of the image data.

   ```
   static void
   _barcode_detected_cb(mv_source_h source, mv_engine_config_h engine_cfg,
                        const mv_quadrangle_s *barcode_locations, const char *message[],
                        const mv_barcode_type_e *types, int number_of_barcodes, void *user_data)
   {
       int i = 0;
       char type[50] = {'\0'};

       /* Clear the source for the next preview image */
       mv_source_clear(mv_source);

       if (number_of_barcode > 0) {
           dlog_print(DLOG_INFO, LOG_TAG, "the number of barcodes: %d", number_of barcode);
           for (i = 0; i < number_of_barcodes; i++)
               dlog_print(DLOG_INFO, LOG_TAG, "%d >> message: %s\n", I, messages[i]);
       }
   }
   ```

4. After the barcode detection is complete, stop the camera preview, unset the camera preview callback function, and destroy the camera handle:

   ```
   error_code = camera_stop_preview(bardetdata.g_camera);
   if (error_code != CAMERA_ERROR_NONE)
       dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);

   error_code = camera_unset_media_packet_preview_cb(bardetdata.g_camera);
   if (error_code != CAMERA_ERROR_NONE)
       dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);

   error_code = camera_destroy(bardetdata.g_camera);
   if (error_code != CAMERA_ERROR_NONE)
       dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);
   ```

   For more information, see [Releasing Resources](camera.md#release) in the Camera guide.

5. Destroy the source and barcode detection engine handles using the `mv_destroy_source()` and `mv_destroy_engine_config()` functions:

   ```
   error_code = mv_destroy_source(bardetdata.g_source)
   if (error_code != MEDIA_VISION_ERROR_NONE)
       dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);

   error_code = mv_destroy_engine_config(bardetdata.g_engine_cfg);
   if (error_code != MEDIA_VISION_ERROR_NONE)
       dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);
   ```

<a name="generate"></a>
## Generating Barcodes

To generate a barcode:

1. Set the barcode type. For the QR type, also set the error correction level, encoding mode, and version.

   ```
   bargendata.type = MV_BARCODE_QR;
   bargendata.ecc = MV_BARCODE_QR_ECC_LOW;
   bargendata.mode = MV_BARCODE_QR_MODE_BYTE;
   bargendata.version = 20;
   ```

2. To generate the barcode into memory:

   1. Create a source handle using the `mv_create_source()` function with the `mv_source_h` member of the generation data structure as the out parameter:

      ```
      int error_code = 0;

      error_code = mv_create_source(&bargendata.g_source);
      if (error_code != MEDIA_VISION_ERROR_NONE)
          dlog_print(DLOG_ERROR, LOG_TAG, "error code= %d", error_code);
      ```

      The source handle is used to save the generated barcode and related data into the source, and to access the barcode and related data from the source.

   2. Generate the barcode using the `mv_barcode_generate_source()` function:

      ```
      error_code = mv_barcode_generate_source(bargendata.g_engine_cfg,
                                              "MediaVision-Tutorial-QRcode",
                                              bargendata.type, bargendata.mode,
                                              bargendata.ecc, bargendata.version,
                                              bargendata.g_source);

      if (error_code != MEDIA_VISION_ERROR_NONE)
          dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);
      ```

   3. Retrieve the width, height, color space, and memory address of the barcode using the `mv_source_get_width()`, `mv_source_get_height()`, `mv_source_get_colorspace()`, and `mv_source_get_buffer()` functions:

      ```
      mv_colorspace_e image_colorspace = MEDIA_VISION_COLORSPACE_INVALID;
      unsigned int image_width = 0;
      unsigned int height_height = 0;
      unsigned char *image_buffer_ptr = NULL;
      unsigned int image_buffer_size = 0;

      error_code = mv_source_get_width(bargendata.g_source, &image_width);
      if (error_code != MEDIA_VISION_ERROR_NONE)
          dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);

      error_code = mv_source_get_height(bargendata.g_source, &image_height);
      if (error_code != MEDIA_VISION_ERROR_NONE)
          dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);

      error_code = mv_source_get_colorspace(bargendata.g_source, &image_colorspace);
      if (error_code != MEDIA_VISION_ERROR_NONE)
          dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);

      error_code = mv_source_get_buffer(bargendata.g_source, &image_buffer_ptr,
                                        &image_buffer_size);
      if (error_code != MEDIA_VISION_ERROR_NONE)
          dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);
      ```

   4. After the barcode generation is complete, destroy the source handle using the `mv_destroy_source()` function:

      ```
      error_code = mv_destroy_source(bargendata.g_source);
      if (error_code != MEDIA_VISION_ERROR_NONE)
          dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);
      ```

3. To generate the barcode into a file:

   1. Define the file format and image resolution:

      ```
      bargendata.width = 800;
      bargendata.height = 800;

      bargendata.image_format = MV_BARCODE_IMAGE_FORMAT_PNG;
      ```

   2. Generate the barcode using the `mv_barcode_generate_image()` function.

      The following example code saves the generated file in the `/opt/usr/media` directory with the file name `mv_barcode_qrcode.png`:

      ```
      error_code = mv_barcode_generate_image(bargendata.g_engine_cfg,
                                             "MediaVision-Tutorial-QRcode",
                                             bargendata.width, bargendata.height,
                                             bargendata.type, bargendata.mode,
                                             bargendata.ecc, bargendata.version,
                                             "/opt/usr/media/mv_barcode_qrcode.png",
                                             bargendata.image_format);

      if (error_code != MEDIA_VISION_ERROR_NONE)
          dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);
      ```

4. Destroy the barcode generation engine handle using the `mv_destroy_engine_config()` function:

   ```
   error_code = mv_destroy_engine_config(bargendata.g_engine_cfg);
   if (error_code != MEDIA_VISION_ERROR_NONE)
       dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);
   ```

<a name="spec"></a>
## Barcode Specifications

The following tables provide more information on the barcode generation specifications.

<a name="barcode"></a>
**Table: Supported barcode types**

| 1D or 2D | Type                                     | Description                              | Example                                  |
|----------|------------------------------------------|------------------------------------------|------------------------------------------|
| 1-D      | UPC-A                                    | Universal product code with numeric 12-digit | ![UPC-A](./media/mediavision_upc_a.png) |
| 1-D      | UPC-E              | Universal product code with numeric 6-digit | ![UPC-E](./media/mediavision_upc_e.png) |
| 1-D      | EAN-8              | International article number with numeric 8-digit | ![EAN-8](./media/mediavision_ean_8.png) |
| 1-D      | EAN-13             | International article number with numeric 13-digit | ![EAN-13](./media/mediavision_ean_13.png) |
| 1-D      | CODE-128           | Code 128; supports alphanumeric or numeric-only | ![CODE-128](./media/mediavision_code_128.png) |                                          |
| 1-D      | CODE-39            | Code 39; supports 34 characters consisting of uppercase letters (A to Z), numeric digits (0 to 9), and special characters(-, ., $, /, %, space) | ![CODE-39](./media/mediavision_code_39.png) |                                          |
| 1-D      | INTERLEAVED 2 of 5 | Interleaved 2 of 5 with numeric digits   | ![UPC-A](./media/mediavision_interleaved_2_5.png) |                                          |
| 2-D      | QR code                                  | Quick Response code                      | ![UPC-A](./media/mediavision_qr.png) |

<a name="qrcode"></a>
**Table: Supported QR code specifications**

| Specification                     | Support type      | Description                         |
|-----------------------------------|-------------------|-------------------------------------|
| Error Correction Code (ECC) Level | ECC Low           | Recovery up to 7% damage            |
| Error Correction Code (ECC) Level | ECC Medium        | Recovery up to 15% damage           |
| Error Correction Code (ECC) Level | ECC Quartile      | Recovery up 25% damage              |
| Error Correction Code (ECC) Level | ECC High          | Recovery up to 30% damage           |
| Encoding mode                     | Numeric           | Numeric digits ('0', '1', ..., '9') |
| Encoding mode                     | Alphanumeric      | Alphanumeric characters: numeric (0, 1, ..., 9), characters (A, B, ..., Z), and punctuation (' ', $, %, *, +, -, '.', /, ':') |
| Encoding mode                     | Byte 8-bit        | Raw 8-bit bytes                     |
| Encoding mode                     | UTF-8             | Universal character set and Transformation Format 8-bit, encoding characters |

## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 3.0 and Higher for Wearable
