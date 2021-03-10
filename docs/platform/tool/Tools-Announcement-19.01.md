We are pleased to announce that new version of Tizen development tools
\[19.01\] is released on download.tizen.org, including the following:

-   GBS 0.25.10
-   MIC 0.28.7
-   REPA 0.6

For information about Tools repositories, refer to:

` [Tools Repository](http://download.tizen.org/tools/archive/16.02/)`

For information about tools release naming conventions and download
folder strucuture, refer to:

` [Tools Repository Specification](http://download.tizen.org/tools/README.txt)`

Enhancements
------------

-   GBS 0.25.10 release

`  - Bug fix:`\
`   * Fix pylint issue for gbs`

` For detailed information about GBS enhancements, refer to: [GBS Release Notes][1]`

-   MIC 0.28.7 release

`  - New features and enhancements:  `\
`    * add option for mic to skip set hosts when create.`\
`  `\
`  - Bug fix:`\
`    * fix pylint errors for mic.`\
`    * skip set hosts by mic when /etc/hosts exists.`

` For detailed information, refer to: [MIC Release Notes][2]`

-   REPA 0.6 release

` - No update`

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
`       "MIC Release Notes"`

Thanks

[Category:Tool](Category:Tool "wikilink")
