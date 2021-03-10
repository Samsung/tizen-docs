Introduction
------------

This document provides information about the package dependency of GBS,
including the following:

-   How many packages related for [GBS](GBS "wikilink")?
-   What\'s the dependency of them?
-   Which packages are developed by us, and which are from upstream?

Packages Related For GBS
------------------------

This section describes the packages related for GBS, including the
following:

-   How to find the packages related for GBS?
-   Package list for GBS

### How To Find The Packages Related For GBS

The automated testing for installing and upgrading GBS is performed
regularly in Jenkins, the packages related for GBS can be found in the
test result.

Take Ubuntu\_13.10-x86\_64 system for example. To find the packages
related, refer to \`HTML Report\`\_.

### Package List For GBS

Open the HTML report in Jenkins. Find the dependency table. The packages
related for GBS is shown.

A package list example for Ubuntu\_13.10-x86\_64 system is shown below.

`+--------------+--------------------------------------+`\
`|Package Number|Package Name                          |`\
`+==============+======================================+`\
`|     1        | gbs                                  |`\
`+--------------+--------------------------------------+`\
`|     2        | depanneur                            |`\
`+--------------+--------------------------------------+`\
`|     3        | git-buildpackage                     |`\
`+--------------+--------------------------------------+`\
`|     4        | build                                |`\
`+--------------+--------------------------------------+`\
`|     5        | qemu-arm-static                      |`\
`+--------------+--------------------------------------+`\
`|     6        | osc                                  |`\
`+--------------+--------------------------------------+`\
`|     7        | createrepo                           |`\
`+--------------+--------------------------------------+`\
`|     8        | pristine-tar                         |`\
`+--------------+--------------------------------------+`\
`|     9        | librpm-tizen                         |`\
`+--------------+--------------------------------------+`\
`|    10        | deltarpm                             |`\
`+--------------+--------------------------------------+`\
`|    11        | pbzip2                               |`\
`+--------------+--------------------------------------+`\
`|    12        | libcrypt-ssleay-perl                 |`\
`+--------------+--------------------------------------+`

Packages Dependency Of GBS
--------------------------

This section describes packages dependency of GBS, including the
follwing:

-   How to check the dependency of the packages?
-   How to analyze the provide information?
-   How many types of packages dependency?
-   Packages dependency of GBS.

### How To Check The Dependency Of The Packages

The following two methods can be used to check the packages dependency.

1\. To check the dependency of the packages, packaging technical should
be used. In debian based system, use command 'dpkg -s \< package name \>
In RPM based system, use command 'rpm -q --requires \< package name \>'.

`  An example is shown below:`\
`       $ dpkg -s gbs`\
`       Depends: python (>= 2.6), python-support (>= 0.90.0), python-pycurl,`\
`       sudo, osc (>= 0.139.0), git-buildpackage-rpm (>= 0.6.8`\
`       -tizen20140521), gbs-api (= 0.22), gbs-export (= 0.22), gbs-`\
`       remotebuild (= 0.22), depanneur (>= 0.13)`

2\. Download the projects related GBS, find the dependency in the SPEC
file for RPM based system or in the CONTROL file for debian based
system.

`  An example for RPM based system is shown below:`\
`      $ git clone `<Project_Path>\
`      $ vi `<Project_Name>`/packaging/project_name.spec`

`  An example for debian based system is shown below:`\
`       $ git clone `<Project_Path>\
`       $ vi `<Project_Name>`/debian/control`

Between the two methods, we recommend Method 2.

### How To Analyze The Provide Information

An example about \`build\` package for RPM based system is shown below.

`   $ cat build/packaging/build.spec`\
`   Name:           build`\
`   Requires:       bash`\
`   Requires:       perl`\
`   Requires:       binutils`\
`   Requires:       tar`\
`   Requires:       perl(LWP::Protocol::https)`\
`   Requires:       perl(LWP::UserAgent)`\
`   Requires:       perl(Crypt::SSLeay)`\
`   Requires:       perl(XML::Parser)`\
`   Requires:       perl(Archive::Tar)`\
`   Requires:       tizen-qemu-arm-static >= 2013.12.12`\
`   Requires:       perl-Crypt-SSLeay >= 0.64-tizen20130308`\
`   %if 0%{?fedora_version} || 0%{?suse_version} == 1220`\
`   || 0%{?centos_version}`\
`   Requires:       rpm-build`\
`   %endif`\
`   Requires:       rpm`\
`   %if 0%{?suse_version} > 1120 || ! 0%{?suse_version}`\
`   %package mkbaselibs`\
`   %package mkdrpms`\
`   %package initvm-%{initvm_arch}`\
`   Requires:       build`\
`   Provides:       tizen-build-initvm-%{initvm_arch} = 20140612`

In the spec file above, the \`Requires\` information shows which
packages are required by \`build\` package.

Pay attention to the \`%package\` information. All these information
shows the sub-packages provided by \`build\` package.

### How Many Types Of Packages Dependency

An example about \`depanneur\` package for debian based system is shown
below:

`  $ cat depanneur/debian/control`\
`    Depends: ${perl:Depends},`\
`    build (>= 2013.11.12-tizen20140227),`\
`    libyaml-perl,`\
`    createrepo (>= 0.9.8),`\
`    libjson-perl,`\
`    libhtml-template-perl`

There are three types of packages dependency above.

-   Packages \`libyaml-perl\`, \`libjson-perl\` and
    \`libhtml-template-perl\`, whose names are shown as only
    \`package-name\`.

` The first type of package can be ignore when analyzing package dependency, as these packages are often stable and not require special versions.`

-   Package \`createrepo (\>= 0.9.8)\`, whose names are shown as
    \`package-name\` + \`package-version\`.

` The second type of package should pay attention to its version, as the special version is required.`

-   Package \`build (\>= 2013.11.12-tizen20140227)\`, whose names are
    shown as \`package-name\` + \`package-version\` + \`tizen-version\`.

` Great importance should be attached to the last type of packages. `\
` These packages often have been development by us or added new features for Tizen. `\
` The special based package version and the special tizen version are required.`

### Packages Dependency Of GBS

-   Packages dependency of GBS build.

` `![` ``600px`](Packages-Dependency-Of-GBS-Build.png "fig: 600px")

-   Packages dependency of GBS remote build.

` `![` ``600px`](Packages-Dependency-Of-GBS-Remotebuild.png "fig: 600px")

-   Packages dependency of GBS export.

` `![` ``600px`](Packages-Dependency-Of-GBS-Export.png "fig: 600px")

The Ddependency Graph
---------------------

This section shows a single graph of packages dependency of GBS. In the
graph, green blocks show the packages developed by us red blocks show
the packages not developed by us, and other white blocks show packages
not developed but modified by us from upstream.

` `![` ``600px`](Packages-Dependency-Of-GBS.png "fig: 600px")

[Category:Tool](Category:Tool "wikilink")
