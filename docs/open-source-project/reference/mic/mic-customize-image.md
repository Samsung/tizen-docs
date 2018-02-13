# Customizing Images

You can customize your image by downloading and editing the kickstart file. For more information on kickstart, see [Kickstart Options](http://fedoraproject.org/wiki/Anaconda/Kickstart).

## Specifying the Repository

You can specify which repository must be used to create a package, including a local repository.

```bash
repo --name=Tizen-main --baseurl=https://download.tizen.org/snapshots/trunk/common/@BUILD_ID@/repos/main/armv7l/packages/ --save  --ssl_verify=no

repo --name=Tizen-base --baseurl=https://download.tizen.org/snapshots/trunk/common/@BUILD_ID@/repos/base/armv7l/packages/ --save  --ssl_verify=no

repo --name=mylocal--baseurl=/local/repo/path/
```

## Specifying the User and Password to Access the Repository

If remote repository access requires a password, you can specify the user and password for the repository in the `.ks` file:

```
repo --name=REPO-NAME --baseurl=https://username:passwd@yourrepo.com/ia32/packages/ --save  --ssl_verify=no
```

## Adding and Removing Packages

You can specify the packages which you plan to install in the `%packages` section of the `.ks` file. Packages can be specified by a group/pattern or by an individual package name. The definition of the group/pattern can be referred to in the `repodata/*comps.xml` or `repodata/pattern.xml` file, which are both released on the download server.

The `%packages` section is required to end with `%end`. Also, multiple `%packages` sections are allowed. Additionally, individual packages can be specified by using globs. For example:

```bash
%packages
...
@Tizen Core            # add a group named Tizen Core, and all the packages in this group are added
e17-*                  # add all the packages whose name starts with "e17-"
kernel                 # add a kernel package
nss-server.armv7hl     # add nss-server with arch armv7hl
-passwd                # remove the package passwd
...
%end
```

## Specifying the Post-scripts

Use the following command:

```bash
rpm -rebuilddb
%end
```

