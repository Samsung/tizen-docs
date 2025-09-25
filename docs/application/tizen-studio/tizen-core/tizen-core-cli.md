# Tizen-Core Command Line Interface Commands

The Tizen-Core Command Line Interface (CLI) provides functionalities for developing Tizen applications using the terminal. It includes the entire development process from creating the project to running the application.

The CLI is located in the `$<TIZEN_STUDIO>/tools/tizen-core/` directory. For developing an application using the CLI, add the CLI directory path to the `$PATH` environment variable using the following command:

```
export PATH=$PATH:$<TIZEN_STUDIO>/tools/tizen-core/
```
## List profile templates

The following command displays the list of project templates for all the versions of the given workspace type. By default, it displays all the available templates:

**Syntax:**

```
tz list templates [options]
```

**Options:**

| Option           | Description                              |
|------------------|------------------------------------------|
| `-t`, `--type=STRING` | Display all the templates for given profile [native/web/dotnet/rpk]. |

**Examples:**

- List of all the Native application templates:

  Windows&reg;, Ubuntu, and macOS:

  ```
  > tz list templates -t native
  tizen-9.0:
    basic-edc-ui [native_app]
    basic-ui [native_app]
    ComponentBasedApp [native_app]
    downloadable-font [native_app]
    gtest [native_app]
    IMEApplication [native_app]
    ServiceApp [native_app]
    SharedLibrary [native_app]
    StaticLibrary [native_app]
    widgetapp [native_app]
  
  > tz list templates -t web
  tizen-9.0:
    Addon [web_app]
    Basic [web_app]
    Companion [web_app]
    WebClip [web_app]
    WebService [web_app]
  ```

## List installed rootstraps

The following command displays a list of all the installed rootstraps in Tizen Studio:

Windows&reg;, Ubuntu, and macOS:
```
tz list rootstraps
[ROOTSTRAP]                              [Information]
tizen-9.0-device.core                    Tizen 9.0, armel
tizen-9.0-device64.core                  Tizen 9.0, aarch64
tizen-9.0-emulator.core                  Tizen 9.0, i586
tizen-9.0-emulator64.core                Tizen 9.0, x86_64
```

## List Emulators

The following command displays the list of Emulators available for all the installed profiles:

**Syntax:**

```
tz emul list-vm [options]
```

**Options:**

| Option           | Description                              |
|------------------|------------------------------------------|
| `-d`, `--type=STRING` | Print details of the VM. |
| `-P`, `--type=STRING` | List VMs for specified PROFILE. |

**Examples:**

- List of all the installed Emulators:

  Windows&reg;, Ubuntu, and macOS:

  ```
  > tz emul list-vm
  T-9.0-x86
  T-9.0-x86_64
  T-samsung-8.0-x86
  ```

## Launch Emulator

The following command is used to launch the installed Emulators:

**Syntax:**

```
tz emul launch [options]
```

**Options:**

| Option           | Description                              |
|------------------|------------------------------------------|
| `-n`, `--name=STRING` | name of the emulator to launch. |

**Examples:**

- Launch Emulator:

  Windows&reg;, Ubuntu, and macOS:

  ```
  > tz emul launch -n T-9.0-x86
  ```

## Create a Tizen project

The following command creates a Tizen native/web/dotnet/resource project from a template in the given directory:

**Syntax:**

```
tz new [options]
```

**Options:**

| Option                 | Description                              |
|------------------------|------------------------------------------|
| `-t`, `--template=STRING`     | Specifies the template name (Required) |
| `-n`, `--project=STRING`      | Specifies the project name (Required) |
| `-w`, `--ws-dir=STRING`       | Specifies the directory where project has to be created. By default it will be current directory |
| `-T`, `--type=STRING`         | Specifies the profile type (Required) [native/web/dotnet/rpk] |
| `-p`, `--profile=STRING`      | Specify the profile name (Required) |

**Examples:**

- Create a native project based on the basic UI native template in the given directory:

  Windows&reg;:
  ```
  > tz new -t basic_ui -n basicnative -T native -p tizen-9.0 -w C:\Users\workspace
  ```

  Ubuntu and macOS:
  ```
  $ tz new -t basic_ui -n basicnative -T native -p tizen-9.0 -w  ~/workspace
  ```

- Create a web project based on the basic UI web template in the workspace.

  Windows&reg;:
  ```
  > tz new -t Basic -n basicweb -T web -p tizen-9.0 -w C:\Users\workspace
  ```

  Ubuntu and macOS:
  ```
  $ tz new -t Basic -n basicweb -T web -p tizen-9.0 -w  ~/workspace
  ```

- Create a dotnet project based on the NUIAPP template in the workspace:

  Windows&reg;:
  ```
  > tz new -t TizenNUIApp -n nuiapp -T dotnet -p tizen-9.0 -w C:\Users\workspace
  ```

  Ubuntu and macOS:
  ```
  $ tz new -t TizenNUIApp -n nuiapp -T dotnet -p tizen-9.0 -w ~/workspace
  ```

## Set global and project configuration options

The following command displays and sets the global and project configuration options. For setting or getting project configurations, project path is mandatory:

**Syntax:**

```
tz set [options]
```

**Options:**

| Option                 | Description                              |
|------------------------|------------------------------------------|
|  `--help`                                                          | Show context-sensitive help. |
|  `--version`                                                       | Print version information and quit. |
|  `-w`, `--proj-dir="."`                                            | Specify the project path (Required for Project). |
|  `-x`, `--profiles-path="-"`                                       | Path of profiles.xml containing the signing profiles (Global). |
|  `-s`, `--signing-profile="-"`                                     | Signing profile used for Tizen packaging (Project). |
|  `-b`, `--build-type=STRING`                                       | Specifies the build type (debug/release/test)(Project). |
|  `-r`, `--rootstrap=STRING`                                        | Rootstrap used for compiling native app (Project). |
|  `-c`, `--compiler=STRING    `                                     | Compiler for native app compilation [gcc/llvm](project). |
|  `-d`, `--dotnet-cli-path=STRING`                                  | Path of dotnet-cli (Global). |
|  `-m`, `--msbuild-path=STRING`                                     | Path of msbuild (Global). |
|  `-D`, `--dotnet-build-tool=STRING          `                      | Tool for dotnet project build [msbuild/dotnet](Global). |
|  `-A`, `--arch=STRING           `                                  | Specifies the architecture for build [arm/aarch64/x86/x86_64](Project). |
|  `-S`, `--src-file-patterns=SRC-FILE-PATTERNS,...`                 | Source file patterns excluded from build, format: pattern1, pattern2 (Project). |
|  `-T`, `--test-file-patterns=TEST-FILE-PATTERNS,...`               | Source file patterns included for test mode, format: pattern1, pattern2 (Project). |
|  `-C`, `--chrome-path=STRING`                                      | Path of the Chrome executable (Global). |
|  `-V`, `--tv-simulator-path=STRING`                                | Path of tv-simulator (Global). |
|  `-L`, `--chrome-inspector-options=CHROME-INSPECTOR-OPTIONS,...`   | List of options for Chrome inspector, format: arg1, arg2 (Global). |
|  `-e`, `--chrome-inspector-data-path=STRING`                       | Path of Chrome inspector data (Global). |
|  `-O`, `--optimize=STRING`                                         | Size optimization of `wgt` for web projects [true/false](project). |
|  `-o`, `--output-path=STRING`                                      | Output Path for project. |


**Examples:**

- Project - set llvm, arm and release type for the project, use the following command:
  
  Windows&reg;:
  ```
  > tz set -A arm -c llvm -b release -w C:\Users\workspace\basicnative
  ```

  Ubuntu and macOS:
  ```
  $ tz set -A arm -c llvm -b release -w ~/workspace/basicnative
  ```
- Global - set dotnet build tool:
  
  ```
  > tz set -D msbuild
  ```

- Displays the list of all configurations for the given workspace. Individual options can be displayed by passing the required option flag:

  ```
  tz get [options]
  ```

**Options:**

| Option                 | Description                              |
|------------------------|------------------------------------------|
|  `--help`                            | Show context-sensitive help. |
|  `--version`                         | Print version information and quit. |
|  `-w`, `--proj-dir="."`              | Specify the project path (Required for Project). |
|  `-p`, `--profile`                   | Tizen profile and API version (Project). |
|  `-x`, `--profiles-path`             | Path of profiles.xml containing the signing profiles (Global). |
|  `-s`, `--signing-profile`           | Signing profile used for Tizen packaging (Project). |
|  `-b`, `--build-type`                | Build type (Project). |
|  `-r`, `--rootstrap`                 | Rootstrap used for compiling native app (Project). |
|  `-c`, `--compiler`                  | Compiler for native app compilation (Project). |
|  `-d`, `--dotnet-cli-path`           | Path of dotnet-cli (Global). |
|  `-m`, `--msbuild-path`              | Path of msbuild (Global). |
|  `-D`, `--dotnet-build-tool`         | Tool for dotnet project build (Global). |
|  `-A`, `--arch`                      | Arch for build (Project). |
|  `-S`, `--src-file-patterns`         | Source file patterns excluded from build (Project). |
|  `-T`, `--test-file-patterns`        | Source file patterns included for test mode (Project). |
|  `-C`, `--chrome-path`               | Path of Chrome executable (Global). |
|  `-L`, `--chrome-inspector-options`  | List of options for Chrome inspector (Global). |
|  `-e`, `--chrome-inspector-data-path`| Path of Chrome inspector data (Global). |
|  `-O`, `--optimize`                  | Returns true if optimization of `wgt` for web workspace is enabled (Project). |
|  `-P`, `--projects`                  | List the project dependencies (Project). |
|  `-o`, `--output-path=STRING`        | Output Path for project (Project). |
|  `-a`, `--all`                       | Return the values of all the attrs. |

**Examples:**

- The following command displays the compiler, architecture, and the build type set:

  Windows&reg;:
  ```
  > tz get -A -c -b -w C:\Users\workspace\basicnative
    build_type:Debug
    compiler:llvm
    arch:x86
  ```
  
  Ubuntu and macOS:
  ```
  $ tz get -A -c -b -w ~/workspace/basicnative
    build_type:Debug
    compiler:llvm
    arch:x86
  ```

## Build the project

The following command builds Tizen native, web, and dotnet projects. The same command can be used to build all the 3 type of projects:

**Syntax:**

```
tz build [options]
```

**Options:**

| Option                 | Description                              |
|------------------------|------------------------------------------|
| `-w`, `--proj-dir=STRING`       | Specifies the project directory to be built. |


**Examples:**

- Build the native project with the default `x86`, `llvm`, and `debug` options:

  Windows&reg;:
  ```
  > tz build -w C:\Users\workspace\basicnative
  ```

  Ubuntu and macOS:
  ```
  $ tz build -w ~/workspace/basicnative
  ```

- Build the Native project with `arm`, `llvm`, and `release` options:

  Windows&reg;:
  ```
  > tz set -A arm -b release -c gcc -w C:\Users\workspace\basicnative
  > tz build -w C:\Users\workspace\basicnative
  ```

  Ubuntu and macOS:
  ```
  $ tz set -A arm -b release -c gcc -w ~/workspace/basicnative
  $ tz build -w ~/workspace/basicnative
  ```
## Package a Tizen application with sign

The following command builds and packages Tizen application with signing. If there is a package file in the option (-b), the package is re-signed. Tizen application is signed with a certified profile in the `tizen-studio-data/profile/profiles.xml` file. Certificate security-profiles can be created as mentioned in the section [manage a security profile](#manage-a-security-profile).

**Syntax:**

```
tz pack [options]
```

**Options:**

| Option                            | Description                              |
|-----------------------------------|------------------------------------------|
| `-w`, `--proj-dir`                | Specifies the project directory. |
| `-t`, `--type={tpk/wgt}`          | [repack] Final pkg type (`tpk`/`wgt`). Default: `tpk`. |
| `-s`, `--sign-profile=STRING` | [repack] Specifies the security profile name for signing. If you skip this option, the CLI uses the active profile or the default profile. The default profile is only valid for the Emulator or reference devices. |
| `-p, --profiles-path=STRING`          | [repack] Path to profiles.xml. Default: tizen-studio-data/profile/profiles.xml specified in config.yaml. |
| `-k --ref-pkgs=STRING`          | [repack] Paths of the reference projects, for hybrid packaging, semicolon separated paths:pkg1;pkg2. |
| `-b --base-pkg=STRING`          | [repack] Path of the base pkg. |
| `-o --out-path=STRING`          | [repack] Path of the output pkg: path/to/finalpkg.ext Default: base pkg path. |

**Examples:**

- Package the project:

  Windows&reg;:
  ```
  > tz.exe pack -w C:\Users\workspace\basicnative\     
  Done. Made 9 targets from 16 files in 25ms
  ninja: Entering directory `Debug'
  [5/6] SIGN package files
  Signing using certificates:
        Author cert : C:/tizen-studio-data/keystore/author/test1.p12
        Distributor cert : C:/tizen-studio/tools/certificate-generator/certificates/distributor/tizen-distributor-signer-new.p12
        Distributor2 cert :

  Package File Location: C:\Users\workspace\basicnative\Debug\org.example.basicnative-1.0.0-x86.tpk
  [6/6] STAMP obj/build/pack.stamp
  ```

  Ubuntu and macOS:
  ```
  $ tz pack -w ~/workspace/basicnative
  Done. Made 9 targets from 16 files in 14ms
  ninja: Entering directory `Debug'
  [1/2] SIGN package files
  Signing using certificates:
        Author cert : /home/user/tizen-studio-data.2/keystore/author/test2.p12
        Distributor cert : /home/user/tizen-studio/tools/certificate-generator/certificates/distributor/tizen-distributor-signer-new.p12
        Distributor2 cert :

  Package File Location: /home/user/basicnative/Debug/org.example.basicnative-1.0.0-x86.tpk
  [2/2] STAMP obj/Build/pack.stamp
  ```

- Repackage the existing pkg file:

  Windows&reg;:
  ```
  > tz pack -t tpk -s profiletest -b C:\Users\workspace\basicnative\Debug\org.example.basicnative-1.0.0-x86.tpk
  Using default certificates
  Signing using certificates:
          Author cert : C:\tizen-studio\tools\certificate-generator\certificates\developer\tempMobile.p12
          Distributor cert : C:\tizen-studio\tools\certificate-generator\certificates\distributor\tizen-distributor-signer.p12
          Distributor2 cert :

  Package File Location: C:\Users\workspace\basicnative\Debug\org.example.basicnative-1.0.0-x86.tpk
  ```

  Ubuntu and macOS:
  ```
  $ tz pack -t tpk -s profiletest -b /home/user/basicnative/Debug/org.example.basicnative-1.0.0-x86.tpk
  Signing using certificates:
          Author cert : /home/user1/tizen-studio/tools/certificate-generator/certificates/developer/tempMobile.p12
          Distributor cert : /home/user1/tizen-studio/tools/certificate-generator/certificates/distributor/tizen-distributor-signer.p12
          Distributor2 cert :

  Package File Location: /home/user/basicnative/Debug/org.example.basicnative-1.0.0-x86.tpk
  ```

- Merge and repackage the existing pkg files:

  Windows&reg;:
  ```
  > tz pack -t tpk -r C:\Users\workspace\serviceapp\Debug\org.example.serviceapp-1.0.0-x86.tpk -b C:\Users\workspace\basicnative\Debug\org.example.basicnative-1.0.0-x86.tpk -s profiletest -o C:\Users\workspace\org.example.basicnative-1.0.0-x86.tpk
  Using default certificates
  Signing using certificates:
          Author cert : C:\tizen-studio\tools\certificate-generator\certificates\developer\profiletest.p12
          Distributor cert : C:\tizen-studio\tools\certificate-generator\certificates\distributor\tizen-distributor-signer.p12
          Distributor2 cert :
  Package File Location: C:\Users\workspace\org.example.basicnative-1.0.0-x86.tpk
  ```

  Ubuntu and macOS:
  ```
  $ tz pack -t tpk -s profiletest -r ~/user/serviceapp/Debug/org.example.serviceapp-1.0.0-x86.tpk -b ~/user/basicnative/Debug/org.example.basicnative-1.0.0-x86.tpk -o ~/user/org.example.basicnative-1.0.0-x86.tpk
  Signing using certificates:
          Author cert : /home/user/tizen-studio/tools/certificate-generator/certificates/developer/profiletest.p12
          Distributor cert : /home/user/tizen-studio/tools/certificate-generator/certificates/distributor/tizen-distributor-signer.p12
          Distributor2 cert :

  Package File Location: /home/user/org.example.basicnative-1.0.0-x86.tpk
  ```  
## Install the application on a target

The following command installs a Tizen application on a specified target or serial device:

**Syntax:**

```
tz install [options]
```

**Options:**

| Option                             | Description                              |
|------------------------------------|------------------------------------------|
| `-w`, `--proj-dir=STRING`          | Specifies the project path to be installed. |
| `-p`, `--package-path=STRING`      | Specifies the package (tpk/wgt) path to be installed. | 
| `-t`, `--target=STRING`            | Specifies the target name to install the package. |
| `-e`, `--serial=STRING`            | Specifies the serial to install the package. |

**Examples:**

- Install the application:

  Windows&reg;:
  ```
  > tz install -e emulator-26101 -w C:\Users\workspace\basicnative
  ```

  Ubuntu and macOS:
  ```
  $ tz install -e emulator-26101 -w ~/workspace/basicnative
  ```
  - Install the package (tpk|wgt).

  Windows&reg;:
  ```
  > tz install -e emulator-26101 -p C:\Users\workspace\basicnative\Debug\org.example.basicnative-1.0.0-x86.tpk
  ```

## Run the application on a target

TThe following command runs Tizen application on a specified target or serial device:

**Syntax:**

```
tz run [options]
```

**Options:**

| Option                           | Description                              |
|----------------------------------|------------------------------------------|
| `-w`, `--proj-dir=STRING`        | Specifies the project path to execute. |
| `-t`, `--target=STRING`          | Specifies the target name to run the package. |
| `-e`, `--serial=STRING`          | Specifies the serial to run the package. |
| `-d`, `--debug-mode`             | Run web app in debug mode in web inspector. |
| `-r`, `--simulator`              | Run the web app in web simulator (only TV simulator supported). |
| `-p`, `--package-id=STRING`      | Specifies the package id to execute. |
| `-c`, `--coverage`               | Generate coverage report for native test app run. |

**Examples:**

- Run the specified application on the Emulator-26101:

  Windows&reg;:
  ```
  > tz run -e emulator-26101 -w C:\Users\workspace\basicnative
  ```

  Ubuntu and macOS:
  ```
  $ tz run -e emulator-26101 -w ~/workspace/basicnative
  ```

## Run the web application in web simulator (only TV simulator supported)

  Windows&reg;:
  ```
  > tz run -r -w C:\Users\workspace\basicweb
  ```

  Ubuntu and macOS:
  ```
  $ tz run -r -w ~/workspace/basicweb
  ```

## Run the web application in debug mode using web inspector

  Windows&reg;:
  ```
  > tz run -d -e emulator-26101 -w C:\Users\workspace\basicweb
  ```

  Ubuntu and macOS:
  ```
  $ tz run -d -e emulator-26101 -w ~/workspace/basicweb
  ```

## Uninstall the application on a target

The following command uninstalls Tizen application on a specified target or serial device:

**Syntax:**

```
tz uninstall [options]
```

**Options:**

| Option                           | Description                              |
|----------------------------------|------------------------------------------|
| `-w`, `--proj-dir=STRING`        | Specifies the project path to be uninstalled. |
| `-t`, `--target=STRING`          | Specifies the target name to uninstall the package. |
| `-e`, `--serial=STRING`          | Specifies the serial to uninstall the package. |

**Examples:**

- Uninstall the application based on the specified working directory:

  Windows&reg;:
  ```
  > tz uninstall -e emulator-26101 -w C:\Users\workspace\nuiapp
  ```

  Ubuntu, and macOS:
  ```
  > tz uninstall -e emulator-26101 -w ~/workspace/nuiapp
  ```
## Clean the project

The following command is used to clean Tizen project. If you clean the project, all output files generated during the build are removed:

**Syntax:**

```
tz clean [options]
```

**Options:**

| Option                   | Description                              |
|--------------------------|------------------------------------------|
| `-w`, `--proj-dir=STRING`| Specifies the project path to be cleaned. |

**Examples:**

- Clean the project:

  Windows&reg;:
  ```
  > tz clean -w C:\Users\workspace\basicnative
  ```

  Ubuntu and macOS:
  ```
  $ tz clean -w ~/workspace/basicnative
  ```

## Add dependency between the projects

The following command adds dependency between the projects in the given directory:

**Syntax:**

```
tz add-deps [options]
```

**Options:**

| Option                                  | Description                              |
|---------------------------------------|----------------------------------------|
| `<project>`                  | Project path relative to main project. |
| `-d`, `--deps=STRING`         | Project dependencies relative to main project, comma separated: -d proj1, proj2. |
| `--help`                     | Show context-sensitive help. |


**Examples:**

- The following command creates Native BasicUI and ServiceApp in the workspace and ServiceApp is added as dependent project of BasicUI:


  Windows&reg;:
  ```
  > tz new -t basic_ui -n basic -T native -p tizen-9.0 -w C:\Users\workspace
  > tz new -t serviceapp -n service -T native -p tizen-9.0 -w C:\Users\workspace
  > tz add-deps C:\Users\workspace\basic -d ..\service
  ```

  Ubuntu and macOS:
  ```
  $ tz new -t basic_ui -n basic -T native -p tizen-9.0 -w ~/workspace
  $ tz new -t serviceapp -n service -T native -p tizen-9.0 -w ~/workspace
  $ tz add-deps /home/test/workspace/basic -d ../service
  ```

## Details to create hybrid projects

A hybrid project is a project which combines different type of projects like native and dotnet, or web and native apps.

**Example:**

Different kinds of projects can be created from the templates using the `-T project_type` argument in `tz new` as mentioned in the section [Create a Tizen Project](#create-a-tizen-project).

**Examples:**

Windows&reg;:
```
tz new -T native -t ServiceApp -n nativeservice -p tizen-9.0 -w C:\Users\workspace
tz new -T web -t BasicUI -n basicweb -p tizen-9.0 -w C:\Users\workspace
```

Ubuntu and macOS:
```
tz new -T native -t basic_ui -p basicnative -w ~/workspace
tz new -T web -t BasicUI -p basicweb -w ~/workspace
```

Once the different types of projects are created in the workspace, dependencies can be added between the projects as mentioned in the section [adding dependency between projects](#add-dependency-between-the-projects).

The rest of the functionalities: [build](#build-the-project), [pack](#package-a-tizen-application-with-signing), [install](#install-the-application-on-a-target), [run](#run-the-application-on-a-target), [setting working_folder](#set-the-working-folder), [adding dependency](#add-dependency-between-the-projects) have the same behaviour in the hybrid workspace.

## Details to create, package, and install resource project

A resource project can contain resource files that can be used by a native application in a workspace:

**Example:**

Resource project can be created from the template the `-T project_type` argument in `tz new` as mentioned in the section [Create a Tizen Project](#create-a-tizen-project).

**Examples:**

Windows&reg;:
```
tz new -T rpk -t rpk_app -n basicrpk -p tizen-9.0 -w C:\Users\workspace
```

Ubuntu and macOS:
```
tz new -T rpk -t rpk_app -n basicrpk -p tizen-9.0 -w ~/workspace
```

To package and install rpk on the target, use the following commands:

**Examples:**

- Package the project into rpk:

  Windows&reg;:
  ```
  > tz pack -w C:\Users\workspace\basicrpk
  ```

  Ubuntu and macOS:
  ```
  $ tz pack -w ~/workspace/basicrpk
  ```

- Install the rpk on the target:

  Windows&reg;:
  ```
  > tz install -w C:\Users\workspace\basicrpk
  ```

  Ubuntu and macOS:
  ```
  $ tz install -w ~/workspace/basicrpk
  ```


## Issue a Tizen certificate

The following command generates a Tizen certificate for your application. If you want to upload your application to the the official site for Tizen applications or install the application on a Tizen device, you must generate a Tizen certificate using the following command:

**Syntax:**
```
tz cert [options]
```

**Options:**

| Option                                | Description                              |
|---------------------------------------|------------------------------------------|
|  `--help`                         | Show context-sensitive help. |
|  `--version`                      | Print version information and quit. |
|  `-n`, `--name=STRING`            | Author's name (required). |
|  `-p`, `--password=STRING`        | Password (required). |
|  `-e`, `--email=STRING`           | Author's email. |
|  `-d`, `--department=STRING`      | Author's department. |
|  `-o`, `--organization=STRING`    | Author's organization. |
|  `-c`, `--city=STRING`            | Author's city. |
|  `-s`, `--state=STRING`           | Author's state. |
|  `-C`, `--country=STRING`         | Author's country. |
|  `-f`, `--cert-file=STRING`       | Certificate file name. |

**Examples:**

- Generate a certificate:
  ```  
  # by default the cert is created in tizen-studio-data/keystore/author/{certfilename}.p12
  > tz cert -n certAuthorName -p password -e authoremail@email.com -d department -o organization -c city -s state -C IN -f certificateFileName
  certificate created at : C:\tizen-studio-data\keystore\author\certificateFileName.p12
  
  # certificates can be created at custom locations by specifying the path in --cert-file arg
  > tz cert -n certAuthorName -p password -e authoremail@email.com -d department -o organization -c city -s state -C IN -f C:\Users\user.name\newcertname.p12
  certificate created at : C:\Users\user.name\newcertname.p12
  
  > tz cert -n certAuthorName -p password -e authoremail@email.com -d department -o organization -c city -s state -C IN -f C:\Users\user.name\newcertname1
  certificate created at : C:\Users\user.name\newcertname1.p12
  ```

## Manage a security profile

The command manages the security profiles, which are a set of signing certificates for a Tizen application:

**Syntax:**

```
tz security-profiles <sub-command> [options]
```

**Sub-commands:**
<table>
	<thead>
		<tr>
			<th>Sub-command</th>
			<th>Description</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td><code>add [options]</code></td>
			<td>Adds the specified security profile, which can contain several certificates.<br />
			<br />
			Options are:
			<ul>
				<li><code>-n</code>, <code>--name=STRING</code> :Profile name (required)</li>
				<li><code>-A</code>, <code>--active</code> :Set as active profile</li>
				<li><code>-x</code>, <code>--xml-path=STRING</code> :Path to profiles.xml, if empty then tizen-studio-data/profile/profiles.xml will be used</li>
				<li><code>-a</code>, <code>--author=STRING</code> :Author certificate (required)</li>
				<li><code>-p</code>, <code>--password=STRING</code> :Password of author certificate (required)</li>
				<li><code>-c</code>, <code>--ca=STRING</code> :Author CA path</li>
				<li><code>-r</code>, <code>--rootca=STRING</code> :Author root-CA path</li>
				<li><code>-d</code>, <code>--dist=STRING</code> :Distributor certificate</li>
				<li><code>-P</code>, <code>--dist-password=STRING</code> :Password of distributor certificate</li>
				<li><code>-C</code>, <code>--dist-ca=STRING</code> :Distributor CA path</li>
				<li><code>-R</code>, <code>--dist-rootca=STRING</code> :Distributor root-CA path</li>
				<li><code>-D</code>, <code>--dist2=STRING</code> :Distributor2 certificate</li>
				<li><code>-w</code>, <code>--dist2-password=STRING</code> :Password of distributor 2 certificate</li>
				<li><code>-e</code>, <code>--dist2-ca=STRING</code> :Distributor 2 CA path</li>
				<li><code>-E</code>, <code>--dist2-rootca=STRING</code> :Distributor 2 root-CA path</li>
			</ul>
			</td>
		</tr>
		<tr>
			<td><code>list [options]</code></td>
			<td>Displays security profiles. <br />
			<br />
			Options are:
			<ul>
        <li><code>-x</code>, <code>--xml-path=STRING</code>    :Path to <code>profiles.xml</code>, if empty then <code>tizen-studio-data/profile/profiles.xml</code> will be used</li>
			</ul>
			</td>
		</tr>
		<tr>
			<td><code>remove [options]</code></td>
			<td>Removes the specified security profile.<br />
			<br />
			Options are:
			<ul>
        <li><code>{profile-name}</code>  :Name of the profile to be removed</li>
        <li><code>-x</code>, <code>--xml-path=STRING</code>    :Path to <code>profiles.xml</code>, if empty then <code>tizen-studio-data/profile/profiles.xml</code> will be used</li>
			</ul>
			</td>
		</tr>
    <tr>
			<td><code>set-active [options]</code></td>
			<td>Sets the specified security profile as active profile.<br />
			<br />
			Options are:
			<ul>
        <li><code>{profile-name}</code>  :Name of the profile to be set as active</li>
        <li><code>-x</code>, <code>--xml-path=STRING</code>    :Path to <code>profiles.xml</code>, if empty then <code>tizen-studio-data/profile/profiles.xml</code> will be used</li>
			</ul>
			</td>
		</tr>
	</tbody>
</table>

**Examples:**

- Add a new security profile:

  ```
  > tz security-profiles add -n newprofile -a C:\tizen-studio-data\keystore\author\certificateFileName.p12 -p password
  ```

- Display the security profile list:

  ```
  > tz security-profiles list
  Current Active Profile: tsprofile
  
  tzprofile
    Author      : C:\tizen-studio-data\keystore\author\certname.p12
    Distributor : C:\tizen-studio\tools\certificate-generator\certificates\distributor\tizen-distributor-signer.p12
    Distributor2:
  
  tsprofile
    Author      : C:\tizen-studio-data\keystore\author\tsprofile.p12
    Distributor : C:\tizen-studio\tools\certificate-generator\certificates\distributor\tizen-distributor-signer.p12
    Distributor2:
  ```

- Remove the security profile:

  ```
  > tz security-profiles remove tsprofile
  ```

- Set security profile as active profile:

  ```
  > tz security-profiles set-active tzprofile
  > tz security-profiles set-active tzprofile
    tzprofile was already set as active in C:\tizen-studio-data\profile\profiles.xml
  ```  

## Usage of your own certificates

The command is used to assign your own SSL root certificates for HTTPS communication:

**Syntax:**
```
tz trust-anchor <sub-command> [options]
```

**Sub-commands:**
<table>
	<thead>
		<tr>
			<th>Sub-command</th>
			<th>Description</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td><code>set [options]</code></td>
			<td>Sets a new user certificate for a project.<br />
			<br />
			Options are:
			<ul>
				<li><code>-p</code>, <code>--project="."</code>          :Project path</li>
        <li><code>-c</code>, <code>--cert-paths=STRING</code>    :Path of the certificate files/directory. Quote enclosed and comma separated</li>
        <li><code>-s</code>, <code>--use-system-cert</code>      :Use system certificate if -s flag present</li>
			</ul>
			</td>
		</tr>
		<tr>
			<td><code>info</code></td>
			<td>Displays the trust anchor configuration for a project.<br />
			<br />
			Options are:
			<ul>
				<li><code>-p</code>, <code>--project="."</code>          :Project path</li>
			</ul>
			</td>
		</tr>
		<tr>
			<td><code>delete [options]</code></td>
			<td>Deletes the specified user certificate.<br />
			<br />
			Options are:
			<ul>
				<li><code>-p</code>, <code>--project="."</code>          :Project path</li>
        <li><code>-c</code>, <code--cert-paths=STRING</code>     :Path of the certificates inside the .trust-anchor/. Quote enclosed and comma separated</li>
			</ul>
			</td>
		</tr>
		<tr>
			<td><code>unset</code></td>
			<td>Disables the trust anchor.<br />
			<br />
			Options are:
			<ul>
				<li><code>-p</code>, <code>--project="."</code>          :Project path</li>
			</ul>
			</td>
		</tr>
	</tbody>
</table>


Examples:

- Set a new user certificate, check the trust anchor configuration, set additional certificates, delete certificates, and unset the trust anchor:

  Windows&reg;:
  ```
  > tz trust-anchor info -p C:\Users\workspace\basic
  trust-anchor is disabled for this project
  trust-anchor certs of project: C:\Users\workspace\basic
  total: 0
  
  >tz trust-anchor set -p C:\Users\workspace\basic -s -c C:\cert\user1.pem

  >tz trust-anchor info -p C:\Users\workspace\basic
  use-system-certs:true
  trust-anchor certs of project: C:\Users\workspace\basic
  res/.trust-anchor/user1.pem
  total: 1
  
  > tz trust-anchor set -c "E:\cert\user2.pem,E:\cert\user3.pem,E:\cert\certdirs" -p C:\Users\workspace\basic
  
  > tz trust-anchor info -p C:\Users\workspace\basic
  use-system-certs: true
  res/.trust-anchor/user1.pem
  res/.trust-anchor/user2.pem
  res/.trust-anchor/user3.pem
  res/.trust-anchor/certdir1.pem
  res/.trust-anchor/certdir2.pem
  res/.trust-anchor/certdir3.pem
  total: 6
  
  > tz trust-anchor delete -c "user2.pem,certdir1.pem" -p C:\Users\workspace\basic

  > tz trust-anchor info -p C:\Users\workspace\basic
  use-system-certs: true
  res/.trust-anchor/user1.pem
  res/.trust-anchor/user3.pem
  res/.trust-anchor/certdir2.pem
  res/.trust-anchor/certdir3.pem
  total: 4
  
  > tz trust-anchor unset -- C:\Users\workspace\basic
  
  > tz trust-anchor info -p C:\Users\workspace\basic
  trust-anchor is disabled for this project
  trust-anchor certs of project: C:\Users\workspace\basic
  total: 0
  ```

## Display the command help

The following command displays the CLI command help:

**Syntax:**

```
tz <command> --help
```

You can use all CLI commands to as `<command>`:

```
templates, new, add-deps, rem-deps, clean, build, pack, install, run, uninstall, cert,  security-profiles, emul, list, get, set, trust-anchor, tidl-build, js-analyze.
```

**Examples:**

- Display the help for project create command:

  Windows&reg;, Ubuntu, and macOS:

  ```
  > tz new --help
  Usage: tz new --project-name=STRING --template=STRING --type=STRING --profile=STRING

  Create new project

  Flags:
      --help                   Show context-sensitive help.
      --version                Print version information and quit

  -w, --path="."               Specify where the base directory is for the command
  -n, --project-name=STRING    Specify the project name (Required)
  -t, --template=STRING        Specify the template name (Required)
  -T, --type=STRING            Specify the project type (Required)
  -p, --profile=STRING         Specify the profile name (Required)
  ```

## Related information
- Dependencies  
  - Tizen Studio 6.0 and Higher