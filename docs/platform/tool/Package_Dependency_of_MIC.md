Introduction
------------

This document provides information about package dependency of
[MIC](MIC "wikilink"), including the following:

-   Packages related MIC
-   Package dependency of MIC
-   The dependency graph

Packages Related MIC
--------------------

This section provides information about packages related MIC.

### Package List Table

  No.   Package
  ----- -------------------
  1.    mic
  2.    mic-native
  3.    libzypp
  4.    qemu-arm-static
  5.    qemu-user-static
  6.    satsolver-tools
  7.    python-zypp
  8.    python-zypp-tizen
  9.    isomd5sum
  10.   syslinux

Table 1 Package List of MIC

### Package Relationships

1\. Packages related \`mic\`

`   ::`

`       $ dpkg -s mic`

`         Package: mic`\
`         Depends: python, python-support (>= 0.90.0), rpm, python-rpm, python-urlgrabber, cpio, bzip2, gzip`

2\. Packages related \`mic-native\`

`   ::`

`       $ dpkg -s mic-native`

`         Package: mic-native`\
`         Source: mic`\
`         Depends: python, util-linux, coreutils, psmisc, e2fsprogs (>= 1.41), dosfstools, isomd5sum, genisoimage, dmsetup, kpartx, parted, squashfs-tools (>= 4.0), yum (>= 3.2), syslinux (>= 2:4.05), extlinux (>= 2:4.05), python-zypp-tizen, python-m2crypto, mic`\
`         Recommends: qemu-arm-static | qemu-user-static, binfmt-support, btrfs-tools, udisks | hal`

3\. Packages related \`python-zypp-tizen\`

`   ::`

`       $ dpkg -s python-zypp-tizen`

`         Package: python-zypp-tizen`\
`         Source: libzypp-bindings`\
`         Replaces: python-zypp`\
`         Depends: libzypp`

4\. Packages related \`libzypp\`

`   ::`

`       $ dpkg -s libzypp`

`         Package: libzypp`\
`         Provides: tizen-libzypp-20131212`\
`         Depends: satsolver-tools (>= 0.17.0), uuid-runtime, e2fsprogs, gnupg2, libcurl3, librpm0 | librpm1 | librpm2 | librpm3`

5\. Packages related \`satsolver-tools\`

`   ::`

`       $ dpkg -s satsolver-tools`

`         Package: satsolver-tools`\
`         Source: satsolver`\
`         Depends: gzip, bzip2, coreutils`

6\. Packages related \`qemu-arm-static\`

`   ::`

`       $ dpkg -s qemu-arm-static`

`         Package: qemu-arm-static`\
`         Replaces: qemu-user-static`\
`         Provides: tizen-qemu-arm-static-2013.12.12`\
`         Depends: bzip2, uuid-dev, zlib1g-dev, zlib1g, texi2html, libc6`

7\. Package related \`isomu5sum\`

`   ::`

`       $ dpkg -s isomu5sum`

`         Package: isomd5sum`\
`         Depends: libc6 (>= 2.14), libpopt0 (>= 1.14)`

8\. Package related \`syslinux\`

`   ::`

`       $ dpkg -s syslinux`

`         Package: syslinux`\
`         Replaces: syslinux-common`\
`         Depends: libc6 (>= 2.8), libuuid1 (>= 2.16), syslinux-common (=3:4.05+dfsg-6+deb8u1)`\
`         Recommends: mtools`\
`         Suggests: dosfstools, os-prober`\
`         Breaks: syslinux-common (<< 3:4.05+dfsg-6+deb8u1)`

### Package Relationship Table

  No.   Name                Depends                                                                         Gerrit
  ----- ------------------- ------------------------------------------------------------------------------- ------------------------
  1     mic-native          mic, pyton-zypp-tizen, qemu-arm-static, qemu-user-static, isomd5sum, syslinux   tools/mic
  2     mic                                                                                                 tools/mic
  3     python-zypp-tizen   libzypp                                                                         tools/libzypp-bindings
  4     libzypp             satsolver-tools                                                                 tools/libzypp
  5     satsolver-tools                                                                                     tools/libsatsolver
  6     qemu-arm-static                                                                                     tools/qemu-arm-static
  7     isomd5sum                                                                                           tools/isomd5sum
  8     syslinux                                                                                            tools/syslinux

Table 2 Package Relationship of MIC

Note
----

-   The packages mentioned above only refer to the packages which are
    provided in the gerrit.
-   \`python-zypp\` is replaced by \`python-zypp-tizen\`.
-   \`qemu-user-static\` is replaced by \`qemu-arm-static\`.
-   \`syslinux\` is a higher version on opensuse. For example, Opensuse
    has
-   \`syslinux 4.04\`, while Tools provide \`syslinux 4.05\`.
-   \`isomd5sum\` is not available on opensuse, \`qemu-arm-static\` is
    not on Fedora.
-   \`libzypp\` and \`libzypp-bindings\` and \`libsatsolver\` is off
    except Opensuse.

The dependency graph
--------------------

<File:Package> Dependency of MIC.png\|Package Dependency of MIC

[Category:Tool](Category:Tool "wikilink")
