# GBS Frequently Asked Questions

## GBS Installation Issues

**Q**: I cannot get zypper to refresh from [http://download.tizen.org/tools/latest-release/openSUSE_13.2/](http://download.tizen.org/tools/latest-release/openSUSE_13.2/), but I am not getting a repository error. What is wrong?  
**A**: This can be caused by proxy settings. Double-check the proxy settings and add the `-E` option when running the `sudo zypper refresh` command. If that solves the problem, preserve the environment variables by modifying `/etc/sudoers`. For more information, see [Setting up Development Environment](../../developing/setting-up.md).

Another possible reason is a cached version at the proxy server. Try running the following commands to clean the cache:
```bash
# clean the cache from proxy server or remote http server
$ wget --no-cache http://download.tizen.org/tools/latest-release/openSUSE_13.2/repodata/repomd.xml
$ zypper refresh
$ zypper install gbs
```

**Q**: I installed GBS from the official repository, so why is it trying to use source code from `/usr/local/lib/python*`?  
**A**: This can be because you have installed GBS from source code before. Remove it and re-install.

**Q**: How do I update GBS and its dependencies?  
**A**: GBS is open source software. For more information, see [Installing Development Tools](../../developing/installing.md).


## GBS Build Issues

**Q**: How can I make my local repository have a higher priority than the remote repository?  
**A**: The priority depends on the order of repositories; the first repository has the highest priority. In v0.10 and higher, GBS automatically puts local repositories before remote repositories.


**Q**: The `gbs build` command reports a build expansion error: "nothing provides X needed by Y". What is wrong?  
**A**: The package you are trying to build is missing a dependency in the repository you specified. You need to configure or add an additional repository. Try using the release repository, instead of the snapshot repository.


**Q**: The `gbs build` command exits unexpectedly when installing packages to create a build root.  
**A**: This can be caused by a remote repository having been changed. Specify `--clean` while running the GBS build:

```bash
$ gbs build -A <arch> --clean ...
```

**Q**: The `gbs build` command exits unexpectedly with errors: "file XXXX from install of YYYYY conflicts with file from package ZZZZZ". What is wrong?  
**A**: This can be caused by a remote repository having been changed. Specify `--clean` while running the GBS build:

```bash
$ gbs build -A <arch> --clean ...
```

**Q**: The `gbs build` command exits with errors: "have choice for XXXX needed by packagename: package1 package2". What is wrong?  
**A**: This can be caused by a remote repository having 2 packages providing XXXX, and GBS not knowing which one to use. In this case, download the build config and add the following line:

```
Prefer: package1
```

or

```
Prefer: package2
```

For more information on downloading and customizing the build config, see [gbs build](gbs-build.md).

**Q**: The `gbs build` command fails to create an arm build environment on Ubuntu 11.10. What is wrong?  
**A**: This can be caused by qemu. The `qemu-user-static` option has some issues with the Ubuntu official repository. Remove `qemu-user-static` and install `qemu-arm-static` from the Tizen tools repository with the following commands:

```bash
$ dpkg -r --force-depends qemu-user-static
$ apt-get update
$ apt-get install qemu-arm-static
```

## GBS Remote Build Issues

**Q**: Why cannot I access the remote build server (OBS) during a remote build?  
**A**: The access requires that you have a username and password and that you set them correctly in the configuration file. Also, make sure the build server API and proxy settings are correct for your environment.


### Proxy Issues

**Q**: The `export no_proxy="localhost; 127.0.0.1; .company.com` command does not work on Ubuntu. Why?  
**A**: Set `no_proxy` as `.company.com` directly, and try again.

**Q**: The `gbs build` command returns "500 Can't connect to xxx". What is wrong?  
**A**: Check whether the proxy environment variable has a trailing '/', and remove it from whatever is setting your environment variables. This is a known bug in the perl library, and it is fixed in GBS 0.11.

**Q**: The `gbs build` command returns "500 SSL negotiation failed error". What is wrong?  
**A**: This is caused by the proxy server setting. The proxy you specified cannot forward SSL correctly. Try using another proxy.


## GBS chroot Issues

**Q**: The `gbs chroot -r <build_root>` command reports an error: "su: user root does not exist". What is wrong?  
**A**: This is caused by missing a login package while creating a build root. You can fix by updating `/etc/passwd` and `/etc/group` to add a root user:

```bash
$ echo "root:x:0:0:root:/root:/bin/bash" >>path/to/buildroot/etc/passwd$ echo "root:x:0:" >>path/to/buildroot/etc/group
```

## Miscellaneous Issues

**Q**: Fedora GBS shows an error: "&lt;user&gt; is not in the sudoers file. This incident will be reported". What is wrong?  
**A**: Update `/etc/sudoers` to give &lt;user&gt; sudo permission.
