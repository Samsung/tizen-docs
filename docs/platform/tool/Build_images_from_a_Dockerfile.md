Introduction
------------

To build an image from a source repository, create a description file
called Dockerfile at the root of your repository. This file will
describe the steps to assemble the image.\
Download Dockerfile on review.tizen.org\

    Log in on review.tizen.org 
    ssh clone

Gerrit Image
------------

\$ git clone <ssh://%5Buser>
id\]\@review.tizen.org:29418/scm/services/docker-script -b gerrit\
\$ cd devgerrit\
\$ ls\

     Dockerfile   dgerrit.sh  env     jdk           proxy  script  supervisor
     config.conf  drupal      gerrit  phpldapadmin  root   slap

     #### Description ####
     * Dockerfile : A Dockerfile is a text document that contains all the commands
                    you would normally execute manually in order to build a Docker image     
     * config.conf : Metaconfig file of container
     * env : Environment variables of container
     * root : Specific configuration files to be applied on container
     

\$ sudo ./dgerrit.sh build\

     Build docker images:
     Sending build context to Docker daemon 104.4 kB
     Sending build context to Docker daemon
     Step 0 : FROM opensuse:13.1
      ---&gt; c8ad3d804d48
      ...
      Successfully built 1a5ffc17324d

\$ docker images

    $ docker images 
    tizendocker:443/gerritdrupalldap         2.9.4.0.2

Jenkins Image
-------------

\$ git clone ssh://\[user
id\]\@review.tizen.org:29418/scm/services/docker-script -b jenkins\
\$ cd devjenkins\
\$ ls\

     Dockerfile  config.conf  djenkins.sh  env  jenkins  root  script  supervisor

     #### Description ####
     * Dockerfile : A Dockerfile is a text document that contains all the commands
                    you would normally execute manually in order to build a Docker image    
     * config.conf : Metaconfig file of container
     * env : Environment variables of container
     * root : Specific configuration files to be applied on container
     

\$ sudo ./djenkins.sh build\

     Build docker images:
     Sending build context to Docker daemon 104.4 kB
     Sending build context to Docker daemon
     ...
      Successfully built 1a5ffc17324d
      

\$ docker images\

    $ docker images 
    tizendocker:443/jenkins               1.580.3-1.2.0.4  

OBS Server Image
----------------

\$ git clone <ssh://%5Buser>
id\]\@review.tizen.org:29418/scm/services/docker-script -b
obsserver-2.4\
\$ cd devobsserver\
\$ ls\

     Dockerfile   dobsserver.sh  obsserver  root    supervisor
     config.conf  env            script
     
     #### Description ####
     * Dockerfile : A Dockerfile is a text document that contains all the commands
                    you would normally execute manually in order to build a Docker image
     * config.conf : Metaconfig file of container
     * env : Environment variables of container
     * root : Specific configuration files to be applied on container
     

\$ sudo ./dobsserver.sh build\

     Build docker images:
     Sending build context to Docker daemon 104.4 kB
     Sending build context to Docker daemon
      ...
      Successfully built 1a5ffc17324d
      

\$ docker images\

    $ docker images 
    tizendocker:443/obsserver            2.4.0.7

OBS Worker Image
----------------

\$ git clone <ssh://%5Buser>
id\]\@review.tizen.org:29418/scm/services/docker-script -b
obsworker-2.4\
\$ cd devobsworker\
\$ ls\

     Dockerfile  config.conf  dobsworker.sh  env  obsw  root  script  supervisor
     
     #### Description ####
     * Dockerfile : A Dockerfile is a text document that contains all the commands
                    you would normally execute manually in order to build a Docker image
     * config.conf : Metaconfig file of container
     * env : Environment variables of container
     * root : Specific configuration files to be applied on container

\$ sudo ./dobsworker.sh build

     Build docker images:
     Sending build context to Docker daemon 104.4 kB
     Sending build context to Docker daemon
      ...
      Successfully built 1a5ffc17324d

\$ docker images

    $ docker images 
    tizendocker:443/obsworker            2.4.0.3

References
----------

Docker can build images automatically by reading the instructions from a
Dockerfile <https://docs.docker.com/reference/builder/>

[Setup\_of\_Tizen\_Infrastructure\_with\_Docker](Setup_of_Tizen_Infrastructure_with_Docker "wikilink")

[Category:Tool](Category:Tool "wikilink")
