# FAQ

[GBS]: (#gbs)
[MIC]: (#mic)

## GBS

### Installation Related Issues

Q: I'm unable to get zypper to refresh from [http://download.tizen.org/tools/openSUSE12.1/](http://download.tizen.org/tools/openSUSE12.1/), but I'm not getting an error of repo issue.

A: This may be caused by proxy settings. Try double-checking the proxy settings and adding "-E" option when running **sudo zypper refresh** command, then see what happens. If problem is solved, preserve environment variables by modifying /etc/suders to solve the problem once and for all. Refer to Section 3 in [Setting up Development Environment](https://source.tizen.org/documentation/developer-guide/environment-setup) for details.

Another possible reason is cached version at the proxy server. Try running the commands below to clean the cache:

```
# clean the cache from proxy server or remote http server.$ wget --no-cache http://download.tizen.org/tools/openSUSE12.1/repodata/repomd.xml$ zypper refresh$ zypper install gbs
```

Q: I installed GBS from the official repo, but it is trying to use source code from /usr/local/lib/python*.

A: This may be because you have installed GBS from source code before. Remove it and re-install.

Q: How do I update GBS and its dependencies?

A: Refer to [Installing Development Tools](https://source.tizen.org/documentation/developer-guide/installing-development-tools).

### gbs-build Related Issues

Q: How can I make the priority of my local repo higher than the remote repo?

A: It depends on the precedence of repos, the first repo has the highest priority. The precedence of local repos is by default higher than remote repos in GBS v0.10 and later.

Q: 'gbs build' report build expansion error: nothing provides X needed by Y.

A: The package you are trying to build is missing a dependency in the repo you specified. You may need to configure/add an additional repository. Try solving the problem by using the release repo instead of the snapshot repo.

Q: 'gbs build' exits unexpectedly when installing packages to create build root.

A: This may be caused by the change of remote repos. Try solving the problem by issuing **gbs-build** command with "--clean" option, as shown below:

```
$ gbs build -A <arch> --clean ...
```

Q: 'gbs build' exits with errors: have choice for XXXX needed by packagename: package1 package2.

A: This may be because remote repo has two packages that provide XXXX, making GBS confused about which one to use. In this case, you need to download the build config and customize it by adding one of the following:

```
Prefer: package1
```

or

```
Prefer: package2
```

Q: 'gbs build' fails to create an arm build env on Ubuntu 11.10.

A: This may be caused by qemu. 'qemu-user-static' has some issues with the Ubuntu official repo. Remove 'qemu-user-static' and install 'qemu-arm-static' from the Tizen tools repo by executing the following commands:

```
$ dpkg -r --force-depends qemu-user-static$ apt-get update$ apt-get install qemu-arm-static
```

### gbs-remotebuild Related Issues

Q: I cannot access the Open Build Systems (OBS) during a remote build.

A: The prerequisites of using **gbs-reomtebuild** include the following:

- OBS account is available.
- The authentication information is correctly configured in GBS configuration file.
- The build server API and proxy settings are correctly configured in the development environment.

Try solving the problem by checking these prerequisites one by one.

### Proxy Related Issues

Q: export no_proxy="localhost; 127.0.0.1; .company.com" does not work on Ubuntu.

A: Set no_proxy as ".company.com" and try again.

Q: 'gbs build' returns '500 Can't connect to xxx'.

A: This is a known issue in the perl library which has been fixed in GBS 0.11. Try solving the problem by removing the trailing "/" in the proxy environment variable.

Q: 'gbs build' returns '500 SSL negotiation failed error'

A: This is caused by the proxy server setting. The proxy you specified cannot forward SSL correctly. Try using another proxy.

### gbs-chroot Related Issues

Q: 'gbs chroot -r <build_root>' report error: 'su: user root does not exist'.

A: This is caused by missing "login" package while creating build root. Fix it by adding "root" user in /etc/passwd and /etc/group:

```
$ echo "root:x:0:0:root:/root:/bin/bash" >>path/to/buildroot/etc/passwd$ echo "root:x:0:" >>path/to/buildroot/etc/group
```

### Miscellaneous

Q: [Fedora] gbs show error: "<user> is not in the sudoers file. This incident will be reported".

A: Update /etc/sudoers to give <user> sudo permission.

## MIC FAQ

Q: When creating an image, MIC shows "Error <creator>: URLGrabber error: [http://www.example.com/latest/repos/oss/ia32/packages/repodata/repomd.xml](http://www.example.com/latest/repos/oss/ia32/packages/repodata/repomd.xml)"

A: Perhaps your network has some issues, or your proxy doesn't work. Try another proxy or find out the network issue.

Q: MIC complains "ERROR: found 1 resolver problem, abort!"

A: This is not an issue of MIC, it's caused by the repo you used. Make sure the packages in the repo you used have proper dependencies.

Q: I used '-A i586' to create an i586 image, but it showed "nothing provided ....". What's wrong with it?

A: Use '-A i686'. i586 is lower than i686, so many packages will be missing from the installation.

Q: Error shows: "uninstallable providers: somepackageA"

A: It's caused by the missing package in the repo. To find it out, modify the %packages section with only one item 'somepackageA' in kickstart file, then you can root cause what's the missing dependency.

Q: MIC shows in the log: "file /usr/share/whatever conflicts between attempted installs of somepackageA and somepackageB"

A: There are conflicts between some packages in the repo you used, but this is not an issue with MIC. Please make sure you are using a proper repo.

Q: Error shows: Command 'modprobe' is not available.

A: In some distributions, when you use sudo, the PATH variable will be changed and you will lose some important paths. Run 'export PATH=/sbin:$PATH' before running MIC.

Q: MIC lost some packages which are specified in '--includepkgs'/'--excludepkgs'

A: Assume you want to include/exclude some packages in one repo, you will use '--includepkgs'/'--excludepkgs' option in the according repo command line, but you should list these packages to %packages section too, otherwise they will not take any effect.

Q: How does mic select packages? And how to set the priority of a repo?

A: In general, mic will select a higher version if two or more available in all repos, if the version is the same, a higher release number is prefferred. But if you assign a priority to one repo, mic will prefer to select packages from the repo with higher priority, even in case a higher version is available in the repo with a lower priority. Actually the default priority for a repo is 99, the range of a repo priority is 1~99, the larger number has the lower priority. An example is given: 'repo --name=base --baseurl=[http://whateverurl](http://whateverurl/) --prioirity=1'.
