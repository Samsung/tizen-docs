# Deep learning based Face Recognition

You can perceive and understand a face in your application.
This document guides how to register a new face, to unregister someone who is registered
with a given label and to recognize a given face.

## Prerequisites

To enable your application for using the deep learning based face recognition functionality:

1. To use the functions and data types of the deep learning based face recognition API, include the `<mv_face_recognition.h>` header file in your application.

   In addition, you may need to include the `<image_util.h>` header file to handle the image decoding task, or the `<camera.h>` header file to provide preview images.
   Of course, you could use other libraries you want.

   ```
   #include <mv_face_recognition.h>

   /* To decode the image file. */
   #include <image_util.h>
   /* To get preview image from Camera device. */
   #include <camera.h>
   ```

To register a new face image with a given label:

1. Create a face recognition handle and prepare for the face recognition framework.

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

2. Prepare an input source to register. The input source should be RGB data. In this guide,
   we will use a image file as a input source, and we will show you how to decode the given image file
   and then prepare for a mv_source(Mediavison source) which contains the decoded image buffer.
   All Mediavision API needs the Mediavision source handle as a input, and that is mandatorily required.

   ```
   char filePath[1024];
   unsigned char *dataBuffer = NULL;
   unsigned long long bufferSize = 0;
   unsigned long width = 0;
   unsigned long height = 0;
   image_util_decode_h imageDecoder = NULL;
   mv_source_h mv_source = NULL;

   ret = mv_create_source(&mv_source);
   if (ret != MEDIA_VISION_ERROR_NONE) {
       // handle an error.
   }

   ret = image_util_decode_create(&imageDecoder);
   if (ret != IMAGE_UTIL_ERROR_NONE) {
       // handle an error.
   }

   ret = image_util_decode_set_colorspace(imageDecoder, IMAGE_UTIL_COLORSPACE_RGB888);
   if (ret != IMAGE_UTIL_ERROR_NONE) {
       // handle an error.
   }

   /* Decode image and fill the image data to mv_source handle */
   snprintf(filePath, 1024, "/path/to/face_image.jpg");
   ret = image_util_decode_set_input_path(imageDecoder, filePath);
   if (ret != IMAGE_UTIL_ERROR_NONE) {
       // handle an error.
   }

   ret = image_util_decode_set_output_buffer(imageDecoder, &dataBuffer);
   if (ret != IMAGE_UTIL_ERROR_NONE) {
       // handle an error.
   }

   ret = image_util_decode_run(imageDecoder, &width, &height, &bufferSize);
   if (ret != IMAGE_UTIL_ERROR_NONE) {
       // handle an error.
   }

   ret = mv_source_fill_by_buffer(mv_source, dataBuffer, (unsigned int)bufferSize,
                                 (unsigned int)width, (unsigned int)height, MEDIA_VISION_COLORSPACE_RGB888);
   if (ret != MEDIA_VISION_ERROR_NONE) {
      free(dataBuffer);
	  // handle an error.
   }

   ret = image_util_decode_destroy(imageDecoder);
   if (ret != IMAGE_UTIL_ERROR_NONE) {
       // handle an error.
   }

   free(dataBuffer);
   ```

3. Now, we are ready for using the face recognition main features. There are three face recognition features - register, unregister and recognize.
   You can use one of them.
 
   3.1 Register a new face, which is a process that the face recognition framework tains and generates
       a internal model file with the given face data and its label. You could repeat this step to train
	   the internal model file with more faces. For the accuracy, we recommend to train at least three images per a face.

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

   3.2 Unregister the face corresponding to a given label string, which is a process that face
       recognition framework drops all data related to the given label string. In fact, this process is to retrain the internal model
       without the dropped data.

   ```
   // Drop all data related to a given label string - "name_a".
   ret = mv_face_recognition_unregister(handle, "name_a");
   if (ret != MEDIA_VISION_ERROR_NONE) {
       // handle an error.
   }
   ```

   3.3 Recognize the given face image, which is a process that face recognition framework performs a forward propergation to find the most suitable label.

   ```
   // Recognize the given face image.
   ret = mv_face_recognition_inference(handle, mv_source);
   if (ret != MEDIA_VISION_ERROR_NONE) {
       // handle an error.
   }
   ```

4. Get the label string as a result. This is a process that face recognition framework returns a inference result as a label string
   which was used when training. Please keep in mind. This function is valid only after mv_face_recognition_inference function call is completed.

   ```
   // Get a label string as a face recognition result.
   const char *out_label = NULL;
   ret = mv_face_recognition_get_label(handle, &out_label);
   if (ret != MEDIA_VISION_ERROR_NONE) {
       // handle an error.
   }
   ```

5. Destroy the face recognition handle. This is a process to release all resources used. Please keep in mind, the out_label variable at step 4 is valid
   only while the face recognition handle is alive.

```
   ret = mv_face_recognition_destroy(handle);
   if (ret != MEDIA_VISION_ERROR_NONE) {
       // handle an error.
   }
```

## Related Information
- Dependencies
  - Tizen 7.0 and Higher for Mobile
  - Tizen 7.0 and Higher for TV