###  <big>***Add zypper repositories***</big>

:   Refer to the \"[**OBS 2.5 Zypper
    Repositories**](OBS_2.5_Zypper_Repositories "wikilink")\" page.

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

#### Install BUILD packages

:   Refer to the \"[**Install BUILD
    packages**](OBS_2.5_All-in-One_Server#Install_BUILD_packages "wikilink")\"
    section in the \"[**Install All-in-One
    Server**](OBS_2.5_All-in-One_Server#Install_All-in-One_Server "wikilink")\"
    chapter in the \"[**OBS 2.5 All-in-One
    Server**](OBS_2.5_All-in-One_Server "wikilink")\" page.

\

#### Fix build script bugs

:   Refer to the \"[**Fix build script
    bugs**](OBS_2.5_All-in-One_Server#Fix_build_script_bugs "wikilink")\"
    section in the \"[**Install All-in-One
    Server**](OBS_2.5_All-in-One_Server#Install_All-in-One_Server "wikilink")\"
    chapter in the \"[**OBS 2.5 All-in-One
    Server**](OBS_2.5_All-in-One_Server "wikilink")\" page.

\

#### Install BACKEND packages

:   Refer to the \"[**Install BACKEND
    packages**](OBS_2.4_Distributed_Servers#Install_BACKEND_packages "wikilink")\"
    section in the \"[**Install BACKEND
    Server**](OBS_2.4_Distributed_Servers#Install_BACKEND_Server "wikilink")\"
    chapter in the \"[**OBS 2.4 Distributed
    Servers**](OBS_2.4_Distributed_Servers "wikilink")\" page.

\

#### Install additional packages for dependencies

:   Refer to the \"[**Install additional packages for
    dependencies**](OBS_2.5_All-in-One_Server#Install_additional_packages_for_dependencies "wikilink")\"
    section in the \"[**Install All-in-One
    Server**](OBS_2.5_All-in-One_Server#Install_All-in-One_Server "wikilink")\"
    chapter in the \"[**OBS 2.5 All-in-One
    Server**](OBS_2.5_All-in-One_Server "wikilink")\" page.

\

#### Generate configuration.xml file

:   Refer to the \"[**Generate configuration.xml
    file**](OBS_2.5_All-in-One_Server#Generate_configuration.xml_file "wikilink")\"
    section in the \"[**Install All-in-One
    Server**](OBS_2.5_All-in-One_Server#Install_All-in-One_Server "wikilink")\"
    chapter in the \"[**OBS 2.5 All-in-One
    Server**](OBS_2.5_All-in-One_Server "wikilink")\" page.

\

#### Modify OBS account

:   Refer to the \"[**Modify OBS
    account**](OBS_2.5_All-in-One_Server#Modify_OBS_account "wikilink")\"
    section in the \"[**Install All-in-One
    Server**](OBS_2.5_All-in-One_Server#Install_All-in-One_Server "wikilink")\"
    chapter in the \"[**OBS 2.5 All-in-One
    Server**](OBS_2.5_All-in-One_Server "wikilink")\" page.

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
<font color=red>our \$obsname = \$rep\_host;</font>\
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
<font color=red>our \$noproxy = \"localhost, 127.0.0.1,
<font color=blue>**pilot.tizen.org, build, frontend, front, fe, api,
webui, backend, be, rep, storage, src, db**</font>\";</font>\
\
······\
</font> \|} </span>\

#### Install Apache2 for REPO download

:   Refer to the \"[**Install Apache2 for REPO
    download**](OBS_2.4_Distributed_Servers#Install_Apache2_for_REPO_download "wikilink")\"
    section in the \"[**Install BACKEND
    Server**](OBS_2.4_Distributed_Servers#Install_BACKEND_Server "wikilink")\"
    chapter in the \"[**OBS 2.4 Distributed
    Servers**](OBS_2.4_Distributed_Servers "wikilink")\" page.

\

#### Configure Apache2 for REPO download

:   Refer to the \"[**Configure Apache2 for REPO
    download**](OBS_2.4_Distributed_Servers#Configure_Apache2_for_REPO_download "wikilink")\"
    section in the \"[**Install BACKEND
    Server**](OBS_2.4_Distributed_Servers#Install_BACKEND_Server "wikilink")\"
    chapter in the \"[**OBS 2.4 Distributed
    Servers**](OBS_2.4_Distributed_Servers "wikilink")\" page.

\

#### Set up firewall for BACKEND server

:   Refer to the \"[**Set up firewall for BACKEND
    server**](OBS_2.4_Distributed_Servers#Set_up_firewall_for_BACKEND_server "wikilink")\"
    section in the \"[**Install BACKEND
    Server**](OBS_2.4_Distributed_Servers#Install_BACKEND_Server "wikilink")\"
    chapter in the \"[**OBS 2.4 Distributed
    Servers**](OBS_2.4_Distributed_Servers "wikilink")\" page.

\

#### Register BACKEND services

:   \# chkconfig \--add obsrepserver obsscheduler obsdispatcher
    obspublisher obswarden
:   \# systemctl enable apache2

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

#### Make OBS **events** directory

:   \# mkdir -p <font color=red>**/srv/obs/events**</font>

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

:   Refer to the \"[**Install SOURCE/SERVICE
    packages**](OBS_2.4_Distributed_Servers#Install_SOURCE/SERVICE_packages "wikilink")\"
    section in the \"[**Install STORAGE
    Server**](OBS_2.4_Distributed_Servers#Install_STORAGE_Server "wikilink")\"
    chapter in the \"[**OBS 2.4 Distributed
    Servers**](OBS_2.4_Distributed_Servers "wikilink")\" page.

\

#### Install additional packages for dependencies

:   Refer to the \"[**Install additional packages for
    dependencies**](OBS_2.5_All-in-One_Server#Install_additional_packages_for_dependencies "wikilink")\"
    section in the \"[**Install All-in-One
    Server**](OBS_2.5_All-in-One_Server#Install_All-in-One_Server "wikilink")\"
    chapter in the \"[**OBS 2.5 All-in-One
    Server**](OBS_2.5_All-in-One_Server "wikilink")\" page.

\

#### Modify OBS account

:   Refer to the \"[**Modify OBS
    account**](OBS_2.5_All-in-One_Server#Modify_OBS_account "wikilink")\"
    section in the \"[**Install All-in-One
    Server**](OBS_2.5_All-in-One_Server#Install_All-in-One_Server "wikilink")\"
    chapter in the \"[**OBS 2.5 All-in-One
    Server**](OBS_2.5_All-in-One_Server "wikilink")\" page.

\

#### Set owner of OBS HOME directory <font color=orange>(*if necessary*)</font>

:   Refer to the \"[**Set owner of OBS HOME
    directory**](OBS_2.4_All-in-One_Server#chown_obs_home "wikilink")\"
    section in the \"[**Install All-in-One
    Server**](OBS_2.4_All-in-One_Server#Install_All-in-One_Server "wikilink")\"
    chapter in the \"[**OBS 2.4 All-in-One
    Server**](OBS_2.4_All-in-One_Server "wikilink")\" page.

\

#### Create OBS database

:   Refer to the \"[**Create OBS
    database**](OBS_2.5_All-in-One_Server#Create_OBS_database "wikilink")\"
    section in the \"[**Install All-in-One
    Server**](OBS_2.5_All-in-One_Server#Install_All-in-One_Server "wikilink")\"
    chapter in the \"[**OBS 2.5 All-in-One
    Server**](OBS_2.5_All-in-One_Server "wikilink")\" page.

\

#### Configure OBS services

:   Refer to the \"[**Configure OBS
    services**](OBS_2.4_Distributed_Servers#Configure_OBS_services "wikilink")\"
    section in the \"[**Install STORAGE
    Server**](OBS_2.4_Distributed_Servers#Install_STORAGE_Server "wikilink")\"
    chapter in the \"[**OBS 2.4 Distributed
    Servers**](OBS_2.4_Distributed_Servers "wikilink")\" page.

\

#### Modify *BSConfig.pm* file

:   Refer to the \"[**Modify BSConfig.pm file**](#bsconfig "wikilink")\"
    section in the \"**[Install BACKEND
    Server](#Install_BACKEND_Server "wikilink")**\" chapter.

\

#### Set up firewall for STORAGE server

:   Refer to the \"[**Set up firewall for STORAGE
    server**](OBS_2.4_Distributed_Servers#Set_up_firewall_for_STORAGE_server "wikilink")\"
    section in the \"[**Install BACKEND
    Server**](OBS_2.4_Distributed_Servers#Install_BACKEND_Server "wikilink")\"
    chapter in the \"[**OBS 2.4 Distributed
    Servers**](OBS_2.4_Distributed_Servers "wikilink")\" page.

\

#### Register STORAGE services

:   \# chkconfig \--add mysql obssrcserver obsservice

\

------------------------------------------------------------------------

### <big>***Install FRONTEND Server***</big>

FRONTEND server = WebUI server + API server\
\

#### Install Apache2 for FE

:   Refer to the \"[**Install Apache2 for
    FE**](OBS_2.4_Distributed_Servers#Install_Apache2_for_FE "wikilink")\"
    section in the \"[**Install FRONTEND
    Server**](OBS_2.4_Distributed_Servers#Install_FRONTEND_Server "wikilink")\"
    chapter in the \"[**OBS 2.4 Distributed
    Servers**](OBS_2.4_Distributed_Servers "wikilink")\" page.

\

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

\

#### Install additional packages for dependencies

:   Refer to the \"[**Install additional packages for
    dependencies**](OBS_2.5_All-in-One_Server#Install_additional_packages_for_dependencies "wikilink")\"
    section in the \"[**Install All-in-One
    Server**](OBS_2.5_All-in-One_Server#Install_All-in-One_Server "wikilink")\"
    chapter in the \"[**OBS 2.5 All-in-One
    Server**](OBS_2.5_All-in-One_Server "wikilink")\" page.

\

#### Configure API database.yml file

:   \# vi /srv/www/obs/api/config/database.yml
:   {\| width=\"1000px\" border=\"0\" style=\"margin:0;
    background:\#f2f2f2; font-family:Consolas,Monaco,Monospace;\"

\|- \| <font color=green> ······\
production:\
  adapter: mysql2\
  database: api\_production\
  <font color=red>host:
\"<font color=blue>**zzz.zzz.zzz.zzz**</font>\"</font>   
<font color=blue>*\#\# The hostname of the MySQL server for OBS*</font>\
  <font color=red>port: \'<font color=blue>**3306**</font>\'</font>   
<font color=blue>*\#\# The port number of the MySQL service in the MySQL
server*</font>\
  username: ~~root~~<font color=red>**obs**</font>   
<font color=blue>*\#\# The user name in the step of \"[Create OBS
database](OBS_2.5_All-in-One_Server#Create_OBS_database "wikilink")\"*</font>\
  password: ~~opensuse~~<font color=red>**obspassword**</font>   
<font color=blue>*\#\# The password in the step of \"[Create OBS
database](OBS_2.5_All-in-One_Server#Create_OBS_database "wikilink")\"*</font>\
  encoding: utf8\
······\
</font> \|}\

#### Populate API production database

:   Refer to the \"[**Populate API production
    database**](OBS_2.5_All-in-One_Server#Populate_API_production_database "wikilink")\"
    section in the \"[**Install All-in-One
    Server**](OBS_2.5_All-in-One_Server#Install_All-in-One_Server "wikilink")\"
    chapter in the \"[**OBS 2.5 All-in-One
    Server**](OBS_2.5_All-in-One_Server "wikilink")\" page.

\

#### Configure API options.yml file

:   \# vi /srv/www/obs/api/config/options.yml
:   {\| width=\"1000px\" border=\"0\" style=\"margin:0;
    background:\#f2f2f2; font-family:Consolas,Monaco,Monospace;\"

\|- \| <font color=green> ······\
<font color=red>\#</font>use\_xforward: true\
<font color=red>use\_xforward: true</font>\
\
······\
<font color=red>\#</font>source\_host: localhost\
<font color=red>source\_host:
\"<font color=blue>**zzz.zzz.zzz.zzz**</font>\"</font>   
<font color=blue>*\#\# The hostname or the IP address of the SRC
server*</font>\
source\_port: 5352\
<font color=red>\#</font>source\_protocol: https\
<font color=red>source\_protocol: http</font>\
\
······\
<font color=red>\#</font>frontend\_host: localhost\
<font color=red>frontend\_host:
\"<font color=blue>**xxx.xxx.xxx.xxx**</font>\"</font>   
<font color=blue>*\#\# The hostname or the IP address of the API
(FRONTEND) server*</font>\
<font color=red>\#</font>frontend\_port: 443\
<font color=red>frontend\_port: 80</font>    <font color=blue>*\#\# **If
HTTP must be used** for OBS API service **instead of HTTPS**, the port
number for API must be 80.*</font>\
<font color=red>\#</font>frontend\_protocol: https\
<font color=red>frontend\_protocol: http</font>\
······\
</font> \|}\

#### Configure Apache2 for FE

    **Edit /etc/sysconfig/apache2 file**

:   Refer to the \"[Edit /etc/sysconfig/apache2
    file](OBS_2.5_All-in-One_Server#setup_syscfg_apache2 "wikilink")\"
    subsection in the \"[Configure
    Apache2](OBS_2.5_All-in-One_Server#Configure_Apache2 "wikilink")\"
    section in the \"[Install All-in-One
    Server](OBS_2.5_All-in-One_Server#Install_All-in-One_Server "wikilink")\"
    chapter in the \"[OBS 2.5 All-in-One
    Server](OBS_2.5_All-in-One_Server "wikilink")\" page.

\
    **Generate SSL certificate** <font color=red>***(only if HTTPS is
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

#### Configure virtual hosts for FE

:   \# vi /etc/apache2/vhosts.d/obs.conf
:   {\| width=\"1000px\" border=\"0\" style=\"margin:0;
    background:\#f2f2f2; font-family:Consolas,Monaco,Monospace;\"

\|- \| <font color=green> <font color=red>Listen 80</font>\
<font color=grey>*Listen 443*</font>\
<font color=red>\#</font>Listen 82\
······\
\
······\
<font color=blue>*\#\# Comment out or remove this block.*</font>\
<font color=red>\#</font>\<VirtualHost \*:80\>\
<font color=red>\#</font>    ······\
<font color=red>\#</font></VirtualHost>\
\
······\
<font color=blue>*\#\# Comment out or remove this block.*</font>\
<font color=red>\#</font>\<VirtualHost \*:82\>\
<font color=red>\#</font>    ······\
<font color=red>\#</font></VirtualHost>\
\
······\
<font color=blue>*\#\# Comment out this block **if HTTPS is NOT
used**.*</font>\
<font color=red>\#</font>\<VirtualHost \*:443\>\
<font color=red>\#</font>    ······\
<font color=red>\#</font></VirtualHost>\
</font>\
<font color=red> <font color=red>\# OBS WEBUI & API without SSL</font>\
\<VirtualHost \*:80\>\
    ServerName api\
\
    DocumentRoot \"/srv/www/obs/api/public\"\
    ErrorLog /srv/www/obs/api/log/apache\_error\_log\
    TransferLog /srv/www/obs/api/log/apache\_access\_log\
\
    PassengerMinInstances 2\
    PassengerPreStart http://api\
\
    <Directory /srv/www/obs/api/public>\
        AllowOverride all\
        Options -MultiViews\
        XForward on\
        Allow from all\
    </Directory>\
</VirtualHost>\
</font> \|}\

#### Change owner/group of API directories

:   \# chown -R wwwrun:www /srv/www/obs/api

\

#### Set up firewall

    **Add TCP ports for FRONTEND server**

:   YaST \--\> Security and Users \--\> Firewall \--\> Allowed Services
    \--\> Advanced\... \--\> TCP Ports
:   {\| width=\"1000px\" border=\"0\" style=\"margin:0;
    background:\#f2f2f2; font-family:Consolas,Monaco,Monospace;\"

\|- \| <font color=red> 80 <font color=grey>*443*</font> </font> \|}

:   <font color=red>† *\"443\" port should be enabled only if it is
    used.*</font>\

\

#### Register FRONTEND services

:   \# chkconfig \--add memcached obsapidelayed
:   \# systemctl enable apache2

\

------------------------------------------------------------------------

### <big>***Reboot OBS Servers***</big>

<big>

<li>

Reboot BACKEND server

<li>

Reboot STORAGE server

<li>

Reboot FRONTEND server </big>

</ol>

\

------------------------------------------------------------------------

### <big>***Install Workers***</big>

Refer to the \"[**Install
Workers**](OBS_2.4_All-in-One_Server#Install_Workers "wikilink")\"
chapter in the \"[**OBS 2.4 All-in-One
Server**](OBS_2.4_All-in-One_Server "wikilink")\" page.\
\

[Category:Tool](Category:Tool "wikilink")
