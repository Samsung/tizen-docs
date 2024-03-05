Using OBS to build AArch64 Tizen application
--------------------------------------------

This manual describes work with [Official Tizen
OBS](https://build.tizen.org)

At the moment porting Tizen onto AArch64 architecture is in progress but
base set of packages needed for build is nearly complete. This set is
placed in
[devel:arm\_toolchain:Mobile:Base](https://build.tizen.org/project/show?project=devel%3Aarm_toolchain%3AMobile%3ABase)
project and could be connected to any project developer wants to use.

osc tool is commonly used to interact with [OBS](OBS "wikilink")
servers, you can install it using your OS package manager. First of all
you will need Tizen tool repository enabled like it described in
[Developer
Guide](https://source.tizen.org/documentation/developer-guide/installing-development-tools).
And then you may just install osc tool

`# Ubuntu example`\
`$ sudo apt-get update`\
`$ sudo apt-get install osc`

Current status
--------------

Now we have a working toolchain and development tools in
[devel:arm\_toolchain:Mobile:Base
project](https://build.tizen.org/project/show?project=devel%3Aarm_toolchain%3AMobile%3ABase)
which you may use to build your software and almost the whole
Tizen:Common in [devel:arm\_toolchain:Mobile:Main
project](https://build.tizen.org/project/show?project=devel%3Aarm_toolchain%3AMobile%3AMain).

There are still some problems with a few packages listed at
[OSDev/AArch64\_porting](OSDev/AArch64_porting "wikilink") status page.

The firmware can be built using *mic* tool and booted up using ARM64
simulator like ARM FastModels.

Creating own development project
--------------------------------

This manual describes project creation at *build.tizen.org* OBS. If you
want to set up your dedicated instance, please read
[OSDev/Creating\_AArch64\_Project](OSDev/Creating_AArch64_Project "wikilink")
page.

If you want to use current AArch64 toolchain you may create your own
(home or team) project in OBS. Two things are needed to do that:
tizen.org account and OBS access permission.

Then there are three steps to use binaries.

:\# Add *aarch64* architecture to your project: either through web
interface \"Repositories\" section or by adding tags to Meta info
directly.

:\# Edit project Meta at
*<https://build.tizen.org/project/meta?project=PRJ>* and add link to
devel:arm\_toolchain:Mobile:Main with
*<path project="devel:arm_toolchain:Mobile:Base" repository="aarch"/>*
line. You may see example at
[devel:arm\_toolchain:Mobile:Main](https://build.tizen.org/project/meta?project=devel:arm_toolchain:Mobile:Main)
Meta page.

:\# Add project config and tune your project for your needs. Example of
project config for Tizen AArch64 can be seen at
[devel:arm\_toolchain:Mobile:Main](https://build.tizen.org/project/prjconf?project=devel:arm_toolchain:Mobile:Main).

:\# Switch on build for aarch64 in *Repositories* section of your
project

After changes are performed Project Meta page should have something like
this:

<repository name="AArch">\
<path project="devel:arm_toolchain:Mobile:Main" repository="aarch"/>\
<arch>`aarch64`</arch>\
</repository>

After these actions OBS should start building your packages for AArch64
using prebuilt toolchain.

At the moment this toolchain should be enough for building daemons or
console applications.

Now you may upload a package you want to build using osc tool. For
example if you want to build your own bash package you may copy it from
Tizen:Mobile and build for AArch64 in your project

`$ osc copypac Tizen:Mobile bash YourTeam:YourProject bash`

And the you may look at build process in web interface.

For local build using osc:

`$ osc co YourTeam:YourProject bash`\
`$ cd YourTeam:YourProject/bash`\
`$ osc build AArch aarch64`

If you want to create new package you may use

`$ osc mkpac pkg`\
`$ cd pkg`\
`$ # placing sources and .spec file:`\
`$ cp /home/developer/pkg/{pkg-1.0.tar.gz,pkg.spec} .`\
`$ osc ar`\
`$ osc commit -m 'Initial commit'`\
`$ osc rebuild`

And then wait until build finishes.

[Category:Tool](Category:Tool "wikilink")
