# Tizen Agent Skills

Tizen Agent Skills (`tizen-agent-skills`) is Samsung's open-source collection of agent skills and plugins that bring the Tizen platform development environment to AI coding assistants. Instead of memorizing `tizen`, `sdb`, and `em-cli` commands, you describe what you want in plain English or Korean. The matching skill then installs the SDK, creates and builds your project, launches an emulator, installs the app, or sets up a remote debugging session.

The collection works with Claude Code, Cline, Codex CLI, Gemini CLI, and Visual Studio Code. The `tizen-sdk-skills` plugin also ships as a standalone `tizen-sdk` command-line tool that runs the same automation without any AI assistant, which makes it useful in shell scripts and CI pipelines.

Tizen Agent Skills is developed by Samsung and published under the Apache License 2.0 in the [tizen-agent-skills](https://github.com/Samsung/tizen-agent-skills) repository on GitHub. This section describes version 1.1.1, the third release of the collection as a whole. Each plugin in the repository is versioned independently and has its own README and changelog.

## Plugins in this collection

The `tizen-agent-skills` repository contains one directory per plugin. Each plugin covers one area of Tizen development and can be installed on its own.

| Plugin | What it does | Hosts |
|--------|--------------|-------|
| [`tizen-sdk-skills`](https://github.com/Samsung/tizen-agent-skills/blob/main/tizen-sdk-skills/README.md) | Automates the Tizen SDK end to end: SDK install, project creation and build, emulator and device management, app installation, remote debugging (GDB / netcoredbg / CDP), certificates, dlog analysis, and Playwright testing. 29 skills, 24 agents, a standalone `tizen-sdk` CLI, and the Tizen AI Extension for VS Code. | Claude Code, Cline, Codex CLI, VS Code, standalone CLI |
| [`tizen-action-skills`](https://github.com/Samsung/tizen-agent-skills/blob/main/tizen-action-skills/README.md) | Builds Tizen Action Framework providers: picks a default Action category or authors custom `.action`/`.entity` schemas, generates `actionc`/TIDL stubs for C#, C++, JavaScript or Flutter-Tizen/Dart, registers provider metadata, and verifies with `action-tool`. 1 skill. | Claude Code |

The rest of this section focuses on the `tizen-sdk-skills` plugin, which covers the application development lifecycle. For the `tizen-action-skills` plugin, see its [README on GitHub](https://github.com/Samsung/tizen-agent-skills/blob/main/tizen-action-skills/README.md).

> [!NOTE]
> You do not need to install the Tizen SDK before you start. The `tizen-sdk-install` skill downloads and installs it for you. See [Installing Tizen Agent Skills](install.md).

## What you can do with it

The `tizen-sdk-skills` plugin covers the whole application development lifecycle with 29 skills:

- **Set up the environment**: check Node.js and free disk space, install the Tizen SDK from the public CDN or from your own package repository, install platform, emulator, mobile, and TV SDK packages, add custom rootstraps, update packages, and set up the .NET workload.
- **Create and build projects**: scaffold Native, .NET, Web, RPK resource, TV, and Platform projects from the templates in your installed SDK, import an existing `.wgt` archive as a project, and build `.tpk`, `.wgt`, `.rpk`, or `.rpm` packages.
- **Manage emulators and devices**: create emulator images with the screen size you want, launch and stop them, find connected devices, connect a TV over the network instead of USB, and take screenshots.
- **Install and run apps**: install a package on the emulator or device and launch it, push and pull files, and run everyday `sdb` actions such as port forwarding or rebooting.
- **Debug and analyze**: set up remote debugging with GDB for Native apps, netcoredbg for .NET apps, and Remote Web Inspector or Chrome DevTools Protocol (CDP) for Web apps. Collect device logs (dlog) and kernel logs and get an automatic crash and exception analysis. Report a symptom such as high CPU usage or a video that does not play, and the analyzer runs evidence probes, collects logs while you reproduce the problem, and reports the likely root cause.
- **Test**: scaffold and run Playwright tests against a Tizen Web app over CDP.
- **Sign**: generate author certificates, choose distributor certificates, manage signing profiles, and issue Samsung certificates for TV targets.

For the full list, see [Tizen Agent Skills reference](skills-reference.md).

## Supported hosts

You can use Tizen Agent Skills from any of the following environments. The same skills, agents, and guard rules are installed in every host; only the installation location and the file format differ.

| Host | What is installed | Notes |
|------|-------------------|-------|
| Claude Code | Skills, agents, and PreToolUse guard hooks | Long-running installs run in the background, and you are notified when they finish. |
| Cline | Skills, guard hooks, and an always-on rules file | Long-running installs run as a detached process. The assistant checks the status a few times, then hands control back to you. Ask for the install progress to continue. Hooks are not active on Windows; the rules file covers that case. On Windows, each skill carries a separate runner lookup for the cmd.exe and PowerShell terminals. |
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

Each request is routed to a skill such as `tizen-sdk-install`, `tizen-create-project`, `tizen-build-project`, `tizen-install-app`, `tizen-gdb-debug`, or `tizen-dlog-analyzer`. For step-by-step workflows, see [Using Tizen Agent Skills](usage-scenarios.md).

## Release history

This section documents what changed in each release of the `tizen-agent-skills` collection. Each plugin in the repository is versioned independently; for the full plugin changelogs, see [tizen-sdk-skills](https://github.com/Samsung/tizen-agent-skills/blob/main/tizen-sdk-skills/CHANGELOG.md) and [tizen-action-skills](https://github.com/Samsung/tizen-agent-skills/blob/main/tizen-action-skills/CHANGELOG.md) on GitHub.

### v1.1.1 (2026-10-18)

The third unified release. It ships `tizen-sdk-skills` 1.4.4 and `tizen-action-skills` 1.0.0. No new skills were added; the release adds features to existing skills and fixes routing and emulator issues.

#### tizen-sdk-skills plugin
- Plugin version bumped from 1.4.3 to 1.4.4.
- Tizen AI Extension (vsix) 1.4.4 and the standalone CLI bundle `tizen-sdk-v1.4.4.zip` released alongside.

#### tizen-dlog-analyzer
- The runner now exposes the feature set of the bundled v0.2.8a0 analyzer binary. The binary itself is unchanged from v1.1.0.
- New `rules` action: `rules list`, `rules show <id>`, `rules validate [path]`, and `rules test <fixture.json>` inspect the 24 built-in analysis rules read-only. `--rules-dir <path>` loads additional user rule YAML files.
- `investigate` accepts the v0.2.8a0 options (`--rules-dir`, `--parallel`, `--max-workers`, `--deduplicate`, `--similarity-threshold`, `--allow-heavy`, `--no-noise-filter`, `--fuzzy-symptoms`, `--symptom-map`). Its result now includes ranked `conclusions` (confidence, role, evidence, and fix), `ruled_out`, `unexplained`, `consent_needed`, and `redaction_summary`.
- `probe run` accepts `--app-id` to scope probes to one app and `--allow-network-probe` to run network probes only with your consent.
- Existing capture files can be analyzed offline in file mode.
- The analysis report template adds `Confidence` and `Role` fields to each root cause, plus `Ruled Out` and `Unexplained Anomalies` sections.
- A new guard rule denies hand-typed `openssl s_client`, `curl`, or `wget` over `sdb shell` and points to the consent-gated `--allow-network-probe` options instead.

#### Emulator management
- A request such as "list the available emulators" is now routed to `tizen-create-emulator`, which runs `list-vm --detail`, instead of the assistant searching for VMs by hand. A new guard rule denies running `em-cli` directly and listing the emulator VM directory with `ls`, `find`, or `Get-ChildItem`.
- `list-vm --detail` reports each VM's `profile`, derived from its platform image name (`tizen-*` is `tizen`, `tv-*` is `tv`), so a `tizen-10.0-x86_64` VM is no longer reported as a Mobile emulator.
- When no VM name is given, `tizen-launch-emulator` compares platform versions segment by segment and filters by profile, so `10.0` is chosen over `9.0` and a `tizen` request never picks a TV image.
- The emulator home-screen recovery for WSL also covers headless Linux hosts.

#### Runner lookup
- Every CLI runner lookup section in SKILL.md now notes that the `node` line must be run as is.

#### Test runner
- The plugin's test runner always runs the locally built `tizen-sdk` launcher instead of looking up globally installed `tizen-cli` or `tizen-sdk` binaries on `PATH`, which could pick a stale install.

### v1.1.0 (2026-10-14)

The second unified release. It ships `tizen-sdk-skills` 1.4.3 and `tizen-action-skills` 1.0.0. No new skills were added; the release is a patch and improvement update.

#### tizen-sdk-skills plugin
- Plugin version bumped from 1.4.2 to 1.4.3.
- Tizen AI Extension (vsix) 1.4.3 released alongside.

#### tizen-dlog-analyzer
- Bundled analyzer binary updated to v0.2.8a0 (Linux / Windows / macOS).

#### PowerShell runner lookup improvement
- Added a `FullName` secondary sort key to the PowerShell runner lookup block in every SKILL.md: mitigates the case where wrapping the lookup in `powershell -Command "..."` causes the outer shell to expand `$_` to an empty string, which defeats the `[version]` sort.
- The fallback is correct for same-digit versions (1.4.0 vs 1.4.2) but may pick the lower version for different digit counts (1.4.2 vs 1.4.10), so wrapping the lookup in `powershell -Command` is still not recommended.
- The guard rules now document this limitation.

#### Repository documentation
- Added a repository-level `AGENTS.md` for AI coding agents: covers plugin structure, versioning model, documentation conventions, security, commit/PR style, and per-plugin validation commands.

### v1.0.0 (2026-10-07)

The first unified release of the `tizen-agent-skills` collection. It ships `tizen-sdk-skills` 1.4.2 and `tizen-action-skills` 1.0.0. No new skills were added; the release is a patch update.

#### tizen-dlog-analyzer
- Bundled analyzer binary updated to v0.2.5a0 (Linux / Windows / macOS).
- Collector lock (`_meta/collector.lock`) handling fixed: when another collector held the lock, `start` reported success and then deleted the lock file. It now returns `already_running` with the owning PID and a stop command. The runner never touches the lock file.
- When a previous session's collector held the lock, the PID's executable name is checked so that only a `tizen-dlog-analyzer` process is targeted for shutdown; a reused PID is reported as a stale lock.
- The runner now prefers the binary that ships with its own plugin version and falls back to the newest cached version only when that binary is missing. Previously it used the first binary found, which could be an older version from an earlier plugin install.
- On Windows cp949 code page, if `UnicodeEncodeError` truncates the report, the printed report is returned as `success` + warning + `output_truncated: true` instead of returning only the traceback.

#### Cline on Windows (PowerShell terminal)
- SKILL.md runner lookup block titles now name the shell they are for (the cmd.exe chain is cmd.exe-only; the PowerShell block is run directly in the terminal).
- Added an `$CLI is empty` guard to the PowerShell `node "$CLI" …` line, preventing a misleading `MODULE_NOT_FOUND` such as `Cannot find module '<cwd>\list-templates'` when the line is run on its own.
- The guard rules (Korean 7/9, English 8/10) now document both failure modes and restrict the encoding wrapper to commands without `$` variables.

#### Setup scripts
- `setup.ps1` now accepts the `setup.sh` spelling of the options (`--harness … --repo … --skip-validation --no-restart`).

## In this section

- [Installing Tizen Agent Skills](install.md): prerequisites, setup for each host, the VS Code extension, and the standalone `tizen-sdk` CLI.
- [Tizen Agent Skills reference](skills-reference.md): every skill grouped by task, with example requests.
- [Using Tizen Agent Skills](usage-scenarios.md): end-to-end walkthroughs from a fresh machine to a debugged app.
- [Troubleshooting Tizen Agent Skills](troubleshooting.md): common messages and how to resolve them.
- [Tizen Agent Skills 요약 (한국어)](tizen-agent-skills-summary-ko.md): Korean-language summary of Tizen Agent Skills.

## Related information
* Dependencies
  - Node.js 20 or higher
  - Tizen SDK 10.0 and higher (installed by the plugin if missing)
* [tizen-agent-skills on GitHub](https://github.com/Samsung/tizen-agent-skills)
* [tizen-sdk-skills plugin README](https://github.com/Samsung/tizen-agent-skills/blob/main/tizen-sdk-skills/README.md)
* [tizen-action-skills plugin README](https://github.com/Samsung/tizen-agent-skills/blob/main/tizen-action-skills/README.md)
* [Command Line Interface](../../../baseline-sdk/common-tools/command-line-interface.md)
* [Smart Development Bridge](../../../baseline-sdk/common-tools/smart-development-bridge.md)
* [Emulator Manager](../../../baseline-sdk/common-tools/emulator-manager.md)
