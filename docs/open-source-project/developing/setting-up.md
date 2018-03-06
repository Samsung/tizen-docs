# Setting up the Development Environment

This topic provides information on how to set up a development environment.

> **Note**
>
> If you encounter problems while obtaining the repo tool, see [Development Tips](tips.md).

## Setting Up Gerrit Access

You can set up access to [Tizen Gerrit](http://review.tizen.org/gerrit/) through the following steps:

1. Register a user account to gain access to tizen.org.
2. Configure Secure Shell (SSH) for Gerrit access.
3. Configure Git for Gerrit access.

### Registering a User Account

To register a user account to gain access to tizen.org:

1. Open the [Register page](https://www.tizen.org/user/register).
2. Fill in the mandatory fields and other necessary information, and click **Register**.  
   Gerrit sends a verification email to the email address you have provided.
3. Follow the instructions in the verification email to verify the email address, change the password, and gain access to tizen.org.
   > **Note**
   >
   >  If an error message is shown when you click the link in the verification email, copy the link to the address bar of the browser manually.

At this point, the prerequisites for accessing Gerrit are ready. Move on to the next section to enable Gerrit access.

### Configuring SSH for Gerrit Access

To configure SSH for Gerrit access:

1. Generate RSA keys:

   ```bash
   $ ssh-keygen [-t rsa] [-C "<Comments>"]
   ```

   > **Note**
   >
   > `[-t rsa]` and `[-C "<Comments>"]` are both optional arguments for the `ssh-keygen` command.
   >
   > If invoked without specifying key type, `ssh-keygen` generates an RSA key for use in SSH protocol 2 connections, thus making `[-t rsa]`, which specifies the key type, optional.
   >
   > For an RSA key, if invoked without adding any comment, `ssh-keygen` initializes the comment as "<user>@<host>" when the key is generated, thus making `[-C "<Comments>"]` optional. In spite of this, adding this argument is recommended because a rephrased comment can make it easier to identify the keys.

   Based on the on-screen prompts, specify the file in which to save the key, and the passphrase.

   ```
   Enter file in which to save the key (/home/<User>/.ssh/id_rsa):
   Enter passphrase (empty for no passphrase):
   Enter same passphrase again:
   ```

   If you press ENTER directly for the file, the default value `/home/<User>/.ssh/id_rsa` is used. If you press ENTER directly for the passphrase, no passphrase is used.

   At this point, the SSH keys are successfully generated.

2. Create an SSH configuration file, `~/.ssh/config`, and add 1 of the following, as appropriate:

   - Ubuntu, openSUSE, CentOS, or Debian:

     ```
     Host tizen review.tizen.org
     Hostname review.tizen.org
     IdentityFile ~/.ssh/id_rsa
     User <Gerrit_Username>
     Port 29418
     # Add the line below when using proxy, otherwise, skip it
     # ProxyCommand nc -X5 -x <Proxy Address>:<Port> %h %p
     ```

   - Fedora:

     ```
     Host tizen review.tizen.org
     Hostname review.tizen.org
     IdentityFile ~/.ssh/id_rsaUser <Gerrit_Username>
     Port 29418
     # Add the line below when using proxy, otherwise, skip it
     # ProxyCommand nc --proxy-type socks4 --proxy <Proxy Address>:<Port> %h %p
     ```

   > **Note**
   >
   > - Both "tizen" and "review.tizen.org" are aliases of the hostname. "tizen" is configured for simplicity of commands when initializing Git repositories and cloning specific Tizen projects, and "review.tizen.org" is configured to work with the `manifest.xml` and `_remote.xml` files when synchronizing the entire Tizen source.
   >
   > - The `~/.ssh/config` file must not be written in by other users. Make sure to remove the write permission by executing `chmod o-w ~/.ssh/config`. For more information on `ssh_config`, see `man ssh_config`.

3. Copy the full text in `~/.ssh/id_rsa.pub`, including all of the following:

   - `ssh-rsa` lead
   - SSH public key
   - Email address tail

4. Log in to [Tizen Gerrit](http://review.tizen.org/gerrit/) and upload the key:

   1. In the Gerrit Web page, click the user name on the top right corner (with an inverted triangle on the right), and select **Settings**.
   2. Click **SSH Public Keys** in the left panel, paste the text copied earlier into the **Add SSH Public Key** box, and click **Add**.

5. Verify the SSH connection:

   ```bash
   $ ssh tizen
   ```

   The following message indicates that SSH connection has been established successfully:

   ```bash
   **** Welcome to Gerrit Code Review ****
   ```

### Configuring Git for Gerrit Access

Git must know the user's name and email address to determine the author of each commit. If the user name or email address is not set up in a way that Git can find it, the user can encounter some odd warnings.

This configuration operation requires developer access. In addition, it is recommended to match the email address with the one registered in contact information, which helps Git identify the user.

To configure Git for Gerrit access:

1. Set the user name by executing the following command:
   ```bash
   $ git config --global user.name <First_Name Last_Name>
   ```
2. Set the email address by executing the following command:
   ```bash
   $ git config --global user.email "<E-mail_Address>"
   ```

> **Note**
>
> Using the `GIT_AUTHOR_NAME` and `GIT_AUTHOR_EMAIL` environment variables is an alternative solution. These variables override all configuration settings once set.

## Setting Up the GBS Configuration

You can set up the GBS configuration through editing the `.gbs.conf` file.

### Setting Up the Default GBS Configuration File

The default GBS configuration file is located in `~/.gbs.conf`:

```
[general]
profile = profile.3.0-mobile_target-TM1


#########################################################
################## Profile Section ##################
#########################################################
 
############# 5.0-unified #############
[profile.unified_standard]
buildconf=./scm/meta/build-config/unified/standard_build.conf
repos = repo.base_standard,repo.base_standard_debug,repo.unified_standard,repo.unified_standard_debug
 
[profile.unified_emulator]
buildconf=./scm/meta/build-config/unified/emulator_build.conf
repos = repo.base_standard,repo.base_standard_debug,repo.unified_emulator,repo.unified_emulator_debug
 
############# 4.0-unified #############
[profile.4.0-unified_standard]
buildconf=./scm/meta/build-config/4.0/unified/standard_build.conf
repos = repo.4.0-base_arm,repo.4.0-base_arm_debug,repo.4.0-base_arm64,repo.4.0-base_arm64_debug,repo.4.0-base_ia32,repo.4.0-base_ia32_debug,repo.4.0-base_x86_64,repo.4.0-base_x86_64_debug,repo.4.0-unified_standard,repo.4.0-unified_standard_debug
 
[profile.4.0-unified_emulator]
buildconf=./scm/meta/build-config/4.0/unified/emulator_build.conf
repos = repo.4.0-base_ia32,repo.4.0-base_ia32_debug,repo.4.0-base_x86_64,repo.4.0-base_x86_64_debug,repo.4.0-unified_emulator,repo.4.0-unified_emulator_debug
 
############# 3.0-common #############
[profile.3.0-common_x86_64-wayland]
buildconf=./scm/meta/build-config/3.0/common/x86_64-wayland_build.conf
repos = repo.3.0-base_x86_64,repo.3.0-base_x86_64_debug,repo.3.0-common_x86_64-wayland,repo.3.0-common_x86_64-wayland_debug
 
[profile.3.0-common_ia32-wayland]
buildconf=./scm/meta/build-config/3.0/common/ia32-wayland_build.conf
repos = repo.3.0-base_ia32,repo.3.0-base_ia32_debug,repo.3.0-common_ia32-wayland,repo.3.0-common_ia32-wayland_debug
 
[profile.3.0-common_emulator32-wayland]
buildconf=./scm/meta/build-config/3.0/common/emulator32-wayland_build.conf
repos = repo.3.0-base_emulator32,repo.3.0-base_emulator32_debug,repo.3.0-common_emulator32-wayland,repo.3.0-common_emulator32-wayland_debug
 
[profile.3.0-common_arm64-wayland]
buildconf=./scm/meta/build-config/3.0/common/arm64-wayland_build.conf
repos = repo.3.0-base_arm64,repo.3.0-base_arm64_debug,repo.3.0-common_arm64-wayland,repo.3.0-common_arm64-wayland_debug
 
[profile.3.0-common_arm-wayland]
buildconf=./scm/meta/build-config/3.0/common/arm-wayland_build.conf
repos = repo.3.0-base_arm,repo.3.0-base_arm_debug,repo.3.0-common_arm-wayland,repo.3.0-common_arm-wayland_debug
 
############# 3.0-mobile #############
[profile.3.0-mobile_target-TM1]
buildconf=./scm/meta/build-config/3.0/mobile/target-TM1_build.conf
repos = repo.3.0-base_arm,repo.3.0-base_arm_debug,repo.3.0-mobile_target-TM1,repo.3.0-mobile_target-TM1_debug
 
[profile.3.0-mobile_emulator32-wayland]
buildconf=./scm/meta/build-config/3.0/mobile/emulator32-wayland_build.conf
repos = repo.3.0-base_emulator32,repo.3.0-base_emulator32_debug,repo.3.0-mobile_emulator32-wayland,repo.3.0-mobile_emulator32-wayland_debug
 
[profile.3.0-mobile_arm-wayland]
buildconf=./scm/meta/build-config/3.0/mobile/arm-wayland_build.conf
repos = repo.3.0-base_arm,repo.3.0-base_arm_debug,repo.3.0-mobile_arm-wayland,repo.3.0-mobile_arm-wayland_debug
 
############# 3.0-tv #############
[profile.3.0-tv_emulator64-wayland]
buildconf=./scm/meta/build-config/3.0/tv/emulator64-wayland_build.conf
repos = repo.3.0-base_emulator64,repo.3.0-base_emulator64_debug,repo.3.0-tv_emulator64-wayland,repo.3.0-tv_emulator64-wayland_debug
 
[profile.3.0-tv_emulator32-wayland]
buildconf=./scm/meta/build-config/3.0/tv/emulator32-wayland_build.conf
repos = repo.3.0-base_emulator32,repo.3.0-base_emulator32_debug,repo.3.0-tv_emulator32-wayland,repo.3.0-tv_emulator32-wayland_debug
 
[profile.3.0-tv_arm-wayland]
buildconf=./scm/meta/build-config/3.0/tv/arm-wayland_build.conf
repos = repo.3.0-base_arm,repo.3.0-base_arm_debug,repo.3.0-tv_arm-wayland,repo.3.0-tv_arm-wayland_debug
 
############# 3.0-wearable #############
[profile.3.0-wearable_target-circle]
buildconf=./scm/meta/build-config/3.0/wearable/target-circle_build.conf
repos = repo.3.0-base_arm,repo.3.0-base_arm_debug,repo.3.0-wearable_target-circle,repo.3.0-wearable_target-circle_debug
 
[profile.3.0-wearable_emulator32-wayland]
buildconf=./scm/meta/build-config/3.0/wearable/emulator32-wayland_build.conf
repos = repo.3.0-base_emulator32,repo.3.0-base_emulator32_debug,repo.3.0-wearable_emulator32-wayland,repo.3.0-wearable_emulator32-wayland_debug
 
[profile.3.0-wearable_emulator-circle]
buildconf=./scm/meta/build-config/3.0/wearable/emulator-circle_build.conf
repos = repo.3.0-base_emulator32,repo.3.0-base_emulator32_debug,repo.3.0-wearable_emulator-circle,repo.3.0-wearable_emulator-circle_debug
 
############# 3.0-ivi #############
[profile.3.0-ivi_emulator]
buildconf=./scm/meta/build-config/3.0/ivi/emulator_build.conf
repos = repo.3.0-base_emulator32,repo.3.0-base_emulator32_debug,repo.3.0-ivi_emulator,repo.3.0-ivi_emulator_debug
 
[profile.3.0-ivi_arm]
buildconf=./scm/meta/build-config/3.0/ivi/arm_build.conf
repos = repo.3.0-base_arm,repo.3.0-base_arm_debug,repo.3.0-ivi_arm,repo.3.0-ivi_arm_debug
 
 
 
#########################################################
################## Repo Section##################
#########################################################
 
############# base #############
[repo.base_standard]
url = http://download.tizen.org/releases/daily/tizen/base/latest/repos/standard/packages/
[repo.base_standard_debug]
url = http://download.tizen.org/releases/daily/tizen/base/latest/repos/standard/debug/
 
############# 4.0-base #############
[repo.4.0-base_x86_64]
url = http://download.tizen.org/releases/daily/tizen/4.0-base/latest/repos/x86_64/packages/
[repo.4.0-base_x86_64_debug]
url = http://download.tizen.org/releases/daily/tizen/4.0-base/latest/repos/x86_64/debug/
 
[repo.4.0-base_ia32]
url = http://download.tizen.org/releases/daily/tizen/4.0-base/latest/repos/ia32/packages/
[repo.4.0-base_ia32_debug]
url = http://download.tizen.org/releases/daily/tizen/4.0-base/latest/repos/ia32/debug/
 
[repo.4.0-base_emulator64]
url = http://download.tizen.org/releases/daily/tizen/4.0-base/latest/repos/emulator64/packages/
[repo.4.0-base_emulator64_debug]
url = http://download.tizen.org/releases/daily/tizen/4.0-base/latest/repos/emulator64/debug/
 
[repo.4.0-base_emulator32]
url = http://download.tizen.org/releases/daily/tizen/4.0-base/latest/repos/emulator32/packages/
[repo.4.0-base_emulator32_debug]
url = http://download.tizen.org/releases/daily/tizen/4.0-base/latest/repos/emulator32/debug/
 
[repo.4.0-base_arm64]
url = http://download.tizen.org/releases/daily/4.0-base/latest/repos/arm64/packages/
[repo.4.0-base_arm64_debug]
url = http://download.tizen.org/releases/daily/tizen/4.0-base/latest/repos/arm64/debug/
 
[repo.4.0-base_arm]
url = http://download.tizen.org/releases/daily/tizen/4.0-base/latest/repos/arm/packages/
[repo.4.0-base_arm_debug]
url = http://download.tizen.org/releases/daily/tizen/4.0-base/latest/repos/arm/debug/
 
############# 3.0-base #############
[repo.3.0-base_x86_64]
url = http://download.tizen.org/releases/daily/tizen/3.0-base/latest/repos/x86_64/packages/
[repo.3.0-base_x86_64_debug]
url = http://download.tizen.org/releases/daily/tizen/3.0-base/latest/repos/x86_64/debug/
 
[repo.3.0-base_ia32]
url = http://download.tizen.org/releases/daily/tizen/3.0-base/latest/repos/ia32/packages/
[repo.3.0-base_ia32_debug]
url = http://download.tizen.org/releases/daily/tizen/3.0-base/latest/repos/ia32/debug/
 
[repo.3.0-base_emulator64]
url = http://download.tizen.org/releases/daily/tizen/3.0-base/latest/repos/emulator64/packages/
[repo.3.0-base_emulator64_debug]
url = http://download.tizen.org/releases/daily/tizen/3.0-base/latest/repos/emulator64/debug/
 
[repo.3.0-base_emulator32]
url = http://download.tizen.org/releases/daily/tizen/3.0-base/latest/repos/emulator32/packages/
[repo.3.0-base_emulator32_debug]
url = http://download.tizen.org/releases/daily/tizen/3.0-base/latest/repos/emulator32/debug/
 
[repo.3.0-base_arm64]
url = http://download.tizen.org/releases/daily/tizen/3.0-base/latest/repos/arm64/packages/
[repo.3.0-base_arm64_debug]
url = http://download.tizen.org/releases/daily/tizen/3.0-base/latest/repos/arm64/debug/
 
[repo.3.0-base_arm]
url = http://download.tizen.org/releases/daily/tizen/3.0-base/latest/repos/arm/packages/
[repo.3.0-base_arm_debug]
url = http://download.tizen.org/releases/daily/tizen/3.0-base/latest/repos/arm/debug/
 
############# 5.0-unified #############
[repo.unified_standard]
url = http://download.tizen.org/releases/daily/tizen/unified/latest/repos/standard/packages/
[repo.unified_standard_debug]
url = http://download.tizen.org/releases/daily/tizen/unified/latest/repos/standard/debug/
 
[repo.unified_emulator]
url = http://download.tizen.org/releases/daily/tizen/unified/latest/repos/emulator/packages/
[repo.unified_emulator_debug]
url = http://download.tizen.org/releases/daily/tizen/unified/latest/repos/emulator/debug/
 
############# 4.0-unified #############
[repo.4.0-unified_standard]
url = http://download.tizen.org/releases/daily/tizen/4.0-unified/latest/repos/standard/packages/
[repo.4.0-unified_standard_debug]
url = http://download.tizen.org/releases/daily/tizen/4.0-unified/latest/repos/standard/debug/
 
[repo.4.0-unified_emulator]
url = http://download.tizen.org/releases/daily/tizen/4.0-unified/latest/repos/emulator/packages/
[repo.4.0-unified_emulator_debug]
url = http://download.tizen.org/releases/daily/tizen/4.0-unified/latest/repos/emulator/debug/
 
############# 3.0-common #############
[repo.3.0-common_x86_64-wayland]
url = http://download.tizen.org/releases/daily/tizen/3.0-common/latest/repos/x86_64-wayland/packages/
[repo.3.0-common_x86_64-wayland_debug]
url = http://download.tizen.org/releases/daily/tizen/3.0-common/latest/repos/x86_64-wayland/debug/
 
[repo.3.0-common_ia32-wayland]
url = http://download.tizen.org/releases/daily/tizen/3.0-common/latest/repos/ia32-wayland/packages/
[repo.3.0-common_ia32-wayland_debug]
url = http://download.tizen.org/releases/daily/tizen/3.0-common/latest/repos/ia32-wayland/debug/
 
[repo.3.0-common_emulator32-wayland]
url = http://download.tizen.org/releases/daily/tizen/3.0-common/latest/repos/emulator32-wayland/packages/
[repo.3.0-common_emulator32-wayland_debug]
url = http://download.tizen.org/releases/daily/tizen/3.0-common/latest/repos/emulator32-wayland/debug/
 
[repo.3.0-common_arm64-wayland]
url = http://download.tizen.org/releases/daily/tizen/3.0-common/latest/repos/arm64-wayland/packages/
[repo.3.0-common_arm64-wayland_debug]
url = http://download.tizen.org/releases/daily/tizen/3.0-common/latest/repos/arm64-wayland/debug/
 
[repo.3.0-common_arm-wayland]
url = http://download.tizen.org/releases/daily/tizen/3.0-common/latest/repos/arm-wayland/packages/
[repo.3.0-common_arm-wayland_debug]
url = http://download.tizen.org/releases/daily/tizen/3.0-common/latest/repos/arm-wayland/debug/
 
############# 3.0-mobile #############
[repo.3.0-mobile_target-TM1]
url = http://download.tizen.org/releases/daily/tizen/3.0-mobile/latest/repos/target-TM1/packages/
[repo.3.0-mobile_target-TM1_debug]
url = http://download.tizen.org/releases/daily/tizen/3.0-mobile/latest/repos/target-TM1/debug/
 
[repo.3.0-mobile_emulator32-wayland]
url = http://download.tizen.org/releases/daily/tizen/3.0-mobile/latest/repos/emulator32-wayland/packages/
[repo.3.0-mobile_emulator32-wayland_debug]
url = http://download.tizen.org/releases/daily/tizen/3.0-mobile/latest/repos/emulator32-wayland/debug/
 
[repo.3.0-mobile_arm-wayland]
url = http://download.tizen.org/releases/daily/tizen/3.0-mobile/latest/repos/arm-wayland/packages/
[repo.3.0-mobile_arm-wayland_debug]
url = http://download.tizen.org/releases/daily/tizen/3.0-mobile/latest/repos/arm-wayland/debug/
 
############# 3.0-tv #############
[repo.3.0-tv_emulator64-wayland]
url = http://download.tizen.org/releases/daily/tizen/3.0-tv/latest/repos/emulator64-wayland/packages/
[repo.3.0-tv_emulator64-wayland_debug]
url = http://download.tizen.org/releases/daily/tizen/3.0-tv/latest/repos/emulator64-wayland/debug/
 
[repo.3.0-tv_emulator32-wayland]
url = http://download.tizen.org/releases/daily/tizen/3.0-tv/latest/repos/emulator32-wayland/packages/
[repo.3.0-tv_emulator32-wayland_debug]
url = http://download.tizen.org/releases/daily/tizen/3.0-tv/latest/repos/emulator32-wayland/debug/
 
[repo.3.0-tv_arm-wayland]
url = http://download.tizen.org/releases/daily/tizen/3.0-tv/latest/repos/arm-wayland/packages/
[repo.3.0-tv_arm-wayland_debug]
url = http://download.tizen.org/releases/daily/tizen/3.0-tv/latest/repos/arm-wayland/debug/
 
############# 3.0-wearable #############
[repo.3.0-wearable_target-circle]
url = http://download.tizen.org/releases/daily/tizen/3.0-wearable/latest/repos/target-circle/packages/
[repo.3.0-wearable_target-circle_debug]
url = http://download.tizen.org/releases/daily/tizen/3.0-wearable/latest/repos/target-circle/debug/
 
[repo.3.0-wearable_emulator32-wayland]
url = http://download.tizen.org/releases/daily/tizen/3.0-wearable/latest/repos/emulator32-wayland/packages/
[repo.3.0-wearable_emulator32-wayland_debug]
url = http://download.tizen.org/releases/daily/tizen/3.0-wearable/latest/repos/emulator32-wayland/debug/
 
[repo.3.0-wearable_emulator-circle]
url = http://download.tizen.org/releases/daily/tizen/3.0-wearable/latest/repos/emulator-circle/packages/
[repo.3.0-wearable_emulator-circle_debug]
url = http://download.tizen.org/releases/daily/tizen/3.0-wearable/latest/repos/emulator-circle/debug/
 
############# 3.0-ivi #############
[repo.3.0-ivi_emulator]
url = http://download.tizen.org/releases/daily/tizen/3.0-ivi/latest/repos/emulator/packages/
[repo.3.0-ivi_emulator_debug]
url = http://download.tizen.org/releases/daily/tizen/3.0-ivi/latest/repos/emulator/debug/
 
[repo.3.0-ivi_arm]
url = http://download.tizen.org/releases/daily/tizen/3.0-ivi/latest/repos/arm/packages/
[repo.3.0-ivi_arm_debug]
url = http://download.tizen.org/releases/daily/tizen/3.0-ivi/latest/repos/arm/debug/
```

> **Note**
>
> The file contains the GBS configuration for all profiles and repositories in Tizen version 3.0, Tizen version 4.0 and Tizen version 5.0. In the near future in new GBS versions, the above default configuration file (`~/.gbs.conf`) is automatically installed when GBS is installed.

The default profile used in GBS is specified in the `[general]` section:

```
[general]
profile = profile.unified_standard
```

> **Note**
>
> The default GBS build parameters, based on the above block, are as follows:  
> - Tizen version: 5.0  
> - Profile: unified  
> - Repository: standard

### Setting Up a Specific Profile in the `.gbs.conf` File

To build using a non-default Tizen version, profile, or repository, select 1 of the profiles specified in the `.gbs.conf` file and set that profile in the `[general]` section, using the following format:

```
[general]
profile = profile."$Version""$Profile"_"$Repository"
```

- If the Tizen version is 3.0, `$Version` equals "3.0-".
- If the Tizen version is 4.0, `$Version` equals "4.0-".
- If the Tizen version is 5.0, `$Version` equals "".

Other examples:

- Tizen 5.0 Unified / emulator repository

  ```
  [general]
  profile = profile.unified_emulator
  ```

- Tizen 4.0 Unified / emulator repository

  ```
  [general]
  profile = profile.4.0-unified_emulator
  ```

- Tizen 3.0 Common / arm64-wayland repository
  ```
  [general]
  profile = profile.3.0-common_arm64-wayland
  ```

- Tizen 3.0 Common / emulator32-wayland repository
  ```
  [general]
  profile = profile.3.0-common_emulator32-wayland
  ```

- Tizen 3.0 Mobile / target-TM1 repository
  ```
  [general]
  profile = profile.3.0-mobile_target-TM1
  ```

- Tizen 3.0 TV / arm-wayland repository
  ```
  [general]
  profile = profile.3.0-tv_arm-wayland
  ```

- Tizen 3.0 Wearable / target-circle repository
  ```
  [general]
  profile = profile.3.0-wearable_target-circle
  ```

- Tizen 3.0 IVI / emulator repository
  ```
  [general]
  profile = profile.3.0-ivi_emulator
  ```

Each `profile` entry in the `.gbs.conf` file specifies multiple `repo` entries, and each `repo` entry specifies a URL where RPM files used in the GBS build are located.

> **Note**
>
> The `latest` directory in the remote repository URLs is a symbolic link in the remote server, which is always linked to the latest new directory and can be changed any time, so make sure to use the latest repo with a specific date to guarantee usability. An example is shown below:
> ```
> url = http://download.tizen.org/releases/daily/tizen/unified/latest/repos/standard/packages/
> ```
> This URL is symbolically linked to the latest snapshot number in "[http://download.tizen.org/releases/daily/tizen/unified/](http://download.tizen.org/releases/daily/tizen/unified/)". To guarantee usability, use a specific date:
> ```
> url = http://download.tizen.org/releases/daily/tizen/unified/tizen-unified_20170627.1/repos/standard/packages/
> ```

For more information on `.gbs.conf`, see [GBS Configuration](../reference/gbs/gbs.conf.md).

## Setting Up the Repo Tool

Repo is a repository management tool built on top of Git.  Multiple Git repositories can be downloaded with a single repo command.

To install and set up the repo tool:

1. Create a `~/bin/` subdirectory, include it in `PATH`, and switch to it:

   ```bash
   $ mkdir ~/bin/
   $ PATH=~/bin:$PATH
   ```

2. Download the repo script:

   ```bash
   $ curl http://commondatastorage.googleapis.com/git-repo-downloads/repo > ~/bin/repo
   ```

   > **Note**
   >
   > If you encounter problems while obtaining the repo tool, see [Development Tips](tips.md).

3. Change the attributes of the repo script to make it executable:

   ```bash
   $ sudo chmod a+x ~/bin/repo
   ```

## Working through a Network Proxy

You can set up your development environment to work through a network proxy.

> **Note**
>
> A network proxy is particularly useful if you also track other Git repositories for which you do not already have a dedicated `ProxyCommand` in your `~/.ssh/config`, or which use "git://" or "http://".

### Configuring a Proxy

To configure a proxy through the Linux shell prompt:

1. Open the `.bashrc` file and set the `http_proxy`, `ftp_proxy`, `https_proxy`, and `no_proxy` environment variables:
   ```
    export http_proxy=<Proxy_Address>:<Port>
    export ftp_proxy=$http_proxy
    export https_proxy=<Proxy_Address>:<Port>
    export no_proxy=<Internal_Address>
   ```

2. Open `/etc/sudoers` and preserve the environment variables by adding the following content:

    ```
    Defaults env_keep="http_proxy ftp_proxy https_proxy no_proxy"
    ```

   > **Note**
   >
   > Replace "=" with "+=" if other `env_keep` settings already exist in `/etc/sudoers`.


### Configuring Git Access through the Proxy

To allow Git access through the proxy:

1. Create a script named `git-proxy` in the `/usr/local/bin` directory by using a text editor.

   The following example uses VIM:

   ```bash
   $ sudo vim /usr/local/bin/git-proxy
   ```

2. Add the following lines into the file and save it:

   ```bash
   #!/bin/bash

   PROXY=<Proxy_Address>
   PORT=<Port>

   case $1 in
   # list Git servers here that you do not want to use
   # the proxy with, separated by a pipe character '|' as below:

   review.tizen.org)
   METHOD="-X connect"
   ;;
   *)
   METHOD="-X 5 -x ${PROXY}:${PORT}"
   #The line above is applicable to Ubuntu and openSUSE
   #For Fedora, use the variation below since it only supports socks v4
   #METHOD="-X 4 -x ${PROXY}:${PORT}"
   ;;
   esac

   nc $METHOD $*
   ```

3. Change the attributes of the `git-proxy` script to make it executable:

   ```bash
   $ sudo chmod +x /usr/local/bin/git-proxy
   ```

4. Set the `GIT_PROXY_COMMAND` and `GIT_PROXY_IGNORE` environment variables by adding the following lines into the `.bashrc` file:

   ```
   export GIT_PROXY_COMMAND=/usr/local/bin/git-proxy
   export GIT_PROXY_IGNORE=<Internal_Address>
   ```

5. Apply the changes:

   ```bash
   $ source ~/.bashrc
   ```
