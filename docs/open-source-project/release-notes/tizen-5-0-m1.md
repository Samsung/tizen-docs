# Tizen 5.0 Public M1 release

Release date: May. 31, 2018


## System (Kernel and System framework)

### New and changed features

- Security improvement on D-bus
  - Default deny is applied to D-bus/Cynara conf files.
  - D-bus is removed from Public Whitelist.
- Refactoring
  - Deviced, Storaged, Feedbackd
    - EFL dependency (edbus, ecore-core) is removed and replaced by Gdbus.
  - Deviced, Deviced HAL
    - Configfs/Functionfs kernel drivers are supported for better portability.
- New APIs
  - Gumd
    - APIs are added for Container and Platform Upgrade.
  - Storaged
    - C# APIs are added for external storage.
  - Deviced
    - Multi-led internal APIs are added.
  - Tizen-Platform-Config
    - UID-based APIs are added.
- Testsuite
  - Deviced, Storaged, Feedbackd.
    - Auto-test is added and developed.
  - Usb-host
    - C# TCT is improved.

### Fixes

- Deviced
  - Developed safe unmount on writable partitions.
- Deviced, Storaged, Feedbackd
  - Race condition during dbus activation is fixed.
- Dlog
  - Crash or blocking issues are fixed.

### Known Issues

- Dbus-glib (deprecated library) is being removed from Public Tizen.


## System (Base)

### New and changed features

- Upgraded the following open source libraries:
  - augeas (1.10.1)
  - dash (0.5.9.1)
  - expat (2.2.5)
  - file (5.32)
  - hostname (3.2)
  - kbd (2.0.4)
  - libarchive (3.3.2)
  - libdatrie (0.2.10)
  - libjson (0.13.1)
  - libxml2 (2.9.7)
  - libxslt (1.1.31)
  - libzio (1.06)
  - lua (5.1.5)
  - lzop (1.04.01)
  - pcre (8.41)
  - procps-ng (3.3.12)
  - pygobject2 (2.28.6)
  - python3 (3.6.3)
  - re2 (20180201)
  - re2c (1.0.3)
  - sqlite3 (3.21.0)
  - xz (5.2.3)
  - zip (1.5.1)
- Expanded the capi-base-utils API set:
  - plural format
  - immutable_idx
  - date interval
  - date interval format
- Expanded the capi-system-settings API set:
  - Added system-settings key value
    - SYSTEM_SETTINGS_KEY_AUTOMATIC_TIME_UPDATE
    - SYSTEM_SETTINGS_KEY_DEVELOPER_OPTION_STATE
  - Added feature for font to support IoT
    - tizen.org/feature/systemsetting.font
  - Added multi notification callback API
    - system_settings_add_changed_cb()
    - system_settings_remove_changed_cb()

### Fixes

- upstream/json-c
  - The libjson package name has been changed to libjson4.


## Application framework

### New and changed features

- TIDL (Tizen Interface Definition Language), rpc-port
  - Introduced a new app rpc-port to app IPC mechanism.
  - Introduced TIDL to support RPC style IPC between applications.
  - Applications can expose RPC style service interface to other applications with TIDL.
  - Native code is generated from the TIDL with tidlc compiler.
  - C, C++, C# languages are supported.
  - tidlc compiler will be released along with the Tizen Studio.
- Watchface complication framework and stylize editable feature support:
  - Applications can provide custom complication data with the new watchface complication provider API.
  - Watchface applications can receive data from the complication providers.
  - Watchface applications can register editable design elements and an user will be able to edit the watchface with editor UI.
- Widget framework refactoring:
  - Screen connector library is rewritten in object-oriented design.
- Package Manager
  - Added API for changing applications’ icon.
  - Changed some enum values for fixing errata.
  - Added new enum value for extended storage.


## Window system

### New and changed features

- Wayland
  - Upgraded the opensource wayland to version 1.14.0.
  - The opensource wayland-protocols is upgraded to the version 1.12, which has xdg_shell_unstable_v6 protocol. The directory path of xdg-shell protocol unstable version 5 is moved to protocol/unstable/xdg-shell from protocol/tizen.
- Extended wayland protocols
  - tizen_keyrouter protocol is upgraded to the version 2 to support the event_surface which is newly added.
- Enlightenment wayland display server
  - keyrouter functionalities is moved from Enlightenment modules to the Enlightenment core.
  - Added support for xdg_shell_unstable_v6 protocol.
  - Added e_input and e_input_device to replace input functionalities of the ecore drm.
  - Applied Dbus policy to org.enlightenment.wm.conf.
  - The debugging tool is extended with the following support:
    - bgcolor_set:  change the background color of canvas to check compositing of the enlightenment.
    - deiconify_approve: enable and disable deiconify_approve function in run time.
    - buffer_flush: enable and disable buffer flush function in run time.
- Tizen ws shell 
  - Tizen ws shell has changed to use ecore_wl2 instead of ecore_wayland to support EFL 1.20.
- efl-util
  - efl-util has changed to use ecore_wl2 instead of ecore_wayland to support EFL 1.20.
- pepper
  - Added pepper-devicemgr module to support key event generation for the IoT device.
- Wayland TBM
  - Added test cases for wayland TBM.
  - Added wayland_tbm_client_queue_get_surfaces API.
  - Added wayland_tbm_server_client_queue_send_buffer_usable API.
- Tizen HAL
  - TBM(Tizen Buffer Manager)
    - Added test cases for TBM HAL.
    - Added tbm_bufmgr_server_init API.
      - The display server calls the tbm_bufmgr_server_init and this API is used in the place of setting the TBM_DISPLAY_SERVER env variable. 
    - Added tbm_bufmgr_set_bo_lock_type API.
      - This API is used in the place of setting the BUFMGR_LOCK_TYPE env variables.
    - Added tbm_surface_internal_set/get_damage APIs.
    - Added tbm_bo.h file that contains the tbm_bo APIs.
    - Added new backend file (tbm_backend.h) and new HAL APIs.
      - The legacy backend file(tbm_bufmgr_backend.h) will be deprecated.
      - The tbm backend module needs to re-implement its backend module with the new backend file(tbm_backend.h).
      - The new features will be supported under the new backend APIs.
    - The front end API returns the error type.
      - The front end API can get the error type that comes from the back end module.
  - TDM(Tizen Display Manager)
    - Added test cases for TDM HAL.
    - Added APIs for the TDM-HWC.
    - The libtbm uses the configuration file intead of using the environment variables.
  - TPL-EGL(Tizen Porting Layer for EGL)
    - libwayland-egl-tizen package is provided.
      - This contains the development header files for wayland-egl Tizen extensions.
    - Added the new backend type TPL_BACKEND_WAYLAND_VULKAN_WSI_THREAD for Vulkan HWC.
      - Added the event-thread to process wayland event.
      - The sub-thread waits for the sync_fd to know the draw_done of the buffers.
      - The four present mode is supported with the draw_done and tdm_client_vblank.
- Vulkan
  - vulkan-wsi-tizen
    - It uses the TPL_BACKEND_WAYLAND_VULKAN_WSI_THREAD type of the TPL-EGL backend by default.
    - It supports the user allocator which can register the allocation callback by the vulkan application.
  - Vulkan-LoaderAndValidationLayers
    - Updated from the upstream to version 1.0.5.
    - Enabled the validation layers.
  - New packages
    - Added the glslang package.
    - Added the SPIRV-Tools package.
    - Added the SPIRV-Headers package.

### Fixes

- Enlightenment wayland display server
  - Fixed attempting to flush window buffer for the keyboard window.
  - Fixed many code defects detected by the static analysis tool.
- Pepper
  - Fixed many code defects detected by the static analysis tool.


## Graphics engine

### New and changed features

- DALi (3D UI Toolkit)
  - Common
    - Added MS Windows backend.
  - Actor and Renderer
    - Added opacity property to Renderer.
    - Added mechanism for registering child properties on arbitrary actor.
    - Added ChildAdded and ChildRemoved signals.
  - Performance Profiling
    - Added trace functionality using Performance Server.
  - Image
    - Added crop and resize APIs to PixelBuffer.
    - Added support for Exif image metadata to PixelBuffer.
    - API to multiply alpha into color channels is added to PixelBuffer.
    - Added support for remote GIF images.
    - Added loop count and playback control support for GIF images.
  - Video
    - Added support for display mode.
    - Added support for codec type and seek functionality.
  - Input
    - Added InputMethod enumerations.
  - Text
    - Memory consumption of TextLabel is reduced.
    - Support for text background is added to TextLabel.
  - Control and Visual
    - A property to keep aspect ratio is added to Visual.
    - Added support for setting a default image.
    - Added support for basic layout functionality.
  - NUI (C# interface)
    - ImfManager class is replaced with InputMethodContext class.
    - Added support for XAML.
    - Added support for mouse wheel event in Window.
- Evas Render Engine
  - Support tbm gl/sw rendering engine for EFL 1.20

### Fixes

- DALi (3D UI Toolkit)
  - Loading of compressed texture formats bug is fixed.
  - A crash in multi-threading environment is fixed.
- Evas Redner Engine
  - Bug of glGetString in EvasGL is fixed.
  - Resource leak in evas engines is fixed.

### Known Issues
- DALi (3D UI Toolkit)
  - Indicator is not working properly.
- Evas Render Engine
  - Multiple EvasGL Images are not working properly.


## UI framework
 
### New and changed features

- EFL
  - Version 1.16 is upgraded to 1.20
  - Edbus and Eldbus is removed for security reasons.
  - Elementary repository is integrated into EFL repository.
  - Added SVG morphing animation.
  - Ecore_wayland is replaced with ecore_wayland2.
  - Added GBS incremental build support.
- Fontconfig
  - Version 2.12.1 is upgraded to 2.13.
- Freetype2
  - Version 2.8 is upgraded to 2.9.
- Fribidi
  - Version 0.19.7 is upgraded to 1.0.2.
- Atk
  - Version 2.16.0 is upgraded to 2.18.1.
- At-spi2-core
  - Version 2.16.1 is upgraded to 2.26.1.
- At-spi2-atk
  - Version 2.16.0 is upgraded to 2.26.1.
- Text Input
  - Added auto-fill hint enumeration and APIs for keyboard prediction.
  - Applied Updated the reference TV IME GUI option in UI.
  - Added keyboard tutorial for wearable profile.
- Voice Interaction
  - Downloadable voice control engine support
  - Added TTS API for repeat function.
  - Added new APIs for supporting third party voice control engine.

### Fixes
- Fixed bugs.
- Added Thread-safety check.
- Improved evas rendering performance.
- Stabilized evas rendering mechanism.

### Known Issues
- CBHM (Clip Board History Manager) is not work properly
- Ector supports only basic functionalities compared to Cairo
- SVG morphing animation supports only in EDC
- Elementary focus manager is disabled (legacy focus mechanism is applied)


## Multimedia framework

### New and changed features

- Media Player
  - Added support for spherical video playback.
  - Added support for replaygain.
  - Removed session based audio API.
  - Pre-condition of settting ROI area API is changed.
  - The “player_set_display()” must be called in main thread of application by restriction of upgraded EFL.
- MediaCodec
  - Added H/W resource management.
  - Added the error enum for resource conflict.
- MediaTool
  - NAdded new APIs for rotation method.
- Radio
  - Removed session based audio API.
- Camera
  - Increase the maximum camera number.(2 -> 10)
  - Added new APIs for hue.
  - A display ROI area can be set before display mode is set as ROI mode.
  - The “camera_set_display()” must be called in main thread of application by restriction of upgraded EFL.
  - Added a dependency of libmm-display-interface.
    - Removed the dependencies of display related packages.
    - “libmm-display”  must be included in platform binary to use display related APIs.
  - New package is added to separate camera API test program from “capi-media-camera” package.
    - “capi-media-camera-tool” must be installed to use “camera_test”
- Recorder
  - A related feature is changed.
    - As-Is: <http://tizen.org/feature/camera>, <http://tizen.org/feature/microphone>
    - To-Be: <http://tizen.org/feature/media.audio_recording>, <http://tizen.org/feature/media.video_recording>
  - New package is added to separate recorder API test program from capi-media-recorder package
    - “capi-media-recorder-tool” must be installed to use “recorder_test”.
- Media Content
  - Added synchronous thumbnail creation API and old asynchronous API is deprecated.
  - Added support for contents moving between internal or SD Card and USB Storage.
- Media Controller
  - Added playback position, shuffle mode, repeat mode control APIs.
  - Added playback action APIs to replace Playback state APIs. And some playback states has changed.
  - Added support for playlist.
  - Added support for response of the request.
- Image Util
  - Deprecated support for hardware acceleration.
- Thumbnail Util
  - Added synchronous thumbnail creation API and old asynchronous API is deprecated.
- Video Util
  - Deprecated video Util API package.
- Opensource Upgrade
  - Tiff 4.0.7 -> 4.0.9
  - GStreamer 1.6.1 -> 1.12.2
  - Pulseaudio 5.0 -> 11.1


## Network and connectivity

### New and changed features

- Network Monitoring (In-house only module)
  - Added support for ethernet cable state feature.
  - Added support for Wi-Fi module state feature.
  - Added support for IP conflict detection feature.
  - Added support for tcpdump feature.
  - Added support for statistics feature.
  - Added support for TCP congestion feature.
  - Added support for TCP Tx retry rate feature.
  - Added support for cellular state feature.
  - Added support for Wi-Fi state feature.
  - Added support for ethernet state feature.
  - Added support for scan state feature.
  - Added support for default connection fuction.
  - Added support for getting the connection related information (e.g,. proxy address, prefix length, IP address) functions have been added
  - Added support for getting the Wi-Fi related informations (e.g,. BSSID, ESSID, RSSI level, frequency) functions have been added
- Network Firewall
  - Added support for In-bound/out-bound rule management.
  - Added support for IP, port and protocol type control.
  - Added support for Accept, Drop and Log targets.
  - Added support for IPv4 and IPv6 rules.
  - Added support for rule chain management.
  - Added support for Tunneling functions.
  - Added support for lock/unlock functions.
- Multipath TCP (In-house only module)
  - Added new feature for multipath TCP support.
    - Added a connection API (In-house only) for enabling the multipath TCP function.
    - Added a connection API (In-house only) for setting the path-manager for multipath TCP.
    - Added a connection API (In-house only) for setting the scheduling for multipath TCP.
- TCP Fast Open
  - Added a http API for allowing TCP Fast Open.
- SoftAP
  - capi-network-softap is open to the public API from the internal API.
- MTP FunctionFS
  - FunctionFS is added in USB File System which is based on MTP operations.
- Wi-Fi Native CAPI
  - Removed capi-wifi, and replaced it with capi-wifi-manager.
  - New features and APIs in mobile, wearable, and TV profiles:
    - Added a wifi-manager API for getting all the VSIE(Vendor Specific Information Elements) of AP.
    - Added a wifi-manager API for getting the WPS PIN number.
    - Added a wifi-manager API for getting the country code.
    - Added a wifi-manager API for getting the BSSID list.
    - Added support for EAP-FAST, EAP-PWD and EAP-AKA-PRIME.
- Wi-Fi Direct Native CAPI
  - New features and APIs in mobile, wearable, and TV profiles:
    - Added a wifi-direct API for getting the peer VSIE(Vendor Specific Information Elements).
    - Added a wifi-direct API for creating Wi-Fi direct group with SSID.
    - Added a wifi-direct API for setting/getting the intent of the group owner for each connection type.
    - Added a wifi-direct API for set/unset the notification for peer device info connection state.
    - Added a wifi-direct API for setting/getting the WPS config method.
    - Added a wifi-direct API for removing the persistent device or devices.
- Telephony
  - Removed voicecall state based API.
  - Removed videocall state based API.
  - Removed poweroff wait sequence for CP detach.
- Bluetooth CAPI
  - Old GATT APIs have been removed, these APIs were deprecated in Tizen 2.3.1
  - New features and APIs in mobile, wearable, and TV profiles:
    - Added a delay report API for AVRCP streaming (in-house only).
  - Added callback API for AVRCP delay changed (in-house only).
- Open Source Upgrade
  - wpa_supplicant: 2.5 to 2.6.
  - connman: 1.29 to 1.35.
  - pacrunner: 0.7 to 0.9
  - curl: 7.53.1 to 7.59
  - bluez: 5.43 to 5.48

### Fixes

- Data Network
  - Removed a gdbus dependency in network related UGs (e.g,.ug-wifi-efl, ug-wifi-direct, download-manager)
- IoT Connectivity.
  - Iotivity is stabilized in multi-thread programming.


## Security

### New and changed features

- Security Event Collector
  - Added support for kernel level audit.
  - Added major protection profiles(CAPP, LSPP, PCI-DSS, NISPOM, STIG).
- Security Analyzer
  - Provide general information of Tizen security
  - Provide access control information of running processes
  - Check security related logs
  - Provide basic guides for developers


## Service framework

### New and changed features

- Account
  - Account module is added in TV profile.

### Fixes

- Phonenumber-util
  - Fixed D-Bus policies
  - Fixed memory leaks & potential defects
- Account-Manager
  - Fixed D-Bus Policies
  - Fixed Memory leaks & potential defects
- Sync-manager
  - Fixed D-bus policies
  - Fixed memory leak & potential defects
- Geofence-server
  - Fixed D-bus policies
  - Fixed memory leak & potential defects
- LBS Server
  - Fixed D-bus policies
  - Fixed memory leak & potential defects
- Maps-plugin-here
  - Fixed D-bus policies
  - Fixed memory leak & potential defects.
- Sensor
  - Fixed Memory leaks & potenatil defects
- Email
  - Fixed memory leak & potential defects
- Message-Service
  - Fixed memory leaks & potential defects
- Context
  - Fixed memory leaks & potential defects
- Calendar
  - Fixed memory leaks & potential defects
- Location 
  - Fixed memory leaks & potential defects


## Web framework

### New and changed features

- Web engine
  - Applying latest open source chromium(blink) : from M56 to M63
    - Provide new W3C Standard  (Animated PNG, Full featured Indexed DB, CSS grid layout, Web USB, MSE/EME)
    - Enhancement standard web features (WebRTC, ARIA 1.1)
    - Web performance enhancement (V8 : ES 6 performance enhancement, Web Assembly default enabling)


## Tizen .NET

### New and changed features

- .NET Runtime
  - Merged memory optmization patches.
- .NET Launcher
  - Plugin interface for dll preloading is added.
- Xamarin.Forms
  - Latest Xamarin.Forms stable version (3.0.0) support.
  - Xamarin.Forms nuget package (Xamarin.Forms.nupkg) supports tizen as a default platform since Xamarin.Forms 3.0.0.
  - TargetIdiom.Watch is now available for wearable profile since Xamarin.Forms 3.1 Pre Release 1.2.
- Tizen.CircularUI
  - Circular UI extension (Tizen.CircularUI) is now available.
- TizenFX
  - Added support for Application Filter by installed location.
  - Added enumeration and method for StorageDevice.
  - Added audio only mode for Player.
  - Added attach Panel.
  - Added support for multiple camera and hue.
  - Added system settings for vibration, time update, developer option state.
  - Added support for Wi-Fi AP update.
  - NUI Version 0.2.66 is upgraded to 0.2.83.
  - Added USB Host API.
  - Tizen.Security.Privilege.GetPrivacyPrivilegeStatus() is deprecated.
  - Added 360 videos support in Tizen.Multimedia.Player.

### Known Issues

- Xamarin.Forms
  - For more information on the list of limitations, see [here](https://developer.tizen.org/ko/development/api-reference/.net-application/current-xamarin.forms-limitations?langredirect=1)


## Experimental

### New and changed features

- nnfw: Neural Network Runtime (Experimental Release)
  - CPU/GPU acceleration support based on ACL(Arm Compute Library) (currently 6 operators)
  - Android NN API compatible (currently 17/29 API support)
  - TenworFlow Lite compatible (currently supports 6/50 operators)
  - Run Inception V3 model
