# GBS Reference

This section provides more details about GBS usage. You can also use $ gbs --help or $ gbs <subcmd> --help to get the help message.

To get help:

- For global options and the command list:

  ```bash
  $ gbs  -h | --help
  ```

- For each sub-command:

  ```bash
  $ gbs <sub-command> --help
  ```

GBS provides several subcommands, including:

- [gbs clone](gbs-clone.md): clone a git repository representing a package managed with gbs
- [gbs pull](gbs-pull.md): update a git repository representing a package managed with gbs
- [gbs devel](gbs.devel.md): facilitates package maintainers to better maintain package in the orphan-packaging branch model by providing five actions, including 'start', 'export', 'drop', 'switch', and 'convert'.
- [gbs build](gbs-build.md): build rpm package from git repositories at the local development environment
- [gbs remotebuild](gbs-remotebuild.md): generate tarballs based on Git repositories, and upload to remote OBS to build rpm packages
- [gbs submit](gbs-submit.md): create/push annotate tag to Gerrit and trigger code submission to remote OBS
- [gbs chroot](gbs-chroot.md): chroot to build root
- [gbs import](gbs-import.md): import source code to git repository, supporting these formats: source rpm, specfile, and tarball
- [gbs export](gbs-export.md): export files and prepare for building package, the spec file defines the format of tarball
- [gbs changelog](gbs-changelog.md): update the changelog file with git commits message


