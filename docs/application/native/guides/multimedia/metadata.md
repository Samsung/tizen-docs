# Metadata


To handle content metadata, you can use the following features:

- Metadata extraction

  Media files, such as MP3 and MP4 files, contain [extractable metadata](#attribute2). You can [extract metadata](#get_metadata) from such media files with the metadata extractor.

  **Figure: Getting metadata**

  ![Getting metadata](./media/metadata.png)

  The metadata extractor can be used with video and audio files only. It is not supported for image files.

- MIME type information

  You can [get the MIME type](#get_file_ext) for a file extension and [get a list of extensions](#get_mime) associated, for example, with an image or the JPEG MIME type.

## Prerequisites

To enable your application to use the metadata functionality:

1. To use the functions and data types of the [Metadata Extractor API](../../api/common/latest/group__CAPI__METADATA__EXTRACTOR__MODULE.html), include the `<metadata_extractor.h>` header file in your application:

   ```
   #include <metadata_extractor.h>
   ```

   To ensure that a Metadata Extractor function has been executed properly, make sure that the return value is equal to `METADATA_EXTRACTOR_ERROR_NONE`.

2. To work with the Metadata Extractor API, define a handle variable for the metadata extractor:

   ```
   static metadata_extractor_h g_metadata_h = NULL;
   ```

   This guide uses a global variable for the handle.

3. Make sure you have access to the files whose metadata you want to extract, and make sure the files contain metadata, since the Metadata Extractor API only works on files with metadata.

   > **Note**
   >
   > The Metadata Extractor functions can use both common content in the device storage (internal or external) and private content in your application data.

   This guide uses 2 files: an MP3 audio file and an MP4 video file, which are accessed through their file paths. The following example code uses an internal storage, so you must include the `storage.h` header file for the code to work.

   ```
   int internal_storage_id;
   char *internal_music_storage_path;
   char *internal_video_storage_path;
   char *music_file_name = "test_music.mp3";
   char *video_file_name = "test_video.mp4";
   char *music_test_path;
   char *video_test_path;

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
       error = storage_get_directory(internal_storage_id, STORAGE_DIRECTORY_MUSIC, &path);
       if (error != STORAGE_ERROR_NONE) {
           internal_music_storage_path = strdup(path);
           free(path);
       }

       error = storage_get_directory(internal_storage_id, STORAGE_DIRECTORY_VIDEOS, &path);
       if (error != STORAGE_ERROR_NONE) {
           internal_video_storage_path = strdup(path);
           free(path);
       }
   }

   void
   _make_test_path()
   {
       int path_len = 0;

       path_len = strlen(internal_music_storage_path) + strlen(music_file_name) + 1;
       music_test_path = malloc(path_len);
       memset(music_test_path, 0x0, path_len);

       strncat(music_test_path, internal_music_storage_path, strlen(internal_music_storage_path));
       strncat(music_test_path, music_file_name, strlen(music_file_name));

       path_len = strlen(internal_video_storage_path) + strlen(video_file_name) + 1;
       video_test_path = malloc(path_len);
       memset(video_test_path, 0x0, path_len);

       strncat(video_test_path, internal_video_storage_path, strlen(internal_video_storage_path));
       strncat(video_test_path, video_file_name, strlen(video_file_name));
   }
   ```

4. To use the functions and data types of the [MIME Type API](../../api/common/latest/group__CAPI__CONTENT__MIME__TYPE__MODULE.html), include the `<mime_type.h>` header file in your application:

   ```
   #include <mime_type.h>
   ```

<a name="get_metadata"></a>
## Retrieving Metadata

To retrieve metadata from the file:

1. Create the metadata extractor handle using the `metadata_extractor_create()` function:

   ```
   ret = metadata_extractor_create(&g_metadata_h);
   ```

2. Set the path to the file whose metadata you want to retrieve using the `metadata_extractor_set_path()` function:

   ```
   ret = metadata_extractor_set_path(g_metadata_h, video_test_path);

   /* Or */

   ret = metadata_extractor_set_path(g_metadata_h, music_test_path);
   ```

   The function binds the metadata extractor handle (first parameter) with the file specified in the path variable (second parameter).

3. Retrieve the metadata from the file using the `metadata_extractor_get_metadata()` function. Retrieve each piece of metadata (each metadata attribute) individually.

   As parameters, define the metadata extractor handle, the attribute you want to retrieve, and a pointer to the `char` variable in which you want to store the attribute value. The possible attributes are defined in the [`metadata_extractor_attr_e` enumeration](../../api/common/latest/group__CAPI__METADATA__EXTRACTOR__MODULE.html#ga5b27fedbf5aaa22106f88b831c596872).

   The following example code retrieves the duration and prints it on the screen. You can retrieve other attributes by defining a different attribute enumerator as the second parameter.

   ```
   char *value = NULL;

   ret = metadata_extractor_get_metadata(g_metadata_h, METADATA_DURATION, &value);
   dlog_print(DLOG_DEBUG, LOG_TAG, "METADATA_DURATION: %s\n", value);
   if (value != NULL) {
       free(value);
       value = NULL;
   }
   ```

   To avoid memory leaks, release the `value` variable using the `free()` function when you no longer need the variable.

4. For an audio file, retrieve the artwork from the file using the `metadata_extractor_get_artwork()` function.

   The retrieved artwork information is available in the 3 out parameters, which define the artwork image, image size, and MIME type.

   The following example code retrieves the artwork and prints the image size and MIME type on the screen:

   ```
   int artwork_size = 0;
   void *artwork = NULL;
   char *artwork_mime = NULL;

   ret = metadata_extractor_get_artwork(g_metadata_h, &artwork, &artwork_size, &artwork_mime);
   dlog_print(DLOG_DEBUG, LOG_TAG, "Artwork: size: %d, mime type: %s\n", artwork_size, artwork_mime);
   if (artwork != NULL) {
       free(artwork);
       artwork = NULL;
   }

   if (artwork_mime != NULL) {
       free(artwork_mime);
       artwork_mime = NULL;
   }
   ```

   To avoid memory leaks, release the `artwork` and `artwork_mime` variables using the `free()` function when you no longer need the variables.

5. For an audio file, retrieve the synchronized lyrics from the file using the `metadata_extractor_get_synclyrics()` function.

   The following example code retrieves the synchronized lyrics from index number 1 and prints the time information and lyrics on the screen:

   ```
   unsigned long time_info = 0;
   char *lyrics = NULL;

   ret = metadata_extractor_get_synclyrics(g_metadata_h, 1, &time_info, &lyrics);
   if (lyrics != NULL) {
       dlog_print(DLOG_DEBUG, LOG_TAG, "Synclyrics: time_info: %d, lyrics: %s\n", time_info, lyrics);
       free(lyrics);
       lyrics = NULL;
   }
   ```

   To retrieve the synchronized lyrics index number, use the `metadata_extractor_get_metadata()` function with the `METADATA_SYNCLYRICS_NUM` attribute.

   To avoid memory leaks, release the `lyrics` variable using the `free()` function when you no longer need the variable.

6. For a video file, retrieve frames from the file in one of the following ways:

   - To retrieve a frame without specifying the time when the frame appears, use the `metadata_extractor_get_frame()` function.
   - To retrieve a frame at a specified time, use the `metadata_extractor_get_frame_at_time()` function.

   The following example code first retrieves a frame at an unspecified time and prints the frame size, and then retrieves another frame at a specified time and prints its size:

   ```
   /* Use metadata_extractor_get_frame() */
   int frame_size = 0;
   void *frame = NULL;

   ret = metadata_extractor_get_frame(g_metadata_h, &frame, &frame_size);
   dlog_print(DLOG_DEBUG, LOG_TAG, "Frame: size: %d\n", frame_size);
   if (frame != NULL) {
       free(frame);
       frame = NULL;
   }

   /* Use metadata_extractor_get_frame_at_time() */
   unsigned long timestamp = 500;

   ret = metadata_extractor_get_frame_at_time(g_metadata_h, timestamp, true, &frame, &frame_size);
   dlog_print(DLOG_DEBUG, LOG_TAG, "Frame at %d: size: %d\n", timestamp, frame_size);
   if (frame != NULL) {
       free(frame);
       frame = NULL;
   }
   ```

   To avoid memory leaks, release the `frame` variable using the `free()` function when you no longer need the variable.

7. When no longer needed, destroy the metadata extractor handle using the `metadata_extractor_destroy()` function:

   ```
   metadata_extractor_destroy(g_metadata_h);
   ```

<a name="get_file_ext"></a>
## Getting the MIME Type for a File Extension

To get the MIME types of all files in a directory when the extensions are known:

- For an individual file extension:

  Use the `mime_type_get_mime_type()` function. The first parameter is the file extension without the leading dot and the second parameter is the MIME type for the given file extension.

  The MIME type is `'application/octet-stream'` if the given file extension is not associated with any specific file format.

  ```
  #include <dirent.h>
  #include <string.h>

  char *mime_type;
  int error = mime_type_get_mime_type("jpg", &mime_type);
  ```

- For the extensions of all files in the resource directory:

  1. To get the directory content, use the `dirent` structure available in the `<dirent.h>` header:

    ```
    struct dirent *pDirent = NULL;
    DIR *dir;
    char *res_path = app_get_resource_path();
    if (!res_path)
        /* Error handling */
    dir = opendir(res_path);
    if (dir) {
        while ((pDirent = readdir(dir)) != NULL) {
            if (pDirent->d_type != DT_REG) /* Only regular files */
                continue;
    ```

  2. Get the extension from a file name using the `strrchr()` function available in the `<string.h>` header. Incrementing the pointer address is necessary, so use the extension without a dot:

     ```
             char *extension = strrchr(pDirent->d_name, '.');
             if (!extension)
                 continue;
             extension++;
     ```

  3. Use the `mime_type_get_mime_type()` function to get the MIME type of each file using the extension pointer as an extension:

     ```
             mime_type_get_mime_type(extension, &mime_type);
             /* Here you have a MIME type in its variable */
             free(mime_type);
         }
         closedir(dir);
     }
     ```

<a name="get_mime"></a>
## Getting Extensions for a MIME Type

To get a list of extensions associated, for example, with an image or JPEG MIME type, use the `mime_type_get_file_extension()` function.

The function takes the MIME type as an input parameter, and fills the array of file extensions and the array length (marked as zero if empty) as the output parameters.

```
char **extension;
int length;
int error = mime_type_get_file_extension("image/jpeg", &extension, &length);

int i;
for (i = 0; i < length; i++)
    /* Use extension[i] */

for (i = 0; i < length; i++)
    free(extension[i]);
free(extension);
```

<a name="attribute2"></a>
## Extractable Metadata Attributes

The following table lists the extractable metadata.

**Table: Metadata extractor attributes**

| Attribute                     | Description                          |
|-------------------------------|--------------------------------------|
| `METADATA_DURATION`           | Duration of the content              |
| `METADATA_VIDEO_BITRATE`      | Bitrate of the video content         |
| `METADATA_VIDEO_FPS`          | FPS of the video content             |
| `METADATA_VIDEO_WIDTH`        | Width of the video content           |
| `METADATA_VIDEO_HEIGHT`       | Height of the video content          |
| `METADATA_HAS_VIDEO`          | Whether the content has video stream |
| `METADATA_AUDIO_BITRATE`      | Bitrate of the audio content         |
| `METADATA_AUDIO_CHANNELS`     | Channel of the audio content         |
| `METADATA_AUDIO_SAMPLERATE`   | Sample rate of the audio content     |
| `METADATA_AUDIO_BITPERSAMPLE` | Bit per sample of the audio content  |
| `METADATA_HAS_AUDIO`          | Whether the content has audio stream |
| `METADATA_ARTIST`             | Artist of the content                |
| `METADATA_TITLE`              | Title of the content                 |
| `METADATA_ALBUM`              | Album of the content                 |
| `METADATA_ALBUM_ARTIST`       | Album artist of the content          |
| `METADATA_GENRE`              | Genre of the content                 |
| `METADATA_COMPOSER`           | Composer of the content                |
| `METADATA_COPYRIGHT`          | Copyright of the content             |
| `METADATA_DATE`               | Date of the content                  |
| `METADATA_DESCRIPTION`        | Description of the content           |
| `METADATA_COMMENT`            | Comment about the content            |
| `METADATA_TRACK_NUM`          | Track number of the content          |
| `METADATA_CLASSIFICATION`     | Classification of the content        |
| `METADATA_RATING`             | Rating of the content                |
| `METADATA_LONGITUDE`          | Longitude of the content             |
| `METADATA_LATITUDE`           | Latitude of the content              |
| `METADATA_ALTITUDE`           | Altitude of the content              |
| `METADATA_CONDUCTOR`          | Conductor of the content             |
| `METADATA_UNSYNCLYRICS`       | Asynchronous lyrics of the content   |
| `METADATA_SYNCLYRICS_NUM`     | Synchronous lyrics of the content    |
| `METADATA_RECDATE`            | Recorded date of the content         |
| `METADATA_ROTATE`             | Orientation of the content           |

## Related Information
- Dependencies
  - Since Tizen 2.4
