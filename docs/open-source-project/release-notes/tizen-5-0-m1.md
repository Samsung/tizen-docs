# Tizen 5.0 Public M1 Release

**Release Date: [May. 31, 2018]**

 

## **System (Kernel and System Framework)**

**New and Changed Features**

​	**·**        **Security improvement on D-bus**

​		**o**   **Default deny has been applied to D-bus/Cynara conf files.**

​		**o**   **D-bus has been removed from Public Whitelist.**

​	**·**        Refactoring

​		o   Deviced, Storaged, Feedbackd

​			**§**  EFL dependency (edbus, ecore-core) has been removed and replaced by Gdbus.

​		o   Deviced, Deviced HAL

​			§  Configfs/Functionfs kernel driver support for better portability.

​	**·**        New APIs

​		**o**   **Gumd**

​			**§**  **New APIs have been added for Container and Platform Upgrade**

​		**o**   **Storaged**

​			**§**  **New C# APIs for external storage have been added**

​		**o**   **Deviced**

​			**§**  **Multi-led internal APIs have been added.**

​		**o**   **Tizen-Platform-Config**

​			**§**  **UID-based APIs have been added.**

​	**·**        **Testsuite**

​		**o**   **Deviced, Storaged, Feedbackd**

​			**§**  **Auto-test has been added and developed.**

​		**o**   **Usb-host**

​			**§**  **C# TCT has been improved.**

**Fixes**

​	**·**        **Deviced**

​		**o**   **Safe umount on writable partions has been developed.**

​	**·**        **Deviced, Storaged, Feedbackd**

​		**o**   **Race condition during dbus activation has been fixed.**

​	**·**        **Dlog**

​		**o**   **Crash/Blocking issues have been fixed.**

**Known Issues**

​	**·**        **Dbus-glib (deprecated library) is being removed from Public Tizen.**

 

## **System (Base)**

 **New and Changed Features**

​	**·**        **The following open-source libraries have been upgraded:**

​		**o**   **augeas (1.10.1)**

​		**o**   **dash (0.5.9.1)**

​		**o**   **expat (2.2.5)**

​		**o**   **file (5.32)**

​		**o**   **hostname (3.2)**

​		**o**   **kbd (2.0.4)**

​		**o**   **libarchive (3.3.2)**

​		**o**   **libdatrie (0.2.10)**

​		**o**   **libjson (0.13.1)**

​		**o**   **libxml2 (2.9.7)**

​		**o**   **libxslt (1.1.31)**

​		**o**   **libzio (1.06)**

​		**o**   **lua (5.1.5)**

​		**o**   **lzop (1.04.01)**

​		**o**   **pcre (8.41)**

​		**o**   **procps-ng (3.3.12)**

​		**o**   **pygobject2 (2.28.6)**

​		**o**   **python3 (3.6.3)**

​		**o**   **re2 (20180201)**

​		**o**   **re2c (1.0.3)**

​		**o**   **sqlite3 (3.21.0)**

​		**o**   **xz (5.2.3)**

​		**o**   **zip (1.5.1)**

​	·        **The capi-base-utils API set has been expanded:**

​		o   plural format

​		o   immutable_idx

​		o   date interval

​		**o**   date interval format

​	**·**        **The capi-system-settings API set has been expanded:**

​		**o**   **Add system-settings key value**

​			§  SYSTEM_SETTINGS_KEY_AUTOMATIC_TIME_UPDATE

​			§  SYSTEM_SETTINGS_KEY_DEVELOPER_OPTION_STATE

​		**o**   **Added feature for font to support IoT.**

​			§  tizen.org/feature/systemsetting.font

​		**o**   **Added multi notification callback API**

​			§  system_settings_add_changed_cb( )

​		**o**   system_settings_remove_changed_cb( )

**Fixes**

​	**·**        **upstream/json-c**

​		**o**   **The libjson package name has been changed to libjson4.**

 

## **Application Framework**

 **New and Changed Features**

​	**·**        **TIDL (Tizen Interface Definition Language), rpc-port**

​		**o**   **A new app to app IPC mechanism, rpc-port has been introduced.**

​		**o**   **TIDL has been introduced to support RPC style IPC between applications.**

​		**o**   **Applications can expose RPC style service interface to other applications with TIDL.**

​		**o**   **Native code is generated from the TIDL with tidlc compiler.**

​		**o**   **C, C++, C# languages are supported.**

​		**o**   **tidlc compiler will be released with the Tizen Studio.**

​	**·**        **Watchface Complication Framework, Stylize Editable Feature Support**

​		**o**   **Applications can provides custom complication data with the new watchface complication provider API.**

​		**o**   **Watchface applications can receive data from the complication providers.**

​		**o**   **Watchface applications can register editable design elements and an user will be able to edit the watchface with editor UI.**

​	**·**        **Widget Framework Refactoring**

​		**o**   **Screen connector library has been rewritten in object-oriented design.**

​	**·**        **Package Manager**

​		**o**   **API for changing applications’ icon has been added.**

​		**o**   **Some enum values for fixing errata has been changed.**

​		**o**   **New enum value for extended storage has been added**

**Known Issues**

​	**·**        **N/A**



## **Window System**

 **New and Changed Features**

​	**·**        wayland

​		**o**   The opensource wayland has been upgraded to       the 1.14.0 version.

- - **o**   The opensource  wayland-protocols has been upgraded to the 1.12 version which has xdg_shell_unstable_v6 protocol. And directory path of xdg-shell protocol unstable version 5 has been moved to protocol/unstable/xdg-shell from protocol/tizen.

  - ·        Extended Wayland Protocols

  - ​	o   tizen_keyrouter protocol has been upgraded to the 2 version to support new event_surface.

  - **·**        **Enlightenment Wayland Display Server**

  - ​	o   **keyrouter functionalities have been moved from Enlightenment modules to the Enlightenment core.**

  - ​	**o**   **Support for xdg_shell_unstable_v6 protocol has been added.**

  - ​	**o**   **e_input and e_input_device have been added to replace input functionalities of the ecore drm.**

  - ​	o   **Dbus policy has applied to org.enlightenment.wm.conf.** 

  - ​	**o**   **The debugging tool has been extended with support for:**

  - ​		**§**  **bgcolor_set:  change the background color of canvas to check compositing of the enlightenment.**

  - ​		**§**  **deiconify_approve: enable and disable deiconify_approve function in run-time.**

  - ​		**§**  **buffer_flush: enable and disable buffer flush function in run-time.**

  - **·**        **Tizen ws Shell** 

  - ​	**o**   **Tizen ws shell has changed to use ecore_wl2 instead of ecore_wayland to support EFL 1.20.**

  - **·**        **efl-util**
    ​	**o**   efl-util has changed to use ecore_wl2 instead       of ecore_wayland to support EFL 1.20.

  - **·**        pepper

  - ​	**o**   **pepper-devicemgr module has been added to support key event generation for the IoT device.**

  - **·**        **Wayland TBM**

  - ​	**o**   **The test cases of Wayland TBM have been added.**

  - ​	**o**   **The wayland_tbm_client_queue_get_surfaces api has beed added.**

  - ​	**o**   **The wayland_tbm_server_client_queue_send_buffer_usable api has beed added.**

  - **·**        **Tizen HAL**

  - ​	**o**   **TBM(Tizen Buffer Manager)**

  - ​		**§**  **The test cases for TBM HAL have been added.**

  - ​		**§**   **The tbm_bufmgr_server_init api has beed added.**

  - ​			**·**        **The tbm_bufmgr_server_init is called by the display server. This api will be used instead of setting the TBM_DISPLAY_SERVER env variable.** 

  - ​		**§**  **The tbm_bufmgr_set_bo_lock_type api has beed added.**

  - ​			**·**        **This api is used intead of setting the BUFMGR_LOCK_TYPE env variables.**

  - ​		**§**  **The tbm_surface_internal_set/get_damage have been added.**

  - ​		**§**  **The tbm_bo.h file which contains the tbm_bo APIs has been added.**

  - ​		**§**  **The new backend file(tbm_backend.h) and APIs(The new HAL APIs) have been added.**

  - ​			**·**        **The legacy backend file(tbm_bufmgr_backend.h) will be deprecated.**

  - ​			**·**        **The tbm backend module needs to re-implement its backend module with the new backend file(tbm_backend.h).**

  - ​			**·**        **The new features will be supported under the new backend APIs.**

  - ​		**§**  **The front-end api will returns the error type.**

  - ​			**·**        **The front-end api can gets the error type which comes from the backend module.**

  - ​	**o**   **TDM(Tizen Display Manager)**

  - ​		**§**  **The test cases for TDM HAL have been added.**

  - ​		**§**  **The APIs for the TDM-HWC have been added.**

  - ​		**§**  **The libtbm uses the configuration file intead of using the environment variables.**

  - ​	**o**   **TPL-EGL(Tizen Porting Layer for EGL)**

  - ​		**§**  **libwayland-egl-tizen package has been provided.**

  - ​			**·**        **This contains the development header files for wayland-egl tizen extensions.**

  - ​		**§**  **The new backend type which is TPL_BACKEND_WAYLAND_VULKAN_WSI_THREAD for Vulkan HWC has been added.**

  - ​			**·**        **The event-thread to process wayland event has been added.**

  - ​			**·**        **The sub-thread waits for the sync_fd to know the draw_done of the buffers.**

  - ​			**·**        **The four present mode has been supported with the draw_done and tdm_client_vblank.**

  - **·**        **Vulkan**

  - ​	**o**   **vulkan-wsi-tizen**

  - ​		**§**  **It uses the TPL_BACKEND_WAYLAND_VULKAN_WSI_THREAD type of the TPL-EGL backend by default.**

  - ​		**§**  **It supports the user allocator which can register the allocation callback by the vulkan application.**

  - ​	**o**   **Vulkan-LoaderAndValidationLayers**

  - ​		**§**  **It has been updated to the version 1.0.5 which gets from the upstream.**

  - ​		**§**  **The validation layers has been enabled.**

  - ​	**o**   **New packages**

  - ​		**§**  **The glslang package has been added.**

  - ​		**§**  **he SPIRV-Tools package has been added.**

  - ​		**§**  **The SPIRV-Headers package has been added.**

**Fixes**

​	**·**        **Enlightenment Wayland Display Server**

​		**o**   **Fixed attempting to flush window buffer for the keyboard window.**

​		**o**   **Many code defects detected by the static analysis tool have been fixed.**

​	**·**        **Pepper**

​		**o**   **Many code defects detected by the static analysis tool have been fixed.**

 

## **Graphics Engine**

 **New and Changed Features**

​	**·**        **DALi (3D UI Toolkit)**

​		**o**   **Common**

​			**§**  MS Windows backend has been added**.**

​		**o**   **Actor and Renderer**

​			**§**  **Opacity property has been added to Renderer.**

​			**§**  **Mechanism for registering child properties on airbitrary actor has been added.**

​			**§**  **ChildAdded and ChildRemoved signals have beend added to Actor.**

​		**o**   **Performance Profiling**

​			**§**  **Trace functionality using Performance Server has been added.**

​		**o**   **Image**

​			**§**  **Crop and resize APIs have been added to PixelBuffer.**

​			**§**  **Support for Exif image metadata has been added to PixelBuffer.**

​			**§**  **API to multiply alpha into color channels has been added to PixelBuffer.**

​			**§**  **Support for remote gif images has been added.**

​			**§**  **Loop count and playback control support for gif images have been added.**

​		**o**   **Video**

​			**§**  **Support for display mode has been added.**

​			**§**  **Support for codec type and seek functionality have been added.**

​		**o**   **Input**

​			**§**  **InputMethod enumerations have been added.**

​		**o**   **Text**

​			**§**  **Memory consumption of TextLabel has been reduced.**

​			**§**  **Support for text background has been added to TextLabel.**

​		**o**   **Control and Visual**

​			**§**  **A property to keep aspect ratio has been added to Visual.**

​			**§**  **Support for setting a default image has been added.**

​			**§**  **Support for basic layout functionality has been added.**

​		**o**   **NUI (C# interface)**

​			**§**  **ImfManager class has been replaced with InputMethodContext class.**

​			**§**  **Support for XAML has been added.**

​			**§**  **Support for mouse wheel event in Window has been added.**

​	**·**        **Evas Render Engine**

​		**o**   **Support tbm gl/sw rendering engine for EFL 1.20**

**Fixes**

​	**·**        **DALi (3D UI Toolkit)**

​		**o**   **Loading of compressed texture formats bug has been fixed.**

​		**o**   **A crash in multi-threading environment has been fixed.**

​	**·**        **Evas Redner Engine**

​		**o**   **Fix the bug of glGetString in EvasGL.**

​		**o**   **Fix resource leak in evas engines.**

**Known Issues**

​	**·**        **DALi (3D UI Toolkit)**

​		**o**   **Indicator is not working properly.**

​	**·**        **Evas Render Engine**

​		**o**   **Two evas gl images is not supported**

 

## **UI Framework**

 **New and Changed Features**

​	**·**        **EFL**

​		**o**   **Version has been upgraded from 1.16 to 1.20**

​		**o**   **Edbus and Eldbus has been removed for security reasons**

​		**o**   **Elementary repository has been integrated into EFL repository**

​		**o**   **SVG morphing animation has been added**

​		**o**   **Ecore_wayland has been replaced into ecore_wayland2**

​		**o**   **GBS incremental build support has been added**

​	**·**        **Fontconfig**

​		**o**   **Version has been upgraded from 2.12.1 to 2.13**

​	**·**        **Freetype2**

​		**o**   **Version has been upgraded from 2.8 to 2.9**

​	**·**        **Fribidi**

​		**o**   **Version has been upgraded from 0.19.7 to 1.0.2**

​	**·**        **Atk**

​		**o**   **Version has been upgraded from 2.16.0 to 2.18.1**

​	**·**        **At-spi2-core**

​		**o**   **Version has been upgraded from 2.16.1 to 2.26.1**

​	**·**        **At-spi2-atk**

​		**o**   **Version has been upgraded from 2.16.0 to 2.26.1**

​	**·**        **Text Input**

​		**o**   **Added auto-fill hint enumeration and APIs for keyboard prediction**

​		**o**   **Applied Updated the reference TV IME GUI (Option UI)**

​		**o**   **Added keyboard tutorial for wearable profile**

​	**·**        **Voice Interaction**

​		**o**   **Downloadable voice control engine support**

​		**o**   **TTS api for repeat function has been added**

​		**o**   **New APIs for supporting 3rd party voice control engine have been added**

**Fixes**

​	**·**        **Many bugs has been fixed:**

​	**·**        **Thread-safety check has been added**

​	**·**        **Evas rendering performance has been improved**

​	**·**        **Evas rendering mechanism has been stablized**

**Known Issues**

​	**·**        **CBHM (Clip Board History Manager) is not work properly**

​	**·**        **Ector supports only basic functionalities compared to Cairo**

​	**·**        **SVG morphing animation supports only in EDC**

​	**·**        **Elementary focus manager has been disabled (legacy focus mechanism is applied)**

 

## **Multimedia Framework**

 **New and Changed Features**

​	**·**        **Media Player**

​		**o**   **Support for spherical video playback has been added.**

​		**o**   **Support for replaygain has been added.**

​		**o**   **Session based audio API has been removed.**

​		**o**   **Pre-condition of settting ROI area API has been changed.**

​		**o**   **The “player_set_display()” should be called in main thread of application by restriction of upgraded EFL.**

​	**·**        **MediaCodec**

​		**o**   **The resource manager has beed added.**

​		**o**   **The error enum for resource conflict has been added.**

​	**·**        **MediaTool**

​		**o**   **New APIs for rotation method have been added.**

​	·        Radio

​		**o**   **Session based audio API has been removed.**

​	**·**        **Camera**

​		**o**   **Increase the maximum camera number.(2 -> 10)**

​		**o**   **New APIs for hue have been added.**

​		**o**   **A display ROI area can be set before display mode is set as ROI mode.**

​		**o**   **The “camera_set_display()” should be called in main thread of application by restriction of upgraded EFL.**

​		**o**   **A dependency of libmm-display-interface has been added.**

​			**§**  **Dependencies of display related packages are removed.**

​			**§**  **“libmm-display”  should be included in platform binary to use display related APIs.**

​		**o**   **New package has been added to separate camera API test program from “capi-media-camera” package.**

​			**§**  **“capi-media-camera-tool” should be installed to use “camera_test”**

​	**·**        **Recorder**

​		**o**   **A related feature is changed.**

​			**§**  **As-Is:** <http://tizen.org/feature/camera>**,** <http://tizen.org/feature/microphone>

​			**§**  **To-Be:** <http://tizen.org/feature/media.audio_recording>**,** <http://tizen.org/feature/media.video_recording>

​		**o**   **New package is added to separate recorder API test program from capi-media-recorder package**

​			**§**  **“capi-media-recorder-tool” should be installed to use “recorder_test”.**

​	**·**        **Media Content**

​		o   Synchronous thumbnail creation API has been added and old asynchronous API has been deprecated.

​		o   Support for contents moving between internal/SD Card and USB Storage has been added.

​	·        Media Controller

​		o   Playback position, shuffle mode, repeat mode control APIs has been added.

​		o   Playback action APIs has been added to replace Playback state APIs. And some playback states has been changed.

​		o   Support for playlist has been added.

​		o   Support for response of the request has been added.

​	·        Image Util

​		o   Support for hardware acceleration has been deprecated.

​	·        Thumbnail Util

​		o   Synchronous thumbnail creation API has been added and old asynchronous API has been deprecated.

​	·        Video Util

​		o   Video Util API package has been deprecated.

​	·        Opensource Upgrade

​		o   Tiff 4.0.7 -> 4.0.9

​		**o**   **GStreamer 1.6.1 -> 1.12.2**

​		**o**   **Pulseaudio 5.0 -> 11.1**

 

## **Network and Connectivity**

 **New and Changed Features**

​	**·**        **Network Monitoring (In-house only module)**

​		**o**   **Support for ethernet cable state feature has been added**

​		**o**   **Support for Wi-Fi module state feature has been added**

​		**o**   **Supported for IP conflict detection feature has been added**

​		**o**   **Supported for tcpdump feature has been added**

​		**o**   **Supported for statistics feature has been added**

​		**o**   **Supported for TCP congestion feature has been added**

​		**o**   **Supported for TCP Tx retry rate feature has been added**

​		**o**   **Supported for cellular state feature has been added**

​		**o**   **Supported for Wi-Fi state feature has been added**

​		**o**   **Supported for ethernet state feature has been added**

​		**o**   **Supported for scan state feature has been added**

​		**o**   **Supported for default connection fuction has been added**

​		**o**   **Supported for getting the connection related information (e.g,. proxy address, prefix length, IP address) functions have been added**

​		**o**   **Supported for getting the Wi-Fi related informations (e.g,. BSSID, ESSID, RSSI level, frequency) functions have been added**

​	**·**        **Network Firewall**

​		**o**   **Supported for In-bound/out-bound rule management has been added**

​		**o**   **Supported for IP, port and protocol type control has been added**

​		**o**   **Supported for Accept, Drop and Log targets has been added**

​		**o**   **Supported for IPv4 and IPv6 rules has been added**

​		**o**   **Supported for rule chain management has been added**

​		**o**   **Supported for Tunneling functions has been added**

​		**o**   **Supported for lock/unlock functions has been added**

​	**·**        **Multipath TCP (In-house only module)**

​		**o**   **New feature for multipath TCP support has been added**

​			**§**  **A connection API (In-house only) for enabling the multipath TCP function has been added**

​		**§**  **A connection API (In-house only) for setting the path-manager for multipath TCP has been added**

​			**§**  **A connection API (In-house only) for setting the scheduling for multipath TCP has been added**

​	**·**        **TCP Fast Open**

​		**o**   **A http API for allowing TCP Fast Open has been added**

​	**·**        **SoftAP**

​		**o**   **capi-network-softap has been open to the public**

​	**·**        **MTP FunctionFS**

​		**o**   **FunctionFS has been added in USB File System which is based on MTP operation**

​	**·**        **Wi-Fi Native CAPI**

​		**o**   **capi-wifi has been removed and instead, capi-wifi-manager has been replaced**

​		**o**   **New features and APIs** in mobile, wearable, and TV profiles**:**

​			§  **A wifi-manager** API for getting the all VSIE(**Vendor Specific Information Elements)** of AP has been added.

​			§  **A wifi-manager** API for getting the WPS PIN number has been added.

​			§  **A wifi-manager** API for getting the country code has been added.

​			§  **A wifi-manager** API for getting the BSSID list has been added.

​			§  **Supported for** EAP-FAST, EAP-PWD and EAP-AKA-PRIME has been added.

​	**·**        **Wi-Fi Direct Native CAPI**

​		**o**   **New features and APIs** in mobile, wearable, and TV profiles**:**

​			**§**  **A wifi-direct API for getting the peer VSIE(Vendor Specific Information Elements) has been added**

​			**§**  **A wifi-direct API for creating Wi-Fi direct group with SSID has been added**

​			**§**  **A wifi-direct API for setting/getting the intent of the group owner for each connection type has been added**

​			**§**  **A wifi-direct API for set/unset the notification for peer device info connection state has been added**

​			**§**  **A wifi-direct API for setting/getting the WPS config method has been added**

​			**§**  **A wifi-direct API for removing the persistent device or devices have been added**

​	**·**        **Telephony**

​		**o**   **Voicecall state based API has been removed.**

​		**o**   **Videocall state based API has been removed.**

​		**o**   **Poweroff wait sequence for CP detach has been applied.**

​	**·**        **Bluetooth CAPI**

​		**o**   **Old GATT APIs have been removed, these APIs were deprecated in Tizen 2.3.1**

​		**o**   **New features and APIs** in mobile, wearable, and TV profiles**:**

​			§  **A delay report API for AVRCP streaming (in-house only)** has been added.

​		**o**   **A callback API for AVRCP delay changed (in-house only)** has been added.

​	**·**        **Open Source Upgrade**

​		**o**   **wpa_supplicant: 2.5** **à** **2.6.**

​		**o**   **connman: 1.29** **à** **1.35.**

​		**o**   **pacrunner: 0.7** **à** **0.9**

​		**o**   **curl: 7.53.1** **à** **7.59**

​		**o**   **bluez: 5.43** **à** **5.48**

**Fixes**

​	**·**        **Data Network**

​		**o**   **A gdbus dependency in network related UGs (e.g,.ug-wifi-efl, ug-wifi-direct, download-manager) have been removed.**

​	**·**        **IoT Connectivity**

​		**o**   **Iotivity has been stabilized in multi-thread programming**

**Known Issues**

​	**·**        **N/A**

 

## **Security**

 **New and Changed Features**

​	**·**        **Security Event Collector**

​		**o**   **Support for kernel level audit has been added**

​		**o**   **Major protection profiles(CAPP, LSPP, PCI-DSS, NISPOM, STIG) have been added**

​	**·**        **Security Analyzer**

​		**o**   **Provide general information of Tizen security**

​		**o**   **Provide access control information of running processes**

​		**o**   **Check security related logs**

​		**o**   **Provide basic guides for developers**

 

## **Service Framework**

**New and Changed Features**

​	**·**        **Account**

​		**o**   **Account module is added in TV profile.**

**Fixes**

​	**·**        **Phonenumber-util**

​		**o**   **Fixed D-Bus policies**

​		**o**   **Fixed memory leaks & potential defects**

​	**·**        **Account-Manager**

​		**o**   **Fixed D-Bus Policies**

​		**o**   **Fixed Memory leaks & potential defects**

​	**·**        **Sync-manager**

​		**o**   **Fixed D-bus policies**

​		**o**   **Fixed memory leak & potential defects**

​	**·**        **Geofence-server**

​		**o**   **Fixed D-bus policies**

​		**o**   **Fixed memory leak & potential defects**

​	**·**        **LBS Server**

​		**o**   **Fixed D-bus policies**

​		**o**   **Fixed memory leak & potential defects**

​	**·**        **Maps-plugin-here**

​		**o**   **Fixed D-bus policies**

​		**o**   **Fixed memory leak & potential defects.**

​	**·**        **Sensor**

​		**o**   **Fixed Memory leaks & potenatil defects**

​	**·**        **Email**

​		**o**   **Fixed memory leak & potential defects**

​	**·**        **Message-Service**

​		**o**   **Fixed memory leaks & potential defects**

​	**·**        **Context**

​		**o**   **Fixed memory leaks & potential defects**

​	**·**        **Calendar**

​		**o**   **Fixed memory leaks & potential defects**

​	**·**        **Location** 

​		**o**   **Fixed memory leaks & potential defects**

##  

## **Web Framework**

 **New and Changed Features**

​	**·**        **Web Engine**

​		**o**   **Applying latest open source chromium(blink) : from M56 to M63**

​			**§**  **Provide new W3C Standard  (Animated PNG, Full featured Indexed DB, CSS grid layout, Web USB, MSE/EME)**

​			**§**  **Enhancement standard web features (WebRTC, ARIA 1.1)**

​			**§**  **Web performance enhancement (V8 : ES 6 performance enhancement, Web Assembly default enabling)**

 

## **Tizen .NET**

 **New and Changed Features**

​	**·**        **.NET Runtime**

​		**o**   **Memory optmization patches have been merged.**

​	**·**        **.NET Launcher**

​		**o**   **Plugin interface for dll preloading is added.**

​	**·**        **Xamarin.Forms**

​		**o**   **Latest Xamarin.Forms stable version (3.0.0) support.**

​		**o**   **Xamarin.Forms nuget package (Xamarin.Forms.nupkg) supports tizen as a default platform since Xamarin.Forms 3.0.0.**

​		**o**   **TargetIdiom.Watch is now available for wearable profile.**

​	·        Tizen.CircularUI

​		**o**   **Circular UI extension (Tizen.CircularUI) is now available.**

​	**·**        **TizenFX**

​		**o**   **Support for Application Filter by installed location has been added.**

​		**o**   **Enumeration and method for StorageDevice has been added.**

​		**o**   **Audio only mode for Player has been added.**

​		**o**   **Attach Panel has been added.**

​		**o**   **Support for multiple camera and hue has been added.**

​		**o**   **System settings for vibration, time update, developer option state has been added.**

​		**o**   **Support for Wi-Fi AP update has been added.**

​		**o**   **NUI Version has been upgraded from 0.2.66 to 0.2.83.**

​		**o**   **USB Host API has been added.**

​		**o**   **Tizen.Security.Privilege.GetPrivacyPrivilegeStatus() has been deprecated.**

​		**o**   **360 videos support has been added in Tizen.Multimedia.Player.**

**Known Issues**

​	**·**        **Xamarin.Forms**

​		**o**   A list of limitations is available at [here](https://developer.tizen.org/ko/development/api-reference/.net-application/current-xamarin.forms-limitations?langredirect=1)

 

## **Experimental**

 **New and Changed Features**

​	**·**        **nnfw: Neural Network Runtime (Experimental Release)**

​		**o**   **CPU/GPU acceleration support based on ACL(Arm Compute Library) (currently 6 operators)**

​		**o**   **Android NN API compatible (currently 17/29 API support)**

​		**o**   **TenworFlow Lite compatible (currently supports 6/50 operators)**

​		**o**   **Run Inception V3 model**

 