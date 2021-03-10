Introduction
------------

This document describes how to use GBS fullbuild script and how to
create Tizen images using MIC.\
How to install GBS and MIC is well described in Tizen
documentation.(https://source.tizen.org/documentation/reference/git-build-system,
<https://source.tizen.org/documentation/reference/mic-image-creator>)\
\'repo init\' and \'repo sync\' are used to construct full source tree
of Tizen\

GBS Local Fullbuild Script
--------------------------

    #!/bin/bash


    #input workspace
    echo "Input your workspace"
    echo "If you input nothing, default workspace is ~/gbs_fullbuild"
    echo -e "workspace: \c"
    read workspace

    if [ ! $workspace ]
    then
        workspace=~/gbs_fullbuild
    fi

    echo "Your workspace=$workspace"
    mkdir -p $workspace

    #Input tizen version
    echo -e "\n\nInput tizen version"


    while [ 1 ]
    do
        echo "Supported tizen version is 3 and 4"
        echo -e "Tizen version: \c"
        read tizen_version
        
        if [ $tizen_version = 3 -o $tizen_version = 4 ];then
            break
        fi

        echo "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
        echo "You selected nothing or invalid tizen version"
        echo -e "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n\n"
    done

    echo "Selected tizen version=$tizen_version"



    #Input tizen profile
    echo -e "\n\n"
    if [ $tizen_version = 3 ]
    then
        echo "Input tizen profile"

        while [ 1 ]
        do
            echo "Select one of tizen profile for tizen 3.0: "
            echo "common, mobile, tv, wearable, ivi"
            echo -e "Tizen profile: \c"
            read profile

            if [ $profile = common -o $profile = mobile -o $profile = tv -o $profile = wearable -o $profile = ivi ];then
                break
            fi
            echo "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
            echo "You selected nothing or invalid tizen profile"
            echo -e "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n\n"
        done
    else
        echo "There is only one profile in tizen 4.0"
        profile=unified
    fi

    echo "Selected tizen profile=$profile"



    #Input profile snapshot number
    echo -e "\n\nSelect profile snapshot"
    if [ $tizen_version = 3 ]
    then
        profile_prefix="3.0-"
    fi

    while [ 1 ]
    do
        snapshot_candidate=$(curl http://download.tizen.org/snapshots/tizen/${profile_prefix}${profile}/ | grep -e "tizen-${profile_prefix}${profile}" | awk -F\" '{print $2}'  |  sed 's/\///')
        echo "You have to select one of snapshot number in http://download.tizen.org/snapshots/tizen/${profile_prefix}${profile}/"
        echo "Candidate snapshot lists are like below. You have to select snapshot number among them"
        echo "================================================="
        echo "latest"
        for ss in $snapshot_candidate; do echo $ss;done
        echo "================================================="
        echo -e "Snapshot number: \c"
        read tmp_snapshot_number

        snapshot_number=$(echo $tmp_snapshot_number | sed 's/\///')

        snapshot_error=$(curl http://download.tizen.org/snapshots/tizen/${profile_prefix}${profile}/$snapshot_number/ | grep "Not Found")

        if [ ! $snapshot_error -a $snapshot_number ];then
            break
        fi

        echo "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
        echo "You selected nothing or invalid snapshot number"
        echo -e "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n\n"
    done

    echo "Selected tizen snapshot number=$snapshot_number"
    srcrpm_snapshot=http://download.tizen.org/snapshots/tizen/${profile_prefix}${profile}/${snapshot_number}/


    #Input repository
    echo -e "\n\nSelect build repository"

    while [ 1 ]
    do
        repo_candidate=$(curl $srcrpm_snapshot/repos/ | grep "a href" | sed '1d' | awk -F\" '{print $2}' |  sed 's/\///')
        echo "You have to select one of repositories in $srcrpm_snapshot/repos/"
        echo "Candidate repository lists are like below. You have to select repository among them"
        echo "================================================="
        for repo in $repo_candidate;do echo $repo;done
        echo "================================================="

        echo -e "build repository: \c"
        read build_repository

        snapshot_error=$(curl $srcrpm_snapshot/repos/${build_repository} | grep "Not Found")
        if [ ! $snapshot_error -a $build_repository ];then
            break
        fi

        echo "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
        echo "You selected nothing or invalid build repository"
        echo -e "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n\n"
    done

    echo "Selected build repository=$build_repository"


    #Clone all tizen code using repo init/ repo sync
    cd $workspace
    repo init -u https://git.tizen.org/cgit/scm/manifest -b tizen -m common.xml

    #replace projects.xml to manifest.xml in snapshot repo
    pushd $workspace/.repo/manifests/common/
    wget $srcrpm_snapshot/builddata/manifest/${snapshot_number}_$build_repository.xml
    mv ${snapshot_number}_$build_repository.xml projects.xml
    popd

    repo sync

    REPO_SYNC_LOG=$workspace/repo_sync_log
    if [ -e $REPO_SYNC_LOG ];then
      rm $REPO_SYNC_LOG
    fi
    repo sync >> $REPO_SYNC_LOG 2>&1
    REPO_SYNC_ERR_RESULT=$(cat $REPO_SYNC_LOG | grep "Cannot fetch")
    if [ $(echo $REPO_SYNC_ERR_RESULT | sed -n '1p' | awk '{print $1}') ];then
      echo -e "\n\n\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
      echo $REPO_SYNC_ERR_RESULT
      echo -e "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n\n"
      echo "repo sync is terminated due to error above"
      exit
    fi


    #Replace build.conf file to that in snapshot repo
    build_conf_dl=$workspace/scm/meta/build-config/
    pushd $build_conf_dl
    build_conf_file=$(curl $srcrpm_snapshot/repos/$build_repository/packages/repodata/ | grep build.conf | awk -F\" '{print $2}')
    wget $srcrpm_snapshot/repos/$build_repository/packages/repodata/$build_conf_file
    gzip -d $build_conf_file
    mv *-build.conf build.conf
    buildconf=$build_conf_dl/build.conf
    popd


    #compose .gbs.conf file
    gbs_conf_file=$workspace/.gbs.conf
    chmod +w $gbs_conf_file

    if [ $tizen_version = 3 ]
    then
        profile_prefix="3.0-"
    fi

    echo "[general]
    profile = profile.tizen_${profile}

    [profile.tizen_${profile}]
    repos = repo.${profile_prefix}base.arm,repo.${profile_prefix}base.arm64,repo.${profile_prefix}base.emulator32,repo.${profile_prefix}base.emulator64,\
    repo.${profile_prefix}base.arm.debug,repo.${profile_prefix}base.arm64.debug,repo.${profile_prefix}base.emulator32.debug,repo.${profile_prefix}base.emulator64.debug
    buildroot=$workspace/GBS-ROOT/
    buildconf=$build_conf_dl/build.conf

    [repo.3.0-base.arm]
    url = http://download.tizen.org/snapshots/tizen/3.0-base/latest/repos/arm/packages/
    [repo.3.0-base.arm.debug]
    url = http://download.tizen.org/snapshots/tizen/3.0-base/latest/repos/arm/debug/

    [repo.3.0-base.arm64]
    url = http://download.tizen.org/snapshots/tizen/3.0-base/latest/repos/arm64/packages/
    [repo.3.0-base.arm64.debug]
    url = http://download.tizen.org/snapshots/tizen/3.0-base/latest/repos/arm64/debug/

    [repo.3.0-base.emulator32]
    url = http://download.tizen.org/snapshots/tizen/3.0-base/latest/repos/emulator32/packages/
    [repo.3.0-base.emulator32.debug]
    url = http://download.tizen.org/snapshots/tizen/3.0-base/latest/repos/emulator32/debug/

    [repo.3.0-base.emulator64]
    url = http://download.tizen.org/snapshots/tizen/3.0-base/latest/repos/emulator64/packages/
    [repo.3.0-base.emulator64.debug]
    url = http://download.tizen.org/snapshots/tizen/3.0-base/latest/repos/emulator64/debug/


    [repo.base.arm]
    url = http://download.tizen.org/snapshots/tizen/base/latest/repos/arm/packages/
    [repo.base.arm.debug]
    url = http://download.tizen.org/snapshots/tizen/base/latest/repos/arm/debug/

    [repo.base.arm64]
    url = http://download.tizen.org/snapshots/tizen/base/latest/repos/arm64/packages/
    [repo.base.arm64.debug]
    url = http://download.tizen.org/snapshots/tizen/base/latest/repos/arm64/debug/

    [repo.base.emulator32]
    url = http://download.tizen.org/snapshots/tizen/base/latest/repos/ia32/packages/
    [repo.base.emulator32.debug]
    url = http://download.tizen.org/snapshots/tizen/base/latest/repos/ia32/debug/

    [repo.base.emulator64]
    url = http://download.tizen.org/snapshots/tizen/base/latest/repos/x86_64/packages/
    [repo.base.emulator64.debug]
    url = http://download.tizen.org/snapshots/tizen/base/latest/repos/x86_64/debug/
    " > $gbs_conf_file



    #Input gbs build command
    echo -e "\n\nInput gbs build command:"
    read gbs_build_command

    cd $workspace
    $gbs_build_command --define 'jobs 8' --define '_smp_mflags -j8'

\

How to use GBS Local Fullbuild Script
-------------------------------------

You have to input parameters while script is running\
====workspace====

-   Overall workspace where source codes are downloaded and GBS build
    results are saved\
-   You will meet below instroction\

<!-- -->

    Input your workspace
    If you input nothing, default workspace is ~/gbs_fullbuild
    workspace:

#### Tizen version

-   Currently, supported tizen version is \'3\' and \'4\'\
-   You will meet below instroction\

<!-- -->

    Input tizen version
    Supported tizen version is 3 and 4
    Tizen version:

-   If you input tizen version except \'3\' and \'4\', you have to input
    tizen version again\

#### Tizen profile

-   If you select tizen version as \'4\', \'unified\' profile will be
    automatically selected, because there is only one profile in tizen
    version \'4\'\
-   If you select tizen version as \'3\', you have to select one of
    profiles among \'mobile, tv, common, ivi, wearabe\'\
-   If you select tizen version as \'3\', you will meet below
    instroction\

<!-- -->

    Select one of tizen profile for tizen 3.0:
    common, mobile, tv, wearable, ivi
    Tizen profile:

-   If you select tizen version as \'3\', and if you input tizen profile
    except \'mobile, tv, common, ivi, wearabe\', you have to input tizen
    profile again\

#### Snapshot number

-   You have to select one of snapshot number which will be used in
    source code downloading\
-   Snapshot candidates are listed up. You have to select one of them\

<!-- -->

    You have to select one of snapshot number in $snapshot_url
    Candidate snapshot lists are like below. You have to select snapshot number among them
    =================================================
    Snapshot candidate list
    =================================================
    Snapshot number:

-   If you select snapshot number which is not in snapshot candidate
    list, you have to input snapshot number again\

#### Build Repository

-   You have to select one of build repository which will be used in
    source code downloading\
-   Repository candidates are listed up. You have to select one of them\

<!-- -->

    You have to select one of repositories in $repository_url
    Candidate repository lists are like below. You have to select repository among them
    =================================================
    Repository candidate list
    =================================================
    build repository:

-   If you select build repository which is not in repository candidate
    list, you have to input build repository again\

\

#### Full source code download

-   Full source code will be downloaded automatically using \'repo
    init\' & \'repo sync\'\
-   .gbs.conf file will be automatically created (path:
    \$workspace/.gbs.conf)\
-   build.conf file will be automatically downloaded (path:
    \$workspace/scm/meta/build-conf/build.conf)\
-   GBS build results will be stored in \$workspace/GBS-ROOT/\

\

#### GBS build command

-   Input build command which will be used in gbs building\
-   example\

<!-- -->

    gbs build -A armv7l --threads=8

\
\

Example
-------

#### Tizen 3.0 Mobile

    nanjing@t016:/data/park_temp/fullbuild_general$ ./gbs_fullbuild.sh 
    Input your workspace
    If you input nothing, default workspace is ~/gbs_fullbuild
    workspace: /data/park_temp/fullbuild_general/3.0-mobile-#1
    Your workspace=/data/park_temp/fullbuild_general/3.0-mobile-#1


    Input tizen version
    Supported tizen version is 3 and 4
    Tizen version: 3
    Selected tizen version=3



    Input tizen profile
    Select one of tizen profile for tizen 3.0: 
    common, mobile, tv, wearable, ivi
    Tizen profile: mobile
    Selected tizen profile=mobile


    Select profile snapshot
      % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                     Dload  Upload   Total   Spent    Left  Speed
    100  2312    0  2312    0     0  30523      0 --:--:-- --:--:-- --:--:-- 30826
    You have to select one of snapshot number in http://download.tizen.org/snapshots/tizen/3.0-mobile/
    Candidate snapshot lists are like below. You have to select snapshot number among them
    =================================================
    latest
    tizen-3.0-mobile_20170407.1
    tizen-3.0-mobile_20170407.2
    tizen-3.0-mobile_20170407.3
    tizen-3.0-mobile_20170407.4
    tizen-3.0-mobile_20170410.1
    tizen-3.0-mobile_20170410.2
    tizen-3.0-mobile_20170411.1
    tizen-3.0-mobile_20170411.2
    tizen-3.0-mobile_20170412.1
    tizen-3.0-mobile_20170412.2
    tizen-3.0-mobile_20170414.1
    tizen-3.0-mobile_20170414.2
    tizen-3.0-mobile_20170414.3
    tizen-3.0-mobile_20170420.1
    tizen-3.0-mobile_20170420.2
    =================================================
    Snapshot number: tizen-3.0-mobile_20170420.2
      % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                     Dload  Upload   Total   Spent    Left  Speed
    100   713    0   713    0     0  16997      0 --:--:-- --:--:-- --:--:-- 17390
    Selected tizen snapshot number=tizen-3.0-mobile_20170420.2


    Select build repository
      % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                     Dload  Upload   Total   Spent    Left  Speed
    100   630    0   630    0     0   8231      0 --:--:-- --:--:-- --:--:--  8289
    You have to select one of repositories in http://download.tizen.org/snapshots/tizen/3.0-mobile/tizen-3.0-mobile_20170420.2//repos/
    Candidate repository lists are like below. You have to select repository among them
    =================================================
    arm-wayland
    emulator32-wayland
    target-TM1
    =================================================
    build repository: arm-wayland
    ...
    ...
    repo init log
    repo sync log
    ...
    ...
    gbs build command: gbs build -A armv7l --threads=8
    ...
    ...
    gbs build log
    ...
    ...

\
\
====Tizen Unified====

    nanjing@t016:/data/park_temp/fullbuild_general$ ./gbs_fullbuild.sh 
    Input your workspace
    If you input nothing, default workspace is ~/gbs_fullbuild
    workspace: /data/park_temp/fullbuild_general/unified-#1
    Your workspace=/data/park_temp/fullbuild_general/unified-#1


    Input tizen version
    Supported tizen version is 3 and 4
    Tizen version: 4
    Selected tizen version=4



    There is only one profile in tizen 4.0
    Selected tizen profile=unified


    Select profile snapshot
      % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                     Dload  Upload   Total   Spent    Left  Speed
    100  3301    0  3301    0     0  10440      0 --:--:-- --:--:-- --:--:-- 10413
    You have to select one of snapshot number in http://download.tizen.org/snapshots/tizen/unified/
    Candidate snapshot lists are like below. You have to select snapshot number among them
    =================================================
    latest
    tizen-unified_20170408.1
    tizen-unified_20170408.2
    tizen-unified_20170410.1
    tizen-unified_20170411.1
    tizen-unified_20170411.2
    tizen-unified_20170412.1
    tizen-unified_20170413.1
    tizen-unified_20170414.1
    tizen-unified_20170414.2
    tizen-unified_20170414.3
    tizen-unified_20170414.4
    tizen-unified_20170417.1
    tizen-unified_20170418.1
    tizen-unified_20170418.2
    tizen-unified_20170418.3
    tizen-unified_20170419.1
    tizen-unified_20170419.2
    tizen-unified_20170420.1
    tizen-unified_20170420.2
    tizen-unified_20170421.1
    tizen-unified_20170421.2
    tizen-unified_20170421.3
    tizen-unified_20170424.1
    =================================================
    Snapshot number: tizen-unified_20170424.1
      % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                     Dload  Upload   Total   Spent    Left  Speed
    100   701    0   701    0     0   1865      0 --:--:-- --:--:-- --:--:--  1864
    Selected tizen snapshot number=tizen-unified_20170424.1


    Select build repository
      % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                     Dload  Upload   Total   Spent    Left  Speed
    100   489    0   489    0     0   3599      0 --:--:-- --:--:-- --:--:--  3622
    You have to select one of repositories in http://download.tizen.org/snapshots/tizen/unified/tizen-unified_20170424.1//repos/
    Candidate repository lists are like below. You have to select repository among them
    =================================================
    emulator
    standard
    =================================================
    build repository: standard
    ...
    ...
    repo init log
    repo sync log
    ...
    ...
    gbs build command: gbs build -A armv7l --threads=8
    ...
    ...
    gbs build log
    ...
    ...

[Category:Tool](Category:Tool "wikilink")
