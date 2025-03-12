# Deep Learning Based Face Recognition

Using deep learning based face recognition, you can perceive and understand faces within your application. This document is a guide on how to register a new face, how to unregister a face that is registered with a given label, and how to recognize a given face.

## Prerequisites

To enable your application for using the deep learning based face recognition functionality, follow these steps:
1.  To use the functions and data types of the deep learning based face recognition API, include the `<mv_face_recognition.h>` header file in your application.
2.  In addition, you may need to include the `<image_util.h>` header file to handle the image decoding task, or the `<camera.h>` header file to provide preview images. 
    Keep in mind that you could use other libraries if required.

    ```
    #include <mv_face_recognition.h>

    /* To decode the image file. */
    #include <image_util.h>
    /* To get preview image from Camera device. */
    #include <camera.h>
    ```
## Register a new face
To register a new face image with a given label, follow these steps:

1. Create a face recognition handle and prepare for the face recognition framework. This is shown in the following code snippet:

   ```
   mv_face_recognition_h handle;
   int ret = 0;

   ret = mv_face_recognition_create(&handle);
   if (ret != MEDIA_VISION_ERROR_NONE) {
       // handle an error.
   }

   ret = mv_face_recognition_prepare(handle);
   if (ret != MEDIA_VISION_ERROR_NONE) {
       // handle an error.
   }
   ```

2. Prepare an input source to register. The input source should be RGB data. In this guide, we will use an image file as an input source, and we will show you how to decode the given image file and then prepare for a mv_source(Mediavison source) which contains the decoded image buffer. All Mediavision API needs the Mediavision source handle as an input, and that is mandatory. An example is shown in the following code snippet:

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
   snprintf(filePath, 1024, "/path/to/face_image.jpg");
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

3. Now, we are ready for using the face recognition main features. There are three face recognition features - register, unregister and recognize. You can use any one of them.
 
   1.  Register a new face, which is a process that the face recognition framework tains and generates an internal model file with the given face data and its label. You could repeat this step to train the internal model file with more faces. For best accuracy, we recommend training at least three images per face. This is shown in the code snippet below:

        ```
        // Train the internal model with a given image - mv_source - and a label string - "name_a".
        ret = mv_face_recognition_register(handle, mv_source, "name_a");
        if (ret != MEDIA_VISION_ERROR_NONE) {
            // handle an error.
        }

        ret = mv_destroy_source(mv_source);
        if (ret != MEDIA_VISION_ERROR_NONE) {
           // handle an error.
        }
        ```

   2.  Unregister the face corresponding to a given label string, which is a process that face recognition framework drops all data related to the given label string. In fact, this process is to retrain the internal model without the dropped data. This is shown in the code snippet below:
        ```
        // Drop all data related to a given label string - "name_a".
        ret = mv_face_recognition_unregister(handle, "name_a");
        if (ret != MEDIA_VISION_ERROR_NONE) {
            // handle an error.
        }
        ```

   3.  Recognize the given face image, which is a process in which the face recognition framework performs a forward propagation to find the most suitable label.
        ```
        // Recognize the given face image.
        ret = mv_face_recognition_inference(handle, mv_source);
        if (ret != MEDIA_VISION_ERROR_NONE) {
            // handle an error.
        }
        ```

4. Get the label string as a result. This is a process in which the face recognition framework returns an inference result as a label string which was used when training. Please keep in mind that the function is valid only after mv_face_recognition_inference function call is completed. This is shown in the code snippet below:

   ```
   // Get a label string as a face recognition result.
   const char *out_label = NULL;
   ret = mv_face_recognition_get_label(handle, &out_label);
   if (ret != MEDIA_VISION_ERROR_NONE) {
       // handle an error.
   }
   ```

5. Destroy the face recognition handle. This is a process to release all resources used. Please keep in mind, the out_label variable at step 4 is valid only while the face recognition handle is alive.

    ```
    ret = mv_face_recognition_destroy(handle);
    if (ret != MEDIA_VISION_ERROR_NONE) {
        // handle an error.
    }
    ```

## Related information
- Dependencies
  - Tizen 7.0 and Higher for Mobile
  - Tizen 7.0 and Higher for TV
- API Reference
  - [Face Recognition API](../../api/common/latest/group__CAPI__MEDIA__VISION__FACE__RECOGNITION__MODULE.html)