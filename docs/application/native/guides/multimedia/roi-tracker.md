# ROI Tracker

ROI Tracker is one of the main features of the Media Vision API. This API allows user to obtain proper roi coordinates that user want to track.
For example, when an image and roi coordinates that user want to track continuously are provided as input to this API, the Media Vision framework while doing provided image and roi coordinates of the decoded image data, will provides roi coordinates in given image.

## Prerequisites

To enable your application to use the media vision ROI tracker functionality:

1. To use the functions and data types of the Media Vision ROI Tracker API (in mobile and wearable applications), include the `<mv_roi_tracker.h>` header file in your application.

   ```c
   #include <mv_roi_tracker.h>
   ```

2. Create a callback function to store the returned roi data.

     For getting roi coordinates result, make callback function:

     ```c
    void _tracked_cb(mv_source_h source, mv_rectangle_s roi, void *user_data)
    {
        printf("In callback: roi.x y width height : %d %d %d %d\n", roi.point.x, roi.point.y, roi.width, roi.height);
    }
     ```

<a name="ROITracker"></a>
## Track object

To track a roi of iamge:

1. Create the source and engine configuration handles:

    ```c
    int error_code = 0;

    error_code = mv_create_source(&mv_source);
    if (error_code != MEDIA_VISION_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);

    error_code = mv_create_engine_config(&imagedata.g_engine_config);
    if (error_code != MEDIA_VISION_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "error code= %d", error_code);
    ```
2. Decode the image file and fill the `mv_source` handle with the decoded raw data.

   In the following example, `sample.jpg` is the image to be tracked, and it is in the `<OwnDataPath>`.
   The `<OwnDataPath>` refers to your own data path. Uses ImageHelper to fill `mv_source`:

    ```c
    mv_source_h mv_source = NULL;

	ret = mv_create_source(&mv_source);
	ASSERT_EQ(ret, MEDIA_VISION_ERROR_NONE);

	ret = ImageHelper::loadImageToSource(image_path.c_str(), mv_source);
	ASSERT_EQ(ret, MEDIA_VISION_ERROR_NONE);
    ```

3. To Track the `sample.jpg` image, create a `handle` media vision ROI Tracker handle:

    ```c
    error_code = mv_roi_tracker_create(&handle);
    if (error_code != MEDIA_VISION_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);
    ```

4. Set tracker mode for running tracker. Defaut mode is `MV_ROI_TRACKER_TYPE_BALANCE`:
    ```c
    int error_code = 0;
    error_code = mv_engine_config_set_int_attribute(engine_cfg, MV_ROI_TRACKER_TYPE, (int) MV_ROI_TRACKER_TYPE_BALANCE);
	if (ret != MEDIA_VISION_ERROR_NONE)
		dlog_print(DLOG_ERROR, LOG_TAG, "error code= %d", error_code);
    ```
    For more information on the configuration attributes such as `MV_ROI_TRACKER_TYPE_BALANCE`, see Media Vision ROI Tracker API (in mobile and wearable applications).

5. Use `mv_roi_tracker_configure()` to configure `handle` ROI Tracker handle with `config`:
    ```c
    error_code = ret = mv_roi_tracker_configure(handle, config);
    if (error_code != MEDIA_VISION_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);
    ```

6. Use `mv_roi_tracker_prepare()` to prepare ROI Traking. Uses coordinates(x,y,width,height) that want to track inside of image:
    ```c
    int x, y, width, height;
    error_code = mv_roi_tracker_prepare(handle, x, y, width, height);
    if (error_code != MEDIA_VISION_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);
    ```

7. Use `mv_roi_tracker_perform()` to track the image continuously.:

    ```c
    error_code = mv_roi_tracker_perform(handle, mv_source, _tracked_cb, NULL);
    if (error_code != MEDIA_VISION_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);
    ```

   `mv_roi_tracker_perform()` invokes `_tracked_cb()` callback.
    The following callback example prints the tracked coordinates:

    ```c
    static 
    void _tracked_cb(mv_source_h source, mv_rectangle_s roi, void *user_data)
    {
        printf("In callback: roi.x y width height : %d %d %d %d\n", roi.point.x, roi.point.y, roi.width, roi.height);
    }
    ```

8. After the ROI tracking is complete, destroy the source, engine configuration, and the ROI Traker handles using `mv_destroy_source()`, `mv_destroy_engine_config()`, and `mv_roi_tracker_destroy()`:

    ```c
    error_code = mv_destroy_source(mv_source);
    if (error_code != MEDIA_VISION_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);

    error_code = mv_destroy_engine_config(config);
    if (error_code != MEDIA_VISION_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);

    error_code = mv_roi_tracker_destroy(handle);
    if (error_code != MEDIA_VISION_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "error code = %d", error_code);
    ```

## Related information
- Dependencies
  - Tizen 7.0 and Higher for Mobile
  - Tizen 7.0 and Higher for Wearable
