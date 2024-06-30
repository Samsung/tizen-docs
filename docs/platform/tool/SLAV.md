Overview
========

The initial motivation behind this project was to aid team of release
engineers in automated testing on different hardware specifications,
different operating system versions, etc. [Tizen Image Testing
System](https://wiki.tizen.org/Laboratory) was developed to achieve
this. The laboratory has resolved the initial problem, but it wasn\'t
extensible and could be used only by release engineers. SLAV was
designed to aid during whole life-cycle of operating system development.

Starting from hardware part of the project- MuxPi was designed to be
extensible. Currently following add-ons were created:

-   Microphone + Speaker - to allow voice interaction with target device
    (e.g. use-case is testing voice assistant)
-   IrDA - to allow test automation of TV (many modern TVs will go into
    specific modes only when specific data is sent via IrDA)
-   Plotter - mechanical touchscreen interactions (e.g. use-case is
    testing secure applications, like banking, where some data cannot be
    sent via SW events- like PIN code)

SLAV elements
-------------

SLAV stack topology:

![image](Slav_topology.jpg "image"){width="640"}

[Read more about **MuxPi**](https://wiki.tizen.org/MuxPi)

**Boruta** is the device farm manager:

-   maintains list of registered MuxPi devices with capabilities of
    connected devices
-   provides status of MuxPi target devices
-   manages requests for test devices access with attention to:
    -   priorities
    -   time schedulign
    -   requested capabilities and interfaces
-   provides API for
    -   requesting and acquiring direct access to test devices
    -   listing devices, their capabilities and states
    -   booking targets for specific time
-   controls access and time windows for working with target

**Weles** is a simple, generic test framework using Boruta for accessing
devices.

-   maintains list of test requests
-   uses Boruta for accessing test devices
-   uses muxPi boards for:
    -   flashing test devices
    -   booting test devices
    -   running tests
-   collects test results and artifacts
-   provides API for:
    -   scheduling tests
    -   monitoring tests status
    -   gathering results and artifacts
-   uses LAVA compatible test description files

Whole test is described by a single yaml file in a format compatible
with Linaro LAVA specification.

The file defines:

-   required capabilities of the target
-   timeouts
-   priority
-   images and partition layout for preparing test device
-   interface for accessing target
-   credentials, input sequences
-   test cases to be run defined as a list of:
-   commands for controller
-   commands for target
-   files to be pushed to target
-   artifacts to be collected from a target

**Perun** is the release engineering test system designed to verify
prerelease and snapshot binary images on different types of test devices
using Weles test framework:

-   monitors publication and downloads prerelease and snapshot binary
    images
    -   compares prerelease images with snapshot images and decides if
        they should be tested
    -   delegates tests to Weles
    -   collects and interprets test results
    -   publishes tests results for binary images

Links
-----

**Wiki:**

<https://wiki.tizen.org/MuxPi>

<https://wiki.tizen.org/SDWire>

<https://wiki.tizen.org/SD_MUX>

**Repositories:**

<https://review.tizen.org/gerrit/#/admin/projects/tools/muxpi-overlay>

<https://review.tizen.org/gerrit/#/admin/projects/tools/muxpi>

<https://review.tizen.org/gerrit/#/admin/projects/tools/boruta>

<https://review.tizen.org/gerrit/#/admin/projects/tools/weles>

<https://review.tizen.org/gerrit/#/admin/projects/tools/perun>

<https://review.tizen.org/gerrit/#/admin/projects/tools/slav>

[Category:Tool](Category:Tool "wikilink")
