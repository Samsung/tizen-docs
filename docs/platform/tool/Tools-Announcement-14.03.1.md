We are pleased to announce that new bug-fix version of Tizen development
tools \[14.03.1\] is released on download.tizen.org, including the
following:

-   GBS 0.23
-   MIC 0.24.3

For information about Tools repositories, refer to:

` [Tools Repository](http://download.tizen.org/tools/latest-release/)`

For information about tools release naming conventions and download
folder strucuture, refer to:

` [Tools Repository Specification](http://download.tizen.org/tools/README.txt)`

Enhancements
------------

-   GBS 0.23 release

`  - Added --fallback-to-native option, to enable gbs-export to fallback to`\
`    "native" packaging mode for "non-native" packages with git tree errors.`\
`  - Added native config option in gbs configuration file to specify packages as`\
`    "native" packaging mode explicitly.`\
`  - Added --skip-srcrpm option, support no source rpm building.`\
`  - Start to support MIPS(mips and mipsel)architecture building targets.`\
`  - Added --icecream option, to build with distributed compiler network.`\
`  - Fix: build on development branch with --include-all option.`\
`  - Fix: dependency issue on gbs repository for fedora.`\
`  - Fix: disable invalid pylint errors.`

` For detailed information about GBS enhancements, refer to: [GBS Release Notes][1]`

-   MIC 0.24.3 release

`  - Added support for creating arm64(aarch64) images`\
`  - Fix: qemu arm execution register issue.`\
`  - Fix: remove --preserve-order option in taring fs image`

` For detailed information, refer to: [MIC Release Notes][2]`

Links
-----

`[1]: `[`http://download.tizen.org/tools/latest-release/RELEASE_NOTES_GBS.txt`](http://download.tizen.org/tools/latest-release/RELEASE_NOTES_GBS.txt)\
`       "GBS Release Notes"`\
`[2]: `[`http://download.tizen.org/tools/latest-release/RELEASE_NOTES_MIC.txt`](http://download.tizen.org/tools/latest-release/RELEASE_NOTES_MIC.txt)\
`       "MIC Release Notes"`\
`[3]: `[`http://download.tizen.org/tools/latest-release/RELEASE_NOTES_REPA.txt`](http://download.tizen.org/tools/latest-release/RELEASE_NOTES_REPA.txt)\
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
