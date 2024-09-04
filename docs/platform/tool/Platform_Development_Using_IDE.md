Tizen IDE
---------

<big>Tizen IDE</big> is released with all SDK versions. Platform
developers across the community can take advantage of using <big>Tizen
IDE</big> as complete tool for Platform Development. The following
method is for the Ubuntu Linux Version of Tizen IDE. Using <big>Tizen
IDE</big>, one can do following (but is not limited to):

-   Compile Platform Modules directly from Tizen IDE by selecting
    appropriate architecture & rootstrap.
-   Browse and clone all existing git repos using IDE.
-   Update rootstrap automatically from IDE.
-   Minimize usage of terminal window by enabling Platform Development
    using IDE.
-   Perform all git operations from IDE itself (add, merge, push, create
    branch... and so on).
-   Perform debugging of modules inside IDE after building and updating
    rootstrap.

At present, Tizen 2.2.1 version is the current version in public and can
be downloaded from
[<https://developer.tizen.org/downloads/tizen-sdk>](https://developer.tizen.org/downloads/tizen-sdk).

Installation
------------

### Supported OS Versions

Here are the excerpts from www.tizen.org regarding supported OS versions
for installing Tizen SDK.

-   Ubuntu® 12.04 or 12.10 (32- or 64-bit)
-   Microsoft Windows® XP (32-bit) Service Pack 2 or later
-   Microsoft Windows® 7 (32- or 64-bit)
-   Apple Mac OS® X 10.7 Lion (64-bit)
-   Apple Mac OS® X 10.8 Mountain Lion (64-bit)

The following method explains the installation procedure in <big>Ubuntu®
12.04 LTS</big> version. The installation method should be the same in
other supported versions as well.

### Prerequisites

-   Make sure all typical installations are in place. Refer to this
    guide for details:
    [developer-guide](https://source.tizen.org/documentation/developer-guide)
-   Make sure latest GBS version is installed in the system. Otherwise
    execute the following commands:

:   

    :   `sudo apt-get update`
    :   `sudo apt-get install gbs`

-   Install the following two required packages using the commands
    below:

:   

    :   `sudo apt-get install ruby`
    :   `sudo apt-get install expect`

### IDE Installation

While installing IDE, in \"Configure\" tab, select \"Custom\" option,
then select:

-   Platform Development option &
-   Platforms option

Not all components inside \"Platforms\" option are selected by default.
Select the complete \"Platforms\" option for enabling IDE for platform
development. Once installed successfully, one new category "Tizen
Platform Project" appears in the project wizard.

Configurations
--------------

### Network Configuration

To enable git operation, you need to set proxy information, if the
working PC is behind the proxy server. To setup the proxy go to Window
Menu \>\> Preferences \>\> General \>\> Network Configuration. Select
\"Active Provider\" as Manual. Set the HTTP & HTTPS proxy. Do not enter
anything under <big>SOCKS</big>. By default it is selected, it should be
empty without any proxy information.

### Site Configurations

After setting up the network in IDE, you need to set the git server
information. To set git server information, go to Window Menu \>\>
Preferences \>\> Tizen SDK \>\> Platform \>\> Site Configurations. Click
\"Add\" and enter \"Name\". The field \"Git Base URI\" should be in the
form of `"`[`ssh://`](ssh://)<your-id>`@review.tizen.org:29418"`. The
\"Location\" field should be set with
`"`[`https://review.tizen.org/git/`](https://review.tizen.org/git/)`"`.
The \"Location\" field URI must point to the page where all git repo
information is kept on the server. Tizen IDE downloads the git repo list
into Tizen IDE for cloning. Press \"Ok\" and then click \"Update\" and
wait. In this step,all git repo information will populate into Tizen
IDE.

All git repos available of configured server at \"File Menu \>\> New
\>\> Tizen Platform Project \>\> Git\" page.

Creating a Project
------------------

### Cloning a Project

Once the update is successful, go to New » Tizen Platform Project menu
option. If there is failure in the update, recheck Network Connection
and Site configurations. To develop "EFL Application" or to create \"New
Project\", click "Template". Otherwise, open the \"Git\" tab. Select a
project from the left pane. Give the project name, click \"Finish\".

The selected project is cloned from git. Repeat this step to clone more
projects from git.

### Changing the Snapshot Path

Post installation, IDE needs to point correct snapshots as per
requirement. Select \"Tizen Platform\" perspective in IDE. Open Windows
» Show View » Rootstrap View, if \"Rootstrap View\" window is not
present. Right-click on any profile Emulator or Device in Rootstrap view
to highlight \"Manage Packages\". Snapshot information is kept in
\"Manage Packages\". Snapshot information can be edited and pointed to
correct snapshot.

For <big>Tizen 3.0</big> (armv7l) development, new rootstrap can be
created using RD-PQ snapshot
[[`http://download.tizen.org/snapshots/tizen/rd-pq/latest/`](http://download.tizen.org/snapshots/tizen/rd-pq/latest/)](http://download.tizen.org/snapshots/tizen/rd-pq/latest/)
as follows. This is just one example. Any working snapshot can be used
for generating rootstrap.

Click on the + (plus) sign on the right top of the Rootstrap View. Give
name of this RootStrap view Paste
[`http://download.tizen.org/snapshots/tizen/rd-pq/latest/`](http://download.tizen.org/snapshots/tizen/rd-pq/latest/)
in \"Snapshot URL\" text box and click \"Search\". It will automatically
fill the \"Architecture\" based on Snapshot URL. Select the \"Generate
Immediately\" check box and press OK. It will download packages and
create the rootstrap.

### Package Manager

In Package Manager, you can Add, Modify, Remove snapshot paths. Also,
other operations with packages like Refresh, Upgrade, Install,
Uninstall, etc., can be performed. In Package Manager, installed
versions of all packages, as well as new version available on the
server, are displayed in a table.

### GBS Options Setting

To set the required GBS options, go to \"Window Menu \>\> Preferences
\>\> C/C++ Build \>\> Tizen Settings\". Various GBS options can be
selected or removed, as per project need.

### Git Operations

To access the git operation menu, right-click on project and select
\"Team\". All git operations like Switch to (branch), Commit, Pull,
Merge, Push, etc., can be invoked from here.

Branch name is appended to the package project name for easy
identification as follows: \>appfw \[appfw <big>tizen</big>\] To switch
to a different branch, right-click on Project -\> Team -\> Switch To -\>
New branch -\> Source ref: Select appropriate branch from the list. A
new branch can also be created from here.

### Compilation

Once the desired snapshot path is selected, the Package Manager can be
closed. To select the required rootstrap, right-click on it and
\"Select\". Alternatively, while selecting the \"Active Build
Configuration\" of a project, the appropriate rootstrap automatically
gets selected. If there are two or more rootstraps for a particular
architecture, the appropriate rootstrap needs to be selected by
right-clicking over it.

To build a project, first right-click on the project in the Project
Explorer and select \"Active Build Configuration\". It will download all
the required packages from server & build after that. Then right-click
and select \"Build Project\".

### Debugging

There are inherent difference between debugging application and module.
Application debugging can be performed just by launching it in debug
mode. But for debugging module, first it needs to select source
application to start debugging.

#### Steps to debug application in emulator environment

1.  Clone the required application in Tizen IDE and change to the
    required branch.
2.  Select the appropriate rootstrap from the \"RootStrap View\" window
    for the emulator.
3.  Build the project with proper Active Configuration.
4.  Set the required breakpoints in the code.
5.  Launch the application by right-clicking on the project and
    selecting <big>Debug As \>\> Tizen Platform Project</big>. It will
    open \"Launch Configuration\" window. Press \"Next\".
6.  In this step it updates the rootstrap with the current compiled
    version of application.
7.  Click \"Remote Browse\" and select the appropriate binary of the
    application under a remote bin directory.
8.  It launches the application and changes IDE to \"Debug Perspective\"
    for debugging.
9.  Set breakpoint will be hit, if it is in the execution path.

#### Steps to debug application in target environment

The above steps can be performed to debug applications in Target
Environment, except:

1.  Select the device rootstrap.
2.  Select the proper \"Active Build Configuration\"
3.  Target should be connected to the PC, with the appropriate settings.

#### Steps to debug a platform module in the emulator/target environment

1.  Clone a platform module and change to the appropriate branch.
2.  Select the appropriate rootstrap from RootStrap View window for
    emulator/target.
3.  Build the project with the proper Active Configuration.
4.  Set the required breakpoints in code.
5.  For target debugging, make sure it is connected to the development
    PC.
6.  Launch by right-clicking on project select <big>Debug As \>\> Tizen
    Platform Project</big>. It will open the \"Launch Configuration\"
    window.
7.  Select the proper \"Tizen Application Project\" from the drop-down
    menu and press \"Next\".
8.  The rootstrap updates with the current compiled version of the
    module.
9.  Click \"Remote Browse\" and select the appropriate binary of
    application under remote bin directory, which actually use the
    platform module.
10. This launches the application and changes IDE to \"Debug
    Perspective\" for debugging.
11. Set the breakpoint to be hit, if it is in execution path or
    otherwise traverse to the breakpoint.

Tizen IDE is customized to enable all kinds of developments related to
Tizen. Using IDE, one can develop all kinds of supported applications,
as well as develop platform modules. To get more information, read the
official documentation at [Platform Development with the
IDE](https://developer.tizen.org/dev-guide/2.2.1/org.tizen.platform.development/html/platform_dev_process/platform_dev_process.htm)

[Category:Tool](Category:Tool "wikilink")
