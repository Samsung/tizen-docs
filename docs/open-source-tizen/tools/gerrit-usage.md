# Gerrit Usage

#### Watch a project

If you're interested in a package that has an important relation to yours, like a dependency, then you can watch those projects. You can receive a notification when a patchset is uploaded to Gerrit. Adjust the Watched Projects settings to monitor projects.

```
Settings (top right) --> Watched Projects --> input Project Name -> click 'Watch'
```

#### Replace a patch set

To add a new patch set that replaces an existing patch set with an updated version of the same logical modification, send the new commit to the change's ref number. For example, to add the commit where the SHA-1 starts with c0ffee, as a new patch set for change number 1979, use the push refspec c0ffee:refs/changes/1979:

```
 $ git push ssh://review.tizen.org/<PROJECT_NAME> c0ffee:refs/changes/1979
```

Hint: Sometimes a developer can use "git commit --amend" to update existing local commit, and then push to gerrit using "HEAD:refs/changes/1979", instead of having to use a hash-ID.

#### Command line Tools

```
ssh -p <port> <host> gerrit review [--message <MESSAGE>] [--verified <N>] [--code-review <N>] [--abandon]{COMMIT | CHANGEID,PATCHSET}…
```

##### Review a patch set

You can review patch sets by using the command line, for example, to verify, approve, and submit the patch c0ff33:

```
 $ ssh review.tizen.org gerrit review --verified=+1 --code-review=+2 --submit c0ff33
```

##### Abandon a patch set

To drop an uploaded patch, just click the Abandon button at Web UI or use the command example, as shown below: for example:

```
 $ ssh review.tizen.org gerrit review --abandon c0ff33
```

##### More detailed instructions

For detailed instructions, you can get information from the '--help' command:

```
 $ ssh review.tizen.org gerrit --help
```

or refer to the [Gerrit Command Line](https://review.tizen.org/gerrit/Documentation/cmd-index.html)