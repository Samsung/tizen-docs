# Multimedia

This document provides a brief introduction to the Tizen HAL (Hardware Abstraction Layer) APIs for various multimedia components. These APIs serve as an interface between the higher-level software frameworks and the underlying hardware drivers, facilitating hardware interaction in an abstracted manner.

**Figure: Multimedia HAL hierarchy**

<img src="media/tizen-hal-multimedia.png" width=800/>

## Audio

**Purpose:**
The `hal-audio.h` file defines the Hardware Abstraction Layer (HAL) API for audio functionalities on the Tizen platform. It provides a standardized interface for controlling audio hardware, including operations like initialization, deinitialization, volume control, stream management, and PCM (Pulse Code Modulation) device handling.

**Key Functionalities:**
*   **Initialization & Deinitialization:** `hal_audio_init()` and `hal_audio_deinit()` manage the lifecycle of the audio HAL.
*   **Volume Control:** Functions like `hal_audio_get_volume_level_max()`, `hal_audio_get_volume_level()`, `hal_audio_set_volume_level()`, `hal_audio_get_volume_value()`, `hal_audio_get_volume_mute()`, and `hal_audio_set_volume_mute()` allow for fine-grained control over audio volume and mute states for different streams and devices.
*   **Audio Routing:** `hal_audio_update_route()` and `hal_audio_update_route_option()` are used to manage audio paths, directing audio streams to appropriate output devices.
*   **Stream Management:** `hal_audio_notify_stream_connection_changed()` notifies the HAL about stream connection events, which can be used for routing and volume adjustments.
*   **PCM Device Operations:** A comprehensive set of functions (`hal_audio_pcm_open()`, `hal_audio_pcm_start()`, `hal_audio_pcm_stop()`, `hal_audio_pcm_close()`, `hal_audio_pcm_avail()`, `hal_audio_pcm_write()`, `hal_audio_pcm_read()`, etc.) for low-level control over PCM devices, including opening, starting, stopping, reading, writing, and managing parameters like sample rate, format, and buffer sizes. It also supports memory-mapped I/O (mmap) operations.
*   **Ducking:** `hal_audio_notify_ducking_activation_changed()` handles ducking scenarios (e.g., lowering volume of background audio during a notification).
*   **Message Callbacks:** `hal_audio_add_message_cb()` and `hal_audio_remove_message_cb()` allow the registration of callback functions to receive asynchronous messages from the audio HAL.

This API is essential for any application or system service that needs to interact directly with audio hardware on Tizen devices.

---

## Camera

**Purpose:**
The `hal-camera.h` and `hal-camera-interface.h` files define the HAL API for camera functionalities on the Tizen platform. They provide an interface for applications to control camera hardware, including device management, preview, capture, recording, and various camera settings.

**Key Functionalities:**
*   **Capabilities:** `hal_camera_get_device_capability_list()` retrieves the capabilities of the camera device.
*   **HAL Initialization:** `hal_camera_init()` and `hal_camera_deinit()` initialize and deinitialize the camera HAL. `hal_camera_open_device()` and `hal_camera_close_device()` manage the connection to a specific camera device.
*   **Message Callbacks:** `hal_camera_add_message_callback()` and `hal_camera_remove_message_callback()` enable asynchronous communication from the camera HAL.
*   **Preview Control:** Functions like `hal_camera_set_preview_stream_format()`, `hal_camera_get_preview_stream_format()`, `hal_camera_start_preview()`, `hal_camera_release_preview_buffer()`, and `hal_camera_stop_preview()` handle the setup, start, and stop of the camera preview stream, including buffer management.
*   **Auto Focus:** `hal_camera_start_auto_focus()` and `hal_camera_stop_auto_focus()` control the camera's auto-focus mechanism.
*   **Image Capture:** `hal_camera_start_capture()` and `hal_camera_stop_capture` manage the process of capturing still images.
*   **Video Recording:** `hal_camera_set_video_stream_format()`, `hal_camera_get_video_stream_format()`, `hal_camera_start_record()`, `hal_camera_release_video_buffer()`, and `hal_camera_stop_record()` handle video stream configuration and recording.
*   **Camera Commands:** `hal_camera_set_command()`, `hal_camera_get_command()`, and `hal_camera_set_batch_command()` allow setting and getting various camera parameters (e.g., exposure, white balance).

This API is fundamental for camera applications, providing the necessary tools to leverage the full capabilities of the device's camera hardware.

---

## Codec

**Purpose:**
The `hal-codec.h` and `hal-codec-interface.h` files define the HAL API for multimedia codec functionalities on the Tizen platform. They provide an interface for encoding and decoding audio/video data, abstracting the underlying hardware or software codec implementations.

**Key Functionalities:**
*   **Capabilities:** `hal_codec_get_capability()` retrieves information about the supported features and formats of the codec.
*   **HAL Initialization:** `hal_codec_init()` and `hal_codec_deinit()` manage the codec HAL lifecycle.
*   **Configuration:** `hal_codec_configure()` sets up the codec with specific parameters like width, height, input/output formats, and security mode.
*   **Message Callbacks:** The `hal_codec_start()` function accepts a callback (`hal_codec_message_cb`) for receiving asynchronous messages from the codec, such as buffer availability or error notifications.
*   **Processing Control:** `hal_codec_start()` and `hal_codec_stop()` initiate and terminate the encoding or decoding process. `hal_codec_flush()` clears the internal buffers of the codec.
*   **Encoding & Decoding:** `hal_codec_start()` and `hal_codec_stop()` start and stop the encoding or decoding operation.  `hal_codec_decode()` and `hal_codec_encode()` are the core functions for processing input data through the codec.
*   **Buffer Management:** `hal_codec_release_output_buffer()` is used to return output buffers to the codec after they have been processed by the application.
*   **Codec Commands:** `hal_codec_set_command()`, `hal_codec_get_command()`, and `hal_codec_set_batch_command()` provide a way to control various codec-specific parameters.

This API is crucial for multimedia playback, streaming, and recording applications, enabling them to perform efficient media encoding and decoding.

---

## DRM

**Purpose:**
The `hal-drm.h` file defines the HAL API for DRM(Digital Rights Management) on the Tizen platform. It provides an interface for handling protected content, including license acquisition, and decryption of media streams, interacting with a CDM(Content Decryption Module).

**Key Functionalities:**
*   **HAL Initialization & State Management:** `hal_drm_init()` and `hal_drm_deinit()` initialize and deinitialize the DRM HAL. `hal_drm_get_state()` retrieves the current state of the DRM system.
*   **Message Callbacks:** `hal_drm_set_message_callback()` allows setting a callback to receive asynchronous messages from the DRM backend.
*   **CDM Information:** `hal_drm_get_cdm_version()` retrieves the version of the underlying Content Decryption Module.
*   **Session based license management:** `hal_drm_session_create()`, `hal_drm_session_load()`, `hal_drm_session_close()`, `hal_drm_session_remove()` manages session's life cycle. `hal_drm_session_generate_request()`, `hal_drm_session_update()`, `hal_drm_session_get_expiration()`, `hal_drm_session_get_key_infos()` handle license acquisition and retrieve key information.
*   **Provisioning & Service Certificates:** `hal_drm_get_provisioning_request()`, `hal_drm_set_provisioning_response()`, `hal_drm_get_service_certificate_request()`, `hal_drm_load_service_certificate_response()` and `hal_drm_set_service_certificate()` handle device provisioning and service certificates.
*   **Decryption:** `hal_drm_allocate_output_buffer()` and `hal_drm_release_output_buffer()` manage output buffers for decrypted content. `hal_drm_decrypt()` decrypt data using the session's keys and provided cryptographic information.
*   **DRM Commands:** `hal_drm_set_command()`, `hal_drm_get_command()` and `hal_drm_set_batch_command()` allow for setting and getting various DRM parameters.

These APIs are essential for applications that need to play DRM content, ensuring secure handling of licenses.

---

## HDCP

**Purpose:**
The `hal-hdcp.h` file defines the HAL API for HDCP(High-bandwidth Digital Content Protection) on the Tizen platform. HDCP is a form of digital copy protection used to prevent copying of digital audio and video content as it travels across connections. This API provides an interface for managing HDCP sessions, including encryption, and decryption for protected content transmission.

**Key Functionalities:**
*   **HAL Initialization & State Management:** `hal_hdcp_init()` and `hal_hdcp_deinit()` initialize and deinitialize the HDCP HAL. `hal_hdcp_get_state()` retrieves the current state of the HDCP system.
*   **HDCP Session Management:** `hal_hdcp_open()` and `hal_hdcp_close()` open and close an HDCP session, specifying the device type (e.g., receiver, transmitter) and protocol version.
*   **Receiver Operations:** `hal_hdcp_start_receiver()` and `hal_hdcp_stop_receiver()` starts and stops the HDCP receiver functionality.
*   **Transmitter Operations:** `hal_hdcp_start_transmitter()` and `hal_hdcp_stop_transmitter()` start and stop the HDCP transmitter functionality.
*   **Encryption & Decryption:** `hal_hdcp_allocate_output_buffer()` and `hal_hdcp_release_output_buffer()` manage output buffers for encrypted/decrypted data. `hal_hdcp_decrypt()` and `hal_hdcp_encrypt()` decrypt and encrypt data using the keys and provided cryptographic information.
*   **HDCP Commands:** `hal_hdcp_set_command()`, `hal_hdcp_get_command()` and `hal_hdcp_set_batch_command()` provide a mechanism to control various HDCP settings and parameters.

These APIs are essential for applications that need to prevent copying of digital audio and video content as it travels across connections.

---

## Radio

**Purpose:**
The `hal-radio.h` file defines the HAL API for FM radio functionalities on the Tizen platform. It provides an interface for controlling the FM radio hardware, allowing applications to tune into frequencies, control playback, and retrieve signal information.

**Key Functionalities:**
*   **HAL Initialization & Backend Management:** `hal_radio_get_backend()` and `hal_radio_put_backend()` manage the underlying radio backend implementation. `hal_radio_init()` and `hal_radio_deinit()` initialize and deinitialize the radio HAL using the acquired backend.
*   **Device Preparation:** `hal_radio_prepare()` and `hal_radio_unprepare()` prepare and unprepare the radio hardware for operation.
*   **Device Control:** `hal_radio_open()` and `hal_radio_close()` open and close the connection to the radio device. `hal_radio_start()` and `hal_radio_stop()` start and stop the radio playback.
*   **Tuning & Seeking:**
    *   `hal_radio_set_frequency()` and `hal_radio_get_frequency()`: Set and get the current radio frequency (in kHz).
    *   `hal_radio_seek()`: Seeks the next available radio frequency up or down from the current frequency.
*   **Signal Information:** `hal_radio_get_signal_strength()` retrieves the current signal strength of the tuned frequency (in dBm).

This API provides the necessary functions for developing FM radio applications on Tizen, enabling users to listen to FM radio broadcasts on their devices.
