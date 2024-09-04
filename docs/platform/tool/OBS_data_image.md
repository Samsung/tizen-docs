Tizen Infra : OBS DATA TAR images
---------------------------------

### Introduction

>     This file contains the OBS Tizen project and OBS Tizen build data. 
>
>     ## Description of OBS Data.
>     OBS Version : 2.4
>     OBS Admin password : Admin/opensuse
>      
>     MYSQL_ROOT_PASSWORD=opensuse                                                    
>     MYSQL_API_DATABASE=api_production                                               
>     MYSQL_WEBUI_DATABASE=webui_production                                           
>     MYSQL_USER=obs                                                                  
>     MYSQL_PASSWORD=obspassword                                                      
>     MYSQL_DATA_DIR_DEFAULT=/var/lib/mysql

### Included Files

>     Folder : /srv/obs/ and /var/lib/mysql/ 

### Download

> ===== URL =====
>
>     http://download.tizen.org/docker/obsdata/

### Execution

##### You must be removed the old data of your OBS container.

##### If you\'ve already started a container, you must stop a container.

>     $ cd clientobsserver
>
>     $ sudo ./dobsserver.sh stop

##### remove this container

>     $ sudo ./dobsserver.sh rm

##### remove the /home/obsserver\_2.4 directory.

>      $ sudo rm -r /home/obsserver_2.4
>      

##### copy to root directory

>     $ sudo cp obsdata_tizen-2.3-mobile_20150311.3.tar.gz /

##### change to root directory.

>     $ cd /

##### Uncompress in your /home/obsserver\_2.4 directory.

>     $ sudo tar xzvpf obsdata_tizen-2.3-mobile_20150311.3.tar.gz

##### change to clientobsserver directory.

>     $ cd clientobsserver

##### start this container

>     $ sudo ./dobsserver.sh start

Done

You can see that the project is created with the \"Tizen:: 2.3
mobile\_20150311.3\".

Back to [Setup of Tizen Infrastructure with Docker](Setup_of_Tizen_Infrastructure_with_Docker "wikilink")
---------------------------------------------------------------------------------------------------------

[Category:Tool](Category:Tool "wikilink")
