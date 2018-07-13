# Live Editing of HTML, CSS, and JavaScript

When you change the source code in the Tizen Studio, the running application is updated instantly without any reloading process.

You can monitor how the changes you have made in a file are rendered in the target window without refreshing the page manually.

<a name="about"></a>
## About Live Editing

Live editing is a special feature, which applies source changes to the running application immediately without building, packaging, and relaunching the application. All changes made in the HTML, CSS, and JavaScript files are automatically and immediately reflected in the running application.

This feature can be used in the [Previewer](previewer.md) view and when running the application in the emulator or the Web simulator.

<a name="prerequisites"></a>
## Configuring Live Editing

Live editing is disabled by default.

To enable live editing in the Tizen Studio:

1. In the menu, go to **Run > Run Configuration > Tizen Web Application > <PROJECT NAME>**.

   Alternatively, right-click the project in the **Project Explorer** view and select **Run As > Run Configuration > Tizen Web Application > <PROJECT NAME>**.

2. Select the **Enable live editing** check box in the run configuration.

If you are running your application for the first time, you must create a new configuration first.

> **Note**  
> The live editing feature has the following limitations:
> - The Tizen Device API does not work on the emulator.
> - Only specific device APIs are supported by the Web simulator.
> - Live editing does not work in certain environments, such as a proxy network.

To define how the live editing works, [set the Tizen Studio Live Editing preferences](ide-preferences.md#live).

## Related Information
- Dependencies
  - Tizen Studio 1.0 and Higher
