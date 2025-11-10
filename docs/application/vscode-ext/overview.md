# Overview Visual Studio Code Extension for Tizen

Visual Studio Code extension for Tizen (""VS Code extension for Tizen"") is a Visual Studio Code extension that enables you to develop Tizen .NET, Web and Native applications easily using Visual Studio Code.

Using VS Code extension for Tizen, you can:

- Create a project from templates.
- Edit code with IntelliSense.
- Build your project and get a Tizen application.
- Deploy your application to the device or emulator and run it.
- Debug your application.

**Figure : Visual Studio Code Views**

![Visual Studio Code Views](./image/overview/vscode-view-overview.png)

### Views of "VSCode Extension for Tizen"

- `Project Explorer` : When you open a workspace with open folder, vscode makes the project structure and you can navigate the file with this view.
- `Run and Debugger` : Tizen Native and .NET Debugger Configuration and provide debugging view

  ※ Web app debugger is provided with individual view (Web-inspector) and triggered by "debug project" on tizen sidebar menu.

- `Tizen sidebar Menu` : When you select the Tizen Activity Bar menu, the Tizen Sidebar provides entry points for managing your development environment and launching key actions.

  - Welcome : Open the Tizen Extension walkthrough page and explore key features.
  - Active Targets
    - Project : Shows the currently active project. Click to view or switch projects.
    - Device : Displays the connected device or emulator. Click to open the Device Manager or change the target.
    - Certificate : Indicates the active signing certificate. Click to open the Certificate Manager or switch profiles.
      > 💡 _Active Targets replaces the old “Tizen Tools” section. Instead of launching tools directly, you can now manage and switch your working targets from one integrated view._
  - Actions
    - Create Project : Create a new app project from templeates (Web, Native, or .NET for the selected platform version)
    - Build Project : Build and sign the active project to generate an installable package
    - Run Project : Build(if needed), install, and launch the active project on a target device or emulator
    - Debug Project : Launch the active project in debugging mode with runtime inspection
  - Report Issue : Open Tizen Github issue page and provide issue reporting templates.

**Figure : Menus of Visual Studio Code Extension for Tizen**

![Tizen VSCode Menu](./image/overview/vscode-menu.png)
