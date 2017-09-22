# Building Packages Locally with GBS

This topic provides information about how to perform local builds using the Git Build System (GBS).

You must read, understand, and correctly follow the instructions in the following documents before performing local builds:

- [Setting up Development Environment](setting-up.md)
- [Installing Development Tools](installing.md)
- [Cloning Tizen Source Files](cloning.md)

## Building a Package for a Specific Project

1. To clone the source of a specific project, follow the instructions in [Cloning Tizen Source Files](cloning.md).

2. Switch to the directory that contains the project:

   ```bash
   $ cd <Specific_Project>
   ```

3. Create a  `<Specific_Project>/.gbs.conf` GBS configuration file (optional).

   If a `<Specific_Project>/.gbs.conf` file exists, the configuration in that file is used when building the project with GBS. If not, the default GBS configuration in `~/.gbs.conf` is used.

   For more information about `.gbs.conf`, see [Configuration File](../tools/gbs/gbs.conf.md).

   For more customization information on remote repositories, see [Setting up Development Environment](setting-up.md).

4. Build a package for the project:

   ```bash
   $ gbs build <gbs build option>
   ```

5. Take followup actions, if necessary. For more information, see [Performing Another Build](#id4).

## Build Tips

The build tips for local builds include:

- How to exclude specific packages.
- How to speed up a local build.
- How to perform another build.

### Excluding Specific Packages <a name="id3"></a>

To exclude specific packages when building locally with GBS, you can either list them in the gbs build argument, which is `--exclude` , or list them in the `.gbs.conf` file. For example:

- To exclude packages when running `gbs build`, use the `--exclude` build argument:
  ```bash
  $ exclude_pkgs="aaa bbb ccc ddd"
  $ gbs build -A armv7l --exclude=${exclude_pkgs},eee,fff
  ```
- To specify a list of excluded packages in `.gbs.conf`, use the `excluded_packages` parameter inside a profile block:
  ```
  [profile.unified_standard]
  repos = repo.base_arm,repo.base_arm_debug,repo.base_arm64,repo.base_arm64_debug,repo.base_ia32,repo.base_ia32_debug,repo.base_x86_64,repo.base_x86_64_debug,repo.unified_standard,repo.unified_standard_debug
  exclude_packages=aaa,bbb,ccc,ddd,eee,fff
  ```

### Speeding up a Local Build <a name="speed"></a>

If the size of your RAM and swap file are both larger than 8 gigabytes, create a GBS `BUILD-ROOTS` directory and mount it as a RAM disk to speed up building:

```bash
$ mkdir -p ~/GBS-ROOT/local/BUILD-ROOTS
$ sudo mount -t tmpfs -o size=16G tmpfs ~/GBS-ROOT/local/BUILD-ROOTS
```

### Performing Another Build <a name="id4"></a>

When the result of the first build is unsatisfactory, perform another build by executing one of the following commands, as appropriate:

- Scenario 1:
  - The URL of the remote repo is the same as in the previous build.
  - New packages to be built are dependent on previously built packages.
  - You want previously built packages to participate in the new build.

  ```bash
  $ gbs build -A <Arch>
  ```

- Scenario  2:
  - The URL of the remote repo is the same as in the previous build.
  - New packages to be built are dependent on previously built packages.
  - You do not want previously built packages to participate in the new build.

  ```bash
  $ gbs build -A <Arch> --clean-repos
  ```

- Scenario 3:

  - The URL of the remote repo is changed.
  - New packages to be built are not dependent on previously built packages.

  ```bash
  $ gbs build -A <Arch> --clean
  ```

- Scenario 4:
  - The URL of the remote repo is changed.
  - New packages to be built are dependent on previously built packages.
  - You want previously built packages to participate in the new build.

  ```bash
  $ gbs build -A <Arch> --clean
  ```

- Scenario 5:
  - The URL of the remote repo is changed.
  - New packages to be built are dependent on previously built packages.
  - You do not want previously built packages to participate in the new build.

  ```bash
  $ gbs build -A <Arch> --clean --clean-repos
  ```

The building directory during runtime is `~/GBS-ROOT/local/BUILD-ROOTS/scratch.<Arch>.<Number_of_Threads>`, into which the following input related to the current build is loaded to construct an independent building environment:

- Source code in `<Spcific_Project>`
- Local RPM packages in `~/GBS-ROOT/local/repos/<Release_ID>/<Arch>`
- Remote RPM packages in repo url inside GBS configuration file. For example:  `http://download.tizen.org/releases/daily/tizen/<Tizen_Profile>/<Release_ID>/repos/<Repository>/packages/`

After a successful build, GBS moves the build results including generated RPM packages, SRPM packages and build logs into the output directory, `~/GBS-ROOT/local/repos/<Release_ID>/<Arch>`. The output directory content automatically participates in a new build, if any, and can have a potential impact on the new build, depending on the dependency between the existing packages already built and new packages to be built. For example:

- Suppose package B has a dependency on package A, which means in package B building, A-1.rpm in remote repo will be used.
- Build package A first.
- A-2.rpm is generated under ~/GBS-ROOT/
- Build package B.
- A-2.rpm under ~/GBS-ROOT/ will be used in package B building,  instead of A-1.rpm in remote repo.

Based on the above working mechanism of the GBS build, the following rules must be followed for the `gbs build`command to guarantee the quality of new build:

- Add the `--clean` parameter, if the URL of the remote repo is changed. If this parameter is given, current  `~/GBS-ROOT/local/BUILD-ROOTS/scratch.<Arch>.<Number_of_Threads>` will be cleaned up, so previously constructed GBS build environment will be removed.
- Add the `--clean-repos` parameter, if new packages to be built are dependent on the previously built packages that you do not want to involve in the new build. If this parameter is given,  current `~/GBS-ROOT/local/repos/<Release_ID>/<Arch>` will be cleaned up, so previously built packages will be removed.
