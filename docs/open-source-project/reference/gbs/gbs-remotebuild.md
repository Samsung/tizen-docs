# gbs remotebuild

Use the `gbs remotebuild` subcommand to push local Git code to a remote OBS build server to build.

For command usage details, enter:

```bash
$ gbs remotebuild --help
```

To perform  a remote build:

1. Prepare a Git repository package.

   The packaging directory must exist and have a spec file in it. GBS uses the package name, version, and source tarball format defined in the spec file.

1. When the spec file is ready, go to the top directory of the Git repository, and run the `gbs remotebuild` subcommand.

   The following code gives some command examples:

   ```bash
   $ gbs remotebuild
   $ gbs remotebuild -B Tizen:Main
   $ gbs remotebuild -B Tizen:Main -T home:<userid>:gbs
   $ gbs remotebuild -B Tizen:Main --status
   $ gbs remotebuild -B Tizen:Main --buildlog -R <repo> -A <arch>
   $ gbs remotebuild -B Tizen:Main --include-all
   ```

You can check the build log and build status during the remote build with the `--buildlog` and `--status` options:

1. Submit the changes to the remote OBS using the `gbs remotebuild` subcommand.

   For example, to submit a package to home:user:gbs:Tizen:Main and build against Tizen:Main:

   ```bash
   test@test-desktop:~/ail$ gbs remotebuild -B Tizen:Main --include-all
   info: Creating (native) source archive ail-0.2.29.tar.gz from 'c7309adbc60eae08782b51470c20aef6fdafccc0'
   info: checking status of obs project: home:test:gbs:Tizen:Main ...
   info: commit packaging files to build server ...
   info: local changes submitted to build server successfully
   info: follow the link to monitor the build progress:
   https://build.tizendev.org/package/show?package=ail&project=home:test:gbs:Tizen:Main
   ```

1. Check the build status:

   ```bash
   # -B or -T options is needed if your target project is not home:user:gbs:Tizen:Main
   test@test-desktop:~/ail$ gbs remotebuild --status
   info: build results from build server:
   standard       i586           building
   standard       armv7el        building
   ```

   The first column is the repository name and the second column is the architecture.

1. Check the build log for specific repository and architecture:

   ```bash
   test@test-desktop:~/ail$ gbs remotebuild --buildlog
   error: please specify arch(-A) and repository(-R)
   test@test-desktop:~/ail$ gbs remotebuild --buildlog -A i586 -R standard
   info: build log for home:test:gbs:Tizen:Main/ail/standard/i586
   ```
