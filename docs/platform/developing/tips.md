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

    ```
    $ tsocks curl http://commondatastorage.googleapis.com/git-repo-downloads/repo > ~/bin/repo
    $ tsocks repo init -u ssh://<Username>@review.tizen.org:29418/scm/manifest -b tizen -m ivi.xml
    $ tsocks repo init -u https://<Username>:<HTTPS_Password>@review.tizen.org/gerrit/p/scm/manifest -b tizen -m ivi.xml
    ```

  - When initializing and cloning through HTTP, you can be blocked by the "server certificate verification" issue. Run the following command and try again:

    ```
    $ export GIT_SSL_NO_VERIFY=1
    ```

- **Speed up a full build using GBS**

  - Normally a full build using GBS takes more time. So, GBS provides several options to speed up the build.
    You can see other build options on [gbs-build](../reference/gbs/gbs-build.md) page and use a recommended option in this page.
  - For example:
    ```
    $ gbs build -A i586 --threads=6 --define "_smp_mflags -j8" --baselibs --clean-once --skip-srcrpm
    ```
    - --threads
      - number of threads to build multiple packages in parallel
    - --define
      - define macro X with value Y in format "X Y"
      - "_smp_mflags"
        - allow jobs at once
    - --baselibs
      - create -32bit/-64bit/-x86 rpms for other architectures.
    - --clean-once
      - clean the build environment only once when you start building multiple packages. Later, use existing environment for all packages.
    - --skip-srcrpm
      - don't build source rpm file.