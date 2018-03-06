# Command Line Interface
The .NET CLI (Command Line Interface) provides functionalities for developing Tizen .NET applications without the IDE.
It includes the entire development process from creating the project to running the application. The CLI tool is located in the `$<TIZEN_BASELINE_SDK>/tools/ide/bin/` directory.

> **Note**
>
> The .NET CLI does not support restoring and building Xamarin.Forms projects, as the .NET Core CLI 2.0.0 does not fully support Xamarin.Forms.

## Prerequisites

The following tools must be installed to use the .NET CLI:

- Tizen Baseline SDK
- .NET Core CLI tools 2.0.0

## Setting Configuration Options
The `cli-config` command displays, sets, replaces, and removes .NET CLI configuration options.

The .NET CLI configuration keys are:

- `default.build.configuration=<Debug|Release>`: Sets the default build configuration.
- `default.csharp.buildtool.path=<path/to/msbuild>`: Sets the C# build tool path. The default is `C:/Program Files (x86)/MSBuild/15.0/Bin/MSBuild.exe`.
- `default.csharp.toolchain=<dotnet-cli|msbuild>`: Sets the C# build tool. The default is `dotnet-cli` for Windows&reg; and Ubuntu, and `msbuild` is only supported on Windows&reg;.
- `default.dotnet.tool.path=<path/to/dotnet>`: Sets the `dotnet` CLI tool path. The default is `C:/Program Files/dotnet/dotnet.exe` for Windows&reg;, and `/usr/bin/dotnet` for Ubuntu.
- `default.profiles.path=<PROFILE_PATH>`: Sets the directory path where the `profiles.xml` file is located.
- `default.sdb.timeout=<TIMEOUT_VALUE>`: Sets the default connection timeout value. The default is 60000 milliseconds.


**Syntax:**
```
dotnet tizen cli-config [arguments] [options]
```

**Arguments:**

| Argument | Description |
| ------ | ------ |
| `<KEY>=<VALUE>` | Sets a value for the .NET CLI configuration key. |

**Options:**

| Option | Description |
| ------ | ------ |
| `-g`, `--global` | Specifies whether the operation must be done for a global scope (for all installed SDKs or for the current Tizen Baseline SDK only). |
| `-l`, `--list` | Displays the list of all .NET CLI configuration keys and values. |
| `-d`, `--delete <KEY>` | Removes the .NET CLI configuration key and value. |

**Examples:**
- Display a list of all configurations for which values are set:
  - Windows&reg;:
    ```sh
    > dotnet tizen cli-config -l
    default.build.architecture=x86
    default.build.compiler=llvm
    default.build.configuration=Debug
    default.csharp.buildtool.path=C:\Program Files (x86)\Microsoft Visual Studio\2017\Professional\MSBuild\15.0\Bin\msbuild.exe
    default.csharp.toolchain=dotnet-cli
    default.dotnet.tool.path=C:/Program Files/dotnet/dotnet.exe
    default.profiles.path=D:\tizen-install-data\profile\profiles.xml
    default.sdb.timeout=60000
    ```
  - Ubuntu and macOS:
    ```sh
    > dotnet tizen cli-config -l
    default.build.architecture=x86
    default.build.compiler=llvm
    default.build.configuration=Debug
    default.csharp.buildtool.path=C:/Program Files (x86)/Microsoft Visual Studio/2017/Professional/MSBuild/15.0/Bin/MSBuild.exe
    default.csharp.toolchain=dotnet-cli
    default.dotnet.tool.path=/usr/bin/dotnet
    default.profiles.path=/home/tizen-developer/tizen-studio-data/profile/profiles.xml
    default.sdb.timeout=60000
    ```
- Set a `profiles.xml` path globally:
  - Windows&reg;:
    ```sh
    > dotnet tizen cli-config -g "default.profiles.path=C:\workspace\.metadata\.plugins\org.tizen.common.sign\profiles.xml"
    ```
  - Ubuntu and macOS:
    ```sh
    $ dotnet tizen cli-config -g default.profiles.path=~/workspace/.metadata/.plugins/org.tizen.common.sign/profiles.xml
    ```


## Creating a Tizen .NET Project
The `new` command creates a Tizen .NET project from a template. If a template is not specified, the command displays project templates and a usage message.

**Syntax:**
```
dotnet tizen new [arguments] [options]
```  

**Arguments:**

| Argument | Description |
| ------ | ------ |
| `<TEMPLATE_NAME>` | Specifies the template name. 

**Options:**

| Option | Description |
| ------ | ------ |
| `-n`,  `--name <PROJECT_NAME>` | Specifies the project name. If no name is specified, the template name is used. |
| `-o`, `--output <OUTPUT_DIR>` | Specifies the output directory path for the output being created. If no output directory is specified, the current directory is used. |
| `-all`, `--show-all` | Shows all templates. |

**Examples:**
- Display Tizen .NET templates:
  - Windows&reg;, Ubuntu, and macOS:
    ```sh
    > dotnet tizen new
    Initialize Tizen .NET projects.

    Usage: dotnet tizen new [arguments] [options]

    Arguments:
      <TEMPLATE_NAME>  Template name.

    Options:
      -h, --help                 Show help information.
      -n, --name <PROJECT_NAME>  The project name. If no name is specified, the template name is used for the project name.
      -o, --output <OUTPUT_DIR>  The output directory path for the output being created. If no output directory is specified, the current directory is used as the root directory.
      -all, --show-all           Show all templates.

    Examples:
        dotnet tizen new Tizen.Template.BlankAppCorporate

    [TEMPLATE]
    Tizen.NET.Template.ElmSharp
    Tizen.NET.Template.NSClassLib
    Tizen.NUI.Template.Single
    ```
- Create a Tizen .NET project with a specific template:
  - Windows&reg;:
    ```sh
    > dotnet tizen new Tizen.NUI.Template.Single -n blank -o C:\workspace
    > cd C:\workspace\blank
    ```

## Restoring the Project
The `restore` command restores the dependencies and tools of a Tizen .NET project.

The following options are based on .NET Core CLI tools 2.0.0.  For more information, see [dotnet restore command](https://docs.microsoft.com/en-us/dotnet/core/tools/dotnet-restore?tabs=netcore2x).

**Syntax:**
```
dotnet tizen restore [options]
```
**Options:**

| Option | Description |
| ------ | ------ |
| `-s`, `--source <SOURCE>` | Specifies a NuGet package source to use during the restore operation. This overrides all of the sources specified in the `NuGet.config` files. Multiple sources can be provided by specifying this option multiple times. |
| `-r`, `--runtime <RUNTIME_IDENTIFIER>` | Specifies a runtime for package restoration. This is used to restore packages for runtimes not explicitly listed in the `<RuntimeIdentifiers>` tag in the `.csproj` file. For a list of Runtime Identifiers (RIDs), see the [RID catalog](https://docs.microsoft.com/en-us/dotnet/core/rid-catalog). Provide multiple RIDs by specifying this option multiple times. |
| `--packages <PACKAGES_DIRECTORY>` | Specifies the directory for restored packages. |
| `--disable-parallel` | Disables restoring multiple projects in parallel. |
| `--configfile <FILE>` | Specifies the NuGet configuration file (`NuGet.config`) to use for the restore operation. |
| `--no-cache` | Does not cache packages and HTTP requests. |
| `--ignore-failed-sources` | Only warns about failed sources if there are packages meeting the version requirement. |
| `--no-dependencies` |When restoring a project with project-to-project (P2P) references, restores the root project and not the references. |
| `-f`, `--force` | Forces all dependencies to be resolved even if the last restore was successful. This is equivalent to deleting the `project.assets.json` file. |
| `-v`, `--verbosity` | Sets the verbosity level of the command. Allowed values are `q[uiet]`, `m[inimal]`, `n[ormal]`, `d[etailed]`, and `diag[nostic]`. |

**Examples:**
- Restore the Tizen .NET project:
  - Windows&reg;, Ubuntu, and macOS:
    ```sh
    > dotnet tizen restore
    ```

## Building the Project
The `build` command builds a Tizen .NET project and its dependencies into a set of binaries.

The following arguments and options are based on .NET Core CLI tools 2.0.0.  For more information, see [dotnet build command](https://docs.microsoft.com/en-us/dotnet/core/tools/dotnet-build?tabs=netcore2x).

**Syntax:**
```
dotnet tizen build [arguments] [options]
```

**Arguments:**

| Argument | Description |
| ------ | ------ |
| `<PROJECT>` | Specifies the MSBuild project file (`.csproj`) to build. If a project file is not specified, .NET Core CLI (MSBuild) searches the current working directory for a file that has a file extension that ends in `csproj` and uses that file. |

**Options:**

| Option | Description |
| ------ | ------ |
| `-o`, `--output <OUTPUT_DIR>` | Specifies the directory in which to place the built binaries. You also need to define `--framework` when you specify this option. |
| `-f`, `--framework <FRAMEWORK>` | Compiles for a specific framework. The framework must be defined in the project file. |
| `-r`, `--runtime <RUNTIME_IDENTIFIER>` | Specifies the target runtime. For a list of Runtime Identifiers (RIDs), see the [RID catalog](https://docs.microsoft.com/en-us/dotnet/core/rid-catalog). Provide multiple RIDs by specifying this option multiple times. |
| `-c`, `--configuration <CONFIGURATION>` | Defines the build configuration. The default value is `Debug`.|
| `--version-suffix <VERSION_SUFFIX>` | Defines the version suffix for an asterisk (`*`) in the version field of the project file. The format follows NuGet's version guidelines. |
| `--no-incremental` | Marks the build as unsafe for incremental build. This turns off incremental compilation and forces a clean rebuild of the project's dependency graph. |
| `--no-dependencies` | Ignores project-to-project (P2P) references and only builds the root project specified to build. |
| `--no-restore` | Does not perform an implicit restore during build. |
| `-f`, `--force` | Forces all dependencies to be resolved even if the last restore was successful. This is equivalent to deleting the `project.assets.json` file. |
| `-v`, `--verbosity` | Sets the verbosity level of the command. Allowed values are `q[uiet]`, `m[inimal]`, `n[ormal]`, `d[etailed]`, and `diag[nostic]`. |

**Examples:**
- Build the Tizen .NET project:
  - Windows&reg;, Ubuntu, and macOS:
    ```sh
    > dotnet tizen build
    ```

## Cleaning the Project
The `clean` command cleans the Tizen .NET project. If you clean the project, all build output directories under the project root path are removed.

**Syntax:**
```
dotnet tizen clean [arguments]
```
**Arguments:**

| Argument | Description |
| ------ | ------ |
| `<PROJECT_DIR>` | Specifies the project directory. Defaults to the current directory if no directory is specified. |

**Examples:**
- Clean the Tizen .NET project:
  - Windows&reg;:
    ```sh
    > dotnet tizen clean C:\workspace\blank
    ```
  - Ubuntu and macOS:
    ```sh
    $ dotnet tizen clean ~/workspace/blank
    ```

## Issuing a Tizen Certificate
The `certificate` command generates a Tizen certificate for your application. If you want to upload your application to the Tizen Store or install the application on a Tizen device, you must generate a Tizen certificate.

**Syntax:**
```
dotnet tizen certificate [options]
```

**Options:**

| Option | Description |
| ------ | ------ |
| `-a`, `--alias <ALIAS_NAME>` | Specifies the certificate alias name. (Required) |
| `-pw`, `--password <PASSWORD>` | Specifies the certificate password. (Required) |
| `-n`, `--name <USER_NAME>` | Specifies the user name. |
| `-c`, `--country <COUNTRY_CODE>` | Specifies the user's 2-letter country code. |
| `-s`, `--state <STATE>` | Specifies the user's state. |
| `-ct`, `--city <CITY>` | Specifies the user's city. |
| `-og`, `--organization <ORGANIZATION>` | Specifies the user's organization. |
| `-u`, `--unit <UNIT>` | Specifies the user's organization unit. |
| `-e`, `--email <EMAIL>` | Specifies the user's email. |
| `-fn`, `--filename <FILE_NAME>` | Specifies the certificate file name, without file extension. If you omit this option, the default file name, `author`, is used. |
| `-o`, `--output <CERT_OUTPUT_DIR>` | Specifies the output directory path for the created certificate. If you omit this option, the certificate file is saved in the default output directory path, `<TIZEN_BASELINE_SDK_DATA>/keystore/author/`.|

**Examples:**
- Generate a certificate:
  - Windows&reg;:
    ```sh
    > dotnet tizen certificate -a MyTizen -pw 1234 -n "Gildong Hong" -c KR -s Seoul -ct Gangnamgu -og Tizen -u Development -e gildonghong@example.org -fn mycert
    Generating a certificate with
      File name = mycert
      Container Password = ****
      Alias = MyTizen
      Key Password = ****
      Country = KR
      State = Seoul
      City = Gangnamgu
      Name = Gildong Hong
      Organization = Tizen
      Organization Unit = Develop
      E-mail = gildonghong@example.org
    'mycert' has been generated in 'C:\tizen-studio-data\keystore\author'.
    ```
  - Ubuntu and macOS:
    ```sh
    $ dotnet tizen certificate -a MyTizen -pw 1234 -n "Gildong Hong" -c KR -s Seoul -ct Gangnamgu -og Tizen -u Development -e gildonghong@example.org -fn mycert
    Generating a certificate with
      File name = mycert
      Container Password = ****
      Alias = MyTizen
      Key Password = ****
      Country = KR
      State = Seoul
      City = Gangnamgu
      Name = Gildong Hong
      Organization = Tizen
      Organization Unit = Develop
      E-mail = gildonghong@example.org
    'mycert' has been generated in '~/tizen-studio-data/keystore/author'.
    ```

## Managing Security Profiles
The `security-profiles` command manages the security profiles, which are sets of signing certificates for Tizen applications.

**Syntax:**
```
dotnet tizen security-profiles <sub-command> [options]
```
**Sub-commands and options:**

| Sub-command | Option | Description |
| ------ | ------ | ------ |
| `add [options]` |`-n`, `--name <PROFILE_NAME>` | Specifies the name of the security profile to add. (Required) |
|| `-a`, `--author <AUTHOR_PATH>` | Specifies the file path where the author certificate file is located. The format of the certificate is PKCS#12, and the file extension is `.p12`. (Required) |
|| `-pw`, `--password <AUTHOR_PASSWORD>` | Specifies the password used to access the author certificate. (Required) |
|| `-c`, `--ca <AUTHOR_CA_PATH>` | Specifies the file path where the author CA certificate file is located. The file extension of the CA certificate is `.cer`. |
|| `-r`, `--rootca <AUTHOR_ROOT_CA_PATH>` | Specifies the file path where the author root CA certificate file is located. The file extension of the root CA certificate is `.cer`. |
|| `-d`, `--dist <DIST_PATH>` | Specifies the file path where the distributor certificate file is located. If you omit this option, the default distributor certificate file embedded in the Tizen Baseline SDK is used. |
|| `-dp`, `--dist-password <DIST_PASSWORD>` | Specifies the distributor certificate password. |
|| `-dc`, `--dist-ca <DIST_CA_PATH>` | Specifies the file path where the distributor CA certificate file is located. |
|| `-dr`, `--dist-rootca <DIST_ROOT_CA_PATH>` | Specifies the file path where the distributor root CA certificate file is located.
|| `--force`| If there is no `profiles.xml` file, generates the file. |
|| `-p`, `--path <PROFILE_PATH>` | Specifies the file path where the `profiles.xml` file is located. If you omit this option, the value of the `default.profiles.path` key in the CLI configuration is used to find the `profiles.xml` file, which consists of new security profiles that are generated in the `<TIZEN_BASELINE_SDK_DATA>/keystore/` directory. The directory path is added to the CLI configuration. |
| `list [options]` | `-n, --name <PROFILE_NAME>` | Specifies the name of the security profile to list. If you omit this option, a list of the security profile names in the `profiles.xml` file is displayed. |
|| `-p`, `--path <PROFILE_PATH>` | Specifies the file path where the `profiles.xml` file is located. If you omit this option, the value of the `default.profiles.path` key in the CLI configuration is used to find the `profiles.xml` file, which consists of new security profiles that are generated in the `<TIZEN_BASELINE_SDK_DATA>/keystore/` directory. The directory path is added to the CLI configuration. |
| `remove [options]` | `-n`, `--name <PROFILE_NAME>` | Specifies the name of the security profile to remove. (Required) |
|| `-p`, `--path <PROFILE_PATH>` | Specifies the file path where the `profiles.xml` file is located. If you omit this option, the value of the `default.profiles.path` key in the CLI configuration is used to find the `profiles.xml` file, which consists of new security profiles that are generated in the `<TIZEN_BASELINE_SDK_DATA>/keystore/` directory. The directory path is added to the CLI configuration. |

**Examples:**
- Add a security profile:
  - Windows&reg;:
    ```sh
    > dotnet tizen security-profiles add -n MyProfile -a C:\tizen-studio-data\keystore\author\mycert.p12 -pw 1234
    No exist the default path of security profiles.
    author path: C:\tizen-studio-data\keystore\author\mycert.p12
    author password: ****
    distributor1 path: C:\tizen-studio\tools\certificate-generator\certificates\distributor\tizen-distributor-signer.p12
    distributor1 password: *************************
    distributor1 CA path: C:\tizen-studio\tools\certificate-generator\certificates\distributor\tizen-distributor-ca.cer
    In Configuration, Set a default profile path to 'C:\tizen-studio-data\ide\keystore\profiles.xml'.
    Wrote to 'C:\tizen-studio-data\ide\keystore\profiles.xml'.
    Succeed to add 'MyProfile' profile.
    If want to sign by this, add the file of security profiles in CLI configuration like 'tizen cli-config "default.profiles.path=C:\tizen-studio-data\ide\keystore\profiles.xml"'.
    ```
  - Ubuntu and macOS:
    ```sh
    $ dotnet tizen security-profiles add -n MyProfile -a ~/tizen-studio-data/keystore/author/mycert.p12 -pw 1234
    No exist the default path of security profiles.
    author path: ~/tizen-studio-data/keystore/author/mycert.p12
    author password: ****
    distributor1 path: ~/tizen-studio/tools/certificate-generator/certificates/distributor/tizen-distributor-signer.p12
    distributor1 password: *************************
    distributor1 CA path: ~/tizen-studio/tools/certificate-generator/certificates/distributor/tizen-distributor-ca.cer
    In Configuration, Set a default profile path to '~/tizen-studio-data/ide/keystore/profiles.xml'.
    Wrote to '~/tizen-studio-data/ide/keystore/profiles.xml'.
    Succeed to add 'MyProfile' profile.
    If want to sign by this, add the file of security profiles in CLI configuration like 'tizen cli-config "default.profiles.path=~/tizen-studio-data/ide/keystore/profiles.xml"'.
    ```
- Display the security profile list:
  - Windows&reg;:
    ```sh
    > dotnet tizen security-profiles list
    Loaded in 'C:\tizen-studio-data\ide\keystore\profiles.xml'.
    ========================================
    Name
    ========================================
    MyProfile
    ```
  - Ubuntu and macOS:
    ```sh
    $ dotnet tizen security-profiles list
    Loaded in '~/tizen-studio-data/ide/keystore/profiles.xml'.
    ========================================
    Name
    ========================================
    MyProfile
    ```
- Display the details for a security profile:
  - Windows&reg;:
    ```sh
    > dotnet tizen security-profiles list -n MyProfile
    Loaded in 'C:\tizen-studio-data\ide\keystore\profiles.xml'.
    ========================================
    'MyProfile' profile information
    ========================================
    author path: C:\tizen-studio-data\keystore\author\mycert.p12
    author password: ****
    distributor1 path: C:\tizen-studio\tools\certificate-generator\certificates\distributor\tizen-distributor-signer.p12
    distributor1 password: *************************
    distributor1 CA path: C:\tizen-studio\tools\certificate-generator\certificates\distributor\tizen-distributor-ca.cer
    ```
  - Ubuntu and macOS:
    ```sh
    $ dotnet tizen security-profiles list -n MyProfile
    Loaded in '~/tizen-studio-data/ide/keystore/profiles.xml'.
    ========================================
    'MyProfile' profile information
    ========================================
    author path: ~/tizen-studio-data/keystore/author/mycert.p12
    author password: ****
    distributor1 path: ~/tizen-studio/tools/certificate-generator/certificates/distributor/tizen-distributor-signer.p12
    distributor1 password: *************************
    distributor1 CA path: ~/tizen-studio/tools/certificate-generator/certificates/distributor/tizen-distributor-ca.cer
    ```
- Remove the security profile:
  - Windows&reg;:
    ```sh
    > dotnet tizen security-profiles remove -n MyProfile
    Loaded in 'C:\tizen-studio-data\ide\keystore\profiles.xml'.
    Wrote to 'C:\tizen-studio-data\ide\keystore\profiles.xml'.
    Succeed to remove 'MyProfile' profile
    ```
  - Ubuntu and macOS:
    ```sh
    $ dotnet tizen security-profiles remove -n MyProfile
    Loaded in '~/tizen-studio-data/ide/keystore/profiles.xml'.
    Wrote to '~/tizen-studio-data/ide/keystore/profiles.xml'.
    Succeed to remove 'MyProfile' profile
    ```

## Installing the Application on a Target
The `install` command installs the Tizen .NET application on a target.

**Syntax:**
```
dotnet tizen install [arguments] [options]
```
**Arguments:**

| Argument | Description |
| ------ | ------ |
| `<PACKAGE_FILE>` | Specifies the path of the package file. (Required) |

**Options:**

| Option | Description |
| ------ | ------ |
| `-t`, `--target <TARGET_NAME>` | Specifies the target to install the package onto. |
| `-s`, `--serial <TARGET_SERIAL>` | Specifies the serial to install the package onto. |

**Examples:**
- Install the Tizen .NET application with the package name `blank-1.0.0.tpk` on `emulator-26101`:
  - Windows&reg;:
    ```sh
    > dotnet tizen install C:\workspace\blank\bin\Debug\netcoreapp1.0\blank-1.0.0.tpk -s emulator-26101
    ```
  - Ubuntu and macOS:
    ```sh
    $ dotnet tizen install ~/workspace/blank/bin/Debug/netcoreapp1.0/blank-1.0.0.tpk -s emulator-26101
    ```

## Running the Application on a Target
The `run` command runs the Tizen application on a target.

**Syntax:**
```
dotnet tizen run [options]
```

**Options:**

| Option | Description |
| ------ | ------ |
|`-p`, `--pkgid <PACKAGE_ID>` | Specifies the Tizen package ID installed on the target. (Required) |
|`-t`, `--target <TARGET_NAME>` | Specifies the target to run the package on. |
|`-s`, `--serial <TARGET_SERIAL>` | Specifies the serial to run the package on. |

**Examples:**
- Run the Tizen .NET application with the package ID `blank` on `emulator-26101`:
  - Windows&reg;, Ubuntu, and macOS:
    ```sh
    > dotnet tizen run -p blank -s emulator-26101
    ```

## Uninstalling an Application from a Target
The `uninstall` command uninstalls a Tizen application from a target.

**Syntax:**
```
dotnet tizen uninstall [options]
```
**Options:**

| Option | Description |
| ------ | ------ |
| `-p`, `--pkgid <PACKAGE_ID>` | Specifies the Tizen package ID to be uninstalled from the target. (Required) |
| `-t`, `--target <TARGET_NAME>` | Specifies the target to uninstall the package from. |
| `-s`, `--serial <TARGET_SERIAL>` | Specifies the serial to uninstall the package from. |

**Examples:**
- Uninstall the Tizen .NET application with the package ID `blank` from `emulator-26101`:
  - Windows&reg;, Ubuntu, and macOS:
    ```sh
    > dotnet tizen uninstall -p blank -s emulator-26101
    ```

## Displaying the .NET CLI Version
The `--version` option displays the .NET CLI version number.

**Syntax:**
```
dotnet tizen [-v|--version]
```

**Examples:**
- Display the .NET CLI version number:
  - Windows&reg;, Ubuntu, and macOS:
    ```sh
    > dotnet tizen --version
    Tizen .NET Command Line Tools
    1.0.0
    ```
