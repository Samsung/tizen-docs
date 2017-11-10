# MIC Frequently Asked Questions

**Q**: When creating an image, MIC shows "Error &lt;creator&gt;: URLGrabber error: http://www.example.com/latest/repos/oss/ia32/packages/repodata/repomd.xml". What does it mean?  
**A**: Your network can have some issues, or your proxy does not work. Try another proxy and check the network status.


**Q**: MIC shows "Error &lt;repository&gt;: found 1 resolver problem, abort!" What does it mean?  
**A**: This is not an issue with MIC, but with the repository you used. Make sure the packages in the used repository have proper dependencies. Try using the repository under the `release` folder, instead of the `snapshot` folder.


**Q**: I used `-A i586` to create an i586 image, but MIC showed "nothing provided ....". What is wrong?  
**A**: Use `-A i686`. i586 is lower than i686, causing many packages to be missing from the installation.


**Q**: MIC shows in the log: "file /usr/share/whatever conflicts between attempted installs of packageA and packageB". What does it mean?  
**A**: There are conflicts between some packages in the repository you used, but this is not an issue with MIC. Make sure you are using a proper repository. Try using the repository under the `release` folder, instead of the `snapshot` folder.


**Q**: MIC shows an error: "Command 'modprobe' is not available." What is wrong?  
**A**: In some distributions, when you use sudo, the `PATH` variable is changed and you lose some important paths. Run `export PATH=/sbin:$PATH` before running MIC.


**Q**: MIC shows an error: "Command 'modprobe' is not available in Fedora 17." What is wrong?  
**A**: In Fedora 17, when you use sudo, the `PATH` variable is changed and you lose some important paths. Run `export PATH=/sbin:$PATH` before running MIC.


**Q**: MIC lost some packages which are specified in `--includepkgs`/`--excludepkgs`. What happened?  
**A**: If you want to include or exclude some packages in a repository, use the `--includepkgs`/`--excludepkgs` option in the proper repository command line. However, you must also list these packages in the `%packages` section; otherwise, the `--includepkgs`/`--excludepkgs` option has no effect.


**Q**: How does MIC select packages? And how do I set the priority of a repository?  
**A**: In general, MIC selects a higher version if 2 or more are available in all repositories. If the version is the same, a higher release number is preferred.  
If you assign a priority to a repository, MIC prefers to select packages from a repository with a higher priority, even if a higher version is available in a repository with a lower priority. The default priority for a repository is 99, the range of repository priorities is 1~99, and the larger number has the lower priority.  
To set the priority:  
```
repo --name=base --baseurl=[http://whateverurl](http://whateverurl/) --priority=1
```

## Known Issues

MIC has the following known issues:

- **'zypp' backend is not supported in Fedora 17**  
libsat-solver changed to libsolv in Fedora 17, so the zypp backend cannot work well for some dependency issues. Use 'yum' as the backend in the Fedora 17 distribution.
- **Unable to install syslinux bootloader**  
In some new Linux distributions, the "syslinux" package in their official software repositories is version 4.04. It causes a segfault, which is a fatal bug, and MIC fails with syslinux installation errors. The solution is to install the patched "syslinux" package in Tizen's tools repositories, until the officially released one has been fixed.
- **Failed to create btrfs image in OpenSUSE**  
When creating a btrfs image in OpenSUSE, it hangs, showing image kernel panic. This issue impacts OpenSUSE distributions, such as 12.1.
- **Failed to create an image when password in the repository URL contains "@"**  
MIC cannot support passwords that contain the "@" character. This issue is to be fixed soon. For example:
  ```bash
  repo --name=Tizen-base --baseurl=https://username:passwd@example.com/arch/packages/ --save  --ssl_verify=no
  ```


## Reporting MIC Issues

Report bugs or make feature requests at [JIRA](https://bugs.tizen.org/):

1. Click **create issue**.
1. Select the **Development Tools** project.
1. Select the **MIC** component.