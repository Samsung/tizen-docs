# Troubleshooting Tizen Agent Skills

This page lists messages and situations you may run into with Tizen Agent Skills and how to resolve them. Every failure is reported as a Standard JSON Envelope with an `error_code`, an `error_category`, and usually a `suggested_fix`, so the first step is always to read that object, or to ask your assistant to apply the suggested fix.

## A skill is not picked up

**When you see this:** You ask to "Install the Tizen SDK" and the assistant does not use a `tizen-*` skill, or it tries to run `tizen` commands by hand.

**What it means:** The host has not loaded the skills yet, or the installation is incomplete.

**How to resolve:**

1. Restart the assistant session. Skills are read at startup.
2. Run the setup script for your host again. The setup is idempotent and repairs missing files.
3. Check that a runner is present in the plugin cache:

   ```
   ls ~/.claude/plugins/cache/tizen-platform/tizen-sdk-skills/*/lib/cli/sdk-init-cli.js
   ```

   Replace `.claude` with `.cline`, `.codex`, or `.gemini` for other hosts.

## Node.js is not installed or not on PATH

**When you see this:** An envelope with `error_category` `node_not_found`, or the message "Node.js is not installed or not on PATH".

**What it means:** The runners behind every skill need Node.js 20 or higher.

**How to resolve:** Install Node.js and open a new terminal so the `PATH` change takes effect.

| OS | Command |
|----|---------|
| Windows | `winget install OpenJS.NodeJS.LTS` |
| macOS | `brew install node` |
| Ubuntu and Debian | `sudo apt update && sudo apt install -y nodejs npm` |
| Any OS | Download the LTS installer from [nodejs.org](https://nodejs.org/) |

Then ask the assistant to "check node" to confirm.

## PLUGIN_NOT_BUILT from the standalone CLI

**When you see this:** `node bin/tizen-sdk.js` prints an envelope with the error code `PLUGIN_NOT_BUILT`.

**What it means:** The standalone CLI has not been built yet. The launcher needs `dist/tizen-sdk.js`.

**How to resolve:** Build it from the `tizen-cli` directory and try again:

```
cd tizen-cli
pnpm install && pnpm run build
node bin/tizen-sdk.js --doctor
```

## No connected device or emulator

**When you see this:** An envelope with the error code `TIZEN_SDK_DEVICE_E001` and the category `device_not_found`.

**What it means:** `sdb` sees no device. The emulator is not running, or a physical device is not connected or not authorized.

**How to resolve:**

1. Ask to "Launch the emulator", or "Create and launch an emulator" if you have none.
2. For a physical device, check the USB cable or ask to "Connect to the device at `<ip>`" to use the network.
3. Ask to "Show me the connected devices" to confirm.

## Several devices are connected

**When you see this:** An envelope with the category `multiple_devices`. The `details` list names the online serials, and `suggested_fix.command` repeats the command with a serial.

**What it means:** More than one device or emulator is online and the request did not say which one to use.

**How to resolve:** Name the target in your request, for example "Take a screenshot of emulator-26101", or ask the assistant to run the suggested command. Only online devices are listed.

## Tizen SDK path not found

**When you see this:** A message that the SDK path does not exist, or that `~/.tizen.sdk.path.config` is missing.

**What it means:** The plugin looks for the SDK in `~/tizen-sdk`, in the path stored in `~/.tizen.sdk.path.config`, or in the `TIZEN_SDK_PATH` environment variable. None of them points to an installed SDK.

**How to resolve:**

- If you have no SDK yet, ask to "Install the Tizen SDK".
- If you installed the SDK yourself, ask to "Set the Tizen SDK path to `<path>`". The `tizen-sdk-init` skill validates the path and saves it.

## Not enough disk space

**When you see this:** The SDK install pre-check stops with a disk space error.

**What it means:** Less than 15 GB is free on your home drive.

**How to resolve:** Free up space on the home drive, or install the SDK to another drive and register the path with `tizen-sdk-init`.

## The tizen CLI command was blocked

**When you see this:** The assistant reports that a `tizen` or `sdb` command was denied by a hook.

**What it means:** The guard hooks are working as intended. They stop the assistant from calling the SDK tools directly so that every operation goes through a skill and returns a structured result.

**How to resolve:** Ask for the task in natural language instead, for example "Build this project" rather than asking the assistant to run `tizen build-native`.

## Codex CLI hooks do not run

**When you see this:** The guard rules are not applied in Codex CLI, or `/skills` does not list the Tizen skills.

**What it means:** Codex treats hooks written by a script as untrusted until you approve them, and the hooks feature may be disabled.

**How to resolve:**

1. Restart Codex and run `/hooks` to trust the Tizen Agent Skills hooks.
2. If they still do not run, add the following to `~/.codex/config.toml`:

   ```
   [features]
   hooks = true
   ```

3. Confirm that `/skills` lists the `tizen-*` skills and `/agent` lists the `tizen-*` agents.

## Codex CLI sandbox blocks network or writes

**When you see this:** An envelope with the category `sandbox_blocked`, or an install job that exits immediately without a result.

**What it means:** The default Codex sandbox blocks network sockets and writes outside the workspace. Installers download packages and write to the SDK directory, so they cannot run inside it.

**How to resolve:** Re-run the command with escalated permissions when Codex asks. The envelope's `suggested_fix.command` contains the exact command to run. Long operations such as builds, installs, and emulator launches should be started with `--background` and polled, because Codex limits each tool call to about 30 seconds.

## Cline hooks are inactive on Windows

**When you see this:** The guard hooks do nothing in Cline on Windows.

**What it means:** Cline hooks are supported on macOS and Linux only.

**How to resolve:** No action is needed. The setup installs an always-on rules file under `Documents/Cline/Rules` that applies the same guard rules on Windows.

## The runner is not found in a Cline terminal on Windows

**When you see this:** In Cline on Windows, the assistant reports that it cannot find the runner for a skill, or one of these errors appears:

- `AmpersandNotAllowed` or "The ampersand (&) character is not allowed" in a PowerShell terminal.
- "foreach 뒤에 변수 이름이 없습니다" or "Missing variable name after foreach".
- `MODULE_NOT_FOUND` with a message such as `Cannot find module '<your working directory>\list-templates'`.

**What it means:** Each skill contains a runner lookup for the cmd.exe terminal and another for the PowerShell terminal. The lookup for the wrong shell was used:

- The cmd.exe lookup chains `dir` commands with `&`, which is a reserved character in PowerShell.
- The PowerShell lookup was wrapped in `powershell -Command "..."`. The outer shell expands `$CLI`, `$env:USERPROFILE`, and the other variables first, and the inner shell receives an empty script.
- The `node "$CLI" ...` line was run on its own, without the two lookup lines before it in the same session. `$CLI` is then empty, Windows PowerShell drops the empty argument, and Node.js treats the first command argument as the script path. The module is not missing. The lookup was skipped.

**How to resolve:**

1. Update the plugin to version 1.0.0 or later and run the setup script again. From this version the lookup blocks name the shell they are for, and the PowerShell `node` line stops with the message `$CLI is empty` instead of a misleading module error.
2. In a PowerShell terminal, run all three lines of the PowerShell block in order, in the same session, directly in the terminal.
3. In a cmd.exe terminal, run the `cmd /c dir ...` chain and then `node "<found path>" ...` with the highest version that was listed.
4. If no lookup finds a runner in `~/.claude`, `~/.cline`, `~/.codex`, or `~/.gemini`, the plugin is not installed on this machine. Install it first.

## Breakpoints do not bind in a .NET app

**When you see this:** `tizen-dotnet-debug` stops with `build_failed`, or netcoredbg attaches but breakpoints are never hit.

**What it means:** The app was built in Release configuration, which ships no portable PDB files.

**How to resolve:** Ask to "Build the project with the Debug configuration", reinstall the app, and start debugging again.

## A second F5 in Visual Studio Code ends the .NET session at once

**When you see this:** The first .NET debug session works. After you stop it, the next F5 reports that the session started and then ends immediately.

**What it means:** Stopping a session ends both the app and netcoredbg on the device, while the port forward on the host keeps accepting connections. Nothing is listening behind it anymore.

**How to resolve:** Let `tizen-dotnet-debug` write the Visual Studio Code files by telling it the project directory, for example "Debug MyTizenDotnetApp in this project". It writes a `tasks.json` with a relaunch task and wires it into the `Tizen .NET (netcoredbg)` configuration as `preLaunchTask`, so every F5 relaunches the app first. If you wrote `launch.json` by hand, remove your entry and run the skill again. A `launch.json` that is not strict JSON, for example one with comments or trailing commas, is left alone with a warning.

## The app name is rejected

**When you see this:** Creating a project fails with `invalid_parameters` and a message that the name needs at least 10 letters or digits.

**What it means:** The Tizen package ID is made of the first 10 ASCII letters and digits of the app name. Hyphens, underscores, spaces, and non-ASCII characters do not count, so `MyApp` or `dali-demo` cannot produce a valid ID. A package with a shorter ID would fail to install on the device.

**How to resolve:** Choose a name such as `MyTizenWebApp` or `MyTizenApp01`. The assistant states the rule when it asks for the name and only offers names that pass it.

## A Native project for Tizen 11.0 does not build

**When you see this:** A Native project that was created from the Basic UI template with an earlier plugin version for a `tizen-11.0` profile fails to build, and the build output cannot resolve a consistent rootstrap.

**What it means:** The template copy carried a fixed API version 10.0 in `tizen-manifest.xml`, while the project files named 11.0.

**How to resolve:** Update the plugin and ask to "Show me the app templates". Listing the templates repairs template copies that are still identical to the shipped template. Then create the project again, or set the `api-version` attribute of the `<manifest>` element in your existing project to `11.0`.

## The assistant stops after starting log collection

**When you see this:** After you report a problem, the assistant starts the log collectors and ends its turn with two options, "Done, the symptom occurred" and "Nothing happened", without analyzing anything.

**What it means:** This is the intended flow of `tizen-dlog-analyzer`. The reproduction window is yours. The assistant does not wait on a timer, and the guard hooks deny `sleep` around the analyzer.

**How to resolve:** Reproduce the problem on the device, then answer with one of the two options. The analysis runs in both cases, because silent errors are common.

## Log collection fails with sdk_path_not_set

**When you see this:** A log action such as monitoring, app log collection, or kernel log collection fails with the category `sdk_path_not_set`, although a device is connected.

**What it means:** The log analyzer stores its logs in the SDK data directory, for example `<sdk>-data/dloganalyzer/`, and reads the SDK location from `~/.tizen.sdk.path.config`. The file is missing, empty, or points to a directory that no longer exists. A byte order mark at the start of the file also breaks the path, and the message says so.

**How to resolve:** Ask to "Set the Tizen SDK path to `<path>`", or ask to "Install the Tizen SDK" if you have none. Only the one-shot log dump and log clear work without a configured SDK path.

## Log collection is refused with already_running

**When you see this:** Starting log monitoring or app log collection returns the category `already_running`. The message names a process ID that holds the collector lock and the command that stops it.

**What it means:** The log analyzer runs one device log collector at a time and records the owner in a lock file under the log directory. Another collector is already streaming the same log buffer. It is either a session this assistant started, or a collector from an earlier session that outlived its tracking files.

**How to resolve:** Follow the command in the envelope:

- If system-wide monitoring holds the lock and you asked for app log collection, keep the monitor running. It already captures the app, and the analysis uses its capture.
- If the holder is a session you started, stop it first with "Stop log monitoring" or "Stop collecting the app logs", then start again.
- If the holder is a collector from an earlier session, the envelope tells you to terminate that process after confirming that it is still the analyzer. Terminate it and start again.
- If the envelope reports a stale lock, the process ID has been reused by an unrelated program. Do not terminate that program. The lock file can be removed once no analyzer process is running.

Do not delete the lock file while its holder runs. Two collectors on the same directory corrupt each other's logs.

## The log analyzer warns about UnicodeEncodeError on Windows

**When you see this:** On Windows, an investigation, probe, or error analysis succeeds, but the envelope carries a warning that mentions `UnicodeEncodeError` and a code page such as cp949, and `output_truncated` is `true`.

**What it means:** The analyzer binary writes through the system code page and stopped on a character that the code page cannot represent, after it had already printed the report. The runner keeps the printed output and returns it as a success.

**How to resolve:** Use the output as it is. Retrying with `chcp 65001` or with the `PYTHONUTF8` or `PYTHONIOENCODING` environment variables has no effect, because they do not reach the bundled binary. If the end of the report matters, check the log files in the SDK data directory under `dloganalyzer/`.

## The log analyzer reports No such command

**When you see this:** A symptom investigation fails with a message such as `No such command 'investigate'`, although the plugin is up to date.

**What it means:** Before version 1.0.0 the runner used the first analyzer binary it found in the plugin caches, which could be an older version from an earlier plugin install. From version 1.0.0 the runner always uses the binary that ships with its own plugin version, and falls back to the newest cached version only when that binary is missing.

**How to resolve:** Update the plugin and run the setup script again. You can also remove old version directories under `~/<dot-dir>/plugins/cache/tizen-platform/tizen-sdk-skills/` that you no longer need.

## The emulator disappears after a reboot

**When you see this:** On Windows, you ask to reboot the emulator, the emulator window closes, and `sdb` never sees the emulator again.

**What it means:** A reboot from inside the guest resets the virtual CPU under the Windows Hypervisor Platform, which terminates the emulator process.

**How to resolve:** Ask to "Restart the emulator" instead. `tizen-sdb-helper` hands that request to `tizen-device-manager`, which stops the emulator, and to `tizen-launch-emulator`, which starts it again. If you ask to reboot or shut down a device whose serial belongs to an emulator, the confirmation repeats this warning.

## Cline stops checking an install after a few status checks

**When you see this:** In Cline, the assistant reports that the SDK install continues in the background and ends its turn while the install is still running.

**What it means:** Cline aborts a tool after five identical calls in a row and does not wake the assistant when a background job finishes. The installer therefore runs detached, and the assistant polls at most four times per turn.

**How to resolve:** Wait for the install to finish, which takes 10 to 15 minutes for a full SDK, then ask "Tell me the install progress" or "설치 진행 상태를 알려줘". The assistant runs the status check and continues where it left off. No completion notice arrives on its own.

## .NET setup used a bundled dotnet but did not persist it

**When you see this:** `tizen-dotnet-setup` succeeds with a warning that the .NET SDK bundled inside a Tizen extension was used for this run only.

**What it means:** No .NET SDK was found on `PATH`, in `DOTNET_ROOT`, or in an official install location, so the setup fell back to a dotnet that ships inside a Tizen extension. That copy can move or disappear when the extension updates, so it is not written into your user environment by default.

**How to resolve:** Either install an official .NET SDK and run the setup again, or ask to "Set up .NET for Tizen and persist the environment", which passes `--persist-env`. If the result reports a stale `DOTNET_ROOT`, run the command it suggests to clear it.

## File transfer fails with a path under the Git installation

**When you see this:** In Claude Code on Windows, a push or pull to a device path such as `/opt/usr/apps/x` fails, or the envelope carries a warning that a path starting with `C:/Program Files/Git` was restored.

**What it means:** Claude Code uses Git Bash, which rewrites any argument that starts with a slash into a path under the Git installation before the runner sees it. The runner detects this and restores the device path. The warning is informational.

**How to resolve:** Pass the device path exactly as it is on the device. Do not add a second leading slash and do not set `MSYS_NO_PATHCONV`, which would also break the path to the runner itself. If the error names `EXEPATH`, the Git installation is in an unusual location. In that case run the request from PowerShell instead.

## The emulator does not start in WSL

**When you see this:** The emulator fails to boot inside Windows Subsystem for Linux.

**What it means:** The emulator needs nested virtualization, which WSL2 provides only with extra configuration.

**How to resolve:** Enable nested virtualization in `%USERPROFILE%\.wslconfig`, restart WSL, and follow the WSL emulator guide in the project repository under `docs/wsl/`.

## Report an issue

If the steps above do not help, open an issue in the [tizen-agent-skills](https://github.com/Samsung/tizen-agent-skills/issues) repository. Include the JSON envelope of the failing command, your operating system, the host you use, and the output of `tizen-sdk --doctor` if you use the standalone CLI. Remove any personal information from paths before you post them.

## Related information
* Dependencies
  - Node.js 20 or higher
  - Tizen SDK 10.0 and higher
* [Tizen Agent Skills](index.md)
* [Installing Tizen Agent Skills](install.md)
* [Using Tizen Agent Skills](usage-scenarios.md)
