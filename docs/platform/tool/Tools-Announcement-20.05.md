We are pleased to announce that new version of Tizen development tools
\[20.04\] is released on download.tizen.org, including the following:

-   GBS 0.25.15
-   MIC 0.28.11
-   REPA 0.7

For information about Tools repositories, refer to:

` [Tools Repository](http://download.tizen.org/tools/releases/milestone/latest/)`

For information about tools release naming conventions and download
folder strucuture, refer to:

` [Tools Repository Specification](http://download.tizen.org/tools/README.txt)`

\'\'\'Notice:

` '''In this version, we have a big change, we removed dependence for createrepo package, because it is too old. Instead, we use creterepo-c package, So before installing gbs 0.25.15 version, you need to   uninstall creterepo. `\
` '''Ubuntu: "sudo apt-get remove createreo", or "sudo apt-get autoremove gbs", then "sudo apt-get install gbs"; `\
` '''OpenSuse: "sudo zypper remove createrepo", or "sudo zypper remove gbs". Then sudo "sudo zypper install gbs"`\
`   '''`

\'\'\'

Enhancements
------------

-   GBS 0.25.15 release

` - Bug fix::`\
`   * Fix build failed when gbs full build.`\
` - New feature and enhancements added:`\
`   * Remove build dependence with python-support.`\
`   * Support gen depends of exported sources.`\
`   * Add --tarfile option for gbs depends subcommand to generate tar xml file.`\
`   * Support zstd decompression for old rpm version`\
`   * Support zstd arch for tar`

` For detailed information about GBS enhancements, refer to: [GBS Release Notes][1]`

-   MIC 0.28.11 release

` - Bug fix::`\
`   * fix run error issue for parser repomd.xml when here is group type..`\
` - New feature and enhancements added:`\
`   * Separate qcow plugin scripts.`

` For detailed information, refer to: [MIC Release Notes][2]`

Links
-----

`[1]: `[`http://download.tizen.org/tools/releases/milestone/latest/RELEASE_NOTES_GBS.txt`](http://download.tizen.org/tools/releases/milestone/latest/RELEASE_NOTES_GBS.txt)\
`       "GBS Release Notes"`\
`[2]: `[`http://download.tizen.org/tools/releases/milestone/latest/RELEASE_NOTES_MIC.txt`](http://download.tizen.org/tools/releases/milestone/latest/RELEASE_NOTES_MIC.txt)\
`       "MIC Release Notes"`\
`[3]: `[`https://source.tizen.org/documentation/developer-guide/environment-setup`](https://source.tizen.org/documentation/developer-guide/environment-setup)\
`      "Tools Installation Guide"`\
`[4]: `[`https://source.tizen.org/documentation/reference/git-build-system`](https://source.tizen.org/documentation/reference/git-build-system)\
`      "GBS Reference Guide"`\
`[5]: `[`https://source.tizen.org/documentation/reference/mic-image-creator`](https://source.tizen.org/documentation/reference/mic-image-creator)\
`      "MIC Reference Guide"`\
`[6]: `[`https://source.tizen.org/documentation/reference/git-build-system/maintenance-models-supported-gbs`](https://source.tizen.org/documentation/reference/git-build-system/maintenance-models-supported-gbs)\
`      "Maintenance Models"`

Thanks

[Category:Tool](Category:Tool "wikilink")
