Unfortunately, the Tizen
tools(http://download.tizen.org/tools/latest-release) are only supported
until ubuntu 14.10. When you try to build your package with gbs build on
ubuntu 15.04/15.10, you\'ve got below error message.

    Traceback (most recent call last):
      File "/usr/bin/gbs", line 30, in <module>
        from gitbuildsys import cmd_build
      File "/usr/lib/pymodules/python2.7/gitbuildsys/cmd_build.py", line 33, in <module>
        from gitbuildsys.cmd_export import get_packaging_dir, config_is_true
      File "/usr/lib/pymodules/python2.7/gitbuildsys/cmd_export.py", line 34, in <module>
        from gbp.scripts.buildpackage_rpm import main as gbp_build
    ImportError: No module named buildpackage_rpm

It seems that the git-buildpackage of the ubuntu 15.04 is newer version
of the tizen\'s one. Thus, the gbp of the tizen will be not installed.
It already discussed in tizen mailing list\[1\], but source.tizen.org
doesn\'t provide the guide. Like rafal\'s guide\[1\], to address this
conflict, we should raise the tizen repository up than the ubuntu
repository.

    sudo sh -c 'echo "Package: *\nPin: origin download.tizen.org\nPin-Priority: 1001" > /etc/apt/preferences.d/tizen'
    sudo apt-get update
    sudo apt-get dist-upgrade

When you\'ve got below error,

    Errors were encountered while processing:
     /var/cache/apt/archives/git-buildpackage-common_0.6.15-tizen20140828_all.deb
    E: Sub-process /usr/bin/dpkg returned an error code (1)

Just try below:

    sudo apt-get install -f

-   Trouble shooting

When you try to build for arm/arm64 architecture, it will be failed due
to cpio error.\[2\] You\'ll need to apply openSUSE patch\[3\] into the
init\_buildsystem script.

    sed -i "/CPIO=\"cpio --extract/ a \\\tcpio --help 2>\/dev\/null | grep -q -e --extract-over-symlinks && CPIO=\"\$CPIO --extract-over-symlinks\"" /usr/lib/build/init_buildsystem

\[1\]:<https://lists.tizen.org/pipermail/dev/2015-April/006280.html>\
\[2\]:<https://bugs.tizen.org/jira/browse/DEVT-241>\
\[3\]:<https://github.com/openSUSE/obs-build/pull/153/commits/4627ac0f1523f8567a7effcdbcf4571ec4bc30be>

[Category:Tool](Category:Tool "wikilink")
