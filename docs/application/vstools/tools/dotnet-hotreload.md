# Tizen .NET Hot Reload

With Hot Reload you can now modify your apps managed source code while the application is being debugged, without the need to stop and restart the debugging.
After starting the debugging of the application on the emulator or real device, you can apply the changed file without stopping the debugging of the application.
With Hot Reload changes are applied only on the second entrance to the function. If the change you made is supported, your app will now be patched while it's running with your new logic. You should see the changes in your app’s behavior the next time the updated code is re-executed by either your action or by a timer triggering the code.

## Prerequisites

Below are the prerequisites for using Tizen .NET Hot Reload in Visual Studio:

- Make sure that Tizen Studio Version 5.1 or above is installed.
- Make sure to set the Tool Path (Tizen SDK) in **Tools > Options > Tizen > Tools** with the installed 5.1 or above Tizen Studio path.

## Enable Tizen .NET Hot Reload

Go to **Tools** menu in Visual Studio, and select **Tools > Options...** from the dropdown menu. **Options** window will open.

**1.** Go to **Tizen &gt; Tools** and check the **Enable Hot Reload** checkbox.

**Figure: Tizen options page to enable .NET Hot Reload**

![Tizen options page to enable .NET Hot Reload](media/enable_tizen_hotreload.png)

**2.** Go to **Debugging &gt; .NET / C++ Hot Reload** and check all the checkboxes.

**Figure: VS options page to enable .NET Hot Reload**

![Tizen options page to enable .NET Hot Reload](media/enable_vs_hotreload.png)


## Supported/Unsupported changes and architecture
Currently, Tizen .NET Hot Reload is supported on aarch64 and armv7l.
No matter how you use .NET Hot Reload please be aware that some changes are not supported at runtime and will prompt you with a rude edit dialog and require you to restart your app in order to apply the changes. [Supported Edits in Tizen .NET Hot Reload](https://github.com/dotnet/roslyn/blob/main/docs/wiki/EnC-Supported-Edits.md){:target="_blank"}


## Examples

### Tizen .NET Hot Reload without breakpoint

The example shown here uses Hot Reload in a Tizen ElmSharp based UI application.
Here, we add a callback method on the button click event and once the application is launched on a target device and it is running in debug mode, we modify the callback method and Save (Ctrl+S) to apply Hot Reload.

The following video demonstrates the example on a Tizen device:


[![Hotreload Example Video](media/hotreload_without_bp.png)](media/Hotreload_Without_Breakpoint.mp4 "Hot Reload example video without breakpoint")


### Tizen .NET Hot Reload with breakpoint

The example shown here uses Hot Reload in a Tizen ElmSharp based UI application.
Here, we add a breakpoint in the main method on a static method call and once the application is launched on a target device and it is running in debug mode, we will modify the method and Save (Ctrl+S) to apply Hot Reload.

The following video demonstrates the example on a Tizen device:

[![Hotreload Example Video](media/hotreload_with_bp.png)](media/Hotreload_With_Breakpoint.mp4 "Hot Reload example video with breakpoint")