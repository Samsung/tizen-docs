# MIC Frequently Asked Questions

**Q**: When creating an image, MIC shows "Error: URLGrabber error: [http://www.example.com/latest/repos/oss/ia32/packages/repodata/repomd.xml](http://www.example.com/latest/repos/oss/ia32/packages/repodata/repomd.xml)"   
**A**: Perhaps your network has some issues, or your proxy doesn't work. Try another proxy or find out the network issue. 


**Q**: MIC complains "Error: found 1 resolver problem, abort!"  
**A**: This is not an issue with MIC, but with the repo you used. Make sure the packages in the repo you used have proper dependencies. Try using the repo under 'release' folder, instead of 'snapshot' folder. 


**Q**: I used '-A i586' to create an i586 image, but it showed "nothing provided ....". What's wrong with it?  
**A**: Use '-A i686'. i586 is lower than i686, so many packages will be missing from the installation. 


**Q**: MIC shows in the log: "file /usr/share/whatever conflicts between attempted installs of packageA and packageB"  
**A**: There are conflicts between some packages in the repo you used, but this is not an issue with MIC. Make sure you are using a proper repo. Try using the repo under 'release' folder, instead of 'snapshot' folder. 


**Q**: Error shows: Command 'modprobe' is not available.  
**A**: In some distribution, when you use sudo, the PATH variable will be changed and you will lose some important paths. Run 'export PATH=/sbin:$PATH' before running MIC.


**Q**: MIC lost some packages which are specified in '--includepkgs'/'--excludepkgs'  
**A**: Assume you want to include/exclude some packages in one repo, you will use '--includepkgs'/'--excludepkgs' option in the according repo command line, but you should list these packages to %packages section too, otherwise they will not take any effect.


**Q**: How does mic select packages? And how to set the priority of a repo?  
**A**: In general, mic will select a higher version if two or more available in all repos, if the version is the same, a higher release number is prefferred. But if you assign a priority to one repo, mic will prefer to select packages from the repo with higher priority, even in case a higher version is available in the repo with a lower priority. Actually the default priority for a repo is 99, the range of a repo priority is 1~99, the larger number has the lower priority. An example is given: 'repo --name=base --baseurl=[http://whateverurl](http://whateverurl/) --prioirity=1'.


**Q**: When creating an image, MIC shows "Error <creator>: URLGrabber error: http://www.example.com/latest/repos/oss/ia32/packages/repodata/repomd.xml" 
**A**: Perhaps your network has some issues, or your proxy doesn't work. Try another proxy or find out the network issue. Q: MIC complains "Error <repo>: found 1 resolver problem, abort!" A: This is not an issue with MIC, but with the repo you used. Make sure the packages in the repo you used have proper dependencies. Try using the repo under ‘release’ folder, instead of 'snapshot' folder. Q: I used '-A i586' to create an i586 image, but it showed "nothing provided ....". What's wrong with it? A: Use '-A i686'. i586 is lower than i686, so many packages will be missing from the installation. Q: MIC shows in the log: "file /usr/share/whatever conflicts between attempted installs of packageA and packageB" A: There are conflicts between some packages in the repo you used, but this is not an issue with MIC. Make sure you are using a proper repo. Try using the repo under ‘release’ folder, instead of 'snapshot' folder. Q: Error shows: Command 'modprobe' is not available in Fedora 17. A: In Fedora 17, when you use sudo, the PATH variable will be changed and you will lose some important paths. Run 'export PATH=/sbin:$PATH' before running MIC.

## Known Issues

### 'zypp' backend is not supported in Fedora 17

libsat-solver changed to libsolv in Fedora 17, so the zypp backend can't work well for some dependency issues. Please use 'yum' as the backend in the Fedora 17 distribution.

### Unable to install syslinux bootloader

In some new Linux distributions, the "syslinux" package in their official software repositories is version 4.04. It causes a segfault, which is a fatal bug, and MIC will fail with syslinux installation errors. The solution is to install the patched "syslinux" package in Tizen's tools repos, until the official released one has been fixed.

### Failed to create btrfs image in OpenSUSE

When creating a btrfs image in OpenSUSE, it hangs, showing image kernel panic. This issue impacts OpenSUSE distributions: 12.1, etc.

### Failed to create an image when password in the repo URL contains "@"

MIC cannot support passwords that contain the char "@", but this will be fixed soon. Example:

```bash
repo --name=Tizen-base --baseurl=https://username:passwd@example.com/arch/packages/ --save  --ssl_verify=no
```


## Reporting issues

### Reporting issues

Report bugs or feature requests at JIRA: [https://bugs.tizen.org](https://bugs.tizen.org/)

Detailed steps:

- Click "create issue"
- Select Projects: "Development Tools"
- Select Components: "MIC"