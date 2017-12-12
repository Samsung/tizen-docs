# GBS Configuration

The GBS configuration files are all simple INI-style files that record various choices and settings used by many GBS commands. Some settings represent purely personal preferences, while others are vital to a correctly-functioning build, and still others simply tweak command behavior a little.

> **Note**
>
> `.conf` is a common extension for an INI file, an informal standard for configuration files. INI files are simple text files with a basic structure composed of sections and properties. Like many tools, GBS supports a hierarchy of configuration files, which are shown below in decreasing precedence:
> - `$PWD/.gbs.conf`: project-specific configuration settings that affect only the specific project in the specified working directory. These settings have the highest precedence.
> - `/home/<user>/.gbs.conf`: user-specific configuration settings that affect only the specified user.
> - `/etc/gbs.conf`: system-wide configuration settings that affect the entire system. These settings have the lowest precedence.

When specifying the configuration file by using the `-c (--config)` option, 1 of the above files is loaded and applied by GBS. If no configuration file can be found, GBS automatically generates a `~/.gbs.conf` file. To specify a file among a hierarchy of configuration files:

```bash
$ gbs -c ~/gbs-my.conf build -A ...
```

## Profile-oriented Configuration Style

This section provides information about the profile-oriented style in a GBS configuration file.

### Basic Structure

The basic structure of a configuration file is composed of properties and sections:

- Properties  
The basic element contained in a configuration file is a property. Every property has a name and a value, delimited by an equal sign (=). The name appears to the left of the equal sign.
- Sections  
Properties can be grouped into various sections, named according to the [naming conventions](#naming-conventions). The section name appears on a line by itself in square brackets ([ ]). All the properties after the section declaration are associated with that section. No explicit "end of section" delimiter is needed. Sections end at the next section declaration or the end of the file. Possible sections include:
  - **General section**  
The default profile is defined in the general section and affect GBS behavior on a general basis. That is, upon the modification of the general section, all GBS behaviors are changed accordingly.

    The supported properties include:
    - `native`  
      This property explicitly defines whether a package is native or non-native. Values `yes`, `on`, `1`, `true`, and `enabled` are interpreted as `True`, directing GBS to export in the native packaging mode. All other non-empty values are interpreted as `False`, making GBS export in the non-native mode.
    - `fallback_to_native`  
      This property serves as an emergency option for non-native packages. When enabled for non-native packages, it forces GBS to fallback to the native packaging mode if export fails in the non-native packaging mode. This means that it directs GBS to ignore the upstream branch and create a tarball from HEAD (by default) or specified commit without generating any patch.
    - `tmpdir`
    - `upstream_branch`
    - `upstreamtag`
    - `buildroot`
    - `packaging_dir`
  - **Profile section**  
Set common authentication information on the profile level, instead of repeating identical configurations in various sections. These settings can be automatically passed to OBS and repository sections.

    Add authentication information to a specific repository or OBS section only when it is unique to the corresponding OBS or repository. In addition, multiple profile sections can exist in 1 configuration file, enabling the manipulation of GBS behaviors aimed at different devices (for example, mobile phone and IVI) in a central configuration file. For more information, see [Configuring Multiple Profiles](#configuring-multiple-profiles).

    The supported properties include:
    - `user`
    - `passwd`
    - `repos`
    - `obs`
    - `buildconf`  
The build config for the `gbs build`command to build all profiles.
    - `exclude_packages`  
A list of packages that do not participate in the building. This property can also be used to break the dependency circle.
  - **OBS section**  
The OBS section specifies the configurations of the remote build server for a remote build. The supported properties include `url`, `user`, and `password`.
  - **Repository section**  
As with the profile section, multiple repository sections can exist in 1 configuration file, allowing various repositories to be manipulated in "batch". The supported properties include `url`, `user`, and `password`. The `user` and `password` properties can be omitted if the corresponding repository does not need authentication information.

<a name="naming-conventions"></a>
### Naming Conventions

The section names must follow these naming conventions:

- Name the general section exactly as [general].
- Start the profile section name with "profile.". For example, [profile.tizen] or [profile.IVI].
- Start the OBS section name with "obs.". For example, [obs.tizen].
- Start the repository section name with "repo.".

```bash
[general]
#Current profile name which must match a profile section name
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
# can also be used to break dependency circle
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

Typical common properties include `buildroot`, `user`, and `password`.

To configure the `buildroot` property to override the default `~/GBS-ROOT` value:

```bash
buildroot=<New_Build_Root>
```

The reason you need to configure the `passwd` property is because the password line is automatically converted to an encoded version after running the GBS:

```bash
passwdx = QlpoOTFBWSZTWVyCeo8AAAKIAHJAIAAhhoGaAlNOLuSKcKEguQT1
```

To reset the password, delete the `passwdx` line above and add a new assignment equation:

```bash
passwd=<New_Password>
```

<a name="configuring-multiple-profiles"></a>
### Configuring Multiple Profiles

By adding configuration specifications of multiple profiles aimed at various devices in 1 configuration file, the GBS behavior oriented for a variety of devices can be manipulated by using a central configuration file.

To configure multiple profiles:

```bash
[general]
profile = profile.ivi

[profile.mobile]
...
[profile.ivi]
...
```

When you specify the profile section with the `-P (--profile)` option in a GBS command, the specified profile configuration is applied:

```bash
$ gbs build --profile=profile.mobile -A i586
$ gbs remotebuild --profile=mobile
```

### Configuring a Repository

You can configure a repository to adapt the GBS build. The repository configuration specification starts with the section declaration named "[repo.<customized_name>]", and is followed by various properties, including:

- `url`

  The `url` property specifies the URL of a remote repository, or the full path of a local or remote repository. The following 2 types of remote repositories are supported:

  - Standard RPM repository that has a `repodata/` subdirectory under the `/repos/` directory.
  - Tizen repository that has a `builddata/` subdirectory, for example, [http://download.tizen.org/releases/daily/2.0alpha/common/latest/](http://download.tizen.org/releases/daily/2.0alpha/common/latest/).

  > **Note**
  >
  > To guarantee the quality of the GBS build, the `release` folder must be used instead the `snapshot` folder.

- `user`

- `passwd`

```bash
[repo.tizen_latest]
url = http://download.tizen.org/releases/trunk/daily/ivi/latest/
user = xxx
passwd = xxx
[repo.my_local]
#local repo must be an absolute path
url = <Full_Path_of_Local_Repository>
```

### Shell-style Variable References

Properties defined in the `[general]` section can be directly used in other sections by using shell-style variable references in GBS 0.17 and higher:

```bash
[general]
tmpdir=/var/tmp
work_dir=~/test
[profile.tizen]
buildconf=${work_dir}/tizen.conf
buildroot=${tmpdir}/profile.tizen/
```
