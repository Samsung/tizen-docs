We are very pleased to announce that new bug-fix version of Tizen
development tools \[14.02.2\] is released on download.tizen.org,
including the following:

-   GBS 0.22.1
-   MIC 0.25.2

For information about Tools repositories, refer to:

` [Tools Repository](http://download.tizen.org/tools/latest-release/)`

For information about tools release naming conventions and download
folder strucuture, refer to:

` [Tools Repository Specification](http://download.tizen.org/tools/README.txt)`

Enhancements
------------

-   GBS 0.22.1 release

`  - Fix backtrace issue caused by desktop notifications`\
`  - Change VCS tag in spec to commitish sha1sum in export module`\
`  - Fix bug: OS/ABI field in ELF header messed up aarch64`

` For detailed information about GBS enhancements, refer to: [GBS Release Notes][1]`

-   MIC 0.25.2 release

` - Fix critial bug that crashed /etc if using /etc/mic.conf as config option`\
` - Fix python xml module requirements`\
` - Fix AttributeError traceback in zypp backend`

` For detailed information, refer to: [MIC Release Notes][2]`

WARNING
-------

In MIC 0.25, a critial bug would crash your /etc directory when adding
\'-c /etc/mic.conf\' in MIC command line, this bug only affects 0.25 and
it has been fixed in 0.25.1. Please avoid this bug by upgrading MIC
version according to the hints.

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
