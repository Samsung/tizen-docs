# Command Line Interface Commands

The Command Line Interface (CLI) provides functionalities for developing Tizen applications without the Tizen Studio. It includes the entire development process from creating the project to running the application.

The CLI is located in the `$<TIZEN_STUDIO>/tools/ide/bin/` directory. For developing an application using the CLI, add the CLI directory path to the `$PATH` environment variable using the following command:

```
export PATH=$PATH:$<TIZEN_STUDIO>/tools/ide/bin/
```

## Setting Configuration Options

The command displays, sets, replaces, and removes CLI configuration options. The CLI configuration keys are:

- `default.build.architecture=<x86|arm>`: Sets the default executable architecture type.
- `default.build.compiler=<llvm|gcc>`: Sets the default compiler.
- `default.build.configuration=<Debug|Release>`: Sets the default build configuration.
- `default.profiles.path=<profiles.xml file path>`: Sets the default path of security profile file.
- `default.sdb.timeout=<timeout value>`: Sets the default connection timeout value. The default is 60000 milliseconds.

**Syntax:**

```
tizen cli-config [options]
```

**Options:**

| Option                 | Description                              |
|------------------------|------------------------------------------|
| `-g`, `--global`       | Specifies whether the operation must be done for a global scope (for all installed SDKs or for the current Tizen Studio only). |
| `<key>=<value>`        | Sets a value for the CLI configuration key. |
| `-l`, `--list`         | Displays the list of all CLI configuration keys and values. |
| `-d`, `--delete <key>` | Removes the CLI configuration key and value. |

**Examples:**

- Display a list of all configurations for which values are set.

  Windows&reg;, Ubuntu, and macOS:

  ```
  > tizen cli-config -l
  default.build.architecture=x86
  default.build.compiler=llvm
  default.build.configuration=Debug
  default.sdb.timeout=60000
  ```

- Set a `profiles.xml` path globally.

  Windows&reg;:
  ```
  > tizen cli-config -g "default.profiles.path=C:\Users\workspace\.metadata\.plugins\org.tizen.common.sign\profiles.xml"
  ```
  Ubuntu and macOS:
  ```
  $ tizen cli-config -g default.profiles.path=~/workspace/.metadata/.plugins/org.tizen.common.sign/profiles.xml
  ```

## Displaying Profile Templates

The command displays a list of project templates or rootstraps suitable to a given option.

**Syntax:**

```
tizen list <option>
```

**Options:**

| Option           | Description                              |
|----------------|----------------------------------------|
| `native-project` | Displays the list of project templates for Tizen native applications. |
| `web-project`    | Displays the list of project templates for Tizen Web applications. |
| `rootstrap`      | Displays the list of available rootstraps. The rootstrap is a set of build configurations, which consists of the profile, platform version, and target architecture. |

**Examples:**

- List all native application templates.

  Windows&reg;, Ubuntu, and macOS:

  ```
  > tizen list native-project

  [PROFILE]		[TEMPLATE]
  mobile-2.3		service_app
  mobile-2.3		basic_edc_ui
  mobile-2.3		shared_library
  wearable-2.3		service_app
  wearable-2.3		basic_edc_ui
  wearable-2.3		shared_library
  ```

- List rootstraps.

  Windows&reg;, Ubuntu, and macOS:

  ```
  > tizen list rootstrap
  [ROOTSTRAP] 			[INFORMATION]
  mobile-2.3-device.core		Mobile 2.3, armel
  mobile-2.3-emulator.core	Mobile 2.3, i386
  mobile-2.4-device.core		Mobile 2.4, armel
  mobile-2.4-emulator.core	Mobile 2.4, i386
  wearable-3.0-device.core	Wearable 3.0, armel

  > tizen list rootstrap wearable-3.0-device.core
  rootstrap : wearable-3.0-device.core
  [FRAMEWORK NAME]        [TYPE]      [DESCRIPTION]
  Native_API              base        Native_API Libraries
  bixby                   add-on
  ```

## Creating a Tizen Project

The command creates a Tizen native or Web project from a template.

**Syntax:**
```
tizen create <sub-command> [options]
```

**Sub-commands:**

| Sub-command                              | Description                              |
|------------------------------------------|------------------------------------------|
| `native-project [options]` or `web-project [options]` | Create the Tizen native or Web project.Options are:`-p`, `--profile`: Specifies the profile name.`-t`, `--template`: Specifies the template name.`-n`, `--name`: Specifies the project name.`--`: Specifies the destination directory where the project is created. |

**Examples:**

- Create a template project based on the basic Tizen mobile UI project.

  Windows&reg;:

  ```
  > tizen create native-project -p mobile-2.4 -t basic-ui -n basic -- C:\Users\workspace
  > cd C:\Users\workspace\basic
  ```

  Ubuntu and macOS:

  ```
  $ tizen create native-project -p mobile-2.3 -t basic_ui -n basic -- ~/workspace
  $ cd ~/workspace/basic
  ```

## Building the Project

The command builds the Tizen native or Web project. To build the native project, 3 options are needed: architecture, compiler, and configuration. If you do not set these options, the default values are used. You can check or set the default build options with the `cli-config`command.

**Syntax:**

```
tizen <sub-command> [options]
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
			<td><code>build-native [options]</code></td>
			<td>Build the Tizen native project.<br>
			<br>
			Options are:
			<ul>
				<li><code>-a</code>, <code>--arch</code>: Specifies the architecture type: <code>x86</code> (default) or <code>arm</code></li>
				<li><code>-c</code>, <code>--compiler</code>: Specifies the compiler to build: <code>llvm</code> (default) or <code>gcc</code></li>
				<li><code>-C</code>, <code>--configuration</code>: Specifies the build configuration: <code>Debug</code> (default) or <code>Release</code></li>
				<li><code>-j</code>, <code>--jobs</code>: Specifies the number of parallel builds for the native project.</li>
				<li><code>-r</code>, <code>--rootstrap</code>: Specifies the rootstrap name. The rootstrap contains information on the profile name, platform version, and the target architecture type.</li>
				<li><code>-f</code>, <code>--framework</code>: Specifies the add-on framework name. If you installed an add-on framework, you can use this option to add the additional build environments (headers and libraries for add-on framework API).</li>
				<li><code>--</code>: Specifies the project directory.</li>
			</ul>
			</td>
		</tr>
		<tr>
			<td><code>build-web [options]</code></td>
			<td>Build the Tizen Web project.<br>
			<br>
			Options are:
			<ul>
				<li><code>-e</code>, <code>--exclude</code>: Specifies a list of exclude files by patterns. By default, the following resources are excluded: <code>.build/*</code>, <code>.build</code>, <code>.sign/*</code>, <code>.sign</code>, <code>webUnitTest/*</code>, <code>webUnitTest</code>, <code>.externalToolBuilders/*</code>, <code>.externalToolBuilders</code>, <code>.buildResult/*</code>, <code>.buildResult</code>, <code>.settings/*</code>, <code>.settings</code>, <code>.package/*</code>, <code>.package</code>, <code>.tproject</code>, <code>.project</code>, <code>.sdk_delta.info</code>, <code>.rds_delta</code>, <code>*.wgt</code>, <code>.tizen-ui-builder-tool.xml</code></li>
				<li><code>-euf</code>, <code>--exclude-uifw</code>: Specifies whether to exclude the Tizen Web UI framework, and use the Tizen UI framework in the target. This option is only used for applications using the Tizen UI framework.</li>
				<li><code>-out</code>, <code>--output</code>: Sets the output directory name. If you omit this option, the <code>.buildResult</code> directory is created under the project directory by default.</li>
				<li><code>-opt</code>, <code>--optimize</code>: Optimizes the application size. The JavaScript and CSS files are minimized and the Tizen Web UI framework source is excluded. The related link address is modified to a platform-dependent location instead.</li>
				<li><code>--</code>: Specifies the project directory.</li>
			</ul>
			</td>
		</tr>
	</tbody>
</table>


**Examples:**

- Build the native project with the `x86`, `llvm`, and `Debug` options.

  Windows&reg;:
  ```
  > tizen build-native -a x86 -c llvm -C Debug -- C:\Users\workspace\basic> dir C:\Users\workspace\basic\Debug
  ```

  Ubuntu and macOS:
  ```
  $ tizen build-native -a x86 -c llvm -C Debug -- ~/workspace/basic$ ls ~/workspace/basic/Debug
  ```

- Build the native project with a rootstrap.

  Windows&reg;:

  ```
  > tizen build-native -r mobile-2.4-device.core -C Release -- C:\Users\workspace\basic
  > dir C:\Users\workspace\basic\Release
  ```

  Ubuntu and macOS:

  ```
  $ tizen build-native -r mobile-2.4-device.core -C Release -- ~/workspace/basic
  $ ls ~/workspace/basic/Release
  ```

- Build the Web project with default options.

  Windows&reg;:

  ```
  > tizen build-web -- C:\Users\workspace\basicWeb
  > dir C:\Users\workspace\basicWeb\.buildResult
  ```

  Ubuntu and macOS:

  ```
  $ tizen build-web -- ~/workspace/basicWeb
  $ ls ~/workspace/basicWeb/.buildResult
  ```

## Cleaning the Project

The command cleans the Tizen project. If you clean the project, all build output directories under the project root path are removed (`Debug`, `Release`, and `.buildResult`).

**Syntax:**

```
tizen clean [-- <project directory>]
```

**Options:**

| Option                   | Description                              |
|--------------------------|------------------------------------------|
| `-- <project directory>` | Specifies the project directory to clean. |

**Examples:**

- Clean the project.

  Windows&reg;:

  ```
  > tizen clean -- C:\Users\workspace\basic
  ```

  Ubuntu and macOS:

  ```
  $ tizen clean -- ~/workspace/basic
  ```

## Issuing a Tizen Certificate

The command generates a Tizen certificate for your application. If you want to upload your application to the Tizen Store or install the application to a Tizen device, you must generate a Tizen certificate.

**Syntax:**
```
tizen certificate [options]
```

**Options:**

| Option                                | Description                              |
|---------------------------------------|------------------------------------------|
| `-a`, `--alias <alias name>`          | Specifies an alias name of the certificate. |
| `-p`, `--password <password>`         | Specifies the password of the certificate. |
| `-c`, `--country <country code>`      | Specifies the user's country code, which consists of 2 letters. |
| `-s`, `--state <state>`               | Specifies the user's state.              |
| `-ct`, `--city <city>`                | Specifies the user's city.               |
| `-o`, `--organization <organization>` | Specifies the user organization.         |
| `-u`, `--unit <unit>`                 | Specifies the user's organization unit.  |
| `-n`, `--name <name>`                 | Specifies the user name.                 |
| `-e`, `--email <email>`               | Specifies the user email.                |
| `-f`, `--filename <filename>`         | Specifies the file name without a file extension. A certificate file is created with the file name.<br> If you skip this option, the default file name, `author`, is used on creating the certificate file. |
| `-- <certificate output path>`        | Specifies the output directory path to create the certificate.<br> If you skip this option, the default output directory path, `<TIZEN_STUDIO_DATA>/keystore/author/`, is used on saving the certificate file. |

**Examples:**

- Generate a certificate.

  Windows&reg;:

  ```
  > tizen certificate -a MyTizen -p 1234 -c KR -s Seoul -ct Gangnamgu -o Tizen –u Development -n "Gildong Hong" -e gildonghong@example.org -f mycert
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
  'mycert' has been generated in 'C:\tizen-sdk-data\keystore\author'.
  ```

  Ubuntu and macOS:

  ```
  $ tizen certificate -a MyTizen -p 1234 -c KR -s Seoul -ct Gangnamgu -o Tizen –u
  Development -n "Gildong Hong" -e gildonghong@example.org -f mycert
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
  'mycert' has been generated in '~/tizen-sdk-data/keystore/author'.
  ```

## Managing a Security Profile

The command manages the security profiles, which are a set of signing certificates for a Tizen application.

**Syntax:**

```
tizen security-profiles <sub-command> [options]
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
				<li><code>-n</code>, <code>--name</code>: Specifies the name of the security profile to add.</li>
				<li><code>-a</code>, <code>--path</code>: Specifies the directory path where the author certificate file is located. The format of the certificate is PKCS#12, and the file extension is <code>.p12</code>.</li>
				<li><code>-p</code>, <code>--password</code>: Specifies the password used to access the author certificate.</li>
				<li><code>-c</code>, <code>--ca</code>: Specifies the directory path where the author CA certificate file is located. The file extension of the CA certificate is <code>.cer</code>.</li>
				<li><code>-r</code>, <code>--rootca</code>: Specifies the directory path where the author root CA certificate file is located. The file extension of the root CA certificate is <code>.cer</code>.</li>
				<li><code>-d</code>, <code>--dist</code>: Specifies the directory path where the distributor certificate file is located. If you skip this option, the default distributor certificate file embedded in the Tizen Studio is used.</li>
				<li><code>-dp</code>, <code>--dist-password</code>: Specifies the password of the distributor certificate.</li>
				<li><code>-dc</code>, <code>--dist-ca</code>: Specifies the directory path where the distributor CA certificate file is located.</li>
				<li><code>-dr</code>, <code>--dist-rootca</code>: Specifies the directory path where the distributor root CA certificate file is located.</li>
				<li><code>--</code>: Specifies the directory path where the <code>profiles.xml</code> file is located. If you skip this option, the value of the <code>default.profiles.path</code> key in the CLI configuration is used to find the <code>profiles.xml</code> file, which consists of new security profiles that are generated in the <code>&lt;TIZEN_STUDIO_DATA&gt;/keystore/</code> directory. The directory path is added to the CLI configuration.</li>
			</ul>
			</td>
		</tr>
		<tr>
			<td><code>list [options]</code></td>
			<td>Displays security profiles. If you specify the name of the security profile, details about the specified profile are displayed.<br />
			<br />
			Options are:
			<ul>
				<li><code>-n</code>, <code>--name</code>: Specifies the name of the security profile to list. If you skip this option, a set of the security profile names in the <code>profiles.xml</code> file is displayed.</li>
				<li><code>--</code>: Specifies the directory path where the <code>profiles.xml</code> file is located.</li>
			</ul>
			</td>
		</tr>
		<tr>
			<td><code>remove [options]</code></td>
			<td>Removes the specified security profile.<br />
			<br />
			Options are:
			<ul>
				<li><code>-n</code>, <code>--name</code>: Specifies the name of the security profile to remove.</li>
				<li><code>--</code>: Specifies the directory path where the <code>profiles.xml</code> file is located.</li>
			</ul>
			</td>
		</tr>
	</tbody>
</table>

**Examples:**

- Add a new security profile.

  Windows&reg;:

  ```
  > tizen security-profiles add -n MyProfile -a C:\tizen-sdk- data\keystore\author\mycert.p12 -p 1234
  No exist the default path of security profiles.
  author path: C:\tizen-sdk-data\keystore\author\mycert.p12
  author password: ****
  distributor1 path: C:\tizen-sdk\tools\certificate-generator\certificates\distributor\tizen-distributor-signer.p12
  distributor1 password: *************************
  distributor1 CA path: C:\tizen-sdk\tools\certificate-generator\certificates\distributor\tizen-distributor-ca.cer

  In Configuration, Set a default profile path to 'C:\tizen-sdk-data\ide\keystore\profiles.xml'.
  Wrote to 'C:\tizen-sdk-data\ide\keystore\profiles.xml'.
  Succeed to add 'MyProfile' profile.
  If want to sign by this, add the file of security profiles in CLI configuration like 'tizen cli-config "default.profiles.path=C:\tizen-sdk-data\ide\keystore\profiles.xml"'.
  ```

  Ubuntu and macOS:

  ```
  $ tizen security-profiles add -n MyProfile -a ~/tizen-sdk-data/keystore/author/mycert.p12 -p 1234
  No exist the default path of security profiles.
  author path: ~/tizen-sdk-data/keystore/author/mycert.p12
  author password: ****
  distributor1 path: ~/tizen-sdk/tools/certificate-generator/certificates/distributor/tizen-distributor-signer.p12
  distributor1 password: *************************
  distributor1 CA path: ~/tizen-sdk/tools/certificate-generator/certificates/distributor/tizen-distributor-ca.cer

  In Configuration, Set a default profile path to '~/tizen-sdk-data/ide/keystore/profiles.xml'.
  Wrote to '~/tizen-sdk-data/ide/keystore/profiles.xml'.
  Succeed to add 'MyProfile' profile.
  If want to sign by this, add the file of security profiles in CLI configuration like 'tizen cli-config "default.profiles.path=~/tizen-sdk-data/ide/keystore/profiles.xml"'.
  ```

- Display the security profile list.

  Windows&reg;:

  ```
  > tizen security-profiles list
  Loaded in 'C:\tizen-sdk-data\ide\keystore\profiles.xml'.
  ========================================
  Name
  ========================================
  MyProfile
  ```

  Ubuntu and macOS:

  ```
  $ tizen security-profiles list
  Loaded in '~/tizen-sdk-data/ide/keystore/profiles.xml'.
  ========================================
  Name
  ========================================
  MyProfile
  ```

- Display the details for a security profile.

  Windows&reg;:

  ```
  > tizen security-profiles list –n MyProfile
  Loaded in 'C:\tizen-sdk-data\ide\keystore\profiles.xml'.
  ========================================
  'MyProfile' profile information
  ========================================
  author path: C:\tizen-sdk-data\keystore\author\mycert.p12
  author password: ****
  distributor1 path: C:\tizen-sdk\tools\certificate-generator\certificates\distributor\tizen-distributor-signer.p12
  distributor1 password: *************************
  distributor1 CA path: C:\tizen-sdk\tools\certificate-generator\certificates\distributor\tizen-distributor-ca.cer
  ```

  Ubuntu and macOS:

  ```
  $ tizen security-profiles list –n MyProfile
  Loaded in '~/tizen-sdk-data/ide/keystore/profiles.xml'.
  ========================================
  'MyProfile' profile information
  ========================================
  author path: ~/tizen-sdk-data/keystore/author/mycert.p12
  author password: ****
  distributor1 path: ~/tizen-sdk/tools/certificate-generator/certificates/distributor/tizen-distributor-signer.p12
  distributor1 password: *************************
  distributor1 CA path: ~/tizen-sdk/tools/certificate-generator/certificates/distributor/tizen-distributor-ca.cer
  ```

- Remove the security profile.

  Windows&reg;:

  ```
  > tizen security-profiles remove
  Loaded in 'C:\tizen-sdk-data\ide\keystore\profiles.xml'.
  Wrote to 'C:\tizen-sdk-data\ide\keystore\profiles.xml'.
  Succeed to remove 'MyProfile' profile
  ```

  Ubuntu and macOS:

  ```
  $ tizen security-profiles remove
  Loaded in '~/tizen-sdk-data/ide/keystore/profiles.xml'.
  Wrote to '~/tizen-sdk-data/ide/keystore/profiles.xml'.
  Succeed to remove 'MyProfile' profile
  ```

## Using Your Own Certificates

The command is used to assign your own SSL root certificates for HTTPS communication.

**Syntax:**
```
tizen trust-anchor <sub-command> [options]
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
				<li><code>-c</code>, <code>--user-certificate-path &lt;certificate path&gt;</code>: Specifies the file path for the user certificate to be set. If you want to set multiple certificates, separate them with a comma.</li>
				<li><code>-s</code>, <code>--use-system-certs {true|false}</code>: Determines whether to use the system root certificates.</li>
				<li><code>-- &lt;project path&gt;</code>: Specifies the project directory to set the new certificate for.</li>
			</ul>
			</td>
		</tr>
		<tr>
			<td><code>info</code></td>
			<td>Displays the trust anchor configuration for a project.<br />
			<br />
			Options are:
			<ul>
				<li><code>-- &lt;project path&gt;</code>: Specifies the project directory to show the trust-anchor configuration of.</li>
			</ul>
			</td>
		</tr>
		<tr>
			<td><code>delete [options]</code></td>
			<td>Deletes the specified user certificate.<br />
			<br />
			Options are:
			<ul>
				<li><code>-c</code>, <code>--user-certificate-path &lt;certificate name&gt;</code>: Specifies the user certificate file name to be deleted. If you want to delete multiple certificates, separate them with a comma.</li>
				<li><code>-- &lt;project path&gt;</code>: Specifies the project directory to delete the certificate from.</li>
			</ul>
			</td>
		</tr>
		<tr>
			<td><code>unset</code></td>
			<td>Disables the trust anchor.<br />
			<br />
			Options are:
			<ul>
				<li><code>-- &lt;project path&gt;</code>: Specifies the project directory to disable the trust anchor for.</li>
			</ul>
			</td>
		</tr>
	</tbody>
</table>


Examples:

- Set a new user certificate, check the trust anchor configuration, set additional certificates, delete certificates, and unset the trust anchor.

  Windows&reg;:
  ```
   > tizen trust-anchor info -- project1
   Trust-Anchor is disabled for the project project1.
   
   > tizen trust-anchor set -c C:\workspace\user1.pem -s true -- project1
   Succeed to set the trust-anchor.
   
   > tizen trust-anchor info -- project1
   use-system-certs: true
   user certificates: user1.pem
   
   > tizen trust-anchor set -c "C:\workspace\user2.pem,C:\workspace\user3.pem,C:\workspace\certdirs" -- project1
   Succeed to add the certificates user2.pem, user3.pem.
   
   > tizen trust-anchor info -- project1
   use-system-certs: true
   user certificates: user1.pem, user2.pem, user3.pem, certdirs1.pem, certdirs2.pem
   
   > tizen trust-anchor delete -c "user2.pem,certdirs1.pem" -- project1
   Succeed to delete the certificates user2.pem, certdirs1.pem.
   
   > tizen trust-anchor unset -- project1
   Succeed to disable the trust-anchor.
   
   > tizen trust-anchor info -- project1
   Trust-Anchor is disabled for this project.
   ```

## Packaging a Tizen Application with Signing

The command packages the Tizen application with signing. If there is a package file in the options, the package is re-signed. The Tizen application is signed with a certified profile in the `profiles.xml` file. You can create the default profile from the Tizen Studio, which generates the file in a hidden directory in your workspace (`<Your workspace directory>/.metadata/.plugins/org.tizen.common.sign/profiles.xml`). Set the path of the `profiles.xml` file before packaging the Tizen application (by using the tizen `cli-config` command).

**Syntax:**

```
tizen package [options]
```

**Options:**

| Option                            | Description                              |
|-----------------------------------|------------------------------------------|
| `-t`, `--type {tpk|wgt}`          | Specifies the package type. You can use `tpk` for a Tizen native package or `wgt` for a Tizen Web package. |
| `-s`, `--sign <security profile>` | Specifies the security profile name to use for signing. |
| `-S`, `--strip {on|off}`          | Determines whether to strip the native binary. The default value is off. This option only works when the native binary is based on the `arm` architecture and `Release` build configuration. This option is only for the native package. |
| `-- <build output path>`          | Specifies the build output path. If this is a package file, the package is re-signed. |

**Examples:**

- Package the project.

  Windows&reg;:

  ```
  > tizen package -t tpk -s MyProfile -- C:\Users\workspace\basic\Debug
  Initialize... OK
  Copying files... OK
  Signing... OK
  Zip path: C:\Users\workspace\basic\Debug\org.tizen.basic-1.0.0-i386.tpk
      adding: bin/  (in=0) (out=0) (stored 0%)
      adding: bin/basic       (in=11422) (out=4939) (deflated 57%)
      adding: tizen-manifest.xml    (in=428) (out=247) (deflated 42%)
      adding: lib/  (in=0) (out=0) (stored 0%)
      adding: signature1.xml        (in=4254) (out=1971) (deflated 54%)
      adding: shared/       (in=0) (out=0) (stored 0%)
      adding: shared/data/  (in=0) (out=0) (stored 0%)
      adding: shared/trusted/       (in=0) (out=0) (stored 0%)
      adding: shared/res/   (in=0) (out=0) (stored 0%)
      adding: shared/res/basic.png    (in=57662) (out=18633) (deflated 68%)
      adding: author-signature.xml  (in=4132) (out=2174) (deflated 47%)
      adding: res/  (in=0) (out=0) (stored 0%)
  total bytes=77898, compressed=27964 -> 64% savings
  Zipping... OK
  Package File Location: C:\Users\workspace\basic\Debug\org.tizen.basic-1.0.0-i386.tpk
  ```

  Ubuntu and macOS:

  ```
  $ tizen package -t tpk -s MyProfile -- ~/workspace/basic/Debug
  Initialize... OK
  Copying files... OK
  Signing... OK
  Zip path: ~/workspace/basic/Debug/org.tizen.basic-1.0.0-i386.tpk
      adding: bin/  (in=0) (out=0) (stored 0%)
      adding: bin/basic       (in=11422) (out=4939) (deflated 57%)
      adding: tizen-manifest.xml    (in=428) (out=247) (deflated 42%)
      adding: lib/  (in=0) (out=0) (stored 0%)
      adding: signature1.xml        (in=4254) (out=1971) (deflated 54%)
      adding: shared/       (in=0) (out=0) (stored 0%)
      adding: shared/data/  (in=0) (out=0) (stored 0%)
      adding: shared/trusted/       (in=0) (out=0) (stored 0%)
      adding: shared/res/   (in=0) (out=0) (stored 0%)
      adding: shared/res/basic.png    (in=57662) (out=18633) (deflated 68%)
      adding: author-signature.xml  (in=4132) (out=2174) (deflated 47%)
      adding: res/  (in=0) (out=0) (stored 0%)
  total bytes=77898, compressed=27964 -> 64% savings
  Zipping... OK
  Package File Location: ~/workspace/basic/Debug/org.tizen.basic-1.0.0-i386.tpk
  ```


- Re-sign the package.

  Windows&reg;:

  ```
  > tizen package -t tpk -s MyProfile -- C:\Users\workspace\basic\Debug\org.tizen.basic-1.0.0-i386.tpk
  Author certificate: C:\tizen-sdk-data\keystore\author\mycert.p12
  Distributor1 certificate : C:\tizen-sdk\tools\certificate-generator\certificates\distributor\tizen-distributor-signer.p12
  Package (C:\Users\workspace\basic\Debug\org.tizen.basic-1.0.0-i386.tpk) is created successfully.
  ```

  Ubuntu and macOS:

  ```
  $ tizen package -t tpk -s MyProfile -- ~/workspace/basic/Debug/org.tizen.basic-1.0.0-i386.tpk
  Author certificate: ~/tizen-sdk-data/keystore/author/mycert.p12
  Distributor1 certificate : ~/tizen-sdk/tools/certificate-generator/certificates/distributor/tizen-distributor-signer.p12
  Package (~/workspace/basic/Debug/org.tizen.basic-1.0.0-i386.tpk) is created successfully.
  ```

## Building and Packaging Multiple Projects

This command builds and packages multiple Tizen projects at once with various options. By specifying the arguments with a JSON-like format, you can specify the building and packaging process in detail.

**Syntax:**

```
tizen build-app [options] [args specified with JSON-like format]
```

**Options:**

| Option                                  | Description                              |
|---------------------------------------|----------------------------------------|
| `-b`, `--build <args>`                  | Specifies the build description.         |
| `-d`, `--define <macro info>`           | Specifies the macro.                     |
| `-h`, `--help`                          | Displays detailed explanation for a given command. |
| `-m`, `--method <method description>`   | Specifies the build method to use.       |
| `-o`, `--output <path>[...]`            | Specifies the output file paths.         |
| `-p`, `--package <package description>` | Specifies the package description.       |
| `-f`, `--script-file <file path>`       | Specifies the path of the ABS script file. |
| `-s`, `--sign <profile name>`           | Specifies the profile name.              |
| `-t`, `--target <project>[...]`         | Specifies the targets for building and packaging. |
| `--`                                    | Specifies the base directory for the command. |

**Arguments:**

<table>
	<thead>
		<tr>
			<th>Type</th>
			<th>JSON-like expression</th>
		</tr>
	</tead>
	<tbody>
		<tr>
			<td><code>build</code></td>
			<td>
			<pre><code>
build: [
    {
        name: &lt;build alias&gt;,
        targets: [&lt;project directories in workspace separated by commas&gt;],
        methods: [&lt;build methods separated by commas&gt;],
        output: &lt;build output path&gt;,
        multitask: &lt;cout of processes&gt;
    }
]
			</code></pre>
			</td>
		</tr>
		<tr>
			<td><code>method</code></td>
			<td>
			<pre><code>
method: [
    {
        name: &lt;method name&gt;,
        compiler: &lt;compiler name, such as GCC, LLVM&gt;,
        rootstraps: [
            {name: &lt;ID of a dependent project&gt;, platform: &lt;platform name&gt;, arch: &lt;architecture&gt;}
        ],
        predefines: [&lt;predefined build macros separated by commas&gt;],
        configs: [&lt;build config&gt;]
    }
]
			</code></pre>
			</td>
		</tr>
		<tr>
			<td><code>package</code></td>
			<td>
			<pre><code>
package: [
    {
        name: &lt;package name&gt;,
        type: &lt;package type, such as .tpk, .wgt&gt;,
        targets: [&lt; build file or project directories in workspace separated by commas&gt;],
        output: &lt;package file path&gt;
    }
]
			</code></pre>
			</td>
		</tr>
	</tbody>
</table>


**Examples:**

- Package the Web multi application.

  Windows&reg;, Ubuntu, and macOS:

  ```
  > tizen build-app -p "name:webp1,targets:[webbasic,webwidget]"
  ```


- Package the native multi package with the debug and release build configurations.

  Windows&reg;, Ubuntu, and macOS:

  ```
  > tizen build-app -m "name:m1,configs:[Debug,Release]" -b "name:b1,targets:[basic,service],methods:[m1]" -p "name:nativep1,targets:[b1]" -s MyProfile

  ```

## Installing the Application on a Target

The command installs a Tizen application on a target.

**Syntax:**

```
tizen install [options]
```

**Options:**

| Option                             | Description                              |
|------------------------------------|------------------------------------------|
| `-n`, `--name <package file name>` | Specifies the Tizen package file name.   |
| `-t`, `--target <target name>`     | Specifies the target name to install the package. |
| `-s`, `--serial <target serial>`   | Specifies the serial to install the package. |
| `-- <package file path>`           | Specifies the directory path of the package file. |

**Examples:**

- Install the basic application, whose package name is `org.tizen.basic-1.0.0-i386.tpk`, on the emulator-26101.

  Windows&reg;:
  ```
  > tizen install -n org.tizen.basic-1.0.0-i386.tpk -s emulator-26101 -- C:\Users\workspace\basic\Debug
  ```

  Ubuntu and macOS:
  ```
  $ tizen install -n org.tizen.basic-1.0.0-i386.tpk -s emulator-26101 -- ~/workspace/basic/Debug
  ```

## Running the Application on a Target

The command runs the Tizen application on a target.

**Syntax:**

```
tizen run [options]
```

**Options:**

| Option                           | Description                              |
|----------------------------------|------------------------------------------|
| `-p`, `--pkgid <package id>`     | Specifies the Tizen package ID installed on the target. |
| `-t`, `--target <target name>`   | Specifies the target name to run the package. |
| `-s`, `--serial <target serial>` | Specifies the serial to run the package. |

**Examples:**

- Run the basic application, whose package ID is `org.tizen.basic`, on the emulator-26101.

  Windows&reg;, Ubuntu, and macOS:
  ```
  > $ tizen run -p org.tizen.basic -s emulator-26101
  ```

## Uninstalling the Application on a Target

The command uninstalls the Tizen application on a target.

**Syntax:**

```
tizen uninstall [options]
```

**Options:**

| Option                           | Description                              |
|----------------------------------|------------------------------------------|
| `-p`, `--pkgid <package id>`     | Specifies the Tizen package ID installed on the target. |
| `-t`, `--target <target name>`   | Specifies the target name to uninstall the package. |
| `-s`, `--serial <target serial>` | Specifies the serial to uninstall the package. |

**Examples:**

- Uninstall the basic application, whose package ID is `org.tizen.basic`, from the emulator-26101.

  Windows&reg;, Ubuntu, and macOS:
  ```
  > tizen uninstall -p org.tizen.basic -s emulator-26101
  ```

## Displaying the Command Manual

The command displays the CLI command manual.

**Syntax:**

```
tizen manual [<command>]
```

You can use all CLI commands to as `<command>`:

```
cli-config, list, create, build-native, build-web, clean, certificate, security-profiles, package, install, run, uninstall, version
```

**Examples:**

- Display the manual for the create command.

  Windows&reg;, Ubuntu, and macOS:

  ```
  > tizen manual create
  -------------------------------------------
  tizen create
  -------------------------------------------
  Creates a Tizen native project.

  Syntax:
      tizen create native-project [options]

  Options:
      -p, --profile <profile name>
          Specifies the profile name.
      -t, --template <template name>
          Specifies the template name.
      -n, --name <project name>
          Specifies the project name.
      -- <destination directory>
          Specifies the destination directory where the project is created.

  Examples:
      Creates a template project based on the basic Tizen mobile UI project:
          Windows:
              > tizen.bat create native-project -p mobile-2.4 -t basic-ui -n basic --
                  C:\Users\workspace
                  > cd C:\Users\workspace\basic
          Ubuntu and macOS:
                  $ tizen create native-project -p mobile-2.4 -t basic-ui -n basic -- /ho
                  me/workspace
                  $ cd /home/workspace/basic
  ```

## Displaying the CLI Version

The command displays the CLI version number.

**Syntax:**

```
tizen version
```

**Examples:**

- Display the CLI version number.

  Windows&reg;, Ubuntu, and macOS:

  ```
  > tizen version
  Tizen CLI 1.3.5
  ```

## Related Information
* Dependencies  
  - Tizen Studio 1.0 and Higher
