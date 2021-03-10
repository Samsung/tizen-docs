Start Tizen Common Emulator through Tizen IVI SDK
=================================================

Install Tizen IVI SDK
---------------------

You can refer to this wiki page [Tizen IVI
SDK](https://wiki.tizen.org/wiki/Tizen_IVI_SDK) to install Tizen IVI
SDK.

Download Tizen Common Emulator image
------------------------------------

Tizen [Common](Common "wikilink") [Emulator](Emulator "wikilink") image
can be built out automatically. You can download it at this link

-   <http://download.tizen.org/snapshots/tizen/common/latest/images/#>
    emulator32-wayland/common-emulator-qa-unsafe-wayland-mbr-i586/.

TODO: update link to more recent than:

-   <http://download.tizen.org/releases/milestone/tizen/common-3.0.2015.Q2/>

Modify Emulator Image
---------------------

-   Enlarge the loop image root partition size.

`$ e2fsck -f tizen-common.img`\
`$ resize2fs tizen-common.img 3900M`

-   Change the loop format to qcow2 format.

`$ ~/tizen-sdk/tools/emulator/bin/qemu-img convert -O qcow2 tizen-common.img emulimg-3.0.x86`

Create a Tizen Common Emulator
------------------------------

1\. Launch Emulator Manager.

2\. Click \"ivi-custom\" lable. Select \"Base image\" and find the image
emulimg-3.0.x86 you downloaded. Name it and then click \"Confirm\"
button.

![](Create_Common_Image.png "Create_Common_Image.png")

3\. Launch it.

### LINKS

-   <https://wiki.tizen.org/wiki/Emulator>

[Category:Common](Category:Common "wikilink")
[Category:Tool](Category:Tool "wikilink")
