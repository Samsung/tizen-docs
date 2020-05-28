# Tizen 6.0 Public M1 Release Notes

Release date: May 31, 2020


The Tizen 6.0 Public M1 release provides developers with the Tizen kernel, device drivers, middleware subsystems, and Web, Tizen .NET, and Native API set.


## Release Details

- [Getting source code](http://review.tizen.org/git/) (Tizen 6.0 M1 source codes are under **tizen** branch.)

- Getting binaries and images
  - Base: [http://download.tizen.org/releases/milestone/tizen/base/tizen-base_20200503.1/](http://download.tizen.org/releases/milestone/tizen/base/tizen-base_20200503.1/)
  - profile(unified): [http://download.tizen.org/releases/milestone/tizen/unified/tizen-unified_20200521.1/](http://download.tizen.org/releases/milestone/tizen/unified/tizen-unified_20200521.1/)

- [How to flash to a device](../developing/flashing.md)


## Release Notes

### System (Kernel and System framework)

#### New and changed features

- System management
  - Silent boot mode has been developed.
- Device management
  - Multi-frequency feedback vibration has been developed.
  - Safe unmount for external storage has been developed.
  - Extended File Allocation Table (exFAT) mount feature has been added.
  - Blink display has been supported.
  - Battery module has been improved for thermal management and reliability.
  - Product plugin architecture has been developed.
  - Storage cleanup modules have been improved.
  - API set for playing feedback with sound path information has been added.
- Logger
  - API set for dlogutil logdump has been added.
  - Separate persistent logging for critical events has been developed.
- Open source
  - Systemd version has been upgraded with KDBus support.
  - D-Bus (libdbus and dbus-daemon) has been upgraded with KDBus support.
  - GDBus (glib) has been upgraded with KDBus support.


### System (System Reliability)

#### New and changed features

- Generic platform status dump tool has been provided to dump the status of Tizen platform as unified interface.
- System status dump tool has been enhanced to support vendor-specific command line flag.
- C# call stack analyzer and interactive debugging mode have been added to Tizen Callstack Analyzer.

#### Fixes

- Crash garbage due to sudden power failure has been removed.


### System (Base)

#### New and changed features

- Open source
  - aspell 
    - Version 0.60.5.1 has been upgraded to version 0.60.8.
  - boost 
    - Version 1.65.1 has been upgraded to version 1.71.0.
  - bzip 
    - Version 1.06 has been upgraded to version 1.08.
  - dos2unix
    - Version 7.4.0 has been upgraded to version 7.4.1.
  - expat
    - Version 2.2.7 has been upgraded to version 2.2.9.
  - glib 
    - Version 2.52.2 has been upgraded to version 2.62.3.
  - hostname 
    - Version 3.2 has been upgraded to version 3.23.
  - icu 
    - Version 63.2 has been upgraded to version 65.
  - iniparser 
    - Version 3.2 has been upgraded to version 4.1.
  - jsoncpp
    - Version 1.84 has been upgraded to version 1.92.
  - Json-glib 
    - Version 1.4.2 has been upgraded to version 1.4.4.
  - kbd
    - Version 2.0.4 has been upgraded to version 2.2.0.
  - leveldb
    - Version 1.2 has been upgraded to version 1.22.
  - libarchive
    - Version 3.3.3 has been upgraded to version 3.4.0.
  - libevent
    - Version 2.1.8 has been upgraded to version 2.1.11.
  - libsolv
    - Version 0.6.35 has been upgraded to version 0.7.6.
  - libxml2
    - Version 2.9.7 has been upgraded to version 2.9.10.
  - libxslt
    - Version 1.1.32 has been upgraded to version 1.1.34.
  - libzypp
    - Version 14.27.0 has been upgraded to version 17.14.0.
  - meson
    - Version 0.51.2 has been upgraded to version 0.52.1.
  - ncurse
    - Version 6.1 has been upgraded to version 6.1-20191207.
  - ninja
    - Version 1.8.2 has been upgraded to version 1.9.0.
  - python
    - Version 2.7.15 has been upgraded to version 2.7.17.
  - sqlite
    - Version 3.29.0 has been upgraded to version 3.31.1.
  - tzdata
    - Version 2019a has been upgraded to version 2019c.
  - util-linux
    - Version 2.3 has been upgraded to version 2.34.
  - zypper
    - Version 1.11.11 has been upgraded to version 1.14.30.
  - perl-XML-LibXML (2.0134) has been added.
  - perl-XML-NamespaceSupport (1.12) has been added.
  - perl-XML-SAX (1.02) has been added.
- The capi-base-utils API set has been expanded.
  - Add
    - unorm2: Unicode normalization module.
  - New
    - unumsys: Numbering systems module.
    - utext: Text abstraction module.
    - uscript: Unicode Script module.
    - uidna: Internationalizing Domain Names in Applications (IDNA) module.
    - ucnv: Character conversion module.
    - ucnvsel: Converter selector module.
    - ucsdet: Detecting the charset or encoding of character data module.
- The capi-system-settings API has been improved in terms of performance and stability.

#### Fixes

- CVE patches
  - glib
    - CVE-2019-13012
    - CVE-2019-12450
  - libxml2
    - CVE-2018-14404
  - ncurses
    - CVE-2018-19211
    - CVE-2019-17595
    - CVE-2019-17594
  - python
    - CVE-2018-14647
    - CVE-2019-9636
    - CVE-2019-9947
    - CVE-2019-9948
    - CVE-2019-9740
    - CVE-2019-16935
    - CVE-2019-16056
  - bzip
    - CVE-2016-3189
    - CVE-2019-12900
  - libxslt
    - CVE-2019-11068
  - sqlite
    - CVE-2019-19603
    - CVE-2019-19646


### Application framework

#### New and changed features

- Improved alarm usability
  - Several time values have been provided to resolve the uncertainty of the inexact alarm.
- Improved app launch performance
  - A new type of loader called App-defined loader has been provided to improve internal app launch performance.
- Improved widget
  - API set to enable and disable by widget class has been added.


### Window System

#### New and changed features

- Wayland
  - Wayland has been upgraded to version 1.18.0.
  - The debug feature for detecting DEADLOCK has been enhanced.
  - The crash prevention code through map entry reuse on wayland-client side has been added.
- Libevdev
  - Libevdev has been upgraded to version 1.8.0.
- Libinput
  - Libinput has been upgraded to version 1.15.0.
- Libxkbcommon
  - Libxkbcommon has been upgraded to version 1.18.0.
- Pixman
  - Pixman has been upgraded to version 0.38.4.
- Wayland extension
  - The presentation-time protocol has been added. This lets the wayland client know when the wl_surface shows on a screen.
  - The tizen_video_surface_provider interface has been added. Display server can get the serial number of the wl_surface from this interface.
- Enlightenment Wayland display server
  - Video and UI synchronization has been added. The geometry of the video area changes with UI updates synchronously.
  - Display server window grouping feature has been added. It supports the common window grouping feature of display server. The window grouping operation is going to be performed in the display server core. Therefore, each product specific module can focus only on the policy management of the window group mode.
  - Support for the presentation-time protocol has been added. Display server can notify the presentation time of the wl_surface through this protocol.
  - E_EVENT_HWC_ACTIVATE/DEACTIVATE event for the enlightenment module has been added. These events let the enlightenment module know when the hwc is activated and deactivated.
  - The e_client_hwc_visible_skip_set function for the enlightenment module has been added. The enlightenment module can ignore e_client from the hwc visible list with this function.
  - The tizen-dpms protocol support to bind only one wl_client has been added.
  - Key event generation API has been added in e_devicemgr.
  - enlightenment_input_key CLI tool has been added.
  - Support for long press and key composition has been added in e_keyrouter.
  - Functionalities for enlightenment_info have been added.
    - The functionality to check zone's display state has been added.
    - The functionality to display the force_obscured information has been added.
    - The functionality to display the geometry/zoom-factor of a desk has been added.
    - The information on functionalities such as topvwins and focus_history has been enhanced.
    - The functionality to generate key event has been added.
    - The functionality to generate multitouch events has been added.
    - The functionality to generate mouse event has been added.
    - The functionality to apply filters such as blur, grayscale, and color inversion on a window or on the entire screen has been added.
  - Privileges for gesture functionalities have been added.
  - An API to traverse surface tree of an E_Client has been added.
  - An API to reset axis information on a transform matrix has been added.
  - An API to get timeout value regarding e_policy_visibility has been added.
  - An API to remap key codes at runtime has been added.
  - An API to update the base_output_resolution for a remote surface has been added.
  - API set to set/unset zoom of a client has been added.
  - API set to block/unblock input events inside enlightenment has been added.
  - API set to change E_Client’s stack has been added.
    - e_client_stack_above,  e_client_stack_below
  - Blocking input events during custom transition animation has been added.
  - Skipping handling tizen_position_set request for the keyboard window has been added.
  - e_policy_appinfo API set has been changed to e_appinfo API set.
  - e_policy_stack_transient_for_set API has been changed to EINTERN from E_API.
  - E_POLICY_HOOK_CLIENT_ROTATION_GEOMETRY_SET hook has been added.
  - E_COMP_WL_PID_HOOK_CONNECTED_CLIENT_CREATE hook has been added.
  - Logs for quick panel requests have been added.
  - Logs for touch/wheel events have been added.
- Tizen Display Manager (TDM)
  - The tdm_display_get_pp_preferred_align_vertical API has been added.
  - The tdm_layer API set makes the error message when the tdm-backend supports the tdm_hwc.
- TPL-EGL
  - The API set for the synchronization has been added.
    - wl_egl_window_tizen_create_commit_sync_fd
    - wl_egl_window_tizen_create_presentation_sync_fd
    - wl_egl_window_tizen_merge_sync_fds

#### Fixes

- Enlightenment
  - Many code defects detected by the static analysis tool have been fixed.
  - Compilation warnings while building with GCC-9 have been fixed.
  - The output transform bug has been fixed at HWC_Windows.
  - The flickering issues at the time of the HWC transition have been fixed.
  - The several bugs under pp zoom have been fixed.
  - The bug regarding sending quickpanel_state message has been fixed
  - The bug regarding setting input region has been fixed.
  - The bug regarding single touch device has been fixed.
  - The bug regarding positioning cursor under the transformed window has been fixed.
  - The bug regarding displaying cursor on the transformed window has been fixed.
  - The bug regarding positioning cursor when the cursor is reloaded has been fixed.
  - Bugs regarding base_output_resolution have been fixed.
  - Bugs regarding calculation of visibility have been fixed.
  - Bugs regarding checking focus have been fixed.
  - Bugs regarding seamless effect feature have been fixed.
  - Input region request has been fixed to be applied only for the mapped window.
  - Wrong handling of consumer hash data regarding remote surface has been fixed.


### Graphics Engine

#### New and changed features

- DALi (3D UI Toolkit)
  - Actor, Window, and Renderer
    - Support for multiple render targets has been added.
    - Support for the reflection has been added to the Camera.
    - Signals for the window effect have been added.
  - Text, Input and Gesture
    - Support for the rotation gesture has been added.
    - Environment variables for the long press, pinch, and rotation gesture have been added.
    - Some preedit enumerations have been added.
  - Widget
    - Support for the multiple widget instances has been added.
  - Control
    - The shadow property has been added to the Control.
  - Image
    - Support for downloading a remote SVG file has been added.
    - Support for loading an n-patch image file asynchronously has been added.
    - Support for loading an SVG file synchronously has been added.
- NUI
  - LottieAnimationView has been added.
  - Implicit conversion for Size, Size2D, Position, and Position2D has been added.
  - ComponentBasedApplication has been added.
  - Window related API set has been added.
  - ScrollEvent of ScrollableBase has been added.
  - CornerRadius of View has been added.
  - Support for the default style has been added to NUI.Components.
  - Hex color code has been added.
  - NUI.Components styles and extensions have been added.
  - NUI.Components have been updated to support features of wearable profile.
  - .NET pre-initialize has been added.
  - Several InputMethodContext API set has been added.

#### Fixes

- DALi (3D UI Toolkit)
  - Actor, Window and Renderer
    - Some RenderTask bugs have been fixed.
    - A crash caused by the uniforms of the Shader has been fixed.
    - The PropertyNotification bug of the Actor::SIZE property has been fixed.
    - Some bugs of the window rotation have been fixed.
  - Text
    - A paste bug of the clip board has been fixed.
    - Some text bugs have been fixed.
  - Control
    - Some bugs of the controls that render images have been fixed.
- NUI
  - Several Layout bugs have been fixed.
  - AlphaMaskUrl setting order problem has been fixed.

#### Known Issues

- NUI
  - ImfManager has been removed.


### UI framework

#### New and changed features

- EFL
  - Version 1.23 has been upgraded to version 1.24.
  - New API set has been added.
    - elm_conformant_input_area_resize_disabled_get
    - elm_conformant_input_area_resize_disabled_set
    - elm_win_aux_msg_key_get
    - elm_win_aux_msg_val_get
    - elm_win_aux_msg_options_get
    - ecore_wl2_connected_display_get
    - ecore_wl2_display_connect
    - ecore_wl2_display_disconnect
    - ecore_wl2_display_flush
    - ecore_wl2_display_native_get
    - ecore_wl2_display_screen_size_get
    - ecore_wl2_display_sync
    - ecore_wl2_display_window_find
    - ecore_wl2_egl_window_create
    - ecore_wl2_egl_window_destroy
    - ecore_wl2_egl_window_native_get
    - ecore_wl2_egl_window_resize_with_rotation
    - ecore_wl2_init
    - ecore_wl2_input_default_input_get
    - ecore_wl2_input_pointer_xy_get
    - ecore_wl2_shutdown
    - ecore_wl2_window_activate
    - ecore_wl2_window_alpha_get
    - ecore_wl2_window_alpha_set
    - ecore_wl2_window_buffer_attach
    - ecore_wl2_window_commit
    - ecore_wl2_window_damage
    - ecore_wl2_window_display_get
    - ecore_wl2_window_focus_skip_get
    - ecore_wl2_window_focus_skip_set
    - ecore_wl2_window_frame_callback_add
    - ecore_wl2_window_frame_callback_del
    - ecore_wl2_window_free
    - ecore_wl2_window_hide
    - ecore_wl2_window_id_get
    - ecore_wl2_window_keygrab_list_set
    - ecore_wl2_window_keygrab_list_unset
    - ecore_wl2_window_keygrab_set
    - ecore_wl2_window_keygrab_unset
    - ecore_wl2_window_lower
    - ecore_wl2_window_native_surface_get
    - ecore_wl2_window_new
    - ecore_wl2_window_raise
    - ecore_wl2_window_show
    - ecore_wl2_window_title_get
    - ecore_wl2_window_title_set
    - ecore_wl2_window_video_has
    - elm_object_scroll_back_to_top_enabled_set
    - elm_object_scroll_back_to_top_enabled_get
    - elm_object_scroll_back_to_top_cb_set
    - elm_naviframe_item_push_from
    - elm_textpath_circular_set
    - ecore_evas_aux_hint_add
    - evas_map_point_precise_coord_get
    - evas_map_point_precise_coord_set
- EFL-extension
  - New API set has been added.
    - eext_rotary_event_activated_object_get
    - eext_popup_add
- UI-Viewmanager has been deprecated.
- Freetype2
  - Version 2.9.1 has been upgraded to version 2.10.1.
- Fontconfig
  - Version 2.13.0 has been upgraded to version 2.13.1.
- Harfbuzz
  - Version 2.4.0 has been upgraded to version 2.6.4.
- Atk
  - Version 2.30 has been upgraded to version 2.25.1.
- At-spi2-atk
  - Version 2.20.1 has been upgraded to version 2.34.1.
- At-spi2-core
  - Version 2.31.1 has been upgraded to version 2.34.0.
- Aurum has been added.
  - Automation framework for UI testing
- efl-theme-tizen-wearable has been updated with new UX.
- efl-theme-tizen-common has been updated with new UX.
- Voice Framework
  - The Word Recognition Rate (WRR) of default voice control engine has been enhanced.
  - The feature for changing background volume has been added. 
  - The speed of connecting TTS engine service has been enhanced.
  - The downloadable package for TTS engine has been supported. 
- Multi-Assistant Framework
  - The preprocessing processor has been supported.
  - The feature for push to talk and tab to talk has been added. 
  - The API for setting preprocessing mode has been added.
- Sticker Framework
  - Support for on-demand daemon launch has been added.
  - Support for whitelist to limit access to the sticker DB has been added.
  - API set to set/get display type of sticker (emoji, wallpaper) has been added.
  - API set to delete sticker using URI has been added.
  - API set for managing recent stickers history has been added.
  - API for registering has been added whenever sticker info is changed.

#### Fixes

- Reference display for IoT headed has been added. It is 7 inch display with 1280x720 resolution.
- Input Framework
  - The bug for language and return key type callback not working has been fixed.
  - It has been modified to call language_changed, accessibility_changed callback on the C# IME.
  - Many code defects detected by the static analysis tool have been fixed.
  - Compilation warnings while building with GCC-9 have been fixed.
- Sticker Framework
  - It has been modified to create the DB tables when sticker daemon is not launched.
- Voice Framework
  - Many code defects detected by the static analysis tool have been fixed.
  - Compilation warnings while building with GCC-9 have been fixed.
  - The thread safety issue on voice command has been fixed.
  - The memory leak issue has been fixed.
  - The checking UTF-8 validation bug has been fixed.

#### Known Issues

- efl-theme-tizen-wearable is under development, and will be completed by the next release.
- efl-theme-tizen-common is under development, and will be completed by the next release.


### Multimedia framework

#### New and changed features

- Media Vision
  - A new enumeration type has been added.
    - mv_inference_target_device_e
  - An enumeration type has been deprecated.
    - Mv_inference_target_type_e
  - Input tensor data type definition has been added.
    - MV_INFERENCE_INPUT_DATA_TYPE
  - A new neural network runtime support has been added.
    - ARMNN
- Media Player
  - 3rd generation playback engine has been applied.
    - uridecodebin3, decodebin3
- Media Codec
  - A new codec type for OPUS has been added.
- MediaTool
  - A new format type for AV1 has been added.
- Camera
  - A new pixel format type for MJPEG has been added.
  - A new flag to check whether it’s delta frame or not has been added.
- Open source upgrade
  - GStreamer
    - Version 1.12.2 has been upgraded to version 1.16.2.
    - webrtcbin has been enabled to support native webrtc.
  - Pulseaudio
    - Version 11.1 has been upgraded to version 13.0.
  - OpenCV
    - Version 3.4.1 has been upgraded to version 4.2.0.
  - GraphicsMagick
    - Version: 1.3.31 has been upgraded to version 1.3.34.
  - Giflib
    - Version 5.1.2 has been upgraded to version 5.1.9.
  - Libpng
    - Version 1.6.36 has been upgraded to version 1.6.37.
  - Libjpeg-turbo
    - Version 2.0.1 has been upgraded to version 2.0.4.
  - Tiff
    - Version 4.0.10 has been upgraded to version 4.1.0.
- Audio FW
  - An API to control input (capture) volume has been added in audio-in.
  - An API to support looping has been added in wav-player.
  - Support for multi-channel capture from mic-array device (3 ~ 8 channels) has been added.
  - Support for high quality microphone input (up to signed 32-bit) has been added.
  - Support for audio routing of multiple built-in audio devices has been added.


### Network and Connectivity

#### New and changed features

- Wi-Fi Aware
  - Neighbor Awareness Networking (Wi-Fi Aware) specification has been developed.
    - Devices which equip Wi-Fi chips with Wi-Fi Aware support can find each other and exchange data directly without AP.
  - New platform level Wi-Fi Aware API set has been introduced.
- Improved AP selection algorithm
  - AP selection algorithm in ConnMan has been improved to consider network environment more intelligently.
- EAP over Ethernet
  - EAP protocol has been developed to support in Ethernet also.
  - New platform level connection API set has been added.
- curl
  - Version 7.62 has been upgraded to version 7.68.
- libsoup
  - Version 2.46.0 has been upgraded to version 2.62.2.
- libwebsockets
  - Version 2.3.0 has been upgraded to version 3.2.0.

#### Fixes

- Bug in user awareness framework has been fixed.
- Bug in bluetooth framework has been fixed.


### Security

#### New and changed features

- Askuser
  - New application for user consent has been added.
    - It was provided by a daemon, however, now it is being provided by an application.
- Security manager
  - The way to control access of shared/data has been changed.
    - It is controlled in an application’s mount namespace.
  - New privilege control mechanism has been added.
    - Privileges can be mapped to predefined Smack label and rules.
    - Applications that have these privileges have proper Smack rule set when it is launched.
- Privileges
  - New privilege has been added.
    - notification.admin


### Service framework

#### New and changed features

- Battery-Monitor framework
  - Support for fetching battery information for custom period has been added.
  - Battery monitor API set has been changed to return usage in mAh instead of percentage.
  - Support for C# API set for battery monitor has been added. 
  - Support for estimating battery information for external tools has been added.
    - Support for estimating approximate power usage per application ID has been added.
    - Support for estimating power usage per system resource has been added.
    - Per-app statistics of state and events has been added. 
  - Following API set has been changed to provide custom time period support and return usage in mAh.
    - API for fetching information for an application for a particular resource over a certain duration of time has been updated.
    - API for fetching total battery usage information of an application, combining all the resources over certain duration of time has been updated.
    - API for fetching battery usage values for all the resources separately used by an application ID for a certain duration has been updated.
    - API for fetching battery usage values for a particular resource over certain duration of time has been updated.
- Contact Framework
  - Support for getting count for contact records has been added for better performance.
    - API for fetching count of searched records has been added.
    - API for fetching count of searched record with range has been added.
    - API set for fetching count for searched record with query has been added.

#### Fixes

- Context Framework
  - Memory stacking issues have been resolved.
- Contact Framework
  - DB integrity checks have been added.
  - Handling of XCUSTOMCHARSET has been added.


### Web framework

#### New and changed features

- Web Engine
  - Open source chromium 76 version base has been applied. The following features and API set are provided by the new web engine:
    - Named web worker: For multiple workers on the same URL, named web worker makes workers distinguishable by name.
    - Relative time API
    - User activation API
    - Web share API
    - Private class field support
  - Web Engine is able to support multi-platform version. 
    - Chromium 76 based Tizen web engine is compatible with Tizen 5.5.
    - Web engine is packaged with installable tpk format.
- Web Runtime
  - Open source electron 6.1.5 version has been applied for wrt-core functionality.
  - WRT-AddOn feature has been extended as follows:
    - Handle multiple events from an addon.
    - Handle multiple operations for an event.
    - Prohibit the disallowed events and their operation.
  - WRT-Service feature has been extended as follows:
    - Provide background web services with multiple sandbox contexts by sharing single nodejs instance for low memory devices.
    - Support Tizen web API in the WRT-Service context (device API set, nodejs built-in API set, and standard JS API set).
    - Provide global background service (independent of web application and allows web service creations for multiple web applications).
- Web view enhancement
  - Web view API and interface for various back-end has been enhanced.
    - Generic web view: Categorized EWK API set systemically.
    - .NET web view API
      - Xamarin web view: Improves API coverage compared to the other platforms (iOS, Android).
      - tizenFX Tizen.WebView: Improves API coverage compared to the Native web view.
    - NUI Web view API: Provides API consistency (coverage, naming) with .NET webview.
  - WRT-AddOn feature has been extended as follows:
    - Handle multiple events from an addon.
    - Handle multiple operations for an event.


### Lightweight Web Solution

#### New and changed features

- Rendering engine 
  - WebRTC has been added.
- JS Engine (New ES Features)
  - Exponential operator has been added.
  - New built-in methods (related with Array, Object) have been added.
  - Rest parameter and spread operator for object have been added.
- Performance and Memory Optimization
  - Rendering Engine
    - Direct mode has been enabled on EvasGL.
    - CompositorGL has been fixed to enhance performance.
    - Multithreaded image decoding feature has been added.
    - OpenGL texture has been re-used to reduce the loading time.
  - JS Engine
    - Frequently used case about apply operation has been optimized.
    - Source code compression has been updated to reduce large memory consumption in source code.

#### Fixes

- Bug fixes
  - Layout bugs have been fixed.
  - Memory leak has been fixed.
  - Crash has been fixed.


### Tizen .NET

#### New and changed features

- TizenFX (Tizen .NET Device API) API Level 8
  - Pipeline and SingleShot functionalities have been added in MachineLearning Inference.
  - Auto rotation sensor has been added in Sensor.
  - LottieAnimationView has been added in NUI.
- Xamarin Forms
  - Xamarin.Forms 4.5.0, which is the latest stable version has been supported.
- Tizen.CircularUI
  - Wearable UI extension (Tizen.Wearable.CircularUI) 1.5.0 preview has been supported.
- .NET runtime and tools
  - .NETCore has been upgraded from 3.0.0 to 3.1.0.
  - .NETCore diagnostics tools have been supported.


### Toolchain

#### New and changed features

- GNU GCC 9.2 has been enabled by default from Tizen 6.0 Platform.
  - Libraries are updated by gmp 6.1.2, mpc 1.1.0, mpfr 4.0.2, and isl 0.22.
  - Cilk runtime is dropped in upstream.
- Glibc (GNU 2.30), Binutils (GNU 2.33.1) have been upgraded.
  - The NIS (+) support library, libnsl, has been also deprecated from glibc 2.26.
  - Libio.h has been removed from glibc 2.28.
- Compilation options have been updated.
  - The default mode for C++ is now -std=gnu++14 instead of -std=gnu++11.
  - Program Instrumentation Option (-fstack-protector-strong) and Linker option (-Wl,-z,relro) have been added globally to improve security.
  - Code generation Option (-frecord-gcc-switches) has been added and now used command line is recorded into the object file as .GCC.command.line.
  - "_FILE_OFFSET_BITS=64" has been added as default on armv7l.
  - New warning options have been enabled by default in -Wall -Wextra switches.
- Toolchain testing infrastructure has been enabled.
  - Packages (autogen, dejagnu, guile, libgc, tcl and expect) for toolchain testing have been added. 
  - "{package}-testresults.rpm" in gdb, binutils, glibc, and gcc have been provided with run_tests macro.


### Machine Learning

#### New and changed features

- ML/Inference API
  - Pipeline .NET API set has been added.
  - Single C/.NET API set has been updated.
    - Single API support for flexible input tensor dimensions has been added.
      - Applications are no longer required to close and re-open a handle to change input tensor dimensions.
    - Single API support for hardware acceleration configurations has been added.
    - Tizen’s Neural Network Runtime (nnfw) has been integrated.
    - Performance enhancement: low-latency open and invocation.
    - Timeout for invocation may be specified.
- NNStreamer update
  - NNStreamer is upgraded from 1.0.0 to 1.5.2.
  - Tizen Sensor Framework may be used as stream inputs.
  - AI acceleration hardware and neural network framework support has been added.
    - ML API now allows controlling HW acceleration.
    - ML API may utilize NCSDK2, Edge-TPU, OpenVINO, ARMNN, Caffe2, and PyTorch.
      - You may need to download and install additional adaptors from tizen.org for these additional frameworks or hardware.
  - The ability to insert filters implemented as a C++ class (OpenCV compatible) or a simple C function has been added.
- nnfw: Neural Network Runtime
  - nnfw has been upgraded to version 1.4.0.
  - Support for quantized MobileNet and Inception V3 models on CPU Backend has been added.

#### Fixes

- Dynamic tensor dimensions issue of Neural network Single API set, the 5.5 M2 known issue, has been fixed.
  - New Single API set to support flexible tensor dimensions has been added.
- Inference API set/additional neural networm framework supports
  - Tizen’s Neural Network Runtime (nnfw) has been integrated.
  - Others (TensorFlow, Caffe2, PyTorch, and so on) have been supported optionally if the device has additional packages downloaded and installed from tizen.org.

#### Known Issues

- ML/Inference Pipeline C-API and .NET API
  - If APPSRC is used with DO NOT FREE mode, an additional memcpy per input frame has been added as a workaround. This work around is expect to be removed with a performance fix in the later releases.

