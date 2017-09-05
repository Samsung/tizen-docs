# Tips and Heads-up

## Regarding SSH Configuration File

- When working at home, you don't need any proxy, so the SSH configuration files for all Linux distribution versions can be unified as follows:

  ```
  Host tizen review.tizen.org
  Hostname review.tizen.org
  IdentityFile ~/.ssh/id_rsa
  User <Gerrit_Username>
  Port 29418
  ```

- When working in a corporate environment, for example, inside intel, proxy line is must-have, and you need to make a choice based on your Linux distribution versions.

  For Ubuntu, openSUSE, and CentOS, append "ProxyCommand nc -X5 -x <Proxy Address>:<Port> %h %p", whereas for Fedora, append "ProxyCommand nc --proxy-type socks4 --proxy <Proxy Address>:<Port> %h %p".

## Regarding Cloning through SSH/HTTP

- PRC users may find it tricky to "communicate" with google server when downloading the Repo tool, initializing the repo, and synchronizing Tizen source.

  Typical confusion is: No error message is displayed when downloading the Repo tool by using curl, but when proceeding to **repo init**, users may find the "hidden" issue come out of nowhere. In this case, keep in mind that this is an "communication" issue between PRC users and google, just clear your head and try running the commands with tsocks, some examples are shown below:

  ```bash
  $ tsocks curl http://commondatastorage.googleapis.com/git-repo-downloads/repo > ~/bin/repo
  $ tsocks repo init -u ssh://<Username>@review.tizen.org:29418/scm/manifest -b tizen -m ivi.xml
  $ tsocks repo init -u https://<Username>:<HTTPS_Password>@review.tizen.org/gerrit/p/scm/manifest -b tizen -m ivi.xml
  ```

- When initializing and cloning through HTTP, users may be blocked by the "server certificate verification" issue, run the following command and try again:

  ```bash
  $ export GIT_SSL_NO_VERIFY=1
  ```
