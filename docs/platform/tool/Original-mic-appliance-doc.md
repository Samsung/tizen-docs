Overview
--------

[MIC](MIC "wikilink") appliance is a preconfigured KVM image, which runs
mic on the boot. This document describes configuration and deployment of
the appliance.

Creation
--------

### root password is \'appliance\'

### 1. Qemu snapshot mode

### 2. Input and output.

To provide .ks file to the appliance and to get images out of it Plan9
network share is used. Note, that both host and guest kernels should
have Plan9 file system support.

On the host side local directory ./mic is shared to the appliance by
providing -virtfs
local,id=test\_dev,path=mic,security\_model=mapped,mount\_tag=share
command line parameters to qemu. Inside appliance this share is mounted
to /media on boot by adding this line to /etc/fstab:

    share /media  9p  rw,relatime,dirsync,trans=virtio,version=9p2000.L,posixacl,cache=loose 0 0

(JF: currently, this line has been commented out in working appliance)

See \"Qemu wiki\":<http://wiki.qemu.org/Documentation/9psetup> for more
details about Plan9 folder sharing.

### 3. Mic startup file

cat /etc/init.d/mic


    $ cat /etc/init.d/mic

    #!/bin/sh
    ### BEGIN INIT INFO
    # Provides:          mic
    # Required-Start:    $network $syslog
    # Required-Stop:     $network $syslog
    # Default-Start:     3 5
    # Default-Stop:      0 1 2 6
    # Description:       Image creator service
    ### END INIT INFO

    echo
    echo '========= Mic appliance ========='

    mount -t 9p -o trans=virtio share /media -oversion=9p2000.L
    if [ -f /media/out/*.ks ] ; then
        ks=`ls /media/out/*.ks | head -1`
        ks=`basename $ks`
        log=`echo $ks | sed 's/\.ks$/.log/'`
        echo "Found $ks. Running mic"
        cat /media/out/$ks
        echo
        mv /media/out/$ks /media/
        extra=`cat /media/out/command 2>/dev/null;:`
        rm -rf /media/{out,cache,tmp}
        mkdir /media/{out,cache,tmp}
        cp /media/$ks /media/out/$ks
        time mic cr auto $extra /media/out/$ks && echo 'success' > /media/status
        echo s > /proc/sysrq-trigger
        echo u > /proc/sysrq-trigger
        echo o > /proc/sysrq-trigger
    else
        echo '.ks file not found. Nothing to do for mic'
    fi
    umount /media
    exit 0

Added iptables rules into mic appliance to redirect download.tizen.org
-\> download.vlan200.tizen.org for mic to be able to build images:

added /etc/sysconfig/network/if-up.d/iptables script

    #! /bin/sh
    iptables-restore < /etc/iptables.rules
    exit 0
    chmod +x /etc/sysconfig/network/if-up.d/iptables

Added rule to /etc/iptables.rules:

    # redirect download.tizen.org -> download.vlan200.tizen.org
    *nat
    -A OUTPUT -d 198.145.20.32/32 -p tcp -m multiport --dports 80,443 -j DNAT --to-destination 10.0.200.29
    COMMIT

Booting
-------

ssh worker sudo su - jenkins qemu-system-x86\_64 -machine
accel=kvm:xen:tcg -name opensuse -M pc -m 8096 -smp 2 -vga none -drive
file=mic-appliance -nographic

Upgrading the mic-appliance
---------------------------

After booting the mic-appliance:

### 1. Login the mic-appliance by the root user and the password is appliance .

### 2. Upgrade the mic

    $ zypper mr -d repo-oss repo-update
    Update baseurl of tools.repo to "http://download.tizen.org/tools/archive/$archive_id"
    $ zypper refresh
    $ zypper up mic
    $ zypper up mic-native
    $ zypper mr -e repo-oss repo-update

### 3.If you can\'t upgrade the mic because of the proxy , you can do like this:

    export http_proxy = HOSTNAME
    export https_proxy = HOSTNAME

Deployment on tizen.org infrastructure
--------------------------------------

-   reconfigure appliance on some worker, by booting/changing/shutting
    it down. Note, that snapshot mode should be turned off
-   tar -jcSvf mic-appliance.tar.bz2 mic-appliance
-   copy it to master:

<!-- -->

    $ ssh robot
    robot:~> sudo bash
    cd /var/lib/jenkins/imager-setup
    scp -i ../.ssh/robot_tizen_workers_2013_11_25_SN001 jenkins@w09.vlan200.tizen.org:/var/lib/jenkins/mic-appliance.tar.bz2 .

-   propagate to the rest of workers by checking \'deploy on save now\'
    checkbox in \'Slave setups\' configuration on
    <https://build.tizen.org/robot/configure> and clicking \'Save\'
    button. Note, that this operation is heavy and time consuming as it
    requires transfer of quite big tarball to 17 workers and unpack it
    there. It takes about 15 minutes and browser reported 504 Server
    Error couple of times. This is harmless and should be ignored.
-   test image creation by building image-creator job:
    <https://build.tizen.org/robot/job/image-creator/build?delay=0sec>

Resizing appliance
------------------

Mic is very disk-space consuming piece of software and Tizen images are
growing in size. For these reasons sometimes appliance images should be
resized. Here is how to do that:

-   resize image: truncate \--size 10G mic-appliance
-   create loop device with it: losetup /dev/loop0 ./mic-appliance
-   re-create root partition with new size:

<!-- -->

    parted /dev/loop0
    (parted) unit kb
    (parted) print
    Model: Loopback device (loopback)
    Disk /dev/loop0: 10737418kB
    Sector size (logical/physical): 512B/512B
    Partition Table: msdos

    Number  Start     End        Size       Type     File system     Flags
     1      1049kB    534774kB   533725kB   primary  linux-swap(v1)  type=83
     2      534774kB  6442451kB  5907677kB  primary  ext4            boot, type=83
    (parted) rm 2
    (parted) mkpart primary 534774 10737418
    (parted) toggle 2 boot
    (parted) p
    Model: Loopback device (loopback)
    Disk /dev/loop0: 10.7GB
    Sector size (logical/physical): 512B/512B
    Partition Table: msdos

    Number  Start   End     Size    Type     File system     Flags
     1      1049kB  535MB   534MB   primary  linux-swap(v1)  type=83
     2      535MB   10.7GB  10.2GB  primary  ext4            boot, type=83

    (parted) q

-   populate partitions through device mapper using kpartx: kpartx -a -v
    /dev/loop0
-   check file system on new partition: e2fsck -f /dev/mapper/loop0p2
-   resize file system: resize2fs /dev/mapper/loop0p2
-   detach image from loop: losetup -d /dev/loop0

[Category:Tool](Category:Tool "wikilink")
