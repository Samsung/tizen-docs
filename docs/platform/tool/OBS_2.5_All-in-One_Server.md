###  <big>***Add zypper repositories***</big>

:   Refer to the \"[**OBS 2.5 Zypper
    Repositories**](OBS_2.5_Zypper_Repositories "wikilink")\" page.

\

------------------------------------------------------------------------

### <big>***Install All-in-One Server***</big>

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

#### Install MySQL (MariaDB)

:   Refer to the \"[**Install MySQL
    (MariaDB)**](OBS_2.4_All-in-One_Server#Install_MySQL_(MariaDB) "wikilink")\"
    section in the \"[**Install All-in-One
    Server**](OBS_2.4_All-in-One_Server#Install_All-in-One_Server "wikilink")\"
    chapter in the \"[**OBS 2.4 All-in-One
    Server**](OBS_2.4_All-in-One_Server "wikilink")\" page.

\

#### Install Apache2

:   Refer to the \"[**Install
    Apache2**](OBS_2.4_All-in-One_Server#Install_Apache2 "wikilink")\"
    section in the \"[**Install All-in-One
    Server**](OBS_2.4_All-in-One_Server#Install_All-in-One_Server "wikilink")\"
    chapter in the \"[**OBS 2.4 All-in-One
    Server**](OBS_2.4_All-in-One_Server "wikilink")\" page.

\

#### Install PHP5

:   Refer to the \"[**Install
    PHP5**](OBS_2.4_All-in-One_Server#Install_PHP5 "wikilink")\" section
    in the \"[**Install All-in-One
    Server**](OBS_2.4_All-in-One_Server#Install_All-in-One_Server "wikilink")\"
    chapter in the \"[**OBS 2.4 All-in-One
    Server**](OBS_2.4_All-in-One_Server "wikilink")\" page.

\

#### Install BUILD packages

:   <font color=red>\# zypper remove -u build build-mkbaselibs
    build-mkdrpms build-initvm-x86\_64 build-initvm-i586</font>
:   \# zypper install build-20140424-1.1 build-mkbaselibs-20140424-1.1
    build-mkdrpms-20140424-1.1
:   \# zypper install build-initvm-x86\_64-20140424-1.1
    build-initvm-i586-20131112-7.1
:   <font color=grey>(\# zypper install build-initvm-x86\_64
    build-initvm-i586)</font>
:   <font color=red>† *The latest build package
    (build-20150115-4.1.noarch) from
    \"http://download.opensuse.org/update/13.1\" makes ARM build in OBS
    very slow.*</font>

\

#### Fix build script bugs

:   \# vi /usr/lib/build/qemu-reg
:   {\| width=\"1000px\" border=\"0\" style=\"margin:0;
    background:\#f2f2f2; font-family:Consolas,Monaco,Monospace;\"

\|- \| <font color=green> ······\
<font color=red>\#</font>:aarch64:M::\\x7fELF\\x02\\x01\\x01\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x02\\x00\\xb7:\\xff\\xff\\xff\\xff\\xff\\xff\\xff\\x00\\xff\\xff\\xff\\xff\\xff\\xff\\xff\\xff\\xfe\\xff\\xff:/usr/bin/qemu-aarch64-binfmt:P\
:aarch64:M::\\x7fELF\\x02\\x01\\x01\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x02\\x00\\xb7:\\xff\\xff\\xff\\xff\\xff\\xff\\xff\\x00\\xff\\xff\\xff\\xff\\xff\\xff\\xff\\xff\\xfe\\xff\\xff:/usr/bin/qemu-arm64-binfmt:P\
······\
</font> \|}

:   <font color=red>† *This is because duplicated definitions for
    \"**aarch64**\" makes ARM build in OBS impossible.*</font>

\
: \# vi /usr/lib/build/build-pkg-rpm

:   {\| width=\"1000px\" border=\"0\" style=\"margin:0;
    background:\#f2f2f2; font-family:Consolas,Monaco,Monospace;\"

\|- \| <font color=green> ······\
pkg\_finalize\_rpm() {\
    if test -n \"\${CUMULATED\_LIST\[\*\]}\" ; then\
        echo \"now installing cumulated packages\"\
        <font color=red>ADDITIONAL\_PARAMS=</font>\
        for ((num=0; num\<=cumulate; num++)) ; do\
······\
</font> \|}

:   <font color=red>† *This bug in the \"**Cumulation**\" functionality
    makes ARM build in OBS impossible.*</font>

\

#### Install OBS packages

:   Refer to the \"[**Install OBS
    packages**](OBS_2.4_All-in-One_Server#Install_OBS_packages "wikilink")\"
    section in the \"[**Install All-in-One
    Server**](OBS_2.4_All-in-One_Server#Install_All-in-One_Server "wikilink")\"
    chapter in the \"[**OBS 2.4 All-in-One
    Server**](OBS_2.4_All-in-One_Server "wikilink")\" page.

\

#### Install additional packages for dependencies

:   \# zypper install sqlite3 perl perl-Net-SSLeay perl-GD perl-BSSolv
    perl-Socket-MsgHdr ruby rubygem-rails rubygem-delayed\_job
    rubygem-exception\_notification rubygem-nokogiri rubygem-sqlite3
    rubygem-daemons rubygem-erubis rubygem-ci\_reporter rubygem-rdoc
    rubygem-json rubygem-xmlhash
:   <font color=green>† Refer to
    <https://github.com/openSUSE/open-build-service/blob/2.5/INSTALL></font>

\

#### Configure OBS services

:   Refer to the \"[**Configure OBS
    services**](OBS_2.4_All-in-One_Server#Configure_OBS_services "wikilink")\"
    section in the \"[**Install All-in-One
    Server**](OBS_2.4_All-in-One_Server#Install_All-in-One_Server "wikilink")\"
    chapter in the \"[**OBS 2.4 All-in-One
    Server**](OBS_2.4_All-in-One_Server "wikilink")\" page.

\

#### Generate configuration.xml file

:   \# vi /srv/obs/configuration.xml
:   {\| width=\"1000px\" border=\"0\" style=\"margin:0;
    background:\#f2f2f2; font-family:Consolas,Monaco,Monospace;\"

\|- \| <font color=red>

    <?xml version="1.0" encoding="UTF-8"?>
    <configuration>
      <description>Tizen OBS</description>
      <title>Open Build Service</title>
      <schedulers>
        <arch>armv7l</arch>
        <arch>i586</arch>
        <arch>x86_64</arch>
      </schedulers>
    </configuration>

</font> \|}\

#### Modify OBS account

:   \# vi /etc/passwd
:   {\| width=\"1000px\" border=\"0\" style=\"margin:0;
    background:\#f2f2f2; font-family:Consolas,Monaco,Monospace;\"

\|- \| <font color=green> ······\
obsrun:x:482:481:User for build service
backend:/usr/lib/obs:~~/bin/false~~<font color=red>**/bin/bash**</font>\
······\
</font> \|}

:   <font color=red>† This is for OBS shell scripts to be executed by
    the OBS account.</font>

\

#### Set owner of OBS HOME directory <font color=orange>(*if necessary*)</font>

:   Refer to the \"[**Set owner of OBS HOME
    directory**](OBS_2.4_All-in-One_Server#chown_obs_home "wikilink")\"
    section in the \"[**Install All-in-One
    Server**](OBS_2.4_All-in-One_Server#Install_All-in-One_Server "wikilink")\"
    chapter in the \"[**OBS 2.4 All-in-One
    Server**](OBS_2.4_All-in-One_Server "wikilink")\" page.

\

#### Modify *BSConfig.pm* file

:   \# vi /usr/lib/obs/server/BSConfig.pm
:   {\| width=\"1000px\" border=\"0\" style=\"margin:0;
    background:\#f2f2f2; font-family:Consolas,Monaco,Monospace;\"

\|- \| <font color=green> \#our \$service\_maxchild = 20;\
<font color=red>our \$service\_maxchild = 20;</font>\
······\
<font color=red>\#</font>our \$repodownload =
\"http://\$hostname/repositories\";\
<font color=red>our \$repodownload = \"http://\$hostname:82\"</font>;\
······\
</font> \|}\

#### Create OBS database

:   \# mysql -u root -p
:   {\| width=\"1000px\" border=\"0\" style=\"margin:0;
    background:\#f2f2f2; font-family:Consolas,Monaco,Monospace;\"

\|- \| <font color=grey>/\* Create empty databases \*/</font>\
<font color=green>mysql\></font> <font color=red>create database
api\_production;</font>\
<font color=grey>/\* Create new account
<font color=blue><I>obs</I></font> with password
<font color=blue><I>obspassword</I></font> \*/</font>\
<font color=green>mysql\></font> <font color=red>create user
\'obs\'@\'%\' identified by \'obspassword\';</font>\
<font color=green>mysql\></font> <font color=red>create user
\'obs\'@\'localhost\' identified by \'obspassword\';</font>\
<font color=grey>/\* Configure permissions \*/</font>\
<font color=green>mysql\></font> <font color=red>GRANT all privileges ON
api\_production.\* TO \'obs\'@\'%\', \'obs\'@\'localhost\';</font>\
<font color=green>mysql\></font> <font color=red>FLUSH
PRIVILEGES;</font>\
<font color=grey>/\* Exit MySQL \*/</font>\
<font color=green>mysql\></font> <font color=red>exit</font>\
\|}\

#### Configure API database.yml file

:   \# vi /srv/www/obs/api/config/database.yml
:   {\| width=\"1000px\" border=\"0\" style=\"margin:0;
    background:\#f2f2f2; font-family:Consolas,Monaco,Monospace;\"

\|- \| <font color=green> ······\
production:\
  adapter: mysql2\
  database: api\_production\
  username: ~~root~~<font color=red>**obs**</font>   
<font color=blue>*\#\# The user name in the step of \"[Create OBS
database](#Create_OBS_database "wikilink")\"*</font>\
  password: ~~opensuse~~<font color=red>**obspassword**</font>   
<font color=blue>*\#\# The password in the step of \"[Create OBS
database](#Create_OBS_database "wikilink")\"*</font>\
  encoding: utf8\
······\
</font> \|}\

#### Populate API production database

:   \# cd /srv/www/obs/api
:   \# RAILS\_ENV=\"production\" rake db:setup
:   <font color=grey>*\# RAILS\_ENV=\"production\" rake
    writeconfiguration*</font>

\

#### Configure API options.yml file (like as follows)

:   \# vi /srv/www/obs/api/config/options.yml
:   {\| width=\"1000px\" border=\"0\" style=\"margin:0;
    background:\#f2f2f2; font-family:Consolas,Monaco,Monospace;\"

\|- \| <font color=green> ······\
\#use\_xforward: true\
<font color=red>use\_xforward: true</font>\
\
······\
<font color=red>\#</font>frontend\_port: 443\
<font color=red>frontend\_port: 80</font>    <font color=blue>*\#\# **If
HTTP must be used** for OBS API service **instead of HTTPS**, the port
number for API must be 80.*</font>\
<font color=red>\#</font>frontend\_protocol: https\
<font color=red>frontend\_protocol: http</font>\
······\
</font> \|}\

#### Configure Apache2

<span id="setup_syscfg_apache2">     **Edit /etc/sysconfig/apache2
file**

:   \# vi /etc/sysconfig/apache2
:   {\| width=\"1000px\" border=\"0\" style=\"margin:0;
    background:\#f2f2f2; font-family:Consolas,Monaco,Monospace;\"

\|- \| <font color=green> ······\
APACHE\_MODULES=\"······ <font color=red>passenger rewrite proxy
proxy\_http xforward headers **socache\_shmcb**</font>\"\
······\
APACHE\_SERVER\_FLAGS=\"<font color=grey>SSL</font>\"   
<font color=grey>*\#\# Enable SSL **if it is necessary**.*</font>\
······\
</font> \|} </span>\
    **Generate SSL certificate** <font color=red>***(only if HTTPS is
used)***</font>\
: Refer to the \"[Generate SSL certificate
\...](OBS_2.4_All-in-One_Server#gen_ssl_cert "wikilink")\" subsection in
the \"[Configure
Apache2](OBS_2.4_All-in-One_Server#Configure_Apache2 "wikilink")\"
section in the \"[Install All-in-One
Server](OBS_2.4_All-in-One_Server#Install_All-in-One_Server "wikilink")\"
chapter in the \"[OBS 2.4 All-in-One
Server](OBS_2.4_All-in-One_Server "wikilink")\" page.\
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

#### Configure virtual hosts for OBS

:   \# vi /etc/apache2/vhosts.d/obs.conf
:   {\| width=\"1000px\" border=\"0\" style=\"margin:0;
    background:\#f2f2f2; font-family:Consolas,Monaco,Monospace;\"

\|- \| <font color=green> <font color=red>Listen 80</font>\
<font color=grey>*Listen 443*</font>\
Listen 82\
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
\
<font color=red>\# Build Results</font>\
\<VirtualHost \*:82\>\
    ServerName rep\
\
    \# The resulting repositories\
    DocumentRoot \"/srv/obs/repos\"\
\
    <Directory /srv>\
        Options FollowSymLinks\
    </Directory>\
\
    <Directory /srv/obs/repos>\
        Options Indexes FollowSymLinks\
        Allow from all\
    </Directory>\
</VirtualHost>\
</font> \|}\

#### Change owner/group of API directories

:   \# chown -R wwwrun:www /srv/www/obs/api

\

#### Set up firewall

    **Add TCP ports for OBS server**

:   YaST \--\> Security and Users \--\> Firewall \--\> Allowed Services
    \--\> Advanced\... \--\> TCP Ports
:   {\| width=\"1000px\" border=\"0\" style=\"margin:0;
    background:\#f2f2f2; font-family:Consolas,Monaco,Monospace;\"

\|- \| <font color=red> 5152 5252 5352 80 82
<font color=grey>*443*</font>\
</font> \|}

:   <font color=red>† *\"443\" port should be enabled only if it is
    used.*</font>\

\

#### Register OBS server services

:   \# systemctl enable mysql
:   \# chkconfig \--add obsrepserver obssrcserver obsservice
    obsscheduler obsdispatcher obspublisher
:   \# systemctl enable apache2
:   \# chkconfig \--add obsapidelayed memcached

\

------------------------------------------------------------------------

### <big>***Reboot OBS Server***</big>

<big>

<li>

Reboot OBS server </big>

</ul>

\

------------------------------------------------------------------------

### <big>***Install Workers***</big>

Refer to the \"[**Install
Workers**](OBS_2.4_All-in-One_Server#Install_Workers "wikilink")\"
chapter in the \"[**OBS 2.4 All-in-One
Server**](OBS_2.4_All-in-One_Server "wikilink")\" page.\
\

[Category:Tool](Category:Tool "wikilink")
