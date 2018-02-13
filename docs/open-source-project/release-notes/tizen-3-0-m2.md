# Tizen 3.0 Public M2

Release Date: Jan 18, 2017

Tizen 3.0 adopts various new features, such as high-performance graphics, the latest Web technology, improved security, and multi-user support.

## Release Details

- [Getting source code](http://review.tizen.org/git/) (Tizen 3.0 M2 source codes are under **tizen_3.0_m2** branch.)

- [Getting binaries and images](http://download.tizen.org/releases/milestone/tizen/3.0.m2)

  - Base: [http://download.tizen.org/releases/milestone/tizen/3.0.m2/3.0.m2-base/tizen-3.0.m2-base_20170104.1/](http://download.tizen.org/releases/milestone/tizen/3.0.m2/3.0.m2-base/tizen-3.0.m2-base_20170104.1/)
  - TV: [http://download.tizen.org/releases/milestone/tizen/3.0.m2/3.0.m2-tv/tizen-3.0.m2-tv_20170111.1/](http://download.tizen.org/releases/milestone/tizen/3.0.m2/3.0.m2-tv/tizen-3.0.m2-tv_20170111.1/)
  - Common: [http://download.tizen.org/releases/milestone/tizen/3.0.m2/common_artik/tizen-common-artik_20170111.3/](http://download.tizen.org/releases/milestone/tizen/3.0.m2/common_artik/tizen-common-artik_20170111.3/)
  - Mobile: [http://download.tizen.org/releases/milestone/tizen/3.0.m2/3.0.m2-mobile/tizen-3.0.m2-mobile_20170111.1/](http://download.tizen.org/releases/milestone/tizen/3.0.m2/3.0.m2-mobile/tizen-3.0.m2-mobile_20170111.1/)
  - Wearable: [http://download.tizen.org/releases/milestone/tizen/3.0.m2/3.0.m2-wearable/tizen-3.0.m2-wearable_20170111.1/](http://download.tizen.org/releases/milestone/tizen/3.0.m2/3.0.m2-wearable/tizen-3.0.m2-wearable_20170111.1/)

- [How to flash to a device](../developing/flashing.md)


## Release Notes

### System (Kernel and System Framework)

**New and Changed Features**

- Systemd/Service initialization time enhancement
  - First service launch time has been improved by optimizing the unit/smack initialization time.
  - Service initialization time has been improved by utilizing tmpfiled.
- Directory hierarchy enhancement and compatibility support
  - System directory structure has been refined to support read-only directories and multi-user.
  - Hard-coded path in source code has been removed.
  - Support for a platform default user has been added.
  - Support for 2.4 content and application directories has been added.
- Storage API and block module enhancement
  - USB/SD Card external storage has been enumerated with the libstorage API.
  - Support for multiple partitions and devices has been added.
  - Block dbus connection has been separated to a special-purpose block module.
- Device HAL upgrade
  - Common device HAL structure has been added.
  - USB configfs is supported.
  - Default device adaptation layer for a standard kernel interface has been added.
- Power management enhancement
  - Dynamic power state transition has been added.
  - Power state actor for supporting several profiles and devices has been added.
- Debug and fail-safe handling system enhancement
  - New kmsg and pipe log backend have been added.
  - The kmsg, pipe, and Android&trade; logger backends are supported.
  - Runtime watchdog functionality has been added.
  - Callstack generation based on ptrace is supported as an option to eliminate the double crash issue.
- Feedback system enhancement
  - Feedback daemon to support multiple patterns has been added.
  - Various patterns are supported, such as a combination of duration and waiting.
- System information enhancement
  - GDBM backend to support a light-weight system registry to improve performance has been added.
- Cynara-based dbus policy support through dbus-daemon
  - Privilege-based access check has been added.
- New APIs
  - IR device APIs have been added.
  - USB Host APIs have been added.
  - Battery and charger status APIs have been added.
  - Detailed build information has been added.
  - CPU frequency APIs have been added.
  - Storage change event handler API has been added.
- Major open-source component upgrades and changes
  - Systemd version has been upgraded from v216 to v219.
  - Pwdutils has been replaced with shadow-utils.
  - Libfuse version has been upgraded to 2.9.6.
  - Fsck-msdos and newfs-msdos have been separated from deviced.
  - The libdbus version has been upgraded to 1.10.6.
  - In TV, the kdbus version has been upgraded to V4.

### System (Base)

**New and Changed Features**

- Base library upgrade
  - Address sanitizer building is supported.
  - ICU binary data file has been changed to text data file.
  - unzip has been patched for CVE-2015-7697.
  - expat version has been upgraded to 2.2.0.
    - CVE-2016-4472
  - iniparser version has been upgraded to 3.2.
- System-settings API enhancement
  - Functions for adding or deleting string-list type data for ringtone-list (internal json handling) have been added.
- i18n (base-utils) API enhancement
  - Detect host time zone function has been added.
  - Ucalendar wrapper API has been added.
  - Utmscale wrapper API has been added.
  - Ushape wrapper API has been added.
  - Ubidi wrapper API has been added.
- Vconf-internal-keys one-branch policy adoption
  - Type check XML scheme validation for 'type' specifier at build-time has been added.
  - 'layer' by automation has been removed.
- tzdata-update parser plugin addition
  - Support for updating tzdata at runtime by downloadable application has been added.

### Application Framework

**New and Changed Features**

- Application
  - An event API to keep last event data has been added.
  - Support for text input delegation has been added.
  - Several new operations have been added.
- Application IPC
  - Data control data change notification API has been added.
  - Support for data control bulk management has been added.
- Application package installer
  - The optional mount installation feature has been added.
  - Separate permission for users for installing global applications and user-private applications has been added. Only admin users can install global applications.
  - Support for listening for the disable/enable application event has been added.
  - A filter property for application information has been added.
- Application launcher
  - Application background launch mode has been added.
  - Support for color-depth on splash screens has been added.
- Notification
  - Support for direct reply has been added.
  - Support for notification template has been added.
- Widget
  - Support for multiple widgets has been added.
  - Widget framework has been rewritten to support the multiple viewer concept.

As a common feature, multi-user support has been added.

### Graphics System

**New and Changed Features**

- Extended Wayland protocols
  - tws_service_screensaver_manager allows a client screensaver manager to register itself and control a user-configurable period of inactivity.
  - tws_service_screensaver sets the screensaver surface, which can be shown after a user-configurable period of inactivity.
  - tizen_launchscreen allows the application manager to show a default splash image of the application before displaying the application window.
  - tizen-clipboard allows the application to communicate with the system clipboard.
  - tizen-remote-surface allows a client to provide its offscreen buffer to other clients.
  - tizen_video and tizen_video_object allow a client to show video content through a hardware overlay.
  - wl_tbm_queue is extended to support selective-composite mode on the fixed-framebuffer target.
  - Tizen keyrouter allows applications to grab 1 or more hardware keys with a single request.
  - tizen_input_device_manager has been added to support input device identification from input events and additional axis information, such as touch pressure and size, for applications.
- Enlightenment Wayland display server
  - X server has been replaced with Wayland in this version.
  - Full specification of the Wayland protocol has been implemented based on Enlightenment 0.20.0.
  - Desktop features (gadget, widget, and file manager) have been removed from Enlightenment (cleanup).
  - The following plug-in submodules are provided:
    - e-mod-tizen-wm-policy controls the appearance and stack of the application window.
    - e-mod-tizen-keyrouter supports the hardware key grab/ungrab feature.
    - e-mod-tizen-devicemgr manages hardware device-related operations, such as DPMS, input device, output device, and video layer controls.
    - e-mod-tizen-processmgr communicates with resourced to provide changed information for the application window.
    - e-mod-tizen-wl-textinput manages virtual keyboard operations.
    - wl_desktop_shell handles the Wayland xdg-shell protocol, which supports general window operations, such as move, resize, and maximized.
    - bufferqueue handles ecore-buffer to support the sharing of the UI buffer between clients.
  - Support for launching an application in the background has been added.
  - Support for a visibility event for the splash image has been added.
  - Support for floating mode windows has been added.
  - Support for the screensaver has been added.
  - Support for hardware compositing has been added and enabled on both GL and software engines.
  - Support for the system clipboard window has been added.
  - Support for sharing an offscreen buffer between clients through the tizen-remote-surface has been added.
  - Support for buffer flush has been added, allowing a suspended application to free its window buffer.
  - wl_drm has been removed from the enlightenment core module and moved to e_comp_drm. It is responsible for initializing the ecore_drm and evas_gl_drm engine.
  - Touch cancel and visibility events have been added to libpepper-efl.
  - To reduce memcpy time, openmp is used for copying framebuffer contents while changing the compositing mode.
  - Support for a hardware cursor has been added. It enables the display server to improve rendering performance when moving the mouse pointer, if the target supports a hardware cursor.
  - Support for setting a quickpanel handler has been added, allowing the external Enlightenment module to change the behavior of the quickpanel according to the UX.
  - Wayland debugging information can be acquired with debugging tools. The following information is included:
    - Window geometries
    - Window stacks
    - Resource allocation status
    - FPS (frame per second) value
    - Wayland protocol messages with user-defined filters
    - List of input devices and related information
    - Key grab status for each hardware key
    - Keymap information
    - List of output devices and related information
    - List of composite objects and related information
  - Easy keymap customization
    - Keymap customization has been enabled and is easily applicable by creating a new key layout file or modifying an existing key layout file.
    - A key layout file is a text file format which includes:
      - Definition of keynames and mapping between a keyname and a keycode
      - Repeat configuration and privilege check Boolean values for each key
    - Prebuilt keymap cache support
        - 1 or more keymap caches can be generated at build time and installed.
        - There is no need to compile a keymap at boot time and runtime by using existing keymap caches.
  - Touch event cancellation
    - A cancellation event can be created and sent to the current touch surface when 1 of the following events takes place:
        - Window stack changes
        - LCD/display is switched off
        - Touch gesture is recognized
  - Input device/event block/unblock support
    - Each type of input device or each input event can be blocked by the client request only when the client has the proper privilege for the request.
  - Input device identification support
    - Source input device information can be acquired from an input event, such as Ecore or Evas event, in an application.
    - The information includes the name, description, and device type of the source input device.
  - Keygrab support for an array of keys
    - Series of key grab requests can be created and sent for multiple keys in a window surface with a single API call.
  - Mouse input event generation API support
    - The request for generating mouse input events on the server side can be created only when the client has the proper privilege for the request.
  - Additional input device axes support for touchscreen
    - Axis information can be acquired from an input event, such as an Ecore or Evas event, in an application.
    - Axis information includes the pressure, angle, and radius of each contacting finger on the touchscreen.
  - Key event repeat support
    - Server informs clients about the keyboard's repeat_info (rate/delay).
    - Generating repeated key events is performed on the client side.
- libpepper-efl
  - libpepper-efl has been released.
  - libpepper-efl is a lightweight and flexible library for developing EFL host applications, which support the embedded Wayland compositor.
- Tizen ws shell
    - API to support controlling of the quickpanel service window has been added.
- efl-util
  - API to support controlling of the screen brightness through the application window has been added.
  - Behavior of the following APIs has been changed to support synchronous operation:
    - `efl_util_set_notification_window_level()`
    - `efl_util_set_window_screen_mode()`
  - The following APIs have been deprecated:
    - `efl_util_set_notification_window_level_error_cb()`
    - `efl_util_unset_notification_window_level_error_cb()`
    - `efl_util_set_window_screen_mode_error_cb()`
    - `efl_util_unset_window_screen_mode_error_cb()`
- Tizen HAL
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
    - TPL (Tizen Porting Layer) is an abstraction layer for surface and buffer management on the Tizen platform, aimed to implement the EGL&trade; porting layer of the OpenGL&reg; ES driver over various display protocols.
    - Supported EGL&trade; backends:
        - Wayland, gbm, tbm
    - Buffer management and Wayland protocol of Vulkan WSI Tizen are supported.
    - Emulator GL Driver (emulator-yagl) supports the libtpl-egl backend.
- Vulkan WSI Tizen
  - The Vulkan WSI (Window System Integration) Layer for Tizen wraps vendor Vulkan&reg; ICDs and provides the WSI (Window-System Interface) for Tizen.
  - The VK_KHR_wayland_surface is supported.
- CoreGL
  - CoreGL is an OpenGL&reg; ES injection layer.
  - CoreGL provides the following capabilities:
    - Support for driver-independent optimization (FastPath)
    - EGL&trade;/OpenGL&reg; ES debugging
    - Performance logging
  - Supported versions:
    - EGL&trade; 1.4
    - OpenGL&reg; ES 1.1, 2.0, 3.0, 3.1, 3.2
  - OpenGL&reg; ES/EGL&trade; development headers are provided.
    - Khronos OpenGL&reg; ES/EGL&trade; headers (Khronos released on Oct 24 2016)
- DALi (3D UI Toolkit) enhancement
  - Wearable profile support has been added.
     - Wearable watch application template has been added.
  - Image
    - Support for N-patch and ASTC native compressed image formats has been added.
    - Support for texture wrapping modes has been added.
    - Support for image fitting modes has been added.
    - Support for PixelArea and pre-multiplied alpha in ImageView has been added.
  - Text
    - TextEditor for multi-line and multi-language edition has been added.
    - Support for markup processing in TextField has been added.
    - Support for auto scrolling in TextLabel has been added.
    - ControlStyleManager has been added.
    - FlexContainer has been added.
    - Slider has been added.
    - VideoView has been added.
    - Model3dView control for full 3D model rendering support has been added.
    - PageTurn control for the page turn function rendering support has been added.
    - Support for child property registration has been added.
    - Support for control background rendering without creating an extra actor has been added.
  - 3D rendering and animation
    - Wayland rendering backend has been added.
    - Renderer API and Visual properties for low-level control including culling, blending, depth, and stencil testing have been added.
    - Support for setting the animation loop count has been added.
    - Support for getting the animation state has been added.
    - Support for the `REQUIRES_SYNC` property to enable and disable GL sync in RenderTask has been added.
    - Support for ostream writers have been added.
- SDL 2.0 (Simple DirectMedia Layer)
  - Tizen backend
    - Support for Tizen App life-cycle management has been added.
    - Support for Tizen App Core event has been added.
    - Support for touch and key event has been added.
    - Support for window system based on Ecore_Wl has been added.
    - Support for input with Tizen ISF has been added.
    - Support for dlog has been added.
    - Support for cursor has been added.
  - Additional features
    - Support for SDL timer with vblank has been added.
    - Support for rotation has been added.
  - Vulkan&reg;
    - Support for using Vulkan&reg; directly (without wrapper) has been added.
    - Support for using WSI wrapper functions to avoid window system dependency has been added.
    - Support for avoid window system dependency in SDL has been added.
- Evas render engine enhancement
  - Evas GL
    - Support for OpenGL&reg; ES 3.1 has been added.
  - Optimization texture uploading
    - To avoid COW case, texture uploading optimization has been added.
  - Runtime shading
    - Downstream runtime shading has been added.
  - Offscreen backend
    - Evas TBM surface SW/GL backends have been added.
    - Ecore-Evas TBM surface SW/GL modules have been added.
  - Native surface set
    - Support for wl_buffer for Evas GL_DRM/wayland backend has been added.
  - Wayland-shm with TBM
    - Support for TBM surface in Evas wayland-shm backend has been added.
- Open-source component upgrade
  - Wayland version has been upgraded to 1.8.0.
  - Enlightenment version has been upgraded to 0.20.0.
  - Cairo version has been upgraded from 1.12.14 to 1.14.2.
  - Vulkan-LoaderAndValidationLayers version has been upgraded to 1.0.29.
  - SDL 2.0.4 has been added.

**Fixes**

- Fixed the copy and paste operation failure caused by the broken pipe on the server side.
- Fixed the first screen resizing during application launch.
    - The root cause was a lack of synchronization between EFL and Wayland for the first scene drawing.
- Fixed the IME rotation problem, which was caused by a lack of synchronization between the display server and client for the window rotation.
- Fixed the server-side handler for the ping-pong protocol, which was not working properly.

**Known Issues**

- DALi control vibration is not supported.

- SDL indicator is not fully verified.

### UI Framework

**New and Changed Features**

- EFL upgrade (from 1.13 to 1.16)
  - Wayland-backed has been enabled.
  - efl-misc has replaced elm-misc.
  - efl-modules has replaced elm-modules.
  - e17-extra-config-modules has been removed.
  - A new efl-config daemon configures scalable UI setting at boot time.
  - The notify style name for popup has been changed (popup to popup/default).
  - The default scroller for popup has been removed. The application must call the `elm_popup_scrollable_set(popup, EINA_TRUE)` function.
  - Item style for ctxpopup has been changed. Use the list item instead of box.
  - The minimum size of a genlist item is not defined. If necessary, the application must specify the minimum size of the genlist item by itself.
  - In mobile, the default theme has been refined.
  - In mobile, LazEDC and color class have been applied to default theme.
  - EDC support for SVG files has been added.
  - EFL vector support for GL and SW backend have been added.
  - In mobile, CBHM (ClipBoard History Manager) has been integrated.
  - In mobile, view manager has been added.
  - Customization APIs have been added.
- Text input
  - Input framework has been changed from X-based to Wayland-based.
  - In mobile, 3 input languages have been added (Irish, Uzbek, and Hindi).  
    The supported languages are: Azerbaijani, Bulgarian, Catalan, Czech, Danish, Greek, German, English (US), Spanish, Estonian, Basque, Finnish, French, Irish, Galician, Croatian, Hungarian, Armenian, Icelandic, Italian, Japanese, Georgian, Kazakh, Korean, Lithuanian, Latvian, Macedonian, Norwegian, Dutch, Polish, Portuguese, Romanian, Russian, Slovak, Slovenian, Serbian, Swedish, Turkish, Ukrainian, Uzbek, Chinese, Chinese (Hong Kong), Chinese (Taiwan), Hindi, and Albanian.
  - The scim-launcher process has been integrated to scim-helper-launcher process.
  - In wearable, the input delegator window has been added.
  - Synchronous `get_surrounding_text()` API support has been added.
- Voice interaction
  - The speech-to-text feature has been enabled.
  - The server-based speech-to-text engine has been included as a default engine.
  - Support for third-party speech-to-text/text-to-speech engines has been added.
  - Support for the voice control framework has been added.
  - The supported languages of the TTS engine have been extended to 28 languages.  
    The supported languages are: English (US), English (UK), English (India), Korean, Spanish, Mexican Spanish, French, German, Italian, Russian, Brazilian Portuguese, Portugal Portuguese, Chinese, Chinese (Hong Kong), Chinese (Taiwan), Japanese, Hindi, Czech, Dutch, Danish, Finnish, Greek, Hungarian, Norwegian, Polish, Slovak, Swedish, and Turkish.

**Fixes**

- Many bugs have been resolved.

**Known Issues**

- EFL
  - EFL abort on error is enabled by default.
  - Joystick currently does not work.
- Accessibility
  - Screen reader functionality has not been fully tested.
- Clipboard
  - CBHM (ClipBoard History Manager) has not been fully tested.
- View manager
  - View manager has not been fully tested.
- Customization API
  - In wearable, the theme is not ready for customization.
- Focused UI has not been fully tested.
- UI mirroring has not been fully tested.
- Tizen 3.0 UX has not been fully implemented, especially visual interactions.

### Multimedia Framework

**New and Changed Features**

- Open-source component upgrade
  - GStreamer has been upgraded from 1.4.5 to 1.6.1.
  - Pulseaudio has been upgraded from 4.0 to 5.0.
  - Alsa-lib has been upgraded from 1.0.25 to 1.0.28.
  - OpenAL has been upgraded from 1.13 to 1.17.2.
  - libsndfile has been upgraded from 1.0.25 to 1.0.26.
  - libjpeg-turbo has been upgraded from 1.3.1 to 1.4.2.
  - libpng has been upgraded from 1.6.13 to 1.6.21.
  - giflib has been upgraded from 4.1.6 to 5.1.2.
  - tiff has been upgraded from 4.0.3 to 4.0.6.
- Player
  - Internal method to provide a player service has been changed from library to server-client.
  - Module to set the sound policy has been changed.
    - Most interrupt callback code has been deprecated, except for the resource conflict.
    - API for setting the sound type has been deprecated.
    - API to set the sound stream info has been added.
  - Error code (`PLAYER_ERROR_BUFFER_SPACE`) for the data push API has been added.
  - Default buffering storage has been changed from file to memory.
  - The performance has been optimized by removing unnecessary IPC when rendering video.
  - API to set the region of interest area in the display has been added.
  - The `player_completed_cb()`, `player_error_cb()`, and `player_prepared_cb()` functions have been made to invoke by default context.
  - Error return value of `player_create()` API and display-related APIs has been added.
  - In wearable, the Evas display type has been added.
- Radio (in mobile and wearable)
  - API to set or get the volume has been added.
  - Pre-state of `radio_scan_start()` API has been changed.
- Media tool
  - APIs to support container type have been added.
  - API to get a flag for the buffer stream information has been added.
  - API to set the video frame rate has been added.
  - API to get the video frame rate has been added.
  - Media packet pool APIs to reuse allocated media packets have been added.
- Media codec
  - API to get media packet pool has been added.
- Media streamer
  - Another player service type to allow the user to design a player structure according to their requirements has been added.
- Media demuxer
  - Demuxing service for a multiplexed media stream has been added.
- Media muxer
  - Muxing service to create audio/video content with a given type of container format has been added.
- Audio
  - API to free the device list has been added.
  - API to manage audio stream focus has been added.
  - API to manage stream based routing has been added.
  - API to manage audio devices has been added.
  - Old Session/Routing API has been deprecated.
  - Enumeration to support Bluetooth SCO has been added.
  - Feature to support power-off mute control has been added.
  - Feature to support transfer Bluetooth property (wideband, nrec) has been added.
  - API to query current media playback device has been added.
  - API to query whether stream is connected to specific device has been added.
  - Feature to support auto-last-connected device policy has been added.
  - Feature to support fading audio in pulseaudio has been added.
  - Feature to protect infinite power consumption caused by improper use of audio APIs has been added.
  - Sound-Server has been changed to operate as an on-demand process.
  - In TV, a feature to support vconf in pulseaudio has been added.
  - In TV, a feature to use of tizen-audio-sink/source has been added.
- Camera
  - Internal method has been changed to provide a camera service from library to server-client.
  - Error enumerations for the sound policy have been deprecated.
  - Error enumerations for resource conflict have been added.
  - API to get the flash state set by the Camera API has been added.
  - API to get the camera facing direction has been added.
  - APIs for the encoded preview format (H.264) have been added.
  - APIs to set and get pan have been added.
  - APIs to set and get tilt have been added.
  - APIs to set and get display ROI (region of interest) area have been added.
- Recorder
  - Internal method to provide a recorder service has been changed from library to server-client.
  - Error enumerations for the sound policy have been deprecated.
  - Error enumerations for resource conflict have been added.
  - API to set the sound stream information has been added.
  - File format (MPEG2TS) has been added.
  - Audio codec (MP3) has been added.
- Media content
  - Multi-user support has been added.
  - New information for detecting and tracking faces on images with media vision has been added.
  - The getter API return value "Unknown" has been modified to an empty string ("") for the following properties:
      - Title, description, album, artist, album_artist, genre, composer, year, copyright, track_num
  - The get thumbnail path API default return value has been modified from a default path to an empty string ("").
  - Thumbnails are no longer extracted automatically by the framework. The application must request thumbnail creation if a thumbnail is needed.
  - API to start and cancel face detection for media has been added.
  - API to get 360 content for image and mp4 files has been added.
- Media controller
  - Multi-user support has been added.
- Image util
  - PNG, GIF, BMP encoding/decoding support has been added.
  - JPEG encoding/decoding has been modified to use a handle.
  - JPEG encoding/decoding APIs have been deprecated.
- Thumbnail util
  - The `http://tizen.org/privilege/content.write` privilege has been removed.
- Metadata extractor
  - Attribute enums have been added.
  - Audio codec, video codec, and 360 attributes have been added.
- Screen mirroring
  - Support for transfer data streaming from the source device has been added.
- Mediavision
  - Face detection, recognition, and tracking have been added.
  - Image detection, recognition, and tracking have been added.
  - Surveillance has been added.

**Fixes**

-  Many bugs have been fixed.

### Network and Connectivity

**New and Changed Features**

- Data network
- In mobile and wearable, SoftAP (Software-enabled Access Point) has been added.
- In mobile, wearable, and TV, support for multi-instance in applications has been added to the WiFi Manager API.
- In mobile and TV, the default VPN to build up the VPN default setting has been added.
- In mobile, wearable, and TV, NSD (Network Service Discovery) has been added.
- In mobile, the additional AP router function (such as port forwarding, 802.11 mode/channel, and dhcp range) has been added to the tethering module.
- In mobile and wearable, APIs for HTTP have been added to the curl wrapper.
- In mobile, the Wi-Fi TDLS (Tunneled Direct Link Setup) has been added.
- In mobile, the tethering configuration has been added.
- In mobile and TV, the VPN service to build up a VPN client has been added.
- In mobile and wearable, an additional connection type has been added to handle a gadget connection.
- In mobile and TV, the IPC of the wifi direct manager has been changed from socket to d-bus.
- In mobile and wearable, the privilege for the `wifi_ap_create()` function has been removed.
- In mobile and TV, an API for wifi-direct peer signal strength has been added.
- In mobile and TV, APIs for connection to get/set cellular pdn type have been added.
- In mobile and wearable, HTTP uploading file/cancel APIs have been added.
- Connectivity
  - MTP initiator has been added.
  - MTP initiator APIs are provided.
  - In mobile and wearable, the NFC preferred application has been added.
  - In mobile and wearable, the NFC internal API for HCE operation and the pkgmgr-plugin-nfc package has been added.
  - In mobile and wearable, the NFC appcontrol operations have been modified for the Tap&Pay menu.
  - In mobile and wearable, the NFC client library has been merged to the CAPI layer because of a smack issue.
  - BLE GATT server behavior has been improved.
  - BLE GATT server API has been added.
  - BLE GATT server API, write request has been modified for the response_needed option. In TV, the BLE IPSP function is supported.
- IoTCon
  - IoTCon has been newly added to support IoTivity 1.2.1.
  - IoTivity security has been enabled.
  - APIs for resource finding and registration have been added.
  - APIs for resource requests and responses have been added.
  - APIs for resource observation and presence have been added.
- Telephony
  - In mobile and wearable, the CDMA/LTE network info getter API has been added.
  - In mobile and wearable, the lac/cell ID network API privilege has been changed.
  - In mobile, support for the do-not-disturb feature has been added.
- Major open-source component upgrades and changes
  - Curl has been upgraded from 7.40 to 7.50.2 for stability.
  - Dnsmasq has been upgraded from 2.57 to 2.74 for stability.
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
- In mobile and wearable, the memory leak in the NFC/Smartcard daemon has been fixed.
- Memory leak in the wifi-direct manager and popup has been fixed.
- Memory leak in net-config and mobileap-agent has been fixed.
- Memory leak in bt-agent and bt-service has been fixed.
- TLS session cache operation to handle TLS resumption has been fixed.
- Chained certificate verification to handle intermediate CA list has been fixed.
- UID/GID of MTP Initiator has been changed from system to network_fw.
- MTP Initiator critical section issues have been fixed.

### Security

**New and Changed Features**

- Access control
  - The smack usage has been changed from many domains to 3 domains for maintainability.
  - The security-manager package has been added.
    - When an application installs, smack labels and rules are added.
    - When an application installs, the application is added to a proper group if needed.
  - The libprivilege-control package has been removed.
    - Functionalities have been moved to security-manager.
  - The security-server package has been removed.
    - Functionalities have been moved to security-manager and cynara.
  - Support for application shared directory has been added for backward compatibility.
  - Support for application private sharing APIs has been added for backward compatibility.
  - All smack rules generated by security-manager have been merged to 1 file to improve performance of smack rule loading.
  - libnss_securitymanager has been implemented.
    - The user session daemon has been inserted to proper groups.
  - A new smack domain, User::Shell, has been created to protect system resources from sdb shell, and restrict permissions of sdb shell
  - In mobile and wearable, the smack onlycap feature has been enabled.
    - A new smack domain, System::Privileged, has been created.
    - Only a process with the System::Privileged label can have `CAP_MAC_ADMIN` and `CAP_MAC_OVERRIDE`.
  - In mobile and wearable, platform upgrade functionalities are supported.
    - The user/global application list has been moved to `/opt/var`.
  - In TV, the `internet` privilege is not checked.
- Application privilege
  - The cynara package has been added.
    - When an application requests a service, it checks whether an application has the proper privilege.
  - Web privilege management method has been changed.
  - The cynara package has been divided into 3 sub-packages to avoid build dependency.
  - Cynara monitor APIs for gathering privacy usage information have been added.
  - In mobile and wearable, privacy setting application has been added.
    - If the user does not want to grant specific privileges to an application, they can disable the privileges.
  - In mobile and wearable, a user confirmation step has been added.
    - If an application uses privacy-related privilege, user confirmation is required.
  - In TV, the `GetConnectionCredentials()` method in gdbus helpers is used for kdbus support.
- Privilege list
  - In mobile, the following privileges have been added:
    - Native
      - `antivirus.admin`, `antivirus.scan`, `antivirus.webprotect`, `appdir.sharedata`, `d2d.datasharing`, `dpm.bluetooth`, `dpm.browser`, `dpm.camera`, `dpm.clipboard`, `dpm.debugging`, `dpm.email`, `dpm.location`, `dpm.lock`, `dpm.message`, `dpm.microphone`, `dpm.password`, `dpm.security`, `dpm.storage`, `dpm.usb`, `dpm.wifi`, `dpm.wipe`, `dpm.zone`, `fido.client`, `location.coarse`, `use_ir`, and `vpnservice`
    - Web
      - `d2d.datasharing` and `widget.viewer`
  - In mobile, the following privileges have been deprecated:
    - Native
      - `keymanager` and `minicontrol.provider`
  - In wearable, the following privileges have been added:
    - Native
      - `account.read`, `account.write`, `antivirus.admin`, `antivirus.scan`, `antivirus.webprotect`, `appdir.shareddata`, `appmanager.kill.bgapp`, `calendar.read`, `calendar.write`, `contact.read`, `contact.write`, `d2d.datasharing`, `dpm.bluetooth`, `dpm.browser`, `dpm.camera`, `dpm.clipboard`, `dpm.debugging`, `dpm.email`, `dpm.location`, `dpm.lock`, `dpm.message`, `dpm.microphone`, `dpm.password`, `dpm.security`, `dpm.storage`, `dpm.usb`, `dpm.wifi`, `dpm.wipe`, `dpm.zone`, `email`, `fido.client`, `ime`, `imemanager`, `inputgenerator`, `keygrab`, `location.coarse`, `mediacontroller.client`, `mediacontroller.server`, `packagemanager.clearcache`, `systemmonitor`, and `use_ir`
    - Web
      - `bluetooth`, `d2d.datasharing`, `ime`, `led`, `mediacontroller.client`, and `mediacontroller.server`
  - In wearable, the following privileges have been deprecated:
    - Native
      - `keymanager` and `keymanager.admin`
    - Web
      - `bluetooth.admin`, `bluetooth.gap`, `bluetooth.health`, and `bluetooth.spp`
  - In TV, the following privileges have been added:
    - Web
      - `bluetooth`, `d2d.datasharing`, and `volume.set`
  - In TV, the following privileges have been deprecated:
    - Web
      - `keymanager`
- Root daemon minimization
  - Converted root daemons to non-root permission to prevent potential attacks.
  - Unlike the system process in Tizen 2.4, each daemon has a separate ID.
    - The following IDs are defined in Tizen 3.0:
      - app_fw, application, broadcasting, graphic, location, messaging, multimedia_fw, network_fw, scm, sdk, security_fw, sensor, service_fw, social, system_fw, telephony, testing, ui_fw, and web_fw
      - Defined system_share for group ID to allow access between daemons.
    - 50+ daemons have been changed from root to non-root ID.
    - Root daemon minimization is still in progress.
- Device policy management framework
  - New device policy management framework and related APIs
    - In mobile and wearable, password policy APIs have been added.
    - Restriction policy APIs have been added.
    - Security policy APIs have been added.
    - In mobile, the zone policy APIs have been added.
- Container (in mobile)
  - New container package:
    - New container framework has been added.
    - KeyGuard has been added.
    - Container App Launcher has been added.
    - Container Setup Wizard has been added.
- Authentication
  - Password Management package has been changed.
    - The password management feature has been moved from security-server (until Tizen 2.4) to auth-fw (since Tizen 3.0).
  - Public Key Pinning has been introduced.
    - Public pinning for HTTPS has been introduced in a browser and the following internal modules: oauth2, download-provider, dali-adaptor, email-service, conn-man, and chromium-efl
    - pubkey-pinning package has been added to help internal modules using HTTPS to check the validity of a server certificate with static pinning data.
  - OCSP checking during application installation has been added.
    - Certificates for an application with OCSP information are checked during the installation with OCSP.
    - If there is no Internet connection, the installer skips the OCSP check and installs the package/application. Cert-checker performs the OCSP check for all newly-installed applications when the Internet connection is available.
  - tizen-security-policy package has been removed.
    - tizen-security-policy in Tizen 2.4 had app-signing root certificates. App-signing root certificates have been moved to ca-certificates-tizen.
  - cert-svc has been changed.
    - Pluggable step has been added to the app-signature validation. The plugin can perform an additional signature validation step.
    - Internal APIs in the `cert-service.h` header file have been completely removed. The cert-svc-vcore capis implement the same functionality.
    - Additional fingerprint file (`fingerprint_list_ext.xml`) for application signature verification root certificates are now allowed.
    - Internal symbolic links in application packaging are now allowed.
    - Certificate blacklist for application signature verification has been added.
- Data protection
  - The secure-storage package has been removed.
    - Its functionality has been replaced by key-manager and libwebappenc packages.
  - Key manager
    - Hardware integration has been upgraded.
    - Encrypted initial value support has been added.
    - Symmetric key (AES key) support has been added.
    - All public APIs have been changed to non-privileged APIs.
    - The following APIs have been added:
      - APIs to handle PKCS12 files, such as `ckmc_save_pkcs12()` and `ckmc_get_pkcs12()`, have been added.
      - API for certificate verification with designated trust certificates has been added.
      - API for OCSP (Online Certificate Status Protocol) has been added.
      - The `kmc_set_permission()` function to manage access control rules efficiently has been added.
      - The `ckmc_remove_alias()` function that deletes data in the database using an alias has been added.
      - Error code (`CKMC_ERROR_AUTHENTICATION_FAILED`) for per-row password mismatched error has been added.
      - API to create an AES key has been added.
      - APIs for encryption and decryption have been added.
      - APIs to handle cryptographic parameters have been added.
    - The following APIs have been changed:
      - Platform-level privilege has been removed from the key-manager control APIs.
      - Getting a certificate chain with the aliases API has been deprecated.
  - Web application encryption
    - Web application (WGT) encryption feature is moved from secure-storage (until Tizen 2.4) to libwebappenc (since Tizen 3.0).
  - YACA (Yet Another Crypto API)
    - A new crypto API package, YACA, has been introduced in Tizen 3.0.
      - It provides the application with the following stable cryptographic APIs:
        - APIs for encryption/decryption operations with symmetric keys and sealing and opening operations with asymmetric keys
        - APIs for creating and verifying a signature, calculating HMAC/CMAC, and calculating a message digest
        - APIs for key handling operations, such as generating, importing, and exporting a key, and deriving a key from a password
        - Simple APIs for cryptographic operations
        - APIs for low-level RSA operations
  - openssl upgrade
    - openssl has been upgraded to 1.0.2j.
    - The following risky SSLv2-related APIs were removed:
      - `SSLv2_method()` ,`SSLv2_client_method()`, `SSLv2_server_method()`
- Anti-virus
  - csr-framework
    - Client-server architecture has been adopted.
    - Whole APIs have been changed to simple and easy APIs.
    - Delta scanning is supported.
    - Only embedded engine is supported (engine in the application is not supported).

### Service Framework

**New and Changed Features**

- Location
  - Map service (in mobile and wearable)
    - APIs to get place list metadata, multiple reverse-geocodes, and alternative routes have been added.
    - APIs to render a map image on an Evas object have been added.
    - APIs for map objects, such as marker, polyline, and polygon, have been added.
    - API to capture snapshots of the current map has been added.
    - Gesture detector to recognize gestures internally has been added.
    - Mapzen map provider plugin has been added.
  - Location (in mobile and wearable)
    - APIs to get mock locations have been added.
    - APIs to get locations in a batch have been added.
  - Geofence (in mobile)
    - APIs to get proximity data based on geofence have been added.
- Sensor
  - Sensor listener (in mobile and wearable)
    - 2 new sensor types, sleep detector and stress monitor, have been added.
  - Sensor recorder (in mobile and wearable)
    - Pedometer, heart-rate monitor, and sleep monitor data recording is supported.
- Context
  - Contextual trigger (in mobile)
    - The contextual trigger allows applications to define and publish custom context data, which can be used to compose triggering rules.
    - Update events in contacts DB can be used as events for trigger rules.
  - Contextual history (in mobile)
    - The contextual history provides per-application battery usage statistics.
- PIMS
  - Contacts (in mobile and wearable)
    - In wearable, the contacts service has been added.
    - API for the aggregation suggestions has been added.
    - Usage types for contact usage statistics have been added.
    - API to reset phone log statistics by SIM slot number has been added.
    - SIP address contact property has been added.
    - APIs for the search snippet have been added.
    - APIs for setting the limit size of the vCard photo have been added.
    - API for checking the initialization status in each SIM has been added. Old API has been deprecated.
    - API for importing contacts from each SIM has been added. Old API has been deprecated.
    - Thumbnail support for contact and person has been added.
    - Database mode has been changed to WAL mode.
    - Multi-user support has been added.
    - API for checking progress of SIM contact import has been added.
    - In mobile, the service running mode is changed from on-demand to always-on.
  - Calendar (in mobile)
    - IPC of the calendar service has been changed from PIMS-ipc to gdbus.
    - Multi-user support has been added.
    - Database mode has been changed to WAL mode.
  - Phonenumber-utils (in mobile and wearable)
      - In wearable, Phonenumber-utils has been added.
      - API for normalization of the phone number has been added.
      - APIs for daemonization of phonenumber-utils have been added.
- Email and message
  - Email (in mobile and wearable)
    - In wearable, the email service has been added.
    - Multi-user support has been added.
    - Email sent notification has been changed. It is cleared automatically after 3 seconds.
  - Message (in mobile and wearable)
    - msg-manager package for multi-user support has been added.
    - API for checking change of thread list has been added.
    - APIs related to v-object have been deprecated.
    - Reply on active notification feature has been added.
    - Support for single-part MMS has been added.

### Web Framework

**New and Changed Features**

- Web View API
  - The following APIs have been added:
    - `ewk_cookie_manager_file_scheme_cookies_allow_get()`, `ewk_cookie_manager_file_scheme_cookies_allow_set()`, `ewk_context_intercept_request_callback_set()`, `ewk_intercept_request_url_get()`, `ewk_intercept_request_http_method_get()`, `ewk_intercept_request_headers_get()`, `ewk_intercept_request_ignore()`, `ewk_intercept_request_response_set()`, `ewk_intercept_request_response_status_set()`, `ewk_intercept_request_response_header_add()`, `ewk_intercept_request_response_header_map_add()`, `ewk_intercept_request_response_body_set()`, `ewk_intercept_request_response_write_chunk()`, `ewk_view_add_in_incognito_mode()`, `ewk_view_javascript_message_handler_add()`, and `ewk_view_evaluate_javascript()`
- HTML5/W3C APIs
  - Responsive Images  
    Enables tag-based responsive image resource mapping for facilitating multi-screen Web application design and implementation.
  - Web Components (`template`, `imports`)  
    Enables user-defined Web components
  - Service Worker  
    Enables background task/page management.
  - WebSpeech API  
    Provides enhanced support for Speech APIs, including speech recognition.
  - Media Source Extensions (MSE)  
    Allows JS to generate media streams.
  - WebRTC  
    Enables real-time communication between browsers.
  - Web Cryptography API and Contents Security Policy 1.1
  - Web Push API  
    Gives Web applications the ability to receive messages pushed to them from the app server. (Not included in the TCS)
- Web Device API
  - Iotcon API  
    Provides functions for IoT connectivity.
  - Preference API  
    Stores and retrieves small pieces of data which can be used for application preferences.
  - Widget Service API  
    Provides information about installed widgets.
  - Player Util API  
    Manages features related to the W3C Player.
  - Key manager  
    Provides a secure repository protected by the Tizen platform for keys, certificates, sensitive data, and application data.
  - Feedback API  
    Plays sound or vibration associated with an action.

**Fixes**

- Web Core
  - Invalid computation (0) of `screen.availableWidth` and `screen.availableHeight` has been fixed.
  - The default encoding type for the data URL scheme has been modified from ascii to app-specified encoding.
  - Layout crash caused by text autosizing has been fixed.
  - The DOM timer suspending while panning is working has been fixed.
  - Incremental image rendering has been switched off.
  - The db path relative to application path has been fixed.
  - Always-on option for the sensor depending on the screen-off condition has been added.
  - The maximum size of data URI scheme data has been increased from 2 MB to 6 MB.
  - Tizen has been applied as a vendor for `navigator.vendor`.
  - A deprecated `document.width` and `document.height` implementation has been added as a working API.

### SCM

**New and Changed Features**

- gcc
  - Address Sanitizer is officially supported.
  - In mobile and wearable, Leak Sanitizer and UndefinedBehavior Sanitizer are now available.

**Fixes**

- gcc
  - An internal compiler error (PR ipa/64896) issue has been fixed.
  - The plugin infrastructure for sanitizer development has been enabled.
- glibc
  - `libBrokenLocale.so` is included in the target image (fix for dlopen fail issue).
  - `libtrhead_Db.so.1` is included in the target image (fix for gdb thread debugging issue).
  - Nss group configuration in `nsswitch.conf` has been modified.
  - CVE-2015-7547, CVE-2015-8779 patches have been applied.
- Configuration options
  - linaro-gcc: `--enable-lto` option has been added.
  - linaro-glibc: `--disable-nscd` option has been added.
- gmp library
  - DEP (Data Execution Prevention) option has been applied.
- elfutils
  - CVE-2014-0172, CVE-2014-9447 patches have been applied.

**Build System Information**

- Tizen 3.0 is built with:
  - OS: Opensuse 12.3
  - OBS Version: 2.4.6
  - GBS Version: 0.24.3
  - MIC Version: 0.27.2
  - OBS Repository: http://download.opensuse.org/repositories/OBS:/Server:/2.4/openSUSE_12.3/
  - Tizen Service Repository: http://download.tizen.org/services/archive/16.03/
  - Tizen Tools Repository: http://download.tizen.org/tools/archive/16.02.2/
  - gcc Version: 4.9.2 (Linaro '15 Jun version)
  - glibc Version: 2.20 (Linaro '14 Nov version)
  - binutils Version: 2.25 (Linaro '15 Oct version)

