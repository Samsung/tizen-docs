# Building Packages Locally with GBS

You can perform local builds using the Git Build System (GBS).

Before performing local builds, study the following instructions:

- [Setting up the Development Environment](setting-up.md)
- [Installing Development Tools](installing.md)
- [Cloning Tizen Source Files](cloning.md)

To build a package for a specific project:

1. To clone the source of a specific project, follow the instructions in [Cloning Tizen Source Files](cloning.md).
2. Switch to the directory that contains the project:

   ```bash
   $ cd <Specific_Project>
   ```
3. Create a  `<Specific_Project>/.gbs.conf` GBS configuration file (optional).

   If a `<Specific_Project>/.gbs.conf` file exists, the configuration in that file is used when building the project with GBS. If not, the default GBS configuration in the `~/.gbs.conf` file is used.

   For more information about the `.gbs.conf` file and the customization of remote repositories, see [GBS Configuration](../reference/gbs/gbs.conf.md) and [Setting up the Development Environment](setting-up.md), respectively.

4. Build a package for the project:

   ```bash
   $ gbs build <gbs build option>
   ```
5. Take follow-up actions, if necessary. For more information, see [Performing Another Build](#performing-another-build).

## Build Tips

The build tips for local builds include:

- How to [exclude specific packages](#excluding-specific-packages).
- How to [speed up a local build](#speeding-up-a-local-build).
- How to [perform another build](#performing-another-build).

### Excluding Specific Packages

To exclude specific packages when building locally with GBS, you can either list them in the `--exclude` argument of the `gbs build` command, or list them in the `.gbs.conf` file:

- To exclude packages when running the `gbs build` command, use the `--exclude` build argument:
  ```bash
  $ exclude_pkgs="aaa bbb ccc ddd"
  $ gbs build -A armv7l --exclude=${exclude_pkgs},eee,fff
  ```
- To specify a list of excluded packages in the `.gbs.conf` file, use the `excluded_packages` parameter inside a profile block:
  ```
  [profile.unified_standard]
  repos = repo.base_arm,repo.base_arm_debug,repo.base_arm64,repo.base_arm64_debug,repo.base_ia32,repo.base_ia32_debug,repo.base_x86_64,repo.base_x86_64_debug,repo.unified_standard,repo.unified_standard_debug
  exclude_packages=aaa,bbb,ccc,ddd,eee,fff
  ```

### Speeding up a Local Build

If the size of your RAM and swap file are both larger than 8 GB, you can speed up building by creating a GBS `BUILD-ROOTS` directory and mounting it as a RAM disk:

```bash
$ mkdir -p ~/GBS-ROOT/local/BUILD-ROOTS
$ sudo mount -t tmpfs -o size=16G tmpfs ~/GBS-ROOT/local/BUILD-ROOTS
```

### Performing Another Build

When the result of the first build is unsatisfactory, perform another build by executing 1 of the following commands, as appropriate:

- Scenario 1:
  - The URL of the remote repository is the same as in the previous build.
  - New packages to be built are dependent on previously built packages.
  - You want previously built packages to participate in the new build.

  ```bash
  $ gbs build -A <Arch>
  ```

- Scenario 2:
  - The URL of the remote repository is the same as in the previous build.
  - New packages to be built are dependent on previously built packages.
  - You do not want previously built packages to participate in the new build.

  ```bash
  $ gbs build -A <Arch> --clean-repos
  ```

- Scenario 3:

  - The URL of the remote repository has changed.
  - New packages to be built are not dependent on previously built packages.

  ```bash
  $ gbs build -A <Arch> --clean
  ```

- Scenario 4:
  - The URL of the remote repository has changed.
  - New packages to be built are dependent on previously built packages.
  - You want previously built packages to participate in the new build.

  ```bash
  $ gbs build -A <Arch> --clean
  ```

- Scenario 5:
  - The URL of the remote repository has changed.
  - New packages to be built are dependent on previously built packages.
  - You do not want previously built packages to participate in the new build.

  ```bash
  $ gbs build -A <Arch> --clean --clean-repos
  ```

The building directory during runtime is `~/GBS-ROOT/local/BUILD-ROOTS/scratch.<Arch>.<Number_of_Threads>`, into which the following input related to the current build is loaded to construct an independent building environment:

- Source code in `<Specific_Project>`
- Local RPM packages in `~/GBS-ROOT/local/repos/<Release_ID>/<Arch>`
- Remote RPM packages in a repository URL inside the GBS configuration file. For example: `http://download.tizen.org/releases/daily/tizen/<Tizen_Profile>/<Release_ID>/repos/<Repository>/packages/`

After a successful build, GBS moves the build result, including generated RPM packages, SRPM packages, and build logs, into the output directory, `~/GBS-ROOT/local/repos/<Release_ID>/<Arch>`. The output directory content automatically participates in a new build, if any, and can have a potential impact on the new build, depending on the dependency between the existing packages already built and new packages to be built. For example:

- Suppose package B has a dependency on package A, which means in package B building, `A-1.rpm` in the remote repository is used.
- Build package A first.
- `A-2.rpm` is generated under `~/GBS-ROOT/`.
- Build package B.
- `A-2.rpm` under `~/GBS-ROOT/` is used in package B building, instead of `A-1.rpm` in the remote repository.

Based on the above working mechanism of the GBS build, the following rules must be followed for the `gbs build`command to guarantee the quality of the new build:

- If the URL of the remote repository has changed, add the `--clean` parameter. If this parameter is given, the current `~/GBS-ROOT/local/BUILD-ROOTS/scratch.<Arch>.<Number_of_Threads>` directory is cleaned up, to remove previously constructed GBS build environment.
- If new packages to be built are dependent on the previously built packages that you do not want to involve in the new build, add the `--clean-repos` parameter. If this parameter is given, the current `~/GBS-ROOT/local/repos/<Release_ID>/<Arch>` directory is cleaned up, to remove previously built packages.
