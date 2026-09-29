# Using Tizen SDK Skills

This page walks through common Tizen development workflows with Tizen SDK Skills. Each step shows what to type in your AI coding assistant, which skill answers, and what a successful result looks like. You can copy the requests as they are, or phrase them in your own words in English or Korean.

Before you start, install the plugin as described in [Installing Tizen SDK Skills](install.md).

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

   `tizen-sdk-install` runs its pre-check and then starts the installer as a background job. In Claude Code you are notified when it completes. In Cline the install runs in the foreground. The SDK is installed to `~/tizen-sdk` by default and the path is saved in `~/.tizen.sdk.path.config`.

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

   `tizen-create-project` discovers the Web templates in your SDK and scaffolds the project. The `config.xml` file is generated from the template, never written by hand.

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
   Create a native ServiceApp template app named MyApp, then build it in Debug configuration
   ```

3. **Install and start debugging.**

   ```
   Install MyApp on the emulator and debug it with GDB
   ```

   `tizen-gdb-debug` starts the app, finds its process ID, starts `gdbserver` on the device, forwards the port, and attaches the host GDB. It refuses Web and .NET projects because they have no native binary.

## Scenario 4: Develop and debug a .NET app

Goal: a .NET (C# or NUI) app with breakpoints in Visual Studio Code.

1. **Set up .NET.**

   ```
   Set up the .NET environment for Tizen
   ```

   `tizen-dotnet-setup` verifies the .NET SDK and installs the Tizen workload.

2. **Create and build in Debug configuration.**

   ```
   Create a .NET NUI app named MyDotnetApp and build it with the Debug configuration
   ```

   A Debug build is required. Release builds ship no portable PDB files, so breakpoints would never bind.

3. **Install and debug.**

   ```
   Install MyDotnetApp and start .NET debugging
   ```

   `tizen-dotnet-debug` deploys netcoredbg to the device on demand, starts the app, and returns either a command-line attach command or a Debug Adapter Protocol server address. Connect from Visual Studio Code with F5 using the returned configuration.

## Scenario 5: Find the cause of a crash

Goal: understand why an app crashes without reading raw logs yourself.

1. **Start monitoring before you reproduce the problem.**

   ```
   Start monitoring the device logs
   ```

   `tizen-dlog-analyzer` starts collecting the device log in the background.

2. **Reproduce the crash**, then ask for the analysis.

   ```
   The app crashed. Analyze the logs
   ```

   The analyzer detects crashes and exceptions, deduplicates them, and reports the likely root cause with a suggested fix. You can also collect logs for one app only:

   ```
   Collect the logs for org.example.myapp and analyze the errors
   ```

3. **Fix, rebuild, verify.** Apply the fix, ask to rebuild and reinstall, then ask to check the logs again. Stop the monitoring when you are done:

   ```
   Stop log monitoring
   ```

## Scenario 6: Sign an app for a device

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

## Scenario 7: Test a Web app with Playwright

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

## Scenario 8: Use the standalone CLI in a script

Goal: build and install without an AI assistant, for example in CI.

After building the CLI as described in [Installing Tizen SDK Skills](install.md#standalone-tizen-sdk-cli), each command prints one JSON envelope, so you can parse it with a tool such as `jq`:

```
tizen-sdk build-project --project ~/tizen-apps/MyApp > build.json
jq -r '.status' build.json

tizen-sdk device-manager --action start > devices.json
tizen-sdk install-app --package ~/tizen-apps/MyApp/Debug/MyApp.tpk --run
```

Use `tizen-sdk --capabilities` to see which commands can run on the current machine, and `tizen-sdk <command> --help` for the options of a command. SDK installs follow a two-phase pattern: the pre-check returns within seconds, and its `suggested_fix.command` contains the installer command to run in the background. Large builds can take several minutes, and the default script timeout can be extended with the `TIZEN_TOOL_TIMEOUT` environment variable, in milliseconds.

## Tips

- **Be specific about the type.** Say "web app", "native app", or ".NET app" when you create a project, and "app templates" or "emulator templates" when you ask for templates.
- **Long installs.** In Claude Code, SDK and package installs run in the background and you can keep working. In Cline they run in the foreground. In Codex CLI, ask for long operations to run in the background so that they are not cut off by the per-call time limit.
- **Korean works too.** Requests such as "타이젠 SDK 설치해줘" or "웹앱 만들어서 에뮬레이터에 설치해줘" are routed to the same skills.
- **Read the envelope.** When something fails, the error object contains a stable error code, a category such as `device_not_found`, and often a suggested command. You can ask the assistant to apply the suggested fix.
- **Detailed walkthroughs.** The project repository contains longer step-by-step guides for each scenario under `usage/` and `docs/`, including a WSL emulator guide and a Platform GBS build guide.

## Related information
* Dependencies
  - Node.js 20 or higher
  - Tizen SDK 10.0 and higher
* [Tizen SDK Skills](index.md)
* [Tizen SDK Skills reference](skills-reference.md)
* [Troubleshooting Tizen SDK Skills](troubleshooting.md)
* [tizen-agent-skills on GitHub](https://github.com/Samsung/tizen-agent-skills)
