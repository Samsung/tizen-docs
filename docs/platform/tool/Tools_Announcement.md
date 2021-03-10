We are pleased to announce that new version of Tizen development tools
\[15.01\] is released on download.tizen.org, including the following:

-   GBS 0.23.2
-   MIC 0.24.4
-   REPA 0.3
-   BMAP-TOOLS 3.3

For information about Tools repositories, refer to:

` [Tools Repository](http://download.tizen.org/tools/latest-release/)`

For information about tools release naming conventions and download
folder strucuture, refer to:

` [Tools Repository Specification](http://download.tizen.org/tools/README.txt)`

Enhancements
------------

-   GBS 0.23.2 release

`  - Fixed get "fallback_to_native" value from non-default gbs configuration`\
`  - Fixed bad indentation from pylint checking`\
`  - Fixed tag mode in test_import script`

` For detailed information about GBS enhancements, refer to: [GBS Release Notes][1]`

-   MIC 0.24.4 release

`  - Generate manifest file to describe image information`\
`  - Modify mount option to support both toybox and busybox`\
`  - Other hot bug fixes`

` For detailed information, refer to: [MIC Release Notes][2]`\
` The latest mic-appliance can be downloaded from `[`http://download.tizen.org/tools/mic-appliance/15.01/`](http://download.tizen.org/tools/mic-appliance/15.01/)

-   REPA 0.3 release

`  - group: disable publishing when aggregating packages`\
`  - Skip conflicting submissions when creating a group`\
`  - group: Implemented parallel package aggregating`\
`  - info: Excluded 'disabled' build status from the list`\
`  - list: Implement --ignore command line option`\
`  - group: Remove binary package check`\
`  - Implement --noaggregate command line and config option`\
`  - List all projects in submitrequest message`\
`  - Drop 'Commit' keyword from the submitrequest info`\
`  - Reworked repa diff`\
`  - Implement --base option for repa list`\
`  - Pylinted codebase`\
`  - Output SR for rejected/accepted submissions`\
`  - create_sr: Fix unicode issue`

` For detailed information, refer to: [repa Release Notes][3]`

-   BMAP-TOOLS 3.3 release

`  - Fix rpm dependency issue for Fedora`

` For detailed information, refer to: [bmap-tools Release Notes][4]`

Links
-----

`[1]: `[`http://download.tizen.org/tools/latest-release/RELEASE_NOTES_GBS.txt`](http://download.tizen.org/tools/latest-release/RELEASE_NOTES_GBS.txt)\
`       "GBS Release Notes"`\
`[2]: `[`http://download.tizen.org/tools/latest-release/RELEASE_NOTES_MIC.txt`](http://download.tizen.org/tools/latest-release/RELEASE_NOTES_MIC.txt)\
`       "MIC Release Notes"`\
`[3]: `[`http://download.tizen.org/tools/latest-release/RELEASE_NOTES_REPA.txt`](http://download.tizen.org/tools/latest-release/RELEASE_NOTES_REPA.txt)\
`       "repa Release Notes"`\
`[4]: `[`http://download.tizen.org/tools/latest-release/RELEASE_NOTES_BMAP-TOOLS.txt`](http://download.tizen.org/tools/latest-release/RELEASE_NOTES_BMAP-TOOLS.txt)\
`       "bmap-tools Release Notes"`\
`[5]: `[`https://source.tizen.org/documentation/developer-guide/environment-setup`](https://source.tizen.org/documentation/developer-guide/environment-setup)\
`       "Tools Installation Guide"`\
`[6]: `[`https://source.tizen.org/documentation/reference/git-build-system`](https://source.tizen.org/documentation/reference/git-build-system)\
`       "GBS Reference Guide"`\
`[7]: `[`https://source.tizen.org/documentation/reference/mic-image-creator`](https://source.tizen.org/documentation/reference/mic-image-creator)\
`       "MIC Reference Guide"`\
`[8]: `[`https://source.tizen.org/documentation/reference/git-build-system/maintenance-models-supported-gbs`](https://source.tizen.org/documentation/reference/git-build-system/maintenance-models-supported-gbs)\
`       "Maintenance Models"`

Thanks

[Category:Tool](Category:Tool "wikilink")
