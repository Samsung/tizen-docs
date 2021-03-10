On behalf of Tizen tools development team

We are very pleased to announce that new version of Tizen developer
tools \[13.06\] is released on tizen.org, at:

` `[`http://download.tizen.org/tools/latest-release/`](http://download.tizen.org/tools/latest-release/)

Highlight of this release
-------------------------

-   It contains several major enhancements for the existing tools:

` - gbs 0.18`\
` - mic 0.21`\
` - bmap-tools 2.6`

-   Distributions support changes:

` * One new distribution supportted`\
`   - Fedora 19`\
` * One distribution dropped:`\
`   - Fedora 17`

-   For tools tools release naming convention and download folder
    structure,

` please see details at: `[`http://download.tizen.org/tools/README.txt`](http://download.tizen.org/tools/README.txt)

Details of the enhancements
---------------------------

-   gbs 0.18 release:

` - offline local full build support for the following Tizen branches:`\
`   * Tizen 2.1`\
`   * Tizen 2.2`\
`   * Tizen 3.0 (tizen): with both common and ivi/mobile profile support`\
` - support CI_CNT and B_CNT OBS build related macros`\
` - zsh command line auto-completion support`\
` - enhance build conf and profile naming:`\
`   * build config file can contains '-'`\
`   * profile name can start with digital and contains '-'`

\- see details release notes at:

` `[`http://download.tizen.org/tools/latest-release/RELEASE_NOTES_GBS.txt`](http://download.tizen.org/tools/latest-release/RELEASE_NOTES_GBS.txt)

-   mic 0.21 release:

` - refactor part of chroot modules for better cleanup handling`\
` - add an alias "installerfw_plugins" for installerfw`\
` - remove unnecessary fuser dependency for "fuser" command`\
` - enable proxy with user authentication setting`\
` - correct no_proxy handling in openSUSE`\
` - kill processes inside chroot after post script running`\
` - ulitize 'dmsetup' to avoid possible dm device unaccessible issue`\
` - bug fixes`

\- see details release notes at:

` `[`http://download.tizen.org/tools/latest-release/RELEASE_NOTES_MIC.txt`](http://download.tizen.org/tools/latest-release/RELEASE_NOTES_MIC.txt)

-   bmap-tools 2.6 release

` - add on-the-fly decompression support for '.xz' and '.tar.xz' files.`\
` - enhancements and fixes in the Debian packaging`

\- see details release notes at:

` `[`http://download.tizen.org/tools/latest-release/RELEASE_NOTES_BMAP-TOOLS.txt`](http://download.tizen.org/tools/latest-release/RELEASE_NOTES_BMAP-TOOLS.txt)

Documentation
-------------

-   Tools installation:

` `[`https://source.tizen.org/documentation/developer-guide/environment-setup`](https://source.tizen.org/documentation/developer-guide/environment-setup)

-   gbs:
    <https://source.tizen.org/documentation/reference/git-build-system>
-   mic:
    <https://source.tizen.org/documentation/reference/mic-image-creator>
-   bmap-tools:
    <https://source.tizen.org/documentation/reference/bmaptool>

Thanks

[Category:Tool](Category:Tool "wikilink")
