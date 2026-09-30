# Installing Tizen SDK Skills

This page explains how to install Tizen SDK Skills for each supported host, how to verify that the installation works, and how to update or remove it. Pick the section for the AI coding assistant you use, or install the standalone `tizen-sdk` CLI if you do not use an assistant at all.

## Prerequisites

- **Node.js 20 or higher** on your `PATH`. Every skill is backed by a Node.js runner. Download it from [nodejs.org](https://nodejs.org/) or use your package manager, for example `winget install OpenJS.NodeJS.LTS` on Windows or `brew install node` on macOS.
- **Git** to clone the repository.
- **One supported host**: Claude Code, Cline, Codex CLI, Gemini CLI, or Visual Studio Code. None is needed for the standalone CLI.
- **Git Bash on Windows** if you want the guard hooks. The hooks are shell scripts and need `bash` on `PATH`.
- **pnpm** only if you build the standalone `tizen-sdk` CLI.
- Windows, Linux, or macOS. About 15 GB of free space on your home drive is needed for the Tizen SDK itself.

> [!NOTE]
> The Tizen SDK does not need to be installed first. After the plugin is set up, ask your assistant to "Install the Tizen SDK" and the `tizen-sdk-install` skill takes care of it. If you already have an SDK at a non-default path, ask it to "Set the SDK path to `<path>`" instead. The path is stored in `~/.tizen.sdk.path.config`.

## Get the source

All script-based installs start from a clone of the public repository. The plugin lives in the `tizen-sdk-skills` subdirectory:

```
git clone https://github.com/Samsung/tizen-agent-skills.git
cd tizen-agent-skills/tizen-sdk-skills
```

Every host has a thin wrapper script in its own directory. All wrappers call the same shared setup implementation, so the result is identical across hosts.

## Claude Code

1. Run the setup script from the `tizen-sdk-skills` directory.

   Windows (PowerShell):

   ```
   .\claude\setup\setup.ps1
   ```

   Linux and macOS:

   ```
   bash claude/setup/setup.sh
   ```

2. The script installs the plugin as user-level components:
   - Mirrors skills, agents, runners, and scripts to `~/.claude/plugins/cache/tizen-platform/tizen-sdk-skills/<version>/`.
   - Copies each skill to `~/.claude/skills/tizen-*/` and each agent to `~/.claude/agents/tizen-*.md`.
   - Merges three PreToolUse guard hooks into `~/.claude/settings.json`. If the file cannot be parsed, the script prints the JSON snippet for you to merge by hand.

3. Restart your Claude Code session so that the new skills are loaded.

## Cline

1. Run the setup script from the `tizen-sdk-skills` directory.

   Windows (PowerShell):

   ```
   .\cline\setup\setup.ps1
   ```

   Linux and macOS:

   ```
   bash cline/setup/setup.sh
   ```

2. The script installs the shared runners to `~/.cline/plugins/cache/tizen-platform/tizen-sdk-skills/<version>/`, the skills to `~/.cline/skills/tizen-*/`, a PreToolUse hook adapter under `Documents/Cline/Hooks`, and an always-on rules file under `Documents/Cline/Rules`.

3. Enable Hooks and Subagents once in the Cline settings, on Cline builds that support them. On Windows the hooks are inactive, and the rules file provides the same guard rules.

4. Restart Cline or reload the VS Code window.

> [!NOTE]
> Cline stops a tool after five identical calls in a row and does not wake the assistant when a background job finishes. SDK and package installs therefore run as a detached process. The assistant checks the status up to four times, then tells you that the install continues in the background and ends its turn. No completion notice arrives on its own. When you want to continue, ask "Tell me the install progress" or "설치 진행 상태를 알려줘".

## Codex CLI

1. Run the setup script from the `tizen-sdk-skills` directory.

   Windows (PowerShell):

   ```
   .\codex\setup\setup.ps1
   ```

   Linux and macOS:

   ```
   bash codex/setup/setup.sh
   ```

2. The script installs the cache under `~/.codex`, the skills to `~/.agents/skills/tizen-*/`, the agents as `~/.codex/agents/tizen-*.toml`, the guard hooks in `~/.codex/hooks.json`, and a marker-delimited guard section in `~/.codex/AGENTS.md`.

3. Restart Codex and run `/hooks` to trust the newly written hooks. If they still do not run, enable hooks in `~/.codex/config.toml`:

   ```
   [features]
   hooks = true
   ```

4. Check that `/skills` lists the `tizen-*` skills and `/agent` lists the `tizen-*` agents.

## Gemini CLI

1. Run the setup script from the `tizen-sdk-skills` directory.

   Windows (PowerShell):

   ```
   .\gemini\setup\setup.ps1
   ```

   Linux and macOS:

   ```
   bash gemini/setup/setup.sh
   ```

2. The script installs the cache under `~/.gemini`, the skills to `~/.gemini/skills/tizen-*/`, the agents to `~/.gemini/agents/tizen-*.md`, a BeforeTool hook entry in `~/.gemini/settings.json`, and a guard section in `~/.gemini/GEMINI.md`.

3. Restart Gemini CLI. `/skills list` and `/agents` should show the Tizen entries.

## Visual Studio Code

The **Tizen AI Extension** installs and synchronizes Tizen SDK Skills for Claude Code, Cline, and Codex CLI from inside Visual Studio Code, without running any script.

1. Download `tizen-ai-extension-vX.Y.Z.vsix` from the [Releases](https://github.com/Samsung/tizen-agent-skills/releases) page.

2. Install it:

   ```
   code --install-extension tizen-ai-extension-vX.Y.Z.vsix
   ```

3. The extension installs the plugin automatically on activation. In the default `auto` mode it detects which hosts are present on your machine (`~/.claude`, `~/.cline`, `~/.codex`) and installs only for those. It also merges the Claude Code hooks into `settings.json` for you and backs up your original file once.

The extension adds these commands to the Command Palette:

| Command | Description |
|---------|-------------|
| **Tizen AI: Install / Re-sync** | Re-runs the installation. Safe to run at any time. |
| **Tizen AI: Show Install Status** | Validates the installed files against the bundled version. |
| **Tizen AI: Remove Installed Files** | Removes only the files the extension installed. |
| **Tizen AI: Show Log** | Opens the install and validation log. |

And these settings:

| Setting | Default | Description |
|---------|---------|-------------|
| `tizenAiExtension.targets` | `auto` | Which hosts to install for: `auto`, `claude`, `cline`, `codex`, `both` (Claude Code and Cline), or `all`. |
| `tizenAiExtension.installHooks` | `true` | Whether to install the guard hooks and rules. |
| `tizenAiExtension.autoSyncOnUpdate` | `true` | Re-install automatically when the extension is updated. |

## Standalone tizen-sdk CLI

`tizen-sdk` runs every command of the plugin from a terminal, a shell script, or CI without any AI assistant. It executes the same runners the skills use and prints a single Standard JSON Envelope.

1. Build it from the `tizen-cli` directory of the clone:

   ```
   cd tizen-cli
   pnpm install && pnpm run build
   ```

   The build produces `dist/tizen-sdk.js` and the launcher `bin/tizen-sdk.js`.

2. Try it:

   ```
   node bin/tizen-sdk.js --doctor           # SDK path, cache, and runner status
   node bin/tizen-sdk.js --capabilities     # which commands are usable right now
   node bin/tizen-sdk.js --help             # list every command
   node bin/tizen-sdk.js check-node
   node bin/tizen-sdk.js build-project --project ~/tizen-apps/MyTizenWebApp
   ```

   `--help`, `--version`, and `<command> --help` also answer with a JSON envelope. The text is carried in `result.help_text`.

3. Optionally put `tizen-sdk` on your `PATH`:

   ```
   pnpm add -g .
   tizen-sdk --doctor
   ```

If you run the launcher before building, it prints a `PLUGIN_NOT_BUILT` envelope that contains the build command. Prebuilt bundles are also attached to each GitHub release as `tizen-sdk-vX.Y.Z.zip`.

> [!NOTE]
> When you run the Node.js launcher, the installer commands (`sdk-install`, `platform-install`, `tv-sdk-install`, `update-package`, and the other package installers) return the installer command in `suggested_fix.command` instead of running it, so that you can start it in the background. Set the environment variable `TIZEN_SDK_INLINE_INSTALLER=1` to have them run the installer inline. The prebuilt bundle attached to a release always runs the installer inline.

## Verify the installation

- In your assistant, ask **"Check whether Node.js is installed"**. The `tizen-check-node` skill should answer with the detected version and path.
- Check that a runner is present in the plugin cache. The path is the same for every host, only the dot-directory differs:

  ```
  ls ~/.claude/plugins/cache/tizen-platform/tizen-sdk-skills/*/lib/cli/sdk-init-cli.js
  ```

- For the standalone CLI, run `tizen-sdk --doctor`.

## Update or remove

The setup is idempotent. To update, pull the latest repository and run the same setup script again. The cache is replaced with a clean mirror, personal skill folders are replaced per skill, and the guard section in `AGENTS.md` or `GEMINI.md` is replaced in place without touching the rest of the file.

To remove a script-based installation, delete the following and then remove the plugin's hook entries from `settings.json` or `hooks.json` and its section from `AGENTS.md` or `GEMINI.md`:

```
rm -rf ~/<dot-dir>/plugins/cache/tizen-platform/tizen-sdk-skills
rm -rf <skills-dir>/tizen-*
rm -f  <agents-dir>/tizen-*.md <agents-dir>/tizen-*.toml
rm -rf ~/<dot-dir>/hooks/tizen-sdk-skills
```

Replace `<dot-dir>`, `<skills-dir>`, and `<agents-dir>` with the paths listed for your host above. If you installed through the Tizen AI Extension, uninstalling the extension removes everything it installed and leaves your own skills and agents untouched.

## Related information
* Dependencies
  - Node.js 20 or higher
  - Tizen SDK 10.0 and higher (installed by the plugin if missing)
* [Tizen SDK Skills](index.md)
* [Tizen SDK Skills reference](skills-reference.md)
* [Installing the Tizen SDK](../baseline-sdk/setup/install-sdk.md)
