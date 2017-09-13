# Tizen 3.0 M2

Release Date: 18 Jan, 2017

The Tizen 3.0 adopts various new features such as high performance graphics, latest web technology, intensified security, and multi-user supports.

  
## Release Notes

### System (Kernel and System Framework)

**New and Changed Features**

- **Systemd/Service initialization time enhancement**
  - First service launch time has been improved by optimizing the unit/smack initialization time.
  - Service initialization time has been improved by utilizing tmpfiled.
- **Directory hierarchy enhancement and compatibility support**
  - System directory structure has been refined to support read-only directories and multi-user.
  - Hard-coded path in the source code has been removed.
  - Support for a platform default user has been added.
  - Support for 2.4 contents and application directories has been added.
- **Storage API and block module enhancement**
  - USB/SD Card external storage has been enumerated with the libstorage API.
  - Support for multiple partitions and devices has been added.
  - Block dbus connection has been separated to a special-purpose block module.
- **Device HAL upgrade**
  - Common device HAL structure has been added.
  - USB configfs is supported.Default device adaptation layer for a standard kernel interface has been added.
- **Power management enhancement**
  - Dynamic power state transition has been added.
  - Power state actor for supporting several profiles and devices has been added.
- **Debug and fail-safe handling system enhancement**
  - New kmsg and pipe log backend have been added.
  - The kmsg, pipe, android logger backends are supported.
  - Runtime watchdog functionality has been added.
  - Callstack generation based on ptrace is supported optionally to eliminate the double crash issue.
- **Feedback system enhancement**
  - Feedback daemon to support multiple patterns has been added.
  - Various patterns are supported, such as combination of duration and waiting.
- **System information enhancement**
  - GDBM backend to support a light-weight system registry to improve performance has been added.
- **Cynara-based dbus policy support through dbus-daemon**
  - Privilege-based access check has been added.
- **New APIs**
  - IR device APIs have been added.
  - USB Host APIs have been added.
  - Battery and charger status APIs have been added.
  - Detailed build information has been added.
  - CPU frequency APIs have been added.
  - Storage change event handler API has been added.
- **Major open source upgrade and changes**
  - Systemd version has been upgraded from v216 to v219.

  - Pwdutils has been replaced with shadow-utils.

  - Libfuse version has been upgraded to 2.9.6.

  - Fsck-msdos and newfs-msdos have been separated from deviced.

  - The libdbus version has been upgraded to 1.10.6.

  - In TV, the kdbus version has been upgraded to V4.

### System (Base)

**New and Changed Features**

- **Base library upgrade**
  - Address sanitizer building is supported.
  - ICU binary data file has been changed to text data file.
  - unzip has been patched for CVE-2015-7697.
  - expat version has been upgraded to 2.2.0.
    - CVE-2016-4472
  - iniparser version has been upgraded to 3.2.

- **System-settings API enhancement**
  - Functions for adding or deleting string-list type data for ringtone-list (internal json handling) has been added.
- **i18n (base-utils) API enhancement**
  - Detect host time zone function has been added.
  - Ucalendar wrapper API has been added.
  - Utmscale wrapper API has been added.
  - Ushape wrapper API has been added.
  - Ubidi wrapper API has been added.
- **Vconf-internal-keys one-branch policy adoption**
  - Type check XML scheme validation for 'type' specifier at build-time has been added.
  - 'layer' by automation has been removed.
- **tzdata-update parser plugin has been added.**
  - Support for updating tzdata at runtime by downloadable application has been added.

### Application Framework

**New and Changed Features**

- **Application**
  - New event API to keep last event data has been added.
  - Support for text input delegation has been added.
  - Several new operations have been added.
- **Application IPC**
  - Data-control data change notification API has been added.
  - Support for Data control bulk management has been added.
- **Application package installer**
  - The optional mount installation feature has been added.
  - Separate permission for users for installing global applications and user-private applications has been added. Only admin users can install global applications.
  - Support for listening for the disable/enable application event has been added.
  - New filter property for application information has been added.
- **Application launcher**
  - Application background launch mode has been added.
  - Support for color-depth for a splash screen has been added.
- **Notification**
  - Support for direct reply has been added.
  - Support for notification template has been added.
- **Widget**
  - Support for multiple widget feature has been added.
  - Widget framework has been rewritten to support multiple viewer concept.

As a common feature, multi-user support has been added.

### Graphics System

**New and Changed Features**

- **Extended Wayland protocols**
  - tws_service_screensaver_manager allows a client screensaver manager to register itself and control a user-settable period of inactivity.
  - tws_service_screensaver sets the screensaver surface, which can be shown after a user-settable period of inactivity.
  - tizen_launchscreen allows the application manager to show a default splash image of the application before displaying the application window.
  - tizen-clipboard allows the application to communicate with the system clipboard.
  - tizen-remote-surface allows a client to provide its offscreen buffer to other clients.
  - tizen_video and tizen_video_object allow a client to show video content through a hardware overlay.
  - wl_tbm_queue is extended to support selective-composite mode on the fixed-framebuffer target.
  - Tizen keyrouter allows applications to grab one or more hardware keys with a single request.
  - tizen_input_device_manager has been added to support input device identification from input events and additional axes information, such as touch pressure and size, for applications.
- **Enlightenment Wayland display server**
  - X server has been replaced with Wayland in this version.
  - Full specification of the Wayland protocol has been implemented based on Enlightenment 0.20.0.
  - Desktop features (gadget, widget, and file manager) have been removed from Enlightenment (cleanup).
  - Provides the following plug-in submodules:
    - e-mod-tizen-wm-policy controls appearance and stack of the application window.
    - e-mod-tizen-keyrouter supports hardware key grab/ungrab feature.
    - e-mod-tizen-devicemgr manages hardware device-related operations, such as DPMS, input device, output device, and video layer controls.
    - e-mod-tizen-processmgr communicates with resourced to provide changed information of the application window.
    - e-mod-tizen-wl-textinput manages virtual keyboard operations.
    - wl_desktop_shell handles the Wayland xdg-shell protocol, which supports general window operations, such as move, resize, and maximized.
    - bufferqueue handles ecore-buffer to support the sharing of the UI buffer between clients.
  - Support for launching an application in the background has been added.
  - Support for a visibility event for the splash image has been added.
  - Support for the floating mode window has been added.
  - Support for the screensaver has been added.
  - Support for the hardware compositing has been added and enabled on the both of GL and software engine.
  - Support for the system clipboard window has been added.
  - Support for sharing an offscreen buffer between clients through the tizen-remote-surface has been added.
  - Support for the buffer flush has been added. It makes it possible for a suspended application to free its window buffer.
  - wl_drm has been removed from the enlightenment core module and moved to e_comp_drm. It is responsible for initializing the ecore_drm and evas_gl_drm engine.
  - Touch cancel and visibility events to the libpepper-efl have been added.
  - To reduce memcpy time, the openmp is used for copying framebuffer contents while changing the compositing mode.
  - Support for a hardware cursor has been added. It enables the display server to improve rendering performance when moving the mouse pointer if the target supports a hardware cursor.
  - Support for setting a quickpanel handler has been added. It makes it possible for the external enlightenment module to change the behavior of the quickpanel according to the UX.
  - Wayland debugging information can be acquired with debugging tools. The following information is included:
    - Window geometries
    - Window stacks
    - Resource allocation status
    - FPS (frame per second) value
    - Wayland protocol messages with user-defined filters
    - List of input devices and related information
    - Key grab status for each hardware key
    - Keymap informationList of output devices and related information
    - List of composite objects and related information
  - Easy keymap customization
    - Keymap customization has been enabled and is easily applicable by creating a new key layout file or modifying an existing key layout file.
    - A key layout file is a text file format which includes:
      - Definition of keynames and mapping between a keyname and a keycode
      - Repeat configuration and privilege check Boolean values for each key
  - Prebuilt keymap cache support
  - One or more keymap caches can be generated at build time and installed.
  - There is no need to compile a keymap at boot time and runtime by using existing keymap caches.
  - Each type of input device or each input event can be blocked by the client request only when the client has the proper privilege for the request.
  - A cancellation event can be created and sent to the current touch surface when one of the following events takes place:
    - Window stack changes
    - LCD/display is switched off
    - Touch gesture is recognized
  - Input device/event block/unblock support
  - Touch event cancellation
  - Input device identification support
    - Source input device information can be acquired from an input event, such as Ecore or Evas event, in an application.
    - Information includes the name, description, and device type of the source input device.
  - Keygrab support with an array of keys
  - Series of key grab requests can be created and sent for multiple keys in a window surface with a single API call.
  - The request for generating mouse input events on the server side can be created only when the client has the proper privilege for the request.
  - Mouse input event generation API supportAdditional input device axes support for touchscreenAxes information can be acquired from an input event, such as Ecore or Evas event, in an application.
  - Axes information includes the pressure, angle, and radius of each contacting finger on the touchscreen.
  - Key Event RepeatServer informs clients about the keyboard's repeat_info (rate/delay).
  - Generating repeated key events would be done in the client side.
- **libpepper-efl**
  - libpepper-efl has been released.
  - libpepper-efl is a lightweight and flexible library for developing EFL host applications, which support the embedded Wayland compositor.
- **Tizen ws shell**
    - API to support controlling of the quickpanel service window has been added.
- **efl-util**
  - API to support controlling of the screen brightness through the application window has been added.
  - Behavior of the following APIs has been changed to support synchronous manner:
    - efl_util_set_notification_window_level()
    - efl_util_set_window_screen_mode()
  - Following APIs have been deprecated:
    - efl_util_set_notification_window_level_error_cb()
    - efl_util_unset_notification_window_level_error_cb()
    - efl_util_set_window_screen_mode_error_cb()
    - efl_util_unset_window_screen_mode_error_cb()
- **Tizen HAL**
  - Tizen display HAL
    - TDM (Tizen Display Manager) support has been added.
    - Reference implementation of Exynos and Sprd tdm backend has been provided.
    - Tizen buffer HALTBM (Tizen Buffer Manager) version 2.0 is supported:
      - The tbm_surface_queue has been provided.
      - TGL has been removed at the frontend.
      - Backend deals with the authentication of the buffer manager device, such as a DRM kernel module.
      - Reference implementation of Exynos and Sprd tbm backend has been provided.
      - Backend interface has been changed.
    - Tizen EGL porting layer
      - TPL-EGL 1.0 support has been added.
      - TPL (Tizen Porting Layer) is an abstraction layer for surface and buffer management on the Tizen platform, aimed to implement the EGL porting layer of the OpenGLES driver over various display protocols.
      - Supported EGL backends:
          - Wayland, gbm, tbm
      - Buffer management and Wayland protocol of Vulkan WSI Tizen are supported.
      - Emulator GL Driver (emulator-yagl) supports the libtpl-egl backend.
- **Vulkan WSI Tizen**
  - Vulkan WSI (Window System Integration) Layer for Tizen.
  - It wraps vendor¡¯s Vulkan ICDs and provides the WSI (Window-System Interface) for Tizen.
  - The VK_KHR_wayland_surface is supported.
- **CoreGL**
  - CoreGL is an injection layer of OpenGL ES.
  - CoreGL provides the following capabilities:
    - Support for driver-independent optimization (FastPath)
    - EGL/OpenGL ES debugging
    - Performance logging
  - Supported versions:
    - EGL 1.4OpenGL ES 1.1, 2.0, 3.0, 3.1, 3.2
  - Provides OpenGLES/EGL development headers.
    - Khronos OpenGLES/EGL headers (Khronos released on Oct 24 2016)
- **DALi (3D UI Toolkit) Enhancement**
  - Wearable profile support has been added.
     - Wearable watch application template has been added.
  - Image
    - Support for image formats have been added (N-patch image, ASTC native compressed image).
    - Support for texture wrapping modes have been added.
    - Support for image fitting modes have been added.
    - Support for PixelArea and pre-multiplied alpha in ImageView have been added.
  - Text
    - TextEditor for multi-line and multi-language edition has been added.
    - Support for markup processing in TextField has been added.
    - Support for auto scrolling in TextLabel has been added.
    - ControlStyleManager has been added.
    - FlexContainer has been added.
    - Slider has been added.
    - VideoView has been added.
    - Model3dView control for full 3d model rendering support has been added.
    - PageTurn control for the page turn function rendering support has been added.
    - Support for child property registration has been added.
    - Support for control background rendering without creating an extra actor has been added.
  - 3D rendering and animation
    - Wayland rendering backend has been added.
    - Renderer API and Visual properties for low-level control including culling, blending, depth, and stencil testing have been added.
    - Support for setting the animation loop count has been added.
    - Support for getting the animation state has been added.
    - Support for the REQUIRES_SYNC property to enable and disable GL sync in RenderTask has been added.
    - Support for ostream writers have been added.
- **SDL 2.0 (Simple DirectMedia Layer)**
  - Tizen Backend
    - Support for Tizen App life-cycle management has been added.
    - Support for Tizen App Core Event has been added.
    - Support for touch and key Event has been added.
    - Support for window system based on Ecore_Wl has been added.
    - Support for input with Tizen ISF has been added.
    - Support for dlog has been added.
    - Support for cursor has been added.
  - Additional functions
    - Support for SDL timer with vblank has been added.
    - Support for rotation has been added.
  - Vulkan
    - Support for using Vulkan directly (without wrapper) has been added.
    - Support for using WSI wrapper functions to avoid window system dependency has been added.
    - Support for avoid window system dependency in SDL has been added.
- **Evas Render Engine Enhancement**
  - Evas GL
    - Support for OpenGL ES 3.1 has been added.
  - Optimization texture uploading
    - To avoid COW case, texture uploading optimization has been added.
  - Runtime shading
    - Downstream runtime shading has been added.
  - Offscreen Backend
    - Evas TBM surface SW/GL backends have been added.
    - Ecore-Evas TBM surface SW/GL modules have been added.
  - Native Surface Set
    - Support for wl_buffer for Evas GL_DRM/wayland backend has been added.
  - Wayland-shm with TBM
    - Support for TBM surface in Evas wayland-shm backend has been added.
- **Open source upgrade**
  - Wayland version has been upgraded to 1.8.0.
  - Enlightenment version has been upgraded to 0.20.0.
  - Cairo version has been upgraded from 1.12.14 to 1.14.2.
  - Vulkan-LoaderAndValidationLayers version has been upgraded to 1.0.29
  - SDL 2.0.4 has been added.

**Fixes**

- Fixed the copy and paste operation failure caused by the broken pipe on the server side.
- Fixed the first screen resizing during the application launch.
- The root cause was a lack of synchronization between EFL and Wayland for the first scene drawing.
- Fixed the IME rotation problem, which was caused by a lack of synchronization between the display server and client for the window rotation.
- Fixed the server-side handler for the ping-pong protocol which was not working properly.

**Known Issues**

- DALi control vibration is not supported.

- SDL indicator is not fully verified.

### UI Framework

**New and Changed Features**

- **EFL Upgrade (from 1.13 to 1.16)**
  - Wayland-backed is enabled.
  - efl-misc replaces elm-misc.
  - efl-modules replaces elm-modules.
  - e17-extra-config-modules is removed.
  - A new efl-config daemon configures scalable UI setting at boot time.
  - Notify style name of popup has been changed (popup a popup/default).
  - The default scroller of popup has been removed. (The application must call the elm_popup_scrollable_set(popup, EINA_TRUE) function.)
  - Item style of ctxpopup has been changed. (Use the list item rather than box.)
  - The minimum size of a genlist item is not defined. (If necessary, the application must specify the minimum size of the genlist item by itself.)
  - In mobile, the default theme is refined.
  - In mobile, LazEDC and color class have been applied to default theme.
  - EDC support for SVG files has been added.
  - EFL vector support GL backend as well as SW backend have been added
- In mobile, CBHM (ClipBoard History Manager) has been integrated.
- In mobile, view manager has been added.
- Customization APIs have been added.
- **Text Input**
  - Input framework has been changed from X-based to Wayland-based.
  - In mobile, 3 new input languages have been added (Irish, Uzbek and Hindi).
    The supported languages are:
    Azerbaijani, Bulgarian, Catalan, Czech, Danish, Greek, German, English (US), Spanish, Estonian, Basque, Finnish, French, Irish, Galician, Croatian, Hungarian, Armenian, Icelandic, Italian, Japanese, Georgian, Kazakh, Korean, Lithuanian, Latvian, Macedonian, Norwegian, Dutch, Polish, Portuguese, Romanian, Russian, Slovak, Slovenian, Serbian, Swedish, Turkish, Ukrainian, Uzbek, Chinese, Chinese (Hong Kong), Chinese (Taiwan), Hindi, and Albanian
    The scim-launcher process has been integrated to scim-helper-launcher process.
    In wearable, the input delegator window has been added.
    Synchronous get_surrounding_text() API support has been added.
- **Voice Interaction**
  - Speech To Text feature is enabled.
  - The server based Speech To Text engine is included as a default engine.
  - Support for a 3rd party Speech To Text / Text To Speech engine has been added..
  - Support the voice control framework has been added.
  - The supported languages of the TTS engine have been extended to 28 languages.
    The supported languages are:
      English (US), English (UK), English (India), Korean, Spanish, Mexican Spanish, French, German, Italian, Russian, Brazilian Portuguese, Portugal Portuguese, Chinese, Chinese (Hong Kong), Chinese (Taiwan), Japanese, Hindi, Czech, Dutch, Danish, Finnish, Greek, Hungarian, Norwegian, Polish, Slovak, Swedish, and Turkish

**Fixes**

- Many bugs have been resolved.

**Known Issues**

- **EFL**
  - EFL abort on errors are enabled by default.
  - Joystick does not work temporarily.
- **Accessibility**
  - ScreenReader functionality has not been fully tested.
- **Clipboard**
  - CBHM (ClipBoard History Manager) has not been fully tested.
- **View manager**
  - View manager has not been fully tested.
- **Customization API**
  - In wearable, the theme is not ready for customization.
- Focused UI has not been fully tested.
- UI mirroring has not been fully tested.
- Tizen 3.0 UX has not been fully implemented, especially for visual interactions.

### Multimedia Framework

**New and Changed Features**

- **Opensource upgrade**
  - GStreamer has been upgraded from 1.4.5 to 1.6.1.
  - Pulseaudio has been upgraded from 4.0 to 5.0.
  - Alsa-lib has been upgraded from 1.0.25 to 1.0.28.
  - OpenAL has been upgraded from 1.13 to 1.17.2.
  - libsndfile has been upgraded from 1.0.25 to 1.0.26.
  - libjpeg-turbo has been upgraded from 1.3.1 to 1.4.2.
  - libpng has been upgraded from 1.6.13 to 1.6.21.
  - giflib has been upgraded from 4.1.6 to 5.1.2.
  - tiff has been upgraded from 4.0.3 to 4.0.6.
- **Player**
  - Internal method has been changed to provide a player service from library to server-client.
  - Module to set the sound policy has been changed
    - Most interrupt callback code has been deprecated, except for the resource conflict.
    - Setting the sound type API has been deprecated.
    - API to set the sound stream info has been added.
  - Error code (PLAYER_ERROR_BUFFER_SPACE) for the data push API has been added.
  - Default buffering storage has been changed from file to memory.
  - The performance has been optimized by removing unnecessary IPC when rendering video.
  - New API to set region of interest area of display has been added.
  - The player_completed_cb(), player_error_cb(), and player_prepared_cb() functions have been made to invoke by default context.
  - New error return value of player_create() API and display related APIs have been added.
  - In wearable, Evas display type has been added.
- **Radio (in mobile and wearable)**
  - API to set or get the volume has been added.
  - Pre-state of radio_scan_start() API has been changed.
- **Media tool**
  - APIs to support container type have been added.
  - API to get a flag about the buffer stream information has been added.
  - API to set the video frame rate has been added.
  - API to get the video frame rate has been added.
  - New media packet pool APIs to reuse allocated media packets have been added.
- **Media codec**
  - API to get media packet pool has been added.
- **Media streamer**
  - Another player service type to allow the user to design a player structure according to their requirements has been added.
- **Media demuxer**
  - Demuxing service of a multiplexed media stream has been added.
- **Media muxer**
  - Muxing service to create audio/video content with a given type of container format has been added.
- **Audio**
  - API to free the device list has been added.
  - New API to manage audio stream focus has been added.
  - New API to manage stream based routing has been added.
  - New API to manage audio devices has been added.
  - Old Session/Routing API has been deprecated.
  - New enumeration to support Bluetooth SCO has been added.
  - New feature to support power-off mute control has been added.
  - New feature to support transfer Bluetooth property (wideband, nrec) has been added.
  - New API to query current media playback device has been added.
  - New API to query whether stream is connected to specific device has been added.
  - New feature to support auto-last-connected device policy has been added.
  - New feature to support fading audio in pulseaudio has been added.
  - New feature to protect infinite power consumption caused by improper use of audio APIs has been added.
  - Sound-Server has been changed to operate as an on-demand process.
  - In TV, a new feature to support vconf in pulseaudio has been added.
  - In TV, a new feature to use of tizen-audio-sink/source has been added.
- **Camera**
  - Internal method has been changed to provide a camera service from library to server-client.
  - Error enums for the sound policy have been deprecated.
  - Error enums for the resource conflict has been added.
  - API to get the flash state set by the Camera API has been added.
  - API to get the facing direction has been added.
  - APIs for the encoded preview format (H.264) have been added.
  - APIs to set and get pan have been added.
  - APIs to set and get tilt have been added.
  - APIs to set and get display ROI (Region Of Interest) area have been added.
- **Recorder**
  - Internal method has been changed to provide a recorder service from library to server-client.
  - Error enums for the sound policy have been deprecated.
  - Error enums for the resource conflict has been added.
  - API to set the sound stream information has been added.
  - New file format (MPEG2TS) has been added.
  - New audio codec (MP3) has been added.
- **Media content**
  - Multi-user support has been added.
  - New information for detecting and tracking faces on images with media vision has been added.
  - The getter API return values have been modified from "Unknown" to an empty string (""):
      - Title, description, album, artist, album_artist, genre, composer, year, copyright, track_num
  - The get thumbnail path API return value has been modified from a default thumbnail path to an empty string ("").
  - Thumbnail creation policy has been modified. It is not extracted automatically by the framework. The application must request thumbnail creation if the thumbnail is needed.
  - New API to start and cancel face detection for media has been added.
  - New API to get 360 content for image and mp4 files has been added.
- **Media controller**
  - Multi-user support has been added.
- **Image util**
  - PNG, GIF, BMP encoding/decoding support has been added.
  - JPEG encoding/decoding has been modified to use a handle.
  - JPEG encoding/decoding APIs have been deprecated.
- **Thumbnail util**
  - http://tizen.org/privilege/content.write privilege has been removed.
- **Metadata extractor**
  - New attribute enums have been added.
  - Audio codec, video codec, and 360 attributes have been added.
- **Screen mirroring**
  - Support for transfer data streaming of the source device has been added.
- **Mediavision**
  - Face detection, recognition, and tracking have been added.
  - Image detection, recognition, and tracking have been added.
  - Surveillance has been added.

**Fixes**

-  Many bugs have been fixed.

### Network and Connectivity

**New and Changed Features**

- **Data network**
 - In mobile and wearable, SoftAP (Software enabled Access Point) has been added.
 - In mobile, wearable, and TV, the WiFi Manager API has been added to support multi-instance in applications.
 - In mobile and TV, the default VPN to build up the VPN default setting has been added.
 - In mobile, wearable, and TV, NSD (Network Service Discovery) has been added.
 - In mobile, the additional AP router function (such as port forwarding, 802.11 mode/channel, and dhcp range) to the tethering module has been added.
 - In mobile and wearable, APIs for HTTP to the curl wrapper have been added.
 - In mobile, the Wi-Fi TDLS (Tunneled Direct Link Setup) has been added.
 - In mobile, the tethering configuration has been added.
 - In mobile and TV, the VPN service to build up a VPN client has been added.
 - In mobile and wearable, the additional connection type to handle a gadget connection has been added.
 - In mobile and TV, IPC of the wifi direct manager has been changed from socket to d-bus.
 - In mobile and wearable, the privilege for the wifi_ap_create() function has been removed.
 - In mobile and TV, API for wifi-direct to the wifi-direct peer signal strength has been added.
 - In mobile and TV, APIs for connection to get/set cellular pdn type have been added.
 - In mobile and wearable, the HTTP uploading file/cancel API have been added.
- **Connectivity**
  - MTP initiator has been added.
  - MTP initiator APIs are provided.
  - In mobile and wearable, the NFC preferred app has been added.
  - In mobile and wearable, the NFC internal API for HCE operation and the pkgmgr-plugin-nfc package has been added.
  - In mobile and wearable, the NFC appcontrol operations have been modified for the Tap&Pay menu.
  - In mobile and wearable, the NFC client library has been merged to the CAPI layer because of a smack issue.
  - BLE GATT server behavior has been improved.
  - BLE GATT server API has been added.
  - BLE GATT server API, write request has been modified for the respose_needed option.In TV, the BLE IPSP function is supported.
- **IoTCon**
  - IoTCon has been newly added to support iotivity 1.2.1.
  - IoTivity Security has been enabled.
  - Provides APIs for registration and finding the resources.
  - Provides APIs for request and responses for the resources.Provides APIs for resource observation and presence.
- **Telephony**
  - In mobile and wearable, the CDMA/LTE network info getter API has been added.
  - In mobile and wearable, the lac/cell ID network API privilege has been changed.
  - In mobile, the do not disturb feature is supported.
- **Major open source upgrade and change**
  - Curl has been upgraded from 7.40 to 7.50.2 for stability.
  - Dnsmasq has been upgraded from 2.57 to 2.74 stability.
  - wpa_supplicant has been upgraded from 2.4 to 2.5 for the d-bus interface.
  - libidn has been upgraded from 1.15 to 1.16 for stability.
  - Libcap has been upgraded from 2.21 to 2.24 for stability.
  - Gnutls has been upgraded from 3.3.5 to 3.4.11 for stability.
  - Gssdp has been upgraded from 0.8.2 to 0.14.4 for stability.
  - Gupnp has been upgraded from 0.14.1 to 0.20.4 for stability.
  - Iproute2 has been upgraded from 3.4.0 to 3.9.0 for stability
  - Nghttp2 has been upgraded from 0.7.3 to 1.0.0 for stability.
  - libmtp has been upgraded from 1.1.9 to 1.1.11 for stability.

**Fixes**

- BLE GATT privilege handling has been fixed.

- In mobile and wearable, the memory leak on the NFC/Smartcard daemon has been fixed.

- Memory leak on the wifi-direct manager and popup has been fixed.

- Memory leak on the net-config and mobileap-agent has been fixed.

- Memory leak on the bt-agent and bt-service has been fixed.

- TLS session cache operation has been fixed to handle TLS resumption.

- Chained certificate verification has been fixed to handle intermediate CA list.

- UID/GID of MTP Initiator has been changed from system to network_fw.

- MTP Initiator critical section issues have been fixed.

### Security

**New and Changed Features**

- **Access control**
  - The smack usage has been changed for maintainability.
    - From many domains to 3 domains
  - The security-manager package has been added.
    - When an application installs, smack labels and rules are added.
    - When an application installs, the application is added into a proper group if needed.
  - The libprivilege-control package has been removed.
    - Functionalities have been moved to security-manager.
  - The security-server package has been removed.
    - Functionalities have been moved to security-manager and cynara.
  - Support application shared directory for backward compatibility.
  - Support application private sharing APIs for backward compatibility.
  - All smack rules generated by security-manager are merged to one file to improve performance of smack rule loading.
  - libnss_securitymanager has been implemented.
    - Insert the user session daemon into proper groups.
  - Make new smack domain, User::Shell.
    - For protecting system resources from sdb shell, restrict permission of sdb shell
  - In mobile and wearable, the smack onlycap feature has been enabled.
    - Make new smack domain, System::Privileged.
    - Only a process with the System::Privileged label can have CAP_MAC_ADMIN and CAP_MAC_OVERRIDE.
  - In mobile and wearable, platform upgrade functionalities are supported.
    - The user/global application list is moved to /opt/var.
  - In TV, the 'internet' privilege is not checked.
- **Application privilege**
  - The cynara package has been added.
    - When an application requests a service, it checks whether an application has a proper privilege.
  - Web privilege management method has been changed.
    - Mapping to core privilege internally.
  - Divide Cynara package into 3 sub packages to avoid build dependency.
  - Cynara monitor APIs have been added.
    - Used for gathering privacy usage information.
  - In mobile and wearable, add privacy setting application.
    - If user does not want specific privilege of an application, they can enable/disable them.
  - In mobile and wearable, add user confirmation step when using application.
    - If an application use privacy-related privilege, user confirmation must be needed.
  - In TV, the GetConnectionCredentials method in gdbus helpers is used for kdbus support.
- **Privilege list**
  - In mobile, the following privileges have been added:
    - Native
      - antivirus.admin / antivirus.scan / antivirus.webprotect / appdir.sharedata / d2d.datasharing / dpm.bluetooth / dpm.browser / dpm.camera / dpm.clipboard / dpm.debugging / dpm.email / dpm.location / dpm.lock / dpm.message / dpm.microphone / dpm.password / dpm.security / dpm.storage / dpm.usb / dpm.wifi / dpm.wipe / dpm.zone / fido.client / location.coarse / use_ir / vpnservice
    - Web
      - d2d.datasharing / widget.viewer
  - In mobile, the following privileges have been deprecated:
    - Native
      - keymanager / minicontrol.provider
  - In wearable, the following privileges have been added:
    - Native
      - account.read / account.write / antivirus.admin / antivirus.scan / antivirus.webprotect / appdir.shareddata / appmanager.kill.bgapp / calendar.read / calendar.write / contact.read / contact.write / d2d.datasharing / dpm.bluetooth / dpm.browser / dpm.camera / dpm.clipboard / dpm.debugging / dpm.email / dpm.location / dpm.lock / dpm.message / dpm.microphone / dpm.password / dpm.security / dpm.storage / dpm.usb / dpm.wifi / dpm.wipe / dpm.zone / email / fido.client / ime / imemanager / inputgenerator / keygrab / location.coarse / mediacontroller.client / mediacontroller.server / packagemanager.clearcache / systemmonitor / use_ir
    - Web
      - bluetooth / d2d.datasharing / ime / led / mediacontroller.client / mediacontroller.server
  - In wearable, the following privileges have been deprecated:
    - Native
      - keymanager / keymanager.adminWebbluetooth.admin / bluetooth.gap / bluetooth.health / bluetooth.spp
  - In TV, the following privileges have been added:
    - Web
      - bluetooth / d2d.datasharing / volume.set
  - In TV, the following privileges have beed deprecated:
    - Web
      - keymanager
- **Root daemon minimization**
  - Convert root daemon to non-root permission to prevent potential attack.
  - Unlike system process in Tizen 2.4, separate ID following specification of each daemon.
    - Following IDs are defined in Tizen 3.0
      - app_fw / application / broadcasting / graphic / location / messaging / multimedia_fw / network_fw / scm / sdk / security_fw / sensor / service_fw / social / system_fw / telephony / testing / ui_fw / web_fw
      - Define system_share for group ID to allow access between each daemon.
    - Until now, 50+ daemons are changed from root to non-root ID.
    - Root daemon minimization process is in progress.
- **Device policy management framework**
  - New device policy management framework and related APIs
    - In mobile and wearable, the password policy APIs have been added.
    - Restriction policy APIs have been added.
    - Security policy APIs have been added.
    - In mobile, the zone policy APIs have been added.
- **Container (in mobile)**
  - New container package:
    - New container framework has been added.
    - KeyGuard has been added.
    - Container App Launcher has been added.
    - Container Setup Wizard has been added.
- **Authentication**
  - Password Management package has been changed.
    - Password management feature has been moved from security-server (until Tizen 2.4) to auth-fw (since Tizen 3.0).
  - Public Key Pinning has been introduced.
    - Public pinning for HTTPS has been introduced in a browser and the following internal modules: oauth2, download-provider, dali-adaptor, email-service, conn-man, and chromium-efl
    - pubkey-pinning package has been added to help internal modules using HTTPS to check the validity of a server certificate with static pinning data.
  - OCSP check during the application installation
    - Certificates of an application with OCSP information are checked during the installation with OCSP.
    - In case there is no Internet connection, the installer skips the OCSP check and installs the package/application. Cert-checker performs the OCSP check for all new installed applications when the Internet connection is available.
  - tizen-security-policy package has been removed.
    - tizen-security-policy in Tizen 2.4 had app-signing root certificates.
    - App-signing root certificates have been moved to ca-certificates-tizen.
  - cert-svc
    - Pluggable step has been added on the app-signature validation. Additional signature validation step can be done by the plugin.
    - Internal APIs on the cert-service.h header file have been totally removed. The cert-svc-vcore capis fully cover them.
    - Allow additional fingerprint file (fingerprint_list_ext.xml) for application signature verification root certificates.
    - Allow internal symbolic links in application packaging.
    - Certificate blacklist for application signature verification has been added.
- **Data protection**
  - The secure-storage package has been removed.
    - Its functionality has been replaced by key-manager and libwebappenc packages.
  - Key manager
    - Hardware integration has been upgraded.
    - Encrypted initial value support has been added.
    - Symmetric key (AES key) support has been added.
    - All public APIs have been changed into non-privileged APIs.
    - The following APIs have been added:
      - APIs to handle PKCS12 files, such as ckmc_save_pkcs12 and ckmc_get_pkcs12, have been added.
      - API for certificate verification with designated trust certificates has been added.
      - API for OCSP (Online Certificate Status Protocol) has been added.
      - The kmc_set_permission() function to manage access control rules efficiently has been added.
      - The ckmc_remove_alias() function that deletes data in the database using an alias has been added.
      - Error code (CKMC_ERROR_AUTHENTICATION_FAILED) for per-row password mismatched error has been added.
      - API to create an AES key has been added.
      - APIs for encryption and decryption have been added.
      - APIs to handle cryptographic parameters have been added.
      - The following APIs have been changed:
        - Platform level privilege has been deleted from key-manager's control APIs.
        - Getting a certificate chain with aliases API has been deprecated.
      - Web app encryption
        - Web application (wgt) encryption feature is moved from secure-storage (until Tizen 2.4) to libwebappenc (since Tizen 3.0).
      - YACA (Yet Another Crypto API)
        - A new crypto API package, YACA, has been introduced in Tizen 3.0.
        - It provides application with the following stable cryptographic APIs:
          - APIs for encryption/decryption operations with symmetric keys and sealing and opening operations with asymmetric keys
          - APIs for creating and verifying a signature, calculating HMAC/CMAC and calculating a message digest
          - APIs for key handling operations such as generating, importing, and exporting a key and deriving a key from password
          - Simple APIs for cryptographic operations
          - APIs for low-level RSA operations
      - openssl upgrade
        - openssl has been upgraded to 1.0.2j.
        - The following risky SSLv2 related APIs were removed:
          - SSLv2_method ,SSLv2_client_method, SSLv2_server_method
- **Anti-virus**
  - csr-framework
    - Client-server architecture has been adopted.
    - Whole APIs have been changed into simple and easy APIs.
    - Delta scanning is supported.
    - Only embedded engine is supported (engine in the application is not supported).

### Service Framework

**New and Changed Features**

- **Location**
  - Map Service (in mobile and wearable)
    - New APIs to get metadata of places list, multiple reverse-geocodes, and alternative routes have been added.
    - New APIs to render a map image on an Evas object have been added.
    - New APIs for map objects, such as marker, polyline, and polygon, have been added.
    - New API to capture snapshots of the current map has been added.
    - Gesture detector to recognize gestures internally has been added.
    - Mapzen map provider plugin has been added.
  - Location (in mobile and wearable)
    - New APIs to get mock locations have been added.
    - New APIs to get locations in a batch have been added.
  - Geofence (in mobile)
    - New APIs to get proximity data based on geofence have been added.
- **Sensor**
  - Sensor Listener (in mobile and wearable)
    - 2 new sensor types, sleep detector and stress monitor, have been added.
  - Sensor Recorder (in mobile and wearable)
    - Recording of pedometer, heart-rate monitor, and sleep monitor is supported.
- **Context**
  - Contextual Trigger (in mobile)
    - The contextual trigger allows applications to define and publish custom context data, which can be used to compose triggering rules.
    - Update events of contacts DB can be used as events of trigger rules.
  - Contextual History (in mobile)
    - The contextual history provides statistics of per-app battery usages.
- **PIMS**
  - Contacts (in mobile and wearable)
   - In wearable, Contacts Service has been newly added.
   - API for the aggregation suggestions has been added.
   - Usage types for the contact usage statistics have been added.
   - API to reset phone log statistics by the SIM slot number has been added.
   - SIP address property of contact has been added.
   - APIs for the search snippet have been added.
   - APIs for setting the limit size of the vCard photo have been added.
   - New API for checking the initialization status in each SIM has been added. Old API has been deprecated.
   - New API for importing contacts from each SIM has been added. Old API has been deprecated.
   - Thumbnails of contact and person have been added.
   - Database mode has been changed to WAL mode.
   - Multi-user support has been added.
   - API for checking progress of SIM contact import has been added.
   - In mobile, the service running mode is changed from on-demand to always-on.
  - Calendar (in mobile)
    - IPC of the Calendar Service has been changed from PIMS-ipc to gdbus.
    - Multi-user support has been added.
    - Database mode has been changed to WAL mode.
  - Phonenumber-utils (in mobile and wearable)
      - In wearable, Phonenumber-utils has been newly added.
      - API for normalization of the phone number has been added.
      - APIs for daemonization of phonenumber-utils have been added.
- **Email and Message**
  - Email (in mobile and wearable)**
    - In wearable, Email Service has been newly added.
    - Multi-user support has been added.
    - Email sent notification has been changed, it is cleared automatically after 3 seconds.
  - Message (in mobile and wearable)
    - msg-manager package for the Multi-user support has been added.
    - API for checking change of thread list has been added.
    - APIs related v-object have been deprecated.
    - Reply on active notification feature is provided.
    - Singlepart MMS is supported.

### Web Framework

**New and Changed Features**

- **Web View API**
  - Following APIs have been added:
    - ewk_cookie_manager_file_scheme_cookies_allow_get() ewk_cookie_manager_file_scheme_cookies_allow_set() ewk_context_intercept_request_callback_set() ewk_intercept_request_url_get() ewk_intercept_request_http_method_get() ewk_intercept_request_headers_get() ewk_intercept_request_ignore() ewk_intercept_request_response_set() ewk_intercept_request_response_status_set() ewk_intercept_request_response_header_add() ewk_intercept_request_response_header_map_add() ewk_intercept_request_response_body_set() ewk_intercept_request_response_write_chunk() ewk_view_add_in_incognito_mode() ewk_view_javascript_message_handler_add() ewk_view_evaluate_javascript()
- **HTML5/W3C APIs**
 - Responsive images
   - Enable tag-based responsive image resource mapping for facilitating multi-screen Web application design and implementation.
 - Web components (template, imports)
   - User-defined Web componentService workerEnables background task/page management.
   - WebSpeech APIProvides enhanced support on Speech APIs including recognition.
   - Media Source Extensions (MSE)Allow JS to generate media streams.
   - WebRTCEnables real time communications between browsers.
   - Web cryptography API and Contents Security Policy 1.1
   - Web Push API
       - Gives Web applications the ability to receive messages pushed to them from the spp server. (Not included in the TCS)
- **Web Device API**
  - Iotcon API
      - Provides functions for IoT connectivity.
  - Preference API
      - Stores and retrieves small pieces of data which can be used for application preferences.
  - Widget Service API
      - Provides information of installed widgets.
  - Player Util API
      - Manage features related to the W3C Player.
  - Key manager
      - Provide a secure repository protected by Tizen platform for keys, certificates, and sensitive data and application data.
  - Feedback API
      - Plays sound or vibration associated with an action.

**Fixes**

- **Web Core**
  - Invalid computation (0) of screen.availableWidth and screen.availableHeight has been fixed.
  - The default encoding type for data url scheme has been modified from ascii to app specified encoding type.
  - Layout crash caused by text autosizing has been fixed.
  - The dom timer suspending while panning is working has been fixed.
  - Incremental image rendering has been switched off.
  - The db path by considering application path has been fixed
  - Always-on option for the sensor by considering the case of the screen off condition has been added.
  - The maximum size of data uri scheme data has been increased from 2MB to 6MB.
  - Tizen has been applied as a vendor for navigator.vendor.
  - A deprecated document.width and document.height implementation as a working API has been added.

### SCM

**New and Changed Features**

- **gcc**
  - Address Sanitizer is officially supported.
  - In mobile and wearable, Leak Sanitizer and UndefindBehavior Sanitizer are available to use.

**Fixes**

- **gcc**
  - An Internal Compiler Error (PR ipa/64896) issue has been fixed.
  - The plugin infrastructure have been enabled for sanitizer developments.
- **glibc**
  - libBrokenLocale.so is included to target image (dlopen fail issue FIX).
  - libtrhead_Db.so.1 is included to target image (gdb thread debugging issue FIX).
  - Nss group configuration in nsswitch.conf has been modified.
  - CVE-2015-7547, CVE-2015-8779 patches have been applied.
- **Configure option**
  - linaro-gcc: ¡°--enable-lto¡± has been added.
  - linaro-glibc: ¡°--disable-nscd¡± has been added.
- **gmp library**
  - DEP (Data Execution Prevention) option has been applied.
- **elfutils**
  - CVE-2014-0172, CVE-2014-9447 patches have been applied.

**Build System Information**

- Tizen 3.0 is built with:
  - OS : Opensuse 12.3
  - OBS Version : 2.4.6
  - GBS Version : 0.24.3
  - MIC Version : 0.27.2
  - OBS Repo : http://download.opensuse.org/repositories/OBS:/Server:/2.4/openSUSE_12.3/
  - Tizen Service Repo : http://download.tizen.org/services/archive/16.03/
  - Tizen Tools Repo : http://download.tizen.org/tools/archive/16.02.2/
  - gcc Version : 4.9.2 (Linaro ¡®15 Jun version)
  - glibc Version : 2.20 (Linaro ¡®14 Nov version)
  - binutils Version : 2.25 (Linaro ¡®15 Oct version)

