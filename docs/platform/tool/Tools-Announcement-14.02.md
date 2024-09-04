We are very pleased to announce that new version of Tizen development
tools \[14.02\] is released on download.tizen.org, including the
following:

-   GBS 0.22
-   MIC 0.25
-   repa 0.2

For information about Tools repositories, refer to:

` [Tools Repository](http://download.tizen.org/tools/latest-release/)`

Highlights
----------

-   New feature: orphan-packaging development model

` Implement 'devel' subcommand for orphan-packaging development model, which`\
` facilitates package maintainers to better maintain package in the orphan-`\
` packaging branch model by providing five actions, including 'start', 'export',`\
` 'drop', 'switch', and 'convert'. Currently, this is only an experimental`\
` version, so please report jira tickets if you find any issues.`

` For detailed information, refer to: [Maintenance Models][7] and [GBS 'devel' command][8]`

-   New support list

` All the supported Linux distributions versions are as follows:`

` - Ubuntu 14.04(New)`\
` - Ubuntu 13.10`\
` - Ubuntu 12.04`\
` - openSUSE 13.1`\
` - openSUSE 12.3`\
` - openSUSE 12.2`\
` - Fedora 20`\
` - Fedora 19`\
` - CentOS 6`\
` - Debian 7(New)`

For information about tools release naming conventions and download
folder strucuture, refer to:

` [Tools Repository Specification](http://download.tizen.org/tools/README.txt)`

Enhancements
------------

-   GBS 0.22 release

`  - Implement 'devel' subcommand to support orphan-packaging development model`\
`  - Conf: support adding new sections and updating an empty conf file`\
`  - Support new profile key 'exclude_packages' like --exclude build option`\
`  - Changelog: utilize rpm-ch from git-buildpackage`\
`  - Build: add group metadata to local repodata if package-groups.rpm exists`

` For detailed information about GBS enhancements, refer to: [GBS Release Notes][1]`

-   MIC 0.25 release

` - Generate manifest file to describe image information`\
` - Refactor archive and compress module`\
` - Support sparse handle for tar command`\
` - Replace system V with systemd on locale setting`\
` - Support lzop compress`

` For detailed information, refer to: [MIC Release Notes][2]`

-   repa 0.2 release

` - Implement --processes options for repa list`\
` - Implement --colorize option`\
` - Implement --showurls option`\
` - Reduce the amount of information in repa list output`\
` - Make 'project' a mandatory config option`\
` - Add configuration file info to the man page`\
` - Enhance man page`\
` - Get rid of --regexp command line option`\
` - Create one SR for all packages in submission`\
` - Add -group suffix to the path for the group`\
` - Draft implementation of repa diff`

` For detailed information, refer to: [repa Release Notes][3]`

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
`       "Maintenance Models"`\
`[8]: `[`https://source.tizen.org/documentation/reference/git-build-system/usage/gbs-devel`](https://source.tizen.org/documentation/reference/git-build-system/usage/gbs-devel)\
`       "GBS 'devel' command"`

Thanks

[Category:Tool](Category:Tool "wikilink")
