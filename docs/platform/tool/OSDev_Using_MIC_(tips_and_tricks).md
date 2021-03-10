Concept of binary repository
----------------------------

[MIC](MIC "wikilink") image creator can create image from so-called
**binary repository**, which can be stored at Web or even on your own
PC.

The **binary repository** is the directory that has the following
structure:

![](Repos-structure.jpg "Repos-structure.jpg"){width="1100"
height="700"}

The XML files contain metadata necessary for work with the repository.

Creating local repository that can be used with MIC
---------------------------------------------------

First you need to have mic and createrepo to be installed on your PC. If
not, follow the guide described on this page: [Installing development
tools](https://source.tizen.org/ru/documentation/developer-guide/installing-development-tools?langredirect=1)

\"createrepo\" is the utility that generates the metadata necessary for
a RPM package repository: primary.xml, other.xml and so on. To install
it, run the following command:

`sudo apt-get install createrepo`

Create the directory where you will store your local repository:

`mkdir /home/user/my-repo`\
`cd /home/user/my-repo`

Create one directory for each architecture that will present in the
repository:

`mkdir aarch64`\
`mkdir noarch`

Download RPM packages from the repository published by OBS server:

`cd aarch64`\
`wget -r -l1 --no-parent -nd -nv -A "*.rpm" `[`http://download.tizen.org/live/devel:/arm_toolchain:/Mobile:/Base/aarch/aarch64/`](http://download.tizen.org/live/devel:/arm_toolchain:/Mobile:/Base/aarch/aarch64/)\
`wget -r -l1 --no-parent -nd -nv -A "*.rpm" `[`http://download.tizen.org/live/devel:/arm_toolchain:/Mobile:/Main/aarch/aarch64/`](http://download.tizen.org/live/devel:/arm_toolchain:/Mobile:/Main/aarch/aarch64/)\
`cd noarch`\
`wget -r -l1 --no-parent -nd -nv -A "*.rpm" `[`http://download.tizen.org/live/devel:/arm_toolchain:/Mobile:/Base/aarch/noarch/`](http://download.tizen.org/live/devel:/arm_toolchain:/Mobile:/Base/aarch/noarch/)\
`wget -r -l1 --no-parent -nd -nv -A "*.rpm" `[`http://download.tizen.org/live/devel:/arm_toolchain:/Mobile:/Main/aarch/noarch/`](http://download.tizen.org/live/devel:/arm_toolchain:/Mobile:/Main/aarch/noarch/)

Download files **group.xml** and **patterns.xml** from some official
Tizen repository and save them into special **repodata** directory:

`cd /home/user/my-repo`\
`mkdir repodata`\
`cd repodata`\
`wget -r -l1 --no-parent -nd -nv -A "group.xml" `[`http://download.tizen.org/releases/daily/tizen/mobile/latest/repos/mobile/ia32/packages/repodata/`](http://download.tizen.org/releases/daily/tizen/mobile/latest/repos/mobile/ia32/packages/repodata/)\
`wget -r -l1 --no-parent -nd -nv -A "patterns.xml" `[`http://download.tizen.org/releases/daily/tizen/mobile/latest/repos/mobile/ia32/packages/repodata/`](http://download.tizen.org/releases/daily/tizen/mobile/latest/repos/mobile/ia32/packages/repodata/)

Run the generation of repository by **createrepo** utility:

`createrepo -g /home/user/my-repo/repodata/group.xml --database --unique-md-filenames /home/user/my-repo`

Add file **patterns.xml** under the control of the repository:

`modifyrepo /home/user/my-repo/repodata/patterns.xml /home/user/my-repo/repodata`

After that you can use directory **\~/my-repo** as the local MIC
repository via **\*.ks** files using the following line:

`repo --name=mobile --baseurl=`[`file:///home/user/my-repo`](file:///home/user/my-repo)` --save --ssl_verify=no`

And then you may run mic for firmware creation

`sudo mic -i create loop -A aarch64 /home/user/my-repo/repodata/fw.ks --shrink --runtime native`

[Category:Tool](Category:Tool "wikilink")
