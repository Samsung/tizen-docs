Litmus is an automated testing tool for tizen platform on
[ARM](ARM "wikilink") [Devices](Devices "wikilink").

This tool provides python APIs for controlling devices.(Flash binaries
to device/ Power up and down device/ Run commands on device/ Push and
pull files/ Take screenshots) And this also provides test project
manager and test project launcher.

Getting Started
---------------

### Prerequisite

Litmus uses sdb to communicate with device. sdb is not released on
download.tizen.org/tools but you can find it from sdk. Install sdb from
tizen sdk or download binary from below url.

32bit:

    http://download.tizen.org/sdk/tizenstudio/official/binary/sdb_2.3.0_ubuntu-32.zip

64bit:

    http://download.tizen.org/sdk/tizenstudio/official/binary/sdb_2.3.0_ubuntu-64.zip

Unzip this package and copy sdb binary to /usr/bin

### Step1. Install Litmus

Litmus supports ubuntu distro only. (Ubuntu 14.04 and Ubuntu 16.04). If
someone wants to use this tool and APIs on other linux distro, please
contribute sources and packages, dependencies for that distro.

First, open the **/etc/apt/sources.list.d/litmus.list** file in your
favorite editor. If the file doesn\'t exist, create it. And add entries
for your ubuntu system.

For Ubuntu 14.04

    deb http://download.tizen.org/live/Tools/Ubuntu_14.04/ /

For Ubuntu 16.04

    deb http://download.tizen.org/live/Tools/Ubuntu_16.04/ /

Update apt cache.

    sudo apt-get update

And install a package litmus.

    sudo apt-get install litmus

You can also clone source code from github and create a debian package
to use latest version.

First, clone latest source code from github.

    git clone https://github.com/dhs-shine/litmus

Build a deb package with debuild

    cd litmus
    debuild

Install the deb package by using dpkg

    cd ..
    sudo dpkg -i litmus_0.3.4-1_amd64.deb

### Step2. Create a Litmus test project

Litmus project manager helps you to manage your test project with
command line interface. First, list all of Litmus project on your
environment.

    litmus ls

Result:

    =====list of all litmus projects=====

There\'s no test project. Let\'s create a new test project.

    litmus mk <new test project name>

Example:

    $ litmus mk 3.0-mobile-tm1
    Enter the device type (u3/xu3/artik5/artik10/standalone_tm1/standalone_tm2/standalone_tw1/standalone_u3/standalone_xu3/empty): standalone_tm1
    Enter descriptions for this project : my first test project for tm1 device
    $ litmus ls
    =====list of all litmus projects=====
    3.0-mobile-tm1 (my first test project for tm1 device : /home/dhsshin/litmus/3.0-mobile-tm1)

You can see that the following project components exist under the
project path.

    -rwxrwxr-x 1 dhsshin dhsshin    0 Oct  21 14:59 __init__.py
    drwxrwxr-x 2 dhsshin dhsshin 4096 Oct  21 15:05 __pycache__
    -rwxrwxr-x 1 dhsshin dhsshin  162 Oct  21 14:59 conf_mobile.yaml
    -rwxrwxr-x 1 dhsshin dhsshin  263 Oct  21 14:59 conf_tv.yaml
    -rwxrwxr-x 1 dhsshin dhsshin  172 Oct  21 14:59 conf_wearable.yaml
    -rwxrwxr-x 1 dhsshin dhsshin 1507 Oct  21 14:59 tc_mobile.yaml
    -rwxrwxr-x 1 dhsshin dhsshin  723 Oct  21 14:59 tc_tv.yaml
    -rwxrwxr-x 1 dhsshin dhsshin 1519 Oct  21 14:59 tc_wearable.yaml
    -rwxrwxr-x 1 dhsshin dhsshin 1545 Oct  21 14:59 userscript.py

These are config files and python scripts for your testing. If you run
this test project with litmus test launcher then userscript.py is the
entry point of this. Please open it.

userscript.py:

    #!/usr/bin/env python3
    import os
    from litmus.core.util import load_yaml
    from litmus.core.manager import manager
    from litmus.helper.helper import tizen_snapshot_downloader as downloader
    from litmus.helper.tests import add_test_helper


    def main(*args, **kwargs):

        # init manager instance
        mgr = manager(*args, **kwargs)

        # init working directory
        mgr.init_workingdir()

        # get projectinfo
        project_info = load_yaml('conf_mobile.yaml')

        username = project_info['username']
        password = project_info['password']
        binary_urls = project_info['binary_urls']

        # get version from parameter
        # ex) 20160923.3
        try:
            version = kwargs['param'][0]
        except (IndexError, TypeError):
            version = None

        # download binaries from snapshot download server
        filenames = []
        for url in binary_urls:
            filenames.extend(downloader(url=url,
                                        username=username,
                                        password=password,
                                        version=version))

        # get an available device for testing.
        dut = mgr.acquire_dut('standalone_tm1', max_retry_times=180)

        # flash binaries to device.
        dut.flash(filenames)

        # turn on dut.
        dut.on()

        # run helper functions for testing.
        if not os.path.exists('result'):
            os.mkdir('result')

        testcases = load_yaml('tc_mobile.yaml')
        add_test_helper(dut, testcases)
        dut.run_tests()

        # turn off dut.
        dut.off()

        # release a device
        mgr.release_dut(dut)

This is a simple python script and main() is the entry point. You can
find classes and functions under litmus package and these can control
your device connected to your host PC.

This default template just download a latest 3.0 mobile profile binary
for TM1 and acquire an available device from your environment, and flash
the binary to acquired device. And just run testcases from
tc\_mobile.yaml.

conf\_mobile.yaml:

    binary_urls:
        - http://download.tizen.org/snapshots/tizen/mobile/latest/images/target-TM1/mobile-wayland-armv7l-tm1/
    username: <username>
    password: <password>

tc\_mobile.yaml:

    testcases:
      - name: verify_process_is_running
        from: litmus.helper.tests
        result_dir: result
        plan:
          - name: dbus_is_running
            param: dbus
            pattern: .*/usr/bin/dbus-daemon.*
          - name: enlightenment_is_running
            param: enlightenment
            pattern: .*/usr/bin/enlightenment.*
          - name: sensord_is_running
            param: sensord
            pattern: .*/usr/bin/sensord.*
          - name: deviced_is_running
            param: deviced
            pattern: .*/usr/bin/deviced.*
          - name: pulseaudio_is_running
            param: pulseaudio
            pattern: .*/usr/bin/pulseaudio.*
          - name: sdbd_is_running
            param: sdbd
            pattern: .*/usr/sbin/sdbd.*
          - name: msg-server_is_running
            param: msg-server
            pattern: .*/usr/bin/msg-server.*
          - name: connmand_is_running
            param: connmand
            pattern: .*/usr/sbin/connmand.*
          - name: callmgrd_is_running
            param: callmgrd
            pattern: .*/usr/bin/callmgrd.*
          - name: alarm-server_is_running
            param: alarm-server
            pattern: .*/usr/bin/alarm-server.*
          - name: media-server_is_running
            param: media-server
            pattern: .*/usr/bin/media-server.*
      - name: verify_dmesg
        from: litmus.helper.tests
        result_dir: result
        plan:
          - name: panel_is_alive
            param: panel
            pattern: .*panel is dead.*
      - name: verify_wifi_is_working
        from: litmus.helper.tests
        wifi_apname: setup
        wifi_password:
        result_dir: result

### Step3. Run the Litmus test project

Before running this test project, you have to configure topology file.
Default path of topology file is **\~/.litmus/topology**. Please open
it.

    [TM1_001]
    dev_type = standalone_tm1
    serialno = 0000d86100006200

You have to write this ini file as above to create a topology of your
test environment. If you don\'t know serial number of your device then
please use \'sdb devices\' command.

    $ sdb devices
    List of devices attached
    0000d86100006200        device          TM1

After configuring topology, you can run your test project as follow:

    litmus run 3.0-mobile-tm1

This will create a temporary directory as working dir and copy all files
under project path to working dir. main() function will be executed and
temporary working dir will be deleted after testing. If you want to keep
test results in working directory then please use -d option.

    litmus run 3.0-mobile-tm1 -d ~/test_result

\~/test\_result will be the working dir and litmus test launcher does
not delete this after testing.

[Category:Tool](Category:Tool "wikilink")
