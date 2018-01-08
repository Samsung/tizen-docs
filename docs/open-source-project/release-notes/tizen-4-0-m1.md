# Tizen 4.0 Public M1

Release Date: 31 May, 2017

The Tizen 4.0 Public M1 release provides developers with the Tizen kernel, device drivers, middleware subsystems, and Web and Native APIs.

### Release Details

- [Getting source code](http://review.tizen.org/git/) (Tizen 4.0 Public M1 source codes are under **tizen_4.0** branch.)

- [Getting binaries and images](http://download.tizen.org/releases/milestone/tizen/4.0.m1/)
  - Base: [http://download.tizen.org/releases/milestone/tizen/4.0.m1/tizen-base_20170520.1/](http://download.tizen.org/releases/milestone/tizen/4.0.m1/tizen-base_20170520.1/)
  - Mobile: [http://download.tizen.org/releases/milestone/tizen/4.0.m1/tizen-unified_20170529.1/images/standard/mobile-wayland-armv7l-tm1/](http://download.tizen.org/releases/milestone/tizen/4.0.m1/tizen-unified_20170529.1/images/standard/mobile-wayland-armv7l-tm1/)
  - Wearable: [http://download.tizen.org/releases/milestone/tizen/4.0.m1/tizen-unified_20170529.1/images/standard/wearable-wayland-armv7l-tw2/](http://download.tizen.org/releases/milestone/tizen/4.0.m1/tizen-unified_20170529.1/images/standard/wearable-wayland-armv7l-tw2/)
  - TV: [http://download.tizen.org/releases/milestone/tizen/4.0.m1/tizen-unified_20170529.1/images/standard/tv-wayland-armv7l-odroidu3/](http://download.tizen.org/releases/milestone/tizen/4.0.m1/tizen-unified_20170529.1/images/standard/tv-wayland-armv7l-odroidu3/)

- [How to flash to a device](../developing/flashing.md)

# Release Notes

## System (Kernel and System Framework)

**New and Changed Features**

- System Framework
  - The PASS (Power Aware Service System) daemon has been added for hardware (CPU, GPU, and memory) resource management.
  - Open-source components have been upgraded and changed:
    - Systemd has been upgraded from 219 to 231.
    - Libgudev package has been detached from Systemd.
    - Initrd package has been added.
    - Libconfig has been upgraded to 1.6.
    - Libusb has been upgraded to 1.0.21.
  - The resource management daemon has been changed to make resources lighter for IoT devices.
  - APIs have been added:
    - Dlog C#-internal APIs
    - Getting physical memory size API

**Fixes**

- System Framework
  - Many Dbus/Kdbus bugs have been fixed.
  - The systemd-journald log starvation bug has been fixed.
  - The dlogutil dump mode (nonblack) bug has been fixed.


## System (Base)

**New and Changed Features**

- Base Library
  - Open-source libraries have been upgraded:
    - Sqlite (3.14.2)
    - leveldb (1.20)
    - libzypp (16.3.1)
    - libzypp-binding (0.7.3)
    - zypper (1.13.14)
    - libsolv (0.6.23)
    - re2 (20161101)
    - re2c (0.16)
    - pbzip2 (1.1.13)
    - json-glib (1.2.0)
    - jsoncpp (1.7.7)
    - icu (57.1)
  - Open-source packages have been added:
    - python-mako (1.0.6)
    - myton-mock (2.0.0)
    - python-funcsigs (1.0.2)
    - python-argparse(1.4.0)
    - python-linecache2 (1.0.0)
    - python-traceback2 (1.4.0)
    - python-unittest2 (1.1.0)
    - python-pbr (2.0.0)
    - python-six (1.10.0)
    - python-setuptools (34.3.3)
    - python-packaging (16.8)
    - python-MarkupSafe (1.0)
    - python-pyparsing (2.2.0)
    - python-appdir (1.4.0)

**Fixes**

- Upstream/file  
    - Rolled back the JPEG data file to support the old JPEG file conversion.
- Upstream/boost  
    - The build option has been modified to reduce the build time (from approximately 30 to 10 minutes).
- capi-base-utils  
    - i18nutil has been added to generate an i18n report for all locales supported in Tizen.



## Application Framework

**New and Changed Features**

- Application Core/Launcher
  - The appcore libraries have been rewritten to support all application models with the same code base.
  - The appcore simple plugin feature has been added.
  - The rua API has been improved to support an update change callback.
- Package Manager
  - An app update flag API has been added.
  - A package archive API has been added.
  - The pkgmgr database-related code has been rewritten to make it more efficient.
- Notification
  - The bigpicture UX feature has been added.
- Widget Framework
  - The screen connector library has been improved to support screen capture and multiple widget viewer in a more structured way.
  - An API for getting the widget setup app ID has been added.
  - An API for getting the watch setup app ID has been added.
- Application IPC
  - The message port registration event callback feature has been added.
  - data-control trusted communication has been added.


## Window System

**New and Changed Features**

- Extended Wayland Protocols
  - tizen_screen_rotation allows the display server to let a client ignore the output transform.
  - tizen_screenshooter is extended to support auto-rotation for the screen capture.
  - tizen_video_object is extended to control video object visibility in the topmost window.
  - tizen_remote_surface has a new mouse in/out event and render request for the provider.
  - tizen_launch has been added to apply the client window effect type according to the launch state.
  - tizen_visibility has added a `pre_unobscured` state for window visibility.
  - tizen_screen_rotation has been added to support screen rotation.
- Enlightenment Wayland Display Server
  - Mouse in/out event creation and render request on provider demand are supported for a remote surface client.
  - A transition effect depending on the launching client window type is applied using `tizen_launch`.
  - A `tws_dummy_extension` handler for tizen-ws-shell extensibility has been added.
  - Support for the screen rotation has been added.
  - A commit is performed for each tdm layer instead of committing a TDM output.
  - Debugging tools have been extended for:
    - Plane state
    - Pending commit
- wayland-tbm
  - Support has been added for checking the hardware compositing state of the client for front buffer rendering.
- libpepper-evdev
  - The libpepper-evdev library reads events from input device nodes, such as `/dev/input/eventX`, and creates pepper input events.
  - The library currently only processes a key event and creates a pepper keyboard event.
- libpepper-keyrouter
  - The libpepper-keyrouter library initializes the keyrouter in a pepper server and deals with keyrouter protocol requests from clients.
  - The library gets a key grab request from a client and sends 1 or more grabbed keys to the clients through the `wl_keyboard` protocol interface.
- Tizen ws Shell
  - A `tzsh_quickpanel_extension_get()` API has been added for extensibility.
- efl-util
  - Input generation with a specified device has been added:
    - An `efl_util_input_initialize_generator_with_name()` API has been added.
    - The existing input generation API provides event generation with a predefined device name, such as "Input Generator".
    - The API provides input generation with the device name provided from a client.
    - When a specific device name is needed, the new API can be utilized to simulate the device completely.
  - Support has been added for auto-rotating the screen capture image:
    - `efl_util_screenshot_set_auto_rotation()`
    - `efl_util_screenshot_get_auto_rotation()`
- Tizen HAL
  - Tizen display HAL
    - Support has been added for the layer commit to ensure an output commit per each vblank:
      - `TDM_COMMIT_PER_VBLANK` environment
    - Support has been added for controlling the client vblank fps in runtime.
    - Support has been added for the protocol trace between the TDM server and client.
  - Tizen buffer HAL
    - Support has been added for the setting/getting function for the DRM file descriptor to share it between TDM and TBM.
    - New error enumeration has been added for the TBM surface queue:
      - `TBM_SURFACE_QUEUE_ERROR_ALREADY_EXIST`
      - `TBM_SURFACE_QUEUE_ERROR_UNKNOWN_SURFACE`
    - Support has been added for the can-dequeue callback to let the user know when a TBM surface queue buffer can be dequeued.
    - Support has been added for buffering the TBM surface queue trace when the state is changed.
    - Support has been added for the capture of the TBM surface to a file.
  - Tizen EGL porting layer
    - New APIs have been added to wayland-egl to support the prerotation feature:
      - `wl_egl_window_set_rotation()`
      - `wl_egl_window_get_capabilities()`
    - The behavior associated with the `tpl_surface_set_frontbuffer_mode()` API has been changed to proper front buffer rendering.

**Fixes**

- Tizen HAL
  - The TDM vblank wrong behavior has been fixed.
  - The TDM buffer management functionality, which caused screen tearing, has been fixed.
  - The TDM thread deadlock bug has been fixed.
- Enlightenment Wayland display server
  - The bug about the screen flickering when hardware compositing mode is changed has been fixed.
  - The window rotation abnormal behavior has been fixed.
  - The floating window move/resize abnormal behavior has been fixed.
  - The notification window stack mismatch has been fixed.
  - The visibility disorder due to the wrong calculation of the window region during the client launch has been fixed.
  - The synchronization between a server and client in the 'copy and paste' feature has been fixed.
  - The move/resize bug in the system cursor image has been fixed.


## Graphics Engine

**New and Changed Features**

- DALi (3D UI Toolkit)
  - Actor and Stage
    - A top margin size has been added to Stage.
    - A sibling order property has been added to Actor.
    - An opacity property has been added to Actor.
    - Support for the enumeration setting in various properties has been added to Actor.
    - A property to allow an actor to ignore the anchor point for its position has been added to Actor.
    - Raise and Lower APIs have been added to Actor.
    - A visibility change signal has been added to Actor.
    - `Layer::TREE_DEPTH_MULTIPLIER` has been deprecated.
  - Property
    - Chaining support for `Property::Array` has been added.
    - Properties have been changed to update a value synchronously.
  - Image
    - Support for the GIF image has been added.
  - Window
    - Support for focus control has been added.
    - Support for visibility control has been added.
    - Support for the auxiliary hint has been added.
    - Support for the notification level, screen mode, and brightness has been added.
  - Key event and input
    - Support for the device name and device class of the key event has been added.
    - Various APIs have been added to IMF Manager.
  - Control and Visual
    - TextVisual has been added.
    - AnimatedImageVisual has been added.
    - Support for stylable transitions has been added.
    - Memory consumption of ImageVisual has been reduced.
    - Position and size properties have been added to Visual.
    - The Button control has been changed to use Visuals.
    - Support for the ItemView layout customization through properties has been added.
    - Tooltip functionality has been added to Control.
    - Support for focus control of the nested TableView control has been added.
    - Support for the vertical scroll animation on text input has been added.
    - Keyboard navigation properties have been added to Control.
    - A border size property has been added to ImageVisual.
    - Support for a custom keyboard focus algorithm has been added.
    - A property to hide input text has been added to TextField.
    - Support for asynchronous remote image loading has been added to ImageVisual.
    - The key event propagation rule has been changed.
    - A property to set a pixel size has been added to text controls.
    - A property to enable an ellipsis has been added to TextLabel.
    - Properties to control text auto-scrolling have been added to TextLabel.
  - 3D rendering and animation
    - Support for the animation of Renderer properties when offstage has been added.
  - NUI (C# interface)
    - DALi was originally developed in C++, then subsequently developed in parallel in C#. A separate Tizen NUI branch was created from this C# DALi branch.
    - More than 400 easy-to-use C# properties are newly added and bound to DALi native properties.
    - C# events are implemented and bound by the native signal/slot mechanism, which enables event chaining through the "+=" operator.
    - DisposeQueue has been added to release automatically unmanaged resources bound to DALi native objects.
    - The key navigation rule is enhanced by FocusManager and CustomKeyAlgorithmInterface.
    - High-level classes, which provide useful functionalities and easy interfacing to users, have been added. For example, Color, Size2D, and RelativeVector.
    - The Animation APIs are revised to improve usability.
    - NUIApplication has been added to inherit from the UICoreApplication class, which provides the Tizen C# application main loop and life-cycle event handling scheme.
    - The VisualView high-level class has been added to improve the DALi native Visual usability.
    - The overall class hierarchy and structure have been changed compared to native DALi.
    - Actor has been obsoleted and merged into View, which is to be the basis of NUI.
    - Stage has been removed and merged into Window, where only Layer can be added.
    - Main classes:
      - Animation: Can be used to animate the properties of any number of objects, typically View.
      - FlexContainer: Provides a more efficient way to lay out, align, and distribute space among items in the container.
      - FocusManager: Provides the functionality of handling key navigation and maintaining the 2-dimensional key focus chain.
      - Layer: Provides a mechanism for overlaying View groups on top of each other.
      - View: Is the primary object with which NUI applications interact. UI components can be built by combining multiple Views.
      - CustomView: Is a base class for the user to customize UI components.
      - ImageView: Used to display an image resource.
      - TextEditor: Provides a multi-line editable text editor.
      - PushButton: Changes its appearance according to its input events.
      - Window: Is used internally for drawing and managing Layers.
- Evas Render Engine
  - Evas GL Render threading
    - Evas GL Render threading has been added and is on by default.
  - TBM surface ROI mode
    - The adjusting ROI mode for the TBM surface has been changed from auto to users.
  - EvasGL
    - OpenGL&reg; ES 3.2
      - Support for OpenGL&reg; ES 3.2 has been added.
      - OpenGL&reg; ES 3.2 wrapper functions have been added to `Evas_GL.h`.
      - `EVAS_GL_DEBUG` for creating debug eglContext has been added to `Evas_GL_Context_Version`.
  - SDL
    - Support for the 32-bit depth window has been added.

**Fixes**

- DALi
  - The hit test has been fixed to include clipping actors as well as their children.
  - The bug in texture where Upload without parameters was incorrectly using the Texture size rather than the PixelData size has been fixed.
  - The bugs in TextureSet have been fixed.
  - The target value bug of the animation only set on `Animation::Play()` has been fixed.
  - Inconsistency of the scene graph and render items has been fixed.
  - The mismatch between the `GetTargetSize()` method and the Size property of Actor has been fixed.
  - The bug that caused a crash when the key is up on a Text control has been fixed.
  - The full progress image is now shown when 100%. The bug has been fixed.
- Evas Render Engine Enhancement
  - stride_get has now been implemented for the TBM surface in the Evas GL Engine.
  - The bug of the rotated image in an Evas object image has been fixed.
  - The memory leak in the Evas object image's rotation function has been fixed.
  - The partial rendering buf in the TBM backend has been fixed.
  - The bug that caused smooth rendering in `GL_TEXTURE_EXTERNAL_OES` to not work has been fixed.
  - The missed macro in OpenGL&reg; ES 3.1 has been fixed.
  - The memory leak of various data (internal data, FD, Wayland buffer) in Ecore Evas extern has been fixed.

**Known Issues**

- EvasGL
  - When MSAA is used, depth/stencil buffer is not created.
  - In EvasGL 3.2, context with robustness is not supported yet, because no drivers support this feature in Tizen devices. When driver support becomes available, this feature is added in EvasGL.



## UI Framework

**New and Changed Features**

- EFL
  - UI control and theme has been changed for Tizen 4.0 UX (TV).
  - Package configuration has been changed:
    - The ecore package has been divided into several smaller packages (ecore-audio, ecore-avahi, ecore-buffer, ecore-con, ecore-core, ecore-drm, ecore-evas, ecore-fb, ecore-file, ecore-imf, ecore-input, ecore-ipc, ecore-wayland).
    - The unified devel package is generated regardless of the Tizen profile.
  - edbus has been changed to support dbus only.
  - Test application and examples are removed from the binary image.
  - A source repository path has been changed:
    - From `profile/PROFILE/platform/core/uifw/efl-ext` to `platform/core/uifw/efl-ext`
- Voice Control
  - An automatic voice setting API for 14 widgets has been added to vc-elm (automatic voice-enabled widgets: Button, Check, Ctx-Popup, Entry, Fastscroll, Gengrid, Genlist,  Hoversel, List, Popup, Radio, Slider, Spinner, Toolbar).
  - The voice browsing feature has been added for Web applications.

**Fixes**

- Many bugs have been fixed.
  - An exception handling code has been added.
  - Memory leaks have been fixed.
  - Broken link in doc has been fixed.

**Known Issues**

- Accessibility
  - ScreenReader functionality has not been fully tested.
- Clipboard
  - CBHM (ClipBoard History Manager) has not been fully tested.
- View manager
  - View manager has not been fully tested.
- Customization API
  - In wearable profile, the theme is not ready for customization.
- Focused UI has not been fully tested.
- UI mirroring has not been fully tested.
- Tizen 4.0 UX is not finalized yet (UI control and theme can change later).



## Multimedia Framework

**New and Changed Features**

- Recorder
  - APIs for getting muxed stream data have been added.
- Media Content
  - An API for getting video rotation information has been added.
  - An API for getting/setting the bookmark name has been added.
  - APIs for updating file metadata (such as title, album, artist, and genre) have been deprecated.
  - The API for getting the storage name has been deprecated.
  - The cloud-related code has been deprecated.
- Thumbnail Utility
  - A new error type has been added.
- Open Source Upgrade
  - Tiff version has been upgraded from 4.0.6 to 4.0.7.
- Player
  - APIs for progressive download have been deprecated.
  - The display type has been replaced with a new value.
  - New error codes have been added.
- Audio
  - The SoundServer WAV handling logic has been improved by replacing the legacy parser and libtremo with libsndfile.
- MediaTool
  - A new media format has been added.
  - An API for setting extra data has been added.



## Network & Connectivity

**New and Changed Features**

- Data Network
  - New features and APIs have been added:
    - In mobile, wearable, and TV profiles, a connection API for getting the DHCP server address has been added.
    - In mobile, wearable, and TV profiles, the enum for the pdn type has been deprecated.
    - In mobile, wearable, and TV profiles, connection APIs for adding/removing a routing table have been added.
    - In the TV profile, connection APIs for attaching/detaching an Ethernet cable have been deprecated/added.
    - In mobile, wearable, and TV profiles, APIs for getting/setting the DNS config type have been added.
    - In mobile, wearable, and TV profiles, connection and wifi-manager APIs for getting/setting the prefix length have been added.
    - In mobile, wearable, and TV profiles, a connection and wifi-manager API for getting multiple ipv6 addresses has been added.
    - In mobile, wearable, and TV profiles, a wifi-manager API for getting multiple ipv6 addresses has been added.
    - In mobile, wearable, and TV profiles, a wifi-manager API for connecting a hidden AP has been added.
    - In mobile, wearable, and TV profiles, a wifi-manager API for getting the disconnect reason has been added.
    - In mobile, wearable, and TV profiles, wifi-manager APIs for connecting/canceling WPS-PIN/PBC without ssid have been added.
    - In mobile, wearable, and TV profiles, wifi-manager APIs for connecting/discovering TDLS without ssid have been added.
    - In mobile, wearable, and TV profiles, a wifi-manager API for switching TDLS's channel has been added.
    - In mobile, wearable, and TV profiles, wifi-manager APIs for getting the DHCP address have been added.
    - In mobile, wearable, and TV profiles, wifi-manager APIs for getting the scan status have been added.
    - In mobile and wearable profiles, the ASP (Application Service Platform) feature support has been added.
    - In mobile, wearable, and TV profiles, the IPv6 tethering feature support has been added.
    - In mobile, wearable, and TV profiles, tethering APIs for getting/setting IPv6 tethering have been added.
    - In the mobile profile, the default VPN (IPsec) feature support has been added.
    - In mobile and wearable profiles, the wifi-direct tethering feature support has been added.
    - In mobile and wearable profiles, the STC (Smart Traffic Control) feature support has been added.
  - Major open source upgrades and changes:
    - Curl has been upgraded from 7.40 to 7.53 for stability.
- Telephony
  - In mobile, wearable, and TV profiles, the telephony manager plugin has been added.
  - In mobile, wearable, and TV profiles, feature-based handling support has been added.
  - In mobile, wearable, and TV profiles, SQLite3 insertion operations for the packet service plugin have been improved.
  - In mobile and wearable profiles, telephony popup plugins have been added.
  - In mobile and wearable profiles, an API for network signal strength with dBm getter has been added.
  - In mobile and wearable profiles, an API for modem power status event register has been added.
  - In mobile and wearable profiles, LTE attach apn logic support has been added.
  - In the wearable profile, the call manager library support has been added.
  - In the wearable profile, the standalone mode telephony framework support has been added.
- Connectivity
  - New features and APIs have been added:
    -  In mobile and wearable profiles, support for OMAPI 3.2 has been added.
  - Major open-source component upgrades and changes have been made.
- Bluetooth
  - New features and APIs have been added:
    - In mobile, wearable, and TV profiles, IPSP (Internet Protocol Support Profile) APIs have been added.
    - In mobile, wearable, and TV profiles, GATT MTU Exchange APIs have been added.
    - In mobile, wearable, and TV profiles, LE Scan filtering APIs have been added.
  - Major open-source component upgrades and changes:
    - Bluez has been upgraded from 5.37 to 5.43.
- IoTCon
  - Dependency with system-settings has been removed.

**Fixes**

- Memory leak on the MTP daemon has been fixed.
- Memory leak on the connman and net-config has been fixed.
- Memory leak on the libnet-client and wifi-manager has been fixed.
- Memory leak on the IotCon has been fixed.
- Sample code bugs in the IoTCon document have been fixed.



## Security

**New and Changed Features**

- Device Encryption / Secure Storage
  - Device encryption:
    - Internal storage encryption has been added.
    - External storage encryption has been added.
  - Secure erase has been added.
- Trusted Execution Environment
  - A C# TEE Client API has been added:
    - This API only works on devices supporting TEE.
- App-defined Privilege
  - The ways to define and declare an app-defined privilege have been added.
- Privilege List
  - In mobile and wearable profiles, the following privilege has been added:
    - Native
      - `zigbee` / `zigbee.admin`
  - In mobile and wearable profiles, the following privilege has been removed:
    - Web
      - `nfc.admin`
  - In mobile, wearable, and TV profiles, the following privileges have been added:
    - C#
      - `tee.client`
    - Web
      - `apphistory.read`



## Service Framework

**New and Changed Features**

- Sensor
  - Sensor URIs for existing sensors have been defined.
  - An API for getting sensor handles with their URIs has been added.
  - An API that allows applications to define their own sensors and publish data through the defined sensors has been added.
- PIMS
  - Calendar
    - In the TV profile, Calendar Service has been added.
    - APIs for event aggregation have been added.
- Convergence
  - FIDO
    - The FIDO Platform ASM module has been added, supporting pluggable FIDO authenticators. Both Bound and Roaming type (Connectivity type: BT) are supported.
    - A FIDO platform authenticator has been added based on auth-fw.
      > **Note**
      >
      > The authenticator is not FIDO-certified and does not work for commercial FIDO servers.
  - Push
    - A service app checking routine has been added.
    - Install/uninstall for multiuser has been added.
    - Delivery of push messages when the application is in freeze state has been added.
  - Account Manager
    - Notification for deletions by package name has been added (in mobile and wearable profiles).
    - An "ADD button" string has been added in My-account setting application (in the wearable profile).
    - An accounts view for showing registered account providers has been added (in the wearable profile).
  - Sync Manager
    - Application enable/disable has been added (in mobile and wearable profiles).

**Fixes**

- Convergence
  - Push
    - The bug in `push_request_unread_notification` has been fixed.
    - The bug causing a crash when there is no record in the reg table has been fixed.
    - Wrong notification posting has been fixed.
    - Lazy mount dependency has been removed.
  - Account Manager
    - The conf name in the service file for `CapabilityBoundingSet` has been fixed (in mobile and wearable profiles).
    - The Global DB path for the owner user has been fixed (in mobile and wearable profiles).
    - Timing for drawing the main UI has been fixed (in the wearable profile).
  - Sync Manager
    - The application control for sync-service has been changed to aul (in mobile and wearable profiles).
    - The runtime profile build dependency has been removed (in mobile and wearable profiles).



## Web Framework

**New and Changed Features**

- HTML5/W3C APIs  
  Open source chromium M56 version has been applied for the Tizen 4.0 Web browser and Web application runtime engine. The following HTML5/W3C standard feature/APIs have been applied:
  - Shadow DOM v1
    - A method has been added for combining multiple DOM trees into a single hierarchy and determining how these trees interact with each other within a document, thus enabling better composition of the DOM.
  - Pointer Events
    - A unified pointer input API has been added, subsuming MouseEvent and TouchEvents.
  - WebGL&trade; 2
    - OpenGL&reg; ES 3.0-level rendering capabilities are provided through the &lt;canvas&gt; element.
  - Credential Management API
    - A programmatic interface is provided for the browser credential manager.
  - ECMAScript6 classes
    - A much simpler and clearer syntax is provided to create objects and deal with inheritance.
  - ECMAScript7 Async and Await
    - The language-level model for writing asynchronous code in ECMAScript has been improved.



## Tizen .NET

**New and Changed Features**

- Xamarin.Forms
  - Xamarin.Forms version 2.3.5 is supported and new .NET APIs have been added:
    - Background
    - CalendarView
    - RadioButton
    - DateTimeView
    - ContextPopup
    - Dialog
    - GridView
- C# 3D UI Framework
  - A new UI framework has been added.
- C# Device API
  - APIs have been added based on native APIs:
    - account-svc
    - bundle
    - capi-appfw-application
    - capi-appfw-app-manager
    - capi-appfw-service-application
    - capi-message-port
    - badge
    - capi-content-media-content
    - capi-system-device
    - web-url-download
    - feedback
    - capi-geofence-manager
    - capi-location-manager
    - Media Controller
    - capi-media-vision
    - capi-content-mime-type
    - capi-media-audio-io
    - capi-media-codec
    - capi-media-metadata-extractor
    - capi-media-player
    - capi-media-sound-manager
    - capi-media-tool
    - capi-media-recorder
    - NFC
    - Smartcard
    - capi-network-connection
    - capi-network-wifi
    - capi-network-wifimanager
    - notification
    - liboauth2
    - capi-appfw-package-manager
    - privilege-info
    - Push
    - key-manager
    - capi-sensor
    - stt
    - capi-system-info
    - libstorage
    - system-settings
    - capi-telephony
    - ttrace
    - tts
    - appcore-widget
    - widget_service
    - capi-network-wifi-direct
    - capi-system-runtime-info
    - Bluetooth
    - capi-media-camera
    - capi-maps-service
    - capi-media-screen-mirroring
    - capi-media-streamrecorder
    - widget_viewer_evas
    - capi-ui-inputmethod-manager
    - capi-media-thumbnail-util
    - capi-media-metadata-editor
    - capi-data-control
    - capi-media-tone-player
    - capi-media-wav-player
    - capi-messaging-messages
    - capi-messaging-email
    - fido-client
    - Alarm
    - capi-tee
    - capi-media-radio
    - voice-control



## SCM

**New and Changed Features**

- Build Environment
  - OS: Opensuse Leap 42.1
  - OBS version: 2.7.3
  - GBS version: 0.24.6
  - MIC version: 0.27.4
  - Tizen Service Repository: [http://download.tizen.org/services/archive/17.06/](http://download.tizen.org/services/archive/17.06/)
  - Tizen Tools Repository: [http://download.tizen.org/tools/archive/17.01.2/](http://download.tizen.org/tools/archive/17.01.2/)
- gcc
  - Version has been upgraded from 4.9.2 to 6.2.1 (Linaro '16 Dec version).
  - Language C++11 is fully supported.
  - The C++ runtime library (libstdc++) uses a new ABI by default. A Dual ABI is provided by the library.
  - Sanitizer features have been improved for arm and aarch64.
  - fortran and libfortran have been added.
  - License files have been added to all subcomponents.
  - 64-bit libraries are provided on a 32-bit build environment.
  - The libcc1 build has been enabled.
- glibc
  - Version has been upgraded from 2.20 to 2.24 (FSF '16 Aug version).
  - `readdir_r` has been deprecated since 2.24.
  - License files have been added to all subcomponents.
  - 64-bit libraries are provided on a 32-bit build environment.
- Upgraded Toolchain-related Packages
  - Binutils: From 2.25 to 2.27 (FSF '16 Aug version)
  - Gmp: From 6.0.0 to 6.1.1
  - Mpc: From 1.0 to 1.0.3
  - Mpfr: From 3.1.2 to 3.1.5
  - Isl: From 0.12.2 to 0.17.1

**Fixes**

- gcc
  - The [asan/lsan] possible deadlock in dynamic ASan runtime thread initialization has been fixed.
- glibc
  - The `fts_set` redirect bug has been fixed.
- binutils
  - A backport fix for PR 17704 from upstream has been implemented.
