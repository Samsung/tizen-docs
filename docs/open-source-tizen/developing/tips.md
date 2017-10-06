# Development Tips

- **SSH configuration file content**

  - When working at home, you do not need a proxy, so the SSH configuration file is identical for all Linux distribution versions:

    ```
    Host tizen review.tizen.org
    Hostname review.tizen.org
    IdentityFile ~/.ssh/id_rsa
    User <Gerrit_Username>
    Port 29418
    ```

  - When working in a corporate environment, a proxy line in the SSH configuration is mandatory, and its format depends on the Linux distribution version you are using.

    For Ubuntu, openSUSE, and CentOS, append `ProxyCommand nc -X5 -x <Proxy Address>:<Port> %h %p` to the SSH configuration, whereas for Fedora, append `ProxyCommand nc --proxy-type socks4 --proxy <Proxy Address>:<Port> %h %p` instead.

- **Problems when cloning through SSH/HTTP**

  - If you are located in China, you can experience problems connecting to Google servers when downloading the repo tool, initializing the repository, and synchronizing Tizen source.

    In a typical error situation, no error message is displayed when downloading the repo tool by using curl, but connection problems occur when attempting to run the `repo init` command. In such cases, clear the Git HEAD and try running the repo commands through the `tsocks` proxy:

    ```bash
    $ tsocks curl http://commondatastorage.googleapis.com/git-repo-downloads/repo > ~/bin/repo
    $ tsocks repo init -u ssh://<Username>@review.tizen.org:29418/scm/manifest -b tizen -m ivi.xml
    $ tsocks repo init -u https://<Username>:<HTTPS_Password>@review.tizen.org/gerrit/p/scm/manifest -b tizen -m ivi.xml
    ```

  - When initializing and cloning through HTTP, you can be blocked by the "server certificate verification" issue. Run the following command and try again:

    ```bash
    $ export GIT_SSL_NO_VERIFY=1
    ```
