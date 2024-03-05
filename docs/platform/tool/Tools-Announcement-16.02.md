We are pleased to announce that new version of Tizen development tools
\[16.02\] is released on download.tizen.org, including the following:

-   GBS 0.24.1
-   MIC 0.27.1
-   REPA 0.4

For information about Tools repositories, refer to:

` [Tools Repository](http://download.tizen.org/tools/archive/16.02/)`

For information about tools release naming conventions and download
folder strucuture, refer to:

` [Tools Repository Specification](http://download.tizen.org/tools/README.txt)`

Enhancements
------------

-   GBS 0.24.1 release

`  - Bug fix:`\
`   * Upgrade pristine-tar with xdelta3 instead of xdelta(xdelta can not work well when codes' size is bigger than 2GB )`\
`   * Add tar extract patches to solve bad message generated by git(2.7.4) mailinfo`\
`  - New feature and enhancements added:`\
`   * Upgrade latest 'build' package from upstream and suit for gbs`\
`   * Upgrade depannuer to meet new version of build`\
`   * Support new platform Ubuntu 16.04, Fedora 23`

` For detailed information about GBS enhancements, refer to: [GBS Release Notes][1]`

-   MIC 0.27.1 release

`  * new distribution support: Ubuntu 16.04, Fedora 23`\
`  * add raw image format support`\
`  * Remove BmapCreate and Filemap source code from MIC (#DEVT-151)`

` For detailed information, refer to: [MIC Release Notes][2]`\
` The latest mic-appliance can be downloaded from `[`http://download.tizen.org/tools/mic-appliance/15.01/`](http://download.tizen.org/tools/mic-appliance/15.01/)

-   REPA 0.4 release

`  - New features and enhancements:`\
`   * group: remove --force option`\
`   * Rename command info -> show`\
`   * Implement rebuild subcommand`\
`   * Implement lock/unlock subcommand`\
`   * Implement remove subcommand`\
`   * list: add build time`\
`   * Implement --edit command line option`

`  - Bugfixes:`\
`   * fix pylint error`

` For detailed information, refer to: [repa Release Notes][3]`

The upgrade reminder
--------------------

\[GBS\]:

`    Duo to we use new dependency for pristine-tar, If you have installed GBS with old version(<0.24) on debian's system（Ubuntu, Debian），`\
`    you need upgrade as below:`

`    1.Add new repo to sources.list file;`\
`    2."sudo apt-get update";`\
`    3."sudo apt-get upgrade gbs";`\
`    4."sudo apt-get upgrade  pristine-tar"`

Links
-----

`[1]: `[`http://download.tizen.org/tools/archive/16.02/RELEASE_NOTES_GBS.txt`](http://download.tizen.org/tools/archive/16.02/RELEASE_NOTES_GBS.txt)\
`       "GBS Release Notes"`\
`[2]: `[`http://download.tizen.org/tools/archive/16.02/RELEASE_NOTES_MIC.txt`](http://download.tizen.org/tools/archive/16.02/RELEASE_NOTES_MIC.txt)\
`       "MIC Release Notes"`\
`[3]: `[`http://download.tizen.org/tools/archive/16.02/RELEASE_NOTES_REPA.txt`](http://download.tizen.org/tools/archive/16.02/RELEASE_NOTES_REPA.txt)\
`       "repa Release Notes"`\
`[4]: `[`https://source.tizen.org/documentation/developer-guide/environment-setup`](https://source.tizen.org/documentation/developer-guide/environment-setup)\
`       "Tools Installation Guide"`\
`[5]: `[`https://source.tizen.org/documentation/reference/git-build-system`](https://source.tizen.org/documentation/reference/git-build-system)\
`       "GBS Reference Guide"`\
`[6]: `[`https://source.tizen.org/documentation/reference/mic-image-creator`](https://source.tizen.org/documentation/reference/mic-image-creator)\
`       "MIC Reference Guide"`\
`[7]: `[`https://source.tizen.org/documentation/reference/git-build-system/maintenance-models-supported-gbs`](https://source.tizen.org/documentation/reference/git-build-system/maintenance-models-supported-gbs)\
`       "Maintenance Models"`

Thanks

[Category:Tool](Category:Tool "wikilink")
