# Deep Learning Based Object Detection

This guide provides instructions on how to utilize the provided Object Detection API within your application to identify objects in a given image.

## Prerequisites
Ensure the following prerequisites are satisfied:
Include the necessary headers `mv_object_detection.h` in your project
    ```
	#include <mv_object_detection.h>
	```

Optionally, include additional headers for handling image decoding `image_util.h` or acquiring preview images from cameras
    ```
	#include <image_util.h>  // Optional: Image decoding support
    #include <camera.h>      // Optional: Acquiring preview images from cameras
	```

## Detect objects in an image
Follow these steps to implement object detection in your application:

Step 1: Initialize and Prepare
First, create a object detection handle and prepare the environment for object detection:
   ```
   mv_object_detection_h handle;
   int ret = 0;

   ret = mv_object_detection_create(&handle);
   if (ret != MEDIA_VISION_ERROR_NONE) {
       // handle an error.
   }

    ret = mv_object_detection_configure(handle);
    if (ret != MEDIA_VISION_ERROR_NONE) {
        // handle an error.
    }

   ret = mv_object_detection_prepare(handle);
   if (ret != MEDIA_VISION_ERROR_NONE) {
       // handle an error.
   }
   ```

Step 2: Input Source Setup
Next, set up the input source containing the image data. Here, we'll demonstrate decoding an image file and filling the resulting data into a mv_source:
   ```
   char filePath[1024];
   unsigned char *dataBuffer = NULL;
   size_t bufferSize = 0;
   unsigned int width = 0;
   unsigned int height = 0;
   image_util_decode_h imageDecoder = NULL;
   mv_source_h mv_source = NULL;
   image_util_image_h decodedImage = NULL;

   ret = mv_create_source(&mv_source);
   if (ret != MEDIA_VISION_ERROR_NONE) {
       // handle an error.
   }

   ret = image_util_decode_create(&imageDecoder);
   if (ret != IMAGE_UTIL_ERROR_NONE) {
       // handle an error.
   }

   /* Decode image and fill the image data to mv_source handle */
   snprintf(filePath, 1024, "/path/to/object_image.jpg");
   ret = image_util_decode_set_input_path(imageDecoder, filePath);
   if (ret != IMAGE_UTIL_ERROR_NONE) {
       // handle an error.
   }

   ret = image_util_decode_set_colorspace(imageDecoder, IMAGE_UTIL_COLORSPACE_RGB888);
   if (ret != IMAGE_UTIL_ERROR_NONE) {
       // handle an error.
   }

   ret = image_util_decode_run2(imageDecoder, &decodedImage);
   if (ret != IMAGE_UTIL_ERROR_NONE) {
       // handle an error.
   }

   ret = image_util_get_image(decodedImage, &width, &height, NULL, &dataBuffer, &bufferSize);
   if (ret != IMAGE_UTIL_ERROR_NONE) {
       // handle an error.
   }

   ret = mv_source_fill_by_buffer(mv_source, dataBuffer, (unsigned int)bufferSize,
                                 width, height, MEDIA_VISION_COLORSPACE_RGB888);
   if (ret != MEDIA_VISION_ERROR_NONE) {
      free(dataBuffer);
	  // handle an error.
   }

   ret = image_util_decode_destroy(imageDecoder);
   if (ret != IMAGE_UTIL_ERROR_NONE) {
       // handle an error.
   }

   ret = image_util_destroy_image(decodedImage);
   if (ret != IMAGE_UTIL_ERROR_NONE) {
       // handle an error.
   }
   ```

Step 3: Object Detection Execution
There are two modes available for executing object detection: synchronous and asynchronous. Choose the appropriate mode based on your application requirements:

[Synchronous Mode]
For synchronous processing, call mv_object_detection_inference() with the prepared mv_source. This API will be returned after the completion of the inference request:
        ```
        // Detect objects in a given image.
        ret = mv_object_detection_inference(handle, mv_source);
        if (ret != MEDIA_VISION_ERROR_NONE) {
            // handle an error.
        }
		```

Afterwards, retrieve the number of detected objects and obtain their respective bounding boxes:
        ```
		unsigned long frame_number;
		unsigned int number_of_objects;

		ret = mv_object_detection_get_result_count(handle, &frame_number, &number_of_objects);
		if (ret!= MEDIA_VISION_ERROR_NONE) {
			// handle an error.
		}

		for (unsigned int idx = 0; idx < number_of_objects; ++idx) {
			int left, top, right, bottom;

			int ret = mv_object_detection_get_bound_box(handle, frame_number, idx, &left, &top, &right, &bottom);
			if (ret!= MEDIA_VISION_ERROR_NONE) {
				// handle an error.
			}
		}

		// Process bounding box information...
        ```

[Asynchronous Mode]
The asynchronous API, mv_object_detection_inference_async(), returns immediately after being called, and inference results can be obtained by creating a thread and calling the mv_object_detection_get_result_count() API within its callback function.
If asynchronous processing is preferred, invoke mv_object_detection_inference_async() with the prepared mv_source, and handle the results via a callback function:
	```
	void object_detection_callback(void *user_data)
	{
		mv_object_detection_h handle = (mv_object_detection_h)user_data;
		bool is_loop_exit = false;

		while (!is_loop_exit) {
			unsigned long frame_number;
			unsigned int number_of_objects;

			int ret = mv_object_detection_get_result_count(handle, &frame_number, &number_of_objects);
			if (ret!= MEDIA_VISION_ERROR_NONE) {
				// handle an error.
			}

			for (unsigned int idx = 0; idx < number_of_objects; ++idx) {
				int left, top, right, bottom;

				int ret = mv_object_detection_get_bound_box(handle, idx, &left, &top, &right, &bottom);
				if (ret!= MEDIA_VISION_ERROR_NONE) {
					// handle an error.
				}
			}
		}
	}

    void some_function()
	{
		...

		// Detect objects in a given image.
		ret = mv_object_detection_inference_async(handle, mv_source);
		if (ret!= MEDIA_VISION_ERROR_NONE) {
			// handle an error.
		}

		// Create a new thread to wait for the inference result.
		thread *thread_handle = new thread(&object_detection_callback, (void *)handle);
		if (thread_handle == NULL) {
			// handle an error.
		}

		thread_handle->join();
	}
	```

Step 4: Cleanup
Finally, clean up by releasing the allocated resources and destroying the handle:
    ```
    ret = mv_object_detection_destroy(handle);
    if (ret != MEDIA_VISION_ERROR_NONE) {
        // handle an error.
    }
    ```

## Related information
- Dependencies
  - Tizen 9.0 and Higher for TV