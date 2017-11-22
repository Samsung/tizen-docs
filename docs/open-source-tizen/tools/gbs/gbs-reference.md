# GBS Reference

To manage GBS operations, use the following GBS subcommands:

- [gbs clone](gbs-clone.md): clone a Git repository representing a package managed with GBS
- [gbs pull](gbs-pull.md): update a Git repository representing a package managed with GBS
- [gbs devel](gbs-devel.md): facilitate package maintainers in maintaining a package in the orphan-packaging branch model by providing 5 actions, including `start`, `export`, `drop`, `switch`, and `convert`.
- [gbs build](gbs-build.md): build an RPM package from Git repositories at the local development environment
- [gbs remotebuild](gbs-remotebuild.md): generate tarballs based on Git repositories, and upload to remote OBS to build RPM packages
- [gbs submit](gbs-submit.md): create and push an annotate tag to Gerrit and trigger code submission to remote OBS
- [gbs chroot](gbs-chroot.md): chroot to build root
- [gbs import](gbs-import.md): import source code to a Git repository, supporting the following formats: source rpm, specfile, and tarball
- [gbs export](gbs-export.md): export files and prepare for building package; the spec file defines the format of tarball
- [gbs changelog](gbs-changelog.md): update the change log file with a Git commit message


To access GBS help:

- For global options and the command list:

  ```bash
  $ gbs  -h | --help
  ```

- For each sub-command:

  ```bash
  $ gbs <sub-command> --help
  ```
