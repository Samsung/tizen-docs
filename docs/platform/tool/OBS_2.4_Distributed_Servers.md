###  <big>***Add zypper repositories***</big>

:   Refer to the \"[**OBS 2.4 Zypper
    Repositories**](OBS_2.4_Zypper_Repositories "wikilink")\" page.

\

------------------------------------------------------------------------

### <big>***Install BACKEND Server***</big>

BACKEND server = REPO server + SCHEDULER + DISPATCHER + PUBLISHER +
WARDEN\
\

#### Make HOME directory for OBS <font color=orange>(*if necessary*)</font>

:   Refer to the \"[**Make a HOME directory for
    OBS**](OBS_2.4_All-in-One_Server#make_obs_home "wikilink")\" section
    in the \"[**Install All-in-One
    Server**](OBS_2.4_All-in-One_Server#Install_All-in-One_Server "wikilink")\"
    chapter in the \"[**OBS 2.4 All-in-One
    Server**](OBS_2.4_All-in-One_Server "wikilink")\" page.

\

#### Make repository directory

:   Refer to the \"[**Make repository
    directory**](OBS_2.4_All-in-One_Server#make_repos_dir "wikilink")\"
    section in the \"[**Install All-in-One
    Server**](OBS_2.4_All-in-One_Server#Install_All-in-One_Server "wikilink")\"
    chapter in the \"[**OBS 2.4 All-in-One
    Server**](OBS_2.4_All-in-One_Server "wikilink")\" page.

\

#### Install BACKEND packages

:   \# zypper install obs-server
:   \# zypper install obs-utils

\

#### Install BUILD packages

:   Refer to the \"[**Install BUILD
    packages**](OBS_2.4_All-in-One_Server#Install_BUILD_packages "wikilink")\"
    section in the \"[**Install All-in-One
    Server**](OBS_2.4_All-in-One_Server#Install_All-in-One_Server "wikilink")\"
    chapter in the \"[**OBS 2.4 All-in-One
    Server**](OBS_2.4_All-in-One_Server "wikilink")\" page.

\

#### Modify OBS account

:   Refer to the \"[**Modify OBS
    account**](OBS_2.4_All-in-One_Server#Modify_OBS_account "wikilink")\"
    section in the \"[**Install All-in-One
    Server**](OBS_2.4_All-in-One_Server#Install_All-in-One_Server "wikilink")\"
    chapter in the \"[**OBS 2.4 All-in-One
    Server**](OBS_2.4_All-in-One_Server "wikilink")\" page.

\

#### Set owner of OBS HOME directory <font color=orange>(*if necessary*)</font>

:   Refer to the \"[**Set owner of OBS HOME
    directory**](OBS_2.4_All-in-One_Server#chown_obs_home "wikilink")\"
    section in the \"[**Install All-in-One
    Server**](OBS_2.4_All-in-One_Server#Install_All-in-One_Server "wikilink")\"
    chapter in the \"[**OBS 2.4 All-in-One
    Server**](OBS_2.4_All-in-One_Server "wikilink")\" page.

\
<span id="bsconfig">

#### Modify *BSConfig.pm* file

:   \# vi /usr/lib/obs/server/BSConfig.pm
:   {\| width=\"1000px\" border=\"0\" style=\"margin:0;
    background:\#f2f2f2; font-family:Consolas,Monaco,Monospace;\"

\|- \| <font color=green> my \$frontend = undef; \# FQDN of the
WebUI/API server if it\'s not \$hostname\
<font color=red> my \$api\_host =
\"<font color=blue>**xxx.xxx.xxx.xxx**</font>\";   
<font color=blue>*\#\# FQDN, IP address, or short hostname of the API
(FRONTEND) server*</font>\
my \$rep\_host = \"<font color=blue>**yyy.yyy.yyy.yyy**</font>\";   
<font color=blue>*\#\# FQDN, IP address, or short hostname of the REPO
(BACKEND) server*</font>\
my \$src\_host = \"<font color=blue>**zzz.zzz.zzz.zzz**</font>\";   
<font color=blue>*\#\# FQDN, IP address, or short hostname of the SRC
(STORAGE) server*</font>\
my \$api\_ip = quotemeta inet\_ntoa(inet\_aton(\$api\_host));\
my \$rep\_ip = quotemeta inet\_ntoa(inet\_aton(\$rep\_host));\
my \$src\_ip = quotemeta inet\_ntoa(inet\_aton(\$src\_host));\
</font>\
······\
\
our \$ipaccess = {\
   \'127\\..\*\' =\> \'rw\', \# only the localhost can write to the
backend\
   \"\^\$ip\" =\> \'rw\', \# Permit IP of FQDN\
<font color=red>    \"\^\$api\_ip\" =\> \'rw\', \# Permit IP of API
server\
   \"\^\$rep\_ip\" =\> \'rw\', \# Permit IP of REPO server\
   \"\^\$src\_ip\" =\> \'rw\', \# Permit IP of SRC server\
</font>    \'.\*\' =\> \'worker\', \# build results can be delivered
from any client in the network\
};\
\
······\
\
<font color=red>\#</font>our \$obsname = \$hostname; \# unique
identifier for this Build Service instance\
<font color=red>our \$obsname = \$rep\_host;\
</font>\
······\
\
<font color=red>\#</font>our \$srcserver = \"http://\$hostname:5352\";\
<font color=red>our \$srcserver = \"http://\$src\_host:5352\";\
</font> <font color=red>\#</font>our \$reposerver =
\"http://\$hostname:5252\";\
<font color=red>our \$reposerver = \"http://\$rep\_host:5252\";\
</font> <font color=red>\#</font>our \$serviceserver =
\"http://\$hostname:5152\";\
<font color=red>our \$serviceserver = \"http://\$src\_host:5152\";\
</font>\
······\
\
<font color=red>\#</font>our \$repodownload =
\"http://\$hostname/repositories\";\
<font color=red>our \$repodownload = \"http://\$rep\_host:82\";</font>\
\
······\
\
<font color=red>\#</font>our \@reposervers =
(\"http://\$hostname:5252\");\
<font color=red>our \@reposervers = (\"http://\$rep\_host:5252\");\
</font>\
······\
\
\#our \$noproxy = \"localhost, 127.0.0.1\";\
<font color=blue>*\#\# Domains, FQDNs, IP addresses, short
hostnames*</font>\
<font color=red>our \$noproxy = =\"localhost, 127.0.0.1,
<font color=blue>**pilot.tizen.org, build, frontend, front, fe, api,
webui, backend, be, rep, storage, src, db**</font>\";</font>\
\
······\
</font> \|} </span>\

#### Install Apache2 for REPO download

    **Install Apache2**

:   \# zypper install apache2

\
    **Set up *server name* for apache2 service**

:   \# vi /etc/sysconfig/apache2
:   {\| width=\"1000px\" border=\"0\" style=\"margin:0;
    background:\#f2f2f2; font-family:Consolas,Monaco,Monospace;\"

\|- \| <font color=green> ······\
APACHE\_SERVERNAME=\"<font color=blue>**yyy.yyy.yyy.yyy**</font>\"   
<font color=blue>*\#\# FQDN, IP address, or short hostname of the REPO
(BACKEND) server*</font>\
······\
</font> \|}\

#### Configure Apache2 for REPO download

    **Edit httpd.conf file**

:   Refer to the \"[**Edit httpd.conf
    file**](OBS_2.4_All-in-One_Server#httpd_conf "wikilink")\"
    subsection in the \"[**Set up Apache2 for
    WebUI**](OBS_2.4_All-in-One_Server#Set_up_Apache2_for_WebUI "wikilink")\"
    section in the \"[**Install All-in-One
    Server**](OBS_2.4_All-in-One_Server#Install_All-in-One_Server "wikilink")\"
    chapter in the \"[**OBS 2.4 All-in-One
    Server**](OBS_2.4_All-in-One_Server "wikilink")\" page.

\
    **Edit obs.conf file**

:   \# vi /etc/apache2/vhosts.d/obs.conf
:   {\| width=\"1000px\" border=\"0\" style=\"margin:0;
    background:\#f2f2f2; font-family:Consolas,Monaco,Monospace;\"

\|- \|

    Listen 82

    # Build Results
    <VirtualHost *:82>
        ServerName rep

        # The resulting repositories
        DocumentRoot "/srv/obs/repos"

        <Directory /srv>
            Options FollowSymLinks
        </Directory>

        <Directory /srv/obs/repos>
            Options Indexes FollowSymLinks
            Allow from all
        </Directory>
    </VirtualHost>

\|}\

#### Set up firewall for BACKEND server

    **Add TCP ports for BACKEND server**

:   YaST \--\> Security and Users \--\> Firewall \--\> Allowed Services
    \--\> Advanced\... \--\> TCP Ports
:   {\| width=\"1000px\" border=\"0\" style=\"margin:0;
    background:\#f2f2f2; font-family:Consolas,Monaco,Monospace;\"

\|- \| <font color=red> 5252 82 </font> \|}\

#### Start BACKEND services

:   \# systemctl start obsrepserver obsscheduler obsdispatcher
    obspublisher obswarden apache2

\

#### Test BACKEND server installation

:   Browse to ***<font color=blue>http://yyy.yyy.yyy.yyy:82</font>***
    with your web browser (yyy.yyy.yyy.yyy = FQDN or IP address of the
    REPO server)

\

#### Register BACKEND services

:   \# chkconfig \--add obsrepserver obsscheduler obsdispatcher
    obspublisher obswarden apache2

\

------------------------------------------------------------------------

### <big>***Install STORAGE Server***</big>

STORAGE server = SOURCE server + SERVICE server + MySQL server\
\

#### Make HOME directory for OBS <font color=orange>(*if necessary*)</font>

:   Refer to the \"[**Make a HOME directory for
    OBS**](OBS_2.4_All-in-One_Server#make_obs_home "wikilink")\" section
    in the \"[**Install All-in-One
    Server**](OBS_2.4_All-in-One_Server#Install_All-in-One_Server "wikilink")\"
    chapter in the \"[**OBS 2.4 All-in-One
    Server**](OBS_2.4_All-in-One_Server "wikilink")\" page.

\

#### Install MySQL (MariaDB)

:   Refer to the \"[**Install MySQL
    (MariaDB)**](OBS_2.4_All-in-One_Server#Install_MySQL_(MariaDB) "wikilink")\"
    section in the \"[**Install All-in-One
    Server**](OBS_2.4_All-in-One_Server#Install_All-in-One_Server "wikilink")\"
    chapter in the \"[**OBS 2.4 All-in-One
    Server**](OBS_2.4_All-in-One_Server "wikilink")\" page.

\

#### Install SOURCE/SERVICE packages

    **Install OBS packages**

:   \# zypper install obs-server
:   \# zypper install obs-utils
:   \# zypper install obs-source\_service obs-service-download\_files
    obs-service-tar\_scm

\
    **Install GBS service packages (for only Tizen)**

:   \# zypper install obs-service-gbs obs-service-git-buildpackage
:   \# zypper install librpm-tizen

\

#### Configure OBS services

:   Refer to the \"[**Configure OBS
    services**](OBS_2.4_All-in-One_Server#Configure_OBS_services "wikilink")\"
    section in the \"[**Install All-in-One
    Server**](OBS_2.4_All-in-One_Server#Install_All-in-One_Server "wikilink")\"
    chapter in the \"[**OBS 2.4 All-in-One
    Server**](OBS_2.4_All-in-One_Server "wikilink")\" page.

\

#### Modify OBS account

:   Refer to the \"[**Modify OBS
    account**](OBS_2.4_All-in-One_Server#Modify_OBS_account "wikilink")\"
    section in the \"[**Install All-in-One
    Server**](OBS_2.4_All-in-One_Server#Install_All-in-One_Server "wikilink")\"
    chapter in the \"[**OBS 2.4 All-in-One
    Server**](OBS_2.4_All-in-One_Server "wikilink")\" page.

\

#### Set owner of OBS HOME directory <font color=orange>(*if necessary*)</font>

:   Refer to the \"[**Set owner of OBS HOME
    directory**](OBS_2.4_All-in-One_Server#chown_obs_home "wikilink")\"
    section in the \"[**Install All-in-One
    Server**](OBS_2.4_All-in-One_Server#Install_All-in-One_Server "wikilink")\"
    chapter in the \"[**OBS 2.4 All-in-One
    Server**](OBS_2.4_All-in-One_Server "wikilink")\" page.

\

#### Create OBS databases

:   Refer to the \"**[Create OBS
    databases](OBS_2.4_All-in-One_Server#Create_OBS_databases "wikilink")**\"
    section in the \"[**Install All-in-One
    Server**](OBS_2.4_All-in-One_Server#Install_All-in-One_Server "wikilink")\"
    chapter in the \"[**OBS 2.4 All-in-One
    Server**](OBS_2.4_All-in-One_Server "wikilink")\" page.

\

#### Modify *BSConfig.pm* file

:   Refer to the \"[**Modify BSConfig.pm file**](#bsconfig "wikilink")\"
    section in the \"**[Install BACKEND
    Server](#Install_BACKEND_Server "wikilink")**\" chapter.

\

#### Set up firewall for STORAGE server

    **Add TCP ports for STORAGE server**

:   YaST \--\> Security and Users \--\> Firewall \--\> Allowed Services
    \--\> Advanced\... \--\> TCP Ports
:   {\| width=\"1000px\" border=\"0\" style=\"margin:0;
    background:\#f2f2f2; font-family:Consolas,Monaco,Monospace;\"

\|- \| <font color=red> 3306 5152 5352\
</font> \|}\

#### Start STORAGE services

:   \# systemctl start obssrcserver obsservice

\

#### Register STORAGE services

:   \# chkconfig \--add mysql obssrcserver obsservice

\

------------------------------------------------------------------------

### <big>***Install FRONTEND Server***</big>

FRONTEND server = WebUI server + API server\
\

#### Install Apache2 for FE

    **Install apache2 package**

:   \# zypper install apache2

\
    **Set up *server name* for apache2 service**

:   \# vi /etc/sysconfig/apache2
:   {\| width=\"1000px\" border=\"0\" style=\"margin:0;
    background:\#f2f2f2; font-family:Consolas,Monaco,Monospace;\"

\|- \| <font color=green> ······\
APACHE\_SERVERNAME=\"<font color=blue>**xxx.xxx.xxx.xxx**</font>\"   
<font color=blue>*\#\# FQDN, IP address, or short hostname of the WebUI
(FRONTEND) server*</font>\
······\
</font> \|}\

#### Install PHP5

:   Refer to the \"[**Install
    PHP5**](OBS_2.4_All-in-One_Server#Install_PHP5 "wikilink")\" section
    in the \"[**Install All-in-One
    Server**](OBS_2.4_All-in-One_Server#Install_All-in-One_Server "wikilink")\"
    chapter in the \"[**OBS 2.4 All-in-One
    Server**](OBS_2.4_All-in-One_Server "wikilink")\" page.

\

#### Install FRONTEND packages

:   \# zypper install obs-api
:   \# zypper install obs-utils
:   \# zypper install perl-GD

\

#### Configure {api,webui} database.yml files

    **API**

:   \# vi /srv/www/obs/api/config/database.yml
:   {\| width=\"1000px\" border=\"0\" style=\"margin:0;
    background:\#f2f2f2; font-family:Consolas,Monaco,Monospace;\"

\|- \| <font color=green> ······\
production:\
  adapter: mysql2\
  database: api\_production\
  <font color=red>host:
<font color=blue>**zzz.zzz.zzz.zzz**</font></font>   
<font color=blue>*\#\# The hostname of the MySQL server for OBS*</font>\
  <font color=red>port: <font color=blue>**3306**</font></font>   
<font color=blue>*\#\# The port number of the MySQL service in the MySQL
server*</font>\
  username: ~~root~~<font color=red>**obs**</font>   
<font color=blue>*\#\# The user name in the step of \"[Create OBS
databases](OBS_2.4_All-in-One_Server#Create_OBS_databases "wikilink")\"*</font>\
  password: ~~opensuse~~<font color=red>**obspassword**</font>   
<font color=blue>*\#\# The password in the step of \"[Create OBS
databases](OBS_2.4_All-in-One_Server#Create_OBS_databases "wikilink")\"*</font>\
  encoding: utf8\
······\
</font> \|}\
    **WebUI**

:   \# vi /srv/www/obs/webui/config/database.yml
:   {\| width=\"1000px\" border=\"0\" style=\"margin:0;
    background:\#f2f2f2; font-family:Consolas,Monaco,Monospace;\"

\|- \| <font color=green> ······\
production:\
  adapter: mysql2\
  database: webui\_production\
  <font color=red>host:
<font color=blue>**zzz.zzz.zzz.zzz**</font></font>   
<font color=blue>*\#\# The hostname of the MySQL server for OBS*</font>\
  <font color=red>port: <font color=blue>**3306**</font></font>   
<font color=blue>*\#\# The port number of the MySQL service in the MySQL
server*</font>\
  username: ~~root~~<font color=red>**obs**</font>   
<font color=blue>*\#\# The user name in the step of \"[Create OBS
databases](OBS_2.4_All-in-One_Server#Create_OBS_databases "wikilink")\"*</font>\
  password: ~~opensuse~~<font color=red>**obspassword**</font>   
<font color=blue>*\#\# The password in the step of \"[Create OBS
databases](OBS_2.4_All-in-One_Server#Create_OBS_databases "wikilink")\"*</font>\
  encoding: utf8\
······\
</font> \|}\

#### Populate {api,webui}\_production databases

:   Refer to the \"[**Populate {api,webui}\_production
    databases**](OBS_2.4_All-in-One_Server#populate_obs_db "wikilink")\"
    section in the \"[**Install All-in-One
    Server**](OBS_2.4_All-in-One_Server#Install_All-in-One_Server "wikilink")\"
    chapter in the \"[**OBS 2.4 All-in-One
    Server**](OBS_2.4_All-in-One_Server "wikilink")\" page.

\

#### Configure {api,webui} options.yml files

    **API**

:   \# vi /srv/www/obs/api/config/options.yml
:   {\| width=\"1000px\" border=\"0\" style=\"margin:0;
    background:\#f2f2f2; font-family:Consolas,Monaco,Monospace;\"

\|- \| <font color=green> ······\
<font color=red>\#</font>use\_xforward: true\
<font color=red>use\_xforward: true</font>\
······\
<font color=red>\#</font>source\_host: localhost\
<font color=red>source\_host:
\"<font color=blue>**zzz.zzz.zzz.zzz**</font>\"</font>   
<font color=blue>*\#\# The hostname or the IP address of the SRC
server*</font>\
······\
<font color=red>\#</font>download\_url: http://localhost:82/\
<font color=red>download\_url:
<http://><font color=blue>**yyy.yyy.yyy.yyy**</font>:82/</font>   
<font color=blue>*\#\# The hostname or the IP address of the REPO
server*</font>\
······\
</font> \|}\
    **WebUI**

:   \# vi /srv/www/obs/webui/config/options.yml
:   {\| width=\"1000px\" border=\"0\" style=\"margin:0;
    background:\#f2f2f2; font-family:Consolas,Monaco,Monospace;\"

\|- \| <font color=green> ······\
<font color=red>\#</font>download\_url: http://myhost:82/\
<font color=red>download\_url:
<http://><font color=blue>**yyy.yyy.yyy.yyy**</font>:82/</font>   
<font color=blue>*\#\# The hostname or the IP address of the REPO
server*</font>\
······\
<font color=red>\#</font>use\_xforward: true\
<font color=red>use\_xforward: true</font>\
······\
<font color=red>\#</font>frontend\_host: api.opensuse.org\
<font color=red>frontend\_host:
\"<font color=blue>**xxx.xxx.xxx.xxx**</font>\"</font>   
<font color=blue>*\#\# The hostname or the IP address of the API
(FRONTEND) server*</font>\
······\
<font color=blue>*\#\# **If the HTTP protocol must be used** for OBS API
service **instead of HTTPS**, the port number for API should be
81.*</font>\
<font color=red>\#</font>frontend\_port: 443\
<font color=red>frontend\_port: 81</font>\
<font color=red>\#</font>frontend\_protocol: https\
<font color=red>frontend\_protocol: http</font>\
······\
</font> \|}\

#### Configure Apache2 for FE

    **Edit /etc/sysconfig/apache2 file**

:   Refer to the \"[Edit /etc/sysconfig/apache2
    file](OBS_2.4_All-in-One_Server#setup_syscfg_apache2 "wikilink")\"
    subsection in the \"[Configure
    Apache2](OBS_2.4_All-in-One_Server#Configure_Apache2 "wikilink")\"
    section in the \"[Install All-in-One
    Server](OBS_2.4_All-in-One_Server#Install_All-in-One_Server "wikilink")\"
    chapter in the \"[OBS 2.4 All-in-One
    Server](OBS_2.4_All-in-One_Server "wikilink")\" page.

\
    **Generate SSL certificate** <font color=red>***(if HTTPS is
used)***</font>

:   Refer to the \"[Generate SSL certificate
    \...](OBS_2.4_All-in-One_Server#gen_ssl_cert "wikilink")\"
    subsection in the \"[Configure
    Apache2](OBS_2.4_All-in-One_Server#Configure_Apache2 "wikilink")\"
    section in the \"[Install All-in-One
    Server](OBS_2.4_All-in-One_Server#Install_All-in-One_Server "wikilink")\"
    chapter in the \"[OBS 2.4 All-in-One
    Server](OBS_2.4_All-in-One_Server "wikilink")\" page.

\
    **Edit httpd.conf file**

:   Refer to the \"[Edit httpd.conf
    file](OBS_2.4_All-in-One_Server#httpd_conf "wikilink")\" subsection
    in the \"[Configure
    Apache2](OBS_2.4_All-in-One_Server#Configure_Apache2 "wikilink")\"
    section in the \"[Install All-in-One
    Server](OBS_2.4_All-in-One_Server#Install_All-in-One_Server "wikilink")\"
    chapter in the \"[OBS 2.4 All-in-One
    Server](OBS_2.4_All-in-One_Server "wikilink")\" page.

\

#### Configure virtual hosts for Web UI and API

:   \# vi /etc/apache2/vhosts.d/obs.conf
:   {\| width=\"1000px\" border=\"0\" style=\"margin:0;
    background:\#f2f2f2; font-family:Consolas,Monaco,Monospace;\"

\|- \| <font color=red>Listen 80</font>\
<font color=red>Listen 81</font>\
~~<font color=green>Listen 82</font>~~\
<font color=grey>*Listen 443*</font>\
<font color=grey>*Listen 444*</font>\
\
<font color=green> ······\
\
~~\<VirtualHost \*:80\>\
    \# just give an overview about this OBS instance via static web
page\
    DocumentRoot \"/srv/www/obs/overview\"\
\
    <Directory /srv/www/obs/overview>\
        Options Indexes\
        Allow from all\
    </Directory>\
</VirtualHost>\
~~\
~~\<VirtualHost \*:82\>\
    \# The resulting repositories\
    DocumentRoot \"/srv/obs/repos\"\
\
    <Directory /srv/obs/repos>\
        Options Indexes FollowSymLinks\
        Allow from all\
    </Directory>\
</VirtualHost>\
~~ </font>\
<font color=red> <font color=blue>\# OBS WEB interface</font>\
\<VirtualHost \*:80\>\
    ServerName webui\
\
    DocumentRoot \"/srv/www/obs/webui/public\"\
    ErrorLog /srv/www/obs/webui/log/apache\_error\_log\
    TransferLog /srv/www/obs/webui/log/apache\_access\_log\
\
    PassengerPreStart http://build\
\
    <Directory /srv/www/obs/webui/public>\
        AllowOverride all\
        Options -MultiViews +FollowSymLinks\
        XForward on\
        Allow from all\
    </Directory>\
</VirtualHost>\
\
<font color=blue>\# OBS API</font>\
\<VirtualHost \*:81\>\
    ServerName api\
\
    DocumentRoot \"/srv/www/obs/api/public\"\
    ErrorLog /srv/www/obs/api/log/apache\_error\_log\
    TransferLog /srv/www/obs/api/log/apache\_access\_log\
\
    PassengerMinInstances 2\
    PassengerPreStart http://api:81\
\
    <Directory /srv/www/obs/api/public>\
        AllowOverride all\
        Options -MultiViews\
        XForward on\
        Allow from all\
    </Directory>\
</VirtualHost>\
\|}\

#### Change owner/group of {api,webui} directories

:   \# chown -R wwwrun:www /srv/www/obs/{api,webui}

\

#### Set up firewall for FRONTEND server

    **Add TCP ports for FRONTEND server**

:   YaST \--\> Security and Users \--\> Firewall \--\> Allowed Services
    \--\> Advanced\... \--\> TCP Ports
:   {\| width=\"1000px\" border=\"0\" style=\"margin:0;
    background:\#f2f2f2; font-family:Consolas,Monaco,Monospace;\"

\|- \| <font color=red> 80 81 <font color=grey>*443 444*</font>\
</font> \|}

:   <font color=red>† *\"443 444\" ports should be enabled only if it is
    used.*</font>\

\

#### Start FRONTEND services

:   \# systemctl start apache2 memcached obsapidelayed

\

#### Test FRONTEND server installation

:   Refer to the \"**[Test OBS server
    installation](OBS_2.4_All-in-One_Server#test_fe "wikilink")**\"
    section in the \"**[Install All-in-One
    Server](OBS_2.4_All-in-One_Server#Install_All-in-One_Server "wikilink")**\"
    chapter in the \"**[OBS 2.4 All-in-One
    Server](OBS_2.4_All-in-One_Server "wikilink")**\" page.

\

#### Register FRONTEND services

:   \# chkconfig \--add apache2 memcached obsapidelayed

\

------------------------------------------------------------------------

### <big>***Install Workers***</big>

Refer to the \"[**Install
Workers**](OBS_2.4_All-in-One_Server#Install_Workers "wikilink")\"
chapter in the \"[**OBS 2.4 All-in-One
Server**](OBS_2.4_All-in-One_Server "wikilink")\" page.\
\

[Category:Tool](Category:Tool "wikilink")
