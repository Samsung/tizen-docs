Tizen Infra : OBS-Server with Docker
====================================

Introduction
------------

The Open Build Service (OBS) is a generic system to build and distribute
packages from sources in an automatic, consistent and reproducible way.
It makes it possible to release software for a wide range of operating
systems and hardware architectures. (https://en.opensuse.org)

Version
-------

>     ver 2.4.0.7 ( OBS : 2.4 Docker Image : 0.7)

Tested on Host OS.
------------------

> ===== Host OS : ubuntu 14.04 =====
>
>     docker version : 1.4.1
>     docker version : 1.6.2     
>     docker version : 1.7.0

> ===== Host OS : opensuse 13.1 =====
>
>     docker version : 1.3.2
>     docker version : 1.6.2 

HW Information of the OBS Server
--------------------------------

> ===== In the default configuration =====
>
>     === Server Info ===
>     CPU clock : 2.70GHz   
>     CPU core : 24
>     RAM MEM : 64GB
>     Disk Cache : 2GB
>     HDD : 1TB

Pre-installed Packages
----------------------

> ===== Image OS : flavio/opensuse-12-3 =====
>
>     vim tar wget telnet supervisor sudo
>     obs-server obs-signd obs-utils obs-api git-buildpackage obs-service-gbs
>     obs-source_service qemu-linux-user build-initvm-x86_64 build-initvm-i586 obs-event-plugin
>     apache2 apache2-mod_xforward rubygem-passenger-apache2 memcached
>     php5 php5-gd php5-gettext php5-mbstring php5-mysql
>     php5-pear php5-suhosin apache2-mod_php5 php5-bcmath
>     php5-bz2 php5-calendar php5-curl php5-ftp php5-gmp
>     php5-imap php5-ldap php5-mcrypt php5-odbc php5-openssl
>     php5-pcntl php5-pgsql php5-posix php5-shmop php5-snmp
>     php5-soap php5-sockets php5-sysvsem php5-wddx php5-xmlrpc
>     php5-xsl php5-exif php5-fastcgi php5-sysvmsg php5-sysvshm
>     npt iputils
>     perl-GD
>     obs-service-git-buildpackage
>     libcurl4-7.42.1
>     librpm-tizen

Download
--------

> URL :
> <http://cdn.download.tizen.org/docker/obsserver/obsserver_2.4-2.4.0.7-docker-script.tar.gz>
>
>     $ wget http://cdn.download.tizen.org/docker/obsserver/obsserver_2.4-2.4.0.7-docker-script.tar.gz
>
>     --2015-09-09 13:18:02--  http://cdn.download.tizen.org/docker/obsserver/obsserver_2.4-2.4.0.7-docker-script.tar.gz
>     Length: 618379115 (590M) [application/x-gzip]
>     Saving to: `obsserver_2.4-2.4.0.7-docker-script.tar.gz'
>
>     100%[========================================================================>] 618,379,115 11.2M/s   in 58s     
>
>     2015-09-09 13:19:00 (10.2 MB/s) - `obsserver_2.4-2.4.0.7-docker-script.tar.gz' saved [618379115/618379115]

Execution
---------

> ===== Download an images and execute. =====\
> \$ wget \< url \>\
> \$ ls
>
>     obsserver_2.4-2.4.0.7-docker-script.tar.gz
>
> \$ tar -xvf obsserver\_2.4-2.4.0.7-docker-script.tar.gz
>
> \$ cd clientobsserver
>
> \$ ls
>
>      config.conf  dobsserver.sh  env  obsserver_2.4-2.4.0.7-docker-image.tar.gz  root
>      
>      #### Description ####
>      * config.conf : Metaconfig file of container
>      * env : Environment variables of container
>      * -docker-image.tar.gz : Docker image 
>         (“$ ./dobsserver.sh load” will load docker image from *-docker-image.tar.gz )
>      * root : Specific configuration files to be applied on container
>
> \$ sudo ./dobsserver.sh load
>
> \$ docker images
>
>     $ docker images 
>     tizendocker:5000/obsserver            2.4.0.7
>
> \$ vi env/env.list
>
>     #If you want to change the password for the MySQL database, you can change it 
>
>     #If you are using the proxy in your enviroment, pleaese add below line.
>     ftp_proxy=ftp://123.456.789.012
>     http_proxy=http://123.456.789.012
>     https_proxy=https://123.456.789.012
>     socks_proxy=socks://123.456.789.012
>
> \$ vi config.conf
>
>     # Configuration of the dobsserver.sh
>     # You can change the hostname. Do not change others.
>     export HOSTNAME= #hostname in container
>
>     #If you remove the Container, the changed values are deleted,
>     # the backup data must be managed volumes.
>     export VOLUMES=&quot;&lt;host dir or filename&gt;:&lt;container dir or filename&gt; 
>
> \$ sudo ./dobsserver.sh start
>
>      $ docker ps
>     1dd1fac2912e        tizendocker:5000/obsserver:2.4.0.7             &quot;/bin/bash /srv/scri   4 hours ago         Up 4 hours         
>      0.0.0.0:80-&gt;80/tcp, 0.0.0.0:82-&gt;82/tcp, 0.0.0.0:443-&gt;443/tcp, 0.0.0.0:444-&gt;444/tcp, 0.0.0.0:5152-&gt;5152/tcp, 
>      0.0.0.0:5252-&gt;5252/tcp, 0.0.0.0:5352-&gt;5352/tcp      obsserver_2.4
>
> Finish
>
> If you use a firewall on host OS, you have to allow a port number.(80
> 81 82 443 444 873 5152 5252 5352)
>
>      $sudo ufw allow 80
>      ... 

Connect OBS
-----------

>     web url : http://localhost:80/ or http:// &lt; ip &gt; /
>     api url : http://localhost:81/ or http:// &lt; ip &gt;:81 /
>     repos url : http://localhost:82/ or http:// &lt; ip &gt;:82 /
>
>     # Admin password
>     Log in = id : Admin , pw : opensuse

Setup OBS Service
-----------------

> If you conncect the download server,jenkins server.
>
>     #  Attach to a running container
>     $ sudo ./dobsserver.sh attach
>
>     &gt; vi /usr/lib/obs/server/BSConfig.pm
>     # 1) Add lines below 
>     our $notification_plugin = &quot;notify_jenkins&quot;;
>     our $jenkinsserver = &quot;Jenkins_Server_IP:8080&quot;; (ex. our $jenkinsserver = &gt;     &quot;http://123.456.789.012:8080&quot;;)
>     our $jenkinsjob = 'job/obs-event-dispatcher/buildWithParameters';
>     our $jenkinsnamespace = &quot;OBS&quot;;
>     our @excl_patterns = (&quot;project:Tizen:.* type:REPO_PUBLISH_STATE&quot;,
>                             &quot;type:BUILD_.*&quot;,
>                             &quot;type:SRCSRV_COMMIT&quot;,
>                             &quot;type:SRCSRV_VERSION_CHANGE&quot;);
>
>     our @incl_patterns = (&quot;project:Tizen:.*&quot;,
>                             &quot;project:home:prerelease:.*&quot;);
>     # You must modify Jenkins_Server_IP as what you use.
>     # Optional : You can modify (add/ remove lists) &quot;our @excl_patterns&quot; &amp; &quot;our &gt;     @incl_patterns&quot;
>     #  : our @excl_patterns -&gt; obs projects which is excluded from snapshot
>     #   :our @incl_patterns -&gt; obs projects which is triggers jenkins to make snapshot
>
>     # 2) Add proxy IP
>     our $proxy = &quot;Proxy_IP&quot;;
>     ex) our $proxy = &quot;http://123.456.789.012/&quot;; 
>
>     # 3) Add information about stage server.
>     our $stageserver = 'rsync://Download_Server_IP/_live_RW_'; 
>     ex) our $stageserver = 'rsync://123.456.789.012/_live_RW_';
>
>     # 4) If you are use the proxy in your enviroment
>     &gt; vi /etc/sysconfig/proxy
>       HTTP_PROXY=
>       HTTPS_PROXY=
>       FTP_PROXY=
>
>     # exit a container
>     &gt; exit
>
>     # restart a container
>     $ sudo ./dobsserver.sh stop
>
>     $ sudo ./dobsserver.sh start&gt;     

Setting up for Gerrit accessing
-------------------------------

>     1. After getting a gerrit account, you need to create an ssh key, 
>     and add your ssh key to Gerrit to enable the connection to gerrit.
>
>     2. Register your contact info on Gerrit
>        Log into Gerrit.
>        On Gerrit UI, follow the links below to register your email address 
>     and update your full name on Gerrit:
>          a.Settings --&gt; Contact Information --&gt; Register New Email...
>          b.Settings --&gt; Contact Information --&gt; Full Name.
>          
>     3. After you register the email, you will receive an email which contains a link. 
>     Please copy the link to your browser to activate the account.
>     Create SSH keys
>
>     $ sudo ./dobsserver.sh attach
>     $  cd /root
>     $ ssh-keygen -f id_rsa -t rsa -N ''
>     Generating public/private rsa key pair.
>     Generating public/private rsa key pair.
>     Your identification has been saved in id_rsa.
>     Your public key has been saved in id_rsa.pub.
>     The key fingerprint is:
>     3a:34:9c:35:7c:58:b1:81:9e:b9:64:3d:27:f7:3e:60 root@OBSServer
>     The key's randomart image is:
>     +--[ RSA 2048]----+
>     | .+. |
>     | ..o o |
>     | .=+o |
>     | . o*o+ o |
>     | =oS. = . |
>     | . o. E . |
>     | o . o |
>     | . o |
>     | . |
>     +-----------------+
>     # cat .ssh/id_rsa.pub
>
>     4. after pressing the Enter key at several prompts, an SSH key-pair will be created in /root/.ssh/id_rsa.pub .
>        Upload SSH pubkey to Gerrit Click the links below to set up the Gerrit WebUI.
>        Settings --&gt; SSH Public Keys --&gt; Add Key...
>        Paste your SSH public key there, and then click 'Add'.
>     5. Verify your SSH connection You can verify your Gerrit connection by executing this command:
>        Make sure to add the server RSA key fingerprint to the known hosts of jenkins account
>        if connect to gerrit server in the first time.
>        If your settings are correct, you'll see the message below. If not, check SSH proxy
>        and SSH public key on Gerrit.
>        $ ssh -p 29418 gerrit_username@gerrit_hostname
>        **** Welcome to Gerrit Code Review ****
>     6. $ vi .ssh/config
>        Host gerrit_hostname
>        Port 29418
>        User gerrit_username
>        IdentityFile ~/.ssh/id_rsa
>     7. Config Git for Gerrit Access After the above installation, which will include git, is complete, you can configure git.
>        $ git config --global user.name &quot;First_Name Last_Name&quot;
>        $ git config --global user.email &quot;account@host&quot;

Initialize
----------

> \#\#\# remove all data\
> \$ sudo ./dobsserver.sh stop\
> \$ sudo rm -rf /home/obsserver\_2.4\
> \$ sudo ./dobsserver.sh rm\
> \$ sudo ./dobsserver.sh start

CLI
---

>     USAGE: ./dobsserver.sh COMMAND
>     -e 
>     Commands:
>         start     Start a stopped container
>         attach    Attach to a running container
>         stop      Stop a running container
>         status    Status a running container
>         rm        Remove this containers
>         restart   stop , start a container
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
>       Known issues
>       This container is not work at a Docker 1.8.1 version.
>       Please use the Docker 1.7.1 version.
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

Back to [Setup of Tizen Infrastructure with Docker](Setup_of_Tizen_Infrastructure_with_Docker "wikilink")
---------------------------------------------------------------------------------------------------------

[Category:Tool](Category:Tool "wikilink")
