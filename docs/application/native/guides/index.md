# Tizen Native APIs

You can develop native applications using the native API modules. You can create diverse applications with a variety of features, and design versatile applications and intriguing user interfaces with text and graphics while taking advantage of many device functionalities, such as sensors and call operations. In addition, you can, for example, manage content and media files, use network and social services, and provide messaging and embedded Web browsing functionality.

The Tizen platform also provides a special kind of native application model, which consists of 1 UI native application and 1 or more native service applications.

The native API specification consists of multiple API modules that represent the versatility and wide variety of features that you can implement in your native application. Each API module represents a set of logically similar submodule APIs which can be grouped into the same category. This structure was designed to make it easier for you to narrow down and find the specific methods that you require to implement a feature in your native application.

There are two types of submodules  - Tizen native modules and open source modules. The integration of open source modules in the native API structure allows you to add additional features by using well-known open source libraries. This is particularly advantageous for developers who are familiar with certain libraries because they can quickly add features and use previously written code in certain cases.

## Mobile Native API Modules

The following list defines the Tizen mobile native API. The list describes the API modules and the functionality of all their submodule APIs within that module. The list also acts as a reference source for when you are planning a new feature for your application and need a way to efficiently compare different API modules to decide which APIs to use.

> **Note**
>
> Except as noted, the mobile native APIs are available since Tizen 2.3.

- [Account](../api/mobile/latest/group__CAPI__ACCOUNT__FRAMEWORK.html)

  The Account API module features include managing various account information, such as receiving sync operation notifications and obtaining an access token by using the OAuth 2.0 authorization.

  | API submodule              | Functionality              | Guide               |
  |----------------------------|----------------------------|---------------------|
  | [Account Manager](../api/mobile/latest/group__CAPI__ACCOUNT__MANAGER__MODULE.html) | Provides CRUD (Create, Read, Update, Delete) account management functionality. | [Account Management](personal/account.md) |
  | [FIDO Client (since 3.0)](../api/mobile/latest/group__CAPI__FIDO__MODULE.html) | Allows you to utilize the device's available authenticators for online service integration. | [FIDO Universal Authentication Framework](personal/fido.md) |
  | [OAuth 2.0 (since 2.4)](../api/mobile/latest/group__CAPI__OAUTH2__MODULE.html) | Provides an easy way to gain an access token between a server and client. | [OAuth 2.0](personal/oauth.md) |
  | [Sync Manager](../api/mobile/latest/group__CAPI__SYNC__MANAGER__MODULE.html) | Helps applications in scheduling their data sync operations. | [Synchronization Management](personal/data-sync.md) |
  | [libOAuth](../api/mobile/latest/group__OPENSRC__LIB__OAUTH__FRAMEK.html) | Provides a library for using an open standard for secure authorization. This library enables users to securely log into an account on an application by using their logon credentials from another secondary account that they can have with another account provider or application. | |

- [Application Framework](../api/mobile/latest/group__CAPI__APPLICATION__FRAMEWORK.html)

  The Application Framework API contains submodule APIs for application development. The submodule APIs enable application life-cycle management, usage of functionality that is exported by other applications, and access to a user's application preferences.

  | API submodule              | Functionality              | Guide               |
  |----------------------------|----------------------------|---------------------|
  | [Application](../api/mobile/latest/group__CAPI__APPLICATION__MODULE.html) | Manages the application's main event loop, state change events, and basic system events, and gets information about the application. It is also used to launch other applications. | [Applications](applications/overview.md) |
  | [Application Manager](../api/mobile/latest/group__CAPI__APPLICATION__MANAGER__MODULE.html) | Gets information, such as the application ID and path to the shared data directory, of the current application and other installed or running applications. | [Application Manager](app-management/app-manager.md) |
  | [Attach Panel (since 2.4)](../api/mobile/latest/group__CAPI__PANEL__ATTACH__MODULE.html) | Provides a panel in which users can take pictures, record voice, and select files to attach. | [Attach Panel](notification/attach-panel.md) |
  | [Badge](../api/mobile/latest/group__BADGE__MODULE.html) | Creates and removes badges on the application's home screen icon. A badge is an image displayed on the application icon, which informs the user about notifications and events. This submodule can also be used to set and get the badge value and visibility. |  [Application Icons](app-management/app-icons.md) |
  | [Bundle](../api/mobile/latest/group__CORE__LIB__BUNDLE__MODULE.html) | Provides a string-based dictionary abstract data type (ADT). A dictionary is an ordered or unordered list of key-element pairs. Keys are used to locate elements in the list. This submodule can be used to create and manage a dictionary. | [Data Bundle](app-management/data-bundles.md) |
  | [Data Control](../api/mobile/latest/group__CAPI__DATA__CONTROL__MODULE.html) | Exchanges data between applications by allowing an application to query the public database of another application that has opted to be a data provider. | [Data Control](app-management/data-control.md) |
  | [Message Port](../api/mobile/latest/group__CAPI__MESSAGE__PORT__MODULE.html) | Sends and receives small messages between applications without interference from other applications and processes. Each message is a bundle. | [Message Port](app-management/message-port.md) |
  | [Notification](../api/mobile/latest/group__NOTIFICATION__MODULE.html) | Creates, inserts, and updates notifications so that applications can relay information to users. Visuals, sounds, or vibrations can be used as notifications. | [Notifications](notification/notifications.md) |
  | [Package Manager](../api/mobile/latest/group__CAPI__PACKAGE__MANAGER__MODULE.html) | Stores and receives information related to packages installed on the device. This is information can be, for example, the package name, path to the icon image, or the application version. It can also be used to check whether 2 package certificates match. If they match, they have been created by the same developer and can share resources securely. | [Package Manager](app-management/package-manager.md) |
  | [Service Application](../api/mobile/latest/group__CAPI__SERVICE__APP__MODULE.html) | Handles Tizen service application (non-UI application) state changes and system events. It is also used to start and exit the main event loop of service applications. | [Service Application](applications/service-app.md) |
  | [Shortcut](../api/mobile/latest/group__SHORTCUT__MODULE.html) | Adds application shortcuts to the device home screen, the main landing screen of the device. | [Application Icons](app-management/app-icons.md) |
  | [Widget (since 2.3.1)](../api/mobile/latest/group__CAPI__WIDGET__FRAMEWORK.html) | Handles Tizen widget application state changes and system events. It is also used to start and exit the main event loop of widget applications. | [EFL Widget Application](applications/widget-app.md) |

- [Base](../api/mobile/latest/group__CAPI__BASE__FRAMEWORK.html)

  The Base API contains submodule APIs for internationalization support and contains various open source libraries.

  | API submodule              | Functionality              |
  |----------------------------|----------------------------|
  | [C++ Standard Library](../api/mobile/latest/group__OPENSRC__STL__GCC__FRAMEWORK.html) | Provides a standard C++ library.    |
  | [Common Error](../api/mobile/latest/group__CAPI__COMMON__ERROR.html) | Provides error codes that are common for the whole Tizen API. |
  | [Glib](../api/mobile/latest/group__OPENSRC__GLIB__FRAMEWORK.html) | Provides low-level libraries and advanced data structures, such as linked lists and hash tables, for use in application development. |
  | [Glibc](../api/mobile/latest/group__OPENSRC__GLIBC__FRAMEWORK.html) | Provides a standard C library.     |
  | [LibXML](../api/mobile/latest/group__OPENSRC__LIBXML__FRAMEWORK.html) | Used to parse XML documents, such as the Application Manifest. |
  | [Minizip](../api/mobile/latest/group__OPENSRC__MINIZIP__FRAMEWORK.html) | Provides a library to process files in the ZIP format. It can be used to zip, unzip and compress files. |
  | [OpenMP](../api/mobile/latest/group__OPENSRC__OPENMP__FRAMEWORK.html) | Supports shared memory multiprocessing. This can be used for complex tasks on multicore processors. |
  | [Sqlite](../api/mobile/latest/group__OPENSRC__SQLITE__FRAMEWORK.html) | Implements a lightweight SQL relational database. This is widely used for embedded client or local storage. |
  | [Utils > i18n](../api/mobile/latest/group__CAPI__BASE__UTILS__I18N__MODULE.html) | Provides internationalization (i18n) support, such as flexibly generating date formats and numbers, depending on the locale setting of the device. |
  | [zlib (since 2.4)](../api/mobile/latest/group__OPENSRC__ZLIB__FRAMEWORK.html) | Used for in-memory compression and decompression. |


- [Content](../api/mobile/latest/group__CAPI__CONTENT__FRAMEWORK.html)

  The Content API module contains submodule APIs for managing the most common device media data types, such as image, audio, and video files. It provides operations to search for content, search for content information stored on the device, create playlists, download content from servers through an HTTP connection, and access the EXIF information in an image file.

  | API submodule              | Functionality              | Guide               |
  |----------------------------|----------------------------|---------------------|
  | [Download](../api/mobile/latest/group__CAPI__WEB__DOWNLOAD__MODULE.html) | Creates and manages 1 or more download requests. Content is downloaded from servers through an HTTP connection. | [Download](connectivity/download.md) |
  | [MIME Type](../api/mobile/latest/group__CAPI__CONTENT__MIME__TYPE__MODULE.html) | Maps MIME types to file extensions and vice versa. For example, the .jpeg file extension is mapped to the image/jpeg MIME type, which is required when using other API modules, such as the AppControl API in the Application submodule API, because it operates with MIME types. | [Metadata](multimedia/metadata.md) |
  | [Media Content](../api/mobile/latest/group__CAPI__MEDIA__CONTENT__MODULE.html) | Connects and disconnects from the media content service. This connection is required to insert, update and remove media file information in the media content database. Common media data types, such as image, audio, and video can be managed through the database. Other queries, such as searching for content and content information and accessing EXIF information from image files, are also possible. | [Media Content](multimedia/media-content.md) |

- [Context](../api/mobile/latest/group__CAPI__CONTEXT__FRAMEWORK.html)

  The Context API module contains submodule APIs to detect user information, such as when a user is running with a device, and device information, such as gestures when a device is tilted.

  | API submodule              | Functionality              | Guide               |
  |----------------------------|----------------------------|---------------------|
  | [Activity Recognition](../api/mobile/latest/group__CAPI__CONTEXT__ACTIVITY__MODULE.html) | Detects user activities, such as walking, running, and being in a moving vehicle with a device. | [Activity Recognition](location-sensors/activity.md) |
  | [Contextual History](../api/mobile/latest/group__CAPI__CONTEXT__HISTORY__MODULE.html) | Allows you to query statistics and patterns derived from contextual history data. | [Contextual Device Usage History Data](personal/context.md) |
  | [Contextual Trigger (since 2.4)](../api/mobile/latest/group__CAPI__CONTEXT__TRIGGER__MODULE.html) | Provides a way to define rules, each of which can trigger a specified action when the rule is satisfied. | [Contextual System Event Trigger](alarm/trigger.md) |
  | [Gesture Recognition](../api/mobile/latest/group__CAPI__CONTEXT__GESTURE__MODULE.html) | Detects user gestures on devices, such as tilt, snap, and double-tap. | [Gesture Recognition](location-sensors/gesture.md) |

- [Location](../api/mobile/latest/group__CAPI__LOCATION__FRAMEWORK.html)

  The Location API module allows the geographical position of a device to be determined for use with location-based services.

  | API submodule              | Functionality              | Guide               |
  |----------------------------|----------------------------|---------------------|
  | [Geofence Manager (since 2.4)](../api/mobile/latest/group__CAPI__GEOFENCE__MANAGER__MODULE.html) | Provides a service related to geofence (geo-fence). | [Geofences](location-sensors/geofences.md) |
  | [Location Manager](../api/mobile/latest/group__CAPI__LOCATION__MANAGER__MODULE.html) | Acquires information about the geographical location of the device. It also allows the receiving of notifications about position changes, velocity changes, and when a given geographical area is left. | [Location Manager](location-sensors/location.md) |
  | [Maps Service (since 2.4)](../api/mobile/latest/group__CAPI__MAPS__SERVICE__MODULE.html) | Provides a set of functions, helping to create map-aware applications. | [Maps and Maps Service](location-sensors/maps.md) |

- [Messaging](../api/mobile/latest/group__CAPI__MESSAGING__FRAMEWORK.html)

  The Messaging API module contains submodule APIs which grant access to the messaging capabilities, such as SMS, MMS and email, of the device.

  | API submodule              | Functionality              | Guide               |
  |----------------------------|----------------------------|---------------------|
  | [Email](../api/mobile/latest/group__CAPI__MESSAGING__EMAIL__MODULE.html) | Allows composing, sending, and receiving of email messages. | [Email](messaging/email.md) |
  | [Messages](../api/mobile/latest/group__CAPI__MESSAGING__MESSAGES__MODULE.html) | Allows composing, sending, and receiving of SMS, MMS, and WAP push messages. | [Messages](messaging/messages.md) |
  | [Push](../api/mobile/latest/group__CAPI__MESSAGING__PUSH__PUBLIC__MODULE.html) | Allows receiving of push notifications from a push server. | [Push](messaging/push.md), [Push Server](messaging/push-server.md) |

- [Multimedia](../api/mobile/latest/group__CAPI__MEDIA__FRAMEWORK.html)

  The Multimedia API module contains submodule APIs for easily integrating an application with audio, image, and video files. It can also be used for image editing.

  | API submodule              | Functionality              | Guide               |
  |----------------------------|----------------------------|---------------------|
  | [Audio I/O](../api/mobile/latest/group__CAPI__MEDIA__AUDIO__IO__MODULE.html) | Manages the system audio devices by granting access to the hardware layer of the sound card. This API must be used for tasks that require raw audio data buffers in PCM format. | [Raw Audio Playback and Recording](multimedia/raw-audio.md) |
  | [Camera](../api/mobile/latest/group__CAPI__MEDIA__CAMERA__MODULE.html) | Accesses the camera preview to display photo previews, focuses images, and captures images. | [Camera](multimedia/camera.md) |
  | [Image Util](../api/mobile/latest/group__CAPI__MEDIA__IMAGE__UTIL__MODULE.html) | Encodes and decodes JPEG images. It also provides tools, such as crop, resize, and rotate, to transform images. | [Image Editing](multimedia/image-edit.md), [Image Recognition](multimedia/image-recognition.md) |
  | [Media Codec](../api/mobile/latest/group__CAPI__MEDIA__CODEC__MODULE.html) | Provides interfaces for encoding and decoding audio and video data, such as AAC audio or MPEG-4 AVC video. | [Media Conversions](multimedia/media-conversions.md) |
  | [Media Controller (since 2.4)](../api/mobile/latest/group__CAPI__MEDIA__CONTROLLER__MODULE.html) | Provides functions for communication between the media controller server and the media controller client. | [Media Controller](multimedia/media-controller.md) |
  | [Media Demuxer (since 3.0)](../api/mobile/latest/group__CAPI__MEDIADEMUXER__MODULE.html) | Provides functions for demuxing media data. | [Media Muxing](multimedia/media-muxing.md) |
  | [Media Muxer (since 3.0)](../api/mobile/latest/group__CAPI__MEDIAMUXER__MODULE.html) | Provides functions for muxing media data. | [Media Muxing](multimedia/media-muxing.md) |
  | [Media Streamer (since 3.0)](../api/mobile/latest/group__CAPI__MEDIA__STREAMER__MODULE.html) | Provides functions for building custom pipeline for streaming media. | [Media Stream Playback](multimedia/media-streams.md) |
  | [Media Tool](../api/mobile/latest/group__CAPI__MEDIA__TOOL__MODULE.html) | Handles audio and video packet buffers. These buffers are utilized by the other Multimedia submodule APIs. | [Media Handle Management](multimedia/media-handle.md), [Media Muxing](multimedia/media-muxing.md), [Media Stream Playback](multimedia/media-streams.md) |
  | [Media Vision (since 2.4)](../api/mobile/latest/group__CAPI__MEDIA__VISION__MODULE.html) | Provides functionality for barcode detection and generation. Since 3.0, it also provides functionality for face detection, and tracking and recognition of both images and faces. | [Barcode Detection and Generation](multimedia/image-barcode.md) |
  | [Metadata Editor (since 2.4)](../api/mobile/latest/group__CAPI__MEDIA__METADATA__EDITOR__MODULE.html) | Provides functions for editing the metadata of several popular audio formats. | [Metadata](multimedia/metadata.md) |
  | [Metadata Extractor](../api/mobile/latest/group__CAPI__METADATA__EXTRACTOR__MODULE.html) | Extracts metadata information from an input media file. | [Metadata](multimedia/metadata.md) |
  | [OpenAL](../api/mobile/latest/group__OPENSRC__OPENAL__FRAMEWORK.html) | Renders multichannel 3D audio. | [OpenAL](multimedia/openal.md) |
  | [Player](../api/mobile/latest/group__CAPI__MEDIA__PLAYER__MODULE.html) | Provides functions for media playback and can be used to control media playback attributes. | [Media Playback](multimedia/media-playback.md) |
  | [Radio](../api/mobile/latest/group__CAPI__MEDIA__RADIO__MODULE.html) | Supports radio usage. This submodule API can be used for tasks, such as starting and stopping the radio and scanning for radio channels. | [Radio](multimedia/radio.md) |
  | [Recorder](../api/mobile/latest/group__CAPI__MEDIA__RECORDER__MODULE.html) | Controls the recording of multimedia content. Recording process attributes, such as setting the recording filename and file format, can also be configured with this API submodule. | [Media Recording](multimedia/media-recording.md), [Media Stream Recording](multimedia/stream-recorder.md) |
  | [Screen Mirroring (since 2.4)](../api/mobile/latest/group__CAPI__MEDIA__SCREEN__MIRRORING__MODULE.html) | Provides functions for screen mirroring as a sink. | [Screen Mirroring](multimedia/screen-mirroring.md) |
  | [Sound Manager](../api/mobile/latest/group__CAPI__MEDIA__SOUND__MANAGER__MODULE.html) | Provides functions to get and set sound parameters, such as output sound volume. Session policy, such as the handling of sound session interrupts, can also be configured with this API submodule. | [Sound Manager](multimedia/sound-manager.md) |
  | [Sound Pool (since 4.0)](../api/mobile/latest/group__CAPI__SOUND__POOL__MODULE.html) | Provides functions for easy sound management, such as grouping sounds in pools, handling sound stream playback operations, and controlling stream and pool states. | [Sound pools](multimedia/sound-pool.md) |
  | [StreamRecorder (since 3.0)](../api/mobile/latest/group__CAPI__MEDIA__STREAMRECORDER__MODULE.html) | Provides functions to record video or audio from a buffer including a media packet. | [Media Stream Recording](multimedia/stream-recorder.md) |
  | [Thumbnail Util (since 2.4)](../api/mobile/latest/group__CAPI__MEDIA__THUMBNAIL__UTIL__MODULE.html) | Provides functions for creating the thumbnail from an input media file. | [Thumbnail Images](multimedia/thumbnail-images.md) |
  | [Tone Player](../api/mobile/latest/group__CAPI__MEDIA__TONE__PLAYER__MODULE.html) | Plays and stops tones. | [Media Playback](multimedia/media-playback.md) |
  | [Video Util](../api/mobile/latest/group__CAPI__MEDIA__VIDEO__UTIL__MODULE.html) | Transcodes or converts media files from one encoding to another. This API supports certain video codecs, audio codecs, and file formats. | |
  | [WAV Player](../api/mobile/latest/group__CAPI__MEDIA__WAV__PLAYER__MODULE.html) | Plays and stops Waveform Audio File (WAV) format files. | [Media Playback](multimedia/media-playback.md) |
  | [libEXIF](../api/mobile/latest/group__OPENSRC__LIBEXIF__FRAMEWORK.html) | Supports an image file format that extends existing formats, such as JPEG and TIFF. Many Tizen devices have a camera and use the EXIF format, and libEXIF can be used to read and write EXIF metainformation to and from image files. | |

- [Network](../api/mobile/latest/group__CAPI__NETWORK__FRAMEWORK.html)

  The Network API module contains submodule APIs, which can be used for data communication. It is responsible for managing connections, maintaining IP addresses, and connecting to the system through Bluetooth, Hypertext Transfer Protocol (HTTP), Near Field Communication (NFC), Sockets, and Wi-Fi. It also provides functions for retrieving information about a specific host from the Internet Domain Name System (DNS).

  | API submodule              | Functionality              | Guide               |
  |----------------------------|----------------------------|---------------------|
  | [Application Service Platform (since 4.0)](../api/mobile/latest/group__CAPI__NETWORK__ASP__MODULE.html) | Provides functions for discovery and session management using the Application Service Platform. | |
  | [Bluetooth](../api/mobile/latest/group__CAPI__NETWORK__BLUETOOTH__MODULE.html) | Manages Bluetooth devices. This involves launching the Bluetooth adapter and discovering, connecting, and bonding with other Bluetooth devices. | [Bluetooth](connectivity/bluetooth.md) |
  | [Connection](../api/mobile/latest/group__CAPI__NETWORK__CONNECTION__MODULE.html) | Gets network connection information, such as IP address, proxy information, gateway information, connection state, and data transfer statistics. | [Connection Manager](connectivity/connection.md) |
  | [Curl](../api/mobile/latest/group__OPENSRC__CURL__FRAMEWORK.html) | Provides a client-side URL data transfer library supporting HTTP, HTTPS, FTP, and file URIs, among many other protocols. Allows applications to perform URL-related activities without a Web browser. | [Curl](connectivity/curl.md) |
  | [DNSSD(since 3.0)](../api/mobile/latest/group__CAPI__NETWORK__DNSSD__MODULE.html) | Provides functions for network service discovery using DNSSD. | [Network Service Discovery](connectivity/nsd.md) |
  | [HTTP (since 3.0)](../api/mobile/latest/group__CAPI__NETWORK__HTTP__MODULE.html) | Allows you to connect to a Web server to fetch and transmit a Web resource. | [HTTP](connectivity/http.md) |
  | [IoTCon (since 3.0)](../api/mobile/latest/group__CAPI__IOT__CONNECTIVITY__MODULE.html) | Provides functions for IoT connectivity. | [IoTCon](connectivity/iotcon.md) |
  | [MTP (since 3.0)](../api/mobile/latest/group__CAPI__NETWORK__MTP__MODULE.html) | Manages Media Transfer Protocol (MTP) file transfers between 2 devices. | [MTP](connectivity/mtp.md) |
  | [NFC](../api/mobile/latest/group__CAPI__NETWORK__NFC__MODULE.html) | Allows management, such as registering and deregistering event listeners, of short-range wireless near field communication (NFC). This submodule API must also be used to read, write, receive, and send NFC messages. | [NFC](connectivity/nfc.md) |
  | [SSDP (since 3.0)](../api/mobile/latest/group__CAPI__NETWORK__SSDP__MODULE.html) | Provides functions for network service discovery using SSDP. | [Network Service Discovery](connectivity/nsd.md) |
  | [Smart Traffic Control (since 4.0)](../api/mobile/latest/group__CAPI__NETWORK__STC__MODULE.html) | Provides functions for managing and monitoring network packets. | [STC](connectivity/stc.md) |
  | [Smartcard (since 2.3.1)](../api/mobile/latest/group__CAPI__NETWORK__SMARTCARD__MODULE.html) | Provides application communication to the SE applet functions. | [Smartcard](connectivity/smartcard.md) |
  | [VPN Service (since 3.0)](../api/mobile/latest/group__CAPI__NETWORK__VPN__SERVICE__MODULE.html) | Manages Virtual Private Network (VPN) connections between 2 VPN devices. | [VPN Connections](connectivity/vpn.md) |
  | [Wi-Fi](../api/mobile/latest/group__CAPI__NETWORK__WIFI__PACKAGE.html) | Manages Wi-Fi connections and monitors the state of Wi-Fi connections. | [Wi-Fi](connectivity/wifi.md) |
  | [Wi-Fi Direct](../api/mobile/latest/group__CAPI__NETWORK__WIFI__DIRECT__MODULE.html) | Manages the settings of Wi-Fi Direct&reg; This submodule API also provides functions to connect and disconnect remote devices that use Wi-Fi Direct. | [Wi-Fi Direct](connectivity/wifi-direct.md) |

- [Security](../api/mobile/latest/group__CAPI__SECURITY__FRAMEWORK.html)

  The Security API module contains submodule APIs which provide basic cryptographic functions, various utility functions through the OpenSSL open source library, and a secure password-protected repository for keys, certificates, and sensitive data.

  | API submodule              | Functionality              | Guide               |
  |----------------------------|----------------------------|---------------------|
  | [CSR (since 3.0)](../api/mobile/latest/group__CAPI__CSR__FRAMEWORK__MODULE.html) | Provides the Content Screening Service to scan the content for data, files, and directories, and the Web Protection Service to protect a device by checking whether a URL the user wants to access is risky. | [CSR](security/csr.md) |
  | [Device Policy Manager (since 3.0)](../api/mobile/latest/group__CAPI__SECURITY__DPM__MODULE.html) | Provides functions to create security-aware applications that are useful in enterprise settings. | [Device Policy Manager](security/dpm.md) |
  | [Key Manager](../api/mobile/latest/group__CAPI__KEY__MANAGER__MODULE.html) | Provides functions to store keys, certificates, and sensitive data related to users and their password-protected applications in a secure repository. It also provides cryptographic operations to prevent key value names from being revealed to clients. | [Key Manager](security/secure-key.md) |
  | [OpenSSL](../api/mobile/latest/group__OPENSRC__OPENSSL__FRAMEWORK.html) | Provides an open source library that provides basic cryptographic functions and various utility functions. | |
  | [Privacy Privilege Manager (since 4.0)](../api/mobile/latest/group__CAPI__PRIVACY__PRIVILEGE__MANAGER__MODULE.html) | Provides functions for retrieving and determining an application's permissions for privacy privileges. | [Privacy Privilege Manager](security/privacy-related-permissions.md) |
  | [Privilege Info](../api/mobile/latest/group__CAPI__SECURITY__FRAMEWORK__PRIVILEGE__INFO__MODULE.html) | Retrieves and displays privilege information. This can be used to show a user the privileges that an application contains when they are downloading it onto their device. This is so that they are aware of the resources which the application may access. | [Privilege Information](security/privilege.md) |
  | [Trusted Execution Framework (since 4.0)](../api/mobile/latest/group__CAPI__TEF__MODULE.html) | Provides the TEE Client API as defined by the GlobalPlatform TEE standard for connecting to applications executed in the TrustZone. | |
  | [YACA (since 3.0)](../api/mobile/latest/group__CAPI__YACA__MODULE.html) | Provides cryptographic functions, such as key management, data integrity, data encryption and decryption, and low-level RSA operations. | [YACA](security/yaca.md) |

- [Social](../api/mobile/latest/group__CAPI__SOCIAL__FRAMEWORK.html)

  The Social API module contains submodule APIs to manage personal data, such as contacts and calendars, on a device.

  | API submodule              | Functionality              | Guide               |
  |----------------------------|----------------------------|---------------------|
  | [Calendar](../api/mobile/latest/group__CAPI__SOCIAL__CALENDAR__SVC__MODULE.html) | Manages calendars, including events and tasks. It also stores and queries calendar information. | [Calendar](personal/calendar.md) |
  | [Contacts](../api/mobile/latest/group__CAPI__SOCIAL__CONTACTS__SVC__MODULE.html) | Manages phone contact information, such as address books, persons, and phone logs. | [Contacts](personal/contacts.md) |
  | [Phonenumber utils (since 2.4)](../api/mobile/latest/group__CAPI__TELEPHONY__PHONE__NUMBER__UTILS__MODULE.html) | Provides functions for parsing and formatting phone numbers. | [Phone Number Management](internationalization/phonenumber.md) |

- [System](../api/mobile/latest/group__CAPI__SYSTEM__FRAMEWORK.html)

  The System API module contains submodule APIs for system management.

  | API submodule              | Functionality              | Guide               |
  |----------------------------|----------------------------|---------------------|
  | [Device](../api/mobile/latest/group__CAPI__SYSTEM__DEVICE__MODULE.html) | Controls devices and monitors their status. For example, this submodule API can be used to control and monitor the device battery, display, and LED. | [System Information](device/system.md) |
  | [Feedback (since 2.4)](../api/mobile/latest/group__CAPI__SYSTEM__FEEDBACK__MODULE.html) | Provides functions to play sound or vibration associated with properties. | [Feedback](device/feedback.md) |
  | [Media key](../api/mobile/latest/group__CAPI__SYSTEM__MEDIA__KEY__MODULE.html) | Provides functions to handle media keys from external devices that are connected to the Tizen device, such as the volume control buttons on a headset. |[Media Key](multimedia/media-key.md) |
  | [Runtime information](../api/mobile/latest/group__CAPI__SYSTEM__RUNTIME__INFO__MODULE.html) | Obtains runtime information from a mobile device. For example, this submodule API can obtain information about the device's GPS. | [Runtime Information](device/runtime.md) |
  | [Sensor](../api/mobile/latest/group__CAPI__SYSTEM__SENSOR__MODULE.html) | Starts and stops sensors and receives sensor data. | [Device Sensors](location-sensors/device-sensors.md) |
  | [Storage](../api/mobile/latest/group__CAPI__SYSTEM__STORAGE__MODULE.html) | Obtains storage information, such as root directory, storage type (internal or external), storage status, and total available space size. | [Data Storage](data/data-storages.md) |
  | [System Information](../api/mobile/latest/group__CAPI__SYSTEM__SYSTEM__INFO__MODULE.html) | Obtains information about the device, such as the platform and API version, device model, supported device features, and screen dimensions. | [System Information](device/system.md) |
  | [System Settings](../api/mobile/latest/group__CAPI__SYSTEM__SYSTEM__SETTINGS__MODULE.html) | Manages system settings, such as the lock screen settings. | [System Settings](device/settings.md) |
  | [T-trace (since 2.4)](../api/mobile/latest/group__CAPI__SYSTEM__TRACE__MODULE.html) | Provides functions for writing trace messages to the system trace buffer. | [Tracepoints](performance/tracepoints.md) |
  | [USB Host (since 3.0)](../api/mobile/latest/group__CAPI__USB__HOST__MODULE.html) | Provides direct access to USB devices to communicate with connected devices. | [USB Host](connectivity/usb-host.md) |
  | [dlog](../api/mobile/latest/group__CAPI__SYSTEM__DLOG.html) | Sends log output and filters log messages from the dlog logging service. | |

- [Telephony](../api/mobile/latest/group__CAPI__TELEPHONY__FRAMEWORK.html)

  The Telephony API module contains a submodule API to enable an application to access the telephony capabilities of the device, such as the call facility (call information and status), the network query services, and the SIM module.

  | API submodule              | Functionality              | Guide               |
  |----------------------------|----------------------------|---------------------|
  | [Telephony Information](../api/mobile/latest/group__CAPI__TELEPHONY__INFORMATION.html) | Obtains call, network, and SIM information. | [Telephony](connectivity/telephony.md) |

- [UI](../api/mobile/latest/group__CAPI__UI__FRAMEWORK.html)

  The UI API module contains submodule APIs and open source libraries for 2D and 3D graphics and text.

  | API submodule              | Functionality              | Guide               |
  |----------------------------|----------------------------|---------------------|
  | [Cairo](../api/mobile/latest/group__OPENSRC__CAIRO__FRAMEWORK.html) | Provides a library for 2D vector graphics drawing. Vector graphics are advantageous because they have small file sizes and can be scaled to any size without any loss of image quality. Cairo EvasGL APIs have been newly added since 2.3.1. | [Cairo](graphics/cairo.md) |
  | [Clipboard History Manager (since 3.0)](../api/mobile/latest/group__CAPI__CBHM__MODULE.html) | Provides copy and paste functionalities for applications. | |
  | [DALi](../api/mobile/latest/group__dali.html) | Provides a cross-platform 3D UI Toolkit for embedded systems. | [DALi](ui/dali/index.md) |
  | [EFL](../api/mobile/latest/group__EFL.html) | Provides a collection of libraries that are independent and can be built on top of each other to provide useful features that complement the existing environment. | [EFL](ui/efl/index.md) |
  | [EFL UTIL](../api/mobile/latest/group__CAPI__EFL__UTIL__MODULE.html) | Gets and sets the priority order of notification windows. | [EFL Utilities](ui/efl/efl-util.md) |
  | [EFL Extension (since 2.3.1)](../api/mobile/latest/group__CAPI__EFL__EXTENSION__MODULE.html) | Enhances the EFL libraries and includes device-specific features (such as support for the hardware Back key). | [Managing Rotary Events](ui/efl/rotary-events.md) |
  | [External Output Manager (since 2.4)](../api/mobile/latest/group__CAPI__UI__EOM__MODULE.html) | Provides functions for external outputs. | |
  | [Fontconfig](../api/mobile/latest/group__OPENSRC__FONTCONFIG__FRAMEWORK.html) and [Freetype](../api/mobile/latest/group__OPENSRC__FREETYPE__FRAMEWORK.html) | Provides a text rendering library and font-handling library to let applications find a font or closely matching font. | |
  | [HarfBuzz (since 2.4)](../api/mobile/latest/group__OPENSRC__HARFBUZZ__FRAMEWORK.html) | Provides functions for text shaping.  | |
  | [Minicontrol (since 2.4)](../api/mobile/latest/group__MINICONTROL__LIBRARY.html) | Provides functions for creating and displaying an EFL socket window. | [Minicontrol Window](notification/minicontrol.md) |
  | [OpenGL ES (since 4.0)](../api/mobile/latest/group__OPENSRC__OPENGLES__FRAMEWORK.html) | Provides a library for rendering 3D and 2D graphics in embedded systems. | [OpenGL ES](graphics/opengl.md) |
  | [SDL (since 3.0)](../api/mobile/latest/group__OPENSRC__SDL__FRAMEWORK.html) | Provides a low level hardware abstraction layer to computer multimedia hardware components. It manages video, audio, input devices, threads, and timers. | [SDL](graphics/sdl.md) |
  | [TBM Surface](../api/mobile/latest/group__CAPI__UI__TBM__SURFACE__MODULE.html) | Provides functions for the graphics buffer. | [Graphic Buffer and Surface](graphics/graphic-buffer.md) |
  | [Tizen WS Shell (since 3.0)](../api/mobile/latest/group__TIZEN__WS__SHELL__MODULE.html) | Allows you to communicate with the window manager. | |
  | [UI View Manager (since 3.0)](../api/mobile/latest/group__CAPI__UI__VIEWMGR__MODULE.html) | Provides functions for application view management. | |
  | [Vulkan (since 3.0)](../api/mobile/latest/group__OPENSRC__VULKAN__FRAMEWORK.html) | Provides functions for rendering 3D and 2D graphics in embedded systems. | [Vulkan](graphics/vulkan.md) |

- [UIX](../api/mobile/latest/group__CAPI__UIX__FRAMEWORK.html)
  The UIX API module contains submodule APIs for managing sound data, such as voice commands.

  | API submodule              | Functionality              | Guide               |
  |----------------------------|----------------------------|---------------------|
  | [Input Method (since 2.4)](../api/mobile/latest/group__CAPI__UIX__INPUTMETHOD__MODULE.html) | Provides functions for starting the IME application life-cycle, for interacting with the current UI state of the IME, and getting attributes and events. | [Input Method](text-input/input-method.md) |
  | [Input Method Manager (since 2.4)](../api/mobile/latest/group__CAPI__UIX__INPUTMETHOD__MANAGER__MODULE.html) | Provides functions for launching the input method editor (IME) list and selector settings. | [Input Method](text-input/input-method.md) |
  | [STT](../api/mobile/latest/group__CAPI__UIX__STT__MODULE.html) | Provides functions to recognize speech. | [Speech-to-text](text-input/stt.md) |
  | [STT Engine (since 3.0)](../api/mobile/latest/group__CAPI__UIX__STTE__MODULE.html) | Provides functions for operating the Speech-To-Text engine. | [Text-to-speech](text-input/stt.md) |
  | [TTS](../api/mobile/latest/group__CAPI__UIX__TTS__MODULE.html) | Provides functions for synthesizing voice from text and playing synthesized sound data. | [Text-to-speech](text-input/tts.md) |
  | [TTS Engine (since 3.0)](../api/mobile/latest/group__CAPI__UIX__TTSE__MODULE.html) | Provides functions for operating the Text-To-Speech engine. | [Text-to-speech](text-input/tts.md) |
  | [Voice control (since 2.4)](../api/mobile/latest/group__CAPI__UIX__VOICE__CONTROL__MODULE.html) | Provides functions for registering commands and getting notifications when a registered command is recognized. | [Voice Control](text-input/voice-control.md) |
  | [Voice control engine (since 4.0)](../api/mobile/latest/group__CAPI__UIX__VOICE__CONTROL__ENGINE__MODULE.html) | Provides functions to operate Voice-Control Engine. | [Voice Control](text-input/voice-control-engine.md) |
  | [Voice control elementary (since 2.4)](../api/mobile/latest/group__VOICE__CONTROL__ELEMENTARY__MODULE.html) | Provides functions to control UI components through voice commands. | [Voice Control](text-input/voice-control.md) |


- [Web](../api/mobile/latest/group__CAPI__WEB__FRAMEWORK.html)

  The Web API module contains submodule APIs for browsing the Internet, tracking browsing history, downloading Web content, and manipulating JavaScript Object Notation (JSON) documents.

  | API submodule              | Functionality              |
  |----------------------------|----------------------------|
  | [Json-Glib](../api/mobile/latest/group__OPENSRC__JSONGLIB__FRAMEWORK.html) | Allows reading and parsing of JavaScript Object Notation (JSON) documents. | |
  | [WebView](../api/wearable/latest/group__WEBVIEW.html) | Displays and controls Web pages. This submodule API contains interfaces for browsing, tracking browsing history, and downloading Web content. | [Web View](connectivity/web-view.md) |

## Wearable Native API Modules

The following list describes the API modules in the wearable profile and the functionality of all their submodule APIs within that module. The list also acts as reference sources for when you are planning a new feature for your application and need a way to efficiently compare different API modules to decide which APIs to use.

> **Note**
>
> Except as noted, the wearable native APIs are available since Tizen 2.3.1. The guides for wearables are same as those for mobiles.

- [Account](../api/wearable/latest/group__CAPI__ACCOUNT__FRAMEWORK.html)

  The Account API module features include managing various account information, such as receiving sync operation notifications and obtaining an access token by using the OAuth 2.0 authorization.

  | API submodule              | Functionality              |
  |----------------------------|----------------------------|
  | [Account Manager](../api/wearable/latest/group__CAPI__ACCOUNT__MANAGER__MODULE.html) | Provides CRUD (Create, Read, Update, Delete) account management functionality. |
  | [FIDO Client (since 3.0)](../api/wearable/latest/group__CAPI__FIDO__MODULE.html) | Allows you to utilize the device's available authenticators for online service integration. | [FIDO Universal Authentication Framework](/application/dotnet/guides/personal/fido.md) |
  | [OAuth 2.0 (since 2.4)](../api/wearable/latest/group__CAPI__OAUTH2__MODULE.html) | Provides an easy way to gain an access token between a server and client. |
  | [Sync Manager (since 2.4)](../api/wearable/latest/group__CAPI__SYNC__MANAGER__MODULE.html) | Helps applications in scheduling their data sync operations. |
  | [libOAuth](../api/wearable/latest/group__OPENSRC__LIB__OAUTH__FRAMEK.html) | Provides a library for using an open standard for secure authorization. This library enables users to securely log into an account on an application by using their logon credentials from another secondary account that they can have with another account provider or application. |

- [Application Framework](../api/mobile/latest/group__CAPI__APPLICATION__FRAMEWORK.html)

  The Application Framework API contains submodule APIs for application development. The submodule APIs enable application life-cycle management, usage of functionality that is exported by other applications, and access to a user's application preferences.

  | API submodule              | Functionality              |
  |----------------------------|----------------------------|
  | [Application](../api/wearable/latest/group__CAPI__APPLICATION__MODULE.html) | Manages the application's main event loop, state change events, and basic system events, and gets information about the application. It is also used to launch other applications. |
  | [Application Manager](../api/wearable/latest/group__CAPI__APPLICATION__MANAGER__MODULE.html) | Gets information, such as the application ID and path to the shared data directory, of the current application and other installed or running applications.
  | [Badge](../api/wearable/latest/group__BADGE__MODULE.html) | Creates and removes badges on the application's home screen icon. [A badge](app-management/app-icons.md) is an image displayed on the application icon, which informs the user about notifications and events. This submodule can also be used to set and get the badge value and visibility.
  | [Bundle](../api/wearable/latest/group__CORE__LIB__BUNDLE__MODULE.html) | Provides a string-based dictionary abstract data type (ADT). A dictionary is an ordered or unordered list of key-element pairs. Keys are used to locate elements in the list. This submodule can be used to create and manage a dictionary.
  | [Data Control](../api/wearable/latest/group__CAPI__DATA__CONTROL__MODULE.html) | Exchanges data between applications by allowing an application to query the public database of another application that has opted to be a data provider.
  |  [Message Port](../api/wearable/latest/group__CAPI__MESSAGE__PORT__MODULE.html) | Sends and receives small messages between applications without interference from other applications and processes. Each message is a bundle.
  | [Notification (since 3.0)](../api/wearable/latest/group__NOTIFICATION__MODULE.html) | Creates, inserts, and updates notifications so that applications can relay information to users. Visuals, sounds, or vibrations can be used as notifications.
  | [Package Manager](../api/wearable/latest/group__CAPI__PACKAGE__MANAGER__MODULE.html) | Stores and receives information related to packages installed on the device. This is information can be, for example, the package name, path to the icon image, or the application version. It can also be used to check whether 2 package certificates match. If they match, they have been created by the same developer and can share resources securely.
  | [Service Application](../api/wearable/latest/group__CAPI__SERVICE__APP__MODULE.html) | Handles [Tizen service application](applications/service-app.md) (non-UI application) state changes and system events. It is also used to start and exit the main event loop of service applications.
  | [Watch Application](../api/wearable/latest/group__CAPI__WATCH__APP__MODULE.html) | Handles Tizen watch application state changes and system events. It is also used to start and exit the main event loop of watch applications.
  | [Widget](../api/wearable/latest/group__CAPI__WIDGET__FRAMEWORK.html) | Handles Tizen widget application state changes and system events. It is also used to start and exit the main event loop of widget applications.

- [Base](../api/wearable/latest/group__CAPI__BASE__FRAMEWORK.html)

  The Base API contains submodule APIs for internationalization support and contains various open source libraries.

  | API submodule              | Functionality              |
  |----------------------------|----------------------------|
  | [C++ Standard Library](../api/wearable/latest/group__OPENSRC__STL__GCC__FRAMEWORK.html) | Provides a standard C++ library.    |
  | [Common Error](../api/wearable/latest/group__CAPI__COMMON__ERROR.html) | Provides error codes that are common for the whole Tizen API. |
  | [Glib](../api/wearable/latest/group__OPENSRC__GLIB__FRAMEWORK.html) | Provides low-level libraries and advanced data structures, such as linked lists and hash tables, for use in application development. |
  | [Glibc](../api/wearable/latest/group__OPENSRC__GLIBC__FRAMEWORK.html) | Provides a standard C library.     |
  | [LibXML](../api/wearable/latest/group__OPENSRC__LIBXML__FRAMEWORK.html) | Used to parse XML documents, such as the [Application Manifest](../index.md#appmanifest) |
  | [Minizip](../api/wearable/latest/group__OPENSRC__MINIZIP__FRAMEWORK.html) | Provides a library to process files in the ZIP format. It can be used to zip, unzip and compress files. |
  | [OpenMP](../api/wearable/latest/group__OPENSRC__OPENMP__FRAMEWORK.html) | Supports shared memory multiprocessing. This can be used for complex tasks on multicore processors. |
  | [Sqlite](../api/wearable/latest/group__OPENSRC__SQLITE__FRAMEWORK.html) | Implements a lightweight SQL relational database. This is widely used for embedded client or local storage. |
  | [Utils > i18n](../api/wearable/latest/group__CAPI__BASE__UTILS__I18N__MODULE.html) | Provides internationalization (i18n) support, such as flexibly generating date formats and numbers, depending on the locale setting of the device. |
  | [zlib (since 3.0)](../api/wearable/latest/group__OPENSRC__ZLIB__FRAMEWORK.html) | Used for in-memory compression and decompression. |

- [Content](../api/wearable/latest/group__CAPI__CONTENT__FRAMEWORK.html)

  The Content API module contains submodule APIs for managing the most common device media data types, such as image, audio, and video files. It provides operations to search for content, search for content information stored on the device, create playlists, and access the EXIF information in an image file.

  | API submodule              | Functionality              |
  |----------------------------|----------------------------|
  | [MIME Type](../api/wearable/latest/group__CAPI__CONTENT__MIME__TYPE__MODULE.html) | Maps MIME types to file extensions and vice versa. For example, the .jpeg file extension is mapped to the image/jpeg MIME type, which is required when using other API modules, such as the AppControl API in the Application submodule API, because it operates with MIME types. |
  | [Media Content](../api/wearable/latest/group__CAPI__MEDIA__CONTENT__MODULE.html) | Connects and disconnects from the media content service. This connection is required to insert, update and remove media file information in the media content database. Common media data types, such as image, audio, and video can be managed through the database. Other queries, such as searching for content and content information and accessing EXIF information from image files, are also possible. |

- [Context](../api/wearable/latest/group__CAPI__CONTEXT__FRAMEWORK.html)

  The Context API module contains submodule APIs to detect user information, such as when a user is running with a device, and device information, such as gestures when a device is tilted.

  | API submodule              | Functionality              |
  |----------------------------|----------------------------|
  | [Activity Recognition](../api/wearable/latest/group__CAPI__CONTEXT__ACTIVITY__MODULE.html) | Detects user activities, such as walking, running, and being in a moving vehicle with a device. |
  | [Contextual History (since 4.0)](../api/wearable/latest/group__CAPI__CONTEXT__HISTORY__MODULE.html) | Allows you to query statistics and patterns derived from contextual history data. |
  | [Gesture Recognition](../api/wearable/latest/group__CAPI__CONTEXT__GESTURE__MODULE.html) | Detects user gestures on devices, such as tilt, snap, and double-tap. |

- [Location](../api/wearable/latest/group__CAPI__LOCATION__FRAMEWORK.html)

  The Location API module allows the geographical position of a device to be determined for use with location-based services.

  | API submodule              | Functionality              |
  |----------------------------|----------------------------|
  | [Location Manager](../api/wearable/latest/group__CAPI__LOCATION__MANAGER__MODULE.html) | Acquires information about the geographical location of the device. It also allows the receiving of notifications about position changes, velocity changes, and when a given geographical area is left. |
  | [Maps Service (since 2.3.2)](../api/wearable/latest/group__CAPI__MAPS__SERVICE__MODULE.html) | Provides a set of functions, helping to create map-aware applications. |

- [Messaging](../api/wearable/latest/group__CAPI__MESSAGING__FRAMEWORK.html)

  The Messaging API module contains submodule APIs which grant access to the messaging capabilities, such as SMS, MMS and email, of the device.

- [Messaging](messaging/overview.md)

  | API submodule              | Functionality              |
  |----------------------------|----------------------------|
  | [Email (since 3.0)](../api/wearable/latest/group__CAPI__MESSAGING__EMAIL__MODULE.html) | Allows composing, sending, and receiving of email messages. |
  | [Messages](../api/wearable/latest/group__CAPI__MESSAGING__MESSAGES__MODULE.html) | Allows composing, sending, and receiving of SMS, MMS, and WAP push messages. |
  | [Push](../api/wearable/latest/group__CAPI__MESSAGING__PUSH__PUBLIC__MODULE.html) | Allows receiving of push notifications from a push server. |

- [Multimedia](../api/wearable/latest/group__CAPI__MEDIA__FRAMEWORK.html)

  The Multimedia API module contains submodule APIs for easily integrating an application with audio, image, and video files. It can also be used for image editing.

  | API submodule              | Functionality              |
  |----------------------------|----------------------------|
  | [Audio I/O](../api/wearable/latest/group__CAPI__MEDIA__AUDIO__IO__MODULE.html) | Manages the system audio devices by granting access to the hardware layer of the sound card. This API must be used for tasks that require raw audio data buffers in PCM format. |
  | [Camera](../api/wearable/latest/group__CAPI__MEDIA__CAMERA__MODULE.html) | Accesses the camera preview to display photo previews, focuses images, and captures images. |
  | [Image Util](../api/wearable/latest/group__CAPI__MEDIA__IMAGE__UTIL__MODULE.html) | Encodes and decodes JPEG images. It also provides tools, such as crop, resize, and rotate, to transform images. |
  | [Media Codec](../api/wearable/latest/group__CAPI__MEDIA__CODEC__MODULE.html) | Provides interfaces for encoding and decoding audio and video data, such as AAC audio or MPEG-4 AVC video. |
  | [Media Controller (since 3.0)](../api/wearable/latest/group__CAPI__MEDIA__CONTROLLER__MODULE.html) | Provides functions for communication between the media controller server and the media controller client. |
  | [Media Demuxer (since 3.0)](../api/wearable/latest/group__CAPI__MEDIADEMUXER__MODULE.html) | Provides functions for demuxing media data. |
  | [Media Muxer (since 3.0)](../api/wearable/latest/group__CAPI__MEDIAMUXER__MODULE.html) | Provides functions for muxing media data. |
  | [Media Streamer (since 3.0)](../api/wearable/latest/group__CAPI__MEDIA__STREAMER__MODULE.html) | Provides functions for building custom pipeline for streaming media. |
  | [Media Tool](../api/wearable/latest/group__CAPI__MEDIA__TOOL__MODULE.html) | Handles audio and video packet buffers. These buffers are utilized by the other Multimedia submodule APIs. |
  | [Media Vision (since 3.0)](../api/wearable/latest/group__CAPI__MEDIA__VISION__MODULE.html) | Provides functionality for barcode detection and generation. It also provides functionality for face detection, and tracking and recognition of both images and faces. |
  | [Metadata Editor (since 3.0)](../api/wearable/latest/group__CAPI__MEDIA__METADATA__EDITOR__MODULE.html) | Provides functions for editing the metadata of several popular audio formats. |
  | [Metadata Extractor](../api/wearable/latest/group__CAPI__METADATA__EXTRACTOR__MODULE.html) | Extracts metadata information from an input media file. |
  | [OpenAL](../api/wearable/latest/group__OPENSRC__OPENAL__FRAMEWORK.html) | Renders efficiently multichannel 3D audio. |
  | [Player](../api/wearable/latest/group__CAPI__MEDIA__PLAYER__MODULE.html) | Provides functions for media playback and can be used to control media playback attributes. |
  | [Radio](../api/wearable/latest/group__CAPI__MEDIA__RADIO__MODULE.html) | Supports radio usage. This submodule API can be used for tasks, such as starting and stopping the radio and scanning for radio channels. |
  | [Recorder](../api/wearable/latest/group__CAPI__MEDIA__RECORDER__MODULE.html) | Controls the recording of multimedia content. Recording process attributes, such as setting the recording filename and file format, can also be configured with this API submodule. |
  | [Sound Manager](../api/wearable/latest/group__CAPI__MEDIA__SOUND__MANAGER__MODULE.html) | Provides functions to get and set sound parameters, such as output sound volume. Session policy, such as the handling of sound session interrupts, can also be configured with this API submodule. |
  | [Sound Pool (since 4.0)](../api/wearable/latest/group__CAPI__SOUND__POOL__MODULE.html) | Provides functions for easy sound management, such as grouping sounds in pools, handling sound stream playback operations, and controlling stream and pool states. |
  | [StreamRecorder (since 3.0)](../api/wearable/latest/group__CAPI__MEDIA__STREAMRECORDER__MODULE.html) | Provides functions to record video or audio from a buffer including a media packet. |
  | [Thumbnail Util (since 3.0)](../api/wearable/latest/group__CAPI__MEDIA__THUMBNAIL__UTIL__MODULE.html) | Provides functions for creating the thumbnail from an input media file. |
  | [Tone Player](../api/wearable/latest/group__CAPI__MEDIA__TONE__PLAYER__MODULE.html) | Plays and stops tones.         |
  | [WAV Player](../api/wearable/latest/group__CAPI__MEDIA__WAV__PLAYER__MODULE.html) | Plays and stops Waveform Audio File (WAV) format files. |
  | [libEXIF](../api/wearable/latest/group__OPENSRC__LIBEXIF__FRAMEWORK.html) | Supports an image file format that extends existing formats, such as JPEG and TIFF. Many Tizen devices have a camera and use the EXIF format, and libEXIF can be used to read and write EXIF metainformation to and from image files. |

- [Network](../api/wearable/latest/group__CAPI__NETWORK__FRAMEWORK.html)

  The Network API module contains submodule APIs, which can be used for data communication. It is responsible for managing connections, maintaining IP addresses, and connecting to the system through Bluetooth, Hypertext Transfer Protocol (HTTP), Near Field Communication (NFC), Sockets, and Wi-Fi. It also provides functions for retrieving information about a specific host from the Internet Domain Name System (DNS).

  | API submodule              | Functionality              |
  |----------------------------|----------------------------|
  | [Application Service Platform (since 4.0)](../api/wearable/latest/group__CAPI__NETWORK__ASP__MODULE.html) | Provides functions for discovery and session management using the Application Service Platform. |
  | [Bluetooth](../api/wearable/latest/group__CAPI__NETWORK__BLUETOOTH__MODULE.html) | Manages Bluetooth devices. This involves launching the Bluetooth adapter and discovering, connecting, and bonding with other Bluetooth devices. |
  | [Connection](../api/wearable/latest/group__CAPI__NETWORK__CONNECTION__MODULE.html) | Gets network connection information, such as IP address, proxy information, gateway information, connection state, and data transfer statistics. |
  | [Curl](../api/wearable/latest/group__OPENSRC__CURL__FRAMEWORK.html) | Provides a client-side URL data transfer library supporting HTTP, HTTPS, FTP, and file URIs, among many other protocols. Allows applications to perform URL-related activities without a Web browser. |
  | [DNSSD (since 3.0)](../api/wearable/latest/group__CAPI__NETWORK__DNSSD__MODULE.html) | Provides functions for network service discovery using DNSSD. |
  | [HTTP (since 3.0)](../api/wearable/latest/group__CAPI__NETWORK__HTTP__MODULE.html) | Allows you to connect to a Web server to fetch and transmit a Web resource. |
  | [IoTCon (since 3.0)](../api/wearable/latest/group__CAPI__IOT__CONNECTIVITY__MODULE.html) | Provides functions for IoT connectivity. |
  | [NFC](../api/wearable/latest/group__CAPI__NETWORK__NFC__MODULE.html) | Allows management, such as registering and deregistering event listeners, of short-range wireless near field communication (NFC). This submodule API must also be used to read, write, receive, and send NFC messages. |
  | [SSDP (since 3.0)](../api/wearable/latest/group__CAPI__NETWORK__SSDP__MODULE.html) | Provides functions for network service discovery using SSDP. |
  | [Smart Traffic Control (since 4.0)](../api/wearable/latest/group__CAPI__NETWORK__STC__MODULE.html) | Provides functions for managing and monitoring network packets. |
  | [Smartcard (since 2.3.1)](../api/wearable/latest/group__CAPI__NETWORK__SMARTCARD__MODULE.html) | Provides application communication to the SE applet functions. |
  | [Wi-Fi](../api/wearable/latest/group__CAPI__NETWORK__WIFI__PACKAGE.html) | Manages Wi-Fi connections and monitors the state of Wi-Fi connections. |

- [Security](../api/wearable/latest/group__CAPI__SECURITY__FRAMEWORK.html)

  The Security API module contains submodule APIs which provide basic cryptographic functions, various utility functions through the OpenSSL open source library, and a secure password-protected repository for keys, certificates, and sensitive data.

  | API submodule              | Functionality              |
  |----------------------------|----------------------------|
  | [CSR (since 3.0)](../api/wearable/latest/group__CAPI__CSR__FRAMEWORK__MODULE.html) | Provides the Content Screening Service to scan the content for data, files, and directories, and the Web Protection Service to protect a device by checking whether a URL the user wants to access is risky. |
  | [Device Policy Manager (since 3.0)](../api/wearable/latest/group__CAPI__SECURITY__DPM__MODULE.html) | Provides functions to create security-aware applications that are useful in enterprise settings. |
  | [Key Manager](../api/wearable/latest/group__CAPI__KEY__MANAGER__MODULE.html) | Provides functions to store keys, certificates, and sensitive data related to users and their password-protected applications in a secure repository. It also provides cryptographic operations to prevent key value names from being revealed to clients. |
  | [OpenSSL](../api/wearable/latest/group__OPENSRC__OPENSSL__FRAMEWORK.html) | Provides an open source library that provides basic cryptographic functions and various utility functions. |
  | [Privacy Privilege Manager (since 4.0)](../api/wearable/latest/group__CAPI__PRIVACY__PRIVILEGE__MANAGER__MODULE.html) | Provides functions for retrieving and determining an application's permissions for privacy privileges. |
  | [Privilege Info](../api/wearable/latest/group__CAPI__SECURITY__FRAMEWORK__PRIVILEGE__INFO__MODULE.html) | Retrieves and displays privilege information. This can be used to show a user the privileges that an application contains when they are downloading it onto their device. This is so that they are aware of the resources which the application may access. |
  | [Trusted Execution Framework (since 4.0)](../api/wearable/latest/group__CAPI__TEF__MODULE.html) | Provides the TEE Client API as defined by the GlobalPlatform TEE standard for connecting to applications executed in the TrustZone. |
  | [YACA (since 3.0)](../api/wearable/latest/group__CAPI__YACA__MODULE.html) | Provides cryptographic functions, such as key management, data integrity, data encryption and decryption, and low-level RSA operations. |

- [Social](../api/wearable/latest/group__CAPI__SOCIAL__FRAMEWORK.html)

  The Social API module contains submodule APIs to manage personal data, such as contacts and calendars, on a device.

  | API submodule              | Functionality              |
  |----------------------------|----------------------------|
  | [Calendar (since 3.0)](../api/wearable/latest/group__CAPI__SOCIAL__CALENDAR__SVC__MODULE.html) | Manages calendars, including events and tasks. It also stores and queries calendar information. |
  | [Contacts (since 3.0)](../api/wearable/latest/group__CAPI__SOCIAL__CONTACTS__SVC__MODULE.html) | Manages phone contact information, such as address books, persons, and phone logs. |
  | [Phonenumber utils (since 3.0)](../api/wearable/latest/group__CAPI__TELEPHONY__PHONE__NUMBER__UTILS__MODULE.html) | Provides functions for parsing and formatting phone numbers. |

- [System](../api/wearable/latest/group__CAPI__SYSTEM__FRAMEWORK.html)

  The System API module contains submodule APIs for system management.

  | API submodule              | Functionality              |
  |----------------------------|----------------------------|
  | [Device](../api/wearable/latest/group__CAPI__SYSTEM__DEVICE__MODULE.html) | Controls devices and monitors their status. For example, this submodule API can be used to control and monitor the device battery, display, and LED. |
  | [Feedback (since 3.0)](../api/wearable/latest/group__CAPI__SYSTEM__FEEDBACK__MODULE.html) | Provides functions to play sound or vibration associated with properties. |
  | [Media key](../api/wearable/latest/group__CAPI__SYSTEM__MEDIA__KEY__MODULE.html) | Provides functions to handle media keys from external devices that are connected to the Tizen device, such as the volume control buttons on a headset. |
  | [Runtime information](../api/wearable/latest/group__CAPI__SYSTEM__RUNTIME__INFO__MODULE.html) | Obtains runtime information from a wearable device. For example, this submodule API can obtain information about the device's GPS. |
  | [Sensor](../api/wearable/latest/group__CAPI__SYSTEM__SENSOR__MODULE.html) | Starts and stops sensors and receives sensor data. |
  | [Storage](../api/wearable/latest/group__CAPI__SYSTEM__STORAGE__MODULE.html) | Obtains storage information, such as root directory, storage type (internal or external), storage status, and total available space size. |
  | [System Information](../api/wearable/latest/group__CAPI__SYSTEM__SYSTEM__INFO__MODULE.html) | Obtains information about the device, such as the platform and API version, device model, supported device features, and screen dimensions. |
  | [System Settings](../api/wearable/latest/group__CAPI__SYSTEM__SYSTEM__SETTINGS__MODULE.html) | Manages system settings, such as the lock screen settings. |
  | [T-trace (since 3.0)](../api/wearable/latest/group__CAPI__SYSTEM__TRACE__MODULE.html) | Provides functions for writing trace messages to the system trace buffer. |
  | [dlog](../api/wearable/latest/group__CAPI__SYSTEM__DLOG.html) | Sends log output and filters log messages from the dlog logging service. |

- [Telephony](../api/wearable/latest/group__CAPI__TELEPHONY__FRAMEWORK.html)

   The Telephony API module contains a submodule API to enable an application to access the telephony capabilities of the device, such as the call facility (call information and status), the network query services, and the SIM module.

  | API submodule              | Functionality              |
  |----------------------------|----------------------------|
  | [Telephony Information](../api/wearable/latest/group__CAPI__TELEPHONY__INFORMATION.html) | Obtains call, network, and SIM information. |

- [UI](../api/wearable/latest/group__CAPI__UI__FRAMEWORK.html)

  The UI API module contains submodule APIs and open source libraries for 2D and 3D graphics and text.

  | API submodule              | Functionality              |
  |----------------------------|----------------------------|
  | [Cairo](../api/wearable/latest/group__OPENSRC__CAIRO__FRAMEWORK.html) | Provides a library for 2D vector graphics drawing. Vector graphics are advantageous because they have small file sizes and can be scaled to any size without any loss of image quality. This module also includes Cairo EvasGL APIs which have been designed to support hardware-accelerated rendering. |
  | [DALi](../api/wearable/latest/group__dali.html) | Provides a cross-platform 3D UI Toolkit for embedded systems. |
  | [EFL](../api/wearable/latest/group__EFL.html) | Provides a collection of libraries that are independent and can be built on top of each other to provide useful features that complement the existing environment. |
  | [EFL UTIL](../api/wearable/latest/group__CAPI__EFL__UTIL__MODULE.html) | Gets and sets the priority order of notification windows. |
  | [EFL Extension](../api/wearable/latest/group__CAPI__EFL__EXTENSION__MODULE.html) | Enhances the EFL libraries and includes device-specific features (such as support for rotary events). |
  | [External Output Manager (since 3.0)](../api/wearable/latest/group__CAPI__UI__EOM__MODULE.html) | Provides functions for external outputs. |
  | [Fontconfig](../api/wearable/latest/group__OPENSRC__FONTCONFIG__FRAMEWORK.html) and [Freetype](../api/wearable/latest/group__OPENSRC__FREETYPE__FRAMEWORK.html)         | Provides a text rendering library and font-handling library to let applications find a font or closely matching font. |
  | [HarfBuzz (since 3.0)](../api/wearable/latest/group__OPENSRC__HARFBUZZ__FRAMEWORK.html) | Provides functions for text shaping.  |
  | [OpenGL ES (since 4.0)](../api/wearable/latest/group__OPENSRC__OPENGLES__FRAMEWORK.html) | Provides a library for rendering 3D and 2D graphics in embedded systems. |
  | [SDL (since 3.0)](../api/wearable/latest/group__OPENSRC__SDL__FRAMEWORK.html) | Provides a low level hardware abstraction layer to computer multimedia hardware components. It manages video, audio, input devices, threads, and timers. |
  | [TBM Surface](../api/wearable/latest/group__CAPI__UI__TBM__SURFACE__MODULE.html) | Provides functions for the graphics buffer. |
  | [Tizen WS Shell (since 3.0)](../api/wearable/latest/group__TIZEN__WS__SHELL__MODULE.html) | Allows you to communicate with the window manager. |
  | [Vulkan (since 3.0)](../api/wearable/latest/group__OPENSRC__VULKAN__FRAMEWORK.html) | Provides functions for rendering 3D and 2D graphics in embedded systems. |

- [UIX](../api/wearable/latest/group__CAPI__UIX__FRAMEWORK.html)

  The UIX API module contains submodule APIs for managing sound data, such as voice commands.

  | API submodule              | Functionality              |
  |----------------------------|----------------------------|
  | [Input Method (since 3.0)](../api/wearable/latest/group__CAPI__UIX__INPUTMETHOD__MODULE.html) | Provides functions for starting the IME application life-cycle, for interacting with the current UI state of the IME, and getting attributes and events. |
  | [Input Method Manager (since 3.0)](../api/wearable/latest/group__CAPI__UIX__INPUTMETHOD__MANAGER__MODULE.html) | Provides functions for launching the input method editor (IME) list and selector settings. |
  | [STT](../api/wearable/latest/group__CAPI__UIX__STT__MODULE.html) | Provides functions to recognize speech. |
  | [STT Engine (since 3.0)](../api/wearable/latest/group__CAPI__UIX__STTE__MODULE.html) | Provides functions for operating the Speech-To-Text engine. |
  | [TTS](../api/wearable/latest/group__CAPI__UIX__TTS__MODULE.html) | Provides functions for synthesizing voice from text and playing synthesized sound data. |
  | [TTS Engine (since 3.0)](../api/wearable/latest/group__CAPI__UIX__TTSE__MODULE.html) | Provides functions for operating the Text-To-Speech engine. |
  | [Voice control (since 3.0)](../api/wearable/latest/group__CAPI__UIX__VOICE__CONTROL__MODULE.html) | Provides functions for registering commands and getting notifications when a registered command is recognized. |
  | [Voice control engine (since 4.0)](../api/wearable/latest/group__CAPI__UIX__VOICE__CONTROL__ENGINE__MODULE.html) | Provides functions to operate Voice-Control Engine. | [Voice Control](text-input/voice-control-engine.md) |
  | [Voice control elementary (since 3.0)](../api/wearable/latest/group__VOICE__CONTROL__ELEMENTARY__MODULE.html) | Provides functions to control UI components through voice commands. |

- [Web](../api/wearable/latest/group__CAPI__WEB__FRAMEWORK.html)

  The Web API module contains submodule APIs for browsing the Internet, tracking browsing history, downloading Web content, and manipulating JavaScript Object Notation (JSON) documents.

  | API submodule              | Functionality              |
  |----------------------------|----------------------------|
  | [Json-Glib](../api/wearable/latest/group__OPENSRC__JSONGLIB__FRAMEWORK.html) | Allows reading and parsing of JavaScript Object Notation (JSON) documents. |
  | [WebView](../api/wearable/latest/group__WEBVIEW.html) | Displays and controls Web pages. This submodule API contains interfaces for browsing, tracking browsing history, and downloading Web content. |


> **Note**
>
> If you have an application based on Tizen 2.3, use the [Migration Guide](migration-guide.md) to make it conform to Tizen 2.4 Application Framework APIs.


## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
