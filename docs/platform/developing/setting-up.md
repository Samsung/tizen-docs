# Set Up the Development Environment

This topic provides information on how to set up a development environment.

## Set up Gerrit access

You can set up access to [Tizen Gerrit](http://review.tizen.org/gerrit/) through the following steps:

1. Register a user account to gain access to tizen.org.
2. Configure Secure Shell (SSH) for Gerrit access.
3. Configure Git for Gerrit access.

### Register a user account

To register a user account to gain access to tizen.org, follow the steps below:

1. Open the [Register page](https://www.tizen.org/user/register).

2. Fill in the mandatory fields and other necessary information, and click **Register**.

   Gerrit sends a verification email to the email address you have provided.

3. Follow the instructions in the verification email to verify the email address, change the password, and gain access to tizen.org.
   > [!NOTE]
   >  If an error message is shown when you click the link in the verification email, copy the link to the address bar of the browser manually.

At this point, the prerequisites for accessing Gerrit are ready. Move on to the next section to enable Gerrit access.

### Configure SSH for Gerrit access

To configure SSH for Gerrit access, follow the steps below:

1. Generate RSA keys:

   ```
   $ ssh-keygen [-t rsa] [-C "<Comments>"]
   ```

   > [!NOTE]
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

   - Ubuntu or openSUSE:

     ```
     Host tizen review.tizen.org
     Hostname review.tizen.org
     IdentityFile ~/.ssh/id_rsa
     User <Gerrit_Username>
     Port 29418
     # Add the line below when using proxy, otherwise, skip it
     # ProxyCommand nc -X5 -x <Proxy Address>:<Port> %h %p
     ```

   > [!NOTE]
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

   ```
   $ ssh tizen
   ```

   The following message indicates that an SSH connection has been established successfully:

   ```
   **** Welcome to Gerrit Code Review ****
   ```

### Configure Git for Gerrit access

Git must know the user's name and email address to determine the author of each commit. If the user name or email address is not set up in a way that Git can find it, the user can encounter some odd warnings.

This configuration operation requires developer access. In addition, it is recommended to match the email address with the one registered in contact information, which helps Git identify the user.

To configure Git for Gerrit access:

1. Set the user name by executing the following command:
   ```
   $ git config --global user.name <First_Name Last_Name>
   ```
2. Set the email address by executing the following command:
   ```
   $ git config --global user.email <E-mail_Address>
   ```

> [!NOTE]
> Using the `GIT_AUTHOR_NAME` and `GIT_AUTHOR_EMAIL` environment variables is an alternative solution. These variables override all configuration settings once set.

## Set up the GBS configuration

You can set up the GBS configuration through editing the `.gbs.conf` file.

### Set up the default GBS configuration file

The default GBS configuration file is located in `~/.gbs.conf`:

```
[general]
profile = profile.unified_standard

#########################################################
################## Profile Section ##################
#########################################################

############# unified #############
[profile.unified_standard]
buildconf=./scm/meta/build-config/unified/standard_build.conf
repos = repo.base_standard,repo.base_standard_debug,repo.unified_standard,repo.unified_standard_debug

[profile.unified_emulator]
buildconf=./scm/meta/build-config/unified/emulator_build.conf
repos = repo.base_standard,repo.base_standard_debug,repo.unified_emulator,repo.unified_emulator_debug


#########################################################
################## Repo Section##################
#########################################################

############# base #############
[repo.base_standard]
url = http://download.tizen.org/releases/daily/tizen/base/latest/repos/standard/packages/
[repo.base_standard_debug]
url = http://download.tizen.org/releases/daily/tizen/base/latest/repos/standard/debug/

############# unified #############
[repo.unified_standard]
url = http://download.tizen.org/releases/daily/tizen/unified/latest/repos/standard/packages/
[repo.unified_standard_debug]
url = http://download.tizen.org/releases/daily/tizen/unified/latest/repos/standard/debug/

[repo.unified_emulator]
url = http://download.tizen.org/releases/daily/tizen/unified/latest/repos/emulator/packages/
[repo.unified_emulator_debug]
url = http://download.tizen.org/releases/daily/tizen/unified/latest/repos/emulator/debug/

```

> [!NOTE]
> The file contains the GBS configuration for latest profiles and repositories. In the near future, in new GBS versions, the default configuration file (`~/.gbs.conf`) is automatically installed when GBS is installed.
> If you want to get specific version of `.gbs.conf` file, see [gbs-config](https://git.tizen.org/cgit/scm/meta/gbs-config/) git.

> [!NOTE]
> If "scm/meta/build-config" git is not cloned in your working directory, every line which starts with "buildconf=./scm/meta/build-config" should be removed.

The default profile used in GBS is specified in the `[general]` section:

```
[general]
profile = profile.unified_standard
```

> [!NOTE]
> The default GBS build parameters, based on the above block, are as follows:
> - Tizen version: latest (check [release note](https://docs.tizen.org/platform/release-notes/tizen-6-5-m1/)).
> - Profile: unified
> - Repository: standard

### Set up a specific profile in the `.gbs.conf` file

To build using a non-default Tizen version, profile, or repository, select 1 of the profiles specified in the `.gbs.conf` file and set that profile in the `[general]` section, using the following format:

```
[general]
profile = profile.<Version><Profile>_<Repository>
```

- If the Tizen version is latest, `$Version` equals "".
- If the Tizen version is others, `$Version` equals "#.#-".

Other examples:

- Tizen Unified / emulator repository:

  ```
  [general]
  profile = profile.unified_emulator
  ```

Each `profile` entry in the `.gbs.conf` file specifies multiple `repo` entries, and each `repo` entry specifies a URL where RPM files used in the GBS build are located.

> [!NOTE]
> The `latest` directory in the remote repository URLs is a symbolic link in the remote server, which is always linked to the latest new directory and can be changed any time, so make sure to use the latest repo with a specific date to guarantee usability. An example is shown below:
> ```
> url = http://download.tizen.org/releases/daily/tizen/unified/latest/repos/standard/packages/
> ```
> This URL is symbolically linked to the latest snapshot number in "[http://download.tizen.org/releases/daily/tizen/unified/](http://download.tizen.org/releases/daily/tizen/unified/)". To guarantee usability, use a specific date:
> ```
> url = http://download.tizen.org/releases/daily/tizen/unified/tizen-unified_20170627.1/repos/standard/packages/
> ```

For more information on `.gbs.conf`, see [GBS Configuration](../reference/gbs/gbs.conf.md).

## Set up the repo tool

Repo is a repository management tool built on top of Git.  Multiple Git repositories can be downloaded with a single repo command.

To install and set up the repo tool:

1. Create a `~/bin/` subdirectory, include it in `PATH`, and switch to it:

   ```
   $ mkdir ~/bin/
   $ PATH=~/bin:$PATH
   ```

2. Download the repo script:

   ```
   $ curl http://commondatastorage.googleapis.com/git-repo-downloads/repo > ~/bin/repo
   ```

   > [!NOTE]
   > This repo tool is launched for Python 3.6 and higher version only. If your environment is lower than Ubuntu 16.04 with Python 3.5.2 version,
   > you can encounter some problems while launching the repo tool. In that case, download the following repo script:
   > ```
   > $ curl https://storage.googleapis.com/git-repo-downloads/repo-1 > ~/bin/repo
   > ```
   > For more information on older repos, see [old-repo-python](https://source.android.com/setup/develop#old-repo-python2) page.
   >
   > If you encounter problems while obtaining the repo tool, see [Development Tips](tips.md).

3. Change the attributes of the repo script to make it executable:

   ```
   $ sudo chmod a+x ~/bin/repo
   ```

## Work through a network proxy

You can set up your development environment to work through a network proxy.

> [!NOTE]
> A network proxy is particularly useful if you also track other Git repositories for which you do not already have a dedicated `ProxyCommand` in your `~/.ssh/config`, or which use "git://" or "http://".

### Configure a proxy

To configure a proxy through the Linux shell prompt, follow the steps below:

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

   > [!NOTE]
   > Replace "=" with "+=" if other `env_keep` settings already exist in `/etc/sudoers`.


### Configure Git access through the proxy

To allow Git access through the proxy, follow the steps below:

1. Create a script named `git-proxy` in the `/usr/local/bin` directory by using a text editor.

   The following example uses VIM:

   ```
   $ sudo vim /usr/local/bin/git-proxy
   ```

2. Add the following lines into the file and save it:

   ```
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

   ```
   $ sudo chmod +x /usr/local/bin/git-proxy
   ```

4. Set the `GIT_PROXY_COMMAND` and `GIT_PROXY_IGNORE` environment variables by adding the following lines into the `.bashrc` file:

   ```
   export GIT_PROXY_COMMAND=/usr/local/bin/git-proxy
   export GIT_PROXY_IGNORE=<Internal_Address>
   ```

5. Apply the changes:

   ```
   $ source ~/.bashrc
   ```
