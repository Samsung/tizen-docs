mic-chroot Manual Page
----------------------

`  Author: Tizen`

Name
----

`  mic chroot (ch) - Runs command or interactive shell inside an image.`

Synopsis
--------

`   mic chroot (ch) [-h, --help]`\
`                   [-s SAVETO, --saveto=SAVETO]`\
`                   `<Image_File>\
`                   [Command [Arguments] ... ]`

Description
-----------

This command runs command or interactive shell inside an image.

MIC can create various types of images, including fs, livecd, liveusb,
loop and raw, only the fs type image can be chroot into by using the
ordinary Linux \`chroot\` command. \`mic chroot\` enables users to
chroot into the other types of images by enhancing the original
\`chroot\` command provided by Linux.

An example is shown below:

:   

    :   

`   $ sudo mic cr loop handset_blackbay.ks`

`   $ cd mic-output/`

`   $ sudo mic chroot platform.img`\
`     mic 0.22.3 (Ubuntu 12.10 quantal)`\
`     INFO: Launching shell. Exit to continue.`\
`     ----------------------------------`\
`     bash-4.1#`\
`   $ sudo mic chroot platform.img ls`\
`     mic 0.22.3 (Ubuntu 12.10 quantal)`\
`     INFO: Launching shell. Exit to continue.`\
`     ----------------------------------`\
`     bin  boot  dev  etc  lib  lost+found  proc  run  sbin  sys  tmp  usr  var`

Parameters
----------

### Mandatory Parameters

`   `<Image_File>`        Specifies the source image to be processed.`

### Optional Parameters

`   -h, --help          Shows this help message and exit.`\
`   -s SAVETO, --saveto=SAVETO`\
`                       Saves the unpacked image to specific directory.`\
`   Command [Arguments] ...`\
`                       Runs specific Linux command after executing chroot.`

[Category:Tool](Category:Tool "wikilink")
