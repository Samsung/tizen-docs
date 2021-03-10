If you\'re not using the [SDK](SDK "wikilink") (e.g. you don\'t have the
right operating system), but still want to install apps on a Tizen
developer device (as handed out at the Tizen conference), there is a
manual method you can use.

This article explains this method, showing how to manually package and
install an app using command line tools on Linux. (Note that it\'s
likely you could follow a similar process on Windows if you don\'t want
the whole SDK, e.g. using
[PuTTY](http://www.chiark.greenend.org.uk/~sgtatham/putty/) and
[7zip](http://www.7-zip.org/), though I\'m not sure how/if USB
networking works on Windows.)

If you want to read more generally about Tizen development, see [the
Tizen developer
documentation](http://developer.tizen.org/documentation).

NB I call the \"Tizen developer device\" a \"phone\" below, for brevity.

<h2>

Packaging an app

</h2>

Tizen apps are packaged according to [the W3C widget packaging
spec](http://www.w3.org/TR/widgets/). The steps below explain how to
manually create one of these packages, but for a real project you\'d
probably want to script it.

1.  Write your app first. As a minimum, you need an HTML page. Make a
    new file called `index.html` with this HTML in it:
        <!doctype html>
        <html>
          <head>
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Tizen test app</title>
          </head>
          <body>
            <p>Nominally a Tizen app...</p>
          </body>
        </html>

    (See [these
    docs](https://developer.apple.com/library/safari/documentation/appleapplications/reference/SafariHTMLRef/Articles/MetaTags.html)
    for more information about the viewport meta element. We add it here
    so the application appears fullscreen.)

2.  Create a 128x128 pixel png for an icon. If you can\'t be bothered to
    make one yourself, generate a placeholder by visiting the URL
    <http://placehold.it/180x180/icon.png> in your browser. Then save
    the image as `icon.png`, in the same directory as `index.html`. This
    icon is optional, but having one makes it slightly easier to find
    your application on the Tizen home screen. And you\'d want one in a
    real project.
3.  Add a `config.xml` file (which tells Tizen\'s web runtime how to
    install, display and run your app). It should look like this as a
    minimum:
        <?xml version="1.0" encoding="UTF-8"?>
        <widget xmlns="http://www.w3.org/ns/widgets"
                xmlns:tizen="http://tizen.org/ns/widgets"
                version="2.0 Beta"
                viewmodes="fullscreen"
                id="http://mydomain/myapp">
          <icon src="icon.png"/>
          <content src="index.html"/>
          <name>myapp</name>
        </widget>

4.  Make a zip file with your app\'s files in it, but give the file a
    `.wgt` suffix. For example, you can do this from a command line in
    your app\'s directory (the one containing `index.html`, `icon.png`
    and `config.xml`) like this:
        zip myapp.wgt config.xml index.html icon.png

    The zip file\'s structure will look like this:

        myapp.wgt
          index.html
          config.xml

<h2>

Installing an app on the phone

</h2>

1.  The next bit involves making a USB network connection between your
    PC and the phone. I found instructions on [Flashing to
    device](Flashing_to_device "wikilink"), but I repeat them here for
    convenience:
    1.  Turn the phone on.
    2.  Connect the phone to your computer via a USB lead.
    3.  On the phone\'s home screen, press the <em>Settings</em> icon;
        at the top of the settings screen, press <em>All</em> to show
        all settings. Then select <em>USB utilities</em> and check the
        <em>USB debugging</em> option. This enables the phone to act as
        a [usbnet device](http://www.linux-usb.org/usbnet/).
    4.  On the computer, configure the USB connection by entering the
        following:
            sudo ifconfig usb0 192.168.129.4

    5.  You should now be able to login to the device from the computer.
        On the computer (not the phone), use SSH from a command line
        like this:
            ssh root@192.168.129.3

        Check that this works before you try to do the next step.
2.  Once the ssh login works, you can copy the `.wgt` file to the device
    with scp:
        scp <path to .wgt file> root@192.168.129.3:/opt/home/root

3.  Now login to the device over SSH again:
        ssh root@192.168.129.3

    You should be in the /opt/home/root directory, where you scp\'d the
    file to.

4.  At the command prompt, install the widget with:
        wrt-installer -i myapp.wgt

    You should now see its icon on the home screen:\
    ![400 px\|App icon on the Tizen home
    screen](Myapp_on_tizen.jpg "fig:400 px|App icon on the Tizen home screen")

5.  Touching the icon should open it in the web runtime, like this:\
    ![400 px\|App running on
    Tizen](Myapp_running-in_wrt.jpg "fig:400 px|App running on Tizen")

That\'s it.

If anything goes wrong, you can uninstall the app on the phone via
<em>Settings \> All \> Manage applications</em>. Select the app from the
list, then click on the <em>Uninstall</em> button.

You can also update an existing app from the command line with:

    wrt-installer -iu myapp.wgt

(though if the app is running, you\'ll have to stop it to get the update
to take).

[Category:Application](Category:Application "wikilink")
[Category:Development](Category:Development "wikilink")
[Category:Tool](Category:Tool "wikilink")
