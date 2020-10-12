# Gesture


According to the dictionary definition, `Gesture` means a movement or position of the hand, body, head, and face, and it expresses emotion, opinion, and so on.

As there are many gesture types, so there are various methods to recognize gestures on the device.
For example, hand gestures are recognized, based on gyro sensor data. And, head movements can be detected with a visual camera and video frames.
According to the targeted gesture, the device and the input sensor, the recognition method can be changed.

In the current Gesture, only wearable device is targeted and only hand gesture is recognized from input sensor data.

The main features of the Gesture API include:

- Getting the supported gesture type

  You can [get the supported gesture type](#info_gesture) to be recognized.

- Setting gesture options

  You can [set options](#set_option) such as a hand gesture type and option.

- Preparing the Gesture service for use

  You can [connect the background Gesture daemon](#prepare) to be able to operate the gesture.


<a name="basic_gesture"></a>
## Basic Gesture Processes

Using Gesture, you can:

- [Create a handle](#create_destroy) and register a error callback function.
  - Create a Gesture handle which is used for distinguishing your application from other applications also using the Gesture.
  - To get notifications about errors[register callback functions](#set).
- [Check the supported gesture type](#info_gesture).
  - Check the gesture type which can be recognized by the gesture service.
- [Set an option](#set_option) for gesture recognition.
  - Set an option to select always-on mode or not.
- [Start the gesture recognition](#start_stop) and [register a callback function](#callback) for recognition results.
  - Start recognizing the gesture.
  - To get the recognition result.
- Stop the gesture recognition.
  - Stop recognizing the gesture.
- Destroy the handle.


## Prerequisites

To enable your application to use the Gesture functionality in [wearable](../../api/wearable/latest/group__CAPI__UIX__GESTURE__MODULE.html) applications, include the `<gesture.h>` header file in your application:

    ```c
    #include <gesture.h>
    ```


<a name="create_destroy"></a>
## Creating and Destroying a Handle

When your application creates a handle by the Gesture API, the Gesture daemon is invoked and connected for background work.
This daemon and your application communicate as the server and the client.

1. To use the Gesture library, create a Gesture handle.

   The Gesture handle is used in other Gesture functions as a parameter:

    ```c
    void
    create_gesture_handle()
    {
        hand_gesture_h gesture_h;
        int ret;
        ret = hand_gesture_create(&gesture_h);
        if (HAND_GESTURE_ERROR_NONE != ret)
            /* Error handling */
    }
    ```

2. When you no longer need the Gesture library, destroy the Gesture handle using the `hand_gesture_destroy()` function:

    ```c
    void
    destroy_gesture_handle(hand_gesture_h gesture_h)
    {
        int ret;
        ret = hand_gesture_destroy(gesture_h); /* gesture_h is the Gesture handle */
        if (HAND_GESTURE_ERROR_NONE != ret)
            /* Error handling */
    }
    ```


<a name="info_gesture"></a>
## Getting Gesture Information

You can get the following information about the Gesture:

1. Get the supported gesture types by checking whether the gesture type you want is supported or not.

   According to the Gesture engine service, the supported gesture types are different.
   The current Gesture engine service supports only one gesture type, `HAND_GESTURE_WRIST_UP`.
   If the Gesture engine service is changed to support more gesture types, you can check more supported gesture types using `hand_gesture_is_supported_type()`.
   The candidates of the gesture types are defined in the `gesture_common.h` header file as the enumerations of `hand_gesture_type_e`.

    ```c
    void
    is_supported_gesture_type(hand_gesture_h gesture_h, hand_gesture_type_e gesture_type, bool* is_supported)
    {
        int ret;
        ret = hand_gesture_is_supported_type(gesture_h, gesture_type, is_supported);
        if (HAND_GESTURE_ERROR_NONE != ret)
            /* Error handling */
    }
    ```

2. Get the information of the Gesture engine service used in current.

   You can get the application ID and name of the current Gesture engine service using `hand_gesture_get_engine_info()` function.

    ```c
    void
    get_info(hand_gesture_h gesture_h)
    {
        int ret;
        char* engine_app_id;
        char* engine_name;

        ret = hand_gesture_get_engine_info(gesture_h, &engine_app_id, &engine_name);
        if (HAND_GESTURE_ERROR_NONE != ret)
            /* Error handling */
    }
    ```

<a name="set_option"></a>
## Setting an Option

You can select an option to detect hand gestures continuously or not. If you would like to make the application detect hand gestures continuously, set the option as `HAND_GESTURE_OPTION_ALWAYS_ON` using `hand_gesture_set_option()` function.

    ```c
    void
    set_option(hand_gesture_h gesture_h)
    {
        int ret;
        ret = hand_gesture_set_option(gesture_h, HAND_GESTURE_OPTION_ALWAYS_ON);
        if (HAND_GESTURE_ERROR_NONE != ret)
            /* Error handling */
    }
    ```


<a name="callback"></a>
## Setting and Unsetting Callbacks

The Gesture provides two types of callbacks for getting error and gesture recognition result.
The enum values, as well as the parameter details, for the callback parameters are defined in the `gesture.h` and `gesture_common.h` header files.

1. Error

   When an error occurs, the Gesture library sends a message using a callback:

   > **Note**
   >
   > Please set the error callback function before calling `hand_gesture_start_recognition()`.

    ```c
    /* Callback */
    void
    error_cb(hand_gesture_h gesture_h, hand_gesture_error_e reason, const char* msg, void* user_data)
    {
        /* Your code */
    }

    /* Set */
    void
    set_error_cb(hand_gesture_h gesture_h)
    {
        int ret;
        ret = hand_gesture_set_error_cb(gesture_h, error_cb, NULL);
        if (HAND_GESTURE_ERROR_NONE != ret)
            /* Error handling */
    }

    /* Unset */
    void
    unset_error_cb(hand_gesture_h gesture_h)
    {
        int ret;
        ret = hand_gesture_unset_error_cb(gesture_h);
        if (HAND_GESTURE_ERROR_NONE != ret)
            /* Error handling */
    }
    ```

2. Recognition result

   When the hand gesture is recognized, the recognized result is delivered through the `hand_gesture_recognition_cb()`.

   You can [set the recognition result callback function using `hand_gesture_start_recognition()`](#start_stop).


<a name="start_stop"></a>
## Start and Stop recognizing the gesture

1. To start recognizing the gesture, use the `hand_gesture_start_recognition()` function.

   When you start the gesture recognition, you should input the gesture type targeted to be recognized. Before calling `hand_gesture_start_recognition()`, please check whether the target gesture type is supported or not with `hand_gesture_is_supported_type()`.

   After calling `hand_gesture_start_recognition()`, the recognition results will be coming through the callback function `hand_gesture_recognition_cb()`.
   When the callback function is invoked, you can handle the recognition results by corresponding to some operations.
   For example, when `HAND_GESTURE_WRIST_UP` is occurred, you can turn on the screen of the wearable device.

    ```c
    void
    recognition_cb(hand_gesture_h gesture_h, hand_gesture_type_e gesture, double timestamp, hand_gesture_error_e error, void* user_data)
    {
        /* Your code */
    }

    void
    start_recognition(hand_gesture_h gesture_h)
    {
        int ret;
        bool is_supported = false;
        ret = hand_gesture_is_supported_type(gesture_h, HAND_GESTURE_WRIST_UP, &is_supported);
        if (HAND_GESTURE_ERROR_NONE == ret && true == is_supported)
        {
            ret = hand_gesture_start_recognition(gesture_h, HAND_GESTURE_WRIST_UP, recognition_cb, NULL);
            if (HAND_GESTURE_ERROR_NONE != ret)
                /* Error handling */
        }
    }
    ```

2. To stop recognizing the gesture, use the `hand_gesture_stop_recognition()` function.

    ```c
    void
    stop_recognition(hand_gesture_h gesture_h)
    {
        int ret;
        ret = hand_gesture_stop_recognition(gesture_h);
        if (HAND_GESTURE_ERROR_NONE != ret)
            /* Error handling */
    }
    ```


## Related Information
* Dependencies
  - Tizen 6.0 and Higher for Wearable
