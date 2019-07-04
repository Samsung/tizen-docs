# Tizen 3.0 Milestones

Release Date: Sep 17, 2015

The Tizen 3.0 first milestone release for TV and mobile profiles provides the Tizen kernel, device drivers, middleware subsystems, and Web/native APIs necessary to develop future Tizen-compliant solutions.

## Release Details

- Getting source code and packages list
  - All Tizen source code is maintained in the Git repository at [tizen.org](https://review.tizen.org/git/).
  - You can access the [TV package list](http://download.tizen.org/releases/milestone/tizen/tv-3.0.m1/tizen-tv_20150914.3/images/arm-wayland/tv-wayland-armv7l-odroidu3/tizen-tv_20150914.3_tv-wayland-armv7l-odroidu3.packages) and the [mobile package list](http://download.tizen.org/releases/milestone/tizen/mobile-3.0.m1/tizen-mobile_20150914.3/images/arm64-wayland/mobile-wayland-arm64-n4/tizen-mobile_20150914.3_mobile-wayland-arm64-n4.packages) for the latest snapshots.
- Getting binaries and images
  - TV binary: [platform](http://download.tizen.org/releases/milestone/tizen/tv-3.0.m1/tizen-tv_20150914.3/images/arm-wayland/tv-wayland-armv7l-odroidu3/tizen-tv_20150914.3_tv-wayland-armv7l-odroidu3.tar.gz) and [bootloader/kernel](http://download.tizen.org/releases/milestone/tizen/tv-3.0.m1/tizen-tv_20150914.3/images/arm-wayland/tv-boot-armv7l-odroidxu3/tizen-tv_20150914.3_tv-boot-armv7l-odroidxu3.tar.gz)
  - Mobile binary: platform ([32-bit](http://download.tizen.org/releases/milestone/tizen/mobile-3.0.m1/tizen-mobile_20150914.3/images/arm-wayland/mobile-wayland-armv7l-n4/tizen-mobile_20150914.3_mobile-wayland-armv7l-n4.tar.gz)/[64-bit](http://download.tizen.org/releases/milestone/tizen/mobile-3.0.m1/tizen-mobile_20150914.3/images/arm64-wayland/mobile-wayland-arm64-n4/tizen-mobile_20150914.3_mobile-wayland-arm64-n4.tar.gz))
- How to flash to a device
  - XU3 (TV profile): [https://wiki.tizen.org/wiki/Quick_guide_for_odroidxu3](https://wiki.tizen.org/wiki/Quick_guide_for_odroidxu3)
  - XU4 (TV profile): [https://wiki.tizen.org/wiki/Quick_guide_for_odroidxu4](https://wiki.tizen.org/wiki/Quick_guide_for_odroidxu4)
  - Mobile profile: A reference device for the mobile profile is not currently available.

## Release Notes

This milestone marks feature completion for the key features of the Tizen 3.0 TV and mobile profiles. Key features in this milestone include:

- 2.4 API compatibility  
The 3.0 TV and mobile profiles are backward-compatible with the 2.4 public API (both native API and Web API). The 2.4 API list is to be published at [https://developer.tizen.org/development](https://developer.tizen.org/development).
- 64-bit support  
64-bit SoC has been tested and verified with 3.0 TV and mobile profiles. 32-bit hard-coded source code has been modified and core components have been re-factored to support both 32-bit and 64-bit SoC. LTP (Linux Testing Project) and TCT (Tizen Compliance Tests) were used to verify behavioral correctness.
- Multi-user architecture  
The 3.0 TV and mobile profiles support multi-user architecture for multi-user/single-login usage. Many services have been moved to user session from system session and the global application and user-specific application concepts have been introduced. This feature enables easy personalization on shared devices, such as tablets and TVs.
- New security architecture: 3 domain smack and Cynara  
The security server and privilege manager have been replaced with security manager and Cynara, respectively. Platform components are categorized depending on their usage domain and the security manager auto-generates the smack rule for each component, rather than based on the module developer.
- Wayland display server  
The X server has been replaced with Wayland in this version. The full specification of the Wayland protocol has been implemented based on Enlightenment 19 and other core platforms, such as AppFW and SystemFW, and the Web engine has been aligned with those changes. This new display server reduces application launch time and computation resource consumption by about 30%, compared to the previous version.
- Blink-based Web engine  
Webkit2 has been replaced with Chromium-efl and core components interacting with the Web engine have been re-designed/re-implemented for the new WRT and browser.
- Buxton2  
Buxton2 has been introduced. Buxton2 provides a secure configuration service based on Cynara and has been re-implemented with consideration for multi-user and recovery support.
- IoTivity integration  
IoTivity 0.9.2 has been integrated into the 3.0 TV and mobile profiles. Simple APIs for this framework are scheduled for the next milestone release.
- Murphy  
A generic policy manager, Murphy, has been integrated into the 3.0 platform. In the M1 release, this manager is only used to control audio session resource conflict scenarios.
- Linux kernel  
The Linux kernel 4.0 is provided.

## Coming in M2 Release

- KDBus  
Integration and hardening of the KDBus feature into the platform, which makes DBus-based IPC faster.
- Crosswalk for Tizen  
Crosswalk for Tizen is under development.
- IoTCon API  
Resource model for typical usage on Tizen devices is abstracted and wrapped with the IoTCon API.
- Linux kernel  
The Linux kernel 4.1 is to be provided.
- Emulator  
The 32-bit/64-bit emulator is being stabilized.

## Known issues

- First screen resizing during application launch  
The root cause of this issue is a lack of synchronization between EFL and Wayland for first scene drawing. This bug is to be resolved before the M2 release.
- DBus privilege bug  
This issue is not caused by the platform module but the DBus configuration for the service adaptor module. It is already fixed but has not been applied to M1 binary, since the bug was discovered very late. This bug is to be resolved before the M2 release.

If you encounter problems with the Tizen milestone release, you are encouraged to interact directly with the Tizen platform developers by subscribing to the tizen dev mailing list.
