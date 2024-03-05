Build Your Own Linux Distro
===========================

-   LFS

<http://www.linuxfromscratch.org/lfs/>

-   Remastersys

<https://www.maketecheasier.com/backup-ubuntu-with-remastersys>

-   Linux Live Kit

<http://www.linux-live.org/>

-   Live-Magic

<apt:live-magic>

-   Revisor

<https://fedoraproject.org/wiki/JeroenVanMeeuwen/Revisor>
<http://pykickstart.readthedocs.io/en/latest/> yum install
system-config-kickstart livecd-creator

-   Instalinux.com

<http://www.instalinux.com/>

-   SUSE Studio

<https://susestudio.com/>

Reference
=========

-   <https://source.tizen.org/documentation/reference/mic-image-creator>
-   <https://source.tizen.org/documentation/developer-guide/getting-started-guide/creating-tizen-images-mic>
-   <https://wiki.tizen.org/wiki/Mic-guide>
-   <https://wiki.tizen.org/wiki/Build_Tizen_in_a_private_OBS#Build_your_image>
-   <https://github.com/01org/mic/releases>
-   <https://www.slideshare.net/again4you/tizen-talk-2016-in-seoul>

MIC file tree
=============

    invain@ubuntu:/work/infra/mic.git$ tree
    .
    ├── AUTHORS
    ├── COPYING
    ├── ChangeLog
    ├── Makefile
    ├── README.rst
    ├── debian
    │   ├── changelog
    │   ├── compat
    │   ├── control
    │   ├── copyright
    │   ├── docs
    │   ├── mic.install
    │   └── rules
    ├── doc
    │   ├── FAQ.rst
    │   ├── KNOWN_ISSUES
    │   ├── RELEASE_NOTES
    │   ├── install.rst
    │   ├── man.rst
    │   └── usage.rst
    ├── etc
    │   ├── bash_completion.d
    │   │   └── mic.sh
    │   ├── mic.conf.in
    │   └── zsh_completion.d
    │       └── _mic
    ├── html
    │   ├── arrowdown.png
    │   ├── arrowright.png
    │   ├── bc_s.png
    │   ├── bdwn.png
    │   ├── closed.png
    │   ├── doc.png
    │   ├── doxygen.css
    │   ├── doxygen.png
    │   ├── dynsections.js
    │   ├── files.html
    │   ├── folderclosed.png
    │   ├── folderopen.png
    │   ├── graph_legend.html
    │   ├── graph_legend.md5
    │   ├── graph_legend.png
    │   ├── index.html
    │   ├── jquery.js
    │   ├── namespacemembers.html
    │   ├── namespacemembers_func.html
    │   ├── namespacemembers_vars.html
    │   ├── namespaces.html
    │   ├── namespacesetup.html
    │   ├── nav_f.png
    │   ├── nav_g.png
    │   ├── nav_h.png
    │   ├── open.png
    │   ├── search
    │   │   ├── all_0.html
    │   │   ├── all_0.js
    │   │   ├── all_1.html
    │   │   ├── all_1.js
    │   │   ├── all_2.html
    │   │   ├── all_2.js
    │   │   ├── all_3.html
    │   │   ├── all_3.js
    │   │   ├── all_4.html
    │   │   ├── all_4.js
    │   │   ├── all_5.html
    │   │   ├── all_5.js
    │   │   ├── all_6.html
    │   │   ├── all_6.js
    │   │   ├── all_7.html
    │   │   ├── all_7.js
    │   │   ├── all_8.html
    │   │   ├── all_8.js
    │   │   ├── all_9.html
    │   │   ├── all_9.js
    │   │   ├── all_a.html
    │   │   ├── all_a.js
    │   │   ├── all_b.html
    │   │   ├── all_b.js
    │   │   ├── close.png
    │   │   ├── files_0.html
    │   │   ├── files_0.js
    │   │   ├── functions_0.html
    │   │   ├── functions_0.js
    │   │   ├── mag_sel.png
    │   │   ├── namespaces_0.html
    │   │   ├── namespaces_0.js
    │   │   ├── nomatches.html
    │   │   ├── search.css
    │   │   ├── search.js
    │   │   ├── search_l.png
    │   │   ├── search_m.png
    │   │   ├── search_r.png
    │   │   ├── searchdata.js
    │   │   ├── variables_0.html
    │   │   ├── variables_0.js
    │   │   ├── variables_1.html
    │   │   ├── variables_1.js
    │   │   ├── variables_2.html
    │   │   ├── variables_2.js
    │   │   ├── variables_3.html
    │   │   ├── variables_3.js
    │   │   ├── variables_4.html
    │   │   ├── variables_4.js
    │   │   ├── variables_5.html
    │   │   ├── variables_5.js
    │   │   ├── variables_6.html
    │   │   ├── variables_6.js
    │   │   ├── variables_7.html
    │   │   ├── variables_7.js
    │   │   ├── variables_8.html
    │   │   ├── variables_8.js
    │   │   ├── variables_9.html
    │   │   ├── variables_9.js
    │   │   ├── variables_a.html
    │   │   ├── variables_a.js
    │   │   ├── variables_b.html
    │   │   └── variables_b.js
    │   ├── setup_8py.html
    │   ├── splitbar.png
    │   ├── sync_off.png
    │   ├── sync_on.png
    │   ├── tab_a.png
    │   ├── tab_b.png
    │   ├── tab_h.png
    │   ├── tab_s.png
    │   └── tabs.css
    ├── latex
    │   ├── Makefile
    │   ├── doxygen.sty
    │   ├── files.tex
    │   ├── namespaces.tex
    │   ├── namespacesetup.tex
    │   ├── refman.tex
    │   └── setup_8py.tex
    ├── mic
    │   ├── 3rdparty
    │   │   └── pykickstart
    │   │       ├── __init__.py
    │   │       ├── __init__.pyc
    │   │       ├── base.py
    │   │       ├── base.pyc
    │   │       ├── commands
    │   │       │   ├── __init__.py
    │   │       │   ├── __init__.pyc
    │   │       │   ├── authconfig.py
    │   │       │   ├── authconfig.pyc
    │   │       │   ├── autopart.py
    │   │       │   ├── autopart.pyc
    │   │       │   ├── autostep.py
    │   │       │   ├── autostep.pyc
    │   │       │   ├── bootloader.py
    │   │       │   ├── bootloader.pyc
    │   │       │   ├── clearpart.py
    │   │       │   ├── clearpart.pyc
    │   │       │   ├── device.py
    │   │       │   ├── device.pyc
    │   │       │   ├── deviceprobe.py
    │   │       │   ├── deviceprobe.pyc
    │   │       │   ├── displaymode.py
    │   │       │   ├── displaymode.pyc
    │   │       │   ├── dmraid.py
    │   │       │   ├── dmraid.pyc
    │   │       │   ├── driverdisk.py
    │   │       │   ├── driverdisk.pyc
    │   │       │   ├── fcoe.py
    │   │       │   ├── fcoe.pyc
    │   │       │   ├── firewall.py
    │   │       │   ├── firewall.pyc
    │   │       │   ├── firstboot.py
    │   │       │   ├── firstboot.pyc
    │   │       │   ├── group.py
    │   │       │   ├── group.pyc
    │   │       │   ├── ignoredisk.py
    │   │       │   ├── ignoredisk.pyc
    │   │       │   ├── interactive.py
    │   │       │   ├── interactive.pyc
    │   │       │   ├── iscsi.py
    │   │       │   ├── iscsi.pyc
    │   │       │   ├── iscsiname.py
    │   │       │   ├── iscsiname.pyc
    │   │       │   ├── key.py
    │   │       │   ├── key.pyc
    │   │       │   ├── keyboard.py
    │   │       │   ├── keyboard.pyc
    │   │       │   ├── lang.py
    │   │       │   ├── lang.pyc
    │   │       │   ├── langsupport.py
    │   │       │   ├── langsupport.pyc
    │   │       │   ├── lilocheck.py
    │   │       │   ├── lilocheck.pyc
    │   │       │   ├── logging.py
    │   │       │   ├── logging.pyc
    │   │       │   ├── logvol.py
    │   │       │   ├── logvol.pyc
    │   │       │   ├── mediacheck.py
    │   │       │   ├── mediacheck.pyc
    │   │       │   ├── method.py
    │   │       │   ├── method.pyc
    │   │       │   ├── monitor.py
    │   │       │   ├── monitor.pyc
    │   │       │   ├── mouse.py
    │   │       │   ├── mouse.pyc
    │   │       │   ├── multipath.py
    │   │       │   ├── multipath.pyc
    │   │       │   ├── network.py
    │   │       │   ├── network.pyc
    │   │       │   ├── partition.py
    │   │       │   ├── partition.pyc
    │   │       │   ├── raid.py
    │   │       │   ├── raid.pyc
    │   │       │   ├── reboot.py
    │   │       │   ├── reboot.pyc
    │   │       │   ├── repo.py
    │   │       │   ├── repo.pyc
    │   │       │   ├── rescue.py
    │   │       │   ├── rescue.pyc
    │   │       │   ├── rootpw.py
    │   │       │   ├── rootpw.pyc
    │   │       │   ├── selinux.py
    │   │       │   ├── selinux.pyc
    │   │       │   ├── services.py
    │   │       │   ├── services.pyc
    │   │       │   ├── skipx.py
    │   │       │   ├── skipx.pyc
    │   │       │   ├── sshpw.py
    │   │       │   ├── sshpw.pyc
    │   │       │   ├── timezone.py
    │   │       │   ├── timezone.pyc
    │   │       │   ├── updates.py
    │   │       │   ├── updates.pyc
    │   │       │   ├── upgrade.py
    │   │       │   ├── upgrade.pyc
    │   │       │   ├── user.py
    │   │       │   ├── user.pyc
    │   │       │   ├── vnc.py
    │   │       │   ├── vnc.pyc
    │   │       │   ├── volgroup.py
    │   │       │   ├── volgroup.pyc
    │   │       │   ├── xconfig.py
    │   │       │   ├── xconfig.pyc
    │   │       │   ├── zerombr.py
    │   │       │   ├── zerombr.pyc
    │   │       │   ├── zfcp.py
    │   │       │   └── zfcp.pyc
    │   │       ├── constants.py
    │   │       ├── constants.pyc
    │   │       ├── errors.py
    │   │       ├── errors.pyc
    │   │       ├── handlers
    │   │       │   ├── __init__.py
    │   │       │   ├── __init__.pyc
    │   │       │   ├── control.py
    │   │       │   ├── control.pyc
    │   │       │   ├── f10.py
    │   │       │   ├── f11.py
    │   │       │   ├── f12.py
    │   │       │   ├── f13.py
    │   │       │   ├── f14.py
    │   │       │   ├── f15.py
    │   │       │   ├── f16.py
    │   │       │   ├── f7.py
    │   │       │   ├── f8.py
    │   │       │   ├── f9.py
    │   │       │   ├── fc3.py
    │   │       │   ├── fc4.py
    │   │       │   ├── fc5.py
    │   │       │   ├── fc6.py
    │   │       │   ├── rhel3.py
    │   │       │   ├── rhel4.py
    │   │       │   ├── rhel5.py
    │   │       │   └── rhel6.py
    │   │       ├── ko.py
    │   │       ├── ko.pyc
    │   │       ├── options.py
    │   │       ├── options.pyc
    │   │       ├── parser.py
    │   │       ├── parser.pyc
    │   │       ├── sections.py
    │   │       ├── sections.pyc
    │   │       ├── urlgrabber
    │   │       │   ├── __init__.py
    │   │       │   ├── __init__.pyc
    │   │       │   ├── byterange.py
    │   │       │   ├── byterange.pyc
    │   │       │   ├── grabber.py
    │   │       │   ├── grabber.pyc
    │   │       │   ├── keepalive.py
    │   │       │   ├── keepalive.pyc
    │   │       │   ├── mirror.py
    │   │       │   ├── progress.py
    │   │       │   ├── sslfactory.py
    │   │       │   └── sslfactory.pyc
    │   │       ├── version.py
    │   │       └── version.pyc
    │   ├── __init__.py
    │   ├── __init__.pyc
    │   ├── archive.py
    │   ├── bootstrap.py
    │   ├── chroot.py
    │   ├── cmd_chroot.py
    │   ├── cmd_create.py
    │   ├── conf.py
    │   ├── conf.pyc
    │   ├── helpformat.py
    │   ├── imager
    │   │   ├── __init__.py
    │   │   ├── baseimager.py
    │   │   ├── fs.py
    │   │   ├── loop.py
    │   │   └── raw.py
    │   ├── kickstart
    │   │   ├── __init__.py
    │   │   ├── __init__.pyc
    │   │   └── custom_commands
    │   │       ├── __init__.py
    │   │       ├── __init__.pyc
    │   │       ├── desktop.py
    │   │       ├── desktop.pyc
    │   │       ├── installerfw.py
    │   │       ├── installerfw.pyc
    │   │       ├── micboot.py
    │   │       ├── micboot.pyc
    │   │       ├── micrepo.py
    │   │       ├── micrepo.pyc
    │   │       ├── partition.py
    │   │       └── partition.pyc
    │   ├── msger.py
    │   ├── msger.pyc
    │   ├── plugin.py
    │   ├── pluginbase.py
    │   ├── rt_util.py
    │   └── utils
    │       ├── __init__.py
    │       ├── __init__.pyc
    │       ├── errors.py
    │       ├── errors.pyc
    │       ├── fs_related.py
    │       ├── fs_related.pyc
    │       ├── gpt_parser.py
    │       ├── gpt_parser.pyc
    │       ├── grabber.py
    │       ├── grabber.pyc
    │       ├── lock.py
    │       ├── lock.pyc
    │       ├── misc.py
    │       ├── misc.pyc
    │       ├── partitionedfs.py
    │       ├── proxy.py
    │       ├── proxy.pyc
    │       ├── rpmmisc.py
    │       ├── rpmmisc.pyc
    │       ├── runner.py
    │       ├── runner.pyc
    │       ├── safeurl.py
    │       └── safeurl.pyc
    ├── packaging
    │   ├── mic.changes
    │   ├── mic.manifest
    │   └── mic.spec
    ├── plugins
    │   ├── backend
    │   │   ├── yumpkgmgr.py
    │   │   └── zypppkgmgr.py
    │   ├── hook
    │   │   └── empty_hook.py
    │   └── imager
    │       ├── fs_plugin.py
    │       ├── loop_plugin.py
    │       ├── qcow_plugin.py
    │       └── raw_plugin.py
    ├── setup.py
    ├── tests
    │   ├── baseimgr_fixtures
    │   │   ├── i586
    │   │   │   ├── A-0.1-1.i586.rpm
    │   │   │   ├── ABC-0.1-1.i586.rpm
    │   │   │   ├── B-0.1-1.i586.rpm
    │   │   │   ├── D-0.1-1.i586.rpm
    │   │   │   ├── E-0.1-1.i586.rpm
    │   │   │   └── G-0.1-1.i586.rpm
    │   │   ├── i686
    │   │   │   └── C-0.2-1.i686.rpm
    │   │   ├── localpkgs
    │   │   │   ├── H-0.2-1.armv7hl.rpm
    │   │   │   └── H-0.2-1.i586.rpm
    │   │   ├── noarch
    │   │   │   ├── F-0.1-1.noarch.rpm
    │   │   │   └── H-0.1-1.noarch.rpm
    │   │   ├── repodata
    │   │   │   ├── 4bb63d1039a6f0d3fd1e7035acff76e7015963cabab2751263c7a20f4ff1c668-group.xml.gz
    │   │   │   ├── ea95ecaccf9abc214715b1724188a3ecfcae1eb9b7855127938b39de83fbc303-patterns.xml.gz
    │   │   │   ├── filelists.xml.gz
    │   │   │   ├── other.xml.gz
    │   │   │   ├── primary.xml.gz
    │   │   │   └── repomd.xml
    │   │   └── test.ks
    │   ├── chroot_fixtures
    │   │   └── minchroot.tar.gz
    │   ├── configmgr_fixtures
    │   │   ├── mic.conf
    │   │   ├── packages
    │   │   │   ├── repodata
    │   │   │   │   ├── filelists.sqlite.bz2
    │   │   │   │   ├── filelists.xml.gz
    │   │   │   │   ├── other.sqlite.bz2
    │   │   │   │   ├── other.xml.gz
    │   │   │   │   ├── primary.sqlite.bz2
    │   │   │   │   ├── primary.xml.gz
    │   │   │   │   └── repomd.xml
    │   │   │   └── test-0-1.i686.rpm
    │   │   └── test.ks
    │   ├── pluginmgr_fixtures
    │   │   ├── backend
    │   │   │   ├── yumtest.py
    │   │   │   └── zypptest.py
    │   │   └── imager
    │   │       ├── fs_test.py
    │   │       └── loop_test.py
    │   ├── suite.py
    │   ├── test_archive.py
    │   ├── test_baseimager.py
    │   ├── test_chroot.py
    │   ├── test_configmgr.py
    │   ├── test_pluginmgr.py
    │   ├── test_proxy.py
    │   └── test_runner.py
    └── tools
        └── mic

    38 directories, 390 files
    invain@ubuntu:/work/infra/mic.git$ 

Example of MIC configuration file
=================================


    # -*-mic2-options-*- -f loop --pack-to=@NAME@.tar.gz -*-mic2-options-*-

    # 
    # Do not Edit! Generated by:
    # kickstarter.py
    # 

    lang en_US.UTF-8
    keyboard us
    timezone --utc Asia/Seoul
    part / --size=2000 --ondisk mmcblk0p --fstype=ext4 --label=rootfs --extoptions="-J size=16"
    part /opt/ --size=1000 --ondisk mmcblk0p --fstype=ext4 --label=system-data --extoptions="-m 0"
    part /boot/kernel/mod_tizen_tm1/lib/modules --size=12 --ondisk mmcblk0p --fstype=ext4 --label=modules
    rootpw tizen 
    xconfig --startxonboot
    bootloader  --timeout=3  --append="rw vga=current splash rootwait rootfstype=ext4 plymouth.enable=0"   --ptable=gpt --menus="install:Wipe and Install:systemd.unit=system-installer.service:test"

    desktop --autologinuser=root  
    user --name root  --groups audio,video --password 'tizen'


    repo --name=mobile-target-TM1 --baseurl=http://download.tizen.org/snapshots/tizen/mobile/tizen-mobile_20170323.3/repos/target-TM1/packages/ --ssl_verify=no
    repo --name=base_arm --baseurl=http://download.tizen.org/snapshots/tizen/base/latest/repos/arm/packages/ --ssl_verify=no

    %packages

    # @ Mobile Headless
    bash
    coreutils
    dbus
    dlogutil
    e2fsprogs
    filesystem
    fsck-msdos
    grep
    gzip
    kmod
    kmod-compat
    libdlog
    net-tools
    newfs-msdos
    pam
    pam-modules-extra
    procps
    psmisc
    rpm
    rpm-security-plugin
    sdbd
    setup
    shadow-utils-adm
    system-plugin-headless
    systemd
    tar
    tizen-release
    unzip
    util-linux
    wpa_supplicant
    xz
    zip
    # @ Mobile Headless Adaptation TM1
    linux-3.10-sc7730_tizen_tm1
    model-config-tm1
    system-plugin-spreadtrum
    # Others




    %end


    %attachment
    /boot/kernel/dzImage
    %end

    %post
    #!/bin/sh
    echo "#################### generic-base.post ####################"

    test ! -e /opt/var && mkdir -p /opt/var
    test -d /var && cp -arf /var/* /opt/var/
    rm -rf /var
    ln -snf opt/var /var

    test ! -e /opt/usr/home && mkdir -p /opt/usr/home
    test -d /home && cp -arf /home/* /opt/usr/home/
    rm -rf /home
    ln -snf opt/usr/home /home

    build_ts=$(date -u +%s)
    build_date=$(date -u --date @$build_ts +%Y%m%d_%H%M%S)
    build_time=$(date -u --date @$build_ts +%H:%M:%S)

    sed -ri \
        -e 's|@BUILD_ID[@]|tizen-mobile_20170323.3|g' \
        -e "s|@BUILD_DATE[@]|$build_date|g" \
        -e "s|@BUILD_TIME[@]|$build_time|g" \
        -e "s|@BUILD_TS[@]|$build_ts|g" \
        /etc/tizen-build.conf

    # setup systemd default target for user session
    cat <<'EOF' >>/usr/lib/systemd/user/default.target
    [Unit]
    Description=User session default target
    EOF
    mkdir -p /usr/lib/systemd/user/default.target.wants

    # sdx: fix smack labels on /var/log
    chsmack -a '*' /var/log

    # create appfw dirs inside homes
    function generic_base_user_exists() {
        user=$1
        getent passwd | grep -q ^${user}:
    }

    function generic_base_user_home() {
        user=$1
        getent passwd | grep ^${user}: | cut -f6 -d':'
    }

    function generic_base_fix_user_homedir() {
        user=$1
        generic_base_user_exists $user || return 1

        homedir=$(generic_base_user_home $user)
        mkdir -p $homedir/apps_rw
        for appdir in desktop manifest dbspace; do
            mkdir -p $homedir/.applications/$appdir
        done
        find $homedir -type d -exec chsmack -a User {} \;
        chown -R $user:users $homedir
        return 0
    }

    # fix TC-320 for SDK
    . /etc/tizen-build.conf
    [ "${TZ_BUILD_WITH_EMULATOR}" == "1" ] && generic_base_fix_user_homedir developer

    # Add info.ini for system-info CAPI (TC-2047)
    /etc/make_info_file.sh

    #!/bin/sh
    echo "############### mobile-base.post ################"

    ######### multiuser mode: create additional users and fix their homedirs

    if ! generic_base_user_exists owner; then
        gum-utils --offline --add-user --username=owner --usertype=admin --usecret=tizen
    fi


    #!/bin/sh
    echo "#################### generic-console-tools.post ####################"

    # customize bash prompt
    cat >/etc/profile.d/bash_prompt_custom.sh <<'EOF'
    if [ "$PS1" ]; then

        function proml {
            # set a fancy prompt (overwrite the one in /etc/profile)
            local default="\[\e[0m\]"
            local usercol='\[\e[1;34m\]' # blue
            local hostcol='\[\e[1;32m\]' # green
            local pathcol='\[\e[1;33m\]' # yellow
            local gitcol='\[\e[1;31m\]' # light red
            local termcmd=''
            local _p="$";

            if [ "`id -u`" -eq 0 ]; then
                usercol='\[\e[1;31m\]'
                _p="#"
            fi

            PS1="${usercol}\u${default}@${hostcol}\h${default}:${pathcol}\w${default}${gitcol}${default}${_p} ${termcmd}"
        }

        proml

        function rcd () {
          [ "${1:0:1}" == "/" ] && { cd $1; } || { cd $(pwd -P)/$1; }
       }

        alias ll="ls -lZ"
        alias lr="ls -ltrZ"
        alias la="ls -alZ"

        function get_manifest () {
            rpm -qa --queryformat="%{name} %{Version} %{Release} %{VCS}\n" | sort
        }
    fi
    EOF


    #!/bin/sh
    echo "############### mobile-packaging.post ################"

    # generate repo files for zypper
    function genrepo() {
        local url=$1
        local reponame=$2
        local filename=${3:-$2}
        local enabled=${4:-0}

        local prefix=${TZ_BUILD_VENDOR}-${TZ_BUILD_PROFILE}-${TZ_BUILD_REPO}

        # remove double slashes if any
        url=$(sed -e  's|/\+|/|g' -e 's|:/|://|' <<<$url)

        cat >> /etc/zypp/repos.d/$prefix-${filename}.repo << EOF
    [$prefix-${reponame}]
    name=$prefix-${reponame}
    enabled=$enabled
    autorefresh=0
    baseurl=${url}?ssl_verify=no
    type=rpm-md
    gpgcheck=0
     
    EOF
    }

    # source /etc/tizen-build.conf to get more infos about project, repos etc.
    . /etc/tizen-build.conf 

    # adjust build_id if this scripts executes before the replacement in /etc/tizen-build.conf
    TZ_BUILD_ID=$(echo $TZ_BUILD_ID | sed 's|@BUILD_ID[@]|tizen-mobile_20170323.3|')

    # snapshot repo
    genrepo ${TZ_BUILD_SNAPSHOT_URL}/${TZ_BUILD_ID}/repos/${TZ_BUILD_REPO}/packages snapshot snapshot 1
    genrepo ${TZ_BUILD_SNAPSHOT_URL}/${TZ_BUILD_ID}/repos/${TZ_BUILD_REPO}/debug snapshot-debug snapshot 1

    # latest repo
    genrepo ${TZ_BUILD_SNAPSHOT_URL}/latest/repos/${TZ_BUILD_REPO}/packages update update 0
    genrepo ${TZ_BUILD_SNAPSHOT_URL}/latest/repos/${TZ_BUILD_REPO}/debug update-debug update 0

    # daily repo
    genrepo ${TZ_BUILD_DAILY_URL}/latest/repos/${TZ_BUILD_REPO}/packages daily daily 0
    genrepo ${TZ_BUILD_DAILY_URL}/latest/repos/${TZ_BUILD_REPO}/debug daily-debug daily 0

    # weekly repo
    genrepo ${TZ_BUILD_WEEKLY_URL}/latest/repos/${TZ_BUILD_REPO}/packages weekly weekly 0
    genrepo ${TZ_BUILD_WEEKLY_URL}/latest/repos/${TZ_BUILD_REPO}/debug weekly-debug weekly 0


    #!/bin/sh
    echo "#################### generic-adaptation.post ####################"

    # fix TIVI-2291
    sed -ri "s/(^blacklist i8042.*$)/#fix from base-general.post \1/" /etc/modprobe.d/blacklist.conf


    #!/bin/sh
    echo "############### mobile-adaptation.post ################"


    #!/bin/sh
    echo "############### mobile-middleware.post ################"


    #!/bin/sh
    echo "#################### generic-multimedia.post ####################"


    #!/bin/sh
    echo "#################### generic-desktop-applications.post ####################"

    # depends on generic-base functions
    function generic_desktop_applications_fix_userhome() {
        user=$1

        generic_base_user_exists $user || return 1
        homedir=$(generic_base_user_home $user)

        echo "Fix app_info.db of $user"
        chown -R $user:users $homedir/.applications/dbspace/
    }

    # fix TC-320 for SDK
    . /etc/tizen-build.conf
    [ "${TZ_BUILD_WITH_EMULATOR}" == "1" ] && generic_desktop_applications_fix_userhome developer


    #!/bin/sh
    echo "#################### generic-crosswalk.post ####################"


    #!/bin/sh
    echo "############### mobile-web-framework.post ################"

    # start wrt widgets preinstall
    prepare_widgets.sh


    #!/bin/sh
    echo "#################### mobile-bluetooth.post ####################"


    #!/bin/sh
    echo "############### mobile-user.post ################"

    #for user in alice bob carol guest; do
    # if ! generic_base_user_exists $user; then
    #  gum-utils --offline --add-user --username="$user" --usertype=normal --usecret=tizen
    # fi
    #done


    #!/bin/sh
    echo "############### mobile-license.post ################"

    LICENSE_DIR=/usr/share/licenses
    LICENSE_FILE=/usr/share/license.html
    MD5_TEMP_FILE=/usr/share/temp_license_md5

    if [[ -f $LICENSE_FILE ]]; then
        rm -f $LICENSE_FILE
    fi

    if [[ -f $MD5_TEMP_FILE ]]; then
        rm -f $MD5_TEMP_FILE
    fi


    cd $LICENSE_DIR
    LICENSE_LIST=`ls */*`

    for INPUT in $LICENSE_LIST; do
        if [[ -f $INPUT ]]; then
            PKG_NAME=`echo $INPUT|cut -d'/' -f1`
            echo `md5sum $INPUT` $PKG_NAME >> $MD5_TEMP_FILE
        fi
    done

    MD5_LIST=`cat $MD5_TEMP_FILE|awk '{print $1}'|sort -u`

    echo "<html>" >> $LICENSE_FILE
    echo "<head>" >> $LICENSE_FILE
    echo "<meta name=\"viewport\" content=\"initial-scale=1.0\">" >> $LICENSE_FILE
    echo "</head>" >> $LICENSE_FILE
    echo "<body>" >> $LICENSE_FILE
    echo "<xmp>" >> $LICENSE_FILE

    for INPUT in $MD5_LIST; do
        PKG_LIST=`cat $MD5_TEMP_FILE|grep $INPUT|awk '{print $3}'`
        FILE_LIST=`cat $MD5_TEMP_FILE|grep $INPUT|awk '{print $2}'`
        PKG_FILE=`echo $FILE_LIST |awk '{print $1}'`

        echo "$PKG_LIST :" >> $LICENSE_FILE
        cat $PKG_FILE >> $LICENSE_FILE
        echo  >> $LICENSE_FILE
        echo  >> $LICENSE_FILE
        echo  >> $LICENSE_FILE
    done

    echo "</xmp>" >> $LICENSE_FILE
    echo "</body>" >> $LICENSE_FILE
    echo "</html>" >> $LICENSE_FILE

    rm -rf $LICENSE_DIR/* $MD5_TEMP_FILE

    #!/bin/sh
    echo "#################### generic-security.post ####################"

    if [ -e /usr/share/security-config/set_capability ]; then
        echo 'Give capabilities to daemons via set_capability from security-config package'
        /usr/share/security-config/set_capability
    fi

    #!/bin/sh
    echo "#################### mobile-adaptation-tm1.post ####################"

    # remove exported dzImage and dzImage-recovery
    rm -f /boot/kernel/dzImage
    rm -f /boot/kernel/dzImage-recovery

    # remove manuals, docs and headers
    rm -rf /usr/include
    rm -rf /usr/share/man
    rm -rf /usr/share/doc



    %end

    %post --nochroot
    # buildname.nochroot 
    if [ -n "$IMG_NAME" ]; then
        echo "BUILD_ID=$IMG_NAME" >> $INSTALL_ROOT/etc/tizen-release
        echo "BUILD_ID=$IMG_NAME" >> $INSTALL_ROOT/etc/os-release
    fi


    %end

How to create your own platform image for yourself
==================================================

    ./run.sh 
    #!/bin/bash
    wget http://download.tizen.org/snapshots/tizen/unified/latest/builddata/images/standard/image-configurations/mobile-headless-tm1.ks
    sudo python -m cProfile -o profile8.pstats  /usr/bin/mic create loop mobile-headless-tm1.ks  -A armv7l -o ./mic-output/mobile-wayland-armv7l-tm1-1 --pack-to=mobile-wayland-armv7l-tm1-1.tar.gz
    tree ./mic-output/ 

How to update a package via network with dnf
============================================

**Coming Soon. !!!**

     
    $ sudo cp /usr/bin/qemu-arm-static /home/invain/tizen-rootfs/usr/bin/ 
    $ sudo mount -t proc /proc                   /home/invain/tizen-rootfs/proc
    $ sudo mount -o bind /dev/                  /home/invain/tizen-rootfs/dev
    $ sudo mount -o bind /dev/pts             /home/invain/tizen-rootfs/pts
    $ sudo mount -t tmpfs shm                  /home/invain/tizen-rootfs/run/shm
    $ sudo mount -o bind /sys                   /home/invain/tizen-rootfs/sys
    $ sudo chroot /home/invain/tizen-rootfs/  (qemu-arm-static) dnf -y install strace

Analysis
========

How to generate callgraph from \*.py file
-----------------------------------------

    $ sudo apt install graphviz gthumb
    $ sudo pip install gprof2dot
    $ python -m cProfile -o profile.pstats  ./mic/utils/partitionedfs.py
    $ gprof2dot -f pstats profile.pstats | dot -Tsvg -o ./mic/utils/partitionedfs.svg
    $ gthumb  ./mic/utils/partitionedfs.png

Example: ./mic/utils/partitionedfs.svg ![FBS (Skeleton)
Screenshot](Partitionedfs.png "fig:FBS (Skeleton) Screenshot"){width="500"}

[Category:Tool](Category:Tool "wikilink")
