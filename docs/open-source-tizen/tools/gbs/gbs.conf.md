# Configuration File

GBS's configuration files are all simple INI-style files that record various choices and settings used by many GBS commands. Some settings represent purely personal preferences, others are vital to a build functioning correctly, and still others tweak command behavior a bit.

> **Note**
> ".conf" is a common extension for an INI file, an informal standard for configuration files. INI files are simple text files with basic structure composed of sections and properties. Like many tools, GBS supports a hierarchy of configuration files, which are shown below in decreasing precedence:
> - **$PWD/.gbs.conf:** project-specific configuration settings that affect only the specific project in the specified working directory. These settings have the highest precedence.
> - **/home/<user>/.gbs.conf:** user-specific configuration settings that affect only the specified user.
> - **/etc/gbs.conf:** system-wide configuration settings that affect the entire system. These settings have the lowest precedence.

When specifying the configuration file by using -c (--config) option, one of the above files is loaded and applied by GBS. If no configuration file can be found, GBS automatically generates ~/.gbs.conf. Here's an example of specifying one configuration file among a hierarchy of configuration files:

```
$ gbs -c ~/gbs-my.conf build -A ...
```

## Profile Oriented Style of Configuration

This section provides information about the profile oriented style in a GBS configuration file.

### Basic Structure

The basic structure of a configuration file is composed of properties and sections.

#### Properties

The basic element contained in a configuration file is the property. Every property has a name and a value, delimited by an equal sign (=). The name appears to the left of the equal sign.

#### Sections

Properties may be grouped into various sections, named according to the naming conventions specified in Section 2.2. The section name appears on a line by itself in square brackets ([ ]). All the properties after the section declaration are associated with that section. No explicit "end of section" delimiter is needed. Sections end at the next section declaration or the end of the file. Possible sections include:

- **General section**

  The default profile is defined in the general section and has impacts on GBS behaviors on a general basis. That is, upon the modification of the general section, all GBS behaviors will be changed accordingly.

  Supported properties include the following:

  - native

    This property explicitly defines if a package is native or non-native. Values 'yes', 'on', '1', 'true' and 'enabled' are interpreted as True, which directs GBS to do export in native packaging mode. All other non-empty values are interpreted as False, which makes GBS to do export in non-native mode.

  - fallback_to_native

    When enabled for non-native packages, this property forces GBS to fallback to native packaging mode if export fails in non-native packaging mode, that is, directs GBS to ignore upstream branch and create tarball from HEAD (by default) or specified commit without generating any patch. In other words, fallback_to_native serves as emergency option for non-native packages.

  - tmpdir

  - upstream_branch

  - upstreamtag

  - buildroot

  - packaging_dir

- **Profile section**

  It is recommended that you set common authentication information in the profile level, instead of repeating identical configurations in various sections. These settings can be automatically passed to OBS and repository sections.

  Add authentication information to a specific repository or OBS section only when it is unique to the corresponding OBS or repository. In addition, multiple profile sections can exist in one configuration file, enabling the manipulation of GBS behaviors aimed at different devices (for example, mobile phone, IVI) in a central configuration file. For more information, refer to Section 3.2.

  Supported properties include the following:

  - user

  - passwd

  - repos

  - obs

  - buildconf

    Build config for gbs build to build all profiles.

  - exclude_packages

    A list of packages that don't participate in the building. This property can also be used to break the dependency circle.

- **OBS section**

  The OBS section specifies the configurations of the remote build server for remote build. Supported properties include url, user, and password.

- **Repository section**

  As with the profile section, multiple repository sections can exist in one configuration file, so, various repositories can be manipulated in "batch". Properties supported include url, user, and password. User and password can be omitted if the corresponding repository does not need authentication information.

### Naming Conventions

The section names must follow these naming conventions:

- Name the general section exactly as "[general]".
- Start the profile section name with "profile.". For example, [profile.tizen], [profile.IVI].
- Start the OBS section name with "obs.". For example, [obs.tizen].
- Start the repository section name with "repo.".

Here's an example of configuration file:

```
[general]
#Current profile name which should match a profile section name
tmpdir = /var/tmp
editor =
packaging_branch = master
upstream_branch = upstream
upstream_tag = upstream/${upstreamversion}
packaging_dir = packaging
profile = profile.tizen
buildroot = ~/GBS-ROOT/
work_dir = .
 
[profile.tizen]
obs = obs.tizen
repos = repo.tizen_latest
# If no buildroot for profile, the buildroot in general section will be used
buildroot = ~/GBS-ROOT-profile.tizen/
# Specify build conf for a specific profile by using shell-style variable references
buildconf = ${work_dir}/tizen-conf/build.conf
# Specify a list of packages that don't participate in the building, which
# can also be used to break dependency circle.
exclude_packages=filesystem,aul,libmm-sound,libtool
 
# Common authentication information
user = xxx
passwd = xxx
 
[obs.tizen]
url = https://api.tizen.org
```

## Configuration Specification

This section provides information about the configuration specification.

### Configuring Common Properties

Typical common properties include buildroot, user, and password. To configure the buildroot to override the default value "~/GBS-ROOT", use this assignment equation:

```
buildroot=<New_Build_Root>
```

The reason we need to configure the "passwd" property is because the password line will be automatically converted to an encoded version after running the GBS, as shown in this example:

```
passwdx = QlpoOTFBWSZTWVyCeo8AAAKIAHJAIAAhhoGaAlNOLuSKcKEguQT1
```

To reset the password, delete the "passwdx" line above and add this assignment equation:

```
passwd=<New_Password>
```

### Configuring Multiple Profiles

By adding configuration specifications of multiple profiles aimed at various devices in one configuration file, the GBS behaviors oriented for a variety of devices can be manipulated by using a central configuration file. Here's an example of configuring multiple profiles:

```
[general]
profile = profile.ivi
 
[profile.mobile]
...
[profile.ivi]
...
```

When specifying the profile section by using -P (--profile) option, the specified profile configurations are applied by GBS. Here are examples of specifying one profile among multiple profiles:

```
$ gbs build --profile=profile.mobile -A i586
$ gbs remotebuild --profile=mobile
```

### Configuring Repository

This section describes how to configure the repository to adapt the GBS build. The repository configuration specification starts with the section declaration named "[repo.<customized_name>]", and followed by various properties, including:

- url

  The url property specifies the URL of a remote repository, or the full path of a local or remote repository. That is, the following two types of remote repositories are supported:

  - a standard RPM repository that has a repodata/ subdirectory under the /repos/ directory.
  - a Tizen repository that has a builddata/ subdirectory, for example, [http://download.tizen.org/releases/daily/2.0alpha/common/latest/](http://download.tizen.org/releases/daily/2.0alpha/common/latest/)

  > **Note** 
  > To guarantee the quality of the GBS build, the release folder must be used, instead the snapshot folder.

- user

- passwd

Here's an example of repository configuration specification:

```
[repo.tizen_latest]
url = http://download.tizen.org/releases/trunk/daily/ivi/latest/
user = xxx
passwd = xxx
[repo.my_local]
#local repo must be an absolute path
url = <Full_Path_of_Local_Repository>
```

### Shell-Style Variable References

Properties defined in [general] section can be directly used in other sections by using shell-style variable references in GBS 0.17 and later versions.

Here's an example:

```
[general]
tmpdir=/var/tmp
work_dir=~/test
[profile.tizen]
buildconf=${work_dir}/tizen.conf
buildroot=${tmpdir}/profile.tizen/
```
