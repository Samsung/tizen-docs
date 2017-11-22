# gbs clone

Use the `gbs clone` subcommand to clone a Git repository into a new directory. Using various parameters, you can also:

- Specify the upstream branch and working branch.
- Track all remote branches.
- Create a shallow clone with a specific depth.
- Customize the directory of the local repository.

Synopsis:

```bash
gbs clone [-h] [--upstream-branch <Upstream_Branch>]
          [--packaging-branch <Working_Branch>]
          [--all] [--depth <Depth>] <Repository> [<Directory>]
```

- Mandatory parameter:
  ```bash
  <Repository>        Specifies the path of target local repository or the URL
                      of target remote repository.

                      A typical URL mainly contains the following information:

                      * Transport protocol
                      * Remote server
                      * Path to the target remote repository

                      The syntaxes are shown below:

                      ssh://<User>@<Remote_Server>[:<Port>]/<Path_to_Target_Remote_Repository>
                      https://<User>:<HTTP_Password>@<Remote_Server>/gerrit/p/<Path_to_Target_Remote_Repository>
  ```

- Optional parameters:

  ```bash
  -h, --help        Shows the help message and exit.
  --upstream-branch <Upstream_Branch>
                    Specifies the upstream branch of the target package when
                    its upstream does not match the default settings, including
                    the following:

                    * upstream
                    * master
                    * pristine-tar

                    When cloning with this parameter, the upstream branches
                    cloned to local disk change to the following:

                    * <Upstream_Branch>
                    * master
                    * pristine-tar

  --packaging-branch <Working_Branch>
                    Specifies the working branch that will be checked out.

  --all             Tracks all remote branches.

  --depth <Depth>   Creates a shallow clone with a history truncated to the
                    specified number of revisions.

  <Directory>       Specifies the destination directory into which GBS clones
                    the repository.
  ```

Examples:

- Clone a Tizen package:

  ```bash
  $ gbs clone tizen:toolchains/zlib.git
  info: cloning tizen:toolchains/zlib.git
  .......
  info: finished
  $ cd zlib/
  $ git branch
  * master
  ```

- Clone a Tizen package, as well as tracking all remote branches:

  ```bash
  $ gbs clone --all tizen:toolchains/zlib.git
  info: cloning tizen:toolchains/zlib.git
  .......
  Branch 1.0_post set up to track remote branch 1.0_post from origin.
  Branch 2.0alpha set up to track remote branch 2.0alpha from origin.
  info: finished
  $ cd zlib/
  $ git branch
  1.0_post
  2.0alpha
  * master
  ```

- Clone a Tizen package through the HTTPS protocol:

  ```bash
  $ gbs clone https://<User>:nownjzm9ICUJ@review.tizen.org/gerrit/p/adaptation/systemd-bootmode
  ```