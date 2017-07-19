# Building Packages Locally with GBS

## 1 Introduction

This document provides information about how to perform local build by using Git Build System (GBS), including the following:

- Preparations
- Building instructions
- Build concepts and tips

This document assumes that the instructions in the following documents have been read, well understood, and correctly followed:

- [Setting up Development Environment](https://source.tizen.org/documentation/developer-guide/environment-setup)
- [Installing Development Tools](https://source.tizen.org/documentation/developer-guide/step-step-instructions/installing-development-tools)
- [Cloning Tizen Source](https://source.tizen.org/documentation/developer-guide/step-step-instructions/cloning-tizen-source)

## 2 Building All Packages

This section describes how to build all packages required for image creation (Local full build).

To perform local full build, perform the following procedure:

**Note**:

- To get a transparent understanding of the local full build commands, refer to [Build Concepts](https://source.tizen.org/documentation/developer-guide/getting-started-guide/building-packages-locally-gbs#build-concepts).
- To speed up the build process when hardware allows, refer to [Speeding up Local Build](https://source.tizen.org/documentation/developer-guide/getting-started-guide/building-packages-locally-gbs#speeding-up-local-build).

1. Follow section 2.2 or section 3.2 in [Cloning Tizen Source](https://source.tizen.org/documentation/developer-guide/step-step-instructions/cloning-tizen-source) to clone source of all projects.

   Upon successful source code cloning, a full GBS configuration file named .gbs.conf is copied from the gbs-config project in Tizen [Project List](https://review.tizen.org/gerrit/#/admin/projects) to the top directory of <Tizen_Project> in which **repo sync** command is executed.

2. Switch to the directory that contains all Tizen projects.

   ```
   $ cd <Tizen_Project>
   ```

3. Configure the default .gbs.conf.

   (3-1) Add customized remote repo (mandatory).

   Default GBS configuration files for Tizen 3.0 common, IVI, and mobile verticals are shown below:

   - Common

     ```
     [general]tmpdir=/var/tmp/profile = profile.tizen3.0_commonwork_dir=. [repo.tizen3.0_x86]url=${work_dir}/pre-built/toolchain-x86/ [repo.tizen3.0_arm]url=${work_dir}/pre-built/toolchain-arm/ [profile.tizen3.0_common]repos=repo.tizen3.0_x86,repo.tizen3.0_armbuildconf=${work_dir}/scm/meta/build-config/build.conf # For wayland ia32# buildconf=${work_dir}/scm/meta/build-config/build-ia32-wayland.conf# For emulator32 wayland# buildconf=${work_dir}/scm/meta/build-config/build-emulator32-wayland.conf# For wayland x86_64# buildconf=${work_dir}/scm/meta/build-config/build-x86_64-wayland.conf# For wayland arm32# buildconf=${work_dir}/scm/meta/build-config/build-arm-wayland.conf# For wayland arm64# buildconf=${work_dir}/scm/meta/build-config/build-arm64-wayland.conf
     ```

   - Mobile

     ```
     [general]tmpdir=/var/tmp/profile = profile.tizen3.0_mobilework_dir=. [repo.tizen3.0_x86]url=${work_dir}/pre-built/toolchain-x86/ [repo.tizen3.0_arm]url=${work_dir}/pre-built/toolchain-arm/ [profile.tizen3.0_mobile]repos=repo.tizen3.0_x86,repo.tizen3.0_armbuildconf=${work_dir}/scm/meta/build-config/build.conf
     ```

   - IVI

     ```
     [general]tmpdir=/var/tmp/profile = profile.tizen3.0_iviwork_dir=. [repo.tizen3.0_x86]url=${work_dir}/pre-built/toolchain-x86/ [profile.tizen3.0_ivi]repos=repo.tizen3.0_x86buildconf=${work_dir}/scm/meta/build-config/build.conf
     ```

   For more information about remote repo customization, refer to [Available Branches and the Corresponding Remote Repos](https://source.tizen.org/documentation/developer-guide/getting-started-guide/building-packages-locally-gbs#available-branches-and-the-corresponding-remote-repos).

   For more information about .gbs.conf, refer to [GBS Configuration File](https://source.tizen.org/documentation/reference/git-build-system/configuration-file).

   (3-2) Specify the build.conf. (optional, only valid for Tizen 3.0 common)

   Choose and uncomment one of the following based on the variants, as appropriate:

   - wayland ia32

     buildconf=${work_dir}/scm/meta/build-config/build-ia32-wayland.conf

   - emulator32 wayland

     buildconf=${work_dir}/scm/meta/build-config/build-emulator32-wayland.conf

   - wayland x86_64

     buildconf=${work_dir}/scm/meta/build-config/build-x86_64-wayland.conf

   - wayland arm32

     buildconf=${work_dir}/scm/meta/build-config/build-arm-wayland.conf

   - wayland arm64

     buildconf=${work_dir}/scm/meta/build-config/build-arm64-wayland.conf

4. Build all packages required for image creation by executing one of the following commands, as appropriate:

   - armv7l

     ```
     $ accel_pkgs="bash,bzip2-libs,c-ares,cmake,coreutils,diffutils,eglibc,elfutils-libelf,elfutils-libs,elfutils,fdupes,file,findutils,gawk,gmp,gzip,libacl,libattr,libcap,libcurl,libfile,libgcc,liblua,libstdc++,make,mpc,mpfr,ncurses-libs,nodejs,nspr,nss-softokn-freebl,nss,openssl,patch,popt,rpm-build,rpm-libs,rpm,sed,sqlite,tar,xz-libs,zlib,binutils,gcc"$ gbs build -A armv7l --threads=4 --clean-once --exclude=${accel_pkgs},filesystem,aul,libmm-sound,libtool
     ```

   - i586

     ```
     $ gbs build -A i586 --threads=4 --clean-once --exclude=gcc,cmake,filesystem,aul,libmm-sound,libtool
     ```

    

5. For detailed information of Tizen branches, refer to [Available Branches and the Corresponding Remote Repos](https://source.tizen.org/documentation/developer-guide/getting-started-guide/building-packages-locally-gbs#available-branches-and-the-corresponding-remote-repos).

   - **Note:**:

     "--exclude" is unnecessary for Tizen 3.0.Starting from gbs 0.22, profile section in gbs.conf supports exclude_packages property, which can be used to set the list of packages to be excluded or to break dependency circle, that is, running the command below:`$ accel_pkgs="bash,bzip2-libs,c-ares,cmake,coreutils,diffutils,eglibc,elfutils-libelf,elfutils-libs,elfutils,fdupes,file,findutils,gawk,gmp,gzip,libacl,libattr,libcap,libcurl,libfile,libgcc,liblua,libstdc++,make,mpc,mpfr,ncurses-libs,nodejs,nspr,nss-softokn-freebl,nss,openssl,patch,popt,rpm-build,rpm-libs,rpm,sed,sqlite,tar,xz-libs,zlib,binutils,gcc"$ gbs build -A armv7l --threads=4 --clean-once --exclude=${accel_pkgs},filesystem,aul,libmm-sound,libtool`is equivalent to running the following command:`$ gbs build -A armv7l --threads=4 --clean-once`after adding the content below in gbs.conf:`[profile.tizen]exclude_packages=bash,bzip2-libs,c-ares,cmake,coreutils,diffutils,eglibc,elfutils-libelf,elfutils-libs,elfutils,fdupes,file,findutils,gawk,gmp,gzip,libacl,libattr,libcap,libcurl,libfile,libgcc,liblua,libstdc++,make,mpc,mpfr,ncurses-libs,nodejs,nspr,nss- softokn-freebl,nss,openssl,patch,popt,rpm-build,rpm-libs,rpm,sed,sqlite,tar,xz-libs,zlib,binutils,gcc,filesystem,aul,libmm-sound,libtool`

6. Take follow-up actions if necessary. For detailed information, refer to [Performing Another Build](https://source.tizen.org/documentation/developer-guide/getting-started-guide/building-packages-locally-gbs#performing-another-build).

## 3 Building Specific Package

This section describes how to build specific package.

To build package for specific project, perform the following procedure:

1. Follow section 3 in [Cloning Tizen Source](https://source.tizen.org/documentation/developer-guide/step-step-instructions/cloning-tizen-source) to clone source of specific project.

2. Switch to the directory that contains specific project.

   ```
   cd <Specific_Project>
   ```

3. Create GBS configuration file <Specific_Project>/.gbs.conf.

   An example of GBS configuration file for Tizen 3.0 is shown below:

   ```
   [general]tmpdir=/var/tmp/profile = profile.common.tizen3.0work_dir=. [repo.tizen3.0]url = https://download.tizen.org/snapshots/tizen/common/latest/repos/arm-wayland/packages/ [profile.common.tizen3.0]repos=repo.tizen3.0
   ```

   For more information about .gbs.conf, refer to [GBS Configuration File](https://source.tizen.org/documentation/reference/git-build-system/configuration-file).

   For more customization information about remote repo, refer to [Available Branches and the Corresponding Remote Repos](https://source.tizen.org/documentation/developer-guide/getting-started-guide/building-packages-locally-gbs#available-branches-and-the-corresponding-remote-repos).

4. Build package for this project.

   ```
   $ gbs build -A <Arch> --include-all
   ```

## 4 Appendix

This section provides supplementary information of local build, including the following:

- Available branches
- Build concept
- Build tips

### 4.1 Available Branches and the Corresponding Remote Repos

Available branches and the corresponding branch names and remote repos are as follows:

- **Tizen 3.0**

  - Branch name: tizen

  - Remote repos:

    - Common:

      Two types of remote repos are shown below, choose one of the following, as appropriate:

      - [http://download.tizen.org/snapshots/tizen/common/latest/repos/ia32-wayland/packages/](http://download.tizen.org/snapshots/tizen/common/latest/repos/ia32-wayland/packages/)
      - [http://download.tizen.org/snapshots/tizen/common/latest/repos/x86_64-wayland/packages/](http://download.tizen.org/snapshots/tizen/common/latest/repos/x86_64-wayland/packages/)

    - Mobile: [http://download.tizen.org/releases/daily/tizen/mobile/latest/](http://download.tizen.org/releases/daily/tizen/mobile/latest/)

    - IVI: [http://download.tizen.org/releases/daily/tizen/ivi/ivi-release/latest/](http://download.tizen.org/releases/daily/tizen/ivi/ivi-release/latest/)

  **Note:** latest in above remote repo url is a symblink in remote server, which is always linked to the latest new directory and may be changed any time, so make sure to use the latest repo with specific date to guarantee the usability. An example is shown below: [http://download.tizen.org/snapshots/tizen/common/latest/repos/arm-waylan...](http://download.tizen.org/snapshots/tizen/common/latest/repos/arm-wayland/packages/)

### 4.2 Concepts of GBS Build

The build concepts that help developers transparently understand the full build commands are as follows:

- **Prebuilt Binary Packages**

  The <Tizen_Project>/pre-built directory contains a group of prebuilt projects that provides base and toolchain binary RPM packages for GBS build.

- **Cycles in Repos**

  Building packages with dependency cycles is not supported by GBS. Known cycles are as follows:

  ```
  gcc->eglibc->gccgcc->binutils->gettext->gccgettext->gcc->eglibc->gettextcmake->curl->c-ares->cmakefilesystem->setup->filesystemaul->privacy-manager-server->aullibtool->texinfo->libzio->bzip2->libtoollibmm-sound->avsystem->pulseaudio->system-server->libfeedback->libmm-sound
  ```

Besides toolchain in Tizen packages, there are several cycles that can't be detected by GBS without binary RPM. Therefore, a remote repo needs to be added in .gbs.conf.

To continue the build by breaking the dependency cycles, add "--exclude" option to exclude specific packages when running **gbs build** command, or specify the excluded packages list in profile section of gbs.conf with exclude_packages property.

- **Accelerator Packages**

  Tizen provides cross-compilers and other accelerator packages, as shown below, in <Tizen_Project>/pre-built/toolchain-arm/ for ARM build.

  ```
  bash,bzip2-libs,c-ares,cmake,coreutils,diffutils,eglibc,elfutils-libelf,elfutils-libs,elfutils,fdupes,file,findutils,gawk,gmp,gzip,libacl,libattr,libcap,libcurl,libfile,libgcc,liblua,libstdc++,make,mpc,mpfr,ncurses-libs,nodejs,nspr,nss-softokn-freebl,nss,openssl,patch,popt,rpm-build,rpm-libs,rpm,sed,sqlite,tar,xz-libs,zlib,binutils,gcc
  ```

For the first build, these packages need to be excluded, otherwise built out packages will be installed and used, which will make accelerator packages fail to work.

### 4.3 Build Tips

The build tips include the following:

- How to speed up local build
- How to perform another build

#### 4.3.1 Speeding up Local Build

If the size of the RAM and swap are all larger than 8G, mount GBS BUILD-ROOTS as tmpfs to speed up building:

```
$ mkdir -p ~/GBS-ROOT/local/BUILD-ROOTS$ sudo mount -t tmpfs -o size=16G tmpfs ~/GBS-ROOT/local/BUILD-ROOTS
```

#### 4.3.2 Performing Another Build

When the result of the first build is unsatisfactory, perform another build by executing one of the following commands, as appropriate:

- The first scenario meets the following conditions:

  - The URL of the remote repo is the same as in the previous build.
  - New packages to be built are dependent on previously built packages.
  - Users want previously built packages to participate in the new build.

  ```
  $ gbs build -A <Arch>
  ```

- The second scenario meets the following conditions:

  - The URL of the remote repo is the same as in the previous build.
  - New packages to be built are dependent on previously built packages.
  - Users want previously built packages to participate in the new build.

  ```
  $ gbs build -A <Arch>
  ```

- The third scenario meets the following conditions:

  - The URL of the remote repo is the same as in the previous build.
  - New packages to be built are dependent on previously built packages.
  - Users do not want previously built packages to participate in the new build.

  ```
  $ gbs build -A <Arch> --clean-repos
  ```

- The fourth scenario meets the following conditions:

  - The URL of the remote repo is changed.
  - New packages to be built are not dependent on previously built packages.

  ```
  $ gbs build -A <Arch> --clean
  ```

- The fifth scenario meets the following conditions:

  - The URL of the remote repo is changed.
  - New packages to be built are dependent on previously built packages.
  - Users want previously built packages to participate in the new build.

  ```
  $ gbs build -A <Arch> --clean
  ```

- The sixth scenario meets the following conditions:

  - The URL of the remote repo is changed.
  - New packages to be builtare dependent on previously built packages.
  - Users do not want previously built packages to participate in the new build.

  ```
  $ gbs build -A <Arch> --clean --clean-repos
  ```

The building directory during runtime is ~/GBS-ROOT/local/BUILD-ROOTS/scratch.`<Arch>.<Number_of_Threads>`, into which the following input related to current build is loaded to construct an independent building environment:

- Source code in ~/tizen
- Local RPM packages in ~/GBS-ROOT/local/repos/<Release_ID>/<Arch>
- Remote RPM packages in [http://download.tizen.org/releases/](http://download.tizen.org/releases/)<Tizen_Version>/<Release_ID>

Upon successful building, GBS moves the generated RPM packages into the output directory, ~/GBS-ROOT/local/repos/<Release_ID>/<Arch>, the content of which will automatically participate in a new build, if any, and may have potential impact on the new build, depending on the dependency between the existing packages and new packages to be built.

Based on the above working mechanism of the GBS build, the following rules must be followed to guarantee the quality of new build:

- Add "--clean" once the URL of the remote repo is changed.
- Add "--clean-repos" if new packages to be built are dependent on the previously built packages that users do not want to involve into the new build.