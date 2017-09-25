# How to Customize Images

This section will describle how to customize your image by updating the kickstart file. You can try to download a kickstart file and try to edit it. For example, download it from: 

## Specify the repository

You can specify which repository should be used to create this package, including a local repository. For example: [http://download.tizen.org/releases/daily/trunk/ivi/latest/images/ivi-min...](http://download.tizen.org/releases/daily/trunk/ivi/latest/images/ivi-min-pc/ivi-min-pc-tizen_20120926.2.ks)

```bash
repo --name=Tizen-main --baseurl=https://download.tizen.org/snapshots/trunk/common/@BUILD_ID@/repos/main/armv7l/packages/ --save  --ssl_verify=no
 
repo --name=Tizen-base --baseurl=https://download.tizen.org/snapshots/trunk/common/@BUILD_ID@/repos/base/armv7l/packages/ --save  --ssl_verify=no
 
repo --name=mylocal--baseurl=/loca/repo/path/ 
```

## How to specify user/password to access repo

If the remote repository access requires a password, then you can specify user/passwdto for the repo in the ks file. For example:

repo --name=REPO-NAME --baseurl=[https://username:passwd@yourrepo.com/ia32/packages/](https://username:passwd@yourrepo.com/ia32/packages/) --save  --ssl_verify=no

## How to add / remove packages

You can specify the packages which you plan to install in the '%packages' section in the ks file. Packages can be specified by group/pattern or by individual package name. The definition of the groups/pattern can be referred to in the repodata/*comps.xml or repodata/pattern.xml file, which are released on the download server. For example: [http://download.tizen.org/snapshots/trunk/common/latest/repos/base/ia32/packages/repodata/](http://download.tizen.org/snapshots/trunk/common/latest/repos/base/ia32/packages/repodata/). The %packages section is required to end with '%end'. Also, multiple '%packages' sections are allowed. Additionally, individual packages may be specified by using globs. For example:

```bash
 %packages
 ...
 @Tizen Core            # add a group named Tizen Core, and all the packages in this group would be added
 e17-*                  # add all the packages with name starting with "e17-"
 kernel                 # add kernel package
 nss-server.armv7hl     # add nss-server with arch armv7hl
 -passwd                # remove the package passwd
 ...
 %end
```

## Specify the post-scripts

```bash
rpm -rebuilddb
%end
```


For more info about kickstat, refer to:

[http://fedoraproject.org/wiki/Anaconda/Kickstart#Chapter_2._](http://fedoraproject.org/wiki/Anaconda/Kickstart)[Kickstart_Options](http://fedoraproject.org/wiki/Anaconda/Kickstart)
