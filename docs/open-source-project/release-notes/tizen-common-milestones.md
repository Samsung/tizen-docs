# Tizen Common milestones

Tizen Common is the common subset of the Tizen profiles, used by platform developers to develop the next version of the profiles. As such, it does not have releases in the traditional fashion. Instead, it has quarterly milestones.

If you encounter problems with the Tizen Common milestones, you're encouraged to interact directly with the Tizen platform developers by subscribing to the [tizen dev mailing list](https://lists.tizen.org/listinfo/dev).

## Milestone 2014Q2 (Tizen 3.0)

This milestone marks feature completion for the common subset of Tizen 3.0 profiles. You can read all about this in the wiki page: [https://wiki.tizen.org/wiki/Tizen_3.0](https://wiki.tizen.org/wiki/Tizen_3.0). Features integrated in this milestone include:

- 64-bit support for both Intel and ARM architectures
- Crosswalk-based web runtime
- Multiuser support
- Systemd
- Security: three-domain rule system for SMACK and Cynara as authorization framework
- Wayland display server

All Git repositories part of this release have been tagged with tag "tizen_common_2014.Q2". To build this release, please refer to the [developer guide](../developing/).

Pre-built images for this milestone can be downloaded from [here](http://download.tizen.org/releases/milestone/tizen/common-3.0.2014.Q3/). Please see the documentation page on [flashing a device](https://source.tizen.org/documentation/reference/flash-device) for information on installing this image. It has been tested on the following device types:

- [Intel Atom E3815-based NUC Kit](https://www-ssl.intel.com/content/www/us/en/nuc/nuc-kit-de3815tykhe.html)
- [Intel Atom E3825-based NEXCOM VTC1010](http://www.nexcom.com/Products/mobile-computing-solutions/tizen-ivi-platform/tizen-ivi-platform/vtc-1010-ivi)
