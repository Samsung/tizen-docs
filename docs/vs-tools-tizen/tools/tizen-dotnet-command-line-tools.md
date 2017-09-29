# Tizen .NET Command Line Tools
The Command Line Tools provides the functionalities for developing Tizen .NET applications without the IDE.
It includes the entire development process from creating the project to running the application.

##### Prerequisite
- Tizen Baseline SDK (including Tizen C# CLI)
- Dotnet CLI (core) 2.0.0

## Creating a Tizen .NET Project
The command creates a Tizen .NET project from a template.

__Syntax:__
```
dotnet tizen create [arguments] [options]
```  

__Arguments:__

| Argument | Description |
| ------ | ------ |
| <TEMPLATE_NAME> | The template name. 

__Options:__

| Option | Description |
| ------ | ------ |
| -n,  --name <PROJECT_NAME> | The project name. |
| -o, --output <OUTPUT_DIR> | The output directory path for the output being created. If no name is specified, the name of the current directory is used. |
| -all, --show-all | Show all templates. |

__Examples:__
- Create the Tizen .NET project based on the blank template.
  - Windows®:
    ```sh
    > dotnet tizen new Tizen.Template.BlankAppCorporate -n blank -o C:\workspace
    > cd C:\workspace\blank
    ```

## Restoring the Project
The command restores the dependencies and tools of a Tizen .NET project.
All Options below are based on dotnet CLI 2.0.0.
Refer to [dotnet restore reference](https://docs.microsoft.com/en-us/dotnet/core/tools/dotnet-restore?tabs=netcore2x) for more details.

__Syntax:__
```
dotnet tizen restore [options]
```
__Options:__

| Option | Description |
| ------ | ------ |
| -s, --source <SOURCE> | Specifies a NuGet package source to use during the restore operation. This overrides all of the sources specified in the NuGet.config file(s). Multiple sources can be provided by specifying this option multiple times. |
| -r, --runtime <RUNTIME_IDENTIFIER> | Specifies a runtime for the package restore. This is used to restore packages for runtimes not explicitly listed in the <RuntimeIdentifiers> tag in the .csproj file. For a list of Runtime Identifiers (RIDs), see the RID catalog. Provide multiple RIDs by specifying this option multiple times. |
| --packages <PACKAGES_DIRECTORY> | Specifies the directory for restored packages. |
| --disable-parallel | Disables restoring multiple projects in parallel. |
| --configfile <FILE> | The NuGet configuration file (NuGet.config) to use for the restore operation. |
| --no-cache | Specifies to not cache packages and HTTP requests. |
| --ignore-failed-sources |	Only warn about failed sources if there are packages meeting the version requirement. |
| --no-dependencies	|When restoring a project with project-to-project (P2P) references, restores the root project and not the references. |
| -f, --force | Forces all dependencies to be resolved even if the last restore was successful. This is equivalent to deleting the project.assets.json file. |
| -v, --verbosity | Sets the verbosity level of the command. Allowed values are q[uiet], m[inimal], n[ormal], d[etailed], and diag[nostic]. |

__Examples:__
- Restore the Tizen .NET project
  - Windows®, Ubuntu, and Mac OS® X:
    ```sh
    > dotnet tizen restore
    ```

## Building the Project
The command builds the Tizen .NET project and its dependencies into a set of binaries.
All options and arguments below are based on dotnet CLI 2.0.0.
Refer to [dotnet build reference](https://docs.microsoft.com/en-us/dotnet/core/tools/dotnet-build?tabs=netcore2x) for more details.

__Syntax:__
```
dotnet tizen build [argument] [options]
```

__Arguments:__

| Argument | Description |
| ------ | ------ |
| \<PROJECT>	| The MSBuild project file to build. If a project file is not specified, MSBuild searches the current working directory for a file that has a file extension that ends in `proj` and uses that file. |

__Options:__

| Option | Description |
| ------ | ------ |
| -o, --output <OUTPUT_DIR> | Directory in which to place the built binaries. You also need to define --framework when you specify this option. |
| -f, --framework <FRAMEWORK> |	Compiles for a specific framework. The framework must be defined in the project file. |
| -r, --runtime <RUNTIME_IDENTIFIER> | Specifies the target runtime. For a list of Runtime Identifiers (RIDs), see the RID catalog. |
| -c, --configuration <CONFIGURATION> |	Defines the build configuration. The default value is Debug.|
| --version-suffix <VERSION_SUFFIX> | Defines the version suffix for an asterisk (*) in the version field of the project file. The format follows NuGet's version guidelines. |
| --no-incremental | Marks the build as unsafe for incremental build. This turns off incremental compilation and forces a clean rebuild of the project's dependency graph. |
| --no-dependencies | Ignores project-to-project (P2P) references and only builds the root project specified to build. |
| --no-restore | Doesn't perform an implicit restore during build. |
| -f, --force | Forces all dependencies to be resolved even if the last restore was successful. This is equivalent to deleting the project.assets.json file. |
| -v, --verbosity | Sets the verbosity level of the command. Allowed values are q[uiet], m[inimal], n[ormal], d[etailed], and diag[nostic]. |

__Examples:__
- Build the Tizen .NET project
  - Windows®, Ubuntu, and Mac OS® X:
    ```sh
    > dotnet tizen build
    ```

## Installing the Application on a Target
The command installs the Tizen .NET application on a target.

__Syntax:__
```
dotnet tizen install [arguments] [options]
```
__Arguments:__

| Argument | Description |
| ------ | ------ |
| <PACKAGE_FILE> | The path of the package file. (Required) |

__Options:__

| Option | Description |
| ------ | ------ |
| -t, --target <TARGET_NAME> | The target name to install the package. |
| -s, --serial <TARGET_SERIAL> | The serial to install the package. |

__Examples:__
- Install the Tizen .NET application, whose package name is blank-1.0.0.tpk, on the emulator-26101.
  - Windows®:
    ```sh
    > dotnet tizen install C:\workspace\blank\bin\Debug\netcoreapp1.0\blank-1.0.0.tpk -s emulator-26101
    ```
  - Ubuntu and Mac OS® X:
    ```sh
    $ dotnet tizen install ~/workspace/blank/bin/Debug/netcoreapp1.0/blank-1.0.0.tpk -s emulator-26101
    ```

## Running the Application on a Target
The command runs the Tizen application on a target.

__Syntax:__
```
dotnet tizen run [options]
```

__Options:__

| Option | Description |
| ------ | ------ |
|-p, --pkgid <PACKAGE_ID> | The Tizen package ID installed on the target. (Required) |
|-t, --target <TARGET_NAME> | The target name to run the package. |
|-s, --serial <TARGET_SERIAL> | The serial to run the package. |

__Examples:__
- Run the basic application, whose package ID is org.tizen.example.blank, on the emulator-26101.
  - Windows®, Ubuntu, and Mac OS® X:
    ```sh
    > dotnet tizen run -p org.tizen.example.blank -s emulator-26101
    ```

## Uninstalling the Application on a Target
The command uninstalls the Tizen application on a target.

__Syntax:__
```
dotnet tizen uninstall [options]
```
__Options:__

| Option | Description |
| ------ | ------ |
| -p, --pkgid <PACKAGE_ID> |	The Tizen package ID installed on the target. (Required) |
| -t, --target <TARGET_NAME> |	The target name to uninstall the package. |
| -s, --serial <TARGET_SERIAL> |	The serial to uninstall the package. |

__Examples:__
- Uninstall the basic application, whose package ID is org.tizen.basic, from the emulator-26101.
  - Windows®, Ubuntu, and Mac OS® X:
    ```sh
    > dotnet tizen uninstall -p org.tizen.example.blank -s emulator-26101
    ```

## Cleaning the Project
The command cleans the Tizen project. If you clean the project, all build output directories under the project root path are removed.

__Syntax:__
```
dotnet tizen clean [arguments]
```
__Arguments:__

| Argument | Description |
| ------ | ------ |
| <PROJECT_DIR> | The project directory. Defaults to current directory if nothing is specified. |

__Examples:__
- Clean the project.
  - Windows®:
    ```sh
    > dotnet tizen clean C:\workspace\blank
    ```
  - Ubuntu and Mac OS® X:
    ```sh
    $ dotnet tizen clean ~/workspace/blank
    ```

## Setting Configuration Options
The command displays, sets, replaces, and removes CLI configuration options. The CLI configuration keys are:
- default.sdb.timeout=<TIMEOUT_VALUE>: Sets the default connection timeout value. The default is 60000 milliseconds.
- default.profiles.path=<PROFILE_PATH>: Sets the the directory path where the profiles.xml file is located.

__Syntax:__
```
dotnet tizen cli-config [arguments] [options]
```

__Arguments:__

| Argument | Description |
| ------ | ------ |
| \<KEY>=\<VALUE> | Sets a value for the CLI configuration key. |

__Options:__

| Option | Description |
| ------ | ------ |
| -l, --list | Displays the list of all CLI configuration keys and values. |
| -d, --delete \<KEY> | Removes the CLI configuration key and value. |
| -g, --global | Specifies whether the operation must be done for a global scope (for all installed SDKs or for the current Tizen Baseline SDK only). |

__Examples:__
- Display a list of all configurations for which values are set.
  - Windows®, Ubuntu, and Mac OS® X:
    ```sh
    > dotnet tizen cli-config -l
    default.sdb.timeout=60000 
    ```
- Set a profiles.xml path globally.
  - Windows®:
    ```sh
    > dotnet tizen cli-config –g "default.profiles.path=C:\workspace\.metadata\.plugins\org.tizen.common.sign\profiles.xml"
    ```
    Ubuntu and Mac OS® X:
    ```sh
    $ dotnet tizen cli-config –g default.profiles.path=~/workspace/.metadata/.plugins/org.tizen.common.sign/profiles.xml
    ```

## Issuing a Tizen Certificate
The command generates a Tizen certificate for your application. If you want to upload your application to the Tizen store or install the application to a Tizen device, you must generate a Tizen certificate.

__Syntax:__
```
dotnet tizen certificate [options]
```

__Options:__

| Option | Description |
| ------ | ------ |
| -a, --alias <ALIAS_NAME> | The alias name of the certificate. (Required) |
| -pw, --password <PASSWORD> | The password of the certificate. (Required) |
| -n, --name <USER_NAME> | The user name. |
| -c, --country <COUNTRY_CODE> | The user's country code, which consists of 2 letters. |
| -s, --state <STATE> | The user's state. |
| -ct, --city <CITY> | The user's city. |
| -og, --organization <ORGANIZATION> | The user organization. |
| -u, --unit <UNIT> | The user's organization unit. |
| -e, --email <EMAIL> |	The user email. |
| -fn, --filename <CERT_FILE_NAME> | The file name without a file extension. A certificate file is created with the file name. If you skip this option, the default file name, author, is used on creating the certificate file. |
| -o, --output <CERT_OUTPUT_DIR> | The output directory path to create the certificate. If you skip this option, the default output directory path, <TIZEN_BASELINE_SDK_DATA>/keystore/author/, is used on saving the certificate file. |

__Examples:__
- Generate a certificate.
  - Windows®:
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
  - Ubuntu and Mac OS® X:
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

## Managing a Security Profile
The command manages the security profiles, which are a set of signing certificates for a Tizen application.
The command consists of three sub-commands. __add__ command adds the specified security profile, which can contain several certificates. __list__ command displays security profiles. If you specify the name of the security profile, the detailed information of the specified security profile is displayed. __remove__ command removes the specified security profile.

__Syntax:__
```
dotnet tizen security-profiles <sub-command> [options]
```
__Sub-commands and options:__

| Sub-command | Option | Description |
| ------ | ------ | ------ |
add [options] |-n, --name <PROFILE_NAME> | The name of the security profile to add. (Required) |
|| -a, --author <AUTHOR_PATH> | The directory path where the author certificate file is located. The format of the certificate is PKCS#12, and the file extension is .p12. (Required) |
|| -pw, --password <AUTHOR_PASSWORD> | The password used to access the author certificate. (Required) |
|| -c, --ca <AUTHOR_CA_PAH> | The directory path where the author CA certificate file is located. The file extension of the CA certificate is .cer. |
|| -r, --rootca <AUTHOR_ROOT_CA_PATH> | The directory path where the author root CA certificate file is located. The file extension of the root CA certificate is .cer. |
|| -d, --dist <DIST_PATH> | The directory path where the distributor certificate file is located. If you skip this option, the default distributor certificate file embedded in the Tizen baseline SDK is used. |
|| -dp, --dist-password <DIST_PASSWORD> | The password of the distributor certificate. |
|| -dc, --dist-ca <DIST_CA_PATH> | The directory path where the distributor CA certificate file is located. |
|| -dr, --dist-rootca <DIST_ROOT_CA_PATH> | The directory path where the distributor root CA certificate file is located.
|| --force|	If there is no Profile XML, then generates a file. |
|| -p, --path <PROFILE_PATH> | The directory path where the profiles.xml file is located. If you skip this option, the value of the default.profiles.path key in the CLI configuration is used to find the profiles.xml file, which consists of new security profiles that are generated in the <TIZEN_BASELINE_SDK_DATA>/keystore/ directory. The directory path is added to the CLI configuration. |
| list [options] | -n, --name <PROFILE_NAME> | The name of the security profile to list. If you skip this option, a set of the security profile names in the profiles.xml file is displayed. |
|| -p, --path <PROFILE_PATH> | The directory path where the profiles.xml file is located. If you skip this option, the value of the default.profiles.path key in the CLI configuration is used to find the profiles.xml file, which consists of new security profiles that are generated in the <TIZEN_BASELINE_SDK_DATA>/keystore/ directory. The directory path is added to the CLI configuration. |
| remove [options] | -n, --name <PROFILE_NAME> | The name of the security profile to remove. (Required) |
|| -p, --path <PROFILE_PATH> | The directory path where the profiles.xml file is located. If you skip this option, the value of the default.profiles.path key in the CLI configuration is used to find the profiles.xml file, which consists of new security profiles that are generated in the <TIZEN_BASELINE_SDK_DATA>/keystore/ directory. The directory path is added to the CLI configuration. |

__Examples:__
- Add a new security profile.
  - Windows®:
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
    Ubuntu and Mac OS® X:
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
- Display the security profile list.
  - Windows®:
    ```sh
    > dotnet tizen security-profiles list
    Loaded in 'C:\tizen-studio-data\ide\keystore\profiles.xml'.
    ========================================
    Name
    ========================================
    MyProfile
    ```
  - Ubuntu and Mac OS® X:
    ```sh
    $ dotnet tizen security-profiles list
    Loaded in '~/tizen-studio-data/ide/keystore/profiles.xml'.
    ========================================
    Name
    ========================================
    MyProfile
    ```
- Display the detailed information of a security profile.
  - Windows®:
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
  - Ubuntu and Mac OS® X:
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
- Remove the security profile.
  - Windows®:
    ```sh
    > dotnet tizen security-profiles remove -n MyProfile
    Loaded in 'C:\tizen-studio-data\ide\keystore\profiles.xml'.
    Wrote to 'C:\tizen-studio-data\ide\keystore\profiles.xml'.
    Succeed to remove 'MyProfile' profile
    ```
  - Ubuntu and Mac OS® X:
    ```sh
    $ dotnet tizen security-profiles remove -n MyProfile
    Loaded in '~/tizen-studio-data/ide/keystore/profiles.xml'.
    Wrote to '~/tizen-studio-data/ide/keystore/profiles.xml'.
    Succeed to remove 'MyProfile' profile
    ```

## Displaying the CLI Version
The option displays the CLI version number.

__Syntax:__
```
dotnet tizen [-v|--version]
```

__Examples:__
- Display the CLI version number.
  - Windows®, Ubuntu, and Mac OS® X:
    ```sh
    > dotnet tizen --version
    Tizen .NET Command Line Tools
    1.0.0
    ```
