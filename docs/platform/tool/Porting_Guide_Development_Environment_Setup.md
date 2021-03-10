This section provides a brief overview about setting up your development
environment on your host system, such as your Ubuntu\* system. The below
figure briefly describes the Tizen development environment setup.

![](Sdk.png "Sdk.png")

Follow the steps below to set up the development environment on your
Ubuntu system.

Tizen OS Development Setup
--------------------------

Please refer to the following links to set up the Tizen OS Development
environment and to obtain infomation regarding development.

<https://source.tizen.org/os-development>

1.  Work Flow

    :   This section explains GIT/Gerrit based source code management
        and review process, package creation using Open Build
        Service(OBS), and code submission methods, including development
        and upstream branches.

2.  Developer Guide

    :   This section describes registration and information on a
        development environment setup for GIT/Gerrit, SSH, GIT Build
        system, Image creator, and install tools. It includes the code
        and package submission using GIT and OBS buildsystem and the
        complete development flow.

3.  Git Build System

    :   The GBS(Git-Build-System) is a custom command line tool that
        supports Tizen package development. This section explains about
        auto-generating tarballs based on git repositories, performing
        local and report builds, and OBS code submission. This section
        also has procedure to monitor remote build log and status.

4.  MIC Image Creator

    :   This tools is used to create images for Tizen. This section
        provides detailed explainations of image creation, conversion
        and chrooting into image procedure.

As is explained in the above URLs, Tizen development requires Open(SuSE)
Build system and the required components. In the following sections, we
will briefly introduce various such build requirements.

Introduction to OBS
-------------------

The Open Build Service (OBS) is an open and complete distribution
development platform that provides a transparent infrastructure for
development of Linux distributions, used by openSUSE, MeeGo, and other
distributions. (Supporting also Fedora, Debian, Ubuntu, RedHat, and
other Linux distributions). OBS provides the developers an easy way of
using web-based and command based interface to achieve development
activities. OBS maintains a consistent build environment, which each
developer can rely on for various Linux distributions. For more
information on OBS, you can refer to this link:

<https://build.tizen.org/>

OBS can be set up locally or we can refer any available OBS services.
<http://doc.opensuse.org/products/draft/OBS/obs-best-practices_draft/cha.obs.best-practices.localsetup.html>
is one of the links that talks about setting up OBS server locally. To
make use of any available OBS servers, user credentials are required.
Each OBS implemetiation can have more customized tools to achieve the
build servies. You can find information on Tizen OBS and its customized
build tool, named git-build-System(GBS), in this link

<https://source.tizen.org/os-development/git-build-system/>

OBS Light
---------

OBS Light is an OBS base development process, but which is lighter to
use. It creates an encapsulation of OBS and presents a lighter face of
OBS.

### OBS Light server Appliance

This is a ready-to-use OBS for MeeGo and Tizen. openSUSE Build
Service(OBS) 2.3.0-1.6. The openSUSE Build Service appliance contains
the complete OBS stack, including a Worker, the Backend, API, Webclient,
and osc, the command line client. FakeOBS is an added utility, through
which we can achieve private OBS Builds.

### OBS Light Client Appliance

OBS Client Appliance consists of a command line (obslight) and a
graphical user interface GUI (obslightgui). OBS Client includes MIC to
create a bootable image.

<http://en.opensuse.org/openSUSE:OBS_Light_Manual>
<http://en.opensuse.org/openSUSE:OBS_Light_Fakeobs>
<http://susestudio.com/a/e0uuBG/obs-obs-server-obs-light>
<http://en.opensuse.org/openSUSE:OBS_Light_Installation>

Installation of SDK
-------------------

The Tizen SDK is a comprehensive set of tools for developing Tizen web
applications. It consists of Web IDE, Emulator, tool chain, sample code,
and documentation. The beta release of the Tizen SDK runs on Windows\*,
as well as Ubuntu. Tizen Web applications may be developed without
relying on an official Tizen IDE, as long as the application complies
with Tizen packaging rules. Use the link below to download the Tizen
SDK.

<https://developer.tizen.org/sdk>

[Category:Tool](Category:Tool "wikilink")
