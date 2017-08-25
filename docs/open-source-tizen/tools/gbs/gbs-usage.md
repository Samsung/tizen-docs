# GBS Usage

This section provides more details about GBS usage. You can also use $ gbs --help or $ gbs <subcmd> --help to get the help message.

To get help:

- For global options and the command list:

```
$ gbs  -h | --help
```

- For each sub-command:

```
$ gbs <sub-command> --help
```

GBS provides several subcommands, including:

- [gbs clone](https://source.tizen.org/documentation/reference/git-build-system/usage/gbs-clone): clone a git repository representing a package managed with gbs
- [gbs pull](https://source.tizen.org/documentation/reference/git-build-system/usage/gbs-pull): update a git repository representing a package managed with gbs
- [gbs devel](https://source.tizen.org/documentation/reference/git-build-system/usage/gbs-devel): facilitates package maintainers to better maintain package in the orphan-packaging branch model by providing five actions, including 'start', 'export', 'drop', 'switch', and 'convert'.
- [gbs build](https://source.tizen.org/documentation/reference/git-build-system/usage/gbs-build): build rpm package from git repositories at the local development environment
- [gbs remotebuild](https://source.tizen.org/documentation/reference/git-build-system/usage/gbs-remotebuild): generate tarballs based on Git repositories, and upload to remote OBS to build rpm packages
- [gbs submit](https://source.tizen.org/documentation/reference/git-build-system/usage/gbs-submit): create/push annotate tag to Gerrit and trigger code submission to remote OBS
- [gbs chroot](https://source.tizen.org/documentation/reference/git-build-system/usage/gbs-chroot): chroot to build root
- [gbs import](https://source.tizen.org/documentation/reference/git-build-system/usage/gbs-import/): import source code to git repository, supporting these formats: source rpm, specfile, and tarball
- [gbs export](https://source.tizen.org/documentation/reference/git-build-system/usage/gbs-export): export files and prepare for building package, the spec file defines the format of tarball
- [gbs changelog](https://source.tizen.org/documentation/reference/git-build-system/usage/gbs-changelog): update the changelog file with git commits message

 