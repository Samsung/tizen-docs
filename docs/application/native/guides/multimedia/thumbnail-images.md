# Thumbnail Images


Tizen allows you to create a thumbnail from an input media file.

The main features of the Thumbnail Util API include:

- Video and image thumbnails

  You can [create thumbnails](#get_thumbnail) from video and image files. Thumbnail Util API does not support audio files.

- Custom size

  You can create the thumbnail of any size.

The API provides the requested thumbnail as raw data or a file.

In case of raw data, if the requested media is a video, thumbnail is RGB colorspace. And if it is an image, thumbnail is BGRA colorspace.

In case of a file, thumbnails are encoded with a user-specified extension.

> **Note**
>
> See `thumbnail_util_extract_to_file()` for details regarding extensions.


## Prerequisites

To enable your application to use the thumbnail util functionality:

1. To use the functions and data types of the Thumbnail Util API (in [mobile](../../api/mobile/latest/group__CAPI__MEDIA__THUMBNAIL__UTIL__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__MEDIA__THUMBNAIL__UTIL__MODULE.html) applications), include the `<thumbnail_util.h>` header file in your application:

   ```
   #include <thumbnail_util.h>
   ```

2. Ensure that you have access to the file required to extract the thumbnail.

   This guide uses a JPEG image file, which is accessed through its file path. Include the <storage.h> header file as the example code uses internal storage. The example code is as follows:

   ```
   int internal_storage_id;
   char *internal_image_storage_path;
   char *image_file_name = "test_image.jpg";
   char *image_test_path;
   char *out_file_name = "result_image.jpg";
   char *out_test_path;

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
       
       strncat(out_test_path, internal_image_storage_path, strlen(internal_image_storage_path));
       strncat(out_test_path, out_file_name, strlen(out_file_name));
   }
   ```

> **Note**  
> The Thumbnail Util functions can use both common content in the device storage (internal or external) and private content in your application data.

<a name="get_thumbnail"></a>
## Extract a Thumbnail

To extract a thumbnail from the file:

1. To receive the results in a file, use the `thumbnail_util_extract_to_file()` function:

   ```
   ret = thumbnail_util_extract_to_file(image_test_path, 512, 288, out_test_path);
   ```

   You find a thumbnail file on `out_test_path`.

2. To receive the results in a raw data, use the `thumbnail_util_extract_to_buffer()` function:

   ```
   unsigned char *out_buf;
   size_t out_buf_size;
   unsigned int out_width;
   unsigned int out_height;
   
   ret = thumbnail_util_extract_to_buffer(image_test_path, 512, 288, &out_buf, &out_buf_size, &out_width, &out_height);
   ```

   You get a BGRA color image.

> **Note**  
>
> Since Tizen 5.5, if the requested width and height of the thumbnail are bigger than the image, then the thumbnail size is changed to the image size.

## Related Information
- Dependencies
  - Tizen 5.0 and Higher for Mobile
  - Tizen 5.0 and Higher for Wearable
