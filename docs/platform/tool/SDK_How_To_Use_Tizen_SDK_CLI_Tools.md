The Tizen Software Development Kit ([SDK](SDK "wikilink")) is a
comprehensive set of tools for developing Web applications, native
applications, and the platform component for Tizen. The SDK contains an
install manager, IDE, tools, documents, samples, and a platform image.

Introduction
------------

The CLI (command line interface) provides functional tools for
developing Tizen Web applications and native applications without the
Tizen SDK IDE. It includes the entire developing process from creating
to running and debugging the project. If you only want to install CLI
and emulator, you can install a Minimal SDK, emulator and a platform
image.

Install Tizen Minimal SDK, Emulator and a Platform Image
--------------------------------------------------------

If you have never installed Tizen SDK before, please refer to
[Installing Tizen
SDK](https://developer.tizen.org/downloads/sdk/installing-tizen-sdk)\]

-   Choose a Minimal SDK \"Minimal\". Select \"Web app tools\" and
    \"Native app tools\"

![](Minimal-SDK1.png "Minimal-SDK1.png")

<li>

If you want to install Tizen Emulator, then you need to switch to
\"Custom\". Select \"Common tools\" -\> \"Emulator\" and \"Platforms\"
-\> \"Tizen 2.1\" -\> \"Platform Image\"

</li>

![](Minimal-SDK2.png "Minimal-SDK2.png")

</ul>

How To Use Web CLI
------------------

The CLI is located in the \$<TIZEN_SDK_HOME>/tools/ directory. For
developing the application using the CLI, set path to the CLI directory
using the following command:

`$ export PATH=$PATH:/home/username/tizen-sdk/tools/ide/bin`

Note that replace the username to a real username. webtizen is an
encapsulation of web-list, web-gen, web-signing, web-packaging,
web-install, web-run, web-debug and web-uninstall. You can also use them
independently.

-   Generate a new web project.

<!-- -->

-   Generate a web project by default.

\$ webtizen -g \--name WebSample \--path \~/workspace/

<li>

Search a template web project.

</li>

`$ web-template --search tizen`\
`tizenwebuifw-singlepage - Tizen Web UI Framework - Single Page.`\
`tizenwebuifw-navigation - Tizen Web UI Framework - Navigation.`\
`tizen-basic - Tizen basic Application.`\
`tizenwebuifw-masterdetail - Tizen Web UI Framework - MasterDetail.`\
`tizenwebuifw-common-resources - Tizen Web UI Framework - common resources.`\
`tizenwebuifw-multipage - Tizen Web UI Framework - Mutil Page.`

There are some samples in the directory
\~/tizen-sdk/tools/ide/realm/template/

</ul>
<li>

Create a signature.

</li>

-   Create a certificate firstly.

\$ cd \~/tizen-sdk/tools/certificate-generator/

`$ ./certificate-generator.sh`

Input some necessary messages such as password and name as below.

![](Minimal-SDK-Certificate.png "Minimal-SDK-Certificate.png")

Then a \*.p12 file will be created in the current directory.

<li>

Modify the key path in template profiles.xml.

</li>

`$ vi ~/tizen-sdk/tools/ide/sample/profiles.xml`

Modify the key path to the key you just created. Note that replace the
username to a real username.

<?xml version="1.0" encoding="UTF-8"?>

<profiles>\
`        `<profile name="test">\
`                `<profileitem author="true" identifier="%a:%f:%w:%h:%t" key="/home/username/tizen-sdk/tools/certificate-generator/sign.p12"
 ca="/home/username/tizen-sdk/tools/certificate-generator/certificates/developer/tizen-developer-ca.cer"/>\
`                `<profileitem author="false" identifier="%a:%f:%w:%h:%t" key="/home/username/tizen-sdk/tools/certificate-generator/sign.p12"
 ca="/home/username/tizen-sdk/tools/certificate-generator/certificates/developer/tizen-developer-ca.cer"/>\
`        `</profile>\
</profiles>

<li>

Create a signature for the web project.

</li>

`$ cd ~/workspace/WebSample/`\
`$ webtizen -s --nocheck -p test:/home/username/tizen-sdk/tools/ide/sample/profiles.xml`

Note that replace the username to a real username.

Input author password and Distributor password which are the same with
the password of the key you created before.

A signature file signature1.xml will be created.

Note: If you have created project with Tizen 2.1.0 SDK IDE, there are
.project file and .setting folder in each project.To create a correct
signature by CLI, you need to remove them manually or using \"-e\"
option to exclude them.

</ul>
<li>

Package files into a widget.

</li>

`$ webtizen -p --nocheck WebSample.wgt ../WebSample/`

<li>

Install the widget into the target.

</li>

`$ webtizen -i -w WebSample.wgt`

If you connect two or more targets, you need to add the parameter \"-d
serial number\", such as \"-d Medfieldxxx\" or \"-d emulator-26100\".

<li>

List web applicaton info installed by user.

</li>

`$ webtizen -l `

\"Package ID\" and \"App ID\" will be listed.

<li>

Launch the app on the target

</li>

`$ webtizen -r -i tSkijLbOmo.WebSample(App ID)`

<li>

Debug the app.

</li>

`$ webtizen -d -i tSkijLbOmo.WebSample(App ID)`

Note that debug dialog cannot be shown up with connecting IA device.

<li>

web-uninstall can uninstall the widget.

</li>

`$ webtizen -u -i tSkijLbOmo(Package ID)`

</ul>

How To Use Native CLI
---------------------

-   Create a native project.

\$ native-gen project -n NativeSample -s form

`Creating a project: NativeSample...`\
`A project was created successfully in /home/username/workspace/NativeSample`\
`To build a project, run native-make in /home/username/workspace/NativeSample/CommandLineBuild.`

Because Native CLI only can be used in the directory
{Project}/CommandLineBuild/, you need to create a project by native-gen
with the same as your project\'s like below, then copy the
CommandLineBuild folder to your own project.

`$ native-gen project -n Calculator -s form`

<li>

Compile the project.

</li>

`$ cd NativeSample/CommandLineBuild/`\
`$ native-make  -a i386 -t LLVM-3.1`

If you want to add the parameters --n --v, please use as this -n \"Tizen
Emulator 2.1\" -v \"Tizen 2.1\".

A \*.exe file is compiled out named NativeSample.exe

<li>

Package the project with signature.

</li>

`$ native-packaging -ak /home/username/tizen-sdk/tools/certificate-generator/sign.p12 -ap 1234 `

Note that replace the username to a real username.

A \*.tpk file is packaged.

<li>

Install the tpk onto target.

</li>

`$ native-install -p B4k8jHVcdG-1.0.0-i386.tpk`\
`B4k8jHVcdG-1.0.0-i386.tpk        3249 KB/s (176309 bytes in 0.052s)`\
`path is /opt/usr/apps/tmp/B4k8jHVcdG-1.0.0-i386.tpk`\
`__return_cb req_id[1] pkg_type[tpk] pkgid[B4k8jHVcdG] key[start] val[install]`\
`__return_cb req_id[1] pkg_type[tpk] pkgid[B4k8jHVcdG] key[install_percent] val[0]`\
`__return_cb req_id[1] pkg_type[tpk] pkgid[B4k8jHVcdG] key[install_percent] val[60]`\
`__return_cb req_id[1] pkg_type[tpk] pkgid[B4k8jHVcdG] key[install_percent] val[100]`\
`__return_cb req_id[1] pkg_type[tpk] pkgid[B4k8jHVcdG] key[end] val[ok]`\
`spend time for pkgcmd is [5559]ms`

If you connect two or more targets, you need to add the parameter \"-s
serial number\", such as \"-s Medfieldxxx\" or \"-s emulator-26100\".

<li>

Launch the app on the target.

</li>

`$ native-run -p B4k8jHVcdG (Package ID)`

<li>

Debug the app.

</li>

`$ native-debug -p B4k8jHVcdG`\
`(gdb)`

</ul>

[Category:Development](Category:Development "wikilink")
[Category:SDK](Category:SDK "wikilink")
[Category:Tool](Category:Tool "wikilink")
