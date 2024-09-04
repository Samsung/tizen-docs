Introduction
------------

This document provides information about mic redesign framework,
including the following aspects.

-   System composition
-   Work flow
-   File directory structure

System Composition
------------------

This section provides information about system composition of mic.

### Mic Instruction

#### What is mic?

MIC is an image creator. It\'s used to create images for Tizen.

#### How many types of images are supported by mic?

There are 5 types of images supported by mic, including live CD images,
live USB images, raw images for KVM, loop images for IVI platforms, and
fs images for chrooting.

#### What functions are provided by mic?

With the MIC tool, users can create images of different types for
different verticals. Also users can chroot into an image using MIC\'s
enhanced chroot command. Besides, MIC enables converting an image to
another image format, a very useful function for those sensitive to
image format.

### Mic Components

#### Main Program

-   The main program for mic is formed by three subcommands: create,
    convert, chroot.
-   They are user interfaces.

#### Config Manager

-   store the configure information from mic config-file.
-   keep the value of the options.
-   take as data center for other components

#### Plugin Manager

-   find all types of plugins from the plugin directory
-   store all found plugins in categories
-   provide interface to create, convert, and chroot

#### Plugin Class

-   consist of three types: imager, backend, hook
-   imager - implement the special interface for create, convert, and
    chroot:

` do_create, do_pack, do_unpack`

-   backend - provide interface to use package manager
-   hook - deal the hook function
-   considered as mid-ware between main program and imager class

#### Imager Class

-   Implement the necessary interfaces of the image creating and
    converting process
-   such as mount, install, configure, umount

### Mic System Composition Diagram

<File:MIC_system_composition.PNG%7CMic> System Composition Diagram

Work Flow
---------

The mic flowchart include three parts: main option parse, sub option
parse,and result output.

The first part parse \"sudo mic create/convert/chroot/help\" do\_option
mathod object. Parsing sub option is the second part by using first part
return do\_option object ,includeing file arg, setting mic format image
arg and so on. Last part output files and information about mic.

<File:Mic> System Flowchart.png\|Mic System Flowchart

File Directory Structure
------------------------

This section provides information about mic file directory structure.

### The directory structure

A simple description about the file directory structure omitted some of
the compiler configuration files and some documentation.

:   

    :   

`   Mic`\
`   | ----- Makefile`\
`   | ----- mic`\
`   | -----| ----- archive.py`\
`   |      | ----- bootstrap.py`\
`   |      | ----- chroot.py`\
`   |      | ----- conf.py`\
`   |      | ----- creator.py`\
`   |      | ----- imager`\
`   |      |      | ----- baseimager.py`\
`   |      |      | ----- fs.py`\
`   |      |      | ----- livecd.py`\
`   |      |      | ----- liveusb.py`\
`   |      |      | ----- loop.py`\
`   |      |      | ----- raw.py`\
`   |      | -----  msger.py`\
`   |      | -----  pluginbase.py`\
`   |      | -----  plugin.py`\
`   |      | -----  utils`\
`   | -----  plugins`\
`   |      | ----- backend`\
`   |      |      | ----- yumpkgmgr.py`\
`   |      |      | ----- zypppkgmgr.py`\
`   |      | -----  hook`\
`   |      |      | ----- empty_hook.py`\
`   |      | -----  imager`\
`   |      |      | ----- fs_plugin.py`\
`   |      |      | ----- livecd_plugin.py`\
`   |      |      | ----- liveusb_plugin.py`\
`   |      |      | ----- loop_plugin.py`\
`   |      |      | ----- raw_plugin.py`\
`   | -----  tests`\
`   | -----  tools`\
`   |      | ----- mic`

### Directory Use Instructions

-   Mic package is formed with three sub-packages: mic main
    sub-package,mic plugins sub-package,and mic tools sub-package.

<!-- -->

-   The directory \`mic/\` presents mic main sub-package, \`plugins\`
    presents mic plugins sub-package, and \`tools/\` presents mic tools
    sub-package.

<!-- -->

-   The code will be placed in categories in \`mic/\`. Main program
    class will be placed in \`mic/\` , imager class will be placed in
    \`mic/ imager/\`,some common code and utility code could be placed
    in \`mic/utils/\`.

<!-- -->

-   Some plugin creator could be placed in \`plugins/\` .

<!-- -->

-   Code for unit test would be placed in tests/.

[Category:Tool](Category:Tool "wikilink")
