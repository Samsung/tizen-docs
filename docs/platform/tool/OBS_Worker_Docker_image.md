Tizen Infra : OBS-Worker with Docker
====================================

Introduction
------------

The obs-workers actually do all the compiling work.
(https://en.opensuse.org)

Version
-------

ver 2.4.0.3 ( OBS : 2.4 Docker Image : 0.3)

Tested on Host OS.
------------------

> ==== Host OS : ubuntu 14.04 ====
>
>     docker version : 1.4.1
>     docker version : 1.6.2     
>     docker version : 1.7.0
>
> #### Host OS : opensuse 13.1
>
>     docker version : 1.3.2
>     docker version : 1.6.2 

HW Information of the OBS Worker
--------------------------------

> ==== In my configuration, I use two (2) obs-workers ====
>
>     === Server Info ===
>     CPU clock : 2.70GHz   
>     CPU core : 24
>     RAM MEM : 64GB
>     Disk Cache : 2GB
>     HDD : 1TB
>
>     === Desktop Info ===
>     CPU clock : 3.40GHz
>     CPU core : 4
>     RAM MEM : 16GB
>     SSD  : 512 MB

Pre-installed Packages
----------------------

> ==== Image OS : flavio/opensuse-12-3 ====
>
>     vim tar wget telnet supervisor sudo
>     obs-worker
>     kvm libvirt libvirt-python qemu virt-manager qemu-linux-user
>     build-initvm-x86_64 build-initvm-i586
>     psmisc

Download
--------

> ===== URL =====
>
>     http://cdn.download.tizen.org/docker/obsworker/obsworker_2.4-2.4.0.3-docker-script.tar.gz

Execution
---------

> ==== Download an images and execute. ====\
> \$ wget \< url \>\
> \$ ls
>
>     obsworker_2.4-2.4.0.3-docker-script.tar.gz
>
> \$ tar -xvf obsworker\_2.4-2.4.0.3-docker-script.tar.gz
>
> \$ cd clientobsworker
>
> \$ ls
>
>      config.conf  dobsworker.sh  env  obsworker_2.4-2.4.0.3-docker-image.tar.gz  root
>
>      #### Description ####
>      * config.conf : Metaconfig file of container
>      * env : Environment variables of container
>      * -docker-image.tar.gz : Docker image 
>         (“$ ./dobsworker.sh load” will load docker image from *-docker-image.tar.gz )
>      * root : Specific configuration files to be applied on container
>
> #### Load an image from a tar archive.
>
> \$ sudo ./dobsworker.sh load
>
> #### List images.
>
> \$ sudo docker images
>
>     $ docker images 
>     tizendocker:443/obsworker            2.4.0.3
>
> #### Configuration of the Container
>
> \$ vi config.conf
>
>     Configuration a config.conf of the dobsworker.sh
>
>     ### In the value of the OBS_WORKER_PORTBASE of the obs-server file must be increased by the number of OBS_WORKER_INSTANCES.
>     export PORTS=&quot;60000-60003&quot; ## ex) &quot;hostport1 hostport2&quot; or &quot;hostport1:containerport1&quot; or &quot;exposeport1-    exposeport2&quot;
>
>     ### Assign a name to the container
>     export CONTAINER=&quot;obsworker&quot;
>
>     ### Container host name
>     export HOSTNAME=&quot;OBSWorker&quot;
>
>     ### Add a custom host-to-IP mapping (host:ip)
>     export ADD_HOSTS=&quot;&lt;obsserver hostname&gt;:&lt;ip&gt;&quot; ## ex)&lt;obsserver hostname1&gt;:&lt;ip1&gt;                            
>
> #### Configuration of OBS worker
>
> \$ vi \$(pwd)/root/etc/sysconfig/obs-server
>
>     # Default setting : 4 instances are created, and 1 job (cpu) is assinged to each instance.
>     # You can change OBS worker setting (optimization based on your server environment)
>     # (refer to https://wiki.tizen.org/wiki/OBS_2.4_All-in-One_Server)
>     ###Set Number of all instances which is used by worker
>     # OBS_WORKER_INSTANCES=(Max Port No. - Min Port No.+1)
>     # ex) if you use &quot;export PORTS=&quot;60000-60007, then OBS_WORKER_INSTANCES=(60007-60000 +1) = 8
>     OBS_WORKER_INSTANCES=&quot;4&quot;
>
>     # OBS_WORKER_JOBS : number of cpus which is used by each instance
>     # Note : (OBS_WORKER_INSTANCES * OBS_WORKER_JOBS ) must not exceed total number of host cpus.
>     # ex) total number of host cpus = 32 core, and OBS_WORKER_INSTANCES=12
>     # if OBS_WORKER_JOBS=2, it's ok (OBS_WORKER_INSTANCES * OBS_WORKER_JOBS =24, which is lower than 32)
>     # if OBS_WORKER_JOBS=3, woker will not work. (OBS_WORKER_INSTANCES * OBS_WORKER_JOBS =36, which is higher than 32)
>     OBS_WORKER_JOBS = 4
>
>     # important ( worker1,worker2 must be different port value.)
>     # ex) worker1 server = &quot;60000&quot; then worker2 server = &quot;60020&quot;
>     OBS_WORKER_PORTBASE=&quot;60000&quot;
>
>     # The hostname or the IP address of the OBS server
>     OBS_SRC_SERVER=&quot;&lt;OBSServer ip&gt;:5352&quot;
>
>     # The hostname or the IP address of the OBS server
>     OBS_REPO_SERVERS=&quot;&lt;OBSServer ip&gt;:5252&quot;
>     ... 
>     #The product of OBS_WORKER_INSTANCES and OBS_WORKER_JOBS should be smaller than the number of CPU cores in each OBS worker node.
>
> If you use a firewall on host OS, you have to allow a obsworker port
> number.
>
>     $sudo ufw allow proto tcp to any port 60000:60004
>
> #### Start OBS worker service
>
>     $ sudo ./dobsworker.sh start

Debugging OBS worker
--------------------

If you want to see the build log.

`$ sudo ./dobsworker.sh attach`\
`# screen -r -d`\
`      starting worker d41d8cd98f00b204e9800998ecf8427e build d41d8cd98f00b204e9800998ecf8427e`

`# how to exit screen => ctrl+A and D`\
`# how to move 0 screen => ctrl+A and 0`

Initialize
----------

> \#\#\# remove all data\
> \$ sudo ./dobsworker.sh stop\
> \$ sudo ./dobsworker.sh rm\
> \$ sudo ./dobsworker.sh start

CLI
---

>     USAGE: ./dobsworker.sh COMMAND
>     -e 
>     Commands:
>         install   Install lxc-docker-1.4.1
>         start     Start a stopped container
>         attach    Attach to a running container
>         stop      Stop a running container
>         status    Status a running container
>         rm        Remove this containers
>         restart   stop, start a container
>         kill      Kill a running container
>         logs      Fetch the logs of a container
>         cp        Copy files/folders from a container's filesystem to the host path
>         pull      Pull an image or a repository from a Docker registry server
>         inspect   Return low-level information on a containe
>         top       Lookup the running processes of a container
>         save      Save an image to a tar archive
>         load      Load an image from a tar archive
>         help      help

Troubleshooting
---------------

>     --------------------------------------------------------------------------

Dockerfile
----------

> If you want to build an image from a Dockerfile, you can find a
> Dockerfile from review.tizen.org.

License
-------

> OBS
>
>      GNU Licenses (http://openbuildservice.org/help/manuals/obs-reference-guide/apb.html)

\
== References ==

>     https://wiki.tizen.org/wiki/OBS_Installation_and_Setup

>     https://en.opensuse.org/openSUSE:Build_Service_private_installation

### OBS\_Server: config.conf


    export HOSTNAME="tizendocker2"

### OBSWorker(default): config.conf

    export CONTAINER="obsworker_2.4"

    export PORTS="60000-60003" ## ex) "hostport1 hostport2" or "hostport1:containerport1" or "exposeport1-exposeport2"

    export HOSTNAME="OBSWorker"

    export ADD_HOSTS="tizendocker2:168.219.201.100"

### OBSWorker(default): root/etc/sysconfig/obs-server

    ...
    OBS_WORKER_INSTANCES="4"
    ...
    OBS_SRC_SERVER="168.219.201.100:5352"
    ...
    OBS_REPO_SERVERS="168.219.201.100:5252"
    ...
    OBS_WORKER_PORTBASE="60000"
    ...

    $ sudo ./dobsworker.sh stop 
    $ sudo ./dobsworker.sh rm 
    $ sudo ./dobsworker.sh start

### OBS\_Worker0: config.conf

    export CONTAINER="obsworker_2.4_0"

    export PORTS="60010-60013" ## ex) "hostport1 hostport2" or "hostport1:containerport1" or "exposeport1-exposeport2"

    export HOSTNAME="OBS_Worker_0"

    export ADD_HOSTS="tizendocker2:168.219.201.100"

### OBS\_Worker0: root/etc/sysconfig/obs-server

    ...
    OBS_WORKER_INSTANCES="4"
    ...
    OBS_SRC_SERVER="168.219.201.100:5352"
    ...
    OBS_REPO_SERVERS="168.219.201.100:5252"
    ...
    OBS_WORKER_PORTBASE="60010"
    ...

    $ sudo ./dobsworker.sh stop 
    $ sudo ./dobsworker.sh rm 
    $ sudo ./dobsworker.sh start

### OBS\_Worker1: config.conf

    <nowiki>

    export CONTAINER="obsworker_2.4_1"

    export PORTS="60020-60023" ## ex) "hostport1 hostport2" or "hostport1:containerport1" or "exposeport1-exposeport2"

    export HOSTNAME="OBS_Worker_1"

    export ADD_HOSTS="tizendocker2:168.219.201.100"

### OBS\_Worker1:root/etc/sysconfig/obs-server

    ...
    OBS_WORKER_INSTANCES="4"
    ...
    OBS_SRC_SERVER="168.219.201.100:5352"
    ...
    OBS_REPO_SERVERS="168.219.201.100:5252"
    ...
    OBS_WORKER_PORTBASE="60020"
    ...

    $ sudo ./dobsworker.sh stop 
    $ sudo ./dobsworker.sh rm 
    $ sudo ./dobsworker.sh start

Back to [Setup of Tizen Infrastructure with Docker](Setup_of_Tizen_Infrastructure_with_Docker "wikilink")
---------------------------------------------------------------------------------------------------------

[Category:Tool](Category:Tool "wikilink")
