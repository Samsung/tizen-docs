We are very pleased to announce that new version of Tizen development
tools \[14.01\] is released on download.tizen.org, including the
following:

-   GBS 0.21
-   MIC 0.24
-   bmap-tools 3.2
-   repa 0.1.1

For information about Tools repositories, refer to:

` [Tools Repository](http://download.tizen.org/tools/latest-release/)`

Highlights
----------

-   New feature: GBS Jenkins jobs for local full build

` These newly added jobs are well documented, easy to deploy and configure,`\
` providing automation solution for small team to efficiently perform package`\
` building, image creation and build artifacts publishing.`

-   New support list

` All the supported Linux distributions versions are as follows:`

` - Ubuntu 13.10`\
` - Ubuntu 12.10`\
` - Ubuntu 12.04`\
` - openSUSE 13.1`\
` - openSUSE 12.3`\
` - openSUSE 12.2`\
` - Fedora 20 (New)`\
` - Fedora 19`\
` - CentOS 6`

For information about tools release naming conventions and download
folder strucuture, refer to:

` [Tools Repository Specification](http://download.tizen.org/tools/README.txt)`

Enhancements
------------

-   GBS 0.21 release

` - From this version, Jenkins jobs support has been included.`\
`     Two subpackages (gbs-jenkins-jobs and gbs-jenkins-scripts) have been`\
`     introduced for jenkins local full build support accordingly.`

` - Add two options, --package-list and --package-from-file, to build customized`\
`   packages specified in the package list directly given in the CLI or a file`\
`   stored in local disk.`\
` - Add more user-friendly error message output for network proxy issues.`

` For detailed information about GBS enhancements, refer to: [GBS Release Notes][1]`

` For detailed information about GBS Jenkins jobs, refer to:`\
` [Deployment and Usage Guide for GBS Jenkins jobs][10]`

` For instructions of the manual equivalent of GBS jenkins jobs, refer to:`\
` [GBS Local Full Build Guide][9]`

-   MIC 0.24 release

` - Add two options, --repo and --ignore-ksrepo, to create customized images`\
`   without updating the ks file.`\
` - Add --user and --password option for %repo directive of ks file.`\
` - Clean up codes relevant to EULA agreement to deprecated EULA support.`\
` - Enhance the handling of password string with special characters.`

` For detailed information, refer to: [MIC Release Notes][2]`

-   bmap-tools 3.2 release

` - Multi-stream bzip2 archives are now supported.`\
` - LZO archives are supported.`\
` - Make 'bmaptool create' (and hence, the BmapCreate module) work with the`\
`   "tmpfs" file-system.`\
` - Decompression should now require less memory, which should fix`\
`   out-of-memory problems reported by some users recently.`\
` - Improve reading and decompressing images.`

` For detailed information, refer to: [bmap-tools Release Notes][3]`

-   repa 0.1.1 release

` - Added --project option to avoid resolving submission to multiple products.`\
` - Added obs and download urls to 'repa list' output`

` For detailed information, refer to: [repa Release Notes][11]`

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
`       "GBS Local Full Build Guide"`\
`[10]: `[`https://source.tizen.org/documentation/developer-guide/jenkins-jobs-local-full-build`](https://source.tizen.org/documentation/developer-guide/jenkins-jobs-local-full-build)\
`       "Deployment and Usage Guide for GBS Jenkins jobs"`\
`[11]: `[`http://download.tizen.org/tools/latest-release/RELEASE_NOTES_REPA.txt`](http://download.tizen.org/tools/latest-release/RELEASE_NOTES_REPA.txt)\
`       "repa Release Notes"`

Thanks

[Category:Tool](Category:Tool "wikilink")
