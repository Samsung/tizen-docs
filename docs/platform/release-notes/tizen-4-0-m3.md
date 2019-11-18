# Tizen 4.0 Public M3

Release date: Aug. 31, 2018

The Tizen 4.0 Public M3 release provides developers with the Tizen kernel, device drivers, middleware subsystems, and Web/Native API set.


## Release Details

- [Getting source code](http://review.tizen.org/git/) (Tizen 4.0 M2 source codes are under **tizen_4.0** branch.)

- [Getting binaries and images](http://download.tizen.org/releases/milestone/tizen/4.0-unified/)
  - Base: [http://download.tizen.org/releases/milestone/tizen/4.0-base/tizen-4.0-base_20180817.1/](http://download.tizen.org/releases/milestone/tizen/4.0-base/tizen-4.0-base_20180817.1/)
  - Mobile: [http://download.tizen.org/releases/milestone/tizen/4.0-unified/tizen-4.0-unified_20180821.6/images/standard/mobile-wayland-armv7l-tm1/](http://download.tizen.org/releases/milestone/tizen/4.0-unified/tizen-4.0-unified_20180821.6/images/standard/mobile-wayland-armv7l-tm1/)
  - Wearable: [http://download.tizen.org/releases/milestone/tizen/4.0-unified/tizen-4.0-unified_20180821.6/images/standard/wearable-wayland-armv7l-tw2/](http://download.tizen.org/releases/milestone/tizen/4.0-unified/tizen-4.0-unified_20180821.6/images/standard/wearable-wayland-armv7l-tw2/)

- [How to flash to a device](../developing/flashing.md)


## Release Notes

### System (Kernel and System Framework)

#### Fixes

- Security improvement
  - Systemd patch has been applied for CVE-2018-1049.


### System (Base)

#### New and changed features

- The following Open-source libraries have been upgraded:
  - file (5.32)
    - CVE-2018-10360
  - sqlite (3.21.0)
    - CVE-2018-8740
  - libxml (2.9.7)
    - CVE-2018-9251
  - libxslt (1.1.31)
  - procps-ng (3.3.15)
    - CVE-2018-1126, CVE-2018-1125, CVE-2018-1124, CVE-2018-1123, CVE-2018-1122
  - tzdata (2017c)
  - unzip (6.10c23)
    - CVE-2018-1000031, CVE-2018-1000032, CVE-2018-1000033
  - vim (8.0.586)


### Application Framework

#### New and changed features

- TIDL (Tizen Interface Definition Language) has been added (Mobile profile).
  - TIDL supports app-to-app RPC style IPC.
  - rpc-port API has been added to support TIDL.


### Window System

#### New and changed features

- Extended Wayland Protocols
  - The 'event_surface' event has been added to tizen_keyrouter protocol for sending the surface information before sending the key to client(s).
- Enlightenment Wayland Display Server
  - A D-Bus policy has been updated to enhance security regarding D-Bus interface.
  - A new layer has been added for e_desk_object.
  - New hooks regarding HW compositing have been provided for vendor's enlightenment module(s) to handle HWC policy properly.
- Tizen buffer HAL
  - Add the tbm_dummy_display.
  - Add the tbm_surface_internal_set/get_damage.

#### Fixes

- Enlightenment Wayland Display Server
  - The bugs regarding sending pre-unobscured visibility event have been fixed.
  - The bugs related to uniconify_render have been fixed.
  - The bug not returning to the default screen mode has been fixed.
  - The error that the quick panel doesn't disappear has been fixed.
  - The bugs related with pending position move request have been fixed.
  - The bugs related with hwc cancel condition have been fixed.
  - E_Desk smart object disorder has been fixed while zooming and maximizing member object.
  - The error of not sending touch cancel event in some special conditions has been fixed.
  - The error of not sending axis event during a touchdown operation has been fixed.


### Graphics Engine

#### New and changed features

- DALi (3D UI Toolkit)
  - Actor and Stage
    - Extents property type has been added.
  - Image
    - Support for 1, 2 and 4 bit depths of PNG has been added.
    - Support for CMYK colorspace of JPG has been added.
    - Support for screen capture has been added for a wearable device.
    - Memory usage to load GIF files has been reduced.
    - Support for remote GIF images has been added.
  - Window and Application
    - An environment variable to set the default indicator visible mode has been added.
    - New signals for battery and memory status have been added.
    - Support for widget application has been added.
  - Key event and input
    - Delete and return key handling has been added.
    - Shift+Left/Right keys support for text selection and Ctrl+C/V/X keys support for text copy/paste/cut have been added.
    - The keyboard repeat information API set have been added.
  - Text
    - Support for custom font registration has been added.
    - Support for XHTML entities has been added.
    - Support for soft shadow and outline has been added.
    - Unicode range of emoji script has been updated based on the latest Unicode specification.
    - A configuration value has been added to ignore the font size change event.
  - Control, Visual, and Style
    - MARGIN and PADDING properties have been added to Control.
    - Support for resetting an image has been added to ImageView.
    - Release policy, load policy and orientation correction properties have been added to ImageVisual.
    - API to get the visual resource status has been added to Control.
    - Support for right-to-left of padding and margin has been added to controls.
    - Text direction property has been added to TextLabel.
    - Support for 360x360 resource package has been added.
    - An auxiliary image has been added to NPatchVisual.
    - An action to reload an image has been added to ImageVisual.
    - Support for line spacing has been added to TextLabel.
  - Performance
    - Certain GL calls have been disabled when depth and/or stencil buffers are not available.
    - A PropertyRetter has been added to reset only animated or constrained properties.
    - String compares in Render have been reduced.
  - Video
    - API set to set a codec type have been added.
    - API set to set a display mode have been added.
    - API set to set a play position have been added.
  - NUI (C# interface)
    - API set to handle AGIF playback have been added.
    - Set property of VerticalLineAlignment has been added.
    - API set for KeyboardRepeatInfo of Window have been added.
    - Protection codes to avoid the crash when the IntPtr of Key class is 0 have been added.
    - Protection codes to change Registry as concurrent collection have been added.
- Evas Render Engine
  - Support for EvasGL thread separation on direct rendering mode has been added.
  - The pre-compiled shader list has been optimized for boot time enhancement.
  - Support for the Evas GL capability test has been added.
  - EGL Sync is added for EvasGL's EGLImage.

#### Fixes

- DALi (3D UI Toolkit)
  - The blending factor of premultiplied alpha format has been fixed.
  - The depth index bug has been fixed in 3D layer.
  - The bug where a depth buffer is sometimes not cleared has been fixed.
  - The bug where a render task is waiting forever has been fixed.
  - The system language change bug has been fixed.
  - When same child object is added to same parent object, an Exception was occurred. This bug has been fixed. (C# NUI)
  - Bug of memory leak problem caused by wrong increased ref-cnt has been fixed. (C# NUI)
  - Bug of View's SiblingOrder has been fixed. (C# NUI)
  - Bug of crash when getting Parent property as View has been fixed. (C# NUI)
- Evas Render Engine Enhancement
  - The resource sharing issue is fixed in Evas TBM backend.


### UI Framework

#### New and changed features

- EFL
  - Assist-panel is added.
  - Rotary Selector support edit mode.
- Voice Framework
  - Voice engine model is changed to a service app for supporting download (only for mobile and TV profile).


### Multimedia Framework

#### New and changed features

- Camera
  - New API set for hue setting have been added.
  - Maximum supported number of camera is changed from 2 to 10.
  - Pre-condition of setting ROI area API has been changed.
- Media Content
  - New Features are added.
    - http://tizen.org/feature/content.scanning.others for scanning OTHERS-type files which are not included in the media content types such as IMAGE, VIDEO, SOUND or MUSIC.
    - http://tizen.org/feature/content.filter.pinyin for supporting the Pinyin Filter. 
- Media Controller
  - In the Mobile profile, repeat mode on for one media enumeration has been added.
  - In the Mobile profile, new API set for supporting playlist have been added.
  - In the Mobile profile, new API set for sending command and receiving command reply have been added.
  - In the Mobile profile, new API set for sending custom event and receiving event reply have been added.
  - In the Mobile profile, the API set for supporting metadata have been changed.
  - In the Mobile profile, the API set for sending custom command and receiving custom reply have been changed.
  - In the Mobile profile, the callbacks for receiving update information have been changed.
  - In the Mobile profile, some playback states enumerations have been changed.
- Player
  - Pre-condition of setting ROI area API has been changed.
- Muse
  - Support the on-demand launching using socket activation.
  - Add initial gtest codes.
  - Update message IPC mechanism.


### Network and Connectivity

#### Fixes

- Data Network
  - A memory leak in the stc-manager has been fixed.
  - The bug in stc-manager that caused a missing process in booting time has been fixed.
  - CVE patches for Open-source packages have been applied.
    - curl: CVE-2017-8816, CVE-2017-8817, CVE-2017-1000101, CVE-2017-1000257, CVE-2018-1000005, CVE-2018-1000007, CVE-2018-000122, CVE-2018-1000300 and CVE-2018-1000301
    - libsoup: CVE-2017-2885
    - libcares: CVE-2017-1000381
  - Major Open-source package upgrades
    - wpa-supplicant has been upgraded to 2.6.
    - nghttp2 has been upgraded to 1.31.1.
    - strongswan has been upgraded to 5.6.3.
    - dnsmasq has been upgraded to 2.79.
    - openvpn has been upgraded to 2.4.6.
  - The bug in download-provider that extract wrong file extension has been fixed.
- Telephony
  - The bug that caused a delay when shutdown is executed has been fixed.
- Bluetooth
  - The bug in multi advertising scenario has been fixed.
  - The native API reference errors have been fixed.


### Security

#### New and changed features

- Security-manager
  - Support application update between wen application and hybrid application.
  - Remove package manager privileges from User::Shell client.
- Cynara
  - Add dlog as Tizen-specific logging option.
- Askuser
  - Handling H/W key event / end effect / screen reader.
  - Add language set.
- Nether
  - Change nether rule to use raw table for UDP packets.


### Service Framework

#### Fixes

- Context
  - Removed critical information from logs.
  - Fixed potential defects.
- Account
  - Fixed Secure information leaks.
- Email
  - Performance enhancement fixes.
- Contact
  - Fixed graceful handling of non standard charset.
- Maps
  - Fixed potential defects.
- Location
  - Fixed potential defects.
- Sensor
  - Fixed potential defects.
- Calendar
  - Fixed potential defects.


### Tizen .NET

#### New and changed features

- Xamarin.Forms
  - Xamarin.Forms version 3.1.0 Service Release 2 is supported.
  - New Tizen.Wearable.CircularUI API set have been added for wearable apps.
  - New Tizen application project templates (Tizen Wearable App and Tizen Watchface App) have been added.

