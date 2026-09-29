# Tizen SDK Skills reference

Tizen SDK Skills provides 29 skills. Each skill is triggered by natural language in your AI coding assistant, and most skills also exist as an agent that can run as a separate task. The standalone `tizen-sdk` CLI exposes the same functionality as 35 commands. This page lists every skill grouped by task, with an example of how to ask for it.

All skills return a Standard JSON Envelope. If a step fails, the envelope includes an error code and, when possible, a suggested fix. See [How it works](index.md#how-it-works).

## SDK setup and packages

| Skill | What it does | Example request |
|-------|--------------|-----------------|
| `tizen-sdk-install` | Installs the Tizen SDK in two phases. A pre-check verifies Node.js, free disk space, and whether an SDK is already present. The install itself then runs as a background job. Also answers questions about the package repository. | "Install the Tizen SDK" |
| `tizen-sdk-install-custom-repo` | Installs the SDK from a package repository URL that you supply, such as a team mirror or a local HTTP server, instead of the public CDN. Validates the URL first. | "Install the SDK from http://mirror.example.com/tizen" |
| `tizen-sdk-init` | Registers an existing SDK installation by writing its path to `~/.tizen.sdk.path.config`. Checks that the path exists and is readable and writable. | "Set the Tizen SDK path to /opt/tizen-sdk" |
| `tizen-update-package` | Downloads the latest package list, compares it with the installed packages, and updates the outdated ones. | "Update the Tizen SDK packages" |
| `tizen-platform-install` | Installs a Tizen platform package (`TIZEN-<version>`), which is required for Native builds. | "Install the Tizen 10.0 platform" |
| `tizen-download-emulator-package` | Installs the emulator package (`TIZEN-<version>-Emulator`) so that emulator images can be created. | "Download the emulator package" |
| `tizen-download-mobile-platform` | Installs the Tizen Mobile platform package (`MOBILE-<version>`), optionally with the IoT Headed extension. | "Install the Mobile platform" |
| `tizen-tv-sdk-install` | Installs the Samsung TV SDK extension (TV-SAMSUNG-Public) on top of an existing SDK. | "Install the TV SDK" |
| `tizen-tv-sdk-install-from-zip` | Installs the TV SDK extension offline from a local ZIP file. | "Install the TV SDK from tv-sdk.zip" |
| `tizen-install-rootstrap` | Installs a custom rootstrap from a ZIP file, for example for a device or architecture that is not in the standard SDK. Rejects unsafe archives. | "Install this rootstrap ZIP" |
| `tizen-dotnet-setup` | Checks that the .NET SDK is installed and installs the Tizen .NET workload. Required before you create or build a .NET project. | "Set up the .NET environment for Tizen" |

Notes:

- The public CDN mirror is chosen automatically from your time zone. The mirrors are `download.tizen.org`, `usa.sdk-dl.tizen.org`, `brazil.sdk-dl.tizen.org`, and `singapore.sdk-dl.tizen.org`. The selected URL is recorded in `<sdk>/.package/repository.info`, and later package downloads reuse it.
- A custom repository URL must serve a `pkg_list_<OS>-64` or `pkg_list_<OS>-32` file. Otherwise the install is refused before anything is downloaded. Use `--force` to switch repositories when an SDK is already installed.
- The default SDK location is `~/tizen-sdk`. You can also set the `TIZEN_SDK_PATH` environment variable.

## Environment checks

| Skill | What it does | Example request |
|-------|--------------|-----------------|
| `tizen-check-node` | Reports whether Node.js is installed, its version, and its path. If it is missing, it returns the install command for your operating system. | "Is Node.js installed?" |
| `tizen-check-disk-space` | Reports the free space on your home drive and whether it meets the 15 GB threshold for an SDK install. | "Do I have enough disk space for the SDK?" |

## Projects

| Skill | What it does | Example request |
|-------|--------------|-----------------|
| `tizen-create-project` | Discovers the templates in your installed SDK and scaffolds a Native, .NET, Web, RPK resource, TV, or Platform project. Also lists templates, imports an existing `.wgt` archive as a Web project, and deletes a project directory after confirmation. | "Create a Tizen web app called HelloTizen" |
| `tizen-build-project` | Detects the project type and builds and packages it: `.tpk` for Native and .NET, `.wgt` for Web, `.rpk` for resource packages, and `.rpm` for Platform projects built with GBS. | "Build this project" |

Notes:

- Project files such as `tizen-manifest.xml` and `config.xml` are always generated from SDK templates. The guard rules stop the assistant from writing them by hand.
- Ask "Show me the app templates" to list the templates before you choose one. If you only say "templates", the assistant asks whether you mean app templates or emulator templates.
- Deleting a project runs on the SDK side and refuses any directory that does not contain a Tizen project marker.

## Emulators and devices

| Skill | What it does | Example request |
|-------|--------------|-----------------|
| `tizen-create-emulator` | Creates an emulator image with the screen size you choose (1080 by default), a platform, and a profile. Also lists platforms, emulator templates, and existing images, and deletes images. | "Create a 720p Tizen emulator" |
| `tizen-launch-emulator` | Boots an existing emulator image and waits until it is connected through `sdb`. If you give no name, it launches the first image in the list. | "Launch the emulator" |
| `tizen-device-manager` | Lists the devices and emulators connected through `sdb`, or shuts down running emulators. Supports both standard Tizen and Samsung TV emulator profiles. | "Show me the connected devices" |
| `tizen-remote-device` | Scans your local network for Tizen devices, connects or disconnects them over the network instead of USB, and manages the bookmarked remote device list. | "Connect to the TV at 192.168.0.20" |
| `tizen-install-app` | Installs a `.tpk`, `.wgt`, `.rpk`, or `.rpm` package on the connected device or emulator and optionally launches the app. | "Install the app and run it" |
| `tizen-file-transfer` | Pushes files and directories to the device or pulls them back to the host through `sdb`. | "Copy data.json to the device" |
| `tizen-sdb-helper` | Runs a single `sdb` action for you: open a shell, run a command, forward a port, reboot or shut down the device, launch or kill an app, list installed packages, or check disk usage. Destructive actions ask for confirmation. | "Forward port 8080 to the device" |
| `tizen-screenshot` | Captures the screen of a device, emulator, or TV and saves it as a PNG file. Tries several capture methods and stops at the first one that works. | "Take a screenshot of the emulator" |

Notes:

- Emulator templates are screen sizes and resolutions. App templates belong to `tizen-create-project`.
- An RPK package contains resources only and cannot be launched. An RPM package from a Platform build can be launched with its `/usr/bin` binary.
- Requests to view, save, or clear device logs are handled by `tizen-dlog-analyzer`, not by `tizen-sdb-helper`.

## Debugging and logs

| Skill | What it does | Example request |
|-------|--------------|-----------------|
| `tizen-gdb-debug` | Sets up remote GDB debugging for a Native app: checks the device, starts the app, finds its PID, starts `gdbserver`, forwards the port, and attaches the host GDB. | "Debug this native app with GDB" |
| `tizen-dotnet-debug` | Sets up remote debugging for a .NET app with netcoredbg: installs the debugger on the device on demand, starts the app, and gives you either an attach command or a Debug Adapter Protocol server for Visual Studio Code. Requires a Debug build. | "Debug this .NET app" |
| `tizen-webapp-debug` | Launches a Web app in debug mode, forwards the Remote Web Inspector port, verifies the CDP endpoint, and returns snippets for Chrome DevTools and Playwright. | "Debug this web app" |
| `tizen-dlog-analyzer` | Dumps, saves, or clears the device log buffer, collects logs for a specific app, monitors the device in the background, detects crashes and exceptions, and suggests root causes. | "The app crashed. Analyze the logs" |

Notes:

- Each debugging skill is bound to one app type. GDB works only for Native apps, netcoredbg only for .NET apps, and Remote Web Inspector only for Web apps. The skills refuse the wrong project type.
- Any report of a crash, freeze, or unexpected behavior is routed to `tizen-dlog-analyzer` first, even if you do not mention logs.

## Testing

| Skill | What it does | Example request |
|-------|--------------|-----------------|
| `tizen-playwright-test` | Scaffolds a Playwright test file for a Tizen Web app, or runs an existing test. It sets up debug mode and port forwarding through the Web app debug flow and then runs the test with Node.js in your test project. Web apps only. | "Run the Playwright tests against my web app" |

## Certificates

| Skill | What it does | Example request |
|-------|--------------|-----------------|
| `tizen-certificate-manager` | Generates local author certificates, lists the bundled distributor certificates, creates and activates signing profiles, imports and inspects certificates, and issues Samsung certificates for TV targets after a Samsung Account login. | "Create a signing profile called dev" |

Notes:

- Local certificates need no network and no account.
- Samsung certificates are for TV targets. They require a Samsung Account and the device unique ID (DUID) of a connected TV or TV emulator, which the skill can read for you.

## Standalone CLI command names

In the standalone `tizen-sdk` CLI, most skills map to a command with the same name without the `tizen-` prefix, for example `tizen-sdk build-project`. Six extra commands expose actions that belong to a larger skill:

| CLI command | Skill that owns it | Purpose |
|-------------|--------------------|---------|
| `sdk-repo-info` | `tizen-sdk-install` | Shows the package repository information. |
| `validate-repo-url` | `tizen-sdk-install-custom-repo` | Validates a repository URL without installing. |
| `list-templates` | `tizen-create-project` | Lists the available project templates. |
| `import-wgt` | `tizen-create-project` | Imports a `.wgt` archive as a Web project. |
| `project-delete` | `tizen-create-project` | Deletes a project directory. |
| `emulator-manager` | `tizen-create-emulator` and `tizen-launch-emulator` | Exposes the full `em-cli` surface, including modify, reset, and image capture. |

Run `tizen-sdk --help` for the full list and `tizen-sdk <command> --help` for the options of one command. The complete mapping is documented in the project repository under `docs/SKILLS_COMMANDS_MAPPING.en.md`.

## Related information
* Dependencies
  - Node.js 20 or higher
  - Tizen SDK 10.0 and higher
* [Tizen SDK Skills](index.md)
* [Using Tizen SDK Skills](usage-scenarios.md)
* [Command Line Interface](../baseline-sdk/common-tools/command-line-interface.md)
* [Smart Development Bridge](../baseline-sdk/common-tools/smart-development-bridge.md)
