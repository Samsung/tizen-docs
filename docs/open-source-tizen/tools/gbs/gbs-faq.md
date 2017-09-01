# GBS Frequently Asked Questions

## Installation Related Issues

**Q**: I'm unable to get zypper to refresh from [http://download.tizen.org/tools/latest-release/openSUSE_13.2/](http://download.tizen.org/tools/latest-release/openSUSE_13.2/), but I'm not getting an error of repo issue 

**A**: This may be caused by proxy settings. Try double-checking the proxy settings and adding "-E" option when running **sudo zypper refresh** command, then see what happens. If problem is solved, preserve environment variables by modifying /etc/suders to solve the problem once and for all.  See [Setting up Development Environment](../../developing/setting-up.md).

Another possible reason is cached version at the proxy server. Try running the commands below to clean the cache:

```
# clean the cache from proxy server or remote http server.
$ wget --no-cache http://download.tizen.org/tools/latest-release/openSUSE_13.2/repodata/repomd.xml
$ zypper refresh
$ zypper install gbs
```

**Q**: I installed gbs from the official repo, but it is trying to use source code from /usr/local/lib/python*. 

**A**: This may be because you have installed GBS from source code before. Remove it and re-install.



**Q**: How do I update GBS and its dependencies? 

**A**: GBS is open source software. See [Installing Development Tools](../../developing/installing.md).



## gbs build Related Issues

**Q**: How can I make my local repo have higher priority than the remote repo? 

**A**: It depends on the order of repos, the first repo will have the highest priority. In v0.10 and higher, GBS automatically puts local repos before remote repos. 



**Q**: 'gbs build' report build expansion error: nothing provides X needed by Y. 

**A**: The package you are trying to build is missing a dependency in the repo you specified. You may need to configure/add an additional repository. Try using the release repo, instead of the snapshot repo. 



**Q**: 'gbs build' exits unexpectedly when installing packages to create build root. 

**A**: This may be caused by a remote repo having been changed. You can specify --clean while running gbs build, like:

```
$ gbs build -A <arch> --clean ...
```



**Q**: 'gbs build' exits unexpectedly with errors: file XXXX from install of YYYYY conflicts with file from package ZZZZZ. 

**A**: This may be caused by a remote repo having been changed. You can specify --clean while running gbs build, like:

```
$ gbs build -A <arch> --clean ...
```



**Q**: 'gbs build' exits with errors: have choice for XXXX needed by packagename: package1 package2. 

**A**: This may be caused by a remote repo having two packages provide XXXX, and gbs don't know which one to use. In this case, you need download the build config and add one line like this:

```
Prefer: package1
```

or

```
Prefer: package2
```

To see how to download and customize build config, please refer to the gbs build usage page. Q: 'gbs build' fails to create an arm build env on Ubuntu 11.10 A: This may be caused by qemu. 'qemu-user-static' has some issues with the Ubuntu official repo. Remove 'qemu-user-static' and install 'qemu-arm-static' from the Tizen tools repo. You can use this command:

```
$ dpkg -r --force-depends qemu-user-static$ apt-get update$ apt-get install qemu-arm-static
```



## gbs Remote build Related Issues

**Q**: I cannot access the remote build server (OBS) during a remote build 

**A**: This requires that you have an username and passwd and that you set them correctly in the configuration file. Also, make sure the build server api and proxy settings are correct for your environment. 

### Proxy Related Issues 

**Q**: export no_proxy="localhost; 127.0.0.1; .company.com" does not work on Ubuntu 

**A**: Please set no_proxy as ".company.com" directly, and try again. 



**Q**: 'gbs build' returns '500 Can't connect to xxx' 

**A**: The proxy environment variable may have a trailing '/'. Remove the '/' from whatever is setting your environment variables and it should work. This is a known bug in the perl library. This issue is fixed in gbs 0.11. 



Q**: 'gbs build' returns '500 SSL negotiation failed error' 

**A**: This is caused by the proxy server setting. The proxy you specified cannot forward SSL correctly. Try using another proxy.



## gbs chroot Related Issues

**Q**: 'gbs chroot -r <build_root>' report error: 'su: user root does not exist'. 

**A**: This is caused by missing login package while creating build root. You can fix by updating /etc/passwd and /etc/group to add root user:

```
$ echo "root:x:0:0:root:/root:/bin/bash" >>path/to/buildroot/etc/passwd$ echo "root:x:0:" >>path/to/buildroot/etc/group
```



## Others

**Q**: [Fedora] gbs show error: "<user> is not in the sudoers file. This incident will be reported". 

**A**: Update /etc/sudoers to give <user> sudo permission.