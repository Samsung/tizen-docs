# Tizen SDK Skills

Tizen SDK Skills (`tizen-sdk-skills`) is an open-source automation plugin that lets AI coding assistants operate the Tizen SDK for you. Instead of memorizing `tizen`, `sdb`, and `em-cli` commands, you describe what you want in plain English or Korean. The matching skill then installs the SDK, creates and builds your project, launches an emulator, installs the app, or sets up a remote debugging session.

The plugin works with Claude Code, Cline, Codex CLI, Gemini CLI, and Visual Studio Code. It also ships as a standalone `tizen-sdk` command-line tool that runs the same automation without any AI assistant, which makes it useful in shell scripts and CI pipelines.

Tizen SDK Skills is developed by Samsung and published under the Apache License 2.0 in the [tizen-agent-skills](https://github.com/Samsung/tizen-agent-skills) repository on GitHub. The plugin lives in the `tizen-sdk-skills/` directory of that repository. This section describes version 1.4.0.

> [!NOTE]
> You do not need to install the Tizen SDK before you start. The `tizen-sdk-install` skill downloads and installs it for you. See [Installing Tizen SDK Skills](install.md).

## What you can do with it

Tizen SDK Skills covers the whole application development lifecycle with 29 skills:

- **Set up the environment**: check Node.js and free disk space, install the Tizen SDK from the public CDN or from your own package repository, install platform, emulator, mobile, and TV SDK packages, add custom rootstraps, update packages, and set up the .NET workload.
- **Create and build projects**: scaffold Native, .NET, Web, RPK resource, TV, and Platform projects from the templates in your installed SDK, import an existing `.wgt` archive as a project, and build `.tpk`, `.wgt`, `.rpk`, or `.rpm` packages.
- **Manage emulators and devices**: create emulator images with the screen size you want, launch and stop them, find connected devices, connect a TV over the network instead of USB, and take screenshots.
- **Install and run apps**: install a package on the emulator or device and launch it, push and pull files, and run everyday `sdb` actions such as port forwarding or rebooting.
- **Debug and analyze**: set up remote debugging with GDB for Native apps, netcoredbg for .NET apps, and Remote Web Inspector or Chrome DevTools Protocol (CDP) for Web apps. Collect device logs (dlog) and kernel logs and get an automatic crash and exception analysis. Report a symptom such as high CPU usage or a video that does not play, and the analyzer runs evidence probes, collects logs while you reproduce the problem, and reports the likely root cause.
- **Test**: scaffold and run Playwright tests against a Tizen Web app over CDP.
- **Sign**: generate author certificates, choose distributor certificates, manage signing profiles, and issue Samsung certificates for TV targets.

For the full list, see [Tizen SDK Skills reference](skills-reference.md).

## Supported hosts

You can use Tizen SDK Skills from any of the following environments. The same skills, agents, and guard rules are installed in every host; only the installation location and the file format differ.

| Host | What is installed | Notes |
|------|-------------------|-------|
| Claude Code | Skills, agents, and PreToolUse guard hooks | Long-running installs run in the background, and you are notified when they finish. |
| Cline | Skills, guard hooks, and an always-on rules file | Long-running installs run as a detached process. The assistant checks the status a few times, then hands control back to you. Ask for the install progress to continue. Hooks are not active on Windows; the rules file covers that case. |
| Codex CLI | Skills, agents in TOML format, hooks, and a guard section in `AGENTS.md` | Hooks must be trusted once with the `/hooks` command after installation. |
| Gemini CLI | Skills, agents, a BeforeTool hook adapter, and a guard section in `GEMINI.md` | |
| Visual Studio Code | The Tizen AI Extension installs and synchronizes the plugin for Claude Code, Cline, and Codex CLI from inside the editor | No scripts to run. Uninstalling the extension removes everything it installed. |
| Standalone `tizen-sdk` CLI | A single executable bundle of all 35 commands | No AI assistant needed. Prints machine-readable JSON, so it fits shell scripts and CI. |

Windows, Linux, and macOS are supported. The log analyzer binary used by `tizen-dlog-analyzer` ships for Linux, Windows, and macOS (x86_64). The Tizen emulator can also run inside Windows Subsystem for Linux (WSL2) with some extra configuration, which is described in the project repository.

## How it works

Each skill is a small Markdown definition that tells the AI assistant when to use it and which command to run. The real work is done by Node.js command-line runners that are shared by every host.

1. You type a request such as "Build this project and install it on the emulator".
2. The assistant matches the request to a skill, for example `tizen-build-project` followed by `tizen-install-app`.
3. The skill runs the matching Node.js runner from the plugin cache in your home directory.
4. The runner locates your installed Tizen SDK, executes the underlying `tizen`, `sdb`, or `em-cli` commands, and handles OS-specific details for you.
5. The runner returns one Standard JSON Envelope on standard output. The assistant reads the envelope and reports the result, or applies the suggested fix if something failed.

### The Standard JSON Envelope

Every command returns exactly one JSON object with the same shape. Diagnostic text goes to standard error only, so the envelope is always safe to parse.

A successful response looks like this:

```
{
  "status": "success",
  "result": {
    "sdk_path": "/home/user/tizen-sdk",
    "config_file": "/home/user/.tizen.sdk.path.config"
  },
  "warnings": [],
  "errors": [],
  "command": "tizen-sdk sdk-init",
  "duration_ms": 150
}
```

A failed response carries a stable error code, a category, a human-readable message, and, when possible, a suggested fix that the assistant can run for you:

```
{
  "status": "failure",
  "errors": [
    {
      "error_code": "TIZEN_SDK_DEVICE_E001",
      "error_category": "device_not_found",
      "message": "No connected device or emulator found.",
      "suggested_fix": {
        "command": "tizen-sdk create-emulator --vm-name myEmul --size 1080 --launch",
        "auto_fixable": false
      }
    }
  ],
  "command": "tizen-sdk install-app",
  "duration_ms": 50
}
```

Secrets such as certificate passwords are redacted from the envelope before it is printed.

### Guard rules

The plugin installs a few guard hooks in your AI assistant that keep the generated work consistent with the Tizen SDK:

- Project files such as `tizen-manifest.xml` and `config.xml` are never written by hand. They are always generated from the templates in the installed SDK.
- The assistant does not call the `tizen` CLI or run `sdb` directly. It always goes through the skills, which know where the SDK is installed and return a structured result. This includes diagnostics: kernel logs and CPU or memory measurements are taken by the log analyzer, not by hand-typed `dmesg`, `top`, or `ps` commands over `sdb`.
- Any report of a problem, such as a crash, a freeze, or high CPU usage, is routed to `tizen-dlog-analyzer`, even when the request mentions the emulator or a device.
- Destructive actions, such as deleting a project, clearing device logs, uninstalling a package, or rebooting a device, ask for confirmation first.

## Talk to it in natural language

Once the plugin is installed, describe what you want in your AI coding assistant. English and Korean requests both work:

```
Install the Tizen SDK
Create a Tizen web app called HelloTizen
Build this project and install it on the emulator
Launch the emulator and show me the connected devices
Debug this native app with GDB
The app crashed. Analyze the dlog
The emulator CPU went to 300% and the video does not play. Investigate
타이젠 SDK 설치해줘
웹앱 만들어서 에뮬레이터에 설치해줘
```

Each request is routed to a skill such as `tizen-sdk-install`, `tizen-create-project`, `tizen-build-project`, `tizen-install-app`, `tizen-gdb-debug`, or `tizen-dlog-analyzer`. For step-by-step workflows, see [Using Tizen SDK Skills](usage-scenarios.md).

## In this section

- [Installing Tizen SDK Skills](install.md): prerequisites, setup for each host, the VS Code extension, and the standalone `tizen-sdk` CLI.
- [Tizen SDK Skills reference](skills-reference.md): every skill grouped by task, with example requests.
- [Using Tizen SDK Skills](usage-scenarios.md): end-to-end walkthroughs from a fresh machine to a debugged app.
- [Troubleshooting Tizen SDK Skills](troubleshooting.md): common messages and how to resolve them.

## Related information
* Dependencies
  - Node.js 20 or higher
  - Tizen SDK 10.0 and higher (installed by the plugin if missing)
* [tizen-agent-skills on GitHub](https://github.com/Samsung/tizen-agent-skills)
* [Command Line Interface](../baseline-sdk/common-tools/command-line-interface.md)
* [Smart Development Bridge](../baseline-sdk/common-tools/smart-development-bridge.md)
* [Emulator Manager](../baseline-sdk/common-tools/emulator-manager.md)
