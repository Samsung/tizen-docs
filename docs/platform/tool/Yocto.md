Yocto Project can be used to build Tizen [Common](Common "wikilink") and
Tizen:[IVI](IVI "wikilink") check subpages :

-   <https://wiki.tizen.org/wiki/Category:Yocto>

DEMOS
-----

Project was presented at various [Events](Events "wikilink"), latest on
is [FOSDEM](FOSDEM "wikilink") 2016 by
[User:Pcoval](User:Pcoval "wikilink") and
[User:Leon](User:Leon "wikilink")

-   <https://fosdem.org/2016/schedule/event/connected_tizen/>
-   <http://www.slideshare.net/SamsungOSG/connected-tizen-bringing-tizen-to-your-connected-devices-using-the-yocto-project>
-   <https://wiki.iotivity.org/tizen>
-   <https://github.com/TizenTeam/meta-yocto-demos>
-   <https://notabug.org/tizen/iotivity-example>
-   <https://vimeo.com/153263103#connected-tizen-20160131rzr>

[IoT](IoT "wikilink") demo code is about to be cleaned up\...

Ask [User:PCoval](User:PCoval "wikilink") and
[User:Leon](User:Leon "wikilink") for support.

Tizen:IVI
---------

Helper script to rebuild image :

` url=`[`http://github.com/TizenTeam/meta-yocto-demos`](http://github.com/TizenTeam/meta-yocto-demos)\
` branch=meta/tizen-distro/tizen_ivi`\
` git clone -b $branch $url`\
` cd meta-yocto-demos && make`

For building for [MinnowMax](MinnowMax "wikilink") image just add this
arg :

` make IMAGE=genericx86-64`

NOTES
-----

This page will be used to also list random resources

How to setup yocto begin a firewall ?

-   <http://www.yoctoproject.org/docs/1.8/ref-manual/ref-manual.html#source-mirrors>

[Category:Yocto](Category:Yocto "wikilink")
[Category:Common](Category:Common "wikilink")
[Category:IVI](Category:IVI "wikilink")
[Category:Development](Category:Development "wikilink")
[Category:Platform](Category:Platform "wikilink")
[Category:Tool](Category:Tool "wikilink")
