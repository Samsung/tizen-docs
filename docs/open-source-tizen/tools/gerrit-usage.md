# Gerrit

You can perform various operations in Gerrit:

- To watch a project
  
  If you are interested in a package that has an important relation to yours, like a dependency, you can watch that package project. You receive notifications when a patchset for a watched project is uploaded to Gerrit.

  To adjust the **Watched Projects** settings to monitor new projects, in the Gerrit Web UI, go to **Settings (top right) &gt; Watched Projects**, enter the project name, and click **Watch**.

- To replace a patch set

  You can add a new patch set that replaces an existing patch set with an updated version of the same logical modification, by sending a new commit to the change's ref number. For example, to add a commit where the SHA-1 starts with "c0ffee", as a new patch set for change number 1979, use the following command:

  ```bash
  $ git push ssh://review.tizen.org/<PROJECT_NAME> c0ffee:refs/changes/1979
  ```

  > **Tip:**
  >
  > Sometimes you can use the `git commit --amend` command to update an existing local commit, and then push to Gerrit using `HEAD:refs/changes/1979`, instead of having to use a hash ID.

- To use command line tools

  You can use various command attributes to manage command line tools:

  ```bash
  ssh -p <port> <host> gerrit review [--message <MESSAGE>] [--verified <N>] [--code-review <N>] [--abandon]{COMMIT | CHANGEID,PATCHSET}...
  ```

- To review a patch set

  You can review patch sets by using the command line. For example, to verify, approve, and submit the patch "c0ff33":

  ```bash
  $ ssh review.tizen.org gerrit review --verified=+1 --code-review=+2 --submit c0ff33
  ```

- To abandon a patch set

  You can drop an uploaded patch by clicking **Abandon** in the Gerrit Web UI or using a command:

  ```bash
  $ ssh review.tizen.org gerrit review --abandon c0ff33
  ```

- To access more detailed instructions

  For detailed instructions, use the `--help` command:

  ```bash
  $ ssh review.tizen.org gerrit --help
  ```

  or see [Gerrit Code Review - Command Line Tools](https://review.tizen.org/gerrit/Documentation/cmd-index.html).