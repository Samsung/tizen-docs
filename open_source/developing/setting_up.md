# Setting up Development Environment

PUBLISHED 21 DEC 2016

## 1 Introduction

This document provides information about how to set up development environment in the following Linux distributions:

- Ubuntu 16.04

- Ubuntu 14.04

- Ubuntu 12.04

- openSUSE 13.1

- openSUSE 12.3

- openSUSE 12.2

- Fedora 20

- Fedora 19

- CentOS 6

- Debian 7

  **Note:** All Tizen platform tools, including Git Build System (GBS), Image Creator (MIC), and bmap-tools, support these popular Linux distribution versions with official support. CentOS is an exception for not providing official support.

## 2 Setting up Gerrit Access

This section describes how to set up Gerrit access, including the following:

- How to register user account to gain access to tizen.org
- How to configure Secure Shell (SSH) for Gerrit access
- How to configure Git

### 2.1 Registering User Account

To register user account to gain access to tizen.org, perform the following procedure:

1. Open the [Register Page](https://www.tizen.org/user/register).

2. Fill in the mandatory fields and other necessary information, then click **Register**.

   Gerrit will send a verification e-mail to the e-mail address provided by the user.

3. Follow the instructions in the verification e-mail to verify the e-mail, change the password and gain access to tizen.org.

   **Note:** If an error message is received upon clicking the link in the verification e-mail, copy the link to the address bar of the browser directly.

At this point, the prerequisites of accessing [Tizen Gerrit](http://review.tizen.org/gerrit/) is ready, move on the Section 2.2 to actually enable the access to [Tizen Gerrit](http://review.tizen.org/gerrit/).

### 2.2 Configuring SSH for Gerrit Access

To configure SSH for Gerrit access, perform the following procedure:

1. Generate RSA keys by executing the following command:

   ```
   $ ssh-keygen [-t rsa] [-C "<Comments>"]
   ```

   **Note:** "[-t rsa]" and "[-C "<Comments>"]" are both optional arguments for ssh-keygen command.

   If invoked, without specifying key type, ssh-keygen command will generate an RSA key for use in SSH protocol 2 connections, thus making "[-t rsa]" that specifies the key type optional.

   For RSA key, if invoked without adding any comment, ssh-keygen command initializes the comment as "<user>@<host>" when the key is generated, thus making "[-C "<Comments>"]" optional. In spite of this, adding this argument is recommended because a rephrased comment can help better identify the keys.

   Follow the on-screen prompt below to specify the file in which to save the key. When pressing ENTER directly, the default value "/home/<User>/.ssh/id_rsa" is used, as shown in the parentheses.

   ```
   Enter file in which to save the key (/home/<User>/.ssh/id_rsa):
   ```

   Then follow the on-screen prompt below to set a passphrase. Pressing ENTER directly indicates no passphrase, as shown in the parentheses.

   ```
   Enter passphrase (empty for no passphrase):Enter same passphrase again:
   ```

   At this point, the SSH keys are successfully generated.

2. Create an SSH configuration file "~/.ssh/config" and add one of the following, as appropriate:

   - Ubuntu, openSUSE, CentOS,and Debian

     ```
     Host tizen review.tizen.orgHostname review.tizen.orgIdentityFile ~/.ssh/id_rsaUser <Gerrit_Username>Port 29418# Add the line below when using proxy, otherwise, skip it.# ProxyCommand nc -X5 -x <Proxy Address>:<Port> %h %p
     ```

   - Fedora

     ```
     Host tizen review.tizen.orgHostname review.tizen.orgIdentityFile ~/.ssh/id_rsaUser <Gerrit_Username>Port 29418# Add the line below when using proxy, otherwise, skip it.# ProxyCommand nc --proxy-type socks4 --proxy <Proxy Address>:<Port> %h %p
     ```


   - **Note:**

     Both "tizen" and "review.tizen.org" are aliases of the hostname, "tizen" is configured for simplicity of commands when initializing git repositories and cloning specific Tizen project, "review.tizen.org" is configured to work with manifest.xml and _remote.xml when synchronizing the entire Tizen source.~/.ssh/config must not be written by others users. Make sure to remove the write permission by executing '$ chmod o-w ~/.ssh/config'. For more details about ssh_config, refer to man ssh_config.

3. Copy the the full text in ~/.ssh/id_rsa.pub, including all of the following:

   - "ssh-rsa" lead
   - SSH public key
   - e-mail address tail

4. Log in to [Tizen Gerrit](http://review.tizen.org/gerrit/) and upload the key.

   1. In the Gerrit web page, click the user name on the upper right corner (with a inverted triangle on the right), then click **Settings** to display the **Settings** web page.
   2. Click **SSH Public Keys** in the left panel, paste the text copied in step-03 to the **Add SSH Public Key** box, and click **Add**.

5. Verify SSH Connection by executing the following command:

   ```
   $ ssh tizen
   ```

   The message below indicates that SSH connection has been established successfully.

   ```
   **** Welcome to Gerrit Code Review ****...
   ```

### 2.3 Configuring Git for Gerrit Access

Git must know the user's name and e-mail address to determine the author of each commit. If the user name or e-mail address is not set up in a way that Git can find it, the user may encounter some odd warnings.

This configuration operation requires developer access. In addition, matching the e-mail address with the one registered in contact information, which helps Git determine a user, is recommended.

To configure Git for Gerrit access, perform the following procedure:

1. Set the user name by executing the following command:

   ```
   $ git config --global user.name <First_Name Last_Name>
   ```

2. Set the e-mail address by executing the following command:

   ```
   $ git config --global user.email "<E-mail_Address>"
   ```

   **Note:** Using the GIT_AUTHOR_NAME and GIT_AUTHOR_EMAIL environment variables is an alternative solution. These variables override all configuration settings once set.

## 3 Working through Network Proxy (Optional)

This section describes how to work through network proxy.

**Note:** It is particularly useful if you also track other git repositories for which you do not already have a dedicated 'ProxyCommand' in your ~/.ssh/config or for those using "git://" or "http://".

### 3.1 Configuring Proxy

To configure proxy through Linux shell prompt, perform the following procedure:

1. Open .bashrc file and set http_proxy, ftp_proxy, https_proxy, and no_proxy environment variables by adding the following content:

   ```
   export http_proxy=<Proxy_Address>:<Port>export ftp_proxy=$http_proxyexport https_proxy=<Proxy_Address>:<Port>export no_proxy=<Internal_Address>
   ```

2. Open /etc/sudoers and preserve environment variables by adding the content below:

   ```
   Defaults env_keep="http_proxy https_proxy no_proxy"
   ```

   **Note:** Replace "=" with "+=" if previous settings of env_keep already exists in /etc/sudoers.

### 3.2 Configuring Git Access through the Proxy

To allow Git access through the proxy, perform the following procedure:

1. Create a script named "git-proxy" in "/usr/local/bin" directory by using text editor.

   Here's an example using VIM:

   ```
   $ sudo vim /usr/local/bin/git-proxy
   ```

2. Add the content below and save the file.

   ```
   #!/bin/bash PROXY=<Proxy_Address>PORT=<Port> case $1 in# list git servers here that you do not want to use# the proxy with, separated by a pipe character '|' as below: review.tizen.org)METHOD="-X connect";;*)METHOD="-X 5 -x ${PROXY}:${PORT}"#The line above is applicable to Ubuntu and openSUSE.#For Fedora, use the variation below since it only supports socks v4.#METHOD="-X 4 -x ${PROXY}:${PORT}";;esac nc $METHOD $*
   ```

3. Change the attribute of git-proxy script to make it executable by executing the following command:

   ```
   $ sudo chmod +x /usr/local/bin/git-proxy
   ```

4. Set GIT_PROXY_COMMAND and GIT_PROXY_IGNORE environment variables by adding the following content in the .bashrc file.

   ```
   export GIT_PROXY_COMMAND=/usr/local/bin/git-proxyexport GIT_PROXY_IGNORE=<Internal_Address>
   ```

5. Run the following command to apply the changes:

   ```
   $ source ~/.bashrc
   ```