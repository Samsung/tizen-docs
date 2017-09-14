# Local Build Guide
Do you need to make sure my development works well? 

This page is a guide to local build.

![](/docs/image/build.PNG)

### Step 1 : Installing the **TS-CLI**

[Once you have set up your environment](environment.md), just Step 2.

### Step 2 : Pull packages

1. You need to create a local repository (file system). You can use local storage to upload and deploy packages.
2. Import packages from the remote storage server to the local repository.

    ※ *Your machine should be able to access(wget) the input url.*

```java
$ ts-cli pull --rr http://172.21.17.55/packages/tizen_studio --lr /repository/tizen_studio -o ubuntu-64

## --rr, --remote-repo    remote repository url
## --lr, --local-repo     loca repository path
## -o, --os              os name
## -b, --base-snapshot   base snapshot name for package pull

```

### Step 3 : Build 

Let's build your code.  Go to the directory you developed and build with the `ts-cli build` command.

```java
$ ts-cli build -r /repository/tizen_studio -c -p

## -r, --repository      repository path. local directory path or http url.
    ex) ./repository/develop | http://download.tizen.org/sdk/tizenstudio/official
## -s, --source          source path           [default: "./"]
## -c, --clean           clean build
## -p, --push-package    push the package(s) to local repository
## -f, --force           skip version comparison and push or pull packages by force. 
                         new packages will overwrite existing ones
```

### Step 4 : Push

To create a snapshot, use the command `ts-cli push`

```java
$ ts-cli push -P <package file path|list> --lr /repository/tizen_studio

## -P, --package         single package file path or package files with seperator comma. 
                          ex) -P test1.zip | -P test1.zip,test2.zip
## --lr, --local-repo     loca repository path
## -f, --force           skip version comparison and push or pull packages by force. 
                          new packages will overwrite existing ones.
```

If successful, a folder named `snapshots` will be created under the location you specify, and a snapshot will be created under it. <br>

![](/docs/image/snapshot-result.png)


### Step 5 : Creating an Installation Image

Currently, Installation is only supported through the package manager.<br>
So, you must create an image to install the package.

```java

$ ts-cli create-image -r /repository/tizen_studio -u http://download.tizen.org/sdk/tizenstudio/official -O MyImage

## -r, --repository      local repository path in filesystem
## -u, --url             base repository URL
## -O, --output          image name
```
![](/docs/image/image-result.png)



**[Next : Pacakge Installation Guide](package-installation-guide.md)**
