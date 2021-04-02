# Tizen Native APIs

You can develop native applications using the native API modules. You can create diverse applications with a variety of features, and design versatile applications and intriguing user interfaces with text and graphics while taking advantage of many device functionalities, such as sensors and call operations. In addition, you can, for example, manage content and media files, use network and social services, and provide messaging and embedded Web browsing functionality.

The Tizen platform also provides a special kind of native application model, which consists of one UI native application and one or more native service applications.

The native API specification consists of multiple API modules that represent the versatility and wide variety of features that you can implement in your native application. Each API module represents a set of logically similar submodule APIs which can be grouped into the same category. This structure was designed to make it easier for you to narrow down and find the specific methods that you require to implement a feature in your native application.

There are two types of submodules - Tizen native modules and open source modules. The integration of open source modules in the native API structure allows you to add additional features by using well-known open source libraries. This is particularly advantageous for developers who are familiar with certain libraries because they can quickly add features and use previously written code in certain cases.

## Native API Modules

The following list defines Tizen Native API. The list describes the API modules and the functionality of all their submodule APIs within that module. The list also acts as a reference source for when you are planning a new feature for your application and need a way to efficiently compare different API modules to decide which APIs to use.

> **Note**
>
> Except as noted, the native APIs for mobile are available since Tizen 2.3 and the native APIs for wearable are available since Tizen 2.3.1.

- **Account**

  The Account API module features include managing various account information, such as receiving sync operation notifications and obtaining an access token by using the OAuth 2.0 authorization.

  | API submodule | Functionality                                    | API reference | Guide   |
  | ------------- | ------------------------------------------------ | ------------- | ------- |
  | AccountManager | Provides CRUD (Create, Read, Update, Delete) account management functionality. | [mobile](../api/mobile/latest/group__CAPI__ACCOUNT__MANAGER__MODULE.html), [wearable](../api/wearable/latest/group__CAPI__ACCOUNT__MANAGER__MODULE.html) | [Account Management](personal/account.md)    |
  | FIDO Client    | Allows you to utilize the device's available authenticators for online service integration. | [mobile](../api/mobile/latest/group__CAPI__FIDO__MODULE.html) (since 3.0), [wearable](../api/wearable/latest/group__CAPI__FIDO__MODULE.html) (since 3.0) | [FIDO Universal Authentication Framework](personal/fido.md) |
  | OAuth 2.0      | Provides an easy way to gain an access token between a server and client. | [mobile](../api/mobile/latest/group__CAPI__OAUTH2__MODULE.html) (since 2.4), [wearable](../api/wearable/latest/group__CAPI__OAUTH2__MODULE.html) (since 2.4) | [OAuth 2.0](personal/oauth.md)               |
  | Sync Manager   | Helps applications in scheduling their data sync operations. | [mobile](../api/mobile/latest/group__CAPI__SYNC__MANAGER__MODULE.html) (since 2.4), [wearable](../api/wearable/latest/group__CAPI__SYNC__MANAGER__MODULE.html) (since 2.4) | [Synchronization Management](personal/data-sync.md) |
  | libOAuth       | Provides a library for using an open standard for secure authorization. This library enables users to securely log into an account on an application by using their logon credentials from another secondary account that they can have with another account provider or application. | [mobile](../api/mobile/latest/group__OPENSRC__LIB__OAUTH__FRAMEK.html), [wearable](../api/wearable/latest/group__OPENSRC__LIB__OAUTH__FRAMEK.html) |        |

- **Application Framework**

  The Application Framework API contains submodule APIs for application development. The submodule APIs enable application life-cycle management, usage of functionality that is exported by other applications, and access to a user's application preferences.

  | API submodule | Functionality                                    | API reference | Guide   |
  | ------------- | ------------------------------------------------ | ------------- | ------- |
  | Application         | Manages the application's main event loop, state change events, and basic system events, and gets information about the application. It is also used to launch other applications. | [mobile](../api/mobile/latest/group__CAPI__APPLICATION__MODULE.html), [wearable](../api/wearable/latest/group__CAPI__APPLICATION__MODULE.html) | [Applications](applications/overview.md)     |
  | Application Manager | Gets information, such as the application ID and path to the shared data directory, of the current application and other installed or running applications. | [mobile](../api/mobile/latest/group__CAPI__APPLICATION__MANAGER__MODULE.html), [wearable](../api/wearable/latest/group__CAPI__APPLICATION__MANAGER__MODULE.html) | [Application Manager](app-management/app-manager.md) |
  | Attach Panel        | Provides a panel in which users can take pictures, record voice, and select files to attach. | [mobile](../api/mobile/latest/group__CAPI__PANEL__ATTACH__MODULE.html) (since 2.4) | [Attach Panel](notification/attach-panel.md) |
  | Badge               | Creates and removes badges on the application's home screen icon. A badge is an image displayed on the application icon, which informs the user about notifications and events. This submodule can also be used to set and get the badge value and visibility. | [mobile](../api/mobile/latest/group__BADGE__MODULE.html), [wearable](../api/wearable/latest/group__BADGE__MODULE.html) | [Application Icons](app-management/app-icons.md)     |
  | Bundle              | Provides a string-based dictionary abstract data type (ADT). A dictionary is an ordered or unordered list of key-element pairs. Keys are used to locate elements in the list. This submodule can be used to create and manage a dictionary. | [mobile](../api/mobile/latest/group__CORE__LIB__BUNDLE__MODULE.html), [wearable](../api/wearable/latest/group__CORE__LIB__BUNDLE__MODULE.html) | [Data Bundle](app-management/data-bundles.md) |
  | Data Control        | Exchanges data between applications by allowing an application to query the public database of another application that has opted to be a data provider. | [mobile](../api/mobile/latest/group__CAPI__DATA__CONTROL__MODULE.html) [wearable](../api/wearable/latest/group__CAPI__DATA__CONTROL__MODULE.html) | [Data Control](app-management/data-control.md)       |
  | Message Port        | Sends and receives small messages between applications without interference from other applications and processes. Each message is a bundle. | [mobile](../api/mobile/latest/group__CAPI__MESSAGE__PORT__MODULE.html), [wearable](../api/wearable/latest/group__CAPI__MESSAGE__PORT__MODULE.html) | [Message Port](app-management/message-port.md)       |
  | Notification        | Creates, inserts, and updates notifications so that applications can relay information to users. Visuals, sounds, or vibrations can be used as notifications. | [mobile](../api/mobile/latest/group__NOTIFICATION__MODULE.html), [wearable](../api/wearable/latest/group__NOTIFICATION__MODULE.html) | [Notifications](notification/notifications.md)       |
  | Package Manager     | Stores and receives information related to packages installed on the device. This is information can be, for example, the package name, path to the icon image, or the application version. It can also be used to check whether two package certificates match. If they match, they have been created by the same developer and can share resources securely. | [mobile](../api/mobile/latest/group__CAPI__PACKAGE__MANAGER__MODULE.html), [wearable](../api/wearable/latest/group__CAPI__PACKAGE__MANAGER__MODULE.html) | [Package Manager](app-management/package-manager.md) |
  | RPC Port            | Provides functions to send and receive messages between applications. | [mobile](../api/mobile/latest/group__CAPI__RPC__PORT__MODULE.html), [wearable](../api/wearable/latest/group__CAPI__RPC__PORT__MODULE.html) | [RPC Port](app-management/rpc-port.md) |
  | Service Application | Handles Tizen service application (non-UI application) state changes and system events. It is also used to start and exit the main event loop of service applications. | [mobile](../api/mobile/latest/group__CAPI__SERVICE__APP__MODULE.html), [wearable](../api/wearable/latest/group__CAPI__SERVICE__APP__MODULE.html) | [Service Application](applications/service-app.md)   |
  | Shortcut            | Adds application shortcuts to the device home screen, the main landing screen of the device. | [mobile](../api/mobile/latest/group__SHORTCUT__MODULE.html) | [Application Icons](app-management/app-icons.md)     |
  | Watch Application   | Handles Tizen watch application state changes and system events. It is also used to start and exit the main event loop of watch applications. | [wearable](../api/wearable/latest/group__CAPI__WATCH__APP__MODULE.html) | [EFL Watch Application](applications/watch-app.md) |
  | Watchface complication  | Provides feature to receive and request watchface complication data. It also provides editable management feature to request edit for complication and design elements to editor. | [wearable](../api/wearable/latest/group__WATCHFACE__COMPLICATION__MODULE.html) | [Watch Face Complications](complications/overview.md) |
  | Widget              | Handles Tizen widget application state changes and system events. It is also used to start and exit the main event loop of widget applications. | [mobile](../api/mobile/latest/group__CAPI__WIDGET__FRAMEWORK.html) (since 2.3.1), [wearable](../api/wearable/latest/group__CAPI__WIDGET__FRAMEWORK.html) | [EFL Widget Application](applications/widget-app.md) |

- **Base**

  The Base API contains submodule APIs for internationalization support and contains various open source libraries.

  | API submodule | Functionality                                    | API reference |
  | ------------- | ------------------------------------------------ | ------------- |
  | C++ Standard Library | Provides a standard C++ library.          | [mobile](../api/mobile/latest/group__OPENSRC__STL__GCC__FRAMEWORK.html), [wearable](../api/wearable/latest/group__OPENSRC__STL__GCC__FRAMEWORK.html) |
  | Common Error         | Provides error codes that are common for the whole Tizen API. | [mobile](../api/mobile/latest/group__CAPI__COMMON__ERROR.html), [wearable](../api/wearable/latest/group__CAPI__COMMON__ERROR.html) |
  | Glib                 | Provides low-level libraries and advanced data structures, such as linked lists and hash tables, for use in application development. | [mobile](../api/mobile/latest/group__OPENSRC__GLIB__FRAMEWORK.html), [wearable](../api/wearable/latest/group__OPENSRC__GLIB__FRAMEWORK.html) |
  | Glibc                | Provides a standard C library.       | [mobile](../api/mobile/latest/group__OPENSRC__GLIBC__FRAMEWORK.html), [wearable](../api/wearable/latest/group__OPENSRC__GLIBC__FRAMEWORK.html) |
  | LibXML               | Used to parse XML documents, such as the [Application Manifest](../index.md#appmanifest). | [mobile](../api/mobile/latest/group__OPENSRC__LIBXML__FRAMEWORK.html), [wearable](../api/wearable/latest/group__OPENSRC__LIBXML__FRAMEWORK.html) |
  | Minizip              | Provides a library to process files in the ZIP format. It can be used to zip, unzip and compress files. | [mobile](../api/mobile/latest/group__OPENSRC__MINIZIP__FRAMEWORK.html), [wearable](../api/wearable/latest/group__OPENSRC__MINIZIP__FRAMEWORK.html) |
  | OpenMP               | Supports shared memory multiprocessing. This can be used for complex tasks on multicore processors. | [mobile](../api/mobile/latest/group__OPENSRC__OPENMP__FRAMEWORK.html), [wearable](../api/wearable/latest/group__OPENSRC__OPENMP__FRAMEWORK.html) |
  | Sqlite               | Implements a lightweight SQL relational database. This is widely used for embedded client or local storage. | [mobile](../api/mobile/latest/group__OPENSRC__SQLITE__FRAMEWORK.html), [wearable](../api/wearable/latest/group__OPENSRC__SQLITE__FRAMEWORK.html) |
  | Utils > i18n         | Provides internationalization (i18n) support, such as flexibly generating date formats and numbers, depending on the locale setting of the device. | [mobile](../api/mobile/latest/group__CAPI__BASE__UTILS__I18N__MODULE.html), [wearable](../api/wearable/latest/group__CAPI__BASE__UTILS__I18N__MODULE.html) |
  | zlib                 | Used for in-memory compression and decompression.    | [mobile](../api/mobile/latest/group__OPENSRC__ZLIB__FRAMEWORK.html) (since 2.4), [wearable](../api/wearable/latest/group__OPENSRC__ZLIB__FRAMEWORK.html) (since 3.0) |

- **Content**

  The Content API module contains submodule APIs for managing the most common device media data types, such as image, audio, and video files. It provides operations to search for content, search for content information stored on the device, create playlists, download content from servers through an HTTP connection, and access the EXIF information in an image file.

  | API submodule | Functionality                                    | API reference | Guide   |
  | ------------- | ------------------------------------------------ | ------------- | ------- |
  | Download      | Creates and manages one or more download requests. Content is downloaded from servers through an HTTP connection. | [mobile](../api/mobile/latest/group__CAPI__WEB__DOWNLOAD__MODULE.html) | [Download](connectivity/download.md) |
  | MIME Type     | Maps MIME types to file extensions and vice versa. For example, the `.jpeg` file extension is mapped to the `image/jpeg MIME` type, which is required when using other API modules, such as the AppControl API in the Application submodule API, because it operates with MIME types. | [mobile](../api/mobile/latest/group__CAPI__CONTENT__MIME__TYPE__MODULE.html), [wearable](../api/wearable/latest/group__CAPI__CONTENT__MIME__TYPE__MODULE.html) | [Metadata](multimedia/metadata.md)   |
  | Media Content | Connects and disconnects from the media content service. This connection is required to insert, update and remove media file information in the media content database. Common media data types, such as image, audio, and video can be managed through the database. Other queries, such as searching for content and content information and accessing EXIF information from image files, are also possible. | [mobile](../api/mobile/latest/group__CAPI__MEDIA__CONTENT__MODULE.html), [wearable](../api/wearable/latest/group__CAPI__MEDIA__CONTENT__MODULE.html) | [Media Content](multimedia/media-content.md) |

- **Context**

  The Context API module contains submodule APIs to detect user information, such as when a user is running with a device, and device information, such as gestures when a device is tilted.

  | API submodule | Functionality                                    | API reference | Guide   |
  | ------------- | ------------------------------------------------ | ------------- | ------- |
  | Contextual History   | Allows you to query statistics and patterns derived from contextual history data. | [mobile](../api/mobile/latest/group__CAPI__CONTEXT__HISTORY__MODULE.html) (since 2.4), [wearable](../api/wearable/latest/group__CAPI__CONTEXT__HISTORY__MODULE.html) (since 4.0) | [Contextual Device Usage History Data](personal/context.md) |
  | Contextual Trigger   | Provides a way to define rules, each of which can trigger a specified action when the rule is satisfied. | [mobile](../api/mobile/latest/group__CAPI__CONTEXT__TRIGGER__MODULE.html) (since 2.4) | [Contextual System Event Trigger](alarm/trigger.md) |

- **Location**

  The Location API module allows the geographical position of a device to be determined for use with location-based services.

  | API submodule | Functionality                                    | API reference | Guide   |
  | ------------- | ------------------------------------------------ | ------------- | ------- |
  | GeofenceManager | Provides a service related to geofence (geo-fence). | [mobile](../api/mobile/latest/group__CAPI__GEOFENCE__MANAGER__MODULE.html) (since 2.4) | [Geofences](location-sensors/geofences.md) |
  | LocationManager | Acquires information about the geographical location of the device. It also allows the receiving of notifications about position changes, velocity changes, and when a given geographical area is left. | [mobile](../api/mobile/latest/group__CAPI__LOCATION__MANAGER__MODULE.html), [wearable](../api/wearable/latest/group__CAPI__LOCATION__MANAGER__MODULE.html) | [Location Information](location-sensors/location.md)  |
  | Maps Service    | Provides a set of functions, helping to create map-aware applications. | [mobile](../api/mobile/latest/group__CAPI__MAPS__SERVICE__MODULE.html) (since 2.4), [wearable](../api/wearable/latest/group__CAPI__MAPS__SERVICE__MODULE.html) (since 2.3.2) | [Maps and Maps Service](location-sensors/maps.md) |

- **Messaging**

  The Messaging API module contains submodule APIs which grant access to the messaging capabilities, such as SMS, MMS and email, of the device.

  | API submodule | Functionality                                    | API reference | Guide   |
  | ------------- | ------------------------------------------------ | ------------- | ------- |
  | Email | Allows composing, sending, and receiving of email messages.  | [mobile](../api/mobile/latest/group__CAPI__MESSAGING__EMAIL__MODULE.html), [wearable](../api/wearable/latest/group__CAPI__MESSAGING__EMAIL__MODULE.html) (since 3.0) | [Email](messaging/email.md) |
  | Messages | Allows composing, sending, and receiving of SMS, MMS, and WAP push messages. | [mobile](../api/mobile/latest/group__CAPI__MESSAGING__MESSAGES__MODULE.html), [wearable](../api/wearable/latest/group__CAPI__MESSAGING__MESSAGES__MODULE.html) | [Messages](messaging/messages.md) |
  | Push | Allows receiving of push notifications from a push server.| [mobile](../api/mobile/latest/group__CAPI__MESSAGING__PUSH__PUBLIC__MODULE.html), [wearable](../api/wearable/latest/group__CAPI__MESSAGING__PUSH__PUBLIC__MODULE.html) | [Push](messaging/push.md), [Push Server](messaging/push-server.md) |

- **Multimedia**

  The Multimedia API module contains submodule APIs for easily integrating an application with audio, image, and video files. It can also be used for image editing.

  | API submodule | Functionality                                    | API reference | Guide   |
  | ------------- | ------------------------------------------------ | ------------- | ------- |
  | Audio I/O          | Manages the system audio devices by granting access to the hardware layer of the sound card. This API must be used for tasks that require raw audio data buffers in PCM format. | [mobile](../api/mobile/latest/group__CAPI__MEDIA__AUDIO__IO__MODULE.html), [wearable](../api/wearable/latest/group__CAPI__MEDIA__AUDIO__IO__MODULE.html) | [Raw Audio Playback and Recording](multimedia/raw-audio.md)  |
  | Camera             | Accesses the camera preview to display photo previews, focuses images, and captures images. | [mobile](../api/mobile/latest/group__CAPI__MEDIA__CAMERA__MODULE.html), [wearable](../api/wearable/latest/group__CAPI__MEDIA__CAMERA__MODULE.html) | [Camera](multimedia/camera.md)       |
  | Image Util         | Encodes and decodes JPEG images. It also provides tools, such as crop, resize, and rotate, to transform images. | [mobile](../api/mobile/latest/group__CAPI__MEDIA__IMAGE__UTIL__MODULE.html), [wearable](../api/wearable/latest/group__CAPI__MEDIA__IMAGE__UTIL__MODULE.html) | [Image Editing](multimedia/image-edit.md), [Image Recognition](multimedia/image-recognition.md) |
  | Media Codec        | Provides interfaces for encoding and decoding audio and video data, such as AAC audio or MPEG-4 AVC video. | [mobile](../api/mobile/latest/group__CAPI__MEDIA__CODEC__MODULE.html), [wearable](../api/wearable/latest/group__CAPI__MEDIA__CODEC__MODULE.html) | [Media Conversions](multimedia/media-conversions.md) |
  | Media Controller   | Provides functions for communication between the media controller server and the media controller client. | [mobile](../api/mobile/latest/group__CAPI__MEDIA__CONTROLLER__MODULE.html) (since 2.4), [wearable](../api/wearable/latest/group__CAPI__MEDIA__CONTROLLER__MODULE.html) (since 3.0) | [Media Controller](multimedia/media-controller.md)   |
  | Media Demuxer      | Provides functions for demuxing media data.  | [mobile](../api/mobile/latest/group__CAPI__MEDIADEMUXER__MODULE.html) (since 3.0), [wearable](../api/wearable/latest/group__CAPI__MEDIADEMUXER__MODULE.html) (since 3.0) | [Media Muxing](multimedia/media-muxing.md)   |
  | Media Muxer        | Provides functions for muxing media data.    | [mobile](../api/mobile/latest/group__CAPI__MEDIAMUXER__MODULE.html) (since 3.0), [wearable](../api/wearable/latest/group__CAPI__MEDIAMUXER__MODULE.html) (since 3.0) | [Media Muxing](multimedia/media-muxing.md)   |
  | Media Streamer     | Provides functions for building custom pipeline for streaming media. | [mobile](../api/mobile/latest/group__CAPI__MEDIA__STREAMER__MODULE.html) (since 3.0), [wearable](../api/wearable/latest/group__CAPI__MEDIA__STREAMER__MODULE.html) (since 3.0) | [Media Stream Playback](multimedia/media-streams.md) |
  | Media Tool         | Handles audio and video packet buffers. These buffers are utilized by the other Multimedia submodule APIs. | [mobile](../api/mobile/latest/group__CAPI__MEDIA__TOOL__MODULE.html), [wearable](../api/wearable/latest/group__CAPI__MEDIA__TOOL__MODULE.html) | [Media Handle Management](multimedia/media-handle.md), [Media Muxing](multimedia/media-muxing.md),   [Media   Stream Playback](multimedia/media-streams.md) |
  | Media Vision       | Provides functionality for bar code detection and generation. Since 3.0, it also provides functionality for face detection, and tracking and recognition of both images and faces. | [mobile](../api/mobile/latest/group__CAPI__MEDIA__VISION__MODULE.html) (since 2.4), [wearable](../api/wearable/latest/group__CAPI__MEDIA__VISION__MODULE.html) (since 3.0) | [Barcode Detection and Generation](multimedia/image-barcode.md) |
  | Metadata Editor    | Provides functions for editing the metadata of several popular audio formats. | [mobile](../api/mobile/latest/group__CAPI__MEDIA__METADATA__EDITOR__MODULE.html) (since 2.4), [wearable ](../api/wearable/latest/group__CAPI__MEDIA__METADATA__EDITOR__MODULE.html) (since 3.0) | [Metadata](multimedia/metadata.md)   |
  | Metadata Extractor | Extracts metadata information from an input media file.   | [mobile](../api/mobile/latest/group__CAPI__METADATA__EXTRACTOR__MODULE.html), [wearable](../api/wearable/latest/group__CAPI__METADATA__EXTRACTOR__MODULE.html) | [Metadata](multimedia/metadata.md)   |
  | OpenAL             | Renders multichannel 3D audio.       | [mobile](../api/mobile/latest/group__OPENSRC__OPENAL__FRAMEWORK.html), [wearable](../api/wearable/latest/group__OPENSRC__OPENAL__FRAMEWORK.html) | [OpenAL](multimedia/openal.md)       |
  | Player             | Provides functions for media playback and can be used to control media playback attributes. | [mobile](../api/mobile/latest/group__CAPI__MEDIA__PLAYER__MODULE.html), [wearable](../api/wearable/latest/group__CAPI__MEDIA__PLAYER__MODULE.html) | [Media Playback](multimedia/media-playback.md)       |
  | Radio              | Supports radio usage. This submodule API can be used for tasks, such as starting and stopping the radio and scanning for radio channels. | [mobile](../api/mobile/latest/group__CAPI__MEDIA__RADIO__MODULE.html), [wearable](../api/wearable/latest/group__CAPI__MEDIA__RADIO__MODULE.html) | [Radio](multimedia/radio.md) |
  | Recorder           | Controls the recording of multimedia content. Recording process attributes, such as setting the recording filename and file format, can also be configured with this API submodule. | [mobile](../api/mobile/latest/group__CAPI__MEDIA__RECORDER__MODULE.html), [wearable](../api/wearable/latest/group__CAPI__MEDIA__RECORDER__MODULE.html) | [Media Recording](multimedia/media-recording.md), [Media Stream Recording](multimedia/stream-recorder.md) |
  | Screen Mirroring   | Provides functions for screen mirroring as a sink.   | [mobile](../api/mobile/latest/group__CAPI__MEDIA__SCREEN__MIRRORING__MODULE.html) (since 2.4) | [Screen Mirroring](multimedia/screen-mirroring.md)   |
  | Sound Manager      | Provides functions to get and set sound parameters, such as output sound volume. Session policy, such as the handling of sound session interrupts, can also be configured with this API submodule. | [mobile](../api/mobile/latest/group__CAPI__MEDIA__SOUND__MANAGER__MODULE.html), [wearable](../api/wearable/latest/group__CAPI__MEDIA__SOUND__MANAGER__MODULE.html) | [Sound Manager](multimedia/sound-manager.md) |
  | Sound Pool         | Provides functions for easy sound management, such as grouping sounds in pools, handling sound stream playback operations, and controlling stream and pool states. | [mobile](../api/mobile/latest/group__CAPI__SOUND__POOL__MODULE.html) (since 4.0), [wearable](../api/wearable/latest/group__CAPI__SOUND__POOL__MODULE.html) (since 4.0) | [Sound pools](multimedia/sound-pool.md)      |
  | StreamRecorder     | Provides functions to record video or audio from a buffer including a media packet. | [mobile](../api/mobile/latest/group__CAPI__MEDIA__STREAMRECORDER__MODULE.html) (since 3.0), [wearable](../api/wearable/latest/group__CAPI__MEDIA__STREAMRECORDER__MODULE.html) (since 3.0) | [Media Stream Recording](multimedia/stream-recorder.md)      |
  | Thumbnail Util     | Provides functions for creating the thumbnail from an input media file. | [mobile](../api/mobile/latest/group__CAPI__MEDIA__THUMBNAIL__UTIL__MODULE.html) (since 2.4), [wearable](../api/wearable/latest/group__CAPI__MEDIA__THUMBNAIL__UTIL__MODULE.html) (since 3.0) | [Thumbnail Images](multimedia/thumbnail-images.md)   |
  | Tone Player        | Plays and stops tones.       | [mobile](../api/mobile/latest/group__CAPI__MEDIA__TONE__PLAYER__MODULE.html) (since 2.4), [wearable](../api/wearable/latest/group__CAPI__MEDIA__TONE__PLAYER__MODULE.html) (since 2.4) | [Media Playback](multimedia/media-playback.md)       |
  | WAV Player         | Plays and stops Waveform Audio File (WAV) format files.      | [mobile](../api/mobile/latest/group__CAPI__MEDIA__WAV__PLAYER__MODULE.html), [wearable](../api/wearable/latest/group__CAPI__MEDIA__WAV__PLAYER__MODULE.html) | [Media Playback](multimedia/media-playback.md)       |
  | libEXIF            | Supports an image file format that extends existing formats, such as JPEG and TIFF. Many Tizen devices have a camera and use the EXIF format, and libEXIF can be used to read and write EXIF metainformation to and from image files. | [mobile](../api/mobile/latest/group__OPENSRC__LIBEXIF__FRAMEWORK.html), [wearable](../api/wearable/latest/group__OPENSRC__LIBEXIF__FRAMEWORK.html) |      |

- **Network**

  The Network API module contains submodule APIs, which can be used for data communication. It is responsible for managing connections, maintaining IP addresses, and connecting to the system through Bluetooth, Hypertext Transfer Protocol (HTTP), Near Field Communication (NFC), Sockets, and Wi-Fi. It also provides functions for retrieving information about a specific host from the Internet Domain Name System (DNS).

  | API submodule | Functionality                                    | API reference | Guide   |
  | ------------- | ------------------------------------------------ | ------------- | ------- |
  | Application Service Platform | Provides functions for discovery and session management using the Application Service Platform. | [mobile](../api/mobile/latest/group__CAPI__NETWORK__ASP__MODULE.html) (since 4.0), [wearable](../api/wearable/latest/group__CAPI__NETWORK__ASP__MODULE.html) (since 4.0) |    |
  | Bluetooth    | Manages Bluetooth devices. This involves launching the Bluetooth adapter and discovering, connecting, and bonding with other Bluetooth devices. | [mobile](../api/mobile/latest/group__CAPI__NETWORK__BLUETOOTH__MODULE.html), [wearable](../api/wearable/latest/group__CAPI__NETWORK__BLUETOOTH__MODULE.html) | [Bluetooth](connectivity/bluetooth.md)     |
  | Connection   | Gets network connection information, such as IP address, proxy information, gateway information, connection state, and data transfer statistics. | [mobile](../api/mobile/latest/group__CAPI__NETWORK__CONNECTION__MODULE.html), [wearable](../api/wearable/latest/group__CAPI__NETWORK__CONNECTION__MODULE.html) | [Connection   Manager](connectivity/connection.md) |
  | Curl         | Provides a client-side URL data transfer library supporting HTTP, HTTPS, FTP, and file URIs, among many other protocols. Curl allows applications to perform URL-related activities without a Web browser. | [mobile](../api/mobile/latest/group__OPENSRC__CURL__FRAMEWORK.html), [wearable](../api/wearable/latest/group__OPENSRC__CURL__FRAMEWORK.html) | [Curl](connectivity/curl.md)       |
  | DNSSD        | Provides functions for network service discovery using DNSSD. | [mobile](../api/mobile/latest/group__CAPI__NETWORK__DNSSD__MODULE.html) (since 3.0), [wearable](../api/wearable/latest/group__CAPI__NETWORK__DNSSD__MODULE.html) (since 3.0) | [Network Service Discovery](connectivity/nsd.md) |
  | HTTP         | Allows you to connect to a Web server to fetch and transmit a Web resource. | [mobile](../api/mobile/latest/group__CAPI__NETWORK__HTTP__MODULE.html) (since 3.0), [wearable](../api/wearable/latest/group__CAPI__NETWORK__HTTP__MODULE.html) (since 3.0) | [HTTP](connectivity/http-api.md)       |
  | Intelligent Network Monitoring | Provides API to manage monitoring network status. | [mobile](../api/mobile/latest/group__CAPI__NETWORK__INM__MODULE.html) (since 5.0), [wearable](../api/wearable/latest/group__CAPI__NETWORK__INM__MODULE.html) (since 5.0)  | [INM](connectivity/inm.md)  |
  | IoTCon       | Provides functions for IoT connectivity.   | [mobile](../api/mobile/latest/group__CAPI__IOT__CONNECTIVITY__MODULE.html), (since 3.0), [wearable](../api/wearable/latest/group__CAPI__IOT__CONNECTIVITY__MODULE.html) (since 3.0) | [IoTCon](connectivity/iotcon.md)   |
  | MTP          | Manages Media Transfer Protocol (MTP) file transfers between two devices. | [mobile](../api/mobile/latest/group__CAPI__NETWORK__MTP__MODULE.html) (since 3.0) | [MTP](connectivity/mtp.md) |
  | NFC          | Allows   management, such as registering and deregistering event listeners, of short-range wireless near field communication (NFC). This submodule API must   also be used to read, write, receive, and send NFC messages. | [mobile](../api/mobile/latest/group__CAPI__NETWORK__NFC__MODULE.html), [wearable](../api/wearable/latest/group__CAPI__NETWORK__NFC__MODULE.html) | [NFC](connectivity/nfc.md) |
  | SSDP         | Provides functions for network service discovery using SSDP. | [mobile](../api/mobile/latest/group__CAPI__NETWORK__SSDP__MODULE.html) (since 3.0), [wearable](../api/wearable/latest/group__CAPI__NETWORK__SSDP__MODULE.html) (since 3.0) | [Network Service   Discovery](connectivity/nsd.md) |
  | Smart Traffic Control      | Provides functions for managing and monitoring network packets. | [mobile](../api/mobile/latest/group__CAPI__NETWORK__STC__MODULE.html) (since 4.0), [wearable](../api/wearable/latest/group__CAPI__NETWORK__STC__MODULE.html) (since 4.0) | [STC](connectivity/stc.md) |
  | Smartcard    | Provides application communication to the SE applet functions. | [mobile](../api/mobile/latest/group__CAPI__NETWORK__SMARTCARD__MODULE.html) (since 2.3.1), [wearable](../api/wearable/latest/group__CAPI__NETWORK__SMARTCARD__MODULE.html) | [Smartcard](connectivity/smartcard.md)     |
  | SoftAP       | Consists of SoftAP Manager and SoftAP Client. SoftAP Manager provides functions for managing the SoftAP and SoftAP Client provides functions for getting the information about a connected client. | [mobile](../api/mobile/latest/group__CAPI__NETWORK__SOFTAP__MODULE.html) (since 5.0), [wearable](../api/wearable/latest/group__CAPI__NETWORK__SOFTAP__MODULE.html) (since 5.0) | [SoftAP](connectivity/softap.md)     |
  | VPN Service  | Manages Virtual Private Network (VPN) connections between two VPN devices. | [mobile](../api/mobile/latest/group__CAPI__NETWORK__VPN__SERVICE__MODULE.html) (since 3.0) | [VPN Connections](connectivity/vpn.md)     |
  | Wi-Fi        | Manages Wi-Fi connections and monitors the state of Wi-Fi connections. | [mobile](../api/mobile/latest/group__CAPI__NETWORK__WIFI__PACKAGE.html), [wearable](../api/wearable/latest/group__CAPI__NETWORK__WIFI__PACKAGE.html) | [Wi-Fi](connectivity/wifi.md)      |
  | Wi-Fi Direct | Manages the settings of Wi-Fi Direct. This submodule API also provides functions to connect and disconnect remote devices that use Wi-Fi Direct. | [mobile](../api/mobile/latest/group__CAPI__NETWORK__WIFI__DIRECT__MODULE.html) | [Wi-Fi Direct](connectivity/wifi-direct.md) |

- **Security**

  The Security API module contains submodule APIs which provide basic cryptographic functions, various utility functions through the OpenSSL open source library, and a secure password-protected repository for keys, certificates, and sensitive data.

  | API submodule | Functionality                                    | API reference | Guide   |
  | ------------- | ------------------------------------------------ | ------------- | ------- |
  | CSR                         | Provides the Content Screening Service to scan the content for data, files, and directories, and the Web Protection Service to protect a device by checking whether a URL the user wants to access is risky. | [mobile](../api/mobile/latest/group__CAPI__CSR__FRAMEWORK__MODULE.html) (since 3.0), [wearable](../api/wearable/latest/group__CAPI__CSR__FRAMEWORK__MODULE.html) (since 3.0) | [CSR](security/csr.md)       |
  | Device Certificate Manager  | Provides cryptography services (digital certificates and keys) for authentication and secure communication with another system. | [mobile](../api/mobile/latest/group__CAPI__DEVICE__CERTIFICATE__MANAGER__MODULE.html) (since 5.0), [wearable](../api/wearable/latest/group__CAPI__DEVICE__CERTIFICATE__MANAGER__MODULE.html) (since 5.0) | [Device Certificate Manager](security/device-certificate-manager.md) |
  | Device Policy Manager       | Provides functions to create security-aware applications that are useful in enterprise settings. | [mobile](../api/mobile/latest/group__CAPI__SECURITY__DPM__MODULE.html) (since 3.0), [wearable](../api/wearable/latest/group__CAPI__SECURITY__DPM__MODULE.html) (since 3.0) | [Device Policy Manager](security/dpm.md)     |
  | Key Manager                 | Provides functions to store keys, certificates, and sensitive data related to users and their password-protected applications in a secure repository. It also provides cryptographic operations to prevent key value names from being revealed to clients. | [mobile](../api/mobile/latest/group__CAPI__KEY__MANAGER__MODULE.html), [wearable](../api/wearable/latest/group__CAPI__KEY__MANAGER__MODULE.html) | [Key Manager](security/secure-key.md) |
  | OpenSSL                     | Provides an open source library that provides basic cryptographic functions and various utility functions. | [mobile](../api/mobile/latest/group__OPENSRC__OPENSSL__FRAMEWORK.html), [wearable](../api/wearable/latest/group__OPENSRC__OPENSSL__FRAMEWORK.html) |      |
  | Privacy Privilege Manager   | Provides functions for retrieving and determining an application's permissions for privacy privileges. | [mobile](../api/mobile/latest/group__CAPI__PRIVACY__PRIVILEGE__MANAGER__MODULE.html) (since 4.0), [wearable](../api/wearable/latest/group__CAPI__PRIVACY__PRIVILEGE__MANAGER__MODULE.html) (since 4.0) | [Privacy Privilege Manager](security/privacy-related-permissions.md) |
  | Privilege Info              | Retrieves and displays privilege information. This can be used to show a user the privileges that an application contains when they are downloading it onto their device. This is so that they are aware of the resources which the application may access. | [mobile](../api/mobile/latest/group__CAPI__SECURITY__FRAMEWORK__PRIVILEGE__INFO__MODULE.html), [wearable](../api/wearable/latest/group__CAPI__SECURITY__FRAMEWORK__PRIVILEGE__INFO__MODULE.html) | [Privilege Information](security/privilege.md)       |
  | Trusted Execution Framework | Provides the TEE Client API as defined by the GlobalPlatform TEE standard for connecting to applications executed in the TrustZone. | [mobile](../api/mobile/latest/group__CAPI__TEF__MODULE.html) (since 4.0), [wearable](../api/wearable/latest/group__CAPI__TEF__MODULE.html) (since 4.0) |   |
  | YACA                        | Provides cryptographic functions, such as key management, data integrity, data encryption and decryption, and low-level RSA operations. | [mobile](../api/mobile/latest/group__CAPI__YACA__MODULE.html) (since 3.0), [wearable](../api/wearable/latest/group__CAPI__YACA__MODULE.html) (since 3.0) | [YACA](security/yaca.md)     |

- **Social**

  The Social API module contains submodule APIs to manage personal data, such as contacts and calendars, on a device.

  | API submodule | Functionality                                    | API reference | Guide   |
  | ------------- | ------------------------------------------------ | ------------- | ------- |
  | Calendar          | Manages calendars, including events and tasks. It also stores and queries calendar information. | [mobile](../api/mobile/latest/group__CAPI__SOCIAL__CALENDAR__SVC__MODULE.html), [wearable](../api/wearable/latest/group__CAPI__SOCIAL__CALENDAR__SVC__MODULE.html) | [Calendar](personal/calendar.md) |
  | Contacts          | Manages phone contact information, such as address books, persons, and phone logs. | [mobile](../api/mobile/latest/group__CAPI__SOCIAL__CONTACTS__SVC__MODULE.html), [wearable](../api/wearable/latest/group__CAPI__SOCIAL__CONTACTS__SVC__MODULE.html) | [Contacts](personal/contacts.md) |
  | Phonenumber utils | Provides functions for parsing and formatting phone numbers. | [mobile](../api/mobile/latest/group__CAPI__TELEPHONY__PHONE__NUMBER__UTILS__MODULE.html) (since 2.4), [wearable](../api/wearable/latest/group__CAPI__TELEPHONY__PHONE__NUMBER__UTILS__MODULE.html) (since 2.4) | [Phone Number Management](personal/phonenumber.md) |

- **System**

  The System API module contains submodule APIs for system management.

  | API submodule | Functionality                                    | API reference | Guide   |
  | ------------- | ------------------------------------------------ | ------------- | ------- |
  | Device   | Controls devices and monitors their status. For example, this submodule API can be used to control and monitor the device battery, display, and LED. | [mobile](../api/mobile/latest/group__CAPI__SYSTEM__DEVICE__MODULE.html), [wearable](../api/wearable/latest/group__CAPI__SYSTEM__DEVICE__MODULE.html) | [System Information](device/system.md)       |
  | Dlog     | Sends log output and filters log messages from the dlog logging service. | [mobile](../api/mobile/latest/group__CAPI__SYSTEM__DLOG.html), [wearable](../api/wearable/latest/group__CAPI__SYSTEM__DLOG.html) |      |
  | Feedback | Provides functions to play sound or vibration associated with properties. | [mobile](../api/mobile/latest/group__CAPI__SYSTEM__FEEDBACK__MODULE.html) (since 2.4), [wearable](../api/wearable/latest/group__CAPI__SYSTEM__FEEDBACK__MODULE.html) (since 2.4) | [Feedback](device/feedback.md)       |
  | Media key | Provides functions to handle media keys from external devices that are connected to the Tizen device, such as the volume control buttons on a headset. | [mobile](../api/mobile/latest/group__CAPI__SYSTEM__MEDIA__KEY__MODULE.html), [wearable](../api/wearable/latest/group__CAPI__SYSTEM__MEDIA__KEY__MODULE.html) | [Media Key](multimedia/media-key.md) |
  | Runtime information | Obtains runtime information from a mobile device. For example, this submodule API can obtain information about the device's GPS. | [mobile ](../api/mobile/latest/group__CAPI__SYSTEM__RUNTIME__INFO__MODULE.html), [wearable](../api/wearable/latest/group__CAPI__SYSTEM__RUNTIME__INFO__MODULE.html) | [Runtime Information](device/runtime.md)
  | Sensor             | Starts and stops sensors and receives sensor data. | [mobile](../api/mobile/latest/group__CAPI__SYSTEM__SENSOR__MODULE.html), [wearable](../api/wearable/latest/group__CAPI__SYSTEM__SENSOR__MODULE.html) | [Device Sensors](location-sensors/device-sensors.md) |
  | Storage            | Obtains storage information, such as root directory, storage type (internal or external), storage status, and total available space size. | [mobile](../api/mobile/latest/group__CAPI__SYSTEM__STORAGE__MODULE.html), [wearable](../api/wearable/latest/group__CAPI__SYSTEM__STORAGE__MODULE.html) | [Data Storage](data/data-storages.md) |
  | System Information  | Obtains information about the device, such as the platform and API version, device model, supported device features, and screen dimensions. | [mobile ](../api/mobile/latest/group__CAPI__SYSTEM__SYSTEM__INFO__MODULE.html), [wearable](../api/wearable/latest/group__CAPI__SYSTEM__SYSTEM__INFO__MODULE.html) | [System Information](device/system.md)       |
  | System Settings     | Manages system settings, such as the lock screen settings. | [mobile](../api/mobile/latest/group__CAPI__SYSTEM__SYSTEM__SETTINGS__MODULE.html), [wearable](../api/wearable/latest/group__CAPI__SYSTEM__SYSTEM__SETTINGS__MODULE.html) | [System Settings](device/settings.md) |
  | T-trace            | Provides functions for writing trace messages to the system trace buffer. | [mobile](../api/mobile/latest/group__CAPI__SYSTEM__TRACE__MODULE.html) (since 2.4), [wearable](../api/wearable/latest/group__CAPI__SYSTEM__TRACE__MODULE.html) (since 3.0) | [Tracepoints](performance/tracepoints.md)     |
  | USB Host            | Provides direct access to USB devices to communicate with connected devices. | [mobile](../api/mobile/latest/group__CAPI__USB__HOST__MODULE.html) (since 3.0) | [USB Host](connectivity/usb-host.md) |

- **Telephony**

  The Telephony API module contains a submodule API to enable an application to access the telephony capabilities of the device, such as the call facility (call information and status), the network query services, and the SIM module.

  | API submodule | Functionality                                    | API reference | Guide   |
  | ------------- | ------------------------------------------------ | ------------- | ------- |
  | Telephony Information | Obtains call, network, and SIM information. | [mobile](../api/mobile/latest/group__CAPI__TELEPHONY__INFORMATION.html), [wearable](../api/wearable/latest/group__CAPI__TELEPHONY__INFORMATION.html)  | [Telephony](connectivity/telephony.md) |

- **UI**

  The UI API module contains submodule APIs and open source libraries for 2D and 3D graphics and text.

  | API submodule | Functionality                                    | API reference | Guide   |
  | ------------- | ------------------------------------------------ | ------------- | ------- |
  | Cairo                     | Provides a library for 2D vector graphics drawing. Vector graphics are advantageous because they have small file sizes and can be scaled to any size without any loss of image quality. Cairo EvasGL APIs have been newly added since 2.3.1. | [mobile](../api/mobile/latest/group__OPENSRC__CAIRO__FRAMEWORK.html), [wearable](../api/wearable/latest/group__OPENSRC__CAIRO__FRAMEWORK.html) | [Cairo](graphics/cairo.md)       |
  | Clipboard History Manager | Provides copy and paste functionalities for applications. | [mobile](../api/mobile/latest/group__CAPI__CBHM__MODULE.html) (since 3.0) |  |
  | EFL                       | Provides a collection of libraries that are independent and can be built on top of each other to provide useful features that   complement the existing environment. | [mobile](../api/mobile/latest/group__EFL.html) [wearable](../api/wearable/latest/group__EFL.html) | [EFL](ui/efl/index.md)   |
  | EFL UTIL                  | Gets and sets the priority order of notification windows.  | [mobile](../api/mobile/latest/group__CAPI__EFL__UTIL__MODULE.html), [wearable](../api/wearable/latest/group__CAPI__EFL__UTIL__MODULE.html) | [EFL Utilities](ui/efl/efl-util.md)    |
  | EFL Extension             | Enhances the EFL libraries and includes device-specific features (such as support for the hardware Back key). | [mobile](../api/mobile/latest/group__CAPI__EFL__EXTENSION__MODULE.html) (since 2.3.1), [wearable](../api/wearable/latest/group__CAPI__EFL__EXTENSION__MODULE.html) | [Managing Rotary Events](ui/efl/rotary-events.md) |
  | External Output Manager   | Provides functions for external outputs.     | [mobile](../api/mobile/latest/group__CAPI__UI__EOM__MODULE.html) (since 2.4), [wearable](../api/wearable/latest/group__CAPI__UI__EOM__MODULE.html) (since 3.0) |  |
  | Fontconfig and Freetype   | Provides a text rendering library and font-handling library to let applications find a font or closely matching font. | [mobile](../api/mobile/latest/group__OPENSRC__FONTCONFIG__FRAMEWORK.html), [wearable](../api/wearable/latest/group__OPENSRC__FONTCONFIG__FRAMEWORK.html) |   |
  | HarfBuzz                  | Provides functions for text shaping. | [mobile](../api/mobile/latest/group__OPENSRC__HARFBUZZ__FRAMEWORK.html) (since 2.4), [wearable](../api/wearable/latest/group__OPENSRC__HARFBUZZ__FRAMEWORK.html) (since 3.0) |  |
  | Minicontrol               | Provides functions for creating and displaying an EFL socket window. | [mobile](../api/mobile/latest/group__MINICONTROL__LIBRARY.html) (since 2.4), [wearable](../api/wearable/latest/group__MINICONTROL__LIBRARY.html) (since 5.0) | [Minicontrol Window](notification/minicontrol.md) |
  | OpenGL ES                 | Provides a library for rendering 3D and 2D graphics in embedded systems. | [mobile](../api/mobile/latest/group__OPENSRC__OPENGLES__FRAMEWORK.html) (since 4.0), [wearable](../api/wearable/latest/group__OPENSRC__OPENGLES__FRAMEWORK.html) (since 4.0) | [OpenGL ES](graphics/opengl.md) |
  | SDL                       | Provides a low level hardware abstraction layer to computer multimedia hardware components. It manages video, audio, input devices, threads, and timers. | [mobile](../api/mobile/latest/group__OPENSRC__SDL__FRAMEWORK.html) (since 3.0), [wearable](../api/wearable/latest/group__OPENSRC__SDL__FRAMEWORK.html) (since 3.0) | [SDL](graphics/sdl.md)   |
  | TBM Surface               | Provides functions for the graphics buffer.  | [mobile](../api/mobile/latest/group__CAPI__UI__TBM__SURFACE__MODULE.html), [wearable](../api/wearable/latest/group__CAPI__UI__TBM__SURFACE__MODULE.html) | [Graphic Buffer and Surface](graphics/graphic-buffer.md) |
  | Tizen Window System Shell            | Allows you to communicate with the window manager.   | [mobile](../api/mobile/latest/group__TIZEN__WS__SHELL__MODULE.html) (since 3.0), [wearable](../api/wearable/latest/group__TIZEN__WS__SHELL__MODULE.html) (since 3.0) | [Tizen Window System Shell](ui/tizen-ws-shell/index.md) |
  | Vulkan                    | Provides functions for rendering 3D and 2D graphics in embedded systems. | [mobile](../api/mobile/latest/group__OPENSRC__VULKAN__FRAMEWORK.html) (since 3.0), [wearable](../api/wearable/latest/group__OPENSRC__VULKAN__FRAMEWORK.html) (since 3.0) | [Vulkan](graphics/vulkan.md)     |

- **UIX**

  The UIX API module contains submodule APIs for handling input method, recognizing gestures, and managing sound data such as voice commands.

  | API submodule | Functionality                                    | API reference | Guide   |
  | ------------- | ------------------------------------------------ | ------------- | ------- |
  | Gesture               | Provides functions for recognizing hand gestures from input sensor data. | [wearable](../api/wearable/latest/group__CAPI__UIX__GESTURE__MODULE.html) (since 6.0) | [Gesture](text-input/capi-ui-gesture.md) |
  | Input Method          | Provides functions for starting the IME application life-cycle, for interacting with the current UI state of the IME, and getting attributes and events. | [mobile](../api/mobile/latest/group__CAPI__UIX__INPUTMETHOD__MODULE.html) (since 2.4), [wearable](../api/wearable/latest/group__CAPI__UIX__INPUTMETHOD__MODULE.html) (since 3.0) | [Input Method](text-input/input-method.md)  |
  | Input Method Manager  | Provides functions for launching the input method editor (IME) list and selector settings. | [mobile](../api/mobile/latest/group__CAPI__UIX__INPUTMETHOD__MANAGER__MODULE.html) (since 2.4), [wearable](../api/wearable/latest/group__CAPI__UIX__INPUTMETHOD__MANAGER__MODULE.html) (since 3.0) | [Input Method](text-input/input-method.md)  |
  | Multi assistance      | Provides functions for supporting users to use several assistants. | [mobile](../api/mobile/latest/group__CAPI__UIX__MULTI__ASSISTANT__MODULE.html) (since 5.0), [wearable](../api/wearable/latest/group__CAPI__UIX__MULTI__ASSISTANT__MODULE.html) (since 5.0) | [Input Method](text-input/input-method.md)  |
  | STT                   | Provides functions to recognize speech.      | [mobile](../api/mobile/latest/group__CAPI__UIX__STT__MODULE.html), [wearable](../api/wearable/latest/group__CAPI__UIX__STT__MODULE.html) | [Speech-to-text](text-input/stt.md) |
  | STT Engine            | Provides functions for operating the Speech-To-Text engine. | [mobile](../api/mobile/latest/group__CAPI__UIX__STTE__MODULE.html) (since 3.0), [wearable](../api/wearable/latest/group__CAPI__UIX__STTE__MODULE.html) (since 3.0) | [Speech-to-text](text-input/stt.md) |
  | TTS                   | Provides functions for synthesizing voice from text and playing synthesized sound data. | [mobile](../api/mobile/latest/group__CAPI__UIX__TTS__MODULE.html), [wearable](../api/wearable/latest/group__CAPI__UIX__TTS__MODULE.html) | [Text-to-speech](text-input/tts.md) |
  | TTS Engine            | Provides functions for operating the Text-To-Speech engine. | [mobile](../api/mobile/latest/group__CAPI__UIX__TTSE__MODULE.html) (since 3.0), [wearable](../api/wearable/latest/group__CAPI__UIX__TTSE__MODULE.html) (since 3.0) | [Text-to-speech](text-input/tts.md) |
  | Voice control         | Provides functions for registering commands and getting notifications when a registered command is recognized. | [mobile](../api/mobile/latest/group__CAPI__UIX__VOICE__CONTROL__MODULE.html) (since 2.4), [wearable](../api/wearable/latest/group__CAPI__UIX__VOICE__CONTROL__MODULE.html) (since 3.0) | [Voice Control](text-input/voice-control.md) |
  | Voice control elementary  | Provides functions to control UI components through voice commands. | [mobile](../api/mobile/latest/group__VOICE__CONTROL__ELEMENTARY__MODULE.html) (since 2.4), [wearable](../api/wearable/latest/group__VOICE__CONTROL__ELEMENTARY__MODULE.html) (since 3.0) | [Voice Control](text-input/voice-control.md) |     |
  | Voice control engine  | Provides functions to operate Voice-Control Engine.  | [mobile](../api/mobile/latest/group__CAPI__UIX__VOICE__CONTROL__ENGINE__MODULE.html) (since 4.0), [wearable](../api/wearable/latest/group__CAPI__UIX__VOICE__CONTROL__ENGINE__MODULE.html) (since 4.0) | [Voice Control](text-input/voice-control-engine.md) |
  | Voice control manager | Provides functions for recording voice and giving responses for recognized voice commands to users.  | [mobile](../api/mobile/latest/group__CAPI__UIX__VOICE__CONTROL__MANAGER__MODULE.html) (since 5.0), [wearable](../api/wearable/latest/group__CAPI__UIX__VOICE__CONTROL__MANAGER__MODULE.html) (since 5.0) | [Voice Control](text-input/voice-control-manager.md) |


- **Web**

  The Web API module contains submodule APIs for browsing the Internet, tracking browsing history, downloading Web content, and manipulating JavaScript Object Notation (JSON) documents.

  | API submodule | Functionality                                    | API reference | Guide   |
  | ------------- | ------------------------------------------------ | ------------- | ------- |
  | Json-Glib     | Allows reading and parsing of JavaScript Object Notation (JSON) documents. | [mobile](../api/mobile/latest/group__OPENSRC__JSONGLIB__FRAMEWORK.html), [wearable](../api/wearable/latest/group__OPENSRC__JSONGLIB__FRAMEWORK.html) |
  | WebView       | Displays and controls Web pages. This submodule API contains interfaces for browsing, tracking browsing history, and downloading Web content. | [mobile](../api/mobile/latest/group__WEBVIEW.html), [wearable](../api/wearable/latest/group__WEBVIEW.html) | [Web View](connectivity/web-view.md) |

> **Note**
>
> If you have an application based on Tizen 2.3, use the [Migration Guide](migration-guide.md) to make it conform to Tizen 2.4 Application Framework APIs.


## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable

