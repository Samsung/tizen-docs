This tutorial demonstrates how to install [HTML5](HTML5 "wikilink")
application, packages as wgt files, on devices with
Tizen:[Common](Common "wikilink") and other [Tizen3](Tizen3 "wikilink")
profiles as well as how to run installed HTML5 applications using the
[Crosswalk](Crosswalk "wikilink") web runtime.

Install
-------

Follow the instructions below to transfer, install and launch an
application to Tizen [device](device "wikilink") or
[Emulator](Emulator "wikilink") with Tizen [IVI](IVI "wikilink") or
another Tizen 3 profile based on Tizen:Common:

1.  Make sure that [SDB](SDB "wikilink") is running on the device. For
    example, execute the following command as root on the device to
    start it on port <port>:
        sdbd --listen-port=<port>

2.  Connect to the devices using sdb by executing the following command
    on a personal computer:
        sdb connect <IP of the Tizen device>:<port>

3.  Verify that the device appears at the list of connected devices:
        sdb devices

4.  Update wgt file to an appropriate directory at the device, for
    example:
        sdb push <wgt file> /home/bob/

5.  Open a terminal on the device on the behalf of an existing user.
6.  Install the web application by running the following command:
        pkgcmd -i -t wgt -p <wgt file> -q

7.  Verify that the application has been installed successfully and
    retrieve its ID:
        app_launcher -l

8.  Launch the application using its ID:
        app_launcher -s <Application ID>

The application can be terminated through the command line with the
following command:

    app_launcher -k <Application ID>

Uninstall
---------

Replace <package> with the corresponding package name of the application
and execute the following command in shell to manually uninstall it:

    pkgcmd -u -n <package>

Troubleshooting
---------------

You might be unable to install wgt file due to the following issues:

-   The package your installing is using the same id as another package
    and they conflict. You should uninstall the other package first.
-   The icon reference in config.xml does not map to an image file.

[Category:IVI](Category:IVI "wikilink")
[Category:SDK‏‎](Category:SDK‏‎ "wikilink")
[Category:Tool](Category:Tool "wikilink")
