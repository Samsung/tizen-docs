Apache Cordova is a mobile software development framework, underlying
PhoneGap.

Consider using it when HTML5 is not enough for
[Application\_Development](Application_Development "wikilink").

### Onsen UI:

![](Monaca.png "Monaca.png")

Monaca / OnSen is providing cloud IDE facilities for
[hybrid](hybrid "wikilink") [mobile](mobile "wikilink")
[Application\_Development](Application_Development "wikilink") based on
(Phonegap/Cordova).

-   <https://monaca.io/>

Tizen is not fully supported but it\'s possible to repackage app.

Here are some hints

-   Register and start IDE : <https://monaca.mobi/en/dashboard>
-   Create project / Sample Apps
-   \"Bricks\"
-   Open : <https://ide.monaca.mobi/project/#>\...
-   File / Export project
-   Title: bricks
-   unzip project.zip
-   Adapt [wgt](wgt "wikilink")\'s config.xml or replace to something
    based on this minimal config.xml :

<!-- -->

    <?xml version="1.0" encoding="UTF-8"?>
    <widget xmlns="http://www.w3.org/ns/widgets" xmlns:tizen="http://tizen.org/ns/widgets"  id="http://example.com/app" version="1.0.0" viewmodes="maximized">
      <tizen:application id="ComExample.main" package="ComExample" required_version="2.4"/>
      <content src="www/index.html"/>
      <feature name="http://tizen.org/feature/screen.size.all"/>
      <name>main</name>
      <tizen:setting context-menu="disable"/>
      <tizen:profile name="mobile"/>
    </widget>

-   -   If you keep generated config.xml make sure to:
        -   Declare in widget element this attribute :
            \"xmlns:tizen=\"<http://tizen.org/ns/widgets>\"
        -   Add \"tizen:application
        -   Keep content src=\"www/index.html\"
        -   Add <tizen:profile name="mobile"/>

-   Then deploy using [SDK](SDK "wikilink"), or CLI SDK (we assume you
    know about generating [certificates](certificates "wikilink"))

<!-- -->

    cert=tizen
    wgt_file=main.wgt
    package=ComExample
    ~/tizen-studio/tools/ide/bin/tizen build-web
    ~/tizen-studio/tools/ide/bin/tizen package -t wgt -s ${cert}
    ~/tizen-studio/tools/ide/bin/tizen install -n ${wgt_file} -- .
    ~/tizen-studio/tools/sdb  shell pkgcmd -l -t wgt
    ~/tizen-studio/tools/ide/bin/tizen run --pkgid ${package}

Et voila !

May sample code could be ported to Tizen, for instance check this
[OpenSource](OpenSource "wikilink")
[Application](Application "wikilink") using [React](React "wikilink")
[JavaScript](JavaScript "wikilink") framework:

-   <https://github.com/TizenTeam/react-onsenui-redux-weather/tree/tizen/mobile/2.4/master>
-   <https://github.com/frankdiox/OnsenUI-Todo-App/issues/3>

Ask me more \--[Pcoval](User:Pcoval "wikilink")
([talk](User_talk:Pcoval "wikilink")) 11:36, 23 October 2016 (UTC)

### Resources:

-   <https://download.tizen.org/misc/media/conference2012/wednesday/bayview/2012-05-09-1415-1455-enabling_cordova_aka_phonegap_on_tizen.pdf>
-   <https://download.tizen.org/misc/media/conference2013/slides/TDC2013-Porting_Cordova_on_Tizen.pdf>
-   <https://01.org/sites/default/files/phonegapdayseu2012-portingcordovatotizen.pdf>
-   <https://cordova.apache.org/docs/en/5.0.0/guide/platforms/tizen/>
-   <http://stackoverflow.com/questions/40800681/using-apache-cordova-plugins-for-tizen-project/40802207#40802207>

[Category:Application](Category:Application "wikilink")
[Category:Tool](Category:Tool "wikilink")
