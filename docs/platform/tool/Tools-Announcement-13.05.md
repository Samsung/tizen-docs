On behalf of Tizen tools development team

We are very pleased to announce that new version of Tizen developer
tools \[13.05\] is released on tizen.org, at:

` `[`http://download.tizen.org/tools/latest-release/`](http://download.tizen.org/tools/latest-release/)

Highlight of this release
-------------------------

-   It contains several major enhancements for the existing tools:

` - gbs 0.17`\
` - mic 0.20`\
` - bmap-tools 2.4`

-   For tools tools release naming convention and download folder
    structure,

` please see details at: `[`http://download.tizen.org/tools/README.txt`](http://download.tizen.org/tools/README.txt)

Details of the enhancements
---------------------------

-   gbs 0.17 release:

` - Totally local full build support, refer to document [3]`\
` - gbs config refinements`\
` - Support fetching build conf from standard RPM repodata`\
` - Create debuginfo and debugsource packages by default`\
` - Add --packaging-branch option for 'gbs clone' to specify default working branch`\
` - Optimizations`\
` - bug fixes`\
`   * get target arch from build conf if 'Target' is set in build config, which`\
`     make gbs and remote obs generate the same arch for final RPM package`

\- see details release notes at:

` `[`http://download.tizen.org/tools/latest-release/RELEASE_NOTES_GBS.txt`](http://download.tizen.org/tools/latest-release/RELEASE_NOTES_GBS.txt)

-   mic 0.20 release:

` - new distribution support: CentOS 6`\
` - drop image creation if checked packages not present in image`\
` - introduce 'installerfw' command in kickstart to customize configuration`\
` - improve output message of post scripts`\
` - bug fixes`

\- see details release notes at:

` `[`http://download.tizen.org/tools/latest-release/RELEASE_NOTES_MIC.txt`](http://download.tizen.org/tools/latest-release/RELEASE_NOTES_MIC.txt)

-   bmap-tools 2.4 release

` - Add SSH URLs support. These URLs start with "`[`ssh://`](ssh://)`" and have the following`\
`   format: `[`ssh://user:password@host:path`](ssh://user:password@host:path)`, where`\
`      * user - user name (optional)`\
`      * password - the password (optional)`\
`      * host - hostname`\
`      * path - path to the image file on the remote host`\
`   If the password was given in the URL, bmaptool will use password-based SSH`\
`   authentication, otherwise key-based SSH authentication will be used.`

\- see details release notes at:

` `[`http://download.tizen.org/tools/latest-release/RELEASE_NOTES_BMAP-TOOLS.txt`](http://download.tizen.org/tools/latest-release/RELEASE_NOTES_BMAP-TOOLS.txt)

Documentation
-------------

-   Tools installation:
    <https://source.tizen.org/documentation/developer-guide/environment-setup>
-   gbs:
    <https://source.tizen.org/documentation/reference/git-build-system>
-   local full build:
    <https://source.tizen.org/documentation/developer-guide/creating-tizen-platform-image-scratch-through-local-build>
-   mic:
    <https://source.tizen.org/documentation/reference/mic-image-creator>
-   bmap-tools:
    <https://source.tizen.org/documentation/reference/bmaptool>

Thanks

[Category:Tool](Category:Tool "wikilink")
