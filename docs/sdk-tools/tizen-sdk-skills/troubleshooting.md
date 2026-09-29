# Troubleshooting Tizen SDK Skills

This page lists messages and situations you may run into with Tizen SDK Skills and how to resolve them. Every failure is reported as a Standard JSON Envelope with an `error_code`, an `error_category`, and usually a `suggested_fix`, so the first step is always to read that object, or to ask your assistant to apply the suggested fix.

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

1. Restart Codex and run `/hooks` to trust the Tizen SDK Skills hooks.
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

## Breakpoints do not bind in a .NET app

**When you see this:** `tizen-dotnet-debug` stops with `build_failed`, or netcoredbg attaches but breakpoints are never hit.

**What it means:** The app was built in Release configuration, which ships no portable PDB files.

**How to resolve:** Ask to "Build the project with the Debug configuration", reinstall the app, and start debugging again.

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
* [Tizen SDK Skills](index.md)
* [Installing Tizen SDK Skills](install.md)
* [Using Tizen SDK Skills](usage-scenarios.md)
