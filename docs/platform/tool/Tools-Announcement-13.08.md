We are very pleased to announce that new version of Tizen development
tools \[13.08\] is released on download.tizen.org. Repositories can be
found at:

` [Tools Repository](http://download.tizen.org/tools/latest-release/)`

Highlight of this release
-------------------------

In this release, we have included three new tools, including repa,
prekit and lthor. Thanks for all the authors for these projects. And
from this release, both GBS and MIC can support ARM64(aarch64)
architecture now.

-   This release contains many enhancements for the following tools:

` - gbs 0.20`\
` - mic 0.23`\
` - bmap-tools 3.1`\
` - repa 0.1 (New)`\
` - prekit 0.9 (New)`\
` - lthor 1.4 (New)`

-   And two new Linux distributions have been added into the support
    list, as

shown below:

` - Ubuntu 13.10`\
` - openSUSE 13.1`

-   All the supported Linux distributions are:

` - Ubuntu 13.10 (New)`\
` - Ubuntu 13.04`\
` - Ubuntu 12.10`\
` - Ubuntu 12.04`\
` - openSUSE 13.1 (New)`\
` - openSUSE 12.3`\
` - openSUSE 12.2`\
` - openSUSE 12.1`\
` - Fedora 19`\
` - Fedora 18`\
` - CentOS 6`

-   For tools release naming convention and download folder structure,
    please refer to:

` [Tools Repository Specifiation](http://download.tizen.org/tools/README.txt)`

Details of the enhancements
---------------------------

-   GBS 0.20 release

` - support ARM64(aarch64) build`\
` - enhance gbs build report summary, including print log directory, show`\
`   number of succeeded packages and always show build report even if some`\
`   packages build failed`\
` - generate html and json format build report`\
` - depend on new pristine-tar (1.28) to fix pristine-tar branch broken issue`\
` - use HTTP no-cache headers to avoid unexpected proxy caching`\
` - depend on initvm static binary to register qemu handler, instead of using`\
`   qemu bash script(/usr/sbin/qemu-binfmt-conf.sh)`

` For detailed information, refer to: [GBS Release Notes][1]`

-   MIC 0.22 release

` - support arm64 architecture image creation in native mode`\
` - split the "native" running mode support to a separated sub-package`\
` - reduce the dependencies(packages) of mic main package dramatically`\
` - add new options '--interactive' and '--non-interactive' to flip`\
`   interaction`\
` - add new option '--uuid' for 'part' in ks file to set filesystem uuid`\
` - export more environment variables related to installer framework for loop`\
`   image format`

` For detailed information, refer to: [MIC Release Notes][2]`

-   bmap-tools 3.1 release

` - Changes the bmap format version from 1.4 to 2.0 in order to lessen the`\
`   versioning screw-up. Increased major bmap format version number will make`\
`   sure that older bmap-tools fail with a readable error message, instead of`\
`   crashing.`

` For detailed information, refer to: [bmap-tools Release Notes][3]`

-   repa 0.1 release

` - Tool for assisting release engineers with their tasks, including operate`\
`   with submissions in easy and flexible manner.`

-   prekit 0.9 release

` - prekit is a Tizen IA client tool of Pre-OS, which is the proviioning`\
`   environment of Tizen operating system. It's the tool used to flash Tizen`\
`   operation system to IA device.`

` For detailed information, refer to: [Prekit Project Home][4]`

-   lthor 1.4 release

` - Tool for downloading binaries from a Linux host PC to a target phone. It`\
`   uses a USB cable as a physical communication medium.`

Links
-----

`[1]: `[`http://download.tizen.org/tools/latest-release/RELEASE_NOTES_GBS.txt`](http://download.tizen.org/tools/latest-release/RELEASE_NOTES_GBS.txt)\
`       "GBS Release Notes"`\
`[2]: `[`http://download.tizen.org/tools/latest-release/RELEASE_NOTES_MIC.txt`](http://download.tizen.org/tools/latest-release/RELEASE_NOTES_MIC.txt)\
`       "MIC Release Notes"`\
`[3]: `[`http://download.tizen.org/tools/latest-release/RELEASE_NOTES_BMAP-TOOLS.txt`](http://download.tizen.org/tools/latest-release/RELEASE_NOTES_BMAP-TOOLS.txt)\
`       "bmap-tools Release Notes"`\
`[4]: `[`https://github.com/kangkai/prekit`](https://github.com/kangkai/prekit)\
`       "Prekit Project Home"`\
`[5]: `[`https://source.tizen.org/documentation/developer-guide/environment-setup`](https://source.tizen.org/documentation/developer-guide/environment-setup)\
`       "Tools installation Guide"`\
`[6]: `[`https://source.tizen.org/documentation/reference/git-build-system`](https://source.tizen.org/documentation/reference/git-build-system)\
`       "GBS Reference Guide"`\
`[7]: `[`https://source.tizen.org/documentation/reference/mic-image-creator`](https://source.tizen.org/documentation/reference/mic-image-creator)\
`       "MIC Reference Guide"`\
`[8]: `[`https://source.tizen.org/documentation/reference/bmaptool`](https://source.tizen.org/documentation/reference/bmaptool)\
`       "bmap-tools Guide"`\
`[9]: `[`https://source.tizen.org/documentation/developer-guide/creating-tizen-image-scratch`](https://source.tizen.org/documentation/developer-guide/creating-tizen-image-scratch)\
`       "GBS Local Full Build Guide"`

Thanks

[Category:Tool](Category:Tool "wikilink")
