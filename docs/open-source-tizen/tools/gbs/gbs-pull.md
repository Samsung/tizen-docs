# gbs pull

The pull command makes it more convenient for a developer to update from a remote git repository being maintained with gbs. The benefit of using gbs pull is that it automatically updates all relevant branches, the upstream and pristine-tar branches in the case of non-native packages. The pull subcommand will update all local branch HEADs that can be fast-forwarded. It will print a warning for branches that could not be fast-forwarded. See the --force option below to override this. It is recommended to always do your local development on feature/development branches, and keep the master/upstream branches untouched and always in sync with the remote by using the gbs pull command. For instructions on using the pull subcommand, type:

```bash
$ gbs pull --help
```

Example: update a tizen package repo using gbs pull

```bash
$ gbs pull
info: updating from remote
.....
info: Updating 'master'
Updating 30e59a6..7ae7fc7
Fast-forward
info: finished
```

### Special options

The --all option can be used to update all remote branches. Using this will update all remote-tracking branches that have identical name in the remote repository. Using the --depth one can deepen shallow clones, that is, fetch deeper history from the remote. With the --force option the developer can force update the local branch HEADs to match the remote repo. **WARNING**: Use the --force option with care. It will discard all local changes to the updated branches! This effectively does a git reset --hard for the local branches. Example:

```bash
$ gbs pull --all
info: updating from remote
.....
info: Branch '1.0_post' is already up to date.
warning: Skipping non-fast forward of '2.0alpha' - use --force or update manually
info: Updating 'master'
Updating 30e59a6..7ae7fc7
Fast-forward
error: Failed to update some of the branches!
$ gbs pull --all --force
info: updating from remote
......
info: Branch '1.0_post' is already up to date.
info: Checking out clean copy of '2.0alpha' due to --force=clean
info: Updating '2.0alpha'
info: Branch 'master' is already up to date.
info: finished
```

 
