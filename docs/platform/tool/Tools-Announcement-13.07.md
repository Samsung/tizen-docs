On behalf of Tizen tools development team, we are very pleased to
announce that new versions of Tizen developer tools \[13.07\] have been
released on tizen.org (http://download.tizen.org/tools/latest-release/),
including the following:

\- Git Build System (GBS) 0.19 - Image Creator (MIC) 0.22 - bmap-tools
3.0

For naming convention and download folder structure for tools release,
refer to <http://download.tizen.org/tools/README.txt>.

Highlights and Major Enhancements
---------------------------------

-   GBS 0.19 release

` - Remove previous built rpm and srpm if new version has been built out.`\
` - Track upstream/pristine-tar branch automatically, as well as using upstream and pristine-tar branch to generate tar ball.`\
` - Split out remote build module to separate sub-package: gbs-remotebuild.`\
` - Fix the bug below:`

`   Failure of loading project specific gbs.conf when gitdir is specified.`

` - Update dependencies below:`

`   * Depend on new pristine-tar 1.28, which contains bug fix while creating pristine-tar delta data.`\
`   * Depend on new librpm-tizen to ignore some spec parser error.`

` For detailed information, refer to `[`http://download.tizen.org/tools/latest-release/RELEASE_NOTES_GBS.txt`](http://download.tizen.org/tools/latest-release/RELEASE_NOTES_GBS.txt)`.`

-   MIC 0.22 release

` - Refactor msger module to ulitize logging module.`\
` - Refine error class module.`\
` - Enhance the support for virtualenv.`\
` - Add bash and zsh completion support.`\
` - Update BmapCreate module to the latest version.`\
` - Fix the bugs below:`

`   + Exit during packing process in Ubuntu.`\
`   + Failure of loop device alloaction in openSUSE.`

` For detailed information, refer to `[`http://download.tizen.org/tools/latest-release/RELEASE_NOTES_MIC.txt`](http://download.tizen.org/tools/latest-release/RELEASE_NOTES_MIC.txt)`.`

-   bmap-tools 3.0 release

` - Switch from using SHA1 checksums in the bmap file to using SHA256.`\
` - Support OpenPGP (AKA gpg) signatures for the bmap file.`\
` - Guarantee the Fiemap module (and thus, bmaptool) to always synchronize the`\
`   image before scanning it for mapped areas. This is done by using the`\
`   "FIEMAP_FLAG_SYNC" flag of the FIEMAP ioctl.`

` For detailed information, refer to `[`http://download.tizen.org/tools/latest-release/RELEASE_NOTES_BMAP-TOOLS.txt`](http://download.tizen.org/tools/latest-release/RELEASE_NOTES_BMAP-TOOLS.txt)`.`

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
