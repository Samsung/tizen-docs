# Tizen-Core Command Line Interface Commands

The Tizen-Core Command Line Interface (CLI) provides functionalities for developing Tizen applications without Tizen Studio. It includes the entire development process from creating the project to running the application.

The CLI is located in the `$<TIZEN_STUDIO>/tools/tizen-core/` directory. For developing an application using the CLI, add the CLI directory path to the `$PATH` environment variable using the following command:

```
export PATH=$PATH:$<TIZEN_STUDIO>/tools/tizen-core/
```

## Initialize the workspace

In Tizen-Core, workspace is used for project creation. The workspace concept is similar to Visual Studio Solution. Each workspace folder can contain the main project along with the dependent projects. Workspace contains configuration YAML file which is created during initialization of workspace. This file contains the entire configuration for that particular workspace.

Create a new folder and initialize workspace using the following command:

**Syntax:**
```
tz init [options]
```

**Options:**

| Option                 | Description                              |
|------------------------|------------------------------------------|
| `-p`, `--profile=STRING`      | Specifies the profile name. |
| `-w`, `--ws-dir=STRING`       | Specifies the workspace directory. |
| `-a`, `--arch={arm|aarch64|x86}`         | Specifies the architecture type: x86 (default). |
| `-b`, `--build-type={debug|release}`   | Specifies the build type: debug (default). |
| `-r`, `--rootstrap=STRING` | Rootstrap for compiling project. (e.g: "--rootstrap=private" for using private rootstrap). |
| `-s`, `--skip-vs-files` | Skip generating files needed for Visual Studio. |


**Examples:**

- To initialize the mobile-6.5 workspace, use the following command:


  Windows&reg;:
  ```
  > mkdir C:\Users\workspace
  > tz init -p mobile-6.5 -w C:\Users\workspace
  ```

  Ubuntu and macOS:

  ```
  $ mkdir ~/workspace
  $ tz init -p mobile-6.5 -w ~/workspace
  ```

## Set workspace configuration options

The command displays and sets the workspace configuration options:

**Syntax:**

```
tz set [options]
```

**Options:**

| Option                 | Description                              |
|------------------------|------------------------------------------|
|  `--help`                                                          | Show context-sensitive help. |
|  `--version`                                                       | Print version information and quit. |
|  `-w`, `--ws-dir="."`                                              | Working directory. |
|  `-g`, `--auto-gen={true|false}`                                   | Auto build file generation enable. |
|  `-i`, `--package-id=STRING`                                       | Package ID for the Tizen package. |
|  `-v`, `--version=STRING`                                          | Version for the Tizen package. |
|  `-x`, `--profiles-path="-"`                                       | Path of profiles.xml containing the signing profiles. |
|  `-s`, `--signing-profile="-"`                                     | Signing profile used for Tizen packaging. |
|  `-b`, `--build-type={debug|release}`                              | Specifies the build type. |
|  `-r`, `--rootstrap=STRING`                                        | Rootstrap used for compiling native app. |
|  `-c`, `--compiler={gcc|llvm}`                                     | Compiler for native app compilation. |
|  `-d`, `--dotnet-cli-path=STRING`                                  | Path of dotnet-cli. |
|  `-m`, `--msbuild-path=STRING`                                     | Path of msbuild. |
|  `-D`, `--dotnet-build-tool={msbuild|dotnet}`                      | Tool for dotnet project build. |
|  `-W`, `--working-folder="-"`                                      | Working folder for web/dotnet workspace. |
|  `-N`, `--tizen-net-version=STRING`                                | Nuget version of Tizen.NET. |
|  `-n`, `--tizen-netsdk-version=STRING`                             | Nuget version of Tizen.NET.Sdk. |
|  `-X`, `--xamarin-forms-version=STRING`                            | Nuget version of Tizen.Xamarin.Forms. |
|  `-B`, `--ms-build-tasks-version=STRING`                           | Nuget version of MSBuild.Tasks. |
|  `-U`, `--tizen-wearable-circle-ui-version=STRING`                 | Nuget version of Tizen.Wearable.CircleUI. |
|  `-k`, `--tizen-open-tk-version=STRING`                            | Nuget version of Tizen.OpenTK. |
|  `-u`, `--tizen-nui-xaml-version=STRING`                           | Nuget version of Tizen.NUI.Xaml. |
|  `-h`, `--tizen-hot-reload-version=STRING`                         | Nuget version of Tizen.Hotreload. |
|  `-A`, `--arch={arm|aarch64|x86}`                                  | Specifies the architecture for build. |
|  `-S`, `--src-file-patterns=SRC-FILE-PATTERNS,...`                 | Source file patterns excluded from build, format: pattern1, pattern2. |
|  `-T`, `--test-file-patterns=TEST-FILE-PATTERNS,...`               | Source file patterns included for test mode, format: pattern1, pattern2. |
|  `-C`, `--chrome-path=STRING`                                      | Path of the Chrome executable. |
|  `-O`, `--chrome-simulator-options=CHROME-SIMULATOR-OPTIONS,...`   | List of options for Chrome simulator, format: arg1, arg2. |
|  `-M`, `--chrome-simulator-data-path=STRING`                       | Path of Chrome simulator data. |
|  `-L`, `--chrome-inspector-options=CHROME-INSPECTOR-OPTIONS,...`   | List of options for Chrome inspector, format: arg1, arg2. |
|  `-e`, `--chrome-inspector-data-path=STRING`                       | Path of Chrome inspector data. |
|  `-o`, `--optimize={true|false}`                                   | Size optimization of `wgt` for web workspace. |
|  `-P`, `--projects=STRING`                                         | List of projects in the workspace and their dependencies, format: proj1=[dep1:dep2:dep3], proj2. |

**Examples:**

- To set llvm, arm and release type for build, use the following command:
  
  Windows&reg;:
  ```
  > tz set -A arm -c llvm -b release -w C:\Users\workspace
  ```

  Ubuntu and macOS:
  ```
  $ tz set -A arm -c llvm -b release -w ~/workspace
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
|  `-w`, `--ws-dir="."`                | Working directory. |
|  `-g`, `--auto-gen`                  | Returns true if auto build file generation enabled. |
|  `-t`, `--workspace-type`            | Workspace type. |
|  `-i`, `--package-id`                | Package ID for the Tizen package. |
|  `-v`, `--version`                   | Version for the Tizen package. |
|  `-p`, `--profile`                   | Tizen profile and API version. |
|  `-x`, `--profiles-path`             | Path of profiles.xml containing the signing profiles. |
|  `-s`, `--signing-profile`           | Signing profile used for Tizen packaging. |
|  `-b`, `--build-type`                | Build type. |
|  `-r`, `--rootstrap`                 | Rootstrap used for compiling native app. |
|  `-c`, `--compiler`                  | Compiler for native app compilation. |
|  `-d`, `--dotnet-cli-path`           | Path of dotnet-cli. |
|  `-m`, `--msbuild-path`              | Path of msbuild. |
|  `-D`, `--dotnet-build-tool`         | Tool for dotnet project build. |
|  `-W`, `--working-folder`            | Working folder for web/dotnet workspace. |
|  `-N`, `--tizen-net-version`         | Nuget version of Tizen.NET. |
|  `-n`, `--tizen-netsdk-version`      | Nuget version of Tizen.NET.Sdk. |
|  `-X`, `--xamarin-forms-version`     | Nuget version of Tizen.Xamarin.Forms. |
|  `-B`, `--ms-build-tasks-version`    | Nuget version of MSBuild.Tasks. |
|  `-U`, `--tizen-wearable-circle-ui-version` | Nuget version of Tizen.Wearable.CircleUI. |
|  `-k`, `--tizen-open-tk-version`     | Nuget version of Tizen.OpenTK. |
|  `-u`, `--tizen-nui-xaml-version`    | Nuget version of Tizen.NUI.Xaml. |
|  `-h`, `--tizen-hot-reload-version` | Nuget version of Tizen.Hotreload. |
|  `-A`, `--arch`                      | Arch for build. |
|  `-S`, `--src-file-patterns`         | Source file patterns excluded from build. |
|  `-T`, `--test-file-patterns`        | Source file patterns included for test mode. |
|  `-C`, `--chrome-path`               | Path of Chrome executable. |
|  `-O`, `--chrome-simulator-options` | List of options for Chrome simulator. |
|  `-M`, `--chrome-simulator-data-path` | Path of Chrome simulator data. |
|  `-L`, `--chrome-inspector-options` | List of options for Chrome inspector. |
|  `-e`, `--chrome-inspector-data-path` | Path of Chrome inspector data. |
|  `-o`, `--optimize`                  | Returns true if optimization of `wgt` for web workspace is enabled. |
|  `-P`, `--projects`                  | List of projects in the workspace and their dependencies. |
|  `-a`, `--all`                       | Return the values of all the attrs. |

**Examples:**

- The command displays the compiler, architecture, and the build type set:

  Windows&reg;:
  ```
  > tz get -A -c -b -w C:\Users\workspace
    build_type:debug
    compiler:llvm
    arch:x86
  ```
  
  Ubuntu and macOS:
  ```
  $ tz get -A -c -b -w ~/workspace
    build_type:debug
    compiler:llvm
    arch:x86
  ```

## Display profile templates

The command displays the list of project templates for all the versions of the given workspace type. By default, it displays all the available native templates:

**Syntax:**

```
tz list templates [options]
```

**Options:**

| Option           | Description                              |
|------------------|------------------------------------------|
| `-t`, `--type={native|web|dotnet}` | Display all the templates for given profile: native (default). |

**Examples:**

- List of all the native application templates:

  Windows&reg;, Ubuntu, and macOS:

  ```
  > tz list -t native
  wearable-6.5:
    basic_ui [native_app]
    basic_edc_ui [native_app]
    imi_app [native_app]
    serviceapp [native_app]
    shared_library [shared_lib]
    static_library [static_lib]
    widget [native_app]

  mobile-6.5:
    basic_ui [native_app]
    basic_edc_ui [native_app]
    imi_app [native_app]
    serviceapp [native_app]
    component_app [native_app]
    widget [native_app]
    shared_library [shared_lib]
    static_library [static_lib]
  ```

## Display workspace templates

The command displays a list of project templates available for the given workspace:

**Syntax:**

```
tz templates [options]
```

**Options:**

| Option           | Description                              |
|------------------|------------------------------------------|
| `-w`, `--ws-dir=`|  Specifies the workspace directory.      |
| `-t`, `--type={native|web|dotnet}`| Specifies the project type. |
**Examples:**

- List of available native templates for the workspace:

  Windows&reg;: 
  ```
  > tz templates -t native -w C:\Users\workspace
  native templates:
    basic_ui [native_app]
    basic_edc_ui [native_app]
    imi_app [native_app]
    serviceapp [native_app]
    component_app [native_app]
    widget [native_app]
    shared_library [shared_lib]
    static_library [static_lib]
  ```

  Ubuntu and macOS:
  ```
  $ tz templates -t native -w ~/workspace
  native templates:
    basic_ui [native_app]
    basic_edc_ui [native_app]
    imi_app [native_app]
    serviceapp [native_app]
    component_app [native_app]
    widget [native_app]
    shared_library [shared_lib]
    static_library [static_lib]
  ```

## Display installed rootstraps

The command displays a list of all the installed rootstraps in Tizen Studio:

Windows&reg;, Ubuntu, and macOS:
```
tz list rootstraps
[ROOTSTRAP]                              [Information]
da-hfp-6.0-device.core.private           da-hfp 6.0, armel
iot-headless-6.0-device.core             Iot-headless 6.0, armel
iot-headless-6.5-device.core             Iot-headless 6.5, armel
mobile-6.0-device.core                   Mobile 6.0, armel
mobile-6.0-emulator.core                 Mobile 6.0, i586
mobile-6.5-device.core                   Mobile 6.5, armel
mobile-6.5-emulator.core                 Mobile 6.5, i586
```

## Create a Tizen project

The command creates a Tizen native or web or dotnet project from a template in the workspace:

**Syntax:**

```
tz new [options]
```

**Options:**

| Option                 | Description                              |
|------------------------|------------------------------------------|
| `-t`, `--template`     | Specifies the template name. |
| `-p`, `--path`         | Specifies the project name. |
| `-w`, `--ws-dir`       | Specifies the workspace directory. |
| `-T`, `--type={native|web|dotnet}`         | Specifies the profile type. |
| `-s`, `--sample`       | Option used to create samples (-s "Category_name, application_name"). |


**Examples:**

- Create a native project based on the basic UI native template in the workspace:

  Windows&reg;:
  ```
  > tz new -t basic_ui -p basicnative -T native -w C:\Users\workspace
  ```

  Ubuntu and macOS:
  ```
  $ tz new -t basic_ui -p basicnative -T native -w  ~/workspace
  ```

- Create a web project based on the basic UI web template in the workspace.

  Windows&reg;:
  ```
  > tz new -t BasicUI -p basicweb -w C:\Users\workspace
  ```

  Ubuntu and macOS:
  ```
  $ tz new -t BasicUI -p basicweb -w  ~/workspace
  ```

- Create a dotnet project based on the ElmSharp template in the workspace.

  Windows&reg;:
  ```
  > tz new -t TizenElmSharpApp -p elmsharp -T dotnet -w C:\Users\workspace
  ```

  Ubuntu and macOS:
  ```
  $ tz new -t TizenElmSharpApp -p elmsharp -T dotnet -w ~/workspace
  ```

## List and creation of Tizen samples

This section describes how to list and create native and web samples. Initialize the workspace as mentioned in the section [Initialize the Workspace](#initialize-the-workspace).

To list the samples available for the workspace, use the following command:

**Syntax:**
```
tz samples [options]
```

**Options:**

| Option                 | Description                              |
|------------------------|------------------------------------------|
| `-w`, `--ws-dir`       | Specifies the workspace directory. |
| `-t`, `--type=`       | Specifies the project type. |

**Examples:**

- List of samples for the mobile-6.5 workspace:

  Windows&reg;:
  ```
  > tz samples -t native -w C:\Users\workspace
  Context :
    Context Trigger
  Locations :
    Gps service
    Geofence
    Geofence3
    Maps
  Machine Learning :
    Machine Learning Single
    Machine Learning Text Classification
  ```

  Ubuntu and macOS:
  ```
  > tz samples -t native -w ~/workspace
  Context :
    Context Trigger
  Locations :
    Gps service
    Geofence
    Geofence3
    Maps
  Machine Learning :
    Machine Learning Single
    Machine Learning Text Classification
  ```

### Create a sample in the workspace

 To create a sample in the workspace, use the following command:

**Syntax:**

```
tz new -T type -s "Category,Application_name"
```

**Examples:**

- The following example creates Maps sample project in the workspace.

  Windows&reg;:
  ```
  > tz new -s "Locations,Maps" -T native -w C:\Users\workspace
  ```

  Ubuntu and macOS:
  ```
  $ tz new -s "Locations,Maps" -T native -w ~/workspace
  ```


## MultiApp and add dependency between projects

The command adds dependency between the projects in the MultiApp workspace. Only the working_folder project (specified in the working_folder attribute in tizen_workspace.yaml) and its dependencies are picked for build and pack.

**Syntax:**

```
tz add-deps [options]
```

**Options:**

| Option                                  | Description                              |
|---------------------------------------|----------------------------------------|
| `<project>`                  | Project path relative to workspace. |
| `-d`, `--deps=STRING`         | Project dependencies, comma separated: -d proj1, proj2. |
| `-w`, `--ws-dir=STRING`      | Workspace directory. |
| `--help`                     | Show context-sensitive help. |


**Examples:**

- Following command creates native BasicUI and ServiceApp in the workspace and ServiceApp is added as dependent project of BasicUI:


  Windows&reg;:
  ```
  > tz new -t basic_ui -p basic -T native -w C:\Users\workspace
  > tz new -t serviceapp -p service -T native -w C:\Users\workspace
  > tz add-deps basic -d service -w C:\Users\workspace
  ```

  Ubuntu and macOS:
  ```
  $ tz new -t basic_ui -p basic -T native -w ~/workspace
  $ tz new -t serviceapp -p service -T native -w ~/workspace
  $ tz add-deps basic -d service -w ~/workspace
  ```


## Set the working folder

The working folder is used to select the project in the workspace that needs to be built and run. If there are multiple projects in the workspace, we need to set the working folder before build and other commands are run. The path is set depending upon the project type. Once the working folder is set, the main project which is set as the working folder and its dependent projects are built and packaged.
To set the path of the working folder, use the following command:

- The path can be either relative to the workspace path or the absolute path of the project.

**Syntax:**
```
tz set -W [path] [options]
```

**Options:**

| Option                 | Description                              |
|------------------------|------------------------------------------|
| `-w`, `--ws-dir`       | Specifies the workspace directory. |
| `-W`, `--working-folder`       | Specifies the project to be built in the workspace. |

**Examples:**

- To build basicnative project in the workspace, set the working folder like mentioned below:
  
  Windows&reg;:
  ```
  > tz set -W basicnative -w C:\Users\workspace
  ```

  Ubuntu and macOS: 
  ```
  $ tz set -W basicnative -w ~/workspace
  ```

- To build the web project in the workspace, set the working folder as described below:
  
  Windows&reg;:
  ```
  > tz set -W basicweb -w C:\Users\workspace
  ```

  Ubuntu and macOS: 
  ```
  $ tz set -W basicweb -w ~/workspace
  ```

- To build the dotnet project in the workspace, set the working folder as described below:
  
  Windows&reg;:
  ```
  > tz set -W elmsharp -w C:\Users\workspace
  ```

  Ubuntu and macOS: 
  ```
  $ tz set -W elmsharp -w ~/workspace
  ```


## Build the project

The command builds the Tizen native, web, and dotnet projects. After the working folder is set, the project and its dependent projects are built. The same command can be used to build all the 3 type of projects.

**Syntax:**

```
tz build [options]
```

**Options:**

| Option                 | Description                              |
|------------------------|------------------------------------------|
| `-w`, `--ws-dir`       | Specifies the workspace directory. |


**Examples:**

- Build the native project with the default `x86`, `llvm`, and `debug` options:

  Windows&reg;:
  ```
  > tz build -w C:\Users\workspace
  ```

  Ubuntu and macOS:
  ```
  $ tz build -w ~/workspace
  ```

- Build the native project with the  `arm`, `llvm`, and `release` options:

  Windows&reg;:
  ```
  > tz set -A arm -b release -c gcc -w C:\Users\workspace
  > tz build -w C:\Users\workspace
  ```

  Ubuntu and macOS:
  ```
  $ tz set -A arm -b release -c gcc -w ~/workspace
  $ tz build -w ~/workspace
  ```

## Clean the project

The command cleans the Tizen workspace. If you clean the workspace, all the output files generated during  
build are removed.

**Syntax:**

```
tz clean [options]
```

**Options:**

| Option                   | Description                              |
|--------------------------|------------------------------------------|
| `-w`, `--ws-dir`       | Specifies the workspace directory. |

**Examples:**

- Clean the project.

  Windows&reg;:
  ```
  > tz clean -w C:\Users\workspace
  ```

  Ubuntu and macOS:
  ```
  $ tz clean -w ~/workspace
  ```

## Issue a Tizen certificate

The command generates a Tizen certificate for your application. If you want to upload your application to the the official site for Tizen applications or install the application on a Tizen device, you must generate a Tizen certificate.

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

## Package a Tizen application with sign

The command builds and packages the Tizen application with signing. If there is a package file in the option (-b), the package is re-signed. The Tizen application is signed with a certified profile in the `tizen-studio-data/profile/profiles.xml` file. Certificate security-profiles can be created as mentioned in the section [manage a security profile](#manage-a-security-profile). The package is created for the project which is set as a working folder as mentioned in the section [Set the working folder](#set-the-working-folder).

**Syntax:**

```
tz pack [options]
```

**Options:**

| Option                            | Description                              |
|-----------------------------------|------------------------------------------|
| `-w`, `--ws-dir`       | Specifies the workspace directory. |
| `-t`, `--type={tpk/wgt}`          | [repack] Final pkg type (`tpk`/`wgt`). Default: `tpk`. |
| `-s`, `--sign-profile=STRING` | [repack] Specifies the security profile name for signing. If you skip this option, the CLI uses the active profile or the default profile. The default profile is only valid for the Emulator or reference devices. |
| `-p, --profiles-path=STRING`          | [repack] Path to profiles.xml. Default: tizen-studio-data/profile/profiles.xml specified in config.yaml. |
| `-r --ref-pkgs=STRING`          | [repack] Paths of the reference projects, for hybrid packaging, semicolon separated paths:pkg1;pkg2. |
| `-b --base-pkg=STRING`          | [repack] Path of the base pkg. |
| `-o --out-path=STRING`          | [repack] Path of the output pkg: path/to/finalpkg.ext Default: base pkg path. |

**Examples:**

- Package the project.

  Windows&reg;:
  ```
  > tz pack -w C:\Users\workspace
  ninja: Entering directory `debug\mobile-6.5\x86'
  [5/6] SIGN package files
  Signing using certificates:
        Author cert : E:\tizen-studio\tools\certificate-generator\certificates\developer\tempMobile.p12
        Distributor cert : E:\tizen-studio\tools\certificate-generator\certificates\distributor\tizen-distributor-signer.p12
        Distributor2 cert :

  Package File Location: C:\Users\workspace\debug\mobile-6.5\x86\org.example.val-0.0.1-x86.tpk
  [6/6] STAMP obj/build/pack.stamp
  ```

  Ubuntu and macOS:
  ```
  $ tz pack -w ~/workspace
  ninja: Entering directory `debug/mobile-6.5/x86'
  [5/6] SIGN package files
  Signing using certificates:
          Author cert : /home/user1/tizen-studio/tools/certificate-generator/certificates/developer/tempMobile.p12
          Distributor cert : /home/user1/tizen-studio/tools/certificate-generator/certificates/distributor/tizen-distributor-signer.p12
          Distributor2 cert :

  Package File Location: /home/user1/mcd_apps/val/debug/mobile-6.5/x86/org.example.val-0.0.1-x86.tpk
  [6/6] STAMP obj/build/pack.stamp
  ```

- Repackage existing pkg file.

  Windows&reg;:
  ```
  > tz pack -t tpk -b C:\Users\workspace\debug\mobile-6.5\x86\org.example.val-0.0.1-x86.tpk
  Using default certificates
  Signing using certificates:
          Author cert : E:\tizen-studio\tools\certificate-generator\certificates\developer\tempMobile.p12
          Distributor cert : E:\tizen-studio\tools\certificate-generator\certificates\distributor\tizen-distributor-signer.p12
          Distributor2 cert :

  Package File Location: C:\Users\workspace\debug\mobile-6.5\x86\org.example.val-0.0.1-x86.tpk
  ```

  Ubuntu and macOS:
  ```
  $ tz pack -b /home/user1/workspace/debug/mobile-6.5/x86/org.example.val-0.0.1-x86.tpk
  Signing using certificates:
          Author cert : /home/user1/tizen-studio/tools/certificate-generator/certificates/developer/tempMobile.p12
          Distributor cert : /home/user1/tizen-studio/tools/certificate-generator/certificates/distributor/tizen-distributor-signer.p12
          Distributor2 cert :

  Package File Location: /home/user1/workspace/debug/mobile-6.5/x86/org.example.val-0.0.1-x86.tpk
  ```

- Merge and repackage existing pkg files.

  Windows&reg;:
  ```
  > tz pack -t tpk -r C:\Users\existing_pkgs\org.example.val.serviceapp-1.0.0-x86.tpk -b C:\Users\existing_pkgs\org.example.val.basic_ui-1.0.0-x86.tpk -o C:\Users\existing_pkgs\merged_pkg.tpk
  Using default certificates
  Signing using certificates:
          Author cert : E:\tizen-studio\tools\certificate-generator\certificates\developer\tempMobile.p12
          Distributor cert : E:\tizen-studio\tools\certificate-generator\certificates\distributor\tizen-distributor-signer.p12
          Distributor2 cert :
  Package File Location: C:\Users\existing_pkgs\merged_pkg.tpk
  ```

  Ubuntu and macOS:
  ```
  $ tz pack -t tpk -r ~/existing_pkgs/org.example.val.serviceapp-1.0.0-x86.tpk -b ~/existing_pkgs/org.example.val.basic_ui-1.0.0-x86.tpk -o ~/existing_pkgs/merged_pkg.tpk
  Signing using certificates:
          Author cert : /home/user1/tizen-studio/tools/certificate-generator/certificates/developer/tempMobile.p12
          Distributor cert : /home/user1/tizen-studio/tools/certificate-generator/certificates/distributor/tizen-distributor-signer.p12
          Distributor2 cert :

  Package File Location: /home/user1/existing_pkgs/merged_pkg.tpk
  ```  

## Details on creating hybrid projects in the workspace 

A hybrid workspace can contain all the 3 different types of projects (native, web, and dotnet) in it.
Hybrid projects can be created in the normal workspace, after initializing the workspace with `tz init` as mentioned in the section [Initialize the Workspace](#initialize-the-workspace).

**Example:**

Different kinds of projects can be created from the templates and samples using the `-T project_type` argument in `tz new` as mentioned in the section [Create a Tizen Project](#create-a-tizen-project).

**Examples:**

Windows&reg;:
```
tz new -T native -t basic_ui -p basicnative -w C:\Users\workspace
tz new -T web -t BasicUI -p basicweb -w C:\Users\workspace
tz new -T dotnet -t TizenElmSharpApp -p elmsharp -w C:\Users\workspace
```

Ubuntu and macOS:
```
tz new -T native -t basic_ui -p basicnative -w ~/workspace
tz new -T web -t BasicUI -p basicweb -w ~/workspace
tz new -T dotnet -t TizenElmSharpApp -p elmsharp -w ~/workspace
```

Once the different types of projects are created in the workspace, dependencies can be added between the projects as mentioned in the section [adding dependency between projects](#multiapp-and-add-dependency-between-projects).

The rest of the functionalities: [build](#build-the-project), [pack](#package-a-tizen-application-with-signing), [install](#install-the-application-on-a-target), [run](#run-the-application-on-a-target), [setting working_folder](#set-the-working-folder), [adding dependency](#multiapp-and-add-dependency-between-projects) have the same behaviour in the hybrid workspace.


## Install the application on a target

The command installs a Tizen application on a specified target or serial device:

**Syntax:**

```
tz install [options]
```

**Options:**

| Option                             | Description                              |
|------------------------------------|------------------------------------------|
| `-w`, `--ws-dir=STRING`       | Specifies the workspace directory. |
| `-t`, `--target=STRING`     | Specifies the target name to install the package. |
| `-s`, `--serial=STRING`   | Specifies the serial to install the package. |

**Examples:**

- Install the application present in the workspace.

  Windows&reg;:
  ```
  > tz install -w C:\Users\workspace
  ```

  Ubuntu and macOS:
  ```
  $ tz install -s emulator-26101 -w ~/workspace
  ```

## Run the application on a target

The command runs the Tizen application on a specified target or serial device:

**Syntax:**

```
tz run [options]
```

**Options:**

| Option                           | Description                              |
|----------------------------------|------------------------------------------|
| `-w`, `--ws-dir`       | Specifies the workspace directory. |
| `-t`, `--target <target name>`   | Specifies the target name to run the package. |
| `-s`, `--serial <target serial>` | Specifies the serial to run the package. |
| `-d`, `--debug-mode` | Run web app in debug mode in web inspector. |
| `-r`, `--simulator` | Run web app in web simulator. |
| `-p`, `--project=STRING` | Specifies the project to execute. |

**Examples:**

- Run the application present in the specified workspace on the emulator-26101.

  Windows&reg;:
  ```
  > tz run -s emulator-26101 -w C:\Users\workspace
  ```

  Ubuntu and macOS:
  ```
  $ tz run -s emulator-26101 -w ~/workspace
  ```

- Run the web application in web simulator.

  Windows&reg;:
  ```
  > tz run -r -w C:\Users\workspace
  ```

  Ubuntu and macOS:
  ```
  $ tz run -r -w ~/workspace
  ```

- Run the web application in debug mode using web inspector.

  Windows&reg;:
  ```
  > tz run -d -s emulator-26101 -w C:\Users\workspace
  ```

  Ubuntu and macOS:
  ```
  $ tz run -d -s emulator-26101 -w ~/workspace
  ```

## Uninstall the application on a target

The command uninstalls the Tizen application on a specified target or serial device:

**Syntax:**

```
tz uninstall [options]
```

**Options:**

| Option                           | Description                              |
|----------------------------------|------------------------------------------|
| `-w`, `--ws-dir`       | Specifies the workspace directory. |
| `-t`, `--target <target name>`   | Specifies the target name to uninstall the package. |
| `-s`, `--serial <target serial>` | Specifies the serial to uninstall the package. |

**Examples:**

- Uninstall the application based on the specified working directory.

  Windows&reg;:
  ```
  > tz uninstall -s emulator-26101 -w C:\Users\workspace
  ```

  Ubuntu, and macOS:
  ```
  > tz uninstall -s emulator-26101 -w ~/workspace
  ```

## Details on creating, packaging and installing resource project

A resource project can contain resource files that can be used by a native application in a workspace.
Resource project can be created in the normal workspace, after initializing the workspace with `tz init` as mentioned in the section [Initialize the Workspace](#initialize-the-workspace).

**Example:**

Resource project can be created from the template the `-T project_type` argument in `tz new` as mentioned in the section [Create a Tizen Project](#create-a-tizen-project).

**Examples:**

Windows&reg;:
```
tz new -T rpk -t rpk_app -p basicrpk -w C:\Users\workspace
```

Ubuntu and macOS:
```
tz new -T rpk -t rpk_app -p basicrpk -w ~/workspace
```

To package and install rpk on the target, use the following commands:

**Examples:**

- Set resource project as working folder.

  Windows&reg;:
  ```
  > tz set -W basicrpk -w C:\Users\workspace
  ```

  Ubuntu and macOS:
  ```
  $ tz set -W basicrpk -w ~/workspace
  ```

- Package the project into rpk

  Windows&reg;:
  ```
  > tz pack -w C:\Users\workspace
  ```

  Ubuntu and macOS:
  ```
  $ tz pack -w ~/workspace
  ```

- Install the rpk on the target

  Windows&reg;:
  ```
  > tz install -w C:\Users\workspace
  ```

  Ubuntu and macOS:
  ```
  $ tz install -w ~/workspace
  ```

## Import project to Tizen-Core format

The projects created in Tizen-Studio, Visual Studio, and other IDEs need to be converted to Tizen-Core format, before building and running the projects in Tizen-Core. 
Init command in Tizen-Core is used to convert and create the required files to build the project in Tizen-Core as Import functionality is accomplished internally through the
Init command.

**Syntax:**

```
tz init [options]
```

**Options:**

| Option                           | Description                              |
|----------------------------------|------------------------------------------|
| `-p`, `--profile=STRING`     | Build profile of the project. |
| `-u`, `--update-sln`   | Add imported project entries in sln present in workspace. |
| `-f`, `--force` | Ignore existing project YAML files. |
| `-w`, `--ws-dir` | Specifies the workspace directory. |
| `-W`, `--wgt-path=STRING` | Path of wgt to be imported as web project. |

**Examples:**

- Create a project in Tizen Studio, right click on the project and select Export to CLI option in the menu, then run the following command in the terminal to convert the projects to Tizen-Core format:

  Windows&reg;:
  ```
  > tz init -w C:\Users\workspace
  ```

  Ubuntu and macOS:
  ```
  $ tz init -w ~/workspace
  ```

- Import web wgt project to Tizen-Core format.
  
  Windows&reg;:
  ```
  > tz init -W C:\Users\basicweb.wgt -w C:\Users\workspace
  ```

  Ubuntu and macOS:
  ```
  $ tz init -W ~/basicweb.wgt -w ~/workspace
  ```

## Display the command help

The command displays the CLI command help:

**Syntax:**

```
tz <command> --help
```

You can use all CLI commands to as `<command>`:

```
init, import, templates, new, add, add-deps, clean, build, pack, install, run, uninstall, cert,  security-profiles, emul, list, get, set, samples, trust-anchor, tidl-build, js-analyze.
```

**Examples:**

- Display the help for project create command:

  Windows&reg;, Ubuntu, and macOS:

  ```
  > tz new --help
  Usage: tz new

  Create new project

  Flags:
      --help               Show context-sensitive help.
      --version            Print version information and quit

  -w, --ws-dir=STRING      Workspace directory
  -p, --path=STRING        Project path
  -t, --template=STRING    Project template
  -T, --type=STRING        Project type
  -s, --sample=STRING      Sample project information,
                           "<category_name,application_name>"
  ```

## Related information
* Dependencies  
  - Tizen Studio 4.5 and Higher