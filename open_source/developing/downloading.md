# Downloading Tizen Source

## 1 Introduction

This document provides information about how to clone Tizen source, including the following:

- Cloning over HTTPS

This document assumes that the instructions in the following documents have been read, well understood, and correctly followed:

- [Setting up Development Environment](https://source.tizen.org/documentation/developer-guide/environment-setup)
- [Installing Development Tools](https://source.tizen.org/documentation/developer-guide/step-step-instructions/installing-development-tools)



## 2 Cloning over HTTPS

This section describes how to clone Tizen source over HTTPS, including the following:

- Cloning specific project over HTTPS
- Cloning all projects over HTTPS

### 2.1 Cloning Specific Project over HTTPS

This section describes how to clone specific project over HTTPS.

To clone specific project over HTTPS, perform the following procedure:

1. Clone the required package by executing the following command:

   ```
   $ git clone [-b <Branch>] https://git.tizen.org/cgit/<Gerrit_Project> [<Local_Project>]
   ```

   An example is shown below:

   ```
   $ git clone https://git.tizen.org/cgit/platform/core/multimedia/avsystem
   ```

### 2.2 Cloning All projects over HTTPS

This section describes how to clone source of all projects over HTTPS, including the following:

- Cloning the latest source of all projects over HTTPS

- Cloning the snapshot source of all projects over HTTPS



To prepare for cloning, perform the following procedure:

1. Create ~/bin/ subdirectory, include it in PATH, and then switch to it by executing the following commands:

   ```
   $ mkdir ~/bin/$ PATH=~/bin:$PATH
   ```

2. Download the repo script by executing the following command:

   ```
   $ curl http://commondatastorage.googleapis.com/git-repo-downloads/repo > ~/bin/repo
   ```

3. Change the attribute of repo to make it executable by executing the command:

   ```
   $ sudo chmod a+x ~/bin/repo
   ```

4. Create a new directory for Tizen and then switch to it by executing the following commands:

   ```
   $ mkdir ~/<Tizen_Project>$ cd ~/<Tizen_Project>
   ```

#### 2.2.1 Cloning the Latest Source of All Projects over HTTPS

To clone the latest source of all projects over HTTPS, perform the following procedure:

1. Initialize the repository by executing one of the following commands, as appropriate:

   - Tizen 3.0

     - Common

       ```
       $ repo init -u https://git.tizen.org/cgit/scm/manifest -b tizen -m common.xml
       ```

     - Mobile

       ```
       $ repo init -u https://git.tizen.org/cgit/scm/manifest -b tizen -m mobile.xml
       ```

     - IVI

       ```
       $ repo init -u https://git.tizen.org/cgit/scm/manifest -b tizen -m ivi.xml
       ```

2. Replace latest manifest with snapshot manifest and make proper modification by executing one of the following two sets of commands, as appropriate:

   - Tizen Common

     <Snapshot_Manifest_URL>  files are available at the [snapshot manifest](http://download.tizen.org/snapshots/tizen/common/latest/builddata/manifest/) webpage.

     ```
     $ curl <Snapshot_Manifest_URL> > .repo/manifests/common/projects.xml
     ```

     The below example is how to download tizen-common_20170110.2_arm-wayland.xml.

     ```
     $curl http://download.tizen.org/snapshots/tizen/common/latest/builddata/manifest/tizen-common_20170110.2_arm-wayland.xml > .repo/manifests/common/projects.xml
     ```

   - The below example is to change a project path correctly from 'framework/base/tizen-locale' to 'core/base/tizen-locale' after checking a correct path  of 'tizen-locale' package at [https://review.tizen.org/gerrit/#/admin/projects/](https://review.tizen.org/gerrit/#/admin/projects/).

     ```
     $ sed -i -e 's/framework\/base\/tizen-locale/core\/base\/tizen-locale/g' .repo/manifests/common/projects.xml
     ```

3. Synchronize the repository by executing the following command:

   ​

   ```
   $ repo sync
   ```


## Tips and Heads-up

### Regarding SSH Configuration File

- When working at home, you don't need any proxy, so the SSH configuration files for all Linux distribution versions can be unified as follows:

  ```
  Host tizen review.tizen.orgHostname review.tizen.orgIdentityFile ~/.ssh/id_rsaUser <Gerrit_Username>Port 29418
  ```

- When working in a corporate environment, for example, inside intel, proxy line is must-have, and you need to make a choice based on your Linux distribution versions.

  For Ubuntu, openSUSE, and CentOS, append "ProxyCommand nc -X5 -x <Proxy Address>:<Port> %h %p", whereas for Fedora, append "ProxyCommand nc --proxy-type socks4 --proxy <Proxy Address>:<Port> %h %p".

### Regarding Cloning through SSH/HTTP

- PRC users may find it tricky to "communicate" with google server when downloading the Repo tool, initializing the repo, and synchronizing Tizen source.

  Typical confusion is: No error message is displayed when downloading the Repo tool by using curl, but when proceeding to **repo init**, users may find the "hidden" issue come out of nowhere. In this case, keep in mind that this is an "communication" issue between PRC users and google, just clear your head and try running the commands with tsocks, some examples are shown below:

  ```
  $ tsocks curl http://commondatastorage.googleapis.com/git-repo-downloads/repo > ~/bin/repo$ tsocks repo init -u ssh://<Username>@review.tizen.org:29418/scm/manifest -b tizen -m ivi.xml$ tsocks repo init -u https://<Username>:<HTTPS_Password>@review.tizen.org/gerrit/p/scm/manifest -b tizen -m ivi.xml
  ```

- When initializing and cloning through HTTP, users may be blocked by the "server certificate verification" issue, run the following command and try again:

  ```
  $ export GIT_SSL_NO_VERIFY=1


