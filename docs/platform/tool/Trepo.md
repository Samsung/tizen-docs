This is a git-repo wrapper to manage tizen platform source codes on your
host more easily.

<http://download.tizen.org/snapshots/tizen/unified/latest/builddata/manifest/>
provides you repo manifest xmls on website, but if you want to clone
source codes with git-repo tools and that manifest then the xml file has
to be located in git repository. (\'repo init\' requires git uri with -u
option.)

This wrapper will generate temporary git automatically and update
manifest.xml. You just need to pass a few arguments (tizen snapshot
version, regex for filtering projects, etc) then trepo tool initialize
proper repo workspace.

How to build and install
------------------------

Build sources with debuild.

`   sudo apt-get install devscripts debhelper python3-setuptools python3-yaml python3-requests python3-bs4`\
`   git clone `[`https://github.com/dhs-shine/trepo`](https://github.com/dhs-shine/trepo)\
`   cd trepo`\
`   debuild`

Install dependencies and trepo deb package with dpkg.

`   cd ..`\
`   sudo dpkg -i trepo_0.1_all.deb`

How to install trepo from launchpad ppa (Recommend)
---------------------------------------------------

`   sudo add-apt-repository ppa:tizen.org/pdk`\
`   sudo apt-get update`\
`   sudo apt-get install trepo`

How to use
----------

### Get a list of tizen snapshots

You can get a list of available snapshots with \'snapshots\' subcommand.

`   trepo snapshots`

Output:

`   20170524.4`\
`   20170524.3`\
`   20170524.2`\
`   20170524.1`\
`   20170523.3`\
`   20170523.2`\
`   20170523.1`\
`   20170522.2`\
`   20170522.1`\
`   20170520.1`\
`   ...`

### Initialize trepo workspace

Let\'s initialize trepo workspace on new directory with \'init\'
subcommand.

`   mkdir test`\
`   cd test`\
`   trepo init`

You can get trepo workspace information with \'info\' subcommand.

`   trepo info -l`

Output:

`   tizen repo snapshot version: tizen-unified_20170524.4`\
`   tizen repo target type: standard`\
`   tizen repo project names (982 projects):`\
`     apps/native/bluetooth-share-ui`\
`     apps/native/boot-animation`\
`     apps/native/menu-screen`\
`     apps/native/starter`\
`     apps/native/thing-toggler`\
`     apps/native/ug-bluetooth-efl`\
`     apps/native/ug-mobile-ap`\
`     apps/native/ug-nfc-efl`\
`     apps/native/ug-wifi-direct`\
`     apps/native/ug-wifi-efl`\
`     apps/native/volume-app`\
`     apps/web/download-manager`\
`     platform/adaptation/ap_samsung/libexynos-common`\
`   ...`

Example) You can reinitialize your trepo workspace whenever you want.
Let\'s reinitialize trepo workspace based on 20170524.1, includes
\'kernel\' string in project name but do not include \'u-boot\' string.

`   trepo init -s 20170524.1 -r 'kernel' -i 'u-boot'`\
`   trepo info -l`

Outputs:

`   tizen repo snapshot version: tizen-unified_20170524.1`\
`   tizen repo target type: standard`\
`   tizen repo project names (8 projects):`\
`     platform/kernel/linux-exynos`\
`     platform/kernel/linux-rpi3`\
`     profile/common/kernel-common`\
`     profile/common/platform/kernel/linux-3.10-artik`\
`     profile/common/platform/kernel/linux-artik7`\
`     profile/mobile/platform/kernel/linux-3.10-sc7730`\
`     profile/wearable/platform/kernel/linux-3.18-exynos7270`\
`     profile/wearable/platform/kernel/linux-3.4-exynos3250`

You can also initialize your trepo workspace with trepo yaml file.

Exmple) trepo\_test.yaml

`   snapshot_version: latest`\
`   project_names:`\
`     - platform/core/api/alarm`\
`     - platform/core/api/app-manager`\
`     - platform/core/api/application`\
`     - platform/core/api/asp`\
`     - platform/core/api/audio-io`\
`     - platform/core/api/base-utils`\
`     - platform/core/api/bluetooth`\
`     - platform/core/api/camera`\
`     - platform/core/api/common`\
`     - platform/core/api/connection`\
`     - platform/core/api/context`\
`     - platform/core/api/cordova-plugins`\
`     - platform/core/api/device`\
`     - platform/core/api/efl-util`

Initialize trepo workspace with this file

`   trepo init -f trepo_test.yaml`\
`   trepo info -l`

Output:

`   tizen repo snapshot version: tizen-unified_20170524.4`\
`   tizen repo target type: standard`\
`   tizen repo project names (14 projects):`\
`     platform/core/api/alarm`\
`     platform/core/api/app-manager`\
`     platform/core/api/application`\
`     platform/core/api/asp`\
`     platform/core/api/audio-io`\
`     platform/core/api/base-utils`\
`     platform/core/api/bluetooth`\
`     platform/core/api/camera`\
`     platform/core/api/common`\
`     platform/core/api/connection`\
`     platform/core/api/context`\
`     platform/core/api/cordova-plugins`\
`     platform/core/api/device`\
`     platform/core/api/efl-util`

### Sync source codes

Trepo workspace was initialized but source codes are not cloned. Let\'s
sync source codes with \'sync\' subcommand

`     trepo sync -f -j 8`

Output:

`   Fetching project platform/core/api/alarm`\
`   Fetching project platform/core/api/audio-io`\
`   Fetching project platform/core/api/context`\
`   Fetching project platform/core/api/efl-util`\
`   Fetching project platform/core/api/app-manager`\
`   Fetching project platform/core/api/base-utils`\
`   Fetching project platform/core/api/connection`\
`   Fetching project platform/core/api/asp`\
`   remote: Counting objects: 84, done`\
`   remote: Counting objects: 45, done`\
`   remote: Finding sources: 100% (25/25)`\
`   remote: Finding sources: 100% (84/84)`\
`   ....`\
`    * [new tag]         submit/tizen_wearable/20160325.075408 -> submit/tizen_wearable/20160325.075408`\
`    * [new tag]         submit/tizen_wearable/20160328.061957 -> submit/tizen_wearable/20160328.061957`\
`    * [new tag]         tizen_3.0.2014.q3_common_release -> tizen_3.0.2014.q3_common_release`\
`    * [new tag]         tizen_3.0.m14.2_ivi_release -> tizen_3.0.m14.2_ivi_release`\
`    * [new tag]         tizen_3.0.m14.3_ivi_release -> tizen_3.0.m14.3_ivi_release`\
`    * [new tag]         tizen_3.0.m1_mobile_release -> tizen_3.0.m1_mobile_release`\
`    * [new tag]         tizen_3.0.m1_tv_release -> tizen_3.0.m1_tv_release`\
`    * [new tag]         tizen_3.0.m2.a1_mobile_release -> tizen_3.0.m2.a1_mobile_release`\
`    * [new tag]         tizen_3.0.m2.a1_tv_release -> tizen_3.0.m2.a1_tv_release`\
`    * [new tag]         tizen_3.0_ivi_release -> tizen_3.0_ivi_release`\
`   Fetching projects: 100% (14/14), done.`

You can figure out that platform source codes are synced.

`   tree -d`\
`   .`\
`   ├── platform`\
`   │   └── core`\
`   │       └── api`\
`   │           ├── alarm`\
`   │           │   ├── capi-appfw-alarm.pc.in`\
`   │           │   ├── CMakeLists.txt`\
`   │           │   ├── doc`\
`   │           │   │   └── appfw_alarm_doc.h`\
`   │           │   ├── include`\
`   │           │   │   ├── app_alarm_extension.h`\
`   │           │   │   └── app_alarm.h`\
`   │           │   ├── LICENSE`\
`   │           │   ├── packaging`\
`   │           │   │   ├── capi-appfw-alarm.manifest`\
`   │           │   │   └── capi-appfw-alarm.spec`\
`   │           │   └── src`\
`   │           │       └── alarm.c`\
`   │           ├── application`\
`   │           │   ├── app_common`\
`   │           │   │   ├── app_error.c`\
`   │           │   │   ├── app_event.c`\
`   │           │   │   ├── app_finalizer.c`\
`   │           │   │   ├── app_package.c`\
`   │           │   │   ├── app_path.c`\
`   │           │   │   ├── app_resource_manager.c`\
`   │           │   │   └── CMakeLists.txt`\
`   │           │   ├── app_control`\
`   │           │   │   ├── app_control.c`\
`   │           │   │   └── CMakeLists.txt`\
`   │           │   ├── AUTHORS`\
`   │           │   ├── capi-appfw-module.pc.in`\
`   │           │   ├── CMakeLists.txt`\
`   │           │   ├── doc`\
`   │           │   │   ├── appfw_app_common_doc.h`\
`   │           │   │   ├── appfw_app_control_doc.h`\
`   │           │   │   ├── appfw_app_doc.h`\
`   │           │   │   ├── appfw_event_doc.h`\
`   │           │   │   ├── appfw_i18n_doc.h`\
`   │           │   │   ├── appfw_preference_doc.h`\
`   │           │   │   ├── appfw_resource_manager_doc.h`\
`   │           │   │   └── images`\
`   │           │   │       ├── capi_appfw_application_lifecycle.png`\
`   │           │   │       ├── capi_appfw_application_package.png`\
`   │           │   │       ├── capi_appfw_application_resource.png`\
`   │           │   │       └── capi_appfw_application_states.png`\
`   ....`

And this sync command generate a proper .gbs.conf file, too. You can
build tizen plaform source code with gbs without gbs.conf configuration
manually.

`   cat .gbs.conf`

Output:

`   [general]`\
`   #Current profile name which should match a profile section name`\
`   profile = profile.standard`\
`   ########################### PROFILES ############################`\
`   [profile.standard]`\
`   repos = repo.base-arm, repo.base-arm-debug, repo.base-arm64, repo.base-arm64-debug, repo.base-ia32, repo.base-ia32-  debug, repo.base-x86_64, repo.base-x86_64-debug, repo.unified-standard`\
`   [profile.emulator]`\
`   repos = repo.base-ia32, repo.base-ia32-debug, repo.base-x86_64, repo.baes-x86_64-debug, repo.unified-emulator`\
`   ########################### REPO ADDRESSES ############################`\
`   [repo.base-arm]`\
`   url=`[`http://download.tizen.org/snapshots/tizen/base/tizen-base_20170520.1/repos/arm/packages/`](http://download.tizen.org/snapshots/tizen/base/tizen-base_20170520.1/repos/arm/packages/)\
`   [repo.base-arm64]`\
`   url=`[`http://download.tizen.org/snapshots/tizen/base/tizen-base_20170520.1/repos/arm64/packages/`](http://download.tizen.org/snapshots/tizen/base/tizen-base_20170520.1/repos/arm64/packages/)\
`   [repo.base-ia32]`\
`   url=`[`http://download.tizen.org/snapshots/tizen/base/tizen-base_20170520.1/repos/ia32/packages/`](http://download.tizen.org/snapshots/tizen/base/tizen-base_20170520.1/repos/ia32/packages/)\
`   [repo.base-x86_64]`\
`   url=`[`http://download.tizen.org/snapshots/tizen/base/tizen-base_20170520.1/repos/x86_64/packages/`](http://download.tizen.org/snapshots/tizen/base/tizen-base_20170520.1/repos/x86_64/packages/)\
`   [repo.base-arm-debug]`\
`   url=`[`http://download.tizen.org/snapshots/tizen/base/tizen-base_20170520.1/repos/arm/debug/`](http://download.tizen.org/snapshots/tizen/base/tizen-base_20170520.1/repos/arm/debug/)\
`   [repo.base-arm64-debug]`\
`   url=`[`http://download.tizen.org/snapshots/tizen/base/tizen-base_20170520.1/repos/arm64/debug/`](http://download.tizen.org/snapshots/tizen/base/tizen-base_20170520.1/repos/arm64/debug/)\
`   [repo.base-ia32-debug]`\
`   url=`[`http://download.tizen.org/snapshots/tizen/base/tizen-base_20170520.1/repos/ia32/debug/`](http://download.tizen.org/snapshots/tizen/base/tizen-base_20170520.1/repos/ia32/debug/)\
`   [repo.base-x86_64-debug]`\
`   url=`[`http://download.tizen.org/snapshots/tizen/base/tizen-base_20170520.1/repos/x86_64/debug/`](http://download.tizen.org/snapshots/tizen/base/tizen-base_20170520.1/repos/x86_64/debug/)\
`   [repo.unified-standard]`\
`   url=`[`http://download.tizen.org/snapshots/tizen/unified/tizen-unified_20170524.4/repos/standard/packages/`](http://download.tizen.org/snapshots/tizen/unified/tizen-unified_20170524.4/repos/standard/packages/)\
`   [repo.unified-emulator]`\
`   url=`[`http://download.tizen.org/snapshots/tizen/unified/tizen-unified_20170524.4/repos/emulator/packages/`](http://download.tizen.org/snapshots/tizen/unified/tizen-unified_20170524.4/repos/emulator/packages/)

You can build these source codes with gbs now.

`   gbs build -A armv7l --threads=4`

Please refer to <https://wiki.tizen.org/GBS> if you want to know more
detail aboug gbs.

### Show the working tree status

You can see the working tree status with subcommand \'status\'

`   trepo status`

Output:

`   project platform/core/api/alarm/                branch tizen-unified_20170524.4`\
`   project platform/core/api/app-manager/          branch tizen-unified_20170524.4`\
`   project platform/core/api/asp/                  branch tizen-unified_20170524.4`\
`   project platform/core/api/application/          branch tizen-unified_20170524.4`\
`   project platform/core/api/audio-io/             branch tizen-unified_20170524.4`\
`   project platform/core/api/base-utils/           branch tizen-unified_20170524.4`\
`   project platform/core/api/camera/               branch tizen-unified_20170524.4`\
`   project platform/core/api/bluetooth/            branch tizen-unified_20170524.4`\
`   project platform/core/api/common/               branch tizen-unified_20170524.4`\
`   project platform/core/api/connection/           branch tizen-unified_20170524.4`\
`   project platform/core/api/context/              branch tizen-unified_20170524.4`\
`   project platform/core/api/device/               branch tizen-unified_20170524.4`\
`   project platform/core/api/cordova-plugins/      branch tizen-unified_20170524.4`\
`   project platform/core/api/efl-util/             branch tizen-unified_20170524.4`

This show you current branch name and changes not staged for commit. For
example, if you modify file platform/core/api/device/NOTICE then \'trepo
status\' show you unstaged file name.

`   project platform/core/api/alarm/                branch tizen-unified_20170524.4`\
`   project platform/core/api/app-manager/          branch tizen-unified_20170524.4`\
`   project platform/core/api/asp/                  branch tizen-unified_20170524.4`\
`   project platform/core/api/application/          branch tizen-unified_20170524.4`\
`   project platform/core/api/audio-io/             branch tizen-unified_20170524.4`\
`   project platform/core/api/base-utils/           branch tizen-unified_20170524.4`\
`   project platform/core/api/bluetooth/            branch tizen-unified_20170524.4`\
`   project platform/core/api/camera/               branch tizen-unified_20170524.4`\
`   project platform/core/api/common/               branch tizen-unified_20170524.4`\
`   project platform/core/api/connection/           branch tizen-unified_20170524.4`\
`   project platform/core/api/context/              branch tizen-unified_20170524.4`\
`   project platform/core/api/device/               branch tizen-unified_20170524.4`\
`    -m     NOTICE`\
`   project platform/core/api/cordova-plugins/      branch tizen-unified_20170524.4`\
`   project platform/core/api/efl-util/             branch tizen-unified_20170524.4`

### Export trepo yaml

You can export trepo yaml to reuse it on another directory or host.

`   trepo export`

default yaml file name is \'default.yml\'

`   cat default.yml`

Output:

`   project_names:`\
`    - platform/core/api/alarm`\
`    - platform/core/api/app-manager`\
`    - platform/core/api/application`\
`    - platform/core/api/asp`\
`    - platform/core/api/audio-io`\
`    - platform/core/api/base-utils`\
`    - platform/core/api/bluetooth`\
`    - platform/core/api/camera`\
`    - platform/core/api/common`\
`    - platform/core/api/connection`\
`    - platform/core/api/context`\
`    - platform/core/api/cordova-plugins`\
`    - platform/core/api/device`\
`    - platform/core/api/efl-util`\
`   snapshot_version: '20170524.4'`\
`   target_type: standard`

### More options

`   trepo -h`

[Category:Tool](Category:Tool "wikilink")
