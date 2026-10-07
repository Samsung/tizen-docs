# Using Tizen Agent Skills

This page walks through common Tizen development workflows with Tizen Agent Skills. Each step shows what to type in your AI coding assistant, which skill answers, and what a successful result looks like. You can copy the requests as they are, or phrase them in your own words in English or Korean.

Before you start, install the plugin as described in [Installing Tizen Agent Skills](install.md).

## Scenario 1: Set up a fresh machine

Goal: go from a machine without any Tizen tools to a running emulator.

1. **Check the prerequisites.**

   ```
   Check whether Node.js is installed and whether I have enough disk space for the Tizen SDK
   ```

   `tizen-check-node` reports the Node.js version and `tizen-check-disk-space` confirms that at least 15 GB is free on your home drive.

2. **Install the SDK.**

   ```
   Install the Tizen SDK
   ```

   `tizen-sdk-install` runs its pre-check and then starts the installer as a background job. In Claude Code you are notified when it completes. In Cline the installer runs as a detached process. The assistant checks its status a few times and then hands control back to you. Ask "Tell me the install progress" when you want to continue. The SDK is installed to `~/tizen-sdk` by default and the path is saved in `~/.tizen.sdk.path.config`. The download mirror is chosen from your time zone. Hosts in Korea and Japan use `download.tizen.org`.

3. **Install the emulator package.**

   ```
   Download the emulator package
   ```

   `tizen-download-emulator-package` installs the `TIZEN-<version>-Emulator` package from the same repository the SDK came from.

4. **Create and launch an emulator.**

   ```
   Create a 1080 emulator called MyEmul and launch it
   ```

   `tizen-create-emulator` creates the image and `tizen-launch-emulator` boots it and waits until `sdb` sees it. A cold boot can take a few minutes.

5. **Confirm the connection.**

   ```
   Show me the connected devices
   ```

   `tizen-device-manager` lists the emulator with its serial number.

## Scenario 2: Create, build, and run a Web app

Goal: a working Web app on the emulator.

1. **Create the project.**

   ```
   Create a Tizen web app called HelloTizen from the Basic UI template
   ```

   `tizen-create-project` discovers the Web templates in your SDK and scaffolds the project. The `config.xml` file is generated from the template, never written by hand. The name needs at least 10 ASCII letters or digits, because the package ID is built from them. `HelloTizen` has exactly 10.

2. **Build it.**

   ```
   Build the HelloTizen project
   ```

   `tizen-build-project` detects a Web project and packages a `.wgt` file.

3. **Install and run it.**

   ```
   Install the app on the emulator and run it
   ```

   `tizen-install-app` installs the `.wgt` file and launches the app. Ask for a screenshot if you want to see the result without switching windows:

   ```
   Take a screenshot of the emulator
   ```

## Scenario 3: Debug a Native app with GDB

Goal: attach GDB to a Native (C/C++) app running on the emulator.

1. **Install the platform package**, which Native builds need.

   ```
   Install the Tizen platform package
   ```

2. **Create and build the app.**

   ```
   Create a native ServiceApp template app named MyTizenNativeApp, then build it in Debug configuration
   ```

3. **Install and start debugging.**

   ```
   Install MyTizenNativeApp on the emulator and debug it with GDB
   ```

   `tizen-gdb-debug` starts the app, finds its process ID, starts `gdbserver` on the device, forwards the port, and attaches the host GDB. It refuses Web and .NET projects because they have no native binary.

## Scenario 4: Develop and debug a .NET app

Goal: a .NET (C# or NUI) app with breakpoints in Visual Studio Code.

1. **Set up .NET.**

   ```
   Set up the .NET environment for Tizen
   ```

   `tizen-dotnet-setup` looks for a .NET SDK on `PATH`, in `DOTNET_ROOT`, and in the official install locations, installs one in user scope if none exists, and installs the Tizen workload. If you want a specific SDK, say so, for example "Use the dotnet in Program Files". A dotnet that ships inside a Tizen extension is used for this run only and is not written into your environment unless you ask for it.

2. **Create and build in Debug configuration.**

   ```
   Create a .NET NUI app named MyTizenDotnetApp and build it with the Debug configuration
   ```

   A Debug build is required. Release builds ship no portable PDB files, so breakpoints would never bind.

3. **Install and debug.**

   ```
   Install MyTizenDotnetApp and start .NET debugging
   ```

   `tizen-dotnet-debug` deploys netcoredbg to the device on demand, starts the app suspended before `Main()`, and returns a Debug Adapter Protocol server address. When the project directory is known, it also writes `.vscode/launch.json` with a configuration named `Tizen .NET (netcoredbg)` and a `tasks.json` that relaunches the app before each session. Open the project in Visual Studio Code, pick that configuration, set a breakpoint, and press F5. The app shows no window until you do. Stopping the session ends the app and the debugger on the device. The next F5 relaunches them through the task, so you do not have to run the skill again.

## Scenario 5: Find the cause of a crash

Goal: understand why an app crashes without reading raw logs yourself.

1. **Start monitoring before you reproduce the problem.**

   ```
   Start monitoring the device logs
   ```

   `tizen-dlog-analyzer` starts collecting the device log in the background and hands control back to you.

2. **Reproduce the crash**, then ask for the analysis.

   ```
   The app crashed. Analyze the logs
   ```

   The analyzer detects crashes and exceptions, deduplicates them, and reports the likely root cause with a suggested fix. The report is rendered in English and Korean. You can also collect logs for one app only:

   ```
   Collect the logs for org.example.myapp and analyze the errors
   ```

3. **Fix, rebuild, verify.** Apply the fix, ask to rebuild and reinstall, then ask to check the logs again. Stop the monitoring when you are done:

   ```
   Stop log monitoring
   ```

   Stopping keeps the analysis that was captured during the session, so you can still ask to check the results afterwards.

## Scenario 6: Investigate a symptom such as high CPU usage

Goal: find out why the emulator or an app misbehaves when nothing crashes.

1. **Describe the symptom in your own words.** Name the app if you know it.

   ```
   While playing a video in org.example.player on the emulator, the host CPU went to 300% and the video does not play. Investigate
   ```

   The request goes to `tizen-dlog-analyzer`, not to the device manager, even though it mentions the emulator. The analyzer detects the device on its own.

2. **First pass and collectors.** The analyzer runs a one-shot investigation that matches your words to probe bundles for CPU, memory, freezes, media, and graphics, and summarizes what it found. It then starts the system-wide log monitor, the kernel log collector, and the app-scoped log collector, and asks you to reproduce the problem. It does not wait on a timer. The reproduction window is yours.

3. **Reproduce the problem**, then answer with one of the two options it offers:

   ```
   Done, the symptom occurred
   ```

   or "Nothing happened". Silent errors are common, so the analysis runs in both cases.

4. **Read the report.** The analyzer stops the collectors and analyzes the app errors first, the crash detections second, and the kernel findings third. It widens to the full app log or to a single probe only when the symptom is still unexplained. The report follows the same bilingual template as a crash analysis and ends with a choice: keep monitoring, apply the suggested fix and retest, or stop and clean up.

You can also ask for one piece of evidence on its own, for example "Show me the kernel log" or "List the available probes". Kernel logs and CPU or memory measurements always go through the analyzer. The guard hooks deny hand-typed `dmesg`, `top`, or `ps` commands over `sdb`.

## Scenario 7: Sign an app for a device

Goal: a signing profile that is used by later builds.

1. **Create a local author certificate and a profile.**

   ```
   Create a signing profile called dev with a new author certificate
   ```

   `tizen-certificate-manager` generates the author certificate, selects a bundled distributor certificate, creates the profile, and sets it active. Later builds sign with this profile.

2. **For a Samsung TV**, ask for a Samsung certificate instead. This requires a Samsung Account and a connected TV or TV emulator so that the device unique ID can be read:

   ```
   Create a Samsung certificate profile for my TV
   ```

## Scenario 8: Test a Web app with Playwright

Goal: an automated UI test against a Tizen Web app.

1. **Scaffold a test.**

   ```
   Scaffold a Playwright test for HelloTizen in ~/tizen-playwright-test
   ```

   `tizen-playwright-test` creates a test file that connects over the Chrome DevTools Protocol.

2. **Install Playwright in the test project**, not in the plugin:

   ```
   cd ~/tizen-playwright-test && npm install playwright
   ```

3. **Run the test.**

   ```
   Run the Playwright test against HelloTizen on the emulator
   ```

   The skill launches the app in debug mode, forwards the Remote Web Inspector port, runs the test with Node.js, and reports pass or fail in the envelope.

## Scenario 9: Use the standalone CLI in a script

Goal: build and install without an AI assistant, for example in CI.

After building the CLI as described in [Installing Tizen Agent Skills](install.md#standalone-tizen-sdk-cli), each command prints one JSON envelope, so you can parse it with a tool such as `jq`:

```
tizen-sdk build-project --project ~/tizen-apps/MyTizenNativeApp > build.json
jq -r '.status' build.json

tizen-sdk device-manager --action start > devices.json
tizen-sdk install-app --package ~/tizen-apps/MyTizenNativeApp/Debug/MyTizenNativeApp.tpk --run
```

Use `tizen-sdk --capabilities` to see which commands can run on the current machine, and `tizen-sdk <command> --help` for the options of a command. Help output is also a JSON envelope, with the text in `result.help_text`. SDK installs follow a two-phase pattern: the pre-check returns within seconds, and its `suggested_fix.command` contains the installer command to run in the background. Set `TIZEN_SDK_INLINE_INSTALLER=1` if you prefer the installer commands to run inline under Node.js. Large builds can take several minutes, and the default script timeout can be extended with the `TIZEN_TOOL_TIMEOUT` environment variable, in milliseconds.

## Tips

- **Be specific about the type.** Say "web app", "native app", or ".NET app" when you create a project, and "app templates" or "emulator templates" when you ask for templates.
- **Pick a long enough app name.** The name needs at least 10 ASCII letters or digits. Names such as `MyApp` or `TestApp` are rejected before anything is created.
- **Long installs.** In Claude Code, SDK and package installs run in the background and you can keep working. In Cline they run as a detached process, the assistant checks the status up to four times, and then hands control back to you. Ask for the install progress to continue. In Codex CLI, ask for long operations to run in the background so that they are not cut off by the per-call time limit.
- **Restart the emulator the safe way.** Ask to "restart the emulator". The emulator is stopped and started again instead of being rebooted from inside, which terminates the emulator on Windows.
- **Korean works too.** Requests such as "타이젠 SDK 설치해줘" or "웹앱 만들어서 에뮬레이터에 설치해줘" are routed to the same skills.
- **Read the envelope.** When something fails, the error object contains a stable error code, a category such as `device_not_found`, and often a suggested command. You can ask the assistant to apply the suggested fix.
- **Detailed walkthroughs.** The project repository contains longer step-by-step guides for each scenario under `usage/` and `docs/`, including a WSL emulator guide and a Platform GBS build guide.

## Related information
* Dependencies
  - Node.js 20 or higher
  - Tizen SDK 10.0 and higher
* [Tizen Agent Skills](index.md)
* [Tizen Agent Skills reference](skills-reference.md)
* [Troubleshooting Tizen Agent Skills](troubleshooting.md)
* [tizen-agent-skills on GitHub](https://github.com/Samsung/tizen-agent-skills)
