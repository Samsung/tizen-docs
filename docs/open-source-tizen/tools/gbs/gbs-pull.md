# gbs pull

Use the `gbs pull` subcommand to update from a remote Git repository being maintained with GBS. Always do your local development on the feature and development branches, and keep the master and upstream branches untouched and always in sync with the remote by using this command.

The benefit of using the `gbs pull` subcommand is that it automatically updates all relevant branches, including the upstream and pristine-tar branches in the case of non-native packages.

The command updates all local branch HEADs that can be fast-forwarded. It prints a warning for branches that cannot be fast-forwarded. To override the warning, use the `--force` option described below.

For command usage details, enter:

```bash
$ gbs pull --help
```

Examples:

- Update a Tizen package repository:

  ```bash
  $ gbs pull
  info: updating from remote
  .....
  info: Updating 'master'
  Updating 30e59a6..7ae7fc7
  Fast-forward
  info: finished
  ```

## Special Options

You can use some special options with the `gbs pull` subcommand:

- `--all` updates all remote branches. It updates all remote-tracking branches that have an identical name in the remote repository.
- `--depth` deepens shallow clones, that is, fetches deeper history from the remote.
- `--force` forces the local branch HEADs to update to match the remote repository.
  > **WARNING**:
  >
  > Use the `--force` option with care. It discards all local changes to the updated branches. This effectively performs a `git reset --hard` for the local branches.

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


