# gbs remotebuild

Use the remotebuild subcommand to push local git code to the remote OBS build server to build. For instructions on using the remotebuild subcommand, use this command:

```bash
$ gbs remotebuild --help
```

Before running gbs remotebuild, you need to prepare a git repository package. The packaging directory must exist and have a spec file in it. GBS uses the package name, version, and source tarball format defined in this spec file. When it's ready, go to the top directory of git repository, and run gbs remotebuild, here's some examples

```bash
$ gbs remotebuild
$ gbs remotebuild -B Tizen:Main
$ gbs remotebuild -B Tizen:Main -T home:<userid>:gbs
$ gbs remotebuild -B Tizen:Main --status
$ gbs remotebuild -B Tizen:Main --buildlog -R <repo> -A <arch>
$ gbs remotebuild -B Tizen:Main --include-all
```

check build log and build status gbs supports the developer checking the build log and build status using the --buildlogand --status options during gbs remotebuild. 
**For example:**
1. Submit the changes to the remote OBS using gbs remotebuild. For example: Submit package to home:user:gbs:Tizen:Main, build against Tizen:Main

  ```bash
  test@test-desktop:~/ail$ gbs remotebuild -B Tizen:Main --include-all
  info: Creating (native) source archive ail-0.2.29.tar.gz from 'c7309adbc60eae08782b51470c20aef6fdafccc0'
  info: checking status of obs project: home:test:gbs:Tizen:Main ...
  info: commit packaging files to build server ...
  info: local changes submitted to build server successfully
  info: follow the link to monitor the build progress:
  https://build.tizendev.org/package/show?package=ail&project=home:test:gbs:Tizen:Main
  ```

2. Check the build status, example:

  ```bash
  # -B or -T options is needed if your target project is not home:user:gbs:Tizen:Main
  test@test-desktop:~/ail$ gbs remotebuild --status
  info: build results from build server:
  standard       i586           building
  standard       armv7el        building
  ```

The first column is repo name and the second column is arch. repo/arch can be used to get buildlog. Step 3: Check the build log for special repo/arch

```bash
test@test-desktop:~/ail$ gbs remotebuild --buildlog
error: please specify arch(-A) and repository(-R)
test@test-desktop:~/ail$ gbs remotebuild --buildlog -A i586 -R standard
info: build log for home:test:gbs:Tizen:Main/ail/standard/i586
....
```

 