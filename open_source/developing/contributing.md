# Contributing Code to Tizen

## 1 Introduction

This document provides information about how to contribute code to Tizen, including the following:

- Cloning over SSH
- Submit a patch to the Gerrit
- Review a patch on the Gerrit
- Submit a package to the build system
- Review and accept a package on the build server (for release engineer only)

For more information about the whole work process, please refer to [Tizen Development Working Mechanism](https://source.tizen.org/documentation/developer-guide/getting-started-guide/tizen-development-working-mechanism).

## 2 Cloning over SSH

This section describes how to clone Tizen source over SSH, including the following:

- Cloning specific project over SSH
- Cloning all projects over SSH

### 2.1 Cloning Specific Project over SSH

This section describes how to clone specific project over SSH.

To clone specific project over SSH, perform the following procedure:

1. Confirm the package name by checking it on Tizen [Project List](https://review.tizen.org/gerrit/#/admin/projects/) or by running the following command:

   ```
   $ ssh review.tizen.org gerrit ls-projects
   ```

2. Clone the required package by executing the following command:

   ```
   $ git clone [-b <Branch>] ssh://<Username>@review.tizen.org:29418/<Gerrit_Project> [<Local_Project>]
   ```

   An example is shown below:

   ```
   $ git clone ssh://<Username>@review.tizen.org:29418/pkgs/a/avsystem
   ```

### 2.2 Cloning All Projects over SSH

This section describes how to clone source of all projects over SSH, including the following:

- Cloning the latest source of all projects over SSH

- Cloning the snapshot source of all projects over SSH

  **Note:** The following two methods can be used to guarantee the synchronization process go on smoothly.

  - **Method 1**

    Make sure the SSH configuration file is correctly configured according to [Setting up Development Environment](https://source.tizen.org/documentation/developer-guide/environment-setup), otherwise, the synchronization can not be performed successfully and the error message is like the following:

    ```
    ...nc: connection failed, SOCKS error 1ssh_exchange_identification: Connection closed by remote hostnc: connection failed, SOCKS error 1...fatal: Could not read from remote repository. Please make sure you have the correct access rightsand the repository exists.ssh_exchange_identification: Connection closed by remote hostfatal: Could not read from remote repository. ...
    ```

  - **Method 2**

    For those who have trouble modifying the SSH configuration file, an alternative is to make the following change in <Tizen_project>/.repo/manifests/_remote.xml:

    Change

    ```
    fetch="ssh://review.tizen.org/"
    ```

    to

    ```
    fetch="ssh://review.tizen.org:29418/"
    ```

  Between the two methods, we recommend **Method 1**, that is, [Setting up Development Environment](https://source.tizen.org/documentation/developer-guide/environment-setup) must be strictly followed to guarantee usability.

To prepare for cloning, perform the following procedure:

1. Create ~/bin/ subdirectory, include it in PATH, and then switch to it by executing the following commands:

   ```
   $ mkdir ~/bin/$ PATH=~/bin:$PATH
   ```

2. Download the repo script by executing the following command:

   ```
   $ curl http://commondatastorage.googleapis.com/git-repo-downloads/repo > ~/bin/repo
   ```

   **Note:** To find solutions for the issues encountered during obtaining the repo tool, refer to [Tips and Heads-up](https://source.tizen.org/documentation/developer-guide/getting-started-guide/tips-and-heads-up).

3. Change the attribute of repo to make it executable by executing the command:

   ```
   $ sudo chmod a+x ~/bin/repo
   ```

4. Create a new directory for Tizen and then switch to it by executing the following commands:

   ```
   $ mkdir ~/<Tizen_Project>$ cd ~/<Tizen_Project>
   ```

#### 2.2.1 Cloning the Latest Source of All Projects over SSH

To clone the latest source of all projects over SSH, perform the following procedure:

Tizen Common

```
$ wget <Snapshot_Manifest_URL> -O .repo/manifests/common/projects.xml$ sed -i '3,4d' .repo/manifests/common/projects.xml
```

1. Initialize the repository by executing one of the following commands, as appropriate:

   - Tizen 3.0

     - Common

       ```
       $ repo init -u ssh://<Username>@review.tizen.org:29418/scm/manifest -b tizen -m common.xml
       ```

     - Mobile

       ```
       $ repo init -u ssh://<Username>@review.tizen.org:29418/scm/manifest -b tizen -m mobile.xml
       ```

     - IVI

       ```
       $ repo init -u ssh://<Username>@review.tizen.org:29418/scm/manifest -b tizen -m ivi.xml
       ```

2. Replace latest manifest with snapshot manifest and make proper modification by executing one of the following two sets of commands, as appropriate:

   - Tizen Common

     ```
     $ wget <Snapshot_Manifest_URL> -O .repo/manifests/common/projects.xml$ sed -i '3,4d' .repo/manifests/common/projects.xml
     ```

   An example for Tizen Common is shown below:

   ```
   $ wget http://download.tizen.org/snapshots/tizen/common/latest/builddata/manifest/tizen-common_20160922.2_arm-wayland.xml -O .repo/manifests/common/projects.xml$ sed -i '3,4d' .repo/manifests/common/projects.xml
   ```

3. Synchronize the repository by executing the following command:

   ```
   $ repo sync
   ```

## 3 Patch Submission and Review on the Gerrit

This section describes how to perform patch submission and review on the Gerrit.

### 3.1 Submitting a Patch to the Gerrit

This section describes how to submit a patch to the Gerrit.

To submit a patch to the Gerrit, perform the following procedure:

1. Switch to the project directory and perform local development.

2. Stage the revised content by executing the following command:

   ```
   $ git add <Revised_File>...
   ```

3. Commit the revised content by executing the following command:

   ```
   $ git commit
   ```

4. Push the patch to Gerrit by executing the following command:

   ```
   $ git push origin HEAD:refs/for/<remote_branch_name>
   ```

   **Note:** Valid values for <remote_branch_name> are as follows:

   - **tizen**: corresponds to Tizen 3.0 branch

For more information, refer to [Gerrit Documentation](https://review.tizen.org/gerrit/Documentation/index.html).

### 3.2 Reviewing a Patch on the Gerrit

To review a patch in the Gerrit web GUI, publish the comments and vote for the patch, the patch will be merged or discarded depending on the voting results.

More specifically, a patch will be merged on the following conditions:

- The patch got at least one "+2" score and no "-2" score in the Code Review category.
- The patch got at least one "+1" score and no "-1" score in the Verified category.

**Note:** Voting "+2" requires proper privilege level. In addition, more than two "+1" serves as "+2".

When a patch meets all the criteria above, privileged users are allowed to click the **Submit and Merge** button to merge the patch into the Gerrit repository.

## 4 Package Submission and Review on the Build System

This section describes how to perform package submission by developers, and for release engineers, how to review and accept the changes on the build system side.

### 4.1 Submitting Package(s) to the Build System

This section includes the following:

- Submitting a package
- Submitting a group of packages

#### 4.1.1 Submitting a Package

To submit a package to the build system, please execute the following command:

```
$ gbs submit [-c <Commit_ID>] -m "<Comments>"
```

During the submission, the GBS automatically creates an annotated tag in the format below:

```
submit/$Tizen_Version/$(%Y%m%d.%H%M%S)
```

If the code change has already been merged by the Gerrit, a merge request will be created and release engineers will be notifed to review.

Important Note: if the patch has not been merged in Gerrit, the backend services will abort the operations and send email to the patch owner, to notify that the patch needs to be re-submitted after it is merged.

#### 4.1.2 Submitting a Group of Packages to the Build System

For multiple changed packages that have mutual dependencies, the submission must be performed as a group, that is, all of the packages must be submitted with one unified identification. This is known as **group submission**.

This feature is supported by the collaboration of Tizen client development tool (GBS) and Tizen backend services.

For the platform developers, GBS provide the --tag <TAG> option, to accept one developer specified "TAG" for the 'gbs submit' command. All submissions for multiple packages with the same TAG will be considered as a "group". And the package in the same "group" will be handled in the build system together.

An example is shown below:

Assuming ail, a low level libray, is depended by aul. Developers of ail has changed some APIs, and aul must be updated to adapt to new API changes of ail. Therefore, once all related patches have been merged to ail and aul separately, these two packages must be submitted as a group.

The procedure is as follows:

1. Submit one of the packages in the group to create a tag.

   ```
   $ cd platform/core/appfw/aul-1/$ gbs submit -m "<Comments>"
   ```

2. Obtain the tag name from the output of the command above, and use the same tag as parameter of --tag for other packages in the group.

   ```
   $ cd platform/core/appfw/ail/$ gbs submit --tag <same_tag> -m "<Comments>"
   ```

Actually, developers can also specify the tag by themselves, and use the same tag for all packages in the package group. In this case, the tag must follow the same rule in above section, or with extra postfix, like:

```
submit/$Tizen_Version/$(%Y%m%d.%H%M%S).N (N stand for a choiced number)
```

Tizen backend services will take care all submission with the same tag, and build them together.

### 4.3 Reviewing a Package on the Build Server (for release engineer only)

After developers run **gbs submit** command, Tizen back-end service starts the pre-release and nornal release processes at the same time. During the pre-release process, packages and Tizen images with specific package inside are presented to release engineers and Quality Assurance (QA) engineers for review.

QA engineers are responsible for testing packages as isolated objects, as well as verifying Tizen images with specific package inside to offer release engineers comprehensive information to make appropriate decision about whether to accept or reject a package, including the following:

- Whether this package impacts other dependent package build.
- Whether this package brings in new bugs.
- Whether this package causes regression issue.
- Whether this package influences the performance of Tizen image.

After packages are accepted by release engineers, the corresponding images are automatically created by the normal release process and can be obtained on [http://download.tizen.org/releases/daily](http://download.tizen.org/releases/daily).