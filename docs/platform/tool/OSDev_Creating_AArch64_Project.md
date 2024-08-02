This guide describe creation of and AArch64 Tizen project from scratch
on your private [OBS](OBS "wikilink") instance. There are two main parts
of bootstrap process: server-side part and user-side part. Server-side
is done once for single OBS server environment --- this is importing
binary packages with toolchain and toolchain dependencies to a project.
We propose to create a single dedicated project without any sources,
just with these imported binaries which can be used by other project
during build.

Server-side part
================

Prerequisites
-------------

-   Local access to OBS server (not only API/web account but ssh or
    terminal access)
-   Access to [tizen.org download
    repository](http://download.tizen.org/live/devel:/arm_toolchain:/Mobile:/Base/aarch/)
-   Official step-by-step OBS project boostrapping manual from [openSUSE
    wiki](https://en.opensuse.org/openSUSE:Build_Service_private_instance)

Summary
-------

Process of creating and enabling of new project is described in details
at [OBS wiki
page](https://en.opensuse.org/openSUSE:Build_Service_private_instance).
The official manual suggests several approaches to project creation but
build.tizen.org project was created using [binary
import](https://en.opensuse.org/openSUSE:Build_Service_private_instance_boot_strapping#Use_Repository_Binary_Import)
method, so instructions here will describe it.

**In order not to damage OBS infrastructure, project bootstrapping
should be done accordingly to official manual for your version of OBS
environment**, this page just shows specific points for Tizen AArch64
project.

Importing binary
----------------

First of all the process is described in [Binary Import from the
web](https://en.opensuse.org/openSUSE:Build_Service_private_instance_boot_strapping#Binary_Import_from_the_web)
section of manual.

The only difference from official manual is package download path.

Prebuilt Tizen AArch64 binaries could be obtained from
*<https://download.tizen.org/live/devel:/arm_toolchain:/Mobile:/Base/aarch/>*
so the command you may use:

`wget --directory-prefix=/data/imports --reject index.html* --mirror --no-parent --no-host-directories --cut-dirs=8 `[`https://download.tizen.org/live/devel:/arm_toolchain:/Mobile:/Base/aarch/`](https://download.tizen.org/live/devel:/arm_toolchain:/Mobile:/Base/aarch/)

User-side part
==============

After binaries are imported and handled by OBS you won\'t need local
server access anymore. Now your OBS enviroment is capable of building
Tizen packages for AArch64 architecture and has toolchain, emulator and
basic libraries set.

This section can be performed using web interface and OBS API by any
user with \"Administrator\" rights in own project.

Prerequisites
-------------

-   Own or team project with administrator access rights (or OBS-wide
    rights to create such a project)
-   Packages sources

Project creation
----------------

As now you have a working AArch64 toolchain, you may just now go on with
[OSDev/Using\_OBS\#Creating own development
project](OSDev/Using_OBS#Creating_own_development_project "wikilink")

\]

[Category:Tool](Category:Tool "wikilink")
