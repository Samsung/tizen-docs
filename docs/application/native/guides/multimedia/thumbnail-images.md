# Thumbnail Images


Tizen allows you to create a thumbnail from an input media file.

The main features of the Thumbnail Util API include:

- Video and image thumbnails

  You can [create thumbnails](#get_thumbnail) from video and image files. Audio files are not supported.

- Custom size

  You can create the thumbnail using any size you like. The Thumbnail Util API outputs the results according to the size you have set. This means that the thumbnail can be generated even if the output size differs from the original aspect ratio.

The requested thumbnail is provided as a raw data type with the BGRA color space, not a JPG or PNG file. If you want to save the thumbnail to a file, you must encode it.

## Prerequisites

To enable your application to use the thumbnail util functionality:

1. To use the functions and data types of the Thumbnail Util API (in [mobile](../../api/mobile/latest/group__CAPI__MEDIA__THUMBNAIL__UTIL__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__MEDIA__THUMBNAIL__UTIL__MODULE.html) applications), include the `<thumbnail_util.h>` header file in your application:

   ```
   #include <thumbnail_util.h>
   ```

2. To work with the Thumbnail Util API, define a handle variable for the thumbnail utility:

   ```
   static thumbnail_h g_thumb_h = NULL;
   ```

   This guide uses a global variable for the handle.

3. Make sure you have access to the file whose thumbnail you want to extract.

   This guide uses a JPEG image file, which is accessed through its file path. The following example code uses internal storage, so you must include the `<storage.h>` header file for the code to work.

   ```
   int internal_storage_id;
   char *internal_image_storage_path;
   char *image_file_name = "test_image.jpg";
   char *image_test_path;

   static bool
   storage_cb(int storage_id, storage_type_e type, storage_state_e state,
              const char *path, void *user_data)
   {
       if (type == STORAGE_TYPE_INTERNAL) {
           internal_storage_id = storage_id;

           return false;
       }

       return true;
   }

   void
   _get_internal_storage_path()
   {
       int error;
       char *path = NULL;

       error = storage_foreach_device_supported(storage_cb, NULL);
       error = storage_get_directory(internal_storage_id, STORAGE_DIRECTORY_IMAGES, &path);
       if (error != STORAGE_ERROR_NONE) {
           internal_image_storage_path = strdup(path);
           free(path);
       }
   }

   void
   _make_test_path()
   {
       int path_len = 0;

       path_len = strlen(internal_image_storage_path) + strlen(image_file_name) + 1;
       image_test_path = malloc(path_len);
       memset(image_test_path, 0x0, path_len);

       strncat(image_test_path, internal_image_storage_path, strlen(internal_image_storage_path));
       strncat(image_test_path, image_file_name, strlen(image_file_name));
   }
   ```

> **Note**  
> The Thumbnail Util functions can use both common content in the device storage (internal or external) and private content in your application data.

<a name="get_thumbnail"></a>
## Extracting a Thumbnail

To extract a thumbnail from the file:

1. Create the thumbnail utility handle using the `thumbnail_util_create()` function:

   ```
   ret = thumbnail_util_create(&g_thumb_h);
   ```

2. Set the path to the file using the `thumbnail_util_set_path()` function:

   ```
   ret = thumbnail_util_set_path(g_thumb_h, image_test_path);
   ```

   The function binds the thumbnail utility handle (first parameter) with the file specified in the path variable (second parameter).

3. Set the thumbnail size using the `thumbnail_util_set_size()` function:

   ```
   int width = 512;
   int height = 288;

   ret = thumbnail_util_set_size(g_thumb_h, width, height);
   ```

   If you do not set the size, the Thumbnail Util API use a default size of 320 x 240.

4. Extract the thumbnail from the file using the `thumbnail_util_extract()` function. As parameters, define the thumbnail utility handle, a callback for checking the extraction result, user data, and a request ID.

   ```
   void
   thumbnail_completed_cb(thumbnail_util_error_e error, const char *request_id,
                          int raw_width, int raw_height, unsigned char *raw_data,
                          int raw_size, void *user_data)
   {
       dlog_print(DLOG_DEBUG, LOG_TAG, "REQUEST ID: %s\n", request_id);
       dlog_print(DLOG_DEBUG, LOG_TAG, "WIDTH: %d, HEIGHT: %d\n", raw_width, raw_height);
   }

   void
   extract()
   {
       char *request_id = NULL;

       ret = thumbnail_util_extract(g_thumb_h, thumbnail_completed_cb, NULL, &request_id);
   }
   ```

   After calling the function, check whether the return value is `THUMBNAIL_UTIL_ERROR_NONE`. If it is, the function extracted the thumbnail successfully and stored it in the `raw_data` parameter returned by the callback. Otherwise, the function failed because of an error, which you need to handle.

   The request ID is returned in the `request_id` parameter of the callback. You can use it to distinguish between different-sized thumbnails extracted from the same file, or to cancel a specific extraction request using the `thumbnail_util_cancel()` function.

   The thumbnail is raw data that you can display on the screen directly. You can also encode and save the thumbnail to a file. When no longer needed, release the thumbnail using the `free()` function.

5. When no longer needed, destroy the thumbnail utility handle using the `thumbnail_util_destroy()` function:

   ```
   thumbnail_util_destroy(g_thumb_h);
   ```

## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 3.0 and Higher for Wearable
