

# Tizen 3.0 Milestones

Release Date: 17 Sep, 2015

The Tizen 3.0 first milestone release for TV and Mobile profiles provides developers with the Tizen kernel, device drivers, middleware subsystems, and Web/Native APIs, necessary to develop future Tizen compliant solutions.

## Release Details

- Getting source code and packages list

  ​

  - All tizen source code is maintained in git of [tizen.org](https://review.tizen.org/git/).
  - [TV packages list](http://download.tizen.org/releases/milestone/tizen/tv-3.0.m1/tizen-tv_20150914.3/images/arm-wayland/tv-wayland-armv7l-odroidu3/tizen-tv_20150914.3_tv-wayland-armv7l-odroidu3.packages) is found in the latest snapshot and [Mobile packages list](http://download.tizen.org/releases/milestone/tizen/mobile-3.0.m1/tizen-mobile_20150914.3/images/arm64-wayland/mobile-wayland-arm64-n4/tizen-mobile_20150914.3_mobile-wayland-arm64-n4.packages) is found in the latest snapshot.


- Getting binaries and images

  ​

  - TV binary: [platform](http://download.tizen.org/releases/milestone/tizen/tv-3.0.m1/tizen-tv_20150914.3/images/arm-wayland/tv-wayland-armv7l-odroidu3/tizen-tv_20150914.3_tv-wayland-armv7l-odroidu3.tar.gz) and [bootloader/kernel](http://download.tizen.org/releases/milestone/tizen/tv-3.0.m1/tizen-tv_20150914.3/images/arm-wayland/tv-boot-armv7l-odroidxu3/tizen-tv_20150914.3_tv-boot-armv7l-odroidxu3.tar.gz)
  - Mobile binary: platform ([32bit](http://download.tizen.org/releases/milestone/tizen/mobile-3.0.m1/tizen-mobile_20150914.3/images/arm-wayland/mobile-wayland-armv7l-n4/tizen-mobile_20150914.3_mobile-wayland-armv7l-n4.tar.gz) / [64bit](http://download.tizen.org/releases/milestone/tizen/mobile-3.0.m1/tizen-mobile_20150914.3/images/arm64-wayland/mobile-wayland-arm64-n4/tizen-mobile_20150914.3_mobile-wayland-arm64-n4.tar.gz))


- How to flash to a device

  ​

  - XU3 (TV profile): [https://wiki.tizen.org/wiki/Quick_guide_for_odroidxu3](https://wiki.tizen.org/wiki/Quick_guide_for_odroidxu3)
  - XU4 (TV profile): [https://wiki.tizen.org/wiki/Quick_guide_for_odroidxu4](https://wiki.tizen.org/wiki/Quick_guide_for_odroidxu4)
  - Mobile profile: reference device for mobile profile is not available right now.

## Release Notes

This milestone marks feature completion for the key features of Tizen 3.0 TV and Mobile profiles. Key features integrated in this milestone include:

- 2.4 API compatibility

  ​

  - 2.4 public API (both Native API and Web API) is backward-compatible with 3.0 TV and Mobile profiles. 2.4 API list will be available on [https://developer.tizen.org/development](https://developer.tizen.org/development) soon.

- 64bit support

  - 64bit SoC is tested and verified with 3.0 TV and Mobile profiles. 32bit hard-coded source code is modified and core components are re-factored to support both 32bit and 64bit SoC. LTP (Linux Testing Project) and TCT (Tizen Compliance Tests) is used to verify behavioral correctness.

- Multi-user architecture

  - 3.0 TV and Mobile profiles support multi-user architecture for multi-user/single-login usage. Many services are moved to user session from system session and global application and user specific application concept is introduced. Utilizing this feature enables easy personalization on the shared devices like Tablet and TV device.

- New security architecture: 3 domain smack and Cynara

  - Security server and privilege manager are replaced with the new components, security manager and Cynara respectively. Platform components are categorized depending on their usage domain and security manager auto-generates the right smack rule for each component, not by module developer.

- Wayland display server

  - X server is replaced with Wayland at this version. Full specification of Wayland protocol is implemented based on Enlightenment 19 and other core platforms like AppFW, SystemFW and Web engine are totally aligned with those changes. This new display server reduces application launching time and computation resource consumption by about 30% compared to previous version.

- Blink based web engine

  - Webkit2 is replaced with Chromium-efl and core components interacting with the web engine are re-designed/re-implemented for the new WRT and browser.

- Buxton2

  - Buxton2 is introduced. Buxton2 provides secure configuration service based on Cynara and is re-implemented considering multi-user and recovery support.

- Iotivity integration

  - Iotivity 0.9.2 is integrated into 3.0 TV and Mobile profiles. Easy APIs for this framework will be released on next milestone release.

- Murphy

  - Generic policy manager, murphy, is integrated into 3.0 platform. This manager is only used to control resource conflict scenario of audio session at this M1 release.

- Linux kernel

  - Linux kernel 4.0 is provided.

## What's next for M2 release?

- KDBus

  ​

  - We're integrating and hardening KDBus feature into platform, which makes DBus based IPC faster.

- Crosswalk for Tizen

  - Crosswalk for Tizen is under development.

- IoTCon API

  - Resource model for typical usage on Tizen devices is abstracted and wrapped with IoTCon API.

- Linux kernel

  - Linux kernel 4.1 will be provided.

- Emulator

  - 32bit/64bit emulator is being stabilized.

## Known issues

- First screen resizing during launching application

  ​

  - The root cause of this issue is lack of synchronization between EFL and Wayland for first scene drawing. This bug will be resolved before M2 release.

- DBus privilege bug

  - This issue is not about platform module but about DBus configuration file of service adaptor module. It is already fixed but not applied to M1 binary since this bug is found so late. This bug will be resolved before M2 release.

 

If you encounter problems with Tizen milestone release, you're encouraged to interact directly with the Tizen platform developers by subscribing to the tizen dev mailing list.