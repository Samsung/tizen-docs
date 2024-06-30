**Binary Import from the web**

The stable repository (or a snapshot) is imported to the backend
repository server machine.

-   The binaries are copied to a staging area (not directly into
    /srv/obs)

`# mkdir -p /data/imports`\
`# cd /data/imports`

Use the wget command:

`# wget --directory-prefix=/data/imports --mirror --reject index.html* -r -nH --no-parent `[`http://download.tizen.org/releases/2.3/2.3-mobile/tizen-2.3-mobile_20150311.3/repos/target/packages/armv7l/`](http://download.tizen.org/releases/2.3/2.3-mobile/tizen-2.3-mobile_20150311.3/repos/target/packages/armv7l/)

-   Now create the ":full" directory.

And define directory names(\$PROJECT, \$REPO, \$ARCH) based on the
Project Profile.

`# mkdir -p /srv/obs/build/$PROJECT/$REPO/$ARCH/:full`\
`# cd /srv/obs/build/$PROJECT/$REPO/$ARCH/:full`

-   Add binaries to the :full directory of the Project

`` for i in `find /data/imports/ -name \*.rpm`;  ``\
`do `\
``     j=`basename $i` ``\
``     k=`echo $j |sed -rn 's/(.*)-.*-.*.rpm/\1.rpm/p'` ``\
`    mv $i /srv/obs/build/$PROJECT/$REPO/$ARCH/:full/$k`\
`done`

-   Change all user/group privileges under /srv/obs/build/ to "obsrun".
    If you leave root as owner of :full, it will still build but the
    scheduler will fail (almost silently) to upgrade :full with the
    latest built packages.

`# chown -R obsrun:obsrun /srv/obs/build/$PROJECT`\
`# rm -r /data/imports`\
`   `

-   The back-end is told about the imported packages. This will send an
    event to the scheduler which will re-index your new \':full\'
    directory and create a file named :full.solv

`# obs_admin --rescan-repository $PROJECT $REPO $ARCH`

**Source Import from the web**

-   You need to download all your source RPMs on a local machine and
    import them into your project with the command

`# osc importsrcpkg --help`\
`importsrcpkg: Import a new package from a src.rpm`\
\
`A new package dir will be created inside the project dir`\
`(if no project is specified and the current working dir is a`\
`project dir the package will be created in this project). If`\
`the package does not exist on the server it will be created`\
`too otherwise the meta data of the existing package will be`\
`updated (`

<title />

and <description />).

`The src.rpm will be extracted into the package dir. The files`\
`won't be committed unless you explicitly pass the --commit switch.`\
\
`SRPM is the path of the src.rpm in the local filesystem,or an URL.`\
\
`Usage:`\
`   osc importsrcpkg SRPM `\
\
`Options:`\
`   -h, --help          show this help message and exit`\
`   -c, --commit        commit the new files`\
`   --delete-old-files  delete existing files from the server`\
`   -d description, --description=description`\
`                       set the description of the package`\
`   -t title, --title=title`\
`                       set a title`\
`   -n name, --name=name`\
`                       specify a package name`\
`   -p project, --project=project`\
`                       specify the path to a project`

-   download SRPM

`# wget --directory-prefix=/source/imports --mirror --reject index.html* -r -nH --no-parent `[`http://download.tizen.org/releases/2.3/2.3-mobile/tizen-2.3-mobile_20150311.3/repos/target/source/`](http://download.tizen.org/releases/2.3/2.3-mobile/tizen-2.3-mobile_20150311.3/repos/target/source/)

-   import SRPM to OBS project(Tizen:2.3)

Before run this script file, there are only SRPM files in
\'/source/imports\' directory and you have to also create OBS
project(Tizen:2.3).

`#!/bin/sh`\
`sudo osc checkout Tizen:2.3`\
`cd Tizen\:2.3/`\
`` RPMLIST=`ls /source/imports` ``\
`for RPMNAME in $RPMLIST`\
`do`\
`    sudo osc importsrcpkg /source/imports/$RPMNAME`\
`done`\
\
`` PKGLIST=`ls` ``\
`for PKGNAME in $PKGLIST`\
`do`\
`    sudo osc add ${PKGNAME}/*`\
`done`\
\
`sudo osc ci -m "commit the src"`

ref:
<https://en.opensuse.org/openSUSE:Build_Service_private_instance_boot_strapping#Use_Repository_Binary_Import>

[Category:Tool](Category:Tool "wikilink")
